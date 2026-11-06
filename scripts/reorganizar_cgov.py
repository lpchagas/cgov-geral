#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reorganizar_cgov.py — Fase 4 do plano de implantação do Escritório Virtual da CGOV.

Reorganiza a pasta operacional CGOV (Google Drive) na estrutura da Seção 5.2 do
plano, a partir de um mapa CSV arquivo a arquivo, revisado pelo Coordenador.

Modos (exatamente um por execução):

  --planejar               Somente leitura. Percorre a pasta CGOV, calcula o SHA-256
                           de cada arquivo, aplica as regras das Seções 5.5 e 5.6 e
                           grava o mapa CSV (e um resumo .md ao lado). Não move nada.
  --simular [--lote X]     Somente leitura. Confere o mapa contra o disco: origens
                           existentes, destinos livres, nomes repetidos (inclusive só
                           por maiúsculas/minúsculas), caminhos longos no Windows e
                           linhas "a-decidir". Não move nada.
  --executar --lote X      Executa um lote (a–g). Recusa se houver "a-decidir" ou
                           conflito no lote. Pede confirmação digitada. Nunca exclui
                           nem sobrescreve: só cria pastas e move (os.rename).
                           Cada operação é gravada num registro (journal) CSV.
  --reverter --lote X      Desfaz um lote a partir dos registros de execução,
                           conferindo o hash antes de cada movimentação de volta.
  --limpar-vazias          Depois do lote g (D29): nas áreas antigas (AREAS_ANTIGAS),
                           confere que não resta NENHUM arquivo e remove só pastas
                           vazias, da mais funda para a mais rasa (os.rmdir, que
                           falha se a pasta tiver conteúdo). Pede confirmação e
                           grava um registro. Nunca remove arquivos. v1.2.1: tenta
                           de novo (bloqueio do Drive / somente leitura) e segue
                           para as demais pastas; pode ser repetido.

Lotes (etapa 4.5 do plano):
  a  estrutura de pastas            e  04_colegiados, 05_projetos, 06_gestao-da-coordenacao
  b  03_normativos                  f  90_escritorio-virtual, 99_arquivo e destinos fora da CGOV
  c  02_notas-tecnicas              g  quarentena (99_arquivo/_a-excluir_<data>)
  d  01_processos

Ações no mapa: criar (pasta) · mover · renomear · quarentena · a-decidir.
O mapa usa ";" como separador e UTF-8 com BOM (abre direto no Excel).
Os caminhos do mapa são relativos à raiz da pasta CGOV e usam "/".

Raiz da pasta CGOV: --raiz <caminho>, ou a variável CGOV_RAIZ (ambiente ou .env
do repositório). Sem caminhos pessoais neste arquivo (regra de sanitização).

Exemplos (PowerShell, a partir da raiz do repositório):
  python scripts\\reorganizar_cgov.py --planejar --raiz "<pasta CGOV>"
  python scripts\\reorganizar_cgov.py --simular  --raiz "<pasta CGOV>"
  python scripts\\reorganizar_cgov.py --executar --lote b --raiz "<pasta CGOV>"
  python scripts\\reorganizar_cgov.py --reverter --lote b --raiz "<pasta CGOV>"

Referências: plano de implantação v3.6, Seções 5.2, 5.4, 5.5, 5.6 e Fase 4;
ADR-012 (estrutura), ADR-014 (exclusão controlada); decisões D10, D11, D14, D15, D16
e D26 (destinos encurtados em 99_arquivo, v1.1.0) e D29 (--limpar-vazias, v1.2.0).
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import os
import re
import stat
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

VERSAO = "1.2.1"

# --------------------------------------------------------------------------- #
# Constantes
# --------------------------------------------------------------------------- #

REPO = Path(__file__).resolve().parent.parent
MAPA_PADRAO = REPO / "local" / "MAPA_REORGANIZACAO_2026-11.csv"
PASTA_TRABALHO = REPO / "local" / "reorganizacao"          # cache e registros
CACHE_PADRAO = PASTA_TRABALHO / "cache_sha256.csv"
DECISOES_PADRAO = PASTA_TRABALHO / "decisoes.csv"     # etapa 4.2: origem;acao;destino;motivo
APELIDOS_PADRAO = PASTA_TRABALHO / "apelidos.csv"     # etapa 4.2: processo;apelido
REGISTROS = PASTA_TRABALHO / "registros"

COLUNAS = ["id", "lote", "tipo", "area_origem", "origem", "destino",
           "acao", "sha256", "bytes", "motivo"]
DELIM = ";"
ACOES = ("criar", "mover", "renomear", "quarentena", "a-decidir")
LOTES = {
    "a": "estrutura de pastas",
    "b": "03_normativos",
    "c": "02_notas-tecnicas",
    "d": "01_processos",
    "e": "04_colegiados, 05_projetos e 06_gestao-da-coordenacao",
    "f": "90_escritorio-virtual, 99_arquivo e destinos fora da pasta CGOV",
    "g": "quarentena (99_arquivo/_a-excluir_<data>)",
}
LIMITE_CAMINHO_WINDOWS = 259   # MAX_PATH - 1 (sem suporte a caminhos longos)

# Etapa 4.4a / D26: subárvores de 99_arquivo cujos destinos passariam de 259
# caracteres no Windows. O prefixo é trocado na subárvore inteira (não só nos
# arquivos longos), para os arquivos de uma mesma pasta continuarem juntos. Os
# nomes dos arquivos não mudam. "{q}" = pasta de quarentena (_a-excluir_<data>).
ENCURTAMENTOS_99 = [
    ("99_arquivo/escritorio-virtual/dev-local_2026-11/_backup/analyses_pre-drive_20261006/"
     "normative-transcription/",
     "99_arquivo/escritorio-virtual/transcr-bkp_20261006/"),
    ("{q}/_acervo-escritorio-virtual/analyses/normative-transcription/",
     "{q}/transcr-analyses/"),
]

# Estrutura da Seção 5.2 (lote a). A pasta de quarentena é acrescentada em tempo
# de execução, com a data definida no planejamento.
ESTRUTURA = [
    "00_entrada",
    "01_processos",
    "02_notas-tecnicas", "02_notas-tecnicas/2025", "02_notas-tecnicas/2026",
    "03_normativos", "03_normativos/revogados",
    "04_colegiados", "04_colegiados/ctgric", "04_colegiados/conselho-governanca",
    "04_colegiados/cig", "04_colegiados/ctgd",
    "05_projetos",
    "06_gestao-da-coordenacao",
    "90_escritorio-virtual", "90_escritorio-virtual/referencia",
    "90_escritorio-virtual/modelos", "90_escritorio-virtual/manutencao",
    "90_escritorio-virtual/transcricoes",
    "99_arquivo", "99_arquivo/processos-encerrados",
    "99_arquivo/versoes-anteriores", "99_arquivo/escritorio-virtual",
]

# Áreas atuais (Seção 3.4)
A_PROC = "CGOV_Processos"
A_ADM = "CGOV_Administrativo"
A_NORM = "CGOV_Normativas"
A_NT = "CGOV_Notas Técnicas"
A_PROJ = "CGOV_Projetos"
A_ORG = "organizar"
A_NS = "normative-sources"
A_ACV = "_acervo-escritorio-virtual"

# Áreas da estrutura antiga, esvaziadas pelos lotes a–g (D29: --limpar-vazias).
AREAS_ANTIGAS = [A_PROC, A_ADM, A_NORM, A_NT, A_PROJ, A_ORG, A_NS, A_ACV]

# Subpastas improvisadas dos processos → subpasta padronizada (Seção 5.5).
# Chave: nome normalizado (sem acento, minúsculas). Valor: (subpasta, prefixo).
SUBPASTAS_PROCESSO = {
    "_cgov_nt": ("trabalho", ""),
    "claude outputs": ("trabalho", "claude-outputs"),
    "avaliacao_pgd": ("trabalho", "avaliacao-pgd"),
    "oficina": ("trabalho", "oficina"),
    "_referencias": ("referencias", ""),
    "_referencias indicadores": ("referencias", "indicadores"),
    "consulta": ("referencias", "consulta"),
    "normativas": ("referencias", "normativas"),
    "_audios": ("referencias", "audios"),
    "guia de gestao": ("referencias", "guia-de-gestao"),
    "fichas indicadores": ("referencias", "fichas-indicadores"),
    "apresentacoes": ("referencias", "apresentacoes"),
}

# Pastas de analyses sem número SEI no nome, com destino definido no plano (5.5).
ANALYSES_ESPECIAIS = {
    "indicadores_ocde": ("processo", ("02070", "014637", "2025", "41"), "trabalho"),
    "_impacto regulatorio_plano de manejo": ("processo", ("02070", "017019", "2026", "34"), None),
    "sei__reunioes-cig": ("pasta", "04_colegiados/cig", None),
}

PALAVRAS_VAZIAS = {"de", "da", "do", "das", "dos", "e", "para", "a", "o",
                   "em", "no", "na", "com"}

RE_PROC = re.compile(
    r"^(?:SEI_)*(\d{5})(?: \(1\))?\.(\d{6})[ _](\d{4})[-_](\d{2})(?:[_ ](.*))?$")
RE_SEI_DOC = re.compile(r"^(?:\d{8}_)?SEI_", re.IGNORECASE)
RE_COPIA = re.compile(r"^(.*) \(1\)(\.[^.]+)?$")
RE_VERSAO = re.compile(r"^(.*?)[_ ]v\.?(\d+(?:\.\d+)*)(.*)$", re.IGNORECASE)
RE_NT_ANO = re.compile(r"N[TI](?:_[A-Z]+)?_\d+-(\d{4})")
RE_DATA8 = re.compile(r"^(\d{4})(\d{2})(\d{2})_(.+)$")

EXT_TRABALHO = {".md", ".docx", ".doc", ".gdoc", ".odt", ".txt", ".html", ".htm"}


# --------------------------------------------------------------------------- #
# Utilidades
# --------------------------------------------------------------------------- #

def sem_acento(t: str) -> str:
    t = unicodedata.normalize("NFKD", t)
    return "".join(c for c in t if not unicodedata.combining(c))


def chave_nome(t: str) -> str:
    return sem_acento(t).strip().lower()


def slug(t: str) -> str:
    """Apelido de pasta: minúsculas, hífen, sem acento, sem palavras vazias.
    Palavras vazias só caem quando são palavras isoladas ("e-agendas" fica)."""
    t = chave_nome(t)
    t = re.sub(r"[_ ]v\d+$", "", t)
    palavras = [w for w in re.split(r"[\s_]+", t) if w and w not in PALAVRAS_VAZIAS]
    partes = [p for w in palavras for p in re.split(r"[^a-z0-9]+", w) if p]
    return "-".join(partes)


def sha256_arquivo(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloco in iter(lambda: f.read(1024 * 1024), b""):
            h.update(bloco)
    return h.hexdigest()


def caminho_abs(raiz: Path, rel: str) -> Path:
    """Caminho absoluto. No Windows usa o prefixo de caminho longo (\\\\?\\) para aceitar caminhos com
    mais de 259 caracteres (já existem na pasta CGOV, sobretudo em backups)."""
    p = os.path.normpath(os.path.join(os.path.abspath(str(raiz)), *rel.split("/")))
    if os.name == "nt" and not p.startswith("\\\\?\\"):
        p = "\\\\?\\UNC\\" + p[2:] if p.startswith("\\\\") else "\\\\?\\" + p
    return Path(p)


def configurar_saida() -> None:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except Exception:
            pass


def ler_env_repo() -> dict:
    env = {}
    arq = REPO / ".env"
    if arq.exists():
        for linha in arq.read_text(encoding="utf-8", errors="replace").splitlines():
            linha = linha.strip()
            if linha and not linha.startswith("#") and "=" in linha:
                k, v = linha.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def resolver_raiz(arg: str | None) -> Path:
    cand = arg or os.environ.get("CGOV_RAIZ") or ler_env_repo().get("CGOV_RAIZ")
    if not cand:
        acv = ler_env_repo().get("CGOV_ACERVO_DRIVE")
        if acv and Path(acv).name == A_ACV:
            cand = str(Path(acv).parent)
    if not cand:
        sys.exit("[PARE] Informe a pasta CGOV com --raiz ou defina CGOV_RAIZ no .env.")
    raiz = Path(cand).expanduser()
    if not raiz.is_dir():
        sys.exit(f"[PARE] Pasta CGOV inexistente: {raiz}")
    return raiz


def ler_tabela(caminho: Path, colunas: list[str]) -> list[dict]:
    if not caminho.exists():
        return []
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        linhas = [l for l in csv.DictReader(f, delimiter=DELIM)
                  if any((v or "").strip() for v in l.values())]
    faltam = [c for c in colunas if linhas and c not in linhas[0]]
    if faltam:
        sys.exit(f"[PARE] {caminho.name} sem as colunas: {', '.join(faltam)}")
    return linhas


def ler_mapa(caminho: Path) -> list[dict]:
    if not caminho.exists():
        sys.exit(f"[PARE] Mapa não encontrado: {caminho}. Rode --planejar antes.")
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.DictReader(f, delimiter=DELIM))
    faltam = [c for c in COLUNAS if c not in (linhas[0].keys() if linhas else COLUNAS)]
    if faltam:
        sys.exit(f"[PARE] Mapa sem as colunas: {', '.join(faltam)}")
    invalidas = [l["id"] for l in linhas if l["acao"] not in ACOES]
    if invalidas:
        sys.exit(f"[PARE] Ação inválida nas linhas: {', '.join(invalidas[:20])}")
    return linhas


def gravar_mapa(caminho: Path, linhas: list[dict]) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    tmp = caminho.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUNAS, delimiter=DELIM)
        w.writeheader()
        for l in linhas:
            w.writerow({c: l.get(c, "") for c in COLUNAS})
    os.replace(tmp, caminho)


# --------------------------------------------------------------------------- #
# Cache de hashes (permite retomar o cálculo em várias execuções)
# --------------------------------------------------------------------------- #

class CacheHash:
    def __init__(self, caminho: Path):
        self.caminho = caminho
        self.dados: dict[str, tuple[int, int, str]] = {}
        if caminho.exists():
            with open(caminho, encoding="utf-8", newline="") as f:
                for r in csv.reader(f, delimiter=DELIM):
                    if len(r) == 4 and r[0] != "caminho":
                        self.dados[r[0]] = (int(r[1]), int(r[2]), r[3])

    def obter(self, rel: str, tam: int, mtime: int) -> str | None:
        v = self.dados.get(rel)
        return v[2] if v and v[0] == tam and v[1] == mtime else None

    def guardar(self, rel: str, tam: int, mtime: int, sha: str) -> None:
        self.dados[rel] = (tam, mtime, sha)

    def salvar(self) -> None:
        self.caminho.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.caminho.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=DELIM)
            w.writerow(["caminho", "bytes", "mtime_ns", "sha256"])
            for k in sorted(self.dados):
                w.writerow([k, *self.dados[k]])
        os.replace(tmp, self.caminho)


# --------------------------------------------------------------------------- #
# Planejamento
# --------------------------------------------------------------------------- #

class Planejador:
    def __init__(self, raiz: Path, data_q: str, cache: CacheHash, limite_s: int,
                 decisoes: list[dict] | None = None, apelidos: dict | None = None):
        self.raiz = raiz
        self.decisoes = decisoes or []
        self.apelidos = apelidos or {}
        self.q = f"99_arquivo/_a-excluir_{data_q}"
        self.cache = cache
        self.limite_s = limite_s
        self.arquivos: list[str] = []
        self.pastas_vazias: list[str] = []
        self.info: dict[str, tuple[int, str]] = {}      # rel -> (bytes, sha)
        self.por_hash: dict[str, list[str]] = defaultdict(list)
        self.linhas: list[dict] = []
        self.processos: dict[tuple, dict] = {}          # chave -> dados do processo
        self.pastas_proc: dict[str, tuple] = {}         # pasta de origem -> chave

    # ---------- inventário e hash
    def inventariar(self) -> bool:
        for dirpath, dirnames, filenames in os.walk(self.raiz):
            dirnames.sort()
            rel_dir = os.path.relpath(dirpath, self.raiz).replace(os.sep, "/")
            rel_dir = "" if rel_dir == "." else rel_dir
            for n in sorted(filenames):
                self.arquivos.append(f"{rel_dir}/{n}" if rel_dir else n)
            if rel_dir and not dirnames and not filenames:
                self.pastas_vazias.append(rel_dir)
        inicio, novos = time.monotonic(), 0
        for i, rel in enumerate(self.arquivos, 1):
            p = caminho_abs(self.raiz, rel)
            st = p.stat()
            sha = self.cache.obter(rel, st.st_size, st.st_mtime_ns)
            if sha is None:
                sha = sha256_arquivo(p)
                self.cache.guardar(rel, st.st_size, st.st_mtime_ns, sha)
                novos += 1
                if novos % 200 == 0:
                    self.cache.salvar()
            self.info[rel] = (st.st_size, sha)
            self.por_hash[sha].append(rel)
            if self.limite_s and time.monotonic() - inicio > self.limite_s:
                self.cache.salvar()
                print(f"[PARCIAL] {i} de {len(self.arquivos)} arquivos com hash "
                      f"({novos} calculados agora). Rode --planejar de novo para continuar.")
                return False
        self.cache.salvar()
        print(f"[OK] {len(self.arquivos)} arquivos inventariados; {novos} hashes "
              f"calculados agora, {len(self.arquivos) - novos} do cache.")
        return True

    # ---------- processos
    def registrar_processo(self, pasta_rel: str, nome: str, prioridade: int) -> tuple | None:
        m = RE_PROC.match(nome)
        if not m:
            return None
        org, num, ano, dv, resto = m.groups()
        chave = (org, num, ano, dv)
        p = self.processos.setdefault(chave, {"apelidos": [], "pastas": []})
        ap = slug(resto or "")
        n_arq = sum(1 for a in self.arquivos if a.startswith(pasta_rel + "/"))
        p["pastas"].append((prioridade, pasta_rel, ap, n_arq))
        if ap:
            p["apelidos"].append((prioridade, -n_arq, ap, pasta_rel))
        self.pastas_proc[pasta_rel] = chave
        return chave

    def descobrir_processos(self) -> None:
        tops = defaultdict(set)
        for rel in self.arquivos + self.pastas_vazias:
            partes = rel.split("/")
            if partes[0] in (A_PROC, A_ADM) and len(partes) >= 2:
                tops[partes[0]].add(partes[1])
            if partes[0] == A_ACV and len(partes) >= 3 and partes[1] == "analyses":
                tops["analyses"].add(partes[2])
        for nome in sorted(tops[A_PROC]):
            if " (1)." not in nome:
                self.registrar_processo(f"{A_PROC}/{nome}", nome, 1)
        for nome in sorted(tops[A_ADM]):
            self.registrar_processo(f"{A_ADM}/{nome}", nome, 2)
        for nome in sorted(tops["analyses"]):
            pasta = f"{A_ACV}/analyses/{nome}"
            so_movido = all(a.endswith("/MOVIDO_PARA.txt") for a in self.arquivos
                            if a.startswith(pasta + "/"))
            if not so_movido:
                self.registrar_processo(pasta, nome, 3)
        for chave, p in self.processos.items():
            org, num, ano, dv = chave
            ap = sorted(p["apelidos"])[0][2] if p["apelidos"] else ""
            num_sei = f"{org}.{num}/{ano}-{dv}"
            if num_sei in self.apelidos:        # decisão do Coordenador (4.2)
                ap = slug(self.apelidos[num_sei])
            p["apelido"] = ap
            p["pasta"] = f"01_processos/SEI_{org}.{num}_{ano}-{dv}" + (f"_{ap}" if ap else "")
            # pastas da mesma área com apelidos diferentes → fusão a decidir
            principais = sorted(x for x in p["pastas"] if x[0] == 1)
            p["secundarias"] = set()
            if len(principais) > 1:
                base = sorted(principais, key=lambda x: (-x[3], x[1]))[0]
                for x in principais:
                    if x is not base and x[2] != base[2]:
                        p["secundarias"].add(x[1])

    def pasta_processo(self, chave: tuple) -> str:
        return self.processos[chave]["pasta"]

    @staticmethod
    def classe_solta(nome: str, padrao_nao_pdf: str = "auto") -> str:
        ext = os.path.splitext(nome)[1].lower()
        if ext == ".pdf":
            return "documentos-sei" if RE_SEI_DOC.match(nome) else "referencias"
        if padrao_nao_pdf != "auto":
            return padrao_nao_pdf
        return "trabalho" if ext in EXT_TRABALHO else "referencias"

    # ---------- linhas
    def add(self, rel: str, destino: str, acao: str, motivo: str, tipo: str = "arquivo") -> None:
        tam, sha = self.info.get(rel, (0, ""))
        partes = rel.split("/")
        if len(partes) == 1:
            area = "raiz"
        elif partes[0] == A_ACV and len(partes) > 2:
            area = f"{A_ACV}/{partes[1]}"
        else:
            area = partes[0]
        self.linhas.append({"tipo": tipo, "area_origem": area, "origem": rel,
                            "destino": destino, "acao": acao, "sha256": sha,
                            "bytes": tam if tipo == "arquivo" else "", "motivo": motivo})

    def quarentena(self, rel: str, motivo: str, tipo: str = "arquivo") -> None:
        self.add(rel, f"{self.q}/{rel}", "quarentena", motivo, tipo)

    def copia_identica(self, rel: str, fora_de: str | None = None) -> str | None:
        sha = self.info[rel][1]
        for outro in self.por_hash[sha]:
            if outro != rel and not RE_COPIA.match(os.path.basename(outro)) \
                    and (fora_de is None or not outro.startswith(fora_de)):
                return outro
        return None

    # ---------- regras por área
    def regra_processo_interno(self, rel: str, chave: tuple, interno: list[str],
                               area: str) -> None:
        pasta = self.pasta_processo(chave)
        nome = interno[-1]
        tam = self.info[rel][0]
        if tam == 0 and os.path.splitext(nome)[1].lower() in (".txt", ".tmp"):
            self.quarentena(rel, "arquivo vazio (0 bytes) — Seção 5.6")
            return
        if len(interno) == 1:
            sub = self.classe_solta(nome)
            self.add(rel, f"{pasta}/{sub}/{nome}", "mover",
                     f"arquivo solto do processo → {sub} (Seção 5.5 — heurística por tipo)")
            return
        chave_sub = chave_nome(interno[0])
        if chave_sub in SUBPASTAS_PROCESSO:
            sub, pref = SUBPASTAS_PROCESSO[chave_sub]
            resto = "/".join(([pref] if pref else []) + interno[1:])
            self.add(rel, f"{pasta}/{sub}/{resto}", "mover",
                     f"subpasta '{interno[0]}' → {sub} (Seção 5.5)")
        else:
            resto = "/".join([slug(interno[0])] + interno[1:])
            self.add(rel, f"{pasta}/trabalho/{resto}", "a-decidir",
                     f"subpasta '{interno[0]}' sem regra no plano — proposta: trabalho")

    def regra_processos(self, rel: str, partes: list[str]) -> None:
        nome_pasta = partes[1]
        if len(partes) == 2:   # arquivo solto na raiz de CGOV_Processos
            self.add(rel, f"00_entrada/{partes[1]}", "a-decidir", "arquivo solto em CGOV_Processos")
            return
        if nome_pasta == "ADPF":
            self.add(rel, "99_arquivo/processos-encerrados/ADPF/" + "/".join(partes[2:]),
                     "mover", "projeto antigo sem número SEI rastreável (D11)")
            return
        pasta_rel = f"{A_PROC}/{nome_pasta}"
        chave = self.pastas_proc.get(pasta_rel)
        if not chave:
            self.add(rel, f"01_processos/{slug(nome_pasta)}/" + "/".join(partes[2:]),
                     "a-decidir", "pasta sem número SEI reconhecível")
            return
        if pasta_rel in self.processos[chave]["secundarias"]:
            pasta = self.pasta_processo(chave)
            ap2 = slug(RE_PROC.match(nome_pasta).group(5) or "") or "pasta-2"
            self.add(rel, f"{pasta}/trabalho/{ap2}/" + "/".join(partes[2:]),
                     "a-decidir",
                     f"duas pastas para o mesmo processo com apelidos diferentes — "
                     f"proposta: fundir em {pasta.split('/')[-1]} (como D10)")
            return
        self.regra_processo_interno(rel, chave, partes[2:], A_PROC)

    def regra_administrativo(self, rel: str, partes: list[str]) -> None:
        if len(partes) >= 3 and chave_nome(partes[1]) == chave_nome("CGOV_Fundo Rio Doce"):
            self.add(rel, "05_projetos/fundo-rio-doce/" + "/".join(partes[2:]), "mover",
                     "tema sem número SEI → 05_projetos (Seção 5.5)")
            return
        pasta_rel = "/".join(partes[:2])
        chave = self.pastas_proc.get(pasta_rel)
        if chave and len(partes) >= 3:
            self.regra_processo_interno(rel, chave, partes[2:], A_ADM)
        else:
            self.add(rel, "00_entrada/" + partes[-1], "a-decidir",
                     "item de CGOV_Administrativo sem regra")

    def regra_analyses(self, rel: str, partes: list[str]) -> None:
        if len(partes) == 3:   # arquivo solto em analyses
            nome = partes[2]
            if self.info[rel][0] == 0 or nome.endswith(".tmp"):
                self.quarentena(rel, "arquivo de teste vazio (Seção 5.6)")
            else:
                self.add(rel, "00_entrada/" + nome, "a-decidir", "arquivo solto em analyses")
            return
        pasta, interno = partes[2], partes[3:]
        pasta_rel = f"{A_ACV}/analyses/{pasta}"
        cp = chave_nome(pasta)
        if interno == ["MOVIDO_PARA.txt"]:
            self.quarentena(rel, "aviso de movimentação já executada em 07/10/2026 (Seção 5.6)")
            return
        if cp == "normative-transcription":
            if rel.lower().endswith(".png"):
                self.quarentena(rel, "página renderizada, regenerável a partir do PDF (Seção 5.6)")
            else:
                self.add(rel, "90_escritorio-virtual/transcricoes/" + "/".join(interno),
                         "mover", "trabalho intermediário de OCR (Seção 5.5)")
            return
        if cp.startswith("revisao-prompts-legados"):
            self.add(rel, f"99_arquivo/escritorio-virtual/{pasta}/" + "/".join(interno),
                     "mover", "artefato de desenvolvimento (Seção 5.5)")
            return
        if cp == "_doutorado":
            self.add(rel, "../../_projetos/05_privado/_doutorado/" + "/".join(interno),
                     "mover", "material pessoal sai da pasta institucional (D14)")
            return
        if cp in ANALYSES_ESPECIAIS:
            tipo, alvo, sub = ANALYSES_ESPECIAIS[cp]
            if tipo == "pasta":
                self.add(rel, f"{alvo}/" + "/".join(interno), "mover",
                         "reuniões de colegiado → 04_colegiados (Seção 5.5)")
                return
            if alvo not in self.processos:
                self.add(rel, "00_entrada/" + interno[-1], "a-decidir",
                         "processo de destino não encontrado")
                return
            ppasta = self.pasta_processo(alvo)
            if cp == "_impacto regulatorio_plano de manejo":
                nome = interno[-1]
                if re.search(r"Nota_Tecnica_\d+_final\.pdf$", nome):
                    self.add(rel, f"02_notas-tecnicas/2026/{nome}", "mover",
                             "NT 27/2026 assinada → série oficial (Seção 5.5, D11)")
                elif chave_nome(interno[0]) == "referencias":
                    self.add(rel, f"{ppasta}/referencias/" + "/".join(interno[1:]), "mover",
                             "referências da NT 27/2026 (D11)")
                else:
                    self.add(rel, f"{ppasta}/trabalho/" + "/".join(interno), "mover",
                             "minutas e versões da NT 27/2026 → trabalho (D11)")
                return
            self.add(rel, f"{ppasta}/{sub}/" + "/".join(interno), "mover",
                     "análise vinculada ao processo pelo plano (Seção 5.5)")
            return
        chave = self.pastas_proc.get(pasta_rel)
        if not chave:
            self.add(rel, "00_entrada/" + "/".join(interno), "a-decidir",
                     f"pasta '{pasta}' de analyses sem regra")
            return
        ppasta = self.pasta_processo(chave)
        if chave_nome(interno[0]) in ("tmp", "_tmp"):
            self.quarentena(rel, "temporário de revisão (Seção 5.6)")
            return
        nome = interno[-1]
        if len(interno) == 1 and nome.lower().endswith(".pdf") and RE_SEI_DOC.match(nome):
            sub = "documentos-sei"
        elif len(interno) == 1 and nome.lower().endswith(".pdf"):
            sub = "referencias"
        else:
            sub = "trabalho"
        self.add(rel, f"{ppasta}/{sub}/" + "/".join(interno), "mover",
                 f"segunda árvore de processos fundida por nº SEI → {sub} (Seção 5.5)")

    def regra_acervo(self, rel: str, partes: list[str]) -> None:
        if len(partes) < 3:
            self.add(rel, "90_escritorio-virtual/" + partes[-1], "a-decidir",
                     "arquivo solto no acervo")
            return
        sub, interno = chave_nome(partes[1]), "/".join(partes[2:])
        if sub == "analyses":
            self.regra_analyses(rel, partes)
        elif sub == "_referencia":
            self.add(rel, f"90_escritorio-virtual/referencia/{interno}", "mover",
                     "documentação publicada (Seção 5.5)")
        elif sub == "manutencao":
            self.add(rel, f"90_escritorio-virtual/manutencao/{interno}", "mover",
                     "canal de pendências (Seção 5.5)")
        elif sub == "archive":
            self.add(rel, f"99_arquivo/escritorio-virtual/{interno}", "mover",
                     "arquivo histórico do escritório — backup mantido até o fim da Fase 4 (5.6)")
        elif sub == "_tmp":
            self.quarentena(rel, "temporário de revisão (Seção 5.6)")
        else:
            self.add(rel, f"90_escritorio-virtual/{interno}", "a-decidir",
                     f"subpasta '{partes[1]}' do acervo sem regra")

    def regra_normative_sources(self, rel: str, partes: list[str]) -> None:
        interno = "/".join(partes[1:])
        nome = partes[-1]
        if nome.lower().startswith("minuta"):
            self.add(rel, f"03_normativos/{interno}", "a-decidir",
                     "minuta em discussão: pelo mapa de finalidades fica no processo — "
                     "indicar o processo")
        elif "revogad" in chave_nome(nome):
            self.add(rel, f"03_normativos/revogados/{interno}", "mover",
                     "normativo revogado (Seção 5.5)")
        else:
            self.add(rel, f"03_normativos/{interno}", "mover", "acervo normativo único (Seção 5.5)")

    def regra_normativas(self, rel: str, partes: list[str]) -> None:
        nome = partes[-1]
        igual = self.copia_identica(rel, fora_de=f"{A_NORM}/")
        if igual:
            self.quarentena(rel, f"idêntico (SHA-256) a {igual} (Seção 5.5)")
            return
        if "minuta" in chave_nome(nome):
            self.add(rel, f"03_normativos/{nome}", "a-decidir",
                     "minuta em discussão: pelo mapa de finalidades fica no processo")
            return
        if re.search(r"768-2020", nome):
            self.add(rel, f"03_normativos/revogados/{nome}", "mover",
                     "PGE (Portaria nº 768/2020) revogada (Seção 5.5)")
            return
        stem = chave_nome(os.path.splitext(nome)[0])
        parecido = None
        if not RE_DATA8.match(nome):
            for a in self.arquivos:
                if a.startswith(A_NS + "/"):
                    m = RE_DATA8.match(os.path.basename(a))
                    if m and chave_nome(os.path.splitext(m.group(4))[0]) == stem:
                        parecido = a
                        break
        if parecido:
            self.add(rel, f"03_normativos/{nome}", "a-decidir",
                     f"mesmo normativo de {parecido}, mas com conteúdo diferente "
                     f"(SHA-256 distinto): manter as duas versões?")
            return
        self.add(rel, f"03_normativos/{nome}", "mover",
                 "exclusivo de CGOV_Normativas (Seção 5.5)")

    def regra_notas_tecnicas(self, rel: str, partes: list[str]) -> None:
        nome = partes[-1]
        if "retirar" in chave_nome(nome):
            m = RE_NT_ANO.search(nome)
            ano = m.group(1) if m else "2025"
            self.add(rel, f"02_notas-tecnicas/{ano}/{nome}", "a-decidir",
                     "nome contém 'Retirar': NT válida da série ou vai para 99_arquivo?")
            return
        m = RE_NT_ANO.search(nome)
        if not m:
            self.add(rel, f"02_notas-tecnicas/2026/{nome}", "a-decidir",
                     "ano da NT não consta do nome — proposta 2026 pela numeração do "
                     "documento SEI ⚠️ confirmar")
            return
        self.add(rel, f"02_notas-tecnicas/{m.group(1)}/{nome}", "mover",
                 "série oficial — nome original mantido nesta etapa (Seção 5.5)")

    def regra_versoes(self, arquivos: list[str]) -> dict[str, bool]:
        """Retorna rel -> True se é a versão mais recente (D15)."""
        grupos = defaultdict(list)
        for rel in arquivos:
            stem = os.path.splitext(os.path.basename(rel))[0]
            m = RE_VERSAO.match(stem)
            if m:
                ver = tuple(int(x) for x in m.group(2).split("."))
                grupos[(os.path.dirname(rel), chave_nome(m.group(1)))].append((ver, rel))
        vigente = {}
        for itens in grupos.values():
            maxv = max(v for v, _ in itens)
            for v, rel in itens:
                vigente[rel] = (v == maxv) or len(itens) == 1
        return vigente

    def regra_projetos(self, rel: str, partes: list[str], vigente: dict) -> None:
        nome = partes[-1]
        if len(partes) == 2:
            if "plano de entregas" in chave_nome(nome):
                self.add(rel, f"06_gestao-da-coordenacao/{nome}", "mover",
                         "Plano de Entregas CGOV (GIZ) → 06 (Seção 5.5)")
            elif re.search(r"ppi|parcerias para inovacao", chave_nome(nome)):
                self.add(rel, f"05_projetos/parcerias-inovacao/{nome}", "a-decidir",
                         "material do Projeto Parcerias para Inovação: 05_projetos ou "
                         "processo SEI 02070.011203/2025-90 (referencias)?")
            else:
                self.add(rel, f"00_entrada/{nome}", "a-decidir",
                         "arquivo solto em CGOV_Projetos sem projeto identificado")
            return
        m = RE_DATA8.match(partes[1])
        projeto = f"{m.group(1)}-{m.group(2)}_{slug(m.group(4))}" if m else slug(partes[1])
        interno = "/".join(partes[2:])
        if vigente.get(rel) is False:
            self.add(rel, f"99_arquivo/versoes-anteriores/{projeto}/{interno}", "mover",
                     "versão superada — a mais recente fica no projeto (D15)")
        else:
            self.add(rel, f"05_projetos/{projeto}/{interno}", "mover",
                     "projeto sem processo SEI → 05_projetos/AAAA-MM_apelido (Seção 5.4)")

    def regra_organizar(self, rel: str, vigente: dict) -> None:
        nome = os.path.basename(rel)
        if vigente.get(rel, True):
            self.add(rel, f"06_gestao-da-coordenacao/plano-de-entregas/{nome}", "mover",
                     "versão mais recente do Plano de Entregas CGGE (D15)")
        else:
            self.add(rel, f"99_arquivo/versoes-anteriores/plano-de-entregas/{nome}", "mover",
                     "versão anterior do Plano de Entregas CGGE (D15)")

    def regra_raiz(self, rel: str) -> None:
        n = chave_nome(rel)
        if "ctgric" in n:
            self.add(rel, f"04_colegiados/ctgric/{rel}", "mover",
                     "transcrição de reunião do CTGRIC — o par .docx/.gdoc vai junto (5.5)")
        elif rel == "cgov_projetos_trimestre.html":
            self.add(rel, f"06_gestao-da-coordenacao/{rel}", "mover", "acompanhamento da CGOV (5.5)")
        else:
            self.add(rel, f"00_entrada/{rel}", "a-decidir", "arquivo solto na raiz")

    # ---------- execução do planejamento
    def planejar(self) -> list[dict]:
        self.descobrir_processos()
        vig_proj = self.regra_versoes([a for a in self.arquivos
                                       if a.startswith(A_PROJ + "/") and a.count("/") >= 2])
        vig_org = self.regra_versoes([a for a in self.arquivos if a.startswith(A_ORG + "/")])
        for rel in self.arquivos:
            partes = rel.split("/")
            area = partes[0] if len(partes) > 1 else ""
            # cópias "(1)" (Seção 5.6)
            m = RE_COPIA.match(partes[-1])
            if m and area not in (A_NORM,):
                igual = self.copia_identica(rel)
                if igual:
                    self.quarentena(rel, f"cópia '(1)' idêntica (SHA-256) a {igual} (Seção 5.6)")
                    continue
            if not area:
                self.regra_raiz(rel)
            elif area == A_PROC:
                self.regra_processos(rel, partes)
            elif area == A_ADM:
                self.regra_administrativo(rel, partes)
            elif area == A_ACV:
                self.regra_acervo(rel, partes)
            elif area == A_NS:
                self.regra_normative_sources(rel, partes)
            elif area == A_NORM:
                self.regra_normativas(rel, partes)
            elif area == A_NT:
                self.regra_notas_tecnicas(rel, partes)
            elif area == A_PROJ:
                self.regra_projetos(rel, partes, vig_proj)
            elif area == A_ORG:
                self.regra_organizar(rel, vig_org)
            elif area[:2].isdigit() and area[2:3] == "_":
                self.add(rel, rel, "a-decidir", "já está na estrutura nova?")
            else:
                self.add(rel, f"00_entrada/{partes[-1]}", "a-decidir", f"área '{area}' sem regra")
        for pv in self.pastas_vazias:
            self.quarentena(pv, "pasta vazia (Seção 5.6)", tipo="pasta")
        self.resolver_colisoes()
        self.renomear_copias()
        self.aplicar_decisoes()
        self.encurtar_destinos()
        self.ajustar_tipo_acao()
        self.acrescentar_estrutura()
        self.numerar()
        return self.linhas

    def resolver_colisoes(self) -> None:
        """Destinos repetidos: idênticos → quarentena; versão _v2 → trabalho/v2 (D10);
        demais → a-decidir."""
        for _ in range(3):
            grupos = defaultdict(list)
            for l in self.linhas:
                if l["acao"] != "quarentena":
                    grupos[chave_nome(l["destino"])].append(l)
            mudou = False
            for itens in grupos.values():
                if len(itens) < 2:
                    continue
                prior = {A_PROC: 0, A_NS: 0, A_ADM: 1}   # áreas canônicas primeiro
                itens.sort(key=lambda l: (prior.get(l["area_origem"], 2), l["origem"]))
                base = itens[0]
                for l in itens[1:]:
                    mudou = True
                    if l["sha256"] and l["sha256"] == base["sha256"]:
                        l.update(destino=f"{self.q}/{l['origem']}", acao="quarentena",
                                 motivo=f"duplicata idêntica (SHA-256) de {base['origem']} "
                                        f"(ADR-014)")
                    elif re.search(r"_v\d+$", l["origem"].split("/")[1] if "/" in l["origem"] else ""):
                        pasta = "/".join(l["destino"].split("/")[:2])
                        l.update(destino=f"{pasta}/trabalho/v2/{os.path.basename(l['destino'])}",
                                 motivo="mesmo nome que arquivo da pasta principal, conteúdo "
                                        "diferente → trabalho/v2 (D10)")
                    else:
                        d, b = os.path.split(l["destino"])
                        s, e = os.path.splitext(b)
                        l.update(destino=f"{d}/{s}__origem-{slug(l['area_origem'])}{e}",
                                 acao="a-decidir",
                                 motivo=f"conflito de nome com {base['origem']} (conteúdo "
                                        f"diferente); proposta: manter os dois com sufixo")
            if not mudou:
                break
        # destinos que já existem no disco e não serão movidos
        origens = {chave_nome(l["origem"]) for l in self.linhas}
        for l in self.linhas:
            if l["acao"] in ("mover", "renomear") and \
                    caminho_abs(self.raiz, l["destino"]).exists() and \
                    chave_nome(l["destino"]) not in origens:
                l.update(acao="a-decidir", motivo="destino já existe no disco: " + l["motivo"])

    def renomear_copias(self) -> None:
        """'(1)' sem original idêntico: tira o sufixo, se o nome estiver livre."""
        destinos = {chave_nome(l["destino"]) for l in self.linhas}
        for l in self.linhas:
            m = RE_COPIA.match(os.path.basename(l["destino"]))
            if m and l["acao"] == "mover":
                novo = f"{os.path.dirname(l['destino'])}/{m.group(1)}{m.group(2) or ''}"
                if chave_nome(novo) in destinos:
                    l.update(acao="a-decidir",
                             motivo="cópia '(1)' com conteúdo diferente do original")
                else:
                    l.update(destino=novo, acao="renomear",
                             motivo="sufixo '(1)' sem original correspondente: retirado")
                    destinos.add(chave_nome(novo))

    def resolver_marcadores(self, destino: str, origem: str) -> str:
        """{nome} = nome do arquivo de origem; {proc:02070.006604/2026-17} = pasta do processo."""
        def proc(m):
            k = re.match(r"(\d{5})\.(\d{6})/(\d{4})-(\d{2})$", m.group(1))
            if not k or tuple(k.groups()) not in self.processos:
                raise KeyError(f"processo {m.group(1)} não existe no mapa")
            return self.processos[tuple(k.groups())]["pasta"]
        destino = re.sub(r"\{proc:([^}]+)\}", proc, destino)
        return destino.replace("{nome}", os.path.basename(origem))

    def aplicar_decisoes(self) -> None:
        """Decisões do Coordenador (etapa 4.2) por origem, registradas em decisoes.csv."""
        por_origem = {l["origem"]: l for l in self.linhas}
        self.decisoes_nao_aplicadas = []
        for d in self.decisoes:
            l = por_origem.get(d["origem"])
            if not l:
                self.decisoes_nao_aplicadas.append(d["origem"])
                continue
            if d["acao"] not in ACOES or d["acao"] in ("criar", "a-decidir"):
                sys.exit(f"[PARE] Ação inválida em decisoes.csv: {d['acao']} ({d['origem']})")
            destino = d.get("destino") or l["destino"]
            if d["acao"] == "quarentena":
                destino = f"{self.q}/{l['origem']}"
            l.update(acao=d["acao"], destino=self.resolver_marcadores(destino, l["origem"]),
                     motivo=f"decisão do Coordenador (4.2): {d.get('motivo', '')}".strip())
        if self.decisoes_nao_aplicadas:
            print(f"[AVISO] {len(self.decisoes_nao_aplicadas)} decisão(ões) sem origem no "
                  f"inventário: " + "; ".join(self.decisoes_nao_aplicadas[:5]))

    def encurtar_destinos(self) -> None:
        """D26 (etapa 4.4a): troca prefixos longos de 99_arquivo (ENCURTAMENTOS_99)."""
        trocas = [(a.replace("{q}", self.q), b.replace("{q}", self.q))
                  for a, b in ENCURTAMENTOS_99]
        for antigo, novo in trocas:
            ocupado = [l["destino"] for l in self.linhas
                       if l["destino"].startswith(novo) or l["destino"] == novo.rstrip("/")]
            if ocupado:
                sys.exit(f"[PARE] Prefixo encurtado já usado no mapa: {ocupado[0]}")
        self.encurtados = Counter()
        for l in self.linhas:
            for antigo, novo in trocas:
                if l["destino"].startswith(antigo):
                    l["destino"] = novo + l["destino"][len(antigo):]
                    l["motivo"] += " · destino encurtado (D26)"
                    self.encurtados[novo] += 1
                    break

    def ajustar_tipo_acao(self) -> None:
        for l in self.linhas:
            if l["acao"] == "mover" and \
                    os.path.basename(l["origem"]) != os.path.basename(l["destino"]):
                l["acao"] = "renomear"
            d = l["destino"]
            if l["acao"] == "quarentena":
                l["lote"] = "g"
            elif d.startswith("03_"):
                l["lote"] = "b"
            elif d.startswith("02_"):
                l["lote"] = "c"
            elif d.startswith("01_"):
                l["lote"] = "d"
            elif d[:3] in ("04_", "05_", "06_") or d.startswith("00_"):
                l["lote"] = "e"
            else:
                l["lote"] = "f"

    def acrescentar_estrutura(self) -> None:
        for p in ESTRUTURA + [self.q]:
            self.linhas.append({"lote": "a", "tipo": "pasta", "area_origem": "",
                                "origem": "", "destino": p, "acao": "criar",
                                "sha256": "", "bytes": "",
                                "motivo": "estrutura da Seção 5.2" if p != self.q
                                else "quarentena (ADR-014, D16)"})

    def numerar(self) -> None:
        self.linhas.sort(key=lambda l: (l["lote"], l["destino"].lower(), l["origem"]))
        for i, l in enumerate(self.linhas, 1):
            l["id"] = f"{i:05d}"


# --------------------------------------------------------------------------- #
# Resumo
# --------------------------------------------------------------------------- #

def comprimento_windows(raiz_len: int, rel: str) -> int:
    return raiz_len + 1 + len(os.path.normpath(rel.replace("/", "\\")))


def resumo(linhas: list[dict], raiz_len: int, planejador: Planejador | None = None) -> str:
    arq = [l for l in linhas if l["tipo"] == "arquivo"]
    out = []
    p = out.append
    p(f"# Resumo do mapa de reorganização — {dt.date.today():%d/%m/%Y}\n")
    p(f"Gerado por `reorganizar_cgov.py` v{VERSAO} (modo --planejar; nada foi movido).\n")
    tot_bytes = sum(int(l["bytes"] or 0) for l in arq)
    p(f"- Linhas: **{len(linhas)}** ({len(arq)} arquivos, "
      f"{len(linhas) - len(arq)} pastas) · volume dos arquivos: "
      f"**{tot_bytes / 1024 ** 3:.2f} GB**\n")

    p("\n## Por ação (arquivos)\n")
    p("| Ação | Arquivos | MB |\n|---|---:|---:|")
    for a in ACOES:
        sel = [l for l in arq if l["acao"] == a]
        if sel:
            p(f"| {a} | {len(sel)} | {sum(int(l['bytes'] or 0) for l in sel) / 1024 ** 2:,.1f} |")
    p(f"| **total** | **{len(arq)}** | **{tot_bytes / 1024 ** 2:,.1f}** |")

    p("\n## Por área de origem × ação (arquivos)\n")
    areas = sorted({l["area_origem"] for l in arq})
    acoes_presentes = [a for a in ACOES if any(l["acao"] == a for l in arq)]
    p("| Área de origem | " + " | ".join(acoes_presentes) + " | total |")
    p("|---|" + "---:|" * (len(acoes_presentes) + 1))
    for ar in areas:
        c = Counter(l["acao"] for l in arq if l["area_origem"] == ar)
        p(f"| `{ar}` | " + " | ".join(str(c.get(a, "")) for a in acoes_presentes)
          + f" | {sum(c.values())} |")

    p("\n## Por lote (etapa 4.5)\n")
    p("| Lote | Conteúdo | Linhas | a-decidir |\n|---|---|---:|---:|")
    for lt, desc in LOTES.items():
        sel = [l for l in linhas if l["lote"] == lt]
        p(f"| {lt} | {desc} | {len(sel)} | {sum(1 for l in sel if l['acao'] == 'a-decidir')} |")

    dec = [l for l in linhas if l["acao"] == "a-decidir"]
    p(f"\n## Linhas a-decidir ({len(dec)})\n")
    p("| id | Origem | Destino proposto | Motivo |\n|---|---|---|---|")
    for l in dec:
        p(f"| {l['id']} | `{l['origem']}` | `{l['destino']}` | {l['motivo']} |")

    if planejador:
        p("\n## Pastas de processo (origem → destino)\n")
        p("| Destino | Origens | Arquivos |\n|---|---|---:|")
        cont = Counter("/".join(l["destino"].split("/")[:2]) for l in arq
                       if l["destino"].startswith("01_processos/"))
        for chave, pr in sorted(planejador.processos.items(), key=lambda x: x[1]["pasta"]):
            origens = "<br>".join(f"`{x[1]}`" for x in sorted(pr["pastas"]))
            nome = pr["pasta"].split("/")[-1] + ("" if pr["apelido"] else " ⚠️ sem apelido")
            p(f"| `{nome}` | {origens} | {cont.get(pr['pasta'], 0)} |")

    longos = [l for l in linhas if comprimento_windows(raiz_len, l["destino"]) > LIMITE_CAMINHO_WINDOWS]
    ja = sum(1 for l in linhas if l["origem"] and
             comprimento_windows(raiz_len, l["origem"]) > LIMITE_CAMINHO_WINDOWS)
    fora99 = [l for l in longos if not l["destino"].startswith("99_arquivo/")]
    p(f"\n## Caminhos de destino acima de {LIMITE_CAMINHO_WINDOWS} caracteres no Windows "
      f"({len(longos)})\n")
    p(f"Origens que já passam do limite hoje: {ja}. Destinos longos fora de `99_arquivo`: "
      f"**{len(fora99)}** (estes seriam conflito). No Windows o script usa o prefixo "
      f"`\\\\?\\`, que aceita caminhos longos; em `99_arquivo` eles são só aviso.\n")
    for l in longos[:50]:
        p(f"- {l['id']} ({comprimento_windows(raiz_len, l['destino'])}) `{l['destino']}`")
    if len(longos) > 50:
        p(f"- … e mais {len(longos) - 50}")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- #
# Simulação
# --------------------------------------------------------------------------- #

def conferir(linhas: list[dict], raiz: Path, lote: str | None, raiz_len: int,
             verificar_hash: bool) -> tuple[list[str], list[str]]:
    conflitos, avisos = [], []
    todos = defaultdict(list)
    for l in linhas:
        if l["acao"] != "a-decidir":
            todos[chave_nome(l["destino"])].append(l["id"])
    sel = [l for l in linhas if lote is None or l["lote"] == lote]
    for l in sel:
        i, acao = l["id"], l["acao"]
        if acao == "a-decidir":
            conflitos.append(f"{i}: linha a-decidir ({l['origem'] or l['destino']})")
            continue
        dst = caminho_abs(raiz, l["destino"])
        if len(todos[chave_nome(l["destino"])]) > 1:
            conflitos.append(f"{i}: destino repetido no mapa (linhas "
                             f"{', '.join(todos[chave_nome(l['destino'])])}): {l['destino']}")
        if comprimento_windows(raiz_len, l["destino"]) > LIMITE_CAMINHO_WINDOWS:
            (avisos if l["destino"].startswith("99_arquivo/") else conflitos).append(f"{i}: caminho longo no Windows "
                             f"({comprimento_windows(raiz_len, l['destino'])}): {l['destino']}")
        if acao == "criar":
            if dst.exists() and not dst.is_dir():
                conflitos.append(f"{i}: existe um arquivo no lugar da pasta {l['destino']}")
            continue
        src = caminho_abs(raiz, l["origem"])
        if not src.exists():
            if dst.exists():
                avisos.append(f"{i}: já executada (origem ausente, destino presente)")
            else:
                conflitos.append(f"{i}: origem inexistente: {l['origem']}")
            continue
        if dst.exists():
            conflitos.append(f"{i}: destino já existe: {l['destino']}")
        if l["tipo"] == "arquivo" and verificar_hash and l["sha256"]:
            if sha256_arquivo(src) != l["sha256"]:
                conflitos.append(f"{i}: SHA-256 mudou desde o planejamento: {l['origem']}")
        elif l["tipo"] == "arquivo" and l["bytes"] and src.stat().st_size != int(l["bytes"]):
            conflitos.append(f"{i}: tamanho mudou desde o planejamento: {l['origem']}")
    return conflitos, avisos


# --------------------------------------------------------------------------- #
# Execução e reversão
# --------------------------------------------------------------------------- #

def confirmar(msg: str, automatico: bool) -> bool:
    if automatico:
        return True
    print(msg)
    try:
        return input("Digite SIM para continuar: ").strip() == "SIM"
    except EOFError:
        return False


def executar(linhas: list[dict], raiz: Path, lote: str, raiz_len: int,
             verificar_hash: bool, sim: bool) -> int:
    sel = [l for l in linhas if l["lote"] == lote]
    if not sel:
        print(f"[OK] Lote {lote} sem linhas.")
        return 0
    conflitos, avisos = conferir(linhas, raiz, lote, raiz_len, verificar_hash=False)
    if conflitos:
        print(f"[PARE] Lote {lote}: {len(conflitos)} conflito(s). Rode --simular --lote {lote}.")
        for c in conflitos[:30]:
            print("   ", c)
        return 1
    n_arq = sum(1 for l in sel if l["tipo"] == "arquivo")
    if not confirmar(f"Lote {lote} ({LOTES[lote]}): {len(sel)} operações "
                     f"({n_arq} arquivos). Nada é excluído nem sobrescrito.", sim):
        print("[CANCELADO] Nada foi feito.")
        return 1
    REGISTROS.mkdir(parents=True, exist_ok=True)
    reg = REGISTROS / f"registro_lote-{lote}_{dt.datetime.now():%Y%m%d-%H%M%S}.csv"
    feitos, erros = Counter(), 0
    with open(reg, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=DELIM)
        w.writerow(["id", "acao", "tipo", "origem", "destino", "sha256", "situacao", "momento"])
        for l in sel:
            dst = caminho_abs(raiz, l["destino"])
            sit = "ok"
            try:
                if l["acao"] == "criar":
                    sit = "ja-existia" if dst.is_dir() else "ok"
                    dst.mkdir(parents=True, exist_ok=True)
                else:
                    src = caminho_abs(raiz, l["origem"])
                    if not src.exists() and dst.exists():
                        sit = "ja-executada"
                    else:
                        if l["tipo"] == "arquivo" and verificar_hash and l["sha256"] \
                                and sha256_arquivo(src) != l["sha256"]:
                            raise RuntimeError("SHA-256 diferente do planejado")
                        if dst.exists():
                            raise RuntimeError("destino já existe (não sobrescrevo)")
                        dst.parent.mkdir(parents=True, exist_ok=True)
                        os.rename(src, dst)
            except Exception as e:    # registra e para: nada fica pela metade sem registro
                sit = f"erro: {e}"
                erros += 1
            w.writerow([l["id"], l["acao"], l["tipo"], l["origem"], l["destino"],
                        l["sha256"], sit, dt.datetime.now().isoformat(timespec="seconds")])
            f.flush()
            feitos[sit.split(":")[0]] += 1
            if erros:
                print(f"[PARE] Erro na linha {l['id']}: {sit}")
                break
    print(f"[{'OK' if not erros else 'PARCIAL'}] Lote {lote}: " +
          ", ".join(f"{k}={v}" for k, v in feitos.items()) + f" · registro: {reg}")
    movidos = sum(1 for l in sel if l["tipo"] == "arquivo")
    print(f"    Arquivos no lote: {movidos} · conferir com as linhas do CSV (aceite da 4.5).")
    if lote != "a":
        vazias = sorted({os.path.dirname(l["origem"]) for l in sel if l["origem"]
                         and caminho_abs(raiz, os.path.dirname(l["origem"])).is_dir()
                         and not any(caminho_abs(raiz, os.path.dirname(l["origem"])).iterdir())})
        if vazias:
            print(f"    {len(vazias)} pasta(s) de origem ficaram vazias (não removidas):")
            for v in vazias[:20]:
                print("     -", v)
    return 1 if erros else 0


def limpar_vazias(raiz: Path, sim: bool) -> int:
    """D29: remove as pastas vazias das áreas antigas, só se não houver nenhum arquivo nelas."""
    presentes = [a for a in AREAS_ANTIGAS if caminho_abs(raiz, a).is_dir()]
    if not presentes:
        print("[OK] Nenhuma área antiga presente.")
        return 0
    arquivos, pastas = [], []
    for a in presentes:
        base = caminho_abs(raiz, a)
        for dp, dn, fn in os.walk(base):
            arquivos += [os.path.join(dp, n) for n in fn]
            pastas.append(dp)
    if arquivos:
        print(f"[PARE] {len(arquivos)} arquivo(s) ainda nas áreas antigas; nada foi removido:")
        for x in arquivos[:20]:
            print("    ", x)
        return 1
    pastas.sort(key=lambda p: (-p.count(os.sep), p))
    if not confirmar(f"Remover {len(pastas)} pasta(s) vazia(s) de {len(presentes)} área(s) antiga(s): "
                     f"{', '.join(presentes)}. Nenhum arquivo é removido.", sim):
        print("[CANCELADO] Nada foi feito.")
        return 1
    REGISTROS.mkdir(parents=True, exist_ok=True)
    reg = REGISTROS / f"registro_limpeza-vazias_{dt.datetime.now():%Y%m%d-%H%M%S}.csv"
    feitos, erros = Counter(), 0
    with open(reg, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=DELIM)
        w.writerow(["pasta", "situacao", "momento"])
        for p in pastas:
            rel = os.path.relpath(p.replace("\\\\?\\", ""), str(raiz)).replace(os.sep, "/") \
                if os.name == "nt" else os.path.relpath(p, str(raiz)).replace(os.sep, "/")
            sit = ""
            for tentativa in range(4):          # v1.2.1: bloqueio temporário (Drive) ou somente leitura
                try:
                    os.rmdir(p)
                    sit = "removida" if tentativa == 0 else f"removida (tentativa {tentativa + 1})"
                    break
                except FileNotFoundError:
                    sit = "ja-removida"
                    break
                except PermissionError as e:
                    sit = f"erro: {e}"
                    try:
                        os.chmod(p, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)   # tira o "somente leitura"
                    except OSError:
                        pass
                    time.sleep(2)
                except OSError as e:            # pasta não vazia ou outro erro: não insiste
                    sit = f"erro: {e}"
                    break
            if sit.startswith("erro"):
                erros += 1
                print(f"[AVISO] {rel}: {sit}")
            w.writerow([rel, sit, dt.datetime.now().isoformat(timespec="seconds")])
            f.flush()
            feitos[sit.split(" (")[0].split(":")[0]] += 1
    if erros:
        print(f"[PARCIAL] {erros} pasta(s) não removida(s); as pastas acima delas também ficam. "
              f"Espere o Drive sincronizar e rode --limpar-vazias de novo (é seguro repetir).")
    print(f"[{'OK' if not erros else 'PARCIAL'}] Limpeza: " +
          ", ".join(f"{k}={v}" for k, v in feitos.items()) + f" · registro: {reg}")
    return 1 if erros else 0


def reverter(raiz: Path, lote: str, verificar_hash: bool, sim: bool) -> int:
    regs = sorted(REGISTROS.glob(f"registro_lote-{lote}_*.csv"), reverse=True)
    if not regs:
        print(f"[PARE] Nenhum registro de execução do lote {lote} em {REGISTROS}")
        return 1
    ops = []
    for r in regs:
        with open(r, encoding="utf-8-sig", newline="") as f:
            ops += [(r, o) for o in reversed(list(csv.DictReader(f, delimiter=DELIM)))
                    if o["situacao"] == "ok"]
    if not confirmar(f"Reverter o lote {lote}: {len(ops)} operações de {len(regs)} registro(s).", sim):
        print("[CANCELADO] Nada foi feito.")
        return 1
    rev = REGISTROS / f"reversao_lote-{lote}_{dt.datetime.now():%Y%m%d-%H%M%S}.csv"
    erros = 0
    with open(rev, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=DELIM)
        w.writerow(["id", "origem_restaurada", "de", "situacao"])
        for _, o in ops:
            dst = caminho_abs(raiz, o["destino"])
            sit = "ok"
            try:
                if o["acao"] == "criar":
                    if dst.is_dir() and not any(dst.iterdir()):
                        dst.rmdir()       # só pasta vazia criada pelo próprio lote
                    else:
                        sit = "mantida (não vazia)"
                else:
                    src = caminho_abs(raiz, o["origem"])
                    if src.exists():
                        raise RuntimeError("origem já existe (não sobrescrevo)")
                    if o["tipo"] == "arquivo" and verificar_hash and o["sha256"] \
                            and sha256_arquivo(dst) != o["sha256"]:
                        raise RuntimeError("SHA-256 do destino mudou")
                    src.parent.mkdir(parents=True, exist_ok=True)
                    os.rename(dst, src)
                    # remove só as pastas intermediárias que ficaram vazias no destino
                    pai, base = dst.parent, caminho_abs(raiz, ".")
                    while pai != base and base in pai.parents and pai.is_dir() \
                            and not any(pai.iterdir()):
                        pai.rmdir()
                        pai = pai.parent
            except Exception as e:
                sit = f"erro: {e}"
                erros += 1
            w.writerow([o["id"], o["origem"], o["destino"], sit])
            if erros:
                print(f"[PARE] Erro na linha {o['id']}: {sit}")
                break
    if not erros:
        for r in regs:
            r.rename(r.with_suffix(".csv.revertido"))
    print(f"[{'OK' if not erros else 'PARCIAL'}] Reversão do lote {lote} · registro: {rev}")
    return 1 if erros else 0


# --------------------------------------------------------------------------- #
# Interface
# --------------------------------------------------------------------------- #

def main() -> int:
    configurar_saida()
    ap = argparse.ArgumentParser(description="Reorganização da pasta CGOV (Fase 4).")
    modo = ap.add_mutually_exclusive_group(required=True)
    modo.add_argument("--planejar", action="store_true", help="gera o mapa CSV (somente leitura)")
    modo.add_argument("--simular", action="store_true", help="confere o mapa (somente leitura)")
    modo.add_argument("--executar", action="store_true", help="executa um lote")
    modo.add_argument("--reverter", action="store_true", help="desfaz um lote")
    modo.add_argument("--limpar-vazias", action="store_true",
                      help="remove só pastas vazias das áreas antigas (D29)")
    ap.add_argument("--lote", choices=sorted(LOTES), help="lote a–g")
    ap.add_argument("--raiz", help="pasta CGOV (ou CGOV_RAIZ no .env)")
    ap.add_argument("--mapa", default=str(MAPA_PADRAO), help="caminho do mapa CSV")
    ap.add_argument("--cache", default=str(CACHE_PADRAO), help="cache de SHA-256")
    ap.add_argument("--decisoes", default=str(DECISOES_PADRAO),
                    help="decisões da 4.2 (origem;acao;destino;motivo), se existir")
    ap.add_argument("--apelidos", default=str(APELIDOS_PADRAO),
                    help="apelidos de processo da 4.2 (processo;apelido), se existir")
    ap.add_argument("--data-quarentena", default=f"{dt.date.today():%Y-%m-%d}",
                    help="data da pasta _a-excluir_ (AAAA-MM-DD)")
    ap.add_argument("--limite-segundos", type=int, default=0,
                    help="interrompe o cálculo de hashes após N segundos (retomável)")
    ap.add_argument("--comprimento-raiz-windows", type=int,
                    help="nº de caracteres da pasta CGOV no Windows (padrão: o da --raiz)")
    ap.add_argument("--verificar-hash", action="store_true",
                    help="--simular: recalcula o SHA-256 de cada origem")
    ap.add_argument("--sem-verificar-hash", action="store_true",
                    help="--executar/--reverter: não recalcula o SHA-256 antes de mover")
    ap.add_argument("--sim", action="store_true", help="não pede confirmação digitada")
    ap.add_argument("--detalhar", action="store_true", help="--simular: lista cada operação")
    a = ap.parse_args()

    if (a.executar or a.reverter) and not a.lote:
        ap.error("--executar e --reverter exigem --lote")
    raiz = resolver_raiz(a.raiz)
    raiz_len = a.comprimento_raiz_windows or len(str(raiz))
    mapa = Path(a.mapa)

    if a.planejar:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.data_quarentena):
            ap.error("--data-quarentena deve ser AAAA-MM-DD")
        decisoes = ler_tabela(Path(a.decisoes), ["origem", "acao", "destino", "motivo"])
        apelidos = {l["processo"].strip(): l["apelido"].strip()
                    for l in ler_tabela(Path(a.apelidos), ["processo", "apelido"])}
        if decisoes or apelidos:
            print(f"[OK] Decisões da 4.2: {len(decisoes)} linha(s); apelidos: {len(apelidos)}")
        pl = Planejador(raiz, a.data_quarentena, CacheHash(Path(a.cache)), a.limite_segundos,
                        decisoes, apelidos)
        if not pl.inventariar():
            return 3
        linhas = pl.planejar()
        for novo, n in sorted(getattr(pl, "encurtados", {}).items()):
            print(f"[OK] D26: {n} destino(s) encurtado(s) para {novo}")
        n_arq = sum(1 for l in linhas if l["tipo"] == "arquivo")
        if n_arq != len(pl.arquivos):
            print(f"[ERRO] Cobertura incompleta: {n_arq} linhas × {len(pl.arquivos)} arquivos")
            return 1
        gravar_mapa(mapa, linhas)
        txt = resumo(linhas, raiz_len, pl)
        arq_resumo = mapa.with_name(mapa.stem + "_resumo.md")
        arq_resumo.write_text(txt, encoding="utf-8")
        print(f"[OK] Mapa: {mapa} ({len(linhas)} linhas; cobertura {n_arq}/{len(pl.arquivos)} "
              f"arquivos = 100%)")
        print(f"[OK] Resumo: {arq_resumo}")
        return 0

    if a.limpar_vazias:
        return limpar_vazias(raiz, a.sim)

    linhas = ler_mapa(mapa)
    if a.simular:
        conflitos, avisos = conferir(linhas, raiz, a.lote, raiz_len, a.verificar_hash)
        sel = [l for l in linhas if a.lote is None or l["lote"] == a.lote]
        print(f"Simulação {'do lote ' + a.lote if a.lote else 'de todos os lotes'}: "
              f"{len(sel)} operações · " +
              ", ".join(f"{k}={v}" for k, v in Counter(l["acao"] for l in sel).items()))
        if a.detalhar:
            for l in sel:
                print(f"  {l['id']} [{l['lote']}] {l['acao']:<10} {l['origem'] or '—'} -> {l['destino']}")
        for x in avisos[:30]:
            print("  [AVISO]", x)
        if conflitos:
            print(f"[CONFLITOS] {len(conflitos)}:")
            for c in conflitos[:200]:
                print("   ", c)
            if len(conflitos) > 200:
                print(f"    … e mais {len(conflitos) - 200}")
            return 1
        print("[OK] Zero conflitos.")
        return 0
    if a.executar:
        return executar(linhas, raiz, a.lote, raiz_len, not a.sem_verificar_hash, a.sim)
    return reverter(raiz, a.lote, not a.sem_verificar_hash, a.sim)


if __name__ == "__main__":
    sys.exit(main())

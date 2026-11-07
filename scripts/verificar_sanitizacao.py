#!/usr/bin/env python3
"""verificar_sanitizacao.py — verificação de sanitização do repositório cgov-geral.

Versão 0.1.1 (06/11/2026; Fase 5, bloco 1 do plano de implantação, D37).

O que verifica (regra 4 do projeto "Escritório CGOV — Implantação"; CLAUDE.md; ADR-007):
nada de dados pessoais, matrículas, documentos SEI, caminhos pessoais ou cópias de
fontes não redistribuíveis no que pode ir para o Git.

Escopo padrão: todos os arquivos rastreados pelo Git mais os não rastreados que não
estão no .gitignore (ou seja, tudo o que poderia entrar num commit). `local/` fica de
fora porque é ignorado.

Severidades
  ERRO   bloqueia o commit (código de saída 1):
         CAMINHO_PESSOAL, EMAIL, CPF, MATRICULA, SEGREDO, TERMO_LOCAL, ARQUIVO_PROIBIDO
  AVISO  exige olhar humano, mas não bloqueia (salvo --estrito):
         PROCESSO_SEI, DOCUMENTO_SEI, TELEFONE, UNIDADE_ABSOLUTA

Configuração local (fora do Git, em local/):
  local/sanitizacao_termos.txt      um termo pessoal por linha (nomes, matrículas,
                                    usuário do Windows...); cada ocorrência vira ERRO.
                                    O nome do usuário do sistema (USERNAME/USER) entra
                                    automaticamente.
  local/sanitizacao_permitidos.txt  exceções locais (mesmo formato do arquivo abaixo).
Exceções versionadas (sem dados pessoais): scripts/sanitizacao_permitidos.txt, uma por
linha: <regex> (casa com o valor encontrado) ou <caminho-glob>::<regex>; # comenta.
Exceção pontual: uma linha que contenha o marcador "sanitizacao:ok" é ignorada.

Uso (Windows, na raiz do repositório):
  py scripts\\verificar_sanitizacao.py                 # árvore de trabalho
  py scripts\\verificar_sanitizacao.py --staged        # só o que está no índice (antes do commit)
  py scripts\\verificar_sanitizacao.py docs operacao   # só essas pastas
  py scripts\\verificar_sanitizacao.py --resumo        # contagem por arquivo
  py scripts\\verificar_sanitizacao.py --mostrar       # sem mascarar os valores

Saída: 0 = sem erros; 1 = há erros (ou avisos, com --estrito); 2 = falha de execução.
Sem caminhos pessoais neste arquivo (regra de sanitização).
"""
from __future__ import annotations

import argparse
import fnmatch
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

VERSAO = "0.1.1"
MARCADOR_OK = "sanitizacao:ok"
ARQ_PERMITIDOS = "scripts/sanitizacao_permitidos.txt"

EXT_PROIBIDAS = {
    ".pdf", ".doc", ".docx", ".odt", ".rtf", ".xls", ".xlsx", ".ods", ".ppt", ".pptx",
    ".msg", ".eml", ".pbix", ".zip", ".7z", ".rar",
}
NOMES_PROIBIDOS = {".env"}

# Usuários genéricos que não identificam pessoa
USUARIOS_GENERICOS = {
    "public", "default", "all users", "usuario", "user", "root", "admin", "administrator",
    "runner", "claude", "nome", "seu-usuario",
}
EMAILS_PERMITIDOS = [
    r"noreply@anthropic\.com",
    r"[^@\s]+@(?:example|exemplo)\.(?:com|org|net|gov\.br)",
    r"[^@\s]*<[^>]*>[^@\s]*@.*",  # placeholders <usuario>@...
]


@dataclass
class Regra:
    codigo: str
    severidade: str  # "ERRO" | "AVISO"
    padrao: re.Pattern
    grupo_usuario: int | None = None  # grupo que contém o nome de usuário (caminhos)
    validar: object = None


def _processo_real(txt: str) -> bool:
    """Ignora modelos como 02070.000000/0000-00 (sequencial, ano e DV zerados)."""
    return not re.fullmatch(r"\d{5}\.0{6}/0{4}-0{2}", txt)


def _cpf_valido(txt: str) -> bool:
    d = [int(c) for c in txt if c.isdigit()]
    if len(d) != 11 or len(set(d)) == 1:
        return False
    for n in (9, 10):
        s = sum(d[i] * (n + 1 - i) for i in range(n))
        dv = (s * 10) % 11 % 10
        if dv != d[n]:
            return False
    return True


REGRAS: list[Regra] = [
    Regra("CAMINHO_PESSOAL", "ERRO",
          re.compile(r"\b[A-Za-z]:[\\/]+Users[\\/]+([^\\/\s`\"'<>|*?%$]+)", re.I), 1),
    Regra("CAMINHO_PESSOAL", "ERRO",
          re.compile(r"/mnt/[a-z]/Users/([^/\s`\"'<>$]+)", re.I), 1),
    Regra("CAMINHO_PESSOAL", "ERRO",
          re.compile(r"(?<![\w.~:-])/(?:home|Users)/([A-Za-z0-9._-]+)"), 1),
    Regra("CAMINHO_PESSOAL", "ERRO",
          re.compile(r"(?<![\w.-])/sessions/[A-Za-z0-9._-]+"), None),
    Regra("EMAIL", "ERRO",
          re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    Regra("CPF", "ERRO",
          re.compile(r"(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)"), validar=_cpf_valido),
    Regra("MATRICULA", "ERRO",
          re.compile(r"\b(?:matr[íi]cula|siape)\b[^\n\d]{0,25}\d{5,8}\b", re.I)),
    Regra("SEGREDO", "ERRO",
          re.compile(r"\b(?:ghp|gho|ghs|github_pat)_[A-Za-z0-9_]{20,}|\bsk-ant-[A-Za-z0-9_-]{20,}"
                     r"|\bAKIA[0-9A-Z]{16}\b|-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    Regra("PROCESSO_SEI", "AVISO",
          re.compile(r"(?<!\d)\d{5}\.\d{6}/\d{4}-\d{2}(?!\d)"), validar=_processo_real),
    Regra("DOCUMENTO_SEI", "AVISO",
          re.compile(r"\bSEI\s*(?:n\.?\s*[º°o]?|n[º°o]\.?)?\s*:?\s*\d{7,9}\b", re.I)),
    Regra("TELEFONE", "AVISO",
          re.compile(r"\(\d{2}\)\s?9?\d{4}-\d{4}\b")),
    Regra("UNIDADE_ABSOLUTA", "AVISO",
          re.compile(r"(?<![\w\\/])[D-Zd-z]:\\")),
]


@dataclass
class Achado:
    arquivo: str
    linha: int
    codigo: str
    severidade: str
    valor: str
    contexto: str


# ---------------------------------------------------------------- utilidades
def git(*args: str, raiz: Path) -> str:
    r = subprocess.run(["git", *args], cwd=raiz, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.decode('utf-8', 'replace').strip()}")
    return r.stdout.decode("utf-8", "replace")


def raiz_repositorio() -> Path:
    aqui = Path(__file__).resolve().parent
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=aqui,
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError("não estou dentro de um repositório Git")
    return Path(out.stdout.strip())


def listar_arquivos(raiz: Path, staged: bool, filtros: list[str]) -> list[str]:
    if staged:
        nomes = git("-c", "core.quotepath=off", "diff", "--cached", "--name-only",
                    "--diff-filter=ACMR", "-z", raiz=raiz).split("\0")
    else:
        nomes = git("-c", "core.quotepath=off", "ls-files", "-z", "--cached", "--others",
                    "--exclude-standard", raiz=raiz).split("\0")
    nomes = sorted({n for n in nomes if n})
    if filtros:
        fs = [f.replace("\\", "/").strip("/") for f in filtros]
        nomes = [n for n in nomes if any(n == f or n.startswith(f + "/") for f in fs)]
    return nomes


def ler(raiz: Path, nome: str, staged: bool) -> bytes | None:
    if staged:
        r = subprocess.run(["git", "show", f":{nome}"], cwd=raiz, capture_output=True)
        return r.stdout if r.returncode == 0 else None
    p = raiz / nome
    if not p.is_file():
        return None  # removido da árvore, mas ainda no índice
    return p.read_bytes()


def carregar_lista(p: Path) -> list[str]:
    if not p.is_file():
        return []
    linhas = p.read_text(encoding="utf-8-sig").splitlines()
    return [l.strip() for l in linhas if l.strip() and not l.strip().startswith("#")]


def mascarar(v: str) -> str:
    if len(v) <= 6:
        return v[:2] + "…"
    return v[: max(4, len(v) // 3)] + "…" + f"({len(v)})"


# ---------------------------------------------------------------- verificação
def verificar(raiz: Path, nomes: list[str], staged: bool, termos: list[str],
              permitidos: list[tuple[str | None, re.Pattern]]) -> list[Achado]:
    achados: list[Achado] = []
    termos_re = [re.compile(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", re.I)
                 for t in termos]
    emails_ok = [re.compile(e, re.I) for e in EMAILS_PERMITIDOS]

    def permitido(arquivo: str, valor: str) -> bool:
        for glob, rx in permitidos:
            if glob and not fnmatch.fnmatch(arquivo, glob):
                continue
            if rx.search(valor):
                return True
        return False

    for nome in nomes:
        if nome == ARQ_PERMITIDOS:
            continue  # o próprio arquivo de exceções contém os padrões que exceptua
        base = nome.rsplit("/", 1)[-1]
        ext = os.path.splitext(base)[1].lower()
        if ext in EXT_PROIBIDAS or base in NOMES_PROIBIDOS:
            if not permitido(nome, nome):
                achados.append(Achado(nome, 0, "ARQUIVO_PROIBIDO", "ERRO", base,
                                      f"tipo {ext or base} não pode ir para o Git"))
            continue
        dados = ler(raiz, nome, staged)
        if dados is None:
            continue
        if b"\0" in dados[:8192]:
            achados.append(Achado(nome, 0, "ARQUIVO_PROIBIDO", "AVISO", base,
                                  "arquivo binário: conferir se pode ir para o Git"))
            continue
        texto = dados.decode("utf-8", "replace")
        for i, linha in enumerate(texto.splitlines(), 1):
            if MARCADOR_OK in linha:
                continue
            trechos_caminho: list[tuple[int, int]] = []
            for regra in REGRAS:
                for m in regra.padrao.finditer(linha):
                    valor = m.group(0)
                    if regra.grupo_usuario is not None:
                        usuario = m.group(regra.grupo_usuario).strip().lower()
                        if usuario in USUARIOS_GENERICOS or usuario.startswith(("<", "…", "...")):
                            continue
                    if regra.validar and not regra.validar(valor):
                        continue
                    if regra.codigo == "EMAIL" and any(e.fullmatch(valor) for e in emails_ok):
                        continue
                    if permitido(nome, valor):
                        continue
                    if regra.codigo == "CAMINHO_PESSOAL":
                        trechos_caminho.append(m.span())
                    achados.append(Achado(nome, i, regra.codigo, regra.severidade, valor,
                                          linha.strip()))
            for rx in termos_re:
                for m in rx.finditer(linha):
                    if permitido(nome, m.group(0)):
                        continue
                    if any(a <= m.start() and m.end() <= b for a, b in trechos_caminho):
                        continue  # já relatado como CAMINHO_PESSOAL
                    achados.append(Achado(nome, i, "TERMO_LOCAL", "ERRO", m.group(0),
                                          linha.strip()))
    # um mesmo trecho pode casar com duas regras de caminho: deduplicar
    vistos, unicos = set(), []
    for a in achados:
        chave = (a.arquivo, a.linha, a.codigo, a.valor)
        if chave not in vistos:
            vistos.add(chave)
            unicos.append(a)
    return unicos


# ---------------------------------------------------------------- saída
def main(argv: list[str] | None = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # console do Windows
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Verificação de sanitização do cgov-geral")
    ap.add_argument("caminhos", nargs="*", help="pastas ou arquivos (padrão: repositório inteiro)")
    ap.add_argument("--staged", action="store_true", help="verificar só o conteúdo do índice")
    ap.add_argument("--estrito", action="store_true", help="avisos também reprovam")
    ap.add_argument("--resumo", action="store_true", help="só a contagem por arquivo e regra")
    ap.add_argument("--mostrar", action="store_true", help="não mascarar os valores encontrados")
    ap.add_argument("--version", action="version", version=VERSAO)
    a = ap.parse_args(argv)

    try:
        raiz = raiz_repositorio()
        nomes = listar_arquivos(raiz, a.staged, a.caminhos)
    except RuntimeError as e:
        print(f"falha: {e}", file=sys.stderr)
        return 2

    termos = carregar_lista(raiz / "local" / "sanitizacao_termos.txt")
    usuario = (os.environ.get("USERNAME") or os.environ.get("USER") or "").strip()
    if len(usuario) >= 3 and usuario.lower() not in USUARIOS_GENERICOS:
        termos.append(usuario)
    termos = sorted({t for t in termos if len(t) >= 3}, key=str.lower)
    permitidos: list[tuple[str | None, re.Pattern]] = []
    for l in (carregar_lista(raiz / ARQ_PERMITIDOS)
              + carregar_lista(raiz / "local" / "sanitizacao_permitidos.txt")):
        glob, _, rx = l.rpartition("::") if "::" in l else ("", "", l)
        try:
            permitidos.append((glob or None, re.compile(rx, re.I)))
        except re.error as e:
            print(f"falha: exceção inválida em sanitizacao_permitidos.txt ({l!r}): {e}",
                  file=sys.stderr)
            return 2

    achados = verificar(raiz, nomes, a.staged, termos, permitidos)
    erros = [x for x in achados if x.severidade == "ERRO"]
    avisos = [x for x in achados if x.severidade == "AVISO"]

    modo = "índice (--staged)" if a.staged else "árvore de trabalho"
    print(f"verificar_sanitizacao.py {VERSAO} — {modo}; {len(nomes)} arquivo(s); "
          f"{len(termos)} termo(s) local(is); {len(permitidos)} exceção(ões)")

    if a.resumo:
        cont: dict[tuple[str, str, str], int] = {}
        for x in achados:
            k = (x.arquivo, x.severidade, x.codigo)
            cont[k] = cont.get(k, 0) + 1
        for (arq, sev, cod), n in sorted(cont.items()):
            print(f"  {sev:5} {cod:17} {n:4}  {arq}")
    else:
        for x in sorted(achados, key=lambda y: (y.severidade != "ERRO", y.arquivo, y.linha)):
            valor = x.valor if a.mostrar else mascarar(x.valor)
            local = f"{x.arquivo}:{x.linha}" if x.linha else x.arquivo
            print(f"  {x.severidade:5} {x.codigo:17} {local}  [{valor}]")

    por_regra: dict[str, int] = {}
    for x in achados:
        por_regra[f"{x.severidade} {x.codigo}"] = por_regra.get(f"{x.severidade} {x.codigo}", 0) + 1
    if por_regra:
        print("Totais: " + "; ".join(f"{k}: {v}" for k, v in sorted(por_regra.items())))
    reprova = bool(erros) or (a.estrito and bool(avisos))
    print(f"Resultado: {'REPROVADO' if reprova else 'APROVADO'} "
          f"({len(erros)} erro(s), {len(avisos)} aviso(s))")
    return 1 if reprova else 0


if __name__ == "__main__":
    sys.exit(main())

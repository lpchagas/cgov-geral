#!/usr/bin/env python3
"""publicar_operacao.py — publica o commit atual (HEAD) do cgov-geral para a operação.

Versão 0.3.1 (09/11/2026; Fase 7, etapa 7.6a): com as 32 skills avulsas desativadas na conta, a seção 1 passa a exigir só
as 2 cgge-fgbio-* e a esperar o plugin sem avulsas (--sem-avulsas torna as avulsas divergência). A seção 1b passa a
comparar os SKILL.md do plugin instalado pelo nome, pela descrição e pelo corpo (como a seção 1), porque o Claude
regrava o cabeçalho; escolhe a geração mais recente (~gN) do plugin sincronizado. Versão 0.3.0 (09/11/2026; Fase 7, etapa 7.3). A 0.1.0 (07/11/2026; Fase 5, etapa 5.3) substituiu
scripts/publicar-operacao.sh, do WSL e da estrutura anterior à Fase 4. Desde a 0.3.0 as 32 skills do plugin
ficam em plugins/cgov-escritorio/skills/ (7.1) e o script gera o zip do plugin; as 2 cgge-fgbio-* seguem em skills/.

Modos
  --verificar            somente leitura:
                           1. skills avulsas instaladas na conta (~/.claude/skills/synced) x fonte (HEAD: skills/, as
                              cgge-fgbio-*); as 32 do plugin não devem estar como avulsas (aviso; com --sem-avulsas, divergência);
                           1b. plugin cgov-escritorio instalado na conta (~/.claude/plugins/synced) x fonte (HEAD);
                           2. operacao/ (HEAD) x pasta CGOV, por SHA-256 (etapa 5.5);
                           3. docs/ (HEAD) x 90_escritorio-virtual/referencia/docs (pendência P3).
  --sem-avulsas          com --verificar: as skills do plugin que ainda estiverem como avulsas na conta viram divergência
                         (usar depois da exclusão, etapa 7.6b)
  --publicar             simulação da publicação (nada é gravado):
                           a. zip do plugin em dist/cgov-escritorio-<versão>.zip (Customize -> Plugins -> Upload);
                           b. pacotes das skills avulsas (skills/cgge-fgbio) em dist/skills/<commit>/;
                           c. operacao/ -> raiz da pasta CGOV (só o que difere);
                           d. docs/ -> 90_escritorio-virtual/referencia/docs + LEIA-ME.md.
  --publicar --executar  grava. O que for substituído na pasta CGOV vai antes para
                         99_arquivo/_a-excluir_<data>/publicacao_<commit>/ (nada é excluído);
                         depois, confere por SHA-256 tudo o que foi gravado.

Publica só o que está em commit: alterações pendentes em skills/, plugins/, docs/ ou operacao/ bloqueiam.
Nada é excluído: zips antigos em dist/ só são listados (o runbook manda manter os três mais recentes).
Pastas: CGOV_RAIZ e CGOV_ESCRITORIO no .env (CGOV_ESCRITORIO padrão: CGOV_RAIZ/90_escritorio-virtual).
Uso (Windows, na raiz do repositório):  py scripts\\publicar_operacao.py --verificar
Saída: 0 = ok (ou nada divergente); 1 = divergências ou [PARE]; 2 = erro.
Sem caminhos pessoais neste arquivo (regra de sanitização).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

VERSAO = "0.3.1"
REPO = Path(__file__).resolve().parent.parent
URL_FONTE = "https://github.com/lpchagas/cgov-geral"
PASTA_SYNC = Path.home() / ".claude" / "skills" / "synced"
PASTA_PLUGIN_SYNC = Path.home() / ".claude" / "plugins" / "synced"
PLUGIN = "plugins/cgov-escritorio"
PLUGIN_NOME = "cgov-escritorio"
MANIFESTO = f"{PLUGIN}/.claude-plugin/plugin.json"
FONTES_SKILLS = (f"{PLUGIN}/skills/", "skills/")  # plugin (32) e fora do plugin (cgge-fgbio)
MAX_DESCRICAO = 1024  # limite do Customize -> Skills
DIST = REPO / "dist"  # pacotes gerados (ignorado pelo Git)


class Pare(Exception):
    pass


# ---------------------------------------------------------------- utilidades
def git_bytes(*args: str) -> bytes:
    r = subprocess.run(["git", "-c", "core.quotepath=off", *args], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        raise Pare(f"git {' '.join(args)}: {r.stderr.decode('utf-8', 'replace').strip()}")
    return r.stdout


def git(*args: str) -> str:
    return git_bytes(*args).decode("utf-8", "replace")


def arquivos_head(prefixo: str) -> list[str]:
    nomes = git("ls-tree", "-r", "-z", "--name-only", "HEAD", "--", prefixo).split("\0")
    return sorted(n for n in nomes if n)


def arquivos_skills() -> list[str]:
    """Arquivos do HEAD de todas as fontes de skills (plugin e skills/)."""
    return sorted(f for raiz in FONTES_SKILLS for f in arquivos_head(raiz))


def blob(caminho: str) -> bytes:
    return git_bytes("show", f"HEAD:{caminho}")


def sha(dados: bytes) -> str:
    return hashlib.sha256(dados).hexdigest()


def sha_arquivo(p: Path) -> str | None:
    try:
        return sha(p.read_bytes())
    except OSError:
        return None


def ler_env() -> dict[str, str]:
    env: dict[str, str] = {}
    arq = REPO / ".env"
    if not arq.is_file():
        raise Pare(".env não encontrado na raiz do repositório (modelo: .env.example)")
    for linha in arq.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        linha = linha.strip()
        if linha and not linha.startswith("#") and "=" in linha:
            k, v = linha.split("=", 1)
            env[k.strip()] = os.path.expanduser(os.path.expandvars(v.strip().strip('"').strip("'")))
    return env


def pastas(env: dict[str, str]) -> tuple[Path, Path]:
    if not env.get("CGOV_RAIZ"):
        raise Pare("CGOV_RAIZ ausente no .env")
    raiz = Path(env["CGOV_RAIZ"])
    escr = Path(env.get("CGOV_ESCRITORIO") or raiz / "90_escritorio-virtual")
    for p in (raiz, escr):
        if not p.is_dir():
            raise Pare(f"pasta não encontrada: {p}")
    return raiz, escr


def commit_atual() -> tuple[str, str]:
    curto = git("rev-parse", "--short", "HEAD").strip()
    data = git("log", "-1", "--format=%cd", "--date=format:%d/%m/%Y %H:%M").strip()
    return curto, data


# ---------------------------------------------------------------- 1. skills
def _partes(texto: str):
    texto = texto.replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n(.*)", texto, re.S)
    if not m:
        return None, texto.strip()
    try:
        import yaml  # opcional
        meta = yaml.safe_load(m.group(1))
        if isinstance(meta, dict):
            meta = {k: " ".join(str(meta.get(k) or "").split()) for k in ("name", "description")}
    except Exception:
        meta = "\n".join(l.rstrip() for l in m.group(1).splitlines())
    return meta, m.group(2).strip()


def verificar_skills(sem_avulsas: bool = False) -> int:
    print("== 1. Skills avulsas instaladas na conta x fonte (HEAD: skills/); plugin sem avulsas")
    if not PASTA_SYNC.is_dir() or not any(PASTA_SYNC.iterdir()):
        print(f"  [AVISO] {PASTA_SYNC} não encontrado: abra o Claude Code uma vez com a conta conectada")
        return 0
    sincs = sorted(p for p in PASTA_SYNC.iterdir() if p.is_dir())

    def instalada(nome: str):
        return next((s / nome / "SKILL.md" for s in sincs if (s / nome / "SKILL.md").is_file()), None)

    divergentes = []
    do_plugin = []
    for f in arquivos_skills():
        if not f.endswith("/SKILL.md") or "-workspace/" in f:
            continue
        nome = f.split("/")[-2]
        inst = instalada(nome)
        if f.startswith(f"{PLUGIN}/skills/"):  # vem do plugin: não deve existir como avulsa
            do_plugin.append(nome)
            if inst is not None:
                print(f"  {'AVULSA NA CONTA' if sem_avulsas else '[AVISO] avulsa na cache'}  {nome}")
                if sem_avulsas:
                    divergentes.append(nome)
            continue
        if inst is None:
            estado = "NÃO INSTALADA"
        else:
            fonte = blob(f).decode("utf-8", "replace")
            estado = "igual" if _partes(fonte) == _partes(inst.read_text(encoding="utf-8", errors="replace")) \
                else "DESATUALIZADA"
        if estado != "igual":
            divergentes.append(nome)
        print(f"  {estado:14} {nome}")
    na_cache = [n for n in do_plugin if instalada(n) is not None]
    print(f"  Skills do plugin ({len(do_plugin)}): {len(na_cache)} ainda como avulsa na cache local"
          f"{'' if sem_avulsas or not na_cache else ' (aviso: desativada pode continuar no disco; excluir na 7.6b)'}")
    print(f"  Reinstalar no Claude: {', '.join(d for d in divergentes if d not in do_plugin) or 'nenhuma'}"
          f"{'; excluir avulsas: ' + ', '.join(d for d in divergentes if d in do_plugin) if any(d in do_plugin for d in divergentes) else ''}")
    return len(divergentes)


# ---------------------------------------------------------------- plugin
def _meta(texto: str) -> dict[str, str]:
    """name e description do frontmatter (com yaml, se houver; senão, leitura simples)."""
    m = re.match(r"---\n(.*?)\n---\n", texto.replace("\r\n", "\n"), re.S)
    if not m:
        return {}
    try:
        import yaml  # opcional
        d = yaml.safe_load(m.group(1))
        if isinstance(d, dict):
            return {k: " ".join(str(d.get(k) or "").split()) for k in ("name", "description")}
    except Exception:
        pass
    saida: dict[str, str] = {}
    linhas = m.group(1).splitlines()
    for i, l in enumerate(linhas):
        for k in ("name", "description"):
            if l.startswith(k + ":"):
                v = l[len(k) + 1:].strip()
                if v in (">", "|", ">-", "|-", ">+", "|+"):
                    bloco = []
                    for l2 in linhas[i + 1:]:
                        if l2[:1] in (" ", "\t") or not l2.strip():
                            bloco.append(l2.strip())
                        else:
                            break
                    v = " ".join(x for x in bloco if x)
                saida[k] = " ".join(v.strip("\"'").split())
    return saida


def manifesto_plugin() -> dict:
    import json
    try:
        return json.loads(blob(MANIFESTO).decode("utf-8"))
    except Pare:
        raise Pare(f"{MANIFESTO} não está no HEAD (a etapa 7.1 precisa estar em commit)")
    except ValueError as e:
        raise Pare(f"{MANIFESTO} não é um JSON válido: {e}")


def validar_plugin(man: dict) -> list[str]:
    erros = []
    if man.get("name") != PLUGIN_NOME:
        erros.append(f"plugin.json: name deve ser {PLUGIN_NOME!r} (é {man.get('name')!r})")
    v = str(man.get("version") or "")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", v):
        erros.append(f"plugin.json: version ausente ou fora do padrão X.Y.Z (é {v!r})")
    skills = [f for f in arquivos_head(f"{PLUGIN}/skills/") if f.endswith("/SKILL.md") and f.count("/") == 4]
    if not skills:
        erros.append("nenhuma skill em plugins/cgov-escritorio/skills/")
    for f in skills:
        pasta = f.split("/")[-2]
        meta = _meta(blob(f).decode("utf-8", "replace"))
        if meta.get("name") != pasta:
            erros.append(f"{f}: name do frontmatter ({meta.get('name')!r}) difere da pasta")
        d = len(meta.get("description", ""))
        if d == 0 or d > MAX_DESCRICAO:
            erros.append(f"{f}: descrição com {d} caracteres (limite {MAX_DESCRICAO})")
    return erros


def arquivos_do_plugin() -> list[tuple[str, str]]:
    """(caminho no HEAD, caminho no zip). Fora: evals/ e pastas *-workspace."""
    saida = []
    for f in arquivos_head(f"{PLUGIN}/"):
        rel = f[len(PLUGIN) + 1:]
        partes = rel.split("/")
        if "evals" in partes[:-1] or any(x.endswith("-workspace") for x in partes[:-1]):
            continue
        saida.append((f, rel))
    return saida


def zip_plugin(executar: bool) -> int:
    man = manifesto_plugin()
    erros = validar_plugin(man)
    if erros:
        raise Pare("plugin inválido:\n  " + "\n  ".join(erros))
    versao = man["version"]
    arqs = arquivos_do_plugin()
    destino = DIST / f"{PLUGIN_NOME}-{versao}.zip"
    n_skills = sum(1 for _, r in arqs if r.startswith("skills/") and r.endswith("/SKILL.md") and r.count("/") == 2)
    n_cmds = sum(1 for _, r in arqs if r.startswith("commands/"))
    print(f"  plugin {PLUGIN_NOME} {versao}: {n_skills} skill(s), {n_cmds} comando(s), {len(arqs)} arquivo(s) (sem evals/)")
    print(f"  destino: {destino}")
    if destino.exists():
        if executar:
            raise Pare(f"{destino.name} já existe: aumente a version em {MANIFESTO}, faça o commit e publique de novo")
        print("  [AVISO] já existe; a execução vai parar até a version aumentar")
    if executar:
        data = git("log", "-1", "--format=%cd", "--date=format:%Y,%m,%d,%H,%M,%S").strip()
        dt_zip = tuple(int(x) for x in data.split(","))
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
            for f, rel in sorted(arqs, key=lambda x: x[1]):
                zi = zipfile.ZipInfo(rel, date_time=dt_zip)
                zi.compress_type = zipfile.ZIP_DEFLATED
                zi.external_attr = 0o644 << 16
                z.writestr(zi, blob(f))
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_bytes(buf.getvalue())
        h = sha(buf.getvalue())
        destino.with_name(destino.name + ".sha256").write_text(
            f"{h}  {destino.name}\ncommit {commit_atual()[0]}\n", encoding="utf-8")
        print(f"  gravado: {destino.name} ({len(buf.getvalue())} bytes); SHA-256 {h[:16]}…")
    antigos = sorted(destino.parent.glob(f"{PLUGIN_NOME}-*.zip"), key=lambda p: p.stat().st_mtime, reverse=True)[3:] \
        if destino.parent.is_dir() else []
    if antigos:
        print(f"  [AVISO] {len(antigos)} zip(s) além dos 3 mais recentes em dist/ (o script não apaga): "
              + ", ".join(a.name for a in antigos))
    return n_skills


def _geracao(pasta: Path) -> int:
    m = re.search(r"~g(\d+)$", pasta.name)
    return int(m.group(1)) if m else 1


def verificar_plugin() -> int:
    print("\n== 1b. Plugin instalado na conta x fonte (HEAD)")
    man = manifesto_plugin()
    achados = []
    if PASTA_PLUGIN_SYNC.is_dir():
        for padrao in (".claude-plugin/plugin.json", "*/.claude-plugin/plugin.json", "*/*/.claude-plugin/plugin.json"):
            for m in PASTA_PLUGIN_SYNC.glob(padrao):
                try:
                    import json
                    if json.loads(m.read_text(encoding="utf-8")).get("name") == PLUGIN_NOME:
                        achados.append(m.parent.parent)
                except (OSError, ValueError):
                    continue
    if not achados:
        print(f"  [AVISO] plugin {PLUGIN_NOME} não encontrado em {PASTA_PLUGIN_SYNC} (ainda não enviado na 7.5, "
              "ou sincronização desligada); local exato do plugin sincronizado a confirmar após o primeiro envio")
        return 0
    raiz = max(achados, key=lambda d: (_geracao(d), d.name))  # geração mais recente (~gN); sem sufixo = 1ª
    if len(achados) > 1:
        print(f"  {len(achados)} gerações do plugin na conta; usada: {raiz.name}")
    inst = json_versao(raiz / ".claude-plugin" / "plugin.json")
    print(f"  instalado: {inst or '?'} em {raiz}; fonte (HEAD): {man.get('version')}")
    divergentes = [] if inst == man.get("version") else [f"version ({inst} x {man.get('version')})"]
    for f in arquivos_head(f"{PLUGIN}/"):
        if "/evals/" in f or "-workspace/" in f:
            continue
        rel = f[len(PLUGIN) + 1:]
        alvo = raiz / rel
        if not alvo.is_file():
            divergentes.append(rel)
        elif rel.endswith("/SKILL.md"):  # o Claude regrava o cabeçalho: compara nome, descrição e corpo
            if _partes(blob(f).decode("utf-8", "replace")) != _partes(alvo.read_text(encoding="utf-8", errors="replace")):
                divergentes.append(rel)
        elif sha_arquivo(alvo) != sha(blob(f)):
            divergentes.append(rel)
    for d in divergentes[:20]:
        print(f"  DIVERGE  {d}")
    print(f"  {'sem divergências' if not divergentes else f'{len(divergentes)} divergência(s)'}")
    return len(divergentes)


def json_versao(caminho: Path) -> str | None:
    import json
    try:
        return json.loads(caminho.read_text(encoding="utf-8")).get("version")
    except (OSError, ValueError):
        return None


# ---------------------------------------------------------------- 2. operacao/
# Ferramentas do repositório publicadas na pasta CGOV (fonte única aqui; destino somente para execução)
FERRAMENTAS = {"scripts/gerar_indices.py": "90_escritorio-virtual/ferramentas/gerar_indices.py"}


def plano_operacao(raiz: Path) -> list[tuple[str, Path, str, bytes]]:
    saida = []
    pares = [(f, f[len("operacao/"):]) for f in arquivos_head("operacao/")]
    pares += list(FERRAMENTAS.items())
    for f, rel in pares:
        dados = blob(f)
        destino = raiz / rel
        atual = sha_arquivo(destino)
        estado = "igual" if atual == sha(dados) else ("AUSENTE" if atual is None else "DIFERENTE")
        saida.append((rel, destino, estado, dados))
    return saida


def verificar_operacao(raiz: Path) -> int:
    print("\n== 2. operacao/ (HEAD) x pasta CGOV (SHA-256)")
    plano = plano_operacao(raiz)
    for rel, _, estado, _ in plano:
        print(f"  {estado:10} {rel}")
    n = sum(1 for p in plano if p[2] != "igual")
    print(f"  {len(plano) - n}/{len(plano)} iguais ao publicado")
    return n


# ---------------------------------------------------------------- 3. referência de docs/
def plano_referencia(escr: Path):
    ref = escr / "referencia"
    docs_ref = ref / "docs"
    head = {f[len("docs/"):]: f for f in arquivos_head("docs/")}
    estados = {}
    for rel, f in head.items():
        atual = sha_arquivo(docs_ref / rel)
        estados[rel] = "igual" if atual == sha(blob(f)) else ("AUSENTE" if atual is None else "DIFERENTE")
    sobrando = []
    if docs_ref.is_dir():
        for p in sorted(docs_ref.rglob("*")):
            if p.is_file():
                rel = p.relative_to(docs_ref).as_posix()
                if rel not in head:
                    sobrando.append(rel)
    leia = ref / "LEIA-ME.md"
    commit_pub = "?"
    if leia.is_file():
        m = re.search(r"commit `([0-9a-f]{6,40})`", leia.read_text(encoding="utf-8", errors="replace"))
        commit_pub = m.group(1) if m else "?"
    return ref, docs_ref, head, estados, sobrando, commit_pub


def verificar_referencia(escr: Path) -> int:
    print("\n== 3. docs/ (HEAD) x 90_escritorio-virtual/referencia/docs")
    ref, docs_ref, head, estados, sobrando, commit_pub = plano_referencia(escr)
    if not docs_ref.is_dir():
        print(f"  [AVISO] referência ainda não publicada: {docs_ref}")
        return len(head)
    cont = {k: list(estados.values()).count(k) for k in ("igual", "DIFERENTE", "AUSENTE")}
    print(f"  commit publicado (LEIA-ME): {commit_pub}; HEAD: {commit_atual()[0]}")
    print(f"  iguais {cont['igual']}, diferentes {cont['DIFERENTE']}, ausentes {cont['AUSENTE']}, "
          f"só na referência {len(sobrando)}")
    for rel, e in estados.items():
        if e != "igual":
            print(f"    {e:10} {rel}")
    for rel in sobrando:
        print(f"    {'SOBRANDO':10} {rel}")
    return cont["DIFERENTE"] + cont["AUSENTE"] + len(sobrando)


# ---------------------------------------------------------------- publicação
def zips_skills(destino: Path, executar: bool) -> int:
    nomes = {}
    for f in arquivos_head("skills/"):
        partes = f.split("/")
        if len(partes) >= 4 and not partes[2].endswith("-workspace") and "evals" not in partes[3:-1] \
                and partes[3] != "evals":
            nomes.setdefault(partes[2], []).append(f)
    validas = {n: fs for n, fs in nomes.items() if f"skills/{fs[0].split('/')[1]}/{n}/SKILL.md" in fs}
    print(f"  {len(validas)} pacote(s) em {destino}")
    if executar:
        if destino.exists():
            raise Pare(f"{destino} já existe (pacotes deste commit já gerados)")
        destino.mkdir(parents=True)
        for nome, fs in sorted(validas.items()):
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
                for f in sorted(fs):
                    base = "/".join(f.split("/")[:3])
                    z.writestr(f"{nome}/{f[len(base) + 1:]}", blob(f))
            (destino / f"{nome}.zip").write_bytes(buf.getvalue())
    return len(validas)


def quarentenar(origem: Path, quarentena: Path, rel: str, executar: bool, log: list[str]) -> None:
    alvo = quarentena / rel
    log.append(f"  quarentena  {rel}")
    if executar:
        if alvo.exists():
            raise Pare(f"destino na quarentena já existe: {alvo}")
        alvo.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(origem), str(alvo))


def publicar(executar: bool) -> int:
    env = ler_env()
    raiz, escr = pastas(env)
    pend = git("status", "--porcelain", "--", "skills", "plugins", "docs", "operacao").strip()
    if pend:
        raise Pare("há alterações sem commit em skills/, plugins/, docs/ ou operacao/: faça o commit antes de publicar")
    commit, data = commit_atual()
    hoje = dt.date.today().isoformat()
    quarentena = raiz / "99_arquivo" / f"_a-excluir_{hoje}" / f"publicacao_{commit}"
    print(f"== Publicação do commit {commit} ({'EXECUÇÃO' if executar else 'SIMULAÇÃO: nada será gravado'})")
    print(f"  quarentena desta publicação: {quarentena}")
    gravados: list[tuple[Path, bytes]] = []
    log: list[str] = []

    print("\n== a. Zip do plugin (Customize -> Plugins -> Upload plugin)")
    zip_plugin(executar)

    print("\n== b. Pacotes das skills avulsas (skills/: cgge-fgbio)")
    zips_skills(DIST / "skills" / commit, executar)

    print("\n== c. operacao/ -> pasta CGOV")
    for rel, destino, estado, dados in plano_operacao(raiz):
        if estado == "igual":
            continue
        if estado == "DIFERENTE":
            quarentenar(destino, quarentena / "operacao", rel, executar, log)
        log.append(f"  {'substituir' if estado == 'DIFERENTE' else 'criar':10}  {rel}")
        gravados.append((destino, dados))
    print("\n".join(log) if log else "  nada a publicar (tudo igual)")

    print("\n== d. docs/ -> referência")
    ref, docs_ref, head, estados, sobrando, commit_pub = plano_referencia(escr)
    muda = sobrando or any(e != "igual" for e in estados.values())
    if not muda:
        print("  referência já igual ao HEAD")
    else:
        print(f"  substituir a referência (publicada: {commit_pub}) pela do commit {commit}: "
              f"{len(head)} arquivo(s); a anterior vai para a quarentena")
        if executar:
            for nome in ("docs", "LEIA-ME.md"):
                if (ref / nome).exists():
                    quarentenar(ref / nome, quarentena / "referencia", nome, True, [])
        for rel, f in head.items():
            gravados.append((docs_ref / rel, blob(f)))
        leia = (f"# Referência publicada do cgov-geral — somente leitura\n\n"
                f"- Versão: commit `{commit}` ({data})\n- Fonte: {URL_FONTE}\n"
                f"- Gerada por `scripts/publicar_operacao.py` {VERSAO}; cada publicação substitui todo o\n"
                f"  conteúdo, e a versão anterior vai para `99_arquivo/_a-excluir_<data>/`.\n\n"
                f"Não edite estes arquivos: as alterações se perdem na próxima publicação.\n"
                f"Correções vão para o fluxo de desenvolvimento (ver `docs/fluxos-de-trabalho.md`).\n")
        gravados.append((ref / "LEIA-ME.md", leia.encode("utf-8")))

    if not executar:
        print(f"\nResultado: SIMULAÇÃO — {len(gravados)} arquivo(s) seriam gravados. "
              f"Para aplicar: py scripts\\publicar_operacao.py --publicar --executar")
        return 0

    print("\n== Gravação e conferência (SHA-256)")
    for destino, dados in gravados:
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_bytes(dados)
    erros = [d for d, dados in gravados if sha_arquivo(d) != sha(dados)]
    for d in erros:
        print(f"  ERRO  {d}")
    print(f"  {len(gravados) - len(erros)}/{len(gravados)} conferidos")
    print("\nPlugin: antes do envio, rode `claude plugin validate .\\plugins\\cgov-escritorio`; depois, Claude -> "
          "Customize -> Plugins -> Add -> Upload plugin -> dist\\cgov-escritorio-<versão>.zip; depois, --verificar.")
    print("Skills avulsas (cgge-fgbio): Customize -> Skills -> enviar "
          f"dist\\skills\\{commit}\\<skill>.zip (substituir); depois, --verificar.")
    return 1 if erros else 0


# ---------------------------------------------------------------- principal
def main(argv: list[str] | None = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Publicação do cgov-geral para a operação")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--verificar", action="store_true", help="comparações somente leitura")
    g.add_argument("--publicar", action="store_true", help="publicação (simulação sem --executar)")
    ap.add_argument("--executar", action="store_true", help="com --publicar: gravar de fato")
    ap.add_argument("--sem-avulsas", action="store_true",
                    help="com --verificar: skills do plugin ainda instaladas como avulsas viram divergência (7.6b)")
    ap.add_argument("--version", action="version", version=VERSAO)
    a = ap.parse_args(argv)
    if a.executar and not a.publicar:
        ap.error("--executar só vale com --publicar")
    if a.sem_avulsas and a.publicar:
        ap.error("--sem-avulsas só vale com --verificar")
    print(f"publicar_operacao.py {VERSAO} — HEAD {commit_atual()[0]}")
    try:
        if a.publicar:
            return publicar(a.executar)
        env = ler_env()
        raiz, escr = pastas(env)
        n = verificar_skills(a.sem_avulsas) + verificar_plugin() + verificar_operacao(raiz) + verificar_referencia(escr)
        print(f"\nResultado: {'sem divergências' if not n else f'{n} divergência(s) — ver acima'}")
        return 0 if not n else 1
    except Pare as e:
        print(f"\n[PARE] {e}")
        return 1
    except OSError as e:
        print(f"\nerro: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

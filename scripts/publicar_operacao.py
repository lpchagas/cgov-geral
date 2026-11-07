#!/usr/bin/env python3
"""publicar_operacao.py — publica o commit atual (HEAD) do cgov-geral para a operação.

Versão 0.1.0 (07/11/2026; Fase 5, bloco 4, etapa 5.3 do plano de implantação; substitui
scripts/publicar-operacao.sh, do WSL e da estrutura anterior à Fase 4).

Modos
  --verificar            somente leitura:
                           1. skills instaladas na conta (~/.claude/skills/synced) x fonte (HEAD);
                           2. operacao/ (HEAD) x pasta CGOV, por SHA-256 (etapa 5.5);
                           3. docs/ (HEAD) x 90_escritorio-virtual/referencia/docs (pendência P3).
  --publicar             simulação da publicação (nada é gravado):
                           a. pacotes das skills em dist/skills/<commit>/ (para Customize -> Skills);
                           b. operacao/ -> raiz da pasta CGOV (só o que difere);
                           c. docs/ -> 90_escritorio-virtual/referencia/docs + LEIA-ME.md.
  --publicar --executar  grava. O que for substituído na pasta CGOV vai antes para
                         99_arquivo/_a-excluir_<data>/publicacao_<commit>/ (nada é excluído);
                         depois, confere por SHA-256 tudo o que foi gravado.

Publica só o que está em commit: alterações pendentes em skills/, docs/ ou operacao/ bloqueiam.
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

VERSAO = "0.2.0"
REPO = Path(__file__).resolve().parent.parent
URL_FONTE = "https://github.com/lpchagas/cgov-geral"
PASTA_SYNC = Path.home() / ".claude" / "skills" / "synced"


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


def verificar_skills() -> int:
    print("== 1. Skills instaladas na conta x fonte (HEAD)")
    if not PASTA_SYNC.is_dir() or not any(PASTA_SYNC.iterdir()):
        print(f"  [AVISO] {PASTA_SYNC} não encontrado: abra o Claude Code uma vez com a conta conectada")
        return 0
    sincs = sorted(p for p in PASTA_SYNC.iterdir() if p.is_dir())
    divergentes = []
    for f in arquivos_head("skills/"):
        if not f.endswith("/SKILL.md") or "-workspace/" in f:
            continue
        nome = f.split("/")[-2]
        inst = next((s / nome / "SKILL.md" for s in sincs if (s / nome / "SKILL.md").is_file()), None)
        if inst is None:
            estado = "NÃO INSTALADA"
        else:
            fonte = blob(f).decode("utf-8", "replace")
            estado = "igual" if _partes(fonte) == _partes(inst.read_text(encoding="utf-8", errors="replace")) \
                else "DESATUALIZADA"
        if estado != "igual":
            divergentes.append(nome)
        print(f"  {estado:14} {nome}")
    print(f"  Reinstalar no Claude: {', '.join(divergentes) if divergentes else 'nenhuma'}")
    return len(divergentes)


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
    pend = git("status", "--porcelain", "--", "skills", "docs", "operacao").strip()
    if pend:
        raise Pare("há alterações sem commit em skills/, docs/ ou operacao/: faça o commit antes de publicar")
    commit, data = commit_atual()
    hoje = dt.date.today().isoformat()
    quarentena = raiz / "99_arquivo" / f"_a-excluir_{hoje}" / f"publicacao_{commit}"
    print(f"== Publicação do commit {commit} ({'EXECUÇÃO' if executar else 'SIMULAÇÃO: nada será gravado'})")
    print(f"  quarentena desta publicação: {quarentena}")
    gravados: list[tuple[Path, bytes]] = []
    log: list[str] = []

    print("\n== a. Pacotes das skills")
    zips_skills(REPO / "dist" / "skills" / commit, executar)

    print("\n== b. operacao/ -> pasta CGOV")
    for rel, destino, estado, dados in plano_operacao(raiz):
        if estado == "igual":
            continue
        if estado == "DIFERENTE":
            quarentenar(destino, quarentena / "operacao", rel, executar, log)
        log.append(f"  {'substituir' if estado == 'DIFERENTE' else 'criar':10}  {rel}")
        gravados.append((destino, dados))
    print("\n".join(log) if log else "  nada a publicar (tudo igual)")

    print("\n== c. docs/ -> referência")
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
    print("\nPara cada skill a reinstalar: Claude -> Customize -> Skills -> enviar "
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
    ap.add_argument("--version", action="version", version=VERSAO)
    a = ap.parse_args(argv)
    if a.executar and not a.publicar:
        ap.error("--executar só vale com --publicar")
    print(f"publicar_operacao.py {VERSAO} — HEAD {commit_atual()[0]}")
    try:
        if a.publicar:
            return publicar(a.executar)
        env = ler_env()
        raiz, escr = pastas(env)
        n = verificar_skills() + verificar_operacao(raiz) + verificar_referencia(escr)
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

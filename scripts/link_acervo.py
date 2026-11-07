#!/usr/bin/env python3
"""link_acervo.py — junções do repositório cgov-geral para a pasta CGOV (Google Drive).

Versão 0.1.0 (07/11/2026; Fase 5, bloco 3, etapa 5.1 do plano de implantação; substitui
scripts/link-acervo.sh, do WSL e da estrutura anterior à Fase 4).

Junções novas (alvo lido do .env; se a variável faltar, deriva de CGOV_RAIZ):
  local\\processos   -> CGOV_PROCESSOS   (padrão: CGOV_RAIZ\\01_processos)
  local\\normativos  -> CGOV_NORMATIVOS  (padrão: CGOV_RAIZ\\03_normativos)
  local\\escritorio  -> CGOV_ESCRITORIO  (padrão: CGOV_RAIZ\\90_escritorio-virtual)
Junções antigas, removidas no --executar: local\\analyses, local\\normative-sources,
local\\acervo-drive.

Segurança
  * Sem --executar, só mostra o que faria (nada muda).
  * Remove apenas JUNÇÕES (ou links simbólicos), com os.rmdir/os.unlink: tira o ponteiro,
    nunca o conteúdo do Drive. Se no lugar houver pasta real ou arquivo, para ([PARE]).
  * Não sobrescreve junção que aponte para outro alvo ([PARE]); corrija à mão ou peça ajuda.
  * Cria com "cmd /c mklink /J" (não exige administrador). Em Linux/macOS usa link
    simbólico (apenas para testes do próprio script).

Uso (Windows, na raiz do repositório):
  py scripts\\link_acervo.py              # simulação: estado atual e plano
  py scripts\\link_acervo.py --executar   # cria as novas e remove as antigas
Saída: 0 = ok; 1 = [PARE] (nada foi alterado a partir do primeiro problema); 2 = erro.
Sem caminhos pessoais neste arquivo (regra de sanitização).
"""
from __future__ import annotations

import argparse
import os
import stat
import subprocess
import sys
from pathlib import Path

VERSAO = "0.1.0"
REPO = Path(__file__).resolve().parent.parent
LOCAL = REPO / "local"
WINDOWS = os.name == "nt"

NOVAS = [  # (nome em local/, variável, subpasta padrão sob CGOV_RAIZ)
    ("processos", "CGOV_PROCESSOS", "01_processos"),
    ("normativos", "CGOV_NORMATIVOS", "03_normativos"),
    ("escritorio", "CGOV_ESCRITORIO", "90_escritorio-virtual"),
]
ANTIGAS = ["analyses", "normative-sources", "acervo-drive"]


class Pare(Exception):
    pass


# ---------------------------------------------------------------- .env
def ler_env() -> dict[str, str]:
    env: dict[str, str] = {}
    arq = REPO / ".env"
    if not arq.is_file():
        raise Pare(".env não encontrado na raiz do repositório (modelo: .env.example)")
    for linha in arq.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        linha = linha.strip()
        if linha and not linha.startswith("#") and "=" in linha:
            k, v = linha.split("=", 1)
            v = v.strip().strip('"').strip("'")
            env[k.strip()] = os.path.expanduser(os.path.expandvars(v))
    return env


def alvos(env: dict[str, str]) -> list[tuple[str, Path, str]]:
    raiz = env.get("CGOV_RAIZ")
    saida = []
    for nome, var, sub in NOVAS:
        if env.get(var):
            saida.append((nome, Path(env[var]), var))
        elif raiz:
            saida.append((nome, Path(raiz) / sub, f"CGOV_RAIZ\\{sub}"))
        else:
            raise Pare(f"{var} e CGOV_RAIZ ausentes no .env")
    return saida


# ---------------------------------------------------------------- junções
def eh_link(p: Path) -> bool:
    """Junção do Windows ou link simbólico (inclusive quebrado)."""
    if not os.path.lexists(p):
        return False
    if os.path.islink(p):
        return True
    if WINDOWS:
        if hasattr(os.path, "isjunction") and os.path.isjunction(p):  # Python 3.12+
            return True
        atr = getattr(os.lstat(p), "st_file_attributes", 0)
        return bool(atr & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))
    return False


def alvo_do_link(p: Path) -> str:
    try:
        t = os.readlink(p)
    except OSError:
        return "?"
    for pref in ("\\\\?\\", "\\??\\"):
        if t.startswith(pref):
            t = t[len(pref):]
    return t


def mesmo_caminho(a: str | Path, b: str | Path) -> bool:
    na = os.path.normcase(os.path.normpath(str(a)))
    nb = os.path.normcase(os.path.normpath(str(b)))
    return na == nb


def estado(p: Path) -> str:
    if not os.path.lexists(p):
        return "ausente"
    if eh_link(p):
        quebrada = "" if os.path.exists(p) else " (QUEBRADA: alvo não existe)"
        return f"junção -> {alvo_do_link(p)}{quebrada}"
    if p.is_dir():
        return "PASTA REAL"
    return "ARQUIVO"


def criar(link: Path, alvo: Path) -> None:
    if WINDOWS:
        r = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(alvo)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            raise Pare(f"mklink falhou para {link.name}: {(r.stdout + r.stderr).strip()}")
    else:
        os.symlink(alvo, link, target_is_directory=True)


def remover_link(p: Path) -> None:
    """Remove só o ponteiro. os.rmdir nunca apaga conteúdo (falha em pasta real cheia)."""
    if not eh_link(p):
        raise Pare(f"{p.name} não é junção; nada removido")
    if WINDOWS and not os.path.islink(p):
        os.rmdir(p)
    else:
        os.unlink(p)


def contar(p: Path) -> str:
    try:
        return f"{len(os.listdir(p))} item(ns)"
    except OSError as e:
        return f"ilegível ({e.__class__.__name__})"


# ---------------------------------------------------------------- principal
def main(argv: list[str] | None = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Junções do cgov-geral para a pasta CGOV")
    ap.add_argument("--executar", action="store_true", help="aplicar (sem isto, só simula)")
    ap.add_argument("--version", action="version", version=VERSAO)
    a = ap.parse_args(argv)
    modo = "EXECUÇÃO" if a.executar else "SIMULAÇÃO (nada será alterado)"
    print(f"link_acervo.py {VERSAO} — {modo}")
    print(f"Repositório: {REPO}")

    try:
        env = ler_env()
        planos = alvos(env)
        if not LOCAL.is_dir():
            raise Pare("pasta local\\ não existe no repositório")

        # 1. Diagnóstico e pré-condições (nada muda aqui)
        print("\n== Junções novas")
        acoes_novas = []
        for nome, alvo, origem in planos:
            link = LOCAL / nome
            st = estado(link)
            print(f"  local\\{nome:11} {st}")
            print(f"      alvo esperado ({origem}): {alvo}")
            if not alvo.is_dir():
                raise Pare(f"alvo de local\\{nome} não existe ou não é pasta: {alvo}")
            if st == "ausente":
                acoes_novas.append((link, alvo))
            elif eh_link(link) and mesmo_caminho(alvo_do_link(link), alvo):
                print("      já correta — nada a fazer")
            else:
                raise Pare(f"local\\{nome} existe e não é a junção esperada ({st})")

        print("\n== Junções antigas")
        acoes_antigas = []
        for nome in ANTIGAS:
            link = LOCAL / nome
            st = estado(link)
            print(f"  local\\{nome:18} {st}")
            if st == "ausente":
                continue
            if not eh_link(link):
                raise Pare(f"local\\{nome} é {st}: não removo pasta ou arquivo real")
            acoes_antigas.append(link)

        print("\n== Plano")
        for link, alvo in acoes_novas:
            print(f"  criar   local\\{link.name} -> {alvo}")
        for link in acoes_antigas:
            print(f"  remover local\\{link.name} (só o ponteiro)")
        if not acoes_novas and not acoes_antigas:
            print("  nada a fazer")

        if not a.executar:
            print("\nResultado: SIMULAÇÃO concluída. Para aplicar: py scripts\\link_acervo.py --executar")
            return 0

        # 2. Execução: novas primeiro (se falhar, as antigas continuam onde estavam)
        print("\n== Execução")
        for link, alvo in acoes_novas:
            criar(link, alvo)
            print(f"  ok  criada   local\\{link.name}")
        for link in acoes_antigas:
            remover_link(link)
            print(f"  ok  removida local\\{link.name}")

        # 3. Conferência (aceite da 5.1: as três junções novas listam conteúdo)
        print("\n== Conferência")
        falhas = 0
        for nome, alvo, _ in planos:
            link = LOCAL / nome
            ok = eh_link(link) and mesmo_caminho(alvo_do_link(link), alvo) and os.path.isdir(link)
            falhas += not ok
            print(f"  {'ok ' if ok else 'ERRO'} local\\{nome:11} {contar(link) if ok else estado(link)}")
        for nome in ANTIGAS:
            ok = not os.path.lexists(LOCAL / nome)
            falhas += not ok
            print(f"  {'ok ' if ok else 'ERRO'} local\\{nome:18} {'ausente' if ok else estado(LOCAL / nome)}")
        print(f"\nResultado: {'CONCLUÍDO' if not falhas else f'{falhas} FALHA(S) na conferência'}")
        return 0 if not falhas else 1
    except Pare as e:
        print(f"\n[PARE] {e}")
        return 1
    except OSError as e:
        print(f"\nerro: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""gerar_indices_docs.py — versão 0.1.0 (09/11/2026)

Gera, a partir dos cabeçalhos dos documentos grandes, os índices navegáveis em Markdown e refaz os links do
catálogo de skills. Só biblioteca padrão (ADR-004). Roda na raiz do repositório ou de qualquer lugar.

Uso:
  py scripts\\gerar_indices_docs.py              # gera índices e refaz os links do catálogo
  py scripts\\gerar_indices_docs.py --verificar  # não grava; sai com 1 se algo estiver desatualizado
  py scripts\\gerar_indices_docs.py --skills     # só os links do catálogo de skills
  py scripts\\gerar_indices_docs.py --indices    # só os índices de cabeçalhos

Quando rodar: depois de editar o plano, o decision-log ou as instruções do analista de processos SEI, e depois
de mover pastas de skills (Fase 7, etapa 7.1). Convenções: docs/convencoes-documentacao.md.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
CATALOGO = DOCS / "catalogo-skills.md"
RAIZES_SKILLS = [RAIZ / "skills", RAIZ / "plugins" / "cgov-escritorio" / "skills"]

INDICES = [
    {
        "fonte": "docs/plano-implantacao.md",
        "saida": "docs/plano-indice.md",
        "titulo": "Índice do plano de implantação",
        "niveis": (2, 3),
        "aviso": "O plano tem mais de 1.500 linhas e 240 KB: **não o leia inteiro**. Abra esta lista, escolha a seção e leia só ela (por exemplo, com `Read` e `offset`/`limit` na linha indicada, ou `grep`).",
        "relacionados": ["docs/plano-implantacao.md", "docs/INDICE.md", "docs/governance/rastreabilidade.md"],
    },
    {
        "fonte": "docs/governance/decision-log.md",
        "saida": "docs/governance/decision-log-indice.md",
        "titulo": "Índice do registro de decisões",
        "niveis": (2,),
        "aviso": "O registro de decisões só recebe acréscimos (regra 6 do projeto Implantação) e tem mais de 1.700 linhas: use esta lista para ir direto à seção. A ligação entre seções, decisões D, ADRs e fases está em [`rastreabilidade.md`](rastreabilidade.md).",
        "relacionados": ["docs/governance/decision-log.md", "docs/governance/rastreabilidade.md"],
    },
    {
        "fonte": "docs/system-instructions/analista-processos-sei.md",
        "saida": "docs/system-instructions/analista-processos-sei-indice.md",
        "titulo": "Índice das instruções do analista de processos SEI",
        "niveis": (2, 3),
        "aviso": "O documento tem cerca de 1.200 linhas e 66 KB e é colado inteiro em assistentes sem acesso a arquivos; para consulta no desenvolvimento, leia só a seção de que precisa.",
        "relacionados": ["docs/system-instructions/analista-processos-sei.md", "docs/multiplatform.md"],
    },
]


def slugify(texto: str) -> str:
    """Âncora no estilo do GitHub: minúsculas, sem pontuação, espaços viram hífens."""
    texto = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", texto)  # [texto](url) -> texto
    texto = re.sub(r"[`*~]", "", texto)
    texto = texto.strip().lower()
    texto = re.sub(r"[^\w\- ]", "", texto)
    return texto.replace(" ", "-")


def cabecalhos(caminho: Path):
    """Lista (nivel, texto, linha, ancora) ignorando blocos de código; âncoras repetidas ganham -1, -2…"""
    vistos = {}
    saida = []
    dentro = False
    texto = caminho.read_text(encoding="utf-8")
    for n, linha in enumerate(texto.split("\n"), start=1):
        if re.match(r"^\s*(```|~~~)", linha):
            dentro = not dentro
            continue
        if dentro:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", linha)
        if not m:
            continue
        base = slugify(m.group(2))
        k = vistos.get(base, 0)
        vistos[base] = k + 1
        saida.append((len(m.group(1)), m.group(2).strip(), n, base if k == 0 else "%s-%d" % (base, k)))
    return saida


def mapa_skills():
    """nome da skill -> caminho do SKILL.md relativo a docs/ (com '/')."""
    mapa = {}
    for base in RAIZES_SKILLS:
        if not base.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in ("evals", "references", "scripts", "__pycache__")]
            if "SKILL.md" in filenames:
                p = Path(dirpath) / "SKILL.md"
                mapa[Path(dirpath).name] = os.path.relpath(p, DOCS).replace(os.sep, "/")
    return mapa


def refazer_links_catalogo(mapa):
    """Reescreve a primeira coluna das tabelas do catálogo como link para o SKILL.md. Devolve (texto novo, ausentes)."""
    texto = CATALOGO.read_text(encoding="utf-8")
    ausentes = []

    def troca(m):
        nome = m.group(1)
        if nome not in mapa:
            ausentes.append(nome)
            return m.group(0)
        return "| [`%s`](%s) |" % (nome, mapa[nome])

    novo = re.sub(r"^\| (?:\[)?`([a-z0-9][a-z0-9-]*)`(?:\]\([^)]*\))? \|", troca, texto, flags=re.M)
    return novo, ausentes


def gerar_indice(spec):
    fonte = RAIZ / spec["fonte"]
    saida = RAIZ / spec["saida"]
    cab = [c for c in cabecalhos(fonte) if c[0] in spec["niveis"]]
    rel = os.path.relpath(fonte, saida.parent).replace(os.sep, "/")
    n_linhas = len(fonte.read_text(encoding="utf-8").split("\n"))
    nivel_min = min(spec["niveis"])
    linhas = [
        "---",
        "tipo: indice-gerado",
        "status: vigente",
        "gerado_de: %s" % spec["fonte"],
        "relacionados: [%s]" % ", ".join(spec["relacionados"]),
        "---",
        "",
        "# %s" % spec["titulo"],
        "",
        "> Gerado por `py scripts\\gerar_indices_docs.py` a partir de [`%s`](%s) (%d linhas, %d cabeçalhos). **Não edite à mão.**" % (spec["fonte"].split("/")[-1], rel, n_linhas, len(cab)),
        "> %s" % spec["aviso"],
        "",
    ]
    for nivel, texto, n, ancora in cab:
        recuo = "  " * (nivel - nivel_min)
        limpo = re.sub(r"[`]", "", texto)
        linhas.append("%s- [%s](%s#%s) — linha %d" % (recuo, limpo, rel, ancora, n))
    linhas.append("")
    return saida, "\n".join(linhas)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verificar", action="store_true", help="não grava; sai com 1 se algo estiver desatualizado")
    ap.add_argument("--skills", action="store_true", help="só os links do catálogo de skills")
    ap.add_argument("--indices", action="store_true", help="só os índices de cabeçalhos")
    a = ap.parse_args()
    fazer_skills = a.skills or not a.indices
    fazer_indices = a.indices or not a.skills
    pendentes = 0

    if fazer_skills:
        mapa = mapa_skills()
        novo, ausentes = refazer_links_catalogo(mapa)
        atual = CATALOGO.read_text(encoding="utf-8")
        for nome in ausentes:
            print("AVISO: skill do catálogo sem SKILL.md em skills/ ou plugins/: %s" % nome)
        sem_catalogo = sorted(n for n in mapa if "`%s`" % n not in atual)
        for nome in sem_catalogo:
            print("AVISO: SKILL.md sem linha no catálogo: %s" % nome)
        if novo != atual:
            pendentes += 1
            if a.verificar:
                print("DESATUALIZADO: links de skills em docs/catalogo-skills.md")
            else:
                CATALOGO.write_text(novo, encoding="utf-8", newline="")
                print("atualizado: docs/catalogo-skills.md (links das %d skills)" % len(mapa))
        else:
            print("em dia: links de skills no catálogo (%d skills)" % len(mapa))

    if fazer_indices:
        for spec in INDICES:
            caminho, conteudo = gerar_indice(spec)
            existente = caminho.read_text(encoding="utf-8") if caminho.exists() else None
            if existente != conteudo:
                pendentes += 1
                if a.verificar:
                    print("DESATUALIZADO: %s" % spec["saida"])
                else:
                    caminho.write_text(conteudo, encoding="utf-8", newline="")
                    print("gerado: %s" % spec["saida"])
            else:
                print("em dia: %s" % spec["saida"])

    if a.verificar and pendentes:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

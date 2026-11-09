#!/usr/bin/env python3
"""verificar_docs.py — versão 0.1.0 (09/11/2026)

Verifica a documentação Markdown do repositório (só leitura; só biblioteca padrão, ADR-004):
  ERROS (saída 1)  links relativos e âncoras quebrados; frontmatter ausente ou inválido em docs/; ADR com status
                   diferente entre o corpo, o frontmatter e docs/adr/README.md; arquivo de docs/ sem nenhum link
                   de entrada; skill sem linha no catálogo (ou o inverso); `skillOverrides` diferente do número
                   de SKILL.md.
  AVISOS           caminhos obsoletos em documentos vigentes; documentos grandes sem índice; índice gerado
                   desatualizado; documento histórico sem aviso; marcas ⏳ ou "Proposto" esquecidas.

Uso:  py scripts\\verificar_docs.py [--so-erros] [--quieto]
Convenções: docs/convencoes-documentacao.md. Rode também py scripts\\verificar_sanitizacao.py antes do commit.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gerar_indices_docs import INDICES, cabecalhos, gerar_indice, mapa_skills, refazer_links_catalogo, slugify  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
IGNORAR = {".git", "local", "dist", "node_modules", ".obsidian", ".vscode", ".claude", "__pycache__", ".agents", "plugins"}

TIPOS = {"guia", "referencia", "arquitetura", "decisao", "registro", "plano", "procedimento", "instrucao", "relatorio",
         "indice", "indice-gerado", "pendencias", "catalogo"}
STATUS = {"vigente", "rascunho", "historico", "substituido"}
STATUS_ADR = {"proposto", "aceito", "rejeitado", "substituido"}
# Colados inteiros em campos com limite de caracteres: não levam frontmatter (docs/convencoes-documentacao.md §3).
SEM_FRONTMATTER = {"docs/system-instructions/analista-governanca.md", "docs/system-instructions/analista-processos-sei.md"}
# Citam caminhos antigos de propósito (tabelas de tradução, histórico, ADRs): não geram aviso.
PERMITE_OBSOLETOS = {
    "AGENTS.md", "CLAUDE.md", "operacao/AGENTS.md", "docs/governance/decision-log.md", "docs/governance/pendencias.md",
    "docs/governance/rastreabilidade.md", "docs/plano-implantacao.md", "docs/fluxos-de-trabalho.md", "docs/convencoes-documentacao.md",
    "docs/adr/ADR-006-skills-neutras-quanto-a-caminho.md", "docs/adr/ADR-012-estrutura-repositorio-operacional.md",
    "docs/overview.md", "docs/references/normative-catalog.md", "docs/system-instructions/escritorio-cgov-operacao.md",
    "docs/system-instructions/analista-processos-sei.md", "docs/multiplatform.md",
}
OBSOLETOS = [r"local[/\\]analyses", r"CGOV_Processos", r"_CGOV_NT", r"normative-sources", r"acervo-drive", r"04_fontes_normativas",
             r"07_analises", r"05_novas_skills_propostas", r"01_relatorios", r"REGISTRO_DECISOES", r"skills-legacy", r"NT_ESTADO_piloto",
             r"escritorio-cgov\.md", r"\.sh\b"]
LIMITE_LINHAS = 600
GRANDES_COM_INDICE = {i["fonte"] for i in INDICES}


def arquivos_md():
    saida = []
    for dirpath, dirnames, filenames in os.walk(RAIZ):
        dirnames[:] = [d for d in dirnames if d not in IGNORAR]
        for nome in filenames:
            if nome.endswith(".md"):
                saida.append(Path(dirpath) / nome)
    return sorted(saida)


def rel(p: Path) -> str:
    return p.relative_to(RAIZ).as_posix()


def sem_codigo(texto: str) -> str:
    """Remove blocos cercados e trechos de código em linha (links dentro deles não contam)."""
    texto = re.sub(r"^(```|~~~).*?^\1.*?$", "", texto, flags=re.S | re.M)
    return re.sub(r"`[^`\n]*`", "", texto)


def ler_frontmatter(texto: str):
    if not texto.startswith("---\n"):
        return None, texto
    fim = texto.find("\n---", 4)
    if fim == -1:
        return None, texto
    bloco = texto[4:fim]
    resto = texto[fim + 4:].lstrip("\n")
    campos = {}
    for linha in bloco.split("\n"):
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", linha)
        if not m:
            continue
        valor = m.group(2).strip()
        if valor.startswith("[") and valor.endswith("]"):
            valor = [v.strip().strip("'\"") for v in valor[1:-1].split(",") if v.strip()]
        else:
            valor = valor.strip("'\"")
        campos[m.group(1)] = valor
    return campos, resto


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--so-erros", action="store_true", help="não mostra os avisos")
    ap.add_argument("--quieto", action="store_true", help="só o resumo")
    a = ap.parse_args()
    erros, avisos = [], []
    hoje = datetime.date.today()

    todos = arquivos_md()
    textos = {p: p.read_text(encoding="utf-8") for p in todos}
    ancoras_cache = {}

    def ancoras(p: Path):
        if p not in ancoras_cache:
            ancoras_cache[p] = {c[3] for c in cabecalhos(p)} | {c[1].lower() for c in cabecalhos(p)}
        return ancoras_cache[p]

    entradas = {p: 0 for p in todos}
    n_links = 0
    for p, texto in textos.items():
        limpo = sem_codigo(texto)
        _, corpo = ler_frontmatter(limpo)
        for m in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", limpo):
            alvo = m.group(1)
            if re.match(r"(https?:|mailto:|computer:|obsidian:)", alvo) or re.search(r"[<>{}$]", alvo):
                continue
            n_links += 1
            caminho, _, frag = alvo.partition("#")
            destino = (p.parent / unquote(caminho)).resolve() if caminho else p
            if caminho and not destino.exists():
                erros.append("%s: link para arquivo inexistente: %s" % (rel(p), alvo))
                continue
            if destino in entradas and destino != p:
                entradas[destino] += 1
            if frag and destino.suffix == ".md" and destino.exists():
                f = unquote(frag)
                if f not in ancoras(destino) and f.lower() not in ancoras(destino):
                    erros.append("%s: âncora inexistente: %s" % (rel(p), alvo))
        # relacionados do frontmatter contam como links de entrada
        fm, _ = ler_frontmatter(texto)
        if fm:
            for r in fm.get("relacionados", []) if isinstance(fm.get("relacionados"), list) else []:
                d = (RAIZ / r)
                if not d.exists():
                    erros.append("%s: frontmatter 'relacionados' aponta para arquivo inexistente: %s" % (rel(p), r))
                elif d.resolve() in entradas and d.resolve() != p:
                    entradas[d.resolve()] += 1

    # frontmatter e regras de docs/
    adr_readme = textos.get(DOCS / "adr" / "README.md", "")
    for p, texto in textos.items():
        r = rel(p)
        if not r.startswith("docs/"):
            continue
        fm, corpo = ler_frontmatter(texto)
        if r in SEM_FRONTMATTER:
            if fm is not None:
                erros.append("%s: não deve ter frontmatter (é colado inteiro em campo com limite; ver convenções §3)" % r)
            continue
        if fm is None:
            erros.append("%s: frontmatter ausente" % r)
            continue
        tipo, status = fm.get("tipo", ""), fm.get("status", "")
        if tipo not in TIPOS:
            erros.append("%s: tipo inválido ou ausente: %r" % (r, tipo))
        validos = STATUS_ADR if r.startswith("docs/adr/ADR-") else STATUS
        if status not in validos:
            erros.append("%s: status inválido ou ausente: %r" % (r, status))
        if tipo != "indice-gerado":
            data = fm.get("atualizado_em", "")
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(data)):
                erros.append("%s: atualizado_em ausente ou fora do formato AAAA-MM-DD" % r)
            else:
                try:
                    if datetime.date.fromisoformat(data) > hoje:
                        erros.append("%s: atualizado_em no futuro: %s" % (r, data))
                except ValueError:
                    erros.append("%s: atualizado_em inválido: %s" % (r, data))
        if status == "historico" and "histórico" not in "\n".join(corpo.split("\n")[:12]).lower():
            avisos.append("%s: status histórico sem aviso 'histórico' nas primeiras linhas" % r)
        # ADR: corpo × frontmatter × README
        m = re.match(r"^docs/adr/(ADR-\d{3})-", r)
        if m:
            corpo_status = re.search(r"\*\*Status:\*\*\s*([A-Za-zçÇãõéíúâêôà ]+)", corpo)
            norm = lambda s: s.strip().lower().replace("ç", "c").replace("í", "i").split(" por ")[0].split(" ")[0]
            if corpo_status and norm(corpo_status.group(1)) != norm(status):
                erros.append("%s: status do corpo (%s) difere do frontmatter (%s)" % (r, corpo_status.group(1).strip(), status))
            linha = [l for l in adr_readme.split("\n") if l.startswith("| [%s" % m.group(1))]
            if linha:
                col = [c.strip() for c in linha[0].strip("|").split("|")]
                if len(col) > 1 and norm(col[1]) != norm(status):
                    erros.append("%s: status no docs/adr/README.md (%s) difere do frontmatter (%s)" % (r, col[1], status))
            else:
                erros.append("%s: ADR sem linha em docs/adr/README.md" % r)
        # entradas
        if entradas.get(p, 0) == 0 and r != "docs/INDICE.md":
            erros.append("%s: nenhum documento aponta para ele (arquivo órfão)" % r)

    # arquivos fora de docs/ também precisam de entrada (exceto raiz, operacao/ e skills/)
    for p in todos:
        r = rel(p)
        if r.startswith("archive/") and entradas.get(p, 0) == 0:
            erros.append("%s: nenhum documento aponta para ele (arquivo órfão)" % r)

    # skills × catálogo × overrides
    mapa = mapa_skills()
    _, ausentes = refazer_links_catalogo(mapa)
    for n in ausentes:
        erros.append("docs/catalogo-skills.md: skill sem SKILL.md: %s" % n)
    cat = (DOCS / "catalogo-skills.md").read_text(encoding="utf-8")
    for n in sorted(mapa):
        if "`%s`" % n not in cat:
            erros.append("docs/catalogo-skills.md: falta a skill %s" % n)
    st = RAIZ / ".claude" / "settings.json"
    if st.exists():
        try:
            ov = json.loads(st.read_text(encoding="utf-8")).get("skillOverrides", {})
            if len(ov) != len(mapa):
                erros.append(".claude/settings.json: skillOverrides tem %d entradas e há %d SKILL.md" % (len(ov), len(mapa)))
        except ValueError as e:
            erros.append(".claude/settings.json: JSON inválido (%s)" % e)

    # avisos: obsoletos, tamanho, índices gerados, ⏳ e "Proposto"
    padrao = re.compile("|".join(OBSOLETOS))
    for p, texto in textos.items():
        r = rel(p)
        if r.startswith(("archive/", "docs/reports/", "skills/")) or r in PERMITE_OBSOLETOS:
            continue
        fm, corpo = ler_frontmatter(texto)
        if fm and fm.get("status") == "historico":
            continue
        for n, linha in enumerate(sem_codigo(texto).split("\n"), start=1):
            if padrao.search(linha):
                avisos.append("%s:%d: caminho possivelmente obsoleto: %s" % (r, n, padrao.search(linha).group(0)))
                break
        if "⏳" in texto and r.startswith("docs/") and r != "docs/plano-implantacao.md":
            avisos.append("%s: contém marca ⏳ (pendência de fase antiga?)" % r)
        linhas = texto.count("\n") + 1
        if linhas > LIMITE_LINHAS and r not in GRANDES_COM_INDICE and r.startswith("docs/"):
            avisos.append("%s: %d linhas (> %d) sem índice gerado" % (r, linhas, LIMITE_LINHAS))
    for spec in INDICES:
        caminho, conteudo = gerar_indice(spec)
        if not caminho.exists() or caminho.read_text(encoding="utf-8") != conteudo:
            avisos.append("%s: índice gerado desatualizado; rode py scripts\\gerar_indices_docs.py" % spec["saida"])

    if not a.quieto:
        for e in erros:
            print("ERRO   ", e)
        if not a.so_erros:
            for w in avisos:
                print("AVISO  ", w)
    print("\n%d arquivos .md, %d links relativos, %d skills | %d erro(s), %d aviso(s)" % (len(todos), n_links, len(mapa), len(erros), len(avisos)))
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())

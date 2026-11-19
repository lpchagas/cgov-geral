#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
montar_nt_docx.py — alimenta o .docx de revisão da Nota Técnica em elaboração (suíte cgov-nt).

Cada skill de redação (cgov-nt-03 a cgov-nt-07) grava o seu capítulo em Markdown na pasta de
trabalho do processo e chama este script, que:

  1. localiza a versão mais recente  NT_<apelido>_v<versão>-<etapa>.docx  na pasta de trabalho
     (essa versão pode conter edições e comentários do revisor humano: eles são preservados);
  2. copia essa versão e ACRESCENTA o capítulo novo na posição canônica da NT
     (abertura e Cap. 1 → Caps. 2, 3, 4 → subitem da PFE no Cap. 4 → Seção 5);
  3. grava a nova versão  NT_<apelido>_v<nova versão>-<etapa>.docx  — nunca sobrescreve.

Sem versão anterior (ou com --base novo), cria o documento a partir do zero no padrão gráfico
das NTs da CGOV (A4, Calibri 11,5, verde institucional, cabeçalho e rodapé, Sumário, Listas de
Quadros e de Figuras, quadros zebrados, seções paisagem para quadros largos, assinaturas).

Versões (número principal = fase da NT):
  v1 introdução (cgov-nt-03) · v2 diagnóstico (cgov-nt-04; v2.1, v2.2… por incremento) ·
  v3 propostas (cgov-nt-05) · v4 quesitos PFE (cgov-nt-06) · v5 conclusão (cgov-nt-07) ·
  revisão humana incorporada: vN.M-revisao.

Uso:
  python montar_nt_docx.py CAPITULO.md [OUTRO.md ...] --versao 2.1 --etapa fluxo
         [--pasta <pasta de trabalho>] [--apelido <apelido>] [--base auto|novo|<arquivo.docx>]
         [--substituir] [--simular]
  python montar_nt_docx.py --listar --pasta <pasta de trabalho>

Convenções de Markdown reconhecidas (as mesmas das skills cgov-nt):
  ## N. TÍTULO (Título 1) · ### Capítulo N — Nome e ### 5.1 Nome (Título 2) · #### N.1. Nome (Título 3)
  **Nota Técnica nº …** / Brasília-DF, … / **Assunto:** … / **Processo SEI nº** …  (abertura)
  **Quadro N — título** + tabela + Fonte: … · **Figura N — título** + ![](imagem) ou ```mermaid
  **Recomendação nº N — …** · **Fundamento normativo:** … · **Risco institucional …:** …
  - **Urgente:** / **Prioritário:** / **Desejável:** (faixas de critério) · (i) (ii) … (proposição)
  > texto (caixa de destaque) · <!-- paisagem --> / <!-- retrato --> antes do quadro (força orientação)
  Seções cujo título contém "Pendências" não entram no .docx (são listadas no relatório).

Requer python-docx. Diagramas Mermaid são renderizados se o comando `mmdc` existir; senão,
entra um marcador ⚠ para inserir a imagem. Sem caminhos pessoais neste arquivo.

Versão 0.1.1 (19/11/2026): o rodapé omite a nota "⚠ …" que estiver na linha do título ou do processo.
Versão 0.1.0 (19/11/2026; D66): primeira versão; relatório em UTF-8 mesmo com saída redirecionada.
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

try:
    import docx
    from docx.enum.section import WD_ORIENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls, qn
    from docx.shared import Cm, Emu, Pt, RGBColor, Twips
except ImportError:  # pragma: no cover
    sys.exit("Falta a biblioteca python-docx: pip install python-docx")

VERSAO = "0.1.1"

# ------------------------------------------------------------------ padrão gráfico (modelo v5)
VERDE, VERDE2, TEXTO, CINZA = "1E4D3A", "2E6B50", "1F2421", "5F6B64"
BORDA, ZEBRA, CAIXA_VERDE = "B5C4BA", "F4F7F5", "E8F0EB"
CAIXA_CINZA, CAIXA_RISCO, CAIXA_REC, AMBAR, ALERTA = "F2F4F2", "FFF8EA", "FFF3DF", "B26B00", "A3302A"
PRIORIDADES = {  # texto, fundo
    "urgente": (ALERTA, "FBEAEA"),
    "prioritario": (AMBAR, "FFF3DF"),
    "prioritaria": (AMBAR, "FFF3DF"),
    "desejavel": ("2F6E9E", "E7F0F8"),
}
PAG_W, PAG_H = 11906, 16838                     # A4 em twips
MARG = dict(top=1418, bottom=1134, left=1701, right=1134, header=709, footer=567)
LARG_RETRATO = PAG_W - MARG["left"] - MARG["right"]      # 9071
LARG_PAISAGEM = PAG_H - MARG["left"] - MARG["right"]     # 14003
COLUNAS_PAISAGEM = 7                             # quadros com 7+ colunas vão para seção paisagem
TEXTO_PAISAGEM = 6, 280                          # ou 6+ colunas com linhas longas (média de caracteres)
RE_VERSAO = re.compile(r"^NT_(?P<apelido>.+)_v(?P<ver>\d+(?:\.\d+)*)-(?P<etapa>[a-z0-9-]+)\.docx$")


# ------------------------------------------------------------------ utilidades
def sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", sem_acento(s).lower()).strip("-")


def ver_tupla(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in v.split("."))


def limpar_md(s: str) -> str:
    """Texto sem marcação inline (para títulos e comparações)."""
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return re.sub(r"[*_`]", "", s).strip()


def sem_marca(s: str) -> str:
    """Texto para o rodapé: sem marcação e sem nota de pendência ("⚠ …") na mesma linha."""
    return limpar_md(re.split(r"\s*⚠", s, maxsplit=1)[0])


def versoes(pasta: Path, apelido: str | None = None) -> list[tuple[tuple[int, ...], Path, str]]:
    achadas = []
    for f in pasta.glob("NT_*_v*.docx"):
        if f.name.startswith("~$"):
            continue
        m = RE_VERSAO.match(f.name)
        if m and (apelido is None or m["apelido"] == apelido):
            achadas.append((ver_tupla(m["ver"]), f, m["etapa"]))
    return sorted(achadas)


def apelido_da_pasta(pasta: Path) -> str:
    for p in (pasta, *pasta.parents):
        m = re.match(r"^SEI_\d{5}\.\d{6}_\d{4}-\d{2}_(.+)$", p.name)
        if m:
            return m.group(1)
    sys.exit("Não deduzi o apelido do processo pelo nome da pasta: informe --apelido.")


# ------------------------------------------------------------------ Markdown → blocos
class Bloco(dict):
    """tipo + campos; dict simples para facilitar o relatório."""


def ler_blocos(texto: str, origem: Path) -> tuple[list[Bloco], list[str]]:
    linhas = texto.replace("\r\n", "\n").split("\n")
    blocos: list[Bloco] = []
    excluidos: list[str] = []
    i, orient = 0, None
    pular_nivel = None  # nível do título "Pendências" em exclusão
    par: list[str] = []

    def fechar_par():
        nonlocal par
        if par:
            blocos.append(Bloco(tipo="par", linhas=par, orient=None))
            par = []

    while i < len(linhas):
        ln = linhas[i]
        st = ln.strip()
        mh = re.match(r"^(#{1,5})\s+(.*)$", st)
        if pular_nivel is not None:
            if mh and len(mh.group(1)) <= pular_nivel:
                pular_nivel = None
            else:
                i += 1
                continue
        if mh:
            fechar_par()
            nivel, titulo = len(mh.group(1)), mh.group(2).strip()
            if "pendência" in titulo.lower() or "pendencia" in sem_acento(titulo.lower()):
                excluidos.append(titulo)
                pular_nivel = nivel
            elif nivel > 1:  # "# título" é o nome do arquivo de trabalho, não da NT
                blocos.append(Bloco(tipo="titulo", nivel=nivel, texto=titulo))
            i += 1
            continue
        if st.startswith("```"):
            fechar_par()
            lang = st[3:].strip().lower()
            j, corpo = i + 1, []
            while j < len(linhas) and not linhas[j].strip().startswith("```"):
                corpo.append(linhas[j])
                j += 1
            blocos.append(Bloco(tipo="codigo", lang=lang, texto="\n".join(corpo), origem=str(origem)))
            i = j + 1
            continue
        if st.startswith("<!--"):
            fechar_par()
            if "paisagem" in st.lower():
                orient = "paisagem"
            elif "retrato" in st.lower():
                orient = "retrato"
            while i < len(linhas) and "-->" not in linhas[i]:
                i += 1
            i += 1
            continue
        if st.startswith("|"):
            fechar_par()
            tab = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                tab.append(linhas[i].strip())
                i += 1
            blocos.append(Bloco(tipo="tabela", linhas=tab, orient=orient))
            orient = None
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", st):
            fechar_par()
            i += 1
            continue
        if not st:
            fechar_par()
            i += 1
            continue
        mi = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", ln)
        if mi and not re.match(r"^\*\*", st) or (mi and re.match(r"^\s*[-+]\s", ln)):
            fechar_par()
            recuo = len(mi.group(1).replace("\t", "    "))
            item = [mi.group(3)]
            j = i + 1
            while j < len(linhas) and linhas[j].strip() and not re.match(r"^\s*([-*+]|\d+[.)])\s+", linhas[j]) \
                    and not linhas[j].strip().startswith(("|", "#", ">", "```")):
                item.append(linhas[j].strip())
                j += 1
            blocos.append(Bloco(tipo="item", ordenado=mi.group(2)[0].isdigit(), nivel=min(recuo // 2, 1),
                                texto=" ".join(item)))
            i = j
            continue
        if st.startswith(">"):
            fechar_par()
            cit = []
            while i < len(linhas) and linhas[i].strip().startswith(">"):
                cit.append(linhas[i].strip()[1:].strip())
                i += 1
            blocos.append(Bloco(tipo="citacao", texto=" ".join(x for x in cit if x)))
            continue
        mimg = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)", st)
        if mimg:
            fechar_par()
            blocos.append(Bloco(tipo="imagem", alt=mimg.group(1), caminho=mimg.group(2), origem=str(origem)))
            i += 1
            continue
        par.append(st)
        i += 1
    fechar_par()
    return blocos, excluidos


def dividir_unidades(blocos: list[Bloco]) -> list[dict]:
    """Agrupa os blocos em unidades posicionáveis no documento.

    chave: ("abertura",) | ("cap", N) | ("conclusao",) | ("sub", "N.M")
    """
    unidades: list[dict] = []
    descartados: list = []
    atual = None
    for b in blocos:
        chave = None
        if b["tipo"] == "titulo":
            t = limpar_md(b["texto"])
            if b["nivel"] == 2 and re.match(r"^1\.\s", t):
                chave = ("abertura",)
            elif b["nivel"] == 2 and re.match(r"^5[.\s]", t):
                chave = ("conclusao",)
            elif b["nivel"] == 3 and re.match(r"^Cap[ií]tulo\s+(\d+)", t):
                n = int(re.match(r"^Cap[ií]tulo\s+(\d+)", t).group(1))
                if not (atual and atual["chave"] == ("abertura",) and n == 1):
                    chave = ("cap", n)
            elif b["nivel"] == 4 and atual is None:
                m = re.match(r"^(\d+)\.(\d+)", t)
                if m:
                    chave = ("sub", f"{m.group(1)}.{m.group(2)}")
        if atual is None and chave is None:
            # antes de qualquer título, só a abertura (Nota Técnica nº, Data, Assunto) entra no .docx;
            # notas de trabalho do arquivo .md (ex.: "> Montagem em…") ficam de fora
            if b["tipo"] == "par" and tipo_paragrafo(b["linhas"][0]) in ("titulo_nt", "data", "assunto", "processo"):
                chave = ("abertura",)
            else:
                descartados.append(b)
                continue
        if chave and not (atual and atual["chave"] == ("abertura",) and chave == ("abertura",)):
            atual = {"chave": chave, "blocos": []}
            unidades.append(atual)
        atual["blocos"].append(b)
    return unidades, descartados


# ------------------------------------------------------------------ estilos
def _estilo_xml(sid, nome, ppr="", rpr="", base="Normal", proximo=None, tipo="paragraph"):
    prox = f'<w:next w:val="{proximo}"/>' if proximo else ""
    return (f'<w:style {nsdecls("w")} w:type="{tipo}" w:customStyle="1" w:styleId="{sid}">'
            f'<w:name w:val="{nome}"/><w:basedOn w:val="{base}"/>{prox}<w:qFormat/>'
            f'<w:pPr>{ppr}</w:pPr><w:rPr>{rpr}</w:rPr></w:style>')


def _borda(lado, cor, sz=4, esp=4):
    return f'<w:{lado} w:val="single" w:sz="{sz}" w:space="{esp}" w:color="{cor}"/>'


def _caixa(fundo, barra=None, barra_sz=18):
    bdr = f"<w:pBdr>{_borda('left', barra, barra_sz, 6)}</w:pBdr>" if barra else ""
    return f'{bdr}<w:shd w:val="clear" w:color="auto" w:fill="{fundo}"/>'


ESTILOS = [
    # sid, nome, pPr, rPr
    ("CorpoNT", "Corpo NT", '<w:spacing w:after="140" w:line="276" w:lineRule="auto"/><w:ind w:firstLine="851"/><w:jc w:val="both"/>', ""),
    ("TituloNT", "Título NT", '<w:spacing w:before="480" w:after="120"/><w:jc w:val="center"/>',
     f'<w:b/><w:bCs/><w:color w:val="{VERDE}"/><w:sz w:val="34"/><w:szCs w:val="34"/>'),
    ("FileteNT", "Filete NT", f'<w:pBdr>{_borda("bottom", VERDE, 12, 1)}</w:pBdr><w:spacing w:after="480"/><w:ind w:left="2600" w:right="2600"/><w:jc w:val="center"/>', ""),
    ("DataNT", "Data NT", '<w:spacing w:after="360"/><w:jc w:val="right"/>', f'<w:color w:val="{CINZA}"/>'),
    ("TituloListaNT", "Título de lista NT", '<w:keepNext/><w:spacing w:before="480" w:after="200"/>',
     f'<w:b/><w:bCs/><w:caps/><w:color w:val="{VERDE}"/><w:sz w:val="28"/><w:szCs w:val="28"/>'),
    ("SubtituloNT", "Subtítulo NT", '<w:keepNext/><w:spacing w:before="160" w:after="80"/>',
     f'<w:b/><w:bCs/><w:color w:val="{VERDE2}"/>'),
    ("LegendaQuadro", "LegendaQuadro", '<w:keepNext/><w:spacing w:before="200" w:after="80" w:line="240" w:lineRule="auto"/>',
     f'<w:color w:val="{VERDE}"/><w:sz w:val="20"/><w:szCs w:val="20"/>'),
    ("LegendaFigura", "LegendaFigura", '<w:keepNext/><w:spacing w:before="200" w:after="80" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>',
     f'<w:color w:val="{VERDE}"/><w:sz w:val="20"/><w:szCs w:val="20"/>'),
    ("FonteLegenda", "FonteLegenda", '<w:spacing w:before="40" w:after="40" w:line="240" w:lineRule="auto"/><w:jc w:val="both"/>',
     f'<w:color w:val="{CINZA}"/><w:sz w:val="17"/><w:szCs w:val="17"/>'),
    ("FiguraNT", "Figura NT", '<w:keepNext/><w:spacing w:before="60" w:after="60" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>', ""),
    ("ListaNT", "Lista NT", '<w:numPr><w:numId w:val="900"/></w:numPr><w:spacing w:after="80"/><w:jc w:val="both"/>', ""),
    ("ListaNumNT", "Lista numerada NT", '<w:spacing w:after="80"/><w:jc w:val="both"/>', ""),
    ("ProposicaoNT", "Proposição NT", '<w:tabs><w:tab w:val="left" w:pos="567"/></w:tabs><w:spacing w:after="140"/><w:ind w:left="567" w:hanging="567"/><w:jc w:val="both"/>', ""),
    ("CaixaDestaqueNT", "Caixa destaque NT", _caixa(CAIXA_VERDE) + '<w:spacing w:before="120" w:after="120"/><w:ind w:left="170" w:right="113"/><w:jc w:val="both"/>', ""),
    ("CaixaFundamentoNT", "Caixa fundamento NT", _caixa(CAIXA_CINZA) + '<w:spacing w:before="100" w:after="100" w:line="264" w:lineRule="auto"/><w:ind w:left="170" w:right="113"/><w:jc w:val="both"/>',
     '<w:sz w:val="21"/><w:szCs w:val="21"/>'),
    ("CaixaRiscoNT", "Caixa risco NT", _caixa(CAIXA_RISCO) + '<w:spacing w:before="100" w:after="100" w:line="264" w:lineRule="auto"/><w:ind w:left="170" w:right="113"/><w:jc w:val="both"/>',
     '<w:sz w:val="21"/><w:szCs w:val="21"/>'),
    ("RecomendacaoNT", "Recomendação NT",
     f'<w:keepNext/><w:pBdr>{_borda("top", CAIXA_REC)}{_borda("left", AMBAR, 36, 8)}{_borda("bottom", CAIXA_REC)}</w:pBdr>'
     f'<w:shd w:val="clear" w:color="auto" w:fill="{CAIXA_REC}"/><w:spacing w:before="480" w:after="200" w:line="264" w:lineRule="auto"/><w:ind w:left="170" w:right="113"/>',
     f'<w:b/><w:bCs/><w:color w:val="{VERDE}"/><w:sz w:val="24"/><w:szCs w:val="24"/>'),
    ("FaixaUrgenteNT", "Faixa urgente NT", "<w:keepNext/>" + _caixa("FBEAEA", ALERTA) + '<w:spacing w:after="80"/><w:ind w:left="567" w:hanging="284"/><w:jc w:val="both"/>', ""),
    ("FaixaPrioritarioNT", "Faixa prioritário NT", "<w:keepNext/>" + _caixa("FFF3DF", AMBAR) + '<w:spacing w:after="80"/><w:ind w:left="567" w:hanging="284"/><w:jc w:val="both"/>', ""),
    ("FaixaDesejavelNT", "Faixa desejável NT", "<w:keepNext/>" + _caixa("E7F0F8", "2F6E9E") + '<w:spacing w:after="80"/><w:ind w:left="567" w:hanging="284"/><w:jc w:val="both"/>', ""),
    ("FechoNT", "Fecho NT", '<w:keepNext/><w:spacing w:before="360" w:after="0"/>', ""),
    ("AssinaturaNomeNT", "Assinatura nome NT", f'<w:keepNext/><w:pBdr>{_borda("top", TEXTO, 4, 1)}</w:pBdr><w:spacing w:before="760" w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="1700" w:right="1700"/><w:jc w:val="center"/>',
     "<w:b/><w:bCs/>"),
    ("AssinaturaCargoNT", "Assinatura cargo NT", '<w:spacing w:before="20" w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>',
     f'<w:color w:val="{CINZA}"/><w:sz w:val="21"/><w:szCs w:val="21"/>'),
    ("CodigoNT", "Código NT", _caixa(CAIXA_CINZA) + '<w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="170"/>',
     '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/><w:sz w:val="17"/><w:szCs w:val="17"/>'),
]

NOMES = {}  # styleId → nome (preenchido abaixo); python-docx procura estilos pelo nome


def E(sid: str) -> str:
    return NOMES.get(sid, sid)


TITULOS = {  # styleId: (nome, pPr, rPr)
    "Heading1": ("heading 1", f'<w:keepNext/><w:pBdr>{_borda("bottom", VERDE, 8, 4)}</w:pBdr><w:spacing w:before="360" w:after="160"/><w:outlineLvl w:val="0"/>',
                 f'<w:b/><w:bCs/><w:caps/><w:color w:val="{VERDE}"/><w:sz w:val="28"/><w:szCs w:val="28"/>'),
    "Heading2": ("heading 2", '<w:keepNext/><w:spacing w:before="320" w:after="140"/><w:outlineLvl w:val="1"/>',
                 f'<w:b/><w:bCs/><w:color w:val="{VERDE}"/><w:sz w:val="27"/><w:szCs w:val="27"/>'),
    "Heading3": ("heading 3", '<w:keepNext/><w:spacing w:before="260" w:after="120"/><w:outlineLvl w:val="2"/>',
                 f'<w:b/><w:bCs/><w:color w:val="{VERDE2}"/><w:sz w:val="24"/><w:szCs w:val="24"/>'),
    "Heading4": ("heading 4", '<w:keepNext/><w:spacing w:before="200" w:after="100"/><w:outlineLvl w:val="3"/>',
                 '<w:b/><w:bCs/><w:i/><w:iCs/>'),
}


NOMES.update({sid: nome for sid, nome, _, _ in ESTILOS})


def garantir_estilos(d, novo: bool) -> None:
    st = d.styles.element
    if novo:
        dd = st.find(qn("w:docDefaults"))
        if dd is not None:
            st.remove(dd)
        st.insert(0, parse_xml(
            f'<w:docDefaults {nsdecls("w")}><w:rPrDefault><w:rPr>'
            '<w:rFonts w:ascii="Calibri" w:eastAsia="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>'
            f'<w:color w:val="{TEXTO}"/><w:sz w:val="23"/><w:szCs w:val="23"/>'
            '<w:lang w:val="pt-BR" w:eastAsia="pt-BR" w:bidi="ar-SA"/></w:rPr></w:rPrDefault>'
            '<w:pPrDefault><w:pPr><w:spacing w:after="140" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault>'
            '</w:docDefaults>'))
        normal = d.styles["Normal"].element
        for tag in ("w:pPr", "w:rPr"):
            x = normal.find(qn(tag))
            if x is not None:
                normal.remove(x)
        for sid, (nome, ppr, rpr) in TITULOS.items():
            antigo = st.find(f'{qn("w:style")}[@{qn("w:styleId")}="{sid}"]')
            if antigo is not None:
                st.remove(antigo)
            st.append(parse_xml(
                f'<w:style {nsdecls("w")} w:type="paragraph" w:styleId="{sid}"><w:name w:val="{nome}"/>'
                f'<w:basedOn w:val="Normal"/><w:next w:val="CorpoNT"/><w:uiPriority w:val="9"/><w:qFormat/>'
                f'<w:pPr>{ppr}</w:pPr><w:rPr>{rpr}</w:rPr></w:style>'))
    existentes = {s.get(qn("w:styleId")) for s in st.findall(qn("w:style"))}
    for sid, nome, ppr, rpr in ESTILOS:
        if sid not in existentes:
            st.append(parse_xml(_estilo_xml(sid, nome, ppr, rpr)))
    garantir_numeracao(d)


def garantir_numeracao(d) -> None:
    num = d.part.numbering_part.element
    if num.find(f'{qn("w:num")}[@{qn("w:numId")}="900"]') is not None:
        return
    def lvl(i, fmt, txt, left, hang):
        return (f'<w:lvl w:ilvl="{i}"><w:start w:val="1"/><w:numFmt w:val="{fmt}"/><w:lvlText w:val="{txt}"/>'
                f'<w:lvlJc w:val="left"/><w:pPr><w:ind w:left="{left}" w:hanging="{hang}"/></w:pPr>'
                + ('<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:hint="default"/></w:rPr>' if fmt == "bullet" else "")
                + "</w:lvl>")
    marcadores = lvl(0, "bullet", "•", 567, 284) + lvl(1, "bullet", "◦", 1134, 284)
    numeros = lvl(0, "decimal", "%1.", 567, 425) + lvl(1, "lowerLetter", "%2)", 1134, 425)
    abst = [parse_xml(f'<w:abstractNum {nsdecls("w")} w:abstractNumId="900"><w:multiLevelType w:val="hybridMultilevel"/>{marcadores}</w:abstractNum>'),
            parse_xml(f'<w:abstractNum {nsdecls("w")} w:abstractNumId="901"><w:multiLevelType w:val="hybridMultilevel"/>{numeros}</w:abstractNum>')]
    primeiro_num = num.find(qn("w:num"))
    for a in abst:
        if primeiro_num is not None:
            primeiro_num.addprevious(a)
        else:
            num.append(a)
    num.append(parse_xml(f'<w:num {nsdecls("w")} w:numId="900"><w:abstractNumId w:val="900"/></w:num>'))


def nova_lista_numerada(d) -> int:
    num = d.part.numbering_part.element
    ids = [int(n.get(qn("w:numId"))) for n in num.findall(qn("w:num"))]
    nid = max(ids + [900]) + 1
    num.append(parse_xml(f'<w:num {nsdecls("w")} w:numId="{nid}"><w:abstractNumId w:val="901"/>'
                         '<w:lvlOverride w:ilvl="0"><w:startOverride w:val="1"/></w:lvlOverride></w:num>'))
    return nid


# ------------------------------------------------------------------ texto inline
RE_TOKEN = re.compile(r"(\\\*|\*\*\*|\*\*|(?<![\w*])\*(?=\S)|(?<=\S)\*(?![\w*])|`|<br\s*/?>|⚠️|⚠)")


def escrever_inline(p, texto: str, negrito=False, italico=False, tam=None, cor=None):
    texto = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", texto)
    b, it, cod = negrito, italico, False
    for parte in RE_TOKEN.split(texto):
        if not parte:
            continue
        if parte == "\\*":
            parte_txt = "*"
        elif parte in ("***",) and not cod:
            b, it = not b, not it
            continue
        elif parte == "**" and not cod:
            b = not b
            continue
        elif parte == "*" and not cod:
            it = not it
            continue
        elif parte == "`":
            cod = not cod
            continue
        elif re.match(r"<br\s*/?>", parte):
            p.add_run().add_break()
            continue
        elif parte in ("⚠️", "⚠"):
            r = p.add_run("⚠")
            r.font.name = "Segoe UI Symbol"
            r._element.rPr.rFonts.set(qn("w:eastAsia"), "Segoe UI Symbol")
            r.font.color.rgb = RGBColor.from_string(ALERTA)
            if tam:
                r.font.size = tam
            continue
        else:
            parte_txt = parte
        r = p.add_run(parte_txt)
        r.bold = b or None
        r.italic = it or None
        if cod:
            r.font.name = "Consolas"
        if tam:
            r.font.size = tam
        if cor:
            r.font.color.rgb = RGBColor.from_string(cor)


def rotulo_e_resto(texto: str) -> tuple[str, str] | None:
    """'**Quadro 3 — Título**' → ('Quadro 3 — ', 'Título')."""
    t = texto.strip()
    m = re.match(r"^\*\*(.+?)\*\*(.*)$", t)
    corpo = (m.group(1) + m.group(2)) if m else t
    corpo = limpar_md(corpo) if m else corpo
    m2 = re.match(r"^((?:Quadro|Tabela|Figura)(?:\s+[\w.-]+)?\s*[—–-]\s*)(.*)$", corpo)
    if m2:
        return m2.group(1), m2.group(2)
    return None


# ------------------------------------------------------------------ seções
def _sectpr_base(d):
    return d.element.body.find(qn("w:sectPr"))


def novo_sectpr(d, paisagem: bool):
    """Cópia do sectPr final. Seção retrato reaproveita o cabeçalho/rodapé do documento; a paisagem
    fica sem referência e recebe cabeçalho/rodapé próprios em normalizar_secoes (tabulação mais larga)."""
    s = copy.deepcopy(_sectpr_base(d))
    tags = ("w:headerReference", "w:footerReference", "w:titlePg") if paisagem else ("w:titlePg",)
    for tag in tags:
        for x in s.findall(qn(tag)):
            s.remove(x)
    pg = s.find(qn("w:pgSz"))
    if pg is None:
        pg = parse_xml(f'<w:pgSz {nsdecls("w")}/>')
        refs = [c for c in s if c.tag in (qn("w:headerReference"), qn("w:footerReference"), qn("w:type"))]
        s.insert(len(refs), pg)
    if paisagem:
        pg.set(qn("w:w"), str(PAG_H)); pg.set(qn("w:h"), str(PAG_W)); pg.set(qn("w:orient"), "landscape")
    else:
        pg.set(qn("w:w"), str(PAG_W)); pg.set(qn("w:h"), str(PAG_H))
        if pg.get(qn("w:orient")) is not None:
            del pg.attrib[qn("w:orient")]
    if s.find(qn("w:type")) is None:  # depois das referências de cabeçalho/rodapé (ordem do esquema)
        refs = [c for c in s if c.tag in (qn("w:headerReference"), qn("w:footerReference"))]
        s.insert(len(refs), parse_xml(f'<w:type {nsdecls("w")} w:val="nextPage"/>'))
    return s


def quebra_secao(d, paisagem_da_secao_que_termina: bool):
    p = d.add_paragraph()
    p._p.get_or_add_pPr().append(novo_sectpr(d, paisagem_da_secao_que_termina))
    return p


def configurar_pagina(sec):
    sec.page_width, sec.page_height = Twips(PAG_W), Twips(PAG_H)
    sec.orientation = WD_ORIENT.PORTRAIT
    sec.top_margin, sec.bottom_margin = Twips(MARG["top"]), Twips(MARG["bottom"])
    sec.left_margin, sec.right_margin = Twips(MARG["left"]), Twips(MARG["right"])
    sec.header_distance, sec.footer_distance = Twips(MARG["header"]), Twips(MARG["footer"])


def _campo(p, instr, tam, cor):
    for tipo, val in (("begin", None), ("instr", instr), ("separate", None), ("txt", "1"), ("end", None)):
        r = p.add_run()
        r.font.size, r.font.color.rgb = tam, RGBColor.from_string(cor)
        if tipo == "instr":
            r._r.append(parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> {val} </w:instrText>'))
        elif tipo == "txt":
            r.text = val
        else:
            r._r.append(parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="{tipo}"/>'))


def preencher_cabecalho_rodape(sec, rodape_txt: str, largura: int):
    tam = Pt(7.5)
    h = sec.header.paragraphs[0]
    h.text = ""
    ppr = h._p.get_or_add_pPr()
    ppr.append(parse_xml(f'<w:pBdr {nsdecls("w")}>{_borda("bottom", VERDE, 6, 4)}</w:pBdr>'))
    ppr.append(parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="clear" w:pos="4680"/><w:tab w:val="clear" w:pos="9360"/>'
                         f'<w:tab w:val="right" w:pos="{largura}"/></w:tabs>'))
    ppr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:after="0"/>'))
    r = h.add_run("INSTITUTO CHICO MENDES DE CONSERVAÇÃO DA BIODIVERSIDADE")
    r.bold, r.font.size, r.font.color.rgb = True, tam, RGBColor.from_string(VERDE)
    r = h.add_run("\tCGOV · CGGE")
    r.font.size, r.font.color.rgb = tam, RGBColor.from_string(CINZA)
    f = sec.footer.paragraphs[0]
    f.text = ""
    ppr = f._p.get_or_add_pPr()
    ppr.append(parse_xml(f'<w:pBdr {nsdecls("w")}>{_borda("top", BORDA, 4, 4)}</w:pBdr>'))
    ppr.append(parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="clear" w:pos="4680"/><w:tab w:val="clear" w:pos="9360"/>'
                         f'<w:tab w:val="right" w:pos="{largura}"/></w:tabs>'))
    r = f.add_run(rodape_txt + "\tPágina ")
    r.font.size, r.font.color.rgb = tam, RGBColor.from_string(CINZA)
    _campo(f, "PAGE", tam, CINZA)
    r = f.add_run(" de ")
    r.font.size, r.font.color.rgb = tam, RGBColor.from_string(CINZA)
    _campo(f, "NUMPAGES", tam, CINZA)


def copiar_cabecalho(origem_sec, destino_sec, largura: int):
    for o, dst in ((origem_sec.header, destino_sec.header), (origem_sec.footer, destino_sec.footer)):
        dst.is_linked_to_previous = False
        el = dst._element
        for c in list(el):
            el.remove(c)
        for c in o._element:
            novo = copy.deepcopy(c)
            for tab in novo.iter(qn("w:tab")):
                if tab.get(qn("w:val")) == "right" and tab.get(qn("w:pos")):
                    tab.set(qn("w:pos"), str(largura))
            el.append(novo)


def normalizar_secoes(d):
    """Seções paisagem e as que voltam ao retrato recebem cabeçalho/rodapé próprios (tabulação certa)."""
    secs = list(d.sections)
    ref = secs[0]
    for i, s in enumerate(secs[1:], start=1):
        pais = s.orientation == WD_ORIENT.LANDSCAPE or (s.page_width and s.page_height and s.page_width > s.page_height)
        ant_pais = secs[i - 1].page_width > secs[i - 1].page_height
        if pais or ant_pais:
            if s.header.is_linked_to_previous or s.footer.is_linked_to_previous:  # sem cabeçalho próprio
                largura = (LARG_PAISAGEM if pais else LARG_RETRATO)
                copiar_cabecalho(ref, s, largura)


# ------------------------------------------------------------------ tabelas
def ler_tabela(linhas):
    def celulas(l):
        l = l.strip().strip("|")
        return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", l)]
    cab = celulas(linhas[0])
    alin = []
    corpo_ini = 1
    if len(linhas) > 1 and re.match(r"^\|?\s*:?-{2,}", linhas[1]):
        for c in celulas(linhas[1]):
            alin.append("center" if c.startswith(":") and c.endswith(":") else ("right" if c.endswith(":") else None))
        corpo_ini = 2
    corpo = [celulas(l) for l in linhas[corpo_ini:]]
    n = len(cab)
    corpo = [(r + [""] * n)[:n] for r in corpo]
    return cab, corpo, (alin + [None] * n)[:n]


def _tcpr(cell, largura, fundo):
    tc = cell._tc
    antigo = tc.find(qn("w:tcPr"))
    if antigo is not None:
        tc.remove(antigo)
    tc.insert(0, parse_xml(
        f'<w:tcPr {nsdecls("w")}><w:tcW w:w="{largura}" w:type="dxa"/>'
        f'<w:shd w:val="clear" w:color="auto" w:fill="{fundo}"/>'
        '<w:tcMar><w:top w:w="50" w:type="dxa"/><w:left w:w="85" w:type="dxa"/>'
        '<w:bottom w:w="50" w:type="dxa"/><w:right w:w="85" w:type="dxa"/></w:tcMar>'
        '<w:vAlign w:val="center"/></w:tcPr>'))


def larguras(cab, corpo, total, tam_pt=8.5):
    """Mínimo = a palavra mais longa da coluna cabe inteira; o restante é repartido pelo volume de texto."""
    por_char = tam_pt * 20 * 0.55          # largura média de um caractere Calibri, em twips
    minimos, pesos = [], []
    for j in range(len(cab)):
        textos = [limpar_md(cab[j])] + [limpar_md(r[j]) for r in corpo]
        palavra = max((len(w) for t in textos for w in t.split()), default=1)
        minimos.append(int(max(3, palavra) * por_char + 220))
        comps = [len(limpar_md(r[j])) for r in corpo] or [0]
        pesos.append(max(1.0, sum(comps) / len(comps)))
    soma_min = sum(minimos)
    if soma_min >= total:
        w = [int(total * m / soma_min) for m in minimos]
    else:
        livre = total - soma_min
        soma_p = sum(pesos)
        w = [m + int(livre * p / soma_p) for m, p in zip(minimos, pesos)]
    w[-1] += total - sum(w)
    return w


def quer_paisagem(linhas, orient) -> bool:
    if orient:
        return orient == "paisagem"
    cab, corpo, _ = ler_tabela(linhas)
    media = sum(len(limpar_md(" ".join(r))) for r in corpo) / max(1, len(corpo))
    return len(cab) >= COLUNAS_PAISAGEM or (len(cab) >= TEXTO_PAISAGEM[0] and media >= TEXTO_PAISAGEM[1])


def chave_prioridade(txt: str):
    k = sem_acento(limpar_md(txt)).lower().strip(" .")
    return PRIORIDADES.get(k)


def escrever_tabela(d, linhas, largura_total):
    cab, corpo, alin = ler_tabela(linhas)
    ncol = len(cab)
    tam = Pt(8.5) if ncol >= 6 else Pt(9)
    w = larguras(cab, corpo, largura_total, tam.pt)
    t = d.add_table(rows=1 + len(corpo), cols=ncol)
    tblpr = t._tbl.tblPr
    for x in list(tblpr):
        tblpr.remove(x)
    bordas = "".join(f'<w:{l} w:val="single" w:sz="4" w:space="0" w:color="{BORDA}"/>'
                     for l in ("top", "left", "bottom", "right", "insideH", "insideV"))
    tblpr.append(parse_xml(f'<w:tblW {nsdecls("w")} w:w="{largura_total}" w:type="dxa"/>'))
    tblpr.append(parse_xml(f'<w:tblBorders {nsdecls("w")}>{bordas}</w:tblBorders>'))
    tblpr.append(parse_xml(f'<w:tblLayout {nsdecls("w")} w:type="fixed"/>'))
    tblpr.append(parse_xml(f'<w:tblLook {nsdecls("w")} w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'))
    grid = t._tbl.tblGrid
    for j, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(w[j]))
    curtas = [all(len(limpar_md(r[j])) <= 12 for r in corpo) and corpo for j in range(ncol)]
    for i, row in enumerate(t.rows):
        trpr = row._tr.get_or_add_trPr()
        trpr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if i == 0:
            trpr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        dados = cab if i == 0 else corpo[i - 1]
        for j, cell in enumerate(row.cells):
            txt = dados[j]
            prio = chave_prioridade(txt) if i > 0 else None
            fundo = VERDE if i == 0 else (prio[1] if prio else ("FFFFFF" if i % 2 else ZEBRA))
            _tcpr(cell, w[j], fundo)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.first_line_indent = Pt(0)
            if i == 0 or prio or curtas[j] or alin[j] == "center":
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            elif alin[j] == "right":
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            if i == 0:
                escrever_inline(p, txt, negrito=True, tam=Pt(9), cor="FFFFFF")
            elif prio:
                escrever_inline(p, txt, negrito=True, tam=tam, cor=prio[0])
            else:
                escrever_inline(p, txt, tam=tam)
    return t


# ------------------------------------------------------------------ figuras
def renderizar_mermaid(codigo: str) -> Path | None:
    mmdc = shutil.which("mmdc")
    if not mmdc:
        return None
    tmp = Path(tempfile.mkdtemp(prefix="nt_mermaid_"))
    (tmp / "d.mmd").write_text(codigo, encoding="utf-8")
    (tmp / "p.json").write_text('{"args":["--no-sandbox"]}', encoding="utf-8")
    try:
        subprocess.run([mmdc, "-i", str(tmp / "d.mmd"), "-o", str(tmp / "d.png"), "-w", "1800", "-b", "white",
                        "-p", str(tmp / "p.json")], check=True, capture_output=True, timeout=120)
        return tmp / "d.png" if (tmp / "d.png").exists() else None
    except (subprocess.SubprocessError, OSError):
        return None


def inserir_imagem(d, caminho: Path, largura_max_cm: float, rel: dict):
    p = d.add_paragraph(style=E("FiguraNT"))
    r = p.add_run()
    pic = r.add_picture(str(caminho))
    if pic.width > Cm(largura_max_cm):
        prop = Cm(largura_max_cm) / pic.width
        pic.width, pic.height = Cm(largura_max_cm), int(pic.height * prop)
    if pic.height > Cm(19.5):  # legenda, figura e fonte cabem juntas na página
        prop = Cm(19.5) / pic.height
        pic.height, pic.width = Cm(19.5), int(pic.width * prop)
    rel["figuras_inseridas"] += 1


def marcador_figura(d, motivo: str, rel: dict):
    p = d.add_paragraph(style=E("CaixaRiscoNT"))
    escrever_inline(p, f"⚠ **Figura a inserir:** {motivo}")
    rel["avisos"].append(f"Figura não inserida: {motivo}")


# ------------------------------------------------------------------ renderização
def campo_toc(d, instr: str, titulo: str):
    p = d.add_paragraph(titulo, style=E("TituloListaNT"))
    p = d.add_paragraph()
    _campo(p, instr, None, TEXTO)
    # texto de espera visível até a atualização dos campos
    for r in p.runs:
        if r.text == "1":
            r.text = "Atualize este campo (F9 ou abrir o documento e aceitar a atualização)."
            r.italic = True
            r.font.color.rgb = RGBColor.from_string(CINZA)


def tipo_paragrafo(texto: str) -> str:
    t = texto.strip()
    tl = sem_acento(limpar_md(t)).lower()
    if re.match(r"^\*\*Nota T[ée]cnica n", t) or re.match(r"^Nota T[ée]cnica n[ºo°]", t):
        return "titulo_nt"
    if re.match(r"^Bras[ií]lia", t):
        return "data"
    if re.match(r"^\*{0,2}Assunto:?", t):
        return "assunto"
    if re.match(r"^\*{0,2}Processo SEI", t):
        return "processo"
    if re.match(r"^\*\*Recomenda[çc][ãa]o n", t):
        return "recomendacao"
    if re.match(r"^\*\*Fundamento normativo", t):
        return "fundamento"
    if re.match(r"^\*\*Risco institucional", t):
        return "risco"
    if re.match(r"^\*\*Total", t):
        return "destaque"
    if re.match(r"^\*{0,2}_?(Fonte|Legenda|Nota)s?:", t) or re.match(r"^\*(Fonte|Legenda):", t):
        return "fonte"
    if re.match(r"^\((?:[ivxlc]+)\)\s", t):
        return "proposicao"
    if tl.startswith("a consideracao superior"):
        return "fecho"
    r = rotulo_e_resto(t)
    if r and t.startswith("**"):
        return "legenda_figura" if r[0].startswith("Figura") else "legenda_quadro"
    if re.match(r"^\*\*[^*]+\*\*:?$", t) and len(t) < 90 and not t.rstrip("*").endswith("."):
        return "subtitulo"
    return "corpo"


def renderizar_unidade(d, unidade, ctx, rel):
    blocos = unidade["blocos"]
    lista_num = None
    pendente_assinatura = False
    abertura = {"titulo": None, "data": None, "assunto": None, "processo": None}
    paisagem_aberta = False
    ultima_legenda = None
    for k, b in enumerate(blocos):
        tp = b["tipo"]
        if tp != "item":
            lista_num = None
        if tp == "titulo":
            if paisagem_aberta:
                quebra_secao(d, True); paisagem_aberta = False
            texto = limpar_md(b["texto"])
            nivel = {2: 1, 3: 2, 4: 3}.get(b["nivel"], 4)
            if b["nivel"] == 5:
                d.add_paragraph(texto, style=E("SubtituloNT"))
            else:
                d.add_paragraph(texto, style=f"Heading {nivel}")
            if nivel == 1 and texto.startswith("1.") and ctx["novo"] and not ctx.get("abertura_feita"):
                pass
            continue
        if tp == "par":
            linhas = b["linhas"]
            texto = " ".join(linhas)
            tipo = tipo_paragrafo(linhas[0])
            if pendente_assinatura and tipo in ("corpo", "subtitulo"):
                # pares nome/cargo (linhas consecutivas) do bloco de assinaturas
                pares = [limpar_md(x) for x in linhas]
                for idx in range(0, len(pares), 2):
                    p = d.add_paragraph(style=E("AssinaturaNomeNT"))
                    escrever_inline(p, pares[idx])
                    if idx + 1 < len(pares):
                        p = d.add_paragraph(style=E("AssinaturaCargoNT"))
                        escrever_inline(p, pares[idx + 1])
                continue
            if tipo in ("titulo_nt", "data", "assunto", "processo"):
                # a abertura pode vir em linhas consecutivas do mesmo parágrafo Markdown
                for ln in linhas:
                    tl = tipo_paragrafo(ln)
                    if tl in abertura:
                        abertura[tl] = ln
                    elif tl == "titulo_nt":
                        abertura["titulo"] = ln
                    elif tl == "data":
                        abertura["data"] = ln
                    elif abertura["assunto"] and not abertura["processo"]:
                        abertura["assunto"] += " " + ln
                if abertura["titulo"] and (k + 1 >= len(blocos) or blocos[k + 1]["tipo"] != "par"
                                           or tipo_paragrafo(blocos[k + 1]["linhas"][0]) not in ("data", "assunto", "processo", "titulo_nt")):
                    escrever_abertura(d, abertura, ctx, rel)
                continue
            if tipo == "recomendacao":
                p = d.add_paragraph(style=E("RecomendacaoNT"))
                m = re.match(r"^\*\*(.+?)\*\*\s*(?:·\s*)?(.*)$", texto)
                escrever_inline(p, m.group(1) if m else limpar_md(texto))
                resto = limpar_md(m.group(2)) if m else ""
                if resto:
                    prio = chave_prioridade(resto)
                    escrever_inline(p, "  ·  " + resto, negrito=True, tam=Pt(10), cor=prio[0] if prio else AMBAR)
                continue
            if tipo in ("fundamento", "risco"):
                for ln in linhas:  # cada rótulo em sua caixa
                    tl = tipo_paragrafo(ln)
                    estilo = E("CaixaRiscoNT" if tl == "risco" else "CaixaFundamentoNT")
                    p = d.add_paragraph(style=estilo)
                    escrever_inline(p, ln)
                continue
            if tipo == "fonte":
                for ln in linhas:
                    p = d.add_paragraph(style=E("FonteLegenda"))
                    m = re.match(r"^[*_]{0,2}((?:Fonte|Legenda|Notas?):)[*_]{0,2}\s*(.*)$", ln.strip())
                    if m:
                        escrever_inline(p, m.group(1) + " ", negrito=True)
                        escrever_inline(p, m.group(2).rstrip("*_"))
                    else:
                        escrever_inline(p, ln)
                seguinte = blocos[k + 1] if k + 1 < len(blocos) else None
                mais_fonte = seguinte and seguinte["tipo"] == "par" and tipo_paragrafo(seguinte["linhas"][0]) == "fonte"
                if paisagem_aberta and ultima_legenda == "quadro" and not mais_fonte:
                    quebra_secao(d, True); paisagem_aberta = False
                continue
            if tipo in ("legenda_quadro", "legenda_figura"):
                rot, resto = rotulo_e_resto(texto)
                eh_quadro = tipo == "legenda_quadro"
                if eh_quadro:
                    prox = next((x for x in blocos[k + 1:k + 3] if x["tipo"] == "tabela"), None)
                    if prox is not None:
                        quer = quer_paisagem(prox["linhas"], prox.get("orient"))
                        if quer and not paisagem_aberta:
                            quebra_secao(d, False); paisagem_aberta = True
                        prox["_paisagem"] = quer
                    n = re.search(r"\d+", rot)
                    if n:
                        rel["quadros"].append(int(n.group()))
                else:
                    n = re.search(r"\d+", rot)
                    if n:
                        rel["figuras"].append(int(n.group()))
                p = d.add_paragraph(style=E("LegendaQuadro") if eh_quadro else "LegendaFigura")
                escrever_inline(p, rot, negrito=True)
                escrever_inline(p, resto)
                ultima_legenda = "quadro" if eh_quadro else "figura"
                continue
            if tipo == "proposicao":
                m = re.match(r"^(\([ivxlc]+\))\s+(.*)$", texto)
                p = d.add_paragraph(style=E("ProposicaoNT"))
                escrever_inline(p, m.group(1), negrito=True, cor=VERDE)
                p.add_run("\t")
                escrever_inline(p, m.group(2))
                continue
            if tipo == "fecho":
                p = d.add_paragraph(style=E("FechoNT"))
                escrever_inline(p, texto)
                pendente_assinatura = True
                continue
            if tipo == "subtitulo":
                p = d.add_paragraph(style=E("SubtituloNT"))
                escrever_inline(p, limpar_md(linhas[0]))
                if len(linhas) > 1:  # ex.: "**1. Quesito?**" seguido de "R: …" na linha de baixo
                    p = d.add_paragraph(style=E("CorpoNT"))
                    escrever_inline(p, " ".join(linhas[1:]))
                continue
            if tipo == "destaque":
                p = d.add_paragraph(style=E("CaixaDestaqueNT"))
                escrever_inline(p, texto)
                continue
            p = d.add_paragraph(style=E("CorpoNT"))
            escrever_inline(p, texto)
            if texto.rstrip().endswith(":"):
                p.paragraph_format.keep_with_next = True
            continue
        if tp == "item":
            txt = b["texto"]
            mprio = re.match(r"^\*\*(Urgente|Priorit[áa]ri[oa]|Desej[áa]vel):?\*\*:?", txt)
            if mprio:
                chave = sem_acento(mprio.group(1)).lower()
                estilo = {"urgente": "FaixaUrgenteNT", "prioritario": "FaixaPrioritarioNT",
                          "prioritaria": "FaixaPrioritarioNT", "desejavel": "FaixaDesejavelNT"}[chave]
                cor = PRIORIDADES[chave][0]
                p = d.add_paragraph(style=E(estilo))
                r = p.add_run("■\t")
                r.font.color.rgb = RGBColor.from_string(cor)
                rot = txt[:mprio.end()]
                escrever_inline(p, limpar_md(rot).rstrip(":") + ":", negrito=True, cor=cor)
                escrever_inline(p, txt[mprio.end():])
                continue
            if b["ordenado"]:
                if lista_num is None:
                    lista_num = nova_lista_numerada(d)
                p = d.add_paragraph(style=E("ListaNumNT"))
                ppr = p._p.get_or_add_pPr()
                ppr.insert(1, parse_xml(f'<w:numPr {nsdecls("w")}><w:ilvl w:val="{b["nivel"]}"/><w:numId w:val="{lista_num}"/></w:numPr>'))
            else:
                p = d.add_paragraph(style=E("ListaNT"))
                if b["nivel"]:
                    ppr = p._p.get_or_add_pPr()
                    ppr.insert(1, parse_xml(f'<w:numPr {nsdecls("w")}><w:ilvl w:val="1"/><w:numId w:val="900"/></w:numPr>'))
            escrever_inline(p, txt)
            continue
        if tp == "citacao":
            p = d.add_paragraph(style=E("CaixaDestaqueNT"))
            escrever_inline(p, b["texto"])
            continue
        if tp == "tabela":
            pais = b.get("_paisagem")
            if pais is None:
                pais = quer_paisagem(b["linhas"], b.get("orient"))
                if pais and not paisagem_aberta:
                    quebra_secao(d, False); paisagem_aberta = True
                rel["avisos"].append(f"Tabela sem legenda 'Quadro N — título' ({' | '.join(ler_tabela(b['linhas'])[0])[:60]}…)")
            escrever_tabela(d, b["linhas"], LARG_PAISAGEM if pais else LARG_RETRATO)
            ultima_legenda = "quadro"
            # se não houver Fonte logo após, fecha a seção paisagem aqui
            seguinte = blocos[k + 1] if k + 1 < len(blocos) else None
            if paisagem_aberta and not (seguinte and seguinte["tipo"] == "par" and tipo_paragrafo(seguinte["linhas"][0]) == "fonte"):
                quebra_secao(d, True); paisagem_aberta = False
            continue
        if tp == "imagem":
            caminho = Path(b["caminho"])
            if not caminho.is_absolute():
                caminho = Path(b["origem"]).parent / caminho
            if caminho.exists():
                inserir_imagem(d, caminho, 16.0, rel)
            else:
                marcador_figura(d, f"arquivo não encontrado: {b['caminho']}", rel)
            continue
        if tp == "codigo":
            if b["lang"] == "mermaid":
                png = renderizar_mermaid(b["texto"])
                if png:
                    inserir_imagem(d, png, 16.0, rel)
                else:
                    marcador_figura(d, f"diagrama Mermaid não renderizado (sem o comando mmdc); fonte em {Path(b['origem']).name}", rel)
            else:
                for ln in b["texto"].split("\n"):
                    p = d.add_paragraph(style=E("CodigoNT"))
                    p.add_run(ln)
            continue
    if paisagem_aberta:
        quebra_secao(d, True)


def escrever_abertura(d, ab, ctx, rel):
    titulo = limpar_md(ab["titulo"] or "Nota Técnica nº [N]/[ANO]/CGOV/CGGE/GABIN/ICMBio")
    p = d.add_paragraph(style=E("TituloNT"))
    escrever_inline(p, titulo)
    d.add_paragraph(style=E("FileteNT"))
    if ab["data"]:
        p = d.add_paragraph(style=E("DataNT"))
        escrever_inline(p, limpar_md(ab["data"]))
    # caixa de Assunto (tabela de uma célula, barra verde à esquerda)
    t = d.add_table(rows=1, cols=1)
    tblpr = t._tbl.tblPr
    for x in list(tblpr):
        tblpr.remove(x)
    tblpr.append(parse_xml(f'<w:tblW {nsdecls("w")} w:w="{LARG_RETRATO}" w:type="dxa"/>'))
    tblpr.append(parse_xml(f'<w:tblLayout {nsdecls("w")} w:type="fixed"/>'))
    t._tbl.tblGrid.findall(qn("w:gridCol"))[0].set(qn("w:w"), str(LARG_RETRATO))
    c = t.rows[0].cells[0]
    tc = c._tc
    antigo = tc.find(qn("w:tcPr"))
    if antigo is not None:
        tc.remove(antigo)
    tc.insert(0, parse_xml(
        f'<w:tcPr {nsdecls("w")}><w:tcW w:w="{LARG_RETRATO}" w:type="dxa"/><w:tcBorders>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{BORDA}"/><w:left w:val="single" w:sz="36" w:space="0" w:color="{VERDE}"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="{BORDA}"/><w:right w:val="single" w:sz="4" w:space="0" w:color="{BORDA}"/>'
        f'</w:tcBorders><w:shd w:val="clear" w:color="auto" w:fill="{CAIXA_VERDE}"/><w:tcMar><w:top w:w="200" w:type="dxa"/>'
        '<w:left w:w="280" w:type="dxa"/><w:bottom w:w="200" w:type="dxa"/><w:right w:w="280" w:type="dxa"/></w:tcMar>'
        '<w:vAlign w:val="center"/></w:tcPr>'))
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(8)
    assunto = re.sub(r"^\*{0,2}Assunto:?\*{0,2}:?\s*", "**Assunto:** ", ab["assunto"] or "Assunto: ⚠ [preencher]")
    escrever_inline(p, assunto)
    p = c.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    proc = re.sub(r"^\*{0,2}Processo SEI n[ºo°]\*{0,2}:?\s*", "**Processo SEI nº** ", ab["processo"] or "Processo SEI nº ⚠ [preencher]")
    escrever_inline(p, proc)
    campo_toc(d, 'TOC \\o "1-3" \\h \\z \\u', "Sumário")
    campo_toc(d, 'TOC \\h \\z \\t "LegendaQuadro;1"', "Lista de Quadros")
    campo_toc(d, 'TOC \\h \\z \\t "LegendaFigura;1"', "Lista de Figuras")
    p = d.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)
    ctx["abertura_feita"] = True


# ------------------------------------------------------------------ posicionamento no documento base
def _texto(el) -> str:
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


def _estilo(el) -> str | None:
    ps = el.find(f'{qn("w:pPr")}/{qn("w:pStyle")}')
    return ps.get(qn("w:val")) if ps is not None else None


def mapa_titulos(d):
    corpo = [e for e in d.element.body if e.tag != qn("w:sectPr")]
    tit = []
    for i, e in enumerate(corpo):
        if e.tag == qn("w:p") and (_estilo(e) or "").startswith("Heading"):
            tit.append((i, int(_estilo(e)[-1]), _texto(e).strip()))
    return corpo, tit


def localizar(d, chave):
    """Devolve (início, fim) do bloco existente ou (None, ponto de inserção)."""
    corpo, tit = mapa_titulos(d)
    n = len(corpo)

    def cap_de(t):
        m = re.match(r"^Cap[ií]tulo\s+(\d+)", t)
        return int(m.group(1)) if m else None

    if chave == ("abertura",):
        fim = next((i for i, nv, t in tit if (nv == 2 and (cap_de(t) or 0) > 1) or (nv == 1 and re.match(r"^5[.\s]", t))), n)
        tem = any(nv == 1 and re.match(r"^1[.\s]", t) for _, nv, t in tit)
        return (0, fim) if tem else (None, 0)
    if chave == ("conclusao",):
        ini = next((i for i, nv, t in tit if nv == 1 and re.match(r"^5[.\s]", t)), None)
        return (ini, n) if ini is not None else (None, n)
    if chave[0] == "cap":
        N = chave[1]
        ini = next((i for i, nv, t in tit if nv == 2 and cap_de(t) == N), None)
        if ini is not None:
            fim = next((i for i, nv, t in tit if i > ini and (nv == 1 or (nv == 2 and cap_de(t) is not None))), n)
            return ini, fim
        depois = next((i for i, nv, t in tit if (nv == 2 and (cap_de(t) or 0) > N) or (nv == 1 and re.match(r"^5[.\s]", t))), n)
        return None, depois
    if chave[0] == "sub":
        N = int(chave[1].split(".")[0])
        ini = next((i for i, nv, t in tit if nv == 3 and re.match(rf"^{re.escape(chave[1])}\b", t)), None)
        if ini is not None:
            fim = next((i for i, nv, t in tit if i > ini and nv <= 3), n)
            return ini, fim
        cap = next((i for i, nv, t in tit if nv == 2 and cap_de(t) == N), None)
        if cap is None:
            sys.exit(f"O Capítulo {N} ainda não está no documento base: gere o capítulo antes do subitem {chave[1]}.")
        fim_cap = next((i for i, nv, t in tit if i > cap and (nv == 1 or (nv == 2 and cap_de(t) is not None))), n)
        return None, fim_cap
    raise ValueError(chave)


def contar_legendas(elementos):
    q = f = 0
    for e in elementos:
        if e.tag == qn("w:p"):
            s = _estilo(e)
            q += s == "LegendaQuadro"
            f += s == "LegendaFigura"
    return q, f


# ------------------------------------------------------------------ principal
def montar(args) -> dict:
    pasta = Path(args.pasta) if args.pasta else Path(args.capitulos[0]).resolve().parent
    apelido = args.apelido or apelido_da_pasta(pasta.resolve())
    etapa = slug(args.etapa)
    if not re.match(r"^\d+(\.\d+)*$", args.versao):
        sys.exit("--versao deve ser numérica: 1, 2.1, 3, 5.1…")
    saida = pasta / f"NT_{apelido}_v{args.versao}-{etapa}.docx"
    if saida.exists():
        sys.exit(f"Já existe {saida.name}: escolha outra versão (este script nunca sobrescreve).")
    existentes = versoes(pasta, apelido)
    if args.base == "novo":
        base = None
    elif args.base == "auto":
        base = existentes[-1][1] if existentes else None
    else:
        base = Path(args.base)
        if not base.exists():
            sys.exit(f"Base não encontrada: {base}")
    if existentes and ver_tupla(args.versao) <= existentes[-1][0] and not args.forcar:
        sys.exit(f"A versão {args.versao} não é posterior à última ({existentes[-1][1].name}). "
                 "Use a próxima subversão da mais recente (ex.: 3.1) ou --forcar.")

    rel = {"saida": str(saida), "base": base.name if base else None, "unidades": [], "excluidos": [],
           "avisos": [], "quadros": [], "figuras": [], "figuras_inseridas": 0}
    unidades = []
    for cap in args.capitulos:
        cp = Path(cap)
        blocos, excl = ler_blocos(cp.read_text(encoding="utf-8"), cp.resolve())
        rel["excluidos"] += [f"{cp.name}: {e}" for e in excl]
        us, desc = dividir_unidades(blocos)
        unidades += us
        if desc:
            rel["avisos"].append(f"{cp.name}: {len(desc)} bloco(s) antes do primeiro título ficaram de fora (notas de trabalho).")

    if base:
        d = docx.Document(str(base))
        novo = False
    else:
        d = docx.Document()
        novo = True
        configurar_pagina(d.sections[0])
        corpo = d.element.body
        for e in list(corpo):
            if e.tag != qn("w:sectPr"):
                corpo.remove(e)
    garantir_estilos(d, novo)
    ctx = {"novo": novo, "rodape": None}
    if novo:
        # cabeçalho e rodapé antes do corpo, para que as seções criadas depois os herdem
        tit = proc = None
        for u in unidades:
            for b in u["blocos"]:
                if b["tipo"] == "par":
                    for ln in b["linhas"]:
                        tl = tipo_paragrafo(ln)
                        tit = tit or (sem_marca(ln) if tl == "titulo_nt" else None)
                        proc = proc or (sem_marca(ln) if tl == "processo" else None)
        rodape = f"{tit or 'Nota Técnica nº [N]/[ANO]/CGOV/CGGE/GABIN/ICMBio'}  ·  {proc or 'Processo SEI nº [preencher]'}"
        preencher_cabecalho_rodape(d.sections[0], rodape, LARG_RETRATO)

    for u in unidades:
        chave = u["chave"]
        if novo and chave != ("abertura",) and not ctx.get("abertura_feita") and not rel["unidades"]:
            rel["avisos"].append("Documento novo sem a abertura (Nota Técnica nº, Assunto, seções 1 a 3): "
                                 "o .docx começa direto no capítulo.")
        ini, fim = localizar(d, chave)
        corpo_atual = [e for e in d.element.body if e.tag != qn("w:sectPr")]
        acao = "acrescentado"
        if ini is not None:
            if not args.substituir:
                sys.exit(f"{descrever(chave)} já existe em {base.name if base else 'documento'}: "
                         "use --substituir para trocá-lo (as edições do revisor nesse trecho se perdem).")
            ancora = corpo_atual[fim] if fim < len(corpo_atual) else None
            sai = [_texto(e).strip() for e in corpo_atual[ini + 1:fim]
                   if e.tag == qn("w:p") and (_estilo(e) or "").startswith("Heading")]
            entra = {limpar_md(b["texto"]) for b in u["blocos"] if b["tipo"] == "titulo"}
            perdidos = [t for t in sai if t not in entra]
            if perdidos:
                rel["avisos"].append(f"{descrever(chave)} substituído: estes títulos da versão anterior não estão no "
                                     f".md novo e saíram do documento: {'; '.join(perdidos)}. Para trocar só um "
                                     "subitem, use um .md que comece pelo título dele (#### N.M.).")
            for e in corpo_atual[ini:fim]:
                d.element.body.remove(e)
            acao = "substituído"
        else:
            ancora = corpo_atual[fim] if fim < len(corpo_atual) else None
        antes = corpo_atual[:ini if ini is not None else fim]
        q0, f0 = contar_legendas(antes)
        nq, nf = len(rel["quadros"]), len(rel["figuras"])
        marca = len(d.element.body)
        renderizar_unidade(d, u, ctx, rel)
        novos = [e for e in list(d.element.body)[marca - 1:] if e.tag != qn("w:sectPr")]
        novos = novos[1:] if novos and novos[0] in corpo_atual else novos
        if ancora is not None:
            for e in novos:
                ancora.addprevious(e)
        qs, fs = rel["quadros"][nq:], rel["figuras"][nf:]
        if qs and qs[0] != q0 + 1:
            rel["avisos"].append(f"{descrever(chave)}: o primeiro quadro é o nº {qs[0]}, mas o documento já tem {q0} "
                                 f"quadro(s) antes dele (esperado nº {q0 + 1}).")
        if fs and fs[0] != f0 + 1:
            rel["avisos"].append(f"{descrever(chave)}: a primeira figura é a nº {fs[0]}, mas há {f0} antes (esperado nº {f0 + 1}).")
        rel["unidades"].append(f"{descrever(chave)}: {acao}")

    normalizar_secoes(d)
    st = d.settings.element
    zoom = st.find(qn("w:zoom"))
    if zoom is not None and zoom.get(qn("w:percent")) is None:  # modelo do python-docx vem sem o atributo
        zoom.set(qn("w:percent"), "100")
    if st.find(qn("w:updateFields")) is None:
        uf = parse_xml(f'<w:updateFields {nsdecls("w")} w:val="true"/>')
        depois = {"hdrShapeDefaults", "footnotePr", "endnotePr", "compat", "docVars", "rsids", "mathPr",
                  "attachedSchema", "themeFontLang", "clrSchemeMapping", "doNotIncludeSubdocsInStats",
                  "doNotAutoCompressPictures", "forceUpgrade", "captions", "readModeInkLockDown", "smartTagType",
                  "schemaLibrary", "shapeDefaults", "doNotEmbedSmartTags", "decimalSymbol", "listSeparator"}
        alvo = next((c for c in st if c.tag.split("}")[1] in depois), None)
        alvo.addprevious(uf) if alvo is not None else st.append(uf)
    cp = d.core_properties
    cp.title = f"Nota Técnica — {apelido}"
    cp.subject = "CGOV/CGGE/ICMBio"
    cp.comments = f"v{args.versao}-{etapa} · montar_nt_docx.py {VERSAO} · {dt.date.today().isoformat()}"
    cp.language = "pt-BR"
    xml = d.element.xml
    rel["alertas_no_texto"] = xml.count("⚠")
    rel["secoes"] = len(d.sections)
    if args.simular:
        rel["simulacao"] = True
        return rel
    d.save(str(saida))
    return rel


def descrever(chave) -> str:
    return {"abertura": "Abertura e Capítulo 1", "conclusao": "Seção 5 (Conclusão)"}.get(chave[0]) or \
        (f"Capítulo {chave[1]}" if chave[0] == "cap" else f"Subitem {chave[1]}")


def main():
    # relatório e mensagens em UTF-8 mesmo com saída redirecionada no Windows (cp1252 não tem "⚠")
    for fluxo in (sys.stdout, sys.stderr):
        reconf = getattr(fluxo, "reconfigure", None)
        if reconf:
            reconf(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Alimenta o .docx de revisão da Nota Técnica (suíte cgov-nt).")
    ap.add_argument("capitulos", nargs="*", help="arquivo(s) .md do capítulo, na ordem do documento")
    ap.add_argument("--versao", help="versão nova: 1, 2.1, 2.2, 3, 4, 5, 5.1…")
    ap.add_argument("--etapa", help="sufixo da etapa: introducao, fluxo, competencias, achados, propostas, quesitos-pfe, conclusao, revisao…")
    ap.add_argument("--pasta", help="pasta de trabalho do processo (padrão: a do primeiro .md)")
    ap.add_argument("--apelido", help="apelido do processo (padrão: deduzido de SEI_…_<apelido>)")
    ap.add_argument("--base", default="auto", help="auto (última versão), novo, ou caminho de um .docx")
    ap.add_argument("--substituir", action="store_true", help="troca capítulo que já existe na base")
    ap.add_argument("--forcar", action="store_true", help="aceita versão não posterior à última")
    ap.add_argument("--simular", action="store_true", help="não grava; só mostra o relatório")
    ap.add_argument("--listar", action="store_true", help="lista as versões existentes na pasta")
    ap.add_argument("--version", action="version", version=VERSAO)
    a = ap.parse_args()
    if a.listar:
        pasta = Path(a.pasta or ".")
        vs = versoes(pasta, a.apelido)
        for v, f, e in vs:
            print(f"v{'.'.join(map(str, v))}\t{e}\t{f.name}")
        if vs:
            q, f = contar_legendas(docx.Document(str(vs[-1][1])).element.body)
            print(f"próximo: Quadro nº {q + 1}, Figura nº {f + 1} (contados em {vs[-1][1].name})")
        else:
            print("nenhuma versão ainda: a primeira será criada do zero (Quadro nº 1, Figura nº 1)")
        return
    if not a.capitulos or not a.versao or not a.etapa:
        ap.error("informe o(s) .md, --versao e --etapa")
    rel = montar(a)
    print(json.dumps(rel, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

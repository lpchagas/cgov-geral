#!/usr/bin/env python3
"""Classifica entregas do PGD (exportação do PETRVS) como candidatas à Carta de Serviços ao Usuário.

Versão 0.1.0 (07/11/2026). Adaptado do script da NT CGOV nº 001/2026, sem conexão com banco de dados:
a entrada é um CSV exportado pelo próprio usuário. Nenhuma credencial é lida ou gravada.

Uso:
    python classificar_entregas.py ENTRADA.csv [--saida PASTA] [--minimo 3] [--delimitador "|"]

Colunas reconhecidas na entrada (as ausentes ficam vazias): nome_entrega, destinatario, descricao_meta,
sigla_unidade, nome_unidade, status_pe, nome_template_entrega, descricao_template, tipo_indicador_template,
qtd_registros, qtd_concluidas.

Saídas (delimitador "|", UTF-8 com BOM, para abrir no Excel):
    carta_servicos_candidatos_<AAAAMMDD_HHMM>.csv    pontuação > 0
    carta_servicos_qualificados_<AAAAMMDD_HHMM>.csv  pontuação >= mínimo, com justificativa

A classificação é léxica (palavras-chave), não semântica: o resultado é uma lista de candidatos para
confirmação pelas unidades, nunca a Carta pronta.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path

__version__ = "0.1.0"

COLUNAS = [
    "nome_entrega", "destinatario", "descricao_meta", "sigla_unidade", "nome_unidade", "status_pe",
    "nome_template_entrega", "descricao_template", "tipo_indicador_template", "qtd_registros", "qtd_concluidas",
]


def normalizar(texto: str) -> str:
    """Minúsculas, sem acentos e com espaços simples, para comparar termos."""
    texto = unicodedata.normalize("NFKD", (texto or "").lower())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", texto).strip()


# Termos já sem acento (a comparação é feita sobre o texto normalizado e por palavra inteira).
TERMOS_DESTINATARIO_EXTERNO = {
    "cidadao": 6, "cidadaos": 6, "publico": 5, "sociedade": 5, "populacao": 5,
    "usuario": 4, "usuarios": 4, "solicitante": 5, "requerente": 5, "interessado": 4, "demandante": 4,
    "pessoa fisica": 6, "pessoa juridica": 6, "empresa": 4, "empresas": 4, "empreendedor": 4,
    "empreendedores": 4, "organizacao": 4, "instituicao": 3, "ong": 4, "ongs": 4, "associacao": 3,
    "cooperativa": 3, "proprietario": 4, "posseiro": 4, "produtor rural": 4, "pesquisador": 5,
    "pesquisadores": 5, "cientista": 4, "cientistas": 4, "estudante": 3, "academico": 3, "visitante": 5,
    "visitantes": 5, "turista": 5, "turistas": 5, "ecoturista": 5, "visitacao": 4, "comunidade": 4,
    "comunidades": 4, "populacao local": 5, "comunidade tradicional": 5, "indigena": 4, "quilombola": 4,
    "ribeirinho": 4, "extrativista": 4, "outros orgaos": 3, "orgao externo": 4, "parceiro": 3,
    "parceiros": 3,
}

TERMOS_TIPO_SERVICO = {
    "licenca": 4, "licenciamento": 5, "autorizacao": 4, "autorizacoes": 4, "outorga": 5, "permissao": 4,
    "concessao": 4, "cessao": 3, "habilitacao": 3, "credenciamento": 4, "certificacao": 4,
    "certificado": 3, "registro": 3, "cadastro": 3, "inscricao": 3, "recadastramento": 3,
    "analise de processo": 4, "instrucao processual": 3, "manifestacao tecnica": 3, "parecer tecnico": 3,
    "tramitacao": 2, "fiscalizacao": 4, "vistoria": 4, "inspecao": 4, "monitoramento ambiental": 3,
    "auto de infracao": 5, "embargo": 4, "autuacao": 4, "processo sancionador": 4, "notificacao": 3,
    "patrimonio genetico": 5, "acesso ao patrimonio": 5, "pesquisa cientifica": 4,
    "pesquisa em unidade de conservacao": 5, "uso publico": 4, "visitacao publica": 5,
    "unidade de conservacao": 3, "educacao ambiental": 4, "regularizacao fundiaria": 5,
    "atendimento ao cidadao": 6, "atendimento ao publico": 5, "ouvidoria": 5, "manifestacao": 3,
    "reclamacao": 3, "acesso a informacao": 4, "servico ao usuario": 5, "solicitacao online": 4,
    "portal do cidadao": 5, "sistema de protocolo": 3,
}

TERMOS_INTERNOS = {
    "reuniao interna": -4, "reuniao de equipe": -3, "reuniao de planejamento": -3,
    "nota tecnica interna": -4, "relatorio de gestao interna": -4, "planejamento estrategico interno": -3,
    "capacitacao interna": -3, "treinamento interno": -3, "instrucao normativa interna": -3,
    "organograma": -3, "norma interna": -3,
}

# Ordem importa: o primeiro tipo cujo termo aparecer é o escolhido.
TIPOS = [
    ("Acesso ao Patrimônio Genético", ["patrimonio genetico", "acesso ao patrimonio"]),
    ("Licenciamento", ["licenca", "licenciamento"]),
    ("Autorização / Outorga", ["autorizacao", "autorizacoes", "outorga", "permissao", "concessao"]),
    ("Certificação / Habilitação", ["certificacao", "certificado", "habilitacao", "credenciamento"]),
    ("Cadastro / Registro", ["cadastro", "registro", "inscricao", "recadastramento"]),
    ("Fiscalização Sancionatória", ["auto de infracao", "embargo", "autuacao", "processo sancionador"]),
    ("Fiscalização / Vistoria", ["fiscalizacao", "vistoria", "inspecao"]),
    ("Pesquisa em Unidades de Conservação", ["pesquisa cientifica", "pesquisa em unidade de conservacao"]),
    ("Visitação / Uso Público em UC", ["visitacao", "uso publico", "turista", "turistas", "ecoturismo",
                                       "visitante", "visitantes"]),
    ("Regularização Fundiária", ["regularizacao fundiaria"]),
    ("Educação Ambiental", ["educacao ambiental"]),
    ("Ouvidoria / Manifestações", ["ouvidoria", "manifestacao", "reclamacao"]),
    ("Acesso à Informação (LAI)", ["acesso a informacao", "informacao ao publico"]),
    ("Atendimento ao Cidadão", ["atendimento ao cidadao", "atendimento ao publico"]),
]
TIPO_PADRAO = "Serviço Público Geral"

JUSTIFICATIVA_BASE = (
    "Entrega com indício de destinatário externo, compatível com o conceito de serviço público do art. 2º, II, "
    "da Lei nº 13.460/2017. Se confirmada pela unidade, deve constar da Carta de Serviços ao Usuário (art. 7º), "
    "com o serviço oferecido, requisitos e documentos, etapas, prazo máximo, forma de prestação e locais e "
    "formas de manifestação (art. 7º, § 2º, I a VI; Decreto nº 9.094/2017, art. 11, § 2º)."
)


def contem(texto: str, termo: str) -> bool:
    return re.search(rf"(?<!\w){re.escape(termo)}(?!\w)", texto) is not None


def calcular_score(linha: dict) -> tuple[int, list[str]]:
    dest = normalizar(linha.get("destinatario", ""))
    tudo = normalizar(" ".join(linha.get(c, "") or "" for c in (
        "destinatario", "nome_entrega", "descricao_meta", "descricao_template", "nome_template_entrega")))
    score, evid = 0, []
    for termo, pts in TERMOS_DESTINATARIO_EXTERNO.items():  # critério A: peso dobrado
        if contem(dest, termo):
            score += 2 * pts
            evid.append(f"destinatário='{termo}' (+{2 * pts})")
    for termo, pts in TERMOS_TIPO_SERVICO.items():  # critério B
        if contem(tudo, termo):
            score += pts
            evid.append(f"tipo='{termo}' (+{pts})")
    for termo, pts in TERMOS_INTERNOS.items():  # critério C
        if contem(tudo, termo):
            score += pts
            evid.append(f"interno='{termo}' ({pts})")
    return score, evid[:8]


def classificar_tipo(linha: dict) -> str:
    texto = normalizar(" ".join(linha.get(c, "") or "" for c in ("destinatario", "nome_entrega", "descricao_meta")))
    for tipo, termos in TIPOS:
        if any(contem(texto, t) for t in termos):
            return tipo
    return TIPO_PADRAO


def ler_csv(caminho: Path, delimitador: str | None) -> list[dict]:
    texto = caminho.read_text(encoding="utf-8-sig")
    if delimitador is None:
        try:
            delimitador = csv.Sniffer().sniff(texto.splitlines()[0], delimiters="|;,\t").delimiter
        except (csv.Error, IndexError):
            delimitador = "|"
    linhas = list(csv.DictReader(texto.splitlines(), delimiter=delimitador))
    if linhas and "nome_entrega" not in linhas[0] and "destinatario" not in linhas[0]:
        sys.exit("ERRO: a entrada não tem as colunas 'nome_entrega' nem 'destinatario'. Veja a docstring.")
    return [{c: (l.get(c) or "").strip() for c in COLUNAS} for l in linhas]


def gravar_csv(caminho: Path, linhas: list[dict], campos: list[str]) -> None:
    with caminho.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter="|", extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)
    print(f"  gravado: {caminho} ({len(linhas)} linhas)")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("entrada", type=Path)
    ap.add_argument("--saida", type=Path, default=None, help="pasta de saída (padrão: a da entrada)")
    ap.add_argument("--minimo", type=int, default=3, help="pontuação mínima para qualificar (padrão: 3)")
    ap.add_argument("--delimitador", default=None, help="delimitador da entrada (padrão: detectar)")
    ap.add_argument("--version", action="version", version=__version__)
    a = ap.parse_args(argv)

    linhas = ler_csv(a.entrada, a.delimitador)
    saida = a.saida or a.entrada.parent
    saida.mkdir(parents=True, exist_ok=True)
    carimbo = datetime.now().strftime("%Y%m%d_%H%M")

    candidatos, qualificados = [], []
    for l in linhas:
        score, evid = calcular_score(l)
        if score <= 0:
            continue
        l["score"], l["evidencias"] = score, " | ".join(evid)
        l["tipo_servico"] = classificar_tipo(l)
        l["justificativa"] = JUSTIFICATIVA_BASE if score >= a.minimo else ""
        candidatos.append(l)
        if score >= a.minimo:
            qualificados.append(l)

    base = ["sigla_unidade", "nome_unidade", "tipo_servico", "nome_entrega", "descricao_meta", "destinatario",
            "nome_template_entrega", "qtd_registros", "qtd_concluidas", "score", "evidencias"]
    gravar_csv(saida / f"carta_servicos_candidatos_{carimbo}.csv",
               sorted(candidatos, key=lambda x: (-x["score"], x["sigla_unidade"])), base)
    gravar_csv(saida / f"carta_servicos_qualificados_{carimbo}.csv",
               sorted(qualificados, key=lambda x: (x["tipo_servico"], x["sigla_unidade"])), base + ["justificativa"])

    print(f"Entregas lidas: {len(linhas)} | candidatas: {len(candidatos)} | qualificadas (>= {a.minimo}): "
          f"{len(qualificados)}")
    for tipo, n in Counter(q["tipo_servico"] for q in qualificados).most_common():
        print(f"  {tipo:<40} {n:>5}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

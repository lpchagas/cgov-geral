#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gerar_indices.py — fichas PROCESSO.md e índices _INDICE.md da pasta operacional CGOV
(etapa 4.7 do plano de implantação; previsto na Fase 5 e antecipado).

Modos (pode combinar):
  --fichas    Cria PROCESSO.md nas pastas de 01_processos que ainda não têm ficha.
              Nunca sobrescreve uma ficha existente. Preenche só o que se deduz com
              segurança (nº SEI, apelido, ano do nº SEI, pastas de origem, conteúdo);
              o resto fica vazio e marcado "⚠️ revisar". NTs da série cujo nº de
              documento SEI aparece nos arquivos do processo entram como candidatas.
  --indices   Gera os _INDICE.md de 01, 02, 03, 04 e 05 (arquivos gerados: são
              reescritos a cada execução; não editar à mão).

Opções:
  --raiz <pasta CGOV>   (ou CGOV_RAIZ no ambiente ou no .env do repositório)
  --saida <pasta>       grava numa cópia de rascunho em vez de gravar na pasta CGOV
                        (as fichas já existentes na saída têm precedência na leitura)
  --mapa <csv>          mapa da reorganização, para listar as pastas de origem (opcional)
  --data AAAA-MM-DD     data de geração (padrão: hoje)

Sem caminhos pessoais neste arquivo (regra de sanitização).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

VERSAO = "0.1.0"
REPO = Path(__file__).resolve().parent.parent
SUBPASTAS = ["documentos-sei", "trabalho", "referencias", "produtos"]
RE_PASTA = re.compile(r"^SEI_(\d{5})\.(\d{6})_(\d{4})-(\d{2})(?:_(.+))?$")
RE_DOC = re.compile(r"(?<!\d)(0\d{8})(?!\d)")
RE_NT = re.compile(r"(?:^|_| )(NT|NI)_(?:([A-Z]+)_)?(\d{1,3})-(\d{4})")
RE_NT2 = re.compile(r"Nota_Tecnica_(\d{1,3})", re.IGNORECASE)
RE_NORMA = re.compile(r"^(\d{8})_(.+?)\.(pdf|md)$", re.IGNORECASE)
AVISO = "⚠️ revisar"


def raiz_padrao(arg: str | None) -> Path:
    cand = arg or os.environ.get("CGOV_RAIZ")
    env = REPO / ".env"
    if not cand and env.exists():
        for l in env.read_text(encoding="utf-8").splitlines():
            if l.strip().startswith("CGOV_RAIZ="):
                cand = l.split("=", 1)[1].strip().strip('"')
    if not cand or not Path(cand).is_dir():
        sys.exit("[PARE] Informe a pasta CGOV com --raiz ou CGOV_RAIZ.")
    return Path(cand)


def arquivos(p: Path) -> list[str]:
    return sorted(os.path.relpath(os.path.join(d, n), p).replace(os.sep, "/")
                  for d, _, fs in os.walk(p) for n in fs)


def serie_nts(raiz: Path) -> list[dict]:
    """Série oficial em 02_notas-tecnicas/<ano>/: nº, ano, doc SEI e tema, pelo nome do arquivo."""
    nts = []
    base = raiz / "02_notas-tecnicas"
    for ano in sorted(x for x in os.listdir(base) if x.isdigit()) if base.is_dir() else []:
        for n in sorted(os.listdir(base / ano)):
            m, m2 = RE_NT.search(n), RE_NT2.search(n)
            doc = RE_DOC.search(n)
            if m:
                tipo = m.group(1) + (f" {m.group(2)}" if m.group(2) else "")
                num, a = int(m.group(3)), m.group(4)
            elif m2:
                tipo, num, a = "NT", int(m2.group(1)), ano
            else:
                tipo, num, a = "?", None, ano
            tema = os.path.splitext(n)[0]
            if doc:
                tema = tema.split(doc.group(1), 1)[-1]
            tema = re.sub(r"^[_ ]+|_final$", "", tema).replace("_", " ").strip() or "—"
            if m2 and not m:
                tema = "—"
            rotulo = f"{tipo} {num:02d}/{a}" if num is not None else n
            nts.append({"ano": ano, "arquivo": n, "tipo": tipo, "num": num, "ano_nt": a,
                        "doc": doc.group(1) if doc else "", "tema": tema, "rotulo": rotulo})
    return nts


def ler_frontmatter(p: Path) -> dict:
    try:
        txt = p.read_text(encoding="utf-8")
    except OSError:
        return {}
    if not txt.startswith("---"):
        return {}
    fm = {}
    for l in txt.split("---", 2)[1].splitlines():
        if ":" in l and not l.startswith(" "):
            k, v = l.split(":", 1)
            fm[k.strip()] = v.split("  #")[0].strip().strip('"')
    return fm


def origens_por_processo(mapa: Path | None) -> dict[str, list[str]]:
    res = defaultdict(set)
    if not mapa or not mapa.exists():
        return {}
    with open(mapa, encoding="utf-8-sig") as f:
        for l in csv.DictReader(f, delimiter=";"):
            d = l.get("destino", "")
            if d.startswith("01_processos/") and l.get("origem"):
                o = l["origem"].split("/")
                k = o[0] if len(o) < 2 else ("/".join(o[:3]) if o[0] == "_acervo-escritorio-virtual"
                                             else "/".join(o[:2]))
                res[d.split("/")[1]].add(k)
    return {k: sorted(v) for k, v in res.items()}


def ficha(pasta: str, conteudo: list[str], nts: list[dict], origens: list[str], hoje: str) -> str:
    m = RE_PASTA.match(pasta)
    org, num, ano, dv, apelido = m.groups()
    sei = f"{org}.{num}/{ano}-{dv}"
    cont = Counter(c.split("/")[0] if "/" in c else "(raiz)" for c in conteudo)
    nte = [c for c in conteudo if os.path.basename(c) == "NT_ESTADO.md" and "_backup" not in c]
    docs = {d for c in conteudo for d in RE_DOC.findall(os.path.basename(c))}
    cand = [n for n in nts if n["doc"] and n["doc"] in docs]
    titulo = ""
    for o in origens:
        nome = o.split("/")[-1]
        if nome.lower().endswith((".pdf", ".md", ".docx")):
            continue
        resto = re.sub(r"^(?:SEI_)*\d{5}(?: \(1\))?\.\d{6}[ _]\d{4}[-_]\d{2}[_ ]?", "", nome).strip(" _")
        if resto and not re.fullmatch(r"v\d+", resto):
            titulo = re.sub(r"_v\d+$", "", resto).replace("_", " ")
            break
    linhas_cand = "\n".join(
        f"- {n['rotulo']} — {n['tema']} (doc. SEI {n['doc']}; "
        f"[02_notas-tecnicas/{n['ano']}/{n['arquivo']}](../../02_notas-tecnicas/{n['ano']}/{n['arquivo']}))"
        for n in cand) or "- (nenhuma encontrada pelo nº do documento SEI)"
    linhas_cont = "\n".join(f"| {s} | {cont.get(s, 0)} |" for s in SUBPASTAS + (["(raiz)"] if cont.get("(raiz)") else []))
    linhas_orig = "\n".join(f"- `{o}`" for o in origens) or "- (não registrada)"
    estado = (f"- NT em elaboração com a suíte `cgov-nt`: [`{nte[0]}`]({nte[0]})\n" if nte else "")
    return f"""---
tipo: processo
sei: "{sei}"
apelido: {apelido or '""'}{'' if apelido else '            # ⚠️ revisar: processo sem apelido (D24)'}
titulo: "{titulo}"{'' if titulo else '                 # ⚠️ revisar'}{'      # deduzido do nome da pasta de origem; ⚠️ revisar' if titulo else ''}
inciso_art37: []            # ⚠️ revisar — I a X do parágrafo único do Art. 37 da Portaria ICMBio nº 5.592/2025
situacao: ""                # ⚠️ revisar — em-andamento | aguardando-terceiros | concluido | arquivado
unidade_demandante: ""      # ⚠️ revisar
aberto_em: "{ano}"            # ano do nº SEI; ⚠️ completar a data
atualizado_em: {hoje}
notas_tecnicas: []          # ⚠️ revisar — ver candidatas em "Produtos da CGOV"
cowork_projeto: ""
---

# {titulo or (apelido.replace('-', ' ') if apelido else sei)} — SEI {sei}

> Ficha criada automaticamente na reorganização de 2026-11 (etapa 4.7). Os campos marcados ⚠️ precisam
> de revisão do responsável. Sem nomes nem matrículas (LGPD).

## Objeto
{AVISO}: descrever em 2–3 linhas o que o processo trata.

## Andamento
| Data | Evento | Documento SEI |
|---|---|---|

## Produtos da CGOV
NTs da série oficial cujo nº de documento SEI aparece nos arquivos deste processo (candidatas — ⚠️ confirmar
se são produtos deste processo ou apenas referências):
{linhas_cand}

## Conteúdo da pasta (em {hoje})
| Subpasta | Arquivos |
|---|---|
{linhas_cont}
{estado}
## Origem (reorganização de 2026-11)
{linhas_orig}

## Instruções específicas
(nenhuma)

## Pendências
- [ ] Revisar os campos ⚠️ do frontmatter e o Objeto
"""


def tabela(cab: list[str], linhas: list[list[str]]) -> str:
    esc = lambda s: str(s).replace("|", "\\|")
    return "\n".join(["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)] +
                     ["| " + " | ".join(esc(c) for c in l) + " |" for l in linhas])


def cab_indice(titulo: str, hoje: str) -> str:
    return f"# {titulo} — gerado em {hoje} por gerar_indices.py v{VERSAO} (não editar à mão)\n\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Fichas e índices da pasta CGOV (etapa 4.7).")
    ap.add_argument("--fichas", action="store_true")
    ap.add_argument("--indices", action="store_true")
    ap.add_argument("--raiz")
    ap.add_argument("--saida")
    ap.add_argument("--mapa")
    ap.add_argument("--data", default=f"{dt.date.today():%Y-%m-%d}")
    a = ap.parse_args()
    if not (a.fichas or a.indices):
        ap.error("use --fichas e/ou --indices")
    raiz = raiz_padrao(a.raiz)
    saida = Path(a.saida) if a.saida else raiz
    hoje = a.data
    nts = serie_nts(raiz)
    procs = sorted(p for p in os.listdir(raiz / "01_processos")
                   if (raiz / "01_processos" / p).is_dir() and RE_PASTA.match(p))
    orig = origens_por_processo(Path(a.mapa) if a.mapa else None)
    criadas = existentes = 0
    if a.fichas:
        for p in procs:
            alvo_raiz = raiz / "01_processos" / p / "PROCESSO.md"
            alvo = saida / "01_processos" / p / "PROCESSO.md"
            if alvo_raiz.exists() or alvo.exists():
                existentes += 1
                continue
            alvo.parent.mkdir(parents=True, exist_ok=True)
            alvo.write_text(ficha(p, arquivos(raiz / "01_processos" / p), nts, orig.get(p, []), hoje),
                            encoding="utf-8", newline="\n")
            criadas += 1
        print(f"[OK] Fichas: {criadas} criada(s), {existentes} já existia(m) (não alteradas).")
    if a.indices:
        def fm(p):
            for b in (saida, raiz):
                f = b / "01_processos" / p / "PROCESSO.md"
                if f.exists():
                    return ler_frontmatter(f)
            return {}
        lin = []
        for p in procs:
            f = fm(p)
            lin.append([f"[{p}]({p}/PROCESSO.md)", f.get("titulo") or "⚠️",
                        f.get("inciso_art37") if f.get("inciso_art37") not in (None, "", "[]") else "⚠️",
                        f.get("situacao") or "⚠️", f.get("atualizado_em", ""),
                        f.get("notas_tecnicas") if f.get("notas_tecnicas") not in (None, "", "[]") else "—"])
        idx = {"01_processos/_INDICE.md": cab_indice("Índice de processos", hoje) +
               f"{len(procs)} processos. ⚠️ = campo da ficha ainda não revisado.\n\n" +
               tabela(["Processo", "Título", "Inciso", "Situação", "Atualizado", "NTs"], lin) + "\n"}
        # 02 — série oficial
        cand = defaultdict(list)
        for p in procs:
            docs = {d for c in arquivos(raiz / "01_processos" / p) for d in RE_DOC.findall(os.path.basename(c))}
            for n in nts:
                if n["doc"] in docs:
                    cand[n["arquivo"]].append(p)
        lin = [[n["ano"], n["rotulo"], n["doc"] or "—", n["tema"],
                ", ".join(f"[{x}](../01_processos/{x}/PROCESSO.md)" for x in cand[n["arquivo"]]) or "—",
                f"[pdf]({n['ano']}/{n['arquivo']})"] for n in nts]
        idx["02_notas-tecnicas/_INDICE.md"] = cab_indice("Série oficial de Notas Técnicas e Informações", hoje) + \
            (f"{len(nts)} documentos. A coluna Processo traz os processos em cujos arquivos aparece o nº do documento "
             "SEI (candidatos — ⚠️ confirmar). Nomes ainda fora do padrão da Seção 5.4.\n\n") + \
            tabela(["Ano", "Documento", "Doc. SEI", "Tema", "Processo (candidato)", "Arquivo"], lin) + "\n"
        # 03 — acervo normativo
        grupos = defaultdict(dict)
        base = raiz / "03_normativos"
        for rel in arquivos(base):
            nome = os.path.basename(rel)
            m = RE_NORMA.match(nome)
            if not m:
                continue
            pasta = os.path.dirname(rel)
            chave = (pasta, os.path.splitext(nome)[0])
            grupos[chave][m.group(3).lower()] = rel
        lin = []
        for (pasta, b), ex in sorted(grupos.items(), key=lambda x: x[0][1]):
            d = b[:8]
            lin.append([f"{d[6:8]}/{d[4:6]}/{d[:4]}", b[9:].replace("_", " · "),
                        f"[pdf]({ex['pdf']})" if "pdf" in ex else "⚠️ falta",
                        f"[md]({ex['md']})" if "md" in ex else "⚠️ falta",
                        "revogado" if pasta == "revogados" else "⚠️ verificar"])
        idx["03_normativos/_INDICE.md"] = cab_indice("Acervo normativo", hoje) + \
            f"{len(grupos)} normativos (PDF + transcrição .md). Vigência ainda não verificada, salvo os de revogados/.\n\n" + \
            tabela(["Data", "Normativo", "PDF", "Texto", "Vigência"], lin) + "\n"
        # 04 e 05 — listagens
        for area, tit in (("04_colegiados", "Material de colegiados"), ("05_projetos", "Projetos")):
            arqs = [x for x in arquivos(raiz / area) if not x.startswith("_")]
            lin = [[x.split("/")[0] if "/" in x else "—", f"[{os.path.basename(x)}]({x})"] for x in arqs]
            idx[f"{area}/_INDICE.md"] = cab_indice(tit, hoje) + f"{len(arqs)} arquivos.\n\n" + \
                tabela(["Pasta", "Arquivo"], lin) + "\n"
        for rel, txt in idx.items():
            alvo = saida / rel
            alvo.parent.mkdir(parents=True, exist_ok=True)
            alvo.write_text(txt, encoding="utf-8", newline="\n")
        print(f"[OK] Índices: {', '.join(idx)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

---
name: cgov-comparar-versoes
description: >
  Use esta skill sempre que o usuário da CGOV/ICMBio precisar comparar versões de um
  dispositivo normativo, resolver controvérsias entre áreas (ex.: PFE vs. Corregedoria,
  CGGP vs. Ouvidoria) ou propor redação saneada de um artigo, inciso ou parágrafo de
  ato normativo. Gatilhos típicos: "COMPARAR_VERSOES", "comparar versões", "comparar
  redações", "qual versão está correta?", "resolver controvérsia", "há conflito entre
  as áreas", "o que a PFE disse sobre esse artigo", "qual a posição da Corregedoria",
  "proposta de redação", "sanar a redação", "evolução normativa", "texto saneado",
  "qual unidade está certa", "como ficou o artigo X após as manifestações", "cruzar
  manifestações", "analisar posições divergentes". Acione também quando o usuário
  colar trechos de uma Nota Técnica, Parecer ou Despacho e pedir para comparar com
  outra versão do mesmo dispositivo — mesmo sem usar o comando exato.
---

# SKILL: Comparar Versões e Resolver Controvérsias Normativas — CGOV/ICMBio

Você está no modo **COMPARAR_VERSOES**. Suspenda a conversação genérica e execute
as fases abaixo em sequência. O objetivo é identificar as versões em disputa de um
dispositivo normativo, analisar a coesão sistêmica e entregar uma **proposta de
redação saneada** pronta para uso pela CGOV.

---

## CONTEXTO INSTITUCIONAL

Este comando opera em qualquer processo normativo da CGOV/ICMBio (o PSPEADBio é
o ato de referência em que nasceu, não um contexto padrão). As normas de
referência são:

- **Técnica legislativa:** Lei Complementar nº 95/1998 e Decreto nº 12.002/2024
- **Processo administrativo:** Lei nº 9.784/1999
- **Edição de atos internos:** Portaria ICMBio nº 271/2013 (Anexo I) e Portaria ICMBio
  nº 129/2020 (espécies, vigência e instrução; prevalece onde as duas colidem)

Sempre que a proposta saneada tocar em competência disciplinar ou de controle,
considere também os normativos do Decreto nº 12.122/2024 e da Portaria MGI nº
6.719/2024.

---

## FASE 1 — COLETA DE DADOS

Se o usuário ainda não forneceu as informações abaixo, solicite **somente** o que
estiver faltando:

1. **Identificação do dispositivo:** Qual artigo, inciso, parágrafo ou capítulo está
   em análise? (ex.: "Art. 12 da minuta")
2. **Versões disponíveis:** Cole ou descreva cada versão do texto — idealmente com a
   origem de cada uma (ex.: "minuta original enviada pela CGGP", "texto sugerido pela
   PFE no Parecer nº 00101/2026", "texto alterado pela Corregedoria em despacho de
   15/05/2026").
3. **Contexto da controvérsia (se houver):** Qual é o ponto de discordância entre as
   áreas? Uma frase basta — o modelo vai fazer a análise aprofundada.
4. **Norma de destino:** Qual ato normativo final vai receber este dispositivo?
   (ex.: Portaria, Instrução Normativa, Resolução)

> Se o usuário fornecer apenas um texto e pedir "como deve ficar", assuma que há
> apenas uma versão e pule para a Fase 3 com foco em saneamento de legística.

---

## FASE 2 — MAPEAMENTO DE ATORES E POSIÇÕES

Antes de escrever qualquer análise, raciocine internamente sobre:

- **Quais unidades manifestaram posição** e qual é o interesse institucional de cada
  uma (ex.: PFE busca segurança jurídica; Corregedoria busca competência exclusiva;
  CGGP busca viabilidade operacional).
- **Qual é o verbo central em disputa** — muitas controvérsias giram em torno de um
  único verbo ambíguo (ex.: "sugerir" vs. "encaminhar" vs. "deliberar").
- **Existe hierarquia normativa clara** que já resolve a disputa sem precisar de
  criatividade interpretativa? Se sim, sinalize.
- **Há dependência circular** — a norma X depende de Y que depende de X? Se sim,
  o texto está com defeito estrutural, não apenas redacional.

---

## FASE 3 — GERAÇÃO DA RESPOSTA

Produza a análise usando **exatamente** o seguinte formato:

---

##### Análise de Controvérsia e Evolução Normativa: [Tema / Artigo identificado]

**1. Visão Geral das Posições:**

* **Minuta Original ([origem/data se conhecida]):** [O que dizia o texto inicial —
  cite literalmente se disponível, entre aspas]
* **Posição [Unidade A] ([documento de origem se conhecido]):** [Resumo do apontamento
  — qual mudança propõe e por qual fundamento]
* **Posição [Unidade B] ([documento de origem se conhecido]):** [Idem]
* *(adicione linhas para quantas unidades houver)*

---

**2. Análise de Coesão e Risco:**

[Análise técnica estruturada em até 4 parágrafos. Responda:
(a) Qual é o núcleo do conflito — disputa de competência, ambiguidade redacional ou
    inconsistência com hierarquia normativa superior?
(b) Do ponto de vista da viabilidade operacional, qual versão cria fluxos mais
    exequíveis? Há gargalo ou beco sem saída processual?
(c) Do ponto de vista da técnica legislativa (Lei Complementar nº 95/1998 e
    Decreto nº 12.002/2024), qual versão está mais correta em estrutura e redação?
(d) Qual é o risco institucional de adotar cada versão? (ex.: nulidade do ato,
    conflito de competência, ineficácia operacional)]

---

**3. Tabela Comparativa e Proposta Saneada:**

| Versão | Texto | Problema Identificado |
| :--- | :--- | :--- |
| Minuta Original | *[texto]* | *[problema]* |
| Proposta [Unidade A] | *[texto]* | *[problema ou vantagem]* |
| Proposta [Unidade B] | *[texto]* | *[problema ou vantagem]* |

**Proposta de Redação Saneada (CGOV):**

> *[Texto final do dispositivo, redigido em conformidade com o Decreto nº 12.002/2024:
> presente do indicativo (não "deverá"), estrutura Capítulo → Artigo → Caput →
> Inciso → Alínea, sem remissões circulares, sem verbos modais desnecessários.
> Se for um artigo completo, inclua o número do artigo. Se for um inciso, inclua
> a numeração em algarismo romano.]*

**Justificativa da proposta:** [2–4 frases explicando por que esta redação é superior
às versões anteriores — cite os dispositivos legais de referência quando relevante]

---

## REGRAS DE REDAÇÃO (aplicar sempre na proposta saneada)

Seguir o Manual de Redação da Presidência da República e o Decreto nº 12.002/2024:

1. **Tempo verbal:** Presente do indicativo para obrigações ("A unidade envia o
   relatório"), nunca futuro do pretérito ("deveria") ou perífrases modais
   desnecessárias ("deverá proceder ao envio").
2. **Verbo único por inciso:** Cada inciso deve conter uma única ação principal.
   Se houver duas ações, separe em dois incisos.
3. **Remissões internas:** Só remeter a artigos que efetivamente existam na minuta.
   Remissões a normas externas devem identificar a norma completa na primeira
   ocorrência.
4. **Verbos de competência vs. verbos de faculdade:** "Compete à unidade X" atribui
   competência; "A unidade X pode" é faculdade. Nunca misture os dois no mesmo
   dispositivo.
5. **Sujeito explícito:** Evite pronomes anafóricos como "esta" ou "aquela" se
   houver risco de ambiguidade. Repita o nome da unidade.
6. **Extensão:** Prefira dispositivos curtos (3–4 linhas). Se o artigo passar de
   6 linhas, divida em parágrafos ou incisos.

---

## REGRA ESPECIAL: CONFLITO INSOLÚVEL

Se a análise revelar um conflito que não pode ser resolvido pela CGOV sem extrapolar
sua competência normativa (ex.: disputa sobre competência disciplinar exclusiva da
Corregedoria ou interpretação de lei federal), não invente uma solução. Em vez disso,
encerre com:

> **⚠️ Encaminhamento recomendado à PFE:** Este ponto envolve [descrever o conflito
> insolúvel] e requer manifestação da Procuradoria Federal Especializada (PFE/ICMBio)
> antes que a CGOV possa propor redação definitiva. Sugestão de quesito: [formule
> o quesito jurídico preciso a ser submetido à PFE].

---

## SAÍDA FINAL

Após a análise, pergunte ao usuário:

> "Deseja que eu modele o fluxo processual resultante desta redação (MODELAR_FLUXO)
> ou que eu realize a auditoria completa de competências do capítulo
> (AUDITORIA_COMPETENCIAS)?"

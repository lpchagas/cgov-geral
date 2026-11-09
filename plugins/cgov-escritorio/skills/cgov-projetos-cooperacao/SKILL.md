---
name: cgov-projetos-cooperacao
description: >
  Projetos de cooperação técnica e internacional em que a CGOV/ICMBio propõe ou acompanha iniciativas:
  Termo de Referência no padrão do parceiro (REDIGIR_TDR), Nota Informativa de andamento (REDIGIR_NOTA_INFORMATIVA),
  despacho de encaminhamento (REDIGIR_DESPACHO), alinhamento da iniciativa ao plano operativo, aos eixos do
  projeto e à Cadeia de Valor (ALINHAR) e conferência dos insumos de um TdR (CHECAR_INSUMOS). Genérica; o
  primeiro caso é a cooperação com a GIZ (references/giz.md). Use ao ouvir "TdR", "termo de referência da
  consultoria", "GIZ", "projeto de cooperação", "POA", "plano operativo", "nota informativa do projeto",
  "consultoria do projeto". Não faz contratação pela Lei nº 14.133/2021 nem prestação de contas financeira.
---

# cgov-projetos-cooperacao — Projetos de cooperação

Esta skill transforma uma demanda técnica do ICMBio (por exemplo, uma solução de IA, um catálogo, um painel)
nos documentos que um projeto de cooperação exige: o Termo de Referência que o parceiro usa para contratar e os
registros internos no SEI. As regras de cada parceiro ficam em `references/` (hoje, só `giz.md`).

⚠️ **Enquadramento:** o Art. 37 da Portaria ICMBio nº 5.592/2025 não cita projetos de cooperação. Enquadre a
iniciativa pelo seu objeto (por exemplo, parágrafo único, III, métodos e soluções de gestão por processos; VI,
Cadeia de Valor) e confirme com o usuário.

## ANTES DE QUALQUER MODO

1. **Identifique o projeto e o parceiro** e leia a referência do parceiro. Se não houver, pergunte: nome do
   projeto, parceiro executor, eixos ou componentes, plano operativo vigente e modelo de TdR do parceiro.
2. **Regras invioláveis:**
   - **não invente** produto, dias de trabalho, honorário, orçamento, prazo, perfil de especialista ou
     identificador de projeto: campo sem informação fica como `[A DEFINIR PELO GESTOR]`;
   - **cláusulas obrigatórias do parceiro** (na GIZ: sustentabilidade nas viagens e proteção de dados) nunca
     são omitidas do TdR;
   - **sem dados pessoais:** nome de consultor ou de servidor só entra se o usuário informar e o documento
     exigir; em modelos e exemplos, colchetes;
   - **dados institucionais:** se o TdR previr acesso a dados ou sistemas do ICMBio, inclua cláusula de
     confidencialidade e de conformidade com a LGPD (Lei nº 13.709/2018).
3. Documentos do projeto ficam na **pasta de projetos** (`AAAA-MM_<apelido>`, conforme o `LEIA-ME.md` da
   pasta CGOV); minutas do SEI, na pasta do processo.

## Cadeia de raciocínio (antes de redigir)

1. **Iniciativa:** qual pacote de trabalho, qual unidade proponente, quais unidades afetadas (mapeie todas).
2. **Alinhamento:** qual eixo ou componente do projeto; qual ação do plano operativo; quais processos da Cadeia
   de Valor (consulte a `cgov-cadeia-valor` para os nomes oficiais; não cite macroprocesso de memória).
3. **Artefato:** TdR (o parceiro contrata), Nota Informativa (registro interno) ou despacho (encaminhamento).
4. **Insumos:** há perfis, dias, produtos e prazos suficientes? Se não, CHECAR_INSUMOS antes de redigir.

## MODO 1 — REDIGIR_TDR

Use o modelo do parceiro (GIZ: `references/giz.md`). Estrutura mínima genérica: informações do projeto;
contexto; serviços a prestar (alinhamento inicial, execução, validação, transferência de conhecimento);
qualificação da equipe; quantitativos (dias por especialista, viagens); produtos e pagamentos (produto,
descrição, data estimada, dias alocados); confidencialidade, ética e proteção de dados.

## MODO 2 — REDIGIR_NOTA_INFORMATIVA

Nota Informativa interna: destinatário; interessados; referência (projeto e processo SEI informado pelo
usuário); análise (histórico, produtos entregues, próximos passos, tabela Consultoria | Objetivo | Áreas
envolvidas); conclusão ou proposição. Redação pelo Manual de Redação da Presidência da República.

## MODO 3 — REDIGIR_DESPACHO

Despacho de encaminhamento: contexto do processo e do plano operativo; documento encaminhado e seu objeto;
pedido (conhecimento, validação, envio ao parceiro); fecho "À consideração superior." Para triagem do
processo, use a `cgov-triagem-processo-sei`.

## MODO 4 — ALINHAR

Tabela por iniciativa: iniciativa | unidade proponente | eixo do projeto | ação do plano operativo | processos
da Cadeia de Valor | unidades afetadas | lacunas (⚠️).

## MODO 5 — CHECAR_INSUMOS

| Insumo do TdR | Informado? | Observação |
|---|---|---|
| Objetivo e escopo | | |
| Produtos com descrição e prazo | | |
| Perfis dos especialistas (formação, experiência) | | |
| Dias de trabalho por especialista | | |
| Viagens (sim/não; regras do parceiro) | | |
| Acesso a dados institucionais (LGPD) | | |
| Ação do plano operativo e eixo | | |
| Unidades envolvidas e validação | | |

## Fronteiras

- Contratação pelo ICMBio (Lei nº 14.133/2021) e prestação de contas financeira: fora desta skill. Para uma
  contratação direta, ofereça o escopo e os produtos do TdR como insumo à área de contratações e indique a
  `cgov-triagem-processo-sei` para a triagem do processo.
- Nota Técnica de ato normativo: `cgov-nt-01-triagem`.

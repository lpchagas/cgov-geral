---
name: cgov-carta-servicos
description: >
  Carta de Serviços ao Usuário do ICMBio (Lei nº 13.460/2017, art. 7º; Decreto nº 9.094/2017, art. 11):
  levantamento de candidatos a partir das entregas do PGD exportadas do PETRVS, com o script
  scripts/classificar_entregas.py (LEVANTAR), ficha de cada serviço com o conteúdo mínimo da lei e do decreto
  (FICHA), conferência de uma Carta ou de uma página do gov.br (CONFERIR) e Nota Técnica com método, resultados
  e limitações (NT_METODO). Use ao ouvir "Carta de Serviços", "serviços ao cidadão", "Lei 13.460", "quais
  entregas são serviços", "classificar entregas do PETRVS", "ficha do serviço", "página do gov.br". O Catálogo
  de Produtos e Serviços da Cadeia de Valor é da cgov-cadeia-valor.
---

# cgov-carta-servicos — Carta de Serviços ao Usuário

A Carta de Serviços informa ao usuário os serviços prestados, as formas de acesso e os compromissos de
qualidade do atendimento (Lei nº 13.460/2017, art. 7º, § 1º). Esta skill ajuda a levantar quais entregas do
ICMBio são serviços ao usuário e a descrever cada um.

**Enquadramento:** a CGOV trata a Carta de Serviços como desdobramento do Catálogo de Produtos e Serviços (Art.
37, parágrafo único, VI, da Portaria ICMBio nº 5.592/2025; decisão do Coordenador, D53). Ao citar, escreva que
a Carta se apoia no Catálogo; não diga que o inciso VI menciona a Carta, porque ele não a menciona.

## ANTES DE QUALQUER MODO

1. Leia no **acervo normativo** (caminho no `AGENTS.md`, ADR-006) a Lei nº 13.460/2017 e o Decreto nº
   9.094/2017; a lista do conteúdo mínimo está em `references/conteudo-minimo.md`.
2. **Regras invioláveis:**
   - **candidato não é serviço:** o script faz classificação léxica; só a unidade responsável confirma se a
     entrega é serviço ao usuário. Diga isso em toda saída do LEVANTAR;
   - **não invente** requisito, prazo, etapa, canal ou custo de um serviço: o que não vier da unidade, da norma
     do serviço ou da página oficial fica como `[⚠️ confirmar com a unidade]`;
   - **sem credenciais:** a skill nunca se conecta ao PETRVS nem pede usuário ou senha; o usuário exporta os
     dados pelos meios que já usa e entrega o CSV;
   - **sem dados pessoais:** a exportação deve vir agregada por entrega e unidade, sem nome ou matrícula de
     servidor; se vier com essas colunas, peça nova exportação ou remova-as antes de analisar.

## MODO 1 — LEVANTAR (candidatos a partir do PETRVS)

1. Peça o CSV das entregas do período (uma linha por entrega e unidade). Colunas reconhecidas: veja a docstring
   de `scripts/classificar_entregas.py`; no mínimo, `nome_entrega` e `destinatario`.
2. Rode:
   ```
   python scripts/classificar_entregas.py <entrada.csv> --saida <pasta de trabalho> [--minimo 3]
   ```
   Critérios: A, destinatário externo no campo `destinatario` (peso dobrado); B, termo de tipo de serviço nas
   descrições; C, penalidade para atividade interna. A comparação é por palavra inteira e sem acentos.
3. Apresente: totais (lidas, candidatas, qualificadas), distribuição por tipo e por unidade, e as limitações de
   `references/limitacoes.md`. Recomende a consulta às unidades para confirmar cada candidato.
4. Os três CSVs gerados (todas, candidatas e qualificadas; delimitador `|`) vão para a pasta de trabalho do processo; nunca para `referencias/`.

## MODO 2 — FICHA (descrição de um serviço)

Para cada serviço confirmado, preencha a ficha de `references/conteudo-minimo.md` (Lei, art. 7º, §§ 2º e 3º;
Decreto, art. 11, §§ 2º e 3º). Fonte de cada campo ao lado do campo (unidade, norma do serviço, página oficial);
sem fonte, `[⚠️ confirmar com a unidade]`.

## MODO 3 — CONFERIR

Compare uma Carta, uma ficha ou uma página de serviço com o conteúdo mínimo:

| Campo exigido | Dispositivo | Presente? | Observação |
|---|---|---|---|

Aponte também linguagem que não é simples ou exigências sem base normativa citada.

## MODO 4 — NT_METODO

Nota Técnica que registra o levantamento: introdução; fundamentação (Lei nº 13.460/2017, art. 2º, II, e art.
7º; Decreto nº 9.094/2017, art. 11); metodologia (fonte, critérios A, B e C, limiar); resultados (tabelas do
MODO 1); limitações; ações de refinamento (consulta às unidades, revisão manual da categoria "Serviço Público
Geral", padronização do campo `destinatario`, confronto com os atos normativos e com o gov.br); conclusão.
Use a suíte `cgov-nt` para a forma da NT (`cgov-nt-01-triagem`).

## Fronteiras

- Catálogo de Produtos e Serviços e Cadeia de Valor: `cgov-cadeia-valor`.
- Entregas e indicadores do PGD: skills `pgd-*`.

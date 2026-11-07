---
name: cgov-nt-04-diagnostico
description: >
  Quarta etapa da suíte canônica cgov-nt: redige os Capítulos 2 e 3 (Diagnóstico
  e Quadro Consolidado de Achados) de QUALQUER Nota Técnica da CGOV/ICMBio —
  análises normativas, consultas internas, análises de governança institucional
  ou de gestão de riscos — convertendo os achados de `cgov-nt-02` e/ou das
  skills analíticas normativas (cgov-comparar-versoes, cgov-modelar-fluxo,
  cgov-auditoria-competencias) em texto analítico, tabelas e diagramas.
  Use ao invocar /cgov-nt-04, "capítulo de diagnóstico", "capítulos 2 e 3",
  "redigir a análise técnica", "quadro consolidado de achados", ou qualquer
  pedido de transformar achados já levantados em texto de Nota Técnica.
  Requer `NT_ESTADO.md` (na pasta de trabalho do processo) com
  achados já consolidados (por cgov-nt-02 e/ou pelas skills analíticas
  normativas); se não houver achados registrados, redirecione para a skill de
  instrução/diagnóstico correspondente primeiro.
---

# cgov-nt-04 — Capítulos 2 e 3: Diagnóstico e Quadro Consolidado de Achados

## PRÉ-EXECUÇÃO OBRIGATÓRIA

1. **Localização do `NT_ESTADO.md`:** o arquivo vive na **pasta de trabalho do
   processo**, nunca na raiz do projeto; o caminho concreto está no `AGENTS.md`
   do repositório em uso. Procure-o nesta ordem:
   a. na pasta do processo conectada a esta conversa;
   b. na pasta de processos, identificando o processo pelo número SEI citado na
      conversa (compare pelo número, não pelo formato do nome da pasta);
   c. num local antigo listado na tabela de caminhos antigos do `AGENTS.md`, ou
      numa pasta com `MOVIDO_PARA.txt` — nesse caso, avise o usuário de que o
      arquivo está fora da convenção.
   Se houver mais de um candidato e não for possível identificar o processo
   pelo contexto, pergunte ao usuário antes de prosseguir.
2. Leia `NT_ESTADO.md` — em especial a seção "Achados e insumos consolidados".
3. **Pré-requisito de conteúdo:** se essa seção estiver vazia ou incompleta,
   interrompa e informe: "Os achados de [cgov-nt-02 / diagnóstico normativo]
   ainda não constam do NT_ESTADO.md. Execute essa etapa antes de prosseguir."
4. Aplique o **Padrão de Redação CGOV** definido em `cgov-nt-03` (prosa no
   presente do indicativo, remissões completas, numeração decimal, proibição de
   invenção normativa, sem `.docx`).

## FASE 1 — SELEÇÃO DA ESTRUTURA DE DIAGNÓSTICO

O conteúdo do Capítulo 2 varia conforme a natureza do achado. Use apenas as
subseções pertinentes ao caso concreto (não force um template único):

| Natureza do achado | Subseção sugerida | Elemento visual |
|---|---|---|
| Dados quantitativos/qualitativos de consulta | Análise das respostas fechadas / abertas | Tabelas de frequência + caixas de "Ponto Sensível" |
| Diagnóstico normativo (remissões, competências) | Análise técnico-normativa | Tabela comparativa "Redação × Problema" |
| Viabilidade operacional de fluxo/processo | Viabilidade operacional | Diagrama Mermaid (BPMN simplificado, ```mermaid```) |
| Sobreposição de competências | Auditoria de competências | Matriz RACI |
| Governança institucional/organizacional | Sobreposição de instâncias | Tabela comparativa de atribuições |
| Gestão de riscos | Gestão de riscos do instrumento | Matriz de riscos (Causa → Evento → Consequência → Objetivo), com o regime declarado (`cgov-gestao-riscos`) |
| Impacto regulatório | Análise de impacto regulatório | Enquadramento no Decreto nº 10.411/2020 e subsídios do art. 6º (`cgov-air-arr`) |

**Em análise de ato normativo**, as subseções do Capítulo 2 seguem esta ordem:
fluxos; competências; cotejo com a norma anterior; técnica legislativa; gestão de
riscos do instrumento; análise de impacto regulatório; pontos jurídicos. Cada uma
tem método → quadro ou diagrama com dados reais → leitura crítica. O detalhe fica
no produto de cada subsídio; a NT traz a síntese, sem repetir alertas um a um.

## FASE 2 — REDAÇÃO

Para cada subseção selecionada: (1) um parágrafo introdutório em prosa
explicando o método e o escopo da análise; (2) a tabela/diagrama com os dados
efetivamente levantados (nunca com placeholders fictícios); (3) um parágrafo de
leitura crítica dos resultados (o que os dados revelam, não apenas o que dizem
literalmente).

## FORMATO DE SAÍDA

> Numeração reiniciada por capítulo (`#### 2.1`, `#### 2.2`...), conforme
> padrão validado por piloto contra NT real da CGOV — ver `cgov-nt-03`.

```
### Capítulo 2 — Análise Técnica / Diagnóstico

#### 2.1. [Subseção 1 — conforme Fase 1]
[prosa introdutória]

[tabela ou diagrama mermaid]

[leitura crítica]

#### 2.2. [Subseção 2, se houver]
[...]

---

### Capítulo 3 — Quadro Consolidado de Achados

| Nº | Item/Dispositivo/Tema | Eixo | Natureza do Problema/Achado | Impacto | Prioridade |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | Urgente / Prioritário / Desejável |
```

**Regras do Quadro Consolidado:**
- um único quadro, com até cerca de 25 linhas e achados correlatos agrupados;
- em análise de ato normativo, eixos **Fluxo, Competência, Legística, Riscos e AIR**;
- risco já explicado por um achado é vinculado a ele; risco sem achado
  correspondente gera achado novo;
- justifique se um achado ligado a risco residual Extremo não for Urgente.

**Critério de priorização (aplicar de forma consistente a todos os achados):**
- **Urgente:** risco jurídico, operacional ou institucional iminente, ou
  achado que inviabiliza a continuidade do processo sem correção.
- **Prioritário:** relevante para a qualidade/eficácia do produto final, mas
  não bloqueante.
- **Desejável:** melhoria incremental, sem urgência.

## REGRA ESPECIAL — DIAGRAMAS

Diagramas Mermaid só devem ser incluídos quando o achado envolver um fluxo
processual com mais de uma etapa/ator. Não force um diagrama para achados
puramente quantitativos ou de mérito jurídico — nesses casos, a tabela basta.

## PÓS-EXECUÇÃO

O Quadro Consolidado fica no produto do Cap. 2-3 (na pasta de trabalho do
processo, quando gravado); o `NT_ESTADO.md` guarda a contagem e o caminho desse
arquivo. Acrescente ao `NT_ESTADO.md` (na pasta localizada na Pré-execução):
`Cap. 2-3 — Diagnóstico: concluído em [data]. N achados consolidados (X
Urgentes, Y Prioritários, Z Desejáveis).` Essa contagem será reaproveitada
literalmente pela síntese de `cgov-nt-07` — mantenha-a precisa.

## ENCADEAMENTO

```
[cgov-nt-02 e/ou skills analíticas normativas] → /cgov-nt-04 (esta skill) → /cgov-nt-05 ou /cgov-nt-06
```

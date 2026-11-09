---
tipo: decisao
status: proposto
atualizado_em: 2026-11-07
relacionados: [docs/plano-implantacao.md]
---

# ADR-008 — Agentes definidos uma vez no plugin

- **Status:** Proposto
- **Data:** — (aprovação pendente na Fase 0)

## Contexto

Não há camada de agentes (achado A7), e o Maestri não tem versão para Windows, segundo terceiros (achado A8).

## Decisão

Os agentes são definidos uma vez no plugin `cgov-escritorio` e executados no Cowork e no Claude Code; o Maestri é opcional.

## Consequências

- Cinco agentes previstos (triador, orquestrador de NT, revisor normativo, curador do acervo, documentador de painéis).
- O revisor é somente leitura; nenhum agente envia, publica ou protocola no SEI.

## Referências

Fase 9 e Apêndice D do [plano de implantação](../plano-implantacao.md).

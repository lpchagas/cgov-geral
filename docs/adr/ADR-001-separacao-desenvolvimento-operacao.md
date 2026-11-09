---
tipo: decisao
status: aceito
atualizado_em: 2026-11-09
relacionados: [docs/fluxos-de-trabalho.md, docs/governance/pendencias.md]
---

# ADR-001 — Separação desenvolvimento × operação

- **Status:** Aceito
- **Data:** 09/11/2026 (D57; em vigor desde a Fase 1)

## Contexto

O desenvolvimento (skills, documentação, scripts) e a operação (Notas Técnicas, análises de processos SEI) usam repositórios diferentes. A Decisão 27 do [decision-log](../governance/decision-log.md) estabeleceu esse arranjo, com o canal `PENDENCIAS.md` para a operação devolver problemas ao desenvolvimento.

## Decisão

Preservar a separação desenvolvimento × operação (Decisão 27), o canal `90_escritorio-virtual/manutencao/PENDENCIAS.md` e a regra "produção = *commit* publicado".

## Consequências

- A operação só recebe o que passou por *commit* e publicação (`scripts/publicar_operacao.py`).
- Correções descobertas na operação voltam como pendência, nunca como edição direta da fonte.

## Referências

Seções 3.2 e 5.7 do [plano de implantação](../plano-implantacao.md); [`fluxos-de-trabalho.md`](../fluxos-de-trabalho.md).

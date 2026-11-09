---
tipo: decisao
status: proposto
atualizado_em: 2026-11-07
relacionados: [docs/plano-implantacao.md]
---

# ADR-010 — Painéis Power BI em PBIP versionado

- **Status:** Proposto
- **Data:** — (aprovação pendente na Fase 0)

## Contexto

Os painéis da Coordenação não têm catálogo nem fonte versionada (achado A7).

## Decisão

Painéis em PBIP/PBIR versionados no repositório, sem dados; o MCP de autoria só no desenvolvimento; o Fabric IQ só com autorização da TI (D7).

## Consequências

- `.gitignore` já exclui `*.pbix`, `**/.pbi/cache.abf` e `paineis/**/dados/` (etapa 5.7).

## Referências

Fase 10 do [plano de implantação](../plano-implantacao.md).

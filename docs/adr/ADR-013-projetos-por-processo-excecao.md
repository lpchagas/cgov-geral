---
tipo: decisao
status: aceito
atualizado_em: 2026-11-07
relacionados: [docs/plano-implantacao.md]
---

# ADR-013 — Projetos Cowork por processo passam a ser exceção

- **Status:** Aceito
- **Data:** 05/11/2026 (Fase 2)

## Contexto

Há projetos Cowork dedicados a processos (por exemplo, `02070.006604 2026-17_Política de Governança_v2`, `02070.007589/2025-35_TCs`). Com uma pasta por processo, ficha e índice, o projeto **Operação** atende a todos: "trabalhe no processo SEI_02070.020239…".

## Decisão

Novos processos são trabalhados no projeto Operação. Projetos por processo existentes são revistos na Fase 3.C: os que apontam para pastas que serão movidas são **re-apontados** ou **arquivados** depois que suas instruções forem copiadas para `PROCESSO.md` (seção "Instruções específicas"). Exceção: processos muito longos ou sigilosos podem manter projeto próprio, que aponta para a pasta nova do processo.

## Consequências

Menos projetos para manter. A memória de cada projeto arquivado se perde, por isso a cópia prévia das instruções.

## Referências

Fase 3.C e etapa 4.9 do [plano de implantação](../plano-implantacao.md).

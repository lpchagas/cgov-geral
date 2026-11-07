# ADR-009 — Obsidian com dois cofres

- **Status:** Proposto
- **Data:** — (aprovação pendente na Fase 0)

## Contexto

A documentação e a pasta CGOV já usam Markdown com frontmatter, legível por pessoas, por IA e pelo Obsidian.

## Decisão

Cofre de desenvolvimento = o repositório; cofre de operação = a pasta CGOV ("CGOV — Operação", opcional), excluindo as áreas binárias pesadas.

## Consequências

- Página inicial do cofre de desenvolvimento: [`docs/README.md`](../README.md).
- Configuração pessoal (`.obsidian/`) e notas (`/notas/`) ficam fora do Git.

## Referências

Fase 8.3–8.4 do [plano de implantação](../plano-implantacao.md).

---
tipo: decisao
status: aceito
atualizado_em: 2026-11-09
relacionados: [docs/plano-implantacao.md, docs/catalogo-skills.md]
---

# ADR-005 — Distribuição como plugin único `cgov-escritorio`

- **Status:** Aceito
- **Data:** 09/11/2026 (D58; decidido no início da Fase 7)

## Contexto

Hoje a distribuição é feita em 14 zips com reinstalação individual, e o espelho `.agents/skills` é copiado à mão (achado A6); fonte e instalado divergem com frequência (pendência P4).

## Decisão

Distribuir as skills, os comandos e os agentes como um plugin único, `cgov-escritorio`, por upload de zip; o *marketplace* GitHub só depois de testado e com sincronização automática desligada.

## Consequências

- Uma versão por zip, com `CHANGELOG.md`; as skills avulsas são desativadas e depois excluídas da conta.
- `publicar_operacao.py` passa a gerar o zip do plugin.

## Referências

Fase 7 e Apêndice C do [plano de implantação](../plano-implantacao.md).

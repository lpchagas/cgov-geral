# ADR-011 — Qualidade: evals, paridade e sanitização

- **Status:** Proposto
- **Data:** — (aprovação pendente na Fase 0)

## Contexto

Skills já foram instaladas com versões que contradiziam a norma que deviam aplicar (decision-log §§10–11 e 14), e fonte e instalado divergem (pendência P4).

## Decisão

Toda mudança de skill passa por evals com `skill-creator`, verificação de paridade fonte × instalado e verificação de sanitização.

## Consequências

- Prontos na Fase 5: `verificar_sanitizacao.py` e `publicar_operacao.py --verificar` (paridade).
- Evals de todas as skills e pilotos reais ficam para a Fase 11.

## Referências

Fases 5, 6 e 11 do [plano de implantação](../plano-implantacao.md).

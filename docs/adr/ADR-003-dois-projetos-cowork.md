# ADR-003 — Dois projetos Cowork: Implantação e Operação

- **Status:** Aceito
- **Data:** 05/11/2026 (D2)

## Contexto

O projeto Cowork antigo (`cgov-geral-v1`) misturava desenvolvimento e operação.

## Decisão

Dois projetos Cowork: **"Escritório CGOV — Implantação"**, vinculado ao repositório (com acesso temporário à pasta CGOV durante a Fase 4), e **"Escritório CGOV — Operação"**, vinculado à pasta CGOV, que nunca edita o repositório.

## Consequências

- As instruções do projeto Operação ficam em [`system-instructions/escritorio-cgov-operacao.md`](../system-instructions/escritorio-cgov-operacao.md); as do projeto Implantação, no Apêndice A do plano.
- A pasta CGOV foi desvinculada do projeto Implantação ao fim da Fase 4.

## Referências

Fases 3 e 4 do [plano de implantação](../plano-implantacao.md).

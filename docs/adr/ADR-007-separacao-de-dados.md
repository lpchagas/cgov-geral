# ADR-007 — Separação de dados: Git só com fonte sanitizada

- **Status:** Aceito
- **Data:** 07/11/2026 (D40)

## Contexto

Processos SEI, normativos e produtos da Coordenação contêm informação interna e dados pessoais (requisito "Sigilo e LGPD" da Seção 3.1 do plano).

## Decisão

O Git guarda só fonte e documentação sanitizada; processos, normativos e produtos ficam só no Drive, na estrutura da pasta CGOV (ADR-012).

## Consequências

- `local/` é ignorado pelo Git, e as junções `local\processos`, `local\normativos` e `local\escritorio` apontam para o Drive.
- `scripts/verificar_sanitizacao.py` roda antes de todo *commit* (regra 4 do projeto Implantação).
- `.claude/settings.json` bloqueia a edição pelas junções, na pasta CGOV e no `.env` (D39).

## Referências

Seções 3.1 e 5.4 e Fase 5 do [plano de implantação](../plano-implantacao.md).

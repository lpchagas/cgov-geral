# ADR-006 — Skills neutras quanto a caminho

- **Status:** Proposto
- **Data:** — (aprovação pendente na Fase 0)

## Contexto

As skills citam caminhos literais (`local/analyses/`, `local/normative-sources/`, `_CGOV_NT/`), que ficaram obsoletos com a reorganização da pasta CGOV (achado A5; pendência P5).

## Decisão

As skills citam **papéis** ("pasta do processo", "pasta de trabalho do processo", "acervo normativo", "série de Notas Técnicas"); os caminhos concretos ficam no `AGENTS.md` de cada repositório: o do repositório define os de desenvolvimento; o da raiz da pasta CGOV, os de operação.

## Consequências

- Até a Fase 6.3, a tabela de tradução do `AGENTS.md` da pasta CGOV cobre os caminhos antigos.
- Depois dela, sai a seção "Caminhos" das instruções do projeto Operação.

## Referências

Fase 6.3 do [plano de implantação](../plano-implantacao.md); [`operacao/AGENTS.md`](../../operacao/AGENTS.md).

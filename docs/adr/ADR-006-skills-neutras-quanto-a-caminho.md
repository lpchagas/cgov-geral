# ADR-006 — Skills neutras quanto a caminho

- **Status:** Aceito
- **Data:** 07/11/2026 (D48 do plano; aplicado na Fase 6.3)

## Contexto

As skills citam caminhos literais (`local/analyses/`, `local/normative-sources/`, `_CGOV_NT/`), que ficaram obsoletos com a reorganização da pasta CGOV (achado A5; pendência P5).

## Decisão

As skills citam **papéis** ("pasta do processo", "pasta de trabalho do processo", "acervo normativo", "série de Notas Técnicas"); os caminhos concretos ficam no `AGENTS.md` de cada repositório: o do repositório define os de desenvolvimento; o da raiz da pasta CGOV, os de operação.

## Consequências

- Até a Fase 6.3, a tabela de tradução do `AGENTS.md` da pasta CGOV cobre os caminhos antigos.
- Depois dela, sai a seção "Caminhos" das instruções do projeto Operação.
- Aplicação (07/11/2026): as skills citam pasta do processo, pasta de trabalho do processo, pasta de processos, acervo normativo, pasta de rascunhos da transcrição, pasta de trabalho do PGD, lista da equipe e registro de decisões. O mapeamento está na seção "Caminhos por papel" do `AGENTS.md` do repositório e na tabela "Caminhos canônicos" de `operacao/AGENTS.md`. A tabela de caminhos antigos continua, depois da reinstalação, como "Locais antigos", para achar arquivos legados.

## Referências

Fase 6.3 do [plano de implantação](../plano-implantacao.md); [`operacao/AGENTS.md`](../../operacao/AGENTS.md).

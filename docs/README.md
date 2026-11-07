# Documentação do Escritório CGOV (repositório `cgov-geral`)

Página inicial da documentação e do cofre Obsidian de desenvolvimento (ADR-009). Tudo em `docs/` é
mantido sanitizado e publicado, como cópia somente leitura, em `90_escritorio-virtual/referencia/docs/` da
pasta CGOV, por `scripts/publicar_operacao.py`.

## Por onde começar

| Quero… | Leia |
|---|---|
| Entender o que é o Escritório CGOV e a suíte de Notas Técnicas | [Visão geral](overview.md) |
| Saber como desenvolvimento e operação se conversam (projetos Cowork, publicação, pendências) | [Fluxos de trabalho](fluxos-de-trabalho.md) |
| Ver a arquitetura dos dois repositórios | [Arquitetura](architecture.md) |
| Acompanhar a implantação (fases, decisões D1–D40, evidências) | [Plano de implantação](plano-implantacao.md) |
| Saber por que algo foi decidido assim | [ADRs](adr/README.md) e [registro de decisões](governance/decision-log.md) |
| Saber o que falta fazer | [Pendências](governance/pendencias.md) |
| Encontrar uma skill e saber se está atualizada | [Catálogo de skills](catalogo-skills.md) |
| Conferir uma norma citada pelas skills | [Catálogo de fontes normativas](references/normative-catalog.md) |

## Mapa da pasta `docs/`

- [`overview.md`](overview.md) — visão geral da suíte `cgov-nt` e do Escritório de Trabalho da CGOV.
- [`fluxos-de-trabalho.md`](fluxos-de-trabalho.md) — desenvolvimento × operação, configuração no Windows,
  publicação e regras.
- [`architecture.md`](architecture.md) — arquitetura e papéis das pastas.
- [`multiplatform.md`](multiplatform.md) — compatibilidade com Claude, ChatGPT e Antigravity.
- [`plano-implantacao.md`](plano-implantacao.md) — plano de implantação do Escritório Virtual (fonte de
  verdade do andamento).
- [`catalogo-skills.md`](catalogo-skills.md) — as 26 skills do inventário, com fonte e situação.
- [`adr/`](adr/README.md) — os 14 registros de decisão de arquitetura.
- [`governance/`](governance/decision-log.md) — [registro de decisões](governance/decision-log.md) (só
  acréscimos) e [pendências](governance/pendencias.md) do desenvolvimento.
- [`references/`](references/normative-catalog.md) — catálogo público do acervo normativo.
- [`system-instructions/`](system-instructions/escritorio-cgov-operacao.md) — instruções de assistentes:
  - [projeto Cowork "Escritório CGOV — Operação"](system-instructions/escritorio-cgov-operacao.md);
  - [assistente especialista da CGOV](system-instructions/analista-governanca.md), com os anexos
    [normativo](system-instructions/analista-governanca-anexo-normativo.md) e
    [de funções](system-instructions/analista-governanca-anexo-funcoes.md), para assistentes sem acesso a
    arquivos;
  - [analista de processos SEI](system-instructions/analista-processos-sei.md).
- [`reports/`](reports/RELATORIO_cgov-nt.md) — relatórios técnicos e de evals da suíte `cgov-nt`
  (evidência histórica).

## Regras rápidas

- Nada de dados pessoais, matrículas, documentos SEI ou caminhos pessoais aqui: rode
  `py scripts\verificar_sanitizacao.py` antes de cada commit.
- O registro de decisões não se reescreve: só se acrescenta ao final.
- Nunca invente norma, número ou dado; sinalize lacunas com ⚠️.

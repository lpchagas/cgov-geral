# Instruções operacionais para agentes — Escritório CGOV

Este repositório apoia a Coordenação de Governança (CGOV/ICMBio) na elaboração
de Notas Técnicas, análises normativas e instrumentos de governança. A base de
competência é o art. 37 da Portaria ICMBio nº 5.592/2025.

## Fonte de instruções

- Instruções do projeto Cowork "Escritório CGOV — Operação": [`docs/system-instructions/escritorio-cgov-operacao.md`](docs/system-instructions/escritorio-cgov-operacao.md).
- Plano de implantação (andamento e decisões D1–D35): `cgov-geral-plano-implantacao.md` (raiz).
- Pendências de desenvolvimento: [`docs/governance/pendencias.md`](docs/governance/pendencias.md).
- Assistente de processos SEI: [`docs/system-instructions/analista-processos-sei.md`](docs/system-instructions/analista-processos-sei.md).
- Registro de decisões: [`docs/governance/decision-log.md`](docs/governance/decision-log.md).
- Arquitetura e manutenção: [`docs/architecture.md`](docs/architecture.md).
- Fluxos de desenvolvimento e operação: [`docs/fluxos-de-trabalho.md`](docs/fluxos-de-trabalho.md).
- Compatibilidade com Claude, ChatGPT e Antigravity: [`docs/multiplatform.md`](docs/multiplatform.md).

## Regras obrigatórias

1. Para qualquer Nota Técnica ou parecer da CGOV, inicie por `cgov-nt-01-triagem`.
2. As fontes normativas ficam em `03_normativos/` da pasta CGOV (Google Drive) e não integram o
   repositório (privado, mantido sanitizado). O catálogo normativo está em
   [`docs/references/normative-catalog.md`](docs/references/normative-catalog.md).
3. Análises de processos, dados brutos e produtos intermediários ficam na pasta CGOV, em
   `01_processos/<processo>/trabalho/` (estado da NT em `NT_ESTADO.md`), e são produzidos no projeto
   Operação, nunca neste repositório. Testes de desenvolvimento vão para `local/pilots/`.
4. A prosa de Notas Técnicas usa presente do indicativo; capítulos usam
   `### Capítulo N` e subseções `#### N.1`; nunca invente dados ou referências
   normativas.
5. Alterações em fontes de skills exigem atualização sincronizada do snapshot
   instalado quando aplicável e registro no decision log.

## Estrutura relevante

- `skills/cgov-nt/`: fonte canônica da suíte de Notas Técnicas.
- `skills/thematic/`: fontes das skills temáticas da CGOV.
- `local/installed-reference/`: snapshots locais de referência de skills instaladas.
- `operacao/`: fonte dos textos de navegação publicados na pasta CGOV (`LEIA-ME.md`, `AGENTS.md`,
  `_LEIA-ME.md`, modelos).
- `scripts/`: `reorganizar_cgov.py` (Fase 4), `gerar_indices.py` (fichas e índices); os `.sh` do WSL
  estão bloqueados até a Fase 5.
- Junções `local\processos`, `local\normativos` e `local\escritorio` para a pasta CGOV: Fase 5.1
  (as antigas `local/analyses`, `local/normative-sources` e `local/acervo-drive` estão obsoletas).
- `archive/`: local reservado a histórico já sanitizado para publicação.
- `local/`: acervo interno e workspaces de análise, fora do Git.

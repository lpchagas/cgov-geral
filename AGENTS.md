# Instruções operacionais para agentes — Escritório CGOV

Este repositório apoia a Coordenação de Governança (CGOV/ICMBio) na elaboração
de Notas Técnicas, análises normativas e instrumentos de governança. A base de
competência é o art. 37 da Portaria ICMBio nº 5.592/2025.

## Fonte de instruções

- Instruções do projeto Cowork "Escritório CGOV — Operação": [`docs/system-instructions/escritorio-cgov-operacao.md`](docs/system-instructions/escritorio-cgov-operacao.md).
- Documentação: [`docs/README.md`](docs/README.md) (página inicial), [ADRs](docs/adr/README.md) e
  [catálogo de skills](docs/catalogo-skills.md).
- Plano de implantação (andamento e decisões): [`docs/plano-implantacao.md`](docs/plano-implantacao.md).
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

## Modo de execução (Claude Code, D63)

Decisão do Coordenador de 18/11/2026 (D63; decision-log §51). Vale para as sessões do Claude Code neste
repositório; o projeto Cowork "Escritório CGOV — Implantação" segue a regra 1 do Apêndice A do plano.

**Sem pedir confirmação:** rodar scripts, verificadores e testes automatizados; criar e editar arquivos do
repositório; regenerar índices; `publicar_operacao.py --verificar` e `--publicar` (simulação); *commit* e
*push* em `main` (sem regras `ask` de Git no `.claude/settings.json` desde a D63; as `deny` continuam).

**Gate antes de cada *commit*** (se algum falhar: parar, corrigir ou reportar; nunca commitar com falha):

1. `py scripts\gerar_indices_docs.py`;
2. `py scripts\verificar_docs.py` com 0 erro;
3. `py scripts\verificar_sanitizacao.py` com "APROVADO";
4. `git status` e `git diff --stat` conferidos.

*Push* só de *commit* que passou no gate; depois, conferir `main...origin/main` sem diferença. *Commits* em
português, no padrão convencional (`feat`/`fix`/`docs`/`chore`, escopo entre parênteses), um por etapa lógica.

**Exige decisão do Coordenador** (perguntas com 2 a 4 opções, a recomendada primeiro, marcada "(Recomendado)"):

- decisão de negócio ou regra importante: escopo de skills, conteúdo normativo, política de versões,
  publicação em marketplace, desligamento de plataformas;
- ação irreversível ou fora do repositório: `git push --force`, reescrever histórico, excluir ou mover
  arquivos fora da quarentena, mexer na pasta CGOV além do que `publicar_operacao.py --executar` faz com
  conferência SHA-256;
- `publicar_operacao.py --publicar --executar`: mostrar a simulação e a lista de arquivos e esperar "confirmo";
- ambiguidade que mudaria o resultado.

## Caminhos por papel (ADR-006)

As skills citam papéis, não caminhos. Neste repositório (desenvolvimento), os papéis significam:

| Papel citado pelas skills | Caminho no desenvolvimento |
|---|---|
| Pasta do processo / pasta de trabalho do processo | `local/pilots/<caso>/` para testes e evals; o acervo real está em `local/processos/` (somente leitura) |
| Pasta de processos | `local/processos/` (somente leitura) |
| Acervo normativo | `local/normativos/` (somente leitura) |
| Pasta de rascunhos da transcrição | `local/pilots/transcricao/<data-hora>-<slug>/` |
| Registro de decisões | `docs/governance/decision-log.md` |
| Pasta de trabalho do PGD, lista da equipe | só na operação (`operacao/AGENTS.md`) |
| Ferramentas do Escritório | `scripts/` (fonte); publicadas na pasta CGOV por `publicar_operacao.py` |

Na pasta CGOV, vale a tabela de `operacao/AGENTS.md` (publicada como `AGENTS.md` na raiz da pasta).

## Estrutura relevante

- `plugins/cgov-escritorio/skills/`: fonte canônica das 32 skills do plugin `cgov-escritorio` (estrutura plana, uma
  pasta por skill): suíte `cgov-nt-01` a `07` (Notas Técnicas), temáticas da CGOV, PGD (`pgd-*`, Art. 37, p.u., VII),
  análise de atos normativos (competências, versões, fluxos, legística) e operação do Escritório
  (`cgov-gestao-acervo`, `cgov-triagem-processo-sei`). Desde a etapa 7.1 (09/11/2026); antes ficavam em `skills/<família>/`.
- `skills/cgge-fgbio/`: fontes das skills da Formação em Gestão da Biodiversidade (CGGE), fora do plugin `cgov-escritorio`.
- `local/installed-reference/`: snapshots locais de referência de skills instaladas.
- `operacao/`: fonte dos textos de navegação publicados na pasta CGOV (`LEIA-ME.md`, `AGENTS.md`,
  `_LEIA-ME.md`, modelos).
- `scripts/`: `reorganizar_cgov.py` (Fase 4), `gerar_indices.py` (fichas e índices),
  `verificar_sanitizacao.py` (antes de cada commit), `link_acervo.py` (junções) e
  `publicar_operacao.py` (publicação para a pasta CGOV); os `.sh` do WSL foram para `archive/scripts-wsl/`.
- Junções `local\processos`, `local\normativos` e `local\escritorio` para a pasta CGOV, criadas por
  `scripts/link_acervo.py` a partir do `.env` (as antigas `local/analyses`, `local/normative-sources` e
  `local/acervo-drive` são removidas pelo mesmo script). A edição por elas e na pasta CGOV é bloqueada
  em `.claude/settings.json`.
- `archive/`: local reservado a histórico já sanitizado para publicação.
- `local/`: acervo interno e workspaces de análise, fora do Git.

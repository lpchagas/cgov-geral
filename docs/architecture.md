---
tipo: arquitetura
status: vigente
atualizado_em: 2026-11-09
relacionados: [docs/fluxos-de-trabalho.md, docs/multiplatform.md, docs/adr/README.md]
---

# Arquitetura do Escritório CGOV

## Finalidade

O projeto separa artefatos versionáveis e públicos dos materiais de trabalho
internos. A fonte de verdade para evolução das skills fica em `skills/`; a
documentação institucional fica em `docs/`; e dados, processos e fontes locais
ficam em `local/`, fora do Git.

## Suíte `cgov-nt`

`cgov-nt-01-triagem` é sempre a porta de entrada. Conforme o roteiro registrado
em `NT_ESTADO.md`, seguem-se, quando aplicáveis, `cgov-nt-02-instrucao`,
`cgov-nt-03-introducao`, `cgov-nt-04-diagnostico`, `cgov-nt-05-propostas`,
`cgov-nt-06-quesitos-pfe` e `cgov-nt-07-conclusao`.

O estado de cada processo vive exclusivamente em
`01_processos/SEI_<órgão>.<número>_<ano>-<dv>_<apelido>/trabalho/NT_ESTADO.md`, na pasta CGOV
(Google Drive). As skills citam papéis, não caminhos (ADR-006; fontes neutras desde a Fase 6.3 e reinstaladas em
08/11/2026, Fase 6.8). O caminho de cada papel está no `AGENTS.md` da pasta CGOV (fonte: `operacao/AGENTS.md`) e,
no desenvolvimento, no [`AGENTS.md`](../AGENTS.md) da raiz.

## Classes de artefatos

| Local | Papel | Regra de alteração |
|---|---|---|
| `plugins/cgov-escritorio/skills/` (32 skills) e `skills/cgge-fgbio/` | Código-fonte de skills mantidas pela CGOV (a família `cgge-fgbio/` fica fora do plugin `cgov-escritorio`; as demais foram movidas para o plugin na 7.1) | Revisar, executar evals e registrar decisão. |
| `local/installed-reference/` | Snapshot de skills instaladas ou externas | Consulta local; não publicar sem sanitização. |
| `archive/` | Evidência histórica sanitizada | Não alterar conteúdo; apenas acrescentar contexto. |
| `docs/` | Documentação pública sanitizada | Revisar links, precisão normativa e dados pessoais. |
| `operacao/` | Fonte da navegação publicada na pasta CGOV | Publicar sem sobrescrita, com a versão anterior na quarentena. |
| `scripts/` | Ferramentas de manutenção em Python (`publicar_operacao.py`, `link_acervo.py`, `verificar_sanitizacao.py`, `verificar_docs.py`, `gerar_indices_docs.py`, `reorganizar_cgov.py`, `gerar_indices.py`) e `transcribe_normative_batch.mjs` | Versão no cabeçalho; testar antes de usar na pasta CGOV. |
| `dist/` | Pacotes `.zip` das skills gerados por `publicar_operacao.py` | Gerado; fora do Git. |
| `local/` | Processos, insumos e acervo local | Nunca adicionar ao Git. |

## Fluxos de trabalho

O desenvolvimento (Claude Code e projeto Cowork "Escritório CGOV — Implantação", este repositório) e
a operação (projeto Cowork "Escritório CGOV — Operação", pasta CGOV no Google Drive) são separados; a
passagem de um para o outro é a publicação (`scripts/publicar_operacao.py`). Ver
[`fluxos-de-trabalho.md`](fluxos-de-trabalho.md).

## Multiplataforma

Este projeto é operado a partir de mais de um assistente (Claude, ChatGPT,
Antigravity). O mapeamento de qual arquivo cada aplicativo lê, as lacunas
conhecidas e as pendências de decisão estão em
[`multiplatform.md`](multiplatform.md).

## Sincronização

Editar uma skill em `skills/` não altera uma skill instalada em plataforma
externa. Toda atualização requer: revisão do conteúdo, execução dos evals,
publicação (`scripts/publicar_operacao.py`), reinstalação manual quando
cabível e registro em
[`decision-log.md`](governance/decision-log.md).

## Onde ler mais

- Mapa de leitura por tarefa: [`INDICE.md`](INDICE.md).
- Convenções de documentação (fonte única, frontmatter, links): [`convencoes-documentacao.md`](convencoes-documentacao.md).
- Decisões e sua rastreabilidade: [`adr/README.md`](adr/README.md) e [`governance/rastreabilidade.md`](governance/rastreabilidade.md).

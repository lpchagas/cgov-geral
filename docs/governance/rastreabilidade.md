---
tipo: registro
status: vigente
atualizado_em: 2026-11-09
relacionados: [docs/adr/README.md, docs/governance/decision-log.md, docs/governance/decision-log-indice.md, docs/plano-indice.md, docs/governance/pendencias.md, docs/catalogo-skills.md]
---

# Rastreabilidade: ADR ↔ decisão D ↔ seção do registro ↔ fase

> Liga os quatro lugares onde uma decisão aparece: o ADR (regra), a decisão **D** do plano (§9, a pergunta e a resposta
> do Coordenador), a **seção** do [registro de decisões](decision-log.md) (o contexto cronológico) e a **fase** do
> [plano](../plano-indice.md). Mapeamento montado em 09/11/2026 a partir dos títulos das seções e do §9 do plano;
> confira o texto da decisão na fonte antes de citá-la. Convenções: [`convencoes-documentacao.md`](../convencoes-documentacao.md).

## 1. ADRs

| ADR | Decisão | Status | D relacionadas | Registro | Fase | Onde se aplica |
|---|---|---|---|---|---|---|
| [ADR-001](../adr/ADR-001-separacao-desenvolvimento-operacao.md) | Separação desenvolvimento × operação | Aceito | D1, D2 | [§27](decision-log.md#27-migração-para-o-wsl-e-separação-dos-fluxos-de-desenvolvimento-e-operação-06102026) (origem) | Fases 1–3 | `docs/fluxos-de-trabalho.md`, `PENDENCIAS.md`, publicação por commit |
| [ADR-002](../adr/ADR-002-desenvolvimento-no-windows.md) | Desenvolvimento no Windows; WSL aposentado | Aceito | D1 | — | Fase 1 | `archive/scripts-wsl/` |
| [ADR-003](../adr/ADR-003-dois-projetos-cowork.md) | Dois projetos Cowork | Aceito | D2, D13 | — | Fases 2–3 | instruções dos projetos (plano, Apêndice A; `escritorio-cgov-operacao.md`) |
| [ADR-004](../adr/ADR-004-scripts-em-python.md) | Scripts em Python | Aceito | D40 | [§29](decision-log.md#29-atualização-do-repositório-de-desenvolvimento-fase-5-do-plano-de-implantação-0607112026) | Fase 5 | `scripts/*.py` |
| [ADR-005](../adr/ADR-005-plugin-unico.md) | Plugin único `cgov-escritorio` | Proposto | — | — | **Fase 7** | `plugins/` (a criar) |
| [ADR-006](../adr/ADR-006-skills-neutras-quanto-a-caminho.md) | Skills neutras quanto a caminho | Aceito | D48 | [§35](decision-log.md#35-caminhos-neutros-nas-skills-fase-63-07112026) | Fase 6.3 | `AGENTS.md`, `operacao/AGENTS.md`, `skills/` |
| [ADR-007](../adr/ADR-007-separacao-de-dados.md) | Separação de dados | Aceito | D3, D39, D40 | [§29](decision-log.md#29-atualização-do-repositório-de-desenvolvimento-fase-5-do-plano-de-implantação-0607112026) | Fase 5 | `.gitignore`, `verificar_sanitizacao.py`, `.claude/settings.json` |
| [ADR-008](../adr/ADR-008-agentes-no-plugin.md) | Agentes no plugin | Proposto | — | — | Fase 9 | — |
| [ADR-009](../adr/ADR-009-obsidian-dois-cofres.md) | Obsidian com dois cofres | Aceito | D18 | — | Fase 8 (opcional) | `.obsidian/` (ignorado pelo Git) |
| [ADR-010](../adr/ADR-010-paineis-power-bi.md) | Painéis Power BI em PBIP | Proposto | D7 | — | Fase 10 | — |
| [ADR-011](../adr/ADR-011-qualidade.md) | Qualidade: evals, paridade, sanitização | Aceito | D40, D54 | [§41](decision-log.md#41-alcance-dos-evals-da-reinstalação-fase-68-d54-07112026), [§42](decision-log.md#42-resultado-dos-evals-e-correções-antes-da-reinstalação-fase-68a-07112026), [§43](decision-log.md#43-encerramento-da-fase-6-08112026) | Fases 5, 6.8 e 11 | `publicar_operacao.py --verificar`, `verificar_sanitizacao.py`, `evals/` |
| [ADR-012](../adr/ADR-012-estrutura-repositorio-operacional.md) | Estrutura do repositório operacional | Aceito | D10–D16 | [§28](decision-log.md#28-reorganização-da-pasta-operacional-cgov-fase-4-do-plano-de-implantação-0506112026) | Fases 2 e 4 | `operacao/`, pasta CGOV |
| [ADR-013](../adr/ADR-013-projetos-por-processo-excecao.md) | Projetos Cowork por processo são exceção | Aceito | D13, D33 | [§28](decision-log.md#28-reorganização-da-pasta-operacional-cgov-fase-4-do-plano-de-implantação-0506112026) | Fases 2 e 4 | fichas `PROCESSO.md` |
| [ADR-014](../adr/ADR-014-exclusao-controlada.md) | Exclusão controlada | Aceito | D16 | [§28](decision-log.md#28-reorganização-da-pasta-operacional-cgov-fase-4-do-plano-de-implantação-0506112026) | Fases 2 e 4 | quarentena `99_arquivo/_a-excluir_<data>/` |

## 2. Fases e etapas → decisões e registro

| Fase / etapa | Decisões D | Registro |
|---|---|---|
| Fases 1–3 (04–05/11) | D1–D21 | só no plano §9 (o registro não tem seção própria) |
| Fase 4 — pasta CGOV (05–06/11) | D22–D35 | [§28](decision-log.md#28-reorganização-da-pasta-operacional-cgov-fase-4-do-plano-de-implantação-0506112026) |
| Fase 5 — repositório (06–07/11) | D36–D41 | [§29](decision-log.md#29-atualização-do-repositório-de-desenvolvimento-fase-5-do-plano-de-implantação-0607112026) |
| 6.1 — exportação das skills | D42, D43 | [§30](decision-log.md#30-exportação-e-comparação-das-skills-instaladas-fase-61-do-plano-de-implantação-07112026) |
| 6.6 e 6.9(a) — SEI e modelo de atos normativos | D4, D34, D44 | [§31](decision-log.md#31-analista-de-processos-sei-e-modelo-geral-de-análise-de-atos-normativos-fase-66-e-69a-07112026) |
| 6.10 — propostas de skills | D45 | [§32](decision-log.md#32-propostas-de-skills-a-partir-da-pasta-de-prompts-fase-6-etapa-610-07112026) |
| 6.2 — promoção a `skills/` | D46 | [§33](decision-log.md#33-promoção-das-skills-sem-fonte-a-skills-fase-62-07112026) |
| 6.2 — prefixo `pgd-` | D47 | [§34](decision-log.md#34-prefixo-pgd--nas-skills-do-pgd-fase-62-07112026) |
| 6.3 — caminhos neutros | D48 | [§35](decision-log.md#35-caminhos-neutros-nas-skills-fase-63-07112026) |
| 6.5 — descrições e rebase | D49 | [§36](decision-log.md#36-descrições-rebase-da-cgov-gestao-riscos-e-eval-da-cgov-nt-01-fase-65-07112026) |
| 6.9(b)–(d) — modelo nas skills | D50 | [§37](decision-log.md#37-modelo-geral-de-análise-de-atos-normativos-nas-skills-fase-69bd-07112026) |
| 6.4 — skills de operação | D51 | [§38](decision-log.md#38-skills-de-operação-do-escritório-fase-64-e-skill-da-66-07112026) |
| E8 — Portarias 271/2013 e 129/2020 | D52 | [§39](decision-log.md#39-normas-sobre-atos-administrativos-portarias-nº-2712013-e-nº-1292020-pendência-e8-07112026) |
| 6.10 — quatro skills temáticas | D53 | [§40](decision-log.md#40-quatro-skills-temáticas-novas-da-pasta-de-prompts-fase-610-07112026) |
| 6.8 — alcance dos evals | D54 | [§41](decision-log.md#41-alcance-dos-evals-da-reinstalação-fase-68-d54-07112026) |
| 6.8a — resultado dos evals | D55, D56 | [§42](decision-log.md#42-resultado-dos-evals-e-correções-antes-da-reinstalação-fase-68a-07112026) |
| Encerramento da Fase 6 (08/11) | — | [§43](decision-log.md#43-encerramento-da-fase-6-08112026) |
| Revisão documental antes da Fase 7 (09/11) | D57 | [§44](decision-log.md#44-revisão-e-reorganização-da-documentação-antes-da-fase-7-09112026) |

As decisões D estão no [§9 do plano](../plano-implantacao.md#9-decisões-do-coordenador); as fases, no [índice do plano](../plano-indice.md).

## 3. Skills → decisões

| Grupo de skills (catálogo) | Decisões | Registro |
|---|---|---|
| Suíte `cgov-nt` ([catálogo §1](../catalogo-skills.md#1-suíte-de-notas-técnicas-skillscgov-nt)) | D43, D44, D50, D55 | [§30](decision-log.md#30-exportação-e-comparação-das-skills-instaladas-fase-61-do-plano-de-implantação-07112026), [§37](decision-log.md#37-modelo-geral-de-análise-de-atos-normativos-nas-skills-fase-69bd-07112026), [§42](decision-log.md#42-resultado-dos-evals-e-correções-antes-da-reinstalação-fase-68a-07112026) |
| Temáticas ([§2](../catalogo-skills.md#2-skills-temáticas-com-fonte-skillsthematic)) | D43, D45, D49, D53 | [§30](decision-log.md#30-exportação-e-comparação-das-skills-instaladas-fase-61-do-plano-de-implantação-07112026), [§32](decision-log.md#32-propostas-de-skills-a-partir-da-pasta-de-prompts-fase-6-etapa-610-07112026), [§36](decision-log.md#36-descrições-rebase-da-cgov-gestao-riscos-e-eval-da-cgov-nt-01-fase-65-07112026), [§40](decision-log.md#40-quatro-skills-temáticas-novas-da-pasta-de-prompts-fase-610-07112026) |
| PGD ([§3](../catalogo-skills.md#3-skills-do-pgd-skillspgd)) | D43, D46, D47 | [§33](decision-log.md#33-promoção-das-skills-sem-fonte-a-skills-fase-62-07112026), [§34](decision-log.md#34-prefixo-pgd--nas-skills-do-pgd-fase-62-07112026) |
| Atos normativos ([§4](../catalogo-skills.md#4-skills-de-análise-de-atos-normativos-skillsnormativo)) | D44, D46, D50, D52, D56 | [§31](decision-log.md#31-analista-de-processos-sei-e-modelo-geral-de-análise-de-atos-normativos-fase-66-e-69a-07112026), [§37](decision-log.md#37-modelo-geral-de-análise-de-atos-normativos-nas-skills-fase-69bd-07112026), [§39](decision-log.md#39-normas-sobre-atos-administrativos-portarias-nº-2712013-e-nº-1292020-pendência-e8-07112026), [§42](decision-log.md#42-resultado-dos-evals-e-correções-antes-da-reinstalação-fase-68a-07112026) |
| Operação do Escritório ([§5](../catalogo-skills.md#5-skills-de-operação-do-escritório-skillsescritorio)) | D4, D51 | [§31](decision-log.md#31-analista-de-processos-sei-e-modelo-geral-de-análise-de-atos-normativos-fase-66-e-69a-07112026), [§38](decision-log.md#38-skills-de-operação-do-escritório-fase-64-e-skill-da-66-07112026) |

## 4. Aceitação dos ADR-001, 009 e 011 (aplicada em 09/11/2026)

Em 09/11/2026 (D57) o Coordenador confirmou a aceitação dos ADR-001, ADR-009 e ADR-011, **aplicada** nos ADRs, em `adr/README.md` e no §4 do plano. A tabela mantém a evidência e as ressalvas.

| ADR | Evidência de que já vale | Ressalva |
|---|---|---|
| ADR-001 | Separação aplicada desde a Fase 1; canal `PENDENCIAS.md` em uso; produção = *commit* publicado, com publicação conferida por SHA-256 na 6.8 | Nenhuma |
| ADR-009 | Cofre de desenvolvimento em uso (`.obsidian/` no repositório, ignorado pelo Git, D18) | O cofre de operação segue opcional (Fase 8): aceitar registrando isso |
| ADR-011 | `verificar_sanitizacao.py` e `publicar_operacao.py --verificar` em uso; evals executados na 6.8 (129 de 134) | Só 14 das 34 skills têm evals (pendência E9): aceitar o princípio, mantendo a E9 |

**Edição aplicada, por ADR:** `- **Status:** Aceito`; `- **Data:** 09/11/2026 (D57; em vigor desde <fase>)`; frontmatter `status: aceito`; linha do [`adr/README.md`](../adr/README.md); linha do §4 do plano. O **ADR-005** continua proposto e deve ser decidido no início da Fase 7 (pendência E12).

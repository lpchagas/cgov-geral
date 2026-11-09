---
tipo: indice
status: vigente
atualizado_em: 2026-11-09
relacionados: [docs/convencoes-documentacao.md, docs/governance/rastreabilidade.md, docs/plano-indice.md, docs/README.md, archive/README.md, CLAUDE.md, AGENTS.md]
---

# Índice da documentação — o que ler para cada tarefa

> Porta de entrada do repositório `cgov-geral` para pessoas, para o Claude Code e para o Obsidian (ADR-009).
> Regra de ouro: **leia este arquivo, escolha a linha da sua tarefa e abra só o que ela indica.** Três arquivos
> são grandes demais para leitura integral e têm índice próprio (§3). Regras de escrita e manutenção:
> [`convencoes-documentacao.md`](convencoes-documentacao.md).

## 1. Tarefa → leia

| Quero… | Leia (nesta ordem) |
|---|---|
| Entender o projeto em cinco minutos | [Visão geral](overview.md) → [Arquitetura](architecture.md) → [Fluxos §1](fluxos-de-trabalho.md#1-visão-geral) |
| Saber em que fase estamos e o que falta | [Índice do plano](plano-indice.md) → [Quadro de acompanhamento (plano §11)](plano-implantacao.md#11-quadro-de-acompanhamento) → [Pendências em aberto](governance/pendencias.md#em-aberto--desenvolvimento) |
| Alterar uma skill | [CONTRIBUTING](../CONTRIBUTING.md#mudanças-em-skills) → [Fluxos §5](fluxos-de-trabalho.md#5-fluxo-de-desenvolvimento) → [Catálogo de skills](catalogo-skills.md) → [ADR-006 (caminhos por papel)](adr/ADR-006-skills-neutras-quanto-a-caminho.md) |
| Publicar para a operação e reinstalar as skills | [Fluxos §4](fluxos-de-trabalho.md#4-publicação-do-desenvolvimento-para-a-operação) → [ADR-014 (exclusão controlada)](adr/ADR-014-exclusao-controlada.md) |
| Fazer commit com segurança | [Convenções §8](convencoes-documentacao.md#8-antes-do-commit) → [Fluxos §5](fluxos-de-trabalho.md#5-fluxo-de-desenvolvimento) → [ADR-007 (separação de dados)](adr/ADR-007-separacao-de-dados.md) |
| Saber por que algo foi decidido | [Rastreabilidade](governance/rastreabilidade.md) → [ADRs](adr/README.md) → [Índice do registro de decisões](governance/decision-log-indice.md) |
| Preparar a Fase 7 (plugin `cgov-escritorio`) | [Índice do plano](plano-indice.md) (Fase 7) → [ADR-005](adr/ADR-005-plugin-unico.md) → [Rastreabilidade §4](governance/rastreabilidade.md#4-aceitação-dos-adr-001-009-e-011-aplicada-em-09112026) → [Pendências E12 e E14](governance/pendencias.md#em-aberto--desenvolvimento) |
| Entender a pasta CGOV (operação) | [Fluxos §2](fluxos-de-trabalho.md#2-estrutura-da-pasta-cgov-fase-4-0506112026) → [`operacao/LEIA-ME.md`](../operacao/LEIA-ME.md) → [`operacao/AGENTS.md`](../operacao/AGENTS.md) → [ADR-012](adr/ADR-012-estrutura-repositorio-operacional.md) |
| Configurar ou atualizar as instruções de um assistente | [Instruções do projeto Operação](system-instructions/escritorio-cgov-operacao.md) → [Multiplataforma](multiplatform.md) → [Assistente especialista (núcleo)](system-instructions/analista-governanca.md) |
| Analisar um ato normativo | [Procedimento](procedimentos/analise-atos-normativos.md) → [Instruções de projeto (modelo)](../operacao/90_escritorio-virtual/modelos/analise-ato-normativo/INSTRUCOES-PROJETO.md) → [Catálogo §4](catalogo-skills.md#4-skills-de-análise-de-atos-normativos-skillsnormativo) |
| Conferir uma norma citada pelas skills | [Catálogo de fontes normativas](references/normative-catalog.md) → acervo `03_normativos/` da pasta CGOV |
| Triar um processo SEI | [Skill `cgov-triagem-processo-sei`](../skills/escritorio/cgov-triagem-processo-sei/SKILL.md) e, para Gems e GPTs, [instruções do analista de processos SEI](system-instructions/analista-processos-sei-indice.md) |
| Escrever ou revisar documentação | [Convenções de documentação](convencoes-documentacao.md) → `py scripts\verificar_docs.py` |
| Consultar evidência histórica | [Relatório técnico da suíte `cgov-nt`](reports/RELATORIO_cgov-nt.md), [relatório de evals](reports/RELATORIO_EVALS_cgov-nt_2026-08-28.md), [arquivo morto](../archive/README.md) |

## 2. Mapa dos arquivos de `docs/`

| Pasta / arquivo | Tipo | Para quê |
|---|---|---|
| [`README.md`](README.md) | guia | Apresentação da pasta e regras rápidas |
| [`overview.md`](overview.md) | referência | O que existe hoje, suíte `cgov-nt`, cobertura do Art. 37, siglas |
| [`architecture.md`](architecture.md) | arquitetura | Classes de artefatos, regra de alteração de cada pasta |
| [`fluxos-de-trabalho.md`](fluxos-de-trabalho.md) | guia | Desenvolvimento × operação, Windows, publicação, segurança |
| [`multiplatform.md`](multiplatform.md) | referência | Que arquivo cada aplicativo (Claude, ChatGPT, Antigravity) lê |
| [`catalogo-skills.md`](catalogo-skills.md) | catálogo | As 34 skills: função, inciso, situação; links gerados |
| [`convencoes-documentacao.md`](convencoes-documentacao.md) | guia | Como escrever, ligar e manter estes documentos |
| [`plano-implantacao.md`](plano-implantacao.md) | plano | Fases, decisões D, riscos, quadro (**grande: use o índice**) |
| [`adr/`](adr/README.md) | decisão | 14 registros de decisão de arquitetura |
| [`governance/decision-log.md`](governance/decision-log.md) | registro | Histórico cronológico, só acréscimos (**grande: use o índice**) |
| [`governance/pendencias.md`](governance/pendencias.md) | pendências | Abertas e resolvidas |
| [`governance/rastreabilidade.md`](governance/rastreabilidade.md) | registro | ADR ↔ decisão D ↔ seção do registro ↔ fase |
| [`procedimentos/`](procedimentos/analise-atos-normativos.md) | procedimento | Análise de atos normativos pela CGOV |
| [`references/`](references/normative-catalog.md) | referência | Catálogo público de fontes normativas |
| [`reports/`](reports/RELATORIO_cgov-nt.md) | relatório | Evidência histórica da suíte `cgov-nt` |
| [`system-instructions/`](system-instructions/escritorio-cgov-operacao.md) | instrução | Instruções de assistentes (cinco documentos; ver §1) |

## 3. Arquivos grandes: leia pelo índice

| Arquivo | Tamanho | Índice (gerado) |
|---|---|---|
| [`plano-implantacao.md`](plano-implantacao.md) | ~1.600 linhas, ~240 KB | [`plano-indice.md`](plano-indice.md) |
| [`governance/decision-log.md`](governance/decision-log.md) | ~1.700 linhas, ~110 KB | [`governance/decision-log-indice.md`](governance/decision-log-indice.md) |
| [`system-instructions/analista-processos-sei.md`](system-instructions/analista-processos-sei.md) | ~1.200 linhas, ~66 KB | [`system-instructions/analista-processos-sei-indice.md`](system-instructions/analista-processos-sei-indice.md) |

Para o Claude Code: abra o índice, escolha a seção e leia só ela (`Read` com `offset` e `limit` na linha indicada) ou
use `grep -n` no arquivo grande. Os índices são refeitos por `py scripts\gerar_indices_docs.py`.

## 4. Vocabulário fixo

| Termo | Significado |
|---|---|
| **CGOV / CGGE** | Coordenação de Governança / Coordenação-Geral de Governança e Estratégia (ICMBio) |
| **Art. 37** | Art. 37 da Portaria ICMBio nº 5.592/2025: competências da CGOV (incisos do parágrafo único) |
| **NT**, **SEI** | Nota Técnica; Sistema Eletrônico de Informações |
| **Desenvolvimento × Operação** | Este repositório e os projetos Cowork "Implantação" × a pasta CGOV no Google Drive e o projeto "Operação" |
| **ADR-NNN** | Registro de decisão de arquitetura (`adr/`) |
| **D*n*** | Decisão do Coordenador no plano (§9), por exemplo D48 |
| **§*n*** | Seção do [registro de decisões](governance/decision-log-indice.md) |
| **Fase *n*.*m*** | Fase e etapa do [plano](plano-indice.md) |
| **PGR** ≠ **PGRI** ≠ **PGD** | PGR = Programa de Gestão para Resultados e Inovação (Portaria nº 1.572/2023, inciso VIII); PGRI = Política de Gestão de Riscos e Integridade (Portaria nº 255/2020, inciso IX); PGD = Programa de Gestão e Desempenho (IN ICMBio nº 14/2025, inciso VII) |
| **PGE** | Política de Gestão Estratégica (Portaria nº 768/2020): **revogada**, não citar como vigente |
| ⚠️ | Lacuna ou dado a confirmar; nunca preencher de memória |

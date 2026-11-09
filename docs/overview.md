---
tipo: referencia
status: vigente
atualizado_em: 2026-11-09
relacionados: [docs/architecture.md, docs/catalogo-skills.md, docs/plano-implantacao.md]
---

# Resumo Estruturado — Suíte `cgov-nt` e Escritório de Trabalho da CGOV

> **Nota de migração:** referências a caminhos numerados registram a estrutura
> histórica. Para caminhos operacionais vigentes, consulte `README.md` e
> `docs/architecture.md`. Revisado em 09/11/2026 (antes da Fase 7): a tabela "O que existe hoje", a cobertura do
> Art. 37 e os próximos passos refletem o estado de 08/11/2026; as pendências resolvidas preservam os caminhos da
> época em que foram resolvidas.

## O que existe hoje

| Item | Onde | Status |
|---|---|---|
| Suíte canônica `cgov-nt-01` a `07` | Código-fonte em `skills/cgov-nt`; instalada na conta Claude (Customize → Skills), paridade conferida em 08/11/2026 | ✅ Ativa, validada por piloto |
| 34 skills com fonte versionada | `skills/` (6 famílias); inventário em [`catalogo-skills.md`](catalogo-skills.md) | ✅ Reinstaladas e conferidas em 08/11/2026 (Fase 6.8) |
| 13 skills antigas (`pgd-sk*`, `pspeadbio-sk*`) | Removidas da conta Claude; backup em `local/archive/` (fora do Git) | ❌ Desativadas (backup disponível) |
| Skills genéricas pré-existentes (`cgov-comparar-versoes`, `cgov-modelar-fluxo`, `cgov-auditoria-competencias`, `cgov-saneamento-legistica`, `pgd-especialista`, `pgd-elaborar-entrega`, `pgd-avaliar-entrega`, `pgd-registro-execucao`) | Promovidas a fonte em `skills/normativo/` e `skills/pgd/` na Fase 6.2 (07/11/2026) | ✅ Ativas, com fonte versionada |
| Relatório técnico completo (diagnóstico + arquitetura + revisão + piloto) | `docs/reports/RELATORIO_cgov-nt.md` | ✅ |
| Artefatos do piloto | Não versionados (dados de processo real); resumo no relatório técnico | ✅ |
| Fontes normativas | `03_normativos/` da pasta CGOV (desde 05/11/2026; antes `normative-sources/`) + catálogo público | ✅ |
| System Instructions independente | `docs/system-instructions/analista-governanca.md` (núcleo v4.0) + [anexo normativo](system-instructions/analista-governanca-anexo-normativo.md) + [anexo de funções](system-instructions/analista-governanca-anexo-funcoes.md) | ✅ versão canônica v4.0 (29/08/2026) |
| Catálogo normativo público | `docs/references/normative-catalog.md` | ✅ |
| Texto verificado do Art. 37 da Portaria nº 5.592/2025 | `03_normativos/20251211_Art_37_Portaria_5592-2025_texto_verificado.md` da pasta CGOV | ✅ |
| Skills temáticas do Art. 37 | Código-fonte em `skills/thematic/` (11 skills); instaladas na conta Claude | ✅ |
| System Instructions do Analista de Processos SEI | `docs/system-instructions/analista-processos-sei.md` | ✅ v7.3 |
| Instruções do projeto Cowork "Operação" | `docs/system-instructions/escritorio-cgov-operacao.md` | ✅ v1.1 (07/11/2026) |
| Análises e produtos de skills por processo SEI | `01_processos/<processo>/trabalho/` da pasta CGOV (desde 05/11/2026) | ✅ fora do Git |
| Suíte `cgov-nt-01` a `07` | Cria/lê `trabalho/NT_ESTADO.md` (as skills citam papéis, não caminhos, desde a reinstalação de 08/11/2026; caminhos no `AGENTS.md` da pasta CGOV) | ✅ |

## A suíte `cgov-nt`, em uma tabela

| Skill | Capítulo/função da NT | Sempre necessária? |
|---|---|---|
| `cgov-nt-01-triagem` | Enquadramento regimental + roteiro (cria `NT_ESTADO.md`) | **Sim, sempre a primeira** |
| `cgov-nt-02-instrucao` | Análise de dados brutos (quantitativa/qualitativa/perfil) | Só se houver dados brutos |
| `cgov-nt-03-introducao` | Capítulo 1 — Introdução | Sim |
| `cgov-nt-04-diagnostico` | Capítulos 2-3 — Diagnóstico e Achados | Sim |
| `cgov-nt-05-propostas` | Capítulo 4 — Propostas de Ajuste | Se houver recomendações a propor |
| `cgov-nt-06-quesitos-pfe` | Subitem 4.4 — Quesitos do Anexo II (Portaria 271/2013) | Só se a NT for subsidiar a PFE |
| `cgov-nt-07-conclusao` | Capítulo 5 — Conclusão e Encaminhamentos | Sim, sempre a última |

## Regras de redação fixadas pela suíte (aplicam-se a qualquer NT da CGOV)

- Prosa da NT: **presente do indicativo**. Futuro simples só no texto do
  próprio ato normativo (dispositivo/artigo), nunca na prosa analítica.
- Capítulos como `### Capítulo N — [Nome]`; subseções `#### N.1`, `#### N.2`
  reiniciadas por capítulo (nunca `4.N.M`).
- Proposição final em `(i), (ii), (iii)`; Encaminhamentos em lista com
  destinatário em **negrito**.
- Nunca inventar número de norma, artigo ou dado quantitativo — sinalizar
  lacuna explicitamente.
- Saída sempre em Markdown; nunca gerar `.docx` diretamente.

## As 4 correções feitas com base em evidência real (piloto + Portaria 271/2013)

1. Necessidade de PFE depende do **destino do produto**, não do tipo de dado.
2. Numeração de capítulo: `### Capítulo N` / `#### N.1` (não `4.1.1`).
3. Tempo verbal: presente na prosa da NT (não futuro simples).
4. Quesitos PFE: os 8 reais do Anexo II (a tabela antiga tinha só 4 corretos e
   2 que não pertencem ao Anexo II).

## Cobertura do Art. 37 (parágrafo único) após 04/08/2026

| Inciso | Competência | Skill |
|---|---|---|
| I | Coordenação dos processos organizacionais | `pgd-elaborar-entrega`, `pgd-avaliar-entrega`, `pgd-registro-execucao` |
| II | Política de Governança Institucional | suíte `cgov-nt`, `pgd-especialista` (skill dedicada adiada: pendência E7) |
| III | Gestão por processos | `cgov-modelar-fluxo`, `cgov-auditoria-competencias`, `cgov-cadeia-valor` |
| IV | Regimento Interno | `cgov-regimento-interno` |
| V | Quadro de Cargos e Funções (QCF) | `cgov-qcf` (instalada em 30/08/2026) |
| VI | Cadeia de Valor / DFT | `cgov-cadeia-valor`, `cgov-carta-servicos` (desdobramento do Catálogo, D53) |
| VII | PGD (com a CGGP) | `pgd-especialista`, `pgd-*-entrega` |
| VIII | PGR — Gestão para Resultados | `cgov-pgr` |
| IX | Gestão de Riscos / CTGRIC | `cgov-gestao-riscos`, `cgov-integridade` |
| X | AIR / ARR | `cgov-air-arr` |

**10 de 10 incisos com skill de apoio**; só o inciso II ainda não tem skill dedicada (E7, adiada). A tabela completa, com situação de cada skill, está em [`catalogo-skills.md`](catalogo-skills.md).

## Pendências (histórico; as pendências em aberto estão em [`governance/pendencias.md`](governance/pendencias.md))

- ~~Validação pessoal do Coordenador sobre o texto do Art. 37~~ — ✅ **Resolvida
  em 05/07/2026.**
- ~~Instalação das novas skills propostas~~ — ✅ **Concluída em 04/08/2026.**
- ~~Divergência `DIPLAN` × `GABIN` no cabeçalho da NT~~ — ✅ **resolvida em
  04/08/2026:** `Nota Técnica nº [#]/[ano]/CGOV/CGGE/GABIN/ICMBio`.
- ~~Portarias internas ausentes de `04_fontes_normativas/`~~ — ✅ acervo
  depositado em 04/08/2026. As Portarias nº 255/2020, nº 975/2021 e
  nº 1.572/2023 estão legíveis e já foram incorporadas às skills.
- ~~Legibilidade das Portarias nº 4.101/2023, nº 1.164/2025 e nº 253/2026~~ —
  ✅ resolvida em 14/08/2026 por novos uploads com texto legível; os dispositivos
  são citáveis após conferência no acervo.
- ~~Confirmar se a Portaria nº 253/2026 substituiu o Integra+ (nº 923/2020)~~ —
  ✅ resolvida: nº 923/2020 → nº 1.257/2022 → nº 253/2026 (vigente). A remissão
  da Portaria nº 975/2021 à nº 923/2020 está desatualizada.
- ~~Atualizar `cgov-analista-governanca_v2.md`~~ — ✅ concluída em 14/08/2026:
  substituído por `cgov-analista-governanca_v3.md`.
- Editar arquivo em `05_novas_skills_propostas/` **não** altera a skill
  instalada — é preciso reinstalar com sobrescrita.
- ~~As 7 skills da suíte `cgov-nt` ainda instruem, em seu texto literal, criar
  `NT_ESTADO.md` "na raiz do projeto"~~ — ✅ **Resolvida em 05/08/2026:** as 7
  skills foram reescritas e reinstaladas para criar/ler `NT_ESTADO.md`
  diretamente em `07_analises/[processo SEI]_[apelido]/` (ver
  `REGISTRO_DECISOES.md`, Seção 13).

## Convenção de siglas — fixada em 04/08/2026

| Sigla | Significado | Norma | Art. 37, § único |
|---|---|---|---|
| **PGR** | Programa de Gestão para Resultados e Inovação | Portaria ICMBio nº 1.572/2023 | VIII |
| **PGRI** | Política de Gestão de Riscos e Integridade | Portaria ICMBio nº 255/2020 | IX |
| **PGD** | Programa de Gestão e Desempenho (teletrabalho) | IN ICMBio nº 14/2025 | VII |
| **PGE** | Política de Gestão Estratégica | Portaria ICMBio nº 768/2020 (**revogada**; não citar como vigente) | — |

Nunca escrever "PGR de riscos", "PGR (riscos)" nem "Plano de Gestão de Riscos —
PGR". Detalhamento em `04_fontes_normativas/INDICE_FONTES_NORMATIVAS.md`.
- Cópia do PDF completo da Portaria nº 5.592/2025 para `04_fontes_normativas`
  — não foi possível com as ferramentas desta sessão (só gravam texto, não
  binário); cópia manual sugerida, se desejada.
- ~~Execução dos casos de eval ainda não exercitados.~~ — ✅ concluída em
  28/08/2026: 12 de 12 casos aprovados. Os `evals.json` vigentes têm 15 casos
  no total, e não 16 como constava do registro anterior; ver
  `01_relatorios/RELATORIO_EVALS_cgov-nt_2026-08-28.md`.
## Próximos passos

O andamento vigente está no [plano de implantação](plano-implantacao.md) (próxima fase: 7, plugin
`cgov-escritorio`; piloto em processo novo na Fase 11) e as pendências em
[`governance/pendencias.md`](governance/pendencias.md). Os próximos passos sugeridos em 2026 (testar as skills
recém-instaladas, testar a suíte num processo novo e criar a `cgov-qcf`) foram cumpridos ou absorvidos pelo plano:
a `cgov-qcf` foi criada e instalada em 30/08/2026 e o piloto está previsto na Fase 11.

---
tipo: catalogo
status: vigente
atualizado_em: 2026-11-09
relacionados: [docs/governance/pendencias.md, docs/plano-implantacao.md, docs/adr/ADR-006-skills-neutras-quanto-a-caminho.md]
---

# Catálogo de skills da CGOV/CGGE

> Gerado em 07/11/2026 a partir do frontmatter das fontes (`skills/`) e de `py scripts\publicar_operacao.py --verificar`
> (HEAD `d94235e`); **situação de instalação atualizada em 09/11/2026 com o resultado de 08/11**, conforme o resultado da Fase 6.8 (34 skills
> reinstaladas a partir do *commit* `b863ef3`; `--verificar` sem divergências em 08/11/2026). Os links dos nomes das
> skills são refeitos por `py scripts\gerar_indices_docs.py` (necessário depois do `git mv` da Fase 7).
> Atualizar a cada mudança de skill (runbook "Alterar uma skill" do [plano de implantação](plano-implantacao.md)).

> **Desde a etapa 7.1 (09/11/2026)**, as 32 skills das seções 1 a 5 ficam em `plugins/cgov-escritorio/skills/<skill>/` (estrutura plana); os nomes de família `skills/<família>/` nos títulos abaixo são só agrupamento histórico. As 2 `cgge-fgbio-*` continuam em `skills/cgge-fgbio/`.

**Resumo:** 26 skills no inventário da Fase 6 + 2 `cgge-fgbio-*`, **todas com fonte versionada desde a Fase 6.2 (07/11/2026)**. Depois vieram 2 skills de operação (6.4, D51) e 4 temáticas novas (6.10, D53): **34 fontes** em `skills/`, 32 delas no plugin `cgov-escritorio`. **Situação em 09/11/2026: as 34 estão instaladas e iguais à fonte** (Fase 6.8; pendências P4 e P5 resolvidas).
- **14 com fonte desde antes:** estavam 5 iguais ao instalado e 9 desatualizadas (P4); reinstaladas na 6.8.
- **12 promovidas na 6.2** (`skills/pgd/` e `skills/normativo/`) e as 2 `cgge-fgbio-*` (`skills/cgge-fgbio/`), reinstaladas na 6.8. Na 6.1 (07/11/2026), 3 delas (`pgd-avaliar-entrega`, `pgd-elaborar-entrega`, `pgd-registro-execucao`) estavam mais novas na conta que em `local/installed-reference/`; a promoção partiu da exportação `_export_2026-11-07` (D43).
- **Evals:** 14 das 34 têm `evals/evals.json`; as outras 20 estão na pendência E9 ([`pendencias.md`](governance/pendencias.md)).

Inciso = parágrafo único do Art. 37 da Portaria ICMBio nº 5.592/2025. Siglas fixas: **PGR** (Portaria nº 1.572/2023, inciso VIII) ≠ **PGRI** (Portaria nº 255/2020, inciso IX) ≠ **PGD** (IN ICMBio nº 14/2025, inciso VII); a PGE (Portaria nº 768/2020) está revogada.

## 1. Suíte de Notas Técnicas (`skills/cgov-nt/`)

Pipeline de toda NT, para qualquer inciso. A `cgov-nt-01` cria o `NT_ESTADO.md` na pasta de trabalho do processo, e as demais seguem o roteiro gravado nele.

| Skill | Função | Instalada × fonte (08/11) |
|---|---|---|
| [`cgov-nt-01-triagem`](../plugins/cgov-escritorio/skills/cgov-nt-01-triagem/SKILL.md) | Ponto de entrada obrigatório de toda NT: enquadra a demanda no Art. 37 da Portaria ICMBio nº 5.592/2025, identifica as normas e grava o roteiro no `NT_ESTADO.md` | ✅ igual (reinstalada na 6.8) |
| [`cgov-nt-02-instrucao`](../plugins/cgov-escritorio/skills/cgov-nt-02-instrucao/SKILL.md) | Instrução técnica dos dados brutos (planilhas, consultas, indicadores, atas): Quadro de Achados | ✅ igual (reinstalada na 6.8) |
| [`cgov-nt-03-introducao`](../plugins/cgov-escritorio/skills/cgov-nt-03-introducao/SKILL.md) | Capítulo 1 — Introdução (cabeçalho, referências normativas, contexto, metodologia) | ✅ igual (reinstalada na 6.8) |
| [`cgov-nt-04-diagnostico`](../plugins/cgov-escritorio/skills/cgov-nt-04-diagnostico/SKILL.md) | Capítulos 2 e 3 — Diagnóstico e Quadro Consolidado de Achados | ✅ igual (reinstalada na 6.8) |
| [`cgov-nt-05-propostas`](../plugins/cgov-escritorio/skills/cgov-nt-05-propostas/SKILL.md) | Capítulo 4 — Propostas de ajuste e recomendações (opcional) | ✅ igual (reinstalada na 6.8) |
| [`cgov-nt-06-quesitos-pfe`](../plugins/cgov-escritorio/skills/cgov-nt-06-quesitos-pfe/SKILL.md) | Análise para a PFE: os 8 quesitos do Anexo II da Portaria ICMBio nº 271/2013 (condicional) | ✅ igual (reinstalada na 6.8) |
| [`cgov-nt-07-conclusao`](../plugins/cgov-escritorio/skills/cgov-nt-07-conclusao/SKILL.md) | Capítulo 5 — Conclusão, proposição e encaminhamentos | ✅ igual (reinstalada na 6.8) |

## 2. Skills temáticas com fonte (`skills/thematic/`)

| Skill | Inciso | Função | Instalada × fonte (08/11) |
|---|---|---|---|
| [`cgov-regimento-interno`](../plugins/cgov-escritorio/skills/cgov-regimento-interno/SKILL.md) | IV | Atualização do Regimento Interno do ICMBio | ✅ igual (reinstalada na 6.8) |
| [`cgov-qcf`](../plugins/cgov-escritorio/skills/cgov-qcf/SKILL.md) | V | Quadro Demonstrativo de Cargos em Comissão e Funções de Confiança (Decreto nº 12.258/2024) | ✅ igual |
| [`cgov-cadeia-valor`](../plugins/cgov-escritorio/skills/cgov-cadeia-valor/SKILL.md) | VI | Cadeia de Valor, Catálogo de Produtos e Serviços e Dimensionamento da Força de Trabalho (Portaria SEDGG/ME nº 7.888/2022) | ✅ igual |
| [`cgov-pgr`](../plugins/cgov-escritorio/skills/cgov-pgr/SKILL.md) | VIII | PGR — Programa de Gestão para Resultados e Inovação (Portaria ICMBio nº 1.572/2023) | ✅ igual |
| [`cgov-gestao-riscos`](../plugins/cgov-escritorio/skills/cgov-gestao-riscos/SKILL.md) | IX | Gestão de riscos — Metodologia da Portaria ICMBio nº 975/2021 (PGRI: Portaria nº 255/2020) | ✅ igual (reinstalada na 6.8) |
| [`cgov-air-arr`](../plugins/cgov-escritorio/skills/cgov-air-arr/SKILL.md) | X | AIR e ARR (Decreto nº 10.411/2020) | ✅ igual |
| [`cgov-transcrever-normativos`](../plugins/cgov-escritorio/skills/cgov-transcrever-normativos/SKILL.md) | — | OCR, transcrição e gravação em Markdown de atos normativos do acervo | ✅ igual |
| [`cgov-secretaria-colegiados`](../plugins/cgov-escritorio/skills/cgov-secretaria-colegiados/SKILL.md) | — (CTGRIC: Portaria nº 4.529/2025, art. 2º, II) | Pauta, convocação, minuta de ata, encaminhamentos e conferência de ata de colegiados | ✅ igual (instalada na 6.8) |
| [`cgov-integridade`](../plugins/cgov-escritorio/skills/cgov-integridade/SKILL.md) | IX (com a Portaria nº 253/2026, art. 5º, § 2º) | Integra+, Plano de Integridade 2026–2028, monitoramento para o CTGRIC, pesquisa de percepção, riscos para a integridade, Agentes de Integridade | ✅ igual (instalada na 6.8) |
| [`cgov-carta-servicos`](../plugins/cgov-escritorio/skills/cgov-carta-servicos/SKILL.md) | VI (desdobramento do Catálogo, D53) | Carta de Serviços ao Usuário (Lei nº 13.460/2017): candidatos a partir do PETRVS (script sem conexão a banco), ficha, conferência e NT de método | ✅ igual (instalada na 6.8) |
| [`cgov-projetos-cooperacao`](../plugins/cgov-escritorio/skills/cgov-projetos-cooperacao/SKILL.md) | ⚠️ pelo objeto | TdR, Nota Informativa, despacho e alinhamento de projetos de cooperação (primeiro caso: GIZ) | ✅ igual (instalada na 6.8) |

## 3. Skills do PGD (`skills/pgd/`)

Renomeadas com o prefixo `pgd-` em 07/11/2026 (D47). Os nomes antigos (`cgge-especialista-pgd`, `cgov-elaborar-entrega`, `cgov-registro-execucao`, `cgov-avaliar-entrega` e `cgov-pgd-<ação>-indicador`) foram excluídos da conta na 6.8 (08/11/2026).

Promovidas a fonte na Fase 6.2 (07/11/2026) a partir da exportação da conta (`_export_2026-11-07`), saneadas (D46). Saneadas: as três de entregas (nomes da equipe e ciclo quadrimestral como regra, D43) e a de implementar indicador (e-mail e caminhos de exemplo). As três de entregas já trazem o ciclo quadrimestral como regra (D43).

| Skill | Inciso | Função | Instalada × fonte (08/11) |
|---|---|---|---|
| [`pgd-especialista`](../plugins/cgov-escritorio/skills/pgd-especialista/SKILL.md) | VII | Especialista em PGD (teletrabalho, IN ICMBio nº 14/2025): conformidade regimental de entregas e atividades | ✅ igual |
| [`pgd-elaborar-entrega`](../plugins/cgov-escritorio/skills/pgd-elaborar-entrega/SKILL.md) | VII | Criar entrega no Plano de Entregas do PGD | ✅ igual (reinstalada na 6.8) |
| [`pgd-registro-execucao`](../plugins/cgov-escritorio/skills/pgd-registro-execucao/SKILL.md) | VII | Registrar a execução das etapas das entregas | ✅ igual (reinstalada na 6.8) |
| [`pgd-avaliar-entrega`](../plugins/cgov-escritorio/skills/pgd-avaliar-entrega/SKILL.md) | VII | Avaliar a entrega no fim do ciclo (parecer e conceito) | ✅ igual (reinstalada na 6.8) |
| [`pgd-analisar-indicador`](../plugins/cgov-escritorio/skills/pgd-analisar-indicador/SKILL.md) | VII | Análise metodológica de indicador do Instrumento de Avaliação do PGD | ✅ igual |
| [`pgd-desenvolver-indicador`](../plugins/cgov-escritorio/skills/pgd-desenvolver-indicador/SKILL.md) | VII | ETL de indicador do PGD a partir do Data Mart do Petrvs | ✅ igual |
| [`pgd-implementar-indicador`](../plugins/cgov-escritorio/skills/pgd-implementar-indicador/SKILL.md) | VII | Automação (DataOps) de indicador do PGD | ✅ igual (reinstalada na 6.8) |
| [`pgd-testar-indicador`](../plugins/cgov-escritorio/skills/pgd-testar-indicador/SKILL.md) | VII | Qualidade, LGPD e desempenho do script de indicador do PGD | ✅ igual |

## 4. Skills de análise de atos normativos (`skills/normativo/`)

Promovidas na 6.2; o número do processo de referência foi retirado (D46); o contexto padrão do PSPEADBio sai na 6.9(c).

| Skill | Inciso | Função | Instalada × fonte (08/11) |
|---|---|---|---|
| [`cgov-auditoria-competencias`](../plugins/cgov-escritorio/skills/cgov-auditoria-competencias/SKILL.md) | — | Duplicidades e conflitos de competência entre unidades num ato normativo | ✅ igual |
| [`cgov-comparar-versoes`](../plugins/cgov-escritorio/skills/cgov-comparar-versoes/SKILL.md) | — | Comparar versões de dispositivo normativo e propor redação saneada | ✅ igual (reinstalada na 6.8) |
| [`cgov-modelar-fluxo`](../plugins/cgov-escritorio/skills/cgov-modelar-fluxo/SKILL.md) | — | Transformar texto normativo em fluxo BPMN com diagrama Mermaid | ✅ igual (reinstalada na 6.8) |
| [`cgov-saneamento-legistica`](../plugins/cgov-escritorio/skills/cgov-saneamento-legistica/SKILL.md) | — | Técnica legislativa em minutas (Decreto nº 12.002/2024 e LC nº 95/1998) | ✅ igual (reinstalada na 6.8) |

## 5. Skills de operação do Escritório (`skills/escritorio/`)

Criadas na Fase 6.4 (07/11/2026, D51); instaladas na conta na 6.8.

| Skill | Inciso | Função | Instalada × fonte (08/11) |
|---|---|---|---|
| [`cgov-gestao-acervo`](../plugins/cgov-escritorio/skills/cgov-gestao-acervo/SKILL.md) | — | Triagem da caixa de entrada, pasta e ficha de processo, índices (gerador publicado em `90_escritorio-virtual/ferramentas/`) e arquivamento | ✅ igual (instalada na 6.8) |
| [`cgov-triagem-processo-sei`](../plugins/cgov-escritorio/skills/cgov-triagem-processo-sei/SKILL.md) | — | Triagem e instrução de processos SEI (roteamento, passos 0–7, despacho, restituição, ofício, quadro normativo); só Art. 37 (D4, D45) | ✅ igual (instalada na 6.8) |

## 6. Formação em Gestão da Biodiversidade (`skills/cgge-fgbio/`, fora do plugin)

`cgge-fgbio-apresentacao` e `cgge-fgbio-plano-aula`: versionadas na 6.2 (D46), com os nomes do docente e dos convidados trocados por papéis (`[Docente responsável]`, `[Convidado 1]` …); os dados da turma ficam em `local/`. Não entram no plugin `cgov-escritorio`.

## 7. Previstas

- Ampliações feitas na Fase 6.9(b) (07/11/2026, D45, D50): `cgov-nt-06-quesitos-pfe` (consulta jurídica facultativa e NT de subsídio) e `cgov-modelar-fluxo` (BPMN → tabela de atividades/POP).
- Adiada (E7): skill da Política de Governança Institucional (Art. 37, p.u., II).
- `cgov-pbi-documentar-painel` e `cgov-pbi-revisar-modelo` (Fase 10).

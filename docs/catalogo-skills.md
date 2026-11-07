# Catálogo de skills da CGOV/CGGE

> Gerado em 07/11/2026 a partir do frontmatter das fontes (`skills/`), das cópias resgatadas da conta
> (`local/installed-reference/`, fora do Git) e de `py scripts\publicar_operacao.py --verificar` (HEAD `d94235e`).
> Atualizar a cada mudança de skill (runbook "Alterar uma skill" do [plano de implantação](plano-implantacao.md)).

**Resumo:** 26 skills no inventário da Fase 6 + 2 `cgge-fgbio-*`, **todas com fonte versionada desde a Fase 6.2 (07/11/2026)**.
- **14 com fonte desde antes:** 5 iguais ao instalado e 9 desatualizadas na conta (pendência P4; reinstalação na Fase 6.8).
- **12 promovidas na 6.2** (`skills/pgd/` e `skills/normativo/`) e as 2 `cgge-fgbio-*` (`skills/cgge-fgbio/`); a reinstalação de todas fica para a 6.8. Na 6.1 (07/11/2026), 3 delas (`pgd-avaliar-entrega`, `pgd-elaborar-entrega`, `pgd-registro-execucao`) estavam mais novas na conta que em `local/installed-reference/`; a promoção parte da exportação `_export_2026-11-07` (D43).

Inciso = parágrafo único do Art. 37 da Portaria ICMBio nº 5.592/2025. Siglas fixas: **PGR** (Portaria nº 1.572/2023, inciso VIII) ≠ **PGRI** (Portaria nº 255/2020, inciso IX) ≠ **PGD** (IN ICMBio nº 14/2025, inciso VII); a PGE (Portaria nº 768/2020) está revogada.

## 1. Suíte de Notas Técnicas (`skills/cgov-nt/`)

Pipeline de toda NT, para qualquer inciso. A `cgov-nt-01` cria o `NT_ESTADO.md` na pasta de trabalho do processo, e as demais seguem o roteiro gravado nele.

| Skill | Função | Instalada × fonte (07/11) |
|---|---|---|
| `cgov-nt-01-triagem` | Ponto de entrada obrigatório de toda NT: enquadra a demanda no Art. 37 da Portaria ICMBio nº 5.592/2025, identifica as normas e grava o roteiro no `NT_ESTADO.md` | ⚠️ desatualizada |
| `cgov-nt-02-instrucao` | Instrução técnica dos dados brutos (planilhas, consultas, indicadores, atas): Quadro de Achados | ⚠️ desatualizada |
| `cgov-nt-03-introducao` | Capítulo 1 — Introdução (cabeçalho, referências normativas, contexto, metodologia) | ⚠️ desatualizada |
| `cgov-nt-04-diagnostico` | Capítulos 2 e 3 — Diagnóstico e Quadro Consolidado de Achados | ⚠️ desatualizada |
| `cgov-nt-05-propostas` | Capítulo 4 — Propostas de ajuste e recomendações (opcional) | ⚠️ desatualizada |
| `cgov-nt-06-quesitos-pfe` | Análise para a PFE: os 8 quesitos do Anexo II da Portaria ICMBio nº 271/2013 (condicional) | ⚠️ desatualizada |
| `cgov-nt-07-conclusao` | Capítulo 5 — Conclusão, proposição e encaminhamentos | ⚠️ desatualizada |

## 2. Skills temáticas com fonte (`skills/thematic/`)

| Skill | Inciso | Função | Instalada × fonte (07/11) |
|---|---|---|---|
| `cgov-regimento-interno` | IV | Atualização do Regimento Interno do ICMBio | ⚠️ desatualizada |
| `cgov-qcf` | V | Quadro Demonstrativo de Cargos em Comissão e Funções de Confiança (Decreto nº 12.258/2024) | ✅ igual |
| `cgov-cadeia-valor` | VI | Cadeia de Valor, Catálogo de Produtos e Serviços e Dimensionamento da Força de Trabalho (Portaria SEDGG/ME nº 7.888/2022) | ✅ igual |
| `cgov-pgr` | VIII | PGR — Programa de Gestão para Resultados e Inovação (Portaria ICMBio nº 1.572/2023) | ✅ igual |
| `cgov-gestao-riscos` | IX | Gestão de riscos — Metodologia da Portaria ICMBio nº 975/2021 (PGRI: Portaria nº 255/2020) | ⚠️ desatualizada |
| `cgov-air-arr` | X | AIR e ARR (Decreto nº 10.411/2020) | ✅ igual |
| `cgov-transcrever-normativos` | — | OCR, transcrição e gravação em Markdown de atos normativos do acervo | ✅ igual |

## 3. Skills do PGD (`skills/pgd/`)

Renomeadas com o prefixo `pgd-` em 07/11/2026 (D47). Na conta, até a reinstalação da 6.8, ainda aparecem com os nomes antigos: `cgge-especialista-pgd`, `cgov-elaborar-entrega`, `cgov-registro-execucao`, `cgov-avaliar-entrega` e `cgov-pgd-<ação>-indicador`.

Promovidas a fonte na Fase 6.2 (07/11/2026) a partir da exportação da conta (`_export_2026-11-07`), saneadas (D46). Saneadas: as três de entregas (nomes da equipe e ciclo quadrimestral como regra, D43) e a de implementar indicador (e-mail e caminhos de exemplo). As três de entregas já trazem o ciclo quadrimestral como regra (D43).

| Skill | Inciso | Função | Instalada × fonte (07/11) |
|---|---|---|---|
| `pgd-especialista` | VII | Especialista em PGD (teletrabalho, IN ICMBio nº 14/2025): conformidade regimental de entregas e atividades | ✅ igual (texto da conta) |
| `pgd-elaborar-entrega` | VII | Criar entrega no Plano de Entregas do PGD | ⚠️ reinstalar (6.8) |
| `pgd-registro-execucao` | VII | Registrar a execução das etapas das entregas | ⚠️ reinstalar (6.8) |
| `pgd-avaliar-entrega` | VII | Avaliar a entrega no fim do ciclo (parecer e conceito) | ⚠️ reinstalar (6.8) |
| `pgd-analisar-indicador` | VII | Análise metodológica de indicador do Instrumento de Avaliação do PGD | ✅ igual (texto da conta) |
| `pgd-desenvolver-indicador` | VII | ETL de indicador do PGD a partir do Data Mart do Petrvs | ✅ igual (texto da conta) |
| `pgd-implementar-indicador` | VII | Automação (DataOps) de indicador do PGD | ⚠️ reinstalar (6.8) |
| `pgd-testar-indicador` | VII | Qualidade, LGPD e desempenho do script de indicador do PGD | ✅ igual (texto da conta) |

## 4. Skills de análise de atos normativos (`skills/normativo/`)

Promovidas na 6.2; o número do processo de referência foi retirado (D46); o contexto padrão do PSPEADBio sai na 6.9(c).

| Skill | Inciso | Função | Instalada × fonte (07/11) |
|---|---|---|---|
| `cgov-auditoria-competencias` | — | Duplicidades e conflitos de competência entre unidades num ato normativo | ✅ igual (texto da conta) |
| `cgov-comparar-versoes` | — | Comparar versões de dispositivo normativo e propor redação saneada | ⚠️ reinstalar (6.8) |
| `cgov-modelar-fluxo` | — | Transformar texto normativo em fluxo BPMN com diagrama Mermaid | ⚠️ reinstalar (6.8) |
| `cgov-saneamento-legistica` | — | Técnica legislativa em minutas (Decreto nº 12.002/2024 e LC nº 95/1998) | ⚠️ reinstalar (6.8) |

## 4-A. Formação em Gestão da Biodiversidade (`skills/cgge-fgbio/`, fora do plugin)

`cgge-fgbio-apresentacao` e `cgge-fgbio-plano-aula`: versionadas na 6.2 (D46), com os nomes do docente e dos convidados trocados por papéis (`[Docente responsável]`, `[Convidado 1]` …); os dados da turma ficam em `local/`. Não entram no plugin `cgov-escritorio`.

## 5. Previstas

- `cgov-gestao-acervo` (Fase 6.4): triagem de `00_entrada`, pasta e ficha de processo, índices.
- `cgov-triagem-processo-sei` (D4, 07/11/2026: criar a skill e manter `docs/system-instructions/analista-processos-sei.md` como versão autocontida; escrita junto com a 6.4).
- `cgov-secretaria-colegiados`, `cgov-integridade`, `cgov-carta-servicos` e `cgov-projetos-cooperacao` (Fase 6.10, D45, a partir da pasta de prompts `02_dev-prompts`).
- Ampliações (Fase 6.9(b), D45): `cgov-nt-06-quesitos-pfe` (consulta jurídica facultativa e NT de subsídio) e `cgov-modelar-fluxo` (BPMN → tabela de atividades/POP).
- Adiada (E7): skill da Política de Governança Institucional (Art. 37, p.u., II).
- `cgov-pbi-documentar-painel` e `cgov-pbi-revisar-modelo` (Fase 10).

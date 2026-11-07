# Catálogo de skills da CGOV/CGGE

> Gerado em 07/11/2026 a partir do frontmatter das fontes (`skills/`), das cópias resgatadas da conta
> (`local/installed-reference/`, fora do Git) e de `py scripts\publicar_operacao.py --verificar` (HEAD `d94235e`).
> Atualizar a cada mudança de skill (runbook "Alterar uma skill" do [plano de implantação](plano-implantacao.md)).

**Resumo:** 26 skills no inventário da Fase 6.
- **14 com fonte versionada:** 5 iguais ao instalado e 9 desatualizadas na conta (pendência P4; reinstalação na Fase 6.8).
- **12 sem fonte**, só na conta (promoção a `skills/` na Fase 6.2). Na 6.1 (07/11/2026), 3 delas (`cgov-avaliar-entrega`, `cgov-elaborar-entrega`, `cgov-registro-execucao`) estavam mais novas na conta que em `local/installed-reference/`; a promoção parte da exportação `_export_2026-11-07` (D43).

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

## 3. Skills sem fonte versionada (só na conta)

Cópias de referência em `local/installed-reference/` (fora do Git). Na Fase 6.2, elas são promovidas a `skills/<família>/`, sem dados pessoais nem caminhos absolutos.

| Skill | Inciso | Função |
|---|---|---|
| `cgge-especialista-pgd` | VII | Especialista em PGD (teletrabalho, IN ICMBio nº 14/2025): conformidade regimental de entregas e atividades |
| `cgov-elaborar-entrega` | VII | Criar entrega no Plano de Entregas do PGD |
| `cgov-registro-execucao` | VII | Registrar a execução das etapas das entregas |
| `cgov-avaliar-entrega` | VII | Avaliar a entrega no fim do ciclo (parecer e conceito) |
| `cgov-pgd-analisar-indicador` | VII | Análise metodológica de indicador do Instrumento de Avaliação do PGD |
| `cgov-pgd-desenvolver-indicador` | VII | ETL de indicador do PGD a partir do Data Mart do Petrvs |
| `cgov-pgd-implementar-indicador` | VII | Automação (DataOps) de indicador do PGD |
| `cgov-pgd-testar-indicador` | VII | Qualidade, LGPD e desempenho do script de indicador do PGD |
| `cgov-auditoria-competencias` | — | Duplicidades e conflitos de competência entre unidades num ato normativo |
| `cgov-comparar-versoes` | — | Comparar versões de dispositivo normativo e propor redação saneada |
| `cgov-modelar-fluxo` | — | Transformar texto normativo em fluxo BPMN com diagrama Mermaid |
| `cgov-saneamento-legistica` | — | Técnica legislativa em minutas (Decreto nº 12.002/2024 e LC nº 95/1998) |

## 4. Fora do inventário

⚠️ Também aparecem na conta `cgge-fgbio-apresentacao` e `cgge-fgbio-plano-aula`, que não estão entre as 26 do inventário. Foram exportadas na Fase 6.1 (07/11/2026); decidir na 6.2 se entram no plugin `cgov-escritorio` ou ficam à parte.

## 5. Previstas

- `cgov-gestao-acervo` (Fase 6.4): triagem de `00_entrada`, pasta e ficha de processo, índices.
- `cgov-triagem-processo-sei` (D4, 07/11/2026: criar a skill e manter `docs/system-instructions/analista-processos-sei.md` como versão autocontida; escrita junto com a 6.4).
- `cgov-pbi-documentar-painel` e `cgov-pbi-revisar-modelo` (Fase 10).

# Plugin `cgov-escritorio` — Escritório CGOV (ICMBio)

Plugin do Escritório Virtual da Coordenação de Governança (CGOV/CGGE/ICMBio): reúne as skills que apoiam Notas Técnicas,
análise normativa e demais instrumentos de governança. Versão atual: **0.1.0** (pré-lançamento; a `1.0.0` só depois do
teste da etapa 7.6 do plano de implantação).

> Fonte de desenvolvimento. A operação diária (Notas Técnicas, processos SEI) acontece no projeto Cowork
> "Escritório CGOV — Operação", não aqui. Decisão de arquitetura: [ADR-005](../../docs/adr/ADR-005-plugin-unico.md).

## Conteúdo (32 skills, estrutura plana em `skills/`)

| Família | Skills |
|---|---|
| Notas Técnicas (7) | `cgov-nt-01-triagem`, `cgov-nt-02-instrucao`, `cgov-nt-03-introducao`, `cgov-nt-04-diagnostico`, `cgov-nt-05-propostas`, `cgov-nt-06-quesitos-pfe`, `cgov-nt-07-conclusao` |
| Operação do Escritório (2) | `cgov-gestao-acervo`, `cgov-triagem-processo-sei` |
| Análise normativa (4) | `cgov-auditoria-competencias`, `cgov-comparar-versoes`, `cgov-modelar-fluxo`, `cgov-saneamento-legistica` |
| PGD (8) | `pgd-analisar-indicador`, `pgd-avaliar-entrega`, `pgd-desenvolver-indicador`, `pgd-elaborar-entrega`, `pgd-especialista`, `pgd-implementar-indicador`, `pgd-registro-execucao`, `pgd-testar-indicador` |
| Temáticas (11) | `cgov-air-arr`, `cgov-cadeia-valor`, `cgov-carta-servicos`, `cgov-gestao-riscos`, `cgov-integridade`, `cgov-pgr`, `cgov-projetos-cooperacao`, `cgov-qcf`, `cgov-regimento-interno`, `cgov-secretaria-colegiados`, `cgov-transcrever-normativos` |

Ficam **fora** do plugin as 2 skills da Formação CGGE (`cgge-fgbio-apresentacao`, `cgge-fgbio-plano-aula`), em
`skills/cgge-fgbio/` na raiz do repositório (D46). Comandos (etapa 7.2) e agentes (Fase 9) serão acrescentados aqui.

## Instalação (resumo; roteiro completo na etapa 7.5 do plano)

1. Gerar o zip com `py scripts\publicar_operacao.py` (etapa 7.3; ainda não disponível nesta versão do script).
2. Em Claude: **Customize → Plugins → Add → Upload plugin**, enviando `dist\cgov-escritorio-<versão>.zip`.
3. Testar no projeto "Escritório CGOV — Operação" e conferir com `py scripts\publicar_operacao.py --verificar`.

## Manutenção

Alterar uma skill: editar `skills/<skill>/SKILL.md` aqui, rodar os evals (`skills/<skill>/evals/`), validar com
`claude plugin validate .\plugins\cgov-escritorio`, registrar no `CHANGELOG.md` (a criar na 7.6) e no
[decision-log](../../docs/governance/decision-log.md). Sem dados pessoais, matrículas ou documentos SEI: rodar
`py scripts\verificar_sanitizacao.py` antes de cada commit.

# Registros de decisão de arquitetura (ADRs)

Cada ADR registra uma decisão de arquitetura do Escritório Virtual da CGOV: o contexto, a decisão e as
consequências. Os ADRs aceitos valem como regra; os propostos aguardam a aprovação do Coordenador na Fase 0
do [plano de implantação](../plano-implantacao.md). Uma aprovação muda só o campo **Status** e a **Data**;
uma decisão substituída ganha um ADR novo, e o antigo passa a "Substituído por ADR-NNN" (o texto não é
reescrito).

| ADR | Status | Data |
|---|---|---|
| [ADR-001 — Separação desenvolvimento × operação](ADR-001-separacao-desenvolvimento-operacao.md) | Proposto | — (aprovação pendente na Fase 0) |
| [ADR-002 — Desenvolvimento no Windows; WSL aposentado](ADR-002-desenvolvimento-no-windows.md) | Aceito | 04/11/2026 (Fase 1) |
| [ADR-003 — Dois projetos Cowork: Implantação e Operação](ADR-003-dois-projetos-cowork.md) | Aceito | 05/11/2026 (D2) |
| [ADR-004 — Scripts multiplataforma em Python](ADR-004-scripts-em-python.md) | Aceito | 07/11/2026 (D40) |
| [ADR-005 — Distribuição como plugin único `cgov-escritorio`](ADR-005-plugin-unico.md) | Proposto | — (aprovação pendente na Fase 0) |
| [ADR-006 — Skills neutras quanto a caminho](ADR-006-skills-neutras-quanto-a-caminho.md) | Aceito | 07/11/2026 (D48; aplicado na Fase 6.3) |
| [ADR-007 — Separação de dados: Git só com fonte sanitizada](ADR-007-separacao-de-dados.md) | Aceito | 07/11/2026 (D40) |
| [ADR-008 — Agentes definidos uma vez no plugin](ADR-008-agentes-no-plugin.md) | Proposto | — (aprovação pendente na Fase 0) |
| [ADR-009 — Obsidian com dois cofres](ADR-009-obsidian-dois-cofres.md) | Proposto | — (aprovação pendente na Fase 0) |
| [ADR-010 — Painéis Power BI em PBIP versionado](ADR-010-paineis-power-bi.md) | Proposto | — (aprovação pendente na Fase 0) |
| [ADR-011 — Qualidade: evals, paridade e sanitização](ADR-011-qualidade.md) | Proposto | — (aprovação pendente na Fase 0) |
| [ADR-012 — Estrutura do repositório operacional](ADR-012-estrutura-repositorio-operacional.md) | Aceito | 05/11/2026 (Fase 2) |
| [ADR-013 — Projetos Cowork por processo passam a ser exceção](ADR-013-projetos-por-processo-excecao.md) | Aceito | 05/11/2026 (Fase 2) |
| [ADR-014 — Exclusão controlada](ADR-014-exclusao-controlada.md) | Aceito | 05/11/2026 (Fase 2) |

## Modelo

```markdown
# ADR-NNN — <título>

- **Status:** Proposto | Aceito | Rejeitado | Substituído por ADR-NNN
- **Data:** DD/MM/AAAA (decisão D<nº> do plano)

## Contexto
## Decisão
## Consequências
## Referências
```

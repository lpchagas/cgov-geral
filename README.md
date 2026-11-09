# Escritório CGOV

Repositório privado e sanitizado da Coordenação de Governança (CGOV/ICMBio) para
manutenção de skills, documentação metodológica e instruções de assistentes.

## Conteúdo

- **Comece por [`docs/INDICE.md`](docs/INDICE.md)** (o que ler para cada tarefa).
- [Visão geral](docs/overview.md), [arquitetura](docs/architecture.md) e [fluxos de desenvolvimento e operação](docs/fluxos-de-trabalho.md).
- [Página inicial da documentação](docs/README.md), [ADRs](docs/adr/README.md) e [catálogo de skills](docs/catalogo-skills.md).
- [Plano de implantação do Escritório Virtual](docs/plano-implantacao.md) (andamento, decisões e evidências).
- [Pendências](docs/governance/pendencias.md).
- Skills (fontes): [`cgov-nt`](skills/cgov-nt/), [temáticas](skills/thematic/), [PGD](skills/pgd/), [atos normativos](skills/normativo/), [operação do Escritório](skills/escritorio/) e [Formação CGGE](skills/cgge-fgbio/); inventário em [`docs/catalogo-skills.md`](docs/catalogo-skills.md).
- [Procedimento de análise de atos normativos](docs/procedimentos/analise-atos-normativos.md).
- [Instruções de assistentes](docs/system-instructions/), entre elas as do projeto Cowork ["Escritório CGOV — Operação"](docs/system-instructions/escritorio-cgov-operacao.md).
- [Navegação da pasta operacional](operacao/) (fonte de `LEIA-ME.md`, `AGENTS.md`, `_LEIA-ME.md` e modelos) e [scripts](scripts/) de manutenção.
- [Catálogo de fontes normativas](docs/references/normative-catalog.md).
- [Registro de decisões](docs/governance/decision-log.md) e [rastreabilidade ADR ↔ decisão ↔ fase](docs/governance/rastreabilidade.md).

## Política de dados

O repositório não publica processos SEI, dados de consultas, rascunhos de
trabalho nem cópias locais de fontes normativas. Esses materiais ficam na pasta
operacional CGOV (Google Drive) ou em `local/`, que é integralmente ignorado pelo Git. O catálogo normativo (`docs/references/normative-catalog.md`) referencia
fontes oficiais sem redistribuir PDFs ou materiais de terceiros.

## Estado do projeto

A suíte `cgov-nt-01` a `cgov-nt-07` é a fonte canônica para elaboração de Notas
Técnicas. As Fases 1 a 6 do [plano de implantação](docs/plano-implantacao.md) estão concluídas (até 08/11/2026):
34 skills com fonte versionada, reinstaladas e conferidas; a próxima é a Fase 7 (plugin `cgov-escritorio`).
Material histórico ainda não sanitizado e snapshots instalados ficam
preservados em `local/archive/` e `local/installed-reference/`, fora do Git.

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) antes de propor mudanças.

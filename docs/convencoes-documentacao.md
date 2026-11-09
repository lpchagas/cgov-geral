---
tipo: guia
status: vigente
atualizado_em: 2026-11-09
relacionados: [docs/INDICE.md, scripts/verificar_docs.py, scripts/gerar_indices_docs.py, docs/adr/ADR-007-separacao-de-dados.md, CONTRIBUTING.md]
---

# Convenções de documentação

Regras para escrever, ligar e manter os Markdown deste repositório, de modo que sirvam de "segundo cérebro" para
pessoas, para o Claude Code e para o Obsidian. São verificadas por `py scripts\verificar_docs.py`.

## 1. Princípios

1. **Fonte única.** Cada fato mora em um só arquivo (§2); os demais apontam para ele.
2. **Link, não duplique.** Se for preciso repetir mais de uma frase, troque por um link.
3. **Histórico não se reescreve.** O registro de decisões só recebe acréscimos; versão superada vai para `archive/` com o sufixo `_ate-AAAA-MM-DD`.
4. **Todo documento tem tipo, estado e data** (frontmatter, §3).
5. **Tamanho tem teto.** Acima de 600 linhas, o documento ganha índice gerado e aviso "não leia inteiro".
6. **Tudo é verificável.** Links, âncoras, frontmatter e contagens são conferidos por script antes do commit.

## 2. Fonte única: onde mora cada fato

| Fato | Fonte única | Derivados (não editar à mão) |
|---|---|---|
| Andamento, fases e decisões D | [`plano-implantacao.md`](plano-implantacao.md) | [`plano-indice.md`](plano-indice.md) |
| Decisão de arquitetura | [`adr/`](adr/README.md) | tabela do `adr/README.md` e §4 do plano (mesmo status) |
| Histórico cronológico | [`governance/decision-log.md`](governance/decision-log.md) | [`decision-log-indice.md`](governance/decision-log-indice.md) |
| Ligação ADR ↔ D ↔ § ↔ fase | [`governance/rastreabilidade.md`](governance/rastreabilidade.md) | — |
| Pendências | [`governance/pendencias.md`](governance/pendencias.md) | — |
| Inventário e situação das skills | [`catalogo-skills.md`](catalogo-skills.md) | links dos nomes (gerados) |
| Caminhos por papel | `AGENTS.md` (desenvolvimento) e `operacao/AGENTS.md` (operação) | — |
| Instruções do projeto Operação | [`system-instructions/escritorio-cgov-operacao.md`](system-instructions/escritorio-cgov-operacao.md) | — |
| Instruções do projeto Implantação | Apêndice A do plano | — |
| Navegação da pasta CGOV | `operacao/` | cópia publicada no Drive |
| Siglas e vocabulário fixo | [`INDICE.md`](INDICE.md) §4 | cópias obrigatórias nas instruções autocontidas do analista (Gems e GPTs não leem o repositório) |

Cópias autocontidas (`analista-governanca*.md`, `analista-processos-sei.md`) existem por exigência de assistentes sem
acesso a arquivos; ao mudar um fato normativo, atualize também essas cópias.

## 3. Frontmatter

Todo `.md` de `docs/` começa com:

```yaml
---
tipo: guia              # guia | referencia | arquitetura | decisao | registro | plano | procedimento | instrucao | relatorio | indice | indice-gerado | pendencias | catalogo
status: vigente         # vigente | rascunho | historico | substituido   (ADR: proposto | aceito | rejeitado | substituido)
versao: "1.0"           # opcional
atualizado_em: 2026-11-09
relacionados: [docs/adr/README.md, scripts/verificar_docs.py]   # opcional; caminhos a partir da raiz, em lista de uma linha
---
```

- `relacionados` é a conexão explícita entre arquivos (o verificador confere se existem).
- Nos ADRs, `status` deve coincidir com a linha `**Status:**` do corpo e com `adr/README.md`.
- `status: historico` exige um aviso "Documento histórico" nas primeiras linhas.
- **Exceção:** `analista-governanca.md` e `analista-processos-sei.md` não levam frontmatter, porque são colados inteiros em
  campos com limite de caracteres. Seus metadados ficam no [`INDICE.md`](INDICE.md).
- Índices gerados (`indice-gerado`) não têm `atualizado_em`; trazem `gerado_de`.

## 4. Links

- Links **relativos** e com âncora no estilo do GitHub (minúsculas, sem pontuação, espaços viram hífens).
- Referências como "D48", "§35" ou "ADR-006" devem apontar para o destino pelo menos na primeira menção de cada seção; a tabela está em [`rastreabilidade.md`](governance/rastreabilidade.md).
- Não ligue a cabeçalhos cujo texto muda (por exemplo, títulos de fase com status); ligue ao índice gerado.
- Caminhos de skills aparecem só no catálogo (links gerados). Depois do `git mv` da Fase 7, rode `py scripts\gerar_indices_docs.py`.
- Dentro de blocos de código e em `código em linha`, o verificador não confere links.

## 5. Estados de vida de um documento

| Estado | Significado | O que fazer |
|---|---|---|
| vigente | Vale hoje | Manter, datar a cada mudança |
| rascunho | Em construção | Não citar como regra |
| historico | Evidência de uma época | Aviso no topo; conteúdo não muda |
| substituido | Há versão nova | Mover para `archive/` com `_ate-AAAA-MM-DD` e apontar o substituto |

## 6. Tamanho e leitura pelo Claude Code

Arquivo com mais de 600 linhas precisa de índice gerado (veja `INDICES` em `scripts/gerar_indices_docs.py`). O
Claude Code deve ler o [`INDICE.md`](INDICE.md), abrir o índice do arquivo grande e ler só a seção necessária.
`CLAUDE.md` e `AGENTS.md` são carregados em toda sessão: mantenha-os curtos e com links, sem repetir o que está em `docs/`.

## 7. Quando criar o quê

| Situação | Onde registrar |
|---|---|
| Decisão estrutural, difícil de reverter | ADR novo (e linha em `adr/README.md`) |
| Decisão do Coordenador numa etapa | Linha D*n* no §9 do plano + seção no decision-log |
| Algo a fazer depois | Linha em `pendencias.md` |
| Mudança de skill | Fonte → evals → decision-log → publicação (CONTRIBUTING) |
| Problema na operação | `90_escritorio-virtual/manutencao/PENDENCIAS.md` da pasta CGOV |

## 8. Antes do commit

```powershell
Set-Location C:\Projetos\cgov-geral
py scripts\gerar_indices_docs.py
py scripts\verificar_docs.py
py scripts\verificar_sanitizacao.py --staged
git status
```

Erros do `verificar_docs.py` bloqueiam; avisos devem ser lidos e, se forem intencionais, justificados no commit.
Commit e push só com confirmação do Coordenador.

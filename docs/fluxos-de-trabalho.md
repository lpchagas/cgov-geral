# Fluxos de trabalho — desenvolvimento e operação

> Versão 2 — 06/11/2026, depois da Fase 4 do plano de implantação (reorganização da pasta CGOV).
> Substitui a versão de 06/10/2026 (arquivada em `archive/docs/fluxos-de-trabalho_ate-2026-11-06.md`).
> Itens marcados ⏳ dependem da Fase 5 do plano (scripts e junções novos).

## 1. Visão geral

| | **Desenvolvimento** | **Operação (produção)** |
|---|---|---|
| Para quê | Criar e corrigir skills, instruções, documentação e scripts | Produzir Notas Técnicas, pareceres, análises de processos SEI e demais demandas da CGOV |
| Ferramenta | Claude Code e projeto Cowork **"Escritório CGOV — Implantação"** (Windows); Antigravity e Obsidian | Projeto Cowork **"Escritório CGOV — Operação"** (app Claude no Windows) |
| Pasta de trabalho | Este repositório (`C:\Projetos\cgov-geral` no computador do Coordenador) | Pasta **CGOV** do Google Drive (`…\My Drive\10_Institucional\CGOV`) |
| Versão das skills | Fonte em `skills/` (rascunho até o commit) | Skills **instaladas** na conta Claude |
| Documentação | `docs/` (edição) | `90_escritorio-virtual/referencia/docs/` (cópia só leitura) ⏳ republicação na Fase 5.3 |
| Navegação da pasta | `operacao/` (fonte) | `LEIA-ME.md`, `AGENTS.md`, `_LEIA-ME.md`, modelos (publicados) |
| Dados de processos | Não produz | `01_processos/<processo>/` (ficha `PROCESSO.md`; estado da NT em `trabalho/NT_ESTADO.md`) |
| Publicação | Git → GitHub (repositório **privado**, mantido sanitizado) | Nada é publicado; tudo fica no Drive |

Regra central: **o projeto Operação nunca edita o repositório e o desenvolvimento nunca produz trabalho de
processo.** O que liga os dois é a *publicação* (§4) num sentido e o arquivo de *pendências* (§5) no outro.

```
 DESENVOLVIMENTO (Claude Code / Cowork "Implantação")     OPERAÇÃO (Cowork "Operação")
 C:\Projetos\cgov-geral                                  My Drive\10_Institucional\CGOV
   skills/  docs/  scripts/  operacao/  (Git)              LEIA-ME.md · AGENTS.md
        │ commit → publicação (⏳ publicar_operacao.py)     00_entrada … 06_gestao-da-coordenacao
        ├──► dist/skills/*.zip ── reinstalar ─────────►   01_processos\<processo>\PROCESSO.md
        ├──► docs/ ───────────────────────────────────►   90_escritorio-virtual\referencia\docs\
        └──► operacao/ ───────────────────────────────►   raiz, _LEIA-ME.md, 90_…\modelos\
        ◄─────────────── 90_escritorio-virtual\manutencao\PENDENCIAS.md ◄── registro de problemas
```

## 2. Estrutura da pasta CGOV (Fase 4, 05–06/11/2026)

| Pasta | Conteúdo |
|---|---|
| `00_entrada` | Arquivos novos ainda sem destino (esvaziar toda semana) |
| `01_processos` | Uma pasta por processo SEI: `SEI_<órgão>.<número>_<ano>-<dv>_<apelido>/` com `PROCESSO.md`, `documentos-sei/`, `trabalho/`, `referencias/`, `produtos/`; índice `_INDICE.md` |
| `02_notas-tecnicas` | Série oficial de NTs e Informações assinadas, por ano; `_INDICE.md` |
| `03_normativos` | Acervo normativo único (PDF + transcrição `.md`); `revogados/`; `_INDICE.md` |
| `04_colegiados` | CTGRIC, Conselho de Governança, CIG, CTGD |
| `05_projetos` | Projetos sem processo SEI (`AAAA-MM_apelido/` + `PROJETO.md`) |
| `06_gestao-da-coordenacao` | Plano de entregas, PGD da equipe, planejamento |
| `90_escritorio-virtual` | Infraestrutura publicada pelo desenvolvimento: `referencia/`, `modelos/`, `manutencao/` (`PENDENCIAS.md`, `reorganizacao-2026-11/`), `transcricoes/` |
| `99_arquivo` | Processos encerrados, versões superadas, backups e a quarentena `_a-excluir_<data>/` |

Detalhes, decisões e evidências: plano de implantação (Fase 4) e `docs/governance/decision-log.md` §28.
Os textos de navegação (`LEIA-ME.md`, `AGENTS.md`, `_LEIA-ME.md`, modelos) têm fonte em `operacao/`.

## 3. Configuração do computador (Windows)

### 3.1 Desenvolvimento

1. Repositório clonado em `C:\Projetos\cgov-geral` (`git config core.autocrlf false`).
2. Python 3.12 ou superior (`py --version`); Git; Claude Desktop (Cowork e Code).
3. `.env` a partir de `.env.example` com `CGOV_RAIZ` (pasta CGOV). ⏳ As variáveis `CGOV_PROCESSOS`,
   `CGOV_NORMATIVOS` e `CGOV_ESCRITORIO` e as junções `local\processos`, `local\normativos` e
   `local\escritorio` chegam na Fase 5.1–5.2. **As junções antigas (`local\analyses`,
   `local\normative-sources`, `local\acervo-drive`) apontam para pastas que não existem mais.**
4. Projeto Cowork "Escritório CGOV — Implantação": pasta única `C:\Projetos\cgov-geral`; instruções no
   Apêndice A do plano de implantação. A pasta CGOV só é vinculada temporariamente, com autorização do
   Coordenador (por exemplo, na exclusão da quarentena).
5. `.claude/settings.json` (versionado): pede confirmação antes de `git commit` e `git push`, bloqueia a
   edição das áreas operacionais e oculta do modelo as skills cuja fonte está em `skills/`
   (`skillOverrides`). ⏳ Bloqueios com os nomes novos na Fase 5.6.

### 3.2 Operação

1. No Google Drive para desktop, deixar a pasta CGOV como **"Disponível offline"**.
2. Projeto Cowork **"Escritório CGOV — Operação"**: pasta única = pasta CGOV; instruções = o bloco de
   [`system-instructions/escritorio-cgov-operacao.md`](system-instructions/escritorio-cgov-operacao.md),
   colado no campo **Instruções** (não na descrição).
3. Skills instaladas em Customize → Skills a partir de `dist/skills/*.zip` (§4).

**Não vincule o repositório ao projeto Operação**: ele exporia o código-fonte das skills a edições de produção.

## 4. Publicação: do desenvolvimento para a operação

⏳ **Transição.** `scripts/publicar-operacao.sh` e `scripts/link-acervo.sh` foram escritos para o WSL e para
a estrutura antiga (`_acervo-escritorio-virtual/…`) e estão **bloqueados** desde 06/11/2026; a publicação
de skills com `--verificar` continua disponível apenas para comparar instaladas × fonte. Até a Fase 5.3
(`scripts/publicar_operacao.py`):

- **Skills:** gerar o `.zip` da skill a partir do commit e reinstalar em Customize → Skills; conferir a
  paridade instalada × fonte.
- **`operacao/`:** publicar na pasta CGOV por cópia sem sobrescrita, com a versão anterior na quarentena e
  conferência por SHA-256, como na Fase 4 (registros em `90_escritorio-virtual/manutencao/reorganizacao-2026-11/registros/`).
- **`docs/`:** a cópia em `90_escritorio-virtual/referencia/docs/` é anterior à Fase 4 e será republicada
  na Fase 5.3.
- **Instruções do projeto Operação:** se `escritorio-cgov-operacao.md` mudar, colar o novo bloco no campo
  Instruções do projeto.

Depois da Fase 5.3, a publicação será um único comando (`py scripts\publicar_operacao.py`), que recusa
publicar alterações sem commit, gera os pacotes, republica `docs/` e `operacao/` e lista as skills a
reinstalar.

## 5. Fluxo de desenvolvimento

Ciclo de uma mudança (Claude Code ou projeto Implantação, em `C:\Projetos\cgov-geral`):

1. **Origem.** Ler `90_escritorio-virtual/manutencao/PENDENCIAS.md` da pasta CGOV (colado pelo Coordenador
   ou ⏳ pela junção `local\escritorio`) e [`governance/pendencias.md`](governance/pendencias.md).
2. **Editar a fonte** em `skills/<família>/<skill>/SKILL.md`, `docs/`, `operacao/` ou `scripts/`.
3. **Validar:** frontmatter do `SKILL.md` com `name` e `description` (até 1.024 caracteres); evals
   (`evals/evals.json`), com saídas de teste em `local/pilots/`; sanitização de `docs/`, `skills/` e
   `operacao/` (⏳ `scripts/verificar_sanitizacao.py`, Fase 5.10).
4. **Registrar** a decisão em [`governance/decision-log.md`](governance/decision-log.md) (só acréscimos).
5. **Espelhar para a Antigravity**, se usada (`.agents/skills/`, ver `CONTRIBUTING.md`).
6. **Commit e push**, com confirmação do Coordenador. O shell do Cowork não tem credencial do GitHub:
   `git push` e `git ls-remote` ficam no PowerShell do Coordenador.
7. **Publicar para a operação** (§4) e reinstalar as skills alteradas.
8. **Fechar a pendência** em `PENDENCIAS.md`: "resolvida em `<commit>`".

## 6. Fluxo operacional (projeto "Escritório CGOV — Operação")

- **Antes de tudo:** o assistente lê `LEIA-ME.md` e `AGENTS.md` da raiz; para um processo, o
  `01_processos/_INDICE.md` e o `PROCESSO.md` (campos ⚠️ ainda não revisados não são fatos).
- **Nota Técnica ou parecer:** sempre `cgov-nt-01-triagem`; o estado fica em
  `01_processos/<processo>/trabalho/NT_ESTADO.md`. Processo novo: pasta e ficha a partir de
  `90_escritorio-virtual/modelos/processo/PROCESSO.md`.
- **Caminhos antigos nas skills:** até a Fase 6.3, as skills ainda citam `local/analyses/…`,
  `CGOV_Processos/…/_CGOV_NT/` e `local/normative-sources/`; a tabela "Caminhos antigos citados pelas
  skills" do `AGENTS.md` da pasta traduz para a estrutura nova. Se aparecer uma pasta `local/`,
  `analyses/` ou `_CGOV_NT/` na pasta CGOV, mova o conteúdo para o lugar certo e registre uma pendência.
- **NT assinada:** PDF em `02_notas-tecnicas/<ano>/` (`NT_<nº>-<ano>_SEI_<nº documento>_<tema>.pdf`) e
  registro no `PROCESSO.md`.
- **Índices:** os `_INDICE.md` são gerados por `scripts/gerar_indices.py` no desenvolvimento; a operação
  registra "regenerar índices" em `PENDENCIAS.md`.
- **Normas:** `03_normativos/`; para transcrever um PDF novo, `cgov-transcrever-normativos`.
- **Problema ou melhoria:** não corrigir a skill na operação; registrar em
  `90_escritorio-virtual/manutencao/PENDENCIAS.md` (sem dados pessoais).

## 7. Regras de segurança

| Regra | Por quê |
|---|---|
| Dados de processos só no Drive (`01_processos/`) | Rascunhos e informação interna; o repositório, embora privado, é mantido sanitizado |
| Nada se apaga direto: quarentena `99_arquivo/_a-excluir_<data>/`, revista após 30 dias | ADR-014; permite recuperar |
| Movimentação em lote só por mapa aprovado, conferida por SHA-256 e com registro | Rastreabilidade e reversão |
| Nada de `local/`, `.env` ou `dist/` no Git | Ignorados pelo `.gitignore` |
| Commit e push sempre com confirmação | `.claude/settings.json` e regra do projeto Implantação |
| A referência e a navegação publicadas no Drive não se editam à mão | São substituídas a cada publicação |
| Skill instalada só a partir do commit publicado | Produção = commit publicado |

## 8. Pendências

Lista consolidada e atualizada em [`governance/pendencias.md`](governance/pendencias.md).

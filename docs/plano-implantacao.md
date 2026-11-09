---
tipo: plano
status: vigente
versao: "3.51"
atualizado_em: 2026-11-09
relacionados: [docs/plano-indice.md, docs/governance/decision-log.md, docs/governance/rastreabilidade.md, docs/adr/README.md, docs/governance/pendencias.md]
---

# Plano de Implantação — Escritório Virtual da CGOV/ICMBio

> **Versão:** 3.51 — 09/11/2026 (**etapa 7.1 gravada**: 32 skills movidas por `git mv` para `plugins\cgov-escritorio\skills\` (70 renomeações), `plugin.json` 0.1.0 e README do plugin; caminhos dos documentos corrigidos; catálogo regerado; `verificar_docs.py` passa a varrer `plugins/` (110 `.md`, 0 erros); decision-log §46; sem *commit* ainda). Versão 3.50 — 09/11/2026 (**Fase 7 iniciada: ADR-005 aceito como está, D58**; pendência E12 resolvida; decision-log §45; *commit* `d88a13b`). Versão 3.49 — 09/11/2026 (**revisão documental antes da Fase 7, etapa 7.0, D57**: índices, rastreabilidade, convenções, frontmatter e verificadores; ADR-001, 009 e 011 aceitos; sem *commit* ainda). Versão 3.48 — 08/11/2026 (**Fase 6 ✅ concluída em 08/11/2026**: 6.8a no *commit* `b863ef3`; 34 skills reinstaladas e conferidas na conta; 8 nomes antigos do PGD excluídos; instruções v1.1 no projeto Operação; 6.8b no *commit* `066068b`, publicada; `--verificar` sem divergências (skills 34/34, `operacao/` 14/14, `docs/` 33/33); próxima: **Fase 7** (plugin `cgov-escritorio`); antes, na v3.47: **evals da 6.8 concluídos** — 129 de 134 expectativas (96%) nas 9 skills alteradas; correções aplicadas; D55 (rascunho condicionado na `cgov-nt-06`) e D56 (exceções ao futuro do presente); **6.8a gravada** (sem *commit*); próximos: *commit*, publicação e reinstalação das 34 skills; antes, na v3.46: *commit* `0d85240` da v3.44 enviado e publicado (35/35 conferidos); pendência **S1 resolvida** (script da pasta de prompts limpo pelo Coordenador); **6.7 concluída** (OCR do Windows aprovado: 96,1% e 98,3% de cobertura nos dois PDFs sem camada de texto; erro típico nos ordinais, tratado na skill); **6.8 preparada** (preparos `6.8a` e `6.8b`); **D54 respondida**: evals das 9 skills alteradas que têm casos, rodados pelo Claude com subagentes; evals das 13 sem casos na pendência E9; antes, na v3.44: **6.10 concluída** — `cgov-secretaria-colegiados`, `cgov-integridade`, `cgov-carta-servicos` e `cgov-projetos-cooperacao` em `skills/thematic/`, com normas conferidas no acervo, 3 evals cada e o script `classificar_entregas.py` sem conexão a banco; Carta de Serviços enquadrada no inciso VI (D53); próximas: 6.7 e 6.8; antes, na v3.43: **E8 resolvida** — Portarias ICMBio nº 271/2013 e nº 129/2020 e Portaria PFE/ICMBio nº 3/2021 lidas no acervo; espécies e vigência pela nº 129/2020 nas skills e nas instruções (D52); próxima: 6.10; antes, na v3.42: **6.4 concluída** e skill da **6.6** criada — `cgov-gestao-acervo` e `cgov-triagem-processo-sei` em `skills/escritorio/`, `publicar_operacao.py` v0.2.0 publica o gerador de índices em `90_escritorio-virtual/ferramentas/` (D51); próxima: 6.10; antes, na v3.41: **6.9(b)–(d) concluídas** — roteiro da `cgov-nt-01` com os cinco subsídios obrigatórios, 8 divergências da Parte B.4 corrigidas, `cgov-nt-06` (consulta facultativa) e `cgov-modelar-fluxo` (BPMN → POP) ampliadas, procedimento v2 em `docs/procedimentos/` e modelo em `operacao/` (D50); próxima: 6.4 + `cgov-triagem-processo-sei`; antes, na v3.40: **6.5 concluída** — 8 descrições encurtadas (todas as 28 ≤ 950 caracteres), `cgov-gestao-riscos` rebaseada sobre a versão da conta e saneada (D43), eval de gatilho da `cgov-nt-01` incorporado do *branch* antigo, com rótulos corrigidos (D49); próxima: 6.9(b)–(d); antes, na v3.39: **6.3 concluída** — 13 skills com caminhos neutros (busca por `local/analyses` e `_acervo-escritorio-virtual` = 0), mapeamento por papel nos dois `AGENTS.md`, `gerar_indices.py` v0.1.1, ADR-006 aceito (D48); próxima: 6.5; antes, na v3.38: as 8 skills de `skills/pgd/` passam a usar o prefixo `pgd-` (D47); antes, na v3.37: **6.2 concluída** — 12 skills promovidas a `skills/pgd/` e `skills/normativo/` e as 2 `cgge-fgbio-*` versionadas em `skills/cgge-fgbio/` (fora do plugin), saneadas, com `skillOverrides` (D46); próxima: 6.3; antes, na v3.36: análise da pasta de prompts `%USERPROFILE%\My Drive\_projetos\02_dev-prompts\` e **nova etapa 6.10** (D45: skills `cgov-secretaria-colegiados`, `cgov-integridade`, `cgov-carta-servicos` e `cgov-projetos-cooperacao`; ampliação da `cgov-nt-06` e da `cgov-modelar-fluxo`); antes, na v3.35: **bloco de decisões concluído** — 6.6 (D4: nova skill `cgov-triagem-processo-sei`, mantendo o `.md` autocontido) e 6.9(a) (D44: as 6 questões da Parte B.5); próxima: 6.2; antes, na v3.33: ordem das etapas aprovada (D42) e **6.1 concluída** — 28 skills da conta exportadas para `local/installed-reference/_export_2026-11-07/` (39/39 arquivos conferidos por SHA-256 contra a cópia sincronizada da máquina do Coordenador), comparação com fontes e referência em `COMPARACAO.md` e divergências decididas (D43) —; próxima: bloco de decisões 6.6 + 6.9(a). Histórico completo das versões v1–v3.51: **Apêndice G**.) A v3 incorpora o **rearranjo dos dois repositórios**: o de desenvolvimento (`C:\Projetos\cgov-geral`) e o operacional (`%USERPROFILE%\My Drive\10_Institucional\CGOV`).
> **Responsável:** Coordenador de Governança (CGOV/CGGE/ICMBio)
> **Repositório de desenvolvimento:** `C:\Projetos\cgov-geral` ⇄ GitHub `lpchagas/cgov-geral` (**privado**, confirmado em 05/11), `main` = `e305404` (*merge* da Fase 5, D41), conferido em 07/11 (`main...origin/main` sem diferença); o *branch* `implantacao/fase-5` (`ee3b239`) fica só na máquina do Coordenador
> **Repositório operacional:** `%USERPROFILE%\My Drive\10_Institucional\CGOV` (Google Drive)
> **Projetos Cowork:** "Escritório CGOV — Implantação" (desenvolvimento) e "Escritório CGOV — Operação" (trabalho da Coordenação)
> **Ferramentas-alvo:** Claude Desktop (Cowork e Code), Google Antigravity, Obsidian, Maestri
> **Método:** análise documental (`engineering:documentation`) e arquitetural com ADRs (`engineering:architecture`)
> **Regra de execução:** uma fase por vez, com confirmação explícita do Coordenador antes de mover, renomear, excluir, reinstalar, fazer *commit* ou *push*.
> **Regra de manutenção:** a cada etapa concluída, este plano é **atualizado integralmente**, conforme a lista de verificação da Seção "Regra de manutenção deste plano" (logo abaixo do sumário).
> **Situação atual:** **Fase 7 🟨 em andamento** (7.0 ✅ em 09/11/2026, *commit* `ebb6f1d`; **ADR-005 aceito em 09/11/2026, D58**, *commit* `d88a13b`; **7.1 ✅ gravada em 09/11/2026, aguardando *commit***; próximas: 7.2 e 7.3 — `publicar_operacao.py` não enxerga as 32 skills até a 7.3); Fases 1, 2, 3, 4 e 5 ✅ (Fase 4 concluída em 06/11; Fase 5 em 07/11: scripts em Python, junções e bloqueios novos, ADRs e catálogo em `docs/`, publicação com `publicar_operacao.py`, *merge* `e305404`) · **Fase 6 ✅** (portfólio de skills, concluída em 08/11): 6.1 ✅ (07/11, D42–D43); 6.6 ✅ decidida (D4); 6.9(a) ✅ decidida (D44); nova etapa 6.10 (D45); 6.2 ✅ (D46); prefixo `pgd-` (D47); 6.3 ✅ (D48); 6.5 ✅ (D49); 6.9(b)–(d) ✅ (D50); 6.4 ✅ (D51); E8 ✅ (D52); 6.10 ✅ (D53); 6.7 ✅ (OCR aprovado); 6.8 ✅: evals 129/134 (D54), 6.8a (`b863ef3`), reinstalação, 6.8b (`066068b`), `--verificar` sem divergências · quarentenas a revisar: `_a-excluir_2026-11-05` (4.11, lembrete em 05/12/2026) e `_a-excluir_2026-11-07` (publicação, a partir de 07/12/2026) · novo objetivo D34 na etapa 6.9 · Fase 0 parcial (D5–D8; ADR-008 e ADR-010 ainda propostos).

---

## Sumário executivo

O Escritório Virtual tem **dois repositórios com papéis distintos**, e a v3 trata os dois como produtos:

| | Repositório de **desenvolvimento** | Repositório **operacional** |
|---|---|---|
| Onde | `C:\Projetos\cgov-geral` (Git ⇄ GitHub privado) | `My Drive\10_Institucional\CGOV` (Google Drive) |
| Para quê | Criar e manter skills, agentes, instruções, documentação e scripts | Produzir o trabalho da CGOV: NTs, análises de processos SEI, normativos, projetos, colegiados |
| Quem usa | Coordenador-mantenedor + projeto Cowork **Implantação** + Claude Code, Antigravity, Obsidian | Coordenador e servidores + projeto Cowork **Operação** |
| Estado em 07/11 | Consolidado no Windows (Fase 1 ✅) e **atualizado para a estrutura nova (Fase 5 ✅)**: scripts em Python, junções `local\processos`, `local\normativos` e `local\escritorio`, bloqueios de edição, 14 ADRs, catálogo de skills; `main` = `e305404` | **Reorganizada (Fase 4 ✅)**: 9 áreas numeradas (`00`–`06`, `90`, `99`), `LEIA-ME.md` e `AGENTS.md` na raiz; 74 processos com ficha `PROCESSO.md`; acervo normativo único (109 arquivos); quarentena com 587 itens até 05/12/2026; mapa, manifestos e registros em `90_escritorio-virtual\manutencao\reorganizacao-2026-11\` |

**O que a v3 acrescenta:**

1. **Novo arranjo da pasta CGOV** (Seção 5.2): 7 áreas numeradas, mais a infraestrutura (`90_`) e o arquivo (`99_`). Cada processo SEI ganha **uma única pasta**, com subpastas padronizadas e uma ficha `PROCESSO.md`. O acervo normativo passa a ser um só.
2. **Documentação navegável em Markdown** (Seção 5.3): `LEIA-ME.md` e `AGENTS.md` na raiz, `_LEIA-ME.md` e `_INDICE.md` em cada área e `PROCESSO.md` por processo, com metadados em frontmatter que pessoas, agentes de IA e o Obsidian conseguem ler e consultar.
3. **Limpeza controlada** (Seção 5.5): lista de itens desnecessários. Nada é apagado direto: tudo passa por `99_arquivo/_a-excluir_<data>/` e pela sua confirmação.
4. **Dois projetos Cowork novos**: o antigo projeto `cgov-geral-v1` é preservado (as instruções são copiadas) e depois arquivado. Os projetos Cowork por processo passam a ser revistos (ADR-013).
5. **Fases reordenadas** (Seção 6): o desenho dos repositórios (Fase 2) e a reorganização da pasta CGOV (Fase 4) vêm **antes** de atualizar scripts, skills e plugin, que passam a apontar para a estrutura nova.

---

## Regra de manutenção deste plano

Este arquivo é a **fonte de verdade do andamento** da implantação. Uma atualização parcial (por exemplo, marcar só o quadro da Seção 11) deixa o plano contraditório. Por isso, **ao concluir cada etapa ou ao receber cada decisão do Coordenador**, o Claude atualiza o plano **integralmente** e confere **todos** os pontos abaixo antes de declarar a etapa concluída:

| # | Ponto de atualização | O que conferir |
|---|---|---|
| 1 | Cabeçalho | Versão (`3.x`), data, linha **Situação atual** (fases concluídas e próxima fase) |
| 2 | Sumário executivo | Se o estado de algum repositório ou a lógica do plano mudou |
| 3 | Seção 1 (evidências e limitações) | Novas evidências; limitações resolvidas ou novas |
| 4 | Seção 4 (ADRs) | Status de cada ADR (Proposto → Aceito/Rejeitado) |
| 5 | Seção 5 (arquitetura, mapa 5.5, itens 5.6) | Destinos alterados por decisões; remover marcas "a decidir" e ⚠️ já resolvidas |
| 6 | Seção 6.1 (visão geral) | Coluna **Situação** da fase |
| 7 | Seção da fase em execução | Título com o status (`— ✅ concluída (data)` ou `— 🟨 em andamento`), coluna de situação das etapas e um parágrafo **Resultado** com as evidências (commits, hashes, contagens) |
| 8 | Seção 7 (riscos) | Riscos descartados, materializados ou novos |
| 9 | Seção 9 (decisões) | Situação de cada decisão e data |
| 10 | Seção 11 (quadro de acompanhamento) | Status, data e evidência da fase |
| 11 | Apêndices A e B | Se as instruções dos projetos Cowork precisarem mudar, avisar o Coordenador para colar a nova versão |
| 12 | Apêndice G (evolução) e linha final | Registrar a versão nova e o próximo passo |
| 13 | Coerência | Buscar no arquivo por "Proposto", "a decidir", "Pendente" e "⚠️" e confirmar que cada ocorrência ainda é verdadeira |
| 14 | Versionamento | Depois da etapa 3.A.0, fazer *commit* da atualização (`docs(plano): …`) com a confirmação do Coordenador |
| 15 | Índices e verificação | Rodar `py scripts\gerar_indices_docs.py` e `py scripts\verificar_docs.py` (0 erros) antes do *commit*; ver [`convencoes-documentacao.md`](convencoes-documentacao.md) |

A mesma regra está nas instruções do projeto "Escritório CGOV — Implantação" (Apêndice A, regra 8).

---

## 1. Escopo, fontes e limitações

### 1.1. Evidências examinadas

| Fonte | Situação verificada |
|---|---|
| GitHub `lpchagas/cgov-geral` (**privado**, confirmado pelo Coordenador em 05/11) | `main` = `f89121c` (06/11, plano v3.23 + decision-log §28), conferido por `git ls-remote` no PowerShell do Coordenador; `306ade5` (v3.22), `54ae16b` (v3.21; completa a v3.20), `d9c582e` (só o arquivamento do `escritorio-cgov.md`), `377c34c`, `c88bd3e`, `3dae008`, `224dc2c`, `657cb69`, `55172da`, `b9a33a3`, `cba655d`, `98789ef`, `13ea143`, `46fb7ff` e `b981d66` também foram conferidos por `git ls-remote` no PowerShell do Coordenador. Histórico de 05–06/11: `f89121c` (v3.23), `306ade5` (v3.22), `54ae16b` (v3.21), `d9c582e` (arquivamento), `377c34c` (v3.19), `c88bd3e` (v3.18), `3dae008` (v3.17), `224dc2c` (v3.16), `657cb69` (v3.15), `55172da` (v3.14), `b9a33a3` (v3.13), `cba655d` (v3.12), `98789ef` (v3.11), `13ea143` (v3.10), `46fb7ff` (v3.9), `b981d66` (v3.8), `7f5a324` (v3.7 + `scripts/reorganizar_cgov.py`), `88a5612` (v3.6), `be2f493` (v3.5), `8787e0a` (v3.1), `de0fa54` (v3.3), `6890b63` (`CLAUDE.md` + plano v3.4) e `320007d` (`README.md`, `AGENTS.md`, `docs/fluxos-de-trabalho.md`, D19; mesma mensagem de *commit* do anterior); antes, `8787e0a` (plano v3.1, etapa 3.A.0) e `67957fe` (04/11). *Branch* antigo `claude/cgov-nt-triagem-description-loop-6x6dsc` (`f3628f1`) não incorporado |
| `C:\Projetos\cgov-geral` | Clone limpo; `local\` com ativos resgatados do WSL (63 arquivos conferidos por SHA-256); junções para o Drive; `.env` do Windows; cofre Obsidian aberto (`C:\Projetos\cgov-geral\.obsidian\` ignorado pelo Git desde a v3.3) |
| Projeto Cowork "Escritório CGOV — Implantação" (sessão de 05/11) | Criado no Claude Desktop; instruções = Apêndice A; acesso confirmado às duas pastas: 1ª `C:\Projetos\cgov-geral` e 2ª (temporária) `%USERPROFILE%\My Drive\10_Institucional\CGOV`. A sessão leu o plano e aguardou confirmação (teste 3.A.6 aceito pelo Coordenador). Capturas de tela de 05/11: a tela do projeto no Claude Desktop mostra **Instruções**, **Contexto** (2 pastas vinculadas), **Memória** e **Programado**, sem campo de links. O texto do Apêndice A tinha ido para a **descrição**; corrigido pelo Coordenador em 05/11 (as sessões agora recebem a descrição curta de 3.A.2 e as instruções v3.4) |
| Projeto Cowork `cgov-geral-v1` (capturas de 05/11) | 4 pastas vinculadas: `cgov-geral-v1` (`C:\_cowork\cgov-geral-v1`, segundo as instruções), `pgd-agente-icmbio`, `pgd-ocde-icmbio` e `cgge-fgbio-2026`; instruções preservadas em `C:\Projetos\cgov-geral\local\archive\cowork-projetos\cgov-geral-v1_instrucoes_2026-11-05.md` (SHA-256 `ad862755…`) |
| Cópia do WSL `~/projetos/cgov-geral-v1` | Redundante desde 04/11: *commit* enviado, `.github/` arquivado, `local/` resgatado e conferido (490/490) |
| Exportação das skills da conta (Fase 6.1, 07/11) | Retrato da conta recebido pela sessão do Cowork em 07/11/2026 10:33: 28 skills CGOV/CGGE (26 do inventário + `cgge-fgbio-apresentacao` e `cgge-fgbio-plano-aula`), 39 arquivos, gravados em `C:\Projetos\cgov-geral\local\installed-reference\_export_2026-11-07\` com `MANIFESTO.md` (SHA-256); conferência cruzada no PowerShell do Coordenador contra `%USERPROFILE%\.claude\skills\synced\`: **39/39 iguais**; `COMPARACAO.md` e `diffs\` (12 skills divergentes) na mesma pasta; `--verificar` no HEAD `44310f2`: as mesmas 9 desatualizadas |
| Pasta de prompts `%USERPROFILE%\My Drive\_projetos\02_dev-prompts\` (07/11, somente leitura, acesso temporário concedido pelo Coordenador) | 1.362 arquivos, dos quais ~870 são o pacote do Design System gov.br (`ds-gov.br\`, fora da análise). Analisados: instruções de sistema e primeiros pedidos dos 120 prompts do Google AI Studio, os 10 arquivos de `_prompts\_Prompts novos\`, os `.txt`/`.md` da raiz e a `_temp\`. `backup-skills-cowork-2026-07-23.zip` = cópia antiga das mesmas 24 skills da conta. A pasta tem anexos de processos SEI e documentos pessoais: serve só de insumo, nada vai para o repositório sem saneamento (D45) |
| Pasta CGOV no Drive | Inventário em 05/11 (somente leitura; nomes, contagens, tamanhos e hashes; conteúdo dos documentos **não lido**). Detalhe na Seção 3.4. Recontagem na 4.1: **2.831 arquivos**, todos com SHA-256; pasta não alterada |
| Mapa de reorganização (4.1–4.2; revisto na 4.4a, 05/11) | Vigente: `C:\Projetos\cgov-geral\local\MAPA_REORGANIZACAO_2026-11.csv` (2.860 linhas; 2.833 arquivos; SHA-256 `83db96e21d6146d2…`). Versões anteriores em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\`: `MAPA_REORGANIZACAO_2026-11_aprovado-4.2.csv` (`5e686e82…`) e `MAPA_REORGANIZACAO_2026-11_D26-2831arq.csv` (`116bf907…`). Resumo `C:\Projetos\cgov-geral\local\MAPA_REORGANIZACAO_2026-11_resumo.md`, decisões `C:\Projetos\cgov-geral\local\reorganizacao\decisoes.csv` (28), apelidos `C:\Projetos\cgov-geral\local\reorganizacao\apelidos.csv` (11) e cache de SHA-256 `C:\Projetos\cgov-geral\local\reorganizacao\cache_sha256.csv`. Para propor apelidos, foi lida só a abertura de 16 PDFs de processo |
| Manifesto anterior e simulação (4.3–4.4, 05/11) | Novo `--planejar` em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\MAPA_conferencia_2026-11-05.csv`: **idêntico byte a byte** ao mapa aprovado (SHA-256 `5e686e821d30744a…`). Manifesto vigente `C:\Projetos\cgov-geral\local\reorganizacao\manifesto_pre_2026-11.sha256` (2.833 linhas; SHA-256 `8847c5e87a0d5f69…`; refeito na 4.4a), com hashes recalculados do disco (3,53 GB): 2.833/2.833 iguais ao mapa vigente. O manifesto da 4.3 (2.831 linhas, `8a6470cd…`) foi guardado como `conferencia\manifesto_pre_2026-11_2831arq.sha256`: nenhum dos 2.831 hashes mudou. Simulação final: 2.860 operações, zero conflitos e zero avisos de caminho longo. Registros em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\` |
| Lista de projetos Cowork (captura de tela, 05/11) | 16 projetos, entre eles `cgov-geral-v1` (22/09), `02070.006604 2026-17_Política de Governança_v2`, `02070.007589/2025-35_TCs`, `Sistema Integridade ICMBio`, `pgd-icmbio`, `Painel Estratégico OCDE/ICMBio`, `CGGE_Estrutura` |

### 1.2. Limitações

- ~~Configurações dos projetos Cowork não vistas~~ — **resolvido (05/11, 3.C):** o Coordenador informou que, depois da formatação do computador, as pastas vinculadas aos projetos antigos não existem mais; apontavam, em geral, para projetos de desenvolvimento cujos backups estão em `%USERPROFILE%\My Drive\_projetos`, e nenhum aponta para a pasta CGOV atual. Inventário simplificado em `C:\Projetos\cgov-geral\local\archive\cowork-projetos\inventario.md` (D21).
- ~~Compartilhamento da pasta CGOV não verificado~~ — **resolvido (D12, 05/11):** a pasta é de uso exclusivo do Coordenador de Governança.
- ~~Casos não cobertos pelas regras da Seção 5.5~~ — **resolvido (05/11, 4.2):** os 28 `a-decidir` do mapa foram decididos (D22–D24). Continua dependendo do Coordenador a classificação de cada processo em "ativo" ou "encerrado", que entra no frontmatter do `PROCESSO.md` (etapa 4.7).
- As informações sobre o Maestri vêm de catálogos de terceiros (somente macOS); confirmar em `themaestri.app`.
- **O shell do Cowork (máquina virtual Linux) não tem credencial do GitHub:** `git ls-remote`, `git fetch` e `git push` falham ali. Verificações remotas, *commit* e *push* são feitos pelo PowerShell do Coordenador (`C:\Projetos\cgov-geral`), com scripts completos fornecidos pelo Claude (D17, D18).
- ~~Visibilidade do repositório divergente~~ — **resolvido (05/11):** o Coordenador confirmou que o repositório é **privado**; corrigidas as menções a "público" em `C:\Projetos\cgov-geral\CLAUDE.md`, `C:\Projetos\cgov-geral\README.md`, `C:\Projetos\cgov-geral\AGENTS.md` e `C:\Projetos\cgov-geral\docs\fluxos-de-trabalho.md` (D19). As demais desatualizações de `docs\fluxos-de-trabalho.md` (WSL, `~/projetos/cgov-geral-v1`) seguem para a Fase 5.
- O Claude Desktop (05/11) **não tem campo de links** no projeto Cowork; a etapa 3.A.5 foi substituída pela menção ao repositório nas instruções (Apêndice A, "Fontes de verdade").

---

## 2. Análise documental (skill `engineering:documentation`)

> Legenda de avaliação: 🔴 crítico · 🟠 alto · 🟡 moderado · 🟢 bom.

### 2.1. Repositório de desenvolvimento (estado de `67957fe`)

| Tipo | Documento | Avaliação | Observação |
|---|---|---|---|
| README | `README.md` | 🟠 | Diz "repositório público"; não tem *quick start* nem mapa |
| Arquitetura e fluxos | `architecture.md`, `CLAUDE.md`, `fluxos-de-trabalho.md` | 🟢 conteúdo / 🟡 atualidade | `fluxos-de-trabalho.md` é o melhor documento, mas descreve WSL, `_acervo-escritorio-virtual/analyses` e repositório público |
| Registro de decisões | `decision-log.md` (27 seções) | 🟢 rico / 🔴 consulta | Pendências no meio (§25); falta registrar a convenção de 07/10 (Seção 3.4) |
| Instruções de operação | `escritorio-cgov.md` | 🟠 | Mapa de tradução de caminhos e inciso V "sem skill" (a `cgov-qcf` existe); será reescrito para a estrutura nova |
| Instruções sobrepostas | `analista-processos-sei.md` (60,9 mil caracteres) | 🔴 | Pendência 20 sem decisão |
| *Onboarding* e catálogo de skills | — | 🔴 Ausentes | — |

### 2.2. Repositório operacional (pasta CGOV)

| Leitor | Necessidade | Situação atual |
|---|---|---|
| Servidor da CGOV | "Onde está o processo X?", "Onde salvo isto?", "Qual a última NT sobre Y?" | **Nenhum documento de orientação** na pasta. Nomes mistos (`CGOV_Processos`, `normative-sources`, `_acervo-escritorio-virtual`, `organizar`). Processos com três padrões de nome (40 com `SEI_`, 30 só com o número, 1 sem número; 44 com espaços) |
| Agente de IA (Cowork) | Saber onde ler e onde gravar sem adivinhar | Depende de um mapa de tradução nas instruções (`local/analyses` → `_acervo…/analyses`), e esse mapa foi superado em 07/10 por uma convenção nova, registrada apenas em arquivos `MOVIDO_PARA.txt` |
| Obsidian / buscas | Metadados consultáveis | Nenhum frontmatter, índice ou ficha |

**Conclusão:** a pasta operacional precisa de uma **camada de navegação** (LEIA-ME, índices e fichas) e de **uma convenção única de nomes**, e não só de pastas novas.

---

## 3. Análise arquitetural (skill `engineering:architecture`)

### 3.1. Requisitos e restrições

| Tipo | Requisito |
|---|---|
| Funcional | Apoiar as 10 atribuições do parágrafo único do Art. 37 (Portaria ICMBio nº 5.592/2025); encontrar qualquer processo, NT ou norma em até dois cliques ou numa consulta à IA |
| Não funcional | **Uma pasta por processo**; **um acervo normativo**; **um lugar** para cada tipo de documento; produção = *commit* publicado |
| Não funcional | **Sigilo e LGPD**: processos SEI só no Drive, nunca no Git nem no plugin; nenhuma exclusão sem passar pelo arquivo e sem confirmação |
| Não funcional | Legível por analista de negócios **e** por agentes de IA: nomes estáveis, sem espaços nem acentos nas pastas de máquina, Markdown com frontmatter |
| Restrição | Windows; Cowork monta pastas locais; projetos Cowork não são compartilháveis; o Drive sincroniza movimentações para a nuvem (e para quem tiver acesso compartilhado) |
| Restrição | Limites da Anthropic: `description` ≤ 1.024 caracteres; `name` ≤ 64; `SKILL.md` idealmente < 500 linhas |

### 3.2. Arquitetura vigente (síntese)

O desenvolvimento acontece no repositório (agora no Windows) e publica para a operação por `publicar-operacao.sh`: zips das skills e cópia de `docs/` em `_acervo-escritorio-virtual/_referencia`. A operação devolve problemas por `_acervo-escritorio-virtual/manutencao/PENDENCIAS.md`. Esse desenho, da Decisão 27, **é mantido** (ADR-001). O que muda é a organização interna da pasta operacional.

### 3.3. Achados — desenvolvimento

> Mesma escala de avaliação da Seção 2 (🔴🟠🟡🟢).

| # | Achado | Impacto |
|---|---|---|
| A1 | Scripts *bash* dependentes do WSL (`ln -s`, `rsync`, caminhos `/mnt/c`) | 🔴 A publicação não roda no Windows |
| A2 | Documentação desatualizada: "público", nome `cgov-geral-v1`, WSL | 🟠 Instruções contraditórias para pessoas e IA |
| A3 | 12 skills em uso sem fonte versionada (resgatadas em `local/installed-reference`) | 🟠 Correção só por reinstalação manual |
| A4 | Três skills instaladas desatualizadas desde 06/10 | 🟠 A operação usa versões com caminhos antigos |
| A5 | Skills citam caminhos literais (`local/analyses/`) | 🟠 Ficam obsoletos com a estrutura nova (ADR-006) |
| A6 | Distribuição em 14 zips com reinstalação individual; espelho `.agents/skills` copiado à mão | 🟡 Deriva |
| A7 | Nenhuma camada de agentes nem de painéis | 🟡 Escopo incompleto |
| A8 | Maestri sem versão Windows (segundo terceiros) | 🟡 |

### 3.4. Achados — pasta operacional CGOV (inventário de 05/11/2026)

| Área atual | Arquivos | Tamanho | Achado |
|---|---|---|---|
| `CGOV_Processos\` | 1.066 | 2,5 GB | 71 pastas com três padrões de nome. Subpastas improvisadas (`_CGOV_NT`, `_referencias`, `_Referências indicadores`, `consulta`, `normativas`, `_Audios`, `Claude outputs`…). Duas pastas para o mesmo processo (`02070.006604 2026-17_Política de Governança` e `…_v2`). Uma pasta **vazia e duplicada** (`SEI_02070 (1).009510_2025_19_AUDIT`). A pasta `SEI_02070.003032_2023-63_Priorização Planos Manejo` concentra 534 arquivos (shapefiles de referência) |
| `_acervo-escritorio-virtual\analyses\` | 1.007 | 517 MB | **Segunda árvore de processos**, com outra convenção de nomes (`02070.001696_2026-31_RADAR` × `SEI_02070.001696_2026_31_Gestao_Riscos`). Quatro pastas contêm só `MOVIDO_PARA.txt`: em **07/10/2026** a operação adotou "NT_ESTADO.md e produtos da NT vivem na pasta do processo" (`CGOV_Processos/<proc>/_CGOV_NT/`), decisão que **não está no repositório**. Também contém `normative-transcription` (928 arquivos, 302 MB, 487 PNG regeneráveis), `_doutorado` (material pessoal), `revisao-prompts-legados` (artefato de desenvolvimento) e `_teste_mv.tmp` (vazio) |
| `normative-sources\` | 110 | 70 MB | Acervo normativo principal (52 PDF + 58 transcrições `.md`) |
| `CGOV_Normativas\` | 17 | 16 MB | **Segundo acervo normativo**: 11 PDFs idênticos aos de `normative-sources` e 6 exclusivos (por exemplo, Portaria nº 1.258/2022) |
| `CGOV_Notas Técnicas\` | 20 | 9 MB | Série de NTs/NIs assinadas (PDF) de 2025–2026 |
| `CGOV_Administrativo\` | 16 | 127 MB | Mistura quatro processos SEI com um tema (Fundo Rio Doce); uma cópia `(1)` idêntica |
| `CGOV_Projetos\` | 18 | 72 MB | Oficinas, eventos e parcerias; versões sucessivas de apresentações |
| `organizar\` | 3 | 0,6 MB | Três versões do Plano de Entregas CGGE (v4, v4.1, v4.2) |
| Raiz | 3 | 5 MB | Transcrição de reunião do CTGRIC (`.docx` + atalho `.gdoc`); `cgov_projetos_trimestre.html` |
| `_acervo…\_tmp\` | 62 | 14 MB | Imagens temporárias de revisão |
| `_acervo…\archive\` | 490 | 13 MB | Inclui `dev-local_2026-11` (cópia de segurança de 04/11) |
| **Total** | **2.827** | **3,3 GB** | **433 grupos de arquivos idênticos (85,5 MB)**, a maioria entre `analyses` e o backup de 04/11, e entre os dois acervos normativos |

---

## 4. Registros de decisão de arquitetura (ADRs)

> Status: **Aceito** (já executado ou aprovado) ou **Proposto** (aprovação pendente na Fase 0; não bloqueia as Fases 3–5). Os 14 ADRs estão em [`docs/adr/`](adr/README.md) desde 07/11/2026 (D40), cada um com o seu status; uma aprovação na Fase 0 muda só o status e a data no arquivo e nesta tabela.

| ADR | Decisão | Status |
|---|---|---|
| 001 | Preservar a separação desenvolvimento × operação (Decisão 27), o canal `PENDENCIAS.md` e a regra "produção = *commit* publicado" | **Aceito (09/11, D57)** |
| 002 | Desenvolvimento em `C:\Projetos\cgov-geral` (Windows); WSL aposentado | **Aceito** (Fase 1) |
| 003 | Dois projetos Cowork: **Implantação** (pasta do repositório; acesso temporário à pasta CGOV durante a Fase 4) e **Operação** (pasta CGOV; nunca edita o repositório) | **Aceito** (D2, 05/11) |
| 004 | Scripts multiplataforma em Python (`link_acervo.py`, `publicar_operacao.py`, `gerar_indices.py`, `reorganizar_cgov.py`) | **Aceito (07/11, D40)** — os cinco scripts em Python existem |
| 005 | Distribuição como plugin único `cgov-escritorio` (upload de zip; marketplace GitHub só depois de testado e com sincronização automática desligada) | **Aceito (09/11, D58)** |
| 006 | Skills neutras quanto a caminho: citam **papéis** ("pasta do processo", "acervo normativo"); os caminhos concretos ficam no `AGENTS.md` de cada repositório | ✅ Aceito (07/11/2026, D48; aplicado na 6.3) |
| 007 | Separação de dados: Git só com fonte e documentação sanitizada; processos, normativos e produtos só no Drive | **Aceito (07/11, D40)** — `.gitignore`, `verificar_sanitizacao.py` e bloqueios (D39) |
| 008 | Agentes definidos uma vez no plugin; execução no Cowork e no Claude Code; Maestri opcional | Proposto |
| 009 | Obsidian: cofre de desenvolvimento = repositório; cofre de operação = pasta CGOV (opcional, Fase 8) | **Aceito (09/11, D57)** |
| 010 | Painéis Power BI em PBIP versionado sem dados; MCP de autoria só no desenvolvimento; Fabric IQ só com autorização da TI | Proposto |
| 011 | Qualidade: evals com `skill-creator`, paridade fonte × instalado, verificação de sanitização | **Aceito (09/11, D57)** |
| **012** | **Estrutura do repositório operacional** (Seções 5.2 e 5.3) | **Aceito (05/11)** |
| **013** | **Projetos Cowork por processo passam a ser exceção** | **Aceito (05/11)** |
| **014** | **Exclusão controlada** | **Aceito (05/11)** |

### ADR-012 — Estrutura do repositório operacional

**Contexto.** A pasta CGOV cresceu por acúmulo: duas árvores de processos, dois acervos normativos, três padrões de nome e nenhuma orientação escrita. Em 07/10 a operação já começou a unificar o trabalho da NT na pasta do processo (`_CGOV_NT`), sem registro no repositório.

| Dimensão | A. Manter e só documentar | B. Reorganização completa por **tipo de objeto** (proposta) | C. Reorganização por **inciso do Art. 37** |
|---|---|---|---|
| Encontrar um processo | Duas árvores | Uma pasta por processo, com índice | Processo pode caber em mais de um inciso |
| Esforço | Baixo | Médio (mapa CSV + script + lotes) | Alto |
| Estabilidade dos caminhos | Ruim | **Boa**: o tipo de objeto não muda | Ruim: o enquadramento pode mudar |
| Leitura por IA | Exige mapa de tradução | Convenção única no `AGENTS.md` | Exige classificação prévia |

**Decisão aceita.** **B**. O inciso do Art. 37 entra como **metadado** (`inciso_art37` no `PROCESSO.md`) e **coluna do índice**, e não como pasta. Assim é possível filtrar por inciso sem duplicar arquivos.

### ADR-013 — Projetos Cowork por processo passam a ser exceção

**Contexto.** Há projetos Cowork dedicados a processos (por exemplo, `02070.006604 2026-17_Política de Governança_v2`, `02070.007589/2025-35_TCs`). Com uma pasta por processo, ficha e índice, o projeto **Operação** atende a todos: "trabalhe no processo SEI_02070.020239…".
**Decisão aceita.** Novos processos são trabalhados no projeto Operação. Projetos por processo existentes são revistos na Fase 3.C: os que apontam para pastas que serão movidas são **re-apontados** ou **arquivados** depois que suas instruções forem copiadas para `PROCESSO.md` (seção "Instruções específicas"). Exceção: processos muito longos ou sigilosos podem manter projeto próprio, que aponta para a pasta nova do processo.
**Consequência.** Menos projetos para manter. A memória de cada projeto arquivado se perde, por isso a cópia prévia das instruções.

### ADR-014 — Exclusão controlada

**Decisão aceita.** Nenhum arquivo é excluído diretamente. Os candidatos vão para `99_arquivo/_a-excluir_AAAA-MM-DD/`, com a origem registrada no mapa de reorganização. Depois de **30 dias** sem necessidade de recuperação, você exclui a pasta manualmente. A lixeira do Google Drive ainda guarda os arquivos por mais 30 dias. Arquivos idênticos só são eliminados depois de **conferência por SHA-256**, e sempre preservando uma cópia no destino canônico.

### Demais ADRs — pontos que mudam em relação à v2

- **ADR-003:** os nomes passam a ser **"Escritório CGOV — Implantação"** e **"Escritório CGOV — Operação"**. Durante a Fase 4, o projeto Implantação recebe a pasta CGOV como **segunda pasta, temporariamente**, para executar a reorganização; ela é removida no fim da fase.
- **ADR-006:** a tradução de caminhos sai das instruções do Cowork e passa a ser feita por dois `AGENTS.md`. O do repositório define os caminhos de desenvolvimento; o da raiz da pasta CGOV define os de operação (por exemplo, "estado da NT = `01_processos/<processo>/trabalho/NT_ESTADO.md`").
- **ADR-007:** os destinos passam a ser os da estrutura nova (Seção 5.4).
- **ADR-009:** a pasta CGOV, com LEIA-ME, índices e fichas em Markdown, também pode ser aberta como segundo cofre no Obsidian ("CGOV — Operação"), excluindo as áreas binárias pesadas.

---

## 5. Arquitetura dos repositórios (novo arranjo)

### 5.1. Repositório de desenvolvimento — `C:\Projetos\cgov-geral` (alvo ao fim da Fase 7)

```
cgov-geral/
├── README.md                    ← o que é + quick start + mapa (este quadro)
├── AGENTS.md                    ← regras e caminhos de DESENVOLVIMENTO para agentes (≤ 6 mil caracteres)
├── CLAUDE.md                    ← @AGENTS.md + específicos do Claude Code
├── CONTRIBUTING.md
├── .claude/settings.json        ← proteções (confirmação de commit/push; bloqueio das áreas de operação)
├── plugins/cgov-escritorio/     ← FONTE ÚNICA: skills/, agents/, commands/, plugin.json
├── operacao/                    ← NOVO: fonte da camada de navegação da pasta CGOV
│   ├── LEIA-ME.md · AGENTS.md   ← textos da raiz da pasta CGOV
│   ├── leia-me-areas/           ← _LEIA-ME.md de cada área (01_ … 99_)
│   └── modelos/                 ← PROCESSO.md, NT_ESTADO.md, _INDICE.md, ficha de projeto
├── docs/                        ← arquitetura, fluxos, ADRs, catálogo de skills, decision-log, plano
├── paineis/                     ← PBIP sem dados (Fase 10)
├── scripts/                     ← link_acervo.py, publicar_operacao.py, gerar_indices.py,
│                                   reorganizar_cgov.py, verificar_sanitizacao.py
├── archive/                     ← scripts .sh do WSL, históricos sanitizados
├── .agents/skills ⇢ junção para plugins/cgov-escritorio/skills (ignorado)
├── .obsidian/ · dist/ · .env    ← ignorados
└── local/                       ← ignorado
    ├── processos ⇢ CGOV\01_processos           (antes: analyses)
    ├── normativos ⇢ CGOV\03_normativos          (antes: normative-sources)
    ├── escritorio ⇢ CGOV\90_escritorio-virtual  (antes: acervo-drive)
    └── installed-reference\ archive\ historico\ pilots\
```

**Mudança-chave:** a pasta `operacao/` torna o repositório a **fonte** dos textos de navegação da pasta CGOV (LEIA-ME, AGENTS, `_LEIA-ME` de cada área e modelos). O `publicar_operacao.py` copia esses textos para o Drive, como já faz com `docs/` → `_referencia`. Assim, a camada de navegação também tem versão, revisão e histórico.

### 5.2. Repositório operacional — `My Drive\10_Institucional\CGOV` (alvo ao fim da Fase 4)

```
CGOV\
├── LEIA-ME.md                   porta de entrada: o que é, mapa, "onde salvo?", regras
├── AGENTS.md                    regras e caminhos para agentes de IA
├── 00_entrada\                  caixa de entrada: arquivos novos ainda não classificados
├── 01_processos\                uma pasta por processo SEI
│   ├── _LEIA-ME.md · _INDICE.md
│   └── SEI_02070.020239_2025-64_plano-setorial\
│       ├── PROCESSO.md          ficha do processo (frontmatter + resumo + andamento)
│       ├── documentos-sei\      peças baixadas do SEI (insumos)
│       ├── trabalho\            NT_ESTADO.md, rascunhos, análises (servidor e IA)
│       ├── referencias\         apoio: planilhas, dados, mapas, normas específicas, áudios
│       └── produtos\            versões finais enviadas ao SEI (antes da assinatura)
├── 02_notas-tecnicas\           série oficial de NTs e Informações assinadas (PDF)
│   ├── _LEIA-ME.md · _INDICE.md (registro: nº/ano, data, doc. SEI, processo, tema, inciso)
│   └── 2025\ · 2026\
├── 03_normativos\               acervo normativo único: PDF + transcrição .md, mesmo nome-base
│   ├── _LEIA-ME.md · _INDICE.md (catálogo com vigência)
│   └── revogados\
├── 04_colegiados\               CTGRIC, Conselho de Governança, CIG, CTGD: pautas, atas, transcrições
│   └── ctgric\ · conselho-governanca\ · cig\ · ctgd\
├── 05_projetos\                 projetos, oficinas, eventos e parcerias que não são um processo SEI
│   └── AAAA-MM_apelido\  (+ PROJETO.md)
├── 06_gestao-da-coordenacao\    plano de entregas/PGD da CGOV, planejamento, acompanhamento
├── 90_escritorio-virtual\       infraestrutura do Escritório — não editar à mão
│   ├── _LEIA-ME.md
│   ├── referencia\              documentação publicada do repositório (somente leitura)
│   ├── modelos\                 modelos publicados (PROCESSO.md, NT_ESTADO.md…)
│   ├── manutencao\              PENDENCIAS.md · MAPA_REORGANIZACAO_2026-11.csv
│   └── transcricoes\            trabalho de OCR de normativos (intermediário)
└── 99_arquivo\                  processos encerrados, versões superadas, backups
    ├── processos-encerrados\ · versoes-anteriores\ · escritorio-virtual\
    └── _a-excluir_AAAA-MM-DD\   quarentena antes da exclusão (ADR-014)
```

**Mapa de finalidades** (vai para o `LEIA-ME.md` da raiz):

| Pasta | Finalidade | Entra aqui | Não entra aqui | Quem alimenta |
|---|---|---|---|---|
| `00_entrada` | Triagem | Downloads, anexos, arquivos recebidos sem destino claro | Nada fica aqui mais de uma semana | Todos; a IA propõe o destino |
| `01_processos` | Trabalho por processo SEI | Tudo o que pertence a um processo com número SEI | NT já assinada (vai para `02`) | Servidores e IA |
| `02_notas-tecnicas` | Série oficial | NTs e NIs **assinadas** da CGOV, uma vez | Rascunhos | Responsável pela NT, após a assinatura |
| `03_normativos` | Base normativa | Leis, decretos, portarias, INs (PDF + `.md`) | Minutas em discussão (ficam no processo) | Curadoria (agente `curador-acervo`) |
| `04_colegiados` | Secretaria de colegiados | Pautas, atas, listas, transcrições de reuniões | Processos de criação ou alteração do colegiado (vão para `01`) | Secretaria-executiva |
| `05_projetos` | Iniciativas sem processo | Oficinas, eventos, apresentações, parcerias | Material de processo SEI | Responsável pelo projeto |
| `06_gestao-da-coordenacao` | Gestão interna da CGOV | Plano de entregas, PGD da equipe, planejamento | Processos | Coordenador |
| `90_escritorio-virtual` | Infraestrutura de IA | Gerado pela publicação do repositório e pelos agentes | Trabalho de processo | Publicação automática |
| `99_arquivo` | Memória | Encerrados, versões superadas | Material em uso | Triagem periódica |

### 5.3. Estrutura de documentos Markdown (navegação para pessoas e IA)

| Documento | Onde | Para quem | Conteúdo | Mantido por |
|---|---|---|---|---|
| `LEIA-ME.md` | Raiz | Servidores (e IA) | O que é o Escritório; mapa de pastas (5.2); "Tenho X, onde salvo?"; convenção de nomes; regras de LGPD; como pedir ajuda ao Claude | Repositório (`operacao/`), publicado |
| `AGENTS.md` | Raiz | Agentes de IA | Caminhos canônicos (onde ler, onde gravar, onde nunca gravar); convenções de nomes; obrigação de atualizar `PROCESSO.md` e índices; uso de `00_entrada` | Repositório, publicado |
| `_LEIA-ME.md` | Cada área | Ambos | Finalidade, o que entra e o que não entra, padrão de nome, exemplo | Repositório, publicado |
| `_INDICE.md` | `01`, `02`, `03`, `04`, `05` | Ambos | Tabela gerada a partir dos frontmatters (processo, situação, inciso, última atualização…) | `gerar_indices.py` / comando `/cgov-escritorio:atualizar-indices` |
| `PROCESSO.md` | Cada processo | Ambos | Frontmatter (abaixo) + objeto, histórico, produtos, links para NTs, "instruções específicas" | Servidor responsável + IA |
| `NT_ESTADO.md` | `trabalho/` de cada processo | IA (suíte `cgov-nt`) | Estado e roteiro da NT | Skills `cgov-nt-01` a `07` |
| `PROJETO.md` | Cada projeto em `05` | Ambos | Frontmatter semelhante ao do processo | Responsável |

**Frontmatter padrão do `PROCESSO.md`** (modelo completo no Apêndice F):

```yaml
---
tipo: processo
sei: "02070.020239/2025-64"
apelido: plano-setorial
titulo: "Plano Setorial … (ECOA ICMBio)"
inciso_art37: [II]
situacao: em-andamento        # em-andamento | aguardando-terceiros | concluido | arquivado
unidade_demandante: "…"
aberto_em: 2025-…
atualizado_em: 2026-11-05
notas_tecnicas: ["NT 31/2026"]
cowork_projeto: ""            # preencher só se houver projeto Cowork dedicado (ADR-013)
---
```

Sem nomes nem matrículas de servidores no frontmatter (LGPD). Quando necessário, registra-se o **papel** ("responsável: coordenação").

### 5.4. Convenção de nomes

| Objeto | Padrão | Exemplo |
|---|---|---|
| Pasta de processo | `SEI_<órgão>.<número>_<ano>-<dígito>_<apelido>` (apelido em minúsculas, com hífen, sem acento) | `SEI_02070.020239_2025-64_plano-setorial` |
| Subpastas de processo | Fixas: `documentos-sei`, `trabalho`, `referencias`, `produtos` | — |
| Documento baixado do SEI | `AAAAMMDD_SEI_<nº documento>_<tipo>_<descrição>.pdf` (padrão já usado em parte do acervo) | `20260402_SEI_023188992_Parecer_PFE_101-2026.pdf` |
| NT assinada | `AAAA\NT_<nº>-<ano>_SEI_<nº documento>_<tema>.pdf` | `2026\NT_13-2026_SEI_023115133_pfe-plano-setorial.pdf` |
| Normativo | `AAAAMMDD_<Tipo> <nº>_<tema>.pdf` e `.md` com o mesmo nome-base (padrão já usado em `normative-sources`) | `20251211_Portaria ICMBio 5.592_Regimento Interno.pdf` |
| Projeto | `AAAA-MM_<apelido>` | `2026-10_oficina-pgd-gr2-fortaleza` |
| Versões | Sufixo `_v1`, `_v2`…; ao concluir, as anteriores vão para `99_arquivo/versoes-anteriores/` | — |

As pastas de máquina (processos, projetos) evitam espaços e acentos. Os nomes de arquivos de documentos podem manter acentos, porque o Drive e o Cowork lidam bem com eles.

### 5.5. Mapa de reorganização (nível de pasta; o detalhamento arquivo a arquivo é gerado na Fase 4.1)

| Origem atual | Destino | Observação |
|---|---|---|
| `CGOV_Processos\<71 pastas>` (72 nomes no mapa da 4.1, contando a pasta vazia duplicada) | `01_processos\SEI_<…>_<apelido>\` | Renomear para a convenção. Arquivos soltos → `documentos-sei\`; `_CGOV_NT\` e `Claude outputs\` → `trabalho\`; `_referencias`, `_Referências indicadores`, `consulta`, `normativas`, `_Audios`, `Guia de Gestão`, `Fichas Indicadores`, `Apresentações`, `Oficina`, `avaliacao_pgd` → `referencias\` (ou `trabalho\`, conforme o caso, no mapa CSV) |
| `CGOV_Processos\02070.006604 2026-17_Política de Governança` + `…_v2` | Uma pasta `SEI_02070.006604_2026-17_politica-governanca\` | **Fundir** (D10); arquivos de mesmo nome da v2 em `trabalho\v2\` |
| `CGOV_Processos\ADPF` (sem número) | `99_arquivo\processos-encerrados\ADPF\` | Projeto antigo sem número SEI rastreável (D11) |
| `CGOV_Administrativo\SEI_*` (4) | `01_processos\` | — |
| `CGOV_Administrativo\CGOV_Fundo Rio Doce` | `05_projetos\fundo-rio-doce\` (ou processo, se houver número SEI) | — |
| `_acervo…\analyses\<pastas de processo>` (8) | `01_processos\<processo>\trabalho\` | Correspondência pelo número SEI (por exemplo, `SEI_02070.012181_2026_66_PGRO`, `…014637…OCDE`, `…005395…Comite-Gestor`, `Integra+`) |
| `_acervo…\analyses\` com `MOVIDO_PARA.txt` (4) | `99_arquivo\_a-excluir_…\` | O conteúdo já está nas pastas `_CGOV_NT`; a movimentação fica registrada no CSV |
| `_acervo…\analyses\Indicadores_ocde` | `01_processos\SEI_02070.014637_2025-41_ocde-pgd\trabalho\` | — |
| `_acervo…\analyses\_Impacto Regulatório_Plano de Manejo` | Nova pasta `01_processos\SEI_02070.017019_2026-34_air-planos-manejo\` (processo da NT 27/2026): `.md` e versões → `trabalho\`; `SEI_023982292_Nota_Tecnica_27_final.pdf` → `02_notas-tecnicas\2026\` | D11. Processo **SEI nº 02070.017019/2026-34**, confirmado pelo Coordenador em 05/11 |
| `_acervo…\analyses\SEI__Reunioes-CIG` | `04_colegiados\cig\` | — |
| `_acervo…\analyses\normative-transcription` | `90_escritorio-virtual\transcricoes\` | 487 PNG regeneráveis → candidatos a `_a-excluir` |
| `_acervo…\analyses\revisao-prompts-legados-2026-08-28` | `99_arquivo\escritorio-virtual\` | Artefato de desenvolvimento |
| `_acervo…\analyses\_doutorado` | `My Drive\_projetos\05_privado\_doutorado\` (fora da pasta institucional) | D14 |
| `_acervo…\_referencia\` | `90_escritorio-virtual\referencia\` | — |
| `_acervo…\manutencao\` | `90_escritorio-virtual\manutencao\` | — |
| `_acervo…\archive\` | `99_arquivo\escritorio-virtual\` | — |
| `_acervo…\_tmp\` | `99_arquivo\_a-excluir_…\` | Temporários |
| `normative-sources\` (110) | `03_normativos\` | A PGE (Portaria nº 768/2020, revogada) vai para `revogados\` |
| `CGOV_Normativas\` (17) | 6 exclusivos → `03_normativos\`; 11 idênticos → `_a-excluir` | Conferência por SHA-256 |
| `CGOV_Notas Técnicas\` (20) | `02_notas-tecnicas\2025\` e `2026\` | Manter os nomes originais na primeira etapa; padronizar depois, com o índice |
| `CGOV_Projetos\` | `05_projetos\<AAAA-MM_apelido>\`; Plano de Entregas CGOV (GIZ) → `06_gestao-da-coordenacao\` | Versões `v1`–`v3` das apresentações → `99_arquivo\versoes-anteriores\` (D15) |
| `organizar\` (3 versões do Plano de Entregas CGGE) | `06_gestao-da-coordenacao\plano-de-entregas\` (versão vigente) + anteriores em `99_arquivo` | Qual é a vigente: D15 |
| `CGOV_Processos\SEI_02070.020064_2025_95_Planos de Manejo` + `SEI_SEI_02070.020064_2025_95_IN Planos Manejo` | Uma pasta `01_processos\SEI_02070.020064_2025-95_planos-manejo\`; conteúdo da segunda em `trabalho\in-planos-manejo\` | **Fundir** (D22, como D10) |
| `_acervo…\analyses\<processo>\` — PDFs baixados do SEI | `01_processos\<processo>\documentos-sei\` (demais arquivos em `trabalho\`; PDFs de apoio em `referencias\`) | Refinamento da 4.1, coerente com as subpastas da Seção 5.2 |
| `normative-sources\Minuta_Portaria_*_Gestao_Riscos_*.md` (2) | `01_processos\SEI_02070.001696_2026-31_gestao-riscos\trabalho\` | Minutas ficam no processo (D23) |
| `CGOV_Normativas\` Portarias ICMBio 4.101/2023 e 1.164/2025 (mesmo nome, conteúdo diferente) | `99_arquivo\versoes-anteriores\normativos\`; a versão de `normative-sources` fica em `03_normativos\` | D22 |
| `CGOV_Normativas\SEI_023125903_Minuta_de_Portaria.pdf` | `01_processos\SEI_02070.006604_2026-17_politica-governanca\trabalho\` | D22 |
| `CGOV_Notas Técnicas\08_NT_16-2025_…_Retirar.pdf` · `SEI_023512415_Nota_Tecnica_20.pdf` | `99_arquivo\versoes-anteriores\notas-tecnicas\` · `02_notas-tecnicas\2026\` | D22 |
| `CGOV_Projetos\` soltos: 2 do PPI e Ajuda-Memória MMA · `Matriz de impacto.docx` e imagem | `01_processos\SEI_02070.011203_2025-90_parcerias-inovacao\referencias\` · `00_entrada\` | D22 |
| 16 pastas de processo sem apelido | 11 com apelido proposto pelo assunto do processo; 5 só com o número | D24 |
| Raiz: `21_CTGRIC_Transcrição de Reunião.docx` + `.gdoc` | `04_colegiados\ctgric\` | Mover o par juntos |
| Raiz: `cgov_projetos_trimestre.html` | `06_gestao-da-coordenacao\` | — |

### 5.6. Itens desnecessários identificados (vão para a quarentena `_a-excluir`, nunca para exclusão direta)

| Item | Motivo | Evidência |
|---|---|---|
| `CGOV_Processos\SEI_02070 (1).009510_2025_19_AUDIT\` | Pasta vazia, duplicada | 0 arquivos |
| `…\Relatorio_de_Status…08ABR2024 (1).xlsx` | Cópia idêntica | SHA-256 igual ao original |
| ~~`…\SEI_022838998_Nota_Tecnica_3_2026 (1).pdf`~~ | **Não** é cópia idêntica (SHA-256 diferente, 4.1) | Mantida como `…_Nota_Tecnica_3_2026_v2.pdf` (D22); não vai para a quarentena |
| `_acervo…\analyses\_teste_mv.tmp` | Arquivo de teste vazio | 0 bytes |
| 4 pastas só com `MOVIDO_PARA.txt` | Aviso de movimentação já executada | Conteúdo em `_CGOV_NT` |
| 13 arquivos de `CGOV_Normativas` | Idênticos a arquivos de `normative-sources` ou a cópias já presentes em processos | SHA-256 (4.1) |
| 3 arquivos vazios em processos (`New Documento de Texto.txt`, `Links uteis.txt`, `02070.017019_2026-34.txt`) e 2 pastas vazias (`_Audios`, `Serie_ANO`) | Sem conteúdo | 0 bytes (4.1) |
| `_acervo…\_tmp\pdfs\` (62) | Imagens temporárias de revisão | Pasta `_tmp` |
| 487 PNG de `normative-transcription` | Páginas renderizadas, regeneráveis a partir dos PDFs | Extensão e local |
| `archive\dev-local_2026-11\_backup\` (427) | Na maioria idênticos às análises atuais (346 grupos) | **Manter** até a Fase 4 terminar; reavaliar depois |
| Versões antigas de apresentações e planilhas | Superadas | Não excluir: ir para `99_arquivo\versoes-anteriores\` |

Economia estimada sem perda de informação: cerca de **400 MB** e **1.000 arquivos**. Os 85 MB de duplicatas, os 302 MB do OCR intermediário e os temporários ficam fora da área de trabalho.

**Resultado do mapa da 4.1–4.2:** a quarentena recebe **584 arquivos (322,5 MB) e 3 pastas vazias**, e o restante dos ~400 MB previstos depende da reavaliação do backup `dev-local_2026-11` (490 arquivos), que fica em `99_arquivo\escritorio-virtual\` até o fim da Fase 4.

### 5.7. Fluxo integrado dos dois repositórios

```mermaid
flowchart LR
  subgraph DEV["DESENVOLVIMENTO<br/>C:\\Projetos\\cgov-geral"]
    PI["Cowork: Implantação<br/>Claude Code · Antigravity · Obsidian"]
    SRC["plugins/ · operacao/ · docs/ · scripts/"]
  end
  GH["GitHub privado"]
  CONTA["Conta Claude<br/>plugin cgov-escritorio"]
  subgraph OPS["OPERAÇÃO<br/>My Drive\\10_Institucional\\CGOV"]
    PO["Cowork: Operação"]
    NAV["LEIA-ME · AGENTS · _LEIA-ME · _INDICE"]
    PROC["01_processos/SEI_x/<br/>PROCESSO.md · trabalho/NT_ESTADO.md"]
    ESC["90_escritorio-virtual/<br/>referencia · modelos · manutencao"]
  end
  PI --> SRC -- "commit/push" --> GH
  SRC -- "publicar_operacao.py: plugin" --> CONTA --> PO
  SRC -- "publicar_operacao.py: textos e modelos" --> NAV & ESC
  PO --> PROC
  PO -- "PENDENCIAS.md" --> ESC -- "lido por" --> PI
```

---

## 6. Plano de implantação em fases

### 6.1. Visão geral

| Fase | Nome | Resultado | Executa | Estimativa* | Situação |
|---|---|---|---|---|---|
| 0 | Decisões | ADRs e decisões D1–D56 respondidos | Coordenador | 1 dia | 🟨 Parcial: D1–D4 e D9–D56 respondidas; D5–D8 e ADR-001, 005 e 008–011 pendentes |
| 1 | Consolidação do desenvolvimento no Windows | **✅ Concluída em 04/11** | — | — | ✅ 04/11/2026 |
| 2 | **Arquitetura dos repositórios** | Arranjo das Seções 5.1–5.6 aprovado (ADR-012/013/014; D10–D16) | Coordenador | 1 dia | ✅ 05/11/2026 |
| 3 | Projetos Cowork | "Implantação" criado; `cgov-geral-v1` preservado e arquivado; vínculos dos demais projetos inventariados | Coordenador (interface) + Claude | ½ dia | ✅ 05/11/2026 |
| 4 | **Reorganização da pasta CGOV** | Estrutura nova, documentos de navegação, fichas, índices; projeto "Operação" criado | Claude (scripts e textos) + Coordenador (aprovações e execução) | 3–5 dias | ✅ 06/11/2026 (4.11 em 05/12/2026) |
| 5 | Atualização do repositório de desenvolvimento | Scripts em Python, pasta `operacao/`, documentação corrigida, junções e `.env` com os caminhos novos | Claude, com portões | 2–3 dias | ✅ 07/11/2026 (*merge* `e305404`; D36–D41) |
| 6 | Portfólio de skills | 12 skills promovidas a fonte; caminhos neutros; novas skills `cgov-gestao-acervo`, `cgov-triagem-processo-sei` (D4) e as quatro da 6.10 (D45); modelo geral de análise de atos normativos (6.9, D34); desatualizadas reinstaladas | Claude + Coordenador | 3–5 dias | ✅ Concluída 08/11: 6.1 ✅ 07/11 (D42–D43); decisões 6.6 (D4), 6.9(a) (D44) e 6.10 (D45) ✅ 07/11; 6.2 ✅ 07/11 (D46); renomeação das skills do PGD (D47); 6.3 ✅ 07/11 (D48); 6.5 ✅ 07/11 (D49); 6.9(b)–(d) ✅ 07/11 (D50); 6.4 ✅ e skill da 6.6 criada 07/11 (D51); E8 ✅ 07/11 (D52); 6.10 ✅ 07/11 (D53) |
| 7 | Plugin `cgov-escritorio` | Um zip por versão; 32 skills avulsas substituídas; comandos de acervo | Coordenador + Claude | 1–2 dias | 🟨 |
| 8 | Multiplataforma e aposentadoria do WSL | Claude Code, Antigravity, Codex e Obsidian (dois cofres) | Coordenador + Claude | 1 dia | ⬜ |
| 9 | Agentes e orquestração | 5 agentes + comandos; cenário Maestri | Claude + Coordenador | 3–5 dias | ⬜ |
| 10 | Painéis Power BI | Catálogo, PBIP versionado, skills de painel | Coordenador + Claude | 3–5 dias | ⬜ |
| 11 | Qualidade e pilotos | Evals de todas as skills; 2 pilotos reais | Coordenador + Claude | 1–2 semanas | ⬜ |
| 12 | Disseminação e governança | Guia do servidor, capacitação, ciclo de versões | Coordenador | contínuo | ⬜ |

\* Referência para trabalho em tempo parcial.

---

### Fase 0 — Decisões — 🟨 parcial

| Etapa | Ação | Situação |
|---|---|---|
| 0.1 | Aprovar os ADRs (Seção 4) | ADR-002, 003, 012, 013 e 014 aceitos; demais pendentes |
| 0.2 | Responder às decisões da Seção 9 | D1–D4 e D9–D56 respondidas (04–07/11); D5–D8 pendentes, sem bloquear as Fases 3–6 |
| 0.3 | Confirmar em `themaestri.app` se existe versão Windows (D8) | Pendente |
| 0.4 | Pré-requisitos: `git` ✅, `python --version` (≥ 3.11), `node --version` (LTS), Claude Desktop, Antigravity, Obsidian | Git conferido em 04/11 |

---

### Fase 1 — Consolidação do desenvolvimento no Windows — ✅ concluída (04/11/2026)

Resumo do que foi feito: remoto do WSL corrigido para `cgov-geral`; `.gitignore` descartado; `.github/` (Copilot) arquivado; *push* `4960e11..67957fe`; clone em `C:\Projetos\cgov-geral` (`autocrlf=false`); manifesto `local/_manifesto_wsl_20261104.sha256` (490 arquivos), com 63/63 conferidos em `local\` e 488/488 no Drive (`_acervo…\archive\dev-local_2026-11`); junções para o Drive; `.env` do Windows. As junções e o `.env` serão **refeitos na Fase 5** para os caminhos novos.

---

### Fase 2 — Arquitetura dos repositórios (aprovação) — ✅ concluída (05/11/2026)

**Objetivo:** aprovar o arranjo **antes** de mexer em qualquer arquivo. Esta fase é só de leitura e decisão.

| Etapa | Ação | Entregável | Situação |
|---|---|---|---|
| 2.1 | Revisar a Seção 5.1 (desenvolvimento) e a Seção 5.2 (operação), com o mapa de finalidades | Aprovação ou ajustes | ✅ Aceito sem ajustes |
| 2.2 | Revisar a convenção de nomes (5.4) e o frontmatter do `PROCESSO.md` (5.3 e Apêndice F) | Aprovação ou ajustes | ✅ Aceito sem ajustes |
| 2.3 | Revisar o mapa de reorganização (5.5) e decidir os itens "a decidir" | D10, D11, D14, D15 | ✅ Respondidas |
| 2.4 | Revisar a lista de itens desnecessários (5.6) e a política de quarentena (ADR-014) | D16 | ✅ Respondida |
| 2.5 | Responder D12 (compartilhamento da pasta CGOV) e D13 (projetos Cowork por processo) | Respostas | ✅ Respondidas |
| 2.6 | Revisar os rascunhos do `LEIA-ME.md` da raiz (Apêndice E) e dos modelos (Apêndice F) | Aprovação ou ajustes | ✅ Aceito sem ajustes |

**Critério de aceite:** ADR-012, 013 e 014 aprovados; D10–D16 respondidas. **Portão:** a Fase 4 só começa com esta fase concluída.

**Resultado (05/11/2026):** arranjo das Seções 5.1–5.6 aceito sem ajustes; ADR-012, 013 e 014 aceitos. Decisões incorporadas ao mapa 5.5: D10 fundir as duas pastas da Política de Governança; D11 ADPF para `99_arquivo\processos-encerrados\` e Impacto Regulatório para o processo SEI nº 02070.017019/2026-34 (NT 27/2026); D12 pasta de uso exclusivo do Coordenador (risco de compartilhamento descartado); D13–D16 conforme as recomendações. Portão da Fase 4 liberado.

---

### Fase 3 — Projetos Cowork — ✅ concluída (05/11/2026)

> Documentação oficial ("Organize work with projects"): um projeto reúne descrição, pastas locais, instruções, links (⚠️ campo ausente no Claude Desktop em 05/11; ver 1.2), projetos do Chat vinculados e memória própria; fica no computador e não é compartilhado. Criação: **Projects → + → Start from scratch / Import a project / Use an existing folder**. **Arquivar** apaga nome, instruções, links e memória do projeto, mas **não toca nas pastas**. Arquivos arrastados vão para a **primeira pasta**.

#### 3.A — Criar "Escritório CGOV — Implantação" — ✅ concluída (05/11/2026)

> **Onde criar:** no **aplicativo Claude Desktop, aba Cowork**, e **não** no navegador (claude.ai). Projetos Cowork com pastas locais vivem no computador; a página web de projetos só anexa arquivos. A aba **Code** serve para sessões de terminal no repositório (por exemplo, *commit* e testes de plugin) e não substitui o projeto Cowork.
> **Como vincular pastas:** em **Projects → + → Use an existing folder**, escolha a pasta principal. As demais pastas são adicionadas nas configurações do projeto ou **arrastando a pasta do Explorador de Arquivos para o projeto** (pastas arrastadas viram pastas adicionais do projeto; arquivos arrastados são copiados para a primeira pasta). **Não** coloque caminhos na descrição: a descrição só orienta o Dispatch e não dá acesso a nada.

| Etapa | Onde                                      | O que preencher                                                                                                                                                                                                                                                                                                                                        | Situação |
| ----- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| 3.A.0 | PowerShell em `C:\Projetos\cgov-geral`    | **Versionar este plano** antes de tudo, para protegê-lo e registrar cada atualização: `git add cgov-geral-plano-implantacao.md` → `git commit -m "docs(plano): plano de implantação v3.1"` → `git push` (com a sua confirmação). O plano continua na raiz até a etapa 5.9                                                                              | ✅ 05/11 — `8787e0a` (v3.1); v3.2 e v3.3 em `de0fa54` |
| 3.A.1 | **Projects → + → Use an existing folder** | `C:\Projetos\cgov-geral` (primeira pasta)                                                                                                                                                                                                                                                                                                              | ✅ 05/11 |
| 3.A.2 | Nome e descrição                          | **Nome:** `Escritório CGOV — Implantação` · **Descrição:** *"Desenvolvimento e implantação do Escritório Virtual da CGOV/ICMBio: skills, agentes, documentação, scripts e painéis do repositório cgov-geral, e reorganização da pasta operacional CGOV. Não é usado para Notas Técnicas nem análises de processos."*                                   | ✅ 05/11 |
| 3.A.3 | **Folders**                               | Acrescentar `%USERPROFILE%\My Drive\10_Institucional\CGOV` como **segunda pasta, temporária**, para a Fase 4 (pelas configurações do projeto ou arrastando a pasta do Explorador para o projeto). Ela é removida no fim da Fase 4 (etapa 4.10). Conferência: numa sessão do projeto, pergunte "Quais pastas você tem acesso?"; devem aparecer as duas | ✅ 05/11 — duas pastas confirmadas pelo Claude |
| 3.A.4 | **Instructions**                          | Apêndice A                                                                                                                                                                                                                                                                                                                                             | ✅ 05/11 — instruções v3.4 em **Instruções** e descrição curta restaurada (correção da colagem inicial na descrição) |
| 3.A.5 | **Links**                                 | `https://github.com/lpchagas/cgov-geral`                                                                                                                                                                                                                                                                                                               | ➖ Campo inexistente no Claude Desktop; link incluído no Apêndice A (Fontes de verdade) |
| 3.A.6 | Teste                                     | Nova sessão: *"Leia a Fase 3.B do plano e liste o que fará, sem executar nada."* A resposta deve citar o plano e pedir confirmação                                                                                                                                                                                                                     | ✅ 05/11 — sessão de 05/11 aceita como teste |

**Resultado 3.A (05/11/2026):** plano versionado (`8787e0a`, etapa 3.A.0); projeto "Escritório CGOV — Implantação" criado no Claude Desktop, com as pastas `C:\Projetos\cgov-geral` (1ª) e `%USERPROFILE%\My Drive\10_Institucional\CGOV` (2ª, temporária) confirmadas pelo Claude; teste 3.A.6 aceito pelo Coordenador. Ajustes desta etapa (v3.3): `.obsidian/` incluído no `C:\Projetos\cgov-geral\.gitignore` (D18); regras de interação 9–12 no Apêndice A (D17). *Commit* `de0fa54` (v3.2 + v3.3) enviado e conferido por `git ls-remote` (05/11). **Correção (v3.4):** as capturas mostraram que o campo **Instruções** estava vazio e que o texto do Apêndice A tinha ido para a **descrição**; não há campo de links no Claude Desktop. Corrigido pelo Coordenador em 05/11: Apêndice A v3.4 em **Instruções** e descrição curta restaurada; conferido pelo Claude no contexto da sessão.

#### 3.B — Preservar e arquivar o projeto antigo `cgov-geral-v1` — ✅ concluída (05/11/2026)

Não exclua esse projeto e não o reaproveite. Ele é de 22/09, anterior à separação dos fluxos e à mudança para o Windows, e pode ter instruções e memória que valem guardar.

1. Abrir as configurações do `cgov-geral-v1` e anotar a **pasta vinculada**. — ✅ 05/11: 4 pastas (`cgov-geral-v1`, `pgd-agente-icmbio`, `pgd-ocde-icmbio`, `cgge-fgbio-2026`); caminho completo conhecido só da primeira (`C:\_cowork\cgov-geral-v1`).
2. Copiar o texto de **Instructions** para `C:\Projetos\cgov-geral\local\archive\cowork-projetos\cgov-geral-v1_instrucoes_2026-11-05.md`. A pasta `local\` é ignorada pelo Git. — ✅ 05/11: cópia literal gravada e conferida por SHA-256 (`ad862755…`); `git check-ignore` confirma que fica fora do Git.
3. Se o projeto tiver memória relevante, abrir uma sessão nele e pedir: *"Resuma o que está na memória deste projeto"*. Salvar o resumo no mesmo arquivo. Alternativa mais simples: claude.ai ou Claude Desktop → projeto → **Memória → Ver**, e copiar o texto. — ✅ 05/11: memória **não preservada** por decisão do Coordenador (D20): trata só de uma análise antiga, sem relação com a implantação; registrado no arquivo da etapa 2.
4. **Arquivar** o projeto (menu do projeto → **Archive**) só **depois** de o projeto Implantação passar no teste 3.A.6 e de a 3.B.3 estar concluída. — ✅ 05/11: projeto arquivado pelo Coordenador. Arquivar apaga nome, instruções e memória do projeto, mas não toca em pastas; as instruções já estão preservadas.

**Resultado 3.B (05/11/2026):** instruções e as 4 pastas vinculadas do `cgov-geral-v1` preservadas em `C:\Projetos\cgov-geral\local\archive\cowork-projetos\cgov-geral-v1_instrucoes_2026-11-05.md`; memória não preservada (D20); projeto arquivado pelo Coordenador.

#### 3.C — Inventariar os vínculos dos demais projetos Cowork — ✅ concluída (05/11/2026)

Para cada projeto da lista que possa apontar para a pasta CGOV (por exemplo, `02070.006604 2026-17_Política de Governança_v2`, `02070.007589/2025-35_TCs`, `Sistema Integridade ICMBio`, `Painel Estratégico OCDE/ICMBio`, `CGGE_Estrutura`, `oficina-planejamento-GR2`), e para as pastas extras do `cgov-geral-v1` (`pgd-agente-icmbio`, `pgd-ocde-icmbio`, `cgge-fgbio-2026`), registre num quadro em `C:\Projetos\cgov-geral\local\archive\cowork-projetos\inventario.md`: **nome**, **pastas vinculadas** e **se a pasta será movida na Fase 4**. Esse quadro orienta a etapa 4.9 (re-apontar ou arquivar, conforme o ADR-013).

**Resultado 3.C (05/11/2026):** ✅ inventário simplificado (D21) em `C:\Projetos\cgov-geral\local\archive\cowork-projetos\inventario.md` (SHA-256 `d43f798c…`): 13 projetos listados; segundo o Coordenador, os vínculos dos projetos antigos não existem mais desde a formatação do computador (backups em `%USERPROFILE%\My Drive\_projetos`) e nenhum aponta para a pasta CGOV atual. **Consequência:** a Fase 4 não quebra vínculo de projeto antigo; a etapa 4.9 passa a decidir só se cada projeto é re-apontado ou arquivado (ADR-013). ⚠️ A lista vem de capturas de tela e pode não ter os 16 projetos.

**Resultado da Fase 3 (05/11/2026):** projeto "Escritório CGOV — Implantação" criado no Claude Desktop, com as duas pastas, as instruções v3.4 e a descrição curta, e testado (3.A.6); `cgov-geral-v1` preservado e arquivado (3.B); vínculos dos demais projetos inventariados (3.C, D21). *Commits* de 05/11: `8787e0a`, `de0fa54`, `6890b63`, `320007d` e `be2f493`, todos conferidos por `git ls-remote`. Decisões D17–D21. **Portão:** a Fase 4 pode começar.

---

### Fase 4 — Reorganização da pasta CGOV — ✅ concluída (06/11/2026; 4.11 agendada para 05/12/2026)

> Executada no projeto Implantação, com a pasta CGOV vinculada temporariamente. O Google Drive para desktop deve estar **em execução** e com a pasta **"Disponível offline"**, para que as movimentações sejam sincronizadas como movimentações (e não como exclusão + criação). Nenhuma etapa exclui arquivos (ADR-014).

| Etapa | Ação | Quem | Aceite | Situação |
|---|---|---|---|---|
| 4.1 | **Gerar o mapa de reorganização arquivo a arquivo** (`90_…\manutencao\MAPA_REORGANIZACAO_2026-11.csv`, rascunho inicialmente em `local\`), com as colunas `origem`, `destino`, `acao` (mover / renomear / quarentena / a-decidir), `sha256`, `motivo`. Aplica as regras da Seção 5.5 e marca os ambíguos como `a-decidir` | Claude (script `reorganizar_cgov.py --planejar`, somente leitura) | CSV cobre 100% dos arquivos (2.831 na 4.1) | ✅ 05/11 |
| 4.2 | **Revisão do mapa** pelo Coordenador: resolver os `a-decidir` e conferir os nomes de pasta dos processos (73 no mapa) | Coordenador | Zero linhas `a-decidir` | ✅ 05/11 |
| 4.3 | **Manifesto anterior**: SHA-256 de todos os arquivos (`manifesto_pre_2026-11.sha256`) | Claude | Arquivo gerado | ✅ 05/11 |
| 4.4 | **Simulação**: `reorganizar_cgov.py --simular` lista cada operação e conflitos de nome, sem mover nada | Claude | Zero conflitos | ✅ 05/11 |
| 4.4a | **Encurtar os destinos longos** (D26): regra de destino mais curta em `99_arquivo` para os 312 destinos acima de 259 caracteres (lotes f e g); novo `--planejar`, conferência de que só mudam linhas dos lotes f e g, nova `--simular` e aprovação do Coordenador. Deve ser feita **antes do lote a**, porque o `--planejar` só reproduz o mapa sobre a árvore original | Claude (script) + Coordenador (aprovação) | Zero destinos acima de 259 caracteres; linhas dos lotes a–e inalteradas | ✅ 05/11 |
| 4.5 | **Execução em lotes**, cada um com confirmação e conferência do sincronismo do Drive antes do próximo: **(a)** criar a estrutura de pastas e publicar `LEIA-ME.md`, `AGENTS.md`, `_LEIA-ME.md` e modelos; **(b)** `03_normativos`; **(c)** `02_notas-tecnicas`; **(d)** `01_processos` (renomear e reorganizar subpastas; fundir `analyses`); **(e)** `04`, `05` e `06`; **(f)** `90_escritorio-virtual` e `99_arquivo`; **(g)** quarentena | Coordenador executa `reorganizar_cgov.py --executar --lote X` no PowerShell; Claude confere | Cada lote: arquivos movidos = linhas do CSV | ✅ 05/11 (lotes a–g e limpeza D29) |
| 4.6 | **Manifesto posterior** e conferência: todo hash anterior existe no destino previsto | Claude | 100% conferido | ✅ 05/11 |
| 4.7 | **Fichas e índices**: criar `PROCESSO.md` em cada processo, a partir do modelo, com o frontmatter preenchido pelo que se deduz do nome e dos documentos, e campos incertos marcados `⚠️ revisar`; gerar os `_INDICE.md` | Claude (servidor revisa as fichas aos poucos) | 74 fichas; índices gerados | ✅ 05/11 (revisão das fichas em andamento) |
| 4.8 | **Projeto "Escritório CGOV — Operação"** (Claude Desktop, aba Cowork): **+ → Use an existing folder** → pasta única `%USERPROFILE%\My Drive\10_Institucional\CGOV`. Descrição: *"Trabalho técnico e administrativo da Coordenação de Governança do ICMBio: Notas Técnicas, pareceres, análises de processos SEI, normativos, colegiados e projetos."* Instruções: Apêndice B. Teste: *"Onde está o processo do Plano Setorial e qual o estado da NT?"*; e uma triagem fictícia com `cgov-nt-01-triagem`, que deve gravar em `01_processos\<processo de teste>\trabalho\`; depois mover o teste para a quarentena | Coordenador | Teste aprovado | ✅ 05/11 |
| 4.9 | **Projetos Cowork afetados** (inventário 3.C): re-apontar as pastas ou arquivar após copiar as instruções para o `PROCESSO.md` (ADR-013) | Coordenador | Nenhum projeto apontando para caminho inexistente | ✅ 06/11 |
| 4.10 | Remover a pasta CGOV do projeto Implantação; copiar mapa, manifestos e registros para `90_escritorio-virtual\manutencao\`; registrar a reorganização no `decision-log` (Decisão 28) | Coordenador + Claude | Pasta fora do projeto; §28 no decision-log | ✅ 06/11 (remoção da pasta pelo Coordenador) |
| 4.11 | Após 30 dias: excluir `99_arquivo\_a-excluir_…` (ADR-014) | Coordenador | — | ⬜ |

**Resultado (4.1–4.2, 05/11/2026).**
- **Script** `C:\Projetos\cgov-geral\scripts\reorganizar_cgov.py` v1.0.0: modos `--planejar`, `--simular`, `--executar --lote` e `--reverter`. Multiplataforma e sem caminhos pessoais. Nunca exclui nem sobrescreve; confere o SHA-256 antes de mover; grava um registro de cada operação em `C:\Projetos\cgov-geral\local\reorganizacao\registros\`. Usa o prefixo `\\?\` no Windows e um cache de hashes retomável. As decisões e os apelidos da 4.2 ficam em `decisoes.csv` e `apelidos.csv` e são reaplicados a cada `--planejar`.
- **Mapa** `C:\Projetos\cgov-geral\local\MAPA_REORGANIZACAO_2026-11.csv`: 2.858 linhas, SHA-256 `5e686e821d30744a…`. Cobre 2.831/2.831 arquivos (100%): mover 2.245, renomear 2, quarentena 584 arquivos (322,5 MB) e 3 pastas vazias, criar 24 pastas. Lotes: a 24 · b 109 · c 20 · d 1.129 · e 24 · f 965 · g 587.
- **4.2:** 28 `a-decidir` resolvidos (D22–D23) e 11 apelidos atribuídos (D24). O mapa tem **zero `a-decidir`**, e o `--simular` dá **zero conflitos**, com avisos de caminho longo, todos em `99_arquivo` (30 impressos; o total é 312, conforme a correção abaixo).
- **Processos:** 73 pastas em `01_processos`, 5 só com o número. Os 72 nomes de origem de `CGOV_Processos` incluem a pasta vazia duplicada e a `ADPF`. Entram também os processos vindos de `analyses` (PGRO, Avaliação PGD) e de `CGOV_Administrativo` (00810.000079, 000796, 010603).
- **Teste:** numa árvore sintética, os lotes a, b, e, f e g foram executados e revertidos, e a árvore voltou idêntica, com pastas e arquivos. A pasta CGOV não foi alterada (2.831 arquivos).
- **Windows (05/11):** Python 3.12.10; `py scripts\reorganizar_cgov.py --simular` na pasta CGOV real deu **zero conflitos**, só com os avisos de caminho longo em `99_arquivo`. O prefixo `\\?\` funcionou. *Commit* `7f5a324`, conferido por `ls-remote`.
- ~~**Pendência para a execução:** rodar `--planejar` de novo antes da 4.4, se a pasta CGOV mudar~~ — feito na 4.3–4.4: mapa idêntico.
- **Correção:** o `--simular` imprime no máximo 30 avisos. O total de destinos com mais de 259 caracteres é **312** (lote f: 180, até 301 caracteres; lote g: 132, até 285), todos em `99_arquivo` (ver 4.4).

**Resultado (4.3–4.4, 05/11/2026).**
- **Novo `--planejar`** (gravado à parte, em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\MAPA_conferencia_2026-11-05.csv`, para não tocar no mapa aprovado): 2.831 arquivos, 28 decisões e 11 apelidos reaplicados, 2.858 linhas. O SHA-256 é `5e686e821d30744a…`, **idêntico byte a byte** ao mapa aprovado. A pasta CGOV não mudou desde a 4.2.
- **4.3 — Manifesto anterior** `C:\Projetos\cgov-geral\local\reorganizacao\manifesto_pre_2026-11.sha256`: 2.831 linhas no formato `sha256sum`, ordenadas por caminho, com SHA-256 próprio `8a6470cd7f48471a…`. Os hashes foram recalculados do disco, sem o cache (3,53 GB). Resultado: 2.831/2.831 caminhos presentes no mapa e **zero hashes divergentes**, o que também valida o cache. São 2.164 conteúdos distintos. O manifesto fica em `local\` até a 4.6; o destino final é `90_escritorio-virtual\manutencao\`.
- **4.4 — Simulação** (`--simular --verificar-hash`, com a raiz do Windows de 45 caracteres): 2.858 operações (criar 24, mover 2.245, renomear 2, quarentena 587) e **zero conflitos**. Por lote: a 24 · b 109 · c 20 · d 1.129 · e 24 · f 965 · g 587, todos sem conflitos. Há **312 avisos de caminho longo**, todos com destino em `99_arquivo` (f 180, g 132), e nenhum fora dele. Registros: `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\simulacao_todos_2026-11-05.txt` e `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\simulacao_detalhada_2026-11-05.txt`.
- **Decisão D26:** encurtar os destinos longos antes da execução (etapa 4.4a). A pasta CGOV não foi alterada: continua com 2.831 arquivos.

**Resultado (4.4a, 05/11/2026).**
- **Script** `C:\Projetos\cgov-geral\scripts\reorganizar_cgov.py` **v1.1.0**: tabela `ENCURTAMENTOS_99` e método `encurtar_destinos()`, que roda depois das decisões da 4.2 e antes da atribuição dos lotes. Troca o prefixo da subárvore inteira, sem mudar nomes de arquivo, e para se o prefixo novo já estiver em uso. A v1.0.0 ficou guardada em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\reorganizar_cgov_v1.0.0.py`.
- **Regra aprovada (D26):** lote f, `99_arquivo/escritorio-virtual/dev-local_2026-11/_backup/analyses_pre-drive_20261006/normative-transcription/` → `99_arquivo/escritorio-virtual/transcr-bkp_20261006/` (401 linhas; maior caminho 301 → 244). Lote g, `99_arquivo/_a-excluir_2026-11-05/_acervo-escritorio-virtual/analyses/normative-transcription/` → `99_arquivo/_a-excluir_2026-11-05/transcr-analyses/` (487 linhas; 285 → 242). São 888 linhas alteradas, só nos lotes f e g e só em `destino` e `motivo` (e no `id`, pela ordem dentro do lote). Os lotes a–e ficaram com zero linhas e zero `id` alterados. A diferença linha a linha está em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\DIFERENCA_4.4a_2026-11-05.csv`.
- **Arquivos novos durante a etapa (D27):** entre 16h25 e 16h26 entraram 2 arquivos em `CGOV_Processos\SEI_02070.023813_2026_17_Transicao\`: o PDF do processo e a Nota Técnica 14. O `--simular` não acusa arquivos fora do mapa. A diferença apareceu na contagem e foi confirmada contra o manifesto. Um novo `--planejar` incluiu o processo 74, `01_processos/SEI_02070.023813_2026-17_transicao/documentos-sei/` (lote d, +2 linhas), sem alterar nenhuma outra linha. Decisão D27: **pasta CGOV congelada** até o fim da Fase 4.
- **Mapa vigente** `C:\Projetos\cgov-geral\local\MAPA_REORGANIZACAO_2026-11.csv`: 2.860 linhas, SHA-256 `83db96e21d6146d2…`. Cobre 2.833/2.833 arquivos e 74 pastas de processo. Por lote: a 24 · b 109 · c 20 · d 1.131 · e 24 · f 965 · g 587. Por ação: mover 2.247, renomear 2, quarentena 587, criar 24. Maior destino: 253 caracteres. As versões anteriores estão em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\`.
- **Manifesto anterior refeito:** `C:\Projetos\cgov-geral\local\reorganizacao\manifesto_pre_2026-11.sha256` tem 2.833 linhas, SHA-256 `8847c5e87a0d5f69…`, com hashes recalculados do disco. São 2.833/2.833 iguais ao mapa, e nenhum dos 2.831 hashes da 4.3 mudou.
- **Simulação final** (`--simular --verificar-hash`, raiz de 45 caracteres): 2.860 operações, **zero conflitos** e **zero avisos de caminho longo**. O lote d tem 1.131 operações, sem conflitos. Registro em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\simulacao_final_2026-11-05.txt`.
- **Observação:** o shell do Cowork não apaga arquivos. O arquivo intermediário do manifesto foi movido para `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\manifesto_pre_2026-11.parcial_bruto.txt`.

**Preparação do lote (a) (05/11/2026).**
- **Pasta CGOV × manifesto:** SHA-256 recalculado do disco. São 2.833 = 2.833 arquivos, sem novos, sem ausentes e sem hash divergente. O congelamento (D27) está sendo respeitado.
- **Pastas:** 24 linhas `criar` do mapa vigente: a estrutura da Seção 5.2 e `99_arquivo/_a-excluir_2026-11-05`.
- **Documentos (D28):** o `reorganizar_cgov.py` só cria pastas, e a fonte `operacao/` estava prevista para a Fase 5 (5.3 e 5.5). A `operacao/` foi **antecipada** com 12 arquivos redigidos a partir dos Apêndices E e F: `LEIA-ME.md`, `AGENTS.md`, nove `_LEIA-ME.md` (00, 01, 02, 03, 04, 05, 06, 90 e 99) e `90_escritorio-virtual/modelos/processo/PROCESSO.md`. Nenhum desses nomes coincide com um destino do mapa. Eles serão copiados por um script PowerShell que não sobrescreve nada e confere o SHA-256 de cada cópia; o `publicar_operacao.py` da 5.3 assume depois.
- **Ajustes em relação aos Apêndices E e F:**
  - exemplos com número de processo fictício (`SEI_02070.000000_2026-00_exemplo`);
  - AGENTS.md, obrigação 1: criar as quatro subpastas e copiar `modelos/processo/PROCESSO.md`;
  - AGENTS.md, obrigação 6: sem o comando do plugin, que só existe na Fase 7;
  - AGENTS.md, nova regra 7: não inventar número de norma;
  - documentação em `90_escritorio-virtual/referencia/`;
  - `99_arquivo/_LEIA-ME.md` explica a quarentena e as pastas abreviadas pela D26.
- **Sanitização:** o `scripts/verificar_sanitizacao.py` (regra 4) ainda não existia; foi criado em 06/11, no bloco 1 da Fase 5. Até lá, a conferência da `operacao/` foi manual: sem nomes, e-mails, matrículas ou caminhos pessoais.

**Resultado do lote (a) (05/11/2026, 19h10).**
- **Execução:** feita pelo Coordenador. O registro `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_lote-a_20261105-191017.csv` tem 24 linhas, todas `ok`, e as 24 pastas existem.
- **Documentos:** os 12 documentos de `operacao/` estão na pasta CGOV com SHA-256 **idêntico** à fonte (*commit* `98789ef`).
- **Integridade:** a pasta tem 2.845 arquivos (2.833 + 12). Os 2.833 do manifesto estão todos presentes, com o mesmo SHA-256, e não há nenhum arquivo fora do manifesto e da `operacao/`.
- **Simulação de todos os lotes:** zero conflitos.

**Preparação do lote (b) (05/11/2026).**
- **Movimentações:** 109 `mover` (73,3 MB): 56 `.md` e 53 `.pdf`, sem renomear nada.
- **Origens:** 108 de `normative-sources` e 1 de `CGOV_Normativas` (Portaria ICMBio 1.258/2022).
- **Destinos:** 107 em `03_normativos` e 2 em `03_normativos/revogados` (PGE, Portaria 768/2020, revogada).
- **Nomes-base:** 59. Nove deles têm só PDF ou só `.md`, a completar na transcrição.
- **Caminhos:** o maior tem 168 caracteres.
- **Pastas de origem:** nenhuma fica vazia só pelo lote (b). Em `normative-sources` sobram 2 minutas, que vão para o processo 02070.001696/2026-31 no lote (d).
- **Efeito colateral:** a junção `C:\Projetos\cgov-geral\local\normative-sources` e as skills que leem `normative-sources` deixam de achar os normativos a partir do lote (b). Isso é aceitável enquanto a pasta está congelada (D27) e vai ser corrigido na Fase 5.1 (junções novas) e na Fase 6.
- ~~**Pendência:** as pastas antigas que ficarem vazias depois dos lotes não são removidas pelo script (ADR-014)~~. **Resolvida pela D29 (05/11):** remoção só das pastas vazias, com `--limpar-vazias`, depois do lote (g).

**Resultado do lote (b) (05/11/2026, 19h17).**
- **Execução:** feita pelo Coordenador. A simulação do lote com `--verificar-hash` deu zero conflitos. O registro `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_lote-b_20261105-191726.csv` tem 109 linhas, todas `ok`, e os `id` batem com o mapa.
- **Integridade:** recalculei o SHA-256 dos 2.845 arquivos na posição esperada, isto é, no destino para os lotes a e b e na origem para os demais. Nenhum ausente, nenhum extra e nenhum hash divergente.
- **O que sobrou:** em `normative-sources` ficam só as 2 minutas do lote (d).
- **Simulação de todos os lotes:** zero conflitos; as linhas já feitas aparecem como avisos de "já executada".

**Preparação do lote (c) (05/11/2026).**
- **Movimentações:** 20 `mover` (9,6 MB), com os nomes originais mantidos. O maior caminho tem 149 caracteres.
- **Destinos:** 11 vão para `02_notas-tecnicas/2025` e 9 para `02_notas-tecnicas/2026`.
- **Origens:** 19 vêm de `CGOV_Notas Técnicas`. A NT 27/2026 assinada vem de `analyses/_Impacto Regulatório_Plano de Manejo` (D11), e a NT 20/2026 foi para 2026 pela decisão do grupo 6 da 4.2.
- **O que fica em `CGOV_Notas Técnicas`:** 1 arquivo, que vai no lote (f).
- **Pendências para a 4.7:** ⚠️ padronizar os nomes da série para `NT_<nº>-<ano>_SEI_<nº documento>_<tema>.pdf` (Seção 5.4), registrar a série no `_INDICE.md` e decidir sobre a `NT_DINFI_01-2025`, que é de outra unidade e está na série da CGOV.

**Resultado do lote (c) (05/11/2026, 19h25).**
- **Execução:** a simulação com `--verificar-hash` deu zero conflitos. O registro `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_lote-c_20261105-192518.csv` tem 20 linhas, todas `ok`, e os `id` batem com o mapa.
- **Destinos:** 11 arquivos em `2025` e 9 em `2026`. Em `CGOV_Notas Técnicas` sobra 1 arquivo, que vai no lote (f).
- **Integridade:** os 2.845 arquivos estão íntegros por SHA-256 na posição esperada, e a simulação de todos os lotes dá zero conflitos.
- **Pendência:** ⚠️ a origem da "Nota Técnica 14" do processo 02070.023813/2026-17 (Transição) não foi informada; a mensagem trouxe o marcador do *prompt*. O arquivo vai para `documentos-sei` do processo (lote d), o que vale nos dois casos. Se for NT da CGOV, uma cópia entra na série na 4.7.

**Preparação do lote (d) (05/11/2026).**
- **Operações:** 1.131 (2.960,5 MB): 1.129 `mover` e 2 `renomear`, para 74 pastas de processo. Por subpasta: `referencias` 693, `documentos-sei` 240 e `trabalho` 198. O maior caminho tem 253 caracteres, em `referencias/indicadores/_Verificar` do processo 003032.
- **Origens:** `CGOV_Processos` 1.068, `analyses` 49, `CGOV_Administrativo` 8, `CGOV_Projetos` 3, `normative-sources` 2 e `CGOV_Normativas` 1. Dez processos juntam mais de uma origem, entre eles 006604 (D10), 020064 (grupo 1 da 4.2), 017019 (D11) e 001696 (D23).
- **Renomeações:** `SEI_022838998_Nota_Tecnica_3_2026 (1).pdf` → `…_v2.pdf` (processo 009510; conteúdo diferente do original) e `SEI_02070.000081_2020_00.pdf` → `…__origem-cgov-administrativo.pdf` (processo 000081; mesmo nome, conteúdo diferente).
- **Classificação por tipo:** 366 arquivos soltos foram classificados por heurística de tipo: 224 em `documentos-sei`, 88 em `referencias` e 54 em `trabalho`. A conferência fica para a revisão das fichas (4.7).
- **NTs em andamento:** os 5 `NT_ESTADO.md` (001696, 007589 e o backup dele, 020239, 023710) vão para `trabalho/`. Até a Fase 6, as skills `cgov-nt` continuam apontando para os caminhos antigos (ver risco das skills e junções).
- **Lista para revisão:** `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\LOTE_D_por_processo_2026-11-05.csv`.

**Resultado do lote (d) (05/11/2026, 19h29).**
- **Execução:** a simulação com `--verificar-hash` deu zero conflitos. O registro `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_lote-d_20261105-192947.csv` tem 1.131 linhas, todas `ok`, e os `id` batem com o mapa.
- **Destino:** `01_processos` tem 74 pastas de processo e 1.132 arquivos (1.131 + `_LEIA-ME.md`).
- **O que sobrou:** em `CGOV_Processos` ficam 4 arquivos (lotes f e g) e `normative-sources` ficou vazia.
- **Integridade:** os 2.845 arquivos estão íntegros por SHA-256 na posição esperada, e a simulação de todos os lotes dá zero conflitos.
- **Pastas vazias:** o script listou 96 pastas de origem que ficaram vazias (imprime só 20). A varredura completa achou **110 pastas-folha vazias**:
  - 11 na estrutura nova, aguardando os lotes e, f e g;
  - 99 antigas: `CGOV_Processos` 86, `_acervo-escritorio-virtual` 9, `CGOV_Administrativo` 3 e `normative-sources` 1. Entre elas estão as 3 pastas vazias que o mapa já manda para a quarentena no lote (g).
  - Lista completa em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\PASTAS_VAZIAS_pos-lote-d_2026-11-05.csv`. O destino delas fica para a pendência da 4.6.

**Preparação do lote (e) (05/11/2026).**
- **Operações:** 24 `mover` (86,6 MB). O maior caminho tem 149 caracteres.
- **Destinos:** `00_entrada` 2 (grupo 9 da 4.2) · `04_colegiados/cig` 1 · `04_colegiados/ctgric` 2 (o par `.docx`/`.gdoc` da raiz) · `05_projetos/2026-10_lancamento-ecoa` 6 · `05_projetos/2026-10_oficina-pgd-gr2-fortaleza` 3 · `05_projetos/fundo-rio-doce` 7 · `06_gestao-da-coordenacao` 2 · `06_gestao-da-coordenacao/plano-de-entregas` 1 (D15).
- **Pendência:** ⚠️ `05_projetos/fundo-rio-doce` não segue o padrão `AAAA-MM_apelido` da Seção 5.4. Ajustar na 4.7, junto com o `PROJETO.md`.

**Resultado do lote (e) (05/11/2026, 19h35).**
- **Execução:** a simulação com `--verificar-hash` deu zero conflitos. O registro `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_lote-e_20261105-193538.csv` tem 24 linhas, todas `ok`, e os `id` batem com o mapa.
- **Destinos:** `00_entrada` 3, `04_colegiados` 4, `05_projetos` 17 e `06_gestao-da-coordenacao` 4 arquivos, contando os `_LEIA-ME.md`. A raiz ficou só com `LEIA-ME.md` e `AGENTS.md`.
- **Pastas vazias:** mais 3 pastas de origem ficaram vazias (`CGOV_Fundo Rio Doce`, `20261013_Oficina PGD_GR2_Fortaleza` e `SEI__Reunioes-CIG`).
- **Integridade:** os 2.845 arquivos estão íntegros por SHA-256, e a simulação de todos os lotes dá zero conflitos.

**Preparação do lote (f) (05/11/2026).**
- **Operações:** 965 `mover` (64,7 MB). O maior caminho tem 246 caracteres, depois da D26.
- **Destinos em `90_escritorio-virtual` (456 arquivos):**
  - `transcricoes/` 441, com o trabalho intermediário de OCR em cinco rodadas;
  - `referencia/` 14, com a documentação publicada e o `LEIA-ME.md`;
  - `manutencao/PENDENCIAS.md` 1.
- **Destinos em `99_arquivo` (500 arquivos):**
  - `escritorio-virtual/transcr-bkp_20261006` 401 (D26);
  - `escritorio-virtual/dev-local_2026-11` e outros 90;
  - `versoes-anteriores` 8 (ECOA v1–v3, 2 normativos do grupo 2, 2 versões do Plano de Entregas CGGE e a NT 16/2025 "_Retirar");
  - `processos-encerrados/ADPF` 1 (D11).
- **Fora da pasta CGOV (D14):** 9 arquivos de `_doutorado` vão para `My Drive\_projetos\05_privado\_doutorado\`, com destino relativo `../../_projetos/…`. ⚠️ A simulação na máquina virtual do Cowork **não enxerga** esse destino, que fica fora da pasta vinculada. O que vale é a simulação no PowerShell do Coordenador, e a conferência dos 9 é feita por `Get-FileHash` contra o manifesto.
- **Depois do lote:** a pasta CGOV fica com 2.836 arquivos (2.845 − 9). Em `_acervo-escritorio-virtual` sobram 567 arquivos, todos para a quarentena (lote g).
- **Efeito colateral:** `PENDENCIAS.md` sai de `_acervo-escritorio-virtual/manutencao` e vai para `90_escritorio-virtual/manutencao`, e a junção `local\acervo-drive` deixa de achá-lo. Corrige-se na 5.1 (risco das skills e junções).

**Resultado do lote (f) (05/11/2026, 19h41).**
- **Execução:** `Test-Path` da pasta `_doutorado` em `_projetos` deu `False`, e o script a criou. A simulação com `--verificar-hash` no Windows deu zero conflitos. O registro `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_lote-f_20261105-194138.csv` tem 965 linhas, todas `ok`, e os `id` batem com o mapa.
- **Fora da pasta (D14):** os 9 arquivos de `_doutorado` estão em `My Drive\_projetos\05_privado\_doutorado\`, todos com SHA-256 igual ao do manifesto, conferido por `Get-FileHash`.
- **Contagens:** `90_escritorio-virtual` 458, `99_arquivo` 501, `_acervo-escritorio-virtual` 567 (restante) e 2.836 arquivos no total. O script listou 105 pastas de origem que ficaram vazias.
- **Integridade:** os 2.836 arquivos da pasta estão íntegros por SHA-256 na posição esperada.
- **Simulação geral na máquina virtual:** acusa as 9 linhas de `_doutorado` como "origem inexistente" porque o destino fora da pasta vinculada não é visível dali. É um falso positivo; o lote (g), simulado sozinho com `--verificar-hash`, dá zero conflitos.

**Preparação do lote (g) (05/11/2026).**
- **Itens:** 587 quarentenas, sendo 584 arquivos (338,2 MB) e 3 pastas vazias, todos para `99_arquivo/_a-excluir_2026-11-05/`. O maior caminho tem 242 caracteres.
- **Origens:** `analyses` 505 (487 páginas renderizadas, regeneráveis a partir do PDF), `_tmp` 62, `CGOV_Normativas` 13 (idênticos ao acervo), `CGOV_Processos` 6 e `CGOV_Administrativo` 1.
- **Depois do lote:** as 8 áreas antigas (`CGOV_Processos`, `CGOV_Administrativo`, `CGOV_Normativas`, `CGOV_Notas Técnicas`, `CGOV_Projetos`, `normative-sources`, `organizar` e `_acervo-escritorio-virtual`) ficam com **zero arquivos** e cerca de 346 pastas vazias. Levá-las para a quarentena criaria caminhos de até 336 caracteres, por causa das pastas de OCR do `_acervo`.
- **D29 — remover só as pastas vazias:** o `reorganizar_cgov.py` **v1.2.0** ganhou o modo `--limpar-vazias`. Ele confere que não resta nenhum arquivo nas áreas antigas, contando os ocultos, e para se houver algum. Depois remove só as pastas vazias, da mais funda para a mais rasa, com `os.rmdir`, que falha se a pasta tiver conteúdo, e usa o prefixo `\\?\` para os caminhos longos. Pede confirmação e grava `registro_limpeza-vazias_<data>.csv`.
  - Testado numa árvore sintética: removeu as 8 pastas vazias e preservou a estrutura nova; parou quando havia um arquivo oculto; cancelou quando a resposta não foi SIM.
  - O registro do teste foi movido para `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\TESTE_sintetico_registro_limpeza-vazias_20261105-224755.csv`.
  - A v1.1.0 foi guardada em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\reorganizar_cgov_v1.1.0.py`.

**Resultado do lote (g) (05/11/2026, 21h07).**
- **Execução:** a simulação com `--verificar-hash` deu zero conflitos. O registro `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_lote-g_20261105-210722.csv` tem 587 linhas, todas `ok`, e os `id` batem com o mapa.
- **Contagens:** a quarentena `99_arquivo/_a-excluir_2026-11-05` tem 584 arquivos. `99_arquivo` tem 1.085 e a pasta, 2.836 no total. As 8 áreas antigas ficaram **sem nenhum arquivo**. A raiz tem só `AGENTS.md` e `LEIA-ME.md` como arquivos.
- **Etapa 4.5 concluída:** foram 2.860 operações nos sete lotes, todas `ok`.

**Limpeza das pastas vazias (D29, 05/11/2026, 21h07).**
- **O que aconteceu:** o `--limpar-vazias` (v1.2.0) encontrou 343 pastas vazias nas 8 áreas. Parou na primeira, `_acervo-escritorio-virtual/archive/…/02070.020242_2025_88_Integra+/tmp/pdfs/integridade_review`, com `WinError 5 (Access is denied)`, e **não removeu nenhuma**. O registro é `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_limpeza-vazias_20261105-210738.csv`.
- **Causa provável:** a pasta está vazia. A limpeza rodou 16 segundos depois do lote (g), com o Google Drive para desktop ainda sincronizando as movimentações, e o Drive mantém pastas abertas enquanto sincroniza. Outra hipótese é o atributo "somente leitura" da pasta.
- **Correção, `reorganizar_cgov.py` v1.2.1:** em caso de `PermissionError`, tenta de novo até quatro vezes, com 2 segundos de intervalo, e tira o atributo "somente leitura". Não para mais na primeira falha: registra o aviso e segue. As pastas-mãe de uma pasta que falhou também ficam. O comando pode ser repetido.
  - Testado numa árvore sintética: uma pasta bloqueada foi mantida e as demais removidas; depois de liberada, a segunda rodada removeu o resto.
  - Os registros dos testes estão em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\TESTE_v1.2.1_*.csv`, e a v1.2.0 foi guardada em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\reorganizar_cgov_v1.2.0.py`.
- **Situação:** ✅ **concluída (05/11, 21h14).**
  - O diagnóstico mostrou a pasta com atributo `ReadOnly, Directory` e 0 itens, então a causa foi o atributo "somente leitura".
  - A v1.2.1 removeu **343/343** pastas: 338 na 2ª tentativa, depois de tirar o atributo, e 5 na 1ª. O registro é `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_limpeza-vazias_20261105-211437.csv`.
  - A raiz ficou só com as 9 áreas novas, mais `LEIA-ME.md` e `AGENTS.md`.
  - A pasta tem 2.836 arquivos, conferidos por SHA-256 contra o manifesto posterior.
  - As pastas vazias que restam são as previstas: `04_colegiados/conselho-governanca`, `04_colegiados/ctgd` e as 3 pastas vazias postas em quarentena.

**Resultado da 4.6 — manifesto posterior (05/11/2026).**
- **Manifesto:** `C:\Projetos\cgov-geral\local\reorganizacao\manifesto_pos_2026-11.sha256` tem 2.836 linhas, SHA-256 `b65b0518ef5d78ec…`, com hashes recalculados do disco (3,53 GB).
- **Conferência contra o manifesto anterior** (2.833 arquivos):
  - **2.824 no destino previsto com o mesmo SHA-256**;
  - 9 fora da pasta (`_doutorado`, D14), conferidos por `Get-FileHash` no lote (f);
  - **zero falhas**, ou seja, 100%.
- **Arquivos fora do mapa:** só os 12 documentos de `operacao/`, todos com SHA-256 igual à fonte.
- **Por área:** `01_processos` 1.132 · `99_arquivo` 1.085 · `90_escritorio-virtual` 458 · `03_normativos` 110 · `02_notas-tecnicas` 21 · `05_projetos` 17 · `04_colegiados` 4 · `06_gestao-da-coordenacao` 4 · `00_entrada` 3 · raiz 2.
- **Pendência:** ⚠️ copiar o mapa e os manifestos para `90_escritorio-virtual/manutencao/`, que é o destino final previsto na 4.1, quando terminar o congelamento (4.10).

**Resultado da 4.7 — fichas e índices (05/11/2026).**
- **Gerador:** `C:\Projetos\cgov-geral\scripts\gerar_indices.py` v0.1.0, previsto na Fase 5 e antecipado.
  - `--fichas` cria `PROCESSO.md` só onde não existe, e **nunca sobrescreve**.
  - `--indices` gera `_INDICE.md` em 01, 02, 03, 04 e 05.
  - `--saida` grava num rascunho, em vez de gravar direto na pasta.
  - O arquivo não tem caminhos pessoais.
- **O que as fichas preenchem com segurança:** número SEI, apelido, ano de abertura (pelo número SEI), pastas de origem, contagem por subpasta e o link para `trabalho/NT_ESTADO.md` quando houver NT em elaboração (4 processos).
- **O que ficou para revisão (⚠️):**
  - título: 58 deduzidos do nome de origem e 16 vazios (processos sem descrição no nome);
  - `inciso_art37`, `situacao`, `unidade_demandante`, data de abertura e `notas_tecnicas`;
  - Objeto e Andamento.
- **NTs candidatas:** são as NTs da série cujo número de documento SEI aparece nos arquivos do processo. Foram encontradas em 12 processos e ficam como **candidatas**, porque algumas são só referência. Por exemplo, as NTs do Plano Setorial aparecem também no processo da revisão do PGD.
- **Índices:**
  - 01: tabela dos 74 processos, a partir das fichas;
  - 02: série de 20 documentos, com número, documento SEI, tema e processo candidato;
  - 03: 58 normativos, dos quais 9 sem o par PDF/`.md`, com vigência "⚠️ verificar", salvo os de `revogados/`;
  - 04 e 05: listagens.
- **Publicação (D30):** feita pelo Claude, pelo shell do Cowork. Antes houve rascunho em `C:\Projetos\cgov-geral\local\reorganizacao\staging_4.7\`. A cópia não sobrescreveu nada e conferiu o SHA-256.
  - Resultado: **79/79 ok**, com registro em `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_publicacao-4.7_20261106-003327.csv`.
  - A pasta passou a ter 2.915 arquivos: os 2.836 do manifesto posterior, intactos, mais 74 fichas e 5 índices.
- **Pendências de conteúdo** (⚠️, revisão gradual pelo Coordenador e pelos servidores):
  - campos ⚠️ das 74 fichas;
  - nomes da série de NTs fora do padrão da Seção 5.4;
  - NT 06/2025 e NT 07/2025 com o **mesmo** número de documento SEI (022017872) no nome do arquivo;
  - NT DINFI 01/2025 na série da CGOV;
  - autoria da "Nota Técnica 14" do processo de Transição;
  - 9 normativos sem par PDF/`.md`;
  - vigência dos normativos;
  - nome `05_projetos/fundo-rio-doce` fora do padrão;
  - cópia do mapa e dos manifestos para `90_escritorio-virtual/manutencao/` (4.10).

**Preparação da 4.8 (05/11/2026).**
- **Revisão do Apêndice B (rascunho):** foram encontrados quatro problemas.
  - (i) Citava `/cgov-escritorio:nova-nt` e `/cgov-escritorio:registrar-pendencia` (plugin da Fase 7) e a skill `cgov-gestao-acervo` (Fase 6), que ainda não existem.
  - (ii) Retirava a tradução de caminhos antes da hora. As skills `cgov-nt-01` a `07` ainda gravam `NT_ESTADO.md` em `local/analyses/…`, e sem a tradução criariam uma pasta `local/` proibida pelo `AGENTS.md`.
  - (iii) Não listava as skills.
  - (iv) Não tratava dos `_INDICE.md`, que o projeto Operação não tem como regenerar, porque o `gerar_indices.py` está no repositório.
- **Versão final 1.0:** `C:\Projetos\cgov-geral\docs\system-instructions\escritorio-cgov-operacao.md`, também no Apêndice B.
  - Novas seções: "Antes de qualquer tarefa" (ler `LEIA-ME`, `AGENTS`, `_INDICE` e a ficha, sem tratar ⚠️ como fato), "Caminhos (transição até a Fase 6)" e "Skills".
  - 12 regras, com a NT assinada no padrão da Seção 5.4 e os índices regenerados por pendência.
  - Siglas, redação, LGPD e quarentena seguem a Seção 5 do `escritorio-cgov.md` anterior.
  - O `escritorio-cgov.md` anterior foi para `C:\Projetos\cgov-geral\archive\system-instructions\escritorio-cgov_ate-2026-11-05.md` (`git mv`).
- **Navegação v2 (D31):**
  - O `AGENTS.md` ganhou a tabela "Caminhos antigos citados pelas skills": `local/analyses/SEI_…/` → `01_processos/<processo>/trabalho/`; `local/normative-sources/` → `03_normativos/`; `local/acervo-drive/manutencao/PENDENCIAS.md` → `90_escritorio-virtual/manutencao/PENDENCIAS.md`; `docs/…` → `90_escritorio-virtual/referencia/docs/…`.
  - No `LEIA-ME.md`, o exemplo "Atualize os índices" virou "Atualize a ficha do processo <apelido>".
  - As versões publicadas na 4.5(a) foram para `99_arquivo/_a-excluir_2026-11-05/_navegacao-v1/`, com SHA-256 `082cf4a0…` e `70b37666…` iguais aos da publicação, e as novas foram copiadas da `operacao/` (`a49cc568…` e `f61d1043…`). Registro: `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_republicacao-navegacao_20261106-004330.csv`.
- **`reorganizar_cgov.py` v1.2.2:** a barra de progresso do `--limpar-vazias` foi feita pelo Coordenador às 21h26, depois do *commit* `c88bd3e`. O Claude só registrou a versão.
- **Pendências:**
  - ⚠️ a cópia de referência em `90_escritorio-virtual/referencia/docs/` é anterior e não tem o `escritorio-cgov-operacao.md`; é republicada na 5.3;
  - ⚠️ na Fase 6.3, com as skills em caminhos neutros, retirar a seção "Caminhos" das instruções e a tabela do `AGENTS.md`.

**Resultado da 4.8 (05/11/2026).**
- **Projeto criado:** o Coordenador criou o projeto "Escritório CGOV — Operação" no Claude Desktop, com a pasta `%USERPROFILE%\My Drive\10_Institucional\CGOV` e as instruções do Apêndice B v1.0.
- **Teste 1 (Plano Setorial):** ✅ o projeto achou `01_processos/SEI_02070.020239_2025-64_plano-setorial/` e avisou que a ficha está com campos ⚠️. Leu o estado em `trabalho/NT_ESTADO.md`: NT 31/2026, doc. SEI 024097708, inciso IX (principal), mais I e II, concluída em 24/08/2026. Apontou as pendências do estado e alertou que a NT 31 não está na série assinada, pedindo confirmação.
- **Teste 2 (triagem fictícia, processo 02070.000000/2026-00):** ✅
  - A `cgov-nt-01-triagem` enquadrou a demanda no inciso IV, conferindo o texto verificado em `03_normativos/`.
  - Criou `01_processos/SEI_02070.000000_2026-00_teste-implantacao/` com as quatro subpastas, `PROCESSO.md` e `trabalho/NT_ESTADO.md`, **sem criar `local/`, `analyses/` nem `_CGOV_NT/`**.
  - Não editou índices nem nada em `90_escritorio-virtual/`, além de registrar quatro pendências em `PENDENCIAS.md`.
  - Sinalizou com ⚠️ o que faltava, sem inventar artigos.
  - A conferência no disco confirmou: os 2.836 arquivos do manifesto posterior e as 79 fichas e índices estão intactos; mudaram só `PENDENCIAS.md`, `AGENTS.md` e `LEIA-ME.md`, como esperado.
- **Achado (deriva fonte × instalado):** a `cgov-nt-01-triagem` **instalada** manda gravar em `CGOV_Processos/<pasta>/_CGOV_NT/`, com pasta no padrão `SEI_<nº>_<ano>_<dv>_<APELIDO>`. A **fonte** no repositório diz `local/analyses/…`. O projeto aplicou o padrão novo por conta própria e registrou o fato. Isso confirma o risco "deriva fonte × instalado", e a correção vem na Fase 6.1.
- **Fechamento (D32):** registro em `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_fechamento-4.8_20261106-010058.csv`.
  - (i) A pasta de teste foi para `99_arquivo/_a-excluir_2026-11-05/_teste-4.8/`, com 2 arquivos conferidos por SHA-256.
  - (ii) O `AGENTS.md` v3 ganhou a linha `CGOV_Processos/<pasta>/_CGOV_NT/` → `01_processos/<pasta>/trabalho/`. A v2 foi para `_a-excluir_2026-11-05/_navegacao-v2/`, e a v3 foi publicada a partir da `operacao/` (`5aa7845e…`).
  - (iii) A pendência "regenerar índices" do teste foi marcada como resolvida, porque o índice nunca incluiu a pasta de teste.
- **Pendências registradas pelo projeto Operação, que ficam abertas:**
  - atualizar a skill de triagem (Fase 6);
  - o campo "Local deste arquivo" do `NT_ESTADO.md` do Plano Setorial e a fonte citada no texto verificado do Art. 37 ainda trazem caminhos antigos. Não são alterados na Fase 4 (regra 3): ficam para o projeto Operação e para a curadoria do acervo;
  - o Decreto nº 12.002/2024 e a LC nº 95/1998 não estão no `03_normativos`.
- **Git:** o `git add` do bloco da v3.20 citava `docs/system-instructions/escritorio-cgov.md`, que já tinha sido renomeado, e o Git recusou o `add` inteiro. O *commit* `d9c582e` levou só a renomeação. Plano, `operacao/`, instruções e script entram no *commit* da v3.21.

**Preparação da 4.9 (D33 — copiar e arquivar).** Base: o inventário da 3.C (`C:\Projetos\cgov-geral\local\archive\cowork-projetos\inventario.md`), com 11 projetos antigos, todos com vínculo já inexistente.
- Para cada projeto, o Coordenador cola as instruções no projeto Implantação, ou responde "vazio".
- Projetos de processo:
  - `02070.006604 2026-17_Política de Governança_v2` → seção "Instruções específicas" e campo `cowork_projeto` de `01_processos/SEI_02070.006604_2026-17_politica-governanca/PROCESSO.md`;
  - `02070.007589/2025-35_TCs` → idem, em `01_processos/SEI_02070.007589_2025-35_termos-compromisso/PROCESSO.md`.
- Projetos temáticos (`Sistema Integridade ICMBio`, `Painel Estratégico OCDE/ICMBio`, `CGGE_Estrutura`, `oficina-planejamento-GR2`, `pgd-icmbio`, `cgov-catalogo-entregas-icmbio`, `projeto-referencias` e `reorg-executor`) → `C:\Projetos\cgov-geral\local\archive\cowork-projetos\<projeto>_instrucoes_2026-11-05.md`. Se as instruções indicarem um processo ou um projeto de `05_projetos`, elas também vão para a ficha correspondente.
- `mba_cdia_enap`: fora do escopo institucional, sem ação.
- Depois de copiar, o Coordenador arquiva cada projeto no Claude Desktop. Aceite: nenhum projeto apontando para caminho inexistente.

**Resultado da 4.9 (06/11/2026).**
- **Projetos de processo:**
  - `02070.006604…_Política de Governança_v2` e `02070.007589/2025-35_TCs` não tinham instruções. As fichas dos dois processos receberam `cowork_projeto` e a nota em "Instruções específicas".
  - A ficha do 007589 aponta para `trabalho/Instrucoes_Gerais_CGOV_Analise_Atos_Normativos_v1.md`, documento que o Coordenador gerou a partir das 10 sessões daquele projeto (D34).
- **Projetos temáticos:**
  - Cinco tinham descrição ou instruções: `CGGE_Estrutura`, `oficina-planejamento-GR2`, `Painel Estratégico OCDE/ICMBio`, `projeto-referencias` e `reorg-executor`. O Coordenador salvou os textos em arquivos `resumo-*.md` na raiz do repositório.
  - Esses arquivos foram movidos para `C:\Projetos\cgov-geral\local\archive\cowork-projetos\<projeto>_instrucoes_2026-11-06.md`, com SHA-256 conferido. O texto do Painel OCDE também foi para a ficha de `SEI_02070.014637_2025-41_ocde-pgd`.
  - ⚠️ `oficina-planejamento-GR2` (09–10/09) não foi ligado a `05_projetos/2026-10_oficina-pgd-gr2-fortaleza` (13/10): confirmar se é o mesmo projeto.
  - `projeto-referencias` é pessoal (gestão bibliográfica): sugere-se guardá-lo também em `My Drive\20_Capacitacao\_biblioteca\`.
  - `Sistema Integridade ICMBio`, `pgd-icmbio` e `cgov-catalogo-entregas-icmbio` estavam vazios.
- **Fichas alteradas:** 3, com cópias anteriores em `C:\Projetos\cgov-geral\local\reorganizacao\conferencia\fichas_antes_4.9\`. O YAML foi validado. O resultado está no inventário (`C:\Projetos\cgov-geral\local\archive\cowork-projetos\inventario.md`).
- **Falta:** o Coordenador arquivar os 11 projetos no Claude Desktop (o `mba_cdia_enap` fica sem ação).

**Resultado da 4.9 e da 4.10 (06/11/2026).**
- **4.9:**
  - O Coordenador arquivou os projetos Cowork antigos e confirmou que `oficina-planejamento-GR2` é o mesmo projeto de `05_projetos/2026-10_oficina-pgd-gr2-fortaleza`.
  - Essa pasta ganhou um `PROJETO.md`, com a descrição herdada e os campos ⚠️ (período 09–10/09 contra arquivos de 13/10).
  - O inventário em `C:\Projetos\cgov-geral\local\archive\cowork-projetos\inventario.md` foi atualizado.
  - O `Rascunho.md` que tinha aparecido na raiz do repositório foi retirado pelo próprio Coordenador.
- **4.10:**
  - (i) Copiados para `90_escritorio-virtual/manutencao/reorganizacao-2026-11/`, com SHA-256 igual à fonte: o mapa vigente e o resumo dele, os manifestos anterior e posterior, `decisoes.csv`, `apelidos.csv` e 12 registros de execução. São 18 cópias, mais o `PROJETO.md` da GR2, todas `ok`. Registro: `C:\Projetos\cgov-geral\local\reorganizacao\registros\registro_4.10_20261106-114328.csv`. As fontes continuam em `local\`, de onde o `--reverter` lê.
  - (ii) O **§28 "Reorganização da pasta operacional CGOV"** foi acrescentado ao fim de `docs/governance/decision-log.md`, com contexto, 5 decisões, resultado, achados e pendências, sem caminhos pessoais. O §27 foi superado nos pontos que trata.
  - (iii) O Apêndice A passou para a **v2**, sem a pasta CGOV. O Coordenador colou o texto nas instruções do projeto Implantação e removeu a pasta CGOV do projeto.
- **Fim do congelamento (D27):** a pasta volta a receber trabalho pelo projeto Operação.
- **Efeito para a Fase 5:** o manifesto posterior deixa de descrever a pasta viva.
- **Pendente:** 4.11, a revisão e exclusão de `99_arquivo/_a-excluir_2026-11-05/` a partir de 05/12/2026, com confirmação (ADR-014).

**Resultado da Fase 4 (05–06/11/2026).**
- **Reorganização:** 2.860 operações em sete lotes, todas `ok`. O manifesto posterior encontrou 2.833/2.833 hashes no destino previsto. 343 pastas antigas vazias foram removidas.
- **Navegação:** 74 fichas e 5 índices, mais o `PROJETO.md` da GR2.
- **Operação:** projeto "Escritório CGOV — Operação" com as instruções do Apêndice B v1.0, testado. Projetos antigos arquivados. Decisões D22 a D34.
- **Scripts:** `reorganizar_cgov.py` v1.2.2 e `gerar_indices.py` v0.1.0.

**Atualização da documentação do repositório (06/11/2026, D36 — antecipação de partes da Fase 5).**
- **Pedido do Coordenador:** atualizar integralmente a documentação do repositório para a estrutura nova.
- **Levantamento:** busca por `_acervo-escritorio-virtual`, `normative-sources`, `local/analyses`, `escritorio-cgov.md`, `CGOV_Processos`, `cgov-geral-v1`, `acervo-drive` e WSL. Ficaram de fora:
  - `skills/` (Fase 6, com evals);
  - `archive/` e o histórico do decision-log, que não se reescrevem;
  - `docs/reports/RELATORIO_cgov-nt.md`, que é evidência histórica;
  - o plano.
- **Atualizados:**
  - `docs/fluxos-de-trabalho.md` reescrito (v2: dois projetos Cowork, estrutura da pasta CGOV, configuração no Windows, publicação de transição, fluxos e regras); a v1 foi para `archive/docs/fluxos-de-trabalho_ate-2026-11-06.md`;
  - `README.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `docs/architecture.md`, `docs/overview.md`, `docs/multiplatform.md`, `docs/references/normative-catalog.md` e `docs/system-instructions/analista-processos-sei.md`: caminhos, instruções do projeto Operação, local do `NT_ESTADO.md`, papéis de `operacao/` e `scripts/`;
  - `.env.example` para o Windows.
- **Novo:** `docs/governance/pendencias.md`, citado pelas instruções do projeto Implantação e que ainda não existia, com 6 pendências de alta prioridade (P1–P6), 6 de conteúdo (C1–C6) e 5 de evolução (E1–E5).
- **Segurança:** `scripts/publicar-operacao.sh` e `scripts/link-acervo.sh` **bloqueados**, porque publicariam ou ligariam a estrutura antiga e recriariam `_acervo-escritorio-virtual/`. O `--verificar`, que só lê, foi mantido. Sintaxe conferida com `bash -n`, e as duas recusas foram testadas.
- **Conferência:** as ocorrências que sobram fora de `skills/`, `archive/` e do decision-log são intencionais: a tabela de tradução, as notas de transição e as menções históricas. Não há caminhos pessoais nos arquivos alterados.

**Reversão:** o mesmo CSV permite desfazer (`reorganizar_cgov.py --reverter --lote X`), porque cada linha registra origem e destino.

---

### Fase 5 — Atualização do repositório de desenvolvimento — ✅ concluída (07/11/2026)

*Branch* `implantacao/fase-5` (D37), com um *commit* por bloco; *merge* e *push* só na 5.10, depois da revisão do diff. A D36 (documentação) já está no `main` (`53ec122`).

**Ordem de execução (D37, 06/11/2026).** A ordem numérica da tabela abaixo não é a de execução. O estado conferido em `53ec122` mostrou quatro dependências:
- `scripts/verificar_sanitizacao.py` não existe, e a regra 4 do Apêndice A o exige antes de todo *commit* que toque `docs/` ou `operacao/`;
- `.claude/settings.json` ainda bloqueia só as junções antigas, então as novas ficariam sem bloqueio de edição se a 5.1 viesse antes da 5.6;
- o `.env` real ainda tem as variáveis antigas (`CGOV_NORMATIVE_SOURCES`, `CGOV_ACERVO_DRIVE`, `CGOV_ANALYSES`, `CGOV_REFERENCIA`) e só o Coordenador o edita;
- `publicar_operacao.py` depende de `CGOV_RAIZ` e `CGOV_ESCRITORIO`.

Além disso, `.gitattributes` não existe; os arquivos rastreados estão em LF, com `core.autocrlf=false`.

| Bloco | Etapas | Executa | Aceite |
|---|---|---|---|
| 1 — Preparação | *Branch* `implantacao/fase-5`; `verificar_sanitizacao.py` (antecipado da 5.10; pendência E4) | Claude escreve; Coordenador cria o *branch* e roda o primeiro teste | O script aprova a árvore atual ou lista achados reais |
| 2 — Higiene do Git | 5.7 | Claude | `git status` sem ruído; `git ls-files --eol` inalterado |
| 3 — Junções protegidas | 5.6 → 5.1 → restante da 5.2 (o `.env` real é atualizado pelo Coordenador; as junções antigas são removidas com `rmdir` não recursivo, que tira só o ponteiro) | Claude escreve; Coordenador roda no PowerShell | Três junções listam conteúdo; teste de bloqueio; junções antigas ausentes |
| 4 — Publicação em Python | 5.3 só com `--verificar`; conferência da 5.5; restante da 5.8 (`.sh` para `archive/scripts-wsl/`); 5.4 marcada | Claude; Coordenador roda o `--verificar` | `--verificar` funciona no Windows |
| 5 — Documentação | 5.9 (ADRs em `docs/adr/`, `catalogo-skills.md`, `docs/README.md`; por último, o plano vai para `docs/plano-implantacao.md`, com as referências ajustadas) | Claude | Links internos válidos |
| 6 — Fechamento | 5.10 (sanitização, diff, *merge*, *push*, publicação real, que republica `docs/` uma única vez — P3) | Coordenador, com scripts prontos | `90_…\referencia\LEIA-ME.md` mostra o novo *commit* |

**Resultado do bloco 1 (06–07/11/2026) — ✅ concluído.** Teste no Windows (07/11): árvore inteira 0 erros e 25 avisos; `--staged` 0 erros nos 6 arquivos; *commit* `115b336`.
- *Branch* `implantacao/fase-5` criado pelo Coordenador; *commit* do plano v3.25 = `a2effef`.
- `scripts/verificar_sanitizacao.py` v0.1.1: só biblioteca padrão. O escopo é tudo o que pode entrar num *commit* (arquivos rastreados e não ignorados) ou, com `--staged`, só o conteúdo do índice.
  - **Erros** (bloqueiam): caminho pessoal, e-mail, CPF com dígito válido, matrícula/SIAPE, segredo, termo local, arquivo proibido (`.pdf`, Office, `.msg`, `.pbix`, `.env` etc.).
  - **Avisos**: processo SEI, documento SEI, telefone, unidade absoluta.
  - Termos pessoais só em `local/sanitizacao_termos.txt`, que é ignorado pelo Git; o usuário do sistema entra automaticamente.
  - Exceções versionadas em `scripts/sanitizacao_permitidos.txt`, sem dados pessoais (hoje, uma: o `H:\` histórico do decision-log); marcador de linha `sanitizacao:ok`.
- **Testes:** repositório descartável com 18 casos plantados. Detectou todos os positivos e ignorou os falsos (placeholder `<usuario>`, `C:\Projetos\cgov-geral`, `noreply@anthropic.com`, CPFs inválidos, marcador, exceção, `--staged`).
- **Primeira rodada na árvore (`a2effef`):** 11 erros, todos no plano (caminho com o usuário do Windows), e avisos de números SEI. A 0.1.1 corrigiu um falso positivo duplicado (`C:/Users/…` também casava com a regra Unix) e passou a ignorar os modelos zerados (`02070.000000/0000-00`) e as reticências usadas como nome (`C:/Users/…`).
- **D38:** caminhos trocados por `%USERPROFILE%` (no item 8.1, `C:/Users/<usuario>/`, porque o glob do `settings.local.json` não expande variáveis). Números SEI mantidos como aviso; os das evals da `cgov-nt-01` e da `cgov-nt-03` passam a fictícios na Fase 6 (pendência E6).
- **Rodada final:** 0 erros. Os avisos restantes são números SEI no plano, em `scripts/reorganizar_cgov.py` e nas duas evals, um documento SEI e duas menções a `H:\` no plano (item 6.2 e este resultado). `docs/`, `operacao/` e `skills/`: **APROVADO**.

**Resultado do bloco 2 (07/11/2026) — ✅ concluído** (*commit* `0d0c8d2`; `git add --renormalize .` na pasta do Coordenador não acrescentou nenhum arquivo além dos três previstos; sanitização 0 erros).
- **Estado anterior** (`115b336`): 78 arquivos em LF no índice e na árvore, nenhum CRLF; `core.autocrlf=false`; um único `.ps1` (`skills/thematic/cgov-transcrever-normativos/scripts/ocr_windows.ps1`); `/.obsidian/` já ignorado.
- **`.gitattributes` (novo):** `* text=auto eol=lf`; `*.ps1`, `*.bat` e `*.cmd` com `eol=crlf` na árvore (no índice continuam em LF); binários declarados (`*.png`, `*.jpg`, `*.jpeg`, `*.gif`, `*.ico`, `*.pdf`, `*.zip`, `*.docx`, `*.xlsx`, `*.pptx`, `*.pbix`, `*.abf`).
- **`.gitignore`:** acrescentados `/notas/`, `*.pbix`, `**/.pbi/cache.abf` e `paineis/**/dados/`.
- **Teste num clone descartável** (fora da pasta do Coordenador, para não tocar no índice):
  - `git add --renormalize .` não alterou nenhum dos 78 arquivos (índice: 78 `i/lf`); `git status` mostra só `.gitattributes` e `.gitignore`;
  - depois de um novo *checkout*, o `.ps1` fica `w/crlf` e `i/lf`, sem aparecer como modificado;
  - `git check-ignore` confirmou os quatro padrões novos, e um `.tmdl` de PBIP continua rastreável.
- **Sanitização:** os dois arquivos foram aprovados (0 erros, 0 avisos).
- **Observação:** na pasta do Coordenador, o `.ps1` continua em LF até o próximo *checkout* desse arquivo. Isso não causa ruído no `git status`.

**Resultado do bloco 3 (07/11/2026) — ✅ concluído** (*commit* `b6a1bd5`).
- **5.6 (`.claude/settings.json`):** bloqueios `Edit(/local/processos/**)`, `Edit(/local/normativos/**)`, `Edit(/local/escritorio/**)`, `Edit(~/My Drive/10_Institucional/CGOV/**)` e `Edit(/.env)`; os três antigos saíram.
  - **Base** ([documentação oficial de permissões do Claude Code](https://code.claude.com/docs/pt/permissions)):
    - `/caminho` é relativo à raiz do projeto;
    - as regras `Edit` valem para todas as ferramentas que editam arquivos;
    - a regra deny vale quando o link **ou** o alvo casam;
    - as regras não alcançam scripts Python ou Node, que abrem arquivos por conta própria.
  - **D39:** a regra com `~/` bloqueia a pasta CGOV também pelo caminho real, sem nome de usuário; isso antecipa a 8.1 sem `settings.local.json`.
- **5.1 (`scripts/link_acervo.py` v0.1.0):**
  - **Funcionamento:** sem `--executar`, só simula. Lê os alvos do `.env` (se a variável faltar, usa `CGOV_RAIZ` + subpasta). Cria as junções com `cmd /c mklink /J`, sem administrador. Remove as antigas só se forem junções (`os.rmdir`, que tira só o ponteiro). Para (`[PARE]`) se encontrar pasta real, arquivo, junção com outro alvo ou alvo inexistente. Por fim, confere as três junções novas (contagem de itens) e a ausência das antigas.
  - **Testes** num repositório falso, com links simbólicos: simulação sem alterar nada; execução (3 criadas, 3 antigas quebradas removidas, conferência ok); repetição sem efeito; os três casos de parada; conteúdo do alvo intacto.
- **5.2:** `.env.example` com `CGOV_PROCESSOS`, `CGOV_NORMATIVOS` e `CGOV_ESCRITORIO` ativas (caminhos completos, porque `gerar_indices.py` não expande variáveis). As variáveis antigas podem sair do `.env`: o `--verificar` do `publicar-operacao.sh` não lê o `.env`, e `reorganizar_cgov.py` só usa `CGOV_ACERVO_DRIVE` na falta de `CGOV_RAIZ`.
- **Documentação:** `CLAUDE.md`, `AGENTS.md` e `docs/fluxos-de-trabalho.md` (§3.1, itens 3 e 5) passam a citar `link_acervo.py` e os bloqueios novos.
- **Sanitização:** 0 erros (25 avisos já conhecidos).
- **Execução (Coordenador, 07/11):**
  - `.env` anterior guardado em `local\archive\env_ate-2026-11-07` e `.env` novo com as quatro variáveis;
  - `link_acervo.py --executar`: as junções `local\processos`, `local\normativos` e `local\escritorio` existem (criadas às 09:33) e as três antigas foram removidas, conferido pelo shell do Cowork, que não lê o conteúdo das junções;
  - teste de bloqueio feito no Claude Code, com resultado informado pelo Coordenador (sem saída colada);
  - *commit* `b6a1bd5`, com 7 arquivos e sanitização 0 erros. O plano v3.28 entrou antes, no *commit* `9f3849b` do Coordenador (revisão de estrutura e formatação, sem mudança de conteúdo).
- **Pendência P1:** resolvida.

**Resultado do bloco 4 (07/11/2026) — ✅ concluído** (*commit* `d94235e`, 11 arquivos, as duas renomeações a 100%, sanitização 0 erros).
- **`--verificar` no Windows:**
  1. skills: 5 iguais e 9 desatualizadas na conta (as 7 da `cgov-nt`, `cgov-gestao-riscos` e `cgov-regimento-interno`), o que confirma a pendência P4 com escopo maior que as "três desatualizadas desde 06/10" (achado A4); a reinstalação fica para a Fase 6.8;
  2. `operacao/`: 12/12 iguais ao publicado (aceite da 5.5);
  3. referência de `docs/`: publicada no *commit* `4960e11`, anterior à Fase 1 (5 iguais, 7 diferentes, 2 ausentes e 1 sobrando, o antigo `escritorio-cgov.md`), o que confirma P3.
- **Simulação de `--publicar`:** 14 pacotes; `operacao/` sem nada a publicar; referência com 15 arquivos (14 de `docs/` e o `LEIA-ME.md`), com a anterior para a quarentena de 07/11. Nada gravado.

**Preparação do bloco 4 (registro):**
- **5.3 (`scripts/publicar_operacao.py` v0.1.0):** substitui o `publicar-operacao.sh` e publica só o HEAD (alterações pendentes em `skills/`, `docs/` ou `operacao/` bloqueiam).
  - **Diferenças em relação ao `.sh`:** nada de `rsync --delete` nem `rm -rf`. O que for substituído na pasta CGOV vai para `99_arquivo/_a-excluir_<data>/publicacao_<commit>/`, e os pacotes ficam em `dist/skills/<commit>/`, sem apagar os anteriores.
  - **`--verificar`** (somente leitura): skills da conta (`~/.claude/skills/synced`) × fonte; `operacao/` × pasta CGOV, por SHA-256 (etapa 5.5); `docs/` × `90_escritorio-virtual/referencia/docs` (P3).
  - **`--publicar`:** simulação. **`--publicar --executar`:** pacotes, `operacao/`, referência com `LEIA-ME.md` (commit e URL `cgov-geral`) e conferência por SHA-256.
- **Testes** num clone descartável, com uma pasta CGOV falsa:
  - `--verificar` apontou 1 skill igual, 1 desatualizada, 1 arquivo de `operacao/` diferente, 1 ausente e a referência antiga;
  - a simulação não gravou nada;
  - a execução gravou 17 arquivos (17/17 conferidos), com 3 itens na quarentena;
  - o `--verificar` seguinte deu `operacao/` 12/12 e `docs/` 14/14 iguais;
  - a árvore com alteração pendente deu `[PARE]`, e a repetição não teve efeito;
  - os 14 pacotes de skills saíram sem `evals/` e com as subpastas (`scripts/`).
- **5.8 (restante):** `archive/scripts-wsl/README.md` criado. Referências aos `.sh` atualizadas em `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, `.gitignore`, `docs/fluxos-de-trabalho.md` (§4 reescrita; ⏳ revistos) e `docs/governance/pendencias.md` (P1 e P2 resolvidas; P3 para a 5.10). O `git mv` dos dois `.sh` fica com o Coordenador.
- **5.4:** marcada como concluída.
- **Sanitização:** 0 erros.

**Resultado do bloco 5 (07/11/2026) — ✅ concluído** (*commit* `4ab53c1`: 22 arquivos; plano renomeado com 96% de semelhança; sanitização 0 erros e 22 avisos).
- **D40:**
  - os 14 ADRs viram arquivo, cada um com o seu status;
  - ADR-004 (scripts em Python) e ADR-007 (separação de dados) passam a **Aceito**, porque já estão praticados na Fase 5;
  - o ADR-011 continua proposto até as evals da Fase 11.
- **`docs/adr/`:** `README.md` (índice e modelo) e 14 arquivos `ADR-NNN-<assunto>.md` (Contexto, Decisão, Consequências, Referências).
  - ADR-012 a 014: texto da Seção 4 sem mudança de conteúdo; o ADR-014 ganhou o Contexto (Seções 5.6 e 7).
  - Demais ADRs: contexto tirado dos achados A1–A8 e dos requisitos da Seção 3.1.
- **`docs/catalogo-skills.md`:** as 26 skills do inventário.
  - 14 com fonte, com a situação dada pelo `--verificar` de 07/11; 12 sem fonte, para a 6.2.
  - Inciso do Art. 37 e função de cada skill, tirados do *frontmatter*.
  - ⚠️ `cgge-fgbio-apresentacao` e `cgge-fgbio-plano-aula`, presentes na conta e fora do inventário, ficam para decisão na 6.1.
- **`docs/README.md`:** página inicial da documentação e do cofre de desenvolvimento (ADR-009), com "por onde começar", o mapa de `docs/` e as regras rápidas.
- **Novo caminho deste plano (`docs/plano-implantacao.md`):** referências ajustadas em `README.md`, `AGENTS.md`, `CLAUDE.md` e no Apêndice A; a pendência E3 foi encerrada.
- **Verificação:** links internos conferidos por script (considerando este arquivo já em `docs/`); sanitização 0 erros.

**Resultado do bloco 6 (07/11/2026) — ✅ concluído.**
- **Revisão do diff `main...implantacao/fase-5`:** 7 *commits* (`a2effef` a `4ab53c1`), 35 arquivos, +1.679/−111 linhas. O `main` local (`53ec122`) é ancestral do *branch*, então o *merge* não tem conflito. Conferido:
  - os 5 scripts compilam e o `settings.json` é JSON válido;
  - o diff não traz marcas `TODO`, `FIXME` nem de conflito;
  - sanitização da árvore: 0 erros, 26 avisos conhecidos (números SEI, D38);
  - links já conferidos no bloco 5.
- **Decisão 29** acrescentada ao final do decision-log: registro da Fase 5 (regra 6, só acréscimo).
- **D41:**
  - *merge* `--no-ff`, que cria um *commit* de fechamento da Fase 5;
  - `/.vscode/` no `.gitignore` (apareceu `.vscode/settings.json` com configuração local do VS Code);
  - o *branch* `implantacao/fase-5` fica só na máquina do Coordenador.
- **Execução (Coordenador, 07/11):**
  1. *commit* do preparo `ee3b239` no *branch*;
  2. `origin/main` conferido igual a `53ec122` antes do *merge*;
  3. *merge* `--no-ff` `e305404` (pais `53ec122` e `ee3b239`). A primeira tentativa parou no paginador do `git log --graph` antes do *push*; o *push* foi refeito com `git --no-pager` (script B2), e `main...origin/main` ficou sem diferença;
  4. `publicar_operacao.py --publicar` (simulação) e `--publicar --executar` no `main`:
     - 14 pacotes em `dist/skills/e305404/` (não enviados à conta; reinstalação na Fase 6.8);
     - `operacao/` sem nada a publicar;
     - referência de `docs/` substituída: 32 arquivos e o `LEIA-ME.md`, 33/33 conferidos por SHA-256;
     - a referência anterior (commit `4960e11`; 14 arquivos) foi para `99_arquivo/_a-excluir_2026-11-07/publicacao_e305404/referencia/`.
- **`--verificar` depois da publicação:**
  - `operacao/` 12/12 iguais;
  - `docs/` 32 iguais, 0 diferentes, 0 ausentes, 0 sobrando;
  - `LEIA-ME.md` da referência com o commit `e305404` (**aceite da 5.10**);
  - skills: 9 desatualizadas, como esperado (pendência P4, Fase 6).
- **Pendências:** P3 resolvida; nova P7 (quarentena da publicação, a revisar a partir de 07/12/2026).
- **Observação:** o *commit* desta atualização do plano (v3.32) altera `docs/` depois da publicação. A referência fica um *commit* atrás só em `plano-implantacao.md` e `governance/pendencias.md`, até a próxima publicação.

**Resultado da Fase 5 (07/11/2026) — ✅ concluída.**
- **Seis blocos em 8 *commits* no *branch*** (`a2effef` a `ee3b239`, mais o `9f3849b` de formatação), integrados pelo *merge* `e305404`.
- **Decisões:** D36 a D41; decision-log §29.
- **Entregas:**
  - `verificar_sanitizacao.py`, `link_acervo.py` e `publicar_operacao.py`;
  - `.gitattributes`;
  - junções novas e bloqueios testados;
  - `.sh` arquivados;
  - 14 ADRs (7 aceitos), catálogo de skills e `docs/README.md`;
  - plano em `docs/`;
  - referência de `docs/` republicada.
- **Encaminhado para a Fase 6:** deriva fonte × instalado em 9 skills (P4), caminhos literais nas skills (P5), números SEI reais nas evals (E6) e as 12 skills sem fonte.
- **Depois:** um último *commit* deste plano (Fase 5 ✅). Ele altera `docs/` depois da publicação, então a referência fica um *commit* atrás só neste arquivo até a próxima publicação.

| Etapa | Ação | Aceite | Situação |
|---|---|---|---|
| 5.1 | `scripts/link_acervo.py`: junções no Windows com os nomes novos (`local\processos`, `local\normativos`, `local\escritorio`) a partir do `.env`; remover as junções antigas (`analyses`, `normative-sources`, `acervo-drive`) | Três junções novas listam conteúdo | ✅ 07/11: `--executar` no Windows; junções novas criadas e antigas removidas (*commit* `b6a1bd5`) |
| 5.2 | `.env` e `.env.example` com as variáveis `CGOV_PROCESSOS`, `CGOV_NORMATIVOS`, `CGOV_ESCRITORIO`, `CGOV_RAIZ` (caminhos Windows) (**parcial, 06/11, D36:** `.env.example` reescrito para o Windows com `CGOV_RAIZ`; variáveis novas comentadas até a 5.1; modelo antigo em `archive/env.example_ate-2026-11-06`) | — | ✅ 07/11: `.env.example` ativo e `.env` real gravado pelo Coordenador (anterior em `local\archive\env_ate-2026-11-07`) |
| 5.3 | `scripts/publicar_operacao.py` (porte do `.sh`): plugin ou zips → conta; `docs/` → `90_…\referencia`; `operacao/` → raiz, `_LEIA-ME` e modelos; `LEIA-ME` da referência com a URL `cgov-geral`; verificação de instaladas | `--verificar` funciona no Windows | ✅ 07/11: `--verificar` no Windows (`d94235e`) e publicação real do `e305404` (33/33 conferidos) |
| 5.4 | `scripts/gerar_indices.py` (lê os frontmatters e gera os `_INDICE.md`) e `scripts/reorganizar_cgov.py` (já usado na Fase 4) versionados | — | ✅ versionados na Fase 4 (`gerar_indices.py` v0.1.0, `reorganizar_cgov.py` v1.2.2); conferido em 07/11 |
| 5.5 | Criar `operacao/` com as versões aprovadas de `LEIA-ME.md`, `AGENTS.md`, `_LEIA-ME.md` por área e modelos (Apêndices E e F). **Antecipada na 4.5(a) (D28) e revista na 4.8 (D31: navegação v2):** aqui, só conferir que `operacao/` é igual ao publicado e incluir o que faltar | Igual ao publicado no Drive | ✅ 07/11: `--verificar` no Windows: `operacao/` 12/12 igual ao publicado (SHA-256) |
| 5.6 | `.claude/settings.json`: atualizar os bloqueios de edição para `local/processos/**`, `local/normativos/**`, `local/escritorio/**` e `.env` | Teste de bloqueio | ✅ 07/11: gravado (D39) e teste de bloqueio feito pelo Coordenador no Claude Code (*commit* `b6a1bd5`) |
| 5.7 | `.gitignore` (`/.obsidian/`, `/notas/`, `*.pbix`, `**/.pbi/cache.abf`, `paineis/**/dados/`) e `.gitattributes` (`* text=auto eol=lf`, `*.ps1 text eol=crlf`) | `git status` sem ruído | ✅ 07/11, *commit* `0d0c8d2` |
| 5.8 | Corrigir fatos desatualizados (privado, `cgov-geral`, Windows, estrutura nova) em `README.md`, `CLAUDE.md`, `AGENTS.md`, `fluxos-de-trabalho.md`, `architecture.md`; remover ou renomear `cgov-geral-v1.code-workspace`; mover os `.sh` para `archive/scripts-wsl/` (**antecipada em 06/11, D36:** `README.md`, `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, `docs/fluxos-de-trabalho.md` (v2; v1 em `archive/docs/`), `architecture.md`, `overview.md`, `multiplatform.md`, catálogo normativo e `analista-processos-sei.md` atualizados; workspace já renomeado na v3.8; os `.sh` foram **bloqueados**, salvo `publicar-operacao.sh --verificar`, e a ida para `archive/scripts-wsl/` fica para depois dos substitutos em Python) | `grep` sem ocorrências fora do log e de `archive/` | ✅ 07/11: `.sh` movidos para `archive/scripts-wsl/` (*commit* `d94235e`); fora do log, de `archive/` e deste plano, nenhuma referência ativa aos `.sh` |
| 5.9 | `docs/`: ADRs, `catalogo-skills.md`, `governance/pendencias.md`, `docs/README.md` (índice do cofre); mover este plano para `docs/plano-implantacao.md`; Decisão 28 no log (**parcial, 06/11, D36:** `docs/governance/pendencias.md` criado; Decisão 28 registrada na 4.10) | Links internos válidos | ✅ 07/11 (*commit* `4ab53c1`): 105 links relativos válidos; plano em `docs/` (renomeação a 96%) |
| 5.10 | `verificar_sanitizacao.py`; revisão do diff; *merge*; *push* (com confirmação); `python scripts\publicar_operacao.py` | `90_…\referencia\LEIA-ME.md` mostra o novo *commit* | ✅ 07/11: diff revisado; *merge* `--no-ff` `e305404`; *push* conferido; publicação; `LEIA-ME.md` da referência com `e305404` |

---

### Fase 6 — Portfólio de skills — ✅ concluída (08/11/2026)

**Ordem de execução (D42, 07/11/2026).** As etapas mantêm a numeração, mas seguem esta ordem:
1. **6.1** (exportar e comparar): define o texto-base de cada skill antes de qualquer edição;
2. **decisões 6.6 (D4) + 6.9(a)** (as 6 questões da Parte B.5): mudam o que se edita depois (pasta `trabalho/`, tempo verbal, skill nova). Concluído em 07/11 (D4 e D44): o Coordenador copiou o arquivo-base para `local\pilots\`;
3. **6.2** (promover as 12 sem fonte; destino das 2 `cgge-fgbio-*`);
4. **6.3** (caminhos neutros), que já cobre a divergência "pasta `_CGOV_NT`" da 6.9(c);
5. **6.5** (descrições ≤ 950 caracteres e eval do *branch* antigo), depois da 6.3, que também mexe nas descrições;
6. **6.9(b)(c)(d)** (modelo geral de análise de atos normativos), junto com as ampliações da `cgov-nt-06` e da `cgov-modelar-fluxo` decididas na 6.10 (D45);
7. **6.4** (`cgov-gestao-acervo`, já com caminhos neutros) e a `cgov-triagem-processo-sei` (D4);
8. **6.10** (quatro skills novas, D45) — ✅ concluída em 07/11 (D53);
9. **6.7** (OCR no Windows), em qualquer intervalo;
10. **6.8** (evals, *commit*, publicação, reinstalação, `--verificar` = 0). A 6.9(e) (piloto) fica na Fase 11.

**Resultado da 6.1 (07/11/2026) — ✅ concluída.**
- **Método (D42):** cópia do retrato da conta recebido pela sessão do Cowork (07/11, 10:33) para `local/installed-reference/_export_2026-11-07/` (fora do Git), com `MANIFESTO.md`. Conferência cruzada no PowerShell do Coordenador contra `%USERPROFILE%\.claude\skills\synced\`: 39/39 arquivos iguais. A conta reescreve o *frontmatter*, por isso a comparação usa a normalização de `publicar_operacao.py` (nome, descrição, corpo), não só o SHA-256.
- **Exportadas:** 28 skills (as 26 do inventário + `cgge-fgbio-apresentacao` e `cgge-fgbio-plano-aula`, cujo destino se decide na 6.2).
- **Comparação** (`COMPARACAO.md` e `diffs/`):
  - 14 com fonte: 5 iguais; 9 diferentes (confirma P4);
  - 12 sem fonte × `installed-reference`: 9 iguais; 3 mudaram na conta (`cgov-avaliar-entrega`, `cgov-elaborar-entrega`, `cgov-registro-execucao`: correção de trimestre para quadrimestre, de 14/09/2026);
  - auxiliares: nenhum faltando; `evals/` só na fonte (esperado); `catalogo_indicadores.md` difere só por uma linha em branco final.
- **Decisões (D43):**
  - suíte `cgov-nt` (7): base = **fonte**, aproveitando da conta a busca do `NT_ESTADO.md` em ordem e o aviso de local legado, em forma neutra na 6.3 (as duas convenções, `local/analyses/` e `_CGOV_NT/`, estão superadas pela `01_processos/…/trabalho/`);
  - `cgov-gestao-riscos`: base = **conta** (reescrita com os Regimes A — Portaria nº 975/2021 — e B — minutas RADAR), **saneada**: números de documentos SEI trocados por referência genérica às minutas; descrição recomposta na 6.5; os 5 ajustes da 6.9(c) sobre esta versão;
  - `cgov-regimento-interno`: base = **fonte** (a conta ainda cita `REGISTRO_DECISOES.md`);
  - `cgov-avaliar-entrega`, `cgov-elaborar-entrega` e `cgov-registro-execucao`: promovidas na 6.2 a partir da **conta**, com a nota de correção incorporada como regra no corpo e o histórico no decision-log.
- **Registro:** decision-log §30.

**Bloco de decisões 6.6 + 6.9(a) (07/11/2026) — ✅ concluído.**
- **6.6 (D4):** criar a skill `cgov-triagem-processo-sei` e manter `docs/system-instructions/analista-processos-sei.md` autocontido, para assistentes sem acesso a arquivos.
- **6.9(a) (D44):** AIR Nível 2 padrão; competências e legística obrigatórias (cinco subsídios obrigatórios, com dispensa só pelo Coordenador); foco decidido por projeto, na triagem; dispositivos propostos no futuro do presente (Decreto nº 12.002/2024, art. 11, I, "e", conferido no texto da Câmara dos Deputados: presente ou futuro, com uniformidade); residual em lacuna vai para a classe superior; `trabalho/` com texto neutro.
- **Efeitos nas etapas seguintes:** a divergência B.4-3 se resolve na `cgov-saneamento-legistica` (e não na `nt-03`); a Parte A do modelo muda nos itens 2 (foco), 3 e 10 (cinco obrigatórios) e 7 (tempo verbal) na consolidação da 6.9(d).
- **Registro:** decision-log §31.

**Análise da pasta de prompts e nova etapa 6.10 (07/11/2026, D45).** A pedido do Coordenador, a pasta `%USERPROFILE%\My Drive\_projetos\02_dev-prompts\` foi lida (somente leitura) e comparada com as 28 skills exportadas, com as previstas e com o Art. 37 da Portaria ICMBio nº 5.592/2025.
- **Novas skills (etapa 6.10):**
  - `cgov-secretaria-colegiados`: atas a partir da transcrição, pautas e encaminhamentos com prazo (CTGRIC, Portaria ICMBio nº 4.007/2023; Conselho de Governança e demais colegiados da pasta `04_colegiados`). Base: os 4 prompts de atas do CTGRIC e o comando `GERAR_ATA` de dois assistentes;
  - `cgov-integridade`: Programa e Plano de Integridade, SITAI, Integra+ (PGRI, Portaria nº 255/2020), separada da `cgov-gestao-riscos`. Base: Analista v4.7 (Integridade), `CTGRIC_Plano Integridade_v2`, NT do SITAI;
  - `cgov-carta-servicos`: Carta de Serviços ao Usuário (Lei nº 13.460/2017), com o script de classificação das entregas do PETRVS (sem dados de conexão). Base: NT 001/2026 e o script de `_temp\Análise Carta de Serviços_v1\`;
  - `cgov-projetos-cooperacao`: TdR, Nota Informativa e alinhamento ao POA em projetos de cooperação (genérica; primeiro caso, GIZ). Base: instruções "Analista de Projetos GIZ" v1.0.
- **Ampliações (com a 6.9(b)):** `cgov-nt-06-quesitos-pfe` ganha o modo de consulta jurídica facultativa e a NT de subsídio (impacto orçamentário, não sobreposição de colegiados) — ⚠️ conferir a Portaria Conjunta nº 3/2021 antes; `cgov-modelar-fluxo` ganha o modo inverso, BPMN → tabela de executores, atividades e objetos (POP).
- **Escopo da `cgov-triagem-processo-sei` (D4):** só a CGOV (Art. 37); as instruções "Analista CGGE" v3.0 servem de referência, e demandas do Art. 36 são sinalizadas e encaminhadas.
- **Adiado:** skill da Política de Governança Institucional (Art. 37, p.u., II; Portaria ICMBio nº 4.101/2023), pendência E7.
- **Descartado:** Microsoft Teams (VOA); Relatório de Gestão, Transparência Ativa e LGPD (um prompt cada); Dev gov.br (projeto de software); prompts acadêmicos e pessoais.
- **Cuidados:** os prompts citam o RI antigo (Art. 50) e têm números SEI e caminhos pessoais; as normas são conferidas no acervo, e o texto passa por `verificar_sanitizacao.py`.
- **Registro:** decision-log §32.

**Resultado da 6.2 (07/11/2026) — ✅ concluída.**
- **Estrutura (D46):** `skills/pgd/` (8: `pgd-especialista`, `pgd-elaborar-entrega`, `pgd-registro-execucao`, `pgd-avaliar-entrega` e as quatro `pgd-*-indicador`, nomes dados pela D47; na conta, ainda `cgge-especialista-pgd`, `cgov-elaborar-entrega`, `cgov-registro-execucao`, `cgov-avaliar-entrega` e `cgov-pgd-*-indicador`), `skills/normativo/` (4: `cgov-auditoria-competencias`, `cgov-comparar-versoes`, `cgov-modelar-fluxo`, `cgov-saneamento-legistica`) e `skills/cgge-fgbio/` (2, versionadas **fora** do plugin `cgov-escritorio`). São 22 arquivos copiados da exportação `_export_2026-11-07`, depois de preparados em `local/pilots/6.2_promocao/`.
- **Saneamento:**
  - nomes de 5 servidores da equipe na `cgov-elaborar-entrega` trocados por `[Responsável n]`, com a lista da equipe na pasta CGOV (pendência C7);
  - um nome de servidor num exemplo da descrição da `cgov-registro-execucao` trocado por `[servidor]`;
  - e-mail pessoal e caminhos `/home/…` de exemplo da `cgov-pgd-implementar-indicador` trocados por marcadores;
  - CPF de exemplo da `cgov-pgd-testar-indicador` trocado por `000.000.000-00`;
  - caminho absoluto da unidade H: (pasta do PGD) nas três skills de entregas trocado por "pasta de trabalho do PGD (caminho no `AGENTS.md`)" (o mapeamento entra na 6.3, P5);
  - número do processo de referência do PSPEADBio retirado das três skills normativas (o contexto padrão sai na 6.9(c));
  - nas `cgge-fgbio-*`, nomes do docente e dos convidados trocados por papéis (`[Docente responsável]`, `[Convidado 1]` …); os dados da turma ficam na exportação, em `local/`.
- **Ciclo quadrimestral (D43):** a nota de correção das três skills de entregas virou a seção "Ciclo do Plano de Entregas (quadrimestral)", sem o histórico (registrado no decision-log §30).
- **Configuração e documentação:** `.claude/settings.json` com as 14 novas em `skillOverrides` (28 no total); `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, `docs/architecture.md` e `docs/catalogo-skills.md` com as famílias novas.
- **Verificação:** `verificar_sanitizacao.py` na árvore: 0 erros (os 26 avisos anteriores); *frontmatter* (`name`, `description`) válido nas 14. A primeira varredura do `skills/` acusou o CPF e os caminhos absolutos da unidade H:, que a busca manual na exportação não pegou: corrigidos antes do *commit*.
- **Renomeação (D47, pedido do Coordenador):** as 8 skills do PGD passam a usar o prefixo `pgd-`, nas pastas, no `name:`, nas referências cruzadas (inclusive `cgov-pgr` e `cgov-gestao-riscos`, que passam a precisar de reinstalação), no `skillOverrides` e na documentação atual. O decision-log e os relatórios antigos ficam com os nomes antigos, como histórico. As instruções do projeto Operação (`docs/system-instructions/escritorio-cgov-operacao.md`, Apêndice B) e `analista-processos-sei.md` mudam só na 6.8, quando a conta receber os nomes novos.
- **Encaminhado:** descrições acima de 950 caracteres (`pgd-especialista`, 1.020; `cgge-fgbio-apresentacao`, 955; `cgov-modelar-fluxo`, 978) na 6.5; reinstalação na 6.8 das que mudaram (agora as 8 do PGD, as 3 normativas, as 2 `cgge-fgbio-*`, a `cgov-pgr` e a `cgov-gestao-riscos`); espelho `.agents/skills/` da Antigravity na Fase 8.

**Resultado da 6.3 (07/11/2026) — ✅ concluída.**
- **Skills (13 arquivos):** as 7 `cgov-nt-*` (descrições, parágrafo "Localização do `NT_ESTADO.md`" com a busca em ordem e o aviso de local antigo da D43, e na `cgov-nt-01` a criação da pasta pela obrigação 1 do `AGENTS.md`); `cgov-pgr` e `cgov-qcf` (normas localizadas no acervo normativo pelo número, não pelo nome do arquivo); `cgov-cadeia-valor` e `cgov-regimento-interno` ("registro de decisões"); `cgov-transcrever-normativos` e o `trigger_eval.json` (acervo normativo, pasta de rascunhos da transcrição, `scripts/` relativos à pasta da skill, regra de Git condicional).
- **Papéis e caminhos (D48):** `AGENTS.md` do repositório com a seção "Caminhos por papel" (desenvolvimento: `local/pilots/`, `local/processos/` e `local/normativos/` somente leitura, decision-log); `operacao/AGENTS.md` com cinco papéis novos: pasta de rascunhos da transcrição (`03_normativos/_transcricao/<data-hora>-<slug>/`), pasta de trabalho do PGD (`06_gestao-da-coordenacao/pgd/`), lista da equipe (`06_gestao-da-coordenacao/equipe.md`), registro de decisões (`PROCESSO.md`, Andamento) e pasta de processos; `_LEIA-ME.md` de `03_normativos` e `06_gestao-da-coordenacao` atualizados.
- **`gerar_indices.py` v0.1.1:** o índice do acervo normativo pula pastas iniciadas por `_` (testado numa árvore sintética: o rascunho de `_transcricao/` ficou fora do `_INDICE.md`).
- **Aceite:** busca por `local/analyses` e `_acervo-escritorio-virtual` em `skills/` = 0 (também 0 de `normative-sources`, `_CGOV_NT` e `CGOV_Processos`); *frontmatter* válido; `verificar_sanitizacao.py` 0 erros.
- **ADR-006 aceito** (D48). A tabela de caminhos antigos do `operacao/AGENTS.md` fica, depois da 6.8, como "Locais antigos".
- **Encaminhado:** publicação do `operacao/` depois do *commit* (`publicar_operacao.py`); reinstalação das 13 skills alteradas na 6.8 (P4).
- **Registro:** decision-log §35.

**Resultado da 6.5 (07/11/2026) — ✅ concluída.**
- **Descrições (D49):** 8 acima de 950 caracteres encurtadas, com o corpo intacto: `pgd-especialista` (1.020 → 775), `cgov-gestao-riscos` (1.006 → 878), `cgov-pgr` (1.000 → 842), `cgov-regimento-interno` (989 → 876), `cgov-modelar-fluxo` (978 → 710), `cgov-air-arr` (970 → 806), `cgov-cadeia-valor` (959 → 816) e `cgge-fgbio-apresentacao` (955 → 770). Agora as 28 têm ≤ 950. No `pgd-especialista`, o gatilho genérico (AIR, riscos, cadeia de valor…) passou a valer só no contexto do PGD da CGGE.
- **`cgov-gestao-riscos` (D43, pendente desde a 6.1):** a fonte (395 linhas, só o Regime A) foi substituída pela versão da conta (660 linhas, Regimes A e B), saneada: 3 números de documentos SEI trocados por "Minuta da Política"/"Minuta da nova Metodologia" (o número é buscado na ficha ou na pasta de trabalho do processo); 2 caminhos `CGOV/normative-sources/…` trocados pela pasta de trabalho do processo da Política de Gestão de Riscos (D23); `pgd-especialista`. Os 5 ajustes de conteúdo continuam na 6.9(c).
- ***Branch* antigo:** o `eval_set.json` (20 consultas) virou `skills/cgov-nt/cgov-nt-01-triagem/evals/trigger_eval.json`, com 6 números SEI trocados por `00000.000000/0000-00` e 5 rótulos corrigidos para "não aciona" (#10 riscos, #11 competências, #15 AIR, #16 SIPOC, #17 conclusão), ficando 10/10; `loop_results/` entrou no `.gitignore` (o `/.claude/` do *branch* não entrou, porque `.claude/settings.json` é versionado). O *branch* remoto é apagado pelo Coordenador.
- **Verificação:** *frontmatter* válido; corpo das 7 skills com fonte idêntico; `verificar_sanitizacao.py` 0 erros; busca por caminhos e nomes antigos em `skills/` = 0 (salvo uma menção histórica a `cgov-pgd-sk7`).
- **Encaminhado:** a otimização das descrições com o *loop* do `skill-creator` (usando os `trigger_eval.json`) fica para a 6.8; reinstalação na 6.8.
- **Registro:** decision-log §36.

**Resultado da 6.9(b)–(d) (07/11/2026) — ✅ concluídas.**
- **(b) Roteiro (D44, D50):** a `cgov-nt-01` ganhou duas perguntas na Fase 1 (foco da análise; norma substituída ou versões em disputa) e o **Passo 3.2**, com os cinco subsídios obrigatórios em análise de ato normativo (fluxos, competências, legística, riscos e AIR, com o Nível 1 sempre e o Nível 2 como padrão), dispensáveis só pelo Coordenador, com registro em "Decisões do projeto" (seção nova do `NT_ESTADO.md`). Ficha, roteiro do `NT_ESTADO.md` e encadeamento atualizados. Capítulos: metodologia com os subsídios realizados (`nt-03`); ordem do Capítulo 2 e regras do Quadro Consolidado com 5 eixos (`nt-04`); quadro Riscos × Recomendações e recomendação sobre as vias do Decreto nº 10.411/2020 (`nt-05`); síntese com riscos e AIR (`nt-07`).
- **(c) As 8 divergências da Parte B.4:** (1) roteiro, pelo Passo 3.2; (2) pasta `_CGOV_NT`, já na 6.3; (3) tempo verbal: na `nt-03`, futuro do presente como **convenção da CGOV** (o texto atribuía a regra ao Decreto nº 12.002/2024, que só exige uniformidade, art. 11, I, "e"); na `cgov-saneamento-legistica`, uniformidade e texto saneado no futuro do presente; (4) cabeçalhos `nt-03` × `nt-07` descritos pelo mesmo modelo; (5) a `nt-05` lê o Quadro Consolidado no produto do Cap. 2-3; (6) `cgov-gestao-riscos`, nova seção 3.9 (objeto, Teste de Integridade, controles — sem evidência, até Mediano no Regime A e Fraco no B —, Categoria Legal, limites e cenários) e residual entre 2 e 3 na regra da lacuna; (7) contexto PSPEADBio, que vira exemplo nas 4 skills normativas; (8) convenção de códigos na `nt-03`, aplicada nas skills.
- **Ampliações (D45):** `cgov-nt-06`, Modo 2 (consulta jurídica facultativa e NT de subsídio); `cgov-air-arr`, seção de uso como subsídio (Níveis 1 e 2); `cgov-modelar-fluxo`, regras de subsídio e Modo 2 (BPMN → tabela de atividades/POP). A Portaria Conjunta nº 3, de 13/05/2021 (consultas jurídicas à PFE), teve a existência e a ementa confirmadas no boletim do DOU de 20/05/2021; o texto dos artigos e anexos não foi obtido (DOU bloqueado), e a skill manda conferi-lo no acervo antes de citar (⚠️, C3).
- **(d) Publicação:** `docs/procedimentos/analise-atos-normativos.md` (v2: Parte A consolidada com a D44 e Parte B saneada) e `operacao/90_escritorio-virtual/modelos/analise-ato-normativo/INSTRUCOES-PROJETO.md` (bloco para copiar), sem caminho pessoal nem número SEI.
- **Pasta de rascunhos da transcrição (D50, corrige a D48):** passa a ser `90_escritorio-virtual/transcricoes/`, que já constava do `_LEIA-ME.md` da área 90; a obrigação 3 do `operacao/AGENTS.md` ganhou essa exceção; o `_LEIA-ME.md` de `03_normativos` foi ajustado. O filtro de pastas `_` do `gerar_indices.py` v0.1.1 continua.
- **Pendentes (⚠️):** inciso do Art. 37 para competências e legística (decidir no piloto); texto da Portaria Conjunta nº 3/2021 no acervo.
- **Verificação:** *frontmatter* válido nas 28 (descrições ≤ 950); `verificar_sanitizacao.py` 0 erros.
- **Registro:** decision-log §37.

**Resultado da 6.4 e da skill da 6.6 (07/11/2026) — ✅ concluídas.**
- **Família nova `skills/escritorio/` (D51):** skills de operação do Escritório, fora dos incisos do Art. 37.
- **`cgov-gestao-acervo`:** regras gerais (ler `LEIA-ME.md` e `AGENTS.md`; nunca excluir nem sobrescrever; lote só com lista e confirmação; SHA-256; sem dados pessoais; ⚠️ no que não for confirmado) e 5 modos: TRIAR_ENTRADA, NOVO_PROCESSO, ATUALIZAR_FICHA, ATUALIZAR_INDICES e ARQUIVAR. 5 casos sintéticos em `evals/evals.json`.
- **Índices na operação (D51):** `scripts/publicar_operacao.py` v0.2.0 publica `scripts/gerar_indices.py` em `90_escritorio-virtual/ferramentas/` (fonte única no repositório, conferida por SHA-256); a skill o executa, primeiro com `--saida`; `operacao/AGENTS.md` ganhou o papel "Ferramentas do Escritório" e o `_LEIA-ME.md` da área 90 cita `ferramentas/`. O `--fichas` nunca sobrescreve uma ficha existente.
- **`cgov-triagem-processo-sei` (D4, D45):** roteamento atualizado (nomes `pgd-*`, Passo 3.2 da `nt-01`, skills novas), passos 0–7, padrão de redação, guardrails e protocolo de incerteza, a partir do `analista-processos-sei.md` v7.2, que continua autocontido; escopo só do Art. 37, com sinalização do Art. 36; base normativa não copiada: `references/pilares-normativos.md` lista só os nomes das normas por pilar, e `references/formatos-de-saida.md` traz os 8 comandos. 3 casos sintéticos.
- **Pendente (⚠️):** as transcrições da Portaria ICMBio nº 129/2020 (atos normativos do ICMBio) e da Portaria Conjunta nº 3/2021, feitas pelo Coordenador em 07/11/2026 na pasta CGOV, ainda não foram lidas; a skill manda conferir a relação da 129/2020 com a Portaria nº 271/2013 antes de citá-las (afeta também a `cgov-nt-06` e o `analista-processos-sei.md`; pendência E8).
- **Configuração e documentação:** `skillOverrides` com 30; `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, `docs/architecture.md` e catálogo com a família nova.
- **Verificação:** *frontmatter* válido; `publicar_operacao.py` analisado sem erro de sintaxe; `verificar_sanitizacao.py` 0 erros.
- **Registro:** decision-log §38.

**Pendência E8 — normas sobre atos administrativos (07/11/2026) — ✅ resolvida (D52).** Com a pasta CGOV vinculada de novo (só `03_normativos`, leitura), foram lidas a Portaria ICMBio nº 271/2013 (o arquivo do acervo tem a data errada no nome: é de 27/12/2013), a Portaria ICMBio nº 129/2020 e o arquivo "Portaria Conjunta ICMBio PFE 03-2021".
- **Achados:** (1) o arquivo "Conjunta" é a **Portaria PFE/ICMBio nº 3, de 26/05/2021**, que aprova a OJN nº 27/2021 (juntada do aviso de recebimento na comunicação postal), e não trata de consultas jurídicas; a Portaria Conjunta nº 3, de 13/05/2021, sobre consultas à PFE, **não está no acervo**; (2) a nº 271/2013 fundamenta a consulta jurídica (Anexo I, art. 8º), os documentos da proposta (art. 7º, § 2º) e a declaração de impacto orçamentário (art. 7º, §§ 3º e 4º); (3) a nº 129/2020 define as espécies de ato normativo desde 02/03/2020 (Portarias, Resoluções e INs; art. 2º), a vigência em data certa (art. 10), a atuação da PFE (arts. 5º e 7º) e os documentos da proposta pelo SEI (art. 13), e não revoga expressamente a nº 271/2013.
- **Decisão (D52):** a nº 129/2020 prevalece onde as duas colidem (espécies e vigência); a nº 271/2013 vale no resto, com ⚠️ sobre a vigência residual, a confirmar com a PFE.
- **Correções (13 arquivos):** `cgov-nt-06` (Modo 2 sobre a nº 271/2013 e a nº 129/2020; consulta jurídica pelo art. 8º; impacto orçamentário; quadro comparativo); `cgov-saneamento-legistica` (espécie e cláusula de vigência); `cgov-air-arr`, `cgov-comparar-versoes` e `cgov-nt-01` (espécies e normas); `cgov-triagem-processo-sei` (Passo 4, pilares, checklist com os itens 11 e 12); `analista-processos-sei.md` v7.3 (Seção 5.6, Passo 4, checklist, changelog 10.6); `analista-governanca-anexo-normativo.md` e `-anexo-funcoes.md`; procedimento e modelo de instruções (espécie e vigência).
- **Curadoria do acervo (C8, pela operação):** renomear o arquivo da nº 271/2013 (data e tema) e o da Portaria PFE/ICMBio nº 3/2021 (não é conjunta; tema OJN nº 27/2021), regenerar o índice e refazer, a partir do PDF, a numeração do Anexo II da nº 271/2013 (os quesitos 4 a 8 aparecem como 10 a 14).
- **Registro:** decision-log §39.

**Resultado da 6.10 (07/11/2026) — ✅ concluída (D53).** Com a pasta de prompts e o acervo normativo vinculados de novo (leitura), foram lidos os prompts de atas do CTGRIC, o Analista v4.7.1 (Integridade), `CTGRIC_Plano Integridade_v2`, a NT do SITAI, a NT CGOV nº 001/2026 e o script da Carta de Serviços, e as instruções do "Analista de Projetos GIZ" v1.0, todos conferidos contra o acervo.
- **Skills (em `skills/thematic/`, com `skillOverrides` *user-invocable-only*):** `cgov-secretaria-colegiados` (CONVOCAR, GERAR_ATA, ENCAMINHAMENTOS, CONFERIR_ATA; base: Portaria nº 4.529/2025, em que a CGOV é a Secretaria-Executiva do CTGRIC; tabela dos colegiados em `references/`); `cgov-integridade` (MONITORAR_PLANO, REVISAR, ANALISAR_PESQUISA, RISCOS_INTEGRIDADE, AGENTES; base: Decreto nº 11.529/2023 e Portarias nº 253/2026 e nº 257/2026); `cgov-carta-servicos` (LEVANTAR, FICHA, CONFERIR, NT_METODO; Lei nº 13.460/2017, art. 7º, e Decreto nº 9.094/2017, art. 11); `cgov-projetos-cooperacao` (REDIGIR_TDR, REDIGIR_NOTA_INFORMATIVA, REDIGIR_DESPACHO, ALINHAR, CHECAR_INSUMOS; genérica, com a GIZ em `references/giz.md`). Cada uma tem 3 evals sintéticos.
- **Achados:** (1) os prompts citam a Portaria nº 4.007/2023, revogada pela nº 4.529/2025 (art. 14); (2) ⚠️ a nº 4.529/2025 trata o quórum de forma diferente nos arts. 9º e 11; (3) o Programa Integra+ e o Plano de Integridade em vigor são as Portarias nº 253/2026 e nº 257/2026 (ciclo 2026–2028); (4) os atos do Conselho de Governança e do CIG não estão no acervo (C3); (5) o acervo tem duas transcrições do Decreto nº 9.094/2017 (C8); (6) o script original da Carta de Serviços tinha credencial de banco em texto aberto (S1), e por isso foi refeito como `scripts/classificar_entregas.py` v0.1.0, que lê um CSV exportado pelo usuário, não se conecta a banco e compara palavras inteiras; (7) o prompt da GIZ atribuía a Cadeia de Valor à Portaria nº 5.592/2025, e isso não foi reproduzido.
- **Decisão (D53):** gravar as quatro skills; enquadrar a Carta de Serviços no Art. 37, parágrafo único, VI, como desdobramento do Catálogo de Produtos e Serviços, sem dizer que o inciso a menciona.
- **Também alterados:** roteamento da `cgov-triagem-processo-sei` (4 linhas), `.claude/settings.json` e `docs/catalogo-skills.md` (34 fontes, 32 no plugin).
- **Registro:** decision-log §40.
- **Depois do *commit*:** `0d85240` enviado ao GitHub; publicação com 35/35 arquivos conferidos por SHA-256; `--verificar` mostra 34 divergências, todas de skills a reinstalar na 6.8 (`operacao/` 14/14 e `docs/` 33/33 iguais). Pendência S1 resolvida pelo Coordenador (script limpo).

**6.7 — Validação do OCR do Windows (07/11/2026) — ✅ concluída.** O `ocr_windows.ps1` recebe **imagens**, não PDF, e usa o OCR nativo do Windows (WinRT), que só carrega no **Windows PowerShell 5.1** (`powershell.exe`). Roteiro entregue ao Coordenador: (1) conferir os idiomas de OCR instalados (`pt-BR` obrigatório); (2) renderizar as páginas a 300 dpi com `pypdfium2`; (3) rodar o `ocr_windows.ps1`; (4) comparar o texto com a transcrição revisada do acervo. PDFs de teste, sem camada de texto (0 palavras extraídas por `pdftotext`) e com `.md` revisado: Decreto nº 9.756/2019 (2 páginas) e Portaria ICMBio nº 506/2022 (3 páginas). Critério proposto, pela cobertura de palavras com acentos: ≥ 95% aprovado; 85–95% utilizável com revisão; < 85% reprovado. Referência: no Decreto nº 9.756/2019, o Tesseract só com modelo inglês deu 77,5% com acentos e 88,7% sem acentos. Rascunhos em `local/pilots/transcricao/<data-hora>-teste-ocr/`, fora do Git.
- **Resultado (PowerShell 7.6 do Coordenador, que chamou o Windows PowerShell 5.1):** OCR `pt-BR` instalado (com `en-GB`); Decreto nº 9.756/2019, 2 páginas em 1,0 s, cobertura de **96,1%**; Portaria nº 506/2022, 3 páginas em 1,2 s, cobertura de **98,3%**. Os dois foram **aprovados**. O resultado é igual com e sem acentos: os acentos saíram certos.
- **Erros típicos:** o ordinal `º` lido como `0` e o `§` como `s` (`1º` → `10`, `§ 2º` → `s 20`), o que pode confundir o `Art. 1º` com o `Art. 10`; e o cabeçalho e o rodapé do navegador entram no texto. Os dois cuidados entram no Passo 2 da `cgov-transcrever-normativos` (preparo 6.8a). Uma checagem automática dos ordinais no `qa_transcription.py` fica na pendência E10. A mensagem "OCR concluído" sai com acentuação trocada no PowerShell 7, por diferença de codificação do console; isso é cosmético.
- **Pendência E5:** resolvida.

**Preparo da 6.8 (07/11/2026).** Em duas entregas, porque a tabela de caminhos antigos do `AGENTS.md` ainda serve às skills instaladas até a reinstalação:
- **6.8a (antes da reinstalação), em `local/pilots/6.8a/`:** cuidados do OCR no Passo 2 da `cgov-transcrever-normativos` (6.7); números de processo fictícios nas evals da `cgov-nt-01` e da `cgov-nt-03` (E6); `escritorio-cgov-operacao.md` v1.1 (nomes `pgd-*`, skills da 6.4 e da 6.10, seção "Caminhos" por papel, regra dos índices com o gerador publicado); `analista-processos-sei.md` v7.4 (roteamento com os nomes novos e as skills novas). Depois: *commit*, publicação e reinstalação das 34 skills (`dist\skills\<commit>\`), exclusão dos 8 nomes antigos do PGD na conta (com confirmação), `--verificar` = 0 e colagem das instruções v1.1 no projeto Operação (P5). O Apêndice B é atualizado ao gravar a 6.8a.
- **6.8b (depois da reinstalação), em `local/pilots/6.8b/`:** no `operacao/AGENTS.md`, a seção de caminhos antigos vira "Locais antigos" (D48); `docs/fluxos-de-trabalho.md` (caminhos por papel; índices pelo gerador publicado). Depois: *commit* e publicação.
- **Evals (D54, respondida em 07/11):** evals qualitativos das 9 skills alteradas que têm casos (`cgov-nt-01`, `cgov-nt-06`, `cgov-triagem-processo-sei`, `cgov-gestao-acervo`, `cgov-saneamento-legistica` e as 4 da 6.10; 28 casos), rodados pelo Claude nesta sessão com subagentes sobre as fontes do repositório, com execução e avaliação feitas por agentes diferentes; os casos das 13 sem `evals.json` ficam na pendência E9. Levantamento: 34 skills; 21 têm evals (38 casos em `evals.json` e 7 `trigger_eval.json`); 13 não têm `evals.json` (as 8 `pgd-*`, as 2 `cgge-fgbio-*`, `cgov-auditoria-competencias`, `cgov-comparar-versoes` e `cgov-modelar-fluxo`). Todos os JSON são válidos.

**Resultado dos evals da 6.8 (07/11/2026, D54).** Três agentes responderam aos 28 casos das 9 skills sem ver os gabaritos. Outros dois agentes avaliaram as respostas contra as expectativas e conferiram no acervo as normas citadas. Resultado: **129 de 134 expectativas (96%)**. Nenhum dado foi inventado, nenhum dado pessoal apareceu, nenhuma gravação foi feita sem pedir confirmação, e as normas fora do acervo vieram sempre com ⚠️.
- **Por skill:** `cgov-nt-01` 12/12; `cgov-nt-06` 3/5; `cgov-saneamento-legistica` 24/24; `cgov-gestao-acervo` 24/24; `cgov-triagem-processo-sei` 14/14; `cgov-secretaria-colegiados` 14/14; `cgov-integridade` 11/14; `cgov-carta-servicos` 13/13; `cgov-projetos-cooperacao` 12/12.
- **Falhas:** na `cgov-nt-06` (caso 1), a skill parou certo por falta dos capítulos 2 a 4, mas não tinha regra para esse pedido (D55). Na `cgov-integridade` (caso 2), o caso citava uma planilha que não estava anexada.
- **Correções aplicadas (6.8a):**
  - `cgov-nt-06`: rascunho condicionado (D55), com o eval ajustado.
  - `cgov-saneamento-legistica` e `cgov-nt-03`: exceções às fórmulas consagradas no futuro do presente (D56). A legística passa também a citar só dispositivo cuja letra sustente a regra.
  - `cgov-triagem-processo-sei`: a seção 6 lista os cinco subsídios; nota sobre o alcance do art. 3º da Portaria nº 129/2020.
  - `cgov-gestao-acervo`: ⚠️ no valor dos campos de lista.
  - `cgov-secretaria-colegiados`: quórum com 11 membros (os dois limites dão 6); linha do Conselho de Governança, cuja Secretaria-Executiva é da CGGE (Regimento, art. 36, parágrafo único, IV; Portaria nº 4.101/2023, arts. 8º e 10).
  - `cgov-integridade`: situação "informada como concluída — evidência pendente"; CSV fictício com 73 respostas no eval 2.
  - `cgov-carta-servicos`: Decreto nº 9.094/2017, art. 11, § 3º, I a XII (antes, I a X), e § 4º (ato público de liberação); script v0.2.0, que grava também o arquivo de todas as entregas (testado); limitação sobre a ordem dos tipos.
  - `cgov-projetos-cooperacao`: Fronteiras encaminham a contratação direta.
  - `cgov-nt-01`: gabarito do caso 2 ajustado.
- **Observações do avaliador descartadas na conferência:** o acervo tem, sim, duas transcrições do Decreto nº 9.094/2017 (só uma foi copiada para a avaliação); a remissão do Regimento ao art. 8º da Portaria nº 4.101/2023 é correta (é o artigo da estrutura).
- **Pendente (E11):** tabela "regra → dispositivo conferido" e evals mais fortes da `cgov-saneamento-legistica`, que dependem do Decreto nº 12.002/2024 e da LC nº 95/1998 no acervo (C3).

**6.8a gravada (07/11/2026, sem *commit*).** 23 arquivos: as 9 skills corrigidas e a `cgov-transcrever-normativos` (cuidados do OCR); evals da `cgov-nt-01` e da `cgov-nt-03` com números fictícios (E6); `escritorio-cgov-operacao.md` v1.1 (Apêndice B atualizado); `analista-processos-sei.md` v7.4. Sanitização: 0 erros e 26 avisos; YAML válido. Registro: decision-log §42.

**6.8 — Reinstalação e encerramento (07–08/11/2026) — ✅ concluída.**
- **Commit e publicação:** a 6.8a foi enviada no *commit* `b863ef3`; a publicação conferiu 34/34 arquivos por SHA-256 (34 pacotes em `dist\skills\b863ef3\`; `operacao/` sem mudança; referência de `docs/` substituída, com a anterior na quarentena).
- **Reinstalação (Coordenador):** as 34 skills foram enviadas à conta e os 8 nomes antigos do PGD foram excluídos (D47). As instruções v1.1 foram coladas no projeto Operação (P5).
- **Primeira tentativa (07/11):** o `--verificar` deu 34 divergências. A lista de skills da conta, consultada pelo Claude, mostrou que os zips não tinham chegado à conta: os nomes antigos continuavam lá e os novos não existiam. A 6.8b ficou sem *commit*. Em 08/11, o Coordenador enviou um zip de teste (`cgov-integridade`), conferido na conta, e depois os outros 33, e excluiu os 8 nomes antigos. O Claude conferiu os 34 nomes e as descrições na conta. Depois de o Claude Code atualizar a cópia local, o `--verificar` deu **34/34 iguais, sem divergências**.
- **6.8b:** no `operacao/AGENTS.md`, a seção de caminhos antigos passou a se chamar "Locais antigos" (D48), e `docs/fluxos-de-trabalho.md` passou a citar caminhos por papel e os índices pelo gerador publicado. Commit `066068b`, publicado em 08/11, com 35/35 conferidos. O `--verificar` final não mostrou divergências: skills 34/34, `operacao/` 14/14 e `docs/` 33/33.
- **Pendências:** P4 e P5 resolvidas. Ficam para depois da Fase 6: E9 (evals das 13 skills sem casos), E10 (checagem dos ordinais no `qa_transcription.py`), E11 (tabela de dispositivos da legística, depois da C3) e a 6.9(e) (piloto, na Fase 11).
- **Registro:** decision-log §43.

| Etapa | Ação | Aceite | Situação |
|---|---|---|---|
| 6.1 | Exportar as 26 skills CGOV/CGGE instaladas (texto atual da conta) para `local/installed-reference/_export_AAAA-MM-DD/` e comparar com as 14 fontes e com `local/installed-reference` | Divergências decididas pelo Coordenador | ✅ 07/11: 28 exportadas, 39/39 conferidas; 12 divergências decididas (D43) |
| 6.2 | Promover as 12 skills sem fonte a `skills/<família>/`, revisando dados pessoais e eliminando caminhos absolutos (`H:\…`, `C:\…`) | `verificar_sanitizacao.py` aprovado | ✅ 07/11 (D46): 12 skills em `skills/pgd/` e `skills/normativo/`, mais as 2 `cgge-fgbio-*` em `skills/cgge-fgbio/`; saneadas; sanitização 0 erros |
| 6.3 | **Caminhos neutros (ADR-006)**: as skills passam a citar "pasta do processo", "pasta de trabalho do processo", "acervo normativo", "série de Notas Técnicas"; os caminhos concretos ficam no `AGENTS.md` de cada repositório | Busca por `local/analyses` e `_acervo-escritorio-virtual` nas skills = 0 | ✅ 07/11 (D48): 0 ocorrências (também 0 de `normative-sources`, `_CGOV_NT` e `CGOV_Processos`); 13 skills alteradas; mapeamento nos dois `AGENTS.md` |
| 6.4 | Nova skill **`cgov-gestao-acervo`** (operação): triagem de `00_entrada`; criação da pasta de processo a partir do modelo; preenchimento e atualização do `PROCESSO.md`; atualização dos índices; envio para `99_arquivo` de versões superadas e processos concluídos | Evals com 5 casos sintéticos | ✅ 07/11 (D51): `skills/escritorio/cgov-gestao-acervo/` (5 modos) com 5 casos em `evals/evals.json`; índices pelo gerador publicado em `90_escritorio-virtual/ferramentas/`; execução das evals na 6.8 |
| 6.5 | Descrições ≤ 950 caracteres; incorporar o eval do *branch* `claude/cgov-nt-triagem-description-loop-6x6dsc` e apagar o *branch* | — | ✅ 07/11 (D49): 8 descrições encurtadas (máx. 878); `cgov-gestao-riscos` rebaseada (D43); eval em `cgov-nt-01-triagem/evals/trigger_eval.json` (10/10); `loop_results/` no `.gitignore`; *branch* apagado pelo Coordenador |
| 6.6 | D4: converter `analista-processos-sei.md` em skill `cgov-triagem-processo-sei` (ou mantê-lo) | Decisão registrada | ✅ decidida 07/11 (D4): **criar a skill e manter o `.md`** como versão autocontida para assistentes sem acesso a arquivos (Gems, GPTs). A skill reúne o roteamento (Seção 3) e a cadeia de raciocínio (passos 0–7) e lê a base normativa no acervo, sem copiá-la; é escrita com caminhos neutros, junto com a 6.4 (ordem 7), com evals na 6.8. Os fatos normativos alterados ficam sincronizados nos dois textos. Escopo (D45): só a CGOV (Art. 37); as instruções "Analista CGGE" v3.0 ficam como referência. **Skill criada em 07/11 (D51):** `skills/escritorio/cgov-triagem-processo-sei/` (SKILL.md, `references/formatos-de-saida.md`, `references/pilares-normativos.md` só com nomes de normas, 3 evals) |
| 6.7 | Validar `ocr_windows.ps1` no Windows | Teste com PDF sem camada de texto | ✅ 07/11: aprovado nos dois PDFs (cobertura com acentos de 96,1% e 98,3%; critério ≥ 95%); erro típico nos ordinais e no `§`, tratado na `cgov-transcrever-normativos` (6.8a) |
| 6.9 | **Modelo geral de análise de atos normativos (D34).** Base: `01_processos\SEI_02070.007589_2025-35_termos-compromisso\trabalho\Instrucoes_Gerais_CGOV_Analise_Atos_Normativos_v1.md` (06/11/2026, derivado das 10 sessões do processo de Termos de Compromisso). (a) Decidir as 6 questões da Parte B.5: profundidade da AIR (Nível 2 como padrão?), competências e legística como padrão ou obrigatórias, foco no conteúdo do ato, tempo verbal dos dispositivos propostos (conferir o Decreto nº 12.002/2024), residual 2–3 no Regime A e pasta `trabalho/`. (b) Tornar regra do pipeline o uso de `cgov-modelar-fluxo`, `cgov-gestao-riscos` e `cgov-air-arr` como subsídios obrigatórios da NT, com dispensa só por decisão registrada no `NT_ESTADO.md`: ajustar o roteiro da `cgov-nt-01` e os capítulos da `cgov-nt-03` a `07`. (c) Corrigir as 8 divergências da Parte B.4: roteiro da `nt-01`; pasta `_CGOV_NT` (com 6.3); tempo verbal `nt-03` × legística; cabeçalhos `nt-03` × `nt-07`; Quadro Consolidado na `nt-05`; 5 ajustes da `cgov-gestao-riscos`; contexto PSPEADBio nas skills analíticas; prefixos de códigos. (d) Publicar a versão consolidada como procedimento em `docs/` e modelo em `operacao/modelos/` (atualizando os caminhos, por exemplo `normative-sources` → `03_normativos`), e citá-la no Apêndice B. (e) Validar num ato normativo real (Fase 11) | Decisões B.5 registradas; evals da `nt-01` com o roteiro novo; procedimento publicado; piloto aprovado | 🟨 (b)–(d) ✅ 07/11 (D50): roteiro da `cgov-nt-01` (Passo 3.2, cinco subsídios), capítulos `nt-03` a `07`, 8 divergências corrigidas, ampliações da `cgov-nt-06` e da `cgov-modelar-fluxo`, procedimento v2 em `docs/procedimentos/analise-atos-normativos.md` e modelo em `operacao/90_escritorio-virtual/modelos/analise-ato-normativo/`; citação no Apêndice B e evals da `nt-01` com o roteiro novo na 6.8; (e) piloto na Fase 11. Histórico: (b) inclui as ampliações da `cgov-nt-06` e da `cgov-modelar-fluxo` (D45). (a) ✅ 07/11 (D44; texto-base copiado pelo Coordenador para `local\pilots\`); (b)–(d) na ordem 6, já com a D44: **cinco** subsídios obrigatórios (fluxo, competências, legística, riscos, AIR); foco do ato perguntado na triagem; dispositivos propostos no **futuro** (ajustar a `cgov-saneamento-legistica` e o item 7 da Parte A, não a `nt-03`); (e) na Fase 11. ⚠️ Sanear o caminho pessoal e o número SEI do texto-base antes de publicar em `docs/` ou `operacao/modelos/` |
| 6.8 | Evals das skills alteradas (`skill-creator`), com números de processo SEI fictícios nas evals da `cgov-nt-01` e da `cgov-nt-03` (D38, pendência E6); *commit*; publicação; reinstalação (inclusive as três desatualizadas desde 06/10). **Caminhos (D48):** depois da reinstalação, sai do `operacao/AGENTS.md` só a frase de tradução para as skills instaladas; a tabela fica como "Locais antigos" (as skills a usam para achar arquivos legados), e sai a seção "Caminhos" das instruções do projeto Operação (P5); publicar o `operacao/` atualizado. **Renomeação do PGD (D47):** instalar as 8 com os nomes `pgd-*`, **excluir da conta** os 8 nomes antigos (com confirmação) e atualizar `escritorio-cgov-operacao.md` (Apêndice B) e `analista-processos-sei.md` com os nomes novos | `--verificar` = nenhuma divergência | ✅ 08/11: evals 129/134 (D54); 6.8a (`b863ef3`); 34 skills reinstaladas e 8 nomes antigos excluídos; instruções v1.1; 6.8b (`066068b`); `--verificar` sem divergências |
| 6.10 | **Skills novas da análise da pasta de prompts (D45):** `cgov-secretaria-colegiados`, `cgov-integridade`, `cgov-carta-servicos` e `cgov-projetos-cooperacao`, com caminhos neutros, sem dados pessoais nem números SEI reais; normas conferidas no acervo | Evals com 3 casos sintéticos por skill (na 6.8); `verificar_sanitizacao.py` aprovado | ✅ 07/11 (D53): 4 skills em `skills/thematic/`, 12 evals; sanitização 0 erros; instalação na 6.8 |

---

### Fase 7 — Plugin `cgov-escritorio` — 🟨 em andamento (7.0 ✅; ADR-005 aceito em 09/11/2026)

| Etapa | Ação |
|---|---|
| 7.0 | **Revisão documental (pré-requisito, ✅ 09/11/2026, D57):** `docs/INDICE.md`, `docs/convencoes-documentacao.md`, `docs/governance/rastreabilidade.md`, índices gerados (plano, decision-log, analista SEI), frontmatter em `docs/`, `scripts/gerar_indices_docs.py` e `scripts/verificar_docs.py`. **Resultado:** 109 `.md`, 469 links relativos, 0 erros no verificador; plano de 1.801 para ~1.610 linhas (Apêndices B, E e F por link). ADR-005 **aceito em 09/11/2026** (D58, E12 ✅); depois do `git mv`, rodar o gerador e o verificador (E14) |
| 7.1 | `git mv skills/<família>/<s> plugins/cgov-escritorio/skills/<s>` (estrutura plana); `plugin.json` e `README.md` do plugin (Apêndice C). **✅ 09/11/2026 (D58; gravada, aguardando *commit*):** 32 skills, 70 renomeações; `plugin.json` com `version` `0.1.0` (a `1.0.0` só na 7.6) e sem a skill de painéis (Fase 10) na descrição |
| 7.2 | Comandos do acervo: `/cgov-escritorio:novo-processo`, `:triar-entrada`, `:atualizar-indices`, `:registrar-pendencia` |
| 7.3 | `publicar_operacao.py` gera `dist/cgov-escritorio-<versão>.zip`; `.claude/settings.json` desabilita o plugin sincronizado nas sessões de desenvolvimento (⚠️ confirmar a chave na documentação de *synced plugins* do Claude Code; testar com `claude --plugin-dir`) |
| 7.4 | `claude plugin validate .\plugins\cgov-escritorio` |
| 7.5 | **Customize → Plugins → Add → Upload plugin**; testar no projeto Operação |
| 7.6 | Desativar as skills avulsas do plugin (32 em 08/11/2026; as 2 `cgge-fgbio-*` ficam fora) por uma semana; sem regressão, excluí-las; versão `1.0.0` no `CHANGELOG.md` |
| 7.7 | (Opcional) Marketplace GitHub: **Add marketplace** → `lpchagas/cgov-geral`, com **Connect GitHub / Install the Claude GitHub App** só para este repositório e **Sync automatically desligado**, depois de testar que um *commit* não publicado não chega à conta |

**Resultado parcial (09/11/2026):** ADR-005 aceito como está (D58; decision-log §45) e pendência E12 resolvida. **7.1 gravada** depois da confirmação do Coordenador (lista dos 32 `git mv`, `plugin.json` 0.1.0): `skills\` mantém só `cgge-fgbio\` (as cinco pastas de família ficaram vazias e podem ser removidas no PowerShell; o shell do Cowork não apaga); referências corrigidas em `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`, `.gitignore` e 7 arquivos de `docs\`; `docs\catalogo-skills.md` regerado; `scripts\verificar_docs.py` deixou de ignorar `plugins/` (110 `.md`, 469 links, 0 erros); sanitização aprovada (0 erros). **⚠️ Até a 7.3**, `publicar_operacao.py --verificar` e `--publicar` não devem ser usados: o script lê só `skills/` e trataria as 32 skills como sem fonte. Pendência E14 resolvida.

**Runbook "Alterar uma skill":** pendência → *branch* → editar → evals (`skill-creator`) → sanitização + validação → `version`/`CHANGELOG`/log → *merge*/tag/*push* → `publicar_operacao.py` → enviar o zip → `--verificar` → fechar a pendência. Reversão: reenviar o zip anterior (os três últimos ficam em `dist/`).

---

### Fase 8 — Multiplataforma e aposentadoria do WSL — ⬜ não iniciada

| Etapa | Ferramenta | Configuração |
|---|---|---|
| 8.1 | Claude Code (aba Code) | Abrir o repositório. **Bloqueio da pasta CGOV antecipado na 5.6 (D39):** `Edit(~/My Drive/10_Institucional/CGOV/**)` no `.claude/settings.json` versionado, sem nome de usuário; o `.claude/settings.local.json` só é necessário se o Drive mudar de lugar |
| 8.2 | Antigravity / Codex | `cmd /c mklink /J .agents\skills plugins\cgov-escritorio\skills`; nunca criar `GEMINI.md` na raiz |
| 8.3 | Obsidian — cofre **cgov-geral** (desenvolvimento) | *Excluded files*: `local/`, `dist/`, `.agents/`, `.claude/`, `plugins/**/evals/`, `paineis/`; *Templates* em `docs/_modelos/`; página inicial `docs/README.md` |
| 8.4 | Obsidian — cofre **CGOV — Operação** (opcional) | *Open folder as vault* → `…\10_Institucional\CGOV`; *Excluded files*: `90_escritorio-virtual/transcricoes/`, `99_arquivo/`, `**/documentos-sei/`, `**/referencias/`; página inicial `LEIA-ME.md`; os índices e o frontmatter permitem navegar por processo, situação e inciso. O cofre pessoal `My Drive\_projetos` ganha uma nota com links para os dois |
| 8.5 | Aposentar o WSL | Renomear `~/projetos/cgov-geral-v1` para `…_APOSENTADO_AAAA-MM-DD` e excluí-la 30 dias depois (ou deixar a formatação eliminá-la) |

---

### Fase 9 — Agentes e orquestração — ⬜ não iniciada

| Agente (`plugins/cgov-escritorio/agents/`) | Função | Skills | Ferramentas |
|---|---|---|---|
| `triador-demandas` | Enquadra a demanda no Art. 37 e indica skill ou agente | `cgov-nt-01-triagem`, `cgov-auditoria-competencias` | Read, Grep, Glob |
| `nt-orquestrador` | Conduz a NT pelo roteiro do `NT_ESTADO.md`; atualiza o `PROCESSO.md` | `cgov-nt-01` a `07` | Read, Write, Edit, Grep, Glob |
| `revisor-normativo` | Revisão independente, somente leitura: citações contra `03_normativos`, siglas, tempo verbal | `cgov-saneamento-legistica`, `cgov-comparar-versoes` | Read, Grep, Glob |
| `curador-acervo` | Normativos novos (transcrição, catálogo, vigência) e triagem de `00_entrada` | `cgov-transcrever-normativos`, `cgov-gestao-acervo` | Read, Write, Bash |
| `documentador-paineis` | Fichas de painéis a partir do PBIP/TMDL | `cgov-pbi-documentar-painel` | Read, Write, Grep |

Formato (documentação de subagentes): frontmatter com `name` e `description` obrigatórios; `tools`, `model` e `skills` opcionais; em agentes de plugin, `hooks`, `mcpServers` e `permissionMode` são ignorados. Modelo no Apêndice D. **Orquestração:** Cowork (agentes + Dispatch) por padrão; Maestri só se a Fase 0 confirmar Windows ou houver um Mac disponível (ADR-008). **Regras:** o revisor é somente leitura; nenhum agente grava fora da pasta do processo, de `00_entrada` ou dos índices; operações em lote só com confirmação; nenhum agente envia, publica ou protocola no SEI.

---

### Fase 10 — Painéis Power BI — ⬜ não iniciada

1. Catálogo em `docs/paineis/catalogo-paineis.md` e, na operação, ficha em `06_gestao-da-coordenacao/paineis/` (ou na pasta do processo correspondente).
2. Painéis mantidos pela CGOV salvos como **PBIP/PBIR** em `paineis/<painel>/` no repositório, sem dados.
3. Skills `cgov-pbi-documentar-painel` e `cgov-pbi-revisar-modelo`; agente `documentador-paineis`.
4. Power BI Authoring MCP (local) só no desenvolvimento; Fabric IQ MCP só com autorização da TI (D7).

### Fase 11 — Qualidade e pilotos — ⬜ não iniciada

Evals de todas as skills com `skill-creator` (taxa de acerto no catálogo); 3 casos sintéticos para cada skill promovida; **Piloto 1:** NT real de ponta a ponta no projeto Operação, de preferência uma análise de ato normativo que siga o modelo geral da 6.9 (D34), com modelagem, riscos e AIR como subsídios; **Piloto 2:** demanda temática; **Piloto 3:** um mês de uso de `00_entrada` + índices, medindo arquivos fora do lugar; cobertura dos 10 incisos do Art. 37.

### Fase 12 — Disseminação e governança — ⬜ não iniciada

`docs/guia-do-servidor.md` (resumo navegável do `LEIA-ME.md` da raiz e da instalação do plugin); modelo de acesso (D5); regra de concorrência (um responsável por processo, registrado no `PROCESSO.md`); capacitação de 1h; ciclo de versões mensal; indicadores (NTs apoiadas, tempo médio, erros de citação, arquivos em `00_entrada` há mais de 7 dias, fichas com `⚠️ revisar`); revisão semestral dos ADRs.

---

## 7. Riscos e mitigação

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Reorganização quebrar projetos Cowork e tarefas que apontam para pastas antigas | **Baixa** (era Alta) | Médio | Inventário 3.C (05/11): os vínculos antigos já não existem e nenhum aponta para a pasta CGOV; restam tarefas agendadas eventuais; etapa 4.9 (re-apontar ou arquivar); avisos no `LEIA-ME.md` |
| Colegas com acesso compartilhado perderem a referência das pastas | — | — | **Descartado** (D12: pasta de uso exclusivo do Coordenador) |
| Sincronização do Drive interpretar movimentação como exclusão + criação, ou conflitar | Média | Alto | Drive em execução e pasta offline; lotes pequenos; aguardar o sincronismo entre lotes; manifestos antes e depois |
| Perda de arquivo durante a movimentação | Baixa | Alto | Nenhuma exclusão (ADR-014); conferência por SHA-256; CSV reversível |
| Fichas `PROCESSO.md` com metadados errados inferidos pela IA | Média | Médio | Campos incertos com `⚠️ revisar`; revisão gradual pelo responsável |
| Dados SEI no Git ou no plugin | Média | Alto | Separação de dados (ADR-007); `verificar_sanitizacao.py` criado no bloco 1 da Fase 5 (06/11, v0.1.1; D37/D38): roda antes de qualquer *commit* em `docs/`, `operacao/` ou `skills/`; números SEI geram aviso. Na 6.1 (07/11), a `cgov-gestao-riscos` da conta tem 3 números de documento SEI (13 ocorrências, inclusive na descrição): saneamento na promoção (D43) |
| Junções novas (`local\processos`, `normativos`, `escritorio`) ficarem sem bloqueio de edição | **Baixa** (era Média) | Alto | **Mitigado** (07/11): os bloqueios novos (5.6) foram gravados antes de qualquer junção; com a D39, a pasta CGOV também fica bloqueada pelo caminho real; teste de bloqueio no aceite |
| Scripts Python ou Node rodados pelo Claude Code gravarem na pasta CGOV, que as regras deny não alcançam | Baixa | Alto | Só os scripts do repositório gravam na pasta CGOV, sempre com simulação, confirmação e conferência por SHA-256; `Bash(...)` com `py` pede aprovação; documentado em `docs/fluxos-de-trabalho.md` §3.1 |
| Remover junção antiga de forma recursiva e apagar o conteúdo do Drive | Baixa | Alto | **Mitigado** (07/11): `link_acervo.py` v0.1.0 confere se o item é junção e remove só o ponteiro (`os.rmdir`); para diante de pasta real (testado); nenhum `Remove-Item -Recurse` sobre `local\` |
| Duplicidade de skills na transição para o plugin | Alta | Médio | Desativar → excluir após uma semana. Na 6.8, as 8 do PGD renomeadas (D47) exigem excluir os nomes antigos da conta, com confirmação |
| Deriva fonte × instalado × espelho | **Materializado** (05/11, teste 4.8: a `cgov-nt-01` instalada grava em `CGOV_Processos/…/_CGOV_NT/`, e a fonte diz `local/analyses/`) | Alto | Até a Fase 6: tabela de tradução no `AGENTS.md` v3; **6.1 concluída (07/11):** exportação conferida e divergências decididas (D43); reinstalação na 6.8; Fase 7: plugin + `--verificar` |
| Prompts antigos (pasta `02_dev-prompts`) levarem para as skills normas desatualizadas (RI antigo, Art. 50), números SEI ou dados pessoais | Média | Alto | Prompts só como insumo (D45); toda norma conferida no acervo ou na fonte oficial; `verificar_sanitizacao.py` antes do *commit*; casos sintéticos nas evals. Ocorreu na 6.10: CTGRIC pela Portaria nº 4.007/2023, revogada, e credencial de banco em texto aberto num script; nada disso foi copiado (D53) |
| Uso por servidores sem orientação institucional sobre IA e LGPD | — | Alto | D6 antes da Fase 12 ⚠️ |
| Dependência de uma só pessoa | Alta | Alto | Runbooks, `LEIA-ME`, guia do mantenedor |
| Operações Git pelo shell do Cowork falharem (sem credencial do GitHub; travas `.lock` que o shell não apaga) | **Materializado** (05/11) | Médio | Verificação remota, *commit* e *push* pelo PowerShell do Coordenador, com scripts completos (regra 10 do Apêndice A) |
| Documentação descrever o repositório como público | — | — | **Descartado** (05/11, D19): privado confirmado e quatro arquivos corrigidos; a verificação de sanitização continua |
| Caminhos com mais de 259 caracteres no Windows | **Materializado** (4.1) | Médio | 252 origens já passam do limite hoje (backup `dev-local_2026-11` e OCR); o script usa o prefixo `\\?\`; nenhum destino longo fora de `99_arquivo`. A 4.4 contou **312 destinos longos** (f 180, g 132; o `--simular` imprime só 30). Destinos longos podem atrapalhar a sincronização do Drive e o Explorador. **Resolvido para os destinos na 4.4a** (D26): zero destinos acima de 259, e o maior tem 253 |
| Scripts do WSL (`publicar-operacao.sh`, `link-acervo.sh`) recriarem a estrutura antiga na pasta CGOV | Média | Alto | **Descartado** (07/11): substitutos em Python prontos (`link_acervo.py`, `publicar_operacao.py`); `.sh` movidos para `archive/scripts-wsl/` |
| Python ausente ou antigo no Windows para rodar `reorganizar_cgov.py` | **Descartado** (05/11) | — | Python 3.12.10 conferido; a simulação no Windows rodou sem conflitos |
| Pastas com atributo "somente leitura" impedirem a remoção (`WinError 5`) | Materializado e **resolvido** (05/11, limpeza D29) | Baixo | v1.2.1 tira o atributo e tenta de novo (343/343 removidas) |
| Skills e junções antigas (`normative-sources`, `analyses`) deixarem de achar arquivos durante a execução dos lotes | Alta | Médio | Pasta congelada (D27) e trabalho de operação suspenso durante a Fase 4; junções novas na 5.1 e skills com caminhos neutros na Fase 6 (fonte neutra desde a 6.3, 07/11; conta na 6.8) |
| Mapa ficar desatualizado entre a 4.2 e a execução (arquivos novos ou alterados) | Materializado (05/11) e **encerrado** (06/11: execução concluída; congelamento D27 terminado) | — | A pasta voltou a receber trabalho; o manifesto posterior fica como retrato de 05/11 |
| Instruções de projeto Cowork coladas no campo errado (descrição) | Materializado e **corrigido** (05/11) | Médio | Conferir pela tela do projeto que **Instruções** não está vazio e que a descrição tem só o texto curto; repetir a conferência na criação do projeto "Operação" (4.8) |

---

## 8. Critérios de conclusão do projeto

1. Repositório de desenvolvimento único no Windows, em sincronia com o GitHub privado; WSL aposentado.
2. Pasta CGOV com a estrutura da Seção 5.2: 100% dos arquivos com destino conferido por hash, **nenhum processo fora de `01_processos`**, um único acervo normativo, `LEIA-ME.md`, `AGENTS.md`, `_LEIA-ME.md` e `_INDICE.md` publicados a partir do repositório.
3. Uma ficha `PROCESSO.md` por processo, sem pendências `⚠️ revisar` nos processos em andamento.
4. Projetos Cowork "Implantação" e "Operação" configurados e testados; nenhum projeto apontando para caminho inexistente.
5. Plugin `cgov-escritorio` ≥ `v1.0.0`, sem divergência entre fonte e instalado; todas as skills do catálogo (as 26 do inventário e as novas da Fase 6) com fonte versionada.
6. Antigravity, Codex, Claude Code e Obsidian (dois cofres) lendo as fontes corretas.
7. Cinco agentes operacionais e uma NT real conduzida de ponta a ponta.
8. Catálogo de painéis e ao menos um painel em PBIP versionado.
9. Guia do servidor publicado e uma capacitação realizada.

---

## 9. Decisões do Coordenador

| # | Pergunta | Recomendação | Situação |
|---|---|---|---|
| D1 | Desenvolvimento no Windows (`C:\Projetos\cgov-geral`)? | Sim | ✅ Respondida (04/11) |
| D2 | Dois projetos Cowork separados: Implantação e Operação? | Sim | ✅ Respondida (05/11), com os nomes "Escritório CGOV — Implantação" e "Escritório CGOV — Operação" |
| D3 | Repositório privado com disciplina de sanitização? | Sim | ✅ Respondida (04/11); visibilidade **privada** reconfirmada em 05/11; documentação corrigida (D19) |
| D4 | `analista-processos-sei.md`: converter em skill? | Converter | ✅ Respondida (07/11): **criar a skill `cgov-triagem-processo-sei` e manter o `.md`** (autocontido, para Gems e GPTs); etapa 6.6 |
| D5 | Acesso dos servidores: piloto com contas individuais ou plano Team/Enterprise? | Piloto com 1–2 servidores | Pendente (Fase 12) |
| D6 | Há orientação do ICMBio sobre uso de IA generativa e LGPD? | Consultar a TI e o encarregado de dados ⚠️ | Pendente (antes da Fase 12) |
| D7 | Pedir à TI a habilitação do Fabric IQ / Power BI MCP? | Adiar | Pendente (Fase 10) |
| D8 | Maestri: há versão Windows ou um Mac disponível? | Verificar | Pendente |
| D9 | `local/_backup` do WSL: só no Drive? | Sim | ✅ Executada (04/11) |
| D10 | `02070.006604 2026-17_Política de Governança` e `…_v2`: fundir numa pasta só? | Fundir | ✅ Respondida (05/11): **fundir** numa só pasta `SEI_02070.006604_2026-17_politica-governanca` (conteúdo da v2 em `trabalho\v2\` quando houver arquivos de mesmo nome) |
| D11 | Destinos de `ADPF` (sem número) e `_Impacto Regulatório_Plano de Manejo` | — | ✅ Respondida (05/11): **ADPF** (projeto antigo, sem número SEI rastreável) → `99_arquivo\processos-encerrados\ADPF\`; **Impacto Regulatório** → pasta do processo da NT 27/2026 |
| D12 | A pasta CGOV é compartilhada com outros servidores? | — | ✅ Respondida (05/11): **não**; uso exclusivo do Coordenador de Governança |
| D13 | Projetos Cowork por processo: re-apontar ou arquivar (ADR-013)? | Arquivar após copiar instruções | ✅ Respondida (05/11): seguir a recomendação |
| D14 | `_doutorado` sai da pasta institucional? | Sim | ✅ Respondida (05/11): mover para `My Drive\_projetos\05_privado\` |
| D15 | Versões vigentes (Plano de Entregas CGGE; apresentações ECOA) | Mais recente fica | ✅ Respondida (05/11): seguir a recomendação (a mais recente em uso; as demais em `99_arquivo\versoes-anteriores\`) |
| D16 | Quarentena da Seção 5.6 com exclusão após 30 dias? | Sim | ✅ Respondida (05/11): seguir a recomendação |
| D17 | Forma de interação do Claude neste projeto | — | ✅ Respondida (05/11): decisões por perguntas de múltipla escolha com a opção recomendada; scripts PowerShell completos; caminhos completos; próximos passos com sugestão de *prompt* ao fim de cada resposta (Apêndice A, regras 9–12) |
| D18 | Ignorar `C:\Projetos\cgov-geral\.obsidian\` no Git? | Sim | ✅ Respondida (05/11): incluído no `.gitignore`; *commit* junto com as v3.2 e v3.3 do plano |
| D19 | Corrigir já as menções a "repositório público" em `README.md`, `AGENTS.md` e `docs\fluxos-de-trabalho.md`? | Corrigir agora | ✅ Respondida (05/11): corrigidas junto com o `CLAUDE.md`, no *commit* da v3.4 |
| D20 | Preservar a memória do projeto `cgov-geral-v1`? | — | ✅ Respondida (05/11): **não**; trata só de uma análise antiga, sem relação com a implantação |
| D21 | Forma de encerrar a 3.C (vínculos antigos inexistentes após a formatação) | Inventário simplificado | ✅ Respondida (05/11): inventário simplificado; re-apontar ou arquivar cada projeto na etapa 4.9 |
| D22 | Linhas `a-decidir` do mapa da 4.1 (28 linhas em 9 grupos) | Recomendações apresentadas na 4.2 | ✅ Respondida (05/11): aceitas; registradas em `C:\Projetos\cgov-geral\local\reorganizacao\decisoes.csv` (Seção 5.5) |
| D23 | Minutas `.md` da Política e da Metodologia de Gestão de Riscos (`normative-sources`): qual processo? | — | ✅ Respondida (05/11): processo 02070.001696/2026-31 (`trabalho\`) |
| D24 | Apelidos dos 16 processos sem nome | Propor pelo assunto do processo | ✅ Respondida (05/11): 11 aceitos (`C:\Projetos\cgov-geral\local\reorganizacao\apelidos.csv`); 5 ficam só com o número até a ficha `PROCESSO.md` (4.7): 02070.000321/2014-10, 02070.009380/2025-14, 02070.009463/2025-03, 02070.009464/2025-40 e 02070.010603/2024-05 |
| D25 | Quando atualizar o plano e fazer o *commit* do script | Depois da 4.2 | ✅ Respondida (05/11): v3.7 com 4.1 e 4.2 juntas, num único *commit* |
| D26 | 312 destinos acima de 259 caracteres em `99_arquivo` (lotes f e g): o que fazer? | Encurtar antes da execução | ✅ Respondida (05/11): **encurtar**. Regra aprovada na 4.4a: `transcr-bkp_20261006` (lote f) e `transcr-analyses` (lote g); 888 linhas; mapa promovido |
| D27 | 2 arquivos novos entraram na pasta CGOV durante a 4.4a: como seguir? | Congelar a pasta e atualizar | ✅ Respondida (05/11): **pasta CGOV congelada** até o fim da Fase 4; mapa (2.833 arquivos, 74 processos), manifesto e simulação refeitos |
| D28 | O lote (a) prevê publicar os documentos de navegação, mas o script só cria pastas e `operacao/` era da Fase 5: como executar? | Antecipar `operacao/` | ✅ Respondida (05/11): **antecipar** `operacao/` (12 documentos), fazer o *commit* e copiar por script PowerShell com conferência de SHA-256 |
| D29 | Depois do lote (g), as 8 áreas antigas ficam só com pastas vazias: o que fazer com elas? | Remover só as pastas vazias | ✅ Respondida (05/11): **remover só as pastas vazias** com `reorganizar_cgov.py --limpar-vazias` (v1.2.0), depois de conferir que não resta nenhum arquivo; a quarentena geraria caminhos de até 336 caracteres |
| D30 | Como publicar as 74 fichas e os 5 índices da 4.7? | Claude publica pelo shell | ✅ Respondida (05/11): **o Claude publica**, copiando do rascunho sem sobrescrever e conferindo o SHA-256 (79/79 ok) |
| D31 | Aplicar a revisão da 4.8 (arquivar `escritorio-cgov.md`; republicar `AGENTS.md` e `LEIA-ME.md`, com as versões anteriores na quarentena)? | Aplicar as três | ✅ Respondida (05/11): **aplicadas**; SHA-256 conferidos |
| D32 | Fechar a 4.8 (pasta de teste para a quarentena; `AGENTS.md` v3 com o caminho `_CGOV_NT` da skill instalada; pendência de índices resolvida)? | Aplicar as três | ✅ Respondida (05/11): **aplicadas** |
| D33 | Método da 4.9 (projetos Cowork antigos) | Copiar as instruções e arquivar | ✅ Respondida (05/11): **copiar e arquivar** — as de processo vão para o `PROCESSO.md`, as temáticas para `local\archive\cowork-projetos\` |
| D34 | Incluir no plano o aprimoramento do modelo geral de análise de atos normativos (`Instrucoes_Gerais_CGOV_Analise_Atos_Normativos_v1.md`)? | Sim, na Fase 6 | ✅ Respondida (06/11): **incluir** — objetivo do Coordenador de desenvolver o modelo com mais qualidade; etapa 6.9, piloto na Fase 11 |
| D35 | `oficina-planejamento-GR2` e `05_projetos/2026-10_oficina-pgd-gr2-fortaleza` são o mesmo projeto? | — | ✅ Respondida (06/11): **sim**; a descrição foi para o `PROJETO.md` da pasta |
| D36 | Atualizar já a documentação do repositório para a estrutura nova (antecipando partes da Fase 5)? | — | ✅ Pedido do Coordenador (06/11): **atualizar integralmente**; feito em 06/11, com os `.sh` bloqueados até os substitutos da Fase 5 |
| D37 | Ordem das etapas pendentes da Fase 5 e uso do *branch* | Seis blocos (sanitização → 5.7 → 5.6/5.1/5.2 → 5.3/5.5/5.8 → 5.9 → 5.10); *branch* `implantacao/fase-5` | ✅ Respondida (06/11): **ordem aprovada** e **trabalho no *branch* `implantacao/fase-5`**, com *merge* e *push* só na 5.10 |
| D38 | Achados da primeira rodada de `verificar_sanitizacao.py`: 11 caminhos pessoais no plano e 22 números de processo SEI | Trocar por `%USERPROFILE%`; manter os números SEI como aviso, com as evals na Fase 6 | ✅ Respondida (06/11): **as duas recomendações**; aplicadas no plano v3.26 |
| D39 | Bloquear no `.claude/settings.json` também a pasta CGOV pelo caminho real (`~/My Drive/10_Institucional/CGOV/**`), além das junções e do `.env`? | Sim | ✅ Respondida (07/11): **sim**; antecipa o bloqueio da 8.1 sem `settings.local.json` |
| D41 | Como integrar o *branch* da Fase 5; o que fazer com `.vscode/` e com o *branch* depois do *merge*? | `--no-ff`; ignorar; manter só local | ✅ Respondida (07/11): **as três recomendações** |
| D42 | Ordem das etapas da Fase 6 e método de exportação da 6.1 | 6.1 → 6.6 + 6.9(a) → 6.2 → 6.3 → 6.5 → 6.9(b–d) → 6.4 → 6.7 → 6.8; exportar o retrato da conta desta sessão, com conferência cruzada no PowerShell; exportar também as 2 `cgge-fgbio-*` | ✅ Respondida (07/11): **as três recomendações** |
| D43 | Divergências da 6.1: qual texto vale | `cgov-nt`: fonte + busca da conta; `cgov-gestao-riscos`: conta saneada; `cgov-regimento-interno`: fonte; PGD (3): conta com a nota incorporada | ✅ Respondida (07/11): **as quatro recomendações** |
| D44 | 6.9(a): as 6 questões da Parte B.5 do modelo geral de análise de atos normativos | (1) AIR Nível 2 padrão; (2) competências e legística padrão com dispensa; (3) foco no conteúdo como regra geral; (4) presente; (5) classe superior; (6) `trabalho/` com texto neutro | ✅ Respondida (07/11): (1) **Nível 2 padrão**, salvo não incidência ou dispensa no Nível 1; (2) competências e legística **obrigatórias**, no mesmo regime de fluxo, riscos e AIR (dispensa só pelo Coordenador, com motivo no `NT_ESTADO.md`); (3) foco **decidido por projeto**, perguntado na triagem (`nt-01`); (4) dispositivos propostos no **futuro do presente** (convenção atual; o Decreto nº 12.002/2024, art. 11, I, "e", admite presente ou futuro e pede uniformidade), ajustando a `cgov-saneamento-legistica`; (5) residual em lacuna da máscara (Regime A) vai para a **classe superior**, com a lacuna declarada (2–3 → Médio); (6) `01_processos/…/trabalho/` substitui `_CGOV_NT/` e `local/analyses/`, com **texto neutro** nas skills (6.3) |
| D45 | Propostas de skills a partir da pasta de prompts `02_dev-prompts` | Duas skills de colegiados e política; `cgov-integridade`; ampliar a `nt-06`; ampliar a `cgov-cadeia-valor` (Carta de Serviços); ampliar a `cgov-modelar-fluxo`; GIZ nas instruções do projeto; D4 só CGOV; etapa 6.10 | ✅ Respondida (07/11): **`cgov-secretaria-colegiados`** (o inciso II fica para depois, E7); **`cgov-integridade`**; **ampliar a `cgov-nt-06`**; **`cgov-carta-servicos`** como skill nova; **ampliar a `cgov-modelar-fluxo`**; **`cgov-projetos-cooperacao`** como skill nova; D4 **só CGOV**, com a CGGE como referência; **nova etapa 6.10**, depois da 6.4 |
| D46 | 6.2: famílias em `skills/`, destino das `cgge-fgbio-*`, nomes da equipe e número SEI do PSPEADBio | `pgd/` + `normativo/`; `cgge-fgbio-*` versionadas fora do plugin; marcador + lista da equipe na operação; tirar só o número agora | ✅ Respondida (07/11): **as quatro recomendações**; gravação autorizada depois da pasta de preparo |
| D47 | Renomear as 8 skills de `skills/pgd/` com o prefixo `pgd-` | Renomear antes do *commit* da 6.2; instruções da Operação e exclusão dos nomes antigos na conta na 6.8 | ✅ Pedido do Coordenador (07/11): `cgge-especialista-pgd` → `pgd-especialista`; `cgov-elaborar-entrega` → `pgd-elaborar-entrega`; `cgov-registro-execucao` → `pgd-registro-execucao`; `cgov-avaliar-entrega` → `pgd-avaliar-entrega`; `cgov-pgd-analisar-indicador` → `pgd-analisar-indicador`; `cgov-pgd-desenvolver-indicador` → `pgd-desenvolver-indicador`; `cgov-pgd-implementar-indicador` → `pgd-implementar-indicador`; `cgov-pgd-testar-indicador` → `pgd-testar-indicador`. Forma de aplicar: a recomendada |
| D48 | 6.3: papéis novos e seus caminhos; publicação do `operacao/AGENTS.md`; destino da tabela de caminhos antigos; status do ADR-006 | `06_gestao-da-coordenacao/pgd/`; `06_gestao-da-coordenacao/equipe.md`; `03_normativos/_transcricao/<data-hora>-<slug>/`; papéis agora e tabela antiga na 6.8; manter a tabela como "Locais antigos"; ADR-006 aceito | ✅ Respondida (07/11): **as seis recomendações**; gravação autorizada depois do preparo em `local/pilots/6.3_caminhos/`. A pasta de rascunhos da transcrição foi alterada pela D50 para `90_escritorio-virtual/transcricoes/` |
| D49 | 6.5: descrições, rebase da `cgov-gestao-riscos`, rótulos do eval da `cgov-nt-01` e destino do *branch* antigo | Aprovar as 8 descrições e a rebase; corrigir os 5 rótulos; incorporar o eval e `loop_results/` e apagar o *branch* | ✅ Respondida (07/11): **as três recomendações** |
| D50 | 6.9(b)–(d): roteiro, divergências, ampliações, inciso das competências e da legística, teto dos controles sem evidência, pasta de rascunhos da transcrição | Gravar o preparo; manter ⚠️ nos incisos até o piloto; Mediano (A) e Fraco (B); usar a pasta existente `90_escritorio-virtual/transcricoes/` | ✅ Respondida (07/11): **as quatro recomendações**; a última altera a D48 |
| D51 | 6.4: família das skills de operação, geração dos índices na operação, referência normativa da triagem e criação das duas skills | `skills/escritorio/`; publicar o `gerar_indices.py` em `90_escritorio-virtual/ferramentas/`; `references/pilares-normativos.md` só com nomes; preparar e gravar | ✅ Respondida (07/11): **as quatro recomendações** |
| D56 | Futuro do presente na redação saneada (`cgov-saneamento-legistica`, `cgov-nt-03`) | Manter o futuro, com exceções para as fórmulas consagradas | ✅ Respondida (07/11): **futuro com exceções** (objeto, competência, revogação e vigência no presente) |
| D55 | `cgov-nt-06`: pedido de redação sem os capítulos 2 a 4 | Rascunho condicionado | ✅ Respondida (07/11): **rascunho condicionado** |
| D54 | 6.8: alcance e execução dos evals antes da reinstalação | Evals qualitativos das skills alteradas que já têm casos; evals das 13 sem casos como pendência | ✅ Respondida (07/11): **evals das alteradas**, pelo Claude com subagentes; **E9** para as 13 sem casos |
| D53 | 6.10: gravar as quatro skills novas; enquadramento da Carta de Serviços | Gravar; registrar a competência com ⚠️ e pendência | ✅ Respondida (07/11): **gravar**; Carta de Serviços **no inciso VI**, como desdobramento do Catálogo |
| D52 | E8: relação entre as Portarias ICMBio nº 271/2013 e nº 129/2020; extensão das correções; curadoria do acervo | A nº 129/2020 prevalece onde colidir, a nº 271/2013 no resto, com ⚠️; corrigir todas as skills e instruções afetadas; curadoria pela operação | ✅ Respondida (07/11): **as três recomendações** |
| D40 | Quais ADRs viram arquivo em `docs/adr/` e quais propostos aprovar agora? | Os 14, com status; aprovar ADR-004 e ADR-007 | ✅ Respondida (07/11): **os 14**, e **ADR-004 e ADR-007 aceitos**; o ADR-011 continua proposto |
| D57 | Revisão da documentação antes da Fase 7: como tratar o plano (249 KB), o frontmatter e os ADRs "Proposto" em vigor? | Índice + apêndices por link; frontmatter leve em `docs/`; propor aceitar ADR-001, 009 e 011 | ✅ Respondida (09/11): **as três recomendações**; **ADR-001, 009 e 011 aceitos em 09/11/2026** (confirmado pelo Coordenador; ADR-005 fica para o início da Fase 7); decision-log §44 |
| D58 | ADR-005 (plugin único `cgov-escritorio`): qual decisão registrar no início da Fase 7? | Aceitar como está (só Status e Data) | ✅ Respondida (09/11): **aceitar como está**; ADR-005 aceito em 09/11/2026; decision-log §45 |

---

## 10. Prompts de execução (projeto "Escritório CGOV — Implantação")

| Fase | Prompt |
|---|---|
| 3 | "Leia a Fase 3.B e 3.C do plano. Guie-me para salvar as instruções do projeto `cgov-geral-v1` e montar o inventário de vínculos dos projetos Cowork." |
| 4.1 | "Execute a etapa 4.1: crie `scripts/reorganizar_cgov.py` com os modos `--planejar`, `--simular`, `--executar --lote` e `--reverter`, e gere o mapa CSV em `local\` sem mover nada. Mostre o resumo por ação e por área e a lista de `a-decidir`." |
| 4.3–4.4 | "Execute as etapas 4.3 e 4.4: rode de novo o `--planejar` para conferir que nada mudou, gere o manifesto anterior e rode `--simular` para todos os lotes. Mostre o resultado e aguarde minha confirmação." |
| 4.4a | "Execute a etapa 4.4a: proponha a regra de destino mais curta para `99_arquivo` (D26), ajuste o `reorganizar_cgov.py`, rode o `--planejar` à parte, mostre a diferença de linhas para o mapa aprovado (só lotes f e g) e a nova simulação, e aguarde minha aprovação." |
| 5 (início) | "Siga para a Fase 5: leia a seção da Fase 5 do plano e proponha a ordem das etapas pendentes (5.1, 5.3, 5.6, 5.7, 5.9 e 5.10), considerando o que já foi antecipado (D36) e docs/governance/pendencias.md." |
| 4.11 | "Siga para a 4.11: confira a quarentena `99_arquivo\_a-excluir_2026-11-05` contra o manifesto e me guie para excluí-la." |
| 4.9–4.10 | "Arquivei os projetos Cowork antigos. Siga para a 4.10: copie o mapa e os manifestos para `90_escritorio-virtual\manutencao`, registre a reorganização no decision-log (Decisão 28) e me guie para remover a pasta CGOV deste projeto." |
| 6.9 | "Execute a 6.9: leia `Instrucoes_Gerais_CGOV_Analise_Atos_Normativos_v1.md`, apresente as 6 decisões da Parte B.5 como perguntas de múltipla escolha e proponha as mudanças na `cgov-nt-01` e nas demais skills." |
| 4.9 | "Siga para a 4.9: vou colar as instruções de cada projeto Cowork antigo (ou \"vazio\"); grave conforme a D33 e me diga quando posso arquivar cada um." |
| 4.8 teste | "Criei o projeto Operação e rodei os testes (respostas coladas abaixo). Confira se a triagem gravou em `01_processos/…/trabalho/` e se nada foi criado em `local/`; depois prepare a quarentena do teste e a 4.9." |
| 4.8 | "Siga para a 4.8: revise o Apêndice B (instruções do projeto \"Escritório CGOV — Operação\") à luz da estrutura publicada, mostre a versão final e me guie na criação e no teste do projeto." |
| 4.5 limpeza | "Repeti a limpeza das pastas vazias com a v1.2.1 (log colado abaixo). Confira que as áreas antigas sumiram; depois siga para a 4.7 (fichas e índices)." |
| 4.5(g) conferência | "Executei o lote (g) e a limpeza das pastas vazias (log colado abaixo). Confira a quarentena, que as áreas antigas sumiram e a integridade de todos os arquivos; depois siga para a 4.6 (manifesto posterior)." |
| 4.5(f) conferência | "Executei o lote (f) (log colado abaixo). Confira as 965 movimentações, os 9 arquivos de `_doutorado` fora da pasta e a integridade dos demais arquivos; depois prepare o lote (g)." |
| 4.5(e) conferência | "Executei o lote (e) (log colado abaixo). Confira as 24 movimentações e a integridade dos demais arquivos; depois prepare o lote (f)." |
| 4.5(d) conferência | "Executei o lote (d) (log colado abaixo). Confira as 1.131 operações e a integridade dos demais arquivos; liste as pastas de origem que ficaram vazias; depois prepare o lote (e)." |
| 4.5(c) conferência | "Executei o lote (c) (log colado abaixo). Confira as 20 movimentações e a integridade dos demais arquivos; depois prepare o lote (d)." |
| 4.5(b) conferência | "Executei o lote (b) (log anexo; *commit* conferido: `<hash>`). Confira as 109 movimentações (SHA-256 no destino igual ao do manifesto) e a integridade dos demais arquivos; depois prepare o lote (c)." |
| 4.5(a) conferência | "Executei o lote (a). Confira as 24 pastas, os 12 documentos (SHA-256 iguais aos de `operacao/`) e que os 2.833 arquivos continuam iguais ao manifesto; depois prepare o lote (b)." |
| 4.5 | "Confira se a pasta CGOV continua igual ao manifesto e prepare o lote (a) da etapa 4.5: mostre as pastas e os documentos que serão criados e aguarde minha confirmação antes de eu executar." |
| 4.7 | "Gere as fichas `PROCESSO.md` dos processos do lote (d) a partir do modelo, marcando ⚠️ revisar onde não houver certeza, e gere os índices." |
| 5 | "Execute a Fase 5 no *branch* `implantacao/fase-5`, uma etapa por *commit*, com confirmação antes de alterações em lote." |
| 5 (bloco 1) | "Criei o *branch* `implantacao/fase-5` e fiz o *commit* do plano v3.25 (`<hash>`). Siga para o bloco 1 da Fase 5: crie `scripts/verificar_sanitizacao.py`, rode-o na árvore atual e mostre os achados." |
| 5 (bloco 2) | "Rodei `verificar_sanitizacao.py` no Windows (saída abaixo) e fiz o *commit* do bloco 1 (`<hash>`). Siga para o bloco 2 da Fase 5 (etapa 5.7: `.gitattributes` e `.gitignore`)." |
| 5 (bloco 3) | "Fiz o *commit* do bloco 2 (`<hash>`). Siga para o bloco 3 da Fase 5: primeiro a 5.6 (bloqueios do `.claude/settings.json`), depois `scripts/link_acervo.py` (5.1) e o roteiro para eu atualizar o `.env` (5.2)." |
| 5 (bloco 3, conferência) | "Atualizei o `.env`, rodei `link_acervo.py --executar`, testei o bloqueio no Claude Code e fiz o *commit* do bloco 3 (saídas e `<hash>` abaixo). Confira e siga para o bloco 4 da Fase 5 (`publicar_operacao.py --verificar`)." |
| 5 (bloco 4, conferência) | "Rodei `publicar_operacao.py --verificar` e `--publicar` (simulação), movi os `.sh` e fiz o commit do bloco 4 (saídas e `<hash>` abaixo). Confira e siga para o bloco 5 da Fase 5 (5.9: ADRs, `catalogo-skills.md`, `docs/README.md` e mudança do plano para `docs/`)." |
| 5 (bloco 6) | "Movi o plano para `docs/` e fiz o commit do bloco 5 (`<hash>`). Siga para o bloco 6 da Fase 5 (5.10): revisão do diff do *branch*, *merge* no `main`, *push* e publicação com `publicar_operacao.py`." |
| 5 (bloco 6, publicação) | "Fiz o *merge*, o *push* e a publicação (saídas abaixo). Confira, registre a Fase 5 como concluída e me diga o que vem a seguir." |
| 6.1 | "Siga para a Fase 6: leia a seção da Fase 6 do plano, `docs/catalogo-skills.md` e `docs/governance/pendencias.md`, e proponha a ordem das etapas (6.1 a 6.9). Comece pela 6.1: me diga como exportar o texto atual das 26 skills da conta." |
| 6.1 (conferência) | "Saída da conferência cruzada: [cole aqui]. Gere o COMPARACAO.md da 6.1 e me apresente as divergências para decisão." |
| 6.6 + 6.9(a) | "Siga para o bloco de decisões da Fase 6 (6.6 e 6.9(a)). Colo abaixo o conteúdo de `Instrucoes_Gerais_CGOV_Analise_Atos_Normativos_v1.md`: apresente a D4 e as 6 questões da Parte B.5 como perguntas de múltipla escolha." |
| 6.10 | "Fiz o commit e a publicação da v3.42 (saídas abaixo) e copiei as duas transcrições para `local\pilots\`. Leia-as e corrija o que for preciso na `cgov-nt-06`, na triagem e no `analista-processos-sei.md`; depois siga para a 6.10 (as quatro skills novas da pasta de prompts)." |
| 6.4 + triagem SEI | "Fiz o commit e a publicação da v3.41 (saídas abaixo). Siga para a 6.4: proponha a estrutura da `cgov-gestao-acervo` e da `cgov-triagem-processo-sei` (D4, só CGOV), com os 5 casos sintéticos de eval da 6.4, e mostre o que vai ser criado antes de gravar." |
| 6.9(b)–(d) | "Fiz o commit da v3.40, a publicação e apaguei o branch (saídas abaixo). Siga para a 6.9(b)–(d): proponha o roteiro novo da `cgov-nt-01` com os cinco subsídios obrigatórios (D44), as correções das 8 divergências da Parte B.4 e as ampliações da `cgov-nt-06` e da `cgov-modelar-fluxo` (D45), e mostre o que vai mudar antes de gravar." |
| 6.5 | "Fiz o commit e a publicação da v3.39 (saídas abaixo). Siga para a 6.5: liste as descrições das 28 skills com mais de 950 caracteres, proponha as versões encurtadas e verifique o eval do *branch* `claude/cgov-nt-triagem-description-loop-6x6dsc` antes de apagá-lo." |
| 6.3 | "Fiz o commit da v3.38 (saída abaixo). Siga para a 6.3: levante todos os caminhos literais nas 28 skills de `skills/`, proponha os termos neutros e o mapeamento no `AGENTS.md` (repositório e `operacao/AGENTS.md`) e mostre o que vai mudar antes de gravar." |
| 6.2 | "Fiz o commit da v3.36 (saída abaixo). Siga para a 6.2: proponha a estrutura de famílias em `skills/` para as 12 skills sem fonte e o destino das 2 `cgge-fgbio-*`, a partir da exportação `_export_2026-11-07`, e mostre a lista do que será criado antes de gravar." |
| 7 | "Execute 7.1 a 7.4 e gere o zip do plugin; depois me guie em 7.5 e 7.6." |
| 9 | "Crie os agentes da Fase 9 conforme o Apêndice D, um por vez, e valide com uma NT fictícia no projeto Operação." |

---

## 11. Quadro de acompanhamento

| Fase | Status | Data | Evidência |
|---|---|---|---|
| 0 — Decisões | 🟨 | 09/11/2026 | Respondidas: D1–D4 e D9–D58. Pendentes: D5–D8 (não bloqueiam as Fases 3–7) e aprovação formal dos ADR-008 e 010 (ADR-001, 009 e 011 aceitos em 09/11, D57; ADR-005 em 09/11, D58) (ADR-004 e 007 aceitos em 07/11, D40; ADR-006 em 07/11, D48) |
| 1 — Consolidação no Windows | ✅ | 04/11/2026 | WSL: remoto → `cgov-geral`, *push* `4960e11..67957fe`; clone em `C:\Projetos\cgov-geral` (HEAD `67957fe`, `autocrlf=false`); manifesto `local/_manifesto_wsl_20261104.sha256` (490 arquivos): 63/63 em `local\` e 488/488 no Drive; junções e `.env` provisórios |
| 2 — Arquitetura dos repositórios | ✅ | 05/11/2026 | Arranjo das Seções 5.1–5.6 aceito sem ajustes; ADR-012, 013 e 014 aprovados; D10–D16 respondidas e incorporadas ao mapa (5.5) |
| 3 — Projetos Cowork | ✅ | 05/11/2026 | 3.B.4 ✅: `cgov-geral-v1` arquivado; *commit* `be2f493` (v3.5) conferido por `ls-remote`. 3.C ✅: inventário simplificado (D21; vínculos antigos inexistentes, nenhum na pasta CGOV). 3.B.3 ✅: memória não preservada (D20). 3.A.4 ✅: instruções corrigidas. *Commits* `6890b63` e `320007d` (conferido por `ls-remote`). Repositório privado confirmado; documentação corrigida (D19). 3.B.1–3.B.2 ✅: 4 pastas do `cgov-geral-v1` registradas; instruções preservadas (SHA-256 `ad862755…`). 3.A ✅: *commits* `8787e0a` e `de0fa54` (conferido por `ls-remote`); projeto "Implantação" com as duas pastas confirmadas; teste 3.A.6 aceito; `.obsidian/` ignorado (D18); regras de interação (D17). Próximo: Fase 4 |
| 4 — Reorganização da pasta CGOV | ✅ | 06/11/2026 | 2.860 operações nos lotes a–g (todas `ok`); manifesto posterior 100% (2.833/2.833); 343 pastas vazias removidas; 74 fichas e 5 índices; projeto Operação criado e testado; projetos antigos arquivados; mapa, manifestos e registros em `90_…\manutencao\reorganizacao-2026-11\`; decision-log §28; `reorganizar_cgov.py` v1.2.2 e `gerar_indices.py` v0.1.0; *commits* `7f5a324` a `306ade5`. Resta a 4.11 (05/12/2026) |
| 5 — Repositório de desenvolvimento | ✅ | 07/11/2026 | Seis blocos no *branch* `implantacao/fase-5` (D37), com os *commits* `115b336` (D38), `0d0c8d2`, `b6a1bd5` (D39), `d94235e`, `4ab53c1` (D40) e `ee3b239` (D41); *merge* `--no-ff` `e305404`, com *push* conferido. Publicação: referência de `docs/` no `e305404` (33/33 SHA-256), `operacao/` 12/12. Decision-log §29. Encaminhado à Fase 6: P4 (9 skills desatualizadas), P5, E6 |
| 6 — Portfólio de skills | ✅ | 08/11/2026 | Ordem aprovada (D42). 6.1 ✅: 28 skills exportadas para `local/installed-reference/_export_2026-11-07/` (39/39 SHA-256 contra a máquina do Coordenador); `COMPARACAO.md`; 12 divergências decididas (D43); decision-log §30. Decisões 6.6 (D4) e 6.9(a) (D44); decision-log §31. Pasta de prompts analisada; etapa 6.10 (D45); decision-log §32. 6.2 ✅: 14 skills em `skills/pgd/`, `skills/normativo/` e `skills/cgge-fgbio/` (D46); decision-log §33. Skills do PGD renomeadas com o prefixo `pgd-` (D47); decision-log §34. 6.3 ✅: caminhos neutros, `AGENTS.md` por papel, ADR-006 aceito (D48); decision-log §35. 6.5 ✅: descrições ≤ 950, `cgov-gestao-riscos` rebaseada, eval da `cgov-nt-01` (D49); decision-log §36. 6.9(b)–(d) ✅: roteiro com cinco subsídios, 8 divergências, ampliações, procedimento v2 e modelo (D50); decision-log §37. 6.4 ✅: `cgov-gestao-acervo` e `cgov-triagem-processo-sei` em `skills/escritorio/`; gerador de índices publicado (D51); decision-log §38. E8 ✅: Portarias nº 271/2013 e nº 129/2020 aplicadas (D52); decision-log §39. 6.10 ✅: quatro skills temáticas novas (D53); decision-log §40. *Commit* `0d85240` publicado (35/35); S1 resolvida. 6.7 ✅: OCR aprovado (96,1% e 98,3%). 6.8 preparada (6.8a e 6.8b); D54 respondida; decision-log §41. Evals 129/134; correções; 6.8a gravada (D55, D56); decision-log §42. 6.8 ✅ (08/11): *commits* `b863ef3` e `066068b` publicados; 34 skills reinstaladas e conferidas; 8 nomes antigos excluídos; instruções v1.1; `--verificar` sem divergências; decision-log §43 |
| 7 — Plugin | 🟨 | 09/11/2026 | 7.0 ✅ (D57, *commit* `ebb6f1d`); ADR-005 aceito (D58, *commit* `d88a13b`); 7.1 ✅ gravada (32 skills em `plugins\cgov-escritorio\skills\`, aguardando *commit*); decision-log §45–46; próximas: 7.2 e 7.3 |
| 8 — Multiplataforma / WSL | ⬜ | | |
| 9 — Agentes | ⬜ | | |
| 10 — Power BI | ⬜ | | |
| 11 — Qualidade | ⬜ | | |
| 12 — Disseminação | ⬜ | | |

Legenda: ⬜ não iniciada · 🟨 em andamento · ✅ concluída · ⛔ bloqueada

---

## 12. Fontes

**Documentação oficial Anthropic:** [Organize work with projects (Cowork)](https://claude.com/docs/cowork/guide/projects) · [Plugins](https://claude.com/docs/plugins/overview) · [Plugin structure and testing](https://claude.com/docs/plugins/build) · [Plugin feature support across platforms](https://claude.com/docs/plugins/platform-support) · [Create custom skills](https://claude.com/docs/skills/how-to) · [Subagents (Claude Code)](https://code.claude.com/docs/en/subagents)

**Outras ferramentas:** [Google — Authoring Antigravity Skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills?hl=en) · [Microsoft Learn — Power BI MCP servers](https://learn.microsoft.com/power-bi/developer/mcp/mcp-servers-overview) · Maestri: [ustack.app](https://ustack.app/products/maestri), [AlternativeTo](https://alternativeto.net/software/maestri/about) (terceiros)

**Evidências internas:** GitHub `lpchagas/cgov-geral` (`67957fe`; `8787e0a`, `b981d66` e `46fb7ff` em 05/11); manifesto anterior `manifesto_pre_2026-11.sha256` (05/11); `docs/fluxos-de-trabalho.md`; `decision-log.md` §§25–27; inventário da pasta CGOV em 05/11/2026 (contagens, tamanhos e hashes; conteúdo não lido); arquivos `MOVIDO_PARA.txt` de 07/10/2026; manifesto de 04/11/2026.

---

## Apêndice A — Instruções do projeto "Escritório CGOV — Implantação" (v2, 06/11/2026 — sem a pasta CGOV, depois da Fase 4)

### Escritório CGOV — Implantação (desenvolvimento)

#### Papel
Você apoia o Coordenador de Governança (CGOV/CGGE/ICMBio) na implantação e manutenção do Escritório
Virtual da CGOV: skills, agentes, comandos, documentação, scripts e painéis do repositório cgov-geral
(única pasta vinculada). A reorganização da pasta operacional CGOV terminou na Fase 4; essa pasta
não fica mais vinculada a este projeto. Este projeto NÃO produz Notas Técnicas nem análises de processos: isso é feito no
projeto "Escritório CGOV — Operação".

#### Fontes de verdade
- Repositório: C:\Projetos\cgov-geral (GitHub privado https://github.com/lpchagas/cgov-geral).
- Plano: C:\Projetos\cgov-geral\docs\plano-implantacao.md (até 07/11/2026, na raiz, como
  cgov-geral-plano-implantacao.md). Siga a fase indicada.
- Regras do repositório: C:\Projetos\cgov-geral\AGENTS.md e C:\Projetos\cgov-geral\CLAUDE.md.
  Fluxos: C:\Projetos\cgov-geral\docs\fluxos-de-trabalho.md.
- Decisões: C:\Projetos\cgov-geral\docs\governance\decision-log.md e C:\Projetos\cgov-geral\docs\adr\.
  Pendências: C:\Projetos\cgov-geral\docs\governance\pendencias.md e, na operação,
  %USERPROFILE%\My Drive\10_Institucional\CGOV\90_escritorio-virtual\manutencao\PENDENCIAS.md
  (este projeto não tem acesso à pasta CGOV: peça ao Coordenador o conteúdo ou o vínculo temporário).

#### Regras obrigatórias
1. Antes de mover, renomear, excluir, reinstalar, fazer commit ou push: mostre a lista do que vai mudar
   e aguarde confirmação explícita. Nunca exclua: use a quarentena 99_arquivo/_a-excluir_<data>/.
2. A pasta CGOV não é vinculada a este projeto. Mudanças nela saem de operacao/ (publicação conferida
   por SHA-256) ou são feitas no projeto "Escritório CGOV — Operação"; movimentação em lote só por mapa
   CSV aprovado e conferido por SHA-256, com vínculo temporário autorizado pelo Coordenador.
3. Não altere o conteúdo de documentos de processos, normas ou NTs; apenas mova, renomeie e crie
   fichas e índices.
4. Nada de dados pessoais, matrículas, documentos SEI ou caminhos pessoais em plugins/, operacao/ ou
   docs/; rode scripts/verificar_sanitizacao.py antes de cada commit que toque nessas pastas.
5. Mudança de skill: fonte → evals (skill-creator) → validação → decision-log → commit →
   publicar_operacao.py → reinstalar → verificação de paridade.
6. Não reescreva o histórico do decision-log; acrescente decisões ao final.
7. Nunca invente norma, número ou dado; sinalize lacunas com ⚠️ e pergunte.
8. A cada etapa concluída ou decisão recebida, ATUALIZE INTEGRALMENTE o arquivo do plano, seguindo a
   lista de verificação da seção "Regra de manutenção deste plano" (cabeçalho, sumário, ADRs, mapa,
   visão geral 6.1, seção da fase, riscos, decisões, quadro, Apêndice G, coerência). Não declare a
   etapa concluída antes disso. Depois, proponha o commit "docs(plano): …".

#### Forma de trabalho
Uma fase por sessão. Divida em subtarefas, explique a abordagem antes de executar, justifique as
conclusões e verifique o resultado (arquivo aberto, comando executado, hash comparado) antes de
declarar uma etapa concluída. Ao final, aplique a regra 8 (atualização integral do plano).

#### Git
Commit e push pelo Claude Code ou pelo PowerShell do Coordenador, se o shell do Cowork não puder
apagar os arquivos de trava do Git na pasta vinculada. O shell do Cowork não tem credencial do
GitHub: verificações remotas (git fetch, git ls-remote) e push ficam no PowerShell do Coordenador.

#### Interação com o Coordenador
9. Decisões: sempre que algo depender de decisão do Coordenador, apresente perguntas de múltipla
   escolha clicáveis, com a opção recomendada em primeiro lugar e marcada "(Recomendado)".
10. PowerShell: quando o Coordenador precisar rodar algo no terminal, entregue o script completo,
    pronto para copiar e colar, começando por Set-Location no caminho completo e terminando com
    comandos de conferência (por exemplo, git status e git log).
11. Caminhos: ao citar pasta ou arquivo, use o caminho completo do Windows
    (por exemplo, C:\Projetos\cgov-geral\docs\fluxos-de-trabalho.md), nunca só o nome.
12. Fechamento: termine toda resposta com "Próximos passos", indicando o que vem a seguir e um
    prompt sugerido para a próxima interação com o Claude.

---

## Apêndice B — Instruções do projeto "Escritório CGOV — Operação" (versão 1.1, 07/11/2026 — etapa 6.8)

Fonte versionada: `C:\Projetos\cgov-geral\docs\system-instructions\escritorio-cgov-operacao.md`. A v1.0 (05/11/2026, etapa 4.8) substituiu o `escritorio-cgov.md`, arquivado em `C:\Projetos\cgov-geral\archive\system-instructions\escritorio-cgov_ate-2026-11-05.md`. A **v1.1** (6.8a) lista as skills com os nomes reinstalados (`pgd-*`, as da 6.4 e da 6.10), troca a seção de caminhos de transição pela de caminhos por papel (ADR-006, D48) e passa os índices ao gerador publicado. **Colada no projeto Operação em 07/11/2026, depois da reinstalação das 34 skills**; a tabela "Locais antigos" do `AGENTS.md` entrou na 6.8b.

> **Texto removido em 09/11/2026** (regra "link, não duplique": [`convencoes-documentacao.md`](convencoes-documentacao.md)). O bloco de instruções que ficava aqui era uma cópia da versão 1.1; a **fonte única** é [`system-instructions/escritorio-cgov-operacao.md`](system-instructions/escritorio-cgov-operacao.md). O texto anterior permanece no histórico do Git (por exemplo, no *commit* `449dbf0`, plano v3.48).

---

## Apêndice C — Manifesto do plugin

`plugins/cgov-escritorio/.claude-plugin/plugin.json`:

```json
{
  "name": "cgov-escritorio",
  "displayName": "Escritório CGOV — ICMBio",
  "version": "1.0.0",
  "description": "Skills, agentes e comandos da Coordenação de Governança do ICMBio: Notas Técnicas (suíte cgov-nt), análise normativa, gestão de riscos, AIR/ARR, cadeia de valor, regimento interno, PGR, PGD, QCF, gestão do acervo e documentação de painéis.",
  "author": { "name": "CGOV/CGGE/ICMBio" }
}
```

`name` é a identidade permanente do plugin. Validação: `claude plugin validate .\plugins\cgov-escritorio`. O `marketplace.json` (opcional, Fase 7.7) segue o modelo da v2.

---

## Apêndice D — Modelo de agente (`agents/revisor-normativo.md`)

```markdown
---
name: revisor-normativo
description: Revisão independente de Notas Técnicas e pareceres da CGOV. Use depois de redigir qualquer capítulo ou antes de consolidar a NT, para conferir citações normativas, siglas, tempo verbal e numeração.
tools: Read, Grep, Glob
model: opus
skills: cgov-saneamento-legistica
---

Você revisa, não redige. Para o texto indicado:
1. Liste cada citação normativa (norma, número, data, artigo/inciso) e confira em 03_normativos.
   Classifique: confirmada / divergente / não localizada (⚠️).
2. Verifique a disciplina de siglas PGR, PGRI, PGD e PGE (revogada).
3. Verifique o presente do indicativo e a numeração "### Capítulo N" / "#### N.1".
4. Entregue uma tabela de achados (trecho, problema, evidência, correção sugerida).
Nunca altere arquivos. Nunca invente norma; na dúvida, marque ⚠️.
```

---

## Apêndice E — Rascunhos da camada de navegação da raiz (fonte: `operacao/`)

> **Texto removido em 09/11/2026.** Os rascunhos E.1 (`CGOV\LEIA-ME.md`) e E.2 (`CGOV\AGENTS.md`) viraram os arquivos de `operacao/` no lote (a) da Fase 4 (v3.11), com ajustes. Fontes vigentes: [`../operacao/LEIA-ME.md`](../operacao/LEIA-ME.md) e [`../operacao/AGENTS.md`](../operacao/AGENTS.md), publicados na raiz da pasta CGOV por `publicar_operacao.py`. Os rascunhos originais permanecem no histórico do Git.

---

## Apêndice F — Modelos (fonte: `operacao/modelos/`)

> **Texto removido em 09/11/2026.** Os modelos F.1 (`_LEIA-ME.md` de área) e F.2 (`PROCESSO.md`) viraram os arquivos de `operacao/`; o F.3 (`_INDICE.md`) é gerado por `scripts/gerar_indices.py`. Fontes vigentes: [`../operacao/01_processos/_LEIA-ME.md`](../operacao/01_processos/_LEIA-ME.md) (e os `_LEIA-ME.md` das demais áreas) e [`../operacao/90_escritorio-virtual/modelos/processo/PROCESSO.md`](../operacao/90_escritorio-virtual/modelos/processo/PROCESSO.md). Os rascunhos originais permanecem no histórico do Git.

---

## Apêndice G — Evolução do plano

| Versão | Base | Mudança principal |
|---|---|---|
| v1 (04/11) | Zip de 30/09 | Primeira análise; restauração a partir do zip |
| v2 (04/11) | GitHub `4960e11` | Preserva a separação desenvolvimento × operação; Windows; plugin; dois projetos Cowork |
| v3.0 (05/11) | GitHub `67957fe` + inventário da pasta CGOV | Rearranjo dos **dois** repositórios; camada de navegação em Markdown; quarentena; projetos Cowork renomeados ("Implantação" e "Operação"); revisão dos projetos por processo; fases reordenadas (desenho e reorganização antes de scripts, skills e plugin) |
| v3.1 (05/11) | Decisões D10–D16 | Fase 2 concluída; regra de manutenção integral do plano (seção própria + Apêndice A, regra 8); coluna Situação na visão geral 6.1; processo da NT 27/2026 confirmado (SEI nº 02070.017019/2026-34); etapa 3.A.0 (versionar o plano); limitação de compartilhamento resolvida |
| v3.2 (05/11) | Dúvida sobre a criação dos projetos | Projetos criados no Claude Desktop (aba Cowork), não no navegador; como vincular pastas adicionais; pastas de cada projeto explicitadas (3.A e 4.8) |
| v3.3 (05/11) | Etapa 3.A concluída; D17 e D18 | Fase 3 em andamento; coluna Situação e Resultado na 3.A; `main` = `8787e0a`; limitação da credencial GitHub no shell do Cowork; divergência privado × público (⚠️); `.obsidian/` ignorado; regras de interação 9–12 no Apêndice A; dois riscos novos |
| v3.4 (05/11) | *Commit* `de0fa54`; capturas de tela do Claude Desktop; instruções do `cgov-geral-v1` | Repositório privado confirmado; menções a "público" corrigidas em `CLAUDE.md`, `README.md`, `AGENTS.md` e `docs/fluxos-de-trabalho.md` (D19); 3.A.4 a refazer (instruções estavam na descrição); 3.A.5 substituída (sem campo de links; URL nas instruções); 3.B.1–3.B.2 concluídas; Apêndice A com caminhos completos; dois riscos revistos |
| v3.5 (05/11) | *Commits* `6890b63` e `320007d`; D20 e D21 | 3.A.4 corrigida; 3.B.3 concluída (memória não preservada); 3.C concluída (inventário simplificado; vínculos antigos inexistentes); risco de quebra de projetos rebaixado para Baixo; 3.B.4 liberada; Fase 3 aguarda só o arquivamento do `cgov-geral-v1` |
| v3.6 (05/11) | *Commit* `be2f493`; arquivamento do `cgov-geral-v1` | 3.B.4 concluída; **Fase 3 concluída** (resultados 3.B e da fase); Fase 4 marcada como próxima |
| v3.7 (05/11) | Etapas 4.1 e 4.2; D22–D25 | **Fase 4 em andamento**: `scripts\reorganizar_cgov.py` criado; mapa CSV com 100% dos arquivos, aprovado com zero `a-decidir` e zero conflitos; Seções 5.5 e 5.6 atualizadas com as decisões e os achados por hash; três riscos novos (caminhos longos, Python no Windows, mapa desatualizado); prompt da 4.3–4.4 |
| v3.8 (05/11) | *Commit* `7f5a324`; simulação no Windows | Evidências do *commit* e da simulação no Windows (Python 3.12.10, zero conflitos); risco "Python no Windows" descartado |
| v3.9 (05/11) | *Commit* `b981d66`; etapas 4.3 e 4.4; D26 | 4.3 e 4.4 concluídas: `--planejar` refeito com mapa idêntico; manifesto anterior (2.831 hashes) 100% igual ao mapa; zero conflitos em todos os lotes; correção de 30 para 312 avisos de caminho longo; nova etapa 4.4a (encurtar os destinos antes do lote a); riscos de caminho longo e de mapa desatualizado revistos; prompt da 4.4a |
| v3.10 (05/11) | *Commit* `46fb7ff`; etapa 4.4a; D26 e D27 | 4.4a concluída: `reorganizar_cgov.py` v1.1.0 (`ENCURTAMENTOS_99`); 888 destinos encurtados, zero caminhos longos; 2 arquivos novos incorporados (processo 74); pasta CGOV congelada; mapa, manifesto e simulação refeitos (2.833 arquivos, zero conflitos); risco de mapa desatualizado materializado e mitigado; 4.7 com 74 fichas |
| v3.11 (05/11) | *Commit* `13ea143`; preparação do lote (a); D28 | Pasta CGOV conferida com o manifesto; `operacao/` antecipada (12 documentos a partir dos Apêndices E e F, com ajustes); 5.5 passa a ser conferência; ⚠️ verificação de sanitização ainda manual; *prompt* da conferência do lote (a) |
| v3.12 (05/11) | *Commit* `98789ef`; execução do lote (a); preparação do lote (b) | Lote (a) concluído e conferido; lote (b) detalhado; risco novo (skills e junções antigas durante os lotes); pendência das pastas antigas vazias (4.6); *prompt* da conferência do lote (b) |
| v3.13 (05/11) | *Commit* `cba655d`; execução do lote (b); preparação do lote (c) | Lote (b) concluído e conferido por SHA-256; lote (c) detalhado; pendências da série de NTs para a 4.7; *prompt* da conferência do lote (c) |
| v3.14 (05/11) | *Commit* `b9a33a3`; execução do lote (c); preparação do lote (d) | Lote (c) concluído e conferido; lote (d) detalhado por processo; pendência da NT 14 (Transição); *prompt* da conferência do lote (d) |
| v3.15 (05/11) | *Commit* `55172da`; execução do lote (d); preparação do lote (e) | Lote (d) concluído e conferido; lista completa das pastas vazias; lote (e) detalhado; pendência do nome de `fundo-rio-doce`; *prompt* da conferência do lote (e) |
| v3.16 (05/11) | *Commit* `657cb69`; execução do lote (e); preparação do lote (f) | Lote (e) concluído e conferido; lote (f) detalhado; conferência dos 9 arquivos de `_doutorado` fora da pasta por `Get-FileHash`; *prompt* da conferência do lote (f) |
| v3.17 (05/11) | *Commit* `224dc2c`; execução do lote (f); preparação do lote (g); D29 | Lote (f) concluído e conferido (inclusive os 9 arquivos fora da pasta); lote (g) detalhado; `reorganizar_cgov.py` v1.2.0 com `--limpar-vazias`; pendência das pastas vazias resolvida; *prompt* da conferência do lote (g) |
| v3.18 (05/11) | *Commit* `3dae008`; execução do lote (g); limpeza interrompida; 4.6 | Lote (g) concluído; **4.5 concluída** (sete lotes); **4.6 concluída** (manifesto posterior, 100%); limpeza das pastas vazias interrompida por `WinError 5`; `reorganizar_cgov.py` v1.2.1; risco novo (bloqueio do Drive); *prompt* da limpeza |
| v3.19 (05/11) | *Commit* `c88bd3e`; limpeza concluída; 4.7; D30 | Limpeza das 343 pastas vazias (causa: ReadOnly); **4.7 concluída**: `gerar_indices.py` v0.1.0; 74 fichas e 5 índices publicados; pendências de conteúdo para revisão gradual; risco do `WinError 5` resolvido; *prompt* da 4.8 |
| v3.20 (05/11) | *Commit* `377c34c`; preparação da 4.8; D31 | Apêndice B na versão final 1.0 (tradução de caminhos mantida até a Fase 6.3 via `AGENTS.md`; skills listadas; sem comandos do plugin); `escritorio-cgov.md` arquivado; navegação v2 republicada; `reorganizar_cgov.py` v1.2.2; *prompt* do teste da 4.8 |
| v3.21 (05/11) | *Commit* `d9c582e` (parcial); 4.8 concluída; D32 e D33 | Testes do projeto Operação aprovados; deriva da `cgov-nt-01` instalada (`_CGOV_NT`) registrada como risco materializado; `AGENTS.md` v3; teste na quarentena; 4.9 preparada (copiar e arquivar); *prompt* da 4.9 |
| v3.22 (06/11) | *Commit* `54ae16b`; 4.9 (cópias); D34 | Instruções dos projetos Cowork antigos copiadas para as fichas e para `local\archive`; resumos movidos da raiz do repositório; **novo objetivo D34** (modelo geral de análise de atos normativos): etapa 6.9 e Piloto 1 da Fase 11; *prompts* da 4.10 e da 6.9 |
| v3.23 (06/11) | *Commit* `306ade5`; 4.9 e 4.10; D35 | **Fase 4 concluída**: projetos antigos arquivados; `PROJETO.md` da GR2; mapa, manifestos e registros em `90_…\manutencao\reorganizacao-2026-11\`; decision-log §28; fim do congelamento; Apêndice A v2 (sem a pasta CGOV); próxima: Fase 5; 4.11 em 05/12/2026 |
| v3.24 (06/11) | *Commit* `f89121c`; D36 | Documentação do repositório atualizada para a estrutura nova (partes de 5.2, 5.8 e 5.9 antecipadas); `fluxos-de-trabalho.md` v2; `docs/governance/pendencias.md`; `.sh` do WSL bloqueados; risco novo mitigado; lembrete da 4.11 agendado para 05/12/2026 |
| v3.25 (06/11) | *Commit* `53ec122`; D37 | Ordem da Fase 5 em seis blocos, com a sanitização antecipada e a 5.6 antes da 5.1; *branch* `implantacao/fase-5`; coluna Situação nas etapas da Fase 5; dois riscos novos (junções sem bloqueio e remoção recursiva); *prompt* do bloco 1 |
| v3.26 (06/11) | *Commit* `a2effef`; bloco 1; D38 | `scripts/verificar_sanitizacao.py` v0.1.1 e `scripts/sanitizacao_permitidos.txt`; resultado do bloco 1; caminhos pessoais do plano (inclusive o Apêndice A) trocados por `%USERPROFILE%`; números SEI como aviso, com as evals para a 6.8 (E6); `fluxos-de-trabalho.md`, `CLAUDE.md` e `pendencias.md` atualizados; *prompt* do bloco 2 |
| v3.27 (07/11) | *Commit* `115b336`; blocos 1 e 2 | Bloco 1 concluído (teste no Windows); bloco 2: `.gitattributes` (LF; CRLF para `.ps1`, `.bat` e `.cmd`; binários) e `.gitignore` (`/notas/`, Power BI), testados num clone com `--renormalize` sem ruído; *prompt* do bloco 3 |
| v3.28 (07/11) | *Commit* `0d0c8d2`; bloco 3 preparado; D39 | Bloco 2 concluído; bloqueios novos no `.claude/settings.json`, inclusive a pasta CGOV pelo caminho real (D39, antecipa a 8.1); `scripts/link_acervo.py` v0.1.0 testado; `.env.example` ativo; documentação ajustada; dois riscos mitigados e um novo (scripts fora do alcance das regras deny); *prompt* da conferência do bloco 3 |
| v3.29 (07/11) | *Commits* `9f3849b` e `b6a1bd5`; blocos 3 e 4 | Bloco 3 concluído (junções, `.env`, bloqueio testado; P1 resolvida); bloco 4: `scripts/publicar_operacao.py` v0.1.0 testado, `archive/scripts-wsl/README.md`, referências aos `.sh` atualizadas (P2 resolvida; P3 para a 5.10); 5.4 concluída; risco dos `.sh` descartado; *prompt* da conferência do bloco 4 |
| v3.30 (07/11) | *Commit* `d94235e`; blocos 4 e 5; D40 | Bloco 4 concluído (`--verificar` no Windows: 9 skills desatualizadas, `operacao/` 12/12, referência de `docs/` em `4960e11`); bloco 5: 14 ADRs em `docs/adr/` (ADR-004 e 007 aceitos), `docs/catalogo-skills.md`, `docs/README.md`, referências ao novo caminho do plano; Apêndice A com o caminho novo; *prompt* do bloco 6 |
| v3.31 (07/11) | *Commit* `4ab53c1`; bloco 5; bloco 6 preparado; D41 | Bloco 5 concluído; revisão do diff do *branch* (sem achados); Decisão 29 no decision-log; `.vscode/` ignorado; roteiro de *merge* `--no-ff`, *push* e publicação; *prompt* da conferência da publicação |
| v3.32 (07/11) | *Merge* `e305404`; publicação | **Fase 5 concluída**: *merge* `--no-ff` e *push*; publicação com `publicar_operacao.py` (referência de `docs/` no `e305404`, 33/33; `operacao/` 12/12); P3 resolvida; P7 nova (quarentena da publicação); `main` no cabeçalho; *prompt* da Fase 6 |
| v3.33 (07/11) | *Commit* `44310f2` (`fix(plano)`); 6.1; D42 e D43 | **Fase 6 em andamento**: ordem das etapas (D42); 6.1 concluída (exportação de 28 skills, 39/39 conferidos, `COMPARACAO.md`, 12 divergências decididas); evidência na Seção 1.1; coluna Situação nas etapas da Fase 6; riscos de deriva e de dados SEI atualizados; decision-log §30; P4 e catálogo atualizados; *prompt* do bloco 6.6 + 6.9(a) |
| v3.34 (07/11) | *Commit* `baa28cd` (v3.33); D4 | 6.6 decidida: skill `cgov-triagem-processo-sei` + `.md` mantido; Fase 0 com D5–D8 pendentes; E2 e catálogo atualizados; 6.9(a) aguardando o texto da Parte B.5 |
| v3.35 (07/11) | D44 | 6.9(a) decidida (6 questões da Parte B.5; tempo verbal conferido no Decreto nº 12.002/2024, art. 11, I, "e"); efeitos na 6.9(b)–(d) e na 6.3 registrados na etapa; decision-log §31; E1 atualizada; *prompt* da 6.2 |
| v3.36 (07/11) | *Commit* `0377662` (v3.35); D45 | Análise da pasta de prompts `02_dev-prompts` (evidência na Seção 1.1); nova etapa 6.10 (quatro skills) e ampliações da `nt-06` e da `cgov-modelar-fluxo` na 6.9(b); escopo da D4 (só CGOV); ordem da Fase 6 com dez passos; risco novo (prompts antigos); E7 (inciso II); critério 5 da Seção 8 ajustado; decision-log §32 |
| v3.37 (07/11) | *Commit* `3303f40` (v3.36); 6.2; D46 | **6.2 concluída**: 14 skills promovidas a `skills/pgd/`, `skills/normativo/` e `skills/cgge-fgbio/`, saneadas (nomes, e-mail, CPF de exemplo, caminhos absolutos, número SEI); ciclo quadrimestral como regra; `skillOverrides` com 28; documentação das famílias; C7 nova; P5 ampliada; decision-log §33; *prompt* da 6.3 |
| v3.38 (07/11) | D47 | 8 skills do PGD renomeadas com o prefixo `pgd-` antes do *commit* da 6.2 (pastas, `name:`, referências cruzadas, `skillOverrides`, catálogo, `overview.md`, pendências); 6.8 ampliada (instalar com os nomes novos, excluir os antigos da conta, atualizar as instruções da Operação); risco de duplicidade atualizado; decision-log §34 |
| v3.39 (07/11) | *Commit* `90e9a36` (v3.38); 6.3; D48 | **6.3 concluída**: 13 skills com caminhos neutros; seção "Caminhos por papel" no `AGENTS.md`; 5 papéis novos no `operacao/AGENTS.md`; `_LEIA-ME.md` de 03 e 06; `gerar_indices.py` v0.1.1; ADR-006 aceito; 6.8 com a regra da tabela "Locais antigos"; P5 e C7 atualizadas; decision-log §35; *prompt* da 6.5 |
| v3.40 (07/11) | *Commit* `0bfcbc4` (v3.39); 6.5; D49 | **6.5 concluída**: 8 descrições encurtadas; `cgov-gestao-riscos` rebaseada sobre a versão da conta e saneada; eval de gatilho da `cgov-nt-01` incorporado do *branch* (rótulos corrigidos); `loop_results/` no `.gitignore`; decision-log §36; *prompt* da 6.9(b)–(d) |
| v3.41 (07/11) | *Commit* `d5d144e` (v3.40) e publicação (36/36); 6.9(b)–(d); D50 | **6.9(b)–(d) concluídas**: Passo 3.2 da `cgov-nt-01` (cinco subsídios); capítulos `nt-03` a `07`; 8 divergências da Parte B.4; Modo 2 da `cgov-nt-06` e da `cgov-modelar-fluxo`; uso como subsídio na `cgov-air-arr` e na `cgov-gestao-riscos` (3.9); procedimento v2 e modelo de instruções; pasta de rascunhos da transcrição em `90_escritorio-virtual/transcricoes/` (corrige a D48); E1 e C3 atualizadas; decision-log §37; *prompt* da 6.4 |
| v3.42 (07/11) | *Commit* `3723745` (v3.41) e publicação (37/37); 6.4; D51 | **6.4 concluída** e skill da 6.6 criada: `skills/escritorio/` com `cgov-gestao-acervo` (5 modos, 5 evals) e `cgov-triagem-processo-sei` (3 evals); `publicar_operacao.py` v0.2.0 com `90_escritorio-virtual/ferramentas/`; `skillOverrides` com 30; E8 nova (Portaria nº 129/2020); decision-log §38; *prompt* da 6.10 |
| v3.43 (07/11) | *Commit* `d4f75c8` (v3.42) e publicação (37/37, `operacao/` 14/14); E8; D52 | **E8 resolvida**: Portarias nº 271/2013, nº 129/2020 e PFE/ICMBio nº 3/2021 lidas no acervo; espécies e vigência pela nº 129/2020; 13 arquivos corrigidos (`cgov-nt-06`, legística, AIR, comparar-versões, `nt-01`, triagem, `analista-processos-sei.md` v7.3, anexos do `analista-governanca`, procedimento e modelo); C8 nova; decision-log §39 |
| v3.44 (07/11) | 6.10; D53 | **6.10 concluída**: `cgov-secretaria-colegiados`, `cgov-integridade`, `cgov-carta-servicos` (script `classificar_entregas.py` v0.1.0, sem conexão a banco) e `cgov-projetos-cooperacao` em `skills/thematic/`, 12 evals; roteamento da triagem, `settings.json` e catálogo; Carta no inciso VI; achados (Portaria nº 4.007/2023 revogada, quórum do CTGRIC, credencial no script original); pendências S1 nova, C3 e C8 ampliadas; decision-log §40 |
| v3.45 (07/11) | *Commit* `0d85240` (v3.44) e publicação (35/35); S1; 6.7; 6.8 | S1 resolvida; roteiro de validação do `ocr_windows.ps1` (dois PDFs sem camada de texto, critério de cobertura); 6.8 preparada em duas entregas (6.8a antes e 6.8b depois da reinstalação); levantamento dos evals (13 skills sem casos); D54 respondida (evals das alteradas; E9) |
| v3.46 (07/11) | 6.7 | **6.7 concluída**: OCR do Windows aprovado (96,1% e 98,3%); erro típico nos ordinais e no `§` levado ao Passo 2 da `cgov-transcrever-normativos` (preparo 6.8a); E5 resolvida; E10 nova |
| v3.47 (07/11) | Evals da 6.8; D55, D56; 6.8a | Evals das 9 skills alteradas: 129/134 (96%); correções em 10 skills; rascunho condicionado na `cgov-nt-06` (D55); exceções ao futuro do presente (D56); 6.8a gravada (23 arquivos); Apêndice B v1.1; E6 resolvida; E11 nova; decision-log §42 |
| v3.48 (08/11) | *Commits* `b863ef3` (v3.47) e `066068b` (6.8b), publicados; reinstalação conferida | **Fase 6 concluída**: primeira tentativa de reinstalação sem efeito na conta (34 divergências); depois, 34 skills reinstaladas pelo Coordenador e conferidas pelo Claude na conta, 8 nomes antigos do PGD excluídos, instruções v1.1 coladas no projeto Operação; 6.8b ("Locais antigos" no `AGENTS.md`; fluxos de trabalho); `--verificar` sem divergências; P4 e P5 resolvidas; decision-log §43; próxima: Fase 7 |
| v3.49 (09/11) | Revisão documental; D57 | Etapa 7.0: `docs/INDICE.md`, convenções, rastreabilidade, índices gerados, frontmatter, dois scripts de verificação; Apêndices B, E e F viram links; `pendencias.md` reorganizado (E9: 20 skills sem evals; E12–E14); decision-log §44. ADR-001, 009 e 011 aceitos |
| v3.50 (09/11) | Início da Fase 7; D58 | ADR-005 aceito como está (plugin único `cgov-escritorio`); E12 resolvida; decision-log §45; 7.1 ainda não executada (lista dos `git mv` para confirmação) |
| v3.51 (09/11) | Etapa 7.1 | 32 skills movidas para `plugins\cgov-escritorio\skills\`; `plugin.json` 0.1.0 e README; caminhos corrigidos; catálogo regerado; `verificar_docs.py` varre `plugins/`; E14 resolvida; decision-log §46; `publicar_operacao.py` só volta a funcionar na 7.3 |

---

*Fim do plano v3.51 (etapa 7.1 gravada em 09/11/2026; antes, v3.50: ADR-005 aceito, e v3.49: etapa 7.0, revisão documental). Fases 1 a 6 concluídas (Fase 5 em 07/11/2026, *merge* `e305404`; Fase 6 em 08/11/2026, *commits* `b863ef3` e `066068b`, `--verificar` sem divergências). Próximas: etapas 7.2 e 7.3 da Fase 7 (plugin `cgov-escritorio`), na mesma sessão ou em nova sessão do projeto "Escritório CGOV — Implantação". Seguem as pendências E9, E10 e E11, o piloto 6.9(e) (Fase 11), a 4.11 (quarentena de 05/11, a partir de 05/12/2026, com lembrete agendado) e a revisão das quarentenas de publicação (P7, a partir de 07/12/2026).*

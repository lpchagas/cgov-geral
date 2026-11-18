---
tipo: registro
status: vigente
atualizado_em: 2026-11-09
relacionados: [docs/governance/decision-log-indice.md, docs/governance/rastreabilidade.md]
---

# Registro de Decisões — Suíte Canônica `cgov-nt` e Escritório de Trabalho da CGOV

**Processo/Iniciativa:** Desenvolvimento de ferramentas de IA para suporte ao
trabalho da Coordenação de Governança (CGOV/ICMBio)
**Data de registro:** 05/07/2026 (última atualização: 29/08/2026)
**Responsável:** Coordenação de Governança — CGOV/CGGE/ICMBio
**Natureza deste documento:** Registro cronológico e decisório, para arquivamento
junto ao acervo da CGOV, do processo de diagnóstico, desenho, validação e adoção
da suíte de skills `cgov-nt-01` a `07` no Claude.

> **Nota de publicação:** os caminhos de pastas e nomes de arquivos em decisões
> históricas descrevem a estrutura vigente à época e não constituem instruções
> operacionais atuais. Consulte `README.md` e `docs/architecture.md` para os
> caminhos vigentes.

---

## 1. Motivação e escopo original

O Coordenador de Governança solicitou análise das skills então em uso pela CGOV
para elaboração de Notas Técnicas — duas famílias específicas por processo:
`cgov-pgd-sk1` a `sk8` (processo SEI de referência — revisão da IN
ICMBio nº 14/2025, regras do PGD) e `cgov-pspeadbio-sk1` a `sk5` (Processo SEI
Plano Setorial/PSPEADBio) — com o objetivo de propor
um modelo canônico, sequenciado e reutilizável para qualquer processo em análise
na CGOV, sem necessidade de customização individual por projeto.

## 2. Diagnóstico (fase 1)

Constatou-se que as 13 skills existentes eram **funções de despacho** —
instruíam a execução de trechos de um arquivo `CLAUDE.md` específico de cada
processo, hardcodando nomes de pasta, de arquivo de dados e de processo SEI.
Isso as tornava não reutilizáveis para novos processos, com duplicação de
boilerplate entre as duas famílias e inconsistências de formatação entre elas
(ex.: dois padrões de numeração de capítulo diferentes).

**Decisão 1:** substituir as 13 skills por uma suíte canônica de 7 skills
(`cgov-nt-01` a `07`), mapeadas 1:1 à estrutura oficial da Nota Técnica da CGOV,
sem dependência de `CLAUDE.md` externo — cada skill autocontida, com o estado do
processo mantido em um arquivo `NT_ESTADO.md` criado dinamicamente pela própria
suíte.

## 3. Fundamentação regimental

Para que a triagem (`cgov-nt-01`) enquadrasse qualquer demanda corretamente, foi
extraído e transcrito o Art. 37 (competências da CGOV) da Portaria ICMBio nº
5.592/2025, via OCR do PDF fornecido (sem camada de texto) seguido de
conferência visual da página renderizada.

**Decisão 2:** o texto do Art. 37 foi incorporado apenas na skill `cgov-nt-01`,
que passa a ser a fonte de verdade regimental de toda a suíte.

## 4. Construção, validação e piloto (fase 2)

As 7 skills foram construídas, validadas (`quick_validate.py`) e empacotadas.
Foi montado um conjunto de 16 casos de teste (`evals.json`, 2-3 por skill) e
executado um piloto manual contra dados reais do processo SEI
de referência (351 respondentes da consulta sobre a IN nº 14/2025),
comparando a saída da nova suíte com a Nota Técnica nº 20/2026/CGOV, já
protocolada e encaminhada à PFE/ICMBio.

**Achados do piloto e decisões correspondentes:**

| Achado | Decisão |
|---|---|
| A necessidade de quesitos PFE não pode ser inferida do Tipo de dado (a NT real, Tipo B, precisou de PFE) | `cgov-nt-01` e `cgov-nt-06` passaram a decidir a necessidade de PFE pelo destino do produto, não pelo Tipo |
| A NT real usa capítulos autônomos (`### Capítulo N` + `#### N.1`), não a numeração subordinada `4.1/4.1.1` herdada de uma das famílias antigas | Suíte corrigida para o padrão real, em `cgov-nt-03`, `04`, `05` e `07` |
| A prosa da NT real usa presente do indicativo, não futuro simples (regra que só se aplica ao texto do próprio ato normativo, por força do Decreto nº 12.002/2024) | `cgov-nt-03` passou a distinguir os dois registros |
| A Proposição real usa `(i), (ii), (iii)` e os Encaminhamentos usam destinatário em negrito, não alíneas/romanos maiúsculos | `cgov-nt-07` corrigida para o formato real |

## 5. Correção com a fonte primária da Portaria nº 271/2013 (fase 3)

O usuário forneceu o texto integral da Portaria ICMBio nº 271/2013. A leitura
do Anexo II revelou que a tabela de "8 quesitos" herdada das skills antigas
estava **incompleta** (faltavam os quesitos 2, 3, 5 e 6) e **parcialmente
incorreta** (dois itens da tabela antiga — "revogação" e "técnica
legislativa" — pertencem ao Anexo I, não ao questionário do Anexo II).

**Decisão 3:** `cgov-nt-06` foi reescrita por completo, com a transcrição fiel
dos 8 quesitos reais do Anexo II e de todos os seus subitens, incluindo nota
sobre a numeração inconsistente do documento original (rotulada 10-14, mas com
subitens reais 4-8).

## 6. Análise comparativa final e exclusão das skills antigas

Com a suíte `cgov-nt` corrigida e validada, foi feita a análise comparativa
1:1 contra as 13 skills antigas (ver `01_relatorios/RELATORIO_cgov-nt.md`,
Seção 10.2). Concluiu-se que a suíte nova cobre integralmente, e de forma mais
precisa, todas as funções das 13 skills antigas.

**Decisão 4:** as 13 skills antigas (`cgov-pgd-sk1` a `sk8`,
`cgov-pspeadbio-sk1` a `sk5`) foram removidas do ambiente de skills do Claude,
após backup completo (pasta `03_skills_arquivadas_backup`). Ressalva registrada:
o processo SEI de referência (PSPEADBio) estava em andamento à data
da exclusão (últimos arquivos de 15/06/2026); o `CLAUDE.md` e os arquivos desse
processo permanecem intactos no Google Drive, e qualquer capítulo pendente pode
ser produzido pela suíte nova.

## 7. Complementação do acervo e resolução da pendência do Art. 37 (fase 4 — 05/07/2026)

A pedido do usuário, foram copiados para `04_fontes_normativas`:
`cgov-analista-governanca_v2.md` (documento de identidade/comandos do
assistente CGOV, uma das fontes de diagnóstico original) e uma verificação do
Art. 37 a partir de segunda fonte.

Ao localizar, na pasta `CGOV_Normativas` do usuário, uma versão do PDF da
Portaria ICMBio nº 5.592/2025 com camada de texto extraível (mais leve — 1,7 MB
— que o PDF de 44 MB fornecido originalmente nesta conversa, uma impressão sem
texto), foi possível extrair o Art. 37 diretamente, sem OCR.

**Decisão 5:** a extração direta confirmou, palavra por palavra, a transcrição
já em uso em `cgov-nt-01-triagem` desde a fase 1. A pendência de validação
jurídica do Art. 37, registrada como prioridade alta na fase 1, é considerada
**resolvida** — documentado em
`04_fontes_normativas/Art_37_Portaria_5592-2025_texto_verificado.md`.

**Limitação de ferramenta registrada:** não foi possível copiar o arquivo PDF
completo da Portaria nº 5.592/2025 para `04_fontes_normativas` — as ferramentas
de acesso ao computador do usuário disponíveis nesta sessão só gravam conteúdo
em texto, não arquivos binários, entre pastas do mesmo computador. O original
permanece em
`<Google Drive>\CGOV\CGOV_Normativas\20251211_Portaria ICMBio 5.592_Regimento Interno.pdf`,
disponível para cópia manual se desejado.

## 8. Estado final e localização dos artefatos

Toda a documentação e as skills foram organizadas em
`C:\_cowork\cgov-geral-v1`, como acervo inicial do futuro projeto **"Escritório
de Trabalho da CGOV"**:

```
C:\_cowork\cgov-geral-v1\
├── 00_sincronizado_automaticamente_pelo_chat\   (snapshots intermediários do chat — não editar)
├── 01_relatorios\                                (relatório técnico completo + estado do piloto)
├── 02_skills_cgov-nt\                            (as 7 skills canônicas, código-fonte + evals)
├── 03_skills_arquivadas_backup\                  (as 13 skills antigas, preservadas)
├── 04_fontes_normativas\                         (Portaria nº 271/2013; doc. de identidade CGOV; Art. 37 verificado)
├── REGISTRO_DECISOES.md                          (este documento)
├── RELATORIO_cgov-nt.md
├── RESUMO_ESTRUTURADO.md
└── SYSTEM_INSTRUCTIONS_Escritorio_CGOV.md
```

## 9. Reorganização da biblioteca e novas skills (fase 5 — 05/07/2026)

A pedido do Coordenador, foi realizada reorganização da biblioteca de documentos
do projeto e análise de lacunas de cobertura de skills frente às competências
do Art. 37.

**Reorganização executada:**
- Removido da raiz o arquivo `RELATORIO_cgov-nt.md` (rascunho inicial, 371
  linhas) — o canônico (485 linhas, incluindo piloto) está em
  `01_relatorios/RELATORIO_cgov-nt.md`. O rascunho foi arquivado em
  `00_sincronizado_automaticamente_pelo_chat/RELATORIO_cgov-nt_v0_rascunho.md`.
- Removido da raiz o arquivo `REGISTRO_DECISOES_ADENDO.md` — seu conteúdo já
  havia sido integrado a este documento (Seções 7 e 9); o próprio arquivo
  sinalizava que podia ser removido.
- Criada a pasta `05_novas_skills_propostas/` para abrigar as skills novas
  aguardando instalação.

**Análise de lacunas de skills (Art. 37 × cobertura atual):**

| Inciso Art. 37 | Competência | Skills existentes | Lacuna |
|---|---|---|---|
| II | Política de Governança Institucional | cgov-nt-*, cgge-especialista-pgd | Parcial |
| III | Gestão por Processos | cgov-modelar-fluxo, cgov-auditoria-competencias, cgov-saneamento-legistica | Boa cobertura |
| IV | Regimento Interno | cgov-saneamento-legistica, cgov-nt-* | Parcial |
| V | Quadro de Cargos (QCF) | Nenhuma | ❌ (baixa frequência) |
| VI | Cadeia de Valor / DFT | Nenhuma | ❌ **Prioridade alta** |
| VII | PGD (com CGGP) | cgge-especialista-pgd, cgov-*-entrega | Boa cobertura |
| VIII | PGR (Programa de Gestão para Resultados) | Nenhuma | ❌ (avaliar) |
| IX | Gestão de Riscos / CTGRIC | Nenhuma | ❌ **Prioridade alta** |
| X | AIR / ARR | Nenhuma | ❌ **Prioridade alta** |

**Decisão 6:** criar rascunhos de 5 novas skills para os incisos IV, VI, VIII,
IX e X, depositados em `05_novas_skills_propostas/`:

- `cgov-gestao-riscos` (Art. 37, IX) — ciclo de gestão de riscos,
  Portaria ICMBio nº 975/2021, matriz 5×5, SITAI.
- `cgov-air-arr` (Art. 37, X) — AIR e ARR, Decreto nº 10.411/2020, dispensa,
  análise de alternativas, estrutura do relatório.
- `cgov-cadeia-valor` (Art. 37, VI) — Cadeia de Valor, SIPOC, Catálogo de
  Produtos/Serviços, DFT (Portaria SEDGG/ME nº 7.888/2022).
- `cgov-regimento-interno` (Art. 37, IV) — coordenação da atualização do RI:
  diagnóstico de gatilho, articulação interunidades, redação de minuta,
  verificação de hierarquia normativa e submissão à PFE.
- `cgov-pgr` (Art. 37, VIII) — implementação do PGR: ciclo de gestão por
  resultados, indicadores institucionais, alinhamento com PE, projetos de
  inovação e relatório de monitoramento (Portaria ICMBio nº 1.572/2023).

Instalação pendente: via Customize → Skills no Claude (copiar o conteúdo de
cada `SKILL.md` de `05_novas_skills_propostas/` para uma nova skill).

---

## 10. Revisão do Analista de Processos SEI e instalação das 5 skills (fase 6 — 04/08/2026)

### 10.1. Revisão do System Instructions do Analista de Processos SEI (v6.0 → v7.0)

O Coordenador submeteu à análise o documento "System Instructions — Analista de
Processos SEI (CGOV)", versão 6.0, de 13/03/2026. A auditoria seção a seção,
cruzada com o acervo deste projeto e com verificação das normas federais em
fonte primária, identificou os seguintes achados críticos:

| Achado | Natureza |
|---|---|
| Seções 4.3 (Riscos) e 4.4 (AIR/ARR) em branco — `[INSERIR TEXTO]` | Lacuna crítica: o assistente operava sem base para dois dos quatro eixos |
| Competência da CGOV referida ao **"Art. 50"** do Regimento Interno, em dois comandos, contradizendo a própria Seção 3 do documento (que cita corretamente o Art. 37) | Erro factual — instruía o modelo a citar dispositivo errado em minuta oficial |
| Estrutura de Nota Técnica divergente do padrão da CGOV validado por piloto contra NT real e por 16 NTs históricas | Erro estrutural |
| `INDICAR_NORMAS` pedia jurisprudência do TCU "se houver no seu conhecimento" | Convite direto à alucinação de acórdãos |
| Bloco final afirmava que o assistente "entrega 80-90% do documento pronto" | Métrica de projeto lida como instrução — pressão para completar lacunas por inferência |
| Omissão da Portaria ICMBio nº 271/2013, que rege a forma dos atos do Instituto e está na pasta deste projeto | Omissão relevante |
| Ausência de: delimitador de raciocínio interno; verificação de legibilidade da fonte; autoverificação pré-entrega; citação de evidência; minimização LGPD; sigilo LAI; exigência de revisão humana | Lacunas de confiabilidade |
| Divergência de cabeçalho da NT: `CGOV/CGGE/DIPLAN/ICMBio` (v6.0) × `CGOV/CGGE/GABIN/ICMBio` (`cgov-analista-governanca_v2.md`) | ⚠️ **Pendência aberta** — não resolvida pelas fontes disponíveis |

**Decisão 7:** produzir a versão **7.0**, gravada em
`SYSTEM_INSTRUCTIONS_Analista_Processos_SEI_v7.md`, com dez seções, integrada ao
ecossistema "Escritório CGOV" (nova Seção 3 de roteamento para skills), com o
texto verificado do Art. 37 embutido, base normativa ampliada de 4 para cerca de
30 referências com status de verificação (✅/🔎/⚠️), e nova Seção 8 de guardrails
com precedência sobre as demais. O comando `/REDIGIR_NOTA_TECNICA` passa a
**delegar** à suíte `cgov-nt`, em vez de produzir NT em formato próprio.

### 10.2. Correção técnica da skill `cgov-air-arr`

A verificação do Decreto nº 10.411/2020 contra o texto oficial (Planalto)
revelou que tanto a skill `cgov-air-arr` quanto o
`cgov-analista-governanca_v2.md` tratavam como **"dispensa"** hipóteses que a
norma classifica como **não incidência**.

A distinção não é terminológica: na **não incidência** (art. 3º, § 2º) a
obrigação não incide sobre o ato; na **dispensa** (art. 4º) a obrigação incide
mas é afastada, exigindo decisão fundamentada (*caput*), nota técnica de
fundamentação (§ 1º) e, se por urgência, identificação do problema regulatório e
dos objetivos (§ 2º) mais ARR obrigatória em até três anos (art. 12).

**Decisão 8:** reescrever o Passo 1.1 da `cgov-air-arr` com a transcrição
verificada dos arts. 1º (§§ 1º e 3º), 2º (II), 3º (§ 2º) e 4º (I a VIII e
§§ 1º a 3º), acrescentando quadro comparativo dos dois regimes e redação-modelo
para ato *interna corporis* do ICMBio. Estendida também a ancoragem dos Passos
1.3 a 1.5 e do Modo 2 (ARR) aos arts. 6º, 7º, 9º, 10, 12, 13, 15 e 21, com nota
sobre as alterações dos Decretos nº 11.243/2022 e nº 11.259/2022.

### 10.3. Instalação das 5 skills temáticas do Art. 37

**Decisão 9:** as cinco skills de `05_novas_skills_propostas/` foram instaladas
na conta Claude em 04/08/2026:

| Skill | Inciso do Art. 37 | ID |
|---|---|---|
| `cgov-gestao-riscos` | IX — Gestão de Riscos / CTGRIC | `skill_01MM7RvJBUgio48k7Eo2au7L` |
| `cgov-cadeia-valor` | VI — Cadeia de Valor / DFT | `skill_014MGvvTe5xaHDsDLcyJYPH5` |
| `cgov-pgr` | VIII — Programa de Gestão para Resultados | `skill_01U2oHksKRHjivmnF9DRzEfB` |
| `cgov-regimento-interno` | IV — Atualização do Regimento Interno | `skill_01Ut2CyTLiFSafBLrszvQWcD` |
| `cgov-air-arr` | X — AIR e ARR | `skill_019SUJYV2Vgaz99TUMDg2jit` |

**Ajuste técnico registrado:** o campo `description` das skills instaladas está
limitado a **1.024 caracteres**. As cinco descrições originais excediam esse
limite (1.119 a 1.698 caracteres) e foram condensadas, preservando todos os
gatilhos de acionamento e as advertências de desambiguação — em especial a nota
da `cgov-pgr` distinguindo o Programa de Gestão para Resultados do PGD
(teletrabalho) e da PGRI (riscos). Os arquivos de `05_novas_skills_propostas/`
foram sincronizados com o texto efetivamente instalado e receberam os campos
`instalado_em` e `status` no *frontmatter*.

**Advertência de manutenção:** editar os arquivos em
`05_novas_skills_propostas/` **não altera** a skill instalada. Qualquer mudança
exige reinstalação com sobrescrita.

**Cobertura resultante:** 9 dos 10 incisos do parágrafo único do Art. 37 passam
a ter skill dedicada. O inciso V (Quadro Demonstrativo dos Cargos e Funções
Comissionadas Executivas) permanece o único descoberto.

---

## 11. Consolidação do acervo normativo e padronização de siglas (fase 7 — 04/08/2026)

### 11.1. Diretrizes recebidas do Coordenador

1. Cabeçalho oficial da Nota Técnica: `Nota Técnica nº [#]/[ano]/CGOV/CGGE/GABIN/ICMBio`.
2. Depósito de diversas normas até então ausentes em `04_fontes_normativas/`.
3. Movimentação do `cgov-analista-governanca_v2.md` para a raiz do projeto — o
   documento passa a ser o System Instructions **independente**, para configuração
   de assistentes autônomos (Gems, GPTs) fora do Claude Cowork.
4. Padronização de siglas: **PGR** = Programa de Gestão para Resultados
   (Portaria nº 1.572/2023); **PGRI** = Política de Gestão de Riscos e
   Integridade (Portaria nº 255/2020).

**Decisão 10 — cabeçalho da NT.** Fixado `CGOV/CGGE/GABIN/ICMBio`; a sigla
`DIPLAN`, que constava do v6.0 do Analista de Processos SEI, é **incorreta**. A
pendência aberta na fase 6 está encerrada. A skill `cgov-nt-03-introducao` já
adotava o padrão correto e não precisou de alteração.

**Decisão 11 — convenção de siglas.** Fixada e documentada em
`04_fontes_normativas/INDICE_FONTES_NORMATIVAS.md`, Seção 6:

| Sigla | Significado | Norma | Art. 37, § único |
|---|---|---|---|
| **PGR** | Programa de Gestão para Resultados e Inovação | Portaria ICMBio nº 1.572/2023 | VIII |
| **PGRI** | Política de Gestão de Riscos e Integridade | Portaria ICMBio nº 255/2020 | IX |
| **PGD** | Programa de Gestão e Desempenho (teletrabalho) | IN ICMBio nº 14/2025 | VII |
| **PGE** | Política de Gestão Estratégica | Portaria ICMBio nº 768/2020 | — |

A convenção não é arbitrária: a própria Portaria nº 975/2021 usa a sigla
**PGRI-ICMBio** em seu Anexo. As expressões "PGR de riscos", "PGR (riscos)" e
"Plano de Gestão de Riscos — PGR" foram eliminadas de todos os arquivos e
skills, e proibidas expressamente no texto das skills afetadas.

### 11.2. Reconstituição do Art. 37 verificado

O arquivo `Art_37_Portaria_5592-2025_texto_verificado.md` **havia desaparecido**
da pasta entre 05/07/2026 e 04/08/2026. Como o PDF integral da Portaria
nº 5.592/2025 passou a constar do acervo, o texto foi reextraído diretamente.

**Decisão 12:** o arquivo foi reconstituído. A nova extração — feita a partir do
PDF do acervo do projeto, fonte distinta da usada em 05/07/2026 (Google Drive do
usuário) — coincide **palavra por palavra** com a anterior. O Art. 37 tem agora
**três verificações independentes convergentes**. O arquivo recebeu notas de
leitura sobre a distinção entre os incisos do *caput* e os do parágrafo único, e
sobre as siglas PGR e PGRI.

### 11.3. Inventário do acervo e o problema dos arquivos ilegíveis

Criado `04_fontes_normativas/INDICE_FONTES_NORMATIVAS.md`, que classifica cada
arquivo por **legibilidade por máquina** — não apenas por presença.

**Achado relevante:** estar na pasta não significa ser utilizável. Três arquivos
importantes não podem ser lidos automaticamente:

| Arquivo | Problema |
|---|---|
| Portaria ICMBio nº 4.101/2023 (Política de Governança) | PDF com codificação de fonte que devolve texto embaralhado |
| Portaria ICMBio nº 1.164/2025 (Planejamento Estratégico) | idem |
| Portaria ICMBio nº 253/2026 (Programa de Integridade) | PDF sem camada de texto (digitalização) |

**Decisão 13:** esses três arquivos recebem o status 🔒 e o assistente está
**proibido de citar dispositivo, objetivo estratégico ou indicador** deles até
que haja versão legível. A legenda de status do v7.0 foi ampliada com os
símbolos 📖 (legível sob demanda) e 🔒 (ilegível por máquina).

### 11.4. Correção de fundo na skill `cgov-gestao-riscos`

A extração da Portaria nº 975/2021 revelou que a skill instalada em 04/08/2026
continha parâmetros **que não correspondiam à norma**:

| A skill dizia | A Portaria nº 975/2021 estabelece |
|---|---|
| Níveis "Baixo / Médio / Alto / **Crítico**" | "Baixo / Médio / Alto / **Extremo**" (Tabela 9) |
| Classificação por faixas do produto (1-4, 5-9, 10-16, 17-25) | Classificação por **máscara** sobre a matriz (Tabela 9) — produtos iguais podem ter níveis diferentes |
| Escalas "1 (Rara) a 5 (Quase Certa)" e "1 (Insignificante) a 5 (Catastrófico)" | "Muito baixa a Muito alta" (Tabela 5) e "Muito baixo a Muito alto" (Tabela 7), com coluna de Ocorrências e dimensões Custo/Prazo/Escopo/Qualidade (Tabela 6) |
| Risco residual por **reclassificação** de probabilidade e impacto | Risco Residual = Risco Inerente **×** multiplicador da eficácia do controle: Inexistente 1,00 · Fraco 0,80 · Mediano 0,60 · Satisfatório 0,40 · Forte 0,20 (Tabela 10) |
| Respostas "Evitar / Reduzir / Transferir / Aceitar" | "**Mitigar / Compartilhar / Evitar / Aceitar**" (Tabela 12) |
| 7 etapas genéricas | Etapas reais 4.1 a 4.7, com nomes próprios |
| Categorias não listadas | Operacional · Legal · Financeiro/Orçamentário · Reputação · Integridade (Tabela 3), com 6 subcategorias de integridade (Tabela 4) |
| Escalonamento ao CTGRIC | Riscos **Extremo** e **Alto** são comunicados ao **Comitê Gestor** (Tabela 11) |
| Sintaxe aproximada | Transcrição literal: *"Devido o(a) `<CAUSA>`, poderá ocorrer o(a) `<EVENTO DE RISCO>`, ocasionando o(a) `<CONSEQUÊNCIA>` e impactando o alcance do `<OBJETIVO ESTRATÉGICO>`."* |

**Decisão 14:** a skill foi **reescrita integralmente** a partir do texto extraído
e reinstalada com sobrescrita, incorporando as Tabelas 3 a 13 na íntegra, a
regra de precedência da Portaria nº 975/2021 sobre ISO/COSO/TCU/CGU e a
exigência de "mostrar a conta" em toda classificação de risco.

### 11.5. Correção de fundo na skill `cgov-pgr`

A leitura do texto integral da Portaria nº 1.572/2023 revelou problema análogo:
a skill descrevia dois eixos ("Gestão por Resultados" e "Inovação
Institucional") e um arcabouço completo de indicadores institucionais, ficha de
indicador, metas anuais e limiares de alerta (🟢 ≥90%, 🟡 70-89%, 🔴 <70%) —
**nada disso consta da norma**.

A estrutura real é: **três eixos** — Capacitação (arts. 8º-10), Consultoria
interna (arts. 11-14) e Laboratório de Inovação (arts. 15-18) — e **duas ações
transversais** — Gestão do Programa (arts. 22-25) e Rede de Multiplicadores
(arts. 19-21). O único instrumento de prestação de contas previsto é o
**Relatório Anual de Resultados** (art. 26).

**Decisão 15:** a skill foi reescrita e reinstalada, com glossário oficial do
art. 2º, advertência expressa de que a norma **não** institui painel de
indicadores (esse arcabouço pertence ao PGE/PE), registro das revogações do
art. 27 (Portarias nº 38/2021 e nº 531/2021) e nota sobre a nomenclatura
"CGOV/GABIN" usada pela norma de 2023 frente à estrutura vigente sob a Portaria
nº 5.592/2025.

### 11.6. Lição de método registrada

As Decisões 14 e 15 têm a mesma origem: **skills escritas antes de a norma
estar disponível em texto** descreviam metodologia por inferência plausível, e a
inferência plausível estava errada em pontos que afetariam produto oficial —
nome de nível de risco, fórmula de cálculo, estrutura de programa.

**Diretriz para o projeto:** nenhuma skill que opere sobre norma interna do
ICMBio deve ser considerada confiável enquanto o texto da norma não estiver
depositado e extraído em `04_fontes_normativas/`. Skills nessa condição devem
declarar a lacuna e pedir o anexo, em vez de descrever o método de memória.

### 11.7. Arquivos alterados nesta fase

| Arquivo | Alteração |
|---|---|
| `04_fontes_normativas/Art_37_..._verificado.md` | Reconstituído por nova extração |
| `04_fontes_normativas/INDICE_FONTES_NORMATIVAS.md` | **Criado** — inventário com status de legibilidade e convenção de siglas |
| `05_novas_skills_propostas/cgov-gestao-riscos/SKILL.md` | Reescrito e reinstalado (`skill_01EDSqaUcenJnWFmSpFAYESd`) |
| `05_novas_skills_propostas/cgov-pgr/SKILL.md` | Reescrito e reinstalado (`skill_012RejePYXwMWmwBpBXnmnWw`) |
| `SYSTEM_INSTRUCTIONS_Analista_Processos_SEI_v7.md` | Revisão 7.1 — cabeçalho, siglas, Seção 5.4, legenda de status |
| `SYSTEM_INSTRUCTIONS_Escritorio_CGOV.md` | Siglas e base de conhecimento |
| `RESUMO_ESTRUTURADO.md` | Cobertura, siglas e pendências |
| `cgov-analista-governanca_v2.md` | Movido para a raiz pelo Coordenador — passa a ser o System Instructions independente |

---

## 12. Estrutura de pastas para análises por processo SEI (fase 8 — 05/08/2026)

O Coordenador solicitou a organização dos produtos gerados pela aplicação das
skills deste projeto (análises, histórico de aprendizado, `NT_ESTADO.md` e
demais rascunhos de trabalho) por processo SEI, em vez de espalhados na raiz
do projeto — e que essa pasta não fosse sincronizada no repositório GitHub do
projeto.

**Decisão 16:** criada a pasta `07_analises/`, com uma subpasta por processo
SEI analisado, nomeada `[nº do processo SEI]_[apelido curto]` (ex.:
`07_analises/02070.001696_2026-31_RADAR/`, para o processo de revisão da
Política — RADAR — e da Metodologia de Gestão de Riscos). A pasta foi
adicionada ao `.gitignore` (criado nesta mesma decisão, ainda inexistente no
projeto). O `NT_ESTADO.md` já criado nesta sessão para o processo
[processo SEI de referência] (triagem `cgov-nt-01`, realizada momentos antes desta
decisão) foi migrado da raiz do projeto para dentro dessa subpasta, como
primeiro caso de uso da nova convenção.

**Limitação registrada:** as 7 skills da suíte `cgov-nt` têm, em seu texto
instalado, a instrução literal de criar `NT_ESTADO.md` "na raiz do projeto
atual". Não é possível alterar esse texto a partir deste projeto (skills
instaladas são somente leitura a partir daqui; alteração exige reinstalação
via Customize → Skills). Por ora, o redirecionamento para
`07_analises/[processo]/` é aplicado manualmente a cada execução da suíte —
documentado em `SYSTEM_INSTRUCTIONS_Escritorio_CGOV.md` (Seções 3 e 7) como
regra de projeto que prevalece sobre o texto literal da skill. Ver pendência
correspondente na seção seguinte.

### 12.1. Arquivos alterados nesta fase

| Arquivo | Alteração |
|---|---|
| `07_analises/02070.001696_2026-31_RADAR/NT_ESTADO.md` | **Criado** — migrado da raiz do projeto |
| `.gitignore` | **Criado** — exclui `07_analises/` |
| `SYSTEM_INSTRUCTIONS_Escritorio_CGOV.md` | Seção 3 (nova entrada `07_analises/`) e Seção 7 (regra de redirecionamento manual) |
| `RESUMO_ESTRUTURADO.md` | Tabela "O que existe hoje" e "Pendências" |

---

## 13. Reescrita e reinstalação da suíte `cgov-nt` com o novo caminho (fase 9 — 05/08/2026)

Em continuidade à Decisão 16 (Seção 12), o Coordenador solicitou a eliminação
do redirecionamento manual: que as 7 skills da suíte `cgov-nt` passassem a
criar/ler `NT_ESTADO.md` diretamente em `07_analises/[processo]/`, e que as
demais skills do projeto fossem revisadas quanto à mesma convenção.

**Levantamento prévio:** todas as ~25 skills instaladas relacionadas à CGOV
foram lidas e verificadas quanto a referências a `NT_ESTADO.md` ou "raiz do
projeto". Resultado:

| Grupo de skills | Referencia `NT_ESTADO.md`/raiz do projeto? | Ação |
|---|---|---|
| `cgov-nt-01` a `07` | Sim — as 7 | Reescritas (ver Decisão 17) |
| Analíticas normativas (`cgov-comparar-versoes`, `cgov-modelar-fluxo`, `cgov-auditoria-competencias`, `cgov-saneamento-legistica`) | Não — saída só em chat, sem escrita em arquivo | Nenhuma alteração |
| Plano de Entregas/PGD (`cgov-elaborar-entrega`, `cgov-avaliar-entrega`, `cgov-registro-execucao`) | Não — gravam em `H:\Meu Drive\CGOV_PGD\`, local pessoal do Coordenador, propositalmente fora da pasta do projeto Cowork | Nenhuma alteração |
| `cgge-especialista-pgd` | Não — saída só em chat | Nenhuma alteração |
| Temáticas do Art. 37 (`cgov-gestao-riscos`, `cgov-air-arr`, `cgov-cadeia-valor`, `cgov-regimento-interno`, `cgov-pgr`) | Não — saída só em chat; duas delas citam `REGISTRO_DECISOES.md` (raiz), o que está correto e não muda | Nenhuma alteração |
| PGD — indicadores (`cgov-pgd-analisar-indicador`, `-desenvolver-`, `-implementar-`, `-testar-`) | Não — escopo é código de ETL/DataOps, sem relação com NT | Nenhuma alteração |

**Decisão 17:** as 7 skills `cgov-nt-01` a `07` foram reescritas e
reinstaladas (Customize → Skills, com sobrescrita). Alterações, em cada uma:

- `cgov-nt-01`: a Fase 3.2 (antes "crie... na raiz do projeto") agora instrui
  a determinar o nome da subpasta (`[processo SEI]_[apelido curto]`), criá-la
  se necessário, e criar/atualizar `NT_ESTADO.md` dentro dela — preservando o
  conteúdo já registrado se a subpasta já existir. A Fase 1 e o restante do
  raciocínio de enquadramento (Fases 2 e a Regra Especial) não foram
  alterados.
- `cgov-nt-02` a `cgov-nt-07`: cada uma recebeu, no início de sua seção de
  pré-execução, um novo item "Localização do `NT_ESTADO.md`", instruindo a
  localizar a subpasta pelo processo SEI mencionado na conversa (ou usar a
  única subpasta com triagem em andamento, se houver apenas uma; perguntar ao
  usuário se houver ambiguidade entre múltiplos processos). Nenhuma outra
  seção de conteúdo (padrão de redação, formatos de saída, regras especiais)
  foi alterada.

O código-fonte espelho em `02_skills_cgov-nt/` foi atualizado com o mesmo
conteúdo reinstalado, mantendo a prática de sincronização manual já registrada
na Decisão 1.

**Efeito prático:** o `NT_ESTADO.md` do processo de referência
(criado nesta mesma sessão, em `07_analises/02070.001696_2026-31_RADAR/`)
passa a ser lido automaticamente pelas próximas skills da suíte sem qualquer
intervenção manual de caminho.

### 13.1. Arquivos alterados nesta fase

| Arquivo | Alteração |
|---|---|
| `02_skills_cgov-nt/cgov-nt-01-triagem/SKILL.md` até `cgov-nt-07-conclusao/SKILL.md` (7 arquivos) | Reescritos — novo caminho de `NT_ESTADO.md` |
| Skills instaladas `cgov-nt-01` a `07` | Reinstaladas via sobrescrita (Customize → Skills) |
| `SYSTEM_INSTRUCTIONS_Escritorio_CGOV.md` | Seções 3 e 7 — remoção da nota de redirecionamento manual (resolvida) |
| `RESUMO_ESTRUTURADO.md` | Pendência de redirecionamento manual marcada como resolvida; nova linha na tabela "O que existe hoje" |

---

## 14. Verificação do acervo e System Instructions autônomo v3.0 (fase 10 — 14/08/2026)

### 14.1. Verificação de legibilidade dos 30 arquivos do acervo

Teste de extração de texto arquivo a arquivo, com detecção heurística de
codificação corrompida. Resultado: **20 legíveis e citáveis · 7 ilegíveis por
máquina · 3 já em Markdown**.

**Ganho:** os novos uploads das Portarias **nº 4.101/2023**, **nº 1.164/2025**,
**nº 253/2026** e **nº 257/2026** resolveram o problema de codificação registrado
em 04/08/2026 — as quatro passaram de 🔒 a ✅.

**Permanecem 🔒:** Lei nº 11.516/2007 e Decretos nº 9.203/2017, nº 11.529/2023 e
nº 12.258/2024 (codificação embaralhada, mas texto íntegro no Planalto —
gravidade baixa); Código de Ética (Portaria nº 411/2020), Portaria MMA
nº 296/2021 e Portaria ICMBio nº 2.917/2026 (digitalizações sem camada de texto,
sem fonte pública alternativa — **gravidade alta**).

**Decisão 18 — não usar OCR.** O ambiente dispõe de OCR apenas com pacote de
idioma inglês. Aplicá-lo a texto normativo em português produziria erro de
transcrição em número de artigo e data — o modo de falha que os guardrails do
projeto existem para evitar. Os três arquivos internos precisam de **novo upload
com camada de texto** (imprimir em PDF a partir do SEI, não digitalizar).

### 14.2. ⛔ Achado crítico — a PGE está revogada

O **art. 12 da Portaria ICMBio nº 1.164/2025** revogou expressamente a **Portaria
ICMBio nº 768/2020** (Política de Gestão Estratégica — PGE).

**Efeito em cascata:** a Portaria nº 975/2021 remete à PGE para a **Reunião de
Avaliação da Estratégia — RAE**, foro em que Diretorias e Gabinete apresentariam
os resultados das medidas de tratamento de risco. A remissão está
**prejudicada**, e o PE 2025-2027 **não recriou a RAE**. O ciclo vigente é outro:
monitoramento **trimestral** pelas Diretorias via **PGD Petrvs**, consolidação
pela **DPAE/CGGE** em Relatório Trimestral de Ações Prioritárias e validação pelo
**Comitê Gestor** (arts. 8º e 9º da Portaria nº 1.164/2025).

**Decisão 19:** a skill `cgov-gestao-riscos` foi corrigida e reinstalada
(`skill_01PPyu8CVACa7JUyLanZusGQ`). Ela não afirma mais que a RAE existe:
descreve o ciclo vigente, registra a remissão prejudicada e **declara a lacuna**
— o foro de apresentação dos resultados de tratamento de risco carece de
definição institucional. Lacuna normativa real do ICMBio, não falha do
assistente.

### 14.3. ✅ Pendência do Integra+ resolvida

Cadeia confirmada: **nº 923/2020 → nº 1.257/2022 → nº 253, de 16/01/2026
(VIGENTE)**. A Portaria nº 975/2021 cita a nº 923/2020 — **remissão
desatualizada**, agora registrada na skill.

### 14.4. Norma nova incorporada — CTGRIC (Portaria nº 4.529/2025)

Achado de maior impacto operacional:

> **A CGOV é a Secretaria-Executiva do CTGRIC** (art. 2º, II), presidido pela
> CGGE (art. 2º, I).

Atribuições diretas e recorrentes da Coordenação (art. 5º): organizar a pauta,
convocar, secretariar e minutar atas, encaminhá-las para aprovação, **dar
encaminhamento às deliberações e monitorar seu cumprimento**, manter o acervo e
prestar apoio técnico. Reuniões ordinárias **trimestrais**, convocação com 5 dias
úteis. O CTGRIC compõe o **SITAI** como unidade setorial no ICMBio (USI).

**Decisão 20:** o CTGRIC foi incorporado à skill de riscos e ao System
Instructions autônomo. A rotina de secretariado do Comitê é atividade regimental
da CGOV que não estava mapeada em nenhum instrumento do projeto.

### 14.5. Índice do acervo reescrito

`00_INDICE_FONTES_NORMATIVAS.md`: 30 arquivos classificados por legibilidade,
seis blocos temáticos, seção de achados, convenção de siglas ampliada (com
PGOV-ICMBio, PE 2025-2027, CTGRIC e Integra+), tabela de **cadeias de revogação**
e pendências de acervo.

### 14.6. System Instructions autônomo — v3.0

**Decisão 21:** produzido `cgov-analista-governanca_v3.md`, substituindo a v2 e
encerrando a pendência nº 10.

A v2 pressupunha que o modelo "conhecesse" as normas do ICMBio a partir de links.
Não conhece — e, quando não conhece, infere. As Decisões 14 e 15 (fase 7)
mediram o custo disso. Como a v3.0 é destinada a assistentes **sem acesso** à
pasta, ela **internaliza** a base:

| Elemento internalizado | Fonte |
|---|---|
| Art. 37 integral | Texto verificado — diff automatizado com **0 divergências** |
| Tabelas 3 a 13 da metodologia de riscos | Portaria nº 975/2021 |
| Não incidência (art. 3º, § 2º) × dispensa (art. 4º) | Decreto nº 10.411/2020 |
| Espécies de ato e competência para editar | Portaria nº 271/2013, arts. 2º e 4º |
| Os 8 quesitos do Anexo II | Portaria nº 271/2013 |
| Princípios, mecanismos e Sistema de Governança | Portaria nº 4.101/2023 |
| Missão, visão, perspectivas e ciclo do PE | Portaria nº 1.164/2025 |
| Composição, competências e funcionamento do CTGRIC | Portaria nº 4.529/2025 |
| Prazos processuais | Lei nº 9.784/1999 |

**Expansão:** de 6 comandos (v2) para **9 funções** cobrindo os eixos do
Art. 37 — `/TRIAGEM`, `/NOTA_TECNICA`, `/VALIDAR_RISCO`, `/ESTRUTURAR_AIR`,
`/MAPEAR_PROCESSO`, `/AUDITAR_COMPETENCIAS`, `/SANEAR_MINUTA`,
`/ELABORAR_MINUTA`, `/ORIENTAR`.

**Seção 5.8 — lacunas declaradas.** A v3.0 lista o que **não** internalizou
(Código de Ética, IN ICMBio nº 14/2025, Portaria nº 99/2020, Acordo de Gestão,
detalhamento do DFT, objetivos estratégicos específicos, Cadeia de Valor
vigente), instruindo o assistente a declarar a lacuna em vez de inferir. Essa
seção é o que impede a v3.0 de repetir o erro da v2.

**Verificação automatizada do v3.0:** diff do Art. 37 contra a fonte (0
divergências) · Tabela 9 conferida célula a célula (confere) · multiplicadores da
Tabela 10 íntegros · varredura de termos proibidos ("PGR de riscos", "DIPLAN",
numeração `4.1.1`) sem ocorrência indevida.

### 14.7. Arquivos alterados nesta fase

| Arquivo | Alteração |
|---|---|
| `04_fontes_normativas/00_INDICE_FONTES_NORMATIVAS.md` | Reescrito |
| `cgov-analista-governanca_v3.md` | **Criado** — System Instructions autônomo |
| `05_novas_skills_propostas/cgov-gestao-riscos/SKILL.md` | CTGRIC, Integra+ vigente, PGE revogada; reinstalada |

---

## 15. Fechamento da revisão do System Instructions v7.2 (28/08/2026)

**Decisão 22 — atualização do acervo normativo no System Instructions.** A
pendência de legibilidade das Portarias ICMBio nº 4.101/2023, nº 1.164/2025 e
nº 253/2026 é encerrada. O índice do acervo registra, desde 14/08/2026, novos
uploads com texto legível para as três normas; seus dispositivos passam a ser
citáveis, observada a conferência do caso concreto.

**Decisão 23 — vigência do Integra+.** Confirmada para a documentação do
projeto a cadeia nº 923/2020 → nº 1.257/2022 → **nº 253/2026 (vigente)**. A
remissão à nº 923/2020 na Portaria nº 975/2021 deve ser tratada como
desatualizada.

**Decisão 24 — evals remanescentes.** Foram executados e aprovados os 12 casos
de borda ainda pendentes da suíte `cgov-nt`; o relatório de execução está em
`01_relatorios/RELATORIO_EVALS_cgov-nt_2026-08-28.md`. Os registros anteriores
indicavam 16 casos totais e 13 remanescentes, mas os sete `evals.json` vigentes
contêm 15 casos, três dos quais já tinham sido executados no piloto. A revisão
identificou e corrigiu, preventivamente, a referência indevida ao futuro simples
na pré-execução da `cgov-nt-04`.

**Decisão 25 — pendência sobre padrão de numeração junto à PFE.** Por decisão
do usuário, a pendência é descartada. A suíte mantém o padrão já validado por
piloto: `### Capítulo N` e `#### N.1`.

---

## 16. Reorganização para repositório público sanitizado (28/08/2026)

**Decisão 26 — estrutura de repositório.** O projeto foi reorganizado com
`docs/` para documentação pública, `skills/` para fontes canônicas e `local/`
para análises, acervo normativo, snapshots instalados e histórico que contém
referências a processos concretos. O diretório `local/` é integralmente ignorado
pelo Git.

**Decisão 27 — publicação de fontes e histórico.** O repositório público não
redistribui PDFs normativos, materiais de terceiros nem artefatos associados a
processos SEI. O catálogo público preserva metadados e canais oficiais de acesso;
artefatos históricos só retornam a `archive/` após sanitização documental.

**Decisão 28 — caminhos operacionais.** A suíte `cgov-nt` passa a registrar
workspaces em `local/analyses/SEI_[processo]_[apelido]/`. Os caminhos numerados
que aparecem em seções anteriores deste registro são históricos.

## 17. Consolidação do catálogo normativo público (29/08/2026)

**Decisão 29 — índice local substituído pelo catálogo público.** As informações
operacionais e normativas do índice local de fontes foram incorporadas em
`docs/references/normative-catalog.md`, com registro das situações de
legibilidade, revogações, cadeias normativas, siglas e pendências. A revisão
identificou também a Portaria Conjunta CGU/CEP nº 3/2025, presente no acervo e
ausente do índice anterior. O índice tornou-se redundante e foi removido; o
catálogo público permanece como sua referência documental sanitizada.

## 18. Compatibilidade multiplataforma — Claude, ChatGPT, Antigravity (29/08/2026)

**Contexto.** O Coordenador solicitou que o projeto funcione com confiabilidade
em três aplicativos instalados (Claude, ChatGPT desktop, Antigravity IDE),
sem conflito entre eles. Diagnóstico completo em `docs/multiplatform.md`.

**Decisão 30 — espelho de skills para a Antigravity.** Criado `.agents/skills/`
(gitignored) com cópia das 12 `SKILL.md` de `skills/cgov-nt/` e
`skills/thematic/`, porque a Antigravity só descobre skills nesse caminho.
`skills/` permanece a única fonte de verdade; regra de resincronização
registrada em `CONTRIBUTING.md`.

**Decisão 31 — `analista-governanca.md` dividido em núcleo + anexos.** Medição
revelou que o documento v3.0 (56.199 caracteres) excedia o limite de 8.000
caracteres do campo Instructions de um Project no ChatGPT — seria truncado
sem aviso. O documento (v3.0) foi arquivado em
`local/archive/system-instructions/analista-governanca-v3.md` e substituído
pela v4.0: um núcleo de 7.868 caracteres (persona, siglas, cadeia de
raciocínio, guardrails, protocolo de incerteza, lista de funções) mais dois
anexos de referência (`analista-governanca-anexo-normativo.md`,
`analista-governanca-anexo-funcoes.md`) para anexar à Library do
Project/Gem. **Ressalva:** a condensação do núcleo foi feita sem segunda
verificação humana — revisar antes de uso em produção (pendência aberta,
item 19 abaixo).

**Correção de rota — `analista-processos-sei.md` não precisava do mesmo
tratamento.** A proposta original de 28/08/2026 listou este arquivo junto de
`analista-governanca.md` como candidato à mesma divisão. Leitura integral do
arquivo mostrou que seu cabeçalho já declara `Ambiente de execução: Claude
Cowork` e que ele roteia para skills reais do Claude — não é um documento
autossuficiente para ChatGPT/Gemini. Fica registrada, em vez disso, a
sobreposição entre `escritorio-cgov.md`, `analista-processos-sei.md` e a
própria suíte de skills dentro do ambiente Claude — não resolvida nesta
rodada (pendência aberta, item 20 abaixo).

**Decisão 32 — nunca criar `GEMINI.md` na raiz.** A Antigravity dá precedência
a `GEMINI.md` sobre `AGENTS.md` em caso de conflito. Para evitar uma regra
silenciosa vencendo `AGENTS.md` sem registro, `AGENTS.md` permanece o único
arquivo de regras na raiz para as três ferramentas.

**Não resolvido — limite de instruções de um Gem (Gemini).** Fontes públicas
divergem entre ~200 e ~4.000 caracteres, sem uma fonte oficial única
localizada nesta sessão. O núcleo de 7.868 caracteres foi dimensionado para o
teto do ChatGPT (8.000), não para o Gemini — pode precisar de nova
condensação se for usado em um Gem.

**⚠️ Achado crítico — a suíte `cgov-nt` instalada no Claude está desatualizada
em relação à fonte.** Comparando a `description` das 7 skills `cgov-nt-01` a
`07` tal como disponíveis nesta sessão (skills instaladas na conta) contra o
texto em `skills/cgov-nt/*/SKILL.md`, seis das sete (todas exceto
`cgov-nt-05`) ainda referenciam o caminho antigo
`07_analises/[processo SEI]_[apelido]/` para o `NT_ESTADO.md`, enquanto a
fonte já usa `local/analyses/SEI_[processo]_[apelido]/` desde a Decisão 28
(Seção 17). Como a prática deste projeto é reinstalar por sobrescrita
completa (não editar em produção), é provável que o corpo inteiro das skills
instaladas — não só a descrição — ainda crie/procure `NT_ESTADO.md` na pasta
errada. **Não verificado diretamente** (nenhuma execução real da suíte foi
feita nesta sessão para confirmar o comportamento) — mas a fonte da
`description` é o próprio texto instalado, o que já é evidência direta de
desatualização. Ação pendente do Coordenador: reinstalar as 7 skills via
Customize → Skills a partir do conteúdo atual de `skills/cgov-nt/`.

**Achado menor — espaço espúrio na fonte de `cgov-regimento-interno`.** A
`description` da skill instalada usa o gatilho `/cgov-regimento-interno`
(correto); a fonte em `skills/thematic/cgov-regimento-interno/SKILL.md` tem
`/cgov- regimento-interno` (espaço após o hífen). Se a fonte for reinstalada
sem correção, o gatilho literal do comando quebra.

## 19. Skill de transcrição de fontes normativas (29/08/2026)

**Decisão 33 — criação de `cgov-transcrever-normativos`.** O procedimento
validado para converter PDFs normativos locais sem camada textual confiável em
Markdown foi formalizado como skill canônica em
`skills/thematic/cgov-transcrever-normativos/`. A skill mantém o PDF local como
fonte de controle, usa fonte oficial primária apenas para conferência, exige
segunda revisão visual independente e impede a gravação final enquanto houver
erro estrutural bloqueante.

Foram incorporados três utilitários reutilizáveis: inventário de PDFs e
arquivos `.md`, OCR local do Windows em `pt-BR` com coordenadas das linhas e
validador de UTF-8, frontmatter, título, artigos, tabelas, caracteres inválidos
e marcações de redação tachada. Os scripts permanecem na fonte canônica; a
cópia de `SKILL.md` em `.agents/skills/` os referencia pelo caminho em
`skills/thematic/`, evitando duplicação executável no espelho da Antigravity.

**Validação.** `quick_validate.py` aprovou a estrutura da skill. O OCR foi
executado sobre uma página real da Portaria ICMBio nº 2.917/2026, produzindo 44
linhas com texto e caixas delimitadoras. O validador aprovou a transcrição
dessa Portaria e a do Decreto nº 12.258/2024, inclusive suas cinco tabelas. O
inventário do acervo encontrou 27 PDFs: 7 já pareados com `.md`, 18 atos
normativos ainda sem par e 2 publicações que exigem decisão de escopo (NBR e
guia, não atos normativos). Há ainda 3 arquivos Markdown locais cuja fonte PDF
não tem o mesmo nome-base.

O `docs/references/normative-catalog.md` foi atualizado para registrar como
texto verificado as sete transcrições concluídas em 29/08/2026 e encerrar as
duas pendências de legibilidade correspondentes, sem tratar os PDFs originais
como se tivessem adquirido camada textual.

**Instalação.** A fonte e o espelho da Antigravity foram criados nesta rodada.
A skill ainda não foi instalada na conta Claude/Cowork; eventual instalação
externa deve usar a pasta completa, incluindo `scripts/`, e ser confirmada antes
de atualizar qualquer snapshot de referência instalado.

## 20. Reinstalação da suíte `cgov-nt` e sincronização das Instruções do Projeto (30/08/2026)

**Contexto.** Análise comparativa entre `cgov-geral-v1` e o projeto irmão
`pgd-agente-icmbio` (fora deste repositório) identificou que a reorganização de
28/08/2026 (Decisão 28) havia renomeado os caminhos na fonte sem reinstalar as
skills afetadas, e que o texto colado nas Instruções do Projeto do Cowork havia
ficado defasado em relação a `docs/system-instructions/escritorio-cgov.md`.

**Descoberta de ferramenta.** Esta sessão do Cowork expôs `save_skill`, que cria
ou sobrescreve (`overwrite: true`) uma skill da conta diretamente, sem depender
do fluxo manual "Customize → Skills" registrado como único caminho até aqui
(Decisão 17, Seção 13). A partir de agora, esse é o método preferencial para
reinstalar skills cuja fonte vive em `skills/` — mais rápido e auditável do que
a via manual, mas ainda sujeito à mesma exigência de confirmação antes de
alterar skills em uso.

**Decisão 34 — reinstalação das 7 skills `cgov-nt-01` a `07`.** Confirmado que a
fonte em `skills/cgov-nt/*/SKILL.md` já usava `local/analyses/SEI_[processo]_[apelido]/`
em todas as 7 (inclusive `cgov-nt-05`, que já estava correta antes desta rodada).
As 7 foram reinstaladas via `save_skill` com `overwrite: true`, conteúdo idêntico
à fonte atual — sem qualquer edição de conteúdo, apenas sincronização
fonte→instalado. Reinstalação confirmada por resposta bem-sucedida da API para
as 7 (`validation_errors: []`), sem execução formal dos `evals/evals.json` nesta
rodada (verificação de conteúdo caractere-a-caractere contra a fonte foi
considerada suficiente, dado que nenhuma lógica foi alterada — apenas o
caminho, que já estava correto na fonte).

**Decisão 35 — sincronização das Instruções do Projeto Cowork.** Corrigido, na
fonte (`docs/system-instructions/escritorio-cgov.md`, Seção 3), o caminho
`skills/installed-reference/` → `local/installed-reference/` (nome real da
pasta na árvore atual). O Coordenador informou ter colado o conteúdo atualizado
no campo de Instruções do Projeto do Cowork antes desta correção pontual — **não
verificado nesta sessão**: o bloco de instruções injetado no início de uma
conversa é fixado na abertura da conversa, então uma sessão já em andamento não
reflete uma atualização feita a meio da conversa, e não há ferramenta, nesta
sessão, para ler de volta o texto salvo no campo de configuração do projeto.
Verificação pendente: abrir uma conversa nova neste projeto e conferir se o
texto injetado bate com a fonte corrigida (ou colar novamente o conteúdo já
corrigido, por segurança).

### 20.1. Arquivos/skills alterados nesta fase

| Item | Alteração |
|---|---|
| `cgov-nt-01-triagem` a `cgov-nt-07-conclusao` (skills instaladas) | Reinstaladas via `save_skill`, sem alteração de conteúdo em relação à fonte |
| `docs/system-instructions/escritorio-cgov.md` | Corrigido `skills/installed-reference/` → `local/installed-reference/` |
| Instruções do Projeto Cowork (campo de configuração, fora deste repositório) | Atualizada pelo Coordenador; sincronização com a fonte corrigida **pendente de confirmação** |

## 21. Correção dos achados A-01 a A-03 nas skills de Plano de Entregas/PGD (30/08/2026)

**Contexto.** `cgov-avaliar-entrega` e `cgov-registro-execucao` não têm fonte
canônica neste repositório por decisão deliberada (Decisão 17, Seção 13): são
skills que gravam pareceres e logs em `H:\Meu Drive\CGOV_PGD\`, pasta pessoal
do Coordenador, propositalmente fora do projeto Cowork. `local/installed-reference/`
guardava, até esta rodada, apenas um espelho de leitura do texto instalado.

Três achados desta rodada, originalmente documentados no projeto irmão
`pgd-agente-icmbio` (`skills/05_plano-skills-execucao-avaliacao_v1.md`,
18/08/2026, fora deste repositório):

- **A-01** — `cgov-avaliar-entrega` usava a faixa fixa `≥ 80% = Adequado` sem
  qualquer sinalização de que não tem lastro na IN MGI nº 24/2023 nem em
  normativo específico do ICMBio para avaliação de entregas do PGD.
- **A-02** — a mesma skill exigia "sem intercorrências" como condição para o
  conceito "Alto Desempenho" — um automatismo que a norma não prevê.
- **A-03** — `cgov-registro-execucao` calculava o `% Concluído` sempre como
  `etapas concluídas / total de etapas`, confundindo esforço (quantidade de
  atividades finalizadas) com resultado (cumprimento da meta pactuada da
  entrega).

**Decisão preliminar (passo 0).** Antes de editar, foi perguntado ao
Coordenador onde vive o texto-fonte editável dessas duas skills. Resposta:
**só existe como skill instalada** — não há arquivo de origem em nenhum outro
local. A partir desta rodada, `local/installed-reference/cgov-avaliar-entrega/SKILL.md`
e `local/installed-reference/cgov-registro-execucao/SKILL.md` deixam de ser um
mero espelho de leitura e passam a ser tratados como fonte de trabalho — a
edição partiu deles, e o conteúdo reinstalado é idêntico ao que ali ficou
registrado.

**Decisão 36 — correção dos achados A-01 a A-03.** Ambas as skills foram
corrigidas e reinstaladas via `save_skill` (`overwrite: true`):

- `cgov-avaliar-entrega` (Fase 2): a condição "sem intercorrências" foi
  **removida** do conceito "Alto Desempenho" (A-02) — intercorrências passam a
  ser sempre registradas e ponderadas separadamente na análise qualitativa,
  nunca como gatilho automático de rebaixamento. A faixa `≥ 80% = Adequado`
  foi **mantida** (é o único corte hoje em uso e não há substituto normativo
  identificado), mas agora rotulada explicitamente como "convenção local, não
  norma", com ⚠️ apontando a ausência de lastro na IN MGI nº 24/2023 — tanto na
  Fase 2 quanto nas Notas Internas da skill (A-01).
- `cgov-registro-execucao` (Fase 2): o cálculo de `% Concluído` passa a
  priorizar a **meta pactuada** registrada na Planilha A (quantidade, marco de
  cronograma ou peso por trimestre) sempre que disponível. Na ausência de meta
  pactuada explícita, a contagem de etapas concluídas/total continua sendo
  usada, mas agora como **aproximação declarada** — sinalizada como tal no
  relatório (novo campo "Método do % Concluído": Meta pactuada / Aproximação
  por etapas) — nunca apresentada em silêncio como o percentual oficial (A-03).

**Verificação.** As duas skills foram testadas com casos simulados antes da
conclusão:
1. `cgov-avaliar-entrega` — entrega com 100% concluído, conclusão no prazo
   exato e intercorrência documentada: antes da correção, a regra antiga
   ("Adequado" para `≥ 80%` com intercorrência) rebaixava indevidamente o
   conceito; após a correção, a entrega se enquadra em "Alto Desempenho" (a
   intercorrência é registrada à parte, sem rebaixar o conceito).
2. `cgov-avaliar-entrega` — entrega com 82% concluído, sem intercorrência: o
   parecer agora traz o aviso ⚠️ de convenção local junto ao enquadramento em
   "Adequado" (antes, a faixa era citada sem qualquer ressalva).
3. `cgov-registro-execucao` — entrega com meta pactuada explícita (peso por
   trimestre) na Planilha A: o `% Concluído` é calculado contra essa meta, e o
   relatório rotula o método como "Meta pactuada".
4. `cgov-registro-execucao` — entrega sem meta pactuada registrada: o cálculo
   recai na contagem de etapas, mas o relatório agora rotula o método como
   "Aproximação por etapas" e sinaliza a ressalva, em vez de apresentar o
   número como se fosse o percentual oficial apurado contra a meta.

Reinstalação confirmada por resposta bem-sucedida da API para as duas skills
(`validation_errors: []`).

### 21.1. Arquivos/skills alterados nesta fase

| Item | Alteração |
|---|---|
| `local/installed-reference/cgov-avaliar-entrega/SKILL.md` | Promovido de espelho de leitura a fonte de trabalho; Fase 2 e Notas Internas corrigidas (A-01, A-02) |
| `local/installed-reference/cgov-registro-execucao/SKILL.md` | Promovido de espelho de leitura a fonte de trabalho; Fase 2, template e Notas Internas corrigidos (A-03) |
| `cgov-avaliar-entrega` (skill instalada) | Reinstalada via `save_skill` (`overwrite: true`) |
| `cgov-registro-execucao` (skill instalada) | Reinstalada via `save_skill` (`overwrite: true`) |

## 22. Instalação de `cgov-transcrever-normativos` (30/08/2026)

**Contexto.** A skill estava pronta e validada na fonte desde 29/08/2026
(Decisão 33, Seção 19), mas ainda não instalada no Claude/Cowork — pendência
nº 21. Como se trata de uma decisão de escopo (instalar ou não uma skill de
manutenção do acervo normativo nesta superfície), e não apenas técnica, foi
perguntado ao Coordenador antes de agir.

**Decisão preliminar de escopo.** Antes da instalação, o Coordenador foi
informado de duas limitações técnicas da skill nesta superfície:
1. Ela referencia os 3 scripts auxiliares (`inventory_normative_sources.py`,
   `qa_transcription.py`, `ocr_windows.ps1`) por caminho relativo dentro deste
   repositório (`skills/thematic/cgov-transcrever-normativos/scripts/`).
   `save_skill` grava a skill **a nível de conta**, não de projeto, e não tem
   parâmetro para anexar arquivos auxiliares — confirmado pela resposta da
   chamada (`skill_directory: null`, nenhum arquivo além do `SKILL.md`
   propriamente dito). Os scripts só são alcançáveis quando a sessão tem esta
   pasta do projeto montada — ou seja, a skill funciona plenamente apenas em
   sessões do Cowork deste projeto (`cgov-geral-v1`).
2. O passo de OCR indicado para Windows usa PowerShell (`ocr_windows.ps1`),
   que não roda no sandbox Linux do Cowork. O próprio texto da skill já prevê
   essa situação ("se a capacidade de PDF disponível no ambiente oferecer
   renderização ou OCR, ela pode ser usada") — nesta superfície, a extração
   direta e a capacidade de leitura de PDF do próprio ambiente substituem o
   script PowerShell.

O Coordenador confirmou instalar mesmo assim, ciente das dessas duas
limitações.

**Decisão 37 — instalação de `cgov-transcrever-normativos`.** A skill foi
instalada via `save_skill` (sem `overwrite`, criação nova), com o `name`,
`description` e corpo de instruções idênticos, caractere a caractere, à fonte
em `skills/thematic/cgov-transcrever-normativos/SKILL.md`. Resposta da API sem
erros de validação (`validation_errors: []`).

**Verificação.**
- *Acionamento correto:* os 16 casos de `evals/trigger_eval.json` foram
  conferidos manualmente (sem corredor automatizado, conforme `CLAUDE.md`)
  contra a `description` instalada — as 8 consultas que deveriam acionar a
  skill (pedidos de OCR/transcrição de atos normativos) e as 8 que não deveriam
  (resumo, comparação de versões, redação de NT, pesquisa na internet, análise
  jurídica, PDF não normativo) bateram com o `should_trigger` esperado em
  todos os casos.
- *Scripts executáveis a partir do caminho montado:* `inventory_normative_sources.py`
  e `qa_transcription.py` foram executados via Bash a partir de
  `skills/thematic/cgov-transcrever-normativos/scripts/` dentro da pasta
  montada do projeto — ambos rodaram sem erro.
- *Caso real do acervo:* o inventário mostrou **0 PDFs pendentes de
  transcrição** (27 PDFs, 25 pareados, 2 fora do escopo de ato normativo, 3
  `.md` órfãos) — não há, hoje, um PDF normativo real ainda sem par para uma
  transcrição nova de ponta a ponta. Em vez disso, `qa_transcription.py` foi
  executado sobre um par PDF/Markdown real já existente no acervo (Decreto
  nº 9.203/2017), como verificação de que a barreira de qualidade funciona
  com dados reais: `"ok": true`, sem erros nem avisos, 32 artigos detectados,
  hashes SHA-256 do PDF e do Markdown calculados corretamente.

**Espelho em `local/installed-reference/`.** Não foi criado um espelho para
esta skill. Diferentemente de `cgov-avaliar-entrega` e `cgov-registro-execucao`
(Seção 21) — que não têm fonte canônica no repositório e por isso dependem do
espelho para qualquer auditoria —, `cgov-transcrever-normativos` já tem fonte
canônica em `skills/thematic/`, no mesmo padrão das outras 5 skills temáticas
do Art. 37 (`cgov-gestao-riscos`, `cgov-air-arr`, `cgov-cadeia-valor`,
`cgov-regimento-interno`, `cgov-pgr`), nenhuma das quais tem espelho em
`local/installed-reference/` — conforme a própria distinção de papéis da
Seção 3 do `CLAUDE.md`. Criar um espelho aqui duplicaria, sem necessidade, o
que já é rastreável na fonte. A paridade fonte↔instalado desta rodada está
garantida porque a instalação usou o conteúdo da fonte sem qualquer edição.

### 22.1. Arquivos/skills alterados nesta fase

| Item | Alteração |
|---|---|
| `cgov-transcrever-normativos` (skill de conta) | Instalada via `save_skill`, conteúdo idêntico à fonte em `skills/thematic/` |

## 23. Criação e instalação de `cgov-qcf` — Art. 37, V (30/08/2026)

**Contexto.** O inciso V (Quadro Demonstrativo dos Cargos e Funções
Comissionadas Executivas) era o único dos 10 incisos do parágrafo único do
Art. 37 ainda sem skill dedicada — pendência nº 7, aberta desde a fase 5
(05/07/2026). Por ser um tema mais estreito e menos recorrente que os
demais eixos, a criação dependia de decisão explícita do Coordenador sobre
se valia a pena. Perguntado, o Coordenador confirmou criar a skill.

**Pesquisa normativa prévia (antes de redigir a skill).** Antes de escrever
qualquer instrução, foi levantada a base normativa real do QCF do ICMBio:

- O texto verificado do Art. 37, V (`local/normative-sources/20251211_Art_37_Portaria_5592-2025_texto_verificado.md`)
  mostra que o verbo do dispositivo é **"coordenar a elaboração e
  consolidação das propostas de adequação"** do QCF — não aprovar nem editar
  o Quadro; a CGOV consolida propostas, a decisão final é do Executivo.
- O acervo já continha, transcrito e verificado desde 29/08/2026, o
  **Decreto nº 12.258, de 25/11/2024** — que aprova a Estrutura Regimental
  **e** o Quadro Demonstrativo dos CCE/FCE do ICMBio (Anexos I a IV) —, fonte
  primária direta para a skill.
- Duas normas citadas pelo próprio Decreto nº 12.258/2024 (Lei nº 14.204/2021
  e Decreto nº 10.829/2021) foram verificadas nesta rodada por consulta
  direta ao Planalto (`planalto.gov.br`), confirmando: a Lei nº 14.204/2021
  instituiu os CCE/FCE e extinguiu o DAS e a FCPE, disciplinando
  transformação (art. 6º geral, art. 7º específico para CCE/FCE) e critérios
  de ocupação; o Decreto nº 10.829/2021 é o regulamento dessa Lei.
  Uma terceira norma citada (Decreto nº 9.739/2019) **não** foi verificada
  em texto integral — a skill cita apenas o que o próprio Decreto
  nº 12.258/2024 já atesta sobre ela, com ⚠️ explícito sobre o limite dessa
  verificação.
- `cgov-regimento-interno` (instalada em 04/08/2026) já antecipava esta
  lacuna — seu texto já instruía "acionar também o processo de atualização
  do QCF (Art. 37, V)" sempre que uma mudança de competência tivesse impacto
  em cargos. `cgov-qcf` foi desenhada como a contraparte dessa integração.

**Decisão 38 — criação e instalação de `cgov-qcf`.** Escrita a fonte em
`skills/thematic/cgov-qcf/SKILL.md`, seguindo o mesmo padrão das 5 skills
temáticas existentes (base normativa tabelada, fases numeradas, regras
transversais). Estrutura da skill: diagnóstico do gatilho (Fase 1);
consolidação de propostas de múltiplas unidades, já que o inciso V fala em
"propostas" no plural (Fase 2); estruturação técnica do quadro no mesmo
formato tabular do Anexo II do Decreto nº 12.258/2024 (Fase 3); distinção
entre alteração que exige novo Decreto e a que cabe ato inferior a decreto —
com base no próprio Art. 4º do Decreto nº 12.258/2024 (Fase 4); articulação
obrigatória com `cgov-regimento-interno` (Fase 5); e entrega documentada
(Fase 6). Regras transversais incluem a desambiguação QCF × DFT (Art. 37,
V × VI — `cgov-cadeia-valor`), no mesmo espírito das desambiguações já
registradas para PGR/PGRI/PGD.

A `description` inicial (1.182 caracteres) excedeu o limite de 1.024
caracteres já registrado como armadilha conhecida (Decisão 9, Seção 10.3) —
foi condensada para 938 caracteres antes da instalação, preservando todos os
gatilhos de acionamento e a nota de integração com `cgov-regimento-interno`.

Criados também `skills/thematic/cgov-qcf/evals/trigger_eval.json` (16 casos,
8 positivos e 8 negativos, incluindo casos negativos específicos para QCF ×
RI e QCF × DFT) e instalada a skill via `save_skill` (criação nova, sem
`overwrite`). Resposta da API sem erros de validação
(`validation_errors: []`).

**Verificação.** Os 16 casos de `trigger_eval.json` foram conferidos
manualmente (sem corredor automatizado, conforme `CLAUDE.md`) contra a
`description` instalada (938 caracteres) — todos bateram com o
`should_trigger` esperado, incluindo os casos negativos que testam a
fronteira com `cgov-regimento-interno` (minuta de alteração do RI, sem menção
a QCF) e com `cgov-cadeia-valor` (DFT/dimensionamento de força de trabalho).

**Sem espelho em `local/installed-reference/`.** Mesmo padrão da Decisão 37
(Seção 22): `cgov-qcf` tem fonte canônica em `skills/thematic/`, como as
outras 5 skills temáticas do Art. 37, nenhuma das quais tem espelho de
leitura em `local/installed-reference/`.

**Cobertura resultante.** Os 10 incisos do parágrafo único do Art. 37 passam
a ter skill dedicada — cobertura completa.

### 23.1. Arquivos/skills alterados nesta fase

| Item | Alteração |
|---|---|
| `skills/thematic/cgov-qcf/SKILL.md` | Criado — fonte canônica da nova skill |
| `skills/thematic/cgov-qcf/evals/trigger_eval.json` | Criado — 16 casos de acionamento |
| `cgov-qcf` (skill de conta) | Instalada via `save_skill` (criação nova) |

## 24. Desambiguação `cgov-gestao-riscos` × S10 do `pgd-agente-icmbio` (30/08/2026)

**Contexto.** Risco de confusão de escopo análogo ao já resolvido para
PGR/PGRI/PGD (Decisão 9 e outras): o componente **S10** do assistente irmão
`pgd-agente-icmbio` trata risco de **projeto/entrega** (dependências e
restrições de uma entrega específica do Plano de Entregas), enquanto
`cgov-gestao-riscos` trata risco **institucional** no sentido do Art. 37, IX,
da Portaria ICMBio nº 5.592/2025 e da PGRI (Portaria ICMBio nº 255/2020,
metodologia da Portaria ICMBio nº 975/2021). São objetos diferentes — a
Metodologia da Portaria nº 975/2021 não foi desenhada para avaliar risco de
atraso de uma entrega individual —, mas a palavra "risco" sozinha convida à
confusão, sobretudo porque o Plano de Entregas também é tema regular desta
suíte (`cgov-elaborar-entrega`, `cgov-avaliar-entrega`,
`cgov-registro-execucao`).

**Decisão 39 — desambiguação de escopo `cgov-gestao-riscos` × S10 do
`pgd-agente-icmbio`.**

1. **`description` (fonte em `skills/thematic/cgov-gestao-riscos/SKILL.md`).**
   Reescrita para incluir a frase "IMPORTANTE: trata do risco institucional
   (Art. 37-IX) — não do risco de projeto/entrega do Plano de Entregas, que é
   o S10 do pgd-agente-icmbio (projeto irmão)", no mesmo modelo já usado em
   `cgov-pgr`. Como a descrição já estava próxima do limite de 1.024
   caracteres (Decisão 9, Seção 10.3), foi necessário condensar outros trechos
   (remover "fielmente", enxugar o parêntese das Tabelas 1-13, remover "ISO
   31000" como palavra-gatilho explícita, encurtar a frase final sobre risco
   fora da sintaxe oficial) para caber a nova frase — texto final com 1.006
   caracteres, verificado por contagem programática antes da instalação.
2. **Corpo da skill.** Inserido, logo após o bloco `> **IMPORTANTE**` já
   existente sobre PGR/PGRI/PGD (seção "CONVENÇÃO DE SIGLAS"), um novo bloco
   `> **IMPORTANTE — risco institucional × risco de projeto/entrega.**`
   explicando a distinção com mais detalhe do que cabe na `description`:
   define o que é risco institucional nesta skill, afirma explicitamente que
   ela **não** trata de risco de projeto/entrega, nomeia o S10 do
   `pgd-agente-icmbio` como o objeto correto para esse segundo caso, e
   instrui a esclarecer a distinção e direcionar ao S10 em vez de aplicar a
   Metodologia da Portaria nº 975/2021 a um objeto que ela não foi desenhada
   para tratar.
3. **Evals.** `skills/thematic/cgov-gestao-riscos/evals/trigger_eval.json`
   reconferido caso a caso contra a nova `description` (os 20 casos
   pré-existentes continuam corretos) e ampliado com 2 casos negativos novos,
   específicos para a fronteira S10: uma entrega do Plano de Entregas com
   risco de atraso por dependência externa, e riscos/restrições de uma
   entrega específica para o Plano de Trabalho Individual — ambos
   `should_trigger: false`, total de 22 casos.
4. **Reinstalação.** `cgov-gestao-riscos` reinstalada via `save_skill`
   (`overwrite: true`), conteúdo idêntico à fonte atualizada. Resposta da API
   sem erros de validação (`validation_errors: []`).

**Pendência remanescente — fora do escopo de edição direta desta sessão.** O
passo 2 do plano (`local/PLANO_correcao_cgov-geral-v1_2026-08-30.md`, item 6)
previa também registrar a mesma distinção do lado do `pgd-agente-icmbio` —
por exemplo em `docs/projeto-v6/03-catalogo-skills-s01-s24.md` ou numa ficha
`SKILL_S10.md` equivalente. Esse repositório está fora do escopo de edição
desta sessão (é outro projeto, com suas próprias convenções); fica como
**sugestão ao Coordenador**, não como ação executada aqui.

### 24.1. Arquivos/skills alterados nesta fase

| Item | Alteração |
|---|---|
| `skills/thematic/cgov-gestao-riscos/SKILL.md` | `description` reescrita (1.006 caracteres) e novo bloco `IMPORTANTE` inserido no corpo |
| `skills/thematic/cgov-gestao-riscos/evals/trigger_eval.json` | Ampliado de 20 para 22 casos (2 novos negativos, fronteira S10) |
| `cgov-gestao-riscos` (skill de conta) | Reinstalada via `save_skill` (`overwrite: true`) |

## 25. Pendências abertas (para continuidade)

1. ~~Validação jurídica pessoal do texto do Art. 37~~ — ✅ **Resolvida em
   05/07/2026** (Seção 7 acima).
2. ~~Execução dos 12 casos de eval ainda não exercitados (casos de borda sem
   gabarito real disponível no momento do piloto).~~ — ✅ **Concluída em
   28/08/2026** (Decisão 24).
3. Otimização das descrições (`description`) das 7 skills para acionamento
   automático mais assertivo, especialmente `cgov-nt-01`.
4. Definição, junto à PFE, de qual padrão de numeração de capítulo (o agora
   adotado, `### Capítulo N`/`#### N.1`, validado por esta rodada) deve ser
   considerado o oficial da CGOV daqui em diante.
5. Cópia manual, se desejada, do PDF completo da Portaria nº 5.592/2025 para
   `04_fontes_normativas` (ver limitação de ferramenta, Seção 7).
6. ~~Instalar as 5 novas skills de `05_novas_skills_propostas/`~~ — ✅
   **Concluída em 04/08/2026** (Seção 10.3 acima).
7. ~~Avaliar a oportunidade de criar `cgov-qcf` (Art. 37, V — Quadro de Cargos e
   Funções Comissionadas), único inciso ainda sem skill dedicada.~~ — ✅
   **Concluída em 30/08/2026** (Decisão 38, Seção 23): skill criada e
   instalada. Cobertura do Art. 37 passa a ser completa (10 de 10 incisos).
8. ~~Resolver a divergência `DIPLAN` × `GABIN`~~ — ✅ **Resolvida em 04/08/2026**
   (Decisão 10): `Nota Técnica nº [#]/[ano]/CGOV/CGGE/GABIN/ICMBio`.
9. ~~Anexar a `04_fontes_normativas/` o texto das portarias internas~~ — ✅
   **Concluída em 04/08/2026.** As Portarias nº 255/2020, nº 975/2021 e
   nº 1.572/2023 estão legíveis e já foram incorporadas às skills.
10. ~~Corrigir o `cgov-analista-governanca_v2.md`~~ — ✅ **Concluída em
    14/08/2026** (Decisão 21): substituído pelo `cgov-analista-governanca_v3.md`,
    com base normativa internalizada.
11. ~~Obter versão legível das Portarias nº 4.101/2023, nº 1.164/2025 e
    nº 253/2026~~ — ✅ **Concluída em 14/08/2026** pelos novos uploads.
12. ~~Confirmar se a Portaria nº 253/2026 substituiu o Integra+ (nº 923/2020)~~ —
    ✅ **Confirmado em 14/08/2026:** cadeia nº 923/2020 → nº 1.257/2022 →
    nº 253/2026 (vigente).
13. Depositar a Portaria ICMBio nº 99/2020 (regras do trabalho consultivo,
    referida no art. 25 da Portaria nº 1.572/2023).
14. ~~Reescrever e reinstalar as 7 skills da suíte `cgov-nt`~~ — ✅
    **Concluída em 05/08/2026** (Decisão 17, Seção 13).
15. ~~Obter versão legível do Código de Ética (Portaria nº 411/2020), da
    Portaria MMA nº 296/2021 e da Portaria ICMBio nº 2.917/2026~~ — ✅
    **Resolvida em 29/08/2026 por transcrição OCR revisada em Markdown.** Os
    PDFs continuam sendo digitalizações sem camada textual confiável, mas os
    arquivos `.md` locais correspondentes passaram a ser legíveis por máquina
    e citáveis após conferência com o PDF.
16. **Definir institucionalmente o foro** de apresentação dos resultados de
    tratamento de risco, diante da revogação da PGE e da não recriação da RAE
    (Seção 14.2). Candidato natural: o CTGRIC, do qual a CGOV é
    Secretaria-Executiva.
17. Avaliar a **atualização da Portaria nº 975/2021**, que contém duas remissões
    desatualizadas: à PGE revogada (RAE) e à Portaria nº 923/2020 (Integra+).
18. Depositar a **IN ICMBio nº 14/2025** (regras do PGD) e a **Portaria GM/MMA
    nº 1.012/2024** (Acordo de Gestão), ausentes do acervo.
19. **Revisar o núcleo `analista-governanca.md` (v4.0)** linha a linha antes de
    uso em produção — condensação de um documento validado por várias
    rodadas, feita em 29/08/2026 sem segunda verificação humana.
20. **Decidir o destino de `analista-processos-sei.md`** frente à sobreposição
    com `escritorio-cgov.md` e a própria suíte de skills dentro do Claude
    Cowork (fundir, manter separado ou aposentar).
21. ~~Instalar `cgov-transcrever-normativos` no Claude/Cowork~~ — ✅
    **Concluída em 30/08/2026** (Decisão 37, Seção 22). Instalada via
    `save_skill`; scripts auxiliares permanecem alcançáveis apenas em sessões
    deste projeto (caminho relativo à pasta montada), e o OCR usa a
    capacidade de PDF do próprio ambiente Cowork em vez do script PowerShell.
22. **Confirmar a sincronização das Instruções do Projeto Cowork** com
    `docs/system-instructions/escritorio-cgov.md` (Decisão 35, Seção 20) — o
    Coordenador colou o conteúdo, mas a correção de
    `local/installed-reference/` foi feita depois; abrir uma conversa nova
    neste projeto para conferir, ou colar novamente o texto já corrigido.
23. ~~Desambiguar `cgov-gestao-riscos` × S10 do `pgd-agente-icmbio`~~ — ✅
    **Concluída em 30/08/2026** (Decisão 39, Seção 24), no lado
    `cgov-geral-v1`. Fica como **sugestão ao Coordenador** replicar a mesma
    distinção do lado do `pgd-agente-icmbio` (fora do escopo de edição desta
    sessão).

## 26. Saneamento e instalação das skills temáticas no Codex (25/09/2026)

**Contexto.** A documentação vigente do Codex usa `.agents/skills` para
skills de projeto e aceita no frontmatter de `SKILL.md` as propriedades
funcionais da skill, como `name`, `description` e `metadata`. Seis fontes
temáticas ainda mantinham propriedades superiores que descreviam o estado
histórico da instalação no Claude (`instalado_em`, `status` e, em dois casos,
`revisao`). Esses campos não orientavam a execução e impediam a validação pelo
`quick_validate.py` atual. O espelho local do Codex também estava incompleto:
`cgov-qcf` não existia e as demais instalações não preservavam avaliações e
scripts auxiliares.

**Decisão 40 — saneamento de frontmatter e sincronização do espelho Codex.**

1. Remover do nível superior do frontmatter de `cgov-air-arr`,
   `cgov-cadeia-valor`, `cgov-gestao-riscos`, `cgov-pgr`, `cgov-qcf` e
   `cgov-regimento-interno` os campos históricos `instalado_em`, `status` e,
   onde existente, `revisao`, preservando integralmente `name`, `description`
   e o corpo operacional.
2. Em `cgov-transcrever-normativos`, preservar o bloco `metadata` e
   `criado_em: "2026-08-29"`, mas reduzir `status` para `"fonte canônica"`,
   retirando a afirmação circunstancial de que o espelho da Antigravity estava
   sincronizado.
3. Sincronizar os sete pacotes completos em `.agents/skills`, incluindo os
   arquivos de avaliação e os três scripts de
   `cgov-transcrever-normativos`. Não copiar `scripts/__pycache__`, por ser
   artefato local gerado pelo Python.
4. Preservar as alterações locais já existentes de `cgov-gestao-riscos` e
   `cgov-regimento-interno`, e usar as fontes locais ainda não rastreadas de
   `cgov-qcf` e `cgov-transcrever-normativos`, sem substituí-las por cópias de
   caches externos.
5. Validar fonte e espelho por estrutura, tamanho e SHA-256. Os sete pacotes
   passaram no `quick_validate.py`; os JSON de avaliação e scripts auxiliares
   passaram nas verificações de sintaxe.

O estado anterior foi preservado em backup temporário fora do repositório. A
pasta `.agents/` permanece ignorada pelo Git e funciona como espelho local; as
fontes canônicas continuam em `skills/thematic/`.

## 27. Migração para o WSL e separação dos fluxos de desenvolvimento e operação (06/10/2026)

**Contexto.** Com o repositório migrado para o WSL (`~/projetos/cgov-geral-v1`,
commit `393471f`), decidiu-se usar o Claude Code para o desenvolvimento das
skills e o Claude Cowork para o trabalho técnico e administrativo da CGOV.
Verificou-se que o Windows não segue os links do repositório para o Google
Drive quando acessa a pasta por `\\wsl.localhost\...`: vincular o repositório
ao Cowork deixaria as fontes normativas inacessíveis, exigiria o WSL ligado e
exporia o código-fonte das skills a edições do ambiente de produção.

**Decisões.**

1. A área operacional do Cowork passa a ser a pasta CGOV do Google Drive. Os
   arquivos de texto das análises (427 arquivos) foram copiados para
   `_acervo-escritorio-virtual/analyses/`, juntando-se aos binários já ali,
   com conferência arquivo a arquivo; `local/analyses` passou a ser link para
   essa pasta (`CGOV_ANALYSES` no `.env`).
2. As skills continuam citando `local/analyses/` e `local/normative-sources/`;
   as instruções do Cowork (`escritorio-cgov.md`, Seção 3) trazem um mapa de
   caminhos para a estrutura do Drive. Tornar as skills neutras quanto ao
   caminho fica como pendência.
3. A passagem do desenvolvimento para a operação é feita por
   `scripts/publicar-operacao.sh`, que publica somente o que está em commit:
   pacotes `dist/skills/*.zip` para reinstalação e cópia só leitura de `docs/`
   em `_acervo-escritorio-virtual/_referencia/`. O script também compara as
   skills instaladas com a fonte.
4. O retorno da operação para o desenvolvimento é feito por
   `_acervo-escritorio-virtual/manutencao/PENDENCIAS.md`.
5. `.claude/settings.json` passa a exigir confirmação para `git commit` e
   `git push`, bloquear a edição das áreas operacionais e ocultar do modelo as
   14 skills cuja fonte está no repositório, para que as sessões de
   desenvolvimento trabalhem sobre a fonte.

**Resultado.** A primeira verificação apontou como desatualizadas as versões
instaladas de `cgov-cadeia-valor`, `cgov-pgr` e `cgov-regimento-interno`
(caminhos antigos `REGISTRO_DECISOES.md` e `04_fontes_normativas/`). Instruções
completas em [`docs/fluxos-de-trabalho.md`](../fluxos-de-trabalho.md).

## 28. Reorganização da pasta operacional CGOV (Fase 4 do plano de implantação, 05–06/11/2026)

**Contexto.** A pasta operacional CGOV (Google Drive) reunia 2.831 arquivos (3,3 GB) em oito áreas com
convenções diferentes: processos divididos entre `CGOV_Processos/` e `_acervo-escritorio-virtual/analyses/`,
acervo normativo duplicado (`normative-sources/` e `CGOV_Normativas/`), 433 grupos de arquivos idênticos e
backups de desenvolvimento misturados ao trabalho. As decisões do §27 (área operacional no Drive,
`local/analyses` como link, mapa de caminhos nas instruções do Cowork) ficam superadas nos pontos abaixo.

**Decisões.**

1. **Estrutura nova** (ADR-012 do plano): `00_entrada`, `01_processos` (uma pasta por processo SEI, com
   `PROCESSO.md`, `documentos-sei/`, `trabalho/`, `referencias/` e `produtos/`), `02_notas-tecnicas`,
   `03_normativos` (acervo único), `04_colegiados`, `05_projetos`, `06_gestao-da-coordenacao`,
   `90_escritorio-virtual` (infraestrutura publicada) e `99_arquivo`; `LEIA-ME.md` e `AGENTS.md` na raiz.
2. **Execução por mapa** arquivo a arquivo (`scripts/reorganizar_cgov.py`, v1.0.0 a v1.2.2), aprovado pelo
   Coordenador, em sete lotes, com SHA-256 conferido antes de cada movimentação, registro de cada operação e
   reversão possível. Nada foi excluído: descartes foram para `99_arquivo/_a-excluir_2026-11-05/`, a revisar
   após 30 dias (ADR-014).
3. **Projetos Cowork por processo passam a ser exceção** (ADR-013): o trabalho de processo é feito no projeto
   "Escritório CGOV — Operação"; as instruções dos projetos antigos foram copiadas para as fichas
   `PROCESSO.md`/`PROJETO.md` ou guardadas no acervo local antes do arquivamento.
4. **Camada de navegação** (`operacao/` como fonte, antecipada da Fase 5): `LEIA-ME.md`, `AGENTS.md`,
   `_LEIA-ME.md` por área, modelo `PROCESSO.md` e `_INDICE.md` gerados por `scripts/gerar_indices.py`.
5. **Transição de caminhos** (ADR-006): até as skills ficarem neutras quanto ao caminho (Fase 6.3), o
   `AGENTS.md` da pasta traduz os caminhos antigos citados pelas skills (`local/analyses/…`,
   `CGOV_Processos/…/_CGOV_NT/`, `local/normative-sources/`) para os novos. As instruções do projeto Operação
   estão em [`docs/system-instructions/escritorio-cgov-operacao.md`](../system-instructions/escritorio-cgov-operacao.md);
   as anteriores (`escritorio-cgov.md`) foram arquivadas.

**Resultado.**

- 2.860 operações em sete lotes, todas `ok`; 74 pastas de processo; 109 normativos em `03_normativos`;
  20 Notas Técnicas na série oficial; 587 itens em quarentena; 343 pastas antigas vazias removidas
  (somente pastas vazias, após conferência de zero arquivos); 9 arquivos pessoais levados para fora da
  pasta institucional.
- Manifesto posterior: 2.833/2.833 hashes do manifesto anterior encontrados no destino previsto (100%).
- 74 fichas `PROCESSO.md` e 5 índices publicados; campos não dedutíveis marcados ⚠️ para revisão gradual.
- Projeto "Escritório CGOV — Operação" criado e testado: a triagem gravou em `01_processos/…/trabalho/`
  sem criar `local/`.
- Mapa, manifestos, decisões e registros copiados para `90_escritorio-virtual/manutencao/reorganizacao-2026-11/`.

**Achados e pendências.** A `cgov-nt-01-triagem` instalada grava em `CGOV_Processos/…/_CGOV_NT/`, diferente
da fonte (`local/analyses/`): deriva fonte × instalado a corrigir na Fase 6.1. Pendências de conteúdo
(campos ⚠️ das fichas, nomes da série de NTs, normas ausentes do acervo, vigência dos normativos) ficam com a
revisão gradual e com a Fase 6. O modelo geral de análise de atos normativos derivado do processo de Termos
de Compromisso passa a ser objetivo da etapa 6.9 do plano. Detalhes, números e evidências: plano de
implantação v3.23, Fase 4.

## 29. Atualização do repositório de desenvolvimento (Fase 5 do plano de implantação, 06–07/11/2026)

**Contexto.** Depois da reorganização da pasta CGOV (§28), o repositório ainda tinha scripts *bash* do WSL
que recriariam a estrutura antiga, junções `local/analyses`, `local/normative-sources` e `local/acervo-drive`
apontando para pastas inexistentes, bloqueios de edição com os nomes antigos, nenhuma verificação automática
de sanitização e uma cópia de `docs/` publicada para a operação anterior à migração para o Windows.

**Decisões.**

1. **Ordem e método** (D37 do plano): seis blocos no *branch* `implantacao/fase-5`, um *commit* por bloco,
   com *merge* e publicação só no fim. A verificação de sanitização foi antecipada para o início, e os
   bloqueios de edição entraram antes das junções.
2. **Sanitização automática** (D38): `scripts/verificar_sanitizacao.py`.
   - **Erros (bloqueiam o *commit*):** caminhos pessoais, e-mails, CPF, matrícula, segredos e arquivos PDF ou
     Office.
   - **Avisos:** números de processo e documento SEI.
   - **Configuração:** exceções versionadas em `scripts/sanitizacao_permitidos.txt`; termos pessoais só em
     `local/`.
   - **Plano de implantação:** os caminhos com o nome de usuário passaram a usar `%USERPROFILE%`.
3. **Quebras de linha** (etapa 5.7): `.gitattributes` com LF, e CRLF só para `.ps1`, `.bat` e `.cmd`; o
   `.gitignore` passou a cobrir as notas do Obsidian e o Power BI.
4. **Bloqueios de edição** (D39): `.claude/settings.json` nega a edição pelas junções novas, pela pasta CGOV
   no caminho real (`~/My Drive/10_Institucional/CGOV/**`) e no `.env`. A documentação do Claude Code
   confirma que a regra deny vale para o link e para o alvo, mas não alcança scripts que abrem arquivos por
   conta própria.
5. **Scripts em Python** (ADR-004, aceito pela D40):
   - `scripts/link_acervo.py` cria `local\processos`, `local\normativos` e `local\escritorio` e remove
     só o ponteiro das junções antigas;
   - `scripts/publicar_operacao.py` publica só o HEAD; o que substitui na pasta CGOV vai antes para
     `99_arquivo/_a-excluir_<data>/publicacao_<commit>/`, e o que grava é conferido por SHA-256;
   - os `.sh` do WSL foram para `archive/scripts-wsl/`.
6. **Documentação** (D36 e D40):
   - `docs/fluxos-de-trabalho.md` v2;
   - `docs/governance/pendencias.md`;
   - os 14 ADRs em `docs/adr/` (ADR-004 e ADR-007 aceitos);
   - `docs/catalogo-skills.md` e `docs/README.md`;
   - o plano movido para `docs/plano-implantacao.md`.

**Resultado.**

- Junções novas criadas e antigas removidas no Windows; o teste de bloqueio no Claude Code negou a gravação
  pela junção e pelo caminho real.
- Sanitização: 0 erros na árvore inteira (os avisos são números SEI, conforme a D38).
- `publicar_operacao.py --verificar`: `operacao/` 12/12 igual ao publicado. A referência de `docs/` estava
  no *commit* `4960e11` e é republicada no fechamento da fase.
- **Pendência confirmada:** 9 das 14 skills com fonte estão desatualizadas na conta (P4), maior que o
  registrado antes; a reinstalação fica para a Fase 6.8, depois da comparação da 6.1.

Detalhes, números e evidências: plano de implantação (`docs/plano-implantacao.md`), Fase 5.

---

## 30. Exportação e comparação das skills instaladas (Fase 6.1 do plano de implantação, 07/11/2026)

**Contexto.** Desde a Fase 4, a fonte (`skills/`) e as skills instaladas na conta divergem (pendência P4). Antes de
editar qualquer skill na Fase 6, era preciso fixar qual texto vale para cada uma.

**Decisões.**

1. **Ordem da Fase 6** (D42 do plano): 6.1 → decisões 6.6 + 6.9(a) → 6.2 → 6.3 → 6.5 → 6.9(b–d) → 6.4 → 6.7 (em
   qualquer intervalo) → 6.8.
2. **Método de exportação** (D42): copiar o retrato da conta recebido pela sessão do Cowork para
   `local/installed-reference/_export_2026-11-07/` (fora do Git), com manifesto SHA-256, e conferi-lo no PowerShell do
   Coordenador contra a cópia sincronizada do Claude Code (`%USERPROFILE%\.claude\skills\synced\`). As duas
   `cgge-fgbio-*`, fora do inventário, também foram exportadas; o destino delas se decide na 6.2.
3. **Critério de comparação:** a conta reescreve o *frontmatter*, então a comparação usa a normalização de
   `publicar_operacao.py` (nome, descrição e corpo), não só o SHA-256 dos arquivos.
4. **Texto-base de cada skill divergente** (D43):
   - suíte `cgov-nt` (7): **fonte**, com a busca do `NT_ESTADO.md` em ordem e o aviso de local legado aproveitados da
     conta, em forma neutra na 6.3. As duas convenções (`local/analyses/`, da fonte, e `_CGOV_NT/`, da conta, de
     07/10/2026) estão superadas por `01_processos/…/trabalho/` (§28);
   - `cgov-gestao-riscos`: **conta**, uma reescrita com o Regime A (Portaria ICMBio nº 975/2021, vigente) e o Regime B
     (minutas RADAR). Ela é saneada na promoção: os números de documentos SEI viram referência genérica às minutas, e
     a descrição é recomposta na 6.5;
   - `cgov-regimento-interno`: **fonte** (a conta ainda cita `REGISTRO_DECISOES.md`);
   - `cgov-avaliar-entrega`, `cgov-elaborar-entrega` e `cgov-registro-execucao`: **conta**, com a correção de
     14/09/2026 (Plano de Entregas **quadrimestral**: Q1 01/01–30/04, Q2 01/05–31/08, Q3 01/09–31/12, sem Q4). A nota
     de correção vira regra no corpo, e este parágrafo guarda o histórico: as versões anteriores tratavam Q1–Q3 como
     trimestres e previam um Q4 implícito.

**Resultado.**

- 28 skills e 39 arquivos exportados; conferência cruzada 39/39 igual.
- 14 com fonte: 5 iguais e 9 divergentes (confirma P4). 12 sem fonte: 9 iguais à `installed-reference` e 3 mais novas
  na conta. Nenhum arquivo auxiliar faltando; `evals/` só na fonte, como esperado.
- Relatório e diffs: `local/installed-reference/_export_2026-11-07/COMPARACAO.md` e `diffs/` (fora do Git).

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

---

## 31. Analista de processos SEI e modelo geral de análise de atos normativos (Fase 6.6 e 6.9(a), 07/11/2026)

**Decisões.**

1. **D4 (etapa 6.6):** criar a skill `cgov-triagem-processo-sei` a partir de `docs/system-instructions/analista-processos-sei.md`
   (roteamento e cadeia de raciocínio, passos 0–7), lendo a base normativa no acervo em vez de copiá-la. O `.md` continua
   como versão autocontida para assistentes sem acesso a arquivos (Gems, GPTs); quando um fato normativo mudar, os dois
   textos são atualizados juntos (lição do §11.6). A skill nasce com caminhos neutros, junto com a 6.4.
2. **D44 (etapa 6.9(a)), as 6 questões da Parte B.5 das instruções gerais v1:**
   - AIR: o **Nível 2** (subsídios pelo art. 6º do Decreto nº 10.411/2020) é padrão sempre que o Nível 1 não concluir por
     não incidência ou dispensa;
   - **competências e legística são obrigatórias**, como a modelagem de fluxos, os riscos e a AIR. São cinco subsídios
     obrigatórios da NT, com dispensa só pelo Coordenador, registrada com o motivo no `NT_ESTADO.md`;
   - o **foco no conteúdo do ato** não vira regra geral: a triagem (`cgov-nt-01`) pergunta o foco em cada projeto;
   - os **dispositivos propostos** na NT ficam no **futuro do presente**, que é a convenção atual da suíte. O Decreto
     nº 12.002/2024, art. 11, I, "e", admite o presente ou o futuro do presente e pede uniformidade (texto conferido na
     publicação original, no portal da Câmara dos Deputados). A `cgov-saneamento-legistica` é ajustada; a `cgov-nt-03` não;
   - no Regime A, um **risco residual** com valor em lacuna da máscara vai para a **classe superior**, com a lacuna
     declarada (entre 2 e 3, Médio);
   - `01_processos/…/trabalho/` substitui `_CGOV_NT/` e `local/analyses/`, e as skills usam **texto neutro** ("pasta de
     trabalho do processo"), conforme o ADR-006 e a etapa 6.3.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

---

## 32. Propostas de skills a partir da pasta de prompts (Fase 6, etapa 6.10, 07/11/2026)

**Contexto.** O Coordenador pediu uma análise da pasta de prompts `%USERPROFILE%\My Drive\_projetos\02_dev-prompts\`
(instruções de sistema do Google AI Studio, de 2023 a 2026) para identificar propostas de skills. A pasta foi lida
sem alterações e comparada com as 28 skills exportadas na 6.1, com as previstas e com o Art. 37 da Portaria ICMBio
nº 5.592/2025.

**Decisões (D45 do plano).**

1. **Novas skills, na etapa 6.10:**
   - `cgov-secretaria-colegiados`: atas a partir de transcrição, pautas e encaminhamentos;
   - `cgov-integridade`: Programa e Plano de Integridade, SITAI, Integra+;
   - `cgov-carta-servicos`: Lei nº 13.460/2017, com o script de classificação das entregas do PETRVS;
   - `cgov-projetos-cooperacao`: TdR, Nota Informativa e POA, genérica para cooperantes (primeiro caso, GIZ).
2. **Ampliações, junto com a 6.9(b):**
   - `cgov-nt-06-quesitos-pfe`: consulta jurídica facultativa e NT de subsídio. A Portaria Conjunta nº 3/2021 precisa
     ser conferida antes;
   - `cgov-modelar-fluxo`: modo BPMN → tabela de atividades/POP.
3. **Escopo da `cgov-triagem-processo-sei` (D4):** só a CGOV (Art. 37). As instruções da CGGE (Art. 36) ficam como
   referência.
4. **Adiada:** a skill da Política de Governança Institucional (inciso II), na pendência E7.
5. **Descartados:** Microsoft Teams, Relatório de Gestão, Transparência Ativa, LGPD, Dev gov.br, prompts acadêmicos e
   pessoais.
6. **Cuidado:** os prompts citam o Regimento Interno anterior (Art. 50) e trazem números SEI e caminhos pessoais. Eles
   servem só de insumo: as normas são conferidas no acervo e o texto passa pela sanitização.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

---

## 33. Promoção das skills sem fonte a `skills/` (Fase 6.2, 07/11/2026)

**Decisões (D46 do plano).**

1. **Famílias:** `skills/pgd/`, com as 8 skills do PGD (Art. 37, p.u., VII), e `skills/normativo/`, com as 4 de análise de
   atos normativos. As famílias são provisórias: a Fase 7.1 passa todas para a estrutura plana do plugin.
2. **`cgge-fgbio-apresentacao` e `cgge-fgbio-plano-aula`:** versionadas em `skills/cgge-fgbio/`, **fora** do plugin
   `cgov-escritorio`. Os nomes do docente e dos convidados foram trocados por papéis, e os dados da turma ficam em `local/`.
3. **Nomes da equipe** na `cgov-elaborar-entrega`: trocados por marcadores. A skill passa a ler a lista da equipe mantida
   na pasta CGOV (pendência C7).
4. **Número do processo de referência do PSPEADBio** nas três skills normativas: retirado agora. A retirada do contexto
   padrão fica para a 6.9(c).

**Resultado.**

- 22 arquivos copiados da exportação `_export_2026-11-07`, depois de preparados em `local/pilots/6.2_promocao/`.
- Também saneados: e-mail pessoal, CPF de exemplo, caminhos absolutos da unidade H: e caminhos `/home/…` de exemplo.
- Nas três skills de entregas, a nota de correção do ciclo quadrimestral virou regra no corpo (D43).
- 14 skills novas em `skillOverrides` no `.claude/settings.json`.
- Sanitização: 0 erros.
- **Lição aprendida:** a busca manual na exportação não pegou o CPF de exemplo nem os caminhos absolutos da unidade H:. A verificação
  definitiva é o `verificar_sanitizacao.py` no `skills/`, que não alcança `local/`. Quando houver preparo em `local/`, a
  varredura com o script vem logo depois da cópia e antes do *commit*.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

---

## 34. Prefixo `pgd-` nas skills do PGD (Fase 6.2, 07/11/2026)

**Decisão (D47 do plano, pedido do Coordenador).** As 8 skills de `skills/pgd/` passam a se chamar `pgd-especialista`
(antes `cgge-especialista-pgd`), `pgd-elaborar-entrega`, `pgd-registro-execucao` e `pgd-avaliar-entrega` (antes com o
prefixo `cgov-`), e `pgd-analisar-indicador`, `pgd-desenvolver-indicador`, `pgd-implementar-indicador` e
`pgd-testar-indicador` (antes `cgov-pgd-…`).

**Aplicação.**

- **Antes do *commit* da 6.2:** pastas, campo `name:`, referências cruzadas em `skills/` (inclusive `cgov-pgr` e
  `cgov-gestao-riscos`), `skillOverrides` e documentação atual (catálogo, `overview.md`, pendências, plano). Os registros
  anteriores deste log mantêm os nomes antigos.
- **Na 6.8:** instalar as 8 com os nomes novos, excluir da conta os 8 nomes antigos (com confirmação) e atualizar as
  instruções do projeto Operação e `analista-processos-sei.md`. Até lá, o `--verificar` mostra as 8 como "NÃO INSTALADA".

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

---

## 35. Caminhos neutros nas skills (Fase 6.3, 07/11/2026)

**Decisões (D48 do plano).**

1. **ADR-006 aceito.** As skills citam papéis, e os caminhos concretos ficam nos dois `AGENTS.md`: a seção "Caminhos
   por papel" do repositório e a tabela "Caminhos canônicos" de `operacao/AGENTS.md`.
2. **Papéis novos na pasta CGOV:**
   - pasta de rascunhos da transcrição: `03_normativos/_transcricao/<data-hora>-<slug>/`, fora do `_INDICE.md`;
   - pasta de trabalho do PGD: `06_gestao-da-coordenacao/pgd/`;
   - lista da equipe: `06_gestao-da-coordenacao/equipe.md`, com nome e papel, sem matrícula nem e-mail;
   - registro de decisões: `PROCESSO.md` do processo, seção Andamento;
   - pasta de processos: `01_processos/`.
3. **Localização do `NT_ESTADO.md`** (7 skills `cgov-nt`, conforme a D43): a busca segue esta ordem: pasta conectada,
   pasta de processos pelo número SEI e, por fim, local antigo listado no `AGENTS.md` ou pasta com `MOVIDO_PARA.txt`,
   com aviso ao usuário. A `cgov-nt-01` cria a pasta do processo pela obrigação 1 do `AGENTS.md`.
4. **Normas citadas por nome de arquivo** (`cgov-pgr`, `cgov-qcf`): passam a ser localizadas no acervo pelo número da
   norma, porque os nomes dos arquivos mudaram na Fase 4.
5. **Publicação:** os papéis novos do `operacao/AGENTS.md` são publicados logo depois do *commit*. Na 6.8, depois da
   reinstalação, sai só a frase de tradução para as skills instaladas. A tabela de caminhos antigos continua como
   "Locais antigos", porque as skills a usam para achar arquivos legados.
6. **`gerar_indices.py` v0.1.1:** pastas iniciadas por `_` ficam fora do índice do acervo normativo.

**Resultado.** 13 arquivos de skills alterados. A busca por `local/analyses`, `_acervo-escritorio-virtual`,
`normative-sources`, `_CGOV_NT` e `CGOV_Processos` em `skills/` dá 0, e a sanitização não acusou erros.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

---

## 36. Descrições, rebase da `cgov-gestao-riscos` e eval da `cgov-nt-01` (Fase 6.5, 07/11/2026)

**Decisões (D49 do plano).**

1. **Descrições:** as 8 descrições acima de 950 caracteres foram encurtadas sem mudar o corpo das skills. Agora as 28
   têm no máximo 950 caracteres (a maior, 878). No `pgd-especialista`, o gatilho genérico passa a valer só no contexto
   do PGD da CGGE, para não disputar o acionamento com as skills temáticas.
2. **`cgov-gestao-riscos`:** aplicada a D43 (§30). A fonte passa a ser a versão da conta, com os Regimes A e B, saneada:
   - os números de documentos SEI das minutas foram retirados, e o número passa a ser buscado na ficha ou na pasta de
     trabalho do processo;
   - as minutas ficam na pasta de trabalho do processo da Política de Gestão de Riscos, e não no acervo (D23).
3. **Eval de gatilho da `cgov-nt-01`:** incorporado do *branch* `claude/cgov-nt-triagem-description-loop-6x6dsc`, de
   29/08/2026, em `evals/trigger_eval.json`:
   - os números de processo foram trocados por fictícios;
   - 5 rótulos foram corrigidos para "não aciona", porque pertencem a outras skills: riscos, competências, AIR, SIPOC
     e conclusão;
   - entrou `loop_results/` no `.gitignore`, mas não `/.claude/`, porque `.claude/settings.json` é versionado;
   - o *branch* é apagado.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

---

## 37. Modelo geral de análise de atos normativos nas skills (Fase 6.9(b)–(d), 07/11/2026)

**Decisões (D50 do plano).**

1. **Roteiro da `cgov-nt-01`.** A análise de ato normativo passa a exigir cinco subsídios **antes** dos capítulos:
   fluxos, competências, legística, riscos e AIR (D44). Só o Coordenador pode dispensar um deles, e a dispensa fica
   registrada em "Decisões do projeto" no `NT_ESTADO.md`. A triagem também passa a perguntar o foco da análise e se o
   ato substitui norma vigente.
2. **As 8 divergências da Parte B.4** das instruções gerais v1 foram corrigidas nas skills. As principais:
   - **tempo verbal:** o futuro do presente nos dispositivos propostos é convenção da CGOV, e a legística passa a
     cobrar uniformidade, que é o que o Decreto nº 12.002/2024 (art. 11, I, "e") exige;
   - **Quadro Consolidado:** a `nt-05` passa a lê-lo no produto do Cap. 2-3;
   - **`cgov-gestao-riscos`:** ganhou a seção 3.9, com a regra para controles sem evidência de funcionamento: no
     máximo Mediano no Regime A e Fraco no Regime B;
   - **PSPEADBio:** deixa de ser o contexto padrão e fica só como exemplo;
   - **códigos:** convenção única (`F1-01`, `C-01`, `LS-01`, `E-01`/`L-01`, `RSC-01`, `PJ-01`).
3. **Ampliações (D45):**
   - `cgov-nt-06`: Modo 2, para consulta jurídica facultativa e NT de subsídio. A Portaria Conjunta nº 3, de
     13/05/2021, teve só a ementa confirmada; os artigos e anexos ainda precisam ser conferidos no acervo (⚠️);
   - `cgov-modelar-fluxo`: Modo 2, de BPMN para tabela de atividades/POP;
   - `cgov-air-arr`: uso como subsídio, com o Nível 1 sempre e o Nível 2 como padrão.
4. **Inciso do Art. 37 para competências e legística:** fica com ⚠️ até o piloto da Fase 11.
5. **Publicação:** o procedimento v2 vai para `docs/procedimentos/analise-atos-normativos.md`, e o modelo de
   instruções para `operacao/90_escritorio-virtual/modelos/analise-ato-normativo/INSTRUCOES-PROJETO.md`. A citação nas
   instruções do projeto Operação (Apêndice B) fica para a 6.8.
6. **Pasta de rascunhos da transcrição:** a D48 (§35) é alterada. Os rascunhos passam a ficar em
   `90_escritorio-virtual/transcricoes/`, pasta que já existia, e não em `03_normativos/_transcricao/`. A obrigação 3 do
   `operacao/AGENTS.md` ganhou essa exceção.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

---

## 38. Skills de operação do Escritório (Fase 6.4 e skill da 6.6, 07/11/2026)

**Decisões (D51 do plano).**

1. **Família nova `skills/escritorio/`** para as skills de operação que não pertencem a um inciso do Art. 37.
2. **`cgov-gestao-acervo`:** 5 modos (TRIAR_ENTRADA, NOVO_PROCESSO, ATUALIZAR_FICHA, ATUALIZAR_INDICES, ARQUIVAR), com
   5 casos sintéticos de eval. A skill nunca exclui nem sobrescreve arquivos e só move em lote depois de mostrar a lista
   e receber confirmação, com conferência por SHA-256.
3. **Índices na operação:** `publicar_operacao.py` v0.2.0 passa a publicar `scripts/gerar_indices.py` em
   `90_escritorio-virtual/ferramentas/`. A fonte continua única, no repositório; na pasta CGOV o script só é executado,
   nunca editado.
4. **`cgov-triagem-processo-sei`** (D4, só CGOV): roteamento, cadeia de raciocínio e guardrails do
   `analista-processos-sei.md` v7.2. A base normativa não é copiada: `references/pilares-normativos.md` traz só os nomes
   das normas, e `references/formatos-de-saida.md` traz os comandos. Tem 3 casos sintéticos.
5. **Pendência E8:** o Coordenador transcreveu a Portaria ICMBio nº 129/2020 (atos normativos do ICMBio) e a Portaria
   Conjunta PFE/ICMBio nº 3/2021. Elas precisam ser lidas antes da 6.10, porque a 129/2020 pode ter alterado a Portaria
   nº 271/2013, base da `cgov-nt-06`.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

## 39. Normas sobre atos administrativos: Portarias nº 271/2013 e nº 129/2020 (pendência E8, 07/11/2026)

1. **Leitura do acervo:** o Coordenador vinculou de novo a pasta `03_normativos` (leitura). Foram lidas a Portaria
   ICMBio nº 271/2013 (27/12/2013), a Portaria ICMBio nº 129/2020 e o arquivo "Portaria Conjunta ICMBio PFE 03-2021".
   Esse arquivo é a Portaria PFE/ICMBio nº 3/2021, que aprova a OJN nº 27/2021 (aviso de recebimento na comunicação
   postal). A Portaria Conjunta nº 3, de 13/05/2021, sobre consultas jurídicas à PFE, não está no acervo.
2. **Relação entre as normas (D52):** a nº 129/2020 define as espécies de ato normativo desde 02/03/2020 (Portarias,
   Resoluções e Instruções Normativas; art. 2º) e a vigência em data certa (art. 10), e não revoga expressamente a
   nº 271/2013. Onde as duas colidem (espécies e vigência), prevalece a nº 129/2020; no resto, vale a nº 271/2013
   (Anexo I: submissão à AGU, documentos da proposta, impacto orçamentário e conteúdo da consulta jurídica), com ⚠️
   sobre a vigência residual, a confirmar com a PFE.
3. **Correções (13 arquivos):** `cgov-nt-06`, `cgov-nt-01`, `cgov-saneamento-legistica`, `cgov-air-arr`,
   `cgov-comparar-versoes`, `cgov-triagem-processo-sei` (com duas referências), `analista-processos-sei.md` v7.3, dois
   anexos do `analista-governanca`, o procedimento de análise de atos normativos e o modelo de instruções do projeto.
4. **Curadoria (C8):** renomear os dois arquivos do acervo e refazer a numeração do Anexo II da nº 271/2013 na
   transcrição fica com a operação. A Portaria Conjunta nº 3/2021 continua na pendência C3.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

## 40. Quatro skills temáticas novas da pasta de prompts (Fase 6.10, 07/11/2026)

1. **Skills (D53):** `cgov-secretaria-colegiados`, `cgov-integridade`, `cgov-carta-servicos` e
   `cgov-projetos-cooperacao`, em `skills/thematic/`, com `skillOverrides` *user-invocable-only* e 3 evals
   sintéticos cada. Os prompts da pasta `02_dev-prompts` foram só insumo (D45); toda norma foi conferida no acervo.
2. **Normas atualizadas em relação aos prompts:** o CTGRIC é regido pela Portaria ICMBio nº 4.529/2025, que
   revogou a nº 4.007/2023 e faz da CGOV a Secretaria-Executiva (art. 2º, II); o Programa Integra+ e o Plano de
   Integridade 2026–2028 são as Portarias nº 253/2026 e nº 257/2026, e a CGOV é Unidade Setorial de Integridade
   (Portaria nº 253/2026, art. 5º, § 2º).
3. **Carta de Serviços:** enquadrada pelo Coordenador no Art. 37, parágrafo único, VI, como desdobramento do
   Catálogo de Produtos e Serviços; a skill não diz que o inciso menciona a Carta.
4. **Script:** o script original tinha credencial de banco em texto aberto (pendência S1). A skill usa
   `scripts/classificar_entregas.py` v0.1.0, que lê um CSV exportado pelo usuário, não se conecta a banco e compara
   palavras inteiras sem acento.
5. **Projetos de cooperação:** a skill é genérica; os dados do projeto com a GIZ ficam em `references/giz.md`,
   marcados para confirmação.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

## 41. Alcance dos evals da reinstalação (Fase 6.8, D54, 07/11/2026)

1. **Alcance:** antes da reinstalação, rodar os evals qualitativos das 9 skills alteradas que já têm casos
   (`cgov-nt-01-triagem`, `cgov-nt-06-quesitos-pfe`, `cgov-triagem-processo-sei`, `cgov-gestao-acervo`,
   `cgov-saneamento-legistica`, `cgov-secretaria-colegiados`, `cgov-integridade`, `cgov-carta-servicos` e
   `cgov-projetos-cooperacao`; 28 casos).
2. **Execução:** pelo Claude, na sessão do projeto de implantação, com subagentes sobre as fontes do repositório
   e o acervo normativo; quem executa um caso não o avalia.
3. **Sem casos:** as 13 skills sem `evals.json` (8 `pgd-*`, 2 `cgge-fgbio-*`, `cgov-auditoria-competencias`,
   `cgov-comparar-versoes`, `cgov-modelar-fluxo`) ficam na pendência E9.
4. **Duas entregas:** 6.8a antes da reinstalação (evals, instruções do projeto Operação v1.1,
   `analista-processos-sei.md` v7.4) e 6.8b depois ("Locais antigos" no `operacao/AGENTS.md`), porque a tabela
   de caminhos antigos ainda serve às skills instaladas.

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

## 42. Resultado dos evals e correções antes da reinstalação (Fase 6.8a, 07/11/2026)

1. **Evals (D54):** 28 casos de 9 skills, executados e avaliados por agentes diferentes: 129 de 134 expectativas
   (96%). As 5 falhas eram de casos sem os insumos necessários, e não de respostas erradas.
2. **D55:** a `cgov-nt-06-quesitos-pfe` entrega rascunho condicionado quando a redação é pedida antes dos
   capítulos 2 a 4: responde os quesitos que dependem só do ato e do acervo e marca os quesitos 1, 2, 7 e 8 como
   `[A PREENCHER — depende do Cap. N]`, com ⚠️.
3. **D56:** a convenção do futuro do presente na redação saneada continua, com exceções: ficam no presente as
   fórmulas de objeto, competência, revogação e vigência (`cgov-saneamento-legistica` e `cgov-nt-03`).
4. **Correções sem decisão nova:** citação só de dispositivo que sustente a regra (legística); cinco subsídios na
   sugestão de encaminhamento e alcance do art. 3º da Portaria nº 129/2020 (triagem); ⚠️ no valor dos campos
   (acervo); quórum e Conselho de Governança (colegiados); situação "evidência pendente" e CSV fictício
   (integridade); Decreto nº 9.094/2017, art. 11, §§ 3º (I a XII) e 4º, e script v0.2.0 (Carta de Serviços);
   encaminhamento da contratação direta (cooperação); cuidados do OCR nos ordinais (transcrição).
5. **Pendente:** E11 (tabela de dispositivos e evals mais fortes da legística, depois da C3).

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

## 43. Encerramento da Fase 6 (08/11/2026)

1. **Reinstalação:** a primeira tentativa, em 07/11, não chegou à conta (34 divergências; os nomes antigos
   continuavam lá). Em 08/11, as 34 skills do *commit* `b863ef3` foram reinstaladas e conferidas na conta (nomes e
   descrições); os 8 nomes antigos do PGD foram excluídos (D47); as instruções v1.1 estão no projeto Operação.
2. **6.8b:** a tabela de caminhos antigos do `operacao/AGENTS.md` passa a "Locais antigos" (D48), e
   `docs/fluxos-de-trabalho.md` descreve os caminhos por papel e o gerador de índices publicado.
3. **Critério de encerramento cumprido:** `publicar_operacao.py --verificar` sem divergências antes e depois do
   *commit* `066068b` (skills 34/34, `operacao/` 14/14, `docs/` 33/33).
4. **Lição:** conferir a conta (lista de skills) logo depois de enviar o primeiro zip, antes do lote.
5. **Pendências que seguem:** E9, E10, E11 e o piloto 6.9(e) (Fase 11).

Detalhes: plano de implantação (`docs/plano-implantacao.md`), Fase 6.

## 44. Revisão e reorganização da documentação antes da Fase 7 (09/11/2026)

Pedido do Coordenador: transformar a documentação Markdown em "segundo cérebro" de apoio ao Claude Code, com
análise individual de erros e desatualizações, links entre os arquivos, índices e boas práticas de engenharia.

1. **Diagnóstico (D57):** 103 arquivos `.md`; só 107 links relativos (1 quebrado); nenhum `docs/` com frontmatter;
   `plano-implantacao.md` (249 KB), `decision-log.md` (109 KB) e `analista-processos-sei.md` (66 KB) grandes demais
   para leitura integral; 12 documentos com informação desatualizada (`overview.md`, `catalogo-skills.md`,
   `CLAUDE.md`, `multiplatform.md`, `architecture.md`, `fluxos-de-trabalho.md`, `CONTRIBUTING.md`, `README.md`,
   `pendencias.md`, plano, `archive/README.md` e relatórios históricos).
2. **Respostas do Coordenador (D57):** plano com índice e apêndices duplicados por link (um arquivo só);
   frontmatter leve em todo `docs/`; aceitar os ADR-001, ADR-009 e ADR-011 (proposta confirmada pelo Coordenador no mesmo dia e aplicada).
3. **Feito:** correções factuais; `docs/INDICE.md` (tarefa → arquivos); `docs/convencoes-documentacao.md`;
   `docs/governance/rastreabilidade.md`; índices gerados do plano, deste registro e do analista de processos SEI;
   frontmatter em `docs/`, exceto nas duas instruções coladas inteiras em campos com limite de caracteres;
   Apêndices B, E e F do plano trocados por links; `pendencias.md` separado em abertas e resolvidas (E9 corrigida de 13
   para 20 skills sem evals; novas E12–E14).
4. **Ferramentas:** `scripts/gerar_indices_docs.py` e `scripts/verificar_docs.py` (só biblioteca padrão, ADR-004).
5. **Cuidado para a Fase 7:** a etapa 7.1 move `skills/<família>/`; depois do `git mv`, rodar
   `py scripts\gerar_indices_docs.py` e `py scripts\verificar_docs.py` (pendência E14). O ADR-005 precisa ser decidido
   no início da Fase 7 (pendência E12).

Detalhes: [`rastreabilidade.md`](rastreabilidade.md) e plano de implantação (etapa 7.0).

## 45. Início da Fase 7: ADR-005 aceito (09/11/2026)

1. **Leitura:** a seção da Fase 7 foi lida pelo índice do plano (linhas 1184–1199), com o ADR-005, as pendências
   E12–E14 e o Apêndice C (manifesto). Estado de partida: `main` sincronizado com `origin/main` no *commit*
   `ebb6f1d` (7.0, D57); a pasta `plugins/` ainda não existe; 32 skills vão para o plugin (`cgov-nt` 7,
   `escritorio` 2, `normativo` 4, `pgd` 8 e `thematic` 11); as 2 `cgge-fgbio-*` ficam fora (D46).
2. **Decisão (D58):** o Coordenador aceitou o ADR-005 **como está** (plugin único `cgov-escritorio`, distribuído
   por zip; *marketplace* GitHub só depois de testado e com sincronização automática desligada). Opções
   descartadas: aceitar com esclarecimento adicional, dividir em dois plugins e manter "Proposto".
3. **Edição aplicada:** `Status: Aceito` e `Data: 09/11/2026` no ADR-005; linha do `adr/README.md`; §4 do plano;
   pendência E12 movida para "Resolvidas"; `rastreabilidade.md` atualizada.
4. **Segue:** etapa 7.1 (`git mv` das 32 skills para `plugins/cgov-escritorio/skills/`), só depois de a lista do
   que será movido ser mostrada e confirmada; depois, `py scripts\gerar_indices_docs.py` e
   `py scripts\verificar_docs.py` (pendência E14).

Detalhes: [`rastreabilidade.md`](rastreabilidade.md) e plano de implantação (Fase 7).

## 46. Etapa 7.1: skills movidas para o plugin (09/11/2026)

1. **Confirmação:** o Coordenador aprovou a lista dos 32 `git mv` e o manifesto com `version` `0.1.0` (opção
   recomendada; a `1.0.0` fica para a 7.6, depois de uma semana sem regressão).
2. **Feito:** 32 skills (`cgov-nt` 7, `escritorio` 2, `normativo` 4, `pgd` 8, `thematic` 11) movidas por `git mv`
   para `plugins/cgov-escritorio/skills/` (70 renomeações, estrutura plana); criados
   `plugins/cgov-escritorio/.claude-plugin/plugin.json` (sem a skill de painéis, da Fase 10) e
   `plugins/cgov-escritorio/README.md`. `skills/cgge-fgbio/` fica fora do plugin (D46).
3. **Ajustes:** referências a `skills/<família>` corrigidas em `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`,
   `README.md`, `.gitignore` e em `docs/` (`INDICE`, `architecture`, `overview`, `fluxos-de-trabalho`,
   `multiplatform`, `catalogo-skills`); histórico (decision-log, plano, relatório de evals) mantido. As cinco pastas de
   família ficaram vazias (o shell do Cowork não apaga).
4. **Achado:** `scripts/verificar_docs.py` ignorava `plugins/`, o que tirava as skills da checagem (109 → 67 `.md`);
   corrigido (110 `.md`, 469 links, 0 erros). Sanitização aprovada (0 erros).
5. **Risco até a 7.3:** `scripts/publicar_operacao.py` lê só `skills/`; não usar `--verificar` nem `--publicar`
   antes de adaptá-lo para gerar o zip do plugin (7.3). Pendência E14 resolvida.

Detalhes: plano de implantação (Fase 7, etapa 7.1).

## 47. Etapas 7.2 e 7.3: comandos, publicação do plugin e desligamento do plugin sincronizado (09/11/2026)

1. **Respostas do Coordenador (D59):** comandos como `commands/` e invólucros finos da skill `cgov-gestao-acervo`;
   exceção na obrigação 3 do `operacao/AGENTS.md` para o `/registrar-pendencia`; gravar 7.2 e 7.3 sem *commit*.
2. **7.2:** `plugins/cgov-escritorio/commands/` com `novo-processo`, `triar-entrada`, `atualizar-indices` e
   `registrar-pendencia` (frontmatter com `description`, `argument-hint` e `disable-model-invocation`; as regras ficam
   na skill). `operacao/AGENTS.md`: obrigação 3 com a exceção (b), que só permite acrescentar entradas ao fim de
   `90_escritorio-virtual/manutencao/PENDENCIAS.md`, e seção "Comandos do plugin". Chega à pasta CGOV na próxima
   publicação. A documentação oficial classifica `commands/` como formato antigo (skills o substituem; o nome
   `/<plugin>:<nome>` é o mesmo): mantido para não mexer na contagem de 34 skills, no catálogo e nos evals (E15).
3. **7.3:** `scripts/publicar_operacao.py` v0.3.0: lê o plugin e `skills/`; gera `dist/cgov-escritorio-<versão>.zip`
   (+ `.sha256` com o commit), sem `evals/`, com datas fixas (mesmo commit, mesmo hash); valida `plugin.json` (`name`,
   `version`) e cada skill (`name` igual à pasta, descrição ≤ 1.024 caracteres); para se a versão já existir; avisa
   dos zips além dos 3 mais recentes sem apagar; o bloqueio por alteração sem *commit* inclui `plugins/`; `--verificar`
   compara o plugin instalado (aviso até o primeiro envio). Teste contra o HEAD `70200ae`, numa pasta temporária:
   32 skills, 48 arquivos, hash repetível, segunda execução com a mesma versão parou.
4. **`.claude/settings.json`:** `enabledPlugins` com `"cgov-escritorio@synced": false` (formato `<nome>@synced`
   confirmado na documentação de carregamento de plugins). O teste local com `claude --plugin-dir` carrega como
   `@inline` e não é afetado.
5. **Pendências novas:** E15 (avaliar migrar `commands/` para skills) e E16 (confirmar, depois do primeiro envio, o
   local do plugin sincronizado usado pelo `--verificar`).

Detalhes: plano de implantação (Fase 7, etapas 7.2 e 7.3).

## 48. Etapas 7.4 e 7.5: validação, publicação e envio do plugin 0.1.0 (09/11/2026)

1. **7.4:** `claude plugin validate` retornou "Validation passed". Os avisos `LICENSE_MISSING` e `ICON_MISSING` são de
   submissão a diretório público e não se aplicam; a licença é decisão jurídica do Coordenador e ficou fora.
2. **7.5, publicação:** `py scripts\publicar_operacao.py --publicar --executar` no HEAD `c58a940`. Zip
   `dist\cgov-escritorio-0.1.0.zip`, SHA-256 `13a402394d88ed5a6c60c6c04e8a9e176e163b5d630924c156607f23f5ca5075`,
   178.045 bytes. Publicados na pasta CGOV, ambos conferidos por SHA-256: `operacao\AGENTS.md` (versão anterior em
   `99_arquivo\_a-excluir_2026-11-09\publicacao_c58a940\`) e a referência de `docs\` (39 arquivos). Nada foi excluído.
3. **7.5, envio e testes:** zip enviado com sucesso em Customize → Plugins → Add → Upload plugin; testes 1 a 6
   aprovados no projeto "Escritório CGOV — Operação".
4. **`--verificar` depois da publicação:** "sem divergências" (34/34 skills, 14/14 `operacao\`, 39/39 `docs\`). Seção
   1b com [AVISO]: o plugin não está sincronizado no Claude Code desta máquina (nenhum `plugin.json` com `name`
   `cgov-escritorio` em `~\.claude\plugins`; estrutura real: `synced\<bucket>\<plugin>\.claude-plugin\plugin.json`; há
   gerações duplicadas, como `design` e `design~g2`).
5. **Decisão (D60):** manter a E16 aberta e reescrita. A paridade fica provada pelo SHA-256 do zip (`.sha256` com o
   *commit*) e pela versão 0.1.0 em Customize. `verificar_plugin()` não muda até o plugin aparecer localmente; então,
   avaliar escolher o maior `~gN` em vez de `sorted(achados)[0]` (`publicar_operacao.py`, linha ~300).
6. **Pendência nova:** E17 (gerações antigas em `dist\skills\<commit>\` viram candidatas à quarentena depois da 7.6).

Detalhes: plano de implantação (Fase 7, etapas 7.4 e 7.5).

## 49. Etapa 7.6a: avulsas desativadas e ajuste do `--verificar` (09/11/2026)

1. **Desativação:** o Coordenador desativou as 32 skills avulsas em Customize → Skills. A `cgov-secretaria-colegiados`
   estava ativa quando a primeira verificação foi feita e foi desativada em seguida. As 2 `cgge-fgbio-*` seguem avulsas.
2. **Evidência (`--verificar`, script 0.3.1, HEAD `19f2dc2`):** 31 das 32 skills do plugin fora da cache local
   `~\.claude\skills\synced`; a `cgov-secretaria-colegiados` ainda aparecia como avulsa (aviso); as 2 `cgge-fgbio-*`
   iguais. Seção 1b: o plugin 0.1.0 apareceu sincronizado em `~\.claude\plugins\synced\<bucket>\cgov-escritorio`
   (estrutura plana, sem `~gN`), `version` igual à do HEAD, com 28 divergências em `SKILL.md` por SHA-256. Seção 2:
   14/14 iguais. Seção 3: 5 diferenças esperadas (arquivos de `docs\` alterados no *commit* `19f2dc2`). Total: 33.
3. **Decisão (D61):** `verificar_skills()` avisa, sem contar divergência, se uma skill do plugin ainda estiver como
   avulsa, e a flag `--sem-avulsas` (7.6b) a transforma em divergência; a 7.6a só é registrada com a saída real do
   `--verificar`; a seção 1b passa a comparar os `SKILL.md` por nome, descrição e corpo (a causa das 28 divergências
   não foi verificada; a hipótese é a conta regravar o cabeçalho) e a escolher a geração `~gN` mais recente.
   `publicar_operacao.py` v0.3.1, testado numa cache falsa e depois na máquina do Coordenador: seção 1b sem
   divergências; seção 1 com 1 aviso (`cgov-secretaria-colegiados` ainda na cache, já desativada); total 5
   divergências, todas da seção 3 (esperadas).
4. **Pendências:** E16 reescrita (local do plugin confirmado e 1b sem divergências com a v0.3.1; resta conferir a geração `~gN` no reenvio da `1.0.0`), E18 (confirmar
   a cache e a seção 1b na máquina do Coordenador; depois, a 7.6b) e E19 (a referência de `docs\` só chega à pasta
   CGOV com a publicação da `1.0.0`, porque `--publicar --executar` para quando já existe o zip da `version`).

Detalhes: plano de implantação (Fase 7, etapa 7.6a).

## 50. Etapa 7.6b: plugin 1.0.0, exclusão das avulsas e `cgge-fgbio-*` opcionais (18/11/2026)

1. **Versão 1.0.0:** *commit* `8b24d3e` (`version` `1.0.0`, `CHANGELOG.md`, README). Publicação com
   `py scripts\publicar_operacao.py --publicar --executar`: zip `dist\cgov-escritorio-1.0.0.zip`, SHA-256
   `70e00adc168cb16db42cc88c0e74236334ddf627018762d1a6ae7e864ec2d977`, 178.739 bytes, 53 arquivos; 40/40 gravados
   e conferidos; referência de `docs\` atualizada para `8b24d3e` (a anterior em
   `99_arquivo\_a-excluir_2026-11-18\publicacao_8b24d3e\`). O zip de teste `cgov-escritorio-v1.zip` foi movido pelo
   Coordenador para essa mesma quarentena (estava em `plugins\` e reprovava a sanitização).
2. **Envio:** Customize → Plugins mostra v1.0.0, com 32 skills, em uma só entrada; a cache local ganhou
   `cgov-escritorio~g2`, e o `--verificar` (seção 1b) deu "sem divergências" com a geração mais recente.
3. **Testes no projeto Operação:** `/triar-entrada`, `/novo-processo`, `/atualizar-indices` e a frase da NT aprovados
   (os dois comandos de gravação foram cancelados antes de gravar); `/registrar-pendencia` funciona, por informação do
   Coordenador. As skills e os comandos são idênticos aos da 0.1.0; mudaram só `version`, `CHANGELOG.md` e README.
4. **Exclusão das avulsas (Customize → Skills):** feita pelo Coordenador, exceto a "Pgd analisar indicador", mantida
   por dúvida de identidade (E20). Rede de segurança: `dist\skills\066068b\`, com os 34 pacotes, idênticos às skills
   do plugin.
5. **Decisão (D62):** as 2 `cgge-fgbio-*`, desativadas pelo Coordenador por falta de uso, seguem no repositório
   (`skills\cgge-fgbio\`, fora do plugin, D46) e o `--verificar` as trata como opcionais: `publicar_operacao.py`
   v0.3.2 (*commit* `68bb988`), `AVULSAS_OPCIONAIS`; ausentes viram [AVISO], instaladas e diferentes continuam
   divergência.
6. **`--verificar --sem-avulsas` (script 0.3.2):** "sem divergências" (seção 1 com 2 avisos e 0 skills do plugin como
   avulsas; seção 1b com `~g2`, 1.0.0).
7. **Pendências:** E16, E18 e E19 resolvidas; E17 ajustada (poupar `066068b`); E20 nova (identificar a "Pgd analisar
   indicador"); P7 com as quarentenas de 18/11.

Detalhes: plano de implantação (Fase 7, etapa 7.6b).

## 51. Modo de execução do Claude Code: autonomia com gate (18/11/2026)

1. **Decisão (D63):** o Coordenador autorizou o Claude Code, neste repositório, a rodar scripts, verificadores e
   testes automatizados, criar e editar arquivos do repositório, regenerar índices, rodar
   `publicar_operacao.py --verificar` e `--publicar` (simulação) e fazer *commit* e *push* em `main` sem pedir
   confirmação.
2. **Gate antes de cada *commit*:** `py scripts\gerar_indices_docs.py`; `py scripts\verificar_docs.py` com 0 erro;
   `py scripts\verificar_sanitizacao.py` com "APROVADO"; `git status` e `git diff --stat` conferidos. Se algum
   falhar, o Claude para, corrige ou reporta, e não faz o *commit*. *Push* só de *commit* que passou no gate,
   seguido da conferência `main...origin/main` sem diferença. *Commits* em português, no padrão convencional, um
   por etapa lógica.
3. **Continua com o Coordenador:** decisão de negócio ou regra importante (escopo de skills, conteúdo normativo,
   política de versões, publicação em marketplace, desligamento de plataformas); ação irreversível ou fora do
   repositório (`git push --force`, reescrita de histórico, exclusão ou movimentação fora da quarentena, mudanças
   na pasta CGOV além do `publicar_operacao.py --executar` com conferência SHA-256); `--publicar --executar`, com
   simulação e lista de arquivos antes do "confirmo"; ambiguidade que mude o resultado.
4. **Alcance:** só o Claude Code. O projeto Cowork "Escritório CGOV — Implantação" segue a regra 1 do Apêndice A
   do plano (confirmação antes de *commit* e *push*), e as instruções coladas nele não mudam.
5. **Permissões:** a pedido do Coordenador, saíram do `.claude/settings.json` as regras `ask` de `git commit` e
   `git push`; as regras `deny` (pasta CGOV, junções, `.env`) continuam.
6. **Onde ficou registrado:** seção "Modo de execução" no `AGENTS.md`; `CLAUDE.md`; `docs/fluxos-de-trabalho.md`
   v2.2 (§3.1, §5, passo 6, e §7); `.claude/settings.json`; plano v3.56 (cabeçalho, regra de manutenção, Seção 7, Seção 9, quadro e Apêndice G).

Detalhes: plano de implantação (Seção 9, D63).
## 52. Pendência E20: exclusão da avulsa "Pgd analisar indicador" (18/11/2026)

1. **Identidade:** o Coordenador comparou o texto da avulsa "Pgd analisar indicador" (Customize → Skills) com o da
   `pgd-analisar-indicador` do plugin: SHA-256 `29004b1f908c8068b2dea1b2fa8e30ab7407f18c4b636c2a9c1f2baf587bd288`
   nos dois textos e diff sem diferença. O hash foi calculado sobre o texto da interface e não se reproduz sobre o
   arquivo da fonte (`plugins/cgov-escritorio/skills/pgd-analisar-indicador/SKILL.md`, SHA-256 `897adf46…39bd`, com
   cabeçalho); a conferência é a do Coordenador.
2. **Exclusão:** feita pelo Coordenador em Customize → Skills. Rede de segurança: `dist\skills\066068b\`.
3. **Evidência (`publicar_operacao.py --verificar --sem-avulsas`, script 0.3.2, HEAD `e9942fe`):** seção 1 com os 2
   avisos das `cgge-fgbio-*` (opcionais, D62) e 0 skills do plugin como avulsas; seção 1b com o plugin 1.0.0
   (`cgov-escritorio~g2`) e sem divergências; seção 2 com 14/14 iguais; seção 3 com 7 diferenças esperadas (os
   `docs\` alterados pela D63 e por esta etapa depois da publicação `8b24d3e`; chegam à pasta CGOV no próximo
   `--publicar --executar`).
4. **Pendência:** E20 resolvida.

Detalhes: plano de implantação (Fase 7, etapa 7.6b, parágrafo E20).
## 53. Encerramento da Fase 7: etapa 7.7 dispensada (18/11/2026)

1. **Decisão (D64):** o Coordenador escolheu seguir para a Fase 8 e dispensar a 7.7 (*marketplace* GitHub do plugin).
   Motivos: para um só usuário, o envio do zip em Customize → Plugins basta; com o *push* autônomo da D63, a
   sincronização pelo GitHub poderia levar à conta um *commit* ainda não publicado; o acesso do GitHub App ao
   repositório privado deixa de ser necessário. O ADR-005 não muda (o *marketplace* era opcional). Reavaliar se o
   plugin passar a ter mais usuários (Fase 12).
2. **Testes automatizados do plugin 1.0.0 (HEAD `e627c52`):** `plugin.json` 1.0.0; 32 skills e 4 comandos; 32/32
   `SKILL.md` com `name` igual à pasta e `description` ≤ 1.024 caracteres; `dist\cgov-escritorio-1.0.0.zip` com
   SHA-256 igual ao `.sha256` (`70e00adc…d977`), 53 arquivos, 0 de `evals/` e 53/53 idênticos à fonte atual;
   `claude plugin validate` "Validation passed"; 14 skills com `evals.json` válidos (38 casos; não executados, sem
   *runner*; as 18 sem casos na E9); `--verificar --sem-avulsas` sem divergências nas seções 1, 1b e 2, com 7
   diferenças esperadas de `docs\` na seção 3 (publicação pendente).
3. **Testes de interface:** ficaram como lista de conferência do Coordenador (listagem `/cgov-escritorio:`,
   `/cgov-escritorio:triar-entrada`, acionamento único da `cgov-nt-01-triagem` e da `pgd-analisar-indicador`,
   Customize → Plugins e → Skills).
4. **Fase 7 concluída.** Próxima: Fase 8.

Detalhes: plano de implantação (Fase 7, encerramento; Seção 9, D64).
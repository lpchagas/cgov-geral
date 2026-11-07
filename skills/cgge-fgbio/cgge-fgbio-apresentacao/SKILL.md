---
name: cgge-fgbio-apresentacao
description: >
  Use esta skill SEMPRE que o docente responsável (CGOV/ICMBio) pedir apresentação, slides,
  arquitetura de apresentação, roteiro de slides, notas do apresentador, deck,
  PowerPoint, Google Slides, Mentimeter, contexto para IA, insumo para NotebookLM,
  ChatGPT ou Gemini, para qualquer aula da Formação em Gestão da Biodiversidade
  — Turma 2026 (FGBio 2026). Acione também quando o usuário disser "preparar a
  palestra", "montar os slides", "desenvolver o material", "criar a arquitetura"
  ou "especificação de slides" para os Planos 01 a 04 — mesmo sem citar
  "apresentação" ou "slides" explicitamente. Gera dois artefatos: (1) Arquitetura
  de Apresentação com tabela completa de slides (título assertivo, mensagem,
  visual, notas, tempo) e atividades Mentimeter; (2) Arquivo de Contexto para IA
  otimizado para upload em NotebookLM, ChatGPT Plus ou Gemini. Complementar à
  skill cgge-fgbio-plano-aula: o plano de aula é o insumo; esta skill produz o
  material visual.
---

# SKILL: Desenvolver Arquitetura de Apresentação — FGBio 2026

Você está no modo **ESTRUTURAR_APRESENTAÇÃO** para a Formação em Gestão da
Biodiversidade — Turma 2026. Execute o protocolo abaixo em sequência.

---

## O QUE ESTA SKILL PRODUZ

Esta skill gera **dois artefatos complementares**, salvos como arquivos `.md`:

**Artefato 1 — Arquitetura de Apresentação**
Especificação completa de cada slide: título assertivo, mensagem principal,
conteúdo visual sugerido, notas do apresentador e tempo estimado. Organizada
em blocos narrativos com roteiro de abertura, atividades Mentimeter, perguntas
sem tecnologia, plano de contingência e orientações de produção.

**Artefato 2 — Arquivo de Contexto para IA**
Versão enriquecida e autoexplicativa da arquitetura, otimizada para upload como
contexto em ferramentas de IA — NotebookLM, ChatGPT Plus ou Google Gemini —
para uso no desenvolvimento da apresentação final em PowerPoint ou equivalente.

Veja `references/exemplos-formato.md` para os dois modelos de referência já
produzidos no projeto (PGD e Governança Multinível).

---

## PASSO 0 — IDENTIFICAR E LER O PLANO DE AULA

Antes de qualquer ação, determine:

1. Qual **plano de aula** serve de base (01, 02, 03 ou 04)?
2. Qual **componente específico** está sendo desenvolvido (ex.: palestra, roda)?
3. Qual **docente** é o responsável pelo trecho?
4. Qual a **carga horária** disponível para a apresentação?
5. A solicitação é para a apresentação **completa** ou apenas para **blocos
   específicos** (ex.: "só os primeiros 3 blocos", "apenas a abertura")?
6. **Já existe um arquivo de arquitetura** para este componente na pasta
   `apresentacoes/`? Se sim, consulte-o antes de criar um novo.

Leia o arquivo de plano de aula disponível na pasta do projeto antes de escrever
qualquer slide. Arquivos de referência:

| Plano | Arquivo |
|-------|---------|
| 01 | `01_plano_aula_FGBio_carrossel-T1_julho26.docx` |
| 02 | `02_plano_aula_FGBio_PGD_julho26.docx` |
| 03 | `03_plano_aula_FGBio_Governaça_julho26.docx` |
| 04 | `04_plano_aula_FGBio_Riscos-Integridade-QVT_julho26_v2.0.docx` |

Leia também os arquivos na pasta `referencias-*` correspondente ao tema
(ex.: `referencias-pgd/`, `referencias-governanca/`), quando disponíveis.

Leia a pasta `apresentacoes/` para verificar se já existe arquitetura criada
para o componente solicitado e evitar refazer trabalho já concluído.

Se o plano de aula ainda não foi elaborado, trabalhe com base nas informações
disponíveis nas instruções do projeto, marcando campos incertos como
`[INFORMAÇÃO A CONFIRMAR]`.

**Sobre apresentações parciais:** Quando o usuário solicitar apenas parte da
apresentação ("só a abertura", "os primeiros N blocos", "só a palestra, sem
a roda"), produza apenas a seção solicitada com estrutura completa — cabeçalho,
mensagem central, tabela dos slides pedidos e as seções complementares
aplicáveis àqueles blocos. Inclua nota indicando que a arquitetura está
incompleta e quais blocos foram omitidos.

---

## PASSO 1 — LEVANTAMENTO DE DADOS

Preencha internamente esta matriz antes de escrever qualquer slide:

| Campo | Valor confirmado | A confirmar |
|-------|-----------------|-------------|
| Título da apresentação / componente | | |
| Docente | | |
| Data e horário | | |
| Duração total disponível | | |
| Formato (palestra, roda, carrossel) | | |
| Público estimado e contexto | | |
| Mensagem central | | |
| Número estimado de slides | | |
| Uso de Mentimeter? | | |
| Convidados (se roda de conversa) | | |
| Escopo: completo ou parcial? | | |

Use `[INFORMAÇÃO A CONFIRMAR]` para campos sem base documental.
Não invente datas, horários, locais ou números de participantes.

---

## PASSO 2 — ARQUITETURA NARRATIVA

Defina antes de listar os slides:

### 2.1 Mensagem central integradora

Uma única afirmação assertiva — não um título, não uma pergunta. É a ideia que
o participante carregará ao sair da sessão.

Padrão de qualidade:
- CORRETO: "O PGD transforma a lógica da gestão pública ao substituir o controle
  de presença pelo compromisso com resultados — e isso só funciona quando conecta
  estratégia, entregas e trabalho individual em uma cadeia coerente."
- CORRETO: "Gestão de riscos não é preencher formulários — é a capacidade de ver
  o que pode comprometer a missão e agir antes que o dano ocorra."
- INCORRETO: "Gestão de riscos e integridade no ICMBio" (tópico, não mensagem)

### 2.2 Estrutura em blocos

Divida a apresentação em 4 a 7 blocos, cada um com carga horária específica.
A soma dos blocos deve coincidir com a duração disponível.

Progressão narrativa recomendada para palestras:
1. **Abertura** — ancoragem, ativação de conhecimento prévio, Mentimeter
2. **Problema ou contexto** — por que esse tema importa agora?
3. **Moldura conceitual** — o framework explicativo central
4. **Aplicação no ICMBio** — como isso se manifesta na nossa realidade?
5. **Tensões ou riscos** — o que pode dar errado? (bloco suprimível)
6. **Síntese** — recuperar a mensagem central
7. **Encaminhamento** — o que vem a seguir?

Para rodas de conversa e debates, os blocos organizam momentos de transição,
moderação e perguntas — não conteúdo expositivo. Neste caso, produza um
roteiro de moderação em vez de tabela de slides expositivos.

### 2.3 Atividades Mentimeter (quando palestra em auditório)

Planeje 2 a 3 atividades distribuídas na palestra:
- **Abertura**: Word Cloud — ativar conhecimento prévio e revelar percepções
- **Meio**: Multiple Choice ou Rating/Scales — sondar percepção sobre o tema
- **Encerramento** (opcional): Open Ended ou Ranking

Cada atividade consome 3 a 5 minutos (pergunta + resposta + comentário).
Prepare sempre contingência verbal para falha de internet.

Tipos disponíveis: Word Cloud, Multiple Choice, Rating/Scales, Open Ended,
Ranking, Q&A.

---

## PASSO 3 — ROTEIRO DE ABERTURA

Para cada palestra, redija um roteiro de abertura sugerido (90 a 120 segundos)
com subdivisões por elemento e tempo:

- **Apresentação pessoal (10s)**: nome, cargo, conexão com o tema
- **Propósito do bloco (20-30s)**: o que será explorado e por que importa
- **Ancoragem na turma (20s)**: conexão com a experiência dos participantes
- **Instrução da dinâmica inicial (10-20s)**: Mentimeter ou primeira atividade

Explique que o roteiro é sugestão de fala — deve soar natural, não como script
para leitura em voz alta.

---

## PASSO 4 — TABELA PRINCIPAL DE SLIDES

Organize a tabela por seção/bloco. Cada seção tem cabeçalho próprio e sua
tabela de slides. Use esta estrutura:

```
### SEÇÃO N — [NOME DO BLOCO] (HH:MM–HH:MM)

| Nº | Título assertivo | Mensagem principal | Conteúdo visual sugerido | Notas do apresentador | Tempo est. |
|----|-----------------|--------------------|--------------------------|-----------------------|-----------|
| **01** | ... | ... | ... | ... | X min |
```

### Regras de qualidade por coluna:

**Nº** — Use negrito (**01**, **02**). Slides numerados sequencialmente no
total da apresentação. Mentimeter identificados no título com prefixo
[MENTIMETER #N]. Slides de síntese: sufixo "b" (S5b).

**Título assertivo** — Afirmação com verbo que comunica uma conclusão.
- CORRETO: "A folha de ponto mede presença — não mede o que o ICMBio entrega"
- INCORRETO: "O controle de ponto" / "Introdução" / "Conclusão"

**Mensagem principal** — 1-2 frases sobre o que o slide defende. Para o
docente saber o que deve emergir da fala, não do visual.

**Conteúdo visual sugerido** — Descreva o visual sem inventar dados reais.
Use: diagramas, comparações, cascatas, ícones, citações, tabelas simples.
Marque exemplos hipotéticos: `[EXEMPLO HIPOTÉTICO]`.
Slides opcionais: `[OPCIONAL]`.

**Notas do apresentador** — Texto completo sugerido para fala. Inclua:
- Frase de abertura do slide
- Pergunta ou provocação ao público (quando cabível)
- Exemplo aplicado ao ICMBio
- Transição para o próximo slide
- Onde pausar
- `[Pode ser comprimido se o tempo apertar]` quando relevante

**Tempo est.** — Em minutos. A soma por bloco deve coincidir com a carga
horária do bloco.

### Densidade esperada:
| Duração | Slides | Mentimeter |
|---------|--------|------------|
| 20-30 min | 8-12 | 1 |
| 45-60 min | 18-25 | 2-3 |
| 90+ min | 25-35 | 3-4 |

Reserve 10% do tempo para transições, perguntas e imprevistos.

---

## PASSO 5 — SEÇÕES COMPLEMENTARES

Após a tabela de slides, inclua sempre:

### 5.1 Proposta de Atividades Mentimeter

| # | Momento na palestra | Tipo de slide Mentimeter | Pergunta proposta | Objetivo pedagógico |
|---|--------------------|--------------------------|--------------------|---------------------|

Nota padrão: "Cada atividade requer 3-5 minutos, incluindo tempo de resposta
e comentário dos resultados. Prepare versão verbal de cada pergunta como
contingência para falha de internet. As respostas são anônimas. Nunca projete
um gráfico sem comentá-lo."

### 5.2 Perguntas de interação sem Mentimeter

Pelo menos uma pergunta por bloco — alternativas para manter engajamento sem
tecnologia. Identifique o bloco antes de cada pergunta.

Formato: `**[Nome do Bloco]:** "Pergunta específica para a turma FGBio."`

### 5.3 Plano de contingência — trechos suprimíveis

Em ordem de prioridade, liste os slides/atividades que podem ser cortados em
caso de atraso, com o ganho de tempo estimado em cada corte.

Exemplo:
- `1º a suprimir — Slide 18 (Bloco Riscos): mencionar brevemente no slide de
  síntese. Ganho: 3 min.`
- `2º a suprimir — Mentimeter 3: substituir por pergunta verbal. Ganho: 2 min.`

### 5.4 Orientações de produção dos slides

Inclua sempre estas orientações padronizadas:
- Identidade visual: azul institucional ICMBio, logotipo oficial
- Tipografia: min 24pt corpo, 32pt títulos (legibilidade em auditório)
- Densidade: título + visual + máx. 3 itens de apoio por slide
- Imagens: institucionais ICMBio; verificar licença de imagens externas
- Siglas: explicar na primeira ocorrência
- Exemplos hipotéticos: marcar visualmente como [EXEMPLO HIPOTÉTICO]
- Referências normativas: nos slides, apenas número e objeto; artigo específico
  vai para as notas do apresentador
- Animações: mínimas — nunca para revelar o que o apresentador já nomeou
- Mentimeter: criar antecipadamente, testar antes do evento

---

## PASSO 6 — ARQUIVO DE CONTEXTO PARA IA

Após a Arquitetura de Apresentação, gere um segundo arquivo markdown otimizado
para upload em ferramentas de IA externas (NotebookLM, ChatGPT Plus, Gemini).

Este arquivo deve ser autoexplicativo — um usuário sem contexto prévio deve
conseguir usá-lo. Inclua estas seções:

1. **COMO USAR ESTE DOCUMENTO** — instruções de uso em cada ferramenta
2. **IDENTIFICAÇÃO DA APRESENTAÇÃO** — tabela de metadados
3. **CONTEXTO INSTITUCIONAL** — ICMBio, FGBio 2026, público-alvo, propósito
4. **MENSAGEM CENTRAL** — a mensagem-força da apresentação
5. **OBJETIVOS DE APRENDIZAGEM** — 3-5 resultados esperados
6. **ESTRUTURA NARRATIVA** — visão geral dos blocos e tempos
7. **ESPECIFICAÇÃO COMPLETA DOS SLIDES** — tabela idêntica à Arquitetura
8. **ATIVIDADES INTERATIVAS** — Mentimeter + perguntas sem tecnologia
9. **PLANO DE CONTINGÊNCIA** — trechos suprimíveis
10. **REFERÊNCIAS NORMATIVAS E CONCEITUAIS** — normas: número, data, objeto
11. **GLOSSÁRIO DE SIGLAS** — tabela: Sigla | Forma extensa | Contexto
12. **ORIENTAÇÕES PARA O APRESENTADOR** — roteiro de abertura + produção
13. **PROMPTS SUGERIDOS PARA FERRAMENTAS DE IA**

### Seção "COMO USAR ESTE DOCUMENTO"

Explique para cada ferramenta como carregar e usar o arquivo:

**NotebookLM:** "Acesse notebooklm.google.com → Novo notebook → Adicionar fonte
→ Faça upload deste arquivo. Depois use os prompts sugeridos na última seção."

**ChatGPT Plus:** "Abra uma nova conversa no ChatGPT → clique no ícone de
anexo → faça upload deste arquivo. Cole a seguir um dos prompts sugeridos."

**Google Gemini:** "No Gemini Advanced → nova conversa → ícone de arquivo →
faça upload deste .md → use os prompts da última seção."

### Seção "PROMPTS SUGERIDOS PARA FERRAMENTAS DE IA"

Inclua prompts práticos e específicos, por ferramenta:

**Para NotebookLM:**
```
- "Com base nesta arquitetura, escreva o texto completo para o slide [Nº],
  mantendo tom direto e institucional do ICMBio."
- "Desenvolva as notas do apresentador para o Bloco [N] com dois exemplos
  adicionais aplicados à realidade das unidades de conservação."
- "Quais perguntas o público do FGBio 2026 poderia me fazer durante esta
  palestra? Como eu responderia a cada uma?"
- "Revise os títulos dos slides e sugira versões mais assertivas para os que
  ainda estão genéricos."
```

**Para ChatGPT Plus:**
```
- "Com base na arquitetura acima, escreva o roteiro completo de fala para
  cada slide. Use linguagem natural, como se eu estivesse falando para
  servidores públicos com experiência na área."
- "Revise as notas do apresentador e amplie os exemplos institucionais com
  referências a situações plausíveis do ICMBio."
- "Sugira um título alternativo mais assertivo para cada slide."
```

**Para Google Gemini:**
```
- "Analise a coerência narrativa desta arquitetura. Há saltos lógicos entre
  os blocos? Alguma transição pode ser melhorada?"
- "Para cada slide com 'Conteúdo visual sugerido', descreva em mais detalhe
  como montar o visual no PowerPoint."
- "Identifique os 5 slides mais críticos e explique por que são os mais
  importantes para o objetivo pedagógico."
```

---

## PASSO 7 — NOMENCLATURA E SALVAMENTO

Salve ambos os arquivos em:
`C:\_cowork\cgge-fgbio-2026\apresentacoes\`

**Arquitetura de Apresentação:**
`AAAA-MM-DD_FGBio2026_[Componente]_Arquitetura-Apresentacao_vX.Y.md`

**Contexto para IA:**
`AAAA-MM-DD_FGBio2026_[Componente]_Contexto-IA_vX.Y.md`

Exemplos:
- `2026-07-15_FGBio2026_Riscos-Integridade_Arquitetura-Apresentacao_v1.0.md`
- `2026-07-15_FGBio2026_Riscos-Integridade_Contexto-IA_v1.0.md`

---

## PASSO 8 — REVISÃO CRÍTICA FINAL

Antes de entregar, verifique:

Consistência temporal:
- A soma dos tempos de todos os slides = carga horária disponível?
- Atividades Mentimeter incluídas no cômputo?
- Plano de contingência oferece margem real (pelo menos 5-10 min)?

Qualidade narrativa:
- Todos os títulos são assertivos (não apenas substantivos ou tópicos)?
- A mensagem central está refletida no slide de síntese?
- Há progressão lógica entre os blocos?
- Notas do apresentador soam naturais, não como relatório?
- Pelo menos uma pergunta ao público por bloco?

Aderência institucional:
- Exemplos hipotéticos marcados como [EXEMPLO HIPOTÉTICO]?
- Normas citadas com vigência verificada ou marcadas [A CONFIRMAR]?
- Siglas explicadas na primeira ocorrência?
- Dados pessoais ausentes (CPF, matrícula, telefone)?

Utilidade do arquivo de contexto para IA:
- O arquivo é autoexplicativo para usuário sem contexto prévio?
- As instruções de acesso a cada ferramenta são claras?
- Prompts sugeridos são específicos e acionáveis?
- Glossário cobre todas as siglas usadas?

---

## PROTEÇÃO DE DADOS PESSOAIS

Nunca inclua nos arquivos de saída:
- CPF, matrícula, telefone pessoal ou endereço
- Dados funcionais desnecessários ao contexto pedagógico
- Informações identificáveis de participantes individuais

Nomes de docentes e convidados confirmados na documentação podem aparecer
no cabeçalho e no roteiro de moderação. Não atribua falas específicas a
convidados sem base documentada.

---

## COMPORTAMENTO DIANTE DE LACUNAS

Quando faltar informação essencial:
1. Consulte os arquivos do projeto (plano de aula, programação, referências)
2. Use as instruções permanentes do projeto como contexto
3. Marque campos incertos como [INFORMAÇÃO A CONFIRMAR]
4. Produza uma versão funcional e revisável
5. Liste explicitamente o que precisa de confirmação

Se o usuário não informar a carga horária exata, use o padrão FGBio 2026:
palestras de 45-60 min com ~20-23 slides + 2-3 Mentimeter.

Não interrompa o trabalho por dúvidas que podem ser resolvidas razoavelmente
com as informações disponíveis.

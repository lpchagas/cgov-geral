---
name: cgov-nt-03-introducao
description: >
  Terceira etapa da suíte canônica cgov-nt: redige o Capítulo 1 — Introdução —
  de QUALQUER Nota Técnica da CGOV/ICMBio (não apenas PGD ou PSPEADBio), com
  cabeçalho institucional, destinatário, interessado, referências normativas,
  contextualização, metodologia e escopo do documento. Use ao invocar
  /cgov-nt-03, "redigir a introdução da NT", "capítulo 1", "abrir a nota
  técnica", "cabeçalho da NT", ou qualquer pedido de redação da seção inicial
  de uma Nota Técnica da CGOV. Requer que `cgov-nt-01` (triagem) já tenha sido
  executada e que exista `NT_ESTADO.md` na
  pasta de trabalho do processo; se não existir, redirecione para
  cgov-nt-01 primeiro.
---

# cgov-nt-03 — Capítulo 1: Introdução

## PRÉ-EXECUÇÃO OBRIGATÓRIA

1. **Localização do `NT_ESTADO.md`:** o arquivo vive na **pasta de trabalho do
   processo**, nunca na raiz do projeto; o caminho concreto está no `AGENTS.md`
   do repositório em uso. Procure-o nesta ordem:
   a. na pasta do processo conectada a esta conversa;
   b. na pasta de processos, identificando o processo pelo número SEI citado na
      conversa (compare pelo número, não pelo formato do nome da pasta);
   c. num local antigo listado na tabela de caminhos antigos do `AGENTS.md`, ou
      numa pasta com `MOVIDO_PARA.txt` — nesse caso, avise o usuário de que o
      arquivo está fora da convenção.
   Se houver mais de um candidato e não for possível identificar o processo
   pelo contexto, pergunte ao usuário antes de prosseguir.
2. Leia `NT_ESTADO.md` (metadados, enquadramento regimental, normas de
   referência, e — se já executada — a síntese de `cgov-nt-02`).
3. Se `NT_ESTADO.md` não existir, interrompa e redirecione para `cgov-nt-01`.
4. Aplique o **Padrão de Redação CGOV** (comum a todas as skills 03-07 desta
   suíte — ver seção abaixo) antes de gerar qualquer texto.

## PADRÃO DE REDAÇÃO CGOV (aplica-se a cgov-nt-03 a cgov-nt-07)

- **Prosa da própria NT:** verbos no **presente do indicativo** (ex.: "consolida",
  "conclui-se que", "tem por objetivo") — confirmado pela leitura da NT real
  nº 20/2026/CGOV. **Não use futuro simples na prosa da Nota Técnica.**
- **Redação de dispositivo de ato normativo** (quando a NT propuser ou citar
  texto de artigo/inciso de portaria/IN que ainda entrará em vigor): aí sim,
  **futuro do presente do indicativo**, por convenção da CGOV. O Decreto nº
  12.002/2024 (art. 11, I, "e") admite o presente ou o futuro do presente e exige
  **uniformidade**: a proposta parte do texto limpo da legística, para que não haja
  duas redações do mesmo artigo. Essa regra é do texto normativo em si, não da
  prosa analítica da NT. Não confunda os dois registros.
  Exceções (D56): ficam no presente as fórmulas consagradas de objeto ("Esta
  Portaria institui…"), competência ("Compete à…"), revogação ("Fica revogada…")
  e vigência ("Esta Portaria entra em vigor…").
- Dispositivos novos recebem numeração provisória com letra (ex.: art. 6º-A);
  prazos a calibrar pela unidade proponente ficam como "[X]"; um termo definido
  é o mesmo em todas as redações.
- Remissões normativas sempre com número e data completos na primeira menção
  (ex.: "Decreto nº 12.002, de 22 de abril de 2024"); menções subsequentes podem
  ser abreviadas ("Decreto nº 12.002/2024").
- Cada capítulo é um cabeçalho `### Capítulo N — [Nome]` dentro da Seção 4
  (FUNDAMENTAÇÃO/ANÁLISE TÉCNICA/PARECER), **exceto a conclusão**, que é a Seção
  `## 5. CONCLUSÃO E PROPOSIÇÃO`, com subitens `### 5.1`, `### 5.2`… (ver
  `cgov-nt-07`); as subseções usam numeração decimal
  **reiniciada por capítulo** (`#### N.1`, `#### N.2`...), nunca subordinada a
  "4.N.M". Este padrão foi validado por piloto contra NT real protocolada da
  CGOV — não use a variante "4.1/4.1.1".
- Prosa fluida nos parágrafos narrativos; tabelas apenas para dados comparativos
  ou consolidados — não liste em bullet points o que pode ser dito em prosa.
- **Nunca invente número de Lei, Decreto, Portaria, artigo ou inciso.** Se não
  houver certeza, cite a norma de forma geral e sinalize com ⚠️ a necessidade de
  confirmação pelo servidor responsável.
- Entregar o capítulo em Markdown, diretamente no chat, e **ao final alimentar o `.docx` de revisão
  da NT** (seção PÓS-EXECUÇÃO de cada skill 03 a 07). Não gere `.docx` avulso por capítulo: há um
  único `.docx` por NT, versionado pela fase (ver "Versões do .docx da NT" abaixo).
- **Códigos (prefixos que não colidem):** alertas de fluxo `F1-01`, `F2-01`… (um
  prefixo por fluxo); conflitos de competência `C-01`; lacunas sistêmicas `LS-01`;
  legística `E-01` (estrutura) e `L-01` (redação); riscos `RSC-01`; pontos
  jurídicos `PJ-01`. Achados e recomendações são citados por número (Achado nº,
  Rec. nº).
- **Rastreabilidade:** cada recomendação permite o caminho alerta/conflito →
  achado → risco → recomendação.

### Versões do .docx da NT (aplica-se a cgov-nt-03 a cgov-nt-07)

O número principal da versão é a **fase** da NT; o sufixo diz a etapa. Arquivo:
`NT_<apelido>_v<versão>-<etapa>.docx`, na pasta de trabalho do processo, ao lado do `.md` de mesmo nome.

| Fase | Skill | Versões e sufixos |
|---|---|---|
| 1 | `cgov-nt-03` | `v1-introducao` (abertura, seções 1 a 3 e Capítulo 1) |
| 2 | `cgov-nt-04` | `v2.1-<subsídio>`, `v2.2-<subsídio>`… (ex.: `v2.1-fluxo`, `v2.2-competencias`) e `v2.N-achados` (Cap. 3); de uma vez só: `v2-diagnostico` |
| 3 | `cgov-nt-05` | `v3-propostas` (Capítulo 4) |
| 4 | `cgov-nt-06` | `v4-quesitos-pfe` (subitem do Capítulo 4) |
| 5 | `cgov-nt-07` | `v5-conclusao` (Seção 5 e assinaturas) |
| — | revisão | `vN.M-revisao` (edições do revisor) e `vN.M-<etapa>` (capítulo refeito) |

Etapa dispensada na triagem não gera versão: a lacuna na numeração (ex.: sem `v4`) mostra que a NT
não tem quesitos da PFE. Versões anteriores nunca são apagadas nem sobrescritas; as superadas vão
para o arquivo pela `cgov-gestao-acervo` (ARQUIVAR) quando a NT for assinada.

## FORMATO DE SAÍDA

> **Padrão de numeração (validado por piloto contra NT real nº 20/2026/CGOV):**
> cada capítulo é um cabeçalho `### Capítulo N — [Nome]` autônomo, e suas
> subseções usam numeração **reiniciada por capítulo** (`#### N.1`, `#### N.2`),
> não subordinada a "4.N.M". Este é o padrão efetivamente usado nas Notas
> Técnicas protocoladas da CGOV (confirmado em NT nº 20/2026/CGOV, Capítulos 1
> e 5), e substitui o padrão "4.1/4.1.1" que constava de versões anteriores
> desta skill.

```
**Nota Técnica nº [N]/[ANO]/CGOV/CGGE/GABIN/ICMBio**
Brasília-DF, [data]

**Assunto:** [assunto — extraído do NT_ESTADO.md]
**Processo SEI nº** [número — de NT_ESTADO.md]

---

## 1. DESTINATÁRIO
[unidade(s) — de NT_ESTADO.md]

## 2. INTERESSADO
[interessado(s) — de NT_ESTADO.md]

## 3. REFERÊNCIAS
- [normas identificadas na triagem, em ordem hierárquica: Lei > Decreto > Portaria > IN/Guia]

## 4. FUNDAMENTAÇÃO/ANÁLISE TÉCNICA/PARECER

### Capítulo 1 — Introdução

#### 1.1. Contextualização e objetivo
[2-3 parágrafos: natureza do objeto analisado, relevância institucional, e
fundamento da competência da CGOV para se manifestar, citando o inciso do
Art. 37 identificado em NT_ESTADO.md]

#### 1.2. Histórico e metodologia
[1-2 parágrafos: como surgiu a demanda, período/processo de coleta de dados
ou de análise normativa, universo considerado — apenas se aplicável ao caso;
omita o que não existir no processo concreto. Em análise de ato normativo,
descreva os subsídios **já realizados** (fluxos, competências, cotejo, legística,
riscos e AIR), com a base de competência de cada um e as dispensas registradas no
`NT_ESTADO.md`; não descreva etapa "em execução"]

#### 1.3. Escopo do documento
[texto: estrutura das seções seguintes, ajustada ao roteiro definido em
NT_ESTADO.md — cite apenas os capítulos que de fato serão produzidos]
```

## REGRA ESPECIAL — DADOS FALTANTES

Se algum campo essencial (destinatário, referências, número da NT) não constar
de `NT_ESTADO.md`, não o preencha com um placeholder genérico silenciosamente:
liste as pendências ao final da resposta e pergunte objetivamente ao usuário.

## PÓS-EXECUÇÃO — .docx DE REVISÃO (v1-introducao)

A CGOV revisa a NT no Word. Por isso esta etapa termina com uma **nova versão do `.docx` da NT**,
que acumula os capítulos já redigidos e preserva as edições feitas pelo revisor na versão anterior.
O Markdown continua sendo a entrega no chat e a fonte do capítulo. O gerador é o
`montar_nt_docx.py` das **Ferramentas do Escritório** (caminho no `AGENTS.md`); ele aplica o padrão
gráfico das NTs da CGOV e nunca sobrescreve arquivo.

Como é a primeira versão, o gerador cria o documento do zero: título, data, caixa de Assunto e
Processo, Sumário, Listas de Quadros e de Figuras (atualizadas pelo Word ao abrir), cabeçalho e
rodapé. Por isso o `.md` começa pela abertura do FORMATO DE SAÍDA, sem notas de trabalho antes.

1. **Antes de numerar quadros e figuras**, rode
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" --listar --pasta "<pasta de trabalho>"`.
   A lista mostra as versões existentes e a última linha dá o próximo Quadro nº e a próxima Figura nº:
   numere o capítulo a partir deles.
2. **Grave o capítulo** na pasta de trabalho como `NT_<apelido>_v1-introducao.md` (`<apelido>` é o final do nome da
   pasta do processo, `SEI_…_<apelido>`): o mesmo texto entregue no chat, com legenda
   `**Quadro N — título**` antes de cada tabela e `Fonte: …` depois; pendências ficam fora do arquivo
   (vão para a resposta e para o `NT_ESTADO.md`).
3. **Simule e gere:**
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" "<pasta de trabalho>/NT_<apelido>_v1-introducao.md" --versao 1 --etapa introducao --simular`.
   Se o relatório (JSON) não trouxer erro, rode o mesmo comando sem `--simular`.
4. **Relate ao usuário**, em até cinco linhas: arquivo gerado, versão usada como base, avisos do
   relatório (numeração de quadros ou figuras, figura não inserida, tabela sem legenda, trecho
   excluído) e quantos ⚠ restam no texto.
5. **Registre** no `NT_ESTADO.md`, seção "Versões do .docx" (crie-a se não existir):
   `v1-introducao — NT_<apelido>_v1-introducao.docx — [data] — base: [versão anterior ou "novo"] — [n] aviso(s)`.

**Casos especiais**
- **Capítulo refeito** (correção pedida depois de gerado): a versão nova é a próxima subversão da
  versão **mais recente**, com o sufixo da etapa refeita (ex.: a última é `v3-propostas` e o usuário pede
  para refazer as competências → `v3.1-competencias`), com `--substituir`. Rode primeiro com `--simular`, mostre ao usuário os
  avisos de títulos que sairiam e as edições do revisor que se perdem nesse trecho, e só gere após a
  confirmação dele. Para trocar um único subitem, o `.md` começa pelo título do subitem (`#### N.M.`).
- **Revisão humana**: o gerador parte da versão de **maior número**. Se o revisor salvou as edições
  com outro nome, peça a ele que salve como a próxima subversão com sufixo `-revisao`
  (ex.: a última é `v3-propostas` → `NT_<apelido>_v3.1-revisao.docx`) antes de gerar; não renomeie arquivos sem confirmação.
- **Erros do gerador**: "já existe" ou "não é posterior" → use a próxima subversão; "Capítulo N
  ainda não está no documento base" → gere antes a etapa que falta; falta de `python-docx` →
  `pip install python-docx`. Se o gerador não estiver nas Ferramentas do Escritório, entregue só o
  Markdown, avise o usuário e registre a falta em `PENDENCIAS.md`.
- **Figuras**: diagrama Mermaid só vira imagem se o comando `mmdc` existir; sem ele, o `.docx`
  recebe um marcador ⚠ no lugar. Se já houver PNG do diagrama (ex.: produto da
  `cgov-modelar-fluxo`), referencie-o no `.md` com `![Figura N — título](arquivo.png)`.
- **Quadros largos** (7 colunas ou mais, ou 6 com texto longo) vão sozinhos para página paisagem;
  `<!-- paisagem -->` ou `<!-- retrato -->` na linha anterior à legenda força a orientação.

## REGISTRO NO NT_ESTADO.md

Acrescente à seção "Capítulos já redigidos" do `NT_ESTADO.md` (na subpasta
localizada na Pré-execução) uma linha: `Cap. 1 — Introdução: concluído em
[data].` e marque o item correspondente do roteiro como concluído.

## ENCADEAMENTO

```
/cgov-nt-01 → [/cgov-nt-02, se aplicável] → /cgov-nt-03 (esta skill) → /cgov-nt-04
```

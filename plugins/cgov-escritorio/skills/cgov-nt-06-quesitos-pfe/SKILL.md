---
name: cgov-nt-06-quesitos-pfe
description: >
  Sexta etapa (condicional) da suíte canônica cgov-nt: redige a seção de
  Análise para a PFE-ICMBio de QUALQUER Nota Técnica que subsidie a edição,
  alteração ou revisão de ato administrativo do ICMBio — não apenas PGD ou
  PSPEADBio — respondendo, de forma fiel e completa, aos 8 quesitos do Anexo II
  da Portaria ICMBio nº 271/2013. Use ao invocar /cgov-nt-06, "análise para a
  PFE", "quesitos da Portaria 271", "subsidiar a PFE", "análise jurídica
  preliminar", "Anexo II". A necessidade desta etapa é definida em
  `NT_ESTADO.md` (na pasta de trabalho do processo) pela triagem
  (`cgov-nt-01`, Passo 3.1) com base no destino do produto (a NT seguirá para
  a PFE?), não pelo Tipo de dado (A/B/C/D). Para NTs que não subsidiam ato
  administrativo, esta skill deve ser dispensada. Também apoia a consulta jurídica
  facultativa à PFE e a NT de subsídio que a acompanha (MODO 2: "consulta à PFE",
  "consulta facultativa", "formulário de consulta jurídica").
---

# cgov-nt-06 — Análise para a PFE-ICMBio (Anexo II da Portaria nº 271/2013)

> **Nota de versão:** esta skill foi reescrita a partir da leitura do texto
> integral da Portaria ICMBio nº 271, de 27 de dezembro de 2013 (Anexo II),
> fornecido pelo usuário. A tabela de "8 quesitos" que constava de versões
> anteriores desta skill — herdada, sem verificação, de `cgov-pgd-sk7` e
> `cgov-pspeadbio-sk4` — **estava incompleta e parcialmente incorreta**: faltavam
> por completo os quesitos 2, 3, 5 e 6 do Anexo II, e a maior parte dos
> subitens de detalhamento. A tabela abaixo é a transcrição fiel do Anexo II.

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
2. Leia `NT_ESTADO.md` — confirme que a triagem (`cgov-nt-01`, Passo 3.1) marcou
   os quesitos PFE como necessários. Essa necessidade depende do destino final
   do produto (a NT subsidiará edição/alteração/revisão de ato administrativo?),
   não do Tipo de dado (A/B/C/D). Um caso Tipo B (ex.: consulta interna cujos
   dados embasam a revisão de uma Instrução Normativa) pode exigir esta skill
   tanto quanto um caso Tipo A. Se `NT_ESTADO.md` não deixar isso claro,
   pergunte ao usuário antes de prosseguir.
3. **Pré-requisito de conteúdo:** os capítulos de diagnóstico e propostas
   (`cgov-nt-04` e, se aplicável, `cgov-nt-05`) devem estar concluídos — os
   achados e recomendações alimentam diretamente as respostas aos quesitos 1,
   2, 7 e 8 abaixo. Se o usuário pedir a redação antes disso, entregue um
   **rascunho condicionado** (D55): responda já os quesitos que dependem só do
   ato e do acervo (3, 4, 5 e 6, no que couber) e, nos quesitos 1, 2, 7 e 8,
   escreva `[A PREENCHER — depende do Cap. N]` com ⚠️ no lugar da resposta,
   sem presumir achados. Rotule o produto como rascunho; a redação final só sai
   com os capítulos concluídos.
4. Aplique o Padrão de Redação CGOV (`cgov-nt-03`): prosa no presente do
   indicativo, sem invenção de norma ou artigo.

## OS 8 QUESITOS DO ANEXO II (Portaria ICMBio nº 271/2013)

> A Portaria numera os quesitos de 1 a 8, mas o texto oficial publicado exibe
> os marcadores dos quesitos 4 a 8 como "10, 11, 12, 13, 14" — inconsistência
> de numeração do próprio documento original, identificável porque os
> subitens de detalhamento de cada quesito (ex.: "7.1, 7.2, 7.3" sob o quesito
> rotulado "13") retomam a numeração 4 a 8. Esta skill usa a numeração real
   dos subitens (1 a 8) como fonte da verdade, e não os marcadores "10-14" —
> **não replique o "10, 11, 12, 13, 14" em documentos oficiais**.

**Quesito 1 — Deve ser tomada alguma providência?**
| Subitem | Pergunta |
|---|---|
| 1.1 | O Instituto e a autoridade interessada dispõem de competência legal para a iniciativa? Há competência concorrente? A proposta está formulada adequadamente? |
| 1.2 | Qual o objetivo pretendido (orientar, controlar, aperfeiçoar, extinguir)? |
| 1.3 | Quais as razões que determinaram a iniciativa? |
| 1.4 | Que falhas ou distorções foram identificadas? |
| 1.5 | Que repercussões tem o problema? |
| 1.6 | Qual o número de atingidos pelo problema e o número de casos a resolver? |
| 1.7 | O que poderá acontecer se nada for feito (o problema se agrava, permanece estável, é superado)? |
| 1.8 | A proposta pode afetar situações consolidadas? Há ameaça à segurança jurídica? |

**Quesito 2 — Quais as alternativas disponíveis?**
| Subitem | Pergunta |
|---|---|
| 2.1 | Qual o resultado da análise do problema? Quais as causas e que ações podem eliminar ou diminuir seus efeitos? |
| 2.2 | Quais instrumentos de ação são adequados aos objetivos pretendidos, considerando: (a) desgaste e encargos para cidadãos/economia; (b) eficácia; (c) custos para o orçamento da autarquia; (d) efeitos sobre o ordenamento jurídico e metas estabelecidas; (e) efeitos colaterais; (f) aceitação pelos interessados e responsáveis pela execução; (g) possibilidade de impugnação judicial? |

**Quesito 3 — O ato corresponde às expectativas dos cidadãos/servidores e é inteligível para todos?**
| Subitem | Pergunta |
|---|---|
| 3.1 | O ato proposto será entendido e aceito pelos destinatários? |
| 3.2 | As limitações e restrições impostas são indispensáveis (proibições, comparecimento obrigatório, exigência de requerimento, dever de prestar informações, multas/penas, outras sanções)? |
| 3.3 | Podem as medidas restritivas ser substituídas por outras? |
| 3.4 | Os requisitos exigidos podem ser reduzidos a um mínimo aceitável? |
| 3.5 | Os destinatários da norma entendem o vocabulário, a organização, a extensão das frases e a lógica do texto? |

**Quesito 4 — Que tipo de ato e qual hierarquia deve ter a normatização?**
| Subitem | Pergunta |
|---|---|
| 4.1 | A matéria já não foi regulada em disposição de hierarquia superior? Há redundância a evitar? |
| 4.2 | Por que a matéria deve ser regulada por esta autoridade — caberia regulação por autoridade hierarquicamente inferior? |

**Quesito 5 — Deve a normatização ter prazo de vigência limitado?**
Norma temporária, submetida a período probatório, é o caso mais adequado?

**Quesito 6 — As normas preservam direito adquirido e demais garantias fundamentais? As exigências impostas são indispensáveis?**
Exemplos de exigência a escrutinar: proibições/necessidade de autorização;
comparecimento obrigatório; exigência de requerimento; dever de prestar
informações; imposição de multas e penas; outras sanções.

**Quesito 7 — O ato é exequível?**
| Subitem | Pergunta |
|---|---|
| 7.1 | As responsabilidades quanto à execução das medidas estão bem definidas? |
| 7.2 | Qual a opinião das autoridades incumbidas da execução quanto à clareza dos objetivos e à possibilidade de execução? |
| 7.3 | A regra foi submetida a testes de exequibilidade com as autoridades encarregadas de aplicá-la? Que conclusão se chegou? |

**Quesito 8 — Existe relação equilibrada entre custos e benefícios?**
| Subitem | Pergunta |
|---|---|
| 8.1 | Qual o ônus imposto aos atingidos pela norma? |
| 8.2 | Os atingidos podem suportar esses custos adicionais? |
| 8.3 | A medida impõe despesas adicionais ao orçamento da União/Estados/Municípios? Como enfrentá-las? |
| 8.4 | Foi feita análise de custo-benefício? A que conclusão se chegou? |
| 8.5 | Como serão avaliados a eficácia, o desgaste e os efeitos colaterais após a entrada em vigor? |

> **Fundamento adicional:** o Art. 7º, §2º, "b" do Anexo I da Portaria nº
> 271/2013 exige que a nota técnica contenha "histórico, fundamentação legal,
> análise e parecer com as justificativas da proposição" — estrutura que
> corresponde, na suíte cgov-nt, aos Capítulos 1 (`cgov-nt-03`), 2-3
> (`cgov-nt-04`) e 4 (`cgov-nt-05`), já produzidos antes desta skill.

## MODO 2 — CONSULTA JURÍDICA FACULTATIVA E NT DE SUBSÍDIO

Use quando a CGOV for **consultar a PFE** sobre uma dúvida jurídica (consulta
facultativa) ou instruir a NT que subsidia a análise jurídica de uma minuta.

**Normas de procedimento (conferidas no acervo em 07/11/2026):**
- Portaria ICMBio nº 271/2013, Anexo I: submissão da proposta de ato à PFE (art. 6º),
  documentos que a acompanham (art. 7º, § 2º), custeio ou declaração de ausência de
  incremento financeiro (art. 7º, §§ 3º e 4º) e conteúdo da consulta jurídica (art. 8º);
- Portaria ICMBio nº 129/2020: parecer conclusivo da PFE (art. 5º), avaliação conjunta e
  devolução por falta de requisitos formais (art. 7º) e documentos da proposta pelo SEI
  (art. 13). Onde colidir com a nº 271/2013, prevalece a nº 129/2020 (posterior).
- ⚠️ A Portaria Conjunta nº 3, de 13/05/2021 (elaboração e envio de consultas jurídicas
  à PFE), não está no acervo: confira o texto antes de citá-la. Não a confunda com a
  Portaria PFE/ICMBio nº 3, de 26/05/2021, que aprova a OJN nº 27/2021 (aviso de
  recebimento em comunicação postal).

**Consulta jurídica:** monte-a com o conteúdo do art. 8º do Anexo I da Portaria nº
271/2013: (I) manifestação conclusiva do órgão consulente; (II) atos e diplomas aplicáveis
ao caso; (III) explicitação da dúvida jurídica; (IV) opiniões contrárias que evidenciam a
dúvida, quando houver; (V) documentos que facilitem o exame da matéria.

**NT de subsídio à análise jurídica de minuta** — além dos capítulos da suíte, confira
se a NT contém:
1. contextualização da competência da CGOV (Art. 37 da Portaria ICMBio nº 5.592/2025);
2. histórico do processo de elaboração da minuta;
3. justificativa dos capítulos e artigos da minuta;
4. análise de não sobreposição com outros colegiados, quando a minuta criar ou
   alterar colegiado (⚠️ conferir a norma federal aplicável antes de citá-la);
5. indicação da fonte de custeio, se houver acréscimo de despesa, ou declaração formal
   de que a proposta não implica incremento financeiro (Portaria nº 271/2013, Anexo I,
   art. 7º, §§ 3º e 4º);
6. as respostas aos 8 quesitos do Anexo II da Portaria ICMBio nº 271/2013 (Modo 1);
7. nos atos de alteração ou consolidação, o quadro comparativo entre o texto vigente e o
   proposto (Portaria nº 129/2020, art. 13, III).

A CGOV não decide questão jurídica: registra os pontos jurídicos (`PJ-01`…) e
apresenta as propostas que deles dependam como condicionadas ou com alternativas.

## FORMATO DE SAÍDA

> Na prática observada da CGOV (validado por piloto contra NT real), esta
> análise é publicada como **subitem do Capítulo 4** (tipicamente item 4.4,
> após as recomendações de `cgov-nt-05`), não como capítulo autônomo. Ajuste o
> número do subitem à numeração final do Capítulo 4 no documento em elaboração.

```
#### 4.4. Questões a analisar na elaboração de atos administrativos, nos
termos do Anexo II da Portaria ICMBio nº 271/2013

[parágrafo de abertura: finalidade desta seção — subsidiar a PFE/ICMBio quanto
à conveniência, oportunidade, exequibilidade e custo-benefício da proposta,
com base nos diagnósticos dos capítulos anteriores]

**1. Deve ser tomada alguma providência?**
R: [Sim/Não] — [resposta corrida cobrindo os subitens 1.1 a 1.8 pertinentes ao
caso concreto; nem todo subitem exigirá desenvolvimento próprio em todo caso]

**2. Quais as alternativas disponíveis?**
R: [...]

**3. O ato corresponde às expectativas dos servidores/cidadãos e é inteligível para todos?**
R: [...]

**4. Que tipo de ato e qual hierarquia deve ter a normatização?**
R: [...]

**5. Deve a normatização ter prazo de vigência limitado?**
R: [...]

**6. As normas preservam direito adquirido e demais garantias fundamentais?**
R: [...]

**7. O ato é exequível?**
R: [...]

**8. Existe relação equilibrada entre custos e benefícios?**
R: [...]
```

**Regras de redação obrigatórias:**
- Cada um dos 8 quesitos recebe resposta assertiva (Sim/Não/Parcialmente),
  seguida de justificativa fundamentada — nunca deixe um quesito sem
  posicionamento.
- Os subitens (1.1 a 1.8, 2.1 a 2.2, etc.) orientam o conteúdo da resposta,
  mas não precisam necessariamente aparecer como sub-respostas destacadas no
  texto final — incorpore-os à prosa corrida da resposta ao quesito principal,
  salvo quando a complexidade do caso recomendar desenvolvimento próprio.
- Se um quesito (ou subitem) não puder ser respondido com segurança pelos
  elementos disponíveis, registre isso explicitamente como limitação, em vez
  de presumir uma resposta.
- Nunca invente artigo, número de norma ou dado quantitativo não constante de
  `NT_ESTADO.md`.

## PÓS-EXECUÇÃO — .docx DE REVISÃO (v4-quesitos-pfe)

A CGOV revisa a NT no Word. Por isso esta etapa termina com uma **nova versão do `.docx` da NT**,
que acumula os capítulos já redigidos e preserva as edições feitas pelo revisor na versão anterior.
O Markdown continua sendo a entrega no chat e a fonte do capítulo. O gerador é o
`montar_nt_docx.py` das **Ferramentas do Escritório** (caminho no `AGENTS.md`); ele aplica o padrão
gráfico das NTs da CGOV e nunca sobrescreve arquivo.

O `.md` começa pelo título do subitem (`#### 4.N. Questões a analisar…`, com o N seguinte ao
último subitem do Capítulo 4): o gerador o encaixa no fim do Capítulo 4, antes da Seção 5.
Cada quesito fica numa linha em negrito e a resposta (`R: …`) na linha de baixo.
No **MODO 2** (consulta facultativa), a NT de subsídio é outro documento: não alimente o `.docx`
desta NT; pergunte ao usuário se a NT de subsídio terá `.docx` próprio (com `--apelido` distinto).

1. **Antes de numerar quadros e figuras**, rode
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" --listar --pasta "<pasta de trabalho>"`.
   A lista mostra as versões existentes e a última linha dá o próximo Quadro nº e a próxima Figura nº:
   numere o capítulo a partir deles.
2. **Grave o capítulo** na pasta de trabalho como `NT_<apelido>_v4-quesitos-pfe.md` (`<apelido>` é o final do nome da
   pasta do processo, `SEI_…_<apelido>`): o mesmo texto entregue no chat, com legenda
   `**Quadro N — título**` antes de cada tabela e `Fonte: …` depois; pendências ficam fora do arquivo
   (vão para a resposta e para o `NT_ESTADO.md`).
3. **Simule e gere:**
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" "<pasta de trabalho>/NT_<apelido>_v4-quesitos-pfe.md" --versao 4 --etapa quesitos-pfe --simular`.
   Se o relatório (JSON) não trouxer erro, rode o mesmo comando sem `--simular`.
4. **Relate ao usuário**, em até cinco linhas: arquivo gerado, versão usada como base, avisos do
   relatório (numeração de quadros ou figuras, figura não inserida, tabela sem legenda, trecho
   excluído) e quantos ⚠ restam no texto.
5. **Registre** no `NT_ESTADO.md`, seção "Versões do .docx" (crie-a se não existir):
   `v4-quesitos-pfe — NT_<apelido>_v4-quesitos-pfe.docx — [data] — base: [versão anterior ou "novo"] — [n] aviso(s)`.

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

Acrescente ao `NT_ESTADO.md` (na subpasta localizada na Pré-execução):
`Quesitos PFE (Anexo II, Portaria nº 271/2013): concluídos em [data].`

## ENCADEAMENTO

```
/cgov-nt-04 → [/cgov-nt-05] → /cgov-nt-06 (esta skill, se aplicável) → /cgov-nt-07
```

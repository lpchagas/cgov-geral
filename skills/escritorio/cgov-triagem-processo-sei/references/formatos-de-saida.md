# Formatos de saída — cgov-triagem-processo-sei

> Origem: Seção 6 de `docs/system-instructions/analista-processos-sei.md` (v7.2), adaptada na Fase 6.4 (07/11/2026).
> "Cadeia de raciocínio" e "guardrails" se referem ao `SKILL.md` desta skill.

Regras gerais para todos os comandos:

- Execute sempre a cadeia de raciocínio do `SKILL.md` antes de produzir a saída.
- Respeite o formato **exatamente**; não adicione nem suprima seções.
- Todo campo não confirmado nos autos vai entre `[COLCHETES]` ou recebe
  `[NÃO CONSTA NOS AUTOS FORNECIDOS]`.
- Saída sempre em **Markdown**, no chat. `.docx` ou `.pdf` somente se
  solicitado expressamente e via ferramenta apropriada.

### 1. `/ANALISAR_PROCESSO` — triagem completa

```markdown
### Relatório de Análise Processual (Triagem)

**0. Escopo da leitura**
* **Documentos lidos:** [listar: tipo, nº SEI, data]
* **Cobertura:** [Integral / Parcial — especificar o que não foi lido e por quê]

**1. Dados Básicos**
* **Processo SEI:** [Número | NÃO CONSTA]
* **Interessado:** [Nome/Unidade | NÃO CONSTA]
* **Assunto:** [Resumo em 1 linha]
* **Unidade de origem:** [ | NÃO CONSTA]
* **Última tramitação:** [Unidade — data | NÃO CONSTA]
* **Entrada na CGOV:** [Data | NÃO CONSTA]
* **Último documento juntado:** [Tipo, nº, data]

**2. Objeto da Demanda**
[O que se pede (pedido explícito) e o que se discute (objeto material), em
até 5 linhas. Indicar o documento e a folha em que isso foi lido.]

**3. Admissibilidade e Competência**
* **Competência da CGOV:** [SIM / NÃO / PARCIAL]
* **Fundamento:** Art. 37, parágrafo único, inciso [N], da Portaria ICMBio
  nº 5.592, de 11 de dezembro de 2025 — [transcrever o inciso].
* **Se NÃO ou PARCIAL:** unidade(s) competente(s) sugerida(s) e fundamento.
* **Regularidade formal:** [Regular / Irregular / Irregular sanável]
  | Item verificado | Situação | Observação |
  | :--- | :--- | :--- |
  | Competência da autoridade | | |
  | Espécie/forma do expediente | | |
  | Documentos essenciais | | |
  | Assinaturas eletrônicas | | |
  | Motivação dos atos decisórios | | |
  | Ordem cronológica | | |

**4. Tempestividade**
* **Prazo aplicável:** [dispositivo]
* **Contagem:** [marco inicial] → [marco final] = [N] dias
* **Situação:** [Tempestivo / Intempestivo / Não aplicável / Indeterminado]

**5. Pontos de Atenção**
* [Riscos processuais, lacunas de instrução, controvérsias entre unidades.]

**6. Sugestão de Encaminhamento**
[Uma das opções: Análise Técnica (NT) / Despacho de encaminhamento /
Restituição para diligência / Sobrestamento / Arquivamento / Declínio de
competência — com justificativa em 2 a 3 linhas.]

**7. Lacunas e pendências desta análise**
* [Tudo que não pôde ser verificado e o que seria necessário para verificar.]

---
*Minuta de apoio técnico. Sujeita a revisão e validação por servidor responsável
antes de qualquer juntada ou tramitação no SEI.*
```

### 2. `/REDIGIR_DESPACHO` — despacho interlocutório ou decisório

```markdown
### Minuta de Despacho

**Processo nº:** [Número | NÃO CONSTA]
**Assunto:** [Assunto]

Ao(À) Senhor(a) [Cargo do destinatário],

1. Trata-se de [objeto], encaminhado a esta Coordenação de Governança — CGOV
   para [finalidade], conforme [documento SEI nº ___].

2. A matéria insere-se na competência desta Coordenação, nos termos do art. 37,
   parágrafo único, inciso [N], da Portaria ICMBio nº 5.592, de 11 de dezembro
   de 2025. [Ou, se for o caso: A matéria não se insere na competência desta
   Coordenação, razão pela qual se propõe o encaminhamento à [unidade].]

3. Da análise dos autos, verifica-se que [síntese objetiva do exame formal e,
   se houver, de mérito, com remissão às folhas/documentos].

4. Diante do exposto, propõe-se:
   a) [ação];
   b) [ação].

5. À consideração superior.

Brasília, [DATA].

**[NOME]**
[Cargo]
Coordenação de Governança — CGOV/CGGE/ICMBio

---
*Minuta. O número do documento e a data são gerados pelo SEI no momento da
assinatura — não os preencha manualmente.*
```

### 3. `/REDIGIR_NOTA_TECNICA` — roteamento obrigatório

> **Este comando não produz a NT diretamente.**
>
> A elaboração de Nota Técnica da CGOV é competência da suíte canônica
> `cgov-nt-01` a `07`, validada por piloto contra Nota Técnica real protocolada
> e encaminhada à PFE. Produzir a NT fora dessa suíte reintroduz erros já
> corrigidos (estrutura, numeração de capítulo, tempo verbal, quesitos do
> Anexo II).
>
> **Ação:** acione `cgov-nt-01-triagem`, transmitindo o resultado da sua
> `/ANALISAR_PROCESSO` como insumo (objeto, processo SEI, unidades, enquadramento
> no Art. 37, destino do produto — se seguirá ou não à PFE).

**Exceção — nota técnica sumária.** Se o usuário pedir expressamente uma
manifestação curta que **não** será juntada como Nota Técnica formal, você pode
produzi-la, sinalizando no topo:

> ⚠️ *Manifestação técnica sumária. Não é Nota Técnica no padrão da CGOV. Para
> NT formal, use a suíte `cgov-nt`.*

Estrutura canônica da NT da CGOV, para sua referência ao preparar o insumo:
**DESTINATÁRIO → INTERESSADO → REFERÊNCIAS → FUNDAMENTAÇÃO / ANÁLISE TÉCNICA /
PARECER → CONCLUSÃO E/OU PROPOSIÇÃO**, com capítulos no formato
`### Capítulo N — [Nome]` e subseções `#### N.1`, `#### N.2` reiniciadas a cada
capítulo.

✅ **Cabeçalho fixado em 04/08/2026.** O padrão oficial da Nota Técnica da CGOV é:

```
Nota Técnica nº [#]/[ANO]/CGOV/CGGE/GABIN/ICMBio
```

A sigla `DIPLAN`, que constava da v6.0, está **incorreta** e não deve ser usada.
Este é o mesmo padrão já aplicado pela skill `cgov-nt-03-introducao`.

### 4. `/INDICAR_NORMAS` — quadro de referência normativa

```markdown
### Quadro de Referência Normativa Aplicável

**Objeto analisado:** [síntese em 1 linha]

| # | Norma | Dispositivos | Aplicação ao caso | Status |
| :-- | :--- | :--- | :--- | :--- |
| 1 | [Norma principal] | [arts.] | [Como afeta o processo] | ✅/🔎/⚠️ |
| 2 | [Norma secundária] | [arts.] | | |

**Normas afastadas e por quê**
* [Norma que poderia parecer aplicável, mas não é — com a razão.]

**Jurisprudência e entendimentos de controle**
* [Somente se houver acórdão, enunciado ou orientação **efetivamente
  verificado** nesta sessão ou constante da base do projeto, com número, órgão
  e data. Caso contrário, escrever exatamente: "Não foram identificados
  precedentes verificáveis nas fontes disponíveis nesta análise."]

**Nível de confiança**
* Alto: [normas ✅ e 🔎] · Requer conferência: [normas ⚠️]
```

> **Proibição expressa:** é vedado citar acórdão, súmula, enunciado ou
> orientação normativa "de memória". Sem verificação, use a frase-padrão de
> ausência acima.

### 5. `/CHECAR_INSTRUCAO` — checklist de saneamento *(novo na v7.0)*

Para uso rápido antes de tramitar, sem relatório completo.

```markdown
### Checklist de Instrução Processual — Processo [nº]

| # | Item | Situação | Fundamento | Providência |
| :-- | :--- | :--- | :--- | :--- |
| 1 | Competência da autoridade | ✅/❌/⚠️ | Lei nº 9.784/1999, arts. 11-17 | |
| 2 | Espécie e forma do expediente | | Portaria ICMBio nº 271/2013, art. 2º | |
| 3 | Documentos essenciais juntados | | | |
| 4 | Anexos citados efetivamente juntados | | | |
| 5 | Assinaturas eletrônicas válidas | | Decreto nº 8.539/2015 | |
| 6 | Motivação dos atos decisórios | | Lei nº 9.784/1999, art. 50 | |
| 7 | Prazos observados | | Lei nº 9.784/1999, arts. 24, 42, 49 | |
| 8 | Manifestação da PFE, se exigível | | Portaria ICMBio nº 271/2013, art. 6º | |
| 9 | Classificação de sigilo adequada | | Lei nº 12.527/2011, arts. 23-24 | |
| 10 | Dados pessoais tratados conforme LGPD | | Lei nº 13.709/2018 | |

**Impedimentos ao prosseguimento:** [listar apenas os ❌ que bloqueiam.]
**Ajustes recomendáveis:** [listar os ⚠️.]
```

### 6. `/REDIGIR_RESTITUICAO` — devolução para diligência *(novo na v7.0)*

```markdown
### Minuta de Despacho de Restituição

**Processo nº:** [Número]
**Assunto:** Restituição para complementação de instrução

À [Unidade de origem],

1. Trata-se de [objeto], recebido nesta Coordenação de Governança em [data],
   por meio do [documento SEI nº ___].

2. Procedida à análise preliminar de admissibilidade, verifica-se que a
   instrução processual encontra-se incompleta para manifestação desta
   Coordenação, nos seguintes pontos:
   a) [pendência 1 — indicar o dispositivo ou a razão técnica que a torna
      necessária];
   b) [pendência 2].

3. Nesses termos, restituem-se os autos à unidade de origem para complementação,
   no prazo de [N] dias, nos termos do art. 24 da Lei nº 9.784, de 29 de janeiro
   de 1999.

4. Sanadas as pendências, os autos poderão retornar a esta Coordenação para
   manifestação de mérito.

Brasília, [DATA].

**[NOME]** — [Cargo]
Coordenação de Governança — CGOV/CGGE/ICMBio
```

### 7. `/REDIGIR_OFICIO` — comunicação externa *(novo na v7.0)*

Padrão ofício do Manual de Redação da PR, 3ª ed. (2018): identificação do
expediente, local e data, destinatário com endereçamento, assunto sintético em
uma linha, texto em parágrafos numerados a partir do segundo, fecho
("Atenciosamente" para autoridades de mesma hierarquia ou inferior;
"Respeitosamente" para autoridade superior) e identificação do signatário.

> Ofício destinado a órgão externo depende de competência para representação
> institucional. Ao minutar, registre: *"Verificar a competência do signatário
> para a comunicação externa antes da assinatura."*

### 8. `/ORIENTAR` — orientação metodológica

```markdown
### 🧭 Orientação: [TEMA]
*Referência: [norma ou guia, com status ✅/🔎/⚠️]*

**1. Conceito e objetivo**
[Explicação direta.]

**2. Passo a passo**
* Passo 1 — [ação]
* Passo 2 — [ação]

**3. Erros comuns e como evitá-los**
> [Armadilhas típicas do tema.]

**4. Limites desta orientação**
[O que precisa de confirmação, de skill dedicada ou da PFE.]
```

---

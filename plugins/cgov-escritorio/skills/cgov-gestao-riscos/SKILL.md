---
name: "cgov-gestao-riscos"
description: >
  Gestão de riscos institucionais da CGOV/ICMBio com o CTGRIC (Art. 37, p.u., IX, da
  Portaria ICMBio nº 5.592/2025), em transição de regime: Regime A, vigente
  (Metodologia da Portaria ICMBio nº 975/2021; PGRI, Portaria nº 255/2020); Regime B,
  minutas da Política RADAR e da nova Metodologia, só como simulação rotulada enquanto
  não publicadas. Declara o regime antes de calcular e nunca mistura réguas. Cobre
  contexto, identificação (causa, evento, consequência), análise, matriz impacto ×
  probabilidade, risco inerente e residual, eficácia de controles, apetite, KRI,
  tratamento, Plano de Gestão de Riscos e monitoramento. Use ao invocar
  /cgov-gestao-riscos, "mapear riscos", "matriz de riscos", "risco residual",
  "eficácia do controle", "plano de tratamento", "CTGRIC", "PGRI", "RADAR", "Portaria
  975". Não é o risco de entrega do PGD; PGR (Gestão para Resultados) é a cgov-pgr.
---

# cgov-gestao-riscos — Gestão de Riscos Institucionais (CGOV/ICMBio)

Esta skill apoia a CGOV/ICMBio no cumprimento do **Art. 37, parágrafo único,
inciso IX**, da Portaria ICMBio nº 5.592/2025: coordenar, em conjunto com o
**CTGRIC**, a implementação da Política de Gestão de Riscos.

A base normativa está **em transição**. A Metodologia vigente (Portaria ICMBio
nº 975/2021) está sendo substituída por uma nova Política, a **RADAR**, e uma nova
Metodologia, ambas ainda em minuta. As duas metodologias produzem **números
diferentes para o mesmo risco**: 6 das 25 células da matriz mudam de classe, e os
controles reduzem bem menos o risco residual na nova versão. Por isso, a primeira
decisão de qualquer trabalho é **sob qual regime** calcular.

---

## 0. REGIME NORMATIVO — DECIDA ANTES DE QUALQUER CÁLCULO

| | **Regime A — vigente** | **Regime B — RADAR (minutas)** |
|---|---|---|
| Política | Portaria ICMBio nº 255/2020, PGRI | Minuta da Política de Gestão de Riscos, **RADAR** (15/09/2026); revoga a Portaria 255/2020 (art. 20) |
| Metodologia | Portaria ICMBio nº 975/2021 | Minuta da nova Metodologia (Anexos I a III) |
| Instância decisória | **Comitê Gestor do ICMBio** (Portaria 4.101/2023, arts. 12-14) | "**Comitê Interno de Governança – CIG**" (ver §8, item 1) |
| Situação em 21/10/2026 | Em vigor | **Não publicadas**; versões posteriores à consulta interna (prazo 03/09/2026) |

**Como escolher:**

1. **Análise de risco real** (matriz de uma unidade, insumo para o Plano, resposta
   a auditoria): use o **Regime A** enquanto a RADAR não estiver publicada. Se for
   útil, apresente o Regime B ao lado como **simulação**, com esse rótulo.
2. **Trabalho da CGOV sobre a própria revisão** (nota técnica, consolidação de
   contribuições, simulação de impacto, capacitação prévia, preparação do Plano de
   Gestão de Riscos 2026-2028 já no novo modelo): use o **Regime B**.
3. **Se o usuário informar a publicação** (número da portaria e data no DOU): o
   Regime B passa a ser o vigente e o A fica revogado. Registre o número e a data,
   e confira se o texto publicado é igual ao das minutas antes de confiar nas
   tabelas abaixo. Os valores do §3 podem ter mudado.
4. **Na dúvida, pergunte uma única vez** e siga com o Regime A, declarando a escolha.

Nunca misture os dois regimes numa mesma matriz. Rotule cada saída com o regime
("Regime A – Portaria 975/2021" ou "Regime B – minuta RADAR").
Quem lê precisa saber de qual régua veio cada número.

### Convenção de siglas

| Sigla | Significado | Norma | Nesta skill? |
|---|---|---|---|
| **PGRI** | Política de Gestão de Riscos e Integridade | Portaria 255/2020 (Regime A) | ✅ |
| **RADAR** | Rede de Avaliação, Diagnóstico e Ação em Riscos: nova Política de Gestão de Riscos | Minuta da Política (Regime B) | ✅ |
| **PGR** | Programa de Gestão para Resultados e Inovação | Portaria 1.572/2023 | ❌ use `cgov-pgr` |
| **PGD** | Programa de Gestão e Desempenho | IN ICMBio 14/2025 | ❌ use `pgd-especialista` |
| **KRI** | Indicador-chave de risco (*Key Risk Indicator*) | Regime B | ✅ |
| **DAR** | Declaração de Apetite a Riscos | Regime B (Anexo III) | ✅ |

> Nunca escreva "PGR de riscos". O Plano de Gestão de Riscos se escreve por
> extenso. A sigla PGR pertence ao Programa de Gestão para Resultados. Se o
> usuário usar "PGR" querendo dizer riscos, corrija brevemente e siga adiante.
>
> A nova Política não tem "Integridade" no nome. Os riscos para a integridade
> continuam como categoria da Metodologia e são tratados no **Integra+**
> (Portaria 253/2026).

### Risco institucional × risco de entrega do PGD

Esta skill trata do risco que entra no ciclo institucional de gestão de riscos:
matriz, Plano de Gestão de Riscos, CTGRIC. No Regime B, os **objetos de gestão de
riscos** incluem processos, metas, atividades e **projetos** (Quadro 1). Um risco
de projeto pode, portanto, ser tratado aqui quando for levado ao ciclo
institucional.

Já o formulário de dependências e riscos de uma entrega do Plano de Entregas do
PGD pertence ao componente **S10** do `pgd-agente-icmbio`. Se o pedido for desse
tipo, explique a diferença e encaminhe ao S10.

---

## 1. BASE NORMATIVA

| Norma | Objeto | Situação / papel |
|---|---|---|
| Portaria ICMBio nº 975/2021 | Metodologia de Gestão de Riscos | **Vigente (Regime A)**. Texto verificado em 04/08/2026 |
| Portaria ICMBio nº 255/2020 | PGRI | **Vigente (Regime A)**; revogação prevista na minuta da RADAR |
| Minuta da Política RADAR | Política de Gestão de Riscos | **Minuta (Regime B)**, transcrita na pasta de trabalho do processo da Política de Gestão de Riscos (localize pela ficha `PROCESSO.md`) |
| Minuta da nova Metodologia | Metodologia de Gestão de Riscos | **Minuta (Regime B)**, transcrita na mesma pasta de trabalho do processo |
| Portaria ICMBio nº 4.101/2023 | Política de Governança | Define o **Comitê Gestor** como instância interna de governança |
| Portaria ICMBio nº 4.529/2025 | CTGRIC | Vigente. A **CGOV é a Secretaria-Executiva** |
| Portaria ICMBio nº 253/2026 | Programa de Integridade Integra+ | Vigente. Ainda cita a PGRI e a Portaria 975 |
| Portaria ICMBio nº 1.164/2025 | Planejamento Estratégico 2025-2027 | Monitoramento trimestral; revogou a PGE (Portaria 768/2020) |
| Decreto nº 9.203/2017 | Governança da APF | Fundamento dos instrumentos (Política, art. 15, I) |
| Decreto nº 11.529/2023 | SITAI | O CTGRIC atua como unidade setorial |
| IN Conjunta MP/CGU nº 1/2016 | Controles internos, riscos e governança | Marco federal |
| ABNT NBR ISO 31000:2018 e ISO/IEC 31010 | Diretrizes e técnicas | Só referência conceitual |
| ⛔ Portaria ICMBio nº 768/2020 | Política de Gestão Estratégica (PGE) | **Revogada** pela Portaria 1.164/2025; não citar como vigente |
| ⛔ Portaria ICMBio nº 923/2020 | Integra+ (versão original) | Superada; a Portaria 975 ainda a cita |

> **Precedência:** a metodologia do ICMBio do regime escolhido prevalece sobre
> ISO, COSO, TCU e CGU. Não importe escalas, matrizes ou nomenclaturas de fora.
> A minuta da RADAR permite que as unidades usem "outras abordagens
> metodológicas, desde que não contrariem" a Metodologia. Isso autoriza técnicas
> complementares, não réguas próprias de classificação.

---

## 2. FASE 1 — ESCOPO E OBJETO

Pergunte apenas o que não estiver claro no contexto:

1. **Regime:** A ou B (§0)?
2. **Objeto:** qual processo, meta, projeto, unidade ou objetivo estratégico?
3. **Fase do ciclo:** mapeamento do zero, revisão de matriz, tratamento,
   monitoramento, consolidação do Plano ou avaliação de maturidade?
4. **Regime B, apetite:** já existe Declaração de Apetite a Riscos aprovada? Se
   não existir, a classificação de "risco crítico" fica pendente (§3.4).
5. **Insumos:** planilha de riscos, ata, relatório de auditoria, mapeamento do
   processo?
6. **Responsável:** quem é o gestor de riscos do objeto? No Regime A, cada
   Diretoria e o Gabinete designam a equipe que participa das etapas. No Regime B,
   a lista de gestores está no art. 17, §1º, da Política.
7. **Contexto institucional:** há deliberação do CTGRIC, do Comitê Gestor/CIG ou
   da alta gestão que oriente o escopo?

> Se o essencial estiver claro, prossiga e registre as lacunas como pendências.

---

## 3. FASE 2 — ETAPAS DO PROCESSO

A numeração segue o Regime B. A correspondência com o Regime A está indicada em
cada etapa.

| Etapa | Regime A (Portaria 975/2021) | Regime B (minuta RADAR) |
|---|---|---|
| Contexto | 4.1 (SIPOC, Tab. 1; ambiente, Tab. 2) | 4.1 (Quadro 1, atributos dos objetos) |
| Identificação | 4.2 (Tab. 3 e 4) | 4.2 (Quadros 2 e 3) |
| Análise | 4.3 (Tab. 5, 6 e 7) | 4.3 (Quadros 4 a 8 e cálculo do residual) |
| Avaliação | 4.4 (Tab. 8, 9 e 10) | 4.4 (comparação com o apetite) |
| Priorização | 4.5 (Tab. 11) | Sem etapa própria; substituída pelo apetite |
| Tratamento | 4.6 (Tab. 12 e 13, 5W2H) | 4.5 (bow tie; estratégias na "Tabela 8") |
| Plano de Gestão de Riscos | — | 4.6 (validação e aprovação) |
| Monitoramento | 4.7 (comunicação e monitoramento) | 4.7 (monitoramento, KRIs, registro e relato) |
| Maturidade | — | 5 (avaliação da gestão de riscos) |

### 3.1 Entendimento do contexto

- **Regime A:** mapear o processo pela ferramenta **SIPOC** (Tabela 1), na ordem
  da norma: (1) Processos → (2) Produtos/Serviços → (3) Clientes → (4) Insumos →
  (5) Fornecedores. A ordem é contraintuitiva em relação à sigla, mas é a que a
  norma determina. Depois, analisar o ambiente (Tabela 2).
- **Regime B:** identificar objetivos, processos, pessoas e fatores internos e
  externos. Em seguida, definir os **objetos de gestão de riscos** (processos de
  trabalho, metas, atividades, projetos) e detalhá-los no **Quadro 1**:

| Tipo de objeto de GR | Descrição do objeto | Principais resultados/objetivos | Recursos necessários |
|---|---|---|---|

O contexto institucional desta etapa também subsidia a Declaração de Apetite a
Riscos.

### 3.2 Identificação de riscos (comum aos dois regimes)

Técnicas admitidas: *brainstorming*, *brainwriting*, questionários, entrevistas,
visitas técnicas, *check-list*, matriz SWOT, dados históricos, análise de
premissas, opiniões especializadas, necessidades das partes interessadas e
diagramas de causa e efeito. Pergunta-chave: *o que pode atrapalhar o alcance do
objetivo/resultado?* Fontes principais: infraestrutura, pessoal, processos e
tecnologia.

**Sintaxe obrigatória, idêntica nos dois regimes:**

> **"Devido o(a) `<CAUSA>`, poderá ocorrer o(a) `<EVENTO DE RISCO>`, ocasionando
> o(a) `<CONSEQUÊNCIA>` e impactando o alcance do `<OBJETIVO ESTRATÉGICO>`."**

- **CAUSA:** origem do risco. A probabilidade é estimada pelas causas.
- **EVENTO:** o fato que pode ocorrer. Não é a causa nem a consequência.
- **CONSEQUÊNCIA:** o efeito se o evento se materializar. O impacto é estimado
  pelas consequências.
- **OBJETIVO:** o resultado afetado.

Se o risco vier fora dessa estrutura, **reescreva antes de prosseguir** e explique
o que faltava. Erros comuns:
- apresentar a consequência como evento;
- apresentar a ausência de controle ("falta de sistema") como risco, quando isso é
  causa;
- omitir o objetivo.

**Categorias.** Um risco pode tocar mais de uma categoria, mas sempre há uma
dominante; registre essa.

| Categoria | Descrição resumida | A | B |
|---|---|---|---|
| Operacional | Falhas ou inadequação de processos, pessoas, infraestrutura e sistemas | ✅ | ✅ |
| Legal | Alterações legislativas ou normativas | ✅ | ✅ |
| Financeiro/Orçamentário | Recursos orçamentários e financeiros, execução orçamentária | ✅ | ✅ |
| Reputação | Confiança da sociedade e imagem da autarquia | ✅ | ✅ |
| Integridade | Corrupção, fraude, irregularidade, desvio ético ou de conduta | ✅ | ✅ |
| Riscos da visitação | Segurança de visitantes em uso público nas UCs | — | ✅ |
| Ocupacionais | Saúde, integridade física e segurança de servidores e colaboradores | — | ✅ |
| Privacidade e Proteção de Dados | Dados pessoais e LGPD (Lei nº 13.709/**2018**) | — | ✅ |

No Regime A, um risco de visitação, ocupacional ou de dados pessoais entra na
categoria dominante entre as cinco existentes (em geral, Operacional ou Legal).
Diga isso ao usuário em vez de criar uma categoria nova.

**Varredura das categorias antes de fechar a lista de riscos.** Use as oito
categorias do Quadro 2 como lentes, mesmo no Regime A. Em análises de norma,
minuta ou processo, pergunte para cada uma: "o que este texto ou processo deixa
exposto aqui?". Três lentes costumam ser esquecidas e merecem pergunta explícita:

- **Ocupacionais:** há trabalho de campo, área de conflito, histórico de violência,
  deslocamento em região remota ou atividade física de risco para servidores e
  colaboradores?
- **Privacidade e Proteção de Dados:** há coleta, cadastro, juntada de documento,
  publicação ou compartilhamento de dados pessoais, sobretudo os sensíveis
  (origem étnica, saúde)?
- **Visitação:** a atividade envolve uso público de UC?

Se uma lente não gerar risco, siga adiante sem mencioná-la. O objetivo é não
deixar passar um risco relevante só porque ele não cabe nas categorias
tradicionais.

**Quando classificar como Integridade.** Um risco é de Integridade quando o
evento depende de um **agente público decidir, atestar ou deixar de agir** em
situação em que um interesse privado pode prevalecer: por pressão, favorecimento,
conflito de interesses ou vantagem. Situações típicas:
- definir quem é beneficiário, elegível, compromissário ou cadastrado;
- conceder autorização, licença, uso de recurso ou direito;
- fiscalizar, aplicar ou deixar de aplicar sanção;
- contratar, atestar execução ou receber bem ou serviço.

Nesses casos:
1. Teste as seis subcategorias abaixo.
2. Se alguma se aplicar, a categoria dominante é **Integridade**. Indique a
   subcategoria e conecte o risco ao Integra+.
3. Se nenhuma se aplicar (por exemplo, o problema é só um erro de cadastro, sem
   espaço para favorecimento), registre em uma linha por que o risco ficou como
   Operacional.

Não use "Operacional com interface de Integridade" como saída: isso esconde o
risco do Programa de Integridade. Um mesmo processo pode gerar dois riscos
distintos, um operacional (erro, atraso) e outro de integridade (favorecimento).
Descreva os dois quando ambos existirem.

**Subcategorias de integridade** (iguais nos dois regimes; Tabela 4 no A, Quadro 3
no B):
1. Abuso de posição ou poder em favor de interesses privados
2. Nepotismo
3. Conflito de interesses
4. Pressão interna ou externa ilegal para influenciar agente público
5. Solicitação ou recebimento de vantagem indevida
6. Utilização de recursos públicos em favor de interesses privados

Riscos para a integridade são tratados no **Integra+** (Portaria 253/2026, que
revogou a 1.257/2022, sucessora da 923/2020). No Regime A, a Portaria 975 ainda
cita a 923/2020. Cite sempre a 253/2026. O Integra+ define riscos para a
integridade como "possibilidade de ocorrência de evento de corrupção, fraude,
irregularidade ou desvio ético ou de conduta que venha a impactar o cumprimento
dos objetivos institucionais" (art. 2º, III).

### 3.3 Análise: escalas, matriz, classificação e risco residual

#### Probabilidade

| Nível | Regime A: descritor (Tab. 5) | Regime A: ocorrências* | Regime B: descritor (Quadro 4) | Regime B: descrição |
|---|---|---|---|---|
| 1 | Muito baixa | Até 5 | **Raro** | Só em situações excepcionais; sem histórico ou indício |
| 2 | Baixa | > 5 até 10 | **Pouco provável** | Histórico de baixa frequência no prazo do objetivo |
| 3 | Média | > 10 até 15 | **Provável** | Esperado, de frequência reduzida, conhecido pela maioria |
| 4 | Alta | > 15 até 20 | **Muito provável** | Usual, habitual, amplamente conhecido |
| 5 | Muito alta | > 20 | **Praticamente certo** | Repetitivo e constante; evidente a quem conhece o processo |

\* No Regime A, o gestor pode ajustar **apenas** a coluna "Ocorrências". O Regime B
não tem essa coluna.

#### Impacto

| Nível | Regime A (Tab. 7) | Regime B (Quadro 5) |
|---|---|---|
| 1 | Muito baixo: insignificante, dispensa reparação | Muito baixo: compromete minimamente; na prática não altera o alcance |
| 2 | Baixo: mínimo, fácil reparação | Baixo: compromete em alguma medida, sem impedir a maior parte |
| 3 | Médio: mediano, reparável | Médio: compromete razoavelmente |
| 4 | Alta *(grafia do original)*: significante, reparação remota | Alto: compromete a maior parte |
| 5 | Muito alto: máximo, irreparável | Muito alto: compromete total ou quase totalmente |

Só no Regime A há a **Tabela 6, Impacto nas Dimensões do Objeto**, que apoia a
escolha do nível:

| Nível | Custo (aumento %) | Prazo (atraso %) | Escopo | Qualidade |
|---|---|---|---|---|
| 1 | Até 5 | Até 5 | Insignificante | Irrisória |
| 2 | > 5 até 10 | > 5 até 10 | Pouco | Pouco |
| 3 | > 10 até 15 | > 10 até 15 | Significativa | Relevante |
| 4 | > 15 até 20 | > 15 até 20 | Muito significativa | Muito relevante |
| 5 | > 20 | > 20 | Ampla | Grave |

#### Risco inerente: Regime A (produto + máscara)

**Valor = Impacto × Probabilidade** (Tabela 8). A **classe vem da máscara** da
Tabela 9, célula a célula, e não de faixas do produto:

| Impacto ↓ / Prob. → | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 · Médio | 10 · Alto | 15 · Extremo | 20 · Extremo | 25 · Extremo |
| **4** | 4 · Médio | 8 · Alto | 12 · Alto | 16 · Extremo | 20 · Extremo |
| **3** | 3 · Médio | 6 · Médio | 9 · Alto | 12 · Alto | 15 · Extremo |
| **2** | 2 · Baixo | 4 · Médio | 6 · Médio | 8 · Alto | 10 · Alto |
| **1** | 1 · Baixo | 2 · Baixo | 3 · Médio | 4 · Médio | 5 · Médio |

O gestor pode adequar a máscara (Tabela 9) ao seu contexto, mas não a matriz de
valores (Tabela 8).

#### Risco inerente: Regime B (matriz ordinal + faixas)

O nível é **lido na célula** do Quadro 7, **não calculado**. A minuta veda soma e
multiplicação porque matrizes simétricas igualam riscos de impacto alto com riscos
de impacto baixo. A **classe vem das faixas** do Quadro 8: 1–5 Baixo · >5–10 Médio
· >10–17 Alto · >17–25 Extremo.

| Impacto ↓ / Prob. → | Raro | Pouco provável | Provável | Muito provável | Praticamente certo |
|---|---|---|---|---|---|
| **Muito alto** | 15 · Alto | 19 · Extremo | 22 · Extremo | 24 · Extremo | 25 · Extremo |
| **Alto** | 10 · Médio | 14 · Alto | 18 · Extremo | 21 · Extremo | 23 · Extremo |
| **Médio** | 6 · Médio | 9 · Médio | 13 · Alto | 17 · Alto | 20 · Extremo |
| **Baixo** | 3 · Baixo | 5 · Baixo | 8 · Médio | 12 · Alto | 16 · Alto |
| **Muito baixo** | 1 · Baixo | 2 · Baixo | 4 · Baixo | 7 · Médio | 11 · Alto |

> A célula Raro × Muito alto (15) vem antes de Praticamente certo × Muito baixo
> (11) na ordenação. A minuta chama o 11 de "bem menos prioritário", embora os
> dois sejam **Alto** pelas faixas. Use o número para ordenar e a faixa para
> classificar.

#### Eficácia dos controles e risco residual (fórmula comum, fatores diferentes)

**Risco residual = risco inerente × fator de eficácia do controle existente.** A
classe do residual vem da mesma régua do inerente no respectivo regime. Não
reclassifique probabilidade e impacto para obter o residual: esse é o método de
outras metodologias, não o do ICMBio. A eficácia dos controles não pode ser
alterada pelo gestor.

| Eficácia | Regime A: multiplicador (Tab. 10) | Regime B: fator (Quadro 6) | Descrição no Regime B |
|---|---|---|---|
| Inexistente | 1,00 | 1,0 | Inexistentes, mal desenhados ou mal implementados (não funcionais) |
| Fraco | 0,80 | **0,9** | Depende do conhecimento pessoal; manual; responsabilidade individual |
| Mediano | 0,60 | **0,75** | Mitigam alguns aspectos; falhas de desenho ou ferramentas |
| Satisfatório | 0,40 | **0,6** | Implementados, com ferramentas adequadas; mitigam satisfatoriamente |
| Forte | 0,20 | **0,5** | "Melhor prática"; mitigam todos os aspectos relevantes |

No Regime B, avalie a eficácia pelo desenho, formalização, implementação,
periodicidade, monitoramento e **evidências de funcionamento**. Um controle sem
evidência não passa de "Fraco".

**Classificação do residual:**
- **Regime A:** a norma manda reclassificar o valor residual pela máscara da
  Tabela 9. A máscara original é coerente por valor: cada produto pertence a uma
  única classe. Daí se derivam as faixas **1–2 Baixo · 3–6 Médio · 8–12 Alto ·
  15–25 Extremo**. Um residual decimal **entre 2 e 3**, **entre 6 e 8** ou **entre 12 e 15** cai
  numa lacuna da norma (ex.: 2,4 vai para Médio). Nesse caso, adote a classe superior por prudência e
  declare a lacuna. Se a unidade tiver adequado a máscara, use a dela.
- **Regime B:** aplique as faixas do Quadro 8 ao valor exato, **sem arredondar**
  (10,2 é Alto; 17,1 é Extremo). A minuta não trata de arredondamento; registre
  isso quando um valor cair perto de uma fronteira.

**Tabela de apoio do Regime B** (derivada por cálculo a partir dos Quadros 6, 7 e
8; não é texto da minuta). Mostra o residual e a classe (B/M/A/E) para cada nível
inerente:

| Inerente | Classe | Inexistente 1,0 | Fraco 0,9 | Mediano 0,75 | Satisfatório 0,6 | Forte 0,5 |
|---|---|---|---|---|---|---|
| 1–5 | Baixo | = · B | ≤4,5 · B | ≤3,75 · B | ≤3 · B | ≤2,5 · B |
| 6 | Médio | 6 · M | 5,4 · M | 4,5 · B | 3,6 · B | 3 · B |
| 7 | Médio | 7 · M | 6,3 · M | 5,25 · M | 4,2 · B | 3,5 · B |
| 8 | Médio | 8 · M | 7,2 · M | 6 · M | 4,8 · B | 4 · B |
| 9 | Médio | 9 · M | 8,1 · M | 6,75 · M | 5,4 · M | 4,5 · B |
| 10 | Médio | 10 · M | 9 · M | 7,5 · M | 6 · M | 5 · B |
| 11 | Alto | 11 · A | 9,9 · M | 8,25 · M | 6,6 · M | 5,5 · M |
| 12 | Alto | 12 · A | 10,8 · A | 9 · M | 7,2 · M | 6 · M |
| 13 | Alto | 13 · A | 11,7 · A | 9,75 · M | 7,8 · M | 6,5 · M |
| 14 | Alto | 14 · A | 12,6 · A | 10,5 · A | 8,4 · M | 7 · M |
| 15 | Alto | 15 · A | 13,5 · A | 11,25 · A | 9 · M | 7,5 · M |
| 16 | Alto | 16 · A | 14,4 · A | 12 · A | 9,6 · M | 8 · M |
| 17 | Alto | 17 · A | 15,3 · A | 12,75 · A | 10,2 · A | 8,5 · M |
| 18 | Extremo | 18 · E | 16,2 · A | 13,5 · A | 10,8 · A | 9 · M |
| 19 | Extremo | 19 · E | 17,1 · E | 14,25 · A | 11,4 · A | 9,5 · M |
| 20 | Extremo | 20 · E | 18 · E | 15 · A | 12 · A | 10 · M |
| 21 | Extremo | 21 · E | 18,9 · E | 15,75 · A | 12,6 · A | 10,5 · A |
| 22 | Extremo | 22 · E | 19,8 · E | 16,5 · A | 13,2 · A | 11 · A |
| 23 | Extremo | 23 · E | 20,7 · E | 17,25 · E | 13,8 · A | 11,5 · A |
| 24 | Extremo | 24 · E | 21,6 · E | 18 · E | 14,4 · A | 12 · A |
| 25 | Extremo | 25 · E | 22,5 · E | 18,75 · E | 15 · A | 12,5 · A |

Consequência prática no Regime B: um risco com inerente de 21 ou mais **não cai
abaixo de Alto** só com controles existentes, mesmo que sejam Fortes.

### 3.4 Avaliação

- **Regime A:** a classe do residual define a diretriz da **Tabela 11**
  (priorização, fixada pelo Comitê Gestor e não adaptável pelo gestor):

| Nível | Leitura | Diretriz |
|---|---|---|
| Extremo | Absolutamente inaceitável | Comunicar ao **Comitê Gestor**; resposta imediata; postergação só por deliberação do Comitê Gestor |
| Alto | Inaceitável | Comunicar ao Comitê Gestor; ação em prazo determinado; postergação só por manifestação escrita do dirigente máximo da unidade (Diretor nas Diretorias; Chefe de Gabinete no GABIN), com ciência ao Presidente, que pode avocar |
| Médio | Aceitável | Monitoramento específico; reduzir sem custo adicional |
| Baixo | Muito baixo | Pode haver oportunidade de assumir mais risco (avaliar custo × benefício) |

- **Regime B:** compare o **residual** com o **limite de exposição da categoria**
  na Declaração de Apetite a Riscos (Anexo III). O modelo prevê dois níveis de
  apetite:

| Apetite da categoria | Devem ser tratados |
|---|---|
| **Baixo** | Residuais **Médios, Altos e Extremos** |
| **Moderado** | Residuais **Altos e Extremos** |

O risco **fora do apetite** é **risco crítico**: entra na carteira do Plano de
Gestão de Riscos e exige pelo menos **uma medida de tratamento e um KRI** (Política,
art. 8º). Abaixo do limite, os riscos podem ser aceitos: Baixo sem providência,
Médio apenas monitorado.

> **Sem DAR aprovada**, não invente apetite. Apresente os dois cenários do modelo
> (Baixo e Moderado) e marque a condição de crítico como **pendente de DAR**. A
> própria Metodologia condiciona a deliberação do CIG ao apetite "quando este
> estiver formalizado". Altos e Extremos são tratados nos dois cenários; a
> diferença está nos Médios.

### 3.5 Tratamento

**Estratégias** (mesmos nomes nos dois regimes: Tabela 12 no A, "Tabela 8" no B):

| Estratégia | Regime A: quando | Regime B: quando | No ICMBio significa |
|---|---|---|---|
| **Mitigar** | Alto/Extremo, com custo/benefício adequado | Acima do limite de exposição, com custo/benefício adequado | Implementar controles que diminuam os efeitos |
| **Compartilhar** | Alto/Extremo, sem custo/benefício adequado | Acima do limite, sem custo/benefício adequado | Terceirização, seguro |
| **Evitar** | Alto/Extremo, controle caro demais e ninguém para compartilhar | Idem, acima do limite | **Encerrar o processo organizacional** |
| **Aceitar** | Médio ou Baixo | Abaixo do limite de exposição | Nenhum novo controle |

Use **Mitigar, Compartilhar, Evitar e Aceitar**, não "Reduzir" nem "Transferir".
A prosa da minuta (item 4.5) diz "transfiram", mas o quadro usa Compartilhar.

**Regime A, plano de tratamento** (Tabela 13, 5W2H): Estratégia · Medidas ·
Ações · Unidade responsável · Pessoa responsável · Custo previsto · Início ·
Conclusão · Situação (a ser iniciada / em andamento / parada / concluída).

**Regime B:**
- Trate **somente** os residuais acima do limite.
- Ataque as **causas** com **medidas preventivas**, para reduzir a probabilidade.
- Ataque as **consequências** com **medidas atenuantes** (contingência), para
  reduzir o impacto.
- Registre no **bow tie**: causas → barreiras de prevenção → evento → barreiras de
  mitigação → consequências.
- Medidas possíveis: controles, redesenho de processos, realocação de pessoas,
  capacitação, soluções de TI, ajuste de estrutura.
- Escolha as medidas pela quantidade e pelo nível dos riscos que cada uma reduz.
- Estrutura, campos e periodicidade do Plano serão definidos **no instrumento do
  Plano de Gestão de Riscos**. Até lá, use o formato 5W2H acima como proposta e
  diga que é proposta.

### 3.6 Plano de Gestão de Riscos (Regime B, item 4.6; Política, arts. 7º a 9º)

- A **1ª linha** (gestores de riscos) comunica os riscos críticos à CGOV.
- A **2ª linha** (**CGOV**) consolida um **Plano único** e verifica a
  **completude e a consistência metodológica**, "sem prejuízo do mérito das
  decisões de risco adotadas na 1ª linha".
- O **CIG** aprova o Plano. Ele pode ser revisto a qualquer tempo, após
  manifestação do **CTGRIC** (art. 9º).
- O Plano reúne a carteira de riscos críticos, as medidas de tratamento e os KRIs
  (art. 7º, II).

### 3.7 Monitoramento, registro e relato

**Regime A:** o monitoramento ocorre durante todo o processo, para garantir a
eficácia dos controles, analisar ocorrências, detectar mudanças e identificar
riscos emergentes. A PGRI atribui **a todos os servidores** o dever de reportar
fragilidades ao gestor do processo.

⚠️ **Remissão prejudicada:** a Portaria 975 manda apresentar os resultados na
**RAE**, prevista na PGE (Portaria 768/2020), que foi **revogada** pela Portaria
1.164/2025. Não afirme que a RAE existe. Descreva o ciclo vigente: monitoramento
trimestral das ações prioritárias no Petrvs pelas Diretorias, consolidação pela
DPAE/CGGE no Relatório Trimestral, validação pelo Comitê Gestor e Relatório Anual
de Avaliação (Portaria 1.164/2025, arts. 8º e 9º). O foro de apresentação dos
resultados de tratamento é uma lacuna real; declare-a, sem contorná-la.

**Regime B (item 4.7):**
- O monitoramento é contínuo: controles, evolução do inerente e do residual,
  execução do Plano, mudanças de contexto, riscos emergentes.
- **KRIs:** pelo menos um por risco ou grupo de riscos "críticos ou relevantes".
  Associe o KRI à causa, ao controle ou ao efeito, e defina:
  - métrica e fórmula;
  - fonte e periodicidade;
  - **meta e limite de alerta**;
  - responsável.
- Exemplo do Anexo II: "% de processos críticos com apenas 1 servidor capacitado",
  meta 0%, alerta acima de 20%, monitoramento trimestral.
- O KRI **complementa** a reavaliação periódica; não a substitui.
- O gestor comunica à CGOV: alteração relevante do residual, perda de eficácia de
  controle, risco emergente, atraso no tratamento e necessidade de revisão do
  Plano.
- A CGOV consolida e relata ao CTGRIC e ao CIG.
- Todos os agentes e colaboradores reportam fragilidades aos gestores (Política,
  art. 18).
- A periodicidade da avaliação da Política acompanha o modelo de avaliação do
  planejamento estratégico (art. 11). Isso resolve, no Regime B, a lacuna da RAE.

**Avaliação da maturidade (Regime B, item 5):** a CGOV avalia periodicamente a
efetividade, a adequação e a maturidade da gestão de riscos e relata ao CTGRIC e
ao CIG, com recomendações.

### 3.8 Estrutura e papéis

| Ator | Regime A | Regime B (Política, arts. 12 a 18) |
|---|---|---|
| Instância decisória | Comitê Gestor | CIG: define o apetite, aprova o Plano e a metodologia, decide conflitos (art. 19) |
| CTGRIC (Portaria 4.529/2025) | Consultivo e propositivo; supervisiona o Plano | Idem; manifesta-se sobre revisões do Plano e aprecia relatos de maturidade |
| CGGE | Supervisão | Supervisiona e orienta com o CTGRIC; articula com o SITAI |
| **CGOV** | Coordena com o CTGRIC; Secretaria-Executiva do CTGRIC | **2ª linha**: elabora instrumentos, avalia maturidade, orienta gestores, consolida e monitora a carteira crítica, mantém histórico, relata ao CIG e ao CTGRIC |
| AUDIT | Avaliação e consultoria | **3ª linha**: avaliação e consultoria independentes, via PAINT; apoia a CGOV nos incisos I a III |
| Gestores de riscos | Gestor do processo | **1ª linha**: lista do art. 17, §1º; devem ser capacitados |

**CTGRIC (Portaria 4.529/2025):**
- Presidido pela CGGE, com a **CGOV como Secretaria-Executiva**.
- Reuniões ordinárias trimestrais, convocadas com 5 dias úteis de antecedência.
- Presença mínima de 50%; quórum de maioria absoluta; aprovação por maioria
  simples.
- Como Secretaria-Executiva, a CGOV organiza a pauta, convoca, secretaria, minuta
  as atas, dá encaminhamento às deliberações, monitora seu cumprimento e mantém o
  acervo.
- Compete ao CTGRIC, entre outros (art. 3º): propor políticas, normas e
  metodologias; elaborar e monitorar o **Plano de Integridade**; supervisionar o
  Plano de Gestão de Riscos; assessorar o Comitê Gestor. Compõe o SITAI como
  unidade setorial.

### 3.9 Uso como subsídio de Nota Técnica de ato normativo

Quando esta skill rodar como subsídio obrigatório do roteiro da `cgov-nt-01`:

1. **Objeto:** os riscos da **aplicação do ato analisado**. Os insumos são os fluxos,
   as competências, a legística e os pontos jurídicos já levantados.
2. **Teste de Integridade:** registre uma linha por risco (sim/não e subcategoria)
   sempre que houver decisão sobre beneficiário, autorização, sanção ou atestação.
   Não use a categoria "Operacional com interface de Integridade".
3. **Controles:** considere só os previstos no ato ou comprovados nos autos,
   avaliados pelo desenho. No Regime A, sem evidência de funcionamento, nenhum
   controle fica acima de **Mediano** (no Regime B vale a regra do item 3.3:
   **Fraco**). O mesmo controle recebe a mesma eficácia em toda a matriz.
4. **Categoria Legal:** inclui não conformidade com norma superior e vício de
   competência ou de rito; declare o critério na matriz.
5. **Limites:** probabilidade e impacto são **preliminares**, a validar pelo gestor
   de riscos que a unidade proponente designar; a CGOV verifica a consistência
   metodológica e não decide o mérito do tratamento. Fato não verificado nos autos é
   premissa e fica marcado como tal. Ao comparar com respostas anteriores ou testes,
   registre as divergências em arquivo próprio.

Numere os riscos `RSC-01`, `RSC-02`… (convenção de códigos da `cgov-nt-03`).

---

## 4. FASE 3 — ENTREGA

1. **Matriz de riscos consolidada**, rotulada com o regime:
   - **Regime A:** ID · Descrição na sintaxe · Categoria · P · I · Inerente
     (produto) · Classe (máscara) · Controles · Eficácia e multiplicador ·
     Residual · Classe residual · Diretriz (Tab. 11) · Estratégia.
   - **Regime B:** ID · Objeto de GR · Descrição na sintaxe · Categoria
     (subcategoria, se Integridade) · P · I · Inerente (célula do Quadro 7) ·
     Classe · Controles e evidências · Eficácia e fator · Residual · Classe
     residual · Apetite da categoria · **Crítico?** (sim / não / pendente de DAR) ·
     Estratégia · KRI.
2. **Diagnóstico de conformidade:** cada desvio metodológico encontrado e a
   correção aplicada.
3. **Tratamento:** 5W2H (Regime A); medidas preventivas e atenuantes, bow tie e
   KRIs dos riscos críticos (Regime B).
4. **Síntese executiva** (até 5 linhas): número de riscos, distribuição por classe,
   número de críticos ou que exigem comunicação à instância decisória, pendências
   (DAR, evidências de controle) e próximos passos.
5. **Se pedido, simulação comparativa A × B** para os mesmos riscos, destacando
   onde a classe muda e por quê.

---

## 5. REGRAS TRANSVERSAIS

- **Mostre a conta.** Probabilidade e por quê → impacto e por quê → valor
  inerente (produto no A; célula no B) → classe → eficácia do controle e
  evidência → fator → residual → classe → decisão (Tab. 11 no A; apetite no B).
  Um número sem derivação não é auditável.
- Não aceite descrição de risco sem causa, evento e consequência distintos.
- O inerente desconsidera controles. O residual é o que orienta avaliação e
  tratamento.
- **Extremo** é o nível mais alto nos dois regimes. Não use "nível crítico". No
  Regime B, **"risco crítico" é um conceito**: residual fora do apetite da
  categoria. Use o termo só nesse sentido.
- Regime A: não sugira aceitar risco Alto ou Extremo. Regime B: Alto e Extremo
  ficam fora do apetite nos dois modelos do Anexo III; o tratamento dos Médios
  depende da DAR.
- "Evitar" significa encerrar o processo organizacional. Trate isso como decisão
  da instância decisória, não do analista.
- Não invente categoria, escala, fator, faixa ou apetite. Se o caso pedir algo
  fora das tabelas, declare a lacuna.
- A CGOV **coordena e verifica a consistência metodológica**. Ela não aprova a
  matriz da unidade nem decide o mérito do tratamento pela 1ª linha.
- Riscos de integridade se conectam ao SITAI (Decreto 11.529/2023) e ao Integra+
  (Portaria 253/2026).
- Ao citar minuta, cite o número do documento SEI que consta da ficha ou da pasta de
  trabalho do processo e diga que é minuta. Não a trate como norma.
- Saída em Markdown com tabelas; não gere `.docx` diretamente.

---

## 6. CASO DE CONTROLE (Anexo II da minuta)

Use este caso para conferir se a régua está aplicada corretamente.

> Devido à concentração do conhecimento do processo em um único servidor e à
> ausência de documentação formal, poderá ocorrer o afastamento do servidor
> responsável, ocasionando a paralisação do processo e impactando o alcance dos
> objetivos da unidade.

- Categoria: Operacional. P = 3 (Provável); I = 5 (Muito alto); sem controles.
- **Regime B:** célula 22 → Extremo; fator 1,0 → residual 22 → Extremo. Estratégia
  Mitigar: documentar o processo (manual, POP), em 90 dias. KRIs: % de processos
  com um só servidor capacitado (meta 0%, alerta acima de 20%); % de processos
  documentados (meta 100%, alerta abaixo de 80%); % de processos com substituto
  capacitado (meta 100%, alerta abaixo de 90%). Todos trimestrais.
- **Regime A, para comparação:** 3 × 5 = 15 → máscara Extremo; residual 15 →
  Extremo.

Se o resultado do Regime B não for 22, a matriz foi lida errado. O valor não deve
ser recalculado por fórmula.

---

## 7. QUANDO A RADAR FOR PUBLICADA

Ao saber da publicação:
1. Registre o número, a data e o link do DOU.
2. Compare o texto publicado com as minutas: Quadros 2 e 4 a 8, Tabela 8, Anexos
   II e III, e Política arts. 7º, 8º e 20.
3. Passe a usar o Regime B como padrão e trate o A como histórico. Riscos
   mapeados antes da publicação precisam ser **reavaliados** na nova régua, não
   convertidos por regra de três.
4. Sinalize as remissões que ficam desatualizadas: a Portaria 253/2026 (Integra+)
   cita a PGRI e a Portaria 975, e a Portaria 4.529/2025 (CTGRIC) cita o "Comitê
   Gestor".

---

## 8. PONTOS DE ATENÇÃO NAS MINUTAS

Úteis para nota técnica, consolidação da consulta ou parecer. Constam das minutas
da Política e da Metodologia conforme transcritas em 21/10/2026.

1. **Nome e sigla da instância decisória.** As minutas usam "Comitê Interno de
   Governança – CIG". As Portarias 4.101/2023 e 4.529/2025 chamam a instância
   interna de governança de "**Comitê Gestor do ICMBio**", e a Portaria 4.101 já
   usa "CIG" para o *Comitê Interministerial de Governança*. O Anexo III da
   própria Metodologia fala em "Comitê Gestor". É preciso harmonizar o texto ou
   alterar a Portaria 4.101.
2. A fórmula do residual remete à "**Tabela 6**", mas o instrumento é o
   **Quadro 6**. As estratégias aparecem como "**Tabela 8**", depois do Quadro 8.
3. O texto que apresenta o Quadro 5 (impacto) diz "escala de **probabilidade**".
4. LGPD citada como "Lei nº 13.709/**2013**"; o correto é **2018**.
5. O item 4.5 diz "transfiram"; a tabela diz "Compartilhar".
6. Matriz introduzida com "**sugere-se** o uso", linguagem facultativa para o
   instrumento central do cálculo.
7. KRIs obrigatórios para riscos "críticos **ou relevantes**", sem definir
   "relevante". A Política (art. 8º, §2º) exige um KRI só para os críticos.
8. A Metodologia atribui à CGGE a elaboração "**desta Política**", texto copiado
   da Política.
9. O texto chama o nível 11 de "bem menos prioritário" que o 15, mas os dois são
   **Alto** pelo Quadro 8.
10. O Anexo II lista "Evento de risco" entre as causas (erro de diagramação).
11. O Anexo III tem redação de portaria ("Art. 1º", "Anexo desta Portaria") dentro
    de um anexo.
12. A minuta não diz se o residual deve ser arredondado antes de aplicar as faixas
    (ex.: 10,2; 17,1).
13. A Política (art. 10) remete à Portaria 975/2021 "ou outra que vier a
    substituí-la". Se as duas portarias forem publicadas juntas, convém citar
    diretamente a nova Metodologia.
14. O cabeçalho da Metodologia mantém a data e o número da v1 (minuta v1, de 26/03/2026;
    o número está na pasta de trabalho do processo).
# Procedimento — análise de atos normativos pela CGOV

> **Versão 2, 07/11/2026** (etapa 6.9 do plano de implantação; D34, D44, D45 e D50). Substitui a versão 1 de 06/11/2026,
> derivada das sessões do projeto de referência (minuta de Instrução Normativa sobre Termos de Compromisso).
> Modelo para copiar nos projetos: `operacao/90_escritorio-virtual/modelos/analise-ato-normativo/INSTRUCOES-PROJETO.md`
> (publicado na pasta CGOV em `90_escritorio-virtual/modelos/analise-ato-normativo/`).

## Parte A — Instruções do projeto

O texto abaixo é o mesmo do modelo publicado em `operacao/`. Os títulos estão um nível abaixo para caber neste documento.

### 1. Dados do projeto

- **Processo SEI:** [nº] | **Apelido:** [sigla curta]
- **Ato analisado:** [tipo, objeto e nº SEI da minuta] | **Norma substituída:** [nº ou "não há"]
- **Demanda:** [despacho, data e o que pede] | **Destinatário:** [unidade] | **Proponente:** [unidade]
- **Pasta do processo e pasta de trabalho:** [conforme o `AGENTS.md` da pasta CGOV]
- **Acervo normativo:** [conforme o `AGENTS.md` da pasta CGOV] (confirmar o acesso no início)
- **Decisões específicas deste projeto:** foco da análise [só o conteúdo do ato / também o trâmite]; quesitos à PFE [sim/não]; escopo adicional; dispensas de subsídio pelo Coordenador [nenhuma / qual, data e motivo]

### 2. Finalidade

Este projeto produz uma Nota Técnica (NT) da CGOV sobre um ato normativo, com fundamento no Regimento Interno (RI, Portaria ICMBio nº 5.592/2025), art. 37. A NT se apoia em subsídios analíticos produzidos **antes** da redação. A análise é objetiva. O **foco** é decidido na triagem e registrado em "Decisões do projeto": em regra, o **conteúdo do ato** (competências, fluxos, riscos e melhoria regulatória); aspectos de trâmite do processo entram só quando o Coordenador decidir.

### 3. Regra do pipeline

**Toda análise de ato normativo passa pelas cinco ferramentas abaixo, que geram subsídios obrigatórios para a NT:**

| Ferramenta | Skill | Base de competência da CGOV | Subsídio para a NT |
|---|---|---|---|
| Modelagem de processos | `cgov-modelar-fluxo` | RI, art. 37, p.u., III | Fluxos, gargalos, desfechos sem saída |
| Auditoria de competências | `cgov-auditoria-competencias` | ⚠️ inciso a confirmar | Conflitos, lacunas, RACI corrigida |
| Técnica legislativa | `cgov-saneamento-legistica` | ⚠️ inciso a confirmar | Erros de estrutura e de redação; texto limpo |
| Análise de riscos | `cgov-gestao-riscos` | RI, art. 37, p.u., IX | Matriz de riscos do instrumento |
| Análise de impacto regulatório | `cgov-air-arr` | RI, art. 37, p.u., X | Enquadramento no Decreto nº 10.411/2020 e subsídios à AIR |

**Dispensa:** só o Coordenador dispensa uma dessas etapas, por decisão expressa registrada no `NT_ESTADO.md` com o motivo. Se o ato não tiver procedimento a modelar, registre isso como resultado da etapa, com a análise que couber. A triagem de AIR é sempre feita, mesmo quando concluir pela não incidência.

**Etapas condicionais:** `cgov-comparar-versoes` é executada quando o ato substitui norma vigente ou há versões em disputa. `cgov-nt-02` só se aplica quando houver dados brutos (consulta, indicadores). `cgov-nt-06` segue a decisão registrada na triagem.

### 4. Sequência de trabalho

Use **um chat para cada linha**, nesta ordem. Não inicie uma etapa com a anterior pendente sem autorização.

| # | Etapa | Skill | Produto (na pasta de trabalho) |
|---|---|---|---|
| 1 | Triagem e enquadramento | `cgov-nt-01-triagem` | `NT_ESTADO.md` |
| 2 | Modelagem dos fluxos | `cgov-modelar-fluxo` | `fluxo_[n]_[nome].md`, `fluxo_[n]_mermaid/` |
| 3 | Auditoria de competências | `cgov-auditoria-competencias` | `auditoria_competencias.md` |
| 4 | Cotejo com a norma anterior, se houver | `cgov-comparar-versoes` | `cotejo_norma_anterior.md` |
| 5 | Técnica legislativa | `cgov-saneamento-legistica` | `saneamento_legistica.md`, `minuta_[apelido]_texto_limpo.md` |
| 6 | Análise de riscos | `cgov-gestao-riscos` | `riscos_[apelido]_matriz.md` |
| 7 | AIR: enquadramento e subsídios | `cgov-air-arr` | `air_[apelido]_subsidios.md` |
| 8 | Dados brutos, se houver | `cgov-nt-02-instrucao` | Quadro de Achados |
| 9 | Cap. 1 — Introdução | `cgov-nt-03-introducao` | `NT_cap1_introducao.md` |
| 10 | Caps. 2 e 3 — Diagnóstico e achados | `cgov-nt-04-diagnostico` | `NT_cap2-3_diagnostico.md` |
| 11 | Cap. 4 — Propostas | `cgov-nt-05-propostas` | `NT_cap4_propostas.md` |
| 12 | Análise para a PFE, se decidido | `cgov-nt-06-quesitos-pfe` | subitem do Cap. 4 |
| 13 | Conclusão | `cgov-nt-07-conclusao` | `NT_cap5_conclusao.md` |
| 14 | Consolidação e revisão final | — | `NT_consolidada_v[n].md` e, se pedido, `.docx` |
| 15 | Apresentação, se pedida | `pptx` | `.pptx` versionado |

**Os subsídios vêm antes dos capítulos.** Riscos e AIR não são inseridos depois da NT pronta. A Introdução descreve etapas já realizadas, sem etapa "em execução".

### 5. Como executar cada subsídio

#### 5.1 Modelagem de processos
- Extraia o texto diretamente da minuta. Separe um fluxo por macroetapa: nível **micro** na etapa central e **macro** nas demais.
- Entregue, por fluxo: diagrama Mermaid validado; tabela de passos (ator, ação, dispositivo, prazo); veredito sobre se o fluxo fecha.
- Procure decisões sem critério, laços sem saída, etapas sem responsável, prazos ausentes e atores sem competência regimental aparente.
- Use `FIM_TRAVADO` onde o fluxo não fecha, sem desenhar um fluxo que "funcione" artificialmente. Fluxos com mais de 15 nós são divididos em diagramas ligados.
- Não inicie a auditoria nesta etapa: indique os alertas a aprofundar nela.

#### 5.2 Análise de riscos
- **Objeto:** riscos da aplicação do ato, tendo como insumos os fluxos, as competências, a legística e os pontos jurídicos.
- **Regime:** decida e declare antes de calcular. Verifique se a Política RADAR já foi publicada. Enquanto não for, use o Regime A (Portaria ICMBio nº 975/2021); o Regime B só entra como simulação rotulada. Nunca misture réguas numa mesma matriz.
- **Conteúdo:** sintaxe causa → evento → consequência → objetivo; varredura das categorias como lentes, inclusive ocupacional e dados pessoais; a conta completa de cada risco.
- **Teste de Integridade:** registre uma linha por risco (sim/não e subcategoria) sempre que houver decisão sobre beneficiário, autorização, sanção ou atestação. Não use "Operacional com interface de Integridade".
- **Controles:** considere só os previstos no ato ou comprovados nos autos, avaliados pelo desenho. Sem evidência de funcionamento, nenhum controle fica acima de Mediano (Regime A). O mesmo controle recebe a mesma eficácia em toda a matriz.
- **Residual fracionário (Regime A):** valor em lacuna da máscara (entre 2 e 3, entre 6 e 8 ou entre 12 e 15) vai para a classe superior, com a lacuna declarada.
- **Categoria Legal:** inclui não conformidade com norma superior e vício de competência ou de rito; declare o critério na matriz.
- **Limites:** probabilidade e impacto são **preliminares**, a validar pelo gestor de riscos que a unidade proponente designar. A CGOV verifica a consistência metodológica; não decide o mérito do tratamento. Fato não verificado nos autos é premissa e fica marcado como tal.
- **Comparação de cenários:** ao usar respostas anteriores ou testes, compare e registre as divergências em arquivo próprio.

#### 5.3 Análise de impacto regulatório
Entregue dois níveis, rotulados como **subsídio metodológico** (RI, art. 37, p.u., X). O produto não é o relatório de AIR.

**Nível 1 — Enquadramento (sempre):** na ordem do Decreto nº 10.411/2020, verifique incidência, não incidência (art. 3º, § 2º) e dispensa (art. 4º). Registre se há nos autos relatório de AIR ou decisão fundamentada de dispensa. Não confunda não incidência com dispensa.

**Nível 2 — Subsídios (padrão, salvo quando o Nível 1 afastar a obrigação):** organize pelo conteúdo do art. 6º o que a análise já permite afirmar:
- problema regulatório e árvore de causas, sem apresentar a própria norma como problema;
- afetados e impactos;
- objetivos;
- alternativas, inclusive não ação e solução não normativa;
- efeitos e riscos, a partir da matriz da etapa 6;
- critérios de comparação pela metodologia sugerida do art. 7º;
- estratégia de implementação, monitoramento e dados para a futura ARR.

Marque o que depende de dado da unidade proponente com ⚠️. Não estime custos ou número de afetados sem fonte.

**Limite:** a decisão entre AIR e dispensa, e a escolha da alternativa, cabem à unidade proponente. A NT indica o caminho e os elementos de que a decisão depende.

### 6. Como os subsídios entram na NT

- **Rastreabilidade:** cada recomendação deve permitir o caminho **alerta/conflito → achado → risco → recomendação**.
- **Cap. 1:** a metodologia descreve as etapas realizadas, incluindo os cinco subsídios, com a base de competência de cada um.
- **Cap. 2:** subseções na ordem fluxos; competências; cotejo com a norma anterior; técnica legislativa; **gestão de riscos do instrumento; análise de impacto regulatório**; pontos jurídicos. Cada subseção tem método → quadro ou diagrama com dados reais → leitura crítica. O detalhe fica no arquivo de apoio e a NT traz a síntese; não repita alertas um a um.
- **Cap. 3:** um único quadro, com até cerca de 25 linhas e achados correlatos agrupados. Eixos: Fluxo, Competência, Legística, Riscos e AIR. Risco já explicado por um achado é vinculado a ele; risco sem achado correspondente gera achado novo. Justifique se um achado ligado a risco residual Extremo não for Urgente.
- **Cap. 4:** toda recomendação deriva de achado numerado e herda sua prioridade. Não crie medidas fora da numeração. "Risco institucional se não corrigido" cita os riscos pelo código. Inclua um quadro riscos × recomendações, em que todo risco residual Alto ou Extremo tenha resposta ou justificativa. Inclua a recomendação sobre as vias do Decreto nº 10.411/2020.
- **Cap. 5:** a síntese traz achados, recomendações, distribuição dos riscos e situação da AIR, com os números exatos dos capítulos. A conclusão é assertiva e diz se o ato está apto e com quais condicionantes.

### 7. Regras de trabalho

**Portões**
- Antes de redigir, responda ao portão inicial: pré-requisitos, sumário proposto e decisões necessárias. Aguarde OK.
- Entregue em Markdown no chat, um bloco por vez (um fluxo, um tema, um grupo de subseções), e aguarde OK em cada um.
- Não grave nada antes do OK final. "Siga para o próximo" não dispensa verificar se o arquivo salvo foi alterado.
- Ao fim de cada chat: (1) grave o produto; (2) atualize "Achados e insumos consolidados" ou "Capítulos já redigidos" no `NT_ESTADO.md`, com contagens exatas; (3) marque o roteiro; (4) liste as pendências, inclusive as que afetam capítulos anteriores; (5) se pedido, redija o prompt do próximo chat conforme o item 9.
- Ajuste em capítulo anterior é listado como pendência; só é feito depois de autorizado.

**Fontes e citações**
- Cite dispositivo só depois de conferi-lo no texto da norma, no acervo normativo ou na fonte oficial. O que não foi conferido recebe ⚠️ e permanece como pendência até a verificação.
- Extraia a minuta diretamente do documento-fonte e confira datas e números SEI nos autos.
- Corrija premissas do pedido quando a fonte as contrariar e avise; não as reproduza.
- Erro encontrado num produto é corrigido em todos os arquivos afetados, com autorização e cópia de segurança.

**Limites institucionais**
- A CGOV não decide questão jurídica. Pontos jurídicos são registrados, e propostas que deles dependam vão como condicionadas ou com alternativas. Conflito com norma superior é sinalizado, não resolvido por redação.
- Os atores, prazos e competências vêm do ato analisado; o contexto de exemplo das skills (por exemplo, o PSPEADBio) não se aplica, salvo se for o objeto.
- Atualizações do RI são identificadas e tratadas pela CGOV em procedimento próprio.
- Não exponha nome ou SIAPE de servidores: use `[Nome Completo]` e `[Cargo]`. Número e data da NT ficam como `[N]` e `[data]` até serem definidos.

**Padrão de redação**
- Prosa da NT no presente do indicativo, fluida e objetiva. Tabelas só para dados comparativos ou consolidados.
- Propostas de dispositivo partem do texto limpo da legística e ficam no **futuro do presente do indicativo**, por convenção da CGOV (o Decreto nº 12.002/2024, art. 11, I, "e", admite o presente ou o futuro do presente e exige uniformidade), para que não haja duas redações do mesmo artigo. Dispositivos novos recebem numeração provisória com letra (art. 6º-A); prazos a calibrar pela proponente ficam em "[X]". Termo definido é único em todas as redações.
- Modelo SEI: `## 1. DESTINATÁRIO` a `## 4. FUNDAMENTAÇÃO/ANÁLISE TÉCNICA/PARECER`, com `### Capítulo N — …` e `#### N.1 …` dentro do item 4; conclusão em `## 5. CONCLUSÃO E PROPOSIÇÃO`, com `### 5.1 …`. Proposição em (i), (ii), (iii); encaminhamentos com destinatário em negrito.
- Correções normativas: "Redação Atual × Problema × Proposta Saneada", com fundamento e risco. Competências: RACI corrigida.

**Códigos**
Use prefixos que não colidam: alertas de fluxo `F1-01`, `F2-01`…; conflitos `C-01`; lacunas sistêmicas `LS-01`; legística `E-01` (estrutura) e `L-01` (redação); riscos `RSC-01`; pontos jurídicos `PJ-01`. Achados e recomendações são citados por número (Achado nº, Rec. nº).

### 8. Arquivos e versões

- `NT_ESTADO.md` é a fonte única de estado do processo; leia-o por inteiro no início de cada chat. O Quadro Consolidado fica no arquivo do Cap. 2-3, e o `NT_ESTADO.md` guarda a contagem e o caminho desse arquivo.
- Os produtos ficam na pasta de trabalho do processo indicada em "Dados do projeto".
- **Confirme no início de cada chat que a pasta está acessível.** Se não estiver, avise antes de trabalhar. Um arquivo só está salvo quando existe na pasta; não informe gravação sem conferir.
- Versione (`_v2`, `_v3`) e nunca sobrescreva um arquivo que possa ter edição manual. Faça cópia antes de mudanças em lote. Se o `.docx` já foi editado, altere-o pontualmente em vez de regenerá-lo.
- O padrão é Markdown. Gere `.docx`, `.xlsx` ou `.pptx` só quando pedido, e confira visualmente o resultado.

### 9. Modelo de prompt para abrir cada chat

```markdown
/[skill]

## Contexto
Processo, ato analisado, demanda e etapas já concluídas. Este chat faz só: [etapa].

## Diretrizes de foco
[Decisões do projeto que se aplicam a esta etapa]

## Leitura obrigatória antes de começar
1. `NT_ESTADO.md`, por inteiro.
2. [Produtos anteriores, indicando o que ler em cada um]
3. [Fontes normativas e páginas dos autos]

## Números a usar (conferir nos arquivos; não recalcular nem arredondar)
[Contagens de achados, recomendações e riscos]

## Portão inicial (responda antes de redigir)
[Pré-requisitos, sumário, decisões]. Aguarde meu OK.

## O que o produto deve refletir
[Conteúdo específico e achados a aprofundar]

## Regras de trabalho
[Ajustes à skill; normas a sinalizar com ⚠️]

## Fora do escopo deste chat
[Etapas seguintes; ajuste em outros capítulos vira pendência]

## Saída e gravação
Markdown no chat, em partes. Só depois do OK final: gravar [arquivo], atualizar o `NT_ESTADO.md`, marcar o roteiro e listar as pendências.
```

### 10. Conferência antes de dar a NT por concluída

- [ ] Modelagem, competências, legística, riscos e AIR executados, ou dispensa registrada pelo Coordenador.
- [ ] Toda recomendação tem achado de origem; todo achado tem recomendação ou justificativa.
- [ ] Todo risco residual Alto ou Extremo tem resposta; regime declarado; níveis indicados como preliminares.
- [ ] Contagens por eixo e prioridade recalculadas a partir dos quadros e iguais em todos os capítulos e no `NT_ESTADO.md`.
- [ ] Quadros que cruzam os mesmos dados coerentes entre si; numeração de quadros e remissões conferida.
- [ ] Nenhum ⚠️ sem pendência correspondente; dispositivos citados conferidos.
- [ ] O item 1.3 corresponde ao que a NT entrega; nenhum quadro apenas repete outro.
- [ ] Nenhum nome ou SIAPE de servidor; placeholders listados como pendência.

## Parte B — Fundamentação

### B.1 Origem

A versão 1 nasceu das dez sessões do projeto de referência (triagem, fluxos, competências, Capítulo 1, legística, Capítulos 2 a 5, consolidação, apresentação e riscos). As lições principais foram:

- **riscos antes da redação** — no projeto de referência, a análise de riscos veio depois da NT pronta e obrigou a renumerar quadros e reescrever parágrafos;
- **AIR mais profunda** — além do enquadramento, o Nível 2 gera subsídios às alternativas e aos impactos;
- **subsídios como regra** — modelagem, competências, legística, riscos e AIR passam de opção a etapas obrigatórias, com dispensa só pelo Coordenador.

### B.2 Decisões incorporadas na versão 2

| Decisão | Conteúdo |
|---|---|
| D44 (07/11/2026) | AIR Nível 2 como padrão; competências e legística obrigatórias (cinco subsídios); foco decidido por projeto; dispositivos propostos no futuro do presente; residual em lacuna da máscara na classe superior; pasta de trabalho com texto neutro |
| D45 (07/11/2026) | Ampliação da `cgov-nt-06` (consulta jurídica facultativa) e da `cgov-modelar-fluxo` (BPMN → tabela de atividades) |
| D50 (07/11/2026) | Correção das 8 divergências entre skills apontadas na versão 1 (ver plano de implantação, etapa 6.9) |

### B.3 Pendências

- ⚠️ Inciso do Art. 37 que fundamenta a auditoria de competências e a técnica legislativa.
- ⚠️ Texto da Portaria Conjunta nº 3/2021 no acervo normativo (consulta facultativa à PFE).
- Piloto num ato normativo real (Fase 11).

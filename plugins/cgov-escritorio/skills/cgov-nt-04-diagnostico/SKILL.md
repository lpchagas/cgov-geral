---
name: cgov-nt-04-diagnostico
description: >
  Quarta etapa da suíte canônica cgov-nt: redige os Capítulos 2 e 3 (Diagnóstico
  e Quadro Consolidado de Achados) de QUALQUER Nota Técnica da CGOV/ICMBio —
  análises normativas, consultas internas, análises de governança institucional
  ou de gestão de riscos — convertendo os achados de `cgov-nt-02` e/ou das
  skills analíticas normativas (cgov-comparar-versoes, cgov-modelar-fluxo,
  cgov-auditoria-competencias) em texto analítico, tabelas e diagramas.
  Use ao invocar /cgov-nt-04, "capítulo de diagnóstico", "capítulos 2 e 3",
  "redigir a análise técnica", "quadro consolidado de achados", ou qualquer
  pedido de transformar achados já levantados em texto de Nota Técnica.
  Requer `NT_ESTADO.md` (na pasta de trabalho do processo) com
  achados já consolidados (por cgov-nt-02 e/ou pelas skills analíticas
  normativas); se não houver achados registrados, redirecione para a skill de
  instrução/diagnóstico correspondente primeiro.
---

# cgov-nt-04 — Capítulos 2 e 3: Diagnóstico e Quadro Consolidado de Achados

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
2. Leia `NT_ESTADO.md` — em especial a seção "Achados e insumos consolidados".
3. **Pré-requisito de conteúdo:** se essa seção estiver vazia ou incompleta,
   interrompa e informe: "Os achados de [cgov-nt-02 / diagnóstico normativo]
   ainda não constam do NT_ESTADO.md. Execute essa etapa antes de prosseguir."
4. Aplique o **Padrão de Redação CGOV** definido em `cgov-nt-03` (prosa no
   presente do indicativo, remissões completas, numeração decimal, proibição de
   invenção normativa; `.docx` só o da NT, alimentado na PÓS-EXECUÇÃO).

## FASE 1 — SELEÇÃO DA ESTRUTURA DE DIAGNÓSTICO

O conteúdo do Capítulo 2 varia conforme a natureza do achado. Use apenas as
subseções pertinentes ao caso concreto (não force um template único):

| Natureza do achado | Subseção sugerida | Elemento visual |
|---|---|---|
| Dados quantitativos/qualitativos de consulta | Análise das respostas fechadas / abertas | Tabelas de frequência + caixas de "Ponto Sensível" |
| Diagnóstico normativo (remissões, competências) | Análise técnico-normativa | Tabela comparativa "Redação × Problema" |
| Viabilidade operacional de fluxo/processo | Viabilidade operacional | Diagrama Mermaid (BPMN simplificado, ```mermaid```) |
| Sobreposição de competências | Auditoria de competências | Matriz RACI |
| Governança institucional/organizacional | Sobreposição de instâncias | Tabela comparativa de atribuições |
| Gestão de riscos | Gestão de riscos do instrumento | Matriz de riscos (Causa → Evento → Consequência → Objetivo), com o regime declarado (`cgov-gestao-riscos`) |
| Impacto regulatório | Análise de impacto regulatório | Enquadramento no Decreto nº 10.411/2020 e subsídios do art. 6º (`cgov-air-arr`) |

**Em análise de ato normativo**, as subseções do Capítulo 2 seguem esta ordem:
fluxos; competências; cotejo com a norma anterior; técnica legislativa; gestão de
riscos do instrumento; análise de impacto regulatório; pontos jurídicos. Cada uma
tem método → quadro ou diagrama com dados reais → leitura crítica. O detalhe fica
no produto de cada subsídio; a NT traz a síntese, sem repetir alertas um a um.

## FASE 2 — REDAÇÃO

Para cada subseção selecionada: (1) um parágrafo introdutório em prosa
explicando o método e o escopo da análise; (2) a tabela/diagrama com os dados
efetivamente levantados (nunca com placeholders fictícios); (3) um parágrafo de
leitura crítica dos resultados (o que os dados revelam, não apenas o que dizem
literalmente).

## FORMATO DE SAÍDA

> Numeração reiniciada por capítulo (`#### 2.1`, `#### 2.2`...), conforme
> padrão validado por piloto contra NT real da CGOV — ver `cgov-nt-03`.

```
### Capítulo 2 — Análise Técnica / Diagnóstico

#### 2.1. [Subseção 1 — conforme Fase 1]
[prosa introdutória]

[tabela ou diagrama mermaid]

[leitura crítica]

#### 2.2. [Subseção 2, se houver]
[...]

---

### Capítulo 3 — Quadro Consolidado de Achados

| Nº | Item/Dispositivo/Tema | Eixo | Natureza do Problema/Achado | Impacto | Prioridade |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | Urgente / Prioritário / Desejável |
```

**Regras do Quadro Consolidado:**
- um único quadro, com até cerca de 25 linhas e achados correlatos agrupados;
- em análise de ato normativo, eixos **Fluxo, Competência, Legística, Riscos e AIR**;
- risco já explicado por um achado é vinculado a ele; risco sem achado
  correspondente gera achado novo;
- justifique se um achado ligado a risco residual Extremo não for Urgente.

**Critério de priorização (aplicar de forma consistente a todos os achados):**
- **Urgente:** risco jurídico, operacional ou institucional iminente, ou
  achado que inviabiliza a continuidade do processo sem correção.
- **Prioritário:** relevante para a qualidade/eficácia do produto final, mas
  não bloqueante.
- **Desejável:** melhoria incremental, sem urgência.

## REGRA ESPECIAL — DIAGRAMAS

Diagramas Mermaid só devem ser incluídos quando o achado envolver um fluxo
processual com mais de uma etapa/ator. Não force um diagrama para achados
puramente quantitativos ou de mérito jurídico — nesses casos, a tabela basta.

## PÓS-EXECUÇÃO — .docx DE REVISÃO (v2.N-<subsídio>)

A CGOV revisa a NT no Word. Por isso esta etapa termina com uma **nova versão do `.docx` da NT**,
que acumula os capítulos já redigidos e preserva as edições feitas pelo revisor na versão anterior.
O Markdown continua sendo a entrega no chat e a fonte do capítulo. O gerador é o
`montar_nt_docx.py` das **Ferramentas do Escritório** (caminho no `AGENTS.md`); ele aplica o padrão
gráfico das NTs da CGOV e nunca sobrescreve arquivo.

**Incrementos da fase 2.** O diagnóstico costuma ser escrito por subsídio analítico; cada
subsídio entregue vira um incremento, para o revisor acompanhar o capítulo crescer:
- primeiro incremento: `.md` com `### Capítulo 2 — …` e a primeira subseção → `--versao 2.1 --etapa fluxo`
  (ou o subsídio que vier primeiro);
- incrementos seguintes: `.md` que começa por `#### 2.N.` → `--versao 2.2 --etapa competencias`,
  `2.3 legistica`, `riscos`, `air`, `cotejo`, `consulta`… (o gerador encaixa o subitem no fim do Capítulo 2);
- último incremento: `.md` com `### Capítulo 3 — Quadro Consolidado de Achados` → `--etapa achados`.
Se o usuário pedir os Capítulos 2 e 3 de uma vez, um só `.md` → `--versao 2 --etapa diagnostico`.
Nos passos abaixo, `2.N` e `<subsídio>` são os valores do incremento em curso.

1. **Antes de numerar quadros e figuras**, rode
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" --listar --pasta "<pasta de trabalho>"`.
   A lista mostra as versões existentes e a última linha dá o próximo Quadro nº e a próxima Figura nº:
   numere o capítulo a partir deles.
2. **Grave o capítulo** na pasta de trabalho como `NT_<apelido>_v2.N-<subsídio>.md` (`<apelido>` é o final do nome da
   pasta do processo, `SEI_…_<apelido>`): o mesmo texto entregue no chat, com legenda
   `**Quadro N — título**` antes de cada tabela e `Fonte: …` depois; pendências ficam fora do arquivo
   (vão para a resposta e para o `NT_ESTADO.md`).
3. **Simule e gere:**
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" "<pasta de trabalho>/NT_<apelido>_v2.N-<subsídio>.md" --versao 2.N --etapa <subsídio> --simular`.
   Se o relatório (JSON) não trouxer erro, rode o mesmo comando sem `--simular`.
4. **Relate ao usuário**, em até cinco linhas: arquivo gerado, versão usada como base, avisos do
   relatório (numeração de quadros ou figuras, figura não inserida, tabela sem legenda, trecho
   excluído) e quantos ⚠ restam no texto.
5. **Registre** no `NT_ESTADO.md`, seção "Versões do .docx" (crie-a se não existir):
   `v2.N-<subsídio> — NT_<apelido>_v2.N-<subsídio>.docx — [data] — base: [versão anterior ou "novo"] — [n] aviso(s)`.

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

O Quadro Consolidado fica no produto do Cap. 2-3 (na pasta de trabalho do
processo, quando gravado); o `NT_ESTADO.md` guarda a contagem e o caminho desse
arquivo. Acrescente ao `NT_ESTADO.md` (na pasta localizada na Pré-execução):
`Cap. 2-3 — Diagnóstico: concluído em [data]. N achados consolidados (X
Urgentes, Y Prioritários, Z Desejáveis).` Essa contagem será reaproveitada
literalmente pela síntese de `cgov-nt-07` — mantenha-a precisa.

## ENCADEAMENTO

```
[cgov-nt-02 e/ou skills analíticas normativas] → /cgov-nt-04 (esta skill) → /cgov-nt-05 ou /cgov-nt-06
```

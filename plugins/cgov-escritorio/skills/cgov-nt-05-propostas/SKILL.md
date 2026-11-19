---
name: cgov-nt-05-propostas
description: >
  Quinta etapa (opcional, conforme triagem) da suíte canônica cgov-nt: redige
  o Capítulo 4 — Propostas de Ajuste e Recomendações — de QUALQUER Nota Técnica
  da CGOV/ICMBio, a partir do Quadro Consolidado de Achados produzido por
  cgov-nt-04. Gera recomendações numeradas com fundamento normativo, redação
  saneada (quando aplicável) e quadro de prioridades. Use ao invocar
  /cgov-nt-05, "propostas de ajuste", "capítulo 4", "recomendações da NT",
  "redação saneada", "matriz de consolidação das propostas". Se a NT for
  puramente descritiva/de status e não comportar recomendações (ver
  NT_ESTADO.md, Tipo D), esta skill pode ser dispensada — confirme com o
  usuário antes de pular a etapa.
---

# cgov-nt-05 — Capítulo 4: Propostas de Ajuste e Recomendações

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
2. Leia o Quadro Consolidado de Achados (Capítulo 3, produzido por `cgov-nt-04`)
   **no produto do Cap. 2-3**, cujo caminho está no `NT_ESTADO.md`; o
   `NT_ESTADO.md` traz só a contagem. Se o produto não estiver gravado, peça o
   Capítulo 3 ao usuário.
3. **Pré-requisito de conteúdo:** cada recomendação desta skill deve derivar de
   um achado numerado do Capítulo 3. Não introduza recomendações "novas" sem
   lastro em achado registrado — se identificar uma questão relevante não
   capturada antes, retorne a `cgov-nt-04` para registrá-la como achado primeiro.
4. Aplique o Padrão de Redação CGOV (`cgov-nt-03`).

## FASE 1 — CLASSIFICAÇÃO DO TIPO DE RECOMENDAÇÃO

Para cada achado do Capítulo 3, identifique o tipo de recomendação cabível —
isso determina o formato da proposta na Fase 2:

- **Correção normativa/legística:** aplica-se quando o achado é um problema de
  redação, remissão ou técnica legislativa em minuta de ato normativo → use o
  formato "Redação Atual × Problema × Proposta Saneada", fundamentado no
  Decreto nº 12.002/2024 e na LC nº 95/1998.
- **Ajuste organizacional/de competências:** aplica-se a sobreposições ou
  lacunas de responsabilidade → proponha redistribuição de atribuições ou
  matriz RACI corrigida.
- **Ação de gestão/processo:** aplica-se a achados quantitativos/qualitativos
  de consultas internas ou de gestão de riscos → proponha ação de mitigação,
  ajuste procedimental ou encaminhamento de estudo complementar.
- **Recomendação de governança institucional:** aplica-se a temas de arranjo
  organizacional, comitês ou alinhamento estratégico → proponha diretriz ou
  condicionante para a instituição da proposta analisada.

## FASE 2 — REDAÇÃO

> Numeração reiniciada por capítulo (`#### 4.1`, `#### 4.2`...), conforme
> padrão validado por piloto contra NT real da CGOV — ver `cgov-nt-03`. A
> análise para a PFE (`cgov-nt-06`), quando necessária, é publicada como
> subitem deste mesmo Capítulo 4 (ex.: item 4.4) na prática observada da CGOV,
> não como um capítulo numerado à parte — ajuste a numeração conforme o
> número final de subitens deste capítulo.

```
### Capítulo 4 — Propostas de Ajustes e Recomendações

#### 4.1. Diretrizes gerais das propostas
[parágrafo: base metodológica das propostas e sua relação com o Capítulo 3]

#### 4.2. Recomendações

**Recomendação nº 1 — [Título] (achado nº [X] do Quadro Consolidado)**

[texto analítico: problema e justificativa técnica]

[Se correção normativa:]
| Redação Atual | Problema Identificado | Proposta Saneada |
|---|---|---|
| "..." | ... | "..." |

**Fundamento normativo:** [norma e artigo — sem invenção]
**Risco institucional se não corrigido:** [consequência prática; cite os riscos pelo código, ex.: RSC-03]

---
[repetir para cada recomendação numerada]
---

**Tabela — Matriz de Consolidação das Propostas**
| Item | Achado nº | Recomendação (síntese) |
|---|---|---|

**Quadro de Prioridades**
| Prioridade | Nº | Recomendação | Justificativa |
|---|---|---|---|
| URGENTE | | | |
| PRIORITÁRIO | | | |
| DESEJÁVEL | | | |

[Em análise de ato normativo:]
**Quadro — Riscos × Recomendações**
| Risco (código) | Residual | Recomendação(ões) | Resposta ou justificativa |
|---|---|---|---|
```

Em análise de ato normativo: todo risco residual **Alto ou Extremo** tem
resposta ou justificativa no quadro Riscos × Recomendações, e há uma
recomendação sobre as vias do Decreto nº 10.411/2020 (AIR, dispensa ou não
incidência), indicando os elementos de que a decisão da unidade proponente
depende. Não crie providências fora da numeração das recomendações.

As prioridades devem ser **herdadas** das prioridades já atribuídas aos
achados correspondentes no Capítulo 3 (`cgov-nt-04`) — não reclassifique sem
justificar a divergência.

## REGRA ESPECIAL — RECOMENDAÇÃO SEM SOLUÇÃO CLARA

Se um achado urgente não tiver solução técnica evidente, não force uma
recomendação artificial. Registre-o como "Recomendação nº [N] — Necessidade de
estudo complementar" e explique o que precisa ser levantado antes de uma
proposta concreta.

## PÓS-EXECUÇÃO — .docx DE REVISÃO (v3-propostas)

A CGOV revisa a NT no Word. Por isso esta etapa termina com uma **nova versão do `.docx` da NT**,
que acumula os capítulos já redigidos e preserva as edições feitas pelo revisor na versão anterior.
O Markdown continua sendo a entrega no chat e a fonte do capítulo. O gerador é o
`montar_nt_docx.py` das **Ferramentas do Escritório** (caminho no `AGENTS.md`); ele aplica o padrão
gráfico das NTs da CGOV e nunca sobrescreve arquivo.

O `.md` começa por `### Capítulo 4 — Propostas de Ajustes e Recomendações`. Cada recomendação
abre com a linha `**Recomendação nº N — título (achado nº X do Quadro Consolidado)** · *Prioridade*`;
`**Fundamento normativo:**` e `**Risco institucional se não corrigido:**` ficam em linhas próprias
(o gerador os põe em caixas) e as tabelas "Matriz de Consolidação", "Quadro de Prioridades" e
"Riscos × Recomendações" recebem legenda numerada `**Quadro N — …**`.

1. **Antes de numerar quadros e figuras**, rode
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" --listar --pasta "<pasta de trabalho>"`.
   A lista mostra as versões existentes e a última linha dá o próximo Quadro nº e a próxima Figura nº:
   numere o capítulo a partir deles.
2. **Grave o capítulo** na pasta de trabalho como `NT_<apelido>_v3-propostas.md` (`<apelido>` é o final do nome da
   pasta do processo, `SEI_…_<apelido>`): o mesmo texto entregue no chat, com legenda
   `**Quadro N — título**` antes de cada tabela e `Fonte: …` depois; pendências ficam fora do arquivo
   (vão para a resposta e para o `NT_ESTADO.md`).
3. **Simule e gere:**
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" "<pasta de trabalho>/NT_<apelido>_v3-propostas.md" --versao 3 --etapa propostas --simular`.
   Se o relatório (JSON) não trouxer erro, rode o mesmo comando sem `--simular`.
4. **Relate ao usuário**, em até cinco linhas: arquivo gerado, versão usada como base, avisos do
   relatório (numeração de quadros ou figuras, figura não inserida, tabela sem legenda, trecho
   excluído) e quantos ⚠ restam no texto.
5. **Registre** no `NT_ESTADO.md`, seção "Versões do .docx" (crie-a se não existir):
   `v3-propostas — NT_<apelido>_v3-propostas.docx — [data] — base: [versão anterior ou "novo"] — [n] aviso(s)`.

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

Acrescente ao `NT_ESTADO.md` (na subpasta localizada na Pré-execução): `Cap. 4
— Propostas: concluído em [data]. N recomendações formuladas.`

## ENCADEAMENTO

```
/cgov-nt-04 → /cgov-nt-05 (esta skill, se aplicável) → /cgov-nt-06 (se aplicável) → /cgov-nt-07
```

---
name: cgov-nt-07-conclusao
description: >
  Sétima e última etapa da suíte canônica cgov-nt: redige o Capítulo 5 —
  Conclusão, Proposição e Encaminhamentos — de QUALQUER Nota Técnica da
  CGOV/ICMBio, com síntese diagnóstica quantificada, posicionamento técnico
  assertivo, proposição formal e bloco de assinaturas. Use ao invocar
  /cgov-nt-07, "conclusão da NT", "capítulo 5", "encaminhamentos",
  "fechar a nota técnica", "finalizar o parecer". Requer que todos os
  capítulos anteriores aplicáveis (cgov-nt-03 a cgov-nt-06, conforme o roteiro
  definido em `NT_ESTADO.md`, na pasta de trabalho do processo) já
  estejam concluídos.
---

# cgov-nt-07 — Capítulo 5: Conclusão, Proposição e Encaminhamentos

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
2. Leia `NT_ESTADO.md` por completo — roteiro de execução, achados
   consolidados (com contagem por prioridade) e recomendações formuladas.
3. **Pré-requisito de conteúdo:** confira, no roteiro do `NT_ESTADO.md`, que
   todas as etapas marcadas como "necessárias" na triagem (`cgov-nt-01`)
   estão de fato concluídas. Se alguma etapa obrigatória estiver pendente,
   interrompa e liste o que falta antes de redigir a conclusão — **a
   conclusão nunca deve ser redigida antes do Quadro Consolidado de Achados**.
4. A conclusão deve ser **assertiva e propositiva**, não uma reprodução do que
   já foi dito. Deve posicionar-se claramente sobre o mérito da análise.
5. Aplique o Padrão de Redação CGOV (`cgov-nt-03`).

## FORMATO DE SAÍDA

> A conclusão é a Seção 5 do modelo SEI, fora da Seção 4: `## 5. CONCLUSÃO E
> PROPOSIÇÃO`, com `### 5.1`, `### 5.2`… (os capítulos 1 a 4 ficam na Seção 4,
> com `### Capítulo N` e `#### N.1`; ver `cgov-nt-03`).
> Formato validado por piloto contra NT real protocolada (nº 20/2026/CGOV):
> capítulo com numeração reiniciada (`### 5.1`, não `#### 5.1`), proposição em
> algarismos romanos minúsculos entre parênteses — (i), (ii), (iii) — e
> encaminhamentos em lista com o destinatário em negrito, não em algarismos
> romanos maiúsculos. Este padrão substitui o que constava de versões
> anteriores desta skill.

```
## 5. CONCLUSÃO E PROPOSIÇÃO

### 5.1. Síntese diagnóstica.
[Um a dois parágrafos: total de achados, distribuição por eixo temático e por
prioridade (Urgente/Prioritário/Desejável) — usar os números exatos
registrados em NT_ESTADO.md pelo Capítulo 3. Tom objetivo e quantificado,
citando percentuais/índices relevantes já calculados nos capítulos anteriores.
Em análise de ato normativo, inclua também o número de recomendações, a
distribuição dos riscos por nível residual e a situação da AIR.]

### 5.2. Conclusão técnica.
[Posicionamento assertivo, adaptado à natureza do objeto analisado:
- Se minuta normativa: apta ou não para publicação, com quais condicionantes?
- Se consulta interna: quais direcionamentos a alta gestão deve adotar, e a
  quais riscos institucionais a manutenção do texto atual expõe a Autarquia?
- Se governança institucional: a proposta está em conformidade, não
  conformidade, ou conformidade condicionada?
1 a 2 parágrafos em prosa direta, sem reabrir a análise já feita nos capítulos
anteriores.]

### 5.3. Proposição.
Ante o exposto, esta Coordenação de Governança **PROPÕE**:

(i) [ação 1, com referência à recomendação/tabela do Capítulo 4, se aplicável];

(ii) [ação 2]; e

(iii) [ação 3].

### 5.4. Encaminhamentos.

- À **[destinatário 1]**: [ação, objeto, referência aos itens desta NT];
- À **[destinatário 2]**: [ação, objeto]; e
- Ao **Processo SEI nº [número]**: juntada da presente Nota Técnica para
  instrução dos autos.

---

À consideração superior.

[Nome Completo]
[Cargo] — CGOV/ICMBio

[Nome Completo]
Coordenador(a) de Governança — CGOV/ICMBio

[Nome Completo]
Coordenador(a)-Geral de Governança e Gestão Estratégica — CGGE/ICMBio
```

**Regras de redação obrigatórias:**
- Síntese quantificada: usar os números reais de achados/prioridades — nunca
  aproximar ou arredondar sem indicar que é aproximação.
- Proposição em algarismos romanos minúsculos entre parênteses — (i), (ii),
  (iii); encaminhamentos em lista com o nome do destinatário em negrito.
- Bloco de assinaturas sem matrícula SIAPE (preenchida manualmente no SEI).
- `.docx` só o da NT, alimentado na PÓS-EXECUÇÃO (versão `v5-conclusao`).

## REGRA ESPECIAL — CONCLUSÃO DIVIDIDA

Se os achados apontarem em direções conflitantes (ex.: parte da equipe técnica
recomenda uma solução e os dados de consulta apontam outra), não force um
consenso artificial na Seção 5.2: explicite a divergência e proponha, na
Seção 5.3, que a decisão final seja submetida à instância superior com as
duas alternativas tecnicamente descritas.

## PÓS-EXECUÇÃO — .docx DE REVISÃO (v5-conclusao)

A CGOV revisa a NT no Word. Por isso esta etapa termina com uma **nova versão do `.docx` da NT**,
que acumula os capítulos já redigidos e preserva as edições feitas pelo revisor na versão anterior.
O Markdown continua sendo a entrega no chat e a fonte do capítulo. O gerador é o
`montar_nt_docx.py` das **Ferramentas do Escritório** (caminho no `AGENTS.md`); ele aplica o padrão
gráfico das NTs da CGOV e nunca sobrescreve arquivo.

O `.md` começa por `## 5. CONCLUSÃO E PROPOSIÇÃO` e termina no bloco de assinaturas ("À
consideração superior." e, em linhas consecutivas, nome e cargo de cada signatário). A
proposição usa um parágrafo por item, iniciado por `(i)`, `(ii)`…

1. **Antes de numerar quadros e figuras**, rode
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" --listar --pasta "<pasta de trabalho>"`.
   A lista mostra as versões existentes e a última linha dá o próximo Quadro nº e a próxima Figura nº:
   numere o capítulo a partir deles.
2. **Grave o capítulo** na pasta de trabalho como `NT_<apelido>_v5-conclusao.md` (`<apelido>` é o final do nome da
   pasta do processo, `SEI_…_<apelido>`): o mesmo texto entregue no chat, com legenda
   `**Quadro N — título**` antes de cada tabela e `Fonte: …` depois; pendências ficam fora do arquivo
   (vão para a resposta e para o `NT_ESTADO.md`).
3. **Simule e gere:**
   `python "<Ferramentas do Escritório>/montar_nt_docx.py" "<pasta de trabalho>/NT_<apelido>_v5-conclusao.md" --versao 5 --etapa conclusao --simular`.
   Se o relatório (JSON) não trouxer erro, rode o mesmo comando sem `--simular`.
4. **Relate ao usuário**, em até cinco linhas: arquivo gerado, versão usada como base, avisos do
   relatório (numeração de quadros ou figuras, figura não inserida, tabela sem legenda, trecho
   excluído) e quantos ⚠ restam no texto.
5. **Registre** no `NT_ESTADO.md`, seção "Versões do .docx" (crie-a se não existir):
   `v5-conclusao — NT_<apelido>_v5-conclusao.docx — [data] — base: [versão anterior ou "novo"] — [n] aviso(s)`.

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
- **Fecho da NT**: depois de gerar a `v5-conclusao`, peça ao usuário que revise essa versão
  (é o documento consolidado) e lembre que o Sumário e as listas se atualizam ao abrir no Word
  (aceitar a atualização dos campos). Revisões posteriores seguem como `v5.1-revisao`, `v5.2-…`.

## REGISTRO NO NT_ESTADO.md

Atualize `NT_ESTADO.md` (na subpasta localizada na Pré-execução): `NT
concluída em [data]. Pronta para revisão final e tramitação no SEI.` A versão de
revisão final é a última do `.docx` registrada em "Versões do .docx".

## ENCADEAMENTO

```
/cgov-nt-04 → [/cgov-nt-05] → [/cgov-nt-06] → /cgov-nt-07 (esta skill — etapa final)
```

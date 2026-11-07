---
name: cgov-gestao-acervo
description: >
  Organiza a pasta de trabalho da CGOV/ICMBio conforme o LEIA-ME.md e o AGENTS.md da raiz: triagem da caixa de
  entrada (TRIAR_ENTRADA), criação da pasta de processo SEI a partir do modelo (NOVO_PROCESSO), preenchimento e
  atualização da ficha PROCESSO.md (ATUALIZAR_FICHA), geração dos _INDICE.md (ATUALIZAR_INDICES) e envio para o
  arquivo de versões superadas e processos concluídos (ARQUIVAR). Use ao ouvir "classifique o que está em
  00_entrada", "onde salvo este arquivo", "abra o processo", "crie a pasta do processo", "atualize a ficha do
  processo", "atualize os índices", "arquive o processo", "mova as versões antigas". Nunca exclui arquivos, nunca
  sobrescreve, e só move em lote depois de mostrar a lista e receber confirmação. Não redige Nota Técnica (use
  cgov-nt-01-triagem) nem analisa o mérito de processo (use cgov-triagem-processo-sei).
---

# cgov-gestao-acervo — Gestão do acervo da pasta CGOV

Esta skill cuida da **organização** da pasta de trabalho da CGOV: onde cada arquivo fica, como se chama, e se
as fichas e os índices estão em dia. Ela não altera o conteúdo de documentos de processos, normas ou Notas
Técnicas: apenas move, renomeia, cria pastas, fichas e índices.

## ANTES DE QUALQUER MODO

1. **Leia o `LEIA-ME.md` e o `AGENTS.md` da raiz da pasta** (mapa, tabela "Onde salvo?", padrões de nome,
   caminhos por papel e obrigações). Esta skill cita **papéis** (caixa de entrada, pasta de processos, pasta do
   processo, série de Notas Técnicas, acervo normativo, arquivo, quarentena); os caminhos concretos estão no
   `AGENTS.md` (ADR-006). Se ele não estiver acessível, peça ao usuário que conecte a pasta antes de continuar.
2. **Regras invioláveis:**
   - **nunca exclua:** o que não serve vai para a quarentena do arquivo (`_a-excluir_<AAAA-MM-DD>/`), revista em
     30 dias e excluída só com confirmação;
   - **nunca sobrescreva:** se o destino já tiver um arquivo de mesmo nome, compare-os; se forem diferentes,
     proponha o sufixo de versão (`_v2`, `_v3`);
   - **lote só com lista e confirmação:** antes de mover ou renomear mais de um item, mostre a tabela completa
     (origem → destino) e espere o OK explícito;
   - **confira a integridade:** registre o SHA-256 de cada arquivo antes de mover e confira-o no destino;
   - **sem dados pessoais:** nenhum nome, matrícula, SIAPE, CPF ou e-mail de servidor em fichas e índices;
   - **não invente:** número SEI, data, unidade ou inciso que não esteja nos autos ou não tenha sido informado
     fica como ⚠️ no campo, nunca como valor plausível.
3. Ao final de cada modo, liste o que foi feito (com caminhos) e as pendências.

## MODO 1 — TRIAR_ENTRADA

1. Liste os arquivos da caixa de entrada com nome, tamanho e data de modificação.
2. Para cada arquivo, proponha um destino pela tabela "Onde salvo?" do `LEIA-ME.md`:

| Arquivo | O que parece ser | Destino proposto | Nome padronizado | Motivo | Confiança |
|---|---|---|---|---|---|
| … | documento do SEI / rascunho / NT assinada / norma publicada / material de colegiado / projeto | … | … | o que no nome ou no conteúdo indica o destino | alta / média / baixa |

3. Abra o arquivo só o necessário para identificá-lo (cabeçalho, número SEI, assinatura). Se o número SEI
   indicar um processo sem pasta, proponha o MODO 2.
4. Confiança **baixa**: não proponha destino; pergunte ao usuário. Arquivos com mais de 7 dias na caixa de
   entrada são sinalizados.
5. Só mova depois do OK. Norma publicada vai para o acervo normativo e é sinalizada para transcrição
   (`cgov-transcrever-normativos`); NT assinada vai para a série de Notas Técnicas no ano correspondente.

## MODO 2 — NOVO_PROCESSO

1. Dados mínimos: número SEI completo (`<órgão>.<número>/<ano>-<dígito>`) e um **apelido curto** (minúsculas,
   hífen, sem acento). Se faltar o apelido, proponha um a partir do assunto e peça confirmação.
2. Monte o nome pela convenção do `LEIA-ME.md` (`SEI_<órgão>.<número>_<ano>-<dígito>_<apelido>`; "_" no lugar
   da barra) e confira se já existe pasta para o mesmo número (compare pelo número, não pelo apelido).
3. Crie a pasta e as subpastas previstas no `AGENTS.md` (obrigação 1): documentos do SEI, trabalho, referências
   e produtos.
4. Copie o modelo da ficha `PROCESSO.md` (modelos do Escritório) e preencha o *frontmatter*: `sei`, `apelido`,
   `titulo`, `inciso_art37` (só se o enquadramento estiver confirmado), `situacao: em-andamento`,
   `unidade_demandante`, `aberto_em` e `atualizado_em`. Campo sem informação confirmada recebe ⚠️.
5. Ofereça rodar o MODO 4 para atualizar o índice de processos.

## MODO 3 — ATUALIZAR_FICHA

Atualize, na ficha `PROCESSO.md` do processo:
- `situacao` (`em-andamento`, `aguardando-terceiros`, `concluido` ou `arquivado`) e `atualizado_em`;
- uma linha na tabela "Andamento" (data, evento, documento SEI);
- `notas_tecnicas` e a seção "Produtos da CGOV", quando houver NT assinada;
- "Pendências", marcando as resolvidas.

Não registre quem fez o trabalho; se o usuário pedir, explique a regra de LGPD do `LEIA-ME.md` e registre o
papel (ex.: "equipe da CGOV"), não o nome.

## MODO 4 — ATUALIZAR_INDICES

Os `_INDICE.md` são **gerados** a partir das fichas e dos nomes de arquivo (obrigação 6 do `AGENTS.md`): nunca os
edite à mão.

1. Rode o gerador publicado nas ferramentas do Escritório (caminho no `AGENTS.md`), primeiro numa pasta de saída
   temporária (`--saida`), e mostre a diferença para os índices atuais.
2. Com o OK, rode-o sobre a raiz (`--indices`, e `--fichas` só se o usuário pedir fichas novas).
3. Se o gerador não estiver acessível ou falhar, não monte o índice à mão: registre a pendência nas pendências
   do Escritório e informe o usuário.

## MODO 5 — ARQUIVAR

- **Versão superada** de um arquivo (há versão mais recente em uso): vai para as versões anteriores do arquivo,
  mantendo o nome.
- **Processo concluído:** a pasta **inteira** vai para os processos encerrados do arquivo; antes, a ficha recebe
  `situacao: arquivado`, `atualizado_em` e uma linha final em "Andamento".
- **Descarte:** só para a quarentena com a data do dia; nunca exclusão direta.

Mostre a lista (origem → destino), espere a confirmação, mova, confira o SHA-256 e ofereça o MODO 4.

## ENCADEAMENTO

- Arquivo de norma publicada → `cgov-transcrever-normativos`.
- Processo que precisa de análise → `cgov-triagem-processo-sei` (triagem) ou `cgov-nt-01-triagem` (Nota Técnica).
- Problema com a estrutura da pasta ou com esta skill → pendências do Escritório (caminho no `AGENTS.md`).

---
name: cgov-secretaria-colegiados
description: >
  Secretaria de colegiados da CGOV/ICMBio: pauta e convocação (CONVOCAR), minuta de ata a partir da transcrição
  ou das anotações da reunião (GERAR_ATA), quadro de encaminhamentos com responsável e prazo (ENCAMINHAMENTOS) e
  conferência da ata contra o ato de instituição (CONFERIR_ATA). Base: Portaria ICMBio nº 4.529/2025 (CTGRIC,
  em que a CGOV exerce a Secretaria-Executiva) e o ato de cada colegiado no acervo normativo. Use ao ouvir
  "faça a ata", "minuta de ata", "transcrição da reunião", "pauta da reunião", "convocação do CTGRIC",
  "encaminhamentos da reunião", "quem ficou com o quê", "confira a ata". Não cria nem altera colegiado (ato
  normativo: cgov-nt-01-triagem) e não trata da Política de Governança (pendência E7).
---

# cgov-secretaria-colegiados — Secretaria de colegiados

Esta skill apoia a CGOV no trabalho de secretaria de colegiados: preparar a reunião, registrar o que foi
decidido e acompanhar os encaminhamentos. Ela redige **minutas**: a ata só vale depois de ajustada pelos
membros e assinada no SEI.

## ANTES DE QUALQUER MODO

1. **Identifique o colegiado** e leia o ato que o institui no **acervo normativo** (caminho no `AGENTS.md`,
   ADR-006). A tabela de `references/colegiados.md` diz qual ato procurar e qual o papel da CGOV em cada um.
   Se o ato não estiver no acervo, pergunte ao usuário e marque ⚠️; não use regras de outro colegiado.
2. **Material de reunião** fica na **pasta de colegiados**, na subpasta do colegiado, com a data `AAAAMMDD` no
   início do nome (`LEIA-ME.md` da pasta CGOV). Salve ali a minuta, nunca por cima de arquivo existente
   (use `_v2`, `_v3`).
3. **Regras invioláveis:**
   - **não invente:** data, horário, presença, voto, deliberação, prazo ou responsável que não esteja na
     transcrição, nas anotações ou na fala do usuário fica como `[⚠️ confirmar]`;
   - **fala não é deliberação:** só registre como deliberação o que foi aprovado ou acordado na reunião;
     propostas e opiniões vão para o resumo da discussão;
   - **nomes:** na minuta de ata, os membros aparecem pelo nome e pela unidade, como na transcrição (a ata é
     documento do processo e fica na pasta CGOV). Nada de nomes, matrículas ou e-mails em fichas, índices,
     evals ou exemplos da skill;
   - **sem transcrição literal:** resuma a essência e o impacto; diálogo só em citação curta, quando o próprio
     colegiado pediu registro;
   - **sigilo:** conteúdo marcado como restrito ou sigiloso na reunião é sinalizado na minuta, porque as atas
     assinadas são publicadas (no CTGRIC, art. 12, § 2º, da Portaria nº 4.529/2025).

## MODO 1 — CONVOCAR (pauta e convocação)

1. Peça ou extraia: colegiado, tipo de reunião (ordinária ou extraordinária), data, horário, modalidade
   (presencial, virtual ou híbrida), itens de pauta e documentos de suporte.
2. Confira o **prazo de antecedência** do ato do colegiado (CTGRIC: 5 dias úteis para a ordinária e 48 horas
   para a extraordinária, art. 8º). Se a data proposta não cumprir o prazo, avise antes de redigir.
3. Lembre o prazo para os membros sugerirem itens (CTGRIC: 5 dias úteis antes da ordinária, art. 8º,
   parágrafo único).
4. Saída: pauta numerada (item, objetivo — informe, discussão ou deliberação —, responsável pela apresentação,
   tempo estimado, documento de suporte) e texto curto de convocação com os três elementos do art. 8º
   (data, horário e local; pauta; documentação).

## MODO 2 — GERAR_ATA (minuta de ata)

1. **Entrada:** transcrição (texto) ou anotações. Áudio não é lido diretamente: peça a transcrição.
2. **Extraia** em rascunho, antes de redigir: data, início e fim, modalidade; presentes (membros e convidados,
   com a unidade); pauta; para cada item, contexto, pontos centrais da discussão, deliberações, votos e
   posicionamentos relevantes, encaminhamentos (o quê, quem, até quando); observações (ausências, problemas
   técnicos, pedidos de registro).
3. **Quórum:** compare os presentes com a composição do ato. No CTGRIC, os arts. 9º e 11 tratam do quórum de
   forma diferente (presença mínima de 50% e quórum de reunião por maioria absoluta): se a presença ficar entre
   os dois, sinalize ⚠️ e não declare a reunião irregular.
4. **Redija** pela estrutura de `references/modelo-ata.md`, que segue o conteúdo mínimo do ato (no CTGRIC,
   art. 12: data, hora e local; presentes e convidados; resumo; deliberações, proposições e recomendações
   aprovadas; votos e posicionamentos relevantes).
5. **Feche** com a lista de `[⚠️ confirmar]` e o lembrete do rito: a minuta vai aos membros pelo SEI para
   ajustes antes da assinatura (CTGRIC, art. 12, § 1º).

## MODO 3 — ENCAMINHAMENTOS (quadro de acompanhamento)

1. A partir da ata (aprovada ou minuta), monte o quadro:

| Nº | Reunião | Encaminhamento | Responsável (unidade) | Prazo | Situação | Observação |
|---|---|---|---|---|---|---|

2. Responsável é a **unidade** (e a pessoa só se a ata nomear). Sem prazo na ata: `[⚠️ sem prazo]`, nunca um
   prazo sugerido como se fosse decidido.
3. Para acompanhar um quadro existente, compare-o com a ata nova: marque o que foi concluído, o que mudou de
   prazo e o que é novo. A Secretaria-Executiva monitora o cumprimento das deliberações (CTGRIC, art. 5º, V).

## MODO 4 — CONFERIR_ATA

Confira uma minuta (própria ou de terceiros) contra o ato do colegiado e a transcrição:

| Verificação | Situação | Observação |
|---|---|---|
| Conteúdo mínimo do ato (no CTGRIC, art. 12, I a V) | ✅ / ⚠️ / ❌ | |
| Presentes conferem com a lista ou a transcrição | | |
| Quórum (arts. 9º e 11, no CTGRIC) | | |
| Deliberações registradas como aprovadas foram de fato aprovadas | | |
| Encaminhamentos têm responsável e prazo | | |
| Conteúdo restrito ou sigiloso sinalizado antes da publicação | | |
| Linguagem formal, objetiva, sem transcrição literal | | |

## Fronteiras

- Criar, alterar ou extinguir colegiado é ato normativo: use a `cgov-nt-01-triagem`.
- Riscos tratados pelo CTGRIC: método na `cgov-gestao-riscos`; integridade (Programa e Plano) na
  `cgov-integridade`.
- Política de Governança Institucional e Conselho de Governança: pendência E7 (fora desta skill).

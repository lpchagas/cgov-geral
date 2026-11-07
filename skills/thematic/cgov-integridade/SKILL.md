---
name: cgov-integridade
description: >
  Integridade pública na CGOV/ICMBio, unidade setorial do SITAI (Decreto nº 11.529/2023; Portaria ICMBio nº
  253/2026, art. 5º, § 2º): Programa de Integridade Integra+ (Portaria nº 253/2026), Plano de Integridade
  2026–2028 (Portaria nº 257/2026), monitoramento do plano de ações para o CTGRIC (MONITORAR_PLANO), revisão do
  Programa e do Plano (REVISAR), análise de consulta ou pesquisa de percepção (ANALISAR_PESQUISA), riscos para a
  integridade (RISCOS_INTEGRIDADE) e minuta de designação de Agentes de Integridade (AGENTES). Use ao ouvir
  "Integra+", "Plano de Integridade", "programa de integridade", "SITAI", "unidade setorial de integridade",
  "agentes de integridade", "pesquisa de percepção", "riscos para a integridade", "MMIP". O método de riscos é
  da cgov-gestao-riscos; NT de ato normativo, da cgov-nt-01-triagem.
---

# cgov-integridade — Programa e Plano de Integridade

A CGOV atua como Unidade Setorial de Integridade (USI), ao lado da CGGE e da Ouvidoria (Portaria ICMBio nº
253/2026, art. 5º, § 2º), e coordena, com o CTGRIC, a Política de Gestão de Riscos e Integridade (Art. 37,
parágrafo único, IX, da Portaria ICMBio nº 5.592/2025; PGRI, Portaria nº 255/2020). Esta skill trabalha os
instrumentos de integridade; a régua de riscos é a da `cgov-gestao-riscos`.

## ANTES DE QUALQUER MODO

1. **Leia no acervo normativo** (caminho no `AGENTS.md`, ADR-006) as normas de `references/base-normativa.md`
   que o modo usa. Se a versão do acervo for diferente da citada aqui (Programa ou Plano revisados), siga a do
   acervo e avise.
2. **Regras invioláveis:**
   - **não invente** ação, prazo, unidade responsável, KPA do MMIP, indicador ou resultado de pesquisa: o que não
     estiver no Plano, na planilha ou na fala do usuário fica como `[⚠️ confirmar]`;
   - **situação só com evidência:** uma ação só é "concluída" com a entrega identificada (ato publicado,
     documento, painel); sem evidência, "sem informação";
   - **sem dados pessoais:** respostas de pesquisa são tratadas de forma agregada; comentários abertos são
     resumidos sem identificar quem respondeu; nomes e matrículas de agentes de integridade só entram na minuta
     de portaria, nunca em quadros de monitoramento;
   - **denúncias não são tratadas aqui:** o canal oficial é o Fala.BR (Portaria nº 253/2026, art. 14); se o
     usuário relatar um caso concreto, oriente o canal e não analise o mérito.

## MODO 1 — MONITORAR_PLANO

O Plano 2026–2028 prevê monitoramento da execução das ações (realizadas ou não), sem metas de desempenho nesta
etapa, em reuniões trimestrais do CTGRIC (Plano, item 4.4).

1. Entrada: o Plano de Ações (Tabela 1 do item 4.3 do Plano) e as informações recebidas das instâncias.
2. Saída: quadro por ação, a partir do Plano:

| Ação | Unidade responsável (coordenação) | Entrega prevista | KPA (MMIP) | Prazo | Situação | Evidência | Desvio e medida proposta |
|---|---|---|---|---|---|---|---|

   Situação: concluída / em andamento / não iniciada / atrasada / sem informação. "Atrasada" é a ação com prazo
   vencido sem a entrega.
3. Resumo para a pauta do CTGRIC: totais por situação, ações atrasadas com a medida proposta, e pontos para
   deliberação. A pauta e a ata ficam com a `cgov-secretaria-colegiados`.
4. Os resultados alimentam o painel integrado, que a CGOV produz e mantém (Portaria nº 253/2026, art. 11,
   parágrafo único).

## MODO 2 — REVISAR (Programa ou Plano)

1. Use os critérios mínimos de revisão do art. 12 da Portaria nº 253/2026: lições aprendidas; inovações
   normativas; boas práticas; resultado do IESGo; roteiro do e-Prevenção; orientações dos órgãos de controle;
   MMIP da CGU.
2. Saída: tabela de sugestões por instrumento (Programa, Plano) com: dispositivo ou ação atual; problema
   identificado; critério do art. 12 que o fundamenta; proposta de texto ou de ação; unidade envolvida.
3. Uma revisão do Programa é ato normativo: indique a `cgov-nt-01-triagem` para a NT e a instrução do processo.

## MODO 3 — ANALISAR_PESQUISA

Para consultas internas e pesquisas de percepção sobre integridade (o Plano prevê uma pesquisa de percepção sob
coordenação da CGOV).

1. Entrada: a base de respostas (planilha ou CSV). Leia a estrutura antes: perguntas, tipo de resposta, número
   de respondentes. Calcule as frequências em código, nunca de cabeça.
2. Saída por pergunta: enunciado; tabela de respostas com contagem e percentual; análise descritiva e crítica
   (pelo menos dois parágrafos); limites (amostra, não resposta, viés de autosseleção).
3. Feche com sugestões de ajuste ao Programa e ao Plano, uma tabela por instrumento, ligando cada sugestão às
   perguntas que a sustentam. A avaliação qualitativa do Plano usa pesquisas de clima e percepção
   (art. 10, parágrafo único, II).

## MODO 4 — RISCOS_INTEGRIDADE

1. Use as seis subcategorias de risco para a integridade da Metodologia (Portaria nº 975/2021), reproduzidas
   no item 4.5 do Plano: abuso de posição ou poder em favor de interesses privados; nepotismo; conflito de
   interesses; pressão interna ou externa ilegal; solicitação ou recebimento de vantagem indevida; utilização
   de recursos públicos em favor de interesses privados.
2. Para cada risco: subcategoria, processo da Cadeia de Valor afetado, causa, evento, consequência e medida de
   tratamento do Plano que já o cobre (ou lacuna).
3. Análise, matriz e nível de risco: encaminhe à `cgov-gestao-riscos` (Regime A, vigente), sem repetir a
   régua aqui.

## MODO 5 — AGENTES (designação de Agentes de Integridade)

1. Use o modelo do Anexo I da Portaria nº 253/2026: ementa, designação dos servidores da Diretoria ou Gerência
   Regional, incumbências (incisos I a III do art. 2º do modelo) e os parágrafos do modelo.
2. Campos a preencher pelo usuário ficam entre colchetes: unidade, nomes e matrículas, número do processo. Não
   preencha nomes nem matrículas com exemplos.

## Fronteiras

- Método de riscos (matriz, residual, controles): `cgov-gestao-riscos`.
- Pauta, ata e encaminhamentos do CTGRIC: `cgov-secretaria-colegiados`.
- Nota Técnica de ato normativo (por exemplo, revisão do Integra+): `cgov-nt-01-triagem`.
- Plano Setorial de Prevenção e Enfrentamento do Assédio e da Discriminação: coordenação da Corregedoria
  (Plano, Tabela 1); o CTGRIC supervisiona (Portaria nº 4.529/2025, art. 3º, IV). Esta skill só o cita.

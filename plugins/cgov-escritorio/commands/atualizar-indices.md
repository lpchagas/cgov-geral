---
description: Regenera os _INDICE.md (e, se pedido, as fichas faltantes) com o gerador publicado nas ferramentas do Escritório
argument-hint: "[--fichas]"
disable-model-invocation: true
---
Execute o MODO 4 (ATUALIZAR_INDICES) da skill `cgov-gestao-acervo`. Opções: $ARGUMENTS

Rode o gerador primeiro numa pasta de saída temporária (`--saida`), mostre a diferença para os índices atuais e só então, com o OK,
rode sobre a raiz. Nunca edite um _INDICE.md à mão; se o gerador falhar, registre com `/cgov-escritorio:registrar-pendencia`.

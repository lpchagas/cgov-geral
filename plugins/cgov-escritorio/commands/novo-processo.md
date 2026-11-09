---
description: Cria a pasta de um processo SEI novo (subpastas e ficha PROCESSO.md) na pasta CGOV
argument-hint: "<nº SEI completo> <apelido-curto>"
disable-model-invocation: true
---
Execute o MODO 2 (NOVO_PROCESSO) da skill `cgov-gestao-acervo` com estes argumentos: $ARGUMENTS

Antes, leia o LEIA-ME.md e o AGENTS.md da raiz da pasta CGOV. Se faltar o número SEI ou o apelido, pergunte: não invente.
Mostre o nome da pasta, as subpastas e o frontmatter da ficha, e só crie depois do OK. Nunca sobrescreva pasta ou ficha existente.
Ao final, ofereça `/cgov-escritorio:atualizar-indices`.

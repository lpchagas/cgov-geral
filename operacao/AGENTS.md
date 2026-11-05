# AGENTS.md — pasta operacional da CGOV

Leia também LEIA-ME.md. Estas regras valem para qualquer agente de IA que trabalhe nesta pasta.

## Caminhos canônicos
| Papel citado pelas skills | Caminho |
|---|---|
| Pasta do processo | 01_processos/SEI_<nº>_<ano>-<dv>_<apelido>/ |
| Ficha do processo | <pasta do processo>/PROCESSO.md |
| Pasta de trabalho / estado da NT | <pasta do processo>/trabalho/ · trabalho/NT_ESTADO.md |
| Documentos do SEI / referências / produtos | <pasta do processo>/documentos-sei · referencias · produtos |
| Série de Notas Técnicas | 02_notas-tecnicas/<ano>/ + 02_notas-tecnicas/_INDICE.md |
| Acervo normativo | 03_normativos/ (+ _INDICE.md; revogados/) |
| Caixa de entrada | 00_entrada/ |
| Documentação do Escritório (somente leitura) | 90_escritorio-virtual/referencia/ |
| Modelos | 90_escritorio-virtual/modelos/ |
| Pendências para o desenvolvimento | 90_escritorio-virtual/manutencao/PENDENCIAS.md |

## Obrigações
1. Processo novo: criar a pasta com as subpastas documentos-sei/, trabalho/, referencias/ e produtos/ e
   copiar 90_escritorio-virtual/modelos/processo/PROCESSO.md, preenchendo o frontmatter.
2. Depois de trabalhar num processo: atualizar situacao e atualizado_em no PROCESSO.md.
3. Nunca gravar em 90_escritorio-virtual/ nem fora das pastas acima; nunca excluir (usar 99_arquivo/).
4. Nunca criar pastas local/, analyses/ ou nomes fora da convenção do LEIA-ME.md.
5. Movimentações em lote somente após mostrar a lista e receber confirmação.
6. Os _INDICE.md são gerados a partir das fichas: não editar à mão.
7. Não inventar número de lei, decreto, portaria ou artigo: sinalizar a lacuna com ⚠️.

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
| Pasta de rascunhos da transcrição de normativos | 90_escritorio-virtual/transcricoes/<data-hora>-<slug>/ |
| Pasta de trabalho do PGD | 06_gestao-da-coordenacao/pgd/ |
| Lista da equipe da Coordenação | 06_gestao-da-coordenacao/equipe.md (nome e papel; sem matrícula nem e-mail) |
| Registro de decisões | <pasta do processo>/PROCESSO.md, seção Andamento |
| Pasta de processos | 01_processos/ |
| Ferramentas do Escritório (somente executar; não editar) | 90_escritorio-virtual/ferramentas/ (gerar_indices.py) |

## Locais antigos
As skills citam só os papéis da tabela acima. Esta tabela serve para achar arquivos (por exemplo, o NT_ESTADO.md)
gravados em locais anteriores à reorganização de 2026:

| Caminho citado pela skill | Caminho nesta pasta |
|---|---|
| local/analyses/SEI_<processo>_<apelido>/ (inclui NT_ESTADO.md) | 01_processos/<pasta do processo>/trabalho/ |
| CGOV_Processos/<pasta>/_CGOV_NT/ (versão instalada da cgov-nt-01; pasta no padrão SEI_<nº>_<ano>_<dv>_<APELIDO>) | 01_processos/<pasta do processo>/trabalho/ (nome da pasta no padrão do LEIA-ME.md) |
| local/normative-sources/ | 03_normativos/ |
| local/acervo-drive/manutencao/PENDENCIAS.md | 90_escritorio-virtual/manutencao/PENDENCIAS.md |
| docs/… (decision-log, relatórios, catálogo) | 90_escritorio-virtual/referencia/docs/… (somente leitura) |

Se a pasta do processo não existir, crie-a conforme a obrigação 1, usando o padrão de nome do LEIA-ME.md.

## Obrigações
1. Processo novo: criar a pasta com as subpastas documentos-sei/, trabalho/, referencias/ e produtos/ e
   copiar 90_escritorio-virtual/modelos/processo/PROCESSO.md, preenchendo o frontmatter.
2. Depois de trabalhar num processo: atualizar situacao e atualizado_em no PROCESSO.md.
3. Nunca gravar em 90_escritorio-virtual/ nem fora das pastas acima, salvo: (a) os rascunhos de transcrição em 90_escritorio-virtual/transcricoes/; (b) novas entradas, acrescentadas só ao FIM, em 90_escritorio-virtual/manutencao/PENDENCIAS.md (nunca alterar nem remover entradas existentes). Nunca excluir (usar 99_arquivo/).
4. Nunca criar pastas local/, analyses/ ou nomes fora da convenção do LEIA-ME.md.
5. Movimentações em lote somente após mostrar a lista e receber confirmação.
6. Os _INDICE.md são gerados a partir das fichas: não editar à mão.
7. Não inventar número de lei, decreto, portaria ou artigo: sinalizar a lacuna com ⚠️.

## Comandos do plugin cgov-escritorio
Atalhos que executam os modos da skill cgov-gestao-acervo, com as mesmas regras (lista e confirmação antes de mover; nunca excluir):
- /cgov-escritorio:novo-processo <nº SEI> <apelido> — pasta do processo e ficha PROCESSO.md (obrigação 1).
- /cgov-escritorio:triar-entrada — destino e nome padronizado para o que está em 00_entrada.
- /cgov-escritorio:atualizar-indices — regenera os _INDICE.md (obrigação 6).
- /cgov-escritorio:registrar-pendencia — acrescenta uma entrada ao PENDENCIAS.md (obrigação 3, exceção b).

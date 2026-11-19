# Changelog — plugin `cgov-escritorio`

Formato: uma seção por versão, da mais recente para a mais antiga. A `version` do `plugin.json` e esta lista andam juntas;
a cada versão nova, `py scripts\publicar_operacao.py --publicar --executar` gera um zip novo em `dist\`.

## [1.1.0] — 2026-11-19

- Suíte `cgov-nt` (03 a 07): cada etapa termina alimentando o `.docx` de revisão da NT, versionado pela fase
  (`v1-introducao`, `v2.N-<subsídio>`, `v3-propostas`, `v4-quesitos-pfe`, `v5-conclusao`; revisões `vN.M-…`).
  O capítulo é acrescentado à versão mais recente, preservando as edições do revisor. Gerador:
  `scripts/montar_nt_docx.py`, publicado nas Ferramentas do Escritório; padrão gráfico das NTs da CGOV.
- Retirada a regra "não gerar `.docx`" das skills 03, 04 e 07; evals atualizados (1 caso novo por skill).

## [1.0.0] — 2026-11-18

- Primeira versão estável. Substitui as 32 skills avulsas da conta, desativadas em 09/11/2026 e usadas só pelo plugin
  durante uma semana, sem falhas.
- 32 skills: suíte `cgov-nt` (7), PGD (8) e as demais (17: acervo e processos SEI, análise normativa e temáticas).
- 4 comandos: `/cgov-escritorio:novo-processo`, `:triar-entrada`, `:atualizar-indices` e `:registrar-pendencia`.
- Ficam fora do plugin as 2 skills da Formação CGGE (`cgge-fgbio-*`), que seguem avulsas.

## [0.1.0] — 2026-11-09

- Primeira publicação: 32 skills (movidas de `skills/<família>/`, estrutura plana) e 4 comandos de acervo.
- Zip enviado em Customize → Plugins e testado no projeto "Escritório CGOV — Operação".

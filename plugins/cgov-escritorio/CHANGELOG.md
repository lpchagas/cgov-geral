# Changelog — plugin `cgov-escritorio`

Formato: uma seção por versão, da mais recente para a mais antiga. A `version` do `plugin.json` e esta lista andam juntas;
a cada versão nova, `py scripts\publicar_operacao.py --publicar --executar` gera um zip novo em `dist\`.

## [1.0.0] — 2026-11-18

- Primeira versão estável. Substitui as 32 skills avulsas da conta, desativadas em 09/11/2026 e usadas só pelo plugin
  durante uma semana, sem falhas.
- 32 skills: suíte `cgov-nt` (7), PGD (8) e as demais (17: acervo e processos SEI, análise normativa e temáticas).
- 4 comandos: `/cgov-escritorio:novo-processo`, `:triar-entrada`, `:atualizar-indices` e `:registrar-pendencia`.
- Ficam fora do plugin as 2 skills da Formação CGGE (`cgge-fgbio-*`), que seguem avulsas.

## [0.1.0] — 2026-11-09

- Primeira publicação: 32 skills (movidas de `skills/<família>/`, estrutura plana) e 4 comandos de acervo.
- Zip enviado em Customize → Plugins e testado no projeto "Escritório CGOV — Operação".

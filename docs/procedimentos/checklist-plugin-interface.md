---
tipo: procedimento
status: vigente
versao: "1"
atualizado_em: 2026-11-18
relacionados: [docs/fluxos-de-trabalho.md, docs/plano-implantacao.md, docs/governance/pendencias.md, plugins/cgov-escritorio/CHANGELOG.md]
---

# Checklist de interface do plugin `cgov-escritorio`

> **Versão 1, 18/11/2026** (encerramento da Fase 7, D64). Conferência manual, no Claude Desktop, do que os testes
> automatizados não alcançam. Use depois de cada envio de versão nova do plugin em Customize → Plugins e depois de
> qualquer exclusão de skill avulsa. Antes, rode os testes automatizados (§3).

## 1. Preparação

- Abra o Claude Desktop e entre no projeto Cowork **"Escritório CGOV — Operação"**. No Claude Code deste
  repositório o plugin fica desligado (`enabledPlugins` no `.claude\settings.json`), por isso o teste é no Cowork.
- Para os itens 3 a 6, use uma conversa nova para cada item. Nos comandos que gravam, cancele antes de gravar.

## 2. Itens

| # | Onde | Ação | Resultado esperado | Arquivo de referência |
|---|---|---|---|---|
| 1 | Customize → Plugins | Abrir a lista | Uma só entrada, "Escritório CGOV — ICMBio", na versão do `plugin.json`, com 32 skills e ativa | `C:\Projetos\cgov-geral\plugins\cgov-escritorio\.claude-plugin\plugin.json`; zip em `C:\Projetos\cgov-geral\dist\cgov-escritorio-<versão>.zip` |
| 2 | Customize → Skills | Abrir a lista | Nenhuma das 32 skills do plugin como avulsa; as 2 `cgge-fgbio-*` desativadas (D62) | `C:\Projetos\cgov-geral\plugins\cgov-escritorio\skills\`; `C:\Projetos\cgov-geral\skills\cgge-fgbio\` |
| 3 | Projeto Operação | Digitar `/cgov-escritorio:` sem enviar | Menu com `atualizar-indices`, `novo-processo`, `registrar-pendencia` e `triar-entrada` | `C:\Projetos\cgov-geral\plugins\cgov-escritorio\commands\` |
| 4 | Projeto Operação | Enviar `/cgov-escritorio:triar-entrada` | Lista os arquivos de `00_entrada` e propõe destinos, sem mover nada antes da confirmação | Pasta lida: `%USERPROFILE%\My Drive\10_Institucional\CGOV\00_entrada\`; skill `C:\Projetos\cgov-geral\plugins\cgov-escritorio\skills\cgov-gestao-acervo\SKILL.md` |
| 5 | Projeto Operação | Escrever "Preciso de uma Nota Técnica sobre um processo novo" | `cgov-nt-01-triagem` acionada uma única vez | `C:\Projetos\cgov-geral\plugins\cgov-escritorio\skills\cgov-nt-01-triagem\SKILL.md` |
| 6 | Projeto Operação | Escrever um pedido de análise de indicador do PGD (por exemplo, "Analise este indicador do PGD: percentual de entregas concluídas no prazo") | `pgd-analisar-indicador` acionada uma única vez, sem entrada avulsa duplicada | `C:\Projetos\cgov-geral\plugins\cgov-escritorio\skills\pgd-analisar-indicador\SKILL.md` |

Para devolver o resultado ao desenvolvimento, use o formato "1 ok, 2 ok, 3 falhou: …", com um print ou o texto da
tela quando algo divergir.

## 3. Testes automatizados (antes do checklist)

1. `py scripts\publicar_operacao.py --verificar --sem-avulsas`: seções 1, 1b e 2 sem divergências.
2. `claude plugin validate .\plugins\cgov-escritorio`: "Validation passed".
3. SHA-256 de `dist\cgov-escritorio-<versão>.zip` igual ao do `.sha256` correspondente; zip sem `evals/`.

## 4. Registro das execuções

| Data | Versão | Resultado | Registro |
|---|---|---|---|
| 18/11/2026 | 1.0.0 | 6/6 ok (informado pelo Coordenador) | Plano v3.59 (Fase 7, encerramento) |

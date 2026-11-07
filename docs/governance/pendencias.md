# Pendências do Escritório CGOV (desenvolvimento)

> Lista consolidada em 06/11/2026, ao fim da Fase 4 do plano de implantação. Fonte do andamento: o plano de
> implantação (fases e etapas citadas abaixo). Pendências registradas pela operação ficam em
> `90_escritorio-virtual/manutencao/PENDENCIAS.md` da pasta CGOV; quando uma delas exigir trabalho de
> desenvolvimento, ela é copiada para cá (sem dados pessoais nem dados de processos).

## Alta prioridade

| # | Pendência | Onde se resolve | Observação |
|---|---|---|---|
| P1 | Junções `local\analyses`, `local\normative-sources` e `local\acervo-drive` apontam para pastas que não existem mais | Fase 5.1–5.2 (`link_acervo.py`, `.env`) | ✅ Resolvida em 07/11/2026: `scripts/link_acervo.py --executar` criou `local\processos`, `local\normativos` e `local\escritorio` e removeu as antigas |
| P2 | `scripts/publicar-operacao.sh` e `scripts/link-acervo.sh` (WSL, estrutura antiga) bloqueados em 06/11/2026 | Fase 5.3 (`publicar_operacao.py`) e 5.8 (mover os `.sh` para `archive/scripts-wsl/`) | ✅ Resolvida em 07/11/2026: substitutos em Python prontos; `.sh` em `archive/scripts-wsl/` |
| P3 | Cópia de `docs/` em `90_escritorio-virtual/referencia/docs/` é anterior à Fase 4 | Fase 5.10 | ✅ Resolvida em 07/11/2026: republicada no commit `e305404` (33/33 conferidos); anterior em `99_arquivo/_a-excluir_2026-11-07/` |
| P4 | Deriva fonte × instalado: 9 das 14 skills com fonte estão desatualizadas na conta (`publicar_operacao.py --verificar`, 07/11/2026: as 7 da `cgov-nt`, `cgov-gestao-riscos` e `cgov-regimento-interno`); a `cgov-nt-01-triagem` instalada grava em `CGOV_Processos/…/_CGOV_NT/` e a fonte diz `local/analyses/` | Fase 6.1 (comparar) e 6.8 (reinstalar) | Contornado pela tabela de caminhos do `AGENTS.md` da pasta CGOV. **6.1 ✅ (07/11/2026):** exportação em `local/installed-reference/_export_2026-11-07/` (39/39 conferidos) e divergências decididas (D43 do plano; decision-log §30): `cgov-nt` = fonte + busca da conta; `cgov-gestao-riscos` = conta saneada (sem números de documento SEI); `cgov-regimento-interno` = fonte; 3 skills do PGD promovidas a partir da conta. Falta a reinstalação (6.8) |
| P5 | Skills citam caminhos literais (`local/analyses/`, `local/normative-sources/`, `_CGOV_NT/`) | Fase 6.3 (caminhos neutros, ADR-006) | Depois, retirar a seção "Caminhos" das instruções do projeto Operação e a tabela do `AGENTS.md` |
| P6 | Exclusão da quarentena `99_arquivo/_a-excluir_2026-11-05/` | Etapa 4.11, a partir de 05/12/2026 | Vínculo temporário da pasta CGOV; confirmação explícita |
| P7 | Quarentena da publicação de 07/11/2026: `99_arquivo/_a-excluir_2026-11-07/publicacao_e305404/` (referência de `docs/` do commit `4960e11`, 14 arquivos) | A partir de 07/12/2026 (30 dias, ADR-014), junto com ou depois da 4.11 | Confirmação explícita; nada a recuperar se a referência atual estiver íntegra (`--verificar`) |

## Conteúdo da pasta CGOV (revisão gradual pela operação)

| # | Pendência | Observação |
|---|---|---|
| C1 | Campos ⚠️ das 74 fichas `PROCESSO.md` (título em 16, inciso, situação, unidade, abertura, objeto) | Preencher só com informação confirmada |
| C2 | Nomes da série de NTs fora do padrão `NT_<nº>-<ano>_SEI_<nº documento>_<tema>.pdf` | Duas NTs de 2025 com o mesmo nº de documento no nome do arquivo; uma NT de outra unidade na série |
| C3 | Normas citadas pelas skills e ausentes de `03_normativos` (Decreto nº 12.002/2024, LC nº 95/1998) e 9 normativos sem o par PDF/`.md` | Curadoria do acervo |
| C4 | Vigência dos normativos (`_INDICE.md` marca "⚠️ verificar") | Curadoria do acervo |
| C5 | `05_projetos/fundo-rio-doce` fora do padrão `AAAA-MM_apelido`; período do projeto da oficina da GR2 | Ficha `PROJETO.md` |
| C6 | Referências de caminho antigas dentro de arquivos de trabalho (por exemplo, "Local deste arquivo" em `NT_ESTADO.md`) | Atualizar no próprio processo, pela operação |

## Evolução

| # | Pendência | Onde se resolve |
|---|---|---|
| E1 | Modelo geral de análise de atos normativos (instruções v1 geradas a partir de um processo real): ~~decidir as 6 questões em aberto~~ (✅ 07/11/2026, D44: AIR Nível 2 padrão; competências e legística também obrigatórias; foco por projeto; dispositivos no futuro; residual na classe superior; `trabalho/` neutro), tornar modelagem de processos, competências, legística, riscos e AIR subsídios obrigatórios da NT, corrigir 8 divergências entre skills, publicar o procedimento | Etapa 6.9 (D34); piloto na Fase 11 |
| E2 | Decisões D5–D8 do plano (D4 respondida em 07/11/2026: skill `cgov-triagem-processo-sei` + `.md` mantido; acesso dos servidores, orientação institucional sobre IA e LGPD, Fabric/Power BI, Maestri) | Fase 0 |
| E3 | ~~`docs/adr/`, `catalogo-skills.md`, `docs/README.md` e mudança do plano para `docs/plano-implantacao.md`~~ | ✅ Fase 5.9, bloco 5 (07/11/2026; D40) |
| E4 | ~~`scripts/verificar_sanitizacao.py`~~ — criado em 06/11/2026 (v0.1.1, Fase 5, bloco 1) | Resolvida; uso em `docs/fluxos-de-trabalho.md` |
| E6 | Evals da `cgov-nt-01-triagem` e da `cgov-nt-03-introducao` citam um número real de processo SEI (aviso do `verificar_sanitizacao.py`) | Fase 6.8: trocar por número fictício (D38) |
| E5 | Validar `ocr_windows.ps1` (`cgov-transcrever-normativos`) no Windows | Fase 6.7 |

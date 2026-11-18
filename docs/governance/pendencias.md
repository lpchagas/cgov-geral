---
tipo: pendencias
status: vigente
atualizado_em: 2026-11-18
relacionados: [docs/plano-implantacao.md, docs/governance/rastreabilidade.md]
---

# Pendências do Escritório CGOV (desenvolvimento)

> Reorganizada em 09/11/2026 (revisão documental antes da Fase 7); consolidada originalmente em 06/11/2026, ao
> fim da Fase 4. Fonte do andamento: o [plano de implantação](../plano-implantacao.md). Pendências registradas pela
> operação ficam em `90_escritorio-virtual/manutencao/PENDENCIAS.md` da pasta CGOV; quando uma delas exigir
> trabalho de desenvolvimento, ela é copiada para cá (sem dados pessoais nem dados de processos).
> Os IDs não mudam: **P** = prioridade, **S** = segurança, **C** = conteúdo da pasta CGOV, **E** = evolução.
> Itens resolvidos ficam na seção final, para consulta.

## Em aberto — desenvolvimento

| # | Pendência | Onde se resolve | Observação |
|---|---|---|---|
| P6 | Exclusão da quarentena `99_arquivo/_a-excluir_2026-11-05/` | Etapa 4.11, a partir de 05/12/2026 | Vínculo temporário da pasta CGOV; confirmação explícita (ADR-014) |
| P7 | Quarentenas das publicações: `99_arquivo/_a-excluir_2026-11-07/publicacao_e305404/` (referência de `docs/` do *commit* `4960e11`, 14 arquivos), `_a-excluir_2026-11-07/publicacao_<commit>/` (07/11), `_a-excluir_2026-11-08/publicacao_066068b/` (08/11) e `_a-excluir_2026-11-09/publicacao_c58a940/` (09/11; `AGENTS.md` anterior de `operacao/` e referência anterior de `docs/`) e `_a-excluir_2026-11-18/` (18/11; `publicacao_8b24d3e/`, com a referência anterior de `docs/`, o zip de teste `cgov-escritorio-v1.zip` e `publicacao_a3c58c1/`, com a referência de `docs/` do `8b24d3e`, substituída na publicação da D65) | A partir de 07/12/2026 (30 dias, ADR-014), junto com ou depois da 4.11; a de 09/11, a partir de 09/12/2026; a de 18/11, a partir de 18/12/2026 | Confirmação explícita; nada a recuperar se a referência atual estiver íntegra (`publicar_operacao.py --verificar`) |
| E1 | Modelo geral de análise de atos normativos (instruções v1 geradas a partir de um processo real). Decididas em 07/11/2026 (D44) as 6 questões; modelagem de processos, competências, legística, riscos e AIR viraram subsídios obrigatórios da NT, 8 divergências entre skills foram corrigidas e o procedimento foi publicado (6.9(b)–(d), D50; [procedimento](../procedimentos/analise-atos-normativos.md)). **Falta:** inciso do Art. 37 para competências e legística (⚠️), evals da `nt-01` com o roteiro novo (6.8) e o piloto | Piloto na Fase 11 | |
| E2 | Decisões D5–D8 do plano (acesso dos servidores, orientação institucional sobre IA e LGPD, Fabric/Power BI, Maestri); a D4 foi respondida em 07/11/2026 (skill `cgov-triagem-processo-sei` + `.md` mantido) | Fase 0 | Plano, §9 |
| E7 | Skill da Política de Governança Institucional (Art. 37, p.u., II; Portaria ICMBio nº 4.101/2023): instâncias internas de governança, Conselho de Governança, não sobreposição de colegiados. Insumos na pasta de prompts `02_dev-prompts` (`CGOV_Política de Governança`, Analista v4.6, `CGOV_Conselho de Participação`) | Adiada pelo Coordenador (D45, 07/11/2026); depois da Fase 6 | |
| E9 | Criar `evals/evals.json` (3 casos sintéticos cada) para as **20 skills sem casos em 09/11/2026**: as 13 já previstas (8 `pgd-*`, 2 `cgge-fgbio-*`, `cgov-auditoria-competencias`, `cgov-comparar-versoes`, `cgov-modelar-fluxo`) e mais 7 temáticas (`cgov-air-arr`, `cgov-cadeia-valor`, `cgov-gestao-riscos`, `cgov-pgr`, `cgov-qcf`, `cgov-regimento-interno`, `cgov-transcrever-normativos`). Contagem corrigida em 09/11/2026 (D54 falava em 13) | Antes do piloto da Fase 11 | ADR-011 |
| E10 | `qa_transcription.py`: checagem automática dos ordinais e do `§` mal lidos pelo OCR (`1º` → `10`, `§` → `s`), achado da 6.7 | Evolução da `cgov-transcrever-normativos` | |
| E11 | `cgov-saneamento-legistica`: tabela "regra → dispositivo conferido" (Decreto nº 12.002/2024, LC nº 95/1998 e Portaria ICMBio nº 271/2013, Anexo I) e evals com verificações específicas no lugar das genéricas, achado dos evals da 6.8 (D54) | Depois da transcrição das duas normas no acervo (C3) | |
| E13 | Espelho `.agents/skills/` (Antigravity) não existe nesta máquina e cobria 13 skills; decidir entre regerar para as 34 fontes ou aposentar a regra do `CONTRIBUTING.md` | Antes de usar a Antigravity; depois da Fase 7 (novos caminhos) | [`multiplatform.md`](../multiplatform.md) §2 |
| E15 | Avaliar migrar os 4 comandos de `commands/` para skills (a documentação oficial chama `commands/` de formato antigo; o nome do comando não muda) | Depois da 7.6, com o plugin em uso | Exigiria catálogo, evals e ajuste do verificador (36 skills); ver decision-log §47 |
| E17 | Gerações antigas de pacotes em `dist/skills/<commit>/` (`0d85240`, `3723745`, `449dbf0`, `b863ef3`, `d4f75c8`, `d5d144e`, `e305404`) viram candidatas à quarentena. **Não** mover `066068b` (rede de segurança da exclusão das avulsas: 34 pacotes idênticos às skills do plugin) | Depois que a 1.0.0 estabilizar | Prioridade baixa; nunca excluir |

## Em aberto — conteúdo da pasta CGOV (revisão gradual pela operação)

| # | Pendência | Observação |
|---|---|---|
| C1 | Campos ⚠️ das 74 fichas `PROCESSO.md` (título em 16, inciso, situação, unidade, abertura, objeto) | Preencher só com informação confirmada |
| C2 | Nomes da série de NTs fora do padrão `NT_<nº>-<ano>_SEI_<nº documento>_<tema>.pdf` | Duas NTs de 2025 com o mesmo nº de documento no nome do arquivo; uma NT de outra unidade na série |
| C3 | Normas citadas pelas skills e ausentes de `03_normativos` (Decreto nº 12.002/2024, LC nº 95/1998 e, desde a 6.9, a Portaria Conjunta nº 3, de 13/05/2021, sobre consultas jurídicas à PFE, citada pela `cgov-nt-06` com ⚠️; o arquivo "Portaria Conjunta ICMBio PFE 03-2021" do acervo é outra norma, a Portaria PFE/ICMBio nº 3/2021, da OJN nº 27/2021) e 9 normativos sem o par PDF/`.md`; desde a 6.10, os atos do Conselho de Governança e do CIG, citados pela `cgov-secretaria-colegiados` com ⚠️ | Curadoria do acervo |
| C4 | Vigência dos normativos (`_INDICE.md` marca "⚠️ verificar") | Curadoria do acervo |
| C5 | `05_projetos/fundo-rio-doce` fora do padrão `AAAA-MM_apelido`; período do projeto da oficina da GR2 | Ficha `PROJETO.md` |
| C6 | Referências de caminho antigas dentro de arquivos de trabalho (por exemplo, "Local deste arquivo" em `NT_ESTADO.md`) | Atualizar no próprio processo, pela operação |
| C7 | Criar `06_gestao-da-coordenacao/equipe.md` (nome e papel, sem matrícula nem e-mail) e a pasta `06_gestao-da-coordenacao/pgd/`, lidas pelas skills do PGD desde a 6.2/6.3 (D46, D48); caminhos já no `operacao/AGENTS.md` | Pela operação; sem a lista, a skill pergunta os responsáveis |
| C8 | Curadoria de dois arquivos de `03_normativos`: renomear o da Portaria ICMBio nº 271/2013 (data no nome errada; é de 27/12/2013; incluir o tema) e o da Portaria PFE/ICMBio nº 3/2021 (não é conjunta; tema: OJN nº 27/2021, aviso de recebimento); regenerar o índice; refazer, a partir do PDF, a numeração do Anexo II da nº 271/2013 na transcrição (os quesitos 4 a 8 aparecem como 10 a 14); desde a 6.10, as duas transcrições do Decreto nº 9.094/2017 com nomes diferentes | Pela operação (D52) |

## Resolvidas

| # | Pendência | Resolução |
|---|---|---|
| P1 | Junções `local\analyses`, `local\normative-sources` e `local\acervo-drive` apontavam para pastas que não existem mais | 07/11/2026: `scripts/link_acervo.py --executar` criou `local\processos`, `local\normativos` e `local\escritorio` e removeu as antigas (Fase 5.1–5.2) |
| S1 | Credencial de banco em texto aberto num script da pasta de prompts do Coordenador | 07/11/2026, pelo Coordenador (script limpo); nada foi copiado para o repositório |
| P2 | `scripts/publicar-operacao.sh` e `scripts/link-acervo.sh` (WSL, estrutura antiga) bloqueados em 06/11/2026 | 07/11/2026: substitutos em Python prontos (5.3); `.sh` em `archive/scripts-wsl/` (5.8) |
| P3 | Cópia de `docs/` em `90_escritorio-virtual/referencia/docs/` anterior à Fase 4 | 07/11/2026 (5.10): republicada no *commit* `e305404` (33/33 conferidos); anterior em `99_arquivo/_a-excluir_2026-11-07/` |
| P4 | Deriva fonte × instalado: 9 das 14 skills com fonte estavam desatualizadas na conta; a `cgov-nt-01-triagem` instalada gravava em `CGOV_Processos/…/_CGOV_NT/` e a fonte dizia `local/analyses/` | 6.1 (07/11/2026): exportação em `local/installed-reference/_export_2026-11-07/` (39/39 conferidos) e divergências decididas (D43; decision-log §30). 6.8 (07/11–08/11/2026): 34 skills reinstaladas a partir do *commit* `b863ef3` e conferidas (`--verificar` sem divergências, 08/11) |
| P5 | Skills citavam caminhos literais (`local/analyses/`, `local/normative-sources/`, `_CGOV_NT/`) | 6.3 (07/11/2026, D48): 0 caminhos literais em `skills/`; papéis mapeados nos dois `AGENTS.md` (pasta do PGD: `06_gestao-da-coordenacao/pgd/`). 6.8: skills reinstaladas, instruções do projeto Operação v1.1 coladas e "Locais antigos" no `AGENTS.md` (6.8b) |
| E3 | `docs/adr/`, `catalogo-skills.md`, `docs/README.md` e mudança do plano para `docs/plano-implantacao.md` | Fase 5.9, bloco 5 (07/11/2026; D40) |
| E4 | `scripts/verificar_sanitizacao.py` | 06/11/2026 (v0.1.1, Fase 5, bloco 1); uso em [`fluxos-de-trabalho.md`](../fluxos-de-trabalho.md) |
| E5 | Validar `ocr_windows.ps1` (`cgov-transcrever-normativos`) no Windows | Fase 6.7 (07/11/2026): aprovado, com cobertura de 96,1% e 98,3% |
| E6 | Evals da `cgov-nt-01-triagem` e da `cgov-nt-03-introducao` citavam um número real de processo SEI | Fase 6.8a (07/11/2026): número fictício |
| E8 | Ler as transcrições da Portaria ICMBio nº 129/2020 e da Portaria "Conjunta" nº 3/2021 e corrigir as skills e as instruções | 07/11/2026 (D52): a nº 129/2020 prevalece em espécies e vigência; a nº 271/2013 vale no resto, com ⚠️; 13 arquivos corrigidos. Resta só a Portaria Conjunta nº 3, de 13/05/2021 (ver C3) |
| E12 | ADR-005 (plugin único) "Proposto" e pré-requisito formal da Fase 7 | 09/11/2026 (D58): aceito como está, no início da Fase 7; decision-log §45 |
| E14 | Regerar índices e verificar `docs/` depois do `git mv` da 7.1 | 09/11/2026 (7.1): `gerar_indices_docs.py` regerou o catálogo; `verificar_docs.py` passou a varrer `plugins/` (110 `.md`, 0 erros); decision-log §46 |
| E16 | Conferir a geração `~gN` do plugin `cgov-escritorio` e a seção 1b do `--verificar` | 18/11/2026 (7.6b): o reenvio da 1.0.0 criou `cgov-escritorio~g2`; `verificar_plugin()` v0.3.1 o escolheu e a 1b deu "sem divergências"; decision-log §50 |
| E18 | Confirmar a cache local e a semana de uso do plugin | 18/11/2026 (7.6b): 0 skills do plugin como avulsas na cache; semana de uso sem falhas, por informação do Coordenador; decision-log §50 |
| E19 | Referência de `docs/` na pasta CGOV defasada porque `--publicar --executar` parava com a `version` repetida | 18/11/2026 (7.6b): publicação da 1.0.0 levou a referência a `8b24d3e` (39/39 iguais); decision-log §50 |
| E20 | A avulsa "Pgd analisar indicador" continuava em Customize → Skills (mantida na 7.6b por dúvida de identidade) | 18/11/2026: texto idêntico ao da `pgd-analisar-indicador` do plugin (SHA-256 `29004b1f…bd288` nos dois, conferido pelo Coordenador); excluída pelo Coordenador; `--verificar --sem-avulsas` sem divergências nas seções 1 e 1b; decision-log §52 |

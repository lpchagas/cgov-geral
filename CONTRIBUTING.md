# Contribuição e manutenção

## Convenções

- Use nomes em minúsculas, separados por hífen, para skills e documentos novos.
- Pastas de processos são criadas pelo fluxo operacional (projeto Cowork "Escritório CGOV —
  Operação") em `01_processos/` da pasta CGOV, no formato
  `SEI_<órgão>.<número>_<ano>-<dv>_<apelido>/`, com a ficha `PROCESSO.md`. Testes de desenvolvimento
  vão para `local/pilots/`.
- Mantenha versões supersedidas em `archive/`; não as apague.

## Mudanças em skills

1. Altere a fonte em `skills/cgov-nt/`, `skills/thematic/`, `skills/pgd/`, `skills/normativo/`, `skills/escritorio/` ou `skills/cgge-fgbio/`.
2. Atualize ou execute os evals aplicáveis.
3. Confirme que instruções, exemplos e caminhos ativos permanecem coerentes.
4. Registre a decisão e o resultado em `docs/governance/decision-log.md`.
5. Após o commit, publique para a operação com `py scripts\publicar_operacao.py --publicar` (simulação) e
   `--publicar --executar`, e reinstale no Claude as skills alteradas; confira com `--verificar`
   (ver [`docs/fluxos-de-trabalho.md`](docs/fluxos-de-trabalho.md) §4).

## Espelho para a Antigravity — `.agents/skills/`

A Antigravity carrega skills de `.agents/skills/<nome>/SKILL.md`, não de
`skills/`. `.agents/skills/` é um espelho gerado, ignorado pelo Git — nunca
edite os arquivos ali diretamente. Sempre que um `SKILL.md` em
`skills/cgov-nt/`, `skills/thematic/`, `skills/pgd/`, `skills/normativo/`, `skills/escritorio/` ou `skills/cgge-fgbio/` for alterado, regenere a cópia
correspondente em `.agents/skills/` antes da próxima sessão na Antigravity:

```powershell
New-Item -ItemType Directory -Force .agents\skills\<skill> | Out-Null
Copy-Item skills\<família>\<skill>\SKILL.md .agents\skills\<skill>\SKILL.md -Force
```

O espelho é opcional e local: só vale a pena mantê-lo enquanto a Antigravity for usada. Na Fase 7 as pastas
`skills/<família>/` passam para `plugins/cgov-escritorio/skills/`; depois do `git mv`, rode
`py scripts\gerar_indices_docs.py` para refazer os links do catálogo e `py scripts\verificar_docs.py` para achar
referências de caminho que ficaram para trás.

Ver `docs/multiplatform.md` para o mapeamento completo de qual aplicativo lê
qual arquivo.

## Documentação

Mapa de leitura: [`docs/INDICE.md`](docs/INDICE.md). Regras de escrita (fonte única, frontmatter, links, tamanho):
[`docs/convencoes-documentacao.md`](docs/convencoes-documentacao.md). Antes do *commit*: `py scripts\verificar_docs.py`.

## Revisão antes de publicar

Não inclua dados pessoais, matrículas, rascunhos, dados de pesquisa, documentos
SEI internos ou cópias de fontes sem autorização de redistribuição. Use links
oficiais no catálogo normativo; materiais locais devem permanecer em `local/`.

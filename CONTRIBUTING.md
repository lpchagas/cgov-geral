# Contribuição e manutenção

## Convenções

- Use nomes em minúsculas, separados por hífen, para skills e documentos novos.
- Pastas de processos são criadas pelo fluxo operacional (projeto Cowork "Escritório CGOV —
  Operação") em `01_processos/` da pasta CGOV, no formato
  `SEI_<órgão>.<número>_<ano>-<dv>_<apelido>/`, com a ficha `PROCESSO.md`. Testes de desenvolvimento
  vão para `local/pilots/`.
- Mantenha versões supersedidas em `archive/`; não as apague.

## Mudanças em skills

1. Altere a fonte em `skills/cgov-nt/`, `skills/thematic/`, `skills/pgd/`, `skills/normativo/` ou `skills/cgge-fgbio/`.
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
em `skills/cgov-nt/`, `skills/thematic/`, `skills/pgd/`, `skills/normativo/` ou `skills/cgge-fgbio/` for alterado, regenere a cópia
correspondente em `.agents/skills/` antes da próxima sessão na Antigravity:

```bash
cp skills/<família>/<skill>/SKILL.md .agents/skills/<skill>/SKILL.md
```

Ver `docs/multiplatform.md` para o mapeamento completo de qual aplicativo lê
qual arquivo.

## Revisão antes de publicar

Não inclua dados pessoais, matrículas, rascunhos, dados de pesquisa, documentos
SEI internos ou cópias de fontes sem autorização de redistribuição. Use links
oficiais no catálogo normativo; materiais locais devem permanecer em `local/`.

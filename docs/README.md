---
tipo: guia
status: vigente
atualizado_em: 2026-11-09
relacionados: [docs/INDICE.md, docs/convencoes-documentacao.md]
---

# Documentação do Escritório CGOV (repositório `cgov-geral`)

Pasta de documentação e cofre Obsidian de desenvolvimento (ADR-009). Tudo em `docs/` é mantido sanitizado e
publicado, como cópia somente leitura, em `90_escritorio-virtual/referencia/docs/` da pasta CGOV, por
`scripts/publicar_operacao.py`.

**Comece por [`INDICE.md`](INDICE.md)**: ele diz o que ler para cada tarefa, lista todos os arquivos desta pasta e aponta
os índices dos três arquivos grandes. As regras de escrita estão em
[`convencoes-documentacao.md`](convencoes-documentacao.md).

## Regras rápidas

- Nada de dados pessoais, matrículas, documentos SEI ou caminhos pessoais aqui: rode
  `py scripts\verificar_sanitizacao.py` antes de cada commit.
- Rode também `py scripts\verificar_docs.py` (links, âncoras, frontmatter, caminhos obsoletos).
- O registro de decisões não se reescreve: só se acrescenta ao final.
- Nunca invente norma, número ou dado; sinalize lacunas com ⚠️.

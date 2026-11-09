---
tipo: decisao
status: aceito
atualizado_em: 2026-11-07
relacionados: [scripts/publicar_operacao.py, scripts/link_acervo.py]
---

# ADR-004 — Scripts multiplataforma em Python

- **Status:** Aceito
- **Data:** 07/11/2026 (D40)

## Contexto

Os scripts de manutenção eram *bash* dependentes do WSL (achado A1) e não rodavam no Windows.

## Decisão

Os scripts do repositório são escritos em Python (3.12 ou superior, só biblioteca padrão): `reorganizar_cgov.py`, `gerar_indices.py`, `link_acervo.py`, `publicar_operacao.py` e `verificar_sanitizacao.py`.

## Consequências

- Rodam no Windows com `py scripts\<script>.py`; os que alteram algo simulam por padrão e só gravam com `--executar`.
- Nenhum deles exclui arquivos na pasta CGOV: o que for substituído vai para a quarentena (ADR-014).
- Os `.sh` do WSL estão aposentados em `archive/scripts-wsl/`.

## Referências

Fases 4 e 5 do [plano de implantação](../plano-implantacao.md); decisões D37 a D40.

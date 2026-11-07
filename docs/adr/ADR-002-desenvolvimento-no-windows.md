# ADR-002 — Desenvolvimento no Windows; WSL aposentado

- **Status:** Aceito
- **Data:** 04/11/2026 (Fase 1)

## Contexto

O repositório vivia no WSL, e a publicação dependia de *bash*, `ln -s`, `rsync` e caminhos `/mnt/c` (achado A1).

## Decisão

Desenvolvimento em `C:\Projetos\cgov-geral` (Windows), sincronizado com o GitHub privado `lpchagas/cgov-geral`; o WSL é aposentado.

## Consequências

- Clone no Windows com `core.autocrlf=false` e `.gitattributes` com LF (etapa 5.7).
- Os scripts passam a Python (ADR-004); os `.sh` foram para `archive/scripts-wsl/`.
- A pasta do WSL é renomeada e excluída na Fase 8.5.

## Referências

Fases 1, 5 e 8 do [plano de implantação](../plano-implantacao.md).

# Scripts do WSL (aposentados em 07/11/2026)

`publicar-operacao.sh` e `link-acervo.sh` foram escritos para o repositório no WSL e para a estrutura
da pasta CGOV anterior à Fase 4 (`_acervo-escritorio-virtual/…`). Estavam bloqueados desde 06/11/2026,
salvo `publicar-operacao.sh --verificar`, e foram movidos para cá na Fase 5 (bloco 4, etapa 5.8 do plano de
implantação) depois que os substitutos em Python ficaram prontos:

| Script aposentado | Substituto |
|---|---|
| `publicar-operacao.sh` | `scripts/publicar_operacao.py` (`--verificar`; `--publicar`; `--publicar --executar`) |
| `link-acervo.sh` | `scripts/link_acervo.py` (simulação; `--executar`) |

Ficam aqui só como evidência histórica: não execute.

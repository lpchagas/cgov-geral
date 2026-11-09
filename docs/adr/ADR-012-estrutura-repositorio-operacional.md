---
tipo: decisao
status: aceito
atualizado_em: 2026-11-07
relacionados: [docs/fluxos-de-trabalho.md, operacao/LEIA-ME.md]
---

# ADR-012 — Estrutura do repositório operacional

- **Status:** Aceito
- **Data:** 05/11/2026 (Fase 2)

## Contexto

A pasta CGOV cresceu por acúmulo: duas árvores de processos, dois acervos normativos, três padrões de nome e nenhuma orientação escrita. Em 07/10 a operação já começou a unificar o trabalho da NT na pasta do processo (`_CGOV_NT`), sem registro no repositório.

| Dimensão | A. Manter e só documentar | B. Reorganização completa por **tipo de objeto** (proposta) | C. Reorganização por **inciso do Art. 37** |
|---|---|---|---|
| Encontrar um processo | Duas árvores | Uma pasta por processo, com índice | Processo pode caber em mais de um inciso |
| Esforço | Baixo | Médio (mapa CSV + script + lotes) | Alto |
| Estabilidade dos caminhos | Ruim | **Boa**: o tipo de objeto não muda | Ruim: o enquadramento pode mudar |
| Leitura por IA | Exige mapa de tradução | Convenção única no `AGENTS.md` | Exige classificação prévia |

## Decisão

**B**. O inciso do Art. 37 entra como **metadado** (`inciso_art37` no `PROCESSO.md`) e **coluna do índice**, e não como pasta. Assim é possível filtrar por inciso sem duplicar arquivos.

## Referências

Seções 5.2 e 5.3 e Fase 4 do [plano de implantação](../plano-implantacao.md); Decisão 28 do [decision-log](../governance/decision-log.md).

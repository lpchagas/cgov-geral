# ADR-014 — Exclusão controlada

- **Status:** Aceito
- **Data:** 05/11/2026 (Fase 2)

## Contexto

A reorganização da pasta CGOV identificou itens desnecessários e duplicados (Seção 5.6 do plano), e uma exclusão direta, sincronizada pelo Drive, poderia causar perda irreversível (risco "Perda de arquivo durante a movimentação", Seção 7).

## Decisão

Nenhum arquivo é excluído diretamente. Os candidatos vão para `99_arquivo/_a-excluir_AAAA-MM-DD/`, com a origem registrada no mapa de reorganização. Depois de **30 dias** sem necessidade de recuperação, o Coordenador exclui a pasta manualmente. A lixeira do Google Drive ainda guarda os arquivos por mais 30 dias. Arquivos idênticos só são eliminados depois de **conferência por SHA-256**, e sempre preservando uma cópia no destino canônico.

## Referências

Etapas 4.5 e 4.11 do [plano de implantação](../plano-implantacao.md); [`publicar_operacao.py`](../../scripts/publicar_operacao.py) aplica a mesma regra.

# Limitações do levantamento pelo PETRVS

1. Depende do preenchimento do campo `destinatario`, que varia entre unidades.
2. A classificação é léxica, não semântica: palavras iguais em contextos diferentes contam igual.
3. O PETRVS registra entregas do PGD, não é catálogo de serviços: serviços prestados sem entrega registrada
   não aparecem.
4. A granularidade das entregas varia entre unidades; o mesmo serviço pode aparecer com nomes diferentes.
5. O período analisado limita o resultado.
6. Não há deduplicação semântica entre unidades.
7. O nível hierárquico da unidade não é considerado.
8. O tipo de serviço é o do primeiro grupo de termos encontrado, na ordem fixa do script (por exemplo,
   "Atendimento ao público no centro de visitantes" sai como "Visitação / Uso Público em UC"); revise o tipo
   das entregas que combinam temas.
9. As entregas com pontuação 0 ou negativa ficam só no arquivo `carta_servicos_todas_<carimbo>.csv`, para
   auditoria do corte.

Por isso o resultado é uma lista de candidatos para confirmação pelas unidades.

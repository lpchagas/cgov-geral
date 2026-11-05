# Escritório CGOV — pasta de trabalho da Coordenação de Governança (ICMBio)

Esta pasta reúne o trabalho da CGOV: processos SEI, Notas Técnicas, normativos, colegiados, projetos
e gestão da coordenação. O assistente Claude (projeto "Escritório CGOV — Operação") usa esta mesma
pasta e segue estas regras (as regras para agentes de IA estão em AGENTS.md).

## Mapa
| Pasta | O que guarda |
|---|---|
| 00_entrada | Arquivos novos que ainda não sabemos onde guardar. Esvaziar toda semana |
| 01_processos | Uma pasta por processo SEI, com a ficha PROCESSO.md. Veja 01_processos/_INDICE.md |
| 02_notas-tecnicas | Série oficial de NTs e Informações assinadas, por ano. Veja o _INDICE.md |
| 03_normativos | Leis, decretos, portarias e INs (PDF + texto .md). Revogados em revogados/ |
| 04_colegiados | Pautas, atas e transcrições do CTGRIC, Conselho de Governança, CIG e CTGD |
| 05_projetos | Oficinas, eventos, parcerias e iniciativas sem processo SEI próprio |
| 06_gestao-da-coordenacao | Plano de entregas, PGD da equipe, planejamento e acompanhamento |
| 90_escritorio-virtual | Infraestrutura do assistente de IA. Não editar |
| 99_arquivo | Processos encerrados, versões superadas e quarentena de exclusão |

Cada pasta tem um _LEIA-ME.md com a finalidade, o que entra, o que não entra e o padrão de nome.

## Tenho um arquivo. Onde salvo?
| Se é… | Salve em… |
|---|---|
| Documento baixado do SEI | 01_processos/<processo>/documentos-sei |
| Rascunho, análise ou planilha de trabalho de um processo | 01_processos/<processo>/trabalho |
| Material de apoio (dados, mapas, estudos, áudios) | 01_processos/<processo>/referencias |
| Versão final enviada ao SEI | 01_processos/<processo>/produtos |
| NT ou Informação já assinada | 02_notas-tecnicas/<ano> (e registre no _INDICE.md) |
| Norma publicada | 03_normativos (o assistente transcreve e cataloga) |
| Material de reunião de colegiado | 04_colegiados/<colegiado> |
| Apresentação de oficina ou evento | 05_projetos/<AAAA-MM_apelido> |
| Não sei | 00_entrada (o assistente sugere o destino) |

## Como nomear
- Processo: SEI_<órgão>.<número>_<ano>-<dígito>_<apelido> — por exemplo, SEI_02070.000000_2026-00_exemplo
  (número SEI com "_" no lugar da barra; apelido curto em minúsculas, com hífen e sem acento)
- Documento do SEI: AAAAMMDD_SEI_<nº do documento>_<tipo>_<descrição>.pdf
- Projeto: AAAA-MM_<apelido>
- Versões: _v1, _v2…; ao concluir, as anteriores vão para 99_arquivo/versoes-anteriores

## Regras
- Nada se apaga: o que não serve vai para 99_arquivo/_a-excluir_<data> e é revisto em 30 dias.
- Sem nomes ou matrículas de servidores em fichas e índices (LGPD).
- Problemas com o assistente ou com as skills: 90_escritorio-virtual/manutencao/PENDENCIAS.md.

## Como pedir ajuda ao Claude (projeto "Escritório CGOV — Operação")
"Abra o processo <apelido> e resuma o andamento" · "Preciso de uma Nota Técnica sobre…"
· "Classifique o que está em 00_entrada" · "Atualize os índices"

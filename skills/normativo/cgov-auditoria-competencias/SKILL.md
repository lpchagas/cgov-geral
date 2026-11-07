---
name: cgov-auditoria-competencias
description: >
  Use esta skill para identificar duplicidades, sobreposições ou conflitos de competência
  entre unidades em um texto normativo do ICMBio (portaria, IN, resolução). Gatilhos:
  "AUDITORIA_COMPETENCIAS", "auditoria de competências", "sombreamento", "sobreposição
  de funções", "duplicidade de competência", "quem faz o quê nessa portaria", "conflito
  de atribuições", "mapeamento de verbos", "matriz RACI", "quem executa e quem aprova",
  "responsabilidades duplicadas", "varredura na minuta", "há sobreposição entre",
  "brigas de competência", "lacuna de responsabilidade". Acione quando o usuário colar
  artigos de ato normativo e pedir para verificar conflito ou ambiguidade sobre quem é
  responsável por cada ação — mesmo sem usar os termos acima. Frequentemente acionada
  após MODELAR_FLUXO ou COMPARAR_VERSOES.
---

# SKILL: Auditoria de Competências — CGOV/ICMBio

Você está no modo **AUDITORIA_COMPETENCIAS**. O objetivo é fazer uma varredura
sistemática no texto normativo fornecido, extrair todas as atribuições de cada
unidade/papel, detectar sobreposições (sombreamento) e lacunas de responsabilidade,
e propor a Matriz RACI que tornaria o texto operacionalmente seguro.

Este trabalho é preventivo: identificar aqui os conflitos de competência evita brigas
institucionais após a publicação do ato normativo.

---

## CONTEXTO INSTITUCIONAL

Os atores, prazos e competências vêm **do próprio ato analisado** e do Regimento
Interno do ICMBio: identifique-os no texto, sem presumir um contexto padrão. Se o
ato tratar de prevenção ao assédio ou de regime disciplinar (como o PSPEADBio, ato
de referência em que esta skill nasceu), os atores típicos são:
Ouvidoria, Corregedoria, CGGP (Coordenação-Geral de Gestão de Pessoas), PFE
(Procuradoria Federal Especializada), Comissão de Ética, chefias imediatas,
DIRAD (Diretoria de Administração), Presidência do ICMBio e Comitê de Prevenção
ao Assédio.

Normas de referência para competências institucionais (o Regimento Interno vale
sempre; as demais, conforme o tema do ato):
- Regimento Interno do ICMBio (Portaria nº 5.592/2025 ou vigente)
- Lei nº 8.112/1990 (competências disciplinares)
- Decreto nº 12.122/2024 (competências do programa federal de assédio)

---

## FASE 1 — COLETA DE DADOS

Solicite apenas o que não foi fornecido:

1. **Texto normativo:** Cole os artigos ou capítulos a serem auditados. Quanto mais
   completo o texto, mais precisa a auditoria — idealmente inclua o capítulo de
   competências/atribuições e os capítulos procedimentais.
2. **Escopo da auditoria:** Varredura completa da minuta ou apenas um capítulo/tema
   específico? (ex.: "só as competências relacionadas a denúncias" ou "toda a portaria")
3. **Suspeita prévia (se houver):** O usuário já identifica algum conflito específico?
   Se sim, dê atenção redobrada a esse ponto, mas realize a varredura completa de
   qualquer forma.

> Se o texto já foi trabalhado com COMPARAR_VERSOES ou MODELAR_FLUXO nesta sessão,
> use a versão mais recente disponível sem pedir o texto novamente.

---

## FASE 2 — EXTRAÇÃO E ANÁLISE

Antes de gerar a resposta, raciocine internamente:

**Passo 1 — Extração de verbos por unidade:**
Para cada unidade/papel mencionado no texto, liste todos os verbos de ação que lhe
são atribuídos. Organize por unidade, não por artigo. Um mesmo verbo pode aparecer
em múltiplos artigos — registre todas as ocorrências com a referência do artigo.

Classifique cada verbo em uma das três categorias:
- **Executa (E):** a unidade realiza a ação diretamente
- **Aprova/Decide (A):** a unidade valida ou decide sobre o resultado de outra
- **É informada (I):** a unidade recebe notificação mas não age diretamente

**Passo 2 — Detecção de sombreamentos:**
Identifique casos em que:
(a) Duas unidades recebem o mesmo verbo para o mesmo objeto (ex.: ambas "recebem
    denúncias" sem critério de separação)
(b) Uma unidade executa e ao mesmo tempo aprova o próprio resultado (concentração
    indevida de poderes)
(c) Um objeto (denúncia, relatório, decisão) não tem nenhuma unidade responsável
    por uma etapa essencial (lacuna de responsabilidade)
(d) O texto usa verbos vagos ("coordena", "acompanha", "apoia") sem deixar claro
    se a unidade executa ou apenas observa

**Passo 3 — Avaliação de impacto:**
Para cada sombreamento ou lacuna, pense no cenário prático: o que acontece quando
duas unidades recebem uma denúncia no mesmo dia? Quem decide? Há risco de
inação por falta de responsável claro? Há risco de conflito por excesso de
responsáveis?

---

## FASE 3 — GERAÇÃO DA RESPOSTA

Numere os conflitos `C-01`, `C-02`… e as lacunas sistêmicas `LS-01`… (convenção
de códigos da `cgov-nt-03`). Classifique cada competência contra o Regimento
Interno vigente e corrija a premissa do pedido quando a fonte a contrariar.

Use **exatamente** o seguinte formato:

---

### Auditoria de Competências (Matriz de Conflitos)

**Escopo auditado:** [Artigos/Capítulos analisados]

---

**1. Mapeamento de Verbos de Ação:**

Para cada unidade, liste as ações em formato de tabela compacta:

| Unidade | Verbo/Ação | Artigo | Categoria (E/A/I) |
| :--- | :--- | :--- | :--- |
| Ouvidoria | Receber denúncias | Art. 14, caput | E |
| Ouvidoria | Encaminhar à Corregedoria | Art. 14, § 1º | E |
| ... | ... | ... | ... |

*(Inclua todas as unidades e todas as ações identificadas no texto)*

---

**2. Sombreamentos e Lacunas Identificados:**

Para cada problema encontrado:

> **[Tipo: Sombreamento / Lacuna / Concentração / Verbo vago]**
>
> **Conflito:** [Descrição precisa — ex.: "O Art. 14 e o Art. 22 atribuem tanto à
> Ouvidoria quanto ao Comitê a função de 'acolher' o denunciante, sem critério de
> separação temporal ou por tipo de caso."]
>
> **Artigos envolvidos:** Art. X e Art. Y
>
> **Impacto Operacional:** [O que ocorre na prática — ex.: "Em um caso real, tanto
> a Ouvidoria quanto o Comitê poderão acionar o denunciante simultaneamente, gerando
> sobrecarga e confusão sobre qual instância é o ponto de contato oficial."]

*(Se não houver sombreamentos, diga explicitamente: "Não foram identificados
sombreamentos de competência no escopo auditado." e passe para a seção 3.)*

---

**3. Recomendação de Ajuste Organizacional (Matriz RACI):**

Apresente a Matriz RACI proposta para as funções em conflito:

| Função/Atividade | [Unidade A] | [Unidade B] | [Unidade C] |
| :--- | :---: | :---: | :---: |
| [Atividade 1] | **R** | I | — |
| [Atividade 2] | I | **A** | **R** |
| [Atividade 3] | — | **R** | C |

*Legenda: **R** = Responsável (executa) | **A** = Aprovador (decide) | **C** =
Consultado (contribui) | **I** = Informado (notificado) | — = Não envolvido*

**Proposta de ajuste normativo:** Para cada sombreamento, sugira a redação corretiva:

> **Para o Conflito [N]:** Substitua [texto atual] por:
> "[nova redação que delimita claramente a competência de cada unidade]"
> Justificativa: [por que essa separação é mais clara e operacionalmente viável]

---

## REGRA ESPECIAL: LACUNA SISTÊMICA

Se a auditoria revelar que uma função essencial (ex.: recebimento de denúncias,
notificação do investigado, decisão final sobre penalidade) não tem nenhuma unidade
claramente responsável em todo o texto, destaque com:

> **⚠️ LACUNA SISTÊMICA:** A função de [descrever] não está atribuída a nenhuma
> unidade no texto auditado. Se publicado assim, o processo ficará sem responsável
> para [consequência prática]. Recomenda-se incluir dispositivo expresso atribuindo
> essa função a [unidade sugerida, com justificativa].

---

## SAÍDA FINAL

Após a Matriz RACI, pergunte:

> "Deseja que eu modele o fluxo processual corrigido com base nesta RACI
> (MODELAR_FLUXO) ou que eu compare versões de algum dispositivo específico
> (COMPARAR_VERSOES)?"

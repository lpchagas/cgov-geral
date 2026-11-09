---
name: pgd-implementar-indicador
description: >
  Desenha e escreve a infraestrutura de automação (DataOps) para que o script de um
  indicador do PGD rode automaticamente e alimente as planilhas institucionais.
  Use esta skill sempre que o usuário quiser automatizar, agendar ou colocar em produção
  um script de indicador. Gatilhos típicos: "/implementar_indicador", "como rodo isso
  automaticamente?", "quero que o script rode todo mês", "como agendar a execução?",
  "preciso que o Excel seja atualizado sozinho", "o que é Airflow?", "cron job",
  "pipeline de dados", "colocar em produção", "automatizar o cálculo do indicador",
  "como faço para não precisar rodar na mão?", "DataOps", "orquestração do script",
  "DAG para o indicador", "alimentar o instrumento PGD automaticamente".
  Acione também quando o usuário perguntar como fazer o script gerar o Excel final.
---

# Skill: implementar_indicador

Você é um Tech Lead em Data Science com especialidade em DataOps. Seu usuário é iniciante
em programação e infraestrutura de TI — explique cada conceito de orquestração com
analogias de negócio antes de mostrar qualquer código.

## O que fazer

Execute os 4 passos obrigatoriamente nesta ordem.

---

### Passo 1 🧩 Divisão da Tarefa (Task Breakdown)

Identifique:
- Qual indicador/script será automatizado (número e nome)
- Com que frequência deve rodar (diária, semanal, mensal)
- Onde o resultado será persistido (aba do Excel, banco de dados, ou ambos)
- Nível de complexidade do pipeline (simples = 1 script; complexo = múltiplos scripts
  com dependências)

Liste as subtarefas: decisão de orquestração, código, teste de agendamento.

---

### Passo 2 🗺️ Raciocínio e Arquitetura de Orquestração (Chain of Thought)

**2.1 — Qual ferramenta de automação usar?**

| Cenário | Ferramenta | Quando usar |
|---|---|---|
| 1 script, execução simples (mensal/semanal) | **Cron + Shell Script** (Linux) | Ideal para começar. Sem interface, mas confiável. |
| Múltiplos scripts com dependências entre si | **Apache Airflow** | Quando o Indicador B depende do resultado do Indicador A |
| Execução agendada em Windows sem servidor Linux | **Agendador de Tarefas do Windows** | Ambiente sem servidor Linux disponível |

> 💡 **O que isso significa na prática:** Pense no Cron como um **relógio despertador**:
> você configura "toca todo dia 1º do mês às 6h" e ele acorda o script na hora certa.
> O Airflow, por sua vez, é como um **maestro de orquestra**: ele sabe a ordem exata em
> que cada instrumento (script) deve tocar, e se um falhar, ele avisa e para o show.

**2.2 — Onde persistir o resultado?**

- **Excel institucional** (`SIGLA_Instrumento_PGD_2025.xlsx`): use `openpyxl` para
  escrever diretamente nas abas "Insira os dados". Ideal para o fluxo atual do ICMBio.
- **Banco de dados (tabela de resultados)**: insira na tabela `fato_resultados_pgd`
  para histórico. Permite gráficos e dashboards no Power BI/Tableau.
- **Ambos**: o script calcula uma vez e salva nos dois destinos.

---

### Passo 3 🔄 Opções de Implementação (Self-Consistency)

**Opção A — Cron Job (Linux/servidor):** Um arquivo `.sh` agendado com `crontab`.
Leve, sem dependências extras. Recomendado quando há um servidor Linux disponível.

**Opção B — Apache Airflow DAG:** Um arquivo Python com a definição do fluxo.
Mais poderoso: reexecuta tarefas falhas, envia alertas por e-mail, tem interface visual.
Recomendado quando há mais de 3 scripts interdependentes ou quando a equipe precisa
de visibilidade do pipeline.

Escolha a opção e justifique para o contexto do projeto.

---

### Passo 4 ✅ Solução Detalhada e Execução (Código Completo)

#### 4.1 — Script Python com persistência no Excel (openpyxl)

```python
# ============================================================
# IMPLEMENTAÇÃO — INDICADOR X: [NOME]
# Objetivo: calcular o indicador e gravar o resultado no Excel
# Requisitos: pip install pandas sqlalchemy pymysql openpyxl
# ============================================================

import pandas as pd
import openpyxl                            # biblioteca para manipular Excel
from sqlalchemy import create_engine
from datetime import datetime
import logging                             # sistema de registro de eventos

# --- 1. CONFIGURAÇÃO DE LOGS ---
# O log é o "diário de bordo" do script: registra o que aconteceu e quando.
# Se algo der errado às 3h da manhã, o log vai te contar o que foi.
logging.basicConfig(
    filename='pgd_indicador_x.log',        # arquivo de log criado na mesma pasta
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def calcular_indicador_x() -> float:
    """
    Extrai dados do Data Mart Petrvs e calcula o Indicador X.
    Retorna o valor final como float (ex.: 73.5 para 73,5%).
    """
    logging.info("Iniciando cálculo do Indicador X...")
    
    try:
        # 2. CONEXÃO COM O BANCO
        engine = create_engine("mysql+pymysql://usuario:senha@host:3306/dm_petrvs")
        logging.info("Conexão com o banco estabelecida.")
        
        # 3. EXTRAÇÃO
        query = """
            SELECT fe.vinculado_pei, COUNT(*) AS total
            FROM fato_entregas fe
            INNER JOIN dim_tempo dt ON fe.id_tempo = dt.id_tempo
            WHERE dt.ano = 2025 AND fe.status_plano <> 'CANCELADO'
            GROUP BY fe.vinculado_pei
        """
        df = pd.read_sql(query, engine)
        
        # 4. CÁLCULO
        total_geral     = df['total'].sum()
        total_vinculados = df.loc[df['vinculado_pei'] == 1, 'total'].sum()
        taxa = round((total_vinculados / total_geral * 100), 2) if total_geral > 0 else 0
        
        logging.info(f"Cálculo concluído: {total_vinculados}/{total_geral} = {taxa}%")
        return taxa
        
    except Exception as e:
        # Se qualquer coisa der errado, registra o erro e não deixa passar silencioso
        logging.error(f"ERRO ao calcular o indicador: {e}")
        raise  # relança o erro para que o orquestrador (Cron/Airflow) saiba que falhou


def gravar_no_excel(valor: float, caminho_excel: str, aba: str, celula: str) -> None:
    """
    Abre o arquivo Excel institucional e grava o resultado na célula indicada.
    
    Exemplo de uso:
        gravar_no_excel(73.5, "ICMBio_Instrumento_PGD_2025.xlsx", "Ind_01", "E21")
    
    Por que usar openpyxl? Porque ele consegue abrir um Excel já existente —
    com fórmulas, cores e formatação — e apenas atualizar uma célula específica,
    sem destruir o restante do arquivo.
    """
    try:
        wb = openpyxl.load_workbook(caminho_excel)    # abre o arquivo Excel existente
        ws = wb[aba]                                   # seleciona a aba correta
        ws[celula] = valor                             # escreve o valor na célula
        wb.save(caminho_excel)                         # salva sem sobrescrever o resto
        logging.info(f"Valor {valor} gravado em {caminho_excel} → aba '{aba}' → célula {celula}")
        print(f"✅ Excel atualizado: {aba} / {celula} = {valor}%")
    except Exception as e:
        logging.error(f"ERRO ao gravar no Excel: {e}")
        raise


# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    ARQUIVO_EXCEL = "ICMBio_Instrumento_PGD_2025.xlsx"
    
    taxa = calcular_indicador_x()
    gravar_no_excel(taxa, ARQUIVO_EXCEL, aba="Ind_01", celula="E21")
    
    print(f"\n🎯 Pipeline concluído: {taxa}% gravado com sucesso.")
    print(f"📄 Log salvo em: pgd_indicador_x.log")
```

#### 4.2 — Opção A: Cron Job (Linux/servidor)

```bash
#!/bin/bash
# ============================================================
# SCRIPT DE AGENDAMENTO — indicador_x.sh
# Executa o cálculo do indicador todo dia 1º do mês às 6h
# ============================================================

# Onde está o Python com os pacotes instalados?
PYTHON_PATH="/usr/bin/python3"

# Onde está o script do indicador?
SCRIPT_PATH="/<pasta-do-servidor>/scripts/indicador_x.py"

# Arquivo de log (separado do log do Python para registrar erros de sistema)
LOG_FILE="/<pasta-do-servidor>/logs/cron_indicador_x.log"

echo "$(date) — Iniciando execução agendada do Indicador X" >> "$LOG_FILE"

# Executa o script Python e redireciona qualquer erro para o log
$PYTHON_PATH $SCRIPT_PATH >> "$LOG_FILE" 2>&1

# Verifica se o script terminou com sucesso (código de saída 0 = OK)
if [ $? -eq 0 ]; then
    echo "$(date) — ✅ Concluído com sucesso" >> "$LOG_FILE"
else
    echo "$(date) — ❌ ERRO na execução. Verifique o log do Python." >> "$LOG_FILE"
fi
```

Para agendar, adicione ao `crontab` do servidor:

```bash
# Para editar o crontab: crontab -e
# Formato: minuto hora dia_mes mês dia_semana comando

# Executar todo dia 1º do mês às 06:00
0 6 1 * * /<pasta-do-servidor>/scripts/indicador_x.sh

# Executar toda segunda-feira às 07:00
0 7 * * 1 /<pasta-do-servidor>/scripts/indicador_x.sh
```

> 🖥️ **Como configurar no servidor:** Conecte via SSH → digite `crontab -e` → adicione
> a linha acima → salve (Ctrl+O, Enter, Ctrl+X no nano) → pronto. O servidor vai lembrar
> de rodar mesmo que você desligue seu computador.

#### 4.3 — Opção B: Apache Airflow DAG (para pipelines complexos)

```python
# ============================================================
# AIRFLOW DAG — pipeline_pgd_indicadores.py
# Orquestra múltiplos indicadores em sequência segura
# ============================================================

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Importa as funções de cálculo de cada indicador
from indicador_01 import calcular_ind01
from indicador_02 import calcular_ind02
from indicador_03 import calcular_ind03

# --- CONFIGURAÇÕES PADRÃO DA DAG ---
# Essas configurações são aplicadas a todas as tarefas automaticamente
args_padrao = {
    'owner': 'cgov_icmbio',             # responsável pelo pipeline
    'retries': 2,                        # tenta 2x antes de declarar falha
    'retry_delay': timedelta(minutes=5), # aguarda 5 min entre tentativas
    'email_on_failure': True,            # envia e-mail se falhar
    'email': ['<e-mail institucional da equipe>'],
}

# --- DEFINIÇÃO DA DAG ---
# A DAG é o "mapa" do pipeline: quais tarefas rodam e em que ordem
with DAG(
    dag_id='pipeline_pgd_2025',          # identificador único da DAG
    description='Calcula e publica todos os indicadores do PGD/ICMBio',
    schedule_interval='0 6 1 * *',       # todo dia 1º do mês às 6h (formato cron)
    start_date=datetime(2025, 1, 1),
    catchup=False,                        # não recalcula datas passadas
    default_args=args_padrao,
    tags=['pgd', 'icmbio', 'indicadores'],
) as dag:
    
    # Tarefa 1: calcula indicadores independentes (rodam em paralelo)
    tarefa_ind01 = PythonOperator(
        task_id='calcular_ind01',
        python_callable=calcular_ind01,
    )
    
    tarefa_ind02 = PythonOperator(
        task_id='calcular_ind02',
        python_callable=calcular_ind02,
    )
    
    # Tarefa 2: Ind_03 depende dos resultados do Ind_01 (rodam em sequência)
    tarefa_ind03 = PythonOperator(
        task_id='calcular_ind03',
        python_callable=calcular_ind03,
    )
    
    # Define a ordem: Ind_01 e Ind_02 rodam primeiro (em paralelo),
    # depois Ind_03 roda (pois depende deles)
    [tarefa_ind01, tarefa_ind02] >> tarefa_ind03
```

> 💡 **O que isso significa na prática:** Imagine o Airflow como um **gerente de projetos
> digital**. Você diz a ele: "Primeiro faça A e B (podem ser simultâneos), depois faça C".
> Se B falhar, ele te avisa por e-mail, tenta novamente 2 vezes e não começa C até que
> tudo esteja certo. Você acompanha tudo numa interface visual, como um kanban de tarefas.

---

## Checklist de deploy (antes de ir para produção)

Antes de ativar o agendamento, confirme:

- [ ] O script passou pela auditoria `/testar_indicador` sem erros críticos
- [ ] As credenciais do banco estão em variável de ambiente (não hardcoded no código)
- [ ] O arquivo Excel de destino existe e a aba/célula estão corretas
- [ ] O log está configurado e gravando em local com espaço suficiente
- [ ] Há alguém responsável por monitorar o log ao menos uma vez por mês

---

## Regras inegociáveis

- Nunca mostrar Airflow como primeira opção para um script simples de único indicador.
  Cron + Shell é a recomendação padrão para iniciantes.
- Sempre incluir `try/except` com `logging.error()` — script silencioso que falha é o
  pior cenário em produção governamental.
- Nunca embutir senhas no código. Usar `os.environ.get('DB_PASSWORD')` ou arquivo `.env`.
- Sempre fechar com o Checklist de deploy acima.
- Sempre mencionar: "Parabéns — você acaba de criar um pipeline de dados governamental!
  Isso significa que o ICMBio terá dados de desempenho atualizados automaticamente,
  sem depender de planilhas manuais."

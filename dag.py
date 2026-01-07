from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner' : 'sanso',
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5)
}

with DAG(
    dag_id='executar_script',
    default_args=default_args,
    description='Roda a cada 24 horas',
    start_date = datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['python', 'etl']
) as dag:
    rodar_script = BashOperator(
        task_id = 'rode_legal',
        bash_command = 'pip install unidecode && python /home/sanso/Área de trabalho/PYTHON /estadao-bs4/'
    )

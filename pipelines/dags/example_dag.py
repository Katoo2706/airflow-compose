from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule='0 0 * * *',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:
    start = EmptyOperator(
        task_id='start',
    )

    hello_world = BashOperator(
        task_id='hello_world',
        bash_command='echo "Hello, World!, This is version 2"',
    )

    end = EmptyOperator(
        task_id='end',
    )

    start >> hello_world >> end

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from utils.dbt_command import run_dbt
from config.constants import Constants

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    # 'retry_delay': timedelta(seconds=5),
}

with DAG(
    'dbt_example_dag',
    default_args=default_args,
    description='A simple DAG to run dbt commands',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['dbt', 'example'],
) as dag:

    dbt_debug = PythonOperator(
        task_id='dbt_debug',
        python_callable=run_dbt,
        op_kwargs={
            'dbt_project_dir': Constants.DBT_PROJECT_DIR,
            'command': 'dbt debug'
        }
    )

    dbt_run = PythonOperator(
        task_id='dbt_run',
        python_callable=run_dbt,
        op_kwargs={
            'dbt_project_dir': Constants.DBT_PROJECT_DIR,
            'command': 'dbt run'
        }
    )

    dbt_test = PythonOperator(
        task_id='dbt_test',
        python_callable=run_dbt,
        op_kwargs={
            'dbt_project_dir': Constants.DBT_PROJECT_DIR,
            'command': 'dbt test'
        }
    )

    # Define the task dependencies
    dbt_debug >> dbt_run >> dbt_test




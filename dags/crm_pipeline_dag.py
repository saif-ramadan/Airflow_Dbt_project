from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Seif',
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='crm_data_pipeline',
    default_args=default_args,
    description='Full End-to-End Pipeline project',
    start_date=datetime(2005, 4, 24),
    schedule='@daily',
    catchup=False,
) as dag:

    # first task: 
    ingest_data = BashOperator(
        task_id='ingest_data',
        bash_command='python /usr/local/airflow/scripts/ingest_to_duckdb.py',
    )

    # second task
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /usr/local/airflow/crm_dbt && dbt run --profiles-dir .',
    )

    #third task
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /usr/local/airflow/crm_dbt && dbt test --profiles-dir .',
    )

    # dependancies
    ingest_data >> dbt_run >> dbt_test
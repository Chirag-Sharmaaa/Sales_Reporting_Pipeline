from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'chirag',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# Define the DAG
with DAG(
    dag_id='sales_reporting_pipeline',
    default_args=default_args,
    description='Daily ETL and DBT model refresh for Sales Reporting',
    start_date=datetime(2025, 7, 28),
    schedule_interval='@daily',  # Runs daily at midnight
    catchup=False
) as dag:

    # Task 1: Ingest the CSV into PostgreSQL
    ingest_csv = BashOperator(
        task_id='ingest_csv_to_postgres',
        bash_command='python "C:/Users/chira/Desktop/Sales_Reporting_Pipeline/airflow_dags/scripts/ingest_csv.py"'
    )

    # Task 2: Run DBT models using batch file
    run_dbt = BashOperator(
        task_id='run_dbt_models',
        bash_command='"C:/Users/chira/Desktop/Sales_Reporting_Pipeline/airflow_dags/scripts/run_dbt.bat"'
    )

    # Set task order
    ingest_csv >> run_dbt

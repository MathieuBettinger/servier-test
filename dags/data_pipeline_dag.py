from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_data_pipeline_dag',
    default_args=default_args,
    description='A DAG to run a data pipeline Docker container',
    schedule_interval=timedelta(days=1),
)

run_pipeline = DockerOperator(
    task_id='run_data_pipeline',
    image='my-data-pipeline',  # Name of your Docker image
    api_version='auto',
    auto_remove=True,
    dag=dag
)

run_pipeline
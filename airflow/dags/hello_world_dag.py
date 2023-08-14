from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

with DAG(
    "hello_world_dag",
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag:
    def print_hello():
        print("Hello world! Airflow")

    tarefa = PythonOperator(
        task_id='hello_world',
        python_callable=print_hello
    )

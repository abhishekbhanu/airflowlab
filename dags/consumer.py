from airflow import DAG,Dataset
from airflow.decorators import task

from datetime import datetime

advocate_file = Dataset('/tmp/advocate_file.txt')

with DAG(
    dag_id='Consumer',
    start_date=datetime(2023,4,17),
    schedule=[advocate_file],
    catchup=False
) as dag:
    
    @task
    def read_dataset():
        with open(advocate_file.uri,'r') as f:
            print(f.read())

    read_dataset()


from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

advocate_file = Dataset('/tmp/advocate_file.txt')

with DAG(
    dag_id= "producer",
    start_date=datetime(2023,4,17),
    schedule='@daily',
    catchup=False
) as dag:

    @task(outlets = advocate_file)
    def update_dataset():
        with open(advocate_file.uri,'a+') as f:
            f.write('producer update')
    
    update_dataset()
    

from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
import sys

from quotegenerator.dailyquotegenerator import getdailyquote

with DAG(
    dag_id= 'dailyquote',
    start_date=datetime(2023,4,16),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    
    
    getdailyquote = PythonOperator(
        task_id = 'getdailyquote',
        python_callable=getdailyquote,
        op_kwargs={"filepath" : "/opt/airflow/data/dailymotivationalquotes.txt"}
    )

    getdailyquote

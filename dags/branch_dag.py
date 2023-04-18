from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator


from datetime import datetime

def _t1(ti):
    ti.xcom_push(key="key1", value= 42)

def _t2():
    print("t2 executed")

def _t3():
    print("t3 executed")

def _t4():
    print("t4 executed")

def _branch(ti):
    val = ti.xcom_pull(key='key1',task_ids= 'T1')
    if val == 42:
        return 'T2'
    return 'T3'

with DAG(
    dag_id= 'branching_test',
    start_date=datetime(2023,4,17),
    schedule='@daily',
    catchup=False
) as dag:
    

    @task.
    t1 = PythonOperator(
        task_id = 'T1',
        python_callable=_t1
    )

    branch = BranchPythonOperator(
        task_id = 'branch',
        python_callable=_branch
    )

    t2 = PythonOperator(
        task_id = 'T2',
        python_callable=_t2
    )
    t3 = PythonOperator(
        task_id = 'T3',
        python_callable=_t3
    )
    t4 = PythonOperator(
        task_id = 't4',
        python_callable=_t4,
        trigger_rule = "all_success"
    )

    t1 >> branch >> [t2,t3] >> t4



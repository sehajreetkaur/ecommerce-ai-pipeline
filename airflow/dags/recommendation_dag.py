from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='recommendation_pipeline',
    default_args=default_args,
    description='Generate product recommendations using collaborative filtering and GenAI',
    schedule_interval='@weekly',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['ecommerce', 'recommendations', 'genai'],
) as dag:

    collaborative_filter = BashOperator(
        task_id='collaborative_filter',
        bash_command='python /opt/airflow/src/ml/collaborative_filter.py',
    )

    product_similarity = BashOperator(
        task_id='product_similarity',
        bash_command='python /opt/airflow/src/ml/product_similarity.py',
    )

    genai_recommend = BashOperator(
        task_id='genai_recommend',
        bash_command='python /opt/airflow/src/genai/recommend.py',
    )

    [collaborative_filter, product_similarity] >> genai_recommend

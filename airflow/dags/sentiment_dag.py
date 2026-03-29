from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='sentiment_analysis_pipeline',
    default_args=default_args,
    description='Run AI sentiment analysis on new customer reviews',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['ecommerce', 'sentiment', 'genai'],
) as dag:

    run_sentiment = BashOperator(
        task_id='run_sentiment_analysis',
        bash_command='python /opt/airflow/src/genai/sentiment.py',
    )

    run_sentiment

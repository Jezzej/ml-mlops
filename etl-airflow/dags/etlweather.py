from airflow import DAG
from airflow.providers.https.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago

LATITUDE = '51.507'
LONGITUDE = '-0.1278'
POSTGRES_CONN_ID = 'postgres_deafult'
API_CONN_ID = 'open-api'

default_args = {
    'owner' : 'jess',
    'start_date': days_ago(1)
}

with DAG(
    dag_id = 'weather-etl-pipeline',
    default_args = default_args,
    schdule_interval = '@daily',
    catchup = False) as dags:

    @task()

    def extract():
        
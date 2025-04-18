from airflow.decorators import dag, task
from pendulum import datetime
from src.extract import extract_weather_data
from src.transform import transform_data
from src.load_mongodb import insert_data_mongodb
import logging

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"owner": "cleave", "retries": 2},
    tags=["weather", "etl"],
)
def weather_etl_dag():

    @task()
    def extract():
        data = extract_weather_data()
        return data

    @task()
    def transform(data):
        transformed = transform_data(data)
        logging.info(f"Transformed data: {transformed}")
        return transformed

    @task()
    def load(data):
        inserted_id = insert_data_mongodb(data, "cleavestone94", "weather_data")
        print(f"Inserted document with ID: {inserted_id}")

    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)

weather_etl_dag()

from src.transform import transform_data
from src.extract import extract_weather_data
from dotenv import load_dotenv
import pymongo
import os
import certifi

ca=certifi.where()
import logging


def insert_data_mongodb(records, database, collection):
        """Insert records into MongoDB."""
        load_dotenv()
        MONGO_DB_URI = os.getenv("MONGO_DB_URI")
        try:
            mongo_client = pymongo.MongoClient(MONGO_DB_URI, tlsCAFile=ca)
            db = mongo_client[database]

            logging.info(f"Total records inserted: {len(records)}")
            return len(records)
        except Exception as e:
            logging.error(f"Error inserting data into MongoDB: {e}")
            return 0

if __name__ == "__main__":
    data = extract_weather_data()
    transformed_data = transform_data(data)
    records_inserted = insert_data_mongodb(transformed_data, "cleavestone94", "weather_data")
    print(f"Inserted {records_inserted} records into MongoDB.")
import pandas as pd
import numpy as np
import json
import datetime
from src.extract import extract_weather_data as extract
import requests
import logging

def convert_unix_to_iso(unix_time, tz_offset=0):
    return datetime.datetime.fromtimestamp(unix_time + tz_offset).isoformat()


def transform_data(data:list):
    """
    Transform the extracted weather data into a JSON format suitable
    for loading into a mongodb database.
    """

    formatted_data = []

    for entry in data:
        transformed = {
            "city_id": entry.get("id"),
            "city_name": entry.get("name"),
            "country": entry.get("country"),
            "coordinates": entry.get("coord"),
            "weather": entry.get("weather"),
            "base": entry.get("base"),
            "main": entry.get("main"),
            "visibility": entry.get("visibility"),
            "wind": entry.get("wind"),
            "clouds": entry.get("clouds"),
            "rain": entry.get("rain", {}),  # Optional field
            "timestamp": convert_unix_to_iso(entry.get("dt"), entry.get("timezone")),
            "sunrise": convert_unix_to_iso(entry["sys"].get("sunrise"), entry.get("timezone")),
            "sunset": convert_unix_to_iso(entry["sys"].get("sunset"), entry.get("timezone")),
            "timezone_offset": entry.get("timezone"),
            "cod": entry.get("cod")
        }
        logging.info(f"Transformed data for city: {transformed['city_name']}")
        formatted_data.append(transformed)
    
    # You can now dump this to a JSON file for MongoDB
    with open('data/weather_data_formatted.json', 'w') as f:
        json.dump(formatted_data, f, indent=4)

    return formatted_data



import pandas as pd
import requests
from dotenv import load_dotenv
import os
import logging


def extract_weather_data() -> list:
    """
    Extracts weather data from Nairobi, Mombasa, Kisumu, Nakuru ,Eldoret , Nyeri and Meru
    from OpenWeather API and returns JSON response
    """
    load_dotenv()
    api_key=os.getenv("WEATHER_API_KEY")
    cities ={
        'Nairobi': {'lat': -1.286389, 'lon': 36.817223},
        'Mombasa': {'lat': -4.043477, 'lon': 39.668206},
        'Kisumu': {'lat': -0.091703, 'lon': 34.767956},
        'Nakuru': {'lat': -0.303099, 'lon': 36.0662},
        'Eldoret': {'lat': 0.512778, 'lon': 35.269722},
        'Nyeri': {'lat': -0.419444, 'lon': 36.953056},
        'Meru': {'lat': -0.047778, 'lon': 37.641944},
        'Eldama Ravine': {'lat': 0.083333, 'lon': 35.783333},
        'Kericho': {'lat': -0.366667, 'lon': 35.283333},
        'Embu': {'lat': -0.416667, 'lon': 37.45},
        'Kitale': {'lat': 1.033333, 'lon': 34.983333},
        'Bomet': {'lat': -0.983333, 'lon': 35.766667},
        'Bungoma': {'lat': 0.566667, 'lon': 34.566667},
        'Busia': {'lat': 0.45, 'lon': 34.083333},
        'Homa Bay': {'lat': -0.533333, 'lon': 34.583333},
        'Migori': {'lat': -1.066667, 'lon': 34.466667},
        'Narok': {'lat': -1.083333, 'lon': 35.9},
        'Nakuru': {'lat': -0.303099, 'lon': 36.0662},
        'Nyandarua': {'lat': -0.083333, 'lon': 36.5},
        'Nyeri': {'lat': -0.419444, 'lon': 36.953056},
        'Othaya': {'lat': -0.5, 'lon': 36.95},
        'Ruiru': {'lat': -1.033333, 'lon': 36.933333}, 
        'Thika': {'lat': -1.033333, 'lon': 37.083333},
        'Uasin Gishu': {'lat': 0.5, 'lon': 35.283333},
        'Vihiga': {'lat': -0.283333, 'lon': 34.566667},
        'West Pokot': {'lat': 1.083333, 'lon': 35.283333}
         
    }
    
    extracted_data=[]

    try:
        for metadata  in cities.values():
            lat=metadata['lat']
            lon=metadata['lon']
            url: str= f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
            data = requests.get(url).json()
            extracted_data.append(data)
        logging.info(f"Extracted data for {len(extracted_data)} cities.")
        return extracted_data

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    print(extract_weather_data())



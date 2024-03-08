from collections import OrderedDict
from datetime import datetime, timedelta
from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')


class WeatherCache:
    def __init__(self, capacity=10):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Проверка, не устарели ли данные
        if key not in self.cache or self.cache[key]['timestamp'] + timedelta(minutes=10) < datetime.now():
            return None
        self.cache.move_to_end(key)
        return self.cache[key]['data']

    def set(self, key, value):
        self.cache[key] = {'data': value, 'timestamp': datetime.now()}
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class WeatherSDK:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.cache = WeatherCache()

    def get_weather_by_city(self, city_name):
        cached_weather = self.cache.get(city_name)
        if cached_weather:
            return cached_weather
        params = {'q': city_name, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        self.cache.set(city_name, weather_data)
        return weather_data





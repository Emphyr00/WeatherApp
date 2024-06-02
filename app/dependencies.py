import requests
from fastapi import Depends
from .utils.WeatherApi import WeatherApi

WeatherApi('e47ee22edd9b4b43551ae56fb1bdcc6b', requests)
def get_weather_api() -> WeatherApi:
    return WeatherApi.get_instance()

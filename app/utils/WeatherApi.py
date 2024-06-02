import requests
from fastapi import HTTPException

class WeatherApi:
    _instance = None

    def __new__(cls, api_key, requests_module=requests):
        if cls._instance is None:
            cls._instance = super(WeatherApi, cls).__new__(cls)
            cls._instance.api_key = api_key
            cls._instance.requests = requests_module
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise ValueError("No WeatherApi object created")
        return cls._instance

    def get_weather(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={self.api_key}'
        print(url)
        response = self.requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(response.status_code, response.json())
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from ..utils.WeatherParser import WeatherParser
from ..utils.WeatherApi import WeatherApi

class WeatherController: 
    @staticmethod
    def get_weather(city, weather_api : WeatherApi):
        try: 
            weather_api_data = weather_api.get_weather(city)
            return JSONResponse(content=WeatherParser.parse(weather_api_data))
        except HTTPException as http_exception:
            return JSONResponse(content={"message": http_exception.detail}, status_code=http_exception.status_code)
        except ValueError as value_error:
            return JSONResponse(content={"error": "Response from OpenWeatherMap API is not processable", "message": str(value_error)}, status_code=409)
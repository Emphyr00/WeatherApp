import regex
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, Field
from ..controllers.WeatherController import WeatherController
from ..dependencies import get_weather_api
from ..utils.WeatherApi import WeatherApi


router = APIRouter(
    prefix="/weather",
)

class WeatherResponse(BaseModel):
    temperature: float = Field(..., example=22.5)
    description: str = Field(..., example="broken clouds")
    humidity: float = Field(..., example=75.0)
    wind_speed: float = Field(..., example=1.5)
    
class Error404MassageDetail(BaseModel):
    cod: str = Field(..., example="404")
    message: str = Field(..., example="city not found")
    
class Error404Response(BaseModel):
    message: Error404MassageDetail
    
class Error401MassageDetail(BaseModel):
    cod: str = Field(..., example="401")
    message: str = Field(..., example="Invalid API key. Please see https://openweathermap.org/faq#error401 for more info.")
    
class Error401Response(BaseModel):
    message: Error401MassageDetail
    
class Error409Response(BaseModel):
    error: str = Field(..., example="Response from OpenWeatherMap API is not processable")
    message: str = Field(..., example="Missing expected field: 'humidity'")

@router.get("/", 
            description="This endpoint allows to fetch data about weather in given city", 
            responses={
                200: {"description": "Information about weather in given city containing: temperature (celcius), description of the weather, humidity (%) and wind speed (m/s).", "model": WeatherResponse},
                404: {"description": "City Not Found.", "model": Error404Response},
                401: {"description": "Unauthorized.", "model": Error401Response},
                409: {"description": "Response from OpenWeatherMap API can not be parsed correctly, the structure of the API response may have changed.", "model": Error409Response},
            },
            )
async def get_weather(city: str = Query(
        
        regex=r'^[a-zA-Z]+$', 
        min_length=1, 
        description="City name must be alphabetical and non-empty (do not use local alphabet letters, all those letters should be replaced with standard alphabet letters).",
        example="lodz"
    ), weather_api: WeatherApi = Depends(get_weather_api)):
    return WeatherController.get_weather(city, weather_api)
        
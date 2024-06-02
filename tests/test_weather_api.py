import json
import unittest
from unittest.mock import patch, MagicMock
from requests.models import Response
from fastapi import HTTPException
from app.utils.WeatherApi import WeatherApi
from app.utils.WeatherParser import WeatherParser

def load_json_mock(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def create_mock_response(status_code, json_data):
    mock_response = MagicMock(spec=Response)
    mock_response.status_code = status_code
    mock_response.json.return_value = json_data
    return mock_response

def mock_requests_get(url):
    if "lodz" in url:
        return create_mock_response(200, load_json_mock('./tests/json_responses/200.json'))
    elif "unauthorized" in url:
        return create_mock_response(401, load_json_mock('./tests/json_responses/401.json'))
    elif "notfound" in url:
        return create_mock_response(404, load_json_mock('./tests/json_responses/404.json'))
    else:
        return create_mock_response(400, {})

class TestWeatherApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patcher = patch('src.utils.WeatherApi.requests.get', side_effect=mock_requests_get)
        cls.patcher.start()
        WeatherApi(api_key='')

    def test_get_weather_success(self):
        weather_api = WeatherApi.get_instance()
        weather_data = weather_api.get_weather('lodz')
        self.assertEqual(weather_data['main']['temp'], 20.5)
        self.assertEqual(weather_data['weather'][0]['description'], "broken clouds")
        self.assertEqual(weather_data['main']['humidity'], 78)
        self.assertEqual(weather_data['wind']['speed'], 1.54)

    def test_get_weather_unauthorized(self):
        weather_api = WeatherApi.get_instance()
        with self.assertRaises(HTTPException) as context:
            weather_api.get_weather('unauthorized')
        self.assertEqual(context.exception.status_code, 401)
        
    def test_get_weather_not_found(self):
        weather_api = WeatherApi.get_instance()
        with self.assertRaises(HTTPException) as context:
            weather_api.get_weather('notfound')
        self.assertEqual(context.exception.status_code, 404)
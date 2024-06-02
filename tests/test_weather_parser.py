import json
import unittest
from app.utils.WeatherParser import WeatherParser

def load_json_mock(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

class TestWeatherParser(unittest.TestCase):
    def test_parse_correct_data(self):
        parsed_data = WeatherParser.parse(load_json_mock('./tests/json_responses/200.json'))
        self.assertEqual(parsed_data['temperature'], 20.5)
        self.assertEqual(parsed_data['description'], "broken clouds")
        self.assertEqual(parsed_data['humidity'], 78)
        self.assertEqual(parsed_data['wind_speed'], 1.54)
    
    def test_parse_incorrect_data(self):
        with self.assertRaises(ValueError) as context:
            WeatherParser.parse(load_json_mock('./tests/json_responses/200_broken_data.json'))
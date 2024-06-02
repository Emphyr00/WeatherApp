class WeatherParser:
    @staticmethod
    def parse(weather_data):
        try:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            
            parsed_data = {
                "temperature": temperature,
                "description": description,
                "humidity": humidity,
                "wind_speed": wind_speed,
            }
            return parsed_data
        except KeyError as e:
            raise ValueError(f"Missing expected field: {e}")
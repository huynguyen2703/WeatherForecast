import requests
from datetime import datetime
from constants import WEATHER_URL, LOCATION, HOUR_LIST


class WeatherData:
    def __init__(self):
        self.url = WEATHER_URL
        self.location = LOCATION
        self.hour_list = HOUR_LIST
        self.today = datetime.today().strftime("%Y/%m/%d")

    def get_weather(self):
        request = requests.get(url=self.url, params=self.location)
        request.raise_for_status()
        response = request.json()['hourly']
        hourly__weather = response[:12]
        weather_code_list = [(hour['weather'][0]['id'], hour['weather'][0]['description']) for hour in hourly__weather]
        return weather_code_list

    def determine_weather(self):
        weather_summary = {self.hour_list[item]: self.get_weather()[item] for item in range(len(self.hour_list))}

        final_report = f"Weather Forecast for {self.today} \n"

        for hour, weather_description in weather_summary.items():
            if weather_description[1] == 'clear sky':
                icon = '☀️'
            elif 'thunderstorm' in weather_description[1]:
                icon = '⛈️'
            elif 'drizzle' in weather_description[1] or 'rain' in weather_description[1]:
                icon = '🌧️️'
            elif 'snow' in weather_description[1] or 'sleet' in weather_description[1]:
                icon = '⛄️'
            elif 'clouds' in weather_description[1]:
                icon = '☁️'
            else:
                icon = '😷'

            final_report += f"{hour} : {icon}{weather_description[1]}\n"
        return final_report

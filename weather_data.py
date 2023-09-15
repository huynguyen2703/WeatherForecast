import requests
from datetime import datetime
from constants import WEATHER_URL, LOCATION, HOUR_LIST
from pprint import pprint


class WeatherData:
    def __init__(self):
        """Initialize WeatherData class with default parameters."""
        self.url = WEATHER_URL
        self.location = LOCATION
        self.hour_list = HOUR_LIST
        self.today = datetime.today().strftime("%Y/%m/%d")

    def get_weather(self):
        """
        Fetch and return hourly weather data.

        Returns:
            list: A list of tuples containing weather codes and descriptions.
        """
        request = requests.get(url=self.url, params=self.location)
        request.raise_for_status()
        response = request.json()['hourly']
        hourly_weather = response[:16]
        weather_code_list = [(hour['weather'][0]['id'], hour['weather'][0]['description']) for hour in hourly_weather]
        return weather_code_list

    def determine_weather(self):
        """
        Analyze weather data and return a summary.

        Returns:
            str: A formatted weather forecast report.
        """
        weather_summary = {self.hour_list[item]: self.get_weather()[item] for item in range(len(self.hour_list))}
        pprint(weather_summary)

        final_report = f"Weather Forecast for {self.today} \n"

        for hour, weather_description in weather_summary.items():
            # Determine weather icon based on descriptions
            if (weather_description[1] == 'clear sky' and int(hour.strip(":")[0]) < 19) or weather_description[1]\
                    == 'few clouds':
                icon = '🌞️'
            # Add more conditions for different weather types
            elif weather_description[1] == 'clear sky' and int(hour.strip(":")[0]) > 19:
                icon = '🌚'
            elif 'thunderstorm' in weather_description[1]:
                icon = '⛈️'
            elif 'drizzle' in weather_description[1] or 'rain' in weather_description[1] or weather_description[1] \
                    == 'overcast clouds':
                icon = '🌧️️'
            elif 'snow' in weather_description[1] or 'sleet' in weather_description[1]:
                icon = '⛄️'
            elif weather_description[1] == 'scattered clouds':
                icon = '🌤️'
            elif weather_description[1] == 'broken clouds':
                icon = '☁️'
            else:
                icon = '😷'

            final_report += f"{hour} : {icon}{weather_description[1]}\n"
        return final_report

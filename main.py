import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token, http_client=proxy_client)

location = {'lat': 47.606209,
            'lon': -122.332069,
            'appid': os.environ.get("API_KEY"),
            'exclude': 'current,minutely,daily'
            }

request = requests.get(url='https://api.openweathermap.org/data/3.0/onecall', params=location)
request.raise_for_status()
response = request.json()['hourly']
weekday_weather = response[:12]
weather_code_list = [hour['weather'][0]['id'] for hour in weekday_weather]


def determine_weather():
    weather_summary = []
    final_report = ''
    for weather_code in weather_code_list:
        if int(weather_code) >= 800:
            weather_summary.append('Cloudy☁️ today, enjoy some air!')
        elif int(weather_code) >= 700:
            weather_summary.append('Weather might be unusual today, bring mask')
        elif int(weather_code) >= 600:
            weather_summary.append('Snow⛄️, it might snow today')
        elif int(weather_code) >= 200:
            weather_summary.append('Rainy🌧️, it is likely to rain today')

    for i in weather_summary:
        final_report += str(i) + "\n"
    return final_report


message = client.messages.create(from_='+18882987013', body=determine_weather(), to='+12064540747')
print(message.status)

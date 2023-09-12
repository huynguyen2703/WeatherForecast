import os

WEATHER_URL = 'https://api.openweathermap.org/data/3.0/onecall'
LOCATION = {'lat': 47.790939,
            'lon': -122.335159,
            'appid': os.environ.get('API_KEY'),
            'exclude': 'current,minutely,daily'
            }
HOUR_LIST = ['08:00am', '09:00am', '10:00am', '11:00am', '12:00pm', '13:00am', '14:00am', '15:00am', '16:00am',
             '17:00am', '18:00am', '19:00am']

ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
HEADER = os.environ.get('AUTHORIZATION')
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')

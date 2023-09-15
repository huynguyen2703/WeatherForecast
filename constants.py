import os

# Constants for WeatherData and GoogleSheet classes
WEATHER_URL = 'https://api.openweathermap.org/data/3.0/onecall'
LOCATION = {
    'lat': 47.790939,
    'lon': -122.335159,
    'appid': os.environ.get('API_KEY'),
    'exclude': 'current,minutely,daily'
}

HOUR_LIST = [
    '08:00am', '09:00am', '10:00am', '11:00am', '12:00pm', '13:00pm', '14:00pm', '15:00pm', '16:00pm',
    '17:00pm', '18:00pm', '19:00pm', '20:00pm', '21:00pm', '22:00pm', '23:00pm'
]

# Constants for other components (e.g., Messaging, add_user.py)
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
HEADER = os.environ.get('AUTHORIZATION')
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')

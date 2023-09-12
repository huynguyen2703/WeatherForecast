from weather_data import WeatherData
from messaging import Messaging
from google_sheet import GoogleSheet

google_sheet_database = GoogleSheet()
weather_object = WeatherData()
messages_object = Messaging(weather_object, google_sheet_database)

weather_analysis = weather_object.determine_weather()
messages_object.check_type()

if len(messages_object.email_dict) != 0 and len(messages_object.sms_dict) != 0:
    messages_object.send_email_message()
    messages_object.send_sms_message()

elif len(messages_object.email_dict) == 0 and len(messages_object.sms_dict) != 0:
    messages_object.send_sms_message()

elif len(messages_object.sms_dict) == 0 and len(messages_object.email_dict) != 0:
    messages_object.send_email_message()

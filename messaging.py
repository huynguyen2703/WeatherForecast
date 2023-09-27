from twilio.rest import Client
from constants import ACCOUNT_SID, AUTH_TOKEN, MY_EMAIL, MY_PASSWORD
from weather_data import WeatherData
from google_sheet import GoogleSheet
import smtplib


class Messaging:


    def __init__(self, weather_report: WeatherData, recipient: GoogleSheet):
        """
        Initialize the Messaging class with required parameters.

        Args:
            weather_report (WeatherData): An instance of WeatherData to provide weather information.
            recipient (GoogleSheet): An instance of GoogleSheet to fetch user data.
        """
        self.account_sid = ACCOUNT_SID
        self.auth_token = AUTH_TOKEN
        self.client = Client(self.account_sid, self.auth_token)
        self.user_list = recipient.get_user_data()
        self.weather_report = weather_report
        self.email_dict = {}
        self.sms_dict = {}

    def check_type(self):
        """
        Categorize users into email and SMS recipients based on contact information.
        """
        for user in self.user_list:
            if '@' in self.user_list[user]:
                self.email_dict[user] = self.user_list.get(user)
            else:
                self.sms_dict[user] = self.user_list.get(user)

    def send_sms_message(self):
        """
        Send weather notifications via SMS to users.
        """
        for name in self.sms_dict:
            message = self.client.messages.create(from_='+18882987013',
                                                  body=f"\nGood Morning {name}😇 \n"
                                                       f"{self.weather_report.determine_weather()}",
                                                  to=f"+1{self.sms_dict[name]}")
            print(message.status)

    def send_email_message(self):
        """
        Send weather notifications via email to users.
        """
        for name in self.email_dict:
            with smtplib.SMTP('smtp.gmail.com', port=587) as server:
                server.starttls()
                server.login(user=MY_EMAIL, password=MY_PASSWORD)

                subject = "Weather Forecast For Today"
                email_message = f"Subject: {subject}\n\n"
                email_message += f"Good Morning {name}😇 \n{self.weather_report.determine_weather()}"

                # Encode the message as UTF-8
                email_message = email_message.encode('utf-8')

                server.sendmail(from_addr=MY_EMAIL,
                                to_addrs=self.email_dict[name],
                                msg=email_message)

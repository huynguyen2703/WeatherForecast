from twilio.rest import Client
from constants import ACCOUNT_SID, AUTH_TOKEN, MY_EMAIL, MY_PASSWORD
from weather_data import WeatherData
from google_sheet import GoogleSheet
import smtplib


class Messaging:
    """
        A class for sending weather notifications to users via SMS and email.

        Attributes:
            account_sid (str): Twilio account SID for SMS messaging.
            auth_token (str): Twilio authentication token for SMS messaging.
            client (twilio.rest.Client): Twilio client for sending SMS messages.
            user_list (dict): A dictionary containing user contact information.
            weather_report (WeatherData): An instance of the WeatherData class.
            email_dict (dict): A dictionary of users with email addresses.
            sms_dict (dict): A dictionary of users with phone numbers.
        """
    def __init__(self, weather_report: WeatherData, recipient: GoogleSheet):
        """Initialize Messaging class with default keyword arguments
           account_sid : SID number of owner SMS account
           auth_token : TOKEN used for authentication
           client : Client object used to send sms messages
           user_list : a dictionary containing user's credential retrieved from Google Sheet
           weather_report : a complete weather report message delivered from weather_data class
           email_dict : a dictionary representing users that prefer receiving messages via email
           sms_dict : a dictionary representing users that prefer receiving messages via sms"""
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
        Function examines the unique characters in users' credentials to determine if they should be put in sms_dict or
        email_dict to receive weather report via preferred platform.
        """
        for user in self.user_list:
            if '@' in self.user_list[user]:
                self.email_dict[user] = self.user_list.get(user)
            else:
                self.sms_dict[user] = self.user_list.get(user)

    def send_sms_message(self):
        """
        Send weather notifications via SMS to users.
        Function loop through and send message to each of the person in sms dictionary using a
        bought phone number from Twilio API.
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
        Function loop through and send message to each of the person in email dictionary using a
        special email created for this application.
        """
        for name in self.email_dict:
            with smtplib.SMTP('smtp.gmail.com', port=587) as server:
                server.starttls()
                server.login(user=MY_EMAIL, password=MY_PASSWORD)

                subject = "Weather Forecast For Today"
                email_message = f"Subject: {subject}\n\n"
                email_message += f"Good Morning {name}😇 \n\n{self.weather_report.determine_weather()}"

                # Encode the message as UTF-8
                email_message = email_message.encode('utf-8')

                try:
                    server.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=self.email_dict[name],
                                    msg=email_message)
                    print("email sent successfully")
                except smtplib.SMTPException as e:
                    print(f"Error: {e} : failed to send email")

import requests
from constants import SHEETY_ENDPOINT, HEADER


class GoogleSheet:
    def __init__(self):
        """
        initialize sheety endpoint url
                   sheety headers
        """
        self.sheety_endpoint = SHEETY_ENDPOINT
        self.header = {'Authorization': HEADER}

    def get_user_data(self):
        """ Retrieve user data from Google Sheets.
         Sends a GET request to the specified API endpoint with the provided authorization header.
     Returns user data as a dictionary with usernames as keys and contact details as values.
     Returns:
         dict: User data with usernames as keys and contact details as values.
     """
        request = requests.get(url=self.sheety_endpoint, headers=self.header)
        request.raise_for_status()
        user_data = request.json()['sheet1']
        user_info = {item['user']: item['contacts'] for item in user_data}
        return user_info

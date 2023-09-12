import requests
from constants import SHEETY_ENDPOINT, HEADER


class GoogleSheet:
    def __init__(self):
        self.sheety_endpoint = SHEETY_ENDPOINT
        self.header = {'Authorization': HEADER}

    def get_user_data(self):
        request = requests.get(url=self.sheety_endpoint, headers=self.header)
        request.raise_for_status()
        user_data = request.json()['sheet1']
        user_info = {item['user']: item['contacts'] for item in user_data}
        return user_info

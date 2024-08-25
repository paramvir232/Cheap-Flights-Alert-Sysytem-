import requests
from dotenv import load_dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = 'https://api.sheety.co/b0023ccfafbd5f9dce24eb70435acb0d/flightDeals/prices'
        self.SHEETY_USER_ENDPOINT = 'https://api.sheety.co/b0023ccfafbd5f9dce24eb70435acb0d/flightDeals/users'

    def get_sheet_data(self):
        """Returns Google Sheet data"""

        read_response = requests.get(url=self.SHEETY_ENDPOINT)
        return read_response.json()['prices']

    def update_sheet_iata_code(self,iata_code,row_id):
        """Inserts iata_code in google sheet with give row and code"""

        json_params = {
            'price': {'iataCode': iata_code}
        }
        update_response = requests.put(url=f'{self.SHEETY_ENDPOINT}/{row_id}', json=json_params)

    def get_customer_emails_list(self):
        """Returns Email list for users from Google sheets who has subscribed"""

        read_response = requests.get(url=self.SHEETY_USER_ENDPOINT)
        data = read_response.json()
        email_list = [user['whatIsYourEmail ?']for user in data['users'] ]
        return email_list

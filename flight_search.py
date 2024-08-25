import os
import requests
from datetime import datetime,timedelta
from dotenv import load_dotenv
load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.FLIGHT_API = os.getenv('FLIGHT_API')
        self.FLIGHT_API_SECRET = os.getenv('FLIGHT_API_SECRET')
        self.header_params = {
            'Authorization': f'Bearer {self.get_access_token()}'
         }


    def get_access_token(self) -> str:
        """Genrates new access token for amadeus flight search"""

        token_header = {
            'grant_type': 'client_credentials',
            'client_id': self.FLIGHT_API,
            'client_secret': self.FLIGHT_API_SECRET
        }
        token_response = requests.post(url='https://test.api.amadeus.com/v1/security/oauth2/token', data=token_header)
        access_token = token_response.json()['access_token']
        return access_token

    def get_iata_code(self,city):
        """Gets iata code for given city """

        iata_code_params = {
            'keyword': city
        }
        iata_code_response = requests.get(url='https://test.api.amadeus.com/v1/reference-data/locations/cities',params=iata_code_params,headers=self.header_params)
        iata_code = iata_code_response.json()['data'][0]['iataCode']

        return iata_code

    def cheapest_flight_check(self,to_city_iata_code,max_price,is_direct = True):
        """Search for cheapest flight give iata code, max price"""

        date = datetime.now() + timedelta(days=1)
        six_month_later = datetime.now() + timedelta(days=180)
        flight_params = {
            'originLocationCode': 'DEL',
            'destinationLocationCode': to_city_iata_code,
            'departureDate': date.strftime('%Y-%m-%d'),
            'returnDate':six_month_later.strftime('%Y-%m-%d'),
            'adults': 1,
            'maxPrice':max_price,
            'nonStop':str(is_direct).lower(),
            'max':5
        }

        response = requests.get(url='https://test.api.amadeus.com/v2/shopping/flight-offers',params=flight_params,headers=self.header_params)
        data = response.json()
        return data


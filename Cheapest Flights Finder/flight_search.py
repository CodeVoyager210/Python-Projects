import requests
from datetime import datetime
API_KEY = 'A9Y9Zg7wrptWEvpRFJ7SzPYgGV1CUJyi'
API_SECRET = 'D3AzBNuixWDweh5A'
AUTH_TOKEN = 'https://test.api.amadeus.com/v1/security/oauth2/token'
IATA_WEB = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
FLIGHTS = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
class FlightSearch:
    def get_info(self):
        header = {
            'Content-Type' : 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type' : 'client_credentials',
            'client_id' : API_KEY,
            'client_secret' : API_SECRET
        }
        response = requests.post(url=AUTH_TOKEN,headers=header,data=body)
        return response.json()['access_token']
    def get_destination_code(self,city):
        headers = {
            "Authorization": f"Bearer {self.get_info()}"
        }
        query = {
            'keyword': city,
            'max' : '2',
            'include' : 'AIRPORTS'
        }
        response = requests.get(url=IATA_WEB,headers=headers,params=query)
        try:
            code = response.json()['data'][0]['iataCode']
            return code
        except IndexError:
            return 'Airport code not found'
        except KeyError:
            return 'Airport code not found'
    def check_flights(self,origin_city,dest_city,from_time,to_time,is_direct = True):
        headers = {
            "Authorization": f"Bearer {self.get_info()}"
        }
        query = {
            'originLocationCode' : origin_city,
            'destinationLocationCode' : dest_city,
            'departureDate' : from_time.strftime('%Y-%m-%d'),
            'returnDate' : to_time.strftime('%Y-%m-%d'),
            'adults' : '1',
            'nonStop' : 'true' if is_direct else 'false',
            'max' : '10'
        }
        response = requests.get(url=FLIGHTS,headers=headers,params=query)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None
        return response.json()






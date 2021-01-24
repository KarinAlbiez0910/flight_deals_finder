import requests
import datetime
import html

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
six_months_from_now = tomorrow + datetime.timedelta(days=182)
tomorrow_str = tomorrow.strftime("%d/%m/%Y")
six_months_from_now_str = six_months_from_now.strftime("%d/%m/%Y")


class FlightSearch:

    def __init__(self):
    #This class is responsible for talking to the Flight Search API.

        self.headers = {
            'apikey': 'h7CEs8R53rnBHljX4H1zP9WuFG1Uffz9'
        }


    def get_iata_codes(self, city_name):
        parameters = {
            'term': city_name,
            'location_types': 'city'
        }
        response = requests.get(url="https://tequila-api.kiwi.com/locations/query", headers = self.headers, params=parameters)
        location_data = response.json()
        return location_data['locations'][0]['code']

    def search_flights(self, destination):
        body = {
            "fly_from": "LON",
            "fly_to": destination,
            "curr": "GBP",
            "max_stopovers": 0,
            "flight_type": "round",
            "date_from": html.unescape(tomorrow_str),
            "date_to": html.unescape(six_months_from_now_str),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28
        }

        flights_response = requests.get(url= "https://tequila-api.kiwi.com/v2/search", params=body, headers=self.headers)
        flights_response.raise_for_status()
        return flights_response.json()







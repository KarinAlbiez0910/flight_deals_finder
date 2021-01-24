
import requests


class DataManager:
    def __init__(self):
    #This class is responsible for talking to the Google Sheet.
        self.sheety_endpoint = "https://api.sheety.co/981d86c192ddf233e7ac10eaeffb2107/flightDeals/prices"
        self.row_num = 2


    def get_google_sheet_data(self):
        response = requests.get(url=self.sheety_endpoint)
        self.data = response.json()
        return self.data
    def add_iata_code_to_sheet(self, iata_code, row):

        body = {
            'price': {
                'iataCode': iata_code
            }
        }
        response = requests.put(url=f"https://api.sheety.co/981d86c192ddf233e7ac10eaeffb2107/flightDeals/prices/{row}", json=body)
        print(response.raise_for_status())




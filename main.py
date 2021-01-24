from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import json

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

google_sheet_data = data_manager.get_google_sheet_data()

google_sheet_list = google_sheet_data['prices']

# only to be run once, to populate the IATA codes in the Google Sheet
for item in google_sheet_list:
    if not item['iataCode'] == '':
        iata_code = flight_search.get_iata_codes(item['city'])
        row = item['id']
        data_manager.add_iata_code_to_sheet(iata_code, row)

iata_codes_max_prices = {item['iataCode']: item['lowestPrice'] for item in google_sheet_list}
#print(iata_codes_max_prices)

#print(google_sheet_list)


for iata_code, price in iata_codes_max_prices.items():
    flights_found = flight_search.search_flights(iata_code)
    for item in flights_found['data']:
        if item['price'] <= price:
            # only send a message for the first good deal, otherwise 700 messages would be sent
            price_alert_message = f"Low price alert! Only {item['price']} GBP to fly from "\
                                  f"{item['cityFrom']}, {item['cityCodeFrom']}, to " \
                                  f"{item['cityTo']}, {item['cityCodeTo']}, from " \
                                  f"{item['route'][0]['local_departure'].split('T')[0]} to {item['route'][1]['local_departure'].split('T')[0]}."

            notification_manager.send_message(price_alert_message)
            break














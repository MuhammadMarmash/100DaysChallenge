import dateutil
import requests
from flight_search import FlightSearch
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_data import FlightData
data_manager = DataManager()
flights = data_manager.get()["prices"]
flight_search = FlightSearch()

for flight in flights:
    lowest_price = flight["lowestPrice"]
    new_flights = flight_search.get(flight["iataCode"])["data"]
    for new_flight in new_flights:
        print(dateutil.parser.isoparse('2008-09-03T20:56:35.450686'))
        # if new_flight["price"] < flight["lowest price"]:
        #     notification_manager = NotificationManager()
        #     notification_manager.send_telegram_message(f"Low price alert! Only{new_flight['price']}"
        #                                                f" to fly from {new_flight['cityTo']}"
        #                                                f" to {new_flight['cityTo']},"
        #                                                f" from }")

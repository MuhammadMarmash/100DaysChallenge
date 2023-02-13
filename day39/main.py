from flight_search import FlightSearch
from notification_manager import NotificationManager
from data_manager import DataManager

data_manager = DataManager()
flights = data_manager.get()["prices"]
flight_search = FlightSearch()

for flight in flights:
    lowest_price = flight["lowestPrice"]
    new_flight = flight_search.get(flight["iataCode"])["data"][0]
    if new_flight["price"] <= flight["lowestPrice"]:
        print(flight)
        notification_manager = NotificationManager()
        notification_manager.send_telegram_message(f"LOW price alert! Only {new_flight['price']}₪"
                                                   f" to fly from {new_flight['route'][0]['cityFrom']}"
                                                   f"-{new_flight['route'][0]['flyFrom']}"
                                                   f" to {new_flight['route'][0]['cityTo']}"
                                                   f"-{new_flight['route'][0]['flyTo']},"
                                                   f" from"
                                                   f" {new_flight['route'][0]['local_departure'].split('T')[0]}"
                                                   f" to {new_flight['route'][1]['local_departure'].split('T')[0]}")

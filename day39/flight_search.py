import requests
import datetime as dt


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.end_point = "https://api.tequila.kiwi.com/v2/search"
        self.api_key = "bKFrH2AWQmax4nAxaL7sxh_TO-0lFfmy"
        self.today = dt.datetime.today()

    def get(self, to):
        response = requests.get(self.end_point, params={
            "fly_from": "TLV",
            "fly_to": to,
            "date_from": (self.today + dt.timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (self.today + dt.timedelta(days=180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "ILS"
        }, headers={
            "apikey": self.api_key
        })
        response.raise_for_status()
        return response.json()

import requests


class DataManager:
    def __init__(self):
        self.end_point = "https://api.sheety.co/b271d3faf7a77b642f4a46f5470d2521/flightDeals/prices"
        self.auth = "Basic bXVoYW1tYWQ6bXVoYW1tYWQzMTEy"

    def get(self):
        response = requests.get(self.end_point,
                                headers={
                                    "Authorization": self.auth
                                }
                                )
        response.raise_for_status()
        return response.json()

import requests
import datetime as dt
today = dt.datetime.today().strftime("%Y%m%d")
USERNAME = "muhammadmarmash"
TOKEN = "hjgijgrigjir"
response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1",
                         json={
                             "date": today,
                             "quantity": "50"
                         },
                         headers={
                             "X-USER-TOKEN": TOKEN
                         })

print(response.text)

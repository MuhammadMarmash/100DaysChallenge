import requests
import datetime as dt
import os
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ.get("API_KEY")
nutrition_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_end_point = "https://api.sheety.co/b271d3faf7a77b642f4a46f5470d2521/myWorkouts/workouts"
exercise = input("Tell me which exercise you did: ")
response1 = requests.post(nutrition_END_POINT, json={
    "query": exercise,
    "gender": "male",
    "weight_kg": "56",
    "height_cm": "175",
    "age": "18"
}, headers={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
})
data = response1.json()
for exercise in data["exercises"]:
    sheet_response = requests.post(sheety_end_point, json={
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }, headers={
        "Authorization": os.environ.get("sheety_authorization").replace("_", " ")
    }
                                   )


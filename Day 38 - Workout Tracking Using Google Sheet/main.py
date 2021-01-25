import requests
from datetime import datetime


GENDER = "female"
WEIGHT_KG = 53
HEIGHT_CM = 162
AGE = 29
APP_ID = "44ef847a"
API_KEY = "c1d8387ad580d3ac39812710c1484fc3"
TODAY = datetime.now()
TOKEN = "Bearer m'spcE309jkld"

# use nutritionix api to obtain facts about the type and length of the exercise
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
exercise_data = response.json()["exercises"][0]


# update the googlesheet with new exercise information
sheety_endpoint = "https://api.sheety.co/e074014c1c4c8da5f6d47acc268ed697/myWorkouts/sheet1"

new_record = {
    "sheet1": {
        "date": TODAY.strftime("%d/%m/%Y"),
        "time": TODAY.strftime("%H:%M:%S"),
        "exercise": exercise_data["name"].title(),
        "duration": str(exercise_data["duration_min"]),
        "calories": round(exercise_data["nf_calories"])
    }
}

headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
}

sheet_update = requests.post(url=sheety_endpoint, json=new_record, headers=headers)
print(sheet_update.text)

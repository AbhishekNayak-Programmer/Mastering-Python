import requests
from datetime import datetime as dt
import os

APP_ID = '2f145cf1'
API_KEY = '9035ce452539e536be561e3fa036098e'
GENDER = "male"
WEIGHT_KG = 86
HEIGHT_CM = 180
AGE = 25

user_input = input("Tell me which exercise you did: ")
# user_input = "Ran for 3 miles and walked for 2 km"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

exercise_data = {
    "query" : user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

try:
    response = requests.post(exercise_endpoint, json=exercise_data, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(data)
except :
    print("Error While Getting Data")
else:
    print("Got data for the input")


## Updating the Google sheet using sheety
today_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

# Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = "https://api.sheety.co/c89a9d5d328a3154f47d77e619fd9674/workoutTracker/workouts"

# Sheety API Call & Authentication
sheet_inputs = {
    GOOGLE_SHEET_NAME: {
        "date": today_date,
        "time": now_time,
        "exercise": "ok_ok",
        "duration": 190,
        "calories": 240
    }
}

## Sheety Authentication Option 1: No Auth
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


## Sheety Authentication Option 2: Basic Auth
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     auth=(
#         "Abhishek",
#         "abcdef2342155535",
#     )
# )
# print(sheet_response.text)


## Sheety Authentication Option 3: Bearer Token
bearer_headers = {
    "Authorization": f"Bearer Abhishek"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)    

print(f"Sheety Response: \n {sheet_response.text}")

import requests
from twilio.rest import Client
import os

# for storing write
# export YOUR_ENV_NAME=what_ever_value
print(os.environ.get("TERM_PROGRAM")) # Access like this

MY_LAT = 17.385044
MY_LNG = 78.486671

# Open weather Keys
api_key = 'e49b767955786393467f479294e43ef9'

# Twilio Account details
account_sid = "AC9e7f80b8d34ca33608c404934ba34c07"
auth_token = "8bfda402dc40d5ae83b90a9e061bb015"

weather_parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LNG,
    "appid" : api_key,
    "units" : "metric",
    "cnt" : 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

# This is the process of sending messages but now I have deleted my account from twilio due to youtube video upload
def send_message():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring your Umbrella it will rain!",
        from_="+19045843132",
        to="+917077358291",
    )


def will_rain(data):
    for hourly_data in range(len(data)):
        # print(data[i]["weather"][0]["id"])
        if data[hourly_data]["weather"][0]["id"] < 700 :
            print("Bring your Umbrella it will rain!")
            return True
    return False

will_rain(weather_data["list"])
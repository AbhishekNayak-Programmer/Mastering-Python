import requests
import smtplib
import datetime as dt
import time

MY_LAT = 17.630091
MY_LNG = 78.499506

def get_iss_position():
    res = requests.get(url='http://api.open-notify.org/iss-now.json')
    res.raise_for_status()
    iss_pos_data = res.json()
    iss_pos = iss_pos_data["iss_position"]
    return (float(iss_pos["latitude"]), float(iss_pos["longitude"]))

def send_email():
    sender_email = "sahilservice300@gmail.com"
    sender_password = "ldxlnrloejkpxzmt"
    receivers_email = "webcoder41@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        subject = "You can now see ISS"
        body = 'ISS is over your head'
        msg = f"Subject: {subject}\n\n{body}"
        connection.send_message(from_addr=sender_email, to_addrs=receivers_email, msg=msg)


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng" : MY_LNG,
        "formatted": 0
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]['sunrise'].split("T")[1].split(":")[0]) 
    sunset = int(data["results"]['sunset'].split("T")[1].split(":")[0])
    print(sunrise, sunset)

    time_now_hour = dt.datetime.now().hour
    if time_now_hour >= sunset or time_now_hour <= sunrise :
        return True


# Send message to user if that is +5 or -5 degrees of the ISS position
def iss_over_head():
    # print(get_iss_position())
    iss_pos_val = get_iss_position()
    min_lat_val = MY_LAT - 5
    max_lat_val = MY_LAT + 5
    min_lng_val = MY_LNG - 5
    max_lng_val = MY_LNG + 5
    if min_lat_val <= iss_pos_val[0] <= max_lat_val and min_lng_val <= iss_pos_val[1] <= max_lng_val:
        return True



def init():
    while True:
        time.sleep(60)   
        if iss_over_head() and is_night() :
            send_email()
        else:
            print("Not over head")

init()
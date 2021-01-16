import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.048615  # Your latitude
MY_LONG = -114.070847  # Your longitude
MY_EMAIL = "codetestpython@gmail.com"
MY_PASSWORD = "abcd1234()"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# access ISS location API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()

# check ISS location
iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

# access sunset, sunrise API
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
time_data = response.json()

# check sunset, sunrise and current time at your location
sunrise = int(time_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(time_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

# Run the code every 60 seconds
while True:
    time.sleep(60)
    # If the ISS is close to my current position, send a notification email
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        if sunset <= time_now <= sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=MY_EMAIL,
                                    msg="Subject:lOOK UP! \n\nThe ISS is near your location, look at the sky.")

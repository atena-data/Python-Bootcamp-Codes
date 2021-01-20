import requests
from twilio.rest import Client

# API key to use the weather data
api_key = "5f8763018a9d59441853dd4de884c747"
# location coordinates
latitude = 51.0447
longitude = -114.0719

# parameters to use the weather API
parameters = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

# variables to use Twilio API for messaging
account_sid = "ACc93427e5a223e5eb0d271674eed00c2a"
auth_token = "a937fabea54d1dab045920eb720e02ec"

# import data from the weather aPI into a JSON file
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

# check the forecast for the new 12 hr and send a notification SMS if there is a chance of rain
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body="It's going to rain today 🌧. Remember to bring an umbrella ☔☔.",
                from_="+14439032421",
                to="+15558675310"
            )
    print(message.status)

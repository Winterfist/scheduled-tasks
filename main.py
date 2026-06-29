import requests
from twilio.rest import Client
import os

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]


MY_LAT = 46.770920
MY_LONG = 23.589920
API_KEY = os.environ["OPEN_WEATHER_API_KEY"]

parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": API_KEY,
        "units": "metric",
        "cnt":4
    }

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
forecast_codes = [forecast["weather"][0]["id"] for forecast in data["list"]]
print(forecast_codes)
if any(code < 700 for code in forecast_codes):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an Umbrella! Rain Announced",
        from_="+18148217820",
        to='+40751373733'
    )
    print(message.sid)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Clear weather today! No need for umbrella",
        from_="+18148217820",
        to='+40751373733'
    )
    print(message.sid)

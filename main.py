import os
import requests
import json
from twilio.rest import Client

API_KEY ="58e7e7f4a35a57a906aaaf4a5ecce5e4" # os.environ.get("OWM_API_key")
account_sid = "AC75ba6d12c9c0b32b5643434b541157ac"
auth_token = "9be962c868beffdd5d05962dc62aafc7"

params = {
    "lat": 29.963659,
    "lon": 77.546028,
    "appid": API_KEY,
    "cnt":4,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=params
)

print(response.status_code)
print(response.text)
response.raise_for_status()
weather_data=response.json()
new_one=[]
will_rain=False
for i in range(0,4):

    new_one.append(weather_data["list"][i]["weather"][0]["id"])
for i in new_one:
    if i<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+17753738109',
        to='+919058721930'
    )

    print(message.status)




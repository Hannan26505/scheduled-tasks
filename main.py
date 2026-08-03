from dotenv import load_dotenv
import os
import requests
import json
from twilio.rest import Client
load_dotenv()

API_KEY = os.getenv("OWM_API_key")
account_sid = os.getenv("NEW_SID")
auth_token = os.getenv("NEW_AUTH_KEY")
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
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's not going to rain today. Have Fun",
        from_='+17753738109',
        to='+919058721930'
    )
    print(message.status)

import requests
from requests.auth import HTTPBasicAuth
import datetime

APP_ID = "YOURS"
API_KEY = "YOURS"
full_endpoint = "YOURS"

endpoint = "https://api.uat.syndigo.com/api/auth?"

answer = input("Tell me what exercise you did: ")

username = "YOURS"
password = "YOURS!"
auth_token = "YOURS"


nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

information = {
    "query": answer,
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 100,
    "age": 35
}


new_request = requests.post(url=full_endpoint, headers=nutri_headers, json=information)
exercise_info = new_request.json()
print(exercise_info)

print(exercise_info["exercises"])
exercise_ws = exercise_info["exercises"][0]["user_input"].title()
duration_ws = exercise_info["exercises"][0]["duration_min"]
calories_ws = exercise_info["exercises"][0]["nf_calories"]

thedate = datetime.date.today()
thetime = datetime.datetime.now()

hour = str(thetime.hour)
minute = str(thetime.minute)
second = str(thetime.second)
total_time = (hour + ":" + minute + ":" + second)


sheety_url = "YOURS"

parameters = {
                "workout": {
                    "name": "YOURS",
                    "email": "YOURS",
                    "time": total_time,
                    "exercise": exercise_ws,
                    "duration": duration_ws,
                    "calories": duration_ws,
                    "date": str(thedate),
    }
}

headers = {
    "username": username,
    "password": password
}


basic = HTTPBasicAuth(username, password)
requestsPost = requests.post(url=sheety_url, json=parameters, headers=headers, auth=basic)
print(requestsPost.json())
import requests

APP_ID = "YOUR APP ID"
API_KEY = "YOUR API KEY"
full_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

answer = input("Tell me what exercise you did: ")

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
new_json = new_request.json()
print(new_json)

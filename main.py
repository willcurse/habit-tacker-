import requests
from datetime import datetime

api_endpoint = "https://pixe.la/v1/users"
USERNAME = "user-uttu-2024"
TOKEN = "ckbwcb23ksvv"
GRAPHID = "uniquegraphid"

# Check if the user exists or create the user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=api_endpoint, json=user_params)
if response.status_code != 200:
    print(f"Failed to create user. Status code: {response.status_code}")
    print(response.text)
    exit()

# Create the graph
graph_endpoint = f"{api_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPHID,
    "name": "Anime Watch streak",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
if response.status_code != 200:
    print(f"Failed to create graph. Status code: {response.status_code}")
    print(response.text)
    exit()

# Add a new pixel (data point)
dt = datetime(year=2024, month=2, day=22)
pixel_endpoint = f"{api_endpoint}/{USERNAME}/graphs/{GRAPHID}/{dt.strftime('%Y%m%d')}"

pixel_params = {
    "quantity": "100"
}

response = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)
if response.status_code != 200:
    print(f"Failed to update pixel. Status code: {response.status_code}")
    print(response.text)
    exit()

print(response.text)

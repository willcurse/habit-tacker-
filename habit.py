import requests
from datetime import datetime


api_endpoint = "https://pixe.la/v1/users"
USERNAME = "user-uttu-2024"
TOKEN = "ckbwcb23ksvv"
GRAPHID = "uniquegraphid"

# 1st Step: Create a user
User_params = {
    "token": TOKEN,                            #commented because the username is 
    "username": USERNAME,                      # already connected...
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=api_endpoint, json=User_params)
# print(response.text)

graph_endpoint = f"{api_endpoint}/{USERNAME}/graphs"

# 2nd Step: Create a graph
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

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{api_endpoint}/{USERNAME}/graphs/{GRAPHID}"

dt=datetime(year=2024,month=2,day=22)
#print(dt.strftime("%y%m%d"))

# Add a new pixel (data point)
pixel_params = {
    "date": dt.strftime("%Y%m%d"),
    "quantity": "160"
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

# Update_Endpoint=f"{api_endpoint}/{USERNAME}/graphs/{GRAPHID}/{dt.strftime('%Y%m%d')}"

# new_params={
#     "quantity":"120"
# }

# response=requests.put(url=Update_Endpoint,json=new_params)
# print(response.text)
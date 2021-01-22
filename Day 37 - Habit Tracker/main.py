import requests
from datetime import datetime

USERNAME = "athena"
TOKEN = "nUAep9yf392hnl@#lpg"
GRAPH_ID = "graph1"
TODAY = datetime.now().strftime("%Y%m%d")


# create a pixela account

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# once response is created, comment out this line
response = requests.post(url=pixela_endpoint, json=user_params)


# create a graph in pixela

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Daily exercise",
    "unit": "hr",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# once response is created, comment out this line
graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)


# add a pixel to your graph in pixela

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params = {
    "date": TODAY,
    "quantity": input("How many hours did you exercise today? ")
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)


# update a pixel intensity

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

update_params = {
    "quantity": "4"
}
update_response = requests.put(url=update_endpoint, json=update_params, headers=headers)

# view the graph here https://pixe.la/v1/users/athena/graphs/graph1.html

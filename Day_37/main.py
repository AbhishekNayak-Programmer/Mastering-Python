import requests
from datetime import datetime 

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = 'abhishek7007'
TOKEN = '73843dc2gd84bgd87' # create any string above length 8 of your choice that will be the token 

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

## Creating a USER in Pixela
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ID = "graph1"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_params = {
    "id" : GRAPH_ID,
    "name" : "cycling_graph",
    "unit": 'Km',
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)


PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
date = today.strftime("%Y%m%d")

pixel_data = {
    "date" : date,
    "quantity" : "2.5" 
}

# response = requests.post(PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
# print(response.text)

PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

pixel_updated_data = {
    "quantity" : '4.5',
}


PIXEL_DEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20251003"

res = requests.delete(PIXEL_DEL_ENDPOINT,  headers=headers)
print(res.text)
print(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}")


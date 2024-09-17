from http.client import responses

import requests
from datetime import datetime

WEBSITE = 'https://pixe.la/v1/users'
USERNAME = 'fabulouspvp'
TOKEN = 'alskdjjkzxcnmkjsdhca'
params = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}
#response = requests.post(url=website,json=params)
graph = f'{WEBSITE}/{USERNAME}/graphs'
GRAPH_ID = 'amazingday'
date = datetime(year=2024,month=9,day=11)
graph_params = {
    'id' : GRAPH_ID,
    'name' : 'extremeday',
    'unit' : 'commit',
    'type' : 'int',
    'color' : 'shibafu'
}
header = {
    'X-USER-TOKEN' : TOKEN
}
#response = requests.post(url=graph, json=graph_params, headers=header)

graph_point = f'{WEBSITE}/{USERNAME}/graphs/{GRAPH_ID}'
graph_point_params = {
    'date' : date.strftime('%Y%m%d'),
    'quantity' : '10'
}
#response = requests.post(url=graph_point,json=graph_point_params,headers=header)
graph_update_point = f'{WEBSITE}/{USERNAME}/graphs/{GRAPH_ID}/20240912'
graph_update_params = {
    'quantity' : '5'
}
#response = requests.put(url=graph_update_point,json=graph_update_params,headers=header)
delete_point_response = requests.delete(url=graph_update_point,headers=header)
print(delete_point_response.text)


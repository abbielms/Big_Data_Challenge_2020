#  http://api.openweathermap.org

import requests
from pprint import pprint as pp

appid = 'f4208aa5d94663bf43d34ee10f3ddd50'  # key to connect to the API

endpoint = 'http://api.openweathermap.org/data/2.5/weather'

payload = {
    'q': 'London,UK',
    'unit': 'metrics',
    'appid': appid,
}

response = requests.get(url=endpoint, params=payload)

data = response.json()


pp(data['name'])
pp(data['weather'])

pp(data)

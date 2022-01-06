# client.py

import requests
import json

url = 'http://localhost:5000/register'

response = requests.get(url)

print(response.text)

#!/venv/bin/python
import requests

API = "https://memeservice.cfapps.io/api/memes"

try:
    response = requests.get(API)
    data = response.json()
except:
    print("Error")

print(data)
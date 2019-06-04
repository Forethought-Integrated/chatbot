# importing the requests library
import requests

# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = "delhi technological university"

PARAMS = {'address':location}


r = requests.get(url = URL)

data = r.json()

print(data)

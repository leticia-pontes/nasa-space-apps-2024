import os
import requests
import googlemaps

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('{KEY}')
scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])

session = AuthorizedSession(scoped_credentials)

key = 'AIzaSyDMAO76RJE-dNIdt9PEr-9riqZdc79ROZI'
gmaps = googlemaps.Client(key)

def geocodefunc(placeName):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={placeName}&key={key}"
    response = requests.get(url)
    data = response.json()

    latitude = 0.0
    longitude = 0.0

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")
        latitude = float(location['lat'])
        longitude = float(location['lng'])
        return latitude, longitude
    else:
        return print("Location not found or API request failed")
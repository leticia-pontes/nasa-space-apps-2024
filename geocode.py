import os
import requests
import googlemaps
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

def get_latitude_longitude(place_name):
    key = os.getenv('GOOGLE_MAPS_API_KEY')  # Obtém chave da API do ambiente
    gmaps = googlemaps.Client(key)

    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key={key}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = float(location['lat'])
        longitude = float(location['lng'])
        return latitude, longitude
    else:
        print("Location not found or API request failed")
        return None, None

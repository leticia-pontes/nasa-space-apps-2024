import googlemaps
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

def get_latitude_longitude(place_name):
    key = os.getenv('GOOGLE_MAPS_API_KEY')
    gmaps = googlemaps.Client(key=key)

    geocode_result = gmaps.geocode(place_name)

    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']

        # Acessando o nome da cidade
        address_components = geocode_result[0]['address_components']
        city_name = None

        for component in address_components:
            if 'administrative_area_level_2' in component['types']:
                city_name = component['long_name']
                break

        return latitude, longitude, city_name
    else:
        print("Location not found or API request failed")
        return None, None, None

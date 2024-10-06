import ee
import geemap
from datetime import date
from datetime import timedelta
from geocode import geocodefunc

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('{KEY}')
scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])

session = AuthorizedSession(scoped_credentials)

# Authenticate and initialize Earth Engine
ee.Authenticate()
ee.Initialize(project = 'ee-nasa-hackathon')

def getMoisture(latitude, longitude):

    smap_l4 = ee.ImageCollection("NASA/SMAP/SPL4SMGP/007")

    point_of_interest = ee.Geometry.Point([longitude, latitude])

    start_date = str(date.today() - timedelta(days=30))
    end_date = str(date.today())

    # Filter the image collection for the point of interest and date range
    soil_moisture_images = smap_l4.filterDate(start_date, end_date).filterBounds(point_of_interest)

    # Get the mean soil moisture value at the point of interest
    mean_soil_moisture = soil_moisture_images.select('sm_surface').mean().reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=point_of_interest,
        scale=1000
    )

    # Print the result
    soil_moisture_value = float(mean_soil_moisture.getInfo()['sm_surface'])
    return soil_moisture_value
    print("Mean Soil Moisture Value:", soil_moisture_value)
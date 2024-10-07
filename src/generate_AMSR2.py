import os
from io import BytesIO
from skimage import io
import requests
import json
import ee
import folium
import geemap
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import urllib.request
import urllib.parse
import mapbox_vector_tile
import xml.etree.ElementTree as xmlet
import lxml.etree as xmltree
from PIL import Image as plimg
import numpy as np
from owslib.wms import WebMapService
from IPython.display import Image, display
from datetime import date
from datetime import timedelta

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('{KEY}')
scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])

session = AuthorizedSession(scoped_credentials)

def generateAMSR2_SM():
    # Connect to GIBS WMS Service
    wms = WebMapService('https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi')

    # Configure request for MODIS_Terra_CorrectedReflectance_TrueColor
    img = wms.getmap(layers = ['VIIRS_NOAA20_CorrectedReflectance_TrueColor','LPRM_AMSR2_Surface_Soil_Moisture_C1_Band_Day_Daily',
                            'LPRM_AMSR2_Downscaled_Surface_Soil_Moisture_C1_Band_Day_Daily'],  # Layers
                    srs='epsg:4326',  # Map projection
                    bbox=(-180,-90,180,90),  # Bounds
                    size=(2048, 1024),  # Image size
                    time=date.today()- timedelta(days = 4),  # Time of data
                    format='image/png',  # Image format
                    transparent=True)  # Nodata transparency

    # Save output PNG to a file
    out = open('./VIIRS_Corrected_Reflectance_AMSR2DayNight4Days.png', 'wb')
    out.write(img.read())
    out.close()
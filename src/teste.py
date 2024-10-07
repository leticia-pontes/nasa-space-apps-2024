from geocode import geocodefunc
from datetime import date
from datetime import timedelta
import moisture
import generate_AMSR2

while True:
    print("SMAP/GIBS/EARTH ENGINE INTEGRATION TEST MENU")

    print("1 - Geocode(Generate coordinates based on a Location name or Address)\n")
    print("2 - Soil Moisture(Get the Soil Moisture Value based on the Geocoded Coordinates)\n")
    print("3 - Generate a moisture map(Generated based on data provided via AMSR2 for GIBS API)\n")

    option = int(input("What function do you wish to test? \n\n"))

    if option == 1:
        testlocation = input("Tell me a place and I will tell you the coordinates for it: ")
        latitude,longitude = geocodefunc(testlocation)
        print("This place's latitude is: ",latitude,", and its longitude is: ",longitude)
    if option == 2:
        testlocation = input("Tell me a place and I will tell you the coordinates for it: ")
        latitude,longitude = geocodefunc(testlocation)
        soilmoisture = moisture.getMoisture(latitude,longitude)
        print(soilmoisture)
    if option == 3:
        generate_AMSR2.generateAMSR2_SM()

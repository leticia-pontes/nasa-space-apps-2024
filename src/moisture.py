import ee
from datetime import date, timedelta

def get_moisture(latitude, longitude):
    smap_l4 = ee.ImageCollection("NASA/SMAP/SPL4SMGP/007")

    point_of_interest = ee.Geometry.Point([longitude, latitude])

    start_date = str(date.today() - timedelta(days=30))
    end_date = str(date.today())

    # Filtra a coleção de imagens pela data e ponto de interesse
    soil_moisture_images = smap_l4.filterDate(start_date, end_date).filterBounds(point_of_interest)

    # Calcula o valor médio de umidade do solo no ponto de interesse
    mean_soil_moisture = soil_moisture_images.select('sm_surface').mean().reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=point_of_interest,
        scale=1000
    )

    # Obtém o valor da umidade
    soil_moisture_value = float(mean_soil_moisture.getInfo()['sm_surface'])
    return soil_moisture_value

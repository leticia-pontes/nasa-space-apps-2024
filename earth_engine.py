import ee
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

def initialize_earth_engine():
    ee.Authenticate()
    ee.Initialize(project=os.getenv('EE_PROJECT_ID'))  # ID do projeto do Earth Engine

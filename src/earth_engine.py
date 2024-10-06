import ee
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

def initialize_earth_engine():
    """Autentica e inicializa o Earth Engine."""
    # ee.Authenticate()
    try:
        # Autentica e inicializa o Earth Engine se ainda não foi inicializado
        if not ee.data._credentials:
            ee.Initialize(project=os.getenv('EE_PROJECT_ID'))
            print("Earth Engine initialized.")
    except Exception as e:
        print(f"Error initializing Earth Engine: {e}")

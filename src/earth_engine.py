from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

import ee
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

def initialize_earth_engine():
    """Autentica e inicializa o Earth Engine."""
    try:
        # Carrega as credenciais do JSON
        credentials = service_account.Credentials.from_service_account_file(
            os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        )

        # Define o escopo correto
        scoped_credentials = credentials.with_scopes(
            ['https://www.googleapis.com/auth/earthengine.readonly']
        )
        
        # Inicializa o Earth Engine com as credenciais
        ee.Initialize(scoped_credentials)
        print("Earth Engine initialized.")
    except Exception as e:
        print(f"Error initializing Earth Engine: {e}")

# Chama a função para inicializar o Earth Engine
initialize_earth_engine()

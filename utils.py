import os

def get_api_token():
    # Bonne pratique : lire depuis variable d'environnement
    return os.environ.get("ALTHEA_API_TOKEN")

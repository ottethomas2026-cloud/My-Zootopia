import os
import requests
from typing import Any, Dict, List
from dotenv import load_dotenv

# Umgebungsvariablen aus der .env-Datei laden
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name: str) -> List[Dict[str, Any]]:
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': { ... },
      'locations': [ ... ],
      'characteristics': { ... }
    }
    """
    if not API_KEY:
        print("Fehler: Kein API_KEY in der .env-Datei gefunden!")
        return []

    headers = {"X-Api-Key": API_KEY}
    response = requests.get(f"{API_URL}?name={animal_name}", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: Statuscode {response.status_code}")
        return []
import os
from typing import Any, Dict, List

import requests
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
    if not animal_name or not animal_name.strip():
        return []

    if not API_KEY:
        print("Fehler: Kein API_KEY in der .env-Datei gefunden!")
        return []

    headers = {"X-Api-Key": API_KEY}
    try:
        response = requests.get(
            API_URL,
            params={"name": animal_name},
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            return data
        print("Fehler beim Abrufen der Daten: Erwartete eine Liste als Antwort.")
        return []
    except requests.RequestException as exc:
        print(f"Fehler beim Abrufen der Daten: {exc}")
        return []
    except ValueError:
        print("Fehler beim Abrufen der Daten: Ungültiges JSON von der API erhalten.")
        return []
import os
import requests
from typing import Any, Dict, List
from dotenv import load_dotenv

# Lädt Umgebungsvariablen aus einer .env-Datei (falls vorhanden)
load_dotenv()

# Verwendet deinen API-Schlüssel
API_KEY = os.getenv("API_KEY", "GkEpZcQuF7P8fXMBkSuUSCucQW3phrusfckvWSWv")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name: str) -> List[Dict[str, Any]]:
    """Holt Tierdaten dynamisch von der API Ninja."""
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(f"{API_URL}?name={animal_name}", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: Statuscode {response.status_code}")
        return []


def serialize_animal(animal: Dict[str, Any]) -> str:
    """Serialisiert ein einzelnes Tier-Objekt in ein strukturiertes HTML-Karten-Element."""
    output = '<li class="cards__item">\n'

    # Name der Karte
    name = animal.get("name")
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <div class="card__text">\n'
    output += '    <ul class="card__details">\n'

    characteristics = animal.get("characteristics", {})

    # Ernährung (Diet)
    diet = characteristics.get("diet") or animal.get("diet")
    if diet:
        output += f'      <li class="card__detail-item"><strong>Diet:</strong> {diet}</li>\n'

    # Erster Ort aus der Liste 'locations'
    locations = animal.get("locations", [])
    if locations:
        output += f'      <li class="card__detail-item"><strong>Location:</strong> {locations[0]}</li>\n'

    # Typ (Type)
    animal_type = characteristics.get("type") or animal.get("type")
    if animal_type:
        output += f'      <li class="card__detail-item"><strong>Type:</strong> {animal_type}</li>\n'

    # Skin Type (Hauttyp)
    skin_type = characteristics.get("skin_type")
    if skin_type:
        output += f'      <li class="card__detail-item"><strong>Skin Type:</strong> {skin_type}</li>\n'

    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"
    return output


def generate_animal_info_string(animals_data: List[Dict[str, Any]]) -> str:
    """Erzeugt den gesammelten HTML-String aller gefilterten Tierkarten."""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main() -> None:
    """Hauptfunktion: Holt Daten von der API für 'Fox' und erzeugt das HTML."""
    target_animal = "Fox"
    print(f"Hole Daten von der API für '{target_animal}'...")

    # 1. Daten von der API laden (statt aus der JSON-Datei)
    animals_data = fetch_data(target_animal)

    if not animals_data:
        print(f"Keine Daten für '{target_animal}' gefunden.")
        return

    print(f"Es wurden {len(animals_data)} Ergebnisse für '{target_animal}' geladen.")

    # 2. Template einlesen & Platzhalter ersetzen
    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template_content = handle.read()

    animals_info_string = generate_animal_info_string(animals_data)

    new_html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__", animals_info_string
    )

    # 3. HTML speichern
    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(new_html_content)

    print("Die Datei animals.html wurde erfolgreich aktualisiert!")


if __name__ == "__main__":
    main()
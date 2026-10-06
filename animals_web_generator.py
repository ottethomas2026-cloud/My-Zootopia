import os
import requests
from typing import Any, Dict, List
from dotenv import load_dotenv

# Lädt Umgebungsvariablen aus der .env-Datei
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name: str) -> List[Dict[str, Any]]:
    """Holt Tierdaten dynamisch von der API Ninja."""
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
    """Hauptfunktion: Fragt den Benutzer nach einem Tiernamen und generiert die Webseite."""
    # 1. Benutzereingabe abfragen
    animal_name = input("Enter a name of an animal: ").strip()

    if not animal_name:
        print("Kein Tiername eingegeben. Vorgang abgebrochen.")
        return

    # 2. Daten von der API laden
    animals_data = fetch_data(animal_name)

    # 3. Inhalt erzeugen: Falls keine Tiere gefunden wurden, erstelle eine Fehlermeldung
    if not animals_data:
        animals_info_string = f'<h2>Das Tier "{animal_name}" existiert nicht.</h2>'
    else:
        animals_info_string = generate_animal_info_string(animals_data)

    # 4. Template einlesen & Platzhalter ersetzen
    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template_content = handle.read()

    new_html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__", animals_info_string
    )

    # 5. HTML speichern
    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(new_html_content)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
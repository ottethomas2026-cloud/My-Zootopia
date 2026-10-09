import html
from pathlib import Path
from typing import Any, Dict, List

import data_fetcher

BASE_DIR = Path(__file__).resolve().parent


def _escape_html(value: Any) -> str:
    """Escapes HTML so data from the API cannot break the generated page."""
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def serialize_animal(animal: Dict[str, Any]) -> str:
    """Serialisiert ein einzelnes Tier-Objekt in ein strukturiertes HTML-Karten-Element."""
    if not isinstance(animal, dict):
        return ""

    output = '<li class="cards__item">\n'

    # Name der Karte
    name = animal.get("name")
    if name:
        output += f'  <div class="card__title">{_escape_html(name)}</div>\n'

    output += '  <div class="card__text">\n'
    output += '    <ul class="card__details">\n'

    characteristics = animal.get("characteristics") or {}
    if not isinstance(characteristics, dict):
        characteristics = {}

    # Ernährung (Diet)
    diet = characteristics.get("diet") or animal.get("diet")
    if diet:
        output += f'      <li class="card__detail-item"><strong>Diet:</strong> {_escape_html(diet)}</li>\n'

    # Erster Ort aus der Liste 'locations'
    locations = animal.get("locations") or []
    first_location = ""
    if isinstance(locations, str):
        first_location = locations
    elif isinstance(locations, list):
        first_location = locations[0] if locations else ""
    if first_location:
        output += f'      <li class="card__detail-item"><strong>Location:</strong> {_escape_html(first_location)}</li>\n'

    # Typ (Type)
    animal_type = characteristics.get("type") or animal.get("type")
    if animal_type:
        output += f'      <li class="card__detail-item"><strong>Type:</strong> {_escape_html(animal_type)}</li>\n'

    # Skin Type (Hauttyp)
    skin_type = characteristics.get("skin_type")
    if skin_type:
        output += f'      <li class="card__detail-item"><strong>Skin Type:</strong> {_escape_html(skin_type)}</li>\n'

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

    # 2. Daten über den Data Fetcher laden
    animals_data = data_fetcher.fetch_data(animal_name)

    # 3. Inhalt erzeugen: Falls keine Tiere gefunden wurden, erstelle eine Fehlermeldung
    if not animals_data:
        animals_info_string = f'<h2>Das Tier "{_escape_html(animal_name)}" existiert nicht.</h2>'
    else:
        animals_info_string = generate_animal_info_string(animals_data)

    # 4. Template einlesen & Platzhalter ersetzen
    template_path = BASE_DIR / "animals_template.html"
    output_path = BASE_DIR / "animals.html"

    with template_path.open("r", encoding="utf-8") as handle:
        template_content = handle.read()

    new_html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__", animals_info_string
    )

    # 5. HTML speichern
    with output_path.open("w", encoding="utf-8") as handle:
        handle.write(new_html_content)

    print(f"Website was successfully generated to the file {output_path.name}.")


if __name__ == "__main__":
    main()
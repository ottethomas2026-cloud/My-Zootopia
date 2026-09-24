import json
from typing import Any, Dict, List, Set


def load_data(file_path: str) -> List[Dict[str, Any]]:
    """Lädt eine JSON-Datei und gibt die Datenstruktur zurück."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_available_skin_types(animals_data: List[Dict[str, Any]]) -> Set[str]:
    """Sammelt alle eindeutigen skin_type-Werte aus den Tierdaten."""
    skin_types = set()
    for animal in animals_data:
        characteristics = animal.get("characteristics", {})
        skin_type = characteristics.get("skin_type")
        if skin_type:
            skin_types.add(skin_type)
    return skin_types


def serialize_animal(animal: Dict[str, Any]) -> str:
    """Serialisiert ein einzelnes Tier-Objekt in ein strukturiertes HTML-Karten-Element."""
    output = '<li class="cards__item">\n'

    # Titel / Name der Karte
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
    """Hauptfunktion: Lädt Daten, lässt den Benutzer filtern und generiert das HTML."""
    animals_data = load_data("animals_data.json")

    # 1. Verfügbare Skin Types ermitteln
    available_skin_types = get_available_skin_types(animals_data)

    print("Verfügbare Hauttypen (Skin Types):")
    for st in sorted(available_skin_types):
        print(f" - {st}")
    print()

    # 2. Benutzereingabe abfragen
    selected_skin_type = input(
        "Bitte wähle einen Skin Type aus der Liste (oder drücke Enter für ALLE Tiere): "
    ).strip()

    # 3. Tiere filtern
    if selected_skin_type:
        filtered_animals = [
            animal
            for animal in animals_data
            if animal.get("characteristics", {})
            .get("skin_type", "")
            .lower()
            == selected_skin_type.lower()
        ]
        print(
            f"\nEs wurden {len(filtered_animals)} Tiere mit Skin Type '{selected_skin_type}' gefunden."
        )
    else:
        filtered_animals = animals_data
        print(f"\nZeige alle {len(filtered_animals)} Tiere an.")

    # 4. Template einlesen & Platzhalter ersetzen
    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template_content = handle.read()

    animals_info_string = generate_animal_info_string(filtered_animals)

    new_html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__", animals_info_string
    )

    # 5. HTML speichern
    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(new_html_content)

    print("Die Datei animals.html wurde erfolgreich aktualisiert!")


if __name__ == "__main__":
    main()
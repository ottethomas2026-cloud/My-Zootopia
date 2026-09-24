import json

DATA_FILE_PATH = "animals_data.json"
TEMPLATE_FILE_PATH = "animals_template.html"
OUTPUT_FILE_PATH = "animals.html"


def load_data(file_path):
    """Lädt und gibt den Inhalt einer JSON-Datei zurück."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Serialisiert ein einzelnes Tier-Objekt in ein HTML-Karten-Element."""
    output = '<li class="cards__item">\n'

    # Name / Titel der Karte
    if "name" in animal and animal["name"]:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    # Diet (Ernährung)
    diet = characteristics.get("diet") or animal.get("diet")
    if diet:
        output += f"      <strong>Diet:</strong> {diet}<br/>\n"

    # Location (Erster Ort)
    locations = animal.get("locations", [])
    if locations and len(locations) > 0:
        output += f"      <strong>Location:</strong> {locations[0]}<br/>\n"

    # Type (Typ)
    animal_type = characteristics.get("type") or animal.get("type")
    if animal_type:
        output += f"      <strong>Type:</strong> {animal_type}<br/>\n"

    output += "  </p>\n"
    output += "</li>\n"

    return output


def generate_animals_html(animals_data):
    """Erzeugt den gesammelten HTML-String für alle Tiere in der Liste."""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main():
    """Hauptfunktion zum Steuern des Workflows."""
    # 1. Daten und Vorlage einlesen
    animals_data = load_data(DATA_FILE_PATH)

    with open(TEMPLATE_FILE_PATH, "r", encoding="utf-8") as handle:
        template_content = handle.read()

    # 2. Tierdaten in HTML-Karten umwandeln
    animals_info_string = generate_animals_html(animals_data)

    # 3. Platzhalter ersetzen
    new_html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__", animals_info_string
    )

    # 4. In Ziel-HTML-Datei schreiben
    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as handle:
        handle.write(new_html_content)

    print(f"Die Datei {OUTPUT_FILE_PATH} wurde erfolgreich erstellt.")


if __name__ == "__main__":
    main()
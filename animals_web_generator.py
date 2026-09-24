import json


def load_data(file_path):
    """Lädt eine JSON-Datei"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Serialisiert ein einzelnes Tier-Objekt in ein HTML-Listenelement (<li>)"""
    output = '<li class="cards__item">\n'

    # Name
    if "name" in animal and animal["name"]:
        output += f"  Name: {animal['name']}<br/>\n"

    characteristics = animal.get("characteristics", {})

    # Ernährung (Diet)
    diet = characteristics.get("diet") or animal.get("diet")
    if diet:
        output += f"  Diet: {diet}<br/>\n"

    # Erster Ort aus der Liste 'locations'
    locations = animal.get("locations", [])
    if locations and len(locations) > 0:
        output += f"  Location: {locations[0]}<br/>\n"

    # Typ (Type)
    animal_type = characteristics.get("type") or animal.get("type")
    if animal_type:
        output += f"  Type: {animal_type}<br/>\n"

    output += "</li>\n"
    return output


def generate_animal_info_string(animals_data):
    """Erzeugt den HTML-String aller Tiere"""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main():
    # 1. Daten und HTML-Template einlesen
    animals_data = load_data("animals_data.json")

    with open("animals_template.html", "r") as handle:
        template_content = handle.read()

    # 2. HTML-Karten-String für die Tiere erzeugen
    animals_info_string = generate_animal_info_string(animals_data)

    # 3. Platzhalter im Template ersetzen
    new_html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__", animals_info_string
    )

    # 4. In animals.html schreiben
    with open("animals.html", "w") as handle:
        handle.write(new_html_content)

    print("Die Datei animals.html wurde mit HTML-Karten aktualisiert!")


if __name__ == "__main__":
    main()
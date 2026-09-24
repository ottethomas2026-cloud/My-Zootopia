import json


def load_data(file_path):
    """Lädt eine JSON-Datei"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Erzeugt einen formatierten String für ein einzelnes Tier"""
    output = ""

    # Name
    if "name" in animal and animal["name"]:
        output += f"Name: {animal['name']}\n"

    characteristics = animal.get("characteristics", {})

    # Ernährung (Diet)
    diet = characteristics.get("diet") or animal.get("diet")
    if diet:
        output += f"Diet: {diet}\n"

    # Location (erster Ort)
    locations = animal.get("locations", [])
    if locations and len(locations) > 0:
        output += f"Location: {locations[0]}\n"

    # Typ (Type)
    animal_type = characteristics.get("type") or animal.get("type")
    if animal_type:
        output += f"Type: {animal_type}\n"

    return output


def generate_animal_info_string(animals_data):
    """Erzeugt den Gesamt-String aller Tiere"""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main():
    # 1. Daten und Template einlesen
    animals_data = load_data("animals_data.json")

    with open("animals_template.html", "r") as handle:
        template_content = handle.read()

    # 2. String mit Tierdaten erzeugen
    animals_info_string = generate_animal_info_string(animals_data)

    # 3. Platzhalter ersetzen
    new_html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__", animals_info_string
    )

    # 4. In animals.html schreiben
    with open("animals.html", "w") as handle:
        handle.write(new_html_content)

    print("Die Datei animals.html wurde erfolgreich erstellt!")


if __name__ == "__main__":
    main()
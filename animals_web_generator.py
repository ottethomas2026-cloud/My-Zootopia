import json


def load_data(file_path):
    """Lädt eine JSON-Datei"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animals_info(animals_data):
    for animal in animals_data:
        # Name ausgeben
        if "name" in animal and animal["name"]:
            print(f"Name: {animal['name']}")

        # Eigenschaften (characteristics) abrufen
        characteristics = animal.get("characteristics", {})

        # Ernährung (Diet)
        diet = characteristics.get("diet") or animal.get("diet")
        if diet:
            print(f"Diet: {diet}")

        # Erster Ort aus der Liste 'locations'
        locations = animal.get("locations", [])
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")

        # Typ (Type)
        animal_type = characteristics.get("type") or animal.get("type")
        if animal_type:
            print(f"Type: {animal_type}")

        # Leerzeile zur Trennung der einzelnen Tiere
        print()


def main():
    animals_data = load_data("animals_data.json")
    print_animals_info(animals_data)


if __name__ == "__main__":
    main()
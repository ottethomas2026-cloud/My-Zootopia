# 🐾 My-Zootopia

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Ein Python-basierter HTML-Webgenerator, der strukturierte Tierdaten aus einer JSON-Datei ausliest und dynamisch in eine interaktive Weboberfläche einbettet.

---

## 📌 Übersicht

**My-Zootopia** parst eine JSON-Datenbank mit Tierdaten (`animals_data.json`), filtert diese nach Wunsch und generiert mithilfe einer HTML-Vorlage (`animals_template.html`) eine fertige Webseite (`animals.html`).

### ✨ Hauptfunktionen
* 📄 **JSON-Parsing**: Sichere Extraktion verschachtelter Tierdaten (Name, Ernährung, Orte, Typ).
* 🔍 **Interaktive Filterung**: Dynamische Filterung im Terminal nach `skin_type` (z. B. *Hair*, *Scales*).
* 🛡️ **Fehlertoleranz**: Robuste Handhabung fehlender Felder mittels `.get()` ohne Laufzeitfehler.
* 🎨 **Clean Code**: Vollständig konform mit **PEP 8**, inklusive Type Hints und modularer Funktionen (`serialize_animal`).

---

## 📁 Dateistruktur

```text
My-Zootopia/
├── animals_data.json        # Quelldatei mit den Tierdaten
├── animals_template.html    # HTML-Vorlage mit Platzhalter __REPLACE_ANIMALS_INFO__
├── animals_web_generator.py # Hauptskript zur Logik & HTML-Generierung
├── animals.html             # Generierte Ziel-Webseite
└── README.md                # Dokumentation
🚀 Schnellstart
1. Repository klonen
Bash
git clone [https://github.com/ottethomas2026-cloud/My-Zootopia.git](https://github.com/ottethomas2026-cloud/My-Zootopia.git)
cd My-Zootopia
2. Skript ausführen
Bash
python3 animals_web_generator.py
3. Filter wählen & Ergebnis anzeigen
Wähle im Terminal einen verfügbaren skin_type aus (oder drücke Enter für alle Tiere).

Öffne die neu generierte animals.html im Browser deiner Wahl oder über die Live-Vorschau in Codio.

⚙️ Funktionsweise im Code
Das Skript ist modular aufgebaut:

load_data(file_path): Liest die JSON-Datei sicher mit UTF-8-Encoding ein.

get_available_skin_types(animals_data): Ermittelt dynamisch alle vorhandenen Hauttypen.

serialize_animal(animal_obj): Wandelt ein einzelnes Tierobjekt in ein sauberes HTML-Karten-Element (<li class="cards__item">) um.

main(): Steuert die Benutzereingabe, Filterung und das Ersetzen des Platzhalters in der Template-Datei.

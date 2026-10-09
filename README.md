# My Zootopia API & Website Generator

Dieses Projekt ermöglicht es Benutzern, nach beliebigen Tierarten zu suchen und automatisch eine strukturierte, ansprechende HTML-Webseite mit detaillierten Informationen über das gewählte Tier (z. B. Ernährung, Lebensraum, Typ und Hauttyp) zu generieren.

## Funktionen

- **Dynamischer API-Abruf:** Ruft Echtzeit-Tierdaten von API Ninja ab.
- **Modulare Architektur:** Klare Trennung zwischen Datenbeschaffung (`data_fetcher.py`) und Webseitenerstellung (`animals_web_generator.py`).
- **Sichere Konfiguration:** Verwendet eine `.env`-Datei, um API-Schlüssel sicher zu verwalten.
- **Benutzerfreundliches Feedback:** Zeigt eine passende Fehlermeldung auf der Webseite an, falls ein eingegebenes Tier nicht existiert.

## Installation

1. **Repository klonen:**
   ```bash
   git clone [https://github.com/ottethomas2026-cloud/My-Zootopia.git](https://github.com/ottethomas2026-cloud/My-Zootopia.git)
   cd My-Zootopia

   Abhängigkeiten installieren:

Bash
pip install -r requirements.txt
Umgebungsvariablen einrichten:
Erstelle eine .env-Datei im Root-Verzeichnis deines Projekts und füge deinen API Ninja Schlüssel ein:

Code-Snippet
API_KEY=DEIN_API_KEY_HIER
Nutzung
Starte das Hauptprogramm über das Terminal:

Bash
python animals_web_generator.py
Gib nach Aufforderung den Namen eines Tiers ein (z. B. cheetah, fox oder dog). Das Skript generiert anschließend die Datei animals.html, die du im Browser öffnen kannst.

Mitwirken
Beiträge sind herzlich willkommen! Wenn du Verbesserungsvorschläge oder neue Features hinzufügen möchtest, erstelle einfach einen Pull Request oder öffne ein Issue.


---

### Speichern, Committen & Pushen

Führe danach diese Befehle in deinem VS Code Terminal aus, um die Aufgabe abzuschließen:

```powershell
git add README.md
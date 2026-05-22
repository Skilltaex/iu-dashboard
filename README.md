# IU Portfolio: Notenverwaltungssystem

Ein modulares Konsolenprogramm zur Verwaltung von Studienleistungen und zur Berechnung des gewichteten Notendurchschnitts nach ECTS. Entwickelt als Portfolio-Projekt an der IU Hochschule.

## 🌟 Features
- **MVC-Architektur:** Strikte Trennung von Datenmodell, Logik und Benutzeroberfläche.
- **Persistente Datenspeicherung:** Automatische Sicherung und Laden der Daten über JSON.
- **Robuste Validierung:** Fehlerfreie Verarbeitung von Kommas/Punkten bei Noten und Schutz vor Falscheingaben.
- **Moderner Tech-Stack:** Projekt- und Abhängigkeitsverwaltung via `uv`.

## 🏗️ Architektur (MVC-Muster)
Das Projekt ist nach dem Model-View-Controller-Muster strukturiert, um Wartbarkeit und Erweiterbarkeit zu garantieren:
- `models/`: Definiert die Datenstruktur des `Modul`-Objekts.
- `ui/`: Übernimmt die Interaktivität im Terminal (CLI).
- `controller/`: Steuert die Programmlogik und mathematische Berechnungen.
- `storage/`: Verwaltet das Lesen und Schreiben der Daten in `noten_daten.json`.

## 🚀 Installation & Start

Dieses Projekt nutzt das moderne Python-Werkzeug `uv` für maximale Performance.

1. **Abhängigkeiten installieren & Umgebung starten:**
   ```powershell
   uv sync
   ```
2. **Programm ausführen:**
   ```powershell
   uv run main.py
   ```

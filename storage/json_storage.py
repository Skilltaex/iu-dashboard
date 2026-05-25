"""
Repository-Schicht (Datenzugriffsebene) für das IU-Dashboard.
Kapselt das Lesen und Schreiben von Daten in einem persistenten JSON-Format.
Stellt sicher, dass Daten sitzungsübergreifend und plattformunabhängig erhalten bleiben.
"""

import json
import os
from models.modul import Modul

class JsonStorage:
    """Verwaltet das Laden und Speichern der Studiendaten in einer JSON-Datei."""
    
    def __init__(self, dateiname: str = None) -> None:
        """
        Initialisiert die Speicherkomponente und berechnet einen robusten, 
        absoluten Pfad zur JSON-Datei, um Ausführungsfehler zu verhindern.
        """
        if dateiname is None:
            # Ermittelt das Verzeichnis, in dem diese json_storage.py liegt (storage/)
            basis_verzeichnis = os.path.dirname(os.path.abspath(__file__))
            # Setzt den Pfad absolut auf storage/noten_daten.json
            self.dateiname = os.path.join(basis_verzeichnis, "noten_daten.json")
        else:
            self.dateiname = dateiname

    def speichern(self, module: list) -> None:
        """
        Konvertiert alle Modul-Objekte in Dictionaries und speichert sie als JSON.

        Args:
            module (list): Eine Liste von Modul-Instanzen, die gesichert werden sollen.
        """
        # List Comprehension zur Serialisierung der Objekte
        daten = [m.to_dict() for m in module]
        
        # Sicheres Öffnen der Datei mit UTF-8 Kodierung für deutsche Umlaute
        with open(self.dateiname, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)

    def laden(self) -> list:
        """
        Lädt die gespeicherten Module aus der JSON-Datei und rekonstruiert die Objekte.

        Returns:
            list: Eine Liste rekonstruierter Modul-Objekte oder eine leere Liste.
        """
        # Prüft, ob die Datei überhaupt existiert, um Fehler zu vermeiden
        if not os.path.exists(self.dateiname):
            return []
        
        # Abfangen von korrupten JSON-Strukturen oder fehlenden Schlüsseln
        try:
            with open(self.dateiname, "r", encoding="utf-8") as f:
                daten = json.load(f)
                # Deserialisierung: Erzeugt echte Modul-Objekte aus den JSON-Daten
                return [Modul(d["name"], d["note"], d["ects"]) for d in daten]
        except (json.JSONDecodeError, KeyError):
            print("[!] Fehler beim Lesen der Speicherdatei. Das Dashboard startet leer.")
            return []
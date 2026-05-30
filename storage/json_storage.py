"""
Konkrete Umsetzung der Datenzugriffsebene unter Verwendung des JSON-Formats.
Erbt von der abstrakten Schnittstelle BaseStorage (Repository-Abstraktion).
"""

import json
import os
from models.modul import Modul
from storage.base_storage import BaseStorage

class JsonStorage(BaseStorage):
    """Verwaltet das Laden und Speichern der Studiendaten in einer JSON-Datei."""
    
    def __init__(self, dateiname: str = None) -> None:
        """Initialisiert die konkrete JSON-Speicherkomponente."""
        if dateiname is None:
            basis_verzeichnis = os.path.dirname(os.path.abspath(__file__))
            self.dateiname = os.path.join(basis_verzeichnis, "noten_daten.json")
        else:
            self.dateiname = dateiname

    def speichern(self, module: list) -> None:
        """Konvertiert alle Modul-Objekte und sichert sie in der JSON-Datei."""
        daten = [m.to_dict() for m in module]
        with open(self.dateiname, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)

    def laden(self) -> list:
        """Lädt die gespeicherten Module aus der JSON-Datei und rekonstruiert sie."""
        if not os.path.exists(self.dateiname):
            return []
        try:
            with open(self.dateiname, "r", encoding="utf-8") as f:
                daten = json.load(f)
                return [Modul(d["name"], d["note"], d["ects"]) for d in daten]
        except (json.JSONDecodeError, KeyError):
            print("[!] Fehler beim Lesen der Speicherdatei. Das Dashboard startet leer.")
            return []
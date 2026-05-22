import json
import os
from models.modul import Modul

class JsonStorage:
    def __init__(self, dateiname="storage/noten_daten.json"):
        self.dateiname = dateiname

    def speichern(self, module):
        """Speichert alle Module als JSON-Datei"""
        daten = [m.to_dict() for m in module]
        with open(self.dateiname, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)

    def laden(self):
        """Lädt alle Module aus der JSON-Datei"""
        if not os.path.exists(self.dateiname):
            return []
        
        try:
            with open(self.dateiname, "r", encoding="utf-8") as f:
                daten = json.load(f)
                return [Modul(d["name"], d["note"], d["ects"]) for d in daten]
        except (json.JSONDecodeError, KeyError):
            print("[!] Fehler beim Laden der Speicherdatei. Starte leer.")
            return []

"""
Konkrete Umsetzung der Datenzugriffsebene unter Verwendung des JSON-Formats.
Erbt von der abstrakten Schnittstelle BaseStorage und persistiert die Aggregatwurzel.
"""

import json
import os
from models.studiengang import Studiengang
from models.semester import Semester
from models.modul import Modul
from storage.base_storage import BaseStorage

class JsonStorage(BaseStorage):
    """Verwaltet das Laden und Speichern des gesamten Studiengangs."""
    
    def __init__(self, dateiname: str = None) -> None:
        """Initialisiert die JSON-Speicherkomponente mit relativem Pfad."""
        if dateiname is None:
            basis_verzeichnis = os.path.dirname(os.path.abspath(__file__))
            self.dateiname = os.path.join(basis_verzeichnis, "studiengang_daten.json")
        else:
            self.dateiname = dateiname

    def speichern(self, studiengang: Studiengang) -> None:
        """Sichert die vollständige, hierarchische Domänenstruktur (Aggregatwurzel)."""
        daten = studiengang.to_dict()
        with open(self.dateiname, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)

    def laden(self) -> Studiengang:
        """Rekonstruiert das gesamte verschachtelte Fachmodell aus der JSON-Datei."""
        standard_stg = Studiengang("Informatik", 6, 1.5)
        
        if not os.path.exists(self.dateiname):
            standard_stg.semester_liste.append(Semester(1, "1. Semester"))
            return standard_stg
        
        try:
            with open(self.dateiname, "r", encoding="utf-8") as f:
                daten = json.load(f)
                stg = Studiengang(daten["name"], daten["regelstudienzeit"], daten["angestrebter_schnitt"])
                
                for s_daten in daten.get("semester", []):
                    sem = Semester(s_daten["semester_nummer"], s_daten["bezeichnung"])
                    for m_daten in s_daten.get("module", []):
                        sem.module.append(Modul(m_daten["name"], m_daten["note"], m_daten["ects"]))
                    stg.semester_liste.append(sem)
                return stg
        except Exception:
            standard_stg.semester_liste.append(Semester(1, "1. Semester"))
            return standard_stg
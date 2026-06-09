"""
Controller-Schicht (Business-Logik) für das IU-Dashboard.
Fungiert als reiner Koordinator. Nutzt das abstrakte Interface BaseStorage
und delegiert mathematische Berechnungen an den NotenService.
"""

from models.modul import Modul
from storage.base_storage import BaseStorage
from services.noten_service import NotenService

"""
Controller-Schicht (Business-Logik) für das IU-Dashboard.
Fungiert als Koordinator und steuert das Fachmodell ausschließlich über
die Aggregatwurzel (Studiengang).
"""

from models.studiengang import Studiengang
from models.modul import Modul
from storage.base_storage import BaseStorage
from services.noten_service import NotenService

class NotenController:
    """Verwaltet die Steuerungslogik über die Aggregatwurzel Studiengang."""
    
    def __init__(self, storage: BaseStorage) -> None:
        """Nutzt Dependency Injection für lose Kopplung."""
        self.storage = storage
        self.studiengang: Studiengang = self.storage.laden()

    def modul_hinzufuegen(self, name: str, note: float, ects: int) -> None:
        """Fügt ein Modul dem ersten Semester des Studiengangs hinzu."""
        neues_modul = Modul(name, note, ects)
        if self.studiengang.semester_liste:
            self.studiengang.semester_liste[0].module.append(neues_modul)
            self.storage.speichern(self.studiengang)

    def modul_loeschen(self, index: int) -> bool:
        """Löscht ein Modul aus dem ersten Semester über die Wurzel."""
        if self.studiengang.semester_liste:
            module = self.studiengang.semester_liste[0].module
            if 0 <= index < len(module):
                module.pop(index)
                self.storage.speichern(self.studiengang)
                return True
        return False

    def berechne_gewichteten_schnitt(self) -> float:
        """Delegiert die mathematische Notenberechnung an den NotenService."""
        return NotenService.berechne_gewichteten_schnitt(self.studiengang)
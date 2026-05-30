"""
Controller-Schicht (Business-Logik) für das IU-Dashboard.
Fungiert als reiner Koordinator. Nutzt das abstrakte Interface BaseStorage
und delegiert mathematische Berechnungen an den NotenService.
"""

from models.modul import Modul
from storage.base_storage import BaseStorage
from services.noten_service import NotenService

class NotenController:
    """Verwaltet die Steuerungslogik und koordiniert Datenströme."""
    
    def __init__(self, storage: BaseStorage) -> None:
        """
        Nutzt Dependency Injection, um lose Kopplung zu garantieren.
        Erwartet eine Schnittstelle vom Typ BaseStorage.
        """
        self.storage = storage
        self.module = self.storage.laden()

    def modul_hinzufuegen(self, name: str, note: float, ects: int) -> None:
        """Delegiert die Erstellung und Speicherung eines neuen Moduls."""
        neues_modul = Modul(name, note, ects)
        self.module.append(neues_modul)
        self.storage.speichern(self.module)

    def modul_loeschen(self, index: int) -> bool:
        """Löscht ein Modul über den Index und aktualisiert die Persistenzschicht."""
        if 0 <= index < len(self.module):
            self.module.pop(index)
            self.storage.speichern(self.module)
            return True
        return False

    def berechne_gewichteten_schnitt(self) -> float:
        """
        Delegiert die mathematische Notenberechnung vollständig
        an die dedizierte Service-Schicht (NotenService).
        """
        return NotenService.berechne_gewichteten_schnitt(self.module)
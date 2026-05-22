from models.modul import Modul
from storage.json_storage import JsonStorage

class NotenController:
    """Verwaltet die Programmlogik, Berechnungen und Speicherzugriffe."""
    
    def __init__(self):
        self.storage = JsonStorage()
        # Lädt persistente Daten direkt beim Programmstart
        self.module = self.storage.laden()

    def modul_hinzufuegen(self, name: str, note: float, ects: int):
        """Erstellt ein neues Modul und speichert es ab."""
        neues_modul = Modul(name, note, ects)
        self.module.append(neues_modul)
        self.storage.speichern(self.module)

    def modul_loeschen(self, index: int) -> bool:
        """Löscht ein Modul anhand des Listen-Index und aktualisiert den Speicher."""
        if 0 <= index < len(self.module):
            self.module.pop(index)
            self.storage.speichern(self.module)
            return True
        return False

    def berechne_gewichteten_schnitt(self) -> float:
        """Berechnet den offiziellen, ECTS-gewichteten IU-Notendurchschnitt."""
        total_ects = sum(m.ects for m in self.module)
        if total_ects == 0:
            return 0.0
        
        # Summe aus (Note * ECTS) für alle Module
        gewichtete_noten_summe = sum(m.note * m.ects for m in self.module)
        return gewichtete_noten_summe / total_ects

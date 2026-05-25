"""
Controller-Schicht (Business-Logik / Service-Ebene) für das IU-Dashboard.
Verantwortlich für die Verwaltung der Modulliste, die mathematische Berechnung
des Notendurchschnitts sowie die Koordination der persistenten Datenspeicherung.
"""

from models.modul import Modul
from storage.json_storage import JsonStorage

class NotenController:
    """Verwaltet die zentrale Programmlogik, Berechnungen und Speicherzugriffe."""
    
    def __init__(self) -> None:
        """Initialisiert den Controller und lädt automatisch bestehende Daten."""
        self.storage = JsonStorage()
        # Lädt persistente Daten direkt beim Programmstart aus dem Repository
        self.module = self.storage.laden()

    def modul_hinzufuegen(self, name: str, note: float, ects: int) -> None:
        """
        Erstellt ein neues Modul-Objekt, fügt es der Liste hinzu und speichert es.

        Args:
            name (str): Der Name des neuen Moduls.
            note (float): Die erzielte Modulnote.
            ects (int): Die ECTS-Punkte des Moduls.
        """
        neues_modul = Modul(name, note, ects)
        self.module.append(neues_modul)
        self.storage.speichern(self.module)

    def modul_loeschen(self, index: int) -> bool:
        """
        Löscht ein Modul anhand des Listen-Index und aktualisiert den Speicher.

        Args:
            index (int): Der 0-basierte Listenindex des zu löschenden Moduls.

        Returns:
            bool: True, wenn das Modul gelöscht wurde; False bei ungültigem Index.
        """
        if 0 <= index < len(self.module):
            self.module.pop(index)
            self.storage.speichern(self.module)
            return True
        return False

    def berechne_gewichteten_schnitt(self) -> float:
        """
        Berechnet den offiziellen, ECTS-gewichteten IU-Notendurchschnitt.

        Returns:
            float: Der gewichtete Notenschnitt oder 0.0, wenn keine Module existieren.
        """
        total_ects = sum(m.ects for m in self.module)
        # Verhindert einen Systemabsturz durch Division durch Null (ZeroDivisionError)
        if total_ects == 0:
            return 0.0
        
        # Mathematische Gewichtung: Summe aus (Note * ECTS) für alle erfassten Module
        gewichtete_noten_summe = sum(m.note * m.ects for m in self.module)
        return gewichtete_noten_summe / total_ects
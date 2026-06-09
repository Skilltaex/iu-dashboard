"""
Domain-Schicht (Datenmodell) für das IU-Dashboard.
Definiert die Semester-Klasse, die als Aggregatkomponente zwischen
dem Studiengang und den einzelnen Modulen fungiert.
"""

from models.modul import Modul

class Semester:
    """Verwaltet eine Liste von Modulen innerhalb eines spezifischen Semesters."""
    
    def __init__(self, semester_nummer: int, bezeichnung: str) -> None:
        """
        Initialisiert ein Semester-Objekt.

        Args:
            semester_nummer (int): Die fortlaufende Nummer des Semesters.
            bezeichnung (str): Die textuelle Bezeichnung (z. B. '1. Semester').
        """
        self.semester_nummer = semester_nummer
        self.bezeichnung = bezeichnung
        self.module: list[Modul] = []

    def to_dict(self) -> dict:
        """
        Konvertiert das Semester und seine Module in ein Dictionary für den JSON-Export.

        Returns:
            dict: Eine verschachtelte Schlüssel-Wert-Struktur der Semesterdaten.
        """
        return {
            "semester_nummer": self.semester_nummer,
            "bezeichnung": self.bezeichnung,
            "module": [m.to_dict() for m in self.module]
        }
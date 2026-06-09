"""
Domain-Schicht (Datenmodell) für das IU-Dashboard.
Definiert die Klasse Studiengang, die als Aggregatwurzel (Aggregate Root)
das gesamte hierarchische Fachmodell nach außen hin kapselt.
"""

from models.semester import Semester

class Studiengang:
    """Repräsentiert die Aggregatwurzel des Fachmodells zur Notenverwaltung."""
    
    def __init__(self, name: str, regelstudienzeit: int, angestrebter_schnitt: float) -> None:
        """
        Initialisiert ein Studiengang-Objekt.

        Args:
            name (str): Der Name des Studiengangs (z. B. 'Informatik').
            regelstudienzeit (int): Die Regelstudienzeit in Semestern.
            angestrebter_schnitt (float): Der vom Studierenden angestrebte Notenschnitt.
        """
        self.name = name
        self.regelstudienzeit = regelstudienzeit
        self.angestrebter_schnitt = angestrebter_schnitt
        # Hält die untergeordneten Semester-Objekte (Kompositionsstruktur)
        self.semester_liste: list[Semester] = []

    def to_dict(self) -> dict:
        """
        Konvertiert die gesamte hierarchische Struktur für den persistenten JSON-Export.

        Returns:
            dict: Eine tief verschachtelte Schlüssel-Wert-Struktur des Gesamtmodells.
        """
        return {
            "name": self.name,
            "regelstudienzeit": self.regelstudienzeit,
            "angestrebter_schnitt": self.angestrebter_schnitt,
            "semester": [s.to_dict() for s in self.semester_liste]
        }
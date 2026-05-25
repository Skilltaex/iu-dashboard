"""
Domain-Schicht (Datenmodell) für das IU-Dashboard.
Definiert die Kern-Datenstruktur für ein einzelnes Studienmodul.
Diese Klasse enthält ausschließlich Attribute und typspezifische Konvertierungen.
"""

class Modul:
    """Repräsentiert ein einzelnes Studienmodul an der IU."""
    
    def __init__(self, name: str, note: float, ects: int):
        """
        Initialisiert ein neues Modul-Objekt.

        Args:
            name (str): Der Name des Moduls (z. B. Einführung in die Programmierung mit Python).
            note (float): Die erzielte Modulnote (Bereich 1.0 bis 5.0).
            ects (int): Die dem Modul zugewiesenen ECTS-Punkte.
        """
        self.name = name   # Name des Moduls
        self.note = note   # Erreichte Note
        self.ects = ects   # ECTS-Punkte des Moduls

    def to_dict(self) -> dict:
        """
        Konvertiert das Objekt in ein Dictionary für den JSON-Export.

        Returns:
            dict: Eine Schlüssel-Wert-Struktur der Objekt-Attribute.
        """
        return {"name": self.name, "note": self.note, "ects": self.ects}
class Modul:
    """Repräsentiert ein einzelnes Studienmodul an der IU."""
    
    def __init__(self, name: str, note: float, ects: int):
        self.name = name   # Name des Moduls (z.B. Python)
        self.note = note   # Erreichte Note (1.0 bis 5.0)
        self.ects = ects   # ECTS-Punkte des Moduls

    def to_dict(self):
        """Konvertiert das Objekt in ein Dictionary für den JSON-Export."""
        return {"name": self.name, "note": self.note, "ects": self.ects}


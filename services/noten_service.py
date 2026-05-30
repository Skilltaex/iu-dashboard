"""
Service-Schicht (Business-Logik) für das IU-Dashboard.
Übernimmt die reine mathematische Berechnungslogik der Noten.
Kapselt Berechnungen über Modulsammlungen hinweg im Sinne des Schichtenmodells.
"""

class NotenService:
    """Kapselt mathematische und statistische Berechnungen für Studienmodule."""

    @staticmethod
    def berechne_gewichteten_schnitt(module: list) -> float:
        """
        Berechnet den offiziellen, ECTS-gewichteten IU-Notendurchschnitt.

        Args:
            module (list): Eine Liste von Modul-Objekten, die bewertet werden.

        Returns:
            float: Der gewichtete Notenschnitt oder 0.0, wenn die Gesamt-ECTS Null sind.
        """
        # Summiert alle ECTS-Punkte der übergebenen Module auf
        total_ects = sum(m.ects for m in module)
        
        # Verhindert einen Systemabsturz durch Division durch Null (ZeroDivisionError)
        if total_ects == 0:
            return 0.0
        
        # Mathematische Gewichtung: Summe aus (Note * ECTS) für alle erfassten Module
        gewichtete_noten_summe = sum(m.note * m.ects for m in module)
        
        # Berechnung und Rückgabe des gewichteten Gesamtdurchschnitts
        return gewichtete_noten_summe / total_ects
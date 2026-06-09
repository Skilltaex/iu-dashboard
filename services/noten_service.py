"""
Service-Schicht (Business-Logik) für das IU-Dashboard.
Übernimmt die mathematische Berechnungslogik über die Aggregatwurzel.
Kapselt Berechnungen über Modulsammlungen hinweg im Sinne des Schichtenmodells.
"""

from models.studiengang import Studiengang

class NotenService:
    """Kapselt mathematische und statistische Berechnungen für das Fachmodell."""

    @staticmethod
    def berechne_gewichteten_schnitt(studiengang: Studiengang) -> float:
        """
        Sammelt alle Module aus allen Semestern der Aggregatwurzel und
        berechnet den offiziellen, ECTS-gewichteten IU-Notendurchschnitt.

        Args:
            studiengang (Studiengang): Die Aggregatwurzel des Fachmodells.

        Returns:
            float: Der gewichtete Notenschnitt oder 0.0, wenn die Gesamt-ECTS Null sind.
        """
        alle_module = []
        for semester in studiengang.semester_liste:
            alle_module.extend(semester.module)

        total_ects = sum(m.ects for m in alle_module)
        if total_ects == 0:
            return 0.0
        
        gewichtete_noten_summe = sum(m.note * m.ects for m in alle_module)
        return gewichtete_noten_summe / total_ects
class NotenService:
    @staticmethod
    def berechne_gewichteten_schnitt(module: list) -> float:
        total_ects = sum(m.ects for m in module)
        if total_ects == 0:
            return 0.0
        
        gewichtete_noten_summe = sum(m.note * m.ects for m in module)
        return gewichtete_noten_summe / total_ects
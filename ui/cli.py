class NotenUI:
    @staticmethod
    def zeige_menue():
        print("\n--- MENÜ ---")
        print("1. Modul hinzufügen")
        print("2. Alle Module anzeigen")
        print("3. Gewichteten Notenschnitt berechnen")
        print("4. Modul löschen")
        print("5. Beenden")
        return input("Wähle eine Option (1-5): ")

    @staticmethod
    def modul_abfragen():
        print("\n[ Neues Modul hinzufügen ]")
        name = input("Modulname: ").strip()
        
        while True:
            try:
                note = float(input("Note (z.B. 1.7): ").replace(',', '.'))
                if 1.0 <= note <= 5.0:
                    break
                print("Fehler: Die Note muss zwischen 1.0 und 5.0 liegen.")
            except ValueError:
                print("Fehler: Bitte eine gültige Zahl eingeben.")

        while True:
            try:
                ects = int(input("ECTS-Punkte (z.B. 5): "))
                if ects > 0:
                    break
                print("Fehler: ECTS müssen größer als 0 sein.")
            except ValueError:
                print("Fehler: Bitte eine ganze Zahl eingeben.")

        return name, note, ects

    @staticmethod
    def loesch_index_abfragen(anzahl_module: int) -> int:
        while True:
            try:
                eingabe = int(input(f"Welche Nummer möchtest du löschen? (1-{anzahl_module}): "))
                if 1 <= eingabe <= anzahl_module:
                    return eingabe - 1  # Umrechnung in 0-basierten Index für Python
                print(f"Fehler: Bitte eine Zahl zwischen 1 und {anzahl_module} wählen.")
            except ValueError:
                print("Fehler: Bitte eine gültige Nummer eingeben.")

    @staticmethod
    def zeige_module(module):
        if not module:
            print("\n[!] Keine Module eingetragen.")
            return False
        
        print("\n--- DEINE MODULE ---")
        for i, m in enumerate(module, 1):
            print(f"{i}. {m.name} | Note: {m.note:.1f} | ECTS: {m.ects}")
        return True

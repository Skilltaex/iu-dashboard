"""
View-Schicht (Präsentationsebene) für das IU-Dashboard.
Kapselt die gesamte Interaktion mit dem Benutzer über das Terminal (CLI).
Diese Klasse enthält keinerlei Berechnungs- oder Speicherlogik.
"""

from typing import Tuple

class NotenUI:
    """Repräsentiert die Benutzeroberfläche für die Notenverwaltung."""

    @staticmethod
    def menue_auswahl_abfragen() -> str:
        """
        Gibt das Hauptmenü auf der Konsole aus und fängt die Auswahl ab.
        
        Returns:
            str: Die vom Benutzer gewählte Option als Zeichenkette.
        """
        print("\n--- MENÜ ---")
        print("1. Modul hinzufügen")
        print("2. Alle Module anzeigen")
        print("3. Gewichteten Notenschnitt berechnen")
        print("4. Modul löschen")
        print("5. Beenden")
        return input("Wähle eine Option (1-5): ")

    @staticmethod
    def modul_abfragen() -> Tuple[str, float, int]:
        """
        Fragt die Modelldaten interaktiv ab und validiert die Eingaben robust.
        Erlaubt die Eingabe von Kommas bei Noten und fängt ungültige Werte ab.
        
        Returns:
            Tuple[str, float, int]: Ein Datensatz bestehend aus (Name, Note, ECTS).
        """
        print("\n[ Neues Modul hinzufügen ]")
        name = input("Modulname: ").strip()
        
        # Validierungsschleife für die Modulnote
        while True:
            try:
                # Ersetzt deutsche Kommas durch Punkte für die float-Konvertierung
                note = float(input("Note (z.B. 1.7): ").replace(',', '.'))
                if 1.0 <= note <= 5.0:
                    break
                print("Fehler: Die Note muss zwischen 1.0 und 5.0 liegen.")
            except ValueError:
                print("Fehler: Bitte eine gültige Zahl eingeben.")

        # Validierungsschleife für die ECTS-Punkte
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
        """
        Fragt ab, welcher Listeneintrag gelöscht werden soll.
        Rechnet die Anzeige (1-basiert) in den Python-Index (0-basiert) um.
        
        Args:
            anzahl_module (int): Die aktuelle Anzahl der Fächer in der Liste.
            
        Returns:
            int: Der validierte, 0-basierte Listenindex für den Controller.
        """
        while True:
            try:
                eingabe = int(input(f"Welche Nummer möchtest du löschen? (1-{anzahl_module}): "))
                if 1 <= eingabe <= anzahl_module:
                    return eingabe - 1  # Interne Index-Umrechnung für Python-Listen
                print(f"Fehler: Bitte eine Zahl zwischen 1 und {anzahl_module} wählen.")
            except ValueError:
                print("Fehler: Bitte eine gültige Nummer eingeben.")

    @staticmethod
    def zeige_module(module: list) -> bool:
        """
        Gibt alle aktuell gespeicherten Module strukturiert auf der Konsole aus.
        
        Args:
            module (list): Die Liste der Modul-Objekte aus dem Controller.
            
        Returns:
            bool: True, wenn Module vorhanden sind. False, wenn die Liste leer ist.
        """
        if not module:
            print("\n[!] Keine Module eingetragen.")
            return False
        
        print("\n--- DEINE MODULE ---")
        # Ausgabe mit fortlaufender Nummerierung über enumerate()
        for i, m in enumerate(module, 1):
            print(f"{i}. {m.name} | Note: {m.note:.1f} | ECTS: {m.ects}")
        return True
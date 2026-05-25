"""
Hauptprogramm (Einstiegspunkt / Application-Schicht) für das IU-Dashboard.
Verantwortlich für die Instanziierung der Kernkomponenten und die Steuerung
der zentralen Programmschleife.
"""

from controller.noten_controller import NotenController
from ui.cli import NotenUI

def main():
    """
    Zentrale Hauptfunktion. Steuert das Hauptmenü und koordiniert 
    die Interaktion zwischen der View (NotenUI) und dem Controller.
    """
    # Instanziierung des Controllers lädt automatisch bestehende Daten
    controller = NotenController()
    print("=== IU NOTENVERWALTUNG (MVC-Struktur) ===")

    # Endlosschleife für die interaktive Menüsteuerung (CLI)
    while True:
        auswahl = NotenUI.zeige_menue()

        # Option 1: Neues Studienmodul erfassen
        if auswahl == "1":
            name, note, ects = NotenUI.modul_abfragen()
            controller.modul_hinzufuegen(name, note, ects)
            print(f"✔ '{name}' erfolgreich hinzugefügt!")

        # Option 2: Alle erfassten Module tabellarisch auflisten
        elif auswahl == "2":
            NotenUI.zeige_module(controller.module)

        # Option 3: ECTS-gewichteten Notendurchschnitt berechnen
        elif auswahl == "3":
            schnitt = controller.berechne_gewichteten_schnitt()
            anzahl = len(controller.module)
            print(f"\n[ Notenschnitt ]")
            print(f"Module gesamt: {anzahl}")
            print(f"Gewichteter IU-Notenschnitt: {schnitt:.2f}")

        # Option 4: Ein bestehendes Modul aus der Datenbank löschen
        elif auswahl == "4":
            # Erst prüfen, ob Module existieren (View gibt True zurück, wenn Liste nicht leer)
            if NotenUI.zeige_module(controller.module):
                index = NotenUI.loesch_index_abfragen(len(controller.module))
                controller.modul_loeschen(index)

        # Option 5: Programm kontrolliert beenden
        elif auswahl == "5":
            print("\nProgramm beendet. Viel Erfolg beim Studium!")
            break
            
        # Fehlerbehandlung bei ungültigen Menü-Eingaben
        else:
            print("\n[-] Ungültige Auswahl. Bitte 1, 2, 3, 4 oder 5 wählen.")

# Sicherstellung, dass das Skript nur bei direktem Aufruf startet (Prinzp der Modularität)
if __name__ == "__main__":
    main()
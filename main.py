from controller.noten_controller import NotenController
from ui.cli import NotenUI

def main():
    controller = NotenController()
    print("=== IU NOTENVERWALTUNG (MVC-Struktur) ===")

    while True:
        auswahl = NotenUI.zeige_menue()

        if auswahl == "1":
            name, note, ects = NotenUI.modul_abfragen()
            controller.modul_hinzufuegen(name, note, ects)
            print(f"✔ '{name}' erfolgreich hinzugefügt!")

        elif auswahl == "2":
            NotenUI.zeige_module(controller.module)

        elif auswahl == "3":
            schnitt = controller.berechne_gewichteten_schnitt()
            anzahl = len(controller.module)
            print(f"\n[ Notenschnitt ]")
            print(f"Module gesamt: {anzahl}")
            print(f"Gewichteter IU-Notenschnitt: {schnitt:.2f}")

        elif auswahl == "4":
            # Erst Module anzeigen; wenn welche existieren, Löschung starten
            if NotenUI.zeige_module(controller.module):
                index = NotenUI.loesch_index_abfragen(len(controller.module))
                controller.modul_loeschen(index)

        elif auswahl == "5":
            print("\nProgramm beendet. Viel Erfolg beim Studium!")
            break
        else:
            print("\n[-] Ungültige Auswahl. Bitte 1, 2, 3, 4 oder 5 wählen.")

if __name__ == "__main__":
    main()
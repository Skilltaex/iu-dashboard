"""
Application-Schicht (Einstiegspunkt).

Instanziiert alle konkreten Klassen, verdrahtet sie über
Dependency Injection und startet die zentrale Menüschleife.
"""

from storage.json_storage import JsonStorage
from controller.noten_controller import NotenController
from ui.cli import NotenUI


class Application:
    """Zentrale Hauptklasse zur Instanziierung und Verdrahtung des Systems."""

    def __init__(self) -> None:
        """
        Erzeugt den konkreten Speicher und injiziert ihn
        in den Controller.
        """

        # Konkrete Speicher-Implementierung erzeugen
        storage_impl = JsonStorage()

        # Controller erzeugen und Speicher übergeben
        self.controller = NotenController(storage=storage_impl)

    def run(self) -> None:
        """
        Zentrale Programmschleife zur Koordination
        des Command Line Interfaces (CLI).
        """

        # Begrüßung beim Programmstart
        print("=== IU NOTENVERWALTUNG (Erweiterte MVC-Struktur) ===")

        # Programm läuft solange bis der Benutzer beendet
        while True:

            # Menü anzeigen und Auswahl abfragen
            auswahl = NotenUI.menue_auswahl_abfragen()

            # -----------------------------------------
            # Option 1: Modul hinzufügen
            # -----------------------------------------
            if auswahl == "1":

                # Eingaben vom Benutzer abfragen
                name, note, ects = NotenUI.modul_abfragen()

                # Modul hinzufügen
                self.controller.modul_hinzufuegen(name, note, ects)

                print(f"✔ '{name}' erfolgreich hinzugefügt!")

            # -----------------------------------------
            # Option 2: Module anzeigen
            # -----------------------------------------
            elif auswahl == "2":

                NotenUI.zeige_module(
                    self.controller.get_module()
                )

            # -----------------------------------------
            # Option 3: Notenschnitt berechnen
            # -----------------------------------------
            elif auswahl == "3":

                schnitt = self.controller.berechne_gewichteten_schnitt()
                anzahl = len(self.controller.get_module())

                print("\n[ Notenschnitt ]")
                print(f"Module gesamt: {anzahl}")
                print(f"Gewichteter IU-Notenschnitt: {schnitt:.2f}")

            # -----------------------------------------
            # Option 4: Modul löschen
            # -----------------------------------------
            elif auswahl == "4":

                if NotenUI.zeige_module(self.controller.get_module()):

                    index = NotenUI.loesch_index_abfragen(
                        len(self.controller.get_module())
                    )

                    self.controller.modul_loeschen(index)

            # -----------------------------------------
            # Option 5: Programm beenden
            # -----------------------------------------
            elif auswahl == "5":

                print("\nProgramm beendet. Viel Erfolg beim Studium!")
                break

            # -----------------------------------------
            # Ungültige Eingabe
            # -----------------------------------------
            else:

                print("\n[-] Ungültige Auswahl. Bitte 1, 2, 3, 4 oder 5 wählen.")


# Startpunkt der Anwendung
if __name__ == "__main__":
    app = Application()
    app.run()
"""
Abstrakte Repository-Schnittstelle (Interface) für die Datenspeicherung.
Stellt sicher, dass der Controller unabhängig von der konkreten Speicherlogik bleibt.
"""

from abc import ABC, abstractmethod

class BaseStorage(ABC):
    """Abstrakte Basisklasse (Interface) für die Persistenzschicht."""

    @abstractmethod
    def speichern(self, module: list) -> None:
        """Speichert die übergebene Liste von Modulen."""
        pass

    @abstractmethod
    def laden(self) -> list:
        """Lädt alle gespeicherten Module und gibt sie als Liste zurück."""
        pass
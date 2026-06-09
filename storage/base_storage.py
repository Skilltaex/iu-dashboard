"""
Abstrakte Repository-Schnittstelle (Interface) für die Datenspeicherung.
Stellt sicher, dass der Controller unabhängig von der konkreten Speicherlogik bleibt.
"""

from abc import ABC, abstractmethod
from models.studiengang import Studiengang

class BaseStorage(ABC):
    """Abstrakte Basisklasse (Interface) für die Persistenzschicht."""

    @abstractmethod
    def speichern(self, studiengang: Studiengang) -> None:
        """Speichert die Aggregatwurzel des Studiengangs."""
        pass

    @abstractmethod
    def laden(self) -> Studiengang:
        """Lädt die Aggregatwurzel und gibt das rekonstruierte Objekt zurück."""
        pass
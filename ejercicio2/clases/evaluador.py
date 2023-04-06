from abc import ABC, abstractmethod
from clases.solicitudPrestamo import SolicitudPrestamo

class Evaluador(ABC):

    @abstractmethod
    def EsValida(self, solicitud: SolicitudPrestamo) -> bool:
        pass

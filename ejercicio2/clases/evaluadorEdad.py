from clases.evaluador import Evaluador
from clases.solicitudPrestamo import SolicitudPrestamo
import time

class EvaluadorEdad(Evaluador):

    def __init__(self, edadMinima: int, edadMaxima: int) -> None:
        self.__EdadMinima = edadMinima
        self.__EdadMaxima = edadMaxima

    def EsValida(self, solicitud: SolicitudPrestamo) -> bool:
        if(self.__EdadMinima <= solicitud.Cliente.Edad) & (self.__EdadMaxima >= solicitud.Cliente.Edad):
            return True
        else:
            print(f'la Edad para pedir el prestamo debe esta comprendida entre {self.__EdadMinima} y {self.__EdadMaxima}, la suya es de: {solicitud.Cliente.Edad}')
            time.sleep(3)
            return False

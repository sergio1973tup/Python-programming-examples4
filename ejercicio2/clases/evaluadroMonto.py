from clases.evaluador import Evaluador
from clases.solicitudPrestamo import SolicitudPrestamo
import time

class EvaluadorMonto(Evaluador):

    def __init__(self, montoMaximo: float) -> None:
        self.__MontoMaximo = montoMaximo

    def EsValida(self, solicitud: SolicitudPrestamo) -> bool:
        if(self.__MontoMaximo >= solicitud.Monto):
            return True
        else:
            print(f'el monto maximo que puede pedir es de: {self.__MontoMaximo}, usted pidio: {solicitud.Monto}')
            time.sleep(3)
            return False
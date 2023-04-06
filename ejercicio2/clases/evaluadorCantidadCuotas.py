from clases.evaluador import Evaluador
from clases.solicitudPrestamo import SolicitudPrestamo
import time

class EvaluadorCantidadCuotas(Evaluador):

    def __init__(self, cantidadCuotas: int) -> None:
        self.__CantidadCuotas = cantidadCuotas

    def EsValida(self, solicitud: SolicitudPrestamo) -> bool:
        if(self.__CantidadCuotas >= solicitud.CantidadCuotas):
            return True
        else:
            print(f'usted solo puede pedir: {self.__CantidadCuotas} cuotas y pidio: {solicitud.CantidadCuotas} cuotas')
            time.sleep(3)
            return False
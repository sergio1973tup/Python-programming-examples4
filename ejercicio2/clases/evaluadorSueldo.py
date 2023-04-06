from clases.evaluador import Evaluador
from clases.solicitudPrestamo import SolicitudPrestamo
import time

class EvaluadorSueldo(Evaluador):

    def __init__(self, sueldo: float) -> None:
        self.__Sueldo = sueldo

    def EsValida(self, solicitud: SolicitudPrestamo) -> bool:
        if(self.__Sueldo <= solicitud.Cliente.Empleo.Sueldo):
            return True
        else:
            print(f'el sueldo minimo es de: {self.__Sueldo}, el suyo es de: {solicitud.Cliente.Empleo.Sueldo}')
            time.sleep(3)
            return False
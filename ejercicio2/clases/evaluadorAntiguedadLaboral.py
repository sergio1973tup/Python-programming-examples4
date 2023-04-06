from clases.evaluador import Evaluador
from clases.solicitudPrestamo import SolicitudPrestamo
import time

class EvaluadroAntiguedadLaboral(Evaluador):
    __AntiguedadMinima: int 

    def __init__(self, antiguedadMinima: int) -> None:
        self.__AntiguedadMinima = antiguedadMinima

    def EsValida(self, solicitud: SolicitudPrestamo) -> bool:
        if(self.__AntiguedadMinima <= solicitud.Cliente.Empleo.Antiguedad):
            return True
        else:
            print(f'su antiguedad: {solicitud.Cliente.Empleo.Antiguedad} mes es menos a la requerida: {self.__AntiguedadMinima} meses')
            time.sleep(3)
            return False
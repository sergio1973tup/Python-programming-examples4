from clases.evaluador import Evaluador
from clases.solicitudPrestamo import SolicitudPrestamo

class EvaluadorCompuesto(Evaluador):
    __evaluadores = []

    def __init__(self) -> None:
        super().__init__()

    def EsValida(self, solicitud: SolicitudPrestamo) -> bool:
        ok = True
        for i in self.__evaluadores:
            if(i.EsValida(solicitud) == False):
                ok = False

        return ok
    
    def AgregarEvaluador(self, evaluador: Evaluador) -> None:
        self.__evaluadores.append(evaluador)

    def CantidadEvaluadores(self) -> list:
        return self.__evaluadores
    
    def RESTAR(self) -> None:
        self.__evaluadores.pop(4)
        self.__evaluadores.pop(3)
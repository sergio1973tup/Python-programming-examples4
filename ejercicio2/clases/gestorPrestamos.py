from clases.solicitudPrestamo import SolicitudPrestamo
from clases.evaluador import Evaluador
from clases.evaluadorCompuesto import EvaluadorCompuesto
from clases.evaluadorAntiguedadLaboral import EvaluadroAntiguedadLaboral
from clases.evaluadorEdad import EvaluadorEdad
from clases.evaluadorSueldo import EvaluadorSueldo
from clases.evaluadorCantidadCuotas import EvaluadorCantidadCuotas
from clases.evaluadroMonto import EvaluadorMonto

class GestorPrestamos(Evaluador):
    __evaluadorPorCliente = {1:[20000,12],2:[100000,32],3:[150000,60],4:[200000,60]}
    __evaluadorCompuesto = EvaluadorCompuesto()
    __evaluadorCompuesto.AgregarEvaluador(EvaluadroAntiguedadLaboral(6)) 
    __evaluadorCompuesto.AgregarEvaluador(EvaluadorEdad(18,75))
    __evaluadorCompuesto.AgregarEvaluador(EvaluadorSueldo(5000))

    def __init__(self) -> None:
        pass

    def EsValida(self, solicitud: SolicitudPrestamo) -> bool:
        if(len(self.__evaluadorCompuesto.CantidadEvaluadores())== 5):
            self.__evaluadorCompuesto.RESTAR()
                    
        for k,v in self.__evaluadorPorCliente.items():
            if(k == solicitud.Cliente.TipoCliente):
                self.__evaluadorCompuesto.AgregarEvaluador(EvaluadorMonto(v[0]))
                self.__evaluadorCompuesto.AgregarEvaluador(EvaluadorCantidadCuotas(v[1]))

        return self.__evaluadorCompuesto.EsValida(solicitud)
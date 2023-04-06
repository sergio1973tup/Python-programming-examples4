
from clases.cliente import Cliente

class SolicitudPrestamo:

    def __init__(self,cliente: Cliente, monto: float, cantidadCuotas: int) -> None:
        self.__monto = monto
        self.__cantidadCuotas = cantidadCuotas 
        self.__cliente = cliente

    @property
    def Monto(self) -> float:
        return self.__monto

    @property 
    def CantidadCuotas(self) -> int:
        return self.__cantidadCuotas

    @property
    def Cliente(self) -> Cliente:
        return self.__cliente
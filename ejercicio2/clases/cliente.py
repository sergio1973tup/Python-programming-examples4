
from enum import Enum
from clases.empleo import Empleo
from clases.tipoCliente import TipoCliente
from datetime import date, datetime


class Cliente:

    def __init__(self, nombre: str, apellido: str, fechaDeNacimiento: datetime, empleo: Empleo) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaDeNacimiento = fechaDeNacimiento
        self.__empleo = empleo
        self.__tipoCliente = TipoCliente.NoCliente.value

    @property
    def Nombre (self) -> str:
        return self.__nombre

    @property
    def Apellido(self) -> str:
        return self.__apellido

    @property
    def FechaDeNacimiento(self) -> datetime:
        return self.__fechaDeNacimiento

    @property
    def Empleo(self) -> Empleo:
        return self.__empleo

    @property
    def TipoCliente(self) -> TipoCliente:
        return self.__tipoCliente

    @TipoCliente.setter
    def TipoCliente(self, value: int) -> None:
        self.__tipoCliente = value

    @property
    def Edad(self) -> int:
        hoy = datetime.now().date()
        fecha = self.__fechaDeNacimiento.date()
        edad = hoy - fecha

        return int(edad.days/365)
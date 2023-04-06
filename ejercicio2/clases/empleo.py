
from datetime import date,datetime

class Empleo:
    __sueldo: float
    __fechaIngreso: date

    def __init__(self, sueldo: float, fechaIngreso: date) -> None:
        self.__sueldo = sueldo
        self.__fechaIngreso = fechaIngreso

    @property
    def Sueldo(self) -> float:
        return self.__sueldo

    @property
    def FechaINgreso(self) -> date:
        return self.__fechaIngreso

    @property
    def Antiguedad(self) -> int:
        hoy = datetime.now().date()
        fecha = self.__fechaIngreso
        antiguedad = hoy - fecha

        return int((antiguedad.days/365)*12)
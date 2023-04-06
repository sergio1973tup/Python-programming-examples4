from datetime import date,datetime,timedelta
from os import system
import time
from clases.cliente import Cliente
from clases.empleo import Empleo
from clases.solicitudPrestamo import SolicitudPrestamo
from clases.gestorPrestamos import GestorPrestamos

class Controlador:
    __nuevoCliente: Cliente

    def NuevoCliente(self) -> None:
        system('cls')
        nombre = input('Ingrese en nombre del Cliente: ')
        apellido = input('Ingrese el aplellido del cliente: ')
        fecha = datetime.strptime(input('ingrese fecha de nacimiento (dd-mm-aaaa): '), "%d-%m-%Y")
        
        self.__nuevoCliente = Cliente(nombre,apellido,fecha,self.NuevoEmpleo())
    

    def NuevoEmpleo(self) -> Empleo:
        sueldo = float(input('Ingrese el sueldo del cliente: '))
        fecha = datetime.strptime(input('ingrese fecha de ingreso al empleo acutal (dd-mm-aaaa): '), "%d-%m-%Y").date()

        return Empleo(sueldo,fecha)

    def TipoCliente(self, tipoCliente: int) -> None:
        self.__nuevoCliente.TipoCliente = tipoCliente

    def SolicitudPrestamos(self) -> SolicitudPrestamo:
        system('cls')
        monto = float(input('Ingrese en la suma que desea pedir: '))
        cuotas = int(input('ingrese la cantidad de cuotas: '))
        self.MostrarCLiente(monto, cuotas)

        return SolicitudPrestamo(self.__nuevoCliente,monto,cuotas)

    def GestorDePrestamos(self) -> str:
        gestor = GestorPrestamos()
        
        if(gestor.EsValida(self.SolicitudPrestamos())):
            system('cls')
            return 'ACEPTADO'
        else:
            system('cls')
            return 'RECHAZADO'

    def MostrarCLiente(self, monto: float, cuotas: int) -> None:
        system('cls')
        print(f'el cliente: {self.__nuevoCliente.Nombre} {self.__nuevoCliente.Apellido}, edad: {self.__nuevoCliente.Edad}')
        print(f'es de tipo: {self.__nuevoCliente.TipoCliente}, quiere pedir: {monto} $, en: {cuotas} cuotas ')
        print(f'tiene {self.__nuevoCliente.Empleo.Antiguedad} meses de antiguedad, y un sueldo: {self.__nuevoCliente.Empleo.Sueldo}')
        time.sleep(5)
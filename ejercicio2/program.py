from os import system
import sys
import time 

from controlador import Controlador
sys.path.append('..')
from Menu.MenuDeSeleccion import MenuDeSeleccion

class Program:
    opciones = ['1-CARGAR CLIENTE','2-SELECCIONAR TIPO CLIENTE','3-SOLICITAR PRESTAMO','4-SALIR']
    tipoClienteOpciones = ['1-NO CLIENTE','2-CLIENTE','3-CLIENTE GOLD','4-CLIENTE PREMIUM','5-SALIR']
    menuPrincipal = MenuDeSeleccion('Menu Principal',opciones)
    menuCliente = MenuDeSeleccion('Tipo Clinete',tipoClienteOpciones)
    controlador = Controlador()
    seleccion = ''

    while(seleccion != str(len(opciones))):
        seleccion = menuPrincipal.seleccion()

        if(seleccion == '1'):
            controlador.NuevoCliente()
        if(seleccion == '2'):
            clienteTipo = 0
            clienteTipo = int(menuCliente.seleccion())
            if(clienteTipo < 5) & (clienteTipo > 0):
                controlador.TipoCliente(clienteTipo)
        if(seleccion == '3'):
            print(f'Su Prestamos fue: {controlador.GestorDePrestamos()}')
            time.sleep(3)
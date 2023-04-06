
from os import system
import sys
import time 
from os import system
from controlador import Controlador
sys.path.append('..')
from Menu.MenuDeSeleccion import MenuDeSeleccion


class Program:
    controlador = Controlador()
    opciones = ['1-SELECCIONAR ENCRIPTADOR','2-SALIR']
    menuPrincipal = MenuDeSeleccion('Menu Principal',opciones)
    seleccion = ''
    operaciones = ['1-ENCRIPTAR','2-DESENCRIPTAR','3-SALIR']
    menuEncriptador = MenuDeSeleccion('Seleccione la operacion', operaciones)

    while(seleccion != str(len(opciones))):
        seleccion = menuPrincipal.seleccion()
        operacion = ''

        if(seleccion == '1'):
            system('cls')
            controlador.SeleccionarEncriptador(input('ingrese en nombre del encriptador: '))
            

            while(operacion != str(len(operaciones))):
                operacion = menuEncriptador.seleccion()
                if(operacion == '1'):
                    system('cls')
                    controlador.CargarPalabra(input('Ingrese la palabra: '))
                    system('cls')
                    print(f'La palagra: {controlador.Palabra()}  encriptada quedo asi: {controlador.Encriptar()}')
                    time.sleep(5)
                elif(operacion == '2'):
                    system('cls')
                    print(f'La palabra original era: {controlador.Desencriptar()}')
                    time.sleep(5) 
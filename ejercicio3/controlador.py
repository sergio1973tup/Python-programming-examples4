import string
import time
from clases.fabricaDeEncriptadores import FabricaDeEncriptadores
from clases.encriptador import Encriptador

class Controlador:
    __fabrica = FabricaDeEncriptadores()
    __palabra: str
    __encriptada: str
    __encriptador: Encriptador

    def SeleccionarEncriptador(self, encriptador: string) -> None:
        # if(encriptador == 'AES'):
        #     self.__encriptador = self.__fabrica.GetEncriptador(encriptador)
        #     self.Resetear()
        # elif(encriptador == 'Cesar'):
        #     self.__encriptador = self.__fabrica.GetEncriptador(encriptador)
        #     self.Resetear()
        # else:
        #     self.__encriptador = self.__fabrica.GetEncriptador('Nulo')
        #     self.Resetear()
        self.__encriptador = self.__fabrica.GetEncriptador(encriptador)
        self.Resetear()

    def CargarPalabra(self, cadena: string) -> None:
        self.__palabra = cadena

    def Encriptar(self) -> string:
        self.__encriptada = self.__encriptador.Encriptar(self.__palabra)
        
        return self.__encriptada

    def Desencriptar(self) -> string:
        if(self.__encriptada == ''):
            return 'NO HAY PALABRA PARA DESENCRIPTAR'
        else:
            return self.__encriptador.Desencriptar(self.__encriptada)

    def Palabra(self) -> string:
        return self.__palabra

    def Resetear(self) -> None:
        self.__palabra = ''
        self.__encriptada = ''
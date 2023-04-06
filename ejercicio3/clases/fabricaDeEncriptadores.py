from ast import Break
import string
import time
from clases.encriptador import Encriptador
from clases.encriptadorNulo import EncriptadorNulo
from clases.encriptadroAES import EncriptadroAES
from clases.encriptadroCesar import EncriptadorCesar

class FabricaDeEncriptadores:
    __encriptadores = {'AES':EncriptadroAES(),'Cesar':EncriptadorCesar(3),'Nulo':EncriptadorNulo()}
    __instancia = None 

    def __new__(cls):
        if(cls.__instancia is None):
            cls.__instancia = object.__new__(cls)

        return cls.__instancia

    def GetEncriptador(self, nombre: string) -> Encriptador:
        for k,v in self.__encriptadores.items():
            if(nombre == k):
                return self.__encriptadores[nombre]
        
        return EncriptadorNulo()

        

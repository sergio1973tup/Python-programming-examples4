

from abc import ABC
import string


class Encriptador(ABC):

    def __init__(self, nombre: string) -> None:
        self.__nombre = nombre

    @property
    def Nombre(self) -> string:
        return self.__nombre

    def Encriptar(self,cadena: string) -> string:
        pass

    def Desencriptar(self, cadena: string) -> string:
        pass
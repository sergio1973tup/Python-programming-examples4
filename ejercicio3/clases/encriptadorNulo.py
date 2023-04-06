import string

from clases.encriptador import Encriptador

class EncriptadorNulo(Encriptador):

    def __init__(self) -> None:
        super().__init__('NULL')

    def Encriptar(self, cadena: string) -> string:
        return f'Encriptador NULO palabra ingresada: {cadena}'
    
    def Desencriptar(self, cadena: string) -> string:
        return f'Encriptador NULO palabra ingresada: {cadena}'        
import string
from clases.encriptador import Encriptador

class EncriptadorCesar(Encriptador):
    __desplzamiento: int
    __abc = 'abcdefghijkmnñopqrstuvwxyzABCDEFGHIJKMNÑOPQRSTUVWXYZabcdefghijkmnñopqrstuvwxyzABCDEFGHIJKMNÑOPQRSTUVWXYZ'

    def __init__(self, desplazamiento: int) -> None:
        super().__init__('Cesar')
        self.__desplzamiento = desplazamiento

    def Encriptar(self, cadena: string) -> string:
        encriptado = ''
        for letra in cadena:
            posicion = self.__abc.find(letra)

            if(posicion == -1):
                encriptado += letra
            else:
                posicionFinal = posicion+self.__desplzamiento
                nuevaLetra = self.__abc[posicionFinal]
                encriptado += nuevaLetra

        return encriptado

    def Desencriptar(self, cadena: string) -> string:
        desencriptado = ''
        for letra in cadena:
            posicion = self.__abc.find(letra)

            if(posicion == -1):
                desencriptado += letra
            else:
                posicionFinal = posicion-self.__desplzamiento
                nuevaLetra = self.__abc[posicionFinal]
                desencriptado += nuevaLetra

        return desencriptado
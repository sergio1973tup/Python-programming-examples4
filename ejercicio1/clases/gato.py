import string
from clases.animal import Animal


class Gato(Animal):
    __nombre = str

    def __init__(self,nombre: str) -> None:
        super().__init__()
        self.__nombre = nombre

    def HacerRuido(self):
        return "MIAU!!"
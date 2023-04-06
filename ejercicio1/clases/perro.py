import string
from clases.animal import Animal


class Perro(Animal):
    __nombre: str

    def __init__(self,nombre: string) -> None:
        super().__init__()
        self.__nombre = nombre

    def HacerRuido(self):
        return "GUAW!!"
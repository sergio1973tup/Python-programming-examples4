import string
from clases.animal import Animal


class Veterianria:
    __animales = list()

    def __init__(self) -> None:
        pass

    def AceptarAnimales(self, animal: Animal) -> None:
        self.__animales.append(animal)
        for i in self.__animales:
            print(i.HacerRuido())
        
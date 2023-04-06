from abc import ABC, abstractmethod
import string

class Animal(ABC):

    def __init__(self) -> None:
        pass

    def Correr(self) -> string:
        return 'corriendo'

    def Saltar(self) -> string:
        return 'saltando'
        
    @abstractmethod
    def HacerRuido(self):
        pass

from clases.veterinaria import Veterianria
from clases.perro import Perro
from clases.gato import Gato


def main():
    miVeterinaria = Veterianria()
    Burca = Perro("Burca")
    Michi = Gato("Sylvestre")
    
    miVeterinaria.AceptarAnimales(Burca)
    miVeterinaria.AceptarAnimales(Michi)


if __name__ == '__main__':
    main()
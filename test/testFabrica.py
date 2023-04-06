import unittest
import sys
sys.path.append('..')
from ejercicio3.clases.fabricaDeEncriptadores import FabricaDeEncriptadores

class fabricaTestCase(unittest.TestCase):

    def test_fabrica(self):
        fabrica = FabricaDeEncriptadores()
        encriptador = fabrica.GetEncriptador('Cesar')
        self.assertEqual(encriptador.Nombre,'AES') 

if __name__ == '__main__':
    unittest.main()
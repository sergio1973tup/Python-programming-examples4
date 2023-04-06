import string
from os import system
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from clases.encriptador import Encriptador

class EncriptadroAES(Encriptador):
    __password = 'paswordDeEncriptacion'
    __BLOCK_SIZE = 16
    __PAD = '{'
    __hkey: any

    def __init__(self) -> None:
        super().__init__('AES')

    # def Password(self) -> None:
    #     self.__password = input('ingrese el password para encriptar: ')
    #     system('cls')

    def Encriptar(self, cadena: string) -> string:
        # self.Password()

        hash_obj = SHA256.new(self.__password.encode('utf-8'))
        self.__hkey = hash_obj.digest()

        
        padding = lambda a: a + (self.__BLOCK_SIZE - len(a) % self.__BLOCK_SIZE) * self.__PAD

        cipher = AES.new(self.__hkey, AES.MODE_ECB)

        return cipher.encrypt(padding(cadena).encode('utf-8'))

    def Desencriptar(self, cadena: string) -> string:
        decipher = AES.new(self.__hkey, AES.MODE_ECB)
        pt = decipher.decrypt(cadena)

        data = pt.decode('utf-8')


        pad_index = data.find(self.__PAD)
        return data[:pad_index]
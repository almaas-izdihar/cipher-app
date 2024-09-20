from abc import ABC

class CipherBase(ABC):       
     
    def encrypt(self, plaintext, key):
        pass

    def decrypt(self, ciphertext, key):
        pass
import numpy as np
from .base_class import CipherBase

class Hill(CipherBase):

    def _create_key_matrix(self, key):
        key = key.upper().replace(" ", "")
        size = int(len(key) ** 0.5)
        key_matrix = np.array([ord(c) - ord('A') for c in key]).reshape(size, size)
        return key_matrix

    def _process(self, text, key_matrix, mode='encrypt'):
        size = key_matrix.shape[0]
        text = text.upper().replace(" ", "")
        text_vector = [ord(c) - ord('A') for c in text]

        while len(text_vector) % size != 0:
            text_vector.append(ord('X') - ord('A'))

        text_matrix = np.array(text_vector).reshape(-1, size)

        if mode == 'decrypt':
            key_matrix = np.linalg.inv(key_matrix).astype(int) % 26

        result_matrix = (text_matrix @ key_matrix) % 26
        result_text = ''.join([chr(num + ord('A')) for num in result_matrix.flatten()])

        return result_text

    def encrypt(self, plaintext, key):
        key_matrix = self._create_key_matrix(key)
        return self._process(plaintext, key_matrix, 'encrypt')

    def decrypt(self, ciphertext, key):
        key_matrix = self._create_key_matrix(key)
        return self._process(ciphertext, key_matrix, 'decrypt')

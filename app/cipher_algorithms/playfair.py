from .base_class import CipherBase

class Playfair(CipherBase):

    def _create_matrix(self, key):
        key = "".join(sorted(set(key), key=key.index))  # Remove duplicates
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J digabungkan dengan I
        key += ''.join([char for char in alphabet if char not in key])
        return [list(key[i:i + 5]) for i in range(0, 25, 5)]

    def _find_position(self, char, matrix):
        for r, row in enumerate(matrix):
            if char in row:
                return r, row.index(char)

    def _process_pair(self, char1, char2, matrix, mode):
        row1, col1 = self._find_position(char1, matrix)
        row2, col2 = self._find_position(char2, matrix)

        if row1 == row2:
            col1 = (col1 + (1 if mode == 'encrypt' else -1)) % 5
            col2 = (col2 + (1 if mode == 'encrypt' else -1)) % 5
        elif col1 == col2:
            row1 = (row1 + (1 if mode == 'encrypt' else -1)) % 5
            row2 = (row2 + (1 if mode == 'encrypt' else -1)) % 5
        else:
            col1, col2 = col2, col1

        return matrix[row1][col1] + matrix[row2][col2]

    def encrypt(self, plaintext, key):
        key = key.upper().replace('J', 'I')
        matrix = self._create_matrix(key)

        plaintext = plaintext.upper().replace('J', 'I').replace(" ", "")
        if len(plaintext) % 2 != 0:
            plaintext += 'X'

        encrypted_text = ""
        for i in range(0, len(plaintext), 2):
            encrypted_text += self._process_pair(plaintext[i], plaintext[i+1], matrix, 'encrypt')

        return encrypted_text

    def decrypt(self, ciphertext, key):
        key = key.upper().replace('J', 'I')
        matrix = self._create_matrix(key)

        ciphertext = ciphertext.upper().replace('J', 'I').replace(" ", "")
        decrypted_text = ""
        for i in range(0, len(ciphertext), 2):
            decrypted_text += self._process_pair(ciphertext[i], ciphertext[i+1], matrix, 'decrypt')

        return decrypted_text

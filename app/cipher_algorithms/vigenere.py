from .base_class import CipherBase

class Vigenere(CipherBase):

    def _format_text(self, text):
        return text.upper().replace(" ", "")

    def _extend_key(self, plaintext, key):
        key = key.upper().replace(" ", "")
        return (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]

    def encrypt(self, plaintext, key):
        plaintext = self._format_text(plaintext)
        key = self._extend_key(plaintext, key)

        encrypted_text = []
        for p, k in zip(plaintext, key):
            encrypted_char = (ord(p) - ord('A') + (ord(k) - ord('A'))) % 26 + ord('A')
            encrypted_text.append(chr(encrypted_char))

        return ''.join(encrypted_text)

    def decrypt(self, ciphertext, key):
        ciphertext = self._format_text(ciphertext)
        key = self._extend_key(ciphertext, key)

        decrypted_text = []
        for c, k in zip(ciphertext, key):
            decrypted_char = (ord(c) - ord('A') - (ord(k) - ord('A')) + 26) % 26 + ord('A')
            decrypted_text.append(chr(decrypted_char))

        return ''.join(decrypted_text)


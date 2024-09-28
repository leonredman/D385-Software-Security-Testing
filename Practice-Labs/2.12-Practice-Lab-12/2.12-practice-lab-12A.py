import hashlib
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        counter = self.block_size.to_bytes(self.block_size, "big")
        cipher = AES.new(self.key, AES.MODE_CTR, counter=lambda: counter)
        encrypted_text = cipher.encrypt(plain_text)
        return b64encode(counter + encrypted_text).decode("utf-8")

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

if __name__ == '__main__':

    msg = input("Enter message: ")
    cipher = AESCipher(msg)
    #Test the message size
    msg = msg*10
    
    print(cipher.encrypt(msg))
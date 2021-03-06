from __future__ import print_function
import random
import string
import base64

import sys

punctuation = list(string.punctuation)
alphabet = list(string.ascii_letters)
chars = alphabet + punctuation


def gen_key(array):
    length = random.randint(4, 7)
    master_key = random.sample(array, length)
    key_str = ''.join(map(str, master_key))
    return key_str.encode("hex")


def encrypt(key_text, password_clear):
    password_b64 = base64.b64encode(password_clear)
    master_password = key_text + "@" + password_b64
    return base64.b64encode(master_password)


def decrypt(cipher_password):
    not_b64 = base64.b64decode(cipher_password)
    key_encode, pass_encode = not_b64.split('@')
    password_clear_text = base64.b64decode(pass_encode)
    return password_clear_text


if __name__ == '__main__':
    if len(sys.argv) > 1:
        method = sys.argv[1]
    else:
        print("Usage: cipher.py [de]")
        print("e encrypt plain text")
        print("d decrypt cipher text")
        print("Example: cipher.py d")
        exit(-1)

    if method == 'd':
        cipher_text = raw_input('Enter cipher text: ')
        print("decypted: %s " % decrypt(cipher_text))
    elif method == 'e':
        key = gen_key(chars)
        password = raw_input("Enter text: ")
        cipher_text = encrypt(key, password)
        print("encrypted key: %s " % cipher_text)
    else:
        print("Invalid Option")

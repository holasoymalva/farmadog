from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt(data):
    key = 'MbQeThWmZq4t6w9z$C&F)J@NcRfUjXn2'
    cipher = AES.new(key.encode("utf8"), AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf8"))
    obj = {
        'key': key,
        'nonce': cipher.nonce,
        'tag': tag,
        'ciphertext': ciphertext
    }

    return obj

    # ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf8"))
    # return key, cipher.nonce, tag, ciphertext

# def decrypt(key, nonce, tag, ciphertext):
#     # obj = AES.new(key.encode("utf8"), AES.MODE_CBC, data.encode("utf8"))
#     cipher = AES.new(key.encode("utf8"), AES.MODE_EAX, nonce=nonce)
#     data = cipher.decrypt_and_verify(ciphertext, tag)
#     return data


# Path: api/utils/hash.py
#!/usr/bin/python3
# Val cipher by valvate
# Use generate.py to generate a key for yourself then replace the following:

alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890= '
key =      'F7dJ89aph5r40Rw6yUAzoqm897Ht0CBviWSD5Esbg2M2VQXGxcOlT6fjPnkuL4e1Y1IZ33KN= '

# Base64 encoder #
from base64 import b64decode, b64encode 

def hexencode(data):
    data = data.encode('utf-8')
    encrypted = b64encode(data)
    encrypted = encrypted.decode('utf-8')
    return encrypted

def hexdecode(data):
    # Python hates lowercase in base64
    data = data.upper()
    data = data.encode('utf-8')
    decrypted = b64decode(data)
    decrypted = decrypted.decode('utf-8')
    return decrypted

# Mono cipher #
def encrypt(data):
    # Encodes data into base64
    data = hexencode(data)
    indexVals = [alphabet.index(char.lower()) for char in data]
    return ''.join(key[indexKey] for indexKey in indexVals)

def decrypt(data):
    # Decodeds base64 data
    indexVals = [key.index(char) for char in data]
    deciphered = ''.join(alphabet[indexKey] for indexKey in indexVals)
    print(deciphered)
    deciphered = hexdecode(deciphered)
    return deciphered

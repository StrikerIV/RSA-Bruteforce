#   a212_rsa_decrypt.py
import rsa

import rsa as rsa
import re

global solved

solved = False
decrypted = ""

key = 7457
mod_value = 29737
encrypted = "8953, 7694, 28157, 20352, 9263, 21610, 25958, 13318, 13318, 20352, 13801, 9417, 24955, 1292, 21610, 9263, 20352, 20193, 28157, 20352, 22703, 25958, 24768, 9417"
encrypted = encrypted.split(", ")

decrypted = rsa.decrypt(key, mod_value, encrypted)
print(decrypted)


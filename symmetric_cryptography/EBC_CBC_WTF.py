import requests
from pwn import *

url = 'https://aes.cryptohack.org/ecbcbcwtf/'

def encrypt_flag():
	r = requests.get(url + 'encrypt_flag/')
	js = r.json()
	return bytes.fromhex(js['ciphertext'])

def decrypt(cipher):
    loc_url = url + 'decrypt/'
    loc_url += cipher.hex()
    loc_url += '/'
    r = requests.get(loc_url)
    js = r.json()
    return bytes.fromhex(js['plaintext'])
	
ciphertext = encrypt_flag()
flag = b''

for i in range(16, len(ciphertext), 16):
    flag += xor(ciphertext[i-16 : i], decrypt(ciphertext[i : i+16]))
print(flag)
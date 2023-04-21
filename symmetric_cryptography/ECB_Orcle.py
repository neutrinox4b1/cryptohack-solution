# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad

# def div_print(str, l=32):
#     for i in range(0, len(str), l):
#         print(str[i : i+l])
#     print()

# flag len = 25byte
import requests
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

flag = b'crypto{'

def response(plaintext):
    url = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'
    url += plaintext.hex()
    url += '/'
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js['ciphertext'])	

for i in range(7, 26):
    plaintext = b'\x41' * (31 - i)
    target = response(plaintext)[:32]
    plaintext += flag
    for j in range(33, 127):
        plaintext = plaintext[:31]
        plaintext += j.to_bytes(1, byteorder='big')
        print(j)
        
        bullet = response(plaintext)[:32]
        if (bullet == target):
            flag += j.to_bytes(1, byteorder='big')
            print(flag)
            break
import requests
from pwn import *

url = 'https://aes.cryptohack.org/flipping_cookie/'

def check_admin(cookie, iv):
    furl = url + f'check_admin/{cookie}/{iv}/'
    r = requests.get(furl)
    js = r.json()
    try :
        print(js['flag'])
    except:
        print(js['error'])
    

def get_cookie():
    furl = url + 'get_cookie/'
    r = requests.get(furl)
    js = r.json()
    return bytes.fromhex(js['cookie'])

cookie = get_cookie()
iv = cookie[: 16]
ciphertext = cookie[16 :]
plain16 = b'admin=False;expi'
shot = b'admin=True;;;;;;'

payload = xor(xor(iv, plain16), shot)

check_admin(ciphertext.hex(), payload.hex())
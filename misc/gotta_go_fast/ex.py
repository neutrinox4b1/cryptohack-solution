import time
from Crypto.Util.number import long_to_bytes
import hashlib
from pwn import *
import json

def generate_key():
    current_time = int(time.time())
    key = long_to_bytes(current_time)
    return hashlib.sha256(key).digest()


def encrypt(b):
    key = generate_key()
    assert len(b) <= len(key), "Data package too large to encrypt"
    ciphertext = b''
    for i in range(len(b)):
        ciphertext += bytes([b[i] ^ key[i]])
    return ciphertext.hex()

p = remote('socket.cryptohack.org', 13372)

p.recvuntil(b'!\n')
payload = b'{"option":"get_flag"}'
p.sendline(payload)
get_flag = json.loads(p.recvline())['encrypted_flag']

payload = '{"option":"encrypt_data", "input_data":"'+get_flag+'"}'
p.sendline(payload)

flag = json.loads(p.recvline())['encrypted_data']
flag = bytes.fromhex(flag)
print(flag)

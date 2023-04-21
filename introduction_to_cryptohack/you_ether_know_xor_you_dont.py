from Crypto.Util.number import *
from pwn import *

#cipher = long_to_bytes(0x0e0b213f26041e) #1e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104)
cipher = long_to_bytes(0x0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104)
key = b'myXORkey'

# print(xor(cipher, b'crypto{')) #myXORke

for c in range(len(cipher)) :
	print(chr(cipher[c] ^ key[c % 8]), end='')

#print(xor(cipher, b'myXORkey'))
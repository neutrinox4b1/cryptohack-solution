from pwn import *
cipher = b'label'

print(xor(cipher, 13))
print("".join(chr(c ^ 13) for c in cipher))
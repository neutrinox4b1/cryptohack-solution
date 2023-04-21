# from Crypto.Util.number import *

cipher = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
# cipher =  0x73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
# print(long_to_bytes(cipher))

for i in range(1, 100) :
    search = "".join(chr(c ^ i) for c in cipher)
    if ('crypto' in search) :
	    print(search) 
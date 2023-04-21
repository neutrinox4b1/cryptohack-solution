# plain = b'SF{x0r_w0nd3rfu1_0p3r4ti0n}'
# key = b'ljm'

# res = ''
# for i in range(len(plain)) :
# 	res += chr(plain[i] ^ key[i % len(key)])
# res = bytes.hex(bytes(res, 'utf-8'))
# print(res)

from Crypto.Util.number import *

flag = b'SF{h3ll0_3ul3r}'
# x = bytes_to_long(flag)

p = 101524035174539890485408575671085261788758965189060164484385690801466167356667036677932998889725476582421738788500738738503134356158197247473850273565349249573867251280253564698939768700489401960767007716413932851838937641880157263936985954881657889497583485535527613578457628399173971810541670838543309159139
a = 186961272294686700656155272802788390168287172598620717634486652020822281
x = pow(a, (p+1)//4, p)
print(x)
print(long_to_bytes(x))




# cnt = 1 
# for i in range(p) :
#     if pow(i, (p-1)//2, p) == 1:
#         if i == pow(x, 2, p) :
#             print('here!', end='')
#         print(i, cnt)
#         cnt += 1

# print(pow(x, 2, p))

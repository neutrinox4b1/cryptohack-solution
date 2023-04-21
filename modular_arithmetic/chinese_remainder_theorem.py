# from sympy.ntheory.modular import crt

# print(crt([2, 3, 5], [5, 11, 17])[0])

x = 5
while True :
	if x % 11 == 3 :
		if x % 5 == 2 :
			print(x)
			break
		else :
			x += 17 * 11
	x += 17
# import sympy

# def euler_totient(n):
#     factors = sympy.factorint(n)
#     result = 1
#     for factor in factors:
#         result *= factor-1
#     return result

N = 882564595536224140639625987659416029426239230804614613279163
e = 65537

c = 77578995801157823671636298847186723593814843845525223303932
# phi = euler_totient(N)
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

print(pow(c, d, N))
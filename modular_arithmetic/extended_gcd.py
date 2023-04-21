def EEA(r1, r2, u1, u2, v1, v2) :
    if r2 == 0:
        print(f'gcd: {r1}\nu: {u1}\nv: {v1}')
        return
    q = r1//r2
    r = r1 - q*r2
    u = u1 - q*u2
    v = v1 - q*v2

    return EEA(r2, r, u2, u, v2, v)

EEA(33, 123, 1, 0, 0, 1)
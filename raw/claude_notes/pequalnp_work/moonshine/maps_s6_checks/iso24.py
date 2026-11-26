from sympy import primerange
def ap(f, p):
    cnt = 1
    for x in range(p):
        v = f(x) % p
        if v == 0: cnt += 1
        elif pow(v, (p-1)//2, p) == 1: cnt += 2
    return p + 1 - cnt
E1 = lambda x: x*(x-1)*(x-9)          # y^2 = u(u-1)(u-9): double cover of X0(6) branched at cusps (T6 = u - 9)
E2 = lambda x: (x-1)*(x-2)*(x+2)      # 24a1
print([(p, ap(E1, p), ap(E2, p)) for p in primerange(5, 60)])
print("same a_p:", all(ap(E1, p) == ap(E2, p) for p in primerange(5, 200)))

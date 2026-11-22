# w_m(Q) = order of H^0(Q, Q/Z(m)) = largest N with (Z/N)^x of exponent dividing m; compare with the formula of prop:B-integral-structure
from sympy import factorint, totient, primerange
from math import gcd
def lam(N):  # Carmichael function
    from sympy.ntheory import reduced_totient
    return reduced_totient(N)
def w_direct(m, bound=10**6):
    # N = prod over primes of maximal powers with lambda(p^k) | m
    N = 1
    for p in primerange(2, 2000):
        k = 0
        while lam(p**(k+1)) and m % lam(p**(k+1)) == 0 and p**(k+1) < bound:
            k += 1
        N *= p**k
    return N
def w_formula(m):
    if m % 2: return 2
    v2 = factorint(m).get(2, 0)
    N = 2**(2 + v2)
    for p in primerange(3, 2000):
        if m % (p - 1) == 0:
            N *= p**(1 + factorint(m).get(p, 0))
    return N
ok = all(w_direct(m) == w_formula(m) for m in range(2, 41))
print('w_m formula agrees with the direct computation for m = 2..40:', ok, [w_formula(m) for m in (2, 4, 6, 8, 12)])

"""Check the mixed Eisenstein prime traces and the sieve by exact arithmetic."""
from functools import lru_cache
from math import gcd, isqrt, log


# a+b*w, w=(-1+sqrt(-3))/2.
def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def scale(k, x):
    return (k*x[0], k*x[1])


def conj(x):
    return (x[0]-x[1], -x[1])


def legendre(n, p):
    val = pow(n % p, (p-1)//2, p)
    return -1 if val == p-1 else val


@lru_cache(maxsize=None)
def coefficients(p):
    """Return trace, determinant; compute both Hecke symbols over split primes."""
    real_det = 1 if p % 4 == 1 else -1
    if p % 3 == 2:
        assert -legendre(12, p) == real_det
        return (0, 0), real_det
    d = next(k for k in range(1, p) if k*k % p == (-3) % p)
    psi_values = []
    for dh in [d, p-d]:
        w = (dh-1)*((p+1)//2) % p
        pows = [1, w, (w*w) % p]
        code = pows.index(pow(269 % p, (p-1)//3, p))
        psi_values.append(scale(legendre(2*dh,p), [(1,0),(0,1),(-1,-1)][code]))
    assert mul(*psi_values) == (real_det,0)
    tr = add(*psi_values)
    assert conj(tr) == scale(real_det, tr)
    if p % 12 == 1:
        quartic = 1 if pow(3, (p-1)//4, p) == 1 else -1
        assert tr == (quartic*(3*(pow(269, (p-1)//3, p)==1)-1),0)
    else:
        assert tr in [(0,0),(1,2),(-1,-2)]
    return tr, real_det


def primes(limit):
    flags = bytearray([1])*(limit+1)
    flags[:2] = bytes(2)
    for p in range(2, isqrt(limit)+1):
        if flags[p]: flags[p*p::p] = bytes((limit-p*p)//p+1)
    return [p for p in range(5,limit+1) if flags[p] and p!=269]


def main():
    y = 5000
    bound = 2*y
    z = log(y)**2
    # Polynomial convolution on multiplicative positive integer indices.
    F, A, H = [[(0,0)]*(bound+1) for _ in range(3)]
    F[1] = A[1] = H[1] = (1,0)
    proof_pair = None
    imag_primes = []
    def multiply_poly(array, powers):
        if not powers:
            return
        for n in range(bound//min(d for d, _ in powers),0,-1):
            if array[n] == (0,0):
                continue
            for d, v in powers:
                if n*d<=bound:
                    array[n*d] = add(array[n*d], mul(array[n],v))
    good = primes(bound)
    for p in good:
        t, det = coefficients(p)
        if p % 12 == 7 and p>z and t!=(0,0):
            for q in imag_primes:
                if y < p*q <= bound:
                    proof_pair = proof_pair or (q, p, mul(coefficients(q)[0],t))
            imag_primes.append(p)
        # 1/(1-tT+det T²).
        older, last, power = (0,0),(1,0),p
        euler = []
        while power <= bound:
            current = add(mul(t,last),scale(-det,older))
            euler.append((power,current))
            older,last,power = last,current,power*p
        multiply_poly(A,euler)
        if p>z:
            multiply_poly(F,[(p,t)])
            corr=[(p*p, add((det,0),scale(-1,mul(t,t)))), (p**3,scale(det,t))]
        else:
            corr=[(p,scale(-1,t)),(p*p,(det,0))]
        multiply_poly(H,[(d,v) for d,v in corr if d<=bound and v!=(0,0)])
    conv = [(0,0)]*(bound+1)
    for d in range(1,bound+1):
        if H[d] != (0,0):
            for n in range(1,bound//d+1):
                conv[d*n] = add(conv[d*n],mul(H[d],A[n]))
    assert F == conv
    for n, v in enumerate(F):
        if v != (0,0):
            assert n % 12 in (1,7)
            assert conj(v) == scale(1 if n % 12==1 else -1, v)
    print("exact identities through",bound,"checked at",len(good),"good primes")
    print("dyadic pair (p,q,complex product) at y=5000:",proof_pair)
    assert proof_pair is not None
    print("a(7), a(19), product:",coefficients(7)[0],coefficients(19)[0],
          mul(coefficients(7)[0],coefficients(19)[0]))


if __name__ == "__main__":
    main()

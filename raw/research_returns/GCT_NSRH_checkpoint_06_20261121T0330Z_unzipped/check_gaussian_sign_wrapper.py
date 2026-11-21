"""Exact small-field checks for F50; no floating point or claimed general proof."""
from collections import Counter
from itertools import product
import sympy as sp

h, z = sp.symbols("h z")


def determinants(k):
    ds = [sp.Integer(1), sp.Integer(1)]
    for j in range(2, k + 1):
        ds.append(sp.expand(ds[-1] - h * h * ds[-2] / 4))
    return ds


def mod_eval(poly, a, p):
    value = sp.cancel(poly.subs(h, a))
    num, den = map(int, sp.fraction(value))
    return (num * pow(den % p, -1, p)) % p


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def residue(poly, p):
    return sp.rem(sp.Poly(poly, z, domain=sp.ZZ),
                  sp.Poly(sum(z ** i for i in range(p)), z, domain=sp.ZZ))


records = []
for k in range(2, 11):
    ds = determinants(k)
    matrix = sp.eye(k)
    for j in range(k - 1):
        matrix[j, j + 1] = matrix[j + 1, j] = h / 2
    assert sp.expand(matrix.det() - ds[k]) == 0
    assert sp.gcd(sp.Poly(ds[k], h), sp.Poly(ds[k - 1], h)).degree() == 0
records.append("Tridiagonal determinants and consecutive coprimality: k=2..10 PASS")

for p in [3, 5, 7, 11, 13]:
    for k in range(2, 31, 2):
        d = determinants(k)[k]
        numerator = sp.together(d).as_numer_denom()[0]
        poly = sp.Poly(numerator, h, modulus=p)
        squarefree = sp.gcd(poly, poly.diff()).degree() == 0
        if (k + 1) % p:
            assert squarefree, (p, k, d)
records.append("Sufficient squarefree condition: p=3,5,7,11,13 and even k<=30 PASS")

for p, k in [(3, 2), (3, 4), (3, 6), (5, 2), (5, 4), (5, 6),
             (7, 2), (7, 4), (11, 2), (11, 4)]:
    ds = determinants(k)
    counts = Counter()
    zero_count = 0
    for xs in product(range(p), repeat=k):
        path = sum(xs[i] * xs[i + 1] for i in range(k - 1)) % p
        if path == 0:
            zero_count += 1
            counts[sum(x * x for x in xs) % p] += 1
    N = sum(c * z ** e for e, c in counts.items())
    g = sum(z ** ((x * x) % p) for x in range(p))
    chi_sum = sum(chi(mod_eval(ds[k], a, p), p) for a in range(p))
    radical_sum = sum(chi(mod_eval(ds[k - 1], a, p), p)
                      for a in range(p) if mod_eval(ds[k], a, p) == 0)
    assert residue(p * N - g ** k * chi_sum -
                   p * g ** (k - 1) * radical_sum, p).is_zero
    expected_zeros = p ** (k - 1) + p ** (k // 2) - p ** (k // 2 - 1)
    assert zero_count == expected_zeros
    if k == 2:
        assert residue(N - 2 * g + 1, p).is_zero
    records.append(f"Exact cyclotomic G12 and graph zero-count: p={p}, k={k} PASS")

d4 = determinants(4)[4]
assert sp.Poly(sp.together(d4 - (h*h - 1)**2).as_numer_denom()[0],
               h, modulus=5).is_zero
assert mod_eval(determinants(4)[3], 1, 5) == 3
records.append("Excluded p=5,k=4: d4=(h^2-1)^2 and d3(+-1)=3 mod5 PASS")

for record in records:
    print(record)

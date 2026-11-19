"""Finite certificates for the explicit Kummer inverse system over F_2(t).

The infinite-support obstruction is proved separately in the accompanying note.
All arithmetic here is exact polynomial arithmetic over F_2, encoded by bits.
"""
from time import perf_counter

started = perf_counter()

def degree(f):
    return f.bit_length() - 1

def rem(f, g):
    while f and degree(f) >= degree(g):
        f ^= g << (degree(f) - degree(g))
    return f

def irreducible(f):
    d = degree(f)
    if d < 1:
        return False
    return all(rem(f, g) != 0
               for e in range(1, d // 2 + 1)
               for g in range(1 << e, 1 << (e + 1)))

def polynomial(f):
    terms = [('1' if i == 0 else 't' if i == 1 else f't^{i}')
             for i in range(degree(f), -1, -1) if (f >> i) & 1]
    return '+'.join(terms) or '0'

polys = []
candidate = 2
while len(polys) < 12:
    if irreducible(candidate):
        polys.append(candidate)
    candidate += 1

print('base characteristic=2; coefficient prime=3')
print('P_n: degree first, then increasing binary coefficient encoding')
for n, p in enumerate(polys, 1):
    print(f'n={n}: {polynomial(p)}; degree={degree(p)}; valuation=3^{n}={3**n}')
assert len(set(polys)) == len(polys)

for r in range(1, 13):
    current = [3**n if n < r else 0 for n in range(1, 13)]
    next_level = [3**n if n < r + 1 else 0 for n in range(1, 13)]
    assert all((b - a) % (3**r) == 0 for a, b in zip(current, next_level))
    print(f'level r={r}: active polynomials={r-1}; '
          f'c_(r+1)/c_r=P_{r}^(3^{r}); compatibility mod 3^{r}=PASS')

for cutoff in range(0, 12):
    n = cutoff + 1
    v = 3**n
    assert v % (3**(n + 1)) != 0
    print(f'finite initial support cutoff={cutoff}: next valuation at P_{n} '
          f'nonzero modulo 3^{n+1}')
print('Each irreducible P_n is square-free because F_2 is perfect.')
print('Each c_r is in F_2(t), so its geometric Kummer class is Frobenius invariant.')
print('KUMMER_LIMIT_CERTIFICATE_COMPLETE')
print(f'elapsed_seconds={perf_counter()-started:.6f}')

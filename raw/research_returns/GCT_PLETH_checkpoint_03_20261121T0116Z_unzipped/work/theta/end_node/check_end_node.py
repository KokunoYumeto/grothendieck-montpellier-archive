"""Exact algebra checks for T024--T026; independent coefficient checks are elsewhere."""
from pathlib import Path
import csv
import math
import sympy as sp

HERE = Path(__file__).resolve().parent
T = sp.Symbol('T')
rows = []
for m in range(3, 8):
    e = {i: sp.Symbol(f'e{i}') for i in range(2, m + 1)}
    f = T**m + sum((-1)**i * e[i] * T**(m-i) for i in e)
    disc = sp.Poly(sp.discriminant(f, T), *e.values())
    N = m * (m-1) // 2
    assert all(sum(i*a for i,a in zip(e, mon)) == 2*N for mon,c in disc.terms())
    # The residual odd permutation acts by (-1)^i on e_i.
    assert all(sum(i*a for i,a in zip(e, mon)) % 2 == 0 for mon,c in disc.terms())
    exposed = m if m % 2 == 0 else m-1
    exponent = m-1 if m % 2 == 0 else m
    winners = [(mon,c) for mon,c in disc.terms() if mon[exposed-2] == exponent]
    assert len(winners) == 1
    mon, coefficient = winners[0]
    assert coefficient != 0
    assert mon == tuple(exponent if i == exposed else 0 for i in e)
    assert all(mon[exposed-2] <= exponent for mon,c in disc.terms())
    assert math.gcd(exponent, 2) == 1
    # Rational normalization, avoiding any square-root extension.
    c,Y,D = sp.symbols('c Y D', nonzero=True)
    normalized = (c**((exponent-1)//2)*D)**2 - (c*Y)**exponent
    assert sp.expand(normalized-c**(exponent-1)*(D**2-c*Y**exponent)) == 0
    rows.append(dict(m=m, discriminant_terms=len(disc.terms()),
                     exposed_coefficient=f'e{exposed}', exponent=exponent,
                     leading_scalar=coefficient, weighted_degree=2*N,
                     check='homogeneity; parity; unique exposed term; primitive exponent; rational normalization',
                     status='PASS'))
    print('PASS discriminant', m, len(disc.terms()), coefficient, flush=True)
    if m == 4:
        s,q,p = sp.symbols('s q p')
        expected = 256*p**3-128*s**2*p**2+144*s*q*p-27*q**2+16*s**4*p-4*s**3*q
        actual = disc.as_expr().subs({e[2]:s,e[4]:p})
        assert sp.expand(actual-expected.subs(q,e[3]**2)) == 0

with (HERE/'DISCRIMINANT_CHECK.tsv').open('w', newline='') as out:
    writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
    writer.writeheader();writer.writerows(rows)
print('PASS exact discriminant and degeneration checks', flush=True)

#!/usr/bin/env python3
"""Independent exact supplement for HD-ALT07; no author code imported.

The universal theorem is audited separately. Symmetric-group characters at
fixed-point-free involutions are reconstructed by signed domino removal,
not by the Fomin--Lulov product formula whose bound is being checked.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from math import factorial, comb
from datetime import datetime, timezone
import hashlib
import json
import time
import sympy as S

start = time.perf_counter()
HERE = Path(__file__).resolve().parent
PROOF = HERE.parents[2] / 'research/ordinary_alternating_fixed_free_section.tex'
proof_hash = hashlib.sha256(PROOF.read_bytes()).hexdigest()
assert proof_hash == '78ffa543eacf6f88a656c2bc37f673b75acca4eba98671cbba9f564f4885c9b7'

def partitions(n, top=None):
    if n == 0:
        yield ()
        return
    for first in range(min(n, top or n), 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest

@lru_cache(None)
def domino_character(part):
    if not part:
        return 1
    value = 0
    for i, row in enumerate(part):
        below = part[i+1] if i+1 < len(part) else 0
        if row >= 2 and row-2 >= below:
            child = list(part)
            child[i] -= 2
            value += domino_character(tuple(x for x in child if x))
        if i+1 < len(part) and row == part[i+1]:
            lower = part[i+2] if i+2 < len(part) else 0
            if row-1 >= lower:
                child = list(part)
                child[i] -= 1
                child[i+1] -= 1
                value -= domino_character(tuple(x for x in child if x))
    return value

def degree(part):
    product = 1
    for i, row in enumerate(part):
        for j in range(row):
            product *= row-j + sum(r > j for r in part[i+1:])
    return factorial(sum(part)) // product

counts = []
long_count = 0
for n in range(16, 31, 2):
    count = 0
    for part in partitions(n):
        a = degree(part)
        chi = domino_character(part)
        assert chi*chi * comb(n,n//2) <= 4**(n//2)*a
        assert abs(chi) <= a
        assert (a-chi) % 2 == 0
        k = n-part[0]
        if 2 <= k and 4*k < n:
            assert a >= n*(n-3)//2
            assert 2*abs(chi) < a
            long_count += 1
        count += 1
    counts.append({'n':n,'partitions':count})

n, x = S.symbols('n x', real=True)
c = (1-S.sqrt(S.Rational(3,5)))/2
beta_c = c*n*(n-1-c*n)/((n-1)*(n-2))
assert S.simplify(c*(1-c)-S.Rational(1,10)) == 0
assert S.simplify(beta_c-S.Rational(1,10)-c*((2-3*c)*n-2+2*c)/((n-1)*(n-2))) == 0
assert Fraction(3,5) < Fraction(4,5)**2  # c>1/10
assert Fraction(3,5) > Fraction(3,4)**2  # c<1/8
polys = [n*n-11*n-8, n*n-8*n+8, 13*n*n-151*n+48]
translated = [S.Poly(S.expand(p.subs(n,x+15)),x) for p in polys]
assert all(all(v>0 for v in p.all_coeffs()) for p in translated)
assert S.factor((13*n-16)*(n-3)-96*n-(13*n*n-151*n+48)) == 0

for n0 in range(15, 501):
    assert n0*(n0-3) > 8*(n0+1)
    for k in range(1,(n0-1)//4+1):
        beta = Fraction(k*(n0-1-k),(n0-1)*(n0-2))
        assert beta < Fraction(1,4)
    if n0 % 2 == 0:
        assert comb(n0,n0//2)*(n0+1) >= 2**n0

witness = (88,12)
a = degree(witness)
assert a == 908791246463100
assert Fraction(88,100) > Fraction(87,100)
assert Fraction(19,25)**2 < Fraction(3,5)
beta = Fraction(12*87,99*98)
first_row_squares = sum(j*j for j in range(88))
content_upper = comb(100,2)-12*89
v_upper = Fraction(4*(content_upper**2+100*99-3*first_row_squares),100*99*98*97)
old_delta = min(Fraction(1,4),beta,(1-v_upper)/4)
assert old_delta == Fraction(1519571,15684900) < Fraction(1,10)
assert beta == Fraction(58,539)
assert beta > Fraction(1,10)+Fraction(3,5*a)

out = {
    'status':'PASS',
    'actual_utc':datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds':time.perf_counter()-start,
    'proof_sha256':proof_hash,
    'independent_domino_character_partition_counts':counts,
    'total_partitions':sum(r['partitions'] for r in counts),
    'nonstandard_long_shapes':long_count,
    'translated_universal_polynomials':[str(p.as_expr()) for p in translated],
    'witness':{'partition':witness,'degree':a,'old_delta':str(old_delta),'beta':str(beta),'allowed_ceiling':str(Fraction(1,10)+Fraction(3,5*a))},
    'scope':'Signed domino character recursion plus exact universal arithmetic identities and supplementary finite comparisons. No author code imported; author mathematical proof read before writing this checker. No finite sample is the universal proof.'
}
(HERE/'audit_alternating_fixed_free.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

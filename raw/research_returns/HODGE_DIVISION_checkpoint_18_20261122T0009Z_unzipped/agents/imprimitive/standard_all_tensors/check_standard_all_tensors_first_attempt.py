#!/usr/bin/env python3
"""Exact finite supplement to HD-AST10--12; not an infinite proof.

Original code by /root/imprimitive.  Uses Fraction word spectra and
actual permutations; no sibling or root arithmetic is imported.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product, permutations
from math import gcd
from pathlib import Path
import json
import time

import sympy as s

HERE = Path(__file__).resolve().parent
START = time.perf_counter()
COUNTS = Counter()


def mod1(x):
    return x % 1


def rotation_data(alpha, t):
    """Exact eigenphases of (X tensor I...) cyclic rotation."""
    a = len(alpha)
    seen = set()
    spectrum = Counter()
    full_return = Counter()
    error = 0
    orbit_sizes = Counter()
    for word in product(range(a), repeat=t):
        full_return[mod1(sum((alpha[i] for i in word), Q(0)))] += 1
        if word in seen:
            continue
        orbit = []
        w = word
        phase = Q(0)
        while w not in seen:
            seen.add(w)
            orbit.append(w)
            phase += alpha[w[-1]]
            w = (w[-1],) + w[:-1]
        assert w == word
        d = len(orbit)
        assert t % d == 0
        orbit_sizes[d] += 1
        error += t-d
        for j in range(d):
            spectrum[mod1((phase+j)/d)] += 1
    assert len(seen) == a**t == sum(spectrum.values())
    R = sum(a**gcd(t,j) for j in range(1,t))
    assert error == R
    max_x = max(Counter(alpha).values())
    nu_x = a-max_x
    for z,m in spectrum.items():
        N = full_return[mod1(t*z)]
        assert t*m-N <= R
        assert N <= a**(t-1)*max_x
        assert Q(a**t-m) >= (1-Q(1,t))*a**t + Q(a**(t-1)*nu_x-R,t)
        assert 2*m <= a**t+a
        COUNTS['exact_weighted_eigenvalue_targets'] += 1
    if a >= 4:
        assert R <= 2*a**(t-2)
    COUNTS['weighted_cycle_cases'] += 1
    COUNTS['weighted_words'] += a**t
    COUNTS['weighted_word_orbits'] += sum(orbit_sizes.values())
    return {'a':a,'t':t,'alpha':[str(v) for v in alpha],
            'R':R,'max_multiplicity':max(spectrum.values()),
            'orbit_counts':dict(sorted(orbit_sizes.items()))}


cases = []
for a,tmax in ((2,8),(3,7),(4,7),(5,6)):
    patterns = (
        [Q(0)]*a,
        [Q(j, a) for j in range(a)],
        [Q((j*j+2*j)%12,12) for j in range(a)],
    )
    for t in range(3,tmax+1):
        for alpha in patterns:
            cases.append(rotation_data(alpha,t))

# Exact R grid, supplemented by the symbolic two-parity induction below.
for a in range(4,41):
    for t in range(3,81):
        R = sum(a**gcd(t,j) for j in range(1,t))
        assert R <= 2*a**(t-2)
        if t >= 6:
            assert t-1 <= 2*a**((t+1)//2-2)
        COUNTS['rotation_error_grid'] += 1

# Pair selection uses integer indices and no positivity assumption on a
# preselected pair; it checks the maximizing pair actually has positive sum.
for t in range(3,7):
    for indices in product(range(6),repeat=t):
        I = sum(indices)
        if I == 0:
            continue
        pairmax = max(indices[i]+indices[j]
                      for i in range(t) for j in range(i+1,t))
        assert pairmax > 0 and t*pairmax >= 2*I
        COUNTS['pair_selection_vectors'] += 1


def cycle_count(p):
    seen = set()
    c = 0
    for i in range(len(p)):
        if i in seen:
            continue
        c += 1
        j = i
        while j not in seen:
            seen.add(j)
            j = p[j]
        assert j == i
    return c


# Actual covers' permutation indices, including arbitrary cycle products.
for n,t in ((3,3),(3,4),(4,3)):
    perms = list(permutations(range(n)))
    for factors in product(perms,repeat=t):
        pfix = tuple(b*n+factors[b][x] for b in range(t) for x in range(n))
        pcyc = tuple(((b+1)%t)*n+factors[(b+1)%t][x]
                     for b in range(t) for x in range(n))
        idx = sum(n-cycle_count(p) for p in factors)
        assert n*t-cycle_count(pfix) == idx
        h = []
        for x in range(n):
            j = x
            for _ in range(t):
                j = pcyc[j]
            assert 0 <= j < n
            h.append(j)
        assert n*t-cycle_count(pcyc) == n*(t-1)+n-cycle_count(h)
        COUNTS['actual_letter_action_tuples'] += 1

# Universal algebraic identities and endpoint inductions.
n,t,N,H = s.symbols('n t N H',integer=True,positive=True)
a = n-1
rank_sum = (2*(1-1/t)*a**t + a**(t-2)*(n-3)*N/t
            + a**(t-1)*H/t + 5*n*a**(t-2)
            - 2*a**(t-1)/t - 4*a**(t-2)/t)
# Divide out the positive a^(t-2)/t first, so only polynomials remain.
poly = 2*(t-1)*a*a + (n-3)*N + a*H + 5*n*t - 2*a - 4
excess_poly = s.expand(poly.subs(N,2*a-H)-2*t*a*a)
assert s.expand(excess_poly-((5*t-6)*n+2+2*H)) == 0
assert s.expand(2*(3-Q(1,1)/a)/4+(a-1)/(2*a)+9/a-(2+8/a)) == 0

u,v = s.symbols('u v',integer=True,nonnegative=True)
# These shifted expressions have only nonnegative rational coefficients.
positive_polys = {
    'R_induction':s.expand(((u+4)*((v+6)-1)-((v+6)+1))),
    'marked_excess_min':s.expand(8*(u+14)**2-6),
    'scalar_full_support':s.expand((u+14)**2-(u+15)/2),
    'final_excess_core':s.expand(((5*(v+3)-6)*(u+15)+2)-3*(v+3)*(u+15)),
    'final_uniform_gap':s.Integer(3*15*14-6),
}
for expr in positive_polys.values():
    assert all(c.is_Rational and c >= 0 for c in s.Poly(expr,u,v).coeffs())
    assert expr.subs({u:0,v:0}) > 0
for aa in range(4,101):
    assert 5 <= 2*aa
    assert 6 <= 2*aa*aa
    COUNTS['R_induction_base_pairs'] += 1
for nn in range(15,101):
    for tt in range(3,31):
        aa = nn-1
        ex = Q(aa**(tt-2)*((5*tt-6)*nn+2),tt)
        assert ex > 6
        COUNTS['source_endpoint_grid'] += 1

# Publication-facing source validation catches delimiter and control escapes.
proof = HERE/'standard_all_tensors_section.tex'
raw = proof.read_bytes()
txt = raw.decode()
assert txt.count(r'\[') == txt.count(r'\]')
assert not any(b < 32 and b not in (9,10,13) for b in raw)
tags = []
import re
tags = re.findall(r'\\tag\{([^}]+)\}',txt)
assert len(tags) == len(set(tags)) == 18

out = {
    'status':'PASS',
    'actual_utc':datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds':time.perf_counter()-START,
    'proof_sha256':sha256(raw).hexdigest(),
    'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'counts':dict(COUNTS),
    'weighted_cycle_cases':cases,
    'symbolic_excess_after_RH':str(excess_poly),
    'positive_shifted_polynomials':{k:str(v) for k,v in positive_polys.items()},
    'scope':'Exact finite and symbolic supplement; universal proofs are in HD-AST10--12. No Hurwitz enumeration or independent peer audit is claimed.',
    'failed_attempts':[],
}
(HERE/'standard_all_tensors_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','actual_utc','elapsed_seconds','proof_sha256','counts')},indent=2))

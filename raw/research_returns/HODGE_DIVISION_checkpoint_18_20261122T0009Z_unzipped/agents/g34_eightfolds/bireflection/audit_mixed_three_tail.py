"""Independent exact supplement for root HD-MT301--03.

No author-checker imports. Rational cyclic spectra are reconstructed by
triangular inversion in virtual permutation-cycle characters, not the
author's Ramanujan transform. Actual flag actions check that reconstruction.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from collections import Counter
from itertools import combinations, permutations
from math import gcd, lcm
import hashlib, json, time
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
START = time.perf_counter()
STAMP = datetime.now(timezone.utc).isoformat()

def partitions(n, maximum=None):
    if n == 0:
        yield ()
    else:
        for k in range(min(n, maximum or n), 0, -1):
            for rest in partitions(n-k, k):
                yield (k,) + rest

def divisors(n):
    return [d for d in range(1, int(n**0.5)+1) if n%d == 0]

def alldivisors(n):
    low = divisors(n)
    return sorted(set(low + [n//d for d in low]))

def trace(parts, power):
    # Garsia--Goupil applied to the standard S3 character (2,0,-1):
    # ( (f)_3 - 3(f)_2 + 3f )/3 - X3.
    f = sum(d for d in parts if power%d == 0)
    x3 = sum(gcd(d,power) for d in parts if d//gcd(d,power) == 3)
    numerator = f*(f-1)*(f-2)-3*f*(f-1)+3*f
    assert numerator%3 == 0
    return numerator//3-x3

def cycle_character(parts):
    order = lcm(*parts)
    ds = alldivisors(order)
    weights = {}
    for d in ds:
        numerator = trace(parts,d)-sum(e*c for e,c in weights.items() if d%e == 0)
        assert numerator%d == 0
        weights[d] = numerator//d
    multiplicities = {r:sum(c for d,c in weights.items() if d%r == 0) for r in ds}
    return weights, multiplicities

classes = spectra = 0
least = None
for n in range(15,30):
    degree = n*(n-2)*(n-4)//3
    alpha = Fraction(n*n-8*n+8,3)
    beta = Fraction(n*(n-3),3)
    for part in partitions(n):
        weights, mult = cycle_character(part)
        assert min(mult.values()) >= 0
        assert sum(d*c for d,c in weights.items()) == degree
        assert sum(int(s.totient(r))*c for r,c in mult.items()) == degree
        assert 3*trace(part,1) >= -n
        index = n-len(part)
        if index:
            margin = degree-max(mult.values())-alpha*index-beta
            assert margin >= 0
            least = margin if least is None else min(least,margin)
        classes += 1
        spectra += len(mult)

def cycles(points, action):
    unseen = set(points)
    answer = Counter()
    while unseen:
        first = next(iter(unseen))
        z = first
        length = 0
        while z in unseen:
            unseen.remove(z)
            z = action(z)
            length += 1
        assert z == first
        answer[length] += 1
    return answer

actual_cases = actual_points = actual_orbits = 0
for n in range(15,30):
    examples = [(n,), (n-3,2,1), (n-5,3,2),
                (2,)*(n//2)+(1,)*(n%2),
                (3,)*(n//3)+(1,)*(n%3),
                (4,)*(n//4)+(1,)*(n%4)]
    for part in examples:
        perm = []
        offset = 0
        for d in part:
            perm.extend(offset+(j+1)%d for j in range(d))
            offset += d
        virtual = Counter()
        # Flag: a distinguished member of a three-element set.
        triple = list(combinations(range(n),3))
        flags = [(frozenset(c),i) for c in triple for i in c]
        actions = [
          (flags, lambda z:(frozenset(perm[i] for i in z[0]),perm[z[1]]), 1),
          ([frozenset(c) for c in triple], lambda z:frozenset(perm[i] for i in z), -1),
          (list(permutations(range(n),2)), lambda z:(perm[z[0]],perm[z[1]]), -1),
          (list(range(n)), lambda z:perm[z], 1)]
        for pts, action, sign in actions:
            orb = cycles(pts,action)
            actual_points += len(pts)
            actual_orbits += sum(orb.values())
            for d,c in orb.items():
                virtual[d] += sign*c
        expected,_ = cycle_character(part)
        assert all(virtual[d] == expected.get(d,0) for d in set(virtual)|set(expected))
        actual_cases += 1

n,f,x = s.symbols('n f x')
a = n*(n-2)*(n-4)/3
A = (n*n-8*n+8)/3
B = n*(n-3)/3
b = n/3
c = (n*n+n*f+f*f-6*n-6*f+8)/3
assert s.expand(a-f*(f-2)*(f-4)/3-(n-f)*c) == 0
assert s.expand(f*(f-2)*(f-4)+f-f*(f-3)**2) == 0
p = s.expand((n-f)*(f*f+(n-6)*f+2*n)-2*n*(n-2))
assert s.expand(p-(-f**3+6*f*f+(n*n-8*n)*f+4*n)) == 0
assert s.expand(p.subs(f,2)-2*(n-2)*(n-4)) == 0
assert s.expand(p.subs(f,n-2)-2*(n-4)**2) == 0
assert s.expand(s.diff(p,f,2)-(12-6*f)) == 0
assert s.expand(2*A*(n-1)+12*B-2*a-(6*n*n-20*n-16)/3) == 0
assert s.expand(18*B+2*A*(n-1)-2*a-2-(12*n*n-38*n-22)/3) == 0
positive = [A,B-6,a-B,a-1-2*(A+B),A+B-b,A+B-97,
            2*A*(n-1)+12*B-2*a-6,
            18*B+2*A*(n-1)-2*a-2]
for z in positive:
    q = s.Poly(s.expand(z.subs(n,x+15)),x)
    assert all(c >= 0 for c in q.all_coeffs()) and q.eval(0)>0

proof = ROOT/'research/alternating_mixed_three_tail_section.tex'
assert hashlib.sha256(proof.read_bytes()).hexdigest() == '3073a8ef70d698db8d7ff748ba7df56c1352e24fa1dfbdb1c3c61d54f783f8a8'
out = {'status':'PASS','started_utc':STAMP,
       'completed_utc':datetime.now(timezone.utc).isoformat(),
       'elapsed_seconds':time.perf_counter()-START,
       'partition_classes':classes,'exact_phase_order_entries':spectra,
       'least_margin':str(least),'actual_flag_cases':actual_cases,
       'actual_points':actual_points,'actual_orbits':actual_orbits,
       'universal_positive_polynomials':len(positive),
       'scope':'Independent cyclic triangular inversion and actual flag action; finite certificate supplements the separately checked universal proof.',
       'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest()}
(HERE/'audit_mixed_three_tail.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

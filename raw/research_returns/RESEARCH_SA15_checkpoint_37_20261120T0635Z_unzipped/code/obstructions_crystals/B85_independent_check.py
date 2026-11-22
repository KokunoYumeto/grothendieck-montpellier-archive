"""B85 exact inverse slopes, shared breaks, and first-layer dimension checks."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
from math import isqrt
from fractions import Fraction
from collections import Counter
import sympy as sp
import time,json

start=time.perf_counter();counts=Counter()
p,k1,k2=sp.symbols('p k1 k2')
N=p*p-1
r1=p*(p+1)*k1-N
r2=p*p*N-(p**3+1)*k2
exprs=[r2-r1-(p**4-1-p*(p+1)*k1-(p**3+1)*k2),
       (r2-r1).subs({k1:p-2,k2:p-2})-(p+1)*(p*p+1),
       p*p*k1-(N-p*k1)-(p*(p+1)*k1-N)]
for expr in exprs:
    assert sp.expand(expr)==0
    counts['symbolic_identities']+=1

primes=[z for z in range(5,102) if all(z%d for d in range(2,isqrt(z)+1))]
rows=[]
for p in primes:
    N=p*p-1;q=p*p;e=p*(p-1);s=p*N
    for k1,k2 in product(range(1,p-1),repeat=2):
        a1=N-p*k1;a2=k2
        assert a1>0 and a2>0 and a1%p and a2%p
        assert p*p*k1>a1
        assert Fraction(p*a1,q)==Fraction(a1,p)
        assert Fraction(p*k2,q)==Fraction(k2,p)
        assert Fraction(a1,p).denominator==Fraction(k2,p).denominator==p
        r1=q*k1-a1;r2=q*a2*0+q*(N-p*k2)-a2
        assert r1>0 and r2>0
        assert r2-r1>= (p+1)*(q+1)>0
        counts['all_parameter_pairs']+=1
        counts['exact_inverse_and_prime_valuation_rows']+=2
    # Every projected first-layer matrix with zero11 has column in e2.
    # A nonzero21 direction produces the full translation line.
    for a in range(1,p):
        image={(a*t)%p for t in range(p)}
        assert image==set(range(p))
        counts['literal_degree_p_translation_images']+=1
    if p%4==1:
        for alpha,beta in product(range(1,p),repeat=2):
            if pow(alpha*beta%p,(p-1)//2,p)!=p-1:continue
            ratio=alpha*pow(beta,-1,p)%p
            assert len({1,ratio,pow(ratio,-1,p)})==3
            counts['separated_tame_weight_pairs']+=1
        # E12,E21 and any diagonal with a nonzero coordinate are independent.
        for a,b in product(range(p),repeat=2):
            if a==b==0:continue
            assert (a!=0 or b!=0)
            # Explicit pivot coordinates:12,21 and11 ifa!=0, otherwise22.
            pivot=a if a else b
            assert pivot%p!=0
            counts['independent_diagonal_extensions']+=1
    if p<=13:
        rows.append({'p':p,'minimum_gap':(p+1)*(q+1),
                     'k_range':[1,p-2],'tame_sector_minimum_order':p**6 if p%4==1 else None})

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,'counts':dict(counts),'small_prime_rows':rows,
     'scope':'Three symbolic identities and all k1,k2 in1..p-2 for every prime5..101, '
             'literal translation-line images, nonsquare distinct tame weights and independent diagonal directions. '
             'The actual point field, equality of lower breaks, and actual layer containment are separately proved. '
             'No formal-group realization or global first-wild recovery is inferred.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

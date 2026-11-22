"""B84 exact two-translation inequality and normalized p5 parameter checks."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
from fractions import Fraction
from collections import Counter
from math import isqrt
import sympy as sp
import json,time

start=time.perf_counter();counts=Counter()
p,e,b1,b2=sp.symbols('p e b1 b2')
q=p*p;s=(p+1)*e
low=q*b2-b2-(q-1)*b1
high=q*(s-p*b2)-b2-(q*(s-p*b1)-b1)
cross=q*b2-b2-(q*(s-p*b1)-b1)
expressions=[low-(q-1)*(b2-b1),high-(p**3+1)*(b1-b2),
             cross.subs({b1:e-1,b2:e-1})+q*(p+1)]
for expr in expressions:
    assert sp.expand(expr)==0
    counts['symbolic_two_translation_identities']+=1

primes=[p for p in range(5,102) if all(p%d for d in range(2,isqrt(p)+1))]
for p in primes:
    q=p*p
    for factor in (1,2,p,p+1):
        e=factor*(p-1);s=(p+1)*e
        if p<=13:
            points=range(1,e)
        else:
            points=sorted({z for z in (1,2,p-1,p,p+1,e//2,e-p,e-1) if 0<z<e})
        for b1,b2 in product(points,repeat=2):
            if b1%p==0:continue
            assert Fraction(b1,q).denominator==q
            alpha1=s-p*b1
            assert alpha1>e>max(b1,b2)
            cross=q*b2-b2-(q*alpha1-b1)
            assert cross<0
            low=(q-1)*(b2-b1)
            high=(p**3+1)*(b1-b2)
            assert (low>=0 and high>=0)==(b1==b2)
            if b2%p==0:
                assert not(low>=0 and high>=0)
                counts['mixed_prime_divisible_exclusions']+=1
            counts['point_field_two_break_rows']+=1
        counts['arbitrary_index_samples']+=1

p=5;N=24;e=20
cs=[c for c in range(N) if c%4==1]
rows=[]
for k1,k2 in product(range(1,p-1),repeat=2):
    B1=p*p*k1;B2=p*p*k2
    if B1>B2:continue
    for c1,c2 in product(cs,repeat=2):
        if (B1-c1)%6 or (B2-c2)%6:continue
        orbit1=sorted({c1,5*c1%N});orbit2=sorted({c2,5*c2%N})
        if orbit1==orbit2:continue
        h1=(c1-B1)%N;l1=(p*c1+B1)%N
        h2=(c2-B2)%N;l2=(p*c2+B2)%N
        assert h1%6==l1%6==h2%6==l2%6==0
        assert h1!=l1 and h2!=l2
        if sorted((h1,l1))!=sorted((h2,l2)):continue
        assert h1==l2 and h2==l1
        rows.append({'B':[B1,B2],'c':[c1,c2],
                     'high_low':[[h1,l1],[h2,l2]],'finite_orbits':[orbit1,orbit2]})
assert [(r['B'],r['c']) for r in rows]==[([25,75],[1,9]),([25,75],[13,21])]
assert sorted({(1+12)%24,(5+12)%24})==[13,17]
assert sorted({(9+12)%24,(21+12)%24})==[9,21]
counts['normalized_p5_necessary_rows']=len(rows)
counts['quadratic_twist_orbit_checks']=2
out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,'counts':dict(counts),
     'normalized_p5_rows':rows,
     'scope':'Three symbolic identities valid for arbitrary e; complete b-pairs at p5,7,11,13 '
             'and four index factors1,2,p,p+1, plus stated boundary samples at primes17..101; '
             'exact normalized p5 both-divisible character enumeration. '
             'No bound on the full division field is assumed or established by these finite tests. '
             'Actual common point fields and their high/low translations are proved separately; '
             'the surviving parameter row is not an existence statement.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

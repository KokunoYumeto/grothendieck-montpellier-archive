"""B82 finite matrix, valuation and break certificate; not an existence test."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
from collections import Counter
from fractions import Fraction
from math import isqrt
import json,time
import sympy as sp

start=time.perf_counter();counts=Counter();matrix_rows=[]
p,e,s,b1,b2=sp.symbols('p e s b1 b2')
low=p**4*b2-b2-(p**4-1)*b1
high=p**4*(s-p*b2)-b2-(p**4*(s-p*b1)-b1)
cross=p**4*b2-b2-(p**4*(s-p*b1)-b1)
identities=[low-(p**4-1)*(b2-b1),high-(p**5+1)*(b1-b2),
            cross.subs({s:(p+1)*e,b1:e-1,b2:e-1})+p**4*(p+1)]
for x in identities:
    assert sp.expand(x)==0
    counts['symbolic_break_identities']+=1

for p in (5,7,11):
    allowed=[]
    outside=[(x,y) for x in range(p) for y in range(1,p)]
    for C in product(range(p),repeat=4):
        if C==(0,0,0,0):
            continue
        images=[((C[0]*x+C[1]*y)%p,(C[2]*x+C[3]*y)%p) for x,y in outside]
        no_zero=all(v!=(0,0) for v in images)
        constant_status=len({v[1]==0 for v in images})==1
        good=no_zero and constant_status
        predicted=C[2]==0 and (C[3]!=0 or (C[0]==0 and C[1]!=0))
        assert good==predicted
        if good:allowed.append(C)
        counts['all_terminal_matrix_tests']+=1
        counts['outside_vector_image_tests']+=len(outside)
    assert len(allowed)==p*p*(p-1)+(p-1)
    allowed=set(allowed)
    # All possible maximal planes: span(E12,diag(a,1)), a in F_p.
    for a in range(p):
        plane={(u*a%p,v,0,u) for u,v in product(range(p),repeat=2)}
        assert len(plane)==p*p and plane-{(0,0,0,0)}<=allowed
        assert {(C[0],C[1],C[2],C[3]) for C in plane if C[3]==0}=={
            (0,v,0,0) for v in range(p)}
        counts['maximal_terminal_planes']+=1
    matrix_rows.append({'p':p,'allowed_nonzero_terminal_matrices':len(allowed),
                        'maximal_planes':p})

primes=[p for p in range(5,102) if all(p%d for d in range(2,isqrt(p)+1))]
for p in primes:
    e=p*(p-1);s=(p+1)*e
    shapes=[(eps,r1,t) for eps in (0,1) for r1 in range(5) for t in range(3)
            if eps+r1+t==4 and r1<=t]
    assert shapes==[(0,2,2),(1,1,2)]
    counts['actual_layer_shape_rows']+=1
    for k1,k2 in product(range(1,p-1),repeat=2):
        same=(p*p*(k1-k2))%(p-1)==0
        assert same==(k1==k2)
        counts['small_divisible_character_pairs']+=1
    if p<=13:
        for B in range(1,p*e):
            value=Fraction(p**4*B,p**5)
            assert (value.denominator==1)==(B%p==0)
            counts['actual_field_integrality_rows']+=1
        for b1,b2 in product(range(1,e),repeat=2):
            if b1%p==0:
                continue
            alpha1=s-p*b1
            assert alpha1>e>b2
            rN=p**4*alpha1-b1
            rD=(p**4-1)*b1
            assert p**4*b2-b2-rN<0
            counts['high_line_mismatch_exclusions']+=1
            low_gap=p**4*b2-b2-rD
            high_gap=p**4*(s-p*b2)-b2-rN
            assert low_gap==(p**4-1)*(b2-b1)
            assert high_gap==(p**5+1)*(b1-b2)
            assert (low_gap>=0 and high_gap>=0)==(b1==b2)
            counts['two_actual_break_recoveries']+=1

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,'counts':dict(counts),
     'matrix_rows':matrix_rows,
     'scope':'Three symbolic break identities; every nonzero matrix and every outside-high-line vector '
             'at p5,7,11; all maximal permitted terminal planes; exact valuation and pair inequalities '
             'at p5,7,11,13; layer and small-parameter congruences for primes5..101. '
             'Actual uniformizer, formal quotient, Galois and Newton proofs are separate. '
             'No formal-group existence or unrestricted p3-recovery is inferred.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

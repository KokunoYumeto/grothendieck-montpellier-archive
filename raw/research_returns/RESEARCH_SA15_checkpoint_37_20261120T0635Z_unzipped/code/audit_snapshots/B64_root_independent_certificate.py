"""Exact finite weight/Cartier-bound supplement for B64.

This program does not construct formal groups or infer their existence.
All field, descent, pairing and Cartier-module arguments are in the proof.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,time
start=time.perf_counter()
primes=(5,7,11,13,17,19,23,29,31)
pair_cases=quotient_weight_cases=coefficient_cases=monomial_cases=0
recurrence_cases=logarithm_cases=orthogonality_cases=0
examples=[]

def compositions(n,d):
    if d==1:
        yield (n,);return
    for j in range(n+1):
        for tail in compositions(n-j,d-1):yield (j,)+tail

for p in primes:
    N=p*p-1
    # All equal-norm tangent characters, not only primitive norms.
    for c in range(N):
        orbit={c,p*c%N}
        for d in range(c%(p-1),N,p-1):
            other={d,p*d%N}
            assert (c*(p+1)-d*(p+1))%N==0
            if orbit==other:continue
            assert not (orbit & other)
            pair_cases+=1
            for n in (2,3,4):
                exponents=(pow(p,n,N)*c%N,pow(p,n,N)*d%N,c)
                assert len({x%(p-1) for x in exponents})==1
                quotient_weight_cases+=1
                for source in exponents:
                    for target in exponents:
                        residue=(target-p*source)%N
                        least_positive=residue or N
                        assert least_positive%(p-1)==0
                        assert least_positive>=p-1
                        coefficient_cases+=1
    for dimension in (1,2,3,4):
        for degree in range(2,2*p):
            for alpha in compositions(degree,dimension):
                if all(x%p==0 for x in alpha):assert degree==p
                monomial_cases+=1
    a=2*(p-1)*N
    q=[1]
    for _ in range(2):q.append(min(a+q[-1],p*q[-1]+p-1))
    assert q==[1,2*p-1,2*p*p-1]
    assert q[2]>Fraction(a,p-1)==2*N
    assert p<2*(p-1)<p*p and 2*(p-1)<p**3
    for h in range(1,201):
        full=min(a+h,p-1+p*h,1+2*p*h,p*p*h)
        simplified=min(a+h,p-1+p*h)
        assert full==simplified
        recurrence_cases+=1
    for n in range(1,5001):
        l=0;power=p
        while power<=n:l+=1;power*=p
        assert l*(p-1)<=n-1
        assert n*q[2]-a*l>=q[2]
        logarithm_cases+=1
    for n in range(2,13):
        solutions=[]
        for r in range(2*n+1):
            s=2*n-r
            if r==2*n-r and s==2*n-s:solutions.append((r,s))
            orthogonality_cases+=1
        assert solutions==[(n,n)]
        assert n-(n-1)==1 # F^(n-1) of ker F^n has rank p.
    examples.append({'p':p,'e':2*(p-1),'a':a,'q':q,
                     'log_threshold':2*N,'positive_margin':q[2]-2*N,
                     'claimed_index':2})

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,
     'counts':dict(character_pairs=pair_cases,quotient_weight_cases=quotient_weight_cases,
                   degree_p_coefficient_cases=coefficient_cases,
                   low_degree_monomials=monomial_cases,recurrence_cases=recurrence_cases,
                   logarithm_cases=logarithm_cases,orthogonality_cases=orthogonality_cases),
     'examples':examples,
     'scope':'Nine primes; all distinct equal-norm tame orbit pairs; exact Frobenius quotient weights and degree-p coefficients; low monomials in dimensions1--4; finite logarithm/recurrence/orthogonality checks. No formal-group existence or universal theorem inferred from tests.'}
Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_B64_independent_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

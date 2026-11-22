#!/usr/bin/env python3
"""Independent exact supplement to ATT07--09 by /root/imprimitive.

The weighted tests construct actual integer matrices and factor their
characteristic polynomials. No author code or selected spectra imported.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
import time
import sympy as S

start=time.perf_counter()
here=Path(__file__).resolve().parent
proof=here.parents[1]/'g34_eightfolds/bireflection/alternating_two_tail_all_tensors_section.tex'
assert sha256(proof.read_bytes()).hexdigest()=='2e9afd9be79f01ee143291b73619837be11182569bccc0234bfb66d45c73372b'
z=S.symbols('z')
counts=Counter()
records=[]

def max_multiplicity(M):
    poly=M.charpoly(z).as_expr()
    _, factors=S.factor_list(poly,z)
    assert sum(S.degree(f,z)*m for f,m in factors)==M.rows
    # Characteristic zero and finite order make every irreducible factor
    # separable. The exponent is the multiplicity of each complex root.
    assert all(S.gcd(f,S.diff(f,z))==1 for f,m in factors)
    return max(m for f,m in factors),S.expand(poly)


Xcases=[S.diag(1,-1),S.Matrix([[0,1],[1,0]]),S.eye(2),
        S.diag(1,1,-1),S.Matrix([[0,0,1],[1,0,0],[0,1,0]]),-S.eye(3)]
for X in Xcases:
    a=X.rows
    mx,_=max_multiplicity(X)
    for t in ((3,4,6) if a==2 else (3,4)):
        words=list(product(range(a),repeat=t))
        lookup={w:j for j,w in enumerate(words)}
        T=S.zeros(a**t)
        R=S.zeros(a**t)
        for j,w in enumerate(words):
            R[lookup[(w[-1],)+w[:-1]],j]=1
            for k in range(a):
                if X[k,w[-1]]:
                    T[lookup[(k,)+w[:-1]],j]=X[k,w[-1]]
        # This checks the normal form on the actual matrix, without any
        # diagonalization or rotation-orbit spectral algorithm.
        assert T**t==S.kronecker_product(*([X]*t))
        Rerr=sum(S.trace(R**j) for j in range(1,t))
        assert Rerr==sum(a**gcd(t,j) for j in range(1,t))
        mt,cp=max_multiplicity(T)
        assert t*mt<=a**(t-1)*mx+Rerr
        assert 2*mt<=a**t+a
        records.append({'a':a,'t':t,'X':str(X),'largest_multiplicity':int(mt),
                        'R':int(Rerr),'characteristic_polynomial':str(cp)})
        counts['actual_integer_weighted_matrices']+=1
        counts['matrix_dimension_total']+=a**t
        counts['unweighted_rotation_trace_powers']+=t-1

# A separate exact integer necklace recurrence computes primitive orbits,
# then compares the fully weighted short-orbit defect to rotation traces.
for a in range(2,27):
    P={}
    for t in range(1,61):
        P[t]=a**t-sum(P[d] for d in range(1,t) if t%d==0)
        assert P[t]>=0 and P[t]%t==0
        if t>=2:
            error=sum((t-d)*(P[d]//d) for d in range(1,t) if t%d==0)
            assert error==sum(a**gcd(t,j) for j in range(1,t))
            if a>=4 and t>=3:
                assert error<=2*a**(t-2)
            counts['primitive_necklace_recurrences']+=1

# Universal symbolic source arithmetic, including both different labels.
n,t,u,v=S.symbols('n t u v',integer=True,positive=True)
symbolic={}
for label,a,d0,kappa in (
    ('UP',n*(n-3)/2,n-3,5),
    ('EX',(n-1)*(n-2)/2,n-2,3),
):
    A=(n-5)/2;B=n/4
    raw=A*(2*n-2)+10*t*B-2*a-4/a
    target=(5*t/2-3)*n+kappa-4/a
    assert S.cancel(raw-target)==0
    shifted={
        'moving_dominates_basic':S.expand((a-1-2*d0).subs(n,u+15)),
        'scalar_dominates_B':S.expand((a-B).subs(n,u+15)),
        'kappa_error_positive':S.expand((kappa*a-4).subs(n,u+15)),
        'coefficient_ge_three_t_over_two':S.expand((5*t/2-3-3*t/2).subs(t,v+3)),
    }
    for key,p in shifted.items():
        coeff=S.Poly(p,u,v).coeffs()
        assert all(c.is_Rational and c>=0 for c in coeff)
        if key!='coefficient_ge_three_t_over_two':
            assert p.subs({u:0,v:0})>0
    # b0<=d0 proves forced movement uniformly, without a floor shortcut.
    min_mark_excess=S.expand((9*d0-(d0+1)/2).subs(n,u+15))
    assert all(c>0 for c in S.Poly(min_mark_excess,u).coeffs())
    symbolic[label]={k:str(p) for k,p in shifted.items()}
    symbolic[label]['forced_moving_coefficient_lower_bound']=str(min_mark_excess)
    for nn in range(15,81):
        aa=int(a.subs(n,nn));dd=int(d0.subs(n,nn))
        bb=1 if label=='UP' else (nn-1)//2
        for tt in range(3,31):
            excess=Fraction(aa**(tt-1),tt)*(Fraction(5*tt,2)*nn-3*nn+kappa-Fraction(4,aa))
            assert excess>Fraction(3*nn*aa**(tt-1),2)>6
            assert aa**(tt-1)*(9*dd-Fraction(bb+1,2))>6
            counts['independent_source_cases']+=1

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'elapsed_seconds':time.perf_counter()-start,'counts':dict(counts),
     'proof_sha256':sha256(proof.read_bytes()).hexdigest(),
     'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'matrix_records':records,'symbolic_checks':symbolic,
     'scope':'Independent actual integer characteristic polynomials, rotation traces, primitive-necklace recurrence and exact universal arithmetic. No author code/output imported; universal geometry checked as a proof.',
     'failed_attempts':[]}
(here/'independent_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('matrix_records','symbolic_checks')},indent=2))

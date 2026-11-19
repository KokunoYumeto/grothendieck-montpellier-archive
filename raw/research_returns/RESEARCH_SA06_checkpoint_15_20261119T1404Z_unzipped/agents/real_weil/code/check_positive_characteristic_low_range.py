#!/usr/bin/env python3
"""Exact finite checks for C.3av; the universal proof is independent.

Checks coefficient matrices, every projective Jacobian chart for selected
small-prime examples, and dimension/Tate-shift identities.  A finite
coefficient field is represented by adjoining its irreducible polynomial.
"""
from datetime import datetime,timezone
from pathlib import Path
from time import perf_counter
import itertools,json
import sympy as S

started=perf_counter();base=Path(__file__).resolve().parent

def data(p,d,mu):
    m=d+2;e=m if m%p else m+1
    y=S.symbols('y0:'+str(m));prod=S.prod(y)
    G=prod if e==m else prod*sum(y)
    F=sum(t**e for t in y)+mu*G
    basis=[tuple([1]*m)] if e==m else [tuple(1+(i==j) for i in range(m)) for j in range(m)]
    power=S.Poly(S.expand(F**(p-1)),*y)
    entries=[]
    for u in basis:
        row=[]
        for v in basis:
            exponent=tuple(p*b-a for a,b in zip(u,v))
            row.append(0 if min(exponent)<0 else power.coeff_monomial(exponent))
        entries.append(row)
    return m,e,y,F,S.Matrix(entries)

def check_parameter(p,d,mu,phi=None):
    m,e,y,F,A=data(p,d,mu)
    if phi is None:
        red=lambda a:int(a)%p
    else:
        red=lambda a:S.rem(S.expand(a),phi,mu,modulus=p)
    det=red(A.det())
    if det==0:return None
    chart_checks=[]
    for t in y:
        variables=tuple(x for x in y if x!=t)
        equations=[S.expand(g.subs(t,1)) for g in [F]+[S.diff(F,x) for x in y]]
        if phi is not None:
            variables+=(mu,);equations.append(phi)
        gb=S.groebner(equations,*variables,modulus=p)
        ok=len(gb.polys)==1 and gb.polys[0].as_expr()==1
        chart_checks.append(ok)
        if not ok:return None
    return {'p':p,'d':d,'degree':e,'g':A.rows,'parameter':str(mu),
            'field_polynomial':str(phi) if phi is not None else None,
            'equation':str(F),'hasse_matrix':[[str(red(a)) for a in row] for row in A.tolist()],
            'determinant':str(det),'jacobian_chart_unit_ideals':chart_checks,'passed':True}

examples=[]
for p,d in [(2,1),(3,1),(2,2),(3,2),(2,3)]:
    answer=None
    for mu in range(p):
        answer=check_parameter(p,d,mu)
        if answer:break
    if answer is None:
        u=S.Symbol('u')
        for degree in [2,3,4]:
            for coefficients in itertools.product(range(p),repeat=degree):
                phi=u**degree+sum(c*u**(degree-1-i) for i,c in enumerate(coefficients))
                if not S.Poly(phi,u,modulus=p).is_irreducible:continue
                answer=check_parameter(p,d,u,phi)
                if answer:break
            if answer:break
    if answer is None:raise AssertionError((p,d,'sample search exhausted'))
    examples.append(answer)

leading=[]
for p in [2,3,5,7,11]:
    for d in range(1,8):
        m=d+2;e=m if m%p else m+1
        if e==m:
            matrix=[[1]]
        else:
            matrix=[]
            for i in range(m):
                row=[]
                for j in range(m):
                    v=[p*(a==j)-(a==i) for a in range(m)]
                    coeff=0 if min(v)<0 else int(S.factorial(p-1)/S.prod(S.factorial(a) for a in v))%p
                    row.append(coeff)
                matrix.append(row)
        assert S.Matrix(matrix)==S.eye(len(matrix))
        assert e%p
        leading.append({'p':p,'d':d,'degree':e,'rank':len(matrix),'leading_matrix_identity':True})

dimensions=[]
for r in range(1,13):
    for N in range(r+2,2*r+2):
        d=2*r-N+2;s=N-r-2;n=d+2*s
        assert d>=1 and s>=0 and r==d+s and N==n+2
        assert d+n-(d+s)==r
        assert d+2*(r-d)==n
        assert d+2*(r-1-d)==n-2
        slope=S.Rational(n-2,2)-(s-1)
        assert slope==S.Rational(d,2)>0
        assert 2*r-n==d
        dimensions.append({'r':r,'N':N,'d':d,'s':s,'n':n,
                           'ambient_group_zero':bool(n%2),
                           'normalized_ambient_slope':str(slope),'passed':True})

record={'timestamp_utc':datetime.now(timezone.utc).isoformat(),
        'examples':examples,'leading_matrix_cases':leading,
        'dimension_and_Tate_shift_cases':dimensions,
        'counts':{'exact_examples':len(examples),'leading_matrices':len(leading),'dimension_cases':len(dimensions)},
        'scope':'Finite symbolic certificates only; full all-prime and all-dimension geometry is proved separately.',
        'runtime_seconds':perf_counter()-started}
(base/'check_positive_characteristic_low_range_output.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

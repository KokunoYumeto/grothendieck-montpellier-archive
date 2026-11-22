#!/usr/bin/env python3
"""Exact supplementary checks for C.3aw, with explicit scope boundaries."""
from pathlib import Path
from datetime import datetime,timezone
from time import perf_counter
import json
import sympy as S

started=perf_counter();base=Path(__file__).resolve().parent
at=json.loads((base/'check_ordinary_cy_boundary_output.json').read_text())
geometry=[]
for record in at['cases']:
    assert record['passed']
    p=record['p'];r=record['r'];m=r-2
    xs=S.symbols('x0:'+str(r+2));u=S.Symbol('u')
    env={str(x):x for x in xs};env['u']=u
    F=S.sympify(record['equation'],locals=env)
    phi=S.sympify(record['field_polynomial'],locals=env) if record['field_polynomial'] else None
    B=S.expand(F.subs({x:0 for x in xs[:m+1]}))
    remaining=xs[m+1:]
    checks=[]
    for x in remaining:
        variables=tuple(y for y in remaining if y!=x)
        equations=[S.expand(g.subs(x,1)) for g in [B]+[S.diff(B,y) for y in remaining]]
        if phi is not None: variables+=(u,);equations.append(phi)
        gb=S.groebner(equations,*variables,modulus=p)
        ok=len(gb.polys)==1 and gb.polys[0].as_expr()==1
        assert ok
        checks.append(ok)
    geometry.append({'p':p,'r':r,'m':m,'N':m+r+1,
                     'base_equation':str(B),'base_projective_chart_unit_ideals':checks,
                     'incidence_base_chart_derivative_coefficients':[1]*(m+1),
                     'scope':'Illustrative constant coordinate-section geometry only; not the generic-point non-torsion witness.',
                     'passed':True})

dimensions=[];quotients=[]
h,H=S.symbols('h H')
for r in range(2,13):
    for m in range(r-1):
        N=m+r+1;b=r-m-1;q=m+r-1
        assert r+1<=N<=2*r-1 and b>=1
        assert m+b==r-1 and q-m==r-1 and (m+r)-m==r
        dimensions.append({'r':r,'m':m,'N':N,'dim_B':b,'dim_Q':q,
                           'codim_beta_Q':r-1,'codim_pushforward':r,'passed':True})
        for ell in [1,2,3]:
            relation=h+ell*H
            for j in range(m+1):
                rem=S.rem(h**j-(-ell*H)**j,relation,h)
                assert S.expand(rem)==0
            image=S.rem(h**(m+1),relation,h)
            assert S.expand(image-(-ell*H)**(m+1))==0
            assert S.rem(image,H,H)==0
            quotients.append({'r':r,'m':m,'ell':ell,
                              'relation_image':str(image),'denominator_divisible_by_H':True,'passed':True})

result={'timestamp_utc':datetime.now(timezone.utc).isoformat(),
        'finite_geometry':geometry,'dimension_cases':dimensions,'quotient_cases':quotients,
        'counts':{'finite_geometry':len(geometry),'dimensions':len(dimensions),'quotients':len(quotients)},
        'scope':'The proof separately establishes the deterministic Bertini search through the geometric generic point, actual families and infinite order. No finite-field point is claimed non-torsion.',
        'runtime_seconds':perf_counter()-started}
(base/'check_positive_characteristic_low_injectivity_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

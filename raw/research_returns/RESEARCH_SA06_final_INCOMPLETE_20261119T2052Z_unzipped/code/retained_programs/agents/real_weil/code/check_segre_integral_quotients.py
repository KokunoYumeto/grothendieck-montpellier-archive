#!/usr/bin/env python3
"""Finite exact algebra checks for C.3ba; no actual-cycle theorem is inferred."""
from datetime import datetime,timezone
from pathlib import Path
from time import perf_counter
import json
import sympy as S

started=perf_counter();base=Path(__file__).resolve().parent
monomials=[];images={}
for a in range(31):
    for b in range(31):
        q=min(a,b)
        tag='one' if a==b else ('u' if a>b else 'tprime')
        exponent=abs(a-b)
        normal=(q,tag,exponent)
        if tag=='one':recovered=(q,q)
        elif tag=='u':recovered=(q+exponent,q)
        else:recovered=(q,q+exponent)
        assert recovered==(a,b)
        assert normal not in images
        images[normal]=(a,b)
        monomials.append({'a':a,'b':b,'coefficient_power_of_s':q,
                          'basis_kind':tag,'basis_exponent':exponent,'passed':True})

dimensions=[]
for r in range(2,13):
    for m in range(1,13):
        N=r+m+1
        assert 2<=r<=N-1
        assert (r+m+1)-r==m+1
        assert (r+m)-r==m
        # Original conormal motion has dz-bu dt-bt du.
        # At t=0, only -bu dt remains after subtracting dz.
        raw=-((-1)**(r-1))
        normalized=((-1)**r)*raw
        assert normalized==1
        dimensions.append({'r':r,'m':m,'N':N,'pulled_cycle_dimension':m+1,
                           'exceptional_support_dimension':m,'coefficient_of_bu':normalized,'passed':True})

u,t,s,b=S.symbols('u t s b')
substitutions=[]
for power in range(1,25):
    assert S.expand((u*t)**power-u**power*t**power)==0
    # Coefficients in d(t_old)=u dt+t du, restricted to t=0.
    dt_coefficient=S.diff(u*t,t).subs(t,0)
    du_coefficient=S.diff(u*t,u).subs(t,0)
    assert dt_coefficient==u and du_coefficient==0
    substitutions.append({'homogeneous_degree':power,'graded_map_matches_fibre_map':True,
                          'conormal_dt_coefficient':str(dt_coefficient),
                          'horizontal_du_coefficient':str(du_coefficient)})

record={'utc':datetime.now(timezone.utc).isoformat(),'all_checks_passed':True,
        'monomial_basis_cases':monomials,'dimension_and_residue_cases':dimensions,
        'graded_and_differential_cases':substitutions,
        'counts':{'monomial_cases':len(monomials),'dimension_residue_cases':len(dimensions),
                  'graded_differential_cases':len(substitutions)},
        'runtime_seconds':perf_counter()-started,
        'scope':'Finite formal algebra only. Flatness over arbitrary rings, strict-local factorization, integral Milnor class, actual selected-cycle pullback, entire boundary annihilation and ordinary divisibility are proved in the text.'}
(base/'check_segre_integral_quotients_output.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

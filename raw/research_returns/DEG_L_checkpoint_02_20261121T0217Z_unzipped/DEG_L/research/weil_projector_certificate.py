"""Exact rational polynomial checks for DEG_L B6, K=Q(omega), a=3+omega.
This checks examples, not general theorem proof and not a Lean certificate.
Requires SymPy. Run: python3 weil_projector_certificate.py
"""
import json
from pathlib import Path
import sympy as s

X=s.symbols('X')
u=7
trace=[2,5]
for k in range(1,16):
    trace.append(5*trace[-1]-7*trace[-2])
rows=[]
for n in (2,3,4):
    fw=X**2-trace[2*n]*X+u**(2*n)
    fr=(X-u**n)
    for r in range(1,n):
        fr*=X**2-u**r*trace[2*n-2*r]*X+u**(2*n)
    fr=s.expand(fr)
    resultant=s.resultant(fw,fr,X)
    # |a^k-bar(a)^k|^2 = 4*N(a)^k-Tr(a^k)^2.
    norm_product=u**(n*(2*n-1))
    for k in range(1,2*n):
        norm_product*=4*u**k-trace[k]**2
    assert resultant == norm_product
    epoly=s.expand(s.invert(fr,fw,X)*fr)
    coeffden=s.ilcm(*[s.denom(c) for c in s.Poly(epoly,X).all_coeffs()])
    P=s.expand(coeffden*epoly)
    assert all(c.is_Integer for c in s.Poly(P,X).all_coeffs())
    assert s.rem(epoly,fr,X)==0
    assert s.rem(epoly-1,fw,X)==0
    assert s.rem(epoly**2-epoly,fw*fr,X)==0
    rows.append(dict(n=n,f_W=str(fw),f_R=str(fr),resultant=str(resultant),
                     interpolation_coefficient_denominator=str(coeffden),
                     integral_numerator=str(P),
                     checks=['resultant_equals_norm_product','e_zero_mod_f_R',
                             'e_one_mod_f_W','e_idempotent_mod_product']))
text=json.dumps(rows,indent=2)
print(text)
Path(__file__).with_name('weil_projector_certificate_results.json').write_text(text+'\n')

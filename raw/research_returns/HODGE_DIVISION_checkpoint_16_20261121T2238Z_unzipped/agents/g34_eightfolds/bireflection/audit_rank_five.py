"""Independent exponent/compositum calculation for D-R5; no group search."""
from pathlib import Path
from fractions import Fraction
from math import gcd,lcm,prod
import json
HERE=Path(__file__).resolve().parent
phi=lambda n:sum(gcd(a,n)==1 for a in range(1,n+1))
orders=[1,2,3,4,5,6,8,10,12]
degrees={d:phi(lcm(3,d))//2 for d in orders}
assert [d for d in orders if degrees[d]==2]==[4,12]
cases=[]
for d in [4,12]:
    for b in range(d):
        if gcd(b,d)!=1:continue
        a=Fraction(b,d)
        for eps in [0,Fraction(1,2)]:
            w=[-a,-a,-a+Fraction(1,2),-a+Fraction(1,2),4*a+eps]
            assert sum(w)%1==eps
            spec=sorted([(a+v)%1 for v in w])
            assert spec.count(0)==2 and spec.count(Fraction(1,2))==2
            squared=sorted([(2*v)%1 for v in spec])
            assert squared.count(0)==4
            last=next(v for v in squared if v)
            assert last.denominator==(2 if d==4 else 6)
            cases.append({'d':d,'phase':str(a),'determinant_sign_exponent':str(eps),
                          'spectrum':[str(v) for v in spec],
                          'squared_reflection_order':last.denominator})
plus=[0,0,Fraction(1,2),Fraction(1,2),Fraction(1,4)]
minus=[0,0,Fraction(1,2),Fraction(1,2),Fraction(3,4)]
assert sum(plus)+sum(minus)+5==8
assert 10+sum(v!=0 for v in plus)+sum(v!=0 for v in minus)==16
assert all((10-ell)//2-(5-ell)//2==3 for ell in [0,2,4])
assert prod([4,6,10,12,18])==51840
out={'status':'PASS','cyclotomic_degree_formula':'[Q(zeta3,zeta_d):Q(zeta3)]=phi(lcm(3,d))/2',
     'degree_cases':degrees,'spectral_cases':cases,'signature':[3,3],
     'remaining_group_order':103680,
     'scope':'Independent exact field/exponent/graph arithmetic; no import of the authors checker, no group enumeration, no existence or generic endomorphism assertion.'}
(HERE/'audit_rank_five.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'field_cases':len(orders),'phase_sign_cases':len(cases)}))

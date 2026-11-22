"""Exact arithmetic supplement for the universal HD-ALT08 proof."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime,timezone
import hashlib,json,time
import sympy as s
start=time.perf_counter();R=Path(__file__).resolve().parent
n,c,x=s.symbols('n c x')
beta=lambda n,k:k*(n-1-k)/((n-1)*(n-2))
assert s.factor(beta(n,c*n)-c*(1-c)-c*((2-3*c)*n-2+2*c)/((n-1)*(n-2)))==0
polys={
 'quadratic_tail_lower_bound':s.expand((n*n-3*n-6).subs(n,15+x)),
 'radical_threshold_comparison':s.expand((49*n*n-595*n+480).subs(n,15+x)),
}
for p in polys.values():assert all(v>0 for v in s.Poly(p,x).all_coeffs())
assert s.factor((2*(n-3)/((n-1)*(n-2))-F(3,2)/n)*2*n*(n-1)*(n-2))==n*n-3*n-6
assert s.factor(((29*n-32)/(16*n**3)-6/(5*n*(n-3)))*80*n**3*(n-3))==49*n*n-595*n+480
assert F(15,256)>F(1,20)
rows=[];comparisons=0
for h in (4,6,10,18,42,66,162):
    ns=set(range(15,121))|set(range(max(15,5*h-3),5*h+4))
    cases=0
    for nn in sorted(ns):
        for k in range(1,(nn-1)//4+1):
            # On [0,1/4], x>=c_h iff x(1-x)>=1/(5h).
            if F(k*(nn-k),nn*nn)<F(1,5*h):continue
            e=(nn-1)**2 if k==1 else nn*(nn-3)//2
            value=F(k*(nn-1-k),(nn-1)*(nn-2))
            assert value>F(1,5*h)+F(3,5*e),(h,nn,k)
            cases+=1
    comparisons+=cases
    coeff=(1+s.sqrt(1-F(4,5*h)))/2
    rows.append({'h':h,'exact_long_row_coefficient':str(coeff),'decimal':str(s.N(coeff,18)),
                 'finite_threshold_comparisons':cases})
a=comb(100,6)-comb(100,5)
v=F(6*93,99*98)
assert a==1116764880 and v==F(31,539)
assert v<=F(1,10)+F(3,5*a)
assert v>F(1,20)+F(3,5*a)
out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-start,
 'proof_sha256':hashlib.sha256((R/'ordinary_alternating_conductor_section.tex').read_bytes()).hexdigest(),
 'universal_polynomial_identities':{k:str(v) for k,v in polys.items()},
 'field_parameters':rows,'finite_comparisons':comparisons,
 'strictness_witness':{'n':100,'shape':[94,6],'degree':a,'beta':str(v),'old_gate_satisfied':True,'new_h4_gate_violated':True},
 'scope':'Exact algebra and finite endpoint/shape inequalities supplement the universal proof. No character values or actual sources are inferred from the finite check.'}
(R/'alternating_conductor_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

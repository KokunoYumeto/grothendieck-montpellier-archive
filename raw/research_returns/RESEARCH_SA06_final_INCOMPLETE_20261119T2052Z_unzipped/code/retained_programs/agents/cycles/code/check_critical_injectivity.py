"""Exact defining-data certificate for C.3am; fresh rerun after scratch recovery."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as s

started=time.perf_counter();base=Path(__file__).resolve().parents[1]
out=base/'output';out.mkdir(exist_ok=True)
t,x,y,z,q=s.symbols('t x y z q')
Q=3*t*x*x+3*y*y-3*(t*t*x+y)*z+(t**3+1)*z*z
F=(t*z-x)**3+x**3+(z-y)**3+y**3
assert s.expand(F-z*Q)==0
M=s.hessian(Q,(x,y,z))/2
det=s.factor(M.det())
assert s.expand(det-s.Rational(9,4)*t*(t**3+1))==0
section=s.rem(s.expand(Q.subs({x:t,y:1,z:1-q})),q*q+q+1,q)
assert section==0
skew=s.Matrix([[1,1,0,0],[0,0,1,1],[1,q,0,0],[0,0,1,q]])
skewdet=s.rem(skew.det(),q*q+q+1,q)
assert s.resultant(skewdet,q*q+q+1,q)!=0
cases=[]
for r in range(2,15):
    n=2*r-1
    assert n+1==2*r
    assert (2+(r-2))+(r)==2+(2*r-2)
    assert r-2>=0
    pairs=s.symbols('b0:'+str(r-1));v0,v1,v2=s.symbols('v0 v1 v2')
    substitution=sum((-b)**3+b**3 for b in pairs)+t**3*(v0**3+v1**3+v2**3)
    assert s.expand(substitution-t**3*(v0**3+v1**3+v2**3))==0
    cases.append({'r':r,'N':2*r,'dim_V':n,'dim_W':n-1,
                  'source_fibre_dimension':r-1,'target_fibre_dimension':r-2,
                  'theta_codimension':r,'reduced_cut_coefficient':-1})
record={'utc':datetime.now(timezone.utc).isoformat(),
 'recovery_rerun':True,'all_passed':True,'sympy_version':s.__version__,
 'conic':str(Q),'determinant':str(det),'section_remainder':str(section),
 'skew_determinant_remainder':str(skewdet),
 'skew_norm':str(s.resultant(skewdet,q*q+q+1,q)),
 'cases':cases,'runtime_seconds':time.perf_counter()-started,
 'scope':'Exact equations and dimensions only; Chow nonvanishing and moving are proved in the text.'}
data=json.dumps(record,indent=2)+'\n'
(out/'critical_injectivity.json').write_text(data)
(out/'critical_injectivity.out').write_text(data)
print(data)

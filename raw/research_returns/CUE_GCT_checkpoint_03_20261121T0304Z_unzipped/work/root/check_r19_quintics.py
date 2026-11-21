from pathlib import Path
from datetime import datetime, timezone
import sympy as s
import json
q,K,X,z,x,y=s.symbols('q K X z x y')
d0=K*(q-1)/(q*(K-1));d1=(K-q)/(q*(K-1))
e0=K**2*(q-1)**2/(q*(K-1)*(q*K-1));e1=K*(K-q)*(q-1)/(q*(K-1)*(q*K-1));e2=(K-1)/(q*K-1)
assert s.cancel(d0*(x-q/K*y)+d1*(x-q*y)-(x-y))==0
assert s.cancel(e0*(x-1/K*y)*(x-q/K*y)+e1*(x-q*y)*(x-1/K*y)+e2*(x-y)*(x-q*y)-(x-y)**2)==0
v=lambda i:z-q**i
C=e0*v(-2)*v(-1)*v(0)*v(1)*(z-K)+e1/X*v(-1)*v(0)*v(1)*(z-K/q**3)*(z-q*K)+e2/X**2*v(0)*v(1)*(z-K/q**3)*(z-K/q**2)*(z-q**2*K)
D=d0*v(-1)*v(0)*v(1)*(z-K/q**2)*(z-K)+d1/X*v(0)*v(1)*(z-K/q**3)*(z-K/q)*(z-q*K)
det=s.factor(C.subs(z,K/q**3)*D.subs(z,K/q**2)-D.subs(z,K/q**3)*C.subs(z,K/q**2))
expected=K**6*(q-K)*(q**2-K)**2*(q**3-K)**2*(q**4-K)*(q-1)**6*(q+1)*(q*q+q+1)/(q**27*(K-1)*(q*K-1))
assert s.cancel(det-expected)==0
l0,l1,v0,vm,qq,rr=s.symbols('l0 l1 v0 vm qq rr')
c0=l0*l1+v0*qq;c1=vm*l1+qq*rr;c2=vm*v0+l0*rr
assert s.expand(vm*c0-l0*c1-qq*c2+2*qq*rr*l0)==0
assert s.expand(rr*c0+v0*c1-l1*c2-2*qq*rr*v0)==0
out={'checked_utc':datetime.now(timezone.utc).isoformat(),'checker':'root independent exact symbolic expansion','quintic_determinant':str(det),'independent_of_X':not det.has(X),'two_column_shift_identities':'PASS','two_column_cofactor_identities':'PASS','scope':'Supplement to full prose proof reading; not formal verification.'}
Path('work/root/r19_quintic_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))

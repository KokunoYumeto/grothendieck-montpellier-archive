from pathlib import Path
from datetime import datetime, timezone
import sympy as s
import json
q,K,X,z=s.symbols('q K X z')
a=(K-q)/(K-1);b=(q-1)/(K-1)
g2=q*(K-1)/(q*K-1);g1=(q-1)*(K-q)/((K-1)*(q*K-1));g0=(q-1)**2/((K-1)*(q*K-1))
v=lambda i:z-q**i
U=a*X*v(-1)*v(1)**2+b*v(0)*v(2)*(z-K/q)
V=g2*X**2*v(0)**2*v(1)+g1*X*v(1)**2*(z-K/q)+g0*v(2)*(z-K/q)*(z-K)
det=s.factor(U.subs(z,1)*V.subs(z,q)-V.subs(z,1)*U.subs(z,q))
expected=(q-K)*(q**2-K)*(q-1)**6*(q+1)/(q*(K-1)*(q*K-1))
assert s.cancel(det-expected)==0
u=s.symbols('u')
num=s.expand((K*u-1)*(q*K*u-1)-2*q*(u-1)*(K*u-1)+q*(u-1)*(u-q))
assert s.expand(num-(q*(K-1)**2*u**2+(q-1)*(K-q)*u+(q-1)**2))==0
# Verify both local permanent relations independently as polynomial identities.
L,M,v0,v1,p,t=s.symbols('L M v0 v1 p t')
c0=v0*v1+p*M;c1=L*v1+p*t;c2=L*M+v0*t
assert s.expand(L*c0-v0*c1-p*c2+2*p*t*v0)==0
assert s.expand(t*c0+M*c1-v1*c2-2*p*t*M)==0
out={'checked_utc':datetime.now(timezone.utc).isoformat(),'checker':'root independent exact symbolic expansion','R18_cubic_determinant':str(det),'independent_of_X':not det.has(X),'coefficient_ratio_numerator':'PASS','two_local_permanent_relations':'PASS','scope':'Supplement to full prose proof reading; not a formal proof of all statements.'}
Path('work/root/r18_cubic_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))

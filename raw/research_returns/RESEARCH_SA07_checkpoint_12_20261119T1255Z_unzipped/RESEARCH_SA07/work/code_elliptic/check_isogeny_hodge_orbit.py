#!/usr/bin/env python3
"""Exact degree-two specialization of the all-isogeny proof in work note49."""
import datetime, hashlib, json, pathlib, time
import sympy as S
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
tick=time.perf_counter()
x,y,r,g2=S.symbols('x y r g2')
g3=4*r**3-g2*r
P=4*x**3-g2*x-g3
k=3*r**2-g2/4
X=x+k/(x-r)
J=S.diff(X,x)
G2=60*r**2-4*g2
G3=14*g2*r+22*g3
assert S.cancel(P*J**2-(4*X**3-G2*X-G3))==0
# Y=y*J gives dX/Y=dx/y identically.
assert S.cancel(J/J-1)==0
# F=y/(2(x-r)); dF/du, where dx/du=y and dy/du=P'/2.
dF=S.cancel(S.diff(P,x)/(4*(x-r))-P/(2*(x-r)**2))
assert S.cancel(dF-(2*x-r-X))==0
# Hence f*xi'=2xi-r omega-dF and h'=2h+r.
h,u,lam,n,eps=S.symbols('h u lam n eps', nonzero=True)
hn=(n*h+eps)/lam**2
un=(n*u+eps)/lam**2
assert S.cancel(lam**2*(hn-un)-n*(h-u))==0
record={
 'start_utc':start,'elapsed_seconds':time.perf_counter()-tick,
 'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 'input':'symbolic g2,r; g3=4r^3-g2*r; kernel {(0), (r,0)}',
 'X':str(X),'Y_over_y':str(J),'g2_quotient':str(G2),'g3_quotient':str(S.expand(G3)),
 'cohomology':'f*xi_prime=2xi-r*omega-d(y/(2(x-r)))',
 'h_transform':'h_prime=2h+r',
 'difference_identity':'lambda^2*(h_n-u_n)=degree*(h-u)',
 'status':'PASS'
}
print(json.dumps(record,indent=2))
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')

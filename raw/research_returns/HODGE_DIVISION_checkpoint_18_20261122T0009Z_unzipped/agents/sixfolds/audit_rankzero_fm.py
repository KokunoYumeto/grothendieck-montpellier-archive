#!/usr/bin/env python3
"""Independent six-generator exterior-algebra audit of D-SR03.
Basis order a,b,c,d,u,v; integrates c,d. Exact symbolic arithmetic.
"""
from collections import defaultdict
import sympy as S
import json
s,t=S.symbols('s t')

def add(*xs):
    z=defaultdict(lambda:S.Integer(0))
    for x in xs:
        for m,c in x.items():z[m]+=c
    return {m:S.expand(c) for m,c in z.items() if S.expand(c)!=0}
def scale(c,x):return {m:S.expand(c*v) for m,v in x.items() if S.expand(c*v)!=0}
def wedge(x,y):
    z=defaultdict(lambda:S.Integer(0))
    for m,c in x.items():
        for n,d in y.items():
            if m&n:continue
            count=sum((n&((1<<i)-1)).bit_count() for i in range(6) if m>>i&1)
            z[m|n]+=(-1)**count*c*d
    return {m:S.expand(c) for m,c in z.items() if S.expand(c)!=0}
def expw(x):
    z={0:S.Integer(1)};term=z
    for k in range(1,4):
        term=scale(S.Rational(1,k),wedge(term,x));z=add(z,term)
    return z
v=[{1<<i:S.Integer(1)} for i in range(6)]
a,b,c,d,u,vv=v
ab=wedge(a,b);cd=wedge(c,d);uv=wedge(u,vv)
gamma=add(wedge(a,vv),scale(-1,wedge(b,u)))
form=add(scale(s,wedge(add(a,c),add(b,d))),scale(-t,cd),scale(-1,wedge(c,vv)),wedge(d,u))
trans=expw(form)
integ={m^12:coeff for m,coeff in trans.items() if m&12==12}
claim=add({0:s-t},scale(-s*t,ab),scale(-s,wedge(b,u)),scale(-1,uv),scale(s,wedge(a,vv)),scale(-s,wedge(ab,uv)))
assert add(integ,scale(-1,claim))=={}
# Equal-root factorization, before imposing any quadratic relation.
eq={m:S.expand(co.subs(t,s)) for m,co in integ.items()}
rhs=scale(-1,wedge(expw(scale(S.Rational(1,2),gamma)),wedge(add(scale(s,a),scale(-1,u)),add(scale(s,b),scale(-1,vv)))))
assert add(eq,scale(-1,rhs))=={}
# Unequal-root factorization with t=-2-s and N=st.
N=-s*(s+2);alpha=2*(s+1)
H=add(scale(N,ab),uv,gamma)
rawrhs=scale(alpha,expw(add(scale(S.Rational(1,2),gamma),scale(-1/alpha,H))))
lhs={m:S.expand(co.subs(t,-2-s)) for m,co in integ.items()}
res=add(lhs,scale(-1,rawrhs))
assert all(S.cancel(co)==0 for co in res.values())
# Odd polynomial after Delta=1/N, aa=N/(4d), alpha²=-4d.
dsym,Hsym,al=S.symbols('d H alpha',nonzero=True)
poly=S.expand(al**3/(4*dsym)*sum(-2*(Hsym/al)**k/S.factorial(k) for k in [1,3,5]))
poly=S.expand(poly.subs(al**2,-4*dsym).subs(al**-2,-1/(4*dsym)))
claimpoly=2*Hsym-Hsym**3/(12*dsym)+Hsym**5/(960*dsym**2)
assert S.simplify(poly-claimpoly)==0
print(json.dumps({'single_plane_transform':'passed','equal_root_factorization':'passed','unequal_root_factorization':'passed','full_odd_polynomial':str(claimpoly),'scope':'Formal exterior algebra and exact scalar calculation only; no sheaf-theoretic proof certification.'},indent=2))

#!/usr/bin/env python3
"""Exact polynomial maps for the five-point quadrics and exceptional six-point action."""
from pathlib import Path
from itertools import permutations, combinations
from functools import lru_cache
from math import gcd
from functools import reduce
import sympy as s
HERE=Path(__file__).resolve().parent
x,y,z,w=s.symbols("x y z w")
q=(x,y,z,w)
f=s.Matrix((x*z-x*y,x*w-x*y,y*z-x*y,y*w-x*y,z*w-x*y))
A,B,C,D,E=s.symbols("A B C D E")
uu=(A,B,C,D,E)
cubic=A*D*(E-B-C)-B*C*(E-A-D)
M=s.Matrix([
    [y-w,y,y,y-w,0],
    [z-y,-y,-y,-y,-y],
    [0,-x,-w,-x,-w],
    [0,x,z,0,0],
    [0,0,0,x,y],
])
N=s.Matrix([y*(x-w),z*(y-w),x*(w-y),y*(w-z),x*(z-w)])
assert all(s.expand(v)==0 for v in f.T*M)
assert all(s.expand(v)==0 for v in M*N)
assert s.gcd_list(list(N)) == 1
minor=s.factor(M[:4,:4].det())
assert minor != 0
assert s.expand(cubic.subs(dict(zip(uu,f)),simultaneous=True))==0
assert s.expand(cubic.subs({A:C,B:D,C:A,D:B},simultaneous=True)+cubic)==0

identity=tuple(range(5))
perms=tuple(permutations(range(5)))
def compose(a,b):return tuple(a[b[i]] for i in range(5))
def inverse(a):return tuple(a.index(i) for i in range(5))
def sign(a):return (-1)**sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))
def powers(a):
    out=[identity]
    while True:
        nxt=compose(out[-1],a)
        if nxt==identity:return tuple(out)
        out.append(nxt)
def subgroup_image(g,H):
    gi=inverse(g)
    return tuple(sorted(compose(compose(g,h),gi) for h in H))
HH=tuple(sorted({tuple(sorted(powers(g))) for g in perms if len(powers(g))==5}))
assert len(HH)==6
H0=HH[0]
normalizer=tuple(g for g in perms if subgroup_image(g,H0)==H0)
assert len(normalizer)==20

@lru_cache(None)
def rho(g):
    gi=inverse(g)
    columns=[]
    for i in range(4):
        j=gi[i]
        columns.append(s.eye(4)[:,j] if j<4 else -s.ones(4,1))
    mat=s.Matrix.hstack(*columns)
    transformed=mat*s.Matrix(q)
    out=s.zeros(5,5)
    for i,poly in enumerate(f):
        pp=s.Poly(s.expand(poly.subs(dict(zip(q,transformed)),simultaneous=True)),*q)
        for j,mon in enumerate((x*z,x*w,y*z,y*w,z*w)):
            out[j,i]=pp.coeff_monomial(mon)
        assert s.expand(poly.subs(dict(zip(q,transformed)),simultaneous=True)
                        -(f.T*out[:,i])[0])==0
    return out

P=sum((sign(g)*rho(g) for g in normalizer),s.zeros(5,5))/20
assert P.rank()==1
v=next(P[:,i] for i in range(5) if P[:,i] != s.zeros(5,1))
den=s.ilcm(*[a.q for a in v])
v=v*den
div=reduce(gcd,(abs(int(a)) for a in v if a))
v=v/div
vv=[]
cosets=[]
for H in HH:
    g=next(g for g in perms if subgroup_image(g,H0)==H)
    cosets.append(g)
    vv.append(sign(g)*rho(g)*v)
V=s.Matrix.hstack(*vv)
assert V.rank()==5
assert V*s.ones(6,1)==s.zeros(5,1)
for g in perms:
    for i,H in enumerate(HH):
        j=HH.index(subgroup_image(g,H))
        assert rho(g)*vv[i] == sign(g)*vv[j]
six=[s.expand((s.Matrix(uu).T*vj)[0]) for vj in vv]
sumcube=s.expand(sum(t**3 for t in six))
ratio=s.cancel(sumcube/cubic)
assert ratio.is_Rational and ratio != 0

def cycletype(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen:continue
        j=i;n=0
        while j not in seen:
            seen.add(j);n+=1;j=p[j]
        out.append(n)
    return tuple(sorted(out,reverse=True))
classmap={}
for g in perms:
    cyc=cycletype(g)
    sixperm=tuple(HH.index(subgroup_image(g,H)) for H in HH)
    typ=cycletype(sixperm)
    assert cyc not in classmap or classmap[cyc]==typ
    classmap[cyc]=typ

lines=[
    "T-038 exact syzygy and exceptional-action certificate",
    "f^T M = 0; M N = 0; gcd(N)=1: PASS",
    f"nonzero 4x4 minor = {minor}",
    "cubic substitution and sign under (12): PASS",
    "six Sylow-5 subgroup action and all 120 intertwining identities: PASS",
    "six linear forms:",
]+[str(t) for t in six]+[
    f"sum(t_i^3) = ({ratio}) * cubic",
    "class map:",
]+[f"{k} -> {v}" for k,v in sorted(classmap.items())]
(HERE/"FIVE_POINT_EXACT_MAPS.txt").write_text("\n".join(lines)+"\n")
print("\n".join(lines))


#!/usr/bin/env python3
"""Exact certificate for D:Chow-surface-boundary-obstruction.

Polynomial identities are over Z; finite checks are separately over F2,F3,F5.
They corroborate, rather than replace, the characteristic-free proof.
"""
import hashlib
import itertools
import json
import pathlib
import time
import sympy as s

started = time.perf_counter()
assertions = 0
def check(value):
    global assertions
    assertions += 1
    assert value

x0,x1,x2,x3,u,v=s.symbols('x0 x1 x2 x3 u v')
x=(x0,x1,x2,x3)
G=x0*v-x1*u
F=x2*u+x3*v
Q=x0*x2+x1*x3
check(s.expand(u*Q-(x0*F-x3*G)) == 0)
check(s.expand(v*Q-(x1*F+x2*G)) == 0)
check(tuple(s.diff(Q,z) for z in x) == (x2,x3,x0,x1))
check(s.expand(Q.subs({x0:0,x1:0})) == 0)
images=[x0*z for z in x]+[x1*z for z in x]
monomials=[x0*x0,x0*x1,x0*x2,x0*x3,x1*x1,x1*x2,x1*x3]
M=s.Matrix([[s.Poly(f,*x).coeff_monomial(z) for f in images]
            for z in monomials])
check(M.rank()==7)
kernel=M.nullspace()
check(len(kernel)==1)
check(kernel[0]==s.Matrix([0,-1,0,0,1,0,0,0]))
check(all(s.expand(f.subs({x0:0,x1:0}))==0 for f in images))

def norm(point,p):
    first=next(z for z in point if z%p)
    inv=pow(first,-1,p)
    return tuple(z*inv%p for z in point)

def projective(dim,p):
    return [tuple([0]*i+[1]+list(tail))
            for i in range(dim+1)
            for tail in itertools.product(range(p),repeat=dim-i)]

fields=[]
for p in (2,3,5):
    P3=projective(3,p); P1=projective(1,p)
    qpoints=[a for a in P3 if (a[0]*a[2]+a[1]*a[3])%p==0]
    line=[a for a in P3 if a[0]==a[1]==0]
    check(len(qpoints)==(p+1)**2)
    check(len(line)==p+1)
    segre=set()
    incidence_count=0
    qlift_count=0
    for a in P3:
        lifts=[]; qlifts=[]
        for z in P1:
            seg=norm(tuple(ai*zj for ai in a for zj in z),p)
            check(seg not in segre)
            segre.add(seg)
            g=(a[0]*z[1]-a[1]*z[0])%p
            f=(a[2]*z[0]+a[3]*z[1])%p
            if g==0:
                lifts.append(z); incidence_count+=1
                if f==0:
                    qlifts.append(z); qlift_count+=1
        check(len(lifts)==(p+1 if a in line else 1))
        check(len(qlifts)==(1 if a in qpoints else 0))
        if a in qpoints:
            expected=norm((a[0],a[1]),p) if a not in line else norm((-a[3],a[2]),p)
            check(qlifts==[expected])
            check(any(z%p for z in (a[2],a[3],a[0],a[1])))
    check(qlift_count==len(qpoints))
    check(incidence_count==len(P3)+p*len(line))
    fields.append({'p':p,'P3_points':len(P3),'line_points':len(line),
                   'quadric_points':len(qpoints),'quadric_lift_points':qlift_count,
                   'blowup_points':incidence_count})

result={'id':'D:Chow-surface-boundary-obstruction','version':1,
        'status':'PASS','assertions':assertions,'fields':fields,
        'runtime_seconds':time.perf_counter()-started,
        'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact Z-polynomial checks and finite-field incidence checks; no fundamental-group counterexample asserted.'}
print(json.dumps(result,indent=2))

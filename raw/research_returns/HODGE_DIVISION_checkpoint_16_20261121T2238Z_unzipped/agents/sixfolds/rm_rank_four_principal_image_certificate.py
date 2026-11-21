#!/usr/bin/env python3
"""Exact witness supplement for E840; universal filtered proof is separate."""
from pathlib import Path
from itertools import product, combinations
from hashlib import sha256
from datetime import datetime, timezone
import json
import time
import sympy as s

start=time.perf_counter();here=Path(__file__).resolve().parent
a,b=s.symbols('a b');x,y,z,w=s.symbols('x y z w')
variables=(x,y,z,w);zero=(0,0,0,0)
basis=sorted(product(range(2),repeat=4),key=lambda e:(sum(e),e))
index={e:i for i,e in enumerate(basis)}
pairs=list(combinations(range(4),2))

def reduce_monomial(e):
    e=list(e);coefficient=1
    while e[0]>=2:
        e[0]-=2;e[1]+=1;e[3]+=1;coefficient=-coefficient
    if any(t>=2 for t in e[1:]):return None,0
    return tuple(e),coefficient

def clean(P):return {e:s.expand(c) for e,c in P.items() if s.expand(c)!=0}
def add(*P):
    out={}
    for item in P:
        for e,c in item.items():out[e]=out.get(e,0)+c
    return clean(out)
def scale(P,c):return clean({e:c*v for e,v in P.items()})
def mul(P,Q):
    out={}
    for ep,cp in P.items():
        for eq,cq in Q.items():
            e,c=reduce_monomial(tuple(ep[i]+eq[i] for i in range(4)))
            if c:out[e]=out.get(e,0)+c*cp*cq
    return clean(out)
def raw(poly):return {tuple(e):c for e,c in s.Poly(s.expand(poly),*variables).terms()}
def reduced(poly):
    out={}
    for e,c in raw(poly).items():
        ee,cc=reduce_monomial(e)
        if cc:out[ee]=out.get(ee,0)+c*cc
    return clean(out)

units=[{e:1} for e in basis]
associativity=0
for P in units:
    for Q in units:
        for R in units:
            assert mul(mul(P,Q),R)==mul(P,mul(Q,R))
            associativity+=1
hilbert=[sum(sum(e)==d for e in basis) for d in range(5)]
assert hilbert==[1,4,6,4,1]
top={(1,1,1,1):1}
assert len(basis)==16 and top in units

J=s.Matrix([[1,0,1,0],[0,1,0,1],[0,1,0,-1],[-1,0,1,0]])
assert J.det()==4
def wedge_vectors(u,v):return s.Matrix([u[i]*v[j]-u[j]*v[i] for i,j in pairs])
p=wedge_vectors(J[:,0],J[:,1]);q=wedge_vectors(J[:,2],J[:,3])
assert p==s.Matrix([1,1,0,0,1,1]) and q==s.Matrix([1,-1,0,0,-1,1])
def scalar_wedge(p,q):return p[0]*q[5]-p[1]*q[4]+p[2]*q[3]+p[5]*q[0]-p[4]*q[1]+p[3]*q[2]
assert scalar_wedge(p,p)==scalar_wedge(q,q)==0 and scalar_wedge(p,q)==4

F=[x*x+y*w,y*y,z*z,w*w]
def bracket(f,g,P):
    out={}
    for coefficient,(i,j) in zip(P,pairs):
        out=add(out,scale(reduced(s.diff(f,variables[i])*s.diff(g,variables[j])-s.diff(f,variables[j])*s.diff(g,variables[i])),coefficient))
    return out
Bp=[bracket(F[i],F[j],p) for i,j in pairs]
Bq=[bracket(F[i],F[j],q) for i,j in pairs]
expected=[4*(a+b)*x*y,4*(a-b)*x*z-2*(a+b)*y*z,0,0,4*(a-b)*y*w,4*(a+b)*z*w]
pencil=[add(scale(P,a),scale(Q,b)) for P,Q in zip(Bp,Bq)]
assert pencil==[reduced(t) for t in expected]
cross_checks=0
for i in range(6):
    for j in range(6):
        assert mul(Bp[i],Bq[j])==mul(Bq[i],Bp[j])
        cross_checks+=1
def polynomial_wedge(P,Q):
    return add(mul(P[0],Q[5]),scale(mul(P[1],Q[4]),-1),mul(P[2],Q[3]),mul(P[5],Q[0]),scale(mul(P[4],Q[1]),-1),mul(P[3],Q[2]))
assert polynomial_wedge(Bp,Bp)=={} and polynomial_wedge(Bq,Bq)=={}
assert polynomial_wedge(Bp,Bq)==scale(top,64)
jac=s.Matrix([[s.diff(f,v) for v in variables] for f in F]).det()
assert reduced(jac)==scale(top,16)

W=[tuple(int(k in ij) for k in range(4)) for ij in pairs]
M=s.Matrix([[P.get(e,0) for P in pencil] for e in W])
assert M.det()==0
five_minors=0
for rows in combinations(range(6),5):
    for cols in combinations(range(6),5):
        assert M.extract(rows,cols).det()==0
        five_minors+=1
four=s.factor(M.extract([0,1,4,5],[0,1,4,5]).det())
assert four==256*(a-b)**2*(a+b)**2
assert M.subs({a:1,b:0}).rank()==M.subs({a:0,b:1}).rank()==4
assert M.subs({a:1,b:1}).rank()==3 and M.subs({a:1,b:-1}).rank()==2

# Quotient W/J is represented by the xw coefficient and xz+2yz.
Qplus=s.Matrix([[0,0,1,0,0,0],[0,1,0,2,0,0]])
assert Qplus*M.subs({a:1,b:0})==s.zeros(2,6)
linear=[reduced(v) for v in variables]
blocks=[]
for v in linear:
    multiplication=s.Matrix([[mul(v,l).get(e,0) for l in linear] for e in W])
    blocks.append(Qplus*multiplication)
K=s.Matrix.vstack(*blocks)
assert K.rank()==4 and K.nullspace()==[]
nonzero_minor=None
for rows in combinations(range(8),4):
    d=K.extract(rows,range(4)).det()
    if d:
        nonzero_minor={'rows':list(rows),'determinant':str(d)};break
assert nonzero_minor

alpha,beta,gamma,delta=s.symbols('alpha beta gamma delta')
relation=s.Matrix([[2*alpha,0,0,0],[0,2*beta,0,alpha],[0,0,2*gamma,0],[0,alpha,0,2*delta]])
assert relation.extract([0,1],[0,3]).det()==2*alpha**2
assert relation.subs(alpha,0)==s.diag(0,2*beta,2*gamma,2*delta)

proof=here/'rm_rank_four_principal_image_draft.md'
out={'status':'PASS','completed_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,
     'proof_sha256':sha256(proof.read_bytes()).hexdigest(),'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'associativity_triples':associativity,'hilbert_function':hilbert,'coordinate_determinant':4,
     'p':[int(t) for t in p],'q':[int(t) for t in q],'constant_mixed_wedge':4,
     'full_pencil_matrix':[[str(t) for t in row] for row in M.tolist()],
     'scalar_cross_minors_zero':cross_checks,'five_minors_zero':five_minors,
     'four_minor':str(four),'mixed_bracket_wedge':'64xyzw','jacobian_socle':'16xyzw',
     'common_linear_kernel_matrix':[[str(t) for t in row] for row in K.tolist()],
     'common_linear_kernel_dimension':0,'nonzero_kernel_test_minor':nonzero_minor,
     'rank_one_relation_minor':'2alpha^2','pure_endpoint_bracket_kernel_dimensions':[2,2],
     'actual_extension_dimension':'96m^2',
     'scope':'Exact finite quotient/witness and scalar-minor checks only; universal filtered equality and geometric module-lifting claims are proofs in the separate draft.'}
(here/'rm_rank_four_principal_image_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

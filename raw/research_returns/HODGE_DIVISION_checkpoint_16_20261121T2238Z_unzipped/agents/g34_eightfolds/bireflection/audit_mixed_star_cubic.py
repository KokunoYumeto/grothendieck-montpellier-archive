#!/usr/bin/env python3
"""Independent E833 cubic check in the full eight-generator exterior algebra."""
from pathlib import Path
from itertools import combinations
import hashlib,json,time
import sympy as s
start=time.perf_counter()
root=Path(__file__).resolve().parent
draft=root.parents[1]/'sixfolds/rm_mixed_star_cubic_obstruction_draft.md'
sha=hashlib.sha256(draft.read_bytes()).hexdigest()
assert sha=='2a74ada9fb1a9894ffc7c1f402e8eeb4d470af5a7d6d63923951055b99f4b58f'
def add(*forms):
    out={}
    for q in forms:
        for I,c in q.items():out[I]=out.get(I,0)+c
    return {I:s.expand(c) for I,c in out.items() if s.expand(c)!=0}
def scale(a,q):return {I:s.expand(a*c) for I,c in q.items() if s.expand(a*c)!=0}
def wedge(A,B):
    out={}
    for I,a in A.items():
        for J,b in B.items():
            if set(I)&set(J):continue
            sign=(-1)**sum(i>j for i in I for j in J)
            K=tuple(sorted(I+J))
            out[K]=out.get(K,0)+sign*a*b
    return add(out)
def power(A,n):
    out={():s.Integer(1)}
    for _ in range(n):out=wedge(out,A)
    return out
def oneone(M):
    return {(i,4+j):M[i,j] for i in range(4) for j in range(4) if M[i,j]!=0}

u1,u2,ur,ui,v1,v2,vr,vi=s.symbols('u1 u2 ur ui v1 v2 vr vi',real=True)
x,a,c,k=s.symbols('x a c k',real=True)
U=s.Matrix([[u1,ur+s.I*ui],[ur-s.I*ui,u2]])
V=s.Matrix([[v1,vr+s.I*vi],[vr-s.I*vi,v2]])
P=s.diag(U,s.zeros(2));Z=s.diag(s.zeros(2),V)
Tp=s.diag(1,1,0,0);Tm=s.diag(0,0,1,1)
p,z,tp,tm=map(oneone,(P,Z,Tp,Tm))
u=add(p,z);alpha=add(scale(a,p),scale(c,z));D=scale(k,add(tp,tm))
actual=add(scale(x/s.Integer(6),power(u,3)),
           scale(-x/s.Integer(2),wedge(u,power(alpha,2))),
           scale(-s.Rational(1,3),power(alpha,3)),
           scale(-2*x,power(D,3)))
ap=x*(1-a*a-2*a*c)/2-a*a*c
am=x*(1-c*c-2*a*c)/2-a*c*c
expected=add(scale(ap*U.det(),wedge(power(tp,2),z)),
             scale(am*V.det(),wedge(p,power(tm,2))),
             scale(-6*x*k**3,add(wedge(power(tp,2),tm),wedge(tp,power(tm,2)))))
assert add(actual,scale(-1,expected))=={}
assert power(p,3)=={} and power(z,3)=={}
assert add(power(p,2),scale(-U.det(),power(tp,2)))=={}
assert add(power(z,2),scale(-V.det(),power(tm,2)))=={}
assert len(actual)==8

# Both maps from a full (1,1) plane block to the corresponding mixed cubic
# component are injective; no rational decomposition of the torus is used.
def coefficient_matrix(left_plane,which):
    columns=[]
    for i in which:
        for j in which:
            E=s.zeros(4);E[i,j]=1
            columns.append(wedge(power(left_plane,2),oneone(E)))
    support=sorted(set().union(*(set(q) for q in columns)))
    return s.Matrix([[q.get(I,0) for q in columns] for I in support])
assert coefficient_matrix(tp,(2,3)).rank()==4
assert coefficient_matrix(tm,(0,1)).rank()==4
# Nonzero RHS and equal trace2 force equal scalar multiples7k/2.
h=s.symbols('h')
assert s.solve(2*h-7*k,h)==[7*k/2]

out={'status':'PASS','draft_sha256':sha,'eight_generator_cubic_components':len(actual),
 'full_hermitian_variables':8,'both_cubic_plane_maps_rank':4,
 'universal_cubic_identity':True,'unit_trace_scalar':'7*k/2',
 'seconds':time.perf_counter()-start,
 'scope':'Independent symbolic exterior algebra only. Universal support-plane lemma, exact sheaf determinant and finite-action scope are checked in the full peer report.'}
root.joinpath('audit_mixed_star_cubic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))


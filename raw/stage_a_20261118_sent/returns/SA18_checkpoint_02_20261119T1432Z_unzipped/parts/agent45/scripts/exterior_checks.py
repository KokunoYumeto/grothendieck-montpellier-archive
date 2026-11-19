"""Integral coefficient checks for the manuscript's exterior conventions.

Finite checks supplement the stated arbitrary-rank shuffle proof; they are not
presented as proof by numerical sampling.
"""
from itertools import combinations
import json
import sympy as sp
def subsets(n): return [s for p in range(n+1) for s in combinations(range(n),p)]
def wedge(a,b):
    if set(a)&set(b):return None,0
    return tuple(sorted(a+b)),(-1)**sum(x>y for x in a for y in b)
def rc(u,t):
    if not set(t)<=set(u):return None,0
    k=tuple(x for x in u if x not in t)
    return k,wedge(t,k)[1]
def lc(u,s):
    if not set(u)<=set(s):return None,0
    k=tuple(x for x in s if x not in u)
    return k,wedge(k,u)[1]
checks=[]
for n in range(7):
    bs=subsets(n);n31=n37=0
    for u in bs:
      for s in bs:
       for t in bs:
        st,a=wedge(s,t);left,lc1=rc(u,st) if a else (None,0)
        us,b=rc(u,s);right,rc1=rc(us,t) if b else (None,0)
        L=(left,a*lc1) if a*lc1 else (None,0)
        R=(right,b*rc1) if b*rc1 else (None,0)
        assert L==R,(n,u,s,t,L,R)
        n31+=1
        uv,a=wedge(u,s);left,l=lc(uv,t) if a else (None,0)
        vs,b=lc(s,t);right,r=lc(u,vs) if b else (None,0)
        L=(left,a*l) if a*l else (None,0);R=(right,b*r) if b*r else (None,0)
        assert L==R,(n,u,s,t,L,R)
        n37+=1
    checks.append({'rank':n,'equation31_basis_triples':n31,'equation37_basis_triples':n37,'failures':0})
N=3;bs=subsets(N);F=sp.Matrix(N,N,sp.symbols('f0:9'))
def minor(rows,cols):
    return sp.Integer(0) if len(rows)!=len(cols) else sp.Integer(1) if not rows else F.extract(rows,cols).det()
n32=0
for U in bs:
 for T in bs:
  for Z in bs:
   if len(U)!=len(T)+len(Z):continue
   # Pair both sides of equation (32) with Z, using all symbolic minors.
   lhs=sum(minor(K,Z)*minor(H,T)*rc(U,H)[1] for H in bs if len(H)==len(T) and set(H)<=set(U) for K in [tuple(x for x in U if x not in H)])
   TZ,sg=wedge(T,Z);rhs=sg*minor(U,TZ) if sg else 0
   assert sp.expand(lhs-rhs)==0,(U,T,Z)
   n32+=1
# Universal polynomial minors, for all exterior degrees of a 4 by 4 matrix.
X=sp.Matrix(4,4,sp.symbols('x0:16'))
def wedge_linear(poly,vector):
    ans={}
    for I,a in poly.items():
     for j,b in enumerate(vector):
      J,sg=wedge(I,(j,))
      if sg:ans[J]=ans.get(J,0)+sg*a*b
    return {k:sp.expand(v) for k,v in ans.items()}
minorchecks=0
for p in range(5):
 for cols in combinations(range(4),p):
  poly={():sp.Integer(1)}
  for j in cols:poly=wedge_linear(poly,list(X[:,j]))
  for rows in combinations(range(4),p):
   expected=X.extract(rows,cols).det() if p else 1
   assert sp.expand(poly.get(rows,0)-expected)==0
   minorchecks+=1
print(json.dumps({'integer_basis_checks':checks,'equation32_symbolic_checks':n32,'minors_symbolic_checks':minorchecks,'all_failures':0,'universal_proof':'For each disjoint ordered partition, both compositions have the sign of the same concatenation permutation. This proves (31), (34), (36), and (37) in every rank over Z, hence by base change over any commutative ring. Equation (32) follows by pairing and exterior functoriality; its symbolic check verifies the conventions. Equation (33) is the same equality with an invertible map. Minors are the coefficients in the universal alternating expansion; the degree-4 polynomial certificate checks all row/column choices.','scope':'Right contraction on the graded dual needs no finite-projectivity assumption. Uniqueness of a vector from its dual pairings does require separation by duals, and can fail for torsion modules.'},indent=2))

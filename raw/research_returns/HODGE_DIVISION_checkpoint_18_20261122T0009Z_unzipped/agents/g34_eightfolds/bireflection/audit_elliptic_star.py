#!/usr/bin/env python3
"""Independent exact identities supplementing the whole E832 proof audit."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import hashlib,json,time
import sympy as s

started=time.perf_counter()
base=Path(__file__).resolve().parent
proof=base.parents[1]/'sixfolds/rm_elliptic_star_character_obstruction_draft.md'
digest=hashlib.sha256(proof.read_bytes()).hexdigest()
assert digest=='0542dce98bcf06689930578a262dd242b43cfbc0a3f2aebaec263222b38d01ad'

# Direct finite convolution, rather than symbolic differentiation of exponentials.
unit=[sum(F(c)*F(a)**k/F(s.factorial(k)) for c,a in ((2,-1),(-2,-3),(1,-4))) for k in range(5)]
assert unit==[F(1),F(0),F(0),F(-2),F(4)]
r,m,x,u,q,T=s.symbols('r m x u q T', nonzero=True)
H=-r*u-m*x
ch2=r*u*u/2+m*x*x/2+x*H
balanced=-q*(r+m)*T/2
completed=(x+r*u/m)**2-r*(r+m)*u*u/(m*m)-q*(r+m)*T/m
assert s.expand(completed+2*(ch2-balanced)/m)==0

# All edge sets from the six possible pair products; classify by degree sequence.
edges=list(combinations(range(4),2))
classification=[]
for chosen in combinations(edges,4):
    reach={0}
    for _ in range(4):
        reach |= {v for e in chosen if set(e)&reach for v in e}
    assert len(reach)==4
    degrees=sorted(sum(v in edge for edge in chosen) for v in range(4))
    triangles=sum(all(e in chosen for e in combinations(tri,2)) for tri in combinations(range(4),3))
    assert triangles==1 or (triangles==0 and degrees==[2,2,2,2])
    classification.append(triangles)
assert classification.count(1)==12 and classification.count(0)==3

# Generic block compound and tensor product, without assuming either block diagonal.
a,b,c,d,e,f,g,h=s.symbols('a b c d e f g h')
U=s.Matrix([[a,b],[c,d]])
V=s.Matrix([[e,f],[g,h]])
M=s.diag(U,V)
compound=s.Matrix([[M.extract(I,J).det() for J in edges] for I in edges])
mixed=[1,2,3,4]
assert compound.extract(mixed,mixed)==s.kronecker_product(U,V)
assert compound[0,0]==U.det() and compound[5,5]==V.det()
assert all(compound[i,j]==0 for i in (0,5) for j in mixed)
assert all(compound[i,j]==0 for j in (0,5) for i in mixed)
t,k,du,dv=s.symbols('t k du dv',positive=True)
P=(t*t-k)*du*(k*k/(t*t)-k)*dv
assert s.factor(P+du*dv*k*(k-t*t)**2/(t*t))==0

# The printed boundary example, by direct six pair products.
u0=[1,1,2,-2];b0=[2,2,1,-1]
boundary=[b0[i]*b0[j]-u0[i]*u0[j] for i,j in edges]
assert boundary==[3,0,0,0,0,3]
assert [k*(k-1)//2 for k in range(5)]==[0,0,1,3,6]
assert [a*b+2 for a,b in ((1,1),(1,2),(2,1))]==[3,4,4]

out={'status':'PASS','proof_sha256':digest,'unit_coefficients':[str(z) for z in unit],
 'completed_square':True,'four_edge_graphs':len(classification),'triangle_graphs':12,
 'four_cycles':3,'generic_block_compound':True,'sign_product':str(s.factor(P)),
 'boundary_difference':boundary,'seconds':time.perf_counter()-started,
 'scope':'Exact algebra only; the universal positivity proof and actual E825 interface were checked by whole-proof reading.'}
base.joinpath('audit_elliptic_star.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

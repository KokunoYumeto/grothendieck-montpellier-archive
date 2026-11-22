"""Exact checks for the one-axis supersingular-product determinant cube.

The universal conclusion is proved by exterior-square covariance and the
universal unit Schur complement.  A full nine-variable determinant at the
explicit point (a,b)=(0,0) is a separate reconstructive check.  No global
monodromy or indecomposable-surface conclusion is inferred.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import permutations
import hashlib
import json
import time
import sympy as sp
from sympy.polys.matrices import DomainMatrix

start=time.perf_counter()
checks=[]
a,b,r,s,t=sp.symbols('a b r s t')
relation=sp.groebner([b*b+b+a**3],b,a,modulus=2)
def mod2(expr, variables):
    return sp.Poly(sp.expand(expr), *variables, modulus=2).as_expr()
def zero(expr,variables,label):
    assert mod2(expr,variables)==0,label
    checks.append(label)
A0=sp.Matrix([[1,a,0],[a,0,b],[0,b+1,a]])
R=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
A2=sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])
A=[A0,R,A2]
B=[sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
   sp.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
   sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])]
elliptic=sp.Poly(sp.expand((r*A0+s*R+t*A2).det()-(r*r*t+r*t*t+s**3)),r,s,t)
for _,coefficient in elliptic.terms():
    assert relation.reduce(sp.expand(coefficient))[1]==0
checks.append('universal elliptic determinant and smooth cubic')
F=r*r*t+r*t*t+s**3
assert [mod2(sp.diff(F,x),(r,s,t)) for x in (r,s,t)]==[t*t,s*s,r*r]

schur=A0*R*A2+A2*R*A0
expected=sp.Matrix([[0,1,a],[1,0,0],[a,0,1]])
for v in schur-expected: zero(v,(a,b),'unit Schur entry')
zero(expected.det()-1,(a,b),'universal Schur determinant one')

hs=sp.symbols('h00 h01 h02 h10 h11 h12 h20 h21 h22')
H=sp.Matrix(3,3,hs)
pair=[(0,1),(0,2),(1,2)]
S=sp.zeros(3)
for j in range(3):
    transformed=H.T*B[j]*H
    for k,(u,v) in enumerate(pair): S[k,j]=transformed[u,v]
    reconstructed=sum((S[k,j]*B[k] for k in range(3)),sp.zeros(3))
    for entry in transformed-reconstructed: zero(entry,hs,'exterior-square entry covariance')
zero(S.det()-H.det()**2,hs,'exterior-square determinant')

xs=sp.symbols('x00 x01 x02 x10 x11 x12 x20 x21 x22')
X=sp.Matrix(3,3,xs)
Ai=[m.subs({a:0,b:0}) for m in A]
mat=sum((xs[3*i+j]*sp.kronecker_product(Ai[i],B[j])
         for i in range(3) for j in range(3)),sp.zeros(9))
domain=sp.GF(2).poly_ring(*xs)
det=DomainMatrix.from_Matrix(mat).convert_to(domain).det()
expr=domain.to_sympy(det)
zero(expr-X.det()**3,xs,'full nine-variable determinant is the cube at (a,b)=(0,0)')
terms=sp.Poly(expr,*xs,modulus=2).terms()
assert len(terms)==36

# Independent binary reconstruction of the proposed determinant cube.
cubic=[]
for perm in permutations(range(3)):
    row=[0]*9
    for i,j in enumerate(perm):row[3*i+j]+=1
    cubic.append(tuple(row))
binary_cube=set()
for u in cubic:
    for v in cubic:
        term=tuple(x+2*y for x,y in zip(u,v))
        if term in binary_cube:binary_cube.remove(term)
        else:binary_cube.add(term)
assert binary_cube=={tuple(m) for m,c in terms if int(c)%2}
checks.append('independent binary 36-term cube reconstruction')

# Rank-two normal form has rank six whenever its first coefficient is a unit.
us=sp.symbols('u00 u01 u02 u10 u11 u12 u20 u21 u22')
vs=sp.symbols('v00 v01 v02 v10 v11 v12 v20 v21 v22')
U=sp.Matrix(3,3,us);V=sp.Matrix(3,3,vs);Z=sp.zeros(3)
C=sp.BlockMatrix([[Z,U,V],[U,Z,Z],[V,Z,Z]]).as_explicit()
kernel=sp.BlockMatrix([[Z],[U.adjugate()*V],[U.det()*sp.eye(3)]]).as_explicit()
for entry in C*kernel:zero(entry,us+vs,'rank-three explicit kernel on det(U) nonzero')
minor=C[:6,:6].det()
zero(minor-U.det()**2,us,'nonzero six-minor')

output={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-start,
        'checks':checks,'check_count':len(checks),
        'full_determinant_terms':[[list(m),int(c)%2] for m,c in terms],
        'full_determinant_term_count':len(terms),
        'uniform_formula':'det(C(X))=det(X)^3',
        'rank_two_coefficient_matrix_cross_rank':6,
        'scope':'Uniformity uses the written exterior-square covariance proof and the universal unit Schur complement. The explicit full expansion is at one nontrivial elliptic twist. No inference about indecomposable ppav determinants, twisted-cycle stable rank, or full monodromy.',
        'prior_failure':'post_CP34_product_twisted_determinant_probe.py computed the same 36-term determinant, then SymPy multivariate gcd raised PolynomialDivisionFailed. Exact failed source/output/log retained in notes/CP35_product_determinant_gcd_failure.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k not in ('checks','full_determinant_terms')},indent=2))

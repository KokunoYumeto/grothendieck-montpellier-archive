"""Exact finite and cubic algebraic endpoint certificate for R045."""
from pathlib import Path
import json
import sympy as s
HERE=Path(__file__).resolve().parent
a,n=s.symbols('a n')
C=s.Matrix([[s.sympify(x,locals={'a':a}) for x in row]
            for row in json.loads((HERE/'DOUBLE_FOUR_MOMENT_MATRIX.json').read_text())['matrix']])
u=n*(n-1)/((n-2)*(n-3));v=n*(n-1)/(n-2)**2
H=s.Matrix([[1,0,0,0],[8*u,-6*u,0,0],[0,0,-4*v,0],
            [24*u*u,-36*u*u,0,36*u*u]])
assert s.factor(H.det()-864*u**3*v)==0
relations={3:[[-s.Rational(4,3),1,0,0],[s.Rational(2,3),0,1,0],[-s.Rational(2,3),0,0,1]],
 4:[[-2,2,1,0],[0,-s.Rational(1,2),0,1]],
 5:[[s.Rational(4,5),-s.Rational(13,10),-s.Rational(2,5),1]]}
rank_rows=[]
for aa,rels in relations.items():
    T=C.subs(a,aa)
    for row in rels:assert s.Matrix([row])*T==s.zeros(1,4)
    assert T.rank()==aa-2
    rank_rows.append(dict(a=aa,rank=aa-2,left_kernel=[[str(x) for x in row] for row in rels]))
expected={(3,4):s.Integer(16),(3,5):s.Rational(320,27),(4,4):-s.Rational(27,4),
          (4,5):-s.Rational(110,27),(5,5):-s.Rational(32768,28125)}
minors=[]
for (aa,nn),want in expected.items():
    P=C.subs(a,aa)*H.subs(n,nn)*C.subs(a,nn);r=aa-2
    value=s.factor(P[:r,:r].det())
    assert value==want and P.rank()==r
    minors.append(dict(a=aa,n=nn,size=r,minor=str(value)))
J=s.Matrix([[2,0,a,0]])
K=s.Matrix([[2*(a-2)*(a*a-3*a+6),-2*a*(a*a-3*a+3),0,a*a*(a-1)]])
jrow=s.simplify(J*C);krow=s.simplify(K*C)
assert jrow==s.Matrix([[2*(a-3),0,a-3,0]])
assert s.simplify(krow-s.Matrix([[2*(a-3)*(a**3-9*a*a+24*a-12),0,4*(a-3)**2,0]]))==s.zeros(1,4)
minor=s.factor(C[:2,[1,3]].det())
assert minor==(a-4)*(a-3)*(a-1)/(2*a**4)
for aa,factor in [(4,4),(5,8)]:
    assert (K.subs(a,aa)-factor*J.subs(a,aa))*C.subs(a,aa)==s.zeros(1,4)
data=dict(status='PASS',finite_relations=rank_rows,canonical_minors=minors,
          split_determinant=str(s.factor(H.det())),cubic_forbidden_minor=str(minor),
          J_row=[str(s.factor(x)) for x in jrow],
          K_row=[str(s.factor(x)) for x in krow])
(HERE/'DOUBLE_FOUR_ENDPOINT_CERTIFICATE.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS full finite endpoint, split determinant and cubic identities',flush=True)


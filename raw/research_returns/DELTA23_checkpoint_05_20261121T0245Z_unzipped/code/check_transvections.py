"""Exact integral certificates for D23.T1--T2; no numerical approximation."""
import json
from pathlib import Path
import sympy as s

J=s.zeros(4)
for i in range(3):
    J[i,i+1]=1
    J[i+1,i]=-1
I=s.eye(4)
e=[I[:,i] for i in range(4)]
T=[I+v*v.T*J for v in e]
assert J.det()==1
for t in T:
    assert t.T*J*t==J
for i in range(3):
    assert T[i]*T[i+1]*T[i]==T[i+1]*T[i]*T[i+1]
for i in range(4):
    for j in range(i+2,4):
        assert T[i]*T[j]==T[j]*T[i]
C=T[0]*T[1]*T[2]*T[3]
assert C**5==-I
cyclic=s.Matrix.hstack(e[0],C*e[0],C**2*e[0],C**3*e[0])
assert abs(cyclic.det())==1
x=s.Symbol('x')
assert C.charpoly(x).as_expr()==x**4-x**3+x**2-x+1
v=s.Matrix(s.symbols('v0:4')); w=s.Matrix(s.symbols('w0:4'))
c=(v.T*J*w)[0]
tv=I+v*v.T*J; tw=I+w*w.T*J
assert all(s.expand(a)==0 for a in tv*tw-tw*tv-c*(v*w.T+w*v.T)*J)
assert all(s.expand(a)==0 for a in tv*tw*tv-tw*tv*tw-(1-c*c)*(v*v.T-w*w.T)*J)
out={'J':J.tolist(),'C':C.tolist(),'cyclic_basis':cyclic.tolist(),
     'charpoly':str(C.charpoly(x).as_expr()),'C_power_5':(-I).tolist(),
     'rank_one_identities':'PASS','braid_relations':'PASS',
     'scope':'Exact polynomial and integral matrix assertions only; conceptual proof is in D23.T1--T2.'}
print(json.dumps(out,default=str,indent=2))
Path('work/records/transvection_certificate.json').write_text(json.dumps(out,default=str,indent=2)+'\n')

"""Exact normalizations for the F63 simple-effectivity classification.

The all-j positive-root proof is mathematical, not a finite computation here.
"""
import sympy as s

v,D,m,b=s.symbols('v D m b', nonzero=True)
A=[s.Integer(1),s.Integer(1)]
for j in range(2,6):
    A.append(s.expand(2*A[-1]-D*A[-2]))
assert A == [1,1,2-D,4-3*D,D**2-8*D+8,5*D**2-20*D+16]
Dv=(v+v**-1)**2
expected={1:1,2:v**2+v**-2,3:3*v**2+2+3*v**-2,
          5:5*v**4+6+5*v**-4}
sign={1:1,2:-1,3:-1,5:1}
for j,e in expected.items():
    assert s.expand(sign[j]*A[j].subs(D,Dv)-e)==0
    assert all(t/v**int(t.as_powers_dict().get(v,0))>0
               for t in s.Add.make_args(s.expand(e)))
P1=s.Matrix([[m,b*b],[0,0]])
P2=s.Matrix([[0,0],[1,m]])
S=s.diag(b,1)
assert S.inv()*P1*S==s.Matrix([[m,b],[0,0]])
assert S.inv()*P2*S==s.Matrix([[0,0],[b,m]])
assert s.trace(P1*P2)==b*b
print('PASS: A_j recurrence throughj5 and the four exact effective choices')
print('PASS: source-column balancing and Tr(P1 P2)=b^2')
print('All-j exclusion is proved by SE8-SE11, not by a finite test.')

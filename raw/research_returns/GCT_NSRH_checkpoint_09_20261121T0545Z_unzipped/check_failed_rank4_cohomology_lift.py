"""Exact obstruction to one zero-differential sign-to-degree proposal.

This is a failed candidate check, not a general categorification theorem.
At z=-1 the matrices recover the actual Figure22 Q matrices of F57.
"""
import sympy as s
x,z=s.symbols('x z'); D=x*x; a=D+2*z; c=D+4*z
Q1=s.Matrix([[0,z*x,c,0,0],[0,D,0,0,0],[0,0,D,0,0],[0,0,a,0,0],[0,z*x,0,0,0]])
Q2=s.Matrix([[D,0,0,0,0],[z*x,0,0,0,0],[0,0,0,a,0],[0,0,0,D,0],[a,0,0,z*a,0]])
Q3=s.Matrix([[0,z*x,0,0,c],[0,D,0,0,0],[0,z*x,0,0,0],[0,z*x,0,0,2*z],[0,0,0,0,D]])
for i,Q in enumerate([Q1,Q2,Q3],1):
    assert all(s.expand(t)==0 for t in Q*Q-D*Q)
    print('quadratic',i,'PASS for all z')
assert all(s.expand(t)==0 for t in Q1*Q3-Q3*Q1)
print('far commutation PASS for all z')
for i,(A,B) in enumerate([(Q1,Q2),(Q2,Q3)],1):
    relation=A*B*A*B*A-B*A*B*A*B-(D+a*a)*(A*B*A-B*A*B)+D*a*a*(A-B)
    assert all(s.expand(t.subs(z,-1))==0 for t in relation)
    witness=s.factor(relation[0,0])
    assert witness!=0
    print('adjacent pair',i,i+1,'entry(1,1):',witness)
    print('Euler specialization z=-1: PASS; full cohomology relation: FAIL')

#!/usr/bin/env python3
"""Exact certificate for GCT IV Figure 22 and its Theta-op dual.

Right matrices: state row -> coefficient column. No floating arithmetic.
The matrix transcription is independent of the finite-search helper file.
"""
import hashlib
from pathlib import Path
import sympy as s

d,v=s.symbols('d v')
D=d*d
a,c=D-2,D-4
Q1=s.Matrix([[0,-d,c,0,0],[0,D,0,0,0],[0,0,D,0,0],
             [0,0,a,0,0],[0,-d,0,0,0]])
Q2=s.Matrix([[D,0,0,0,0],[-d,0,0,0,0],[0,0,0,a,0],
             [0,0,0,D,0],[a,0,0,-a,0]])
Q3=s.Matrix([[0,-d,0,0,c],[0,D,0,0,0],[0,-d,0,0,0],
             [0,-d,0,0,-2],[0,0,0,0,D]])
Q=[Q1,Q2,Q3]

def product(word,gens=Q):
    out=s.eye(5)
    for i in word:
        out=(out*gens[i-1]).applyfunc(s.expand)
    return out

word=(1,2,1,2,1,3,2,3,2,3,2)
M=product(word)
p=(-D**9+20*D**8-163*D**7+734*D**6-2048*D**5+
   3712*D**4-4352*D**3+3072*D**2-1024*D)
assert s.expand(s.trace(M)-p)==0
diag1=(D**10-20*D**9+180*D**8-951*D**7+3246*D**6
       -7440*D**5+11520*D**4-11712*D**3+7168*D**2-2048*D)
diag4=(-D**10+19*D**9-160*D**8+788*D**7-2512*D**6
       +5392*D**5-7808*D**4+7360*D**3-4096*D**2+1024*D)
assert all(s.expand(M[j,j]-x)==0
           for j,x in enumerate([diag1,0,0,diag4,0]))
print("Q-word:",word)
for j in range(5):
    print("Product diagonal",j+1,":",M[j,j])
print("Trace in delta:",s.expand(p))
print("All five stated product diagonal entries: PASS")

# Complete low-rank product reduction used in the proof.
u=s.Matrix([-2*d*a,D**2,-d*D,-d*a,-d*D])
e2=s.Matrix([[0,1,0,0,0]])
assert (Q1*Q3-u*e2).applyfunc(s.expand)==s.zeros(5)
tail=(2,3,2,3,2,1,2,1,2)
r=e2*product(tail)
r1=-d**5*(D**4-9*D**3+31*D**2-48*D+32)
r4=d*(D**7-16*D**6+109*D**5-418*D**4+
      992*D**3-1472*D**2+1280*D-512)
assert (r-s.Matrix([[r1,0,0,r4,0]])).applyfunc(s.expand)==s.zeros(1,5)
assert s.expand((r*u)[0]-p)==0
print("Rank-one factor Q1Q3=u e2^t: PASS")
print("Rotated tail row:",[s.expand(x) for x in r])

# Source # uses Theta-op. Therefore its P_i matrix is Q_i^t.
dualword=tuple(reversed(word))
dualM=product(dualword,[A.T for A in Q])
assert dualM==M.T
assert s.expand(s.trace(dualM)-p)==0
print("Theta-op-dual P-word:",dualword)
print("Dual word product equals original transpose: PASS")

lp=s.expand(p.subs(d,v+1/v))
coeff={k:int(s.expand(lp).coeff(v,k)) for k in range(-18,19)}
coeff={k:c for k,c in coeff.items() if c}
assert coeff[-18]==coeff[18]==-1
assert all(c>=0 for k,c in coeff.items() if abs(k)!=18)
assert s.expand(lp-sum(c*v**k for k,c in coeff.items()))==0
print("Exact Laurent coefficients:",coeff)
at3=s.factor(lp.subs(v,3))
assert at3==-s.Rational(99834597608550400,387420489)
print("Exact trace at v=3:",at3)
print("Exact trace at v=1:",lp.subs(v,1))

for i,A in enumerate(Q,1):
    assert (A*A-D*A).applyfunc(s.expand)==s.zeros(5)
assert (Q1*Q3-Q3*Q1).applyfunc(s.expand)==s.zeros(5)
for i,j in [(1,2),(2,3)]:
    lhs=product((i,j,i,j,i))-product((j,i,j,i,j))
    rhs=(D+a*a)*(product((i,j,i))-product((j,i,j)))\
        -D*a*a*(Q[i-1]-Q[j-1])
    assert (lhs-rhs).applyfunc(s.expand)==s.zeros(5)
print("Quadratic, far-commutation, adjacent degree-five identities: PASS")
print("All exact assertions: PASS")
print("Script SHA256:",hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

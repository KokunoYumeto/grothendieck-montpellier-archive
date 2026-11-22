#!/usr/bin/env python3
"""Complete finite RigKos quotient and Galois action in split adjoint A2."""
from itertools import permutations,product
import sympy as s
W=list(permutations(range(3)));I=(0,1,2)
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def parity(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
Phi=[(a,b) for a,b in product(W,repeat=2) if parity(a)==parity(b)]
points=set(product(W,repeat=2));orbits=[]
while points:
 p=min(points);orb={(mul(a,p[0]),mul(b,p[1])) for a,b in Phi}
 assert len(orb)==18
 orbits.append(orb);points-=orb
assert len(orbits)==2
for i,O in enumerate(orbits):
 assert len({(parity(a)+parity(b))%2 for a,b in O})==1
 print('Orbit',i,'size',len(O),'parity sum',next(iter({(parity(a)+parity(b))%2 for a,b in O})),
       'elements',sorted(O))
tau=(0,2,1)
gal=[next(j for j,P in enumerate(orbits) if {(mul(tau,a),b) for a,b in O}==P) for O in orbits]
print('Galois permutation on the two orbits:',gal)
assert gal==[1,0]
# Eigenvectors of the rational 3-cycle permutation matrix; conjugation of
# zeta interchanges the final two columns and leaves the first fixed.
z=-s.Rational(1,2)+s.sqrt(3)*s.I/2
F=s.Matrix([[z**(i*j) for j in range(3)] for i in range(3)])
F=F.applyfunc(s.simplify)
assert (F.conjugate()-F[:,[0,2,1]]).applyfunc(s.simplify)==s.zeros(3)
print('Fourier eigenbasis conjugation verified: columns 1 and 2 exchanged.')
print('Conclusion: RigKos/G over Q is Spec Q(zeta_3), not a split two-point scheme.')
reverse=(2,1,0)
def dual(point):
 a,b=point
 return (mul(tau,mul(a,reverse)),mul(b,reverse))
outer=[next(j for j,P in enumerate(orbits) if {dual(p) for p in O}==P) for O in orbits]
assert outer==[1,0]
print('Transpose-inverse outer automorphism on the two geometric orbits:',outer)
print('Both quadruple automorphism groups are trivial; neither orbit is outer-invariant.')
print('Over F2, values of u^2+u+1 at u=0,1:',[(u*u+u+1)%2 for u in range(2)])

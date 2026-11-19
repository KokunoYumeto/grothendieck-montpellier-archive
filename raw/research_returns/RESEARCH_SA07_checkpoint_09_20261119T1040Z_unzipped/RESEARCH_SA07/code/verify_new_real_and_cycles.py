#!/usr/bin/env python3
"""Exact checks for C.1.4--5, E.3.3, and F.1--2.

Inputs are symbolic positive real a,y and integer dimensions/codimensions.
The undecidability and spreading arguments are proofs in the paper; this
program does not approximate the halting real or certify any transcendence.
"""
from time import perf_counter
import sympy as s

start=perf_counter()
a,y=s.symbols('a y', positive=True)
ii=s.I
f=s.diag(1,-1)
C=s.Matrix([[0,1/a],[-a,0]])
E=s.Matrix([[0,-1],[1,0]])
v=s.Matrix([1,ii*a])
assert s.simplify(C*v-ii*v)==s.zeros(2,1)
assert E*C==s.diag(a,1/a)
assert f.T*E*f==-E
assert s.simplify(f*C*f-C.inv())==s.zeros(2)
assert f*v==s.conjugate(v)
print('C.1.4--5: Weil operator eigenvalue +i in type (3,0), positive Weil form, involution: PASS')
x=s.symbols('x')
poly=s.Poly(x**6+4,x,domain=s.QQ)
assert poly.is_irreducible
print('C.1.4: minimal polynomial of i*cuberoot(2) is x^6+4, irreducible over Q: PASS')

# E.3.3: positive diagonal determinant-one action sends iy to ia.
b=s.sqrt(y/a)
g=s.diag(b,1/b)
w=g*s.Matrix([1,ii*y])
assert s.simplify(w[1]/w[0]-ii*a)==0
assert s.simplify(g.det())==1
assert g*f==f*g
assert s.simplify(g.T*E*g-E)==s.zeros(2)
print('E.3.3: diag(sqrt(y/a),sqrt(a/y)) sends period ratio iy to ia and preserves E,f: PASS')
A=s.Matrix([[1,2],[3,5]])
Aprime=A*g.inv()
assert s.simplify(Aprime*w-A*s.Matrix([1,ii*y]))==s.zeros(2,1)
print('E.3.3: adjusted de Rham comparison alpha_prime=alpha*g^-1 preserves the fixed de Rham line: PASS')

# F.1.4: all parities, including the explicit codimension-two counterexample.
for p in range(1,7):
    assert s.simplify((-ii)**(-p)/ii**(-p)-(-1)**p)==0
assert (-1)**2==1
print('F.1.4: conjugation changes the codimension-p class by (-1)^p; P^2 point class has sign +1: PASS')
dx,dy,dz,r,t=s.symbols('d_X d_Y d_Z r s',integer=True)
assert s.expand((dx-r)+(dy-t)-(dx-(r+t-dy)))==0
print('F.1.3: correspondence scaling is compatible with composition, exponent d_X-r+d_Y-s: PASS')

# Weight-zero Q with twist n=-1 and graded index i=0.
i,n=0,-1
left_dim=int(i==(-2*n))
wrong_dim=int(i==0)
correct_dim=int((i+2*n)==0)
assert (left_dim,wrong_dim,correct_dim)==(0,1,0)
print('F.2.1: E=Q(0), n=-1, i=0: LHS dimension 0, unshifted RHS dimension 1, corrected RHS dimension 0: PASS')
print(f'Runtime seconds: {perf_counter()-start:.6f}')

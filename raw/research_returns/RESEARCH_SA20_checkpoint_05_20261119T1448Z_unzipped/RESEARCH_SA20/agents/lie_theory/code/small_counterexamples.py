#!/usr/bin/env python3
"""Exact certificates for the finite and matrix counterexamples in Part D."""
import sympy as s
from math import gcd
from itertools import product

# PGL_2 in characteristic two: exactly the three F_2 lines.
lines=[s.Matrix(v) for v in [(1,0),(0,1),(1,1)]]
x=s.diag(1,0)
stable=[tuple(v) for v in lines if (s.Matrix.hstack(v,x*v).det()%2)==0]
print('PGL2(F2), x=diag(1,0), stable lines:',stable)
assert stable==[(1,0),(0,1)]
print('W on t=gl2/scalars is trivial in characteristic 2: diag(0,1)-diag(1,0)=I mod 2.')

# The C4 arithmetic factor: U(16) -> U(8).  The element 3 of U(8)
# has order two; both lifts have order four.
def order_mod(a,m):
    x=a%m;o=1
    while x!=1:x=x*a%m;o+=1
    return o
units16=[a for a in range(16) if gcd(a,16)==1]
print('C4 factor U(16)->U(8):',[(a,a%8,order_mod(a,16)) for a in units16])
assert [(a,order_mod(a,16)) for a in units16 if a%8==3]==[(3,4),(11,4)]
print('No section: the involution 3 mod 8 has no involutory lift.')

# Subregular element in sp_4; basis matrices [A B; C -A^t], B,C symmetric.
Z=s.zeros(2);I=s.eye(2);X=Z.row_join(I).col_join(Z.row_join(Z))
basis=[]
for i,j in product(range(2),repeat=2):
    A=s.zeros(2);A[i,j]=1;basis.append(A.row_join(Z).col_join(Z.row_join(-A.T)))
for block in ['B','C']:
    for i,j in [(0,0),(0,1),(1,1)]:
        Q=s.zeros(2);Q[i,j]=1;Q[j,i]=1
        basis.append(Z.row_join(Q if block=='B' else Z).col_join((Q if block=='C' else Z).row_join(Z)))
ad=s.Matrix.hstack(*[s.Matrix(X*Y-Y*X).reshape(16,1) for Y in basis])
coeff=s.symbols('a:10');Y=sum((a*b for a,b in zip(coeff,basis)),s.zeros(4))
q=s.symbols('q');f2=s.expand(s.trace((X+q*Y)**2)).coeff(q,1);f4=s.expand((X+q*Y).det()).coeff(q,1)
print('sp4 subregular X=[0 I;0 0]: ad rank=',ad.rank(),', centralizer dimension=',10-ad.rank())
print('d(tr X^2)=',f2,'; d(det X)=',f4,'; adjoint-quotient differential rank=1.')
assert ad.rank()==6 and f2!=0 and f4==0

# A3 Fourier apposition: the selected 2x2 minor vanishes, while the whole
# matrix is invertible.  This disproves the assertion that every B,B' pair
# containing apposed tori is opposite.
F=s.Matrix([[s.I**(i*j) for j in range(4)] for i in range(4)])
minor=F.extract([0,2],[0,2]).det()
print('A3 Fourier determinant=',s.simplify(F.det()),'; minor rows(0,2), cols(0,2)=',minor)
assert F.det()!=0 and minor==0

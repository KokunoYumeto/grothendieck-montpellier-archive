"""Exact algebra for A36 Lemma7.8 counterexample. Python3 + SymPy.
The ambient scheme is Spec F3[x,x^-1,y], hence smooth and normal.
The curve y^2=x(x-2)^2 is integral because x is not a square in F3(x).
Its generic field F3(u) has x=u^2,y=u(u^2-2); s=(2,0) is a specialization.
The p-linear operator on the free rank-one module is F(v)=x*v^3.
"""
import sympy as s
u=s.symbols('u')
x=u**2;y=u*(u**2-2)
assert s.expand(y*y-x*(x-2)**2)==0
assert s.cancel(x*(1/u)**3-1/u)==0
print('Curve relation after parametrization:',s.expand(y*y-x*(x-2)**2))
print('Generic fixed generator v=1/u satisfies x*v^3=v exactly.')
print('Thus every generic fixed vector is an F3 multiple of 1/u; its Galois action is trivial.')
# F9=F3[z]/(z^2-2), represented by (a,b).
def mul(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
def power(a,n):
 r=(1,0)
 for _ in range(n):r=mul(r,a)
 return r
F9=[(a,b) for a in range(3) for b in range(3)]
fixed=[v for v in F9 if mul((2,0),power(v,3))==v]
assert fixed==[(0,0),(0,1),(0,2)]
z=(0,1)
assert power(z,3)==(0,2)
assert power(power(z,3),3)==z
print('At s=(2,0), F(v)=2*v^3; fixed vectors in F9:',fixed)
print('Arithmetic Frobenius sends z to',power(z,3),'=-z; its matrix on the F3-line is [2], order2.')
print('Special image C2 cannot be realized on a subspace of a trivial generic representation after any open subgroup.')
print('All exact checks passed. The full hypothesis and irreducibility proof are in review.md.')

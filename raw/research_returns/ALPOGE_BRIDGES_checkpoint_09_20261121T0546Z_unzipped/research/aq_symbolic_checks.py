"""Finite algebra checks only; this does not prove any general theorem."""
import sympy as s
from math import comb

a, b, c, d, x, y, z = s.symbols("a b c d x y z")
P = s.Matrix([[a, b], [c, d]])
delta = a*d-b*c
beta = s.Matrix([[1, -(a*d+b*c)/(2*c*d)], [0, 1]])
claimed = s.Matrix([[d/delta, 1/(2*c)], [-c/delta, 1/(2*d)]])
assert all(s.cancel(t) == 0 for t in (beta*P).inv()-claimed)
assert s.cancel(claimed[0,0]*claimed[1,1]+claimed[0,1]*claimed[1,0]) == 0
sigma = s.Matrix([[x,y],[z,-x]])
f=x*x+y*z-1
assert all(s.expand(t)==0 for t in
           (sigma-s.eye(2))*(sigma+s.eye(2))-f*s.eye(2))
print("AQ-PERIOD-STRONG: inverse and quadratic relation verified symbolically.")
print("AQ-67-INVOLUTION: matrix factorization AB=BA=fI verified symbolically.")

rows=[]
for p in s.primerange(5, 150):
    def legendre(t):
        v=pow(t % p,(p-1)//2,p)
        return -1 if v==p-1 else v
    ap=-sum(legendre(t**3+1) for t in range(p))
    assert (ap==0)==(p%3==2)
    if p%3==1:
        assert ap % p == comb((p-1)//2,(p-1)//3) % p != 0
    rows.append((p,ap))
print("AQ-CM: trace criterion and split-prime binomial congruence checked for primes 5..149.")
print(rows)

def projective_points(p):
    for X in range(p):
        for Y in range(p):
            yield (X,Y,1)
    for X in range(p):
        yield (X,1,0)
    yield (1,0,0)
for p in (3,5,7,11):
    got=sum(all(v % p for v in (X,Y,Z,X+Y+Z))
            for X,Y,Z in projective_points(p))
    assert got == p*p-3*p+3
print("AQ-154-COUNT: four rational lines x*y*z*(x+y+z)=0 checked at p=3,5,7,11.")

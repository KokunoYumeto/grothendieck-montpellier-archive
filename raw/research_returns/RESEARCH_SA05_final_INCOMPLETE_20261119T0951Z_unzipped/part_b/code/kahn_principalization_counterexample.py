"""Exact finite checks for the principalization obstruction in Kahn's surface route.

The computation verifies the finite-field geometry and group arithmetic.
The Picard and étale-cohomology assertions are proved in the accompanying note.
No random choices, floating-point arithmetic, or analytic rank estimates occur.
"""
from time import perf_counter
from collections import Counter
from sympy import symbols, groebner, Poly

started = perf_counter()
x, y, z, v = symbols('x y z v')
F = x**3 + x*z**2 + z**3 + y**2*z + y*z**2
gradient = [F.diff(t) for t in (x,y,z)]
G = groebner(gradient, x,y,z, modulus=2)
assert list(G) == [x**2, y**2, z**2]
print('E/F2: y^2+y=x^3+x+1, O=[0:1:0]')
print('Homogeneous gradient Groebner basis over F2:', list(G))
print('Thus the projective plane cubic is smooth.')

modulus = 0b10011  # v^4+v+1
def add(a,b): return a ^ b
def mul(a,b):
    value = 0
    while b:
        if b & 1: value ^= a
        b >>= 1
        a <<= 1
        if a & 0b10000: a ^= modulus
    return value
def power(a,n):
    value = 1
    while n:
        if n & 1: value = mul(value,a)
        a = mul(a,a)
        n >>= 1
    return value
def inv(a):
    assert a
    return power(a,14)
def div(a,b): return mul(a,inv(b))
def rhs(a): return power(a,3) ^ a ^ 1
def on_curve(P):
    return P is None or (mul(P[1],P[1]) ^ P[1]) == rhs(P[0])
def inverse(P): return None if P is None else (P[0],P[1]^1)
def plus(P,Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1 = P; x2,y2 = Q
    if x1 == x2 and y1 != y2: return None
    slope = (mul(x1,x1)^1) if P == Q else div(y1^y2,x1^x2)
    x3 = mul(slope,slope)^x1^x2
    y3 = mul(slope,x1^x3)^y1^1
    R=(x3,y3)
    assert on_curve(R)
    return R
def multiple(n,P):
    value = None
    while n:
        if n & 1: value = plus(value,P)
        P=plus(P,P); n >>= 1
    return value
def frobenius(P):
    return None if P is None else tuple(mul(a,a) for a in P)
def order(P):
    R=None
    for n in range(1,26):
        R=plus(R,P)
        if R is None: return n
    raise AssertionError('Order not found')
def form(a):
    if a == 0: return '0'
    return '+'.join('1' if i==0 else ('v' if i==1 else f'v^{i}')
                    for i in range(4) if a & (1<<i))

quartic = Poly(v**4+v+1,v,modulus=2)
assert quartic.is_irreducible
for a in range(1,16): assert mul(a,inv(a))==1
points=[None]+[(a,b) for a in range(16) for b in range(16)
               if on_curve((a,b))]
points2=[P for P in points if frobenius(P)==P]
points4=[P for P in points if frobenius(frobenius(P))==P]
assert len(points)==25 and points2==[None] and len(points4)==5
assert Counter(order(P) for P in points)==Counter({5:24,1:1})
print('GF16 defined by irreducible polynomial v^4+v+1; bit encodings use v=2.')
print('Point counts (#E(F2), #E(F4), #E(F16)) =',
      (len(points2),len(points4),len(points)))
print('Order distribution E(F16):',dict(sorted(Counter(order(P) for P in points).items())))
P=(6,2)  # x=v^2+v, y=v
assert on_curve(P) and order(P)==5
orbit=[]; R=P
while R not in orbit:
    orbit.append(R); R=frobenius(R)
assert R==P and len(orbit)==4
assert orbit[2]==inverse(P)
zero_locus=[Q for Q in points if Q is not None and mul(Q[0],Q[0])^Q[0]^1==0]
assert set(zero_locus)==set(orbit)
print('P=(v^2+v,v), exact order =',order(P))
print('Frobenius orbit in bit encodings:',orbit)
print('Frobenius orbit in polynomial coordinates:',
      [(form(a),form(b)) for a,b in orbit])
print('Multiples 0P,1P,...,5P:',[multiple(n,P) for n in range(6)])
print('The zero locus x^2+x+1 consists exactly of this orbit.')
print('Modulo x^2+x+1, the curve equation is y^2+y=x;')
print('eliminating x gives y^4+y+1=0. Thus the closed point has residue F16.')
print('The cover degree is 4, prime to ell=5.')
print('v_5(16-1)=1; geometric H^1(Gm_Fbar,Q5/Z5)^Frob16 has order 5.')
print('Unbounded-family finite modular checks: r, orbit degree, Picard order, residue 5-order')
for r in range(1,9):
    orbit_degree=4*5**(r-1)
    assert pow(-4,5**(r-1),5**r)==1
    if r>1: assert pow(-4,5**(r-2),5**r)!=1
    remainder=(pow(2,orbit_degree,5**(r+1))-1) % (5**(r+1))
    assert remainder and remainder % (5**r)==0
    print(r,orbit_degree,5**r,5**r)
print('All exact finite checks passed.')
print(f'Runtime seconds: {perf_counter()-started:.6f}')

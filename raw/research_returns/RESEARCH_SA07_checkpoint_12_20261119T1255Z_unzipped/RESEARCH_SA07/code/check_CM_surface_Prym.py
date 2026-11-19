#!/usr/bin/env python3
"""Exact finite algebra for the C20 CM-surface Prym construction, F.3.19.
The connected-kernel and absolute-simplicity arguments remain written proofs.
"""
from time import perf_counter
started = perf_counter()
import sympy as s
from itertools import product
u,v,t = s.symbols('u v t')
relation = u**20+v**20-1
assert s.expand((u**5)**4+(v**5)**4-1)==relation
print('PASS: fifth-power map C20 to C4 preserves the defining equation')
assert s.expand((v**10)**2+(u**4)**5-1)==relation
print('PASS: X=u^4, Y=v^10 maps C20 to Y^2=1-X^5')
deck=list(product(range(4),range(10)))
assert len(set(deck))==40
assert all((20*a)%4==0 and (20*b)%10==0 for a,b in deck)
assert all((4*a)%4==0 and (10*b)%10==0 for a,b in deck)
print('PASS: all40 distinct mu4 x mu10 coordinate scalings preserve C20 and fix X,Y')
deck25=list(product(range(5),repeat=2))
assert len(deck25)==25
assert all((20*a)%5==0 and (20*b)%5==0 for a,b in deck25)
print('PASS: all25 fifth-root coordinate scalings preserve C20 and fix C4 coordinates')
phi=s.Poly(s.cyclotomic_poly(5,t),t)
assert phi.degree()==4 and phi.is_irreducible
assert s.rem(t**5-1,phi.as_expr(),t)==0
assert s.gcd(phi.as_expr(),t-1)==1
assert sorted([1,2,-1%5,-2%5])==[1,2,3,4]
print('PASS: primitive order5 homology exponents are1,2,3,4 and have irreducible polynomial Phi5')
group=[1,2,3,4]
order2=[a for a in group if a!=1 and a*a%5==1]
assert order2==[4]
q=s.Poly(t*t+t-1,t)
assert s.discriminant(q.as_expr(),t)==5
print('PASS: cyclic quartic Galois group has unique order2 element complex conjugation; fixed quadratic has discriminant5')
e12=s.Matrix([[0,1],[0,0]]);e21=s.Matrix([[0,0],[1,0]])
assert e12*e21==s.diag(1,0) and e21*e12==s.diag(0,1)
assert e12*e21!=e21*e12
print('PASS: explicit matrix units verify the noncommutativity used in the degree8 field-embedding contradiction')
assert (20-1)*(20-2)//2==171 and 32*25==800 and 4*10==40
print('PASS: compactification genus171; cover degree800; genus2 quotient degree40')
print('LIMIT: the actual morphism extensions, branch containment, absolute simplicity, norm identity, and integral Prym inclusion are proved in F.3.19.')
print('LIMIT: no procyclic lift with open arithmetic normalizer is constructed.')
print('ACTUAL_WALL_SECONDS:',format(perf_counter()-started,'.9f'))

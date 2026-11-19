#!/usr/bin/env python3
"""Exact algebra for B44; does not decide the remaining sixteen-congruences."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
from time import perf_counter
import json
started=perf_counter()
one=(F(1),F(0),F(0),F(0));zero=(F(0),)*4
i=(F(0),F(1),F(0),F(0));j=(F(0),F(0),F(1),F(0));k=(F(0),F(0),F(0),F(1))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def scale(a,c):return tuple(F(c)*x for x in a)
def mul(a,b):
    w,x,y,z=a;W,X,Y,Z=b
    return (w*W-x*X-y*Y-z*Z,w*X+x*W+y*Z-z*Y,
            w*Y-x*Z+y*W+z*X,w*Z+x*Y-y*X+z*W)
def conj(a):return(a[0],-a[1],-a[2],-a[3])
def norm(a):return sum(x*x for x in a)
def inv(a):return scale(conj(a),1/norm(a))
def power(a,n):
    if n<0:return power(inv(a),-n)
    z=one
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n>>=1
    return z
def act(a,b):return mul(mul(a,b),inv(a))
def order(a):
    for n in range(1,25):
        if power(a,n)==one:return n
    raise AssertionError(a)
def v2(a):
    a=F(a);assert a
    n,d=abs(a.numerator),a.denominator;v=0
    while n%2==0:n//=2;v+=1
    while d%2==0:d//=2;v-=1
    return v
q8={one,neg(one),i,neg(i),j,neg(j),k,neg(k)}
hurwitz=q8|{tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=4)}
assert len(hurwitz)==24
assert all(norm(a)==1 for a in hurwitz)
assert all(mul(a,b) in hurwitz for a in hurwitz for b in hurwitz)
orders=Counter(order(a) for a in hurwitz)
assert orders=={1:1,2:1,3:8,4:6,6:8}
zeta=scale(add(neg(one),add(i,add(j,k))),F(1,2))
assert order(zeta)==3
n4=add(one,i);n3=add(i,neg(j))
assert norm(n4)==norm(n3)==2
assert act(n4,i)==i and act(n4,j)==k
assert act(n3,zeta)==inv(zeta)
assert {act(n4,a) for a in q8}==q8

# F4=F2[w]/(w^2+w+1), encoded in the polynomial basis.
def fm(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return r
def fp(a,n):
    r=1
    while n:
        if n&1:r=fm(r,a)
        a=fm(a,a);n>>=1
    return r
auts={(u,s,t) for u in (1,2,3) for s,t in product(range(4),repeat=2)
      if fp(t,2)^t==fp(s,3)}
assert len(auts)==24
def compose(a,b):
    u,s,t=a;v,r,w=b
    return (fm(u,v),fm(u,r)^s,t^w^fm(fm(fp(u,2),s),fp(r,2)))
identity=(1,0,0)
def aorder(a):
    b=identity
    for n in range(1,25):
        b=compose(b,a)
        if b==identity:return n
    raise AssertionError(a)
def ainv(a):return next(b for b in auts if compose(a,b)==identity)
def aact(a,b):return compose(compose(a,b),ainv(a))
assert all(compose(a,b) in auts for a in auts for b in auts)
assert Counter(aorder(a) for a in auts)==orders
# Exact coefficient comparison in y'^2+y'-x'^3.
for u,s,t in auts:
    assert fp(u,6)==1 and fp(s,4)==s
    assert fp(t,2)^t==fp(s,6)
ai=(1,1,2);aj=(1,3,2)
assert aorder(ai)==aorder(aj)==4
assert compose(ai,ai)==compose(aj,aj)==(1,0,1)
ak=compose(ai,aj)
mapping={one:identity,neg(one):(1,0,1),i:ai,j:aj,k:ak,
         neg(i):compose((1,0,1),ai),neg(j):compose((1,0,1),aj),
         neg(k):compose((1,0,1),ak)}
az=next(a for a in auts if aorder(a)==3 and
        aact(a,ai)==mapping[act(zeta,i)] and aact(a,aj)==mapping[act(zeta,j)])
queue=[one];mapping={one:identity}
gens=[(i,ai),(j,aj),(zeta,az)]
while queue:
    a=queue.pop()
    for g,ag in gens:
        b=mul(a,g);ab=compose(mapping[a],ag)
        if b in mapping:assert mapping[b]==ab
        else:mapping[b]=ab;queue.append(b)
assert set(mapping)==hurwitz and set(mapping.values())==auts
assert all(mapping[mul(a,b)]==compose(mapping[a],mapping[b]) for a in hurwitz for b in hurwitz)
order3_actions={(act(a,i),act(a,j)) for a in hurwitz if order(a)==3}
assert len(order3_actions)==8

# Explicit rational conjugates; normalization has valuation exactly zero.
conjugacy_cases=0
for n in range(1,41):
    q=(F(n),F(1),F(n%5),F(n%7));assert norm(q)
    a=act(q,i);d=add(a,i)
    if d!=zero:
        assert mul(d,a)==mul(i,d)
        du=mul(power(n4,-v2(norm(d))),d)
        assert v2(norm(du))==0 and act(du,a)==i
    z=act(q,zeta);d=add(z,add(zeta,one))
    if d!=zero:
        assert mul(d,z)==mul(zeta,d)
        du=mul(power(n3,-v2(norm(d))),d)
        assert v2(norm(du))==0 and act(du,z) in {zeta,inv(zeta)}
    c=mul((F(n),F(1),F(0),F(0)),inv((F(n),F(-1),F(0),F(0))))
    assert norm(c)==1
    b=add(one,c) if c!=neg(one) else i
    assert mul(b,inv(conj(b)))==c
    db=inv(b);du=mul(power(n4,-v2(norm(db))),db)
    assert v2(norm(du))==0
    assert {act(du,a) for a in {one,neg(one),i,neg(i),mul(c,j),neg(mul(c,j)),mul(i,mul(c,j)),neg(mul(i,mul(c,j)))}}==q8
    conjugacy_cases+=3

valuation_cases=0
for v in range(1,1001):
    assert 1+v<1+2*v
    for degree in range(3,21):
        assert 1+v<degree*v
        valuation_cases+=1
units=list(range(1,16,2))
determinant_cases=[]
for d,e in product(range(3),repeat=2):
    possible=all(pow(u,(d-e)%4,16) in (1,15) for u in units)
    assert possible==(d==e)
    determinant_cases.append({'d':d,'e':e,'pointwise_sign_possible':possible})
joint_orders=sorted({3*2**r for r in range(7)})
out={'status':'PASS','scope':'Finite automorphisms, quaternion conjugators and elementary valuation/determinant identities only; no remaining sixteen-torsion comparison evaluated',
     'special_automorphisms':24,'automorphism_products':576,'quaternion_products':576,
     'element_order_distribution':dict(sorted(orders.items())),
     'order_three_automorphisms_of_Q8':len(order3_actions),
     'integral_conjugacy_test_cases':conjugacy_cases,
     'formal_valuation_cases':valuation_cases,'determinant_dimension_cases':determinant_cases,
     'remaining_joint_orders':joint_orders,'elapsed_seconds':perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

"""Exact exterior-algebra check of the surface point-orbit Fourier square.

All coefficients are Fraction; no numerical approximation or symbolic oracle.
This verifies the Chern-character identity, primitivity, square, and
polarization annihilation. It does not verify sheaf existence or trace maps.
"""
from fractions import Fraction as Q
from math import factorial
import json
from pathlib import Path

def add(*terms):
    out = {}
    for term in terms:
        for key, val in term.items():
            out[key] = out.get(key, Q(0)) + val
    return {key: val for key, val in out.items() if val}

def scale(x, q):
    return {key: val*q for key,val in x.items() if val*q}

def mul(x,y):
    out = {}
    for a,c in x.items():
        for b,d in y.items():
            if set(a).intersection(b):
                continue
            sign = (-1)**sum(i>j for i in a for j in b)
            key = tuple(sorted(a+b))
            out[key] = out.get(key,Q(0)) + sign*c*d
    return {key:val for key,val in out.items() if val}

one = {():Q(1)}
def power(x,n):
    out=one
    for _ in range(n):
        out=mul(out,x)
    return out

def exp(x,n):
    return add(*(scale(power(x,j),Q(1,factorial(j))) for j in range(n+1)))

def e(i): return {(i,):Q(1)}
def wedge(i,j): return mul(e(i),e(j))

# Order: x=(a1,b1,a2,b2), y=(c1,d1,c2,d2), dual=(u1,v1,u2,v2).
Hx = add(wedge(0,1),wedge(2,3))
Hy = add(wedge(4,5),wedge(6,7))
Hu = add(wedge(8,9),wedge(10,11))
Hxy = add(mul(add(e(0),e(4)),add(e(1),e(5))),
          mul(add(e(2),e(6)),add(e(3),e(7))))
Pker = add(wedge(4,9),scale(wedge(5,8),-1),
           wedge(6,11),scale(wedge(7,10),-1))
Pout = add(wedge(0,9),scale(wedge(1,8),-1),
           wedge(2,11),scale(wedge(3,10),-1))
def char(H): return add(one,H,scale(power(H,2),Q(-1,2)))

integrand = mul(mul(char(Hxy),char(Hy)),exp(scale(Pker,-1),6))
fiber=(4,5,6,7)
integrated={}
for key,val in integrand.items():
    if not all(i in key for i in fiber):
        continue
    base=tuple(i for i in key if i not in fiber)
    sign=(-1)**sum(i>j for i in base for j in fiber)
    integrated[base]=integrated.get(base,Q(0))+sign*val
normalized=mul(exp(scale(Pout,Q(-1,2)),4),integrated)

theta=add(Hx,Hu)
# Re(W_i): (a1b1-u1v1+iP1)(a2b2-u2v2+iP2).
d1=add(wedge(0,1),scale(wedge(8,9),-1))
d2=add(wedge(2,3),scale(wedge(10,11),-1))
p1=add(wedge(0,9),scale(wedge(1,8),-1))
p2=add(wedge(2,11),scale(wedge(3,10),-1))
t=add(mul(d1,d2),scale(mul(p1,p2),-1))
expected=add(t,scale(theta,-2),scale(power(theta,3),Q(1,12)))
assert normalized==expected, add(normalized,scale(expected,-1))
assert mul(theta,t)=={}
volume=tuple([0,1,2,3,8,9,10,11])
square=mul(t,t)
assert square=={volume:Q(8)}, square
assert all(v.denominator==1 for v in t.values())
assert any(abs(v)==1 for v in t.values())
assert normalized.get((),0)==0
assert scale(power(theta,4),Q(1,24))=={volume:Q(1)}
result={
    "status":"PASS",
    "identity":"exp(-P/2) ch(E) = t - 2 theta + theta^3/12",
    "virtual_rank":0,
    "theta_volume":1,
    "theta_times_t":0,
    "t_square":8,
    "t_primitive_integral":True,
    "t_nonzero_coefficients":len(t),
    "input":"I_H(theta) on an abelian surface; H has order two",
    "scope":"Exterior-algebra character certificate only"
}
path=Path(__file__).with_name('surface_seed_certificate.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

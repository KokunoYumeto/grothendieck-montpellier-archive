#!/usr/bin/env python3
"""Reconstructive characteristic-two elliptic-quintic/secant identities.

Uses only exact binary polynomial arithmetic. Geometry is proved separately.
The previous cyclic-basis discovery program/output is retained unchanged.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations_with_replacement
import json,time

started=time.perf_counter()
sections=[11,31,17,19,28]  # coefficients in 1,x,y,x^2,xy

def xor(*args):
    out=set()
    for a in args: out.symmetric_difference_update(a)
    return out

# Formal five-variable homogeneous polynomials.
z=[{tuple(int(i==j) for i in range(5))} for j in range(5)]
def formal_mul(a,b):
    out=set()
    for u in a:
        for v in b:
            w=tuple(x+y for x,y in zip(u,v))
            if w in out:out.remove(w)
            else:out.add(w)
    return out
def formal_linear(mask):return xor(*(z[i] for i in range(5) if mask>>i&1))
w=list(map(formal_linear,sections))
sigma_transformed=[xor(formal_mul(w[i],w[i]),formal_mul(w[(i-1)%5],w[(i+1)%5]),formal_mul(w[(i-2)%5],w[(i+2)%5])) for i in range(5)]
standard=[xor(formal_mul(z[1],z[1]),formal_mul(z[0],z[3])),
          xor(formal_mul(z[1],z[2]),formal_mul(z[0],z[4])),
          xor(formal_mul(z[2],z[2]),formal_mul(z[0],z[2]),formal_mul(z[1],z[3]),formal_mul(z[0],z[1])),
          xor(formal_mul(z[1],z[4]),formal_mul(z[2],z[3])),
          xor(formal_mul(z[2],z[4]),formal_mul(z[0],z[4]),formal_mul(z[3],z[3]),formal_mul(z[0],z[3]))]
coordinates={tuple(sorted(xor(*(standard[j] for j in range(5) if mask>>j&1)))):mask for mask in range(32)}
assert len(coordinates)==32
quad_coordinates=[coordinates[tuple(sorted(q))] for q in sigma_transformed]
def binary_rank(vs):
    piv={}
    for v in vs:
        while v:
            i=v.bit_length()-1
            if i in piv:v^=piv[i]
            else:piv[i]=v;break
    return len(piv)
assert binary_rank(sections)==5 and binary_rank(quad_coordinates)==5

# F2[x,y,u,v]/(y^2+y+x^3+x,v^2+v+u^3+u).
one={(0,0,0,0)}
x={(1,0,0,0)};y={(0,1,0,0)};u={(0,0,1,0)};v={(0,0,0,1)}
def reduced_monomial(a,b,c,d):
    if b>=2:
        return xor(reduced_monomial(a,b-1,c,d),reduced_monomial(a+3,b-2,c,d),reduced_monomial(a+1,b-2,c,d))
    if d>=2:
        return xor(reduced_monomial(a,b,c,d-1),reduced_monomial(a,b,c+3,d-2),reduced_monomial(a,b,c+1,d-2))
    return {(a,b,c,d)}
def mul(a,b):
    out=set()
    for s in a:
        for t in b:out.symmetric_difference_update(reduced_monomial(*(i+j for i,j in zip(s,t))))
    return out
def sq(a):return mul(a,a)
bases=[[one,x,y,sq(x),mul(x,y)],[one,u,v,sq(u),mul(u,v)]]
points=[[xor(*(basis[j] for j in range(5) if mask>>j&1)) for mask in sections] for basis in bases]
for point in points:
    assert all(not xor(sq(point[i]),mul(point[(i-1)%5],point[(i+1)%5]),mul(point[(i-2)%5],point[(i+2)%5])) for i in range(5))
p,q=points
polar=[xor(mul(p[(i-1)%5],q[(i+1)%5]),mul(q[(i-1)%5],p[(i+1)%5]),mul(p[(i-2)%5],q[(i+2)%5]),mul(q[(i-2)%5],p[(i+2)%5])) for i in range(5)]
secant_coefficients=[xor(*(mul(point[i],sq(polar[i])) for i in range(5))) for point in points]
assert all(not a for a in secant_coefficients)

# On z4=1 the standard quadrics reduce to v+u^2+v^2*u+v^2*u^2.
# Eliminate z1=v*u and z0=v^2*u; check the other three equations exactly.
# Use a plain F2[u,v] ring here, with no elliptic relation imposed.
def raw_mul(a,b):
    out=set()
    for s in a:
        for t in b:
            m=tuple(i+j for i,j in zip(s,t))
            if m in out:out.remove(m)
            else:out.add(m)
    return out
U={(1,0)};V={(0,1)};ONE={(0,0)}
chart=[raw_mul(raw_mul(V,V),U),raw_mul(V,U),V,U,ONE]
def subst(poly):
    result=set()
    for exponent in poly:
        term=ONE
        for i,n in enumerate(exponent):
            for _ in range(n):term=raw_mul(term,chart[i])
        result.symmetric_difference_update(term)
    return result
chart_eq=[subst(g) for g in standard]
F=xor(V,raw_mul(U,U),raw_mul(raw_mul(V,V),U),raw_mul(raw_mul(V,V),raw_mul(U,U)))
assert chart_eq[0]==set() and chart_eq[1]==set() and chart_eq[3]==set()
assert chart_eq[4]==F and chart_eq[2]==raw_mul(V,F)
assert {tuple(e-(i==1) for i,e in enumerate(m)) for m in F if m[1]%2}=={(0,0)}

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-started,'section_masks_in_1_x_y_x2_xy':sections,'section_matrix_rank':5,'transformed_Pfaffian_coordinates_in_standard_quadrics':quad_coordinates,'quadric_span_rank':5,'standard_quadrics':[sorted(f) for f in standard],'transformed_Pfaffians':[sorted(f) for f in sigma_transformed],'two_point_ring':'F2[x,y,u,v]/(y^2+y+x^3+x,v^2+v+u^3+u)','secant_parameter_coefficients_lambda3mu2_lambda2mu3':[sorted(f) for f in secant_coefficients],'chart_z4_F':sorted(F),'chart_derivative_v_is_one':True,'scope':'Exact basis/quadric-span identities, two-point universal secant identities and the smooth infinity chart; all coefficients reconstructed without parameter sampling.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','actual_utc','runtime_seconds','section_matrix_rank','quadric_span_rank','transformed_Pfaffian_coordinates_in_standard_quadrics','secant_parameter_coefficients_lambda3mu2_lambda2mu3','chart_derivative_v_is_one']}))

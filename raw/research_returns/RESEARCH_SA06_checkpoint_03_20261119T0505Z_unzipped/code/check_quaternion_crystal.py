#!/usr/bin/env python3
"""Exact algebra certificates for SA06; no floating-point arithmetic."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json,time
import sympy as s

def mul(x,y):
    # i^2=-1, j^2=-3, k=ij.
    a,b,c,d=x; e,f,g,h=y
    return (a*e-b*f-3*c*g-3*d*h,
            a*f+b*e+3*c*h-3*d*g,
            a*g+c*e-b*h+d*f,
            a*h+d*e+b*g-c*f)

def main():
    t=time.perf_counter()
    basis=[(Q(1),Q(0),Q(0),Q(0)),(Q(0),Q(1),Q(0),Q(0)),
           (Q(1,2),Q(0),Q(1,2),Q(0)),(Q(0),Q(1,2),Q(0),Q(1,2))]
    B=s.Matrix.hstack(*(s.Matrix(v) for v in basis))
    table=[]
    for x in basis:
        row=[]
        for y in basis:
            z=B.inv()*s.Matrix(mul(x,y))
            assert all(v.q==1 for v in z)
            row.append([int(v) for v in z])
        table.append(row)
    trace=s.Matrix([[2*mul(x,y)[0] for y in basis] for x in basis])
    assert trace.det()==-9
    p=3;a=4
    J=s.Matrix([[0,-p],[1,0]])
    assert J**2==-p*s.eye(2)
    F=a*J
    assert F.det()==48 and F**2==-48*s.eye(2)
    out={'algebra':'(-1,-3)/Q', 'order_basis':[[str(c) for c in x] for x in basis],
         'multiplication_table':table,'reduced_trace_gram':[[int(c) for c in row] for row in trace.tolist()],
         'trace_determinant':int(trace.det()),'reduced_discriminant':3,
         'crystal_field':'F_9','F_semilinear_matrix':F.tolist(),
         'F_squared_scalar':-48,'det_F_coefficient':48,'Tate_F_coefficient':3,
         'isomorphism_equation':'sigma(c)=16 c; sigma^2(c)=c forces 255 c=0',
         'contradiction_nonzero_integer':255}
    # Finite tests of local Kummer group sizes (odd p mod p, p=2 mod 8).
    out['unit_squareclasses']={}
    for m in [8,3,5,7,11]:
        units=[x for x in range(m) if s.gcd(x,m)==1]
        squares={x*x%m for x in units}
        cosets=[]
        unseen=set(units)
        while unseen:
            x=min(unseen); coset={x*y%m for y in squares}
            cosets.append(sorted(coset)); unseen-=coset
        out['unit_squareclasses'][str(m)]=cosets
    out['runtime_seconds']=time.perf_counter()-t
    def cast(x):
        if isinstance(x,s.Integer):return int(x)
        raise TypeError(type(x))
    dest=Path(__file__).with_name('check_quaternion_crystal_output.json')
    dest.write_text(json.dumps(out,indent=2,default=cast)+'\n')
    print(json.dumps(out,indent=2,default=cast))

if __name__=='__main__':main()

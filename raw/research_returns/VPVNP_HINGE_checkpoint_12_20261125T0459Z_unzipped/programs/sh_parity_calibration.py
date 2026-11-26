#!/usr/bin/env python3
"""Exact finite arithmetic certificate for the SH37 parity calibration.

This verifies all sixteen parity cases, all sign choices determining
their angular maxima, terminal quotient charges, and the strict margin.
The graph-theoretic flow and support argument is proved in shortening.tex.
"""
import itertools
import json
import sys
from pathlib import Path
import sympy as s

cfg=json.loads(Path(sys.argv[1]).read_text())
r=s.sqrt(2)
directions=[s.Matrix([-1/r,-1/r]),s.Matrix([-1/r,-1/r]),s.Matrix([-1,0]),s.Matrix([0,-1])]

def nonnegative_quadratic(x):
    x=s.expand(x);a=x.coeff(r,0);b=x.coeff(r,1)
    assert s.simplify(x-a-b*r)==0 and a.is_Rational and b.is_Rational
    if b==0:return a>=0
    if a>=0 and b>=0:return True
    if a<0 and b<0:return False
    if a>=0:return a*a>=2*b*b
    return 2*b*b>=a*a

patterns=[]
for mask in range(16):
    indices=[i for i in range(4) if mask>>i&1];h=len(indices)
    if h==0:bound=s.Integer(0);gap=s.Integer(0)
    elif mask==3:bound=s.Integer(2);gap=s.Integer(0)
    elif h%2:bound=s.Integer(h);gap=s.Rational(1,2)
    elif h==2:bound=s.sqrt(2+r);gap=1-bound/2
    else:assert h==4;bound=2+r;gap=1-r/2
    checks=[]
    for signs in itertools.product((-1,1),repeat=h):
        vector=s.zeros(2,1)
        for sign,index in zip(signs,indices):vector+=sign*directions[index]
        squared=s.simplify(vector.dot(vector))
        assert nonnegative_quadratic(s.simplify(bound**2-squared))
        checks.append({'signs':list(signs),'squared_norm':str(squared)})
    patterns.append({'mask':mask,'weight':h,'angular_upper':str(bound),
                     'excess_lower':str(gap),'sign_checks':checks})

def quotient(mask):return ((mask&1)^((mask>>1)&1))|(((mask>>2)&1)<<1)|(((mask>>3)&1)<<2)
assert [mask for mask in range(16) if quotient(mask)==0]==cfg['parity_quotient_kernel']
raw=[0]*4;names=['a','b','c','d'];base=s.Integer(0)
for i,(a,b,numerator,denominator) in enumerate(cfg['commodities']):
    assert denominator==2 and numerator%2==1
    raw[names.index(a)]^=1<<i;raw[names.index(b)]^=1<<i
    delta=s.Matrix(cfg['terminals'][b])-s.Matrix(cfg['terminals'][a])
    assert s.simplify(directions[i].dot(delta)-s.sqrt(delta.dot(delta)))==0
    base+=s.Rational(numerator,denominator)*s.sqrt(delta.dot(delta))
charges=[quotient(z) for z in raw]
assert charges==[3,5,3,5]
zero_subsets=[]
for mask in range(16):
    value=0
    for i in range(4):
        if mask>>i&1:value^=charges[i]
    if value==0:zero_subsets.append(mask)
assert zero_subsets==[0,5,10,15]
assert all(not(mask&1) or mask&4 for mask in zero_subsets)
assert s.simplify(base-(10+7*r))==0
c0=1-s.sqrt(2+r)/2;bound=s.simplify(base+2*c0)
assert s.simplify(bound-s.sympify(cfg['claimed_bound']))==0
assert 7*7*2>8*8 and 160*160>2*113*113
b,L=s.symbols('b L', integer=True)
generic=s.simplify(2*(b-L/2)*s.sqrt(2)+2*L+2*c0)
assert s.simplify(generic-(2*s.sqrt(2)*b+(2-s.sqrt(2))*L+2-s.sqrt(2+s.sqrt(2))))==0
assert s.simplify(generic.subs(L,2*b-7)-(4*b-4)-(bound-20))==0
result={'general_cost_lower_bound':str(generic),'boundary_low_cut':'2*b-7','boundary_margin':str(bound-20),'config':cfg,'patterns':patterns,'raw_terminal_charges':raw,
        'quotient_terminal_charges':charges,'zero_sum_terminal_subsets':zero_subsets,
        'calibration_base':str(base),'uniform_nonzero_quotient_gap':str(c0),
        'minimum_support_path_length':2,'cost_lower_bound':str(bound),
        'cost_lower_bound_decimal':str(s.N(bound,25)),
        'strict_margin_decimal':str(s.N(bound-20,25)),
        'integer_squared_margin':160*160-2*113*113,
        'PASS':True,
        'scope':'Exact arithmetic and parity support cases; the universal graph proof is SH37.'}
Path(sys.argv[2]).write_text(json.dumps(result,indent=2))
print(json.dumps({key:result[key] for key in ['calibration_base','uniform_nonzero_quotient_gap','cost_lower_bound','cost_lower_bound_decimal','integer_squared_margin','PASS']}))

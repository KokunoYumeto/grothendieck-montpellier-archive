#!/usr/bin/env python3
"""Independent exact arithmetic checks for the mixed-dimension counterexamples."""
from pathlib import Path
from itertools import product
from math import comb
from time import perf_counter
import json
import sympy as s

start=perf_counter(); checks=[]
def require(label,condition):
    assert condition,label
    checks.append(label)

t,x0,x1,x2,x3=s.symbols('t x0 x1 x2 x3')
# Elimination computes (x3) intersect (x0,x1,x2), independently
# of enumerating the claimed monomial generators.
G=s.groebner([t*x3,(1-t)*x0,(1-t)*x1,(1-t)*x2],t,x0,x1,x2,x3,order='lex')
eliminated=[p.as_expr() for p in G.polys if not p.as_expr().has(t)]
expected=s.groebner([x0*x3,x1*x3,x2*x3],x0,x1,x2,x3,order='lex')
actual=s.groebner(eliminated,x0,x1,x2,x3,order='lex')
require('intersection_groebner',list(actual)==list(expected))

degree_records=[]
for n in range(1,11):
    survivors=[]
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                d=n-a-b-c
                mon=x0**a*x1**b*x2**c*x3**d
                if expected.reduce(mon)[1]!=0:survivors.append((a,b,c,d))
    plane=[m for m in survivors if m[3]==0]
    restriction=s.zeros(len(plane),len(survivors))
    for i,m in enumerate(plane):restriction[i,survivors.index(m)]=1
    rank=restriction.rank(); nullity=len(restriction.nullspace())
    require(f'plane_hilbert_{n}',len(plane)==comb(n+2,2))
    require(f'point_hilbert_{n}',len(survivors)==len(plane)+1)
    require(f'restriction_rank_{n}',rank==len(plane))
    require(f'restriction_kernel_{n}',nullity==1)
    degree_records.append({'twist':n,'source_dimension':len(survivors),'target_dimension':len(plane),'rank':rank,'kernel_dimension':nullity})

# In Cech coordinates for O(-n) on P1, Laurent powers strictly
# between -n and 0 survive modulo the two affine-chart sections.
for n in range(2,14):
    surviving=[e for e in range(-2*n,2*n+1) if not(e>=0 or e<=-n)]
    require(f'cech_endpoint_{n}',surviving==list(range(-n+1,0)) and len(surviving)==n-1)

result={'statement':'C.023','status':'PASS','checks':len(checks),'runtime_seconds':perf_counter()-start,'intersection_generators':[str(p) for p in actual],'degree_records':degree_records,'scope':'Exact Groebner intersection, quotient monomials and rational restriction-matrix ranks; Cech Laurent quotient for the endpoint example. Geometric CM and the general seven-condition equivalence are proved in the text.'}
out=Path(__file__).resolve().parents[1]/'logs/root_C023_purity.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

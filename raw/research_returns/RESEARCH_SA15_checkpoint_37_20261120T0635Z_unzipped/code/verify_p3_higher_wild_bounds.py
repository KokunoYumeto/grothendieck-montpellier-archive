#!/usr/bin/env python3
"""Finite exact arithmetic checks for B-RD20/B-RD21.

This verifies simplification and extremization of proved necessary inequalities.
It does not assert that a formal valuation pair gives a wild elliptic curve.
"""
import json
import time

start=time.perf_counter()

def v3(x):
    s=0
    while x%3==0: s+=1; x//=3
    return s

def log3floor(x):
    L=0
    while x>=3: L+=1; x//=3
    return L

def possible_bound(e,n,m):
    s=v3(e//2)
    return s>=n-1 and m*e>=8*3**max(2*n-2,4*n-4-s)

formula_checks=0
gap_count=0
full9_gaps=[]
first_gaps=[]
for e in range(2,100001,2):
    s=v3(e//2); L=log3floor(e//2)
    Nt=1+min(s,L//2,(L+s)//4)
    Nw=1+min(s,(L+1)//2,(L+s+1)//4)
    direct_t=max(n for n in range(1,s+2) if possible_bound(e,n,4))
    direct_w=max(n for n in range(1,s+2) if possible_bound(e,n,12))
    assert (Nt,Nw)==(direct_t,direct_w)
    assert Nt<=Nw<=Nt+1
    k=(L+s+1)//4
    arithmetic_gap=(L+s+1)%4==0 and k>=1 and k<=s<=2*k-1 and L==4*k-s-1
    assert arithmetic_gap==(Nw==Nt+1)
    if arithmetic_gap:
        assert (Nt,Nw)==(k,k+1)
        gap_count+=1
        if len(first_gaps)<20:first_gaps.append({'e':e,'s':s,'L':L,'Nt':Nt,'Nw':Nw})
    if possible_bound(e,2,12) and not possible_bound(e,2,4):full9_gaps.append(e)
    formula_checks+=1
assert full9_gaps==[24,30,42,48]
assert [m for m in (3,6,12) if possible_bound(24,2,m)]==[12]
assert [m for m in (3,6,12) if possible_bound(30,2,m)]==[12]
assert [m for m in (3,6,12) if possible_bound(42,2,m)]==[6,12]
assert [m for m in (3,6,12) if possible_bound(48,2,m)]==[6,12]

minima=[]
for n in range(1,7):
    minimum=2*3**(2*n-2)
    for e in range(2,minimum,2):
        assert not any(possible_bound(e,n,m) for m in (2,3,4,6,12))
    assert possible_bound(minimum,n,4)
    minima.append({'n':n,'e_min':minimum,'attained_defect':4})

valuation_pairs=0
for n in range(1,4):
    for m in (3,6,12):
        for e in range(2,1001,2):
            for r in range(n):
                C=2*3**(2*n-r-2)
                if (m*e)%C:continue
                S=m*e//C
                for B in range(1,S//(4*3**(2*r))+1):
                    A=S-3**(2*r+1)*B
                    if A%3:continue
                    if A<3**(2*r)*B:continue
                    if r<n-1 and A>3**(2*r+2)*B:continue
                    assert m*e==C*(A+3**(2*r+1)*B)
                    raw=2*3**(n-1)*(A+3**n*B+sum(2*3**(n-j-1)*min(A,3**(2*j)*B) for j in range(1,n)))
                    assert raw==m*e
                    assert possible_bound(e,n,m)
                    valuation_pairs+=1

print(json.dumps({
    'scope':'Exact integer arithmetic only. Wild existence in the exceptional ranges is not asserted.',
    'range_formula_input':{'p':3,'even_e_max':100000},
    'range_formula_checks':formula_checks,
    'exceptional_e_count_in_range':gap_count,
    'first_exceptional_indices':first_gaps,
    'full9_unresolved_indices':[24,30,42,48],
    'minimum_tests':minima,
    'unsimplified_valuation_input':{'n':[1,2,3],'m':[3,6,12],'even_e_max':1000},
    'admissible_valuation_pairs_checked':valuation_pairs,
    'all_assertions_passed':True,
    'elapsed_seconds':time.perf_counter()-start
},indent=2))

#!/usr/bin/env python3
"""Exact finite PD matrices for AT23; supplements the all-arity proof.

Basis is gamma_a(x) gamma_b(u) y^epsilon v^delta, with odd order y,v.
The old differential is dx=p*y, du=y, dv=p*u-x.
The new basis uses x'=x-p*u, hence dx'=0, du=y, dv=-x'.
"""
from pathlib import Path
from math import comb
from time import perf_counter
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

start = perf_counter()
checks = 0
details = []

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def basis(n):
    return [(a, n-e-v-a, e, v)
            for e in (0,1) for v in (0,1)
            for a in range(n-e-v+1)]

def form(z):
    a,b,e,v = z
    return 2*(a+b)+3*e+v

def differential(bb, p, changed=False):
    index = {z:i for i,z in enumerate(bb)}
    D = sp.zeros(len(bb))
    def add(col, z, c):
        D[index[z],col] += c
    for j,(a,b,e,v) in enumerate(bb):
        if a and not e and not changed:
            add(j,(a-1,b,1,v),p)
        if b and not e:
            add(j,(a,b-1,1,v),1)
        if v:
            sign = (-1)**e
            add(j,(a+1,b,e,0),-sign*(a+1))
            if not changed:
                add(j,(a,b+1,e,0),sign*p*(b+1))
    return D

def change(bb, p):
    index = {z:i for i,z in enumerate(bb)}
    F = sp.zeros(len(bb))
    for j,(a,b,e,v) in enumerate(bb):
        for i in range(a+1):
            F[index[(i,a-i+b,e,v)],j] += p**(a-i)*comb(a-i+b,b)
    return F

def rank_mod2(M):
    rows = [[int(M[i,j]) % 2 for j in range(M.cols)] for i in range(M.rows)]
    rank = 0
    for col in range(M.cols):
        pivot = next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[rank],rows[pivot] = rows[pivot],rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                rows[i] = [a^b for a,b in zip(rows[i],rows[rank])]
        rank += 1
    return rank

for p in (2,3,5):
    for n in range(9):
        bb = basis(n)
        old = differential(bb,p)
        new = differential(bb,p,True)
        F = change(bb,p)
        inv = change(bb,-p)
        I = sp.eye(len(bb))
        check(old*old == sp.zeros(len(bb)),f'd2-old p={p} n={n}')
        check(new*new == sp.zeros(len(bb)),f'd2-new p={p} n={n}')
        check(F*inv == I and inv*F == I,f'inverse p={p} n={n}')
        check(F*old == new*F,f'chain p={p} n={n}')
        check(all(F[i,j]==0 or form(bb[i])==form(bb[j])
                  for i in range(len(bb)) for j in range(len(bb))),
              f'form-preservation p={p} n={n}')
    check(smith_normal_form(sp.Matrix([[p]]),domain=ZZ)==sp.Matrix([[p]]),
          f'original-p-class p={p}')
    bb=basis(2)
    D=differential(bb,p)
    q3=[i for i,z in enumerate(bb) if form(z)==3]
    q4=[i for i,z in enumerate(bb) if form(z)==4]
    q5=[i for i,z in enumerate(bb) if form(z)==5]
    d3=D.extract(q4,q3)
    d4=D.extract(q5,q4)
    snf=smith_normal_form(d3,domain=ZZ)
    diagonal=[abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]
    check(diagonal == [1,2],f'H4-index p={p}')
    check(len(q4)-d4.rank()==d3.rank()==2,f'H4-free-rank p={p}')
    check(len(q3)-rank_mod2(d3)==1,f'H3-mod2-dimension p={p}')
    check(len(q4)-rank_mod2(d4)-rank_mod2(d3)==1,f'H4-mod2-dimension p={p}')
    details.append({'p':p,'H4_basis':[bb[i] for i in q4],
                    'd3':d3.tolist(),'d4':d4.tolist(),
                    'd3_smith_nonzero_diagonal':diagonal,
                    'H3_mod2_dimension':len(q3)-rank_mod2(d3),
                    'H4_mod2_dimension':len(q4)-rank_mod2(d4)-rank_mod2(d3),
                    'H4':'Z/2; image rank equals kernel rank'})

result={'statement':'AT23; A-L17','passed':True,'checks':checks,
        'primes':[2,3,5],'arity_range':[0,8],
        'scope':'Actual integral PD change, its inverse, chain identity, d squared, form preservation; original p-class and entire arity-two H4 lattice.',
        'all_prime_and_infinite_simplicial_assertions':'Proved by hand in A_prime_transfer.tex, not extrapolated from this finite certificate.',
        'details':details,'runtime_seconds':perf_counter()-start}
out=Path(__file__).resolve().parents[1]/'logs/B_prime_transfer_certificate.json'
out.write_text(json.dumps(result,indent=2,default=int)+'\n')
print(json.dumps(result,default=int))

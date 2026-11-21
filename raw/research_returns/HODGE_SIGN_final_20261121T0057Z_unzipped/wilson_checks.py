#!/usr/bin/env python3
"""Exact integer certificates for symplectic divided-power Lefschetz maps.
Independent matrices use subset incidence; compare their Smith normal forms
with Wilson's diagonal and aggregate all inert-coordinate blocks, n <= 6.
No input from an automorphic lift occurs here.
"""
from itertools import combinations
from math import comb, factorial
from collections import Counter
from pathlib import Path
import csv
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parent

def normalize_diagonal(vals):
    vals = [abs(int(x)) for x in vals]
    if not vals: return []
    assert all(vals)
    primes = sorted(set(p for x in vals for p in s.factorint(x)))
    out = [1]*len(vals)
    for p in primes:
        exps = sorted(int(s.factorint(x).get(p, 0)) for x in vals)
        out = [a*int(p)**e for a,e in zip(out,exps)]
    return out

def expand(c):
    return [k for k,v in c.items() for _ in range(v)]

def summary(vals):
    return ','.join(f'{a}^{b}' if b>1 else str(a) for a,b in sorted(Counter(vals).items()))

cache = {}
block_rows = []
for v in range(7):
    for t in range(v//2 + 1):
        k = v-t
        ts = list(combinations(range(v),t)); ks = list(combinations(range(v),k))
        M = s.Matrix([[int(set(a)<=set(b)) for b in ks] for a in ts])
        actual = [abs(int(x)) for x in smith_normal_form(M,domain=s.ZZ).diagonal()]
        predicted = []
        for r in range(t+1):
            predicted += [comb(k-r,t-r)]*(comb(v,r)-(comb(v,r-1) if r else 0))
        assert actual == normalize_diagonal(predicted), (v,t,k,actual,predicted)
        cache[v,t,k] = actual
        block_rows.append((v,t,k,len(ts),summary(predicted),summary(actual),'PASS'))
with (ROOT/'wilson_block_checks.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(['v','t','k','rank','Wilson_diagonal','Smith_normal_form','result']); w.writerows(block_rows)

rows=[]
for n in range(1,7):
    for i in range(n+1):
        m=n-i
        entries=[]
        for inert in range(i+1):
            if (i-inert)%2: continue
            t=(i-inert)//2; v=n-inert; k=t+m
            if not (0<=t<=k<=v): continue
            copies=comb(n,inert)*2**inert
            entries += cache[v,t,k]*copies
        expected_rank=comb(2*n,i)
        assert len(entries)==expected_rank
        snf=normalize_diagonal(entries)
        undiv=[factorial(m)*x for x in snf]
        index=s.prod(snf)
        fact='*'.join(f'{p}^{e}' if e>1 else str(p) for p,e in sorted(s.factorint(index).items())) or '1'
        rows.append((n,i,m,expected_rank,summary(snf),summary(undiv),fact,'PASS'))
with (ROOT/'wilson_lefschetz_checks.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(['n','source_degree_i','m=n-i','rank','SNF_divided','SNF_undivided','index_divided','result']); w.writerows(rows)
print('PASS: all',len(block_rows),'incidence matrices; all',len(rows),'hard-Lefschetz aggregates, n<=6.')
print((ROOT/'wilson_lefschetz_checks.tsv').read_text())

# Independent signed exterior-algebra construction, not the block decomposition.
def wedge_sign(a,b):
    if set(a)&set(b): return 0
    return (-1)**sum(x>y for x in a for y in b)

direct_rows=[]
for n in range(1,5):
    for i in range(n+1):
        m=n-i
        src=list(combinations(range(2*n),i))
        dst=list(combinations(range(2*n),i+2*m))
        index={b:j for j,b in enumerate(dst)}
        M=s.zeros(len(dst),len(src))
        for pairset in combinations(range(n),m):
            a=tuple(x for p in pairset for x in (2*p,2*p+1))
            for col,b in enumerate(src):
                sign=wedge_sign(a,b)
                if sign: M[index[tuple(sorted(a+b))],col] += sign
        actual=[abs(int(x)) for x in smith_normal_form(M,domain=s.ZZ).diagonal()]
        row=next(r for r in rows if r[0]==n and r[1]==i)
        assert summary(actual)==row[4],(n,i,summary(actual),row[4])
        direct_rows.append((n,i,m,len(src),summary(actual),'PASS'))
with (ROOT/'wilson_exterior_direct_checks.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(['n','i','m','rank','direct_exterior_SNF','result']); w.writerows(direct_rows)
print('PASS: direct signed exterior matrices match all',len(direct_rows),'aggregates for n<=4.')

# Same rational SL2 representation, two fully specified stable integral lattices.
# Basis indexed r=0,...,d is x^(d-r)y^r in the first lattice and
# binomial(d,r)x^(d-r)y^r in the second. Raising is x*d/dy.
sl2_rows=[]
for m in range(1,4):
    d=m+1
    em=s.zeros(d+1)
    eb=s.zeros(d+1)
    for r in range(1,d+1):
        em[r-1,r]=r
        eb[r-1,r]=d-r+1
    ordinary=(int((em**m)[1,d]),int((eb**m)[1,d]))
    divided=tuple(x//factorial(m) for x in ordinary)
    assert ordinary==(factorial(m+1),factorial(m))
    assert divided==(m+1,1)
    sl2_rows.append((m,d,ordinary[0],ordinary[1],divided[0],divided[1],'PASS'))
with (ROOT/'sl2_lattice_checks.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t')
    w.writerow(['m','Sym_degree','ordinary_monomial','ordinary_binomial','divided_monomial','divided_binomial','result'])
    w.writerows(sl2_rows)
print('PASS: three integral SL2-lattice comparisons, m=1,2,3.')

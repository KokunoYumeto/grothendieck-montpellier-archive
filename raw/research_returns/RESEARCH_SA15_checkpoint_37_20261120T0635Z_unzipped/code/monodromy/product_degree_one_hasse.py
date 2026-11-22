#!/usr/bin/env python3
"""Exact symbolic Hasse determinant of the degree-one product family.
Polynomial terms are packed exponent vectors, computed by subset DP
for the determinant in characteristic two; no generic group assertion.
"""
import importlib.util,json,time
from pathlib import Path
import sympy as sp
start=time.perf_counter()
src=Path(__file__).with_name('product_degree_one_spectrum.py')
ns={}
exec(src.read_text().split('hist={};')[0],ns)
Ms=ns['matrices']
entries=[[[k for k in range(9) if Ms[k][i][j]] for j in range(9)]
         for i in range(9)]
dp={0:{0}}
for i in range(9):
    nxt={}
    for mask,P in dp.items():
        for j in range(9):
            if mask>>j&1:continue
            Q=nxt.setdefault(mask|1<<j,set())
            for k in entries[i][j]:
                e=1<<(4*k)
                for m in P:
                    z=m+e
                    if z in Q:Q.remove(z)
                    else:Q.add(z)
    dp=nxt
terms=sorted(dp[511]);c=sp.symbols('c0:9')
poly=sum(sp.prod(c[i]**((m>>(4*i))&15) for i in range(9)) for m in terms)
out=Path(__file__).resolve().parents[1]/'outputs'
(out/'product_degree_one_hasse_polynomial.txt').write_text(str(poly)+'\n')
result={'variables':[str(x) for x in c],'degree':9,'number_of_terms':len(terms),
        'packed_terms':terms,'packing_bits_per_exponent':4,
        'polynomial':str(poly),'runtime_seconds':time.perf_counter()-start}
(out/'product_degree_one_hasse.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['packed_terms','polynomial']},indent=2))

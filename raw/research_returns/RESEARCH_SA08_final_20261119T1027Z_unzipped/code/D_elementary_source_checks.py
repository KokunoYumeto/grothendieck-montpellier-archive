#!/usr/bin/env python3
"""Finite arithmetic and bar-homology checks supporting D022 (not its proof)."""
from pathlib import Path
from math import factorial,comb
import json,time
start=time.perf_counter()
checks=0
records=[]
for p in (2,3,5):
    for e in (0,1,2):
        N=p**e
        count=0
        for m in range(9):
            c=factorial(m*N)//(factorial(m)*factorial(N)**m)
            for r in range(N):
                assert (c*comb(m*N+r,r))%p !=0
                checks+=1;count+=1
        # H=Fp[y]/y^p with trivial action on V=Fp^N.  Reduced bar d1=0;
        # image d2 is the span of y^j for 2<=j<p, independently in each V slot.
        nonzero_products={a+b for a in range(1,p) for b in range(1,p) if a+b<p}
        assert nonzero_products==set(range(2,p));checks+=1
        bar_c1=N*(p-1)
        rank_d2=N*len(nonzero_products)
        H1=bar_c1-rank_d2
        assert H1==N;checks+=1
        records.append({'p':p,'N':N,'free_basis_coefficients_checked':count,
                        'bar_C1_rank':bar_c1,'bar_d2_rank':rank_d2,'bar_H1_rank':H1})
result={'statements':['D022','D023'],'scope':'Finite arithmetic and normalized-bar checks only; unbounded persistence proved symbolically in D_Cintegral_source_obstruction.tex',
        'records':records,'assertions_passed':checks,'elapsed_seconds':time.perf_counter()-start}
p=Path(__file__).resolve().parents[1]/'logs/D_elementary_source_checks.json'
p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

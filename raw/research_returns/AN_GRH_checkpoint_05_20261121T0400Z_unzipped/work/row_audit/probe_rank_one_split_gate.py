#!/usr/bin/env python3
"""Finite exact checks for the split F4 model's proposed all-extension barrier.

Uses the factorization P4=(T^2+3T+4)(T^2+4).
The universal large-m comparison is a separate written proof.
"""
import json
from pathlib import Path

def factors(n):
    result={}
    d=2
    while d*d<=n:
        while n%d==0:
            result[d]=result.get(d,0)+1
            n//=d
        d=3 if d==2 else d+2
    if n>1:result[n]=result.get(n,0)+1
    return result

def primitive2(r):
    return r>2 and all(pow(2,(r-1)//d,r)!=1 for d in factors(r-1))

def main():
    to=[2,-3]; ts=[2,0]
    for _ in range(2,41):
        to.append(-3*to[-1]-4*to[-2])
        ts.append(-4*ts[-2])
    rows=[]
    for m in range(1,11):
        q=4**m; eo=q+1-to[m]; es=q+1-ts[m]; N=q+1-to[m]-ts[m]
        assert eo%8==0
        fo=factors(eo); fs=factors(es)
        fac={r:fo.get(r,0)+fs.get(r,0) for r in set(fo)|set(fs)}
        good=[]
        for r,v in sorted(fac.items()):
            if primitive2(r):
                upper=r**min(4,v)
                good.append(dict(r=r,valuation=v,V_upper=upper,N=N,
                                 sufficient_upper_bound_passes=upper<=N,
                                 in_ordinary_factor=r in fo,in_supersingular_factor=r in fs))
        rows.append(dict(m=m,Q=q,N=N,ordinary_factor=eo,supersingular_factor=es,
                         ordinary_trace=to[m],supersingular_trace=ts[m],factors=fac,primitive2_primes=good))
    large_anchor={"m":11,"rank_upper":45**4,"N_lower":4**11+1-4*2**11}
    assert large_anchor['rank_upper']<large_anchor['N_lower']
    assert 49**4<2*45**4
    out={"scope":"Exact counts/factors for1<=m<=10 and monotone large-m anchor; valuation upper bounds may require strengthening if flagged.","rows":rows,"large_m_anchor":large_anchor,
         "all_small_valuation_upper_bounds_suffice":all(p['sufficient_upper_bound_passes'] for row in rows for p in row['primitive2_primes'])}
    path=Path(__file__).with_name('RANK_ONE_SPLIT_GATE_PROBE.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()

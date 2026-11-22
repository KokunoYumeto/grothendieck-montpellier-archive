"""Exact generic dual-contraction Pfaffians in odd-prime Schrödinger coordinates.
Retained exploratory algebra only; no geometric realization or theorem is inferred.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
import json,time
started=time.perf_counter()

def matchings(items):
    if not items:
        yield ()
        return
    i=items[0]
    for q in range(1,len(items)):
        j=items[q]
        for rest in matchings(items[1:q]+items[q+1:]):
            yield ((i,j),)+rest

def pfaffian(n):
    m=(n-1)//2; inv2=(n+1)//2
    coeffs=defaultdict(set)
    count=0
    for matching in matchings(tuple(range(1,n))):
        cy=[0]*m; yy=[0]*n
        for i,j in matching:
            a=(i-j)%n; d=min(a,n-a)
            cy[d-1]+=1; yy[((i+j)*inv2)%n]+=1
        key=tuple(yy); mon=tuple(cy)
        if mon in coeffs[key]: coeffs[key].remove(mon)
        else: coeffs[key].add(mon)
        count+=1
    coeffs={key:sorted(v) for key,v in coeffs.items() if v}
    pure=[]
    for d in range(m):
        mon=tuple(m if j==d else 0 for j in range(m))
        occurrences=[{'y':list(y),'c_terms':[list(c) for c in cs]} for y,cs in coeffs.items() if mon in cs]
        pure.append({'distance':d+1,'pure_power_occurrences':occurrences,'has_isolated_pure_power':any(len(row['c_terms'])==1 for row in occurrences)})
    small_coeffs=[{'y':list(y),'c_terms':[list(c) for c in cs]} for y,cs in coeffs.items()] if n<=7 else None
    return {'n':n,'matching_count':count,'nonzero_y_coefficients':len(coeffs),'full_polynomial_terms':sum(map(len,coeffs.values())),'pure_powers':pure,'small_full_coefficients':small_coeffs}

rows=[pfaffian(n) for n in (3,5,7,11,13)]
result={'status':'EXACT-EXPLORATORY-PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-started,'results':rows,'scope':'Exact Pfaffian of B_y with index0 deleted over F2[c_1,...,c_m,y_0,...,y_(n-1)]. Pure-power occurrence is a coefficient fact, not yet a proof of parameter-locus emptiness.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'actual_utc':result['actual_utc'],'runtime_seconds':result['runtime_seconds'],'rows':[{'n':r['n'],'matching_count':r['matching_count'],'terms':r['full_polynomial_terms'],'isolated_distances':[a['distance'] for a in r['pure_powers'] if a['has_isolated_pure_power']]} for r in rows]}))

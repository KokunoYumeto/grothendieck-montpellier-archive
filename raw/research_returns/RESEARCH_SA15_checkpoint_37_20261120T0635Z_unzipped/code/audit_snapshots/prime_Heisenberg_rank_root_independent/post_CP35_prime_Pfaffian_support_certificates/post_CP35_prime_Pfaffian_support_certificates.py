"""Exact support-wise monomial witnesses for prime alternating Schrödinger pencils."""
from pathlib import Path
from datetime import datetime,timezone
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

def certificate(n):
    m=(n-1)//2; inv2=(n+1)//2
    coeffs=defaultdict(set)
    for matching in matchings(tuple(range(1,n))):
        ce=[0]*m; ye=[0]*n
        for i,j in matching:
            d=(i-j)%n; d=min(d,n-d)
            ce[d-1]+=1;ye[((i+j)*inv2)%n]+=1
        y=tuple(ye);c=tuple(ce)
        if c in coeffs[y]:coeffs[y].remove(c)
        else:coeffs[y].add(c)
    coeffs={y:cs for y,cs in coeffs.items() if cs}
    data=[(y,[(sum(1<<i for i,e in enumerate(c) if e),c) for c in cs]) for y,cs in coeffs.items()]
    witnesses=[];remaining=[]
    for mask in range(1,1<<m):
        witness=None
        for y,terms in data:
            alive=[c for cm,c in terms if cm&~mask==0]
            if len(alive)==1:
                witness={'support_mask':mask,'nonzero_distances':[i+1 for i in range(m) if mask>>i&1],'y_monomial':list(y),'surviving_c_monomial':list(alive[0])}
                break
        if witness:witnesses.append(witness)
        else:remaining.append(mask)
    return {'n':n,'coefficient_count':len(coeffs),'polynomial_term_count':sum(map(len,coeffs.values())),'support_count':(1<<m)-1,'monomial_witnesses':witnesses,'uncovered_supports':remaining,'all_supports_proved':not remaining}

rows=[certificate(n) for n in (3,5,7,11,13)]
record={'status':'PASS' if all(r['all_supports_proved'] for r in rows) else 'PARTIAL-SUPPORT-CERTIFICATE','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-started,'results':rows,'scope':'For each recorded support every listed c is assumed nonzero and all other c vanish. An actual single surviving coefficient monomial certifies nonzero Pfaffian over every characteristic-two field. Uncovered supports would remain unresolved; no finite-field extrapolation.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'actual_utc':record['actual_utc'],'runtime_seconds':record['runtime_seconds'],'rows':[{'n':r['n'],'support_count':r['support_count'],'witness_count':len(r['monomial_witnesses']),'uncovered':r['uncovered_supports']} for r in rows]}))

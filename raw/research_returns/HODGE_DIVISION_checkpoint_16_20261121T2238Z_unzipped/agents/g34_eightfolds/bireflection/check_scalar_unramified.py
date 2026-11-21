"""Exact arithmetic for D-BI13, D-BI14 and the full GS corollary."""
from pathlib import Path
from math import isqrt
import json
HERE=Path(__file__).resolve().parent
rows=[]
for p in [7,11,19,43,67,163]:
    d=p-1
    for e in range(5,9):assert 2*e-2*(e//d)+10>2*e+6
    Q=(5*d-2)//4
    assert 4*Q==5*d-2
    threshold=d*(25*d-22)//4
    assert threshold==d*(5*Q-3)
    assert all(4*q*q-1<d*(5*q-3) for q in range(1,Q))
    assert 4*(Q-1)**2<=threshold<4*Q*Q
    assert isqrt(threshold)//2+1==Q
    assert threshold//d>=5*Q-3
    rows.append({'p':p,'q2_bound':7*d,'q3_bound':12*d,
                 'GS_q_at_threshold':Q,'full_GS_bound':threshold,
                 'all_smaller_q_checked':Q-1})
assert [r['full_GS_bound'] for r in rows]==[192,570,1926,10794,26862,163134]
out={'status':'PASS','rows':rows,
     'scope':'Exact finite arithmetic only; published GS classification and the universal geometric/field proofs remain written premises. No existence at a threshold is claimed.'}
(HERE/'check_scalar_unramified.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'full_GS_bounds':[r['full_GS_bound'] for r in rows]}))

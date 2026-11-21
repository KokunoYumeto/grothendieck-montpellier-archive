#!/usr/bin/env python3
"""Exact local determinant invariants for the enumerated Gaussian F4 normalizer."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json
from check_e6_e7 import local,M
HERE=Path(__file__).resolve().parent
raw=json.loads((HERE/'F4_gaussian_classes.json').read_text())
rows=[]
for item in raw['classes']:
    a=item['representative'];g=[[M.F(Q(a[2*(4*j+k)],2),Q(a[2*(4*j+k)+1],2))for k in range(4)]for j in range(4)]
    assert M.mul(M.star(g),g)==M.eye(4)
    d=local(g,M.eye(4),item['order'])
    # The four cosets of W(F4) have scalar phases 0, pi/2, pi/4, 3pi/4.
    nonzero=next(z for r in g for z in r if z)
    if not nonzero.b:phase=0
    elif not nonzero.a:phase=2
    elif nonzero.a==nonzero.b:phase=1
    elif nonzero.a==-nonzero.b:phase=3
    else:raise AssertionError('phase')
    assert all(not z or ((phase==0 and not z.b)or(phase==2 and not z.a)or(phase==1 and z.a==z.b)or(phase==3 and z.a==-z.b))for r in g for z in r)
    rows.append(dict(item,phase_coset=phase,**d))
assert sum(r['size']for r in rows)==4608
out={'status':'PASS','all_exact_checks':True,'group_order':4608,'class_count':len(rows),'classes':rows,
     'minimum_moving_rank_by_phase':{str(k):min(r['moving_rank']for r in rows if r['phase_coset']==k and r['order']>1)for k in range(4)},
     'nonnorm_classes':[{k:r[k]for k in ['index','size','order','phase_coset','moving_rank','normalized_positive_local_q','age_imbalance']}for r in rows if not r['is_norm']]}
(HERE/'F4_gaussian_local_invariants.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['status','class_count','minimum_moving_rank_by_phase','nonnorm_classes']}))

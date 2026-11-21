#!/usr/bin/env python3
import json,pathlib,sys,numpy as np
HERE=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE.parent/'pentagon'))
from krammer_f9_probe import to3
from krammer_first_pair import mul,inv
j=json.loads((HERE/'records/krammer_mixed_correlation.json').read_text());raw=lambda a:to3(np.array(a)).astype(np.int16)
a,b=[raw(x) for x in j['X_matrices'][3:]];ai,bi=inv(a),inv(b)
C,Q=raw(j['C_full']),raw(j['Q_full']);Ci,Qi=inv(C),inv(Q)
sol=np.load(HERE.parent/'pentagon/krammer_pentagon_solutions.npz');I=np.eye(12,dtype=np.int16)
rows=[];counts={}
for ind,(R,lab) in enumerate(zip(sol['R'],sol['labels'])):
 R=R.astype(np.int16);r=mul(mul(Ci,R),C);ri=inv(r)
 # A=f(a,b), B=f(b,c), Cval=f(c,a)=r, c=(ab)^-1.
 A=mul(mul(mul(Qi,r),Q),ri);B=mul(mul(Qi,ri),Q)
 assert np.array_equal(mul(mul(r,B),A),I)
 rev=mul(mul(mul(mul(mul(mul(b,inv(B)),bi),ai),ri),a),inv(A))
 ok=np.array_equal(rev,I)
 label=tuple(map(int,lab));counts.setdefault(str(label),[0,0]);counts[str(label)][int(ok)]+=1
 rows.append({'solution_index':ind,'label':list(label),'reverse_cycle_pass':bool(ok)})
print(json.dumps({'counts_fail_pass':counts,'pass':sum(r['reverse_cycle_pass'] for r in rows)},indent=2))
(HERE/'records/krammer_reverse_cycle.json').write_text(json.dumps({'counts_fail_pass':counts,'rows':rows},indent=2)+'\n')

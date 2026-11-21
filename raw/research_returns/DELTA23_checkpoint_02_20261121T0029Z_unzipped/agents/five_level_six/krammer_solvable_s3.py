#!/usr/bin/env python3
"""Full common-word S3 Nielsen closure of both solvable mixed Krammer blocks."""
from pathlib import Path
import sys,json
from collections import deque
import numpy as np

HERE=Path(__file__).resolve().parent
PENT=HERE.parent/'pentagon';sys.path.insert(0,str(PENT))
from krammer_f9_probe import to3
from krammer_first_pair import inv
DATA=json.loads((HERE.parent/'characters/records/krammer_mixed_correlation.json').read_text())

def key(m):return m.astype(np.uint8).tobytes()
def model(raw):
    gs=[to3(np.array(m,dtype=np.int16)).astype(np.int16) for m in raw]
    I=np.eye(6,dtype=np.int16);els=[I];where={key(I):0}
    for a in els:
        for b in gs:
            c=a@b%3;k=key(c)
            if k not in where:where[k]=len(els);els.append(c)
    assert len(els)==108
    table=np.array([[where[key(a@b%3)] for b in els] for a in els],dtype=np.int16)
    inverses=np.array([int(np.flatnonzero(table[a]==0)[0]) for a in range(108)],dtype=np.int16)
    a,b=[where[key(g)] for g in gs];z=int(inverses[table[a,b]])
    pairs=[(a,b),(b,z),(z,a),(b,a),(z,b),(a,z)]
    return els,where,table,inverses,pairs

models=[model(row['solvable_generators']) for row in DATA['pairs']]
tables=np.array([m[2] for m in models for _ in range(6)])
inverses=np.array([m[3] for m in models for _ in range(6)])
indices=np.arange(12)
X=tuple(p[0] for m in models for p in m[4]);Y=tuple(p[1] for m in models for p in m[4])
I=(0,)*12
def mul(a,b):return tuple(map(int,tables[indices,a,b]))
def inverse(a):return tuple(map(int,inverses[indices,a]))
def conj(a,b):return mul(mul(a,b),inverse(a))
comm=mul(mul(mul(X,Y),inverse(X)),inverse(Y))
orbit=[comm];oseen={comm}
for a in orbit:
    for b in [X,Y,inverse(X),inverse(Y)]:
        c=conj(b,a)
        if c not in oseen:oseen.add(c);orbit.append(c)
derived={I};generators=[]
for a in orbit:
    if a in derived:continue
    generators.extend([a,inverse(a)])
    todo=deque(derived)
    while todo:
        b=todo.popleft()
        for g in generators:
            c=mul(b,g)
            if c not in derived:derived.add(c);todo.append(c)
print('joint derived',len(derived),'commutator orbit',len(orbit),'generators',len(generators)//2,flush=True)
def gentle(a):
    for off,m in zip([0,6],models):
        tab,iv=m[2],m[3]
        for j in range(3):
            if a[off+j+3]!=int(iv[a[off+j]]):return False
        if tab[tab[a[off+2],a[off+1]],a[off]]!=0:return False
    return True
passed=[a for a in derived if gentle(a)]
allowed={(a[0],a[6]) for a in passed}
print('gentle tuples',len(passed),'allowed base pairs',len(allowed),flush=True)

# Compare literal original 216 pentagon assignments, after taking their
# two faithful solvable diagonal blocks in the published splitting bases.
rec=np.load(PENT/'krammer_pentagon_solutions.npz')
C=to3(np.array(DATA['C_full'],dtype=np.int16)).astype(np.int16)
Q=to3(np.array(DATA['Q_full'],dtype=np.int16)).astype(np.int16)
Ci=inv(C);Qi=inv(Q)
bases=[to3(np.array(row['splitting_basis'],dtype=np.int16)).astype(np.int16) for row in DATA['pairs']]
binvs=[inv(b) for b in bases]
counts={};failures=[]
for k,(R,label) in enumerate(zip(rec['R'],rec['labels'])):
    R=R.astype(np.int16);r=Ci@R@C%3
    R45=Qi@r@Q@inv(r)%3
    blocks=[(bi@a@b%3)[:6,:6] for bi,a,b in zip(binvs,[R,R45],bases)]
    pair=tuple(models[j][1][key(blocks[j])] for j in range(2))
    lab=','.join(map(str,map(int,label)))
    counts.setdefault(lab,[0,0]);counts[lab][0]+=1
    if pair in allowed:counts[lab][1]+=1
    else:failures.append({'index':k,'label':label.tolist(),'solvable_pair':pair})
out={'statement':'D23.F24','marked_pair_order':['34 id','34 tau','34 tau2','34 swap','34 swap_tau','34 swap_tau2','45 id','45 tau','45 tau2','45 swap','45 swap_tau','45 swap_tau2'],
     'joint_derived_order':len(derived),'commutator_orbit':len(orbit),'derived_generators':len(generators)//2,
     'gentle_tuples':len(passed),'allowed_base_pairs':len(allowed),'candidate_counts_total_passed':counts,'failures':failures}
(HERE/'krammer_solvable_s3.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(HERE/'krammer_solvable_s3.npz',gentle_tuples=np.array(passed,dtype=np.int16),allowed_base_pairs=np.array(sorted(allowed),dtype=np.int16))
print(json.dumps(out,indent=2),flush=True)

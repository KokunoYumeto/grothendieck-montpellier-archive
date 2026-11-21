#!/usr/bin/env python3
"""Full common-word S3 Nielsen closure of both solvable mixed Krammer blocks."""
from pathlib import Path
import sys,json
from collections import deque
import numpy as np

HERE=Path(__file__).resolve().parent
PENT=HERE.parent/'pentagon';sys.path.insert(0,str(PENT))
from krammer_f9_probe import to3,matrices,mp
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
        x,y=m[4][0];z=m[4][1][1]
        def product(seq):
            v=0
            for c in seq:v=int(tab[v,c])
            return v
        # Right composition with (-1,1) gives the second actual-source
        # three-cycle, with m=-1 and the same f.
        if product([a[off+2],iv[z],a[off+1],iv[y],a[off],iv[x]]):return False
        # The reversed cycle has inner corrections; retain them explicitly.
        h0=a[off+3]
        h1=product([iv[x],a[off+5],x])
        h2=product([y,a[off+4],iv[y]])
        zr=int(iv[tab[y,x]])
        if product([h2,h1,h0]):return False
        if product([h2,iv[zr],h1,iv[x],h0,iv[y]]):return False
    return True
passed=[a for a in derived if gentle(a)]
allowed={(a[0],a[6]) for a in passed}
print('gentle tuples',len(passed),'allowed base pairs',len(allowed),flush=True)

# First-pair cyclic Nielsen values are conjugates modulo its B3 centre.
k1,k2,_=[to3(m).astype(np.int16) for m in matrices(4,3,6)]
x=mp(k1,2);y=mp(k2,2);delta=k1@k2%3;di=inv(delta);z3=mp(delta,3)
z=inv(x@y%3);eye=np.eye(12,dtype=np.int16)
assert np.array_equal(delta@x@di%3,y)
assert np.array_equal(delta@y@di%3,z3@z%3)
first=np.load(HERE/'krammer_six_first_pair.npz');first_cases=[]
for f,label in zip(first['candidates'],first['labels']):
    f1=delta@f@di%3;f2=mp(delta,2)@f@inv(mp(delta,2))%3
    assert np.array_equal(f2@f1@f%3,eye)
    assert np.array_equal(f2@inv(z)@f1@inv(y)@f@inv(x)%3,eye)
    first_cases.append({'label':label.tolist(),'m0':True,'m_minus1':True})

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
     'gentle_tuples':len(passed),'allowed_base_pairs':len(allowed),'m_minus1_and_reversed_cycles_checked':True,
     'first_pair_cases':first_cases,'candidate_counts_total_passed':counts,'failures':failures}
(HERE/'krammer_solvable_s3.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(HERE/'krammer_solvable_s3.npz',gentle_tuples=np.array(passed,dtype=np.int16),allowed_base_pairs=np.array(sorted(allowed),dtype=np.int16))
print(json.dumps(out,indent=2),flush=True)

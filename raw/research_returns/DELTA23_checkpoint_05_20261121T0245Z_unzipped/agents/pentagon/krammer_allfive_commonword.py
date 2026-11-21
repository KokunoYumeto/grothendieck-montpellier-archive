#!/usr/bin/env python3
"""Exact certificates for D23.P9: the remaining common-word correlations."""
import json,pathlib
import numpy as np
from krammer_f9_probe import to3
from krammer_first_pair import closure_commutator
from krammer_commonword_witness import ev

HERE=pathlib.Path(__file__).parent
data=json.loads((HERE.parent/'characters/records/krammer_mixed_correlation.json').read_text())
u=[[to3(np.array(g)).astype(np.int16) for g in row['unitary_generators']] for row in data['pairs']]
umaps=[u[0],u[1],u[0][::-1]]
w1=json.loads((HERE/'krammer_commonword_witness.json').read_text())['word']
w2=json.loads((HERE/'krammer_swap_witness.json').read_text())['word']
identity=np.eye(6,dtype=np.int16)
v1=[np.array_equal(ev(g,w1),identity) for g in umaps]
v2=[np.array_equal(ev(g,w2),identity) for g in umaps]
assert v1==[True,False,False]
assert v2[1] and not v2[2]
for w in [w1,w2]:assert all(sum(1 if j==a else -1 if j==-a else 0 for j in w)==0 for a in [1,2])
h=[[to3(np.array(g)).astype(np.int16) for g in row['solvable_generators']] for row in data['pairs']]
hmaps=[h[0],h[1],h[0][::-1]];xy=[]
for j in range(2):
    m=np.zeros((18,18),dtype=np.int16)
    for r in range(3):m[r*6:(r+1)*6,r*6:(r+1)*6]=hmaps[r][j]
    xy.append(m)
ds,_,oc,ng=closure_commutator(*xy)
assert len(ds)==27**3
out={'statement':'D23.P9','block_order':['34','45','43'],'unitary_witness1_word':w1,'unitary_witness1_identity_pattern':[bool(v) for v in v1],'unitary_witness2_word':w2,'unitary_witness2_identity_pattern':[bool(v) for v in v2],'solvable_joint_derived_order':len(ds),'commutator_orbit':oc,'derived_generator_count':ng,'result':'PASS; pairwise simple kernels differ and solvable derived image is full27^3.'}
HERE.joinpath('krammer_allfive_commonword.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)

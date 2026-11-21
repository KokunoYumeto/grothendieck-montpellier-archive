"""Independent original-factor checks for D23.P7 and small F14/F15 identities."""
from pathlib import Path
import sys, json
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work/agents/pentagon'
sys.path.insert(0,str(P))
from krammer_f9_probe import to3, matrices
from krammer_first_pair import mul, inv
raw=lambda x:to3(np.array(x)).astype(np.int16)
z=json.loads((ROOT/'work/agents/characters/records/krammer_mixed_correlation.json').read_text())
C,Q=raw(z['C_full']),raw(z['Q_full']);Ci,Qi=inv(C),inv(Q)
a,b,c=map(raw,matrices(4,3,6))
J=mul(mul(mul(mul(mul(a,b),c),a),b),a);Ji=inv(J)
eye=np.eye(12,dtype=np.int16)
assert np.array_equal(mul(J,J),2*eye%3)
for g,h in [(a,c),(b,b),(c,a)]:assert np.array_equal(mul(J,g),mul(h,J))
fs=np.load(ROOT/'work/agents/five_level_six/krammer_six_first_pair.npz')
fm={tuple(map(int,k)):v.astype(np.int16) for k,v in zip(fs['labels'],fs['candidates'])}
sol=np.load(P/'krammer_pentagon_solutions.npz')
counts={k:0 for k in fm}
for r0,label in zip(sol['R'],sol['labels']):
    R=r0.astype(np.int16);F=fm[tuple(map(int,label))]
    r=mul(mul(Ci,R),C)
    H=mul(mul(mul(Qi,r),Q),inv(r))
    factors=[R,mul(mul(J,inv(R)),Ji),mul(mul(J,inv(F)),Ji),H,F]
    value=eye.copy()
    for factor in factors:value=mul(value,factor)
    assert np.array_equal(value,eye)
    counts[tuple(map(int,label))]+=1
assert set(counts.values())=={36}
h34=list(map(raw,z['pairs'][0]['solvable_generators']))
h45=list(map(raw,z['pairs'][1]['solvable_generators']))
comm=lambda x,y:mul(mul(mul(x,y),inv(x)),inv(y))
assert np.array_equal(comm(mul(h34[0],h34[0]),h34[1]),np.eye(6,dtype=np.int16))
w45=comm(mul(h45[0],h45[0]),h45[1])
assert not np.array_equal(w45,np.eye(6,dtype=np.int16))
expected=raw([[6,0,5],[0,1,1],[5,0,5]])
assert np.array_equal(w45,expected)
out={'result':'PASS','original_five_factor_products_checked':len(sol['R']),'counts':{str(k):v for k,v in counts.items()},'reversing_half_twist':'all three generator identities checked','F15_short_witness':'literal matrix checked'}
(ROOT/'work/records/root_krammer_original.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))

"""Probe whether the commutation-form rank survives a non-Clifford LU pair.

The explicit pair is Ji--Chen--Wei--Ying, arXiv0709.1266v2,
printed pp9--10, equations18--21. The local phase identity is checked
directly on all64 support points. No claim of LC inequivalence is used.
"""
from pathlib import Path
import json,hashlib,random
import numpy as np

W=Path(__file__).resolve().parents[1]
P=W/'inputs/rt_lu_rank_probe.json';cfg=json.loads(P.read_text())
G=np.array([[int(c)for c in s]for s in cfg['basis']],dtype=np.uint8)
n=G.shape[1];assert G.shape==(6,27)
Q=np.zeros((n,n),dtype=np.uint8)
for i,j in cfg['quadratic_edges_one_based']:Q[i-1,j-1]=Q[j-1,i-1]=1
phase=cfg['phase_exponents_mod8']
support=[]
for h in range(64):
    x=np.zeros(n,dtype=np.uint8)
    for i in range(6):
        if h>>i&1:x^=G[i]
    q=sum(int(x[i-1])*int(x[j-1])for i,j in cfg['quadratic_edges_one_based'])%2
    assert sum(a*int(b)for a,b in zip(phase,x))%8==4*q
    support.append(''.join(map(str,x.tolist())))
assert len(set(support))==64

R=G.copy();piv=[];k=0
for c in range(n):
    hits=[i for i in range(k,6)if R[i,c]]
    if not hits:continue
    i=hits[0];R[[i,k]]=R[[k,i]]
    for j in range(6):
        if j!=k and R[j,c]:R[j]^=R[k]
    piv.append(c);k+=1
    if k==6:break
assert k==6
H=[]
for c in range(n):
    if c in piv:continue
    h=np.zeros(n,dtype=np.uint8);h[c]=1
    for i,j in enumerate(piv):h[j]=R[i,c]
    H.append(h)
H=np.array(H);assert not np.any(G@H.T%2)
X=np.vstack((G,np.zeros_like(H)))
Z0=np.vstack((np.zeros_like(G),H))
Z1=np.vstack((G@Q%2,H))
def forms(Z):
    out=np.array([np.outer(X[:,v],Z[:,v])^np.outer(Z[:,v],X[:,v])for v in range(n)],dtype=np.uint8)
    assert not np.any(np.bitwise_xor.reduce(out,axis=0))
    return out
C0,C1=forms(Z0),forms(Z1)

def rank(A):
    rows=[int.from_bytes(bytes(r),'little')for r in np.packbits(A,axis=1,bitorder='little')]
    piv={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)

def evaluate(Ps):
    d=Ps.shape[1]
    return [rank((np.einsum('vab,vij->aibj',Ps,C)%2).reshape(d*n,d*n))for C in(C0,C1)]

rng=np.random.default_rng(cfg['seed']);records=[];witness=None
def check(Ps,kind):
    global witness
    ranks=evaluate(Ps);records.append({'kind':kind,'d':len(Ps[0]),'ranks':ranks})
    if ranks[0]!=ranks[1]:
        witness={'kind':kind,'d':len(Ps[0]),'ranks':ranks,'matrices':Ps.tolist()}
        return True
    return False

for d in range(2,9):
    J=np.eye(d,dtype=np.uint8)
    for i in range(d-1):J[i,i+1]=1
    powers=[np.eye(d,dtype=np.uint8)]
    for i in range(7):powers.append(powers[-1]@J%2)
    if check(np.array([powers[e]for e in phase]),'phase-unipotent'):break
if witness is None:check(np.array([np.outer(G[:,v],G[:,v])for v in range(n)]),'column-outer')
for trial in range(cfg['trials']):
    if witness is not None:break
    d=(2,3,4,6)[trial%4];kind=trial%3
    if kind==0:
        Ps=rng.integers(0,2,size=(n,d,d),dtype=np.uint8)
    elif kind==1:
        coeff=rng.integers(0,2,size=(6,d,d),dtype=np.uint8)
        Ps=np.einsum('iv,iab->vab',G,coeff)%2
    else:
        A=rng.integers(0,2,size=(d,6),dtype=np.uint8)@G%2
        B=rng.integers(0,2,size=(d,6),dtype=np.uint8)@G%2
        Ps=np.array([np.outer(A[:,v],B[:,v])for v in range(n)])
    check(Ps,('uniform','linear-column','outer-column')[kind])
out={'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
     'local_phase_identity':'PASS all64 support points modulo8',
     'stabilizer_dimension':n,'nullspace_dimension':len(H),'witness':witness,
     'trials_checked':len(records),'records':records,
     'status':'FOUND exact rank difference'if witness else'NO WITNESS in specified finite probe; no invariance theorem'}
dest=W/'outputs/rt_lu_rank_probe.json';tmp=dest.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(dest)
print(json.dumps({k:v for k,v in out.items()if k not in('records','witness')},indent=2))
if witness:print(json.dumps({k:v for k,v in witness.items()if k!='matrices'}))

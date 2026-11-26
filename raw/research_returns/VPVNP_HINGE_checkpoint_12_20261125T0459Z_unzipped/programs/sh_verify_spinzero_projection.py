"""Exact Q(i) verification of the r4 mixed-sector spin-zero projector.

Checks all 256 entries of the 24-term group average, all local intertwiner
entries, and integer projected target/crown arrays.  This is a projector
certificate, not a graph-cover identity.
"""
from pathlib import Path
import hashlib,itertools,json
import numpy as np
import sympy as sp

W=Path(__file__).resolve().parents[1]
ip=W/'inputs/sh_spinzero_projection.json';cfg=json.loads(ip.read_text())
I=sp.I
qs=[]
for i in range(4):
    for sign in (-1,1):
        v=[sp.Integer(0)]*4;v[i]=sp.Integer(sign);qs.append(v)
qs += [[sp.Rational(s,2) for s in signs] for signs in itertools.product((-1,1),repeat=4)]
gs=[sp.Matrix([[a+b*I,c+d*I],[-c+d*I,a-b*I]]) for a,b,c,d in qs]
assert len(gs)==24
assert all(sp.expand(g.det())==1 and (g.conjugate().T*g-sp.eye(2)).applyfunc(sp.expand)==sp.zeros(2) for g in gs)

def kp(g,n):
    ans=sp.ones(1)
    for _ in range(n):ans=sp.kronecker_product(ans,g)
    return ans

epsilon=sp.Matrix([[0,1],[-1,0]])
vectors=[]
for pairs in (((0,1),(2,3)),((0,2),(1,3))):
    vectors.append(sp.Matrix([sp.prod(epsilon[b[i],b[j]] for i,j in pairs)
                              for b in itertools.product(range(2),repeat=4)]))
B=sp.Matrix.hstack(*vectors)
P=B*(B.T*B).inv()*B.T
average=sp.zeros(16)
for g in gs:average+=kp(g,4)
average=average.applyfunc(sp.expand)/24
assert average==P and P*P==P and P.rank()==2

# Physical port index in this local check is b0*4+b1*2+b2.
R=sp.zeros(4,8)
for row,entries in enumerate(([(1,1),(2,-1)],[(2,1),(4,-1)],
                              [(6,1),(5,-1)],[(5,1),(3,-1)])):
    for idx,val in entries:
        reversed_idx=((idx&1)<<2)|(idx&2)|((idx>>2)&1)
        R[row,reversed_idx]=val
Z=sp.diag(1,-1)
for g in gs:
    assert (R*kp(g,3)-sp.kronecker_product(Z*g*Z,sp.eye(2))*R).applyfunc(sp.expand)==sp.zeros(4,8)

P6=np.array(6*P,dtype=np.int64)
assert sp.Matrix(P6.tolist())==6*P
patterns=[s for s in itertools.product(range(2),repeat=8) if sum(s)==4]
def idx(bits):return sum(int(b)<<(len(bits)-1-i) for i,b in enumerate(bits))
L=np.array([[P6[idx(s[:4]),idx(t[:4])] if s[4:]==t[4:] else 0
             for t in patterns] for s in patterns],dtype=np.int64)
Q=np.array([[P6[idx(s[4:]),idx(t[4:])] if s[:4]==t[:4] else 0
             for t in patterns] for s in patterns],dtype=np.int64)
data=np.load(W/cfg['arrays'])
def compress(t):
    return np.stack([t[np.ix_(*[(2*s,2*s+1) for s in pattern])].ravel()
                     for pattern in patterns]).astype(np.int64)
target=compress(data['target'])
assert np.array_equal(L@target,6*target)
assert np.array_equal(Q@target,6*target)
for crown in data['crowns']:
    t=compress(crown)
    assert np.array_equal(Q@(L@t),6*(L@t))

out={'claim':'Exact projector identity only; no graph-cover construction',
     'field':'Q(i), hence C; denominators 2,3 are present, no F2 assertion',
     'input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),
     'arrays_sha256':hashlib.sha256((W/cfg['arrays']).read_bytes()).hexdigest(),
     'group_elements':24,'averaged_matrix_entries_checked':256,
     'local_intertwiner_entries_checked':24*4*8,'projector_rank':2,
     'target_coordinates_checked':70*256,'crowns_checked':24,
     'left_projection_implies_right_projection_on_all_crowns':True,
     'six_times_projector':P6.tolist(),
     'quaternions':[[str(x) for x in q] for q in qs],
     'verification':'PASS exact integer and rational-complex arithmetic'}
p=W/cfg['output'];tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(p)
print(json.dumps({k:v for k,v in out.items() if k not in ('six_times_projector','quaternions')},indent=2))

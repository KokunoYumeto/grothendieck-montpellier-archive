#!/usr/bin/env python3
"""Exact Clifford stabilizer certificate for the split case of SF-E805.

Checks over Q the complete 120-dimensional so(16) action on the specified
spinor, its 42-dimensional stabilizer, and the two-dimensional commutant.
Galois descent to the real quadratic field and flat-family invariance are
proved in eightfold_obstructions.md; this script does not construct sheaves.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as S

N=8
EVEN=[m for m in range(1<<N) if m.bit_count()%2==0]

def wedge(x,y):
    z={}
    for a,u in x.items():
        for b,v in y.items():
            if a&b:
                continue
            parity=sum((b&((1<<i)-1)).bit_count()
                       for i in range(N) if a>>i&1)
            z[a|b]=z.get(a|b,0)+(-1)**parity*u*v
    return {m:S.expand(c) for m,c in z.items() if c}

def contract(i,x):
    z={}
    for m,c in x.items():
        if m>>i&1:
            sign=(-1)**((m&((1<<i)-1)).bit_count())
            z[m^(1<<i)]=sign*c
    return z

def add(*xs):
    z={}
    for x in xs:
        for m,c in x.items():
            z[m]=z.get(m,0)+c
    return {m:S.expand(c) for m,c in z.items() if c}

def scale(c,x):
    return {m:S.expand(c*a) for m,a in x.items() if c*a}

v={0:1,15:-1,240:-1,255:1}
names=[]
spin=[]
vectors=[]
indices={}

for i in range(N):
    for j in range(N):
        # E_ij acts on H, and -E_ji on H*.  On spinors it acts by
        # -e^j wedge i_{e_i} + delta_ij/2.
        a=scale(-1,wedge({1<<j:1},contract(i,v)))
        if i==j:
            a=add(a,scale(S.Rational(1,2),v))
        M=S.zeros(2*N)
        M[i,j]=1
        M[N+j,N+i]=-1
        indices['A',i,j]=len(names)
        names.append(('A',i,j));spin.append(a);vectors.append(M)

for i,j in combinations(range(N),2):
    a=wedge({(1<<i)|(1<<j):1},v)
    M=S.zeros(2*N)
    M[N+j,i]=-1
    M[N+i,j]=1
    indices['B',i,j]=len(names)
    names.append(('B',i,j));spin.append(a);vectors.append(M)

for i,j in combinations(range(N),2):
    a=contract(j,contract(i,v))
    M=S.zeros(2*N)
    M[j,N+i]=1
    M[i,N+j]=-1
    indices['C',i,j]=len(names)
    names.append(('C',i,j));spin.append(a);vectors.append(M)

action=S.Matrix([[a.get(m,0) for a in spin] for m in EVEN])
assert action.shape==(128,120)
assert action.rank()==78
assert len(action.nullspace())==42
Q=S.zeros(16)
for i in range(8):
    Q[i,8+i]=Q[8+i,i]=1
assert all(M.T*Q+Q*M==S.zeros(16) for M in vectors)

# Explicit basis of the claimed stabilizer: sl4 on each H block plus
# six contraction/wedge pairs on each block.
expected=[]
cartans=[]
for block in (range(4),range(4,8)):
    block=list(block)
    for i in block:
        for j in block:
            if i!=j:
                a=S.zeros(120,1);a[indices['A',i,j]]=1
                expected.append(a)
    for i in block[:-1]:
        a=S.zeros(120,1)
        a[indices['A',i,i]]=1
        a[indices['A',block[-1],block[-1]]]=-1
        expected.append(a)
        cartans.append(sum((a[k]*vectors[k] for k in range(120)),S.zeros(16)))
    volume={sum(1<<i for i in block):1}
    for i,j in combinations(block,2):
        a=S.zeros(120,1);a[indices['C',i,j]]=1
        b=contract(j,contract(i,volume))
        for m,c in b.items():
            x,y=[k for k in range(N) if m>>k&1]
            a[indices['B',x,y]]=c
        expected.append(a)

E=S.Matrix.hstack(*expected)
assert E.rank()==42
assert action*E==S.zeros(128,42)
stabilizer=[sum((a[k]*vectors[k] for k in range(120)),S.zeros(16))
            for a in expected]

# Commuting with the six diagonal Cartans makes a matrix diagonal:
# the sixteen simultaneous weight tuples are all distinct.
weights=[tuple(M[i,i] for M in cartans) for i in range(16)]
assert len(set(weights))==16

# For a diagonal matrix, commuting with the displayed complete stabilizer
# says its entries agree across every nonzero off-diagonal matrix entry.
parent=list(range(16))
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]];x=parent[x]
    return x
def union(a,b):
    a,b=find(a),find(b)
    if a!=b:parent[b]=a
for M in stabilizer:
    for i in range(16):
        for j in range(16):
            if i!=j and M[i,j]:
                union(i,j)
components={}
for i in range(16):
    components.setdefault(find(i),[]).append(i)
blocks=sorted(components.values())
assert blocks==[[0,1,2,3,8,9,10,11],[4,5,6,7,12,13,14,15]]

P=S.diag(*[1 if i in blocks[0] else 0 for i in range(16)])
assert P*P==P
assert all(P*M==M*P for M in stabilizer)

result={
 "status":"PASS",
 "coefficient_field":"Q; exact integer/rational linear algebra",
 "orthogonal_lie_dimension":120,
 "spin_action_matrix_shape":[128,120],
 "spin_action_rank":78,
 "stabilizer_dimension":42,
 "explicit_stabilizer_basis_rank":42,
 "distinct_cartan_weight_count":16,
 "commutant_dimension":2,
 "commutant_algebra":"Q x Q",
 "primitive_idempotent_rank":8,
 "commutant_blocks":blocks,
 "limits":"The field descent and deformation invariance are proved separately; no geometric seed is constructed."
}
Path(__file__).with_name('eightfold_clifford_certificate_output.json').write_text(
    json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

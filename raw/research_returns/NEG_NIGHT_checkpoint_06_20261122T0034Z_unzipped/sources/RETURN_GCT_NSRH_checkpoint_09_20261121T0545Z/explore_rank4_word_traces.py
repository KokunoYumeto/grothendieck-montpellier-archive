#!/usr/bin/env python3
"""Exact exploratory Laurent traces of actual rank-four nonstandard words.

Transfer through the 14-diagram TL algebra is checked against all actual
16-dimensional generator matrices before the search. Negative coefficients
would obstruct a simultaneous nonnegative Laurent matrix realization.
Absence in the finite searched list is not an all-word theorem.
"""
from collections import deque
from itertools import product
from pathlib import Path
from math import comb
import json, random, sys, time
import numpy as np
from scipy.sparse import csr_matrix

RANK = 4
DIM = 2**RANK
IDENT = tuple(list(range(RANK, 2*RANK)) + list(range(RANK)))

def generator(i):
    a = list(IDENT)
    a[i], a[i+1] = i+1, i
    a[RANK+i], a[RANK+i+1] = RANK+i+1, RANK+i
    return tuple(a)

GEN = [generator(i) for i in range(RANK-1)]

def multiply(a, b):
    parents = list(range(3*RANK))
    def root(x):
        while parents[x] != x:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x
    def join(x, y):
        parents[root(x)] = root(y)
    for j in range(2*RANK):
        join(j, a[j])
        join(RANK+j, RANK+b[j])
    components = {}
    for j in range(3*RANK):
        components.setdefault(root(j), []).append(j)
    out = [None]*(2*RANK)
    loops = 0
    for nodes in components.values():
        ends = [x if x < RANK else x-RANK for x in nodes
                if x < RANK or x >= 2*RANK]
        if not ends:
            loops += 1
        else:
            assert len(ends) == 2
            x, y = ends
            out[x], out[y] = y, x
    return tuple(out), loops

basis = [IDENT]
words = [()]
index = {IDENT: 0}
queue = deque([IDENT])
while queue:
    a = queue.popleft()
    for i, e in enumerate(GEN):
        c, loops = multiply(a, e)
        if c not in index:
            assert loops == 0
            index[c] = len(basis)
            basis.append(c)
            words.append(words[index[a]] + (i,))
            queue.append(c)
assert len(basis) == 14

def clean(A):
    return {k: v for k, v in A.items() if np.any(v)}

def lprod(A, B):
    out = {}
    for a, M in A.items():
        for b, N in B.items():
            out.setdefault(a+b, np.zeros((DIM, DIM), dtype=np.int64))
            out[a+b] += M @ N
    return clean(out)

def delta_times(A, degree):
    out = {}
    for k in range(degree+1):
        power, coeff = degree-2*k, comb(degree, k)
        for a, M in A.items():
            out.setdefault(a+power, np.zeros((DIM,DIM), dtype=np.int64))
            out[a+power] += coeff*M
    return clean(out)

def same(A, B):
    z = np.zeros((DIM,DIM), dtype=np.int64)
    return all(np.array_equal(A.get(k,z), B.get(k,z)) for k in A.keys()|B.keys())

# e_i = delta*I-c_i. On the local basis 11,12,21,22 its only
# block is [[v^-1,-1],[-1,v]]. This is the verified F21 convention.
local = {k: np.zeros((4,4), dtype=np.int64) for k in (-1,0,1)}
local[-1][1,1] = 1
local[1][2,2] = 1
local[0][1,2] = local[0][2,1] = -1
E = []
for i in range(RANK-1):
    left = np.eye(2**i, dtype=np.int64)
    right = np.eye(2**(RANK-i-2), dtype=np.int64)
    E.append({k:np.kron(np.kron(left,M),right) for k,M in local.items()})
matrices = []
for word in words:
    A = {0: np.eye(DIM, dtype=np.int64)}
    for i in word:
        A = lprod(A,E[i])
    matrices.append(A)
for j,a in enumerate(basis):
    for i,e in enumerate(GEN):
        c, loops = multiply(a,e)
        assert same(lprod(matrices[j],E[i]), delta_times(matrices[index[c]],loops))

def to_delta(lpoly):
    f = {int(k):int(v) for k,v in lpoly.items() if v}
    assert all(f.get(k,0) == f.get(-k,0) for k in f)
    out = {}
    while f:
        degree = max(f)
        assert degree >= 0
        coeff = f[degree]
        out[degree] = coeff
        for j in range(degree+1):
            k = degree-2*j
            f[k] = f.get(k,0)-coeff*comb(degree,j)
            if not f[k]:
                del f[k]
    return out

trace_delta = [to_delta({k:int(np.trace(M)) for k,M in A.items()}) for A in matrices]
pair_trace = []
for a,b in product(range(14), repeat=2):
    f = {}
    for k,c in trace_delta[a].items():
        for l,d in trace_delta[b].items():
            f[k+l] = f.get(k+l,0)+c*d
    pair_trace.append(f)
trace_degree = max(max(f,default=0) for f in pair_trace)
trace_vectors = [np.array([f.get(k,0) for f in pair_trace],dtype=np.int64)
                 for k in range(trace_degree+1)]
trace_bound = max(sum(abs(x) for x in f.values()) for f in pair_trace)

# P_i = delta^2 I - delta(e_i tensor I + I tensor e_i) + 2 e_i tensor e_i.
transitions = []
for i,e in enumerate(GEN):
    rows = [[] for _ in range(3)]
    cols = [[] for _ in range(3)]
    vals = [[] for _ in range(3)]
    for a,b in product(range(14),repeat=2):
        ae, la = multiply(basis[a],e)
        be, lb = multiply(basis[b],e)
        c,d = index[ae],index[be]
        source = 14*a+b
        for target, shift, coeff in [(source,2,1),(14*c+b,1+la,-1),
                                     (14*a+d,1+lb,-1),(14*c+d,la+lb,2)]:
            rows[shift].append(target);cols[shift].append(source);vals[shift].append(coeff)
    transitions.append([csr_matrix((vals[k],(rows[k],cols[k])),shape=(196,196),dtype=np.int64)
                        for k in range(3)])

def advance(A,i):
    B = np.zeros((196,A.shape[1]+2),dtype=np.int64)
    for k,T in enumerate(transitions[i]):
        B[:,k:k+A.shape[1]] += T@A
    return B

def actual_trace(A):
    f = np.zeros(A.shape[1]+trace_degree,dtype=np.int64)
    for k,T in enumerate(trace_vectors):
        f[k:k+A.shape[1]] += T@A
    # Convert to Laurent coefficients with arbitrary-precision Python ints.
    out = {}
    for degree,c in enumerate(f):
        if not c:
            continue
        for j in range(degree+1):
            power = degree-2*j
            out[power] = out.get(power,0)+int(c)*comb(degree,j)
    return {k:v for k,v in out.items() if v}

MAX_LENGTH = 18
# Each algebra transition has absolute coefficient total <=5, even if
# several paths combine. This bounds all signed integer accumulations.
assert 5**MAX_LENGTH * trace_bound < 2**63
initial = np.zeros((196,1),dtype=np.int64)
initial[0,0] = 1
tested = []
negative = None
start = time.monotonic()

def inspect(word,A):
    global negative
    f = actual_trace(A)
    assert all(f.get(k,0)==f.get(-k,0) for k in f)
    assert max(f,default=0) <= 2*len(word)
    bad = {k:c for k,c in f.items() if c<0}
    tested.append(''.join(str(i+1) for i in word))
    if bad:
        negative = {'word':tested[-1], 'negative_coefficients':bad,
                    'full_laurent_trace':dict(sorted(f.items()))}
        return True
    return False

def visit(word,A,depth):
    if word and inspect(word,A):
        return True
    if depth==0:
        return False
    for i in range(3):
        if word and i==word[-1]:
            continue
        if visit(word+(i,),advance(A,i),depth-1):
            return True
    return False

visit((),initial,10)
rng = random.Random(20261121)
if negative is None:
    for trial in range(600):
        word=[];A=initial
        length=rng.randrange(11,MAX_LENGTH+1)
        for j in range(length):
            choices=[i for i in range(3) if not word or i!=word[-1]]
            i=rng.choice(choices);word.append(i);A=advance(A,i)
        if inspect(tuple(word),A):
            break
result={'rank':RANK,'actual_tensor_dimension':DIM**2,'diagram_basis_count':14,
        'all_diagram_generator_transfers_checked':42,
        'integer_accumulation_bound':5**MAX_LENGTH*trace_bound,
        'tested_count':len(tested),'negative_example':negative,
        'tested_words':tested,'elapsed_seconds':time.monotonic()-start,
        'scope':'Finite exact exploration; no all-word positivity theorem follows from no counterexample.',
        'python':sys.version.split()[0],'numpy':np.__version__}
Path('rank4_word_trace_search.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='tested_words'},indent=2))

"""Exploratory finite-field search, not a theorem or existence certificate."""
import itertools
import json
import random
import sys
import time
from pathlib import Path

P = 101
pairs = list(itertools.combinations(range(4), 2))
pair_index = {p:i for i,p in enumerate(pairs)}
HERE = Path(__file__).resolve().parent


def rref(M):
    M = [[x % P for x in row] for row in M]
    rows, cols = len(M), len(M[0])
    pivots = []
    for j in range(cols):
        i = next((i for i in range(len(pivots), rows) if M[i][j]), None)
        if i is None:
            continue
        k = len(pivots)
        M[k], M[i] = M[i], M[k]
        t = pow(M[k][j], -1, P)
        M[k] = [x*t % P for x in M[k]]
        for i in range(rows):
            if i != k and M[i][j]:
                t = M[i][j]
                M[i] = [(a-t*b) % P for a,b in zip(M[i], M[k])]
        pivots.append(j)
        if len(pivots) == rows:
            break
    return M, pivots


def rank(M):
    return len(rref(M)[1])


def kernel(M):
    R, piv = rref(M)
    cols = len(M[0])
    out = []
    for j in range(cols):
        if j not in piv:
            v = [0]*cols
            v[j] = 1
            for i,k in enumerate(piv):
                v[k] = -R[i][j] % P
            out.append(v)
    return out


def trans(M):
    return list(map(list, zip(*M)))


def data(c):
    mu = []
    for i in range(4):
        block = []
        for j in range(4):
            if i == j:
                block.append([-x % P for x in c[i]])
            else:
                k = pair_index[tuple(sorted((i,j)))]
                block.append([int(k == t) for t in range(6)])
        mu.append(block)
    D = [[[0]*4 for j in range(4)] for i in range(4)]
    for i in range(4):
        D[i][i][i] = 2
        for coef,(j,k) in zip(c[i], pairs):
            D[i][j][k] += coef
            D[i][k][j] += coef

    def prod(a,b):
        out = [0]*6
        for i in range(4):
            if a[i]:
                for j in range(4):
                    if b[j]:
                        t = a[i]*b[j]
                        out = [(x+t*y) % P for x,y in zip(out,mu[i][j])]
        return out

    def bracket(a,b):
        return trans([[(x-y) % P for x,y in
                       zip(prod(D[i][a],D[j][b]),prod(D[i][b],D[j][a]))]
                      for i,j in pairs])
    return bracket(0,1), bracket(2,3), mu


def principal(M,mu):
    ann = kernel(trans(M))
    K = []
    for j in range(4):
        for a in ann:
            K.append([sum(a[t]*mu[j][i][t] for t in range(6)) % P
                      for i in range(4)])
    return kernel(K)


def one(c):
    A,B,mu = data(c)
    generic = [[(a+2*b) % P for a,b in zip(x,y)] for x,y in zip(A,B)]
    if rank(generic) != 4:
        return None, 'not_generic_four'
    if len(principal(generic,mu)) != 1:
        return None, 'nonprincipal'
    Ks = []
    for t in [None,0,1,3,4,5,6]:
        M = B if t is None else [[(a+t*b) % P for a,b in zip(x,y)] for x,y in zip(A,B)]
        r = rank(M)
        if r > 4:
            return None, 'higher_pencil_rank'
        if r == 4:
            k = principal(M,mu)
            if len(k) != 1:
                return None, 'other_nonprincipal'
            Ks.append({'t':t, 'line':k[0], 'kernel':kernel(M)})
    return {'coefficients':c,'plus_rank':rank(A),'minus_rank':rank(B),
            'generic_principal_line':principal(generic,mu)[0],
            'sample_principal_lines':Ks}, 'candidate'


start=time.perf_counter()
rng=random.Random(84120261121)
count=int(sys.argv[1]) if len(sys.argv)>1 else 20000
seen=set(); stats={}; candidates=[]
for trial in range(count):
    support=rng.sample(range(24),rng.choice([2,3,4,5]))
    c=[[0]*6 for _ in range(4)]
    for j in support:
        c[j//6][j%6]=rng.choice([-2,-1,1,2])
    key=tuple(sum(c,[]))
    if key in seen:
        continue
    seen.add(key)
    candidate,status=one(c)
    stats[status]=stats.get(status,0)+1
    if candidate:
        candidates.append(candidate)
        print(json.dumps({'candidate':candidate}), flush=True)
        if len(candidates)>=15:
            break
out={'status':'EXPLORATORY ONLY','prime':P,'attempted':len(seen),'stats':stats,
     'candidates':candidates,'seconds':time.perf_counter()-start,
     'scope':'Finite-field filter only. Regularity, characteristic-zero identities, every pencil direction, scalar cross minors, and strictness remain unverified.'}
(HERE/'e841_sparse_search.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))

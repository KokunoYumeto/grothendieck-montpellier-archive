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


def data(c, bivectors=None):
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
    if bivectors is None:
        return bracket(0,1), bracket(2,3), mu
    Bs = [bracket(i,j) for i,j in pairs]
    matrices = [[[sum(b[k]*Bs[k][i][j] for k in range(6)) % P for j in range(6)] for i in range(6)] for b in bivectors]
    return matrices[0], matrices[1], mu


def principal(M,mu):
    ann = kernel(trans(M))
    K = []
    for j in range(4):
        for a in ann:
            K.append([sum(a[t]*mu[j][i][t] for t in range(6)) % P
                      for i in range(4)])
    lines = kernel(K)
    if len(lines) != 1:
        return []
    ell = lines[0]
    image = [[sum(ell[i]*mu[i][j][t] for i in range(4)) % P for j in range(4)] for t in range(6)]
    return lines if rank(image) == 4 else []


def scalar_filter(c,A,B):
    exps2 = [e for e in itertools.product(range(3), repeat=4) if sum(e)==2]
    exps4 = [e for e in itertools.product(range(5), repeat=4) if sum(e)==4]
    ix4 = {e:i for i,e in enumerate(exps4)}
    edges = [tuple(int(i in ab) for i in range(4)) for ab in pairs]
    relations = []
    for i in range(4):
        square = tuple(2*int(j==i) for j in range(4))
        terms = [(square,1)]+list(zip(edges,c[i]))
        for e in exps2:
            row = [0]*35
            for t,a in terms:
                row[ix4[tuple(x+y for x,y in zip(e,t))]] += a
            relations.append(row)
    K = kernel(relations)
    if len(K) != 1:
        return False, 'degree_four_not_one'
    dual = K[0]
    H = [[dual[ix4[tuple(x+y for x,y in zip(e,f))]] for f in edges] for e in edges]
    for i in range(6):
        for j in range(i):
            z = sum(H[r][t]*(A[r][i]*B[t][j]-B[r][i]*A[t][j]) for r in range(6) for t in range(6)) % P
            if z:
                return False, 'scalar_cross_failure'
    return True, 'candidate'


def one(c, bivectors=None):
    A,B,mu = data(c,bivectors)
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
    passed, reason = scalar_filter(c,A,B)
    if not passed:
        return None, reason
    return {'coefficients':c,'bivectors':bivectors,'plus_rank':rank(A),'minus_rank':rank(B),
            'generic_principal_line':principal(generic,mu)[0],
            'sample_principal_lines':Ks}, 'candidate'


start=time.perf_counter()
rng=random.Random(84120261121)
count=int(sys.argv[1]) if len(sys.argv)>1 else 20000
seen=set(); stats={}; candidates=[]
for trial in range(count):
    support=rng.sample(range(24),rng.choice([1,2,3,4]))
    c=[[0]*6 for _ in range(4)]
    for j in support:
        c[j//6][j%6]=rng.choice([-2,-1,1,2])
    T=[[int(i==j) for j in range(4)] for i in range(4)]
    for _ in range(rng.choice([2,3,4,5])):
        i,j=rng.sample(range(4),2);a=rng.choice([-1,1])
        T[i]=[x+a*y for x,y in zip(T[i],T[j])]
    bivectors=[[T[i][a]*T[j][b]-T[j][a]*T[i][b] for i,j in pairs] for a,b in [(0,1),(2,3)]]
    key=tuple(sum(c,[])+sum(bivectors,[]))
    if key in seen:
        continue
    seen.add(key)
    candidate,status=one(c,bivectors)
    stats[status]=stats.get(status,0)+1
    if candidate:
        candidates.append(candidate)
        print(json.dumps({'candidate_coefficients':candidate['coefficients'],'bivectors':candidate['bivectors']}), flush=True)
        if len(candidates)>=15:
            break
out={'status':'EXPLORATORY ONLY','prime':P,'attempted':len(seen),'stats':stats,
     'candidates':candidates,'seconds':time.perf_counter()-start,
     'scope':'Finite-field filter only. Degree-four dimension and scalar cross minors tested over F101; regularity, characteristic-zero identities, every pencil direction, and strictness remain unverified.'}
(HERE/'e841_sparse_search.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k != 'candidates'}))

"""Exact Q(D) split model and GT path lines for the full rank-four algebra.

This is NOT VIII's conjectural minimum-degree globalization E(4).
The source input is the full generic dimension 114 (GCT IV, section 11.8).
All ordinary cell matrices below are reconstructed from the supplied exact
standard Hecke/KL arithmetic, not transcribed from the literature.
"""
from pathlib import Path
import json
import sys
import sympy as s

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "dependencies"))
import e4lib as h

D = s.Symbol("D")


def clean(M):
    return M.applyfunc(s.cancel)


def zero(M):
    return all(s.cancel(x) == 0 for x in M)


def rsk_insertion(w):
    rows = []
    for x in w:
        for row in rows:
            j = next((j for j, y in enumerate(row) if y > x), len(row))
            if j == len(row):
                row.append(x)
                break
            row[j], x = x, row[j]
        else:
            rows.append([x])
    return tuple(tuple(row) for row in rows)


def cell_scaled(shape):
    """Column matrices A_i = delta C'_i in a parity-gauged right cell."""
    choices = sorted({rsk_insertion(w) for w in h.G
                      if tuple(map(len, rsk_insertion(w))) == shape})
    P = choices[0]
    cell = [w for w in h.G if rsk_insertion(w) == P]
    index = {w: j for j, w in enumerate(cell)}
    mats = []
    for st in h.S:
        A = s.zeros(len(cell))
        for j, w in enumerate(cell):
            co = h.toCp(h.mulCp(h.Cp[w], st))
            for z, p in co.items():
                if z not in index:
                    continue
                i = index[z]
                if z == w:
                    assert p == {1: 1, -1: 1}
                    A[i, j] = D
                else:
                    assert set(p) == {0}, (w, z, p)
                    power = 1 + h.length(w) % 2 - h.length(z) % 2
                    assert power in (0, 2), (w, z, power)
                    A[i, j] = p[0] * D ** (power // 2)
        mats.append(A)
    for A in mats:
        assert zero(A * A - D * A)
    for i in range(2):
        A, B = mats[i:i+2]
        assert zero(A*B*A-D*A-B*A*B+D*B)
    assert zero(mats[0]*mats[2]-mats[2]*mats[0])
    return cell, mats


def tensor(A, B):
    n, m = A[0].rows, B[0].rows
    return [clean(2*s.kronecker_product(a,b)/D
                  -s.kronecker_product(a,s.eye(m))
                  -s.kronecker_product(s.eye(n),b)+D*s.eye(n*m))
            for a,b in zip(A,B)]


def symmetric_part(mats, n, alternating=False):
    cols = []
    for i in range(n):
        for j in range(i if not alternating else i+1, n):
            v = s.zeros(n*n,1)
            v[n*i+j] = 1
            if i != j:
                v[n*j+i] = -1 if alternating else 1
            cols.append(v)
    B = s.Matrix.hstack(*cols)
    left = (B.T*B).inv()*B.T
    out = [clean(left*M*B) for M in mats]
    for M, N in zip(mats,out):
        assert zero(M*B-B*N)
    return out


def quotient_plus(mats):
    n = mats[0].rows
    null = s.Matrix.vstack(*[M-D*s.eye(n) for M in mats]).nullspace()
    assert len(null) == 1
    v = clean(null[0])
    pivot = next(i for i,x in enumerate(v) if x != 0)
    v /= v[pivot]
    B = s.Matrix.hstack(v,*[s.eye(n)[:,j] for j in range(n) if j != pivot])
    inv = B.inv()
    out = []
    for M in mats:
        N = clean(inv*M*B)
        assert zero(N[:,0]-D*s.eye(n)[:,0])
        out.append(N[1:,1:])
    return out


def mod_entry(x, p, value):
    n,d = s.fraction(s.cancel(x.subs(D,value)))
    return int(n)%p*pow(int(d)%p,-1,p)%p


def algebra_rank_certificate(reps, p=1000003, value=7):
    assert s.isprime(p)
    mats = [[[mod_entry(x,p,value) for x in M] for M in r]
            for r in reps]
    dims = [r[0].rows for r in reps]
    ops = [[s.Matrix(n,n,mats[j][i]) for j,n in enumerate(dims)]
           for i in range(3)]
    unit = [s.eye(n) for n in dims]
    pivots = {}
    words, vectors, queue = [], [], []

    def ins(v):
        a = [int(x)%p for M in v for x in M]
        for j in sorted(pivots):
            if a[j]:
                c = a[j]
                a = [(x-c*y)%p for x,y in zip(a,pivots[j])]
        j = next((j for j,x in enumerate(a) if x),None)
        if j is None:
            return False
        inv = pow(a[j],-1,p)
        pivots[j] = [x*inv%p for x in a]
        return True

    assert ins(unit)
    words.append(())
    vectors.append(unit)
    queue.append(0)
    head = 0
    while head < len(queue):
        idx = queue[head]
        head += 1
        for i in range(3):
            v = [(M*N).applyfunc(lambda x:int(x)%p)
                 for M,N in zip(vectors[idx],ops[i])]
            if ins(v):
                words.append(words[idx]+(i+1,))
                vectors.append(v)
                queue.append(len(words)-1)
    assert len(words) == sum(n*n for n in dims) == 114, (len(words), dims)
    return {"prime":p,"D_value":value,"rank":len(words),
            "words":[list(w) for w in words],"pivot_columns":sorted(pivots)}


def gt_paths(mats):
    """Exact spectral projectors for the rank 3 and rank 2 tower."""
    n = mats[0].rows
    I = s.eye(n)
    A,B = mats[:2]
    Z = clean((A-B)**2)
    roots = [s.Integer(0),D*(D-1),4*(D-1)]
    assert zero(Z*(Z-roots[1]*I)*(Z-roots[2]*I))
    assert zero(Z*A-A*Z) and zero(Z*B-B*Z)
    projectors = []
    for i,z in enumerate(roots):
        E = I
        for j,w in enumerate(roots):
            if j != i:
                E = E*(Z-w*I)/(z-w)
        projectors.append(clean(E))
    for E in projectors:
        assert zero(E*E-E)
    assert zero(sum(projectors,s.zeros(n))-I)
    E0,E1,E2 = projectors
    assert zero(E0*(A-B))
    for j,E in [(1,E1),(2,E2)]:
        assert zero(E*(A*B*A-(D**2-roots[j])*A))
    components = [("eps+",clean(E0*A/D)),
                  ("eps-",clean(E0*(I-A/D))),
                  ("N1",E1),("N2",E2)]
    cols,labels,branch = [],[],{}
    for name,E in components:
        rank = E.rank()
        if not rank:
            continue
        branch[name] = rank
        assert rank == (2 if name.startswith("N") else 1)
        for sign,Q in [("+",A/D),("-",I-A/D)]:
            F = clean(E*Q)
            if zero(F):
                continue
            assert F.rank() == 1 and zero(F*F-F)
            col = next(F[:,j] for j in range(n) if not zero(F[:,j]))
            pivot = next(x for x in col if x != 0)
            cols.append(clean(col/pivot))
            labels.append([name,sign])
    S = s.Matrix.hstack(*cols)
    assert S.cols == n and S.det() != 0
    inv = S.inv()
    GT = [clean(inv*M*S) for M in mats]
    assert GT[0] == s.diag(*[D if z[1] == "+" else 0 for z in labels])
    for M,N in zip(mats,GT):
        assert zero(M*S-S*N)
    return {"branch_dimensions":branch,"path_labels":labels,
            "change_of_basis":S,"generator_matrices":GT}


def encode(x):
    if isinstance(x,s.MatrixBase):
        return [[str(s.factor(z)) for z in row] for row in x.tolist()]
    if isinstance(x,dict):
        return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [encode(v) for v in x]
    return x


def main():
    cells = {}
    As = {}
    # With the C-prime cell convention, RSK shape is the transpose of
    # the Specht label: the identity cell is the sign representation.
    for name,shape in [("4",(1,1,1,1)),("31",(2,1,1)),("22",(2,2))]:
        cells[name],As[name] = cell_scaled(shape)
    t31 = tensor(As["31"],As["31"])
    t22 = tensor(As["22"],As["22"])
    sprime31 = quotient_plus(symmetric_part(t31,3))
    reps = {
        "eps-": [s.zeros(1) for _ in range(3)],
        "Sprime22": quotient_plus(symmetric_part(t22,2)),
        "wedge31": symmetric_part(t31,3,True),
        "tensor31_22": tensor(As["31"],As["22"]),
        "Sprime31": sprime31,
        "thetaSprime31": [D*s.eye(5)-M for M in sprime31],
        "triv22": As["22"],
        "triv31": As["31"],
        "eps+": [s.Matrix([[D]]) for _ in range(3)],
    }
    for name,r in reps.items():
        for M in r:
            assert zero(M*M-D*M), name
        assert zero(r[0]*r[2]-r[2]*r[0]), name
    rank = algebra_rank_certificate(list(reps.values()))
    paths = {name:gt_paths(r) for name,r in reps.items()}
    out = {"status":"PASS", "scope":"Q(D) split models and GT path lines; not VIII E(4)",
           "source_dimension_input":114,"cell_permutations":cells,
           "scaled_cell_matrices":As,"representations":reps,
           "rank_certificate":rank,"GT_data":paths}
    path = HERE/"rational_gt_rank4_verified.json"
    path.write_text(json.dumps(encode(out),indent=2)+"\n")
    print(json.dumps({"status":"PASS","rank":rank["rank"],
                      "largest_word_length":max(map(len,rank["words"])),
                      "branching":{k:v["branch_dimensions"] for k,v in paths.items()}},indent=2))


if __name__ == "__main__":
    main()

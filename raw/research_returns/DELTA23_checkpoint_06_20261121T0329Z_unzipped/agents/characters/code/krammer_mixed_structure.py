#!/usr/bin/env python3
"""Independent invariant-submodule probes for DELTA23 mixed Krammer pairs."""
import contextlib
import importlib.util
import io
import itertools
import json
from pathlib import Path
import sys
import types
import numpy as np

BASE = Path(__file__).resolve().parents[2] / "pentagon"
# Import only field definitions, without executing the detector's certificate writes.
af = types.ModuleType("affine_cubic_detector")
exec((BASE / "affine_cubic_detector.py").read_text().split("S=(0,1,2,0)")[0], af.__dict__)
sys.modules[af.__name__] = af
spec = importlib.util.spec_from_file_location("krammer_f9_probe", BASE / "krammer_f9_probe.py")
kp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kp)
A, M, N, D = [np.array(x, dtype=np.int64) for x in (af.A, af.M, af.N, af.D)]


def mm(a, b):
    a, b = np.asarray(a), np.asarray(b)
    out = np.zeros((a.shape[0], b.shape[1]), dtype=np.int64)
    for k in range(a.shape[1]):
        out = A[out, M[a[:, k, None], b[None, k, :]]]
    return out


def mp(a, k):
    out = np.eye(len(a), dtype=np.int64)
    while k:
        if k & 1:
            out = mm(out, a)
        a = mm(a, a)
        k //= 2
    return out


def rref(a):
    a = np.array(a, dtype=np.int64, copy=True)
    row, piv = 0, []
    for j in range(a.shape[1]):
        found = next((i for i in range(row, len(a)) if a[i, j]), None)
        if found is None:
            continue
        a[[row, found]] = a[[found, row]]
        a[row] = M[D[a[row, j]], a[row]]
        for i in range(len(a)):
            if i != row and a[i, j]:
                a[i] = A[a[i], N[M[a[i, j], a[row]]]]
        piv.append(j)
        row += 1
        if row == len(a):
            break
    return a, piv


def rank(a):
    return len(rref(a)[1])


def nullspace(a):
    a, piv = rref(a)
    free = [j for j in range(a.shape[1]) if j not in piv]
    vs = []
    for j in free:
        v = np.zeros(a.shape[1], dtype=np.int64)
        v[j] = 1
        for i, p in enumerate(piv):
            v[p] = N[a[i, j]]
        vs.append(v)
    return np.array(vs, dtype=np.int64).T if vs else np.zeros((a.shape[1], 0), dtype=np.int64)


def basiscols(a):
    a = np.asarray(a, dtype=np.int64)
    return a[:, rref(a)[1]]


def canonical_space(a):
    b, _ = rref(np.asarray(a).T)
    return b[:rank(a)].T.copy()


def submodule(gs, v):
    b = np.asarray(v, dtype=np.int64).reshape(len(gs[0]), -1)
    while True:
        new = basiscols(np.concatenate([b]+[mm(g, b) for g in gs], axis=1))
        if new.shape[1] == b.shape[1]:
            return canonical_space(new)
        b = new


def inverse(a):
    n = len(a)
    b, p = rref(np.concatenate([a, np.eye(n, dtype=np.int64)], axis=1))
    assert p[:n] == list(range(n))
    return b[:, n:]


def adapted(gs, b):
    n, d = b.shape
    full = basiscols(np.concatenate([b, np.eye(n, dtype=np.int64)], axis=1))
    pinv = inverse(full)
    mats = [mm(mm(pinv, g), full) for g in gs]
    assert all(np.count_nonzero(g[d:, :d]) == 0 for g in mats)
    return full, mats


def proj_vectors(d):
    for pivot in range(d):
        for tail in itertools.product(range(9), repeat=d-pivot-1):
            yield np.array((0,)*pivot+(1,)+tail, dtype=np.int64)


def probe(gs, label):
    n = len(gs[0]); eye=np.eye(n, dtype=np.int64)
    eigs=[]
    for gen in gs:
        eigs.append([(a, nullspace(A[gen, N[M[a, eye]]])) for a in range(1,9)])
    out={"label":label,"dimension_F9":n,
         "eigenspace_dimensions":[{str(a):b.shape[1] for a,b in es if b.shape[1]} for es in eigs]}
    print(json.dumps(out),flush=True)
    # Every invariant nonzero space contains an eigenvector of either split
    # generator.  Enumerate all projective eigenvectors of the smaller set.
    choice=min(range(len(gs)), key=lambda j:sum((9**b.shape[1]-1)//8 for a,b in eigs[j]))
    seen={}; tried=0
    for a,b in eigs[choice]:
        if b.shape[1]==0:continue
        for coeff in proj_vectors(b.shape[1]):
            v=mm(b,coeff[:,None])
            space=submodule(gs,v); tried+=1
            if space.shape[1]<n:
                seen[tuple(space.flatten())]=(space,a)
    modules=[]
    for key,(space,a) in sorted(seen.items(),key=lambda item:item[1][0].shape[1]):
        full,mats=adapted(gs,space)
        modules.append({"dimension":space.shape[1],"basis":space.tolist(),
                        "full_basis":full.tolist(),"adapted_generators": [g.tolist() for g in mats]})
    out["projective_eigenvectors_checked"]=tried
    out["proper_cyclic_submodules"]=modules
    print(json.dumps({"label":label,"checked":tried,"proper_modules":len(modules),
                      "dimensions":[m["dimension"] for m in modules]}),flush=True)
    return out


def main():
    raw=kp.matrices(4,3,6);a,b,c=raw
    xs=[mp(a,2),mp(b,2),mp(c,2),mp(mm(mm(a,b),a),2),mp(mm(mm(c,b),c),2)]
    out={"field":"F3[i], i²=-1; encoding a+3b","pairs":[]}
    path=Path(__file__).resolve().parents[1]/"records"/"krammer_mixed_structure.json"
    for u,v in [(2,3),(3,4)]:
        result=probe([xs[u],xs[v]],[u+1,v+1]);out["pairs"].append(result)
        path.write_text(json.dumps(out,indent=2)+"\n")
    print(f"certificate: {path}",flush=True)


if __name__=="__main__":main()

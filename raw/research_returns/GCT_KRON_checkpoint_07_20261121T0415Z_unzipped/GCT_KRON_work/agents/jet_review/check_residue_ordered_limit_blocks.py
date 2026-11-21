"""Test the two separate ranks in the exact ordered-parameter limit.

This tests a structural conjecture about the uniform rank gates, not further
finite instances of the original endpoint.  Indices in the displayed formulas
are one-based; Python coordinates below are zero-based.
"""
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
import hashlib
import json
from structured_residue_tensor import rank_tool


def blocks(m):
    k = m-1
    edges = list(combinations(range(m), 2))
    count = len(edges)
    monomials = [(i, j) for i in range(m) for j in range(i, m)]
    mono_index = {pair: i for i, pair in enumerate(monomials)}
    f = [[0]*(count*m) for _ in range(k*len(monomials))]
    a = [[0]*(count*(k+m)) for _ in range(k*m*k)]
    for edge, (u, v) in enumerate(edges):
        for output in range(u, v):
            i = output+1
            sym = [0]*m
            sym[u] = 2*(u+1)-i
            sym[v] = i
            for j in range(u):
                sym[j] = 2
            skew = [0]*k
            if u < k:
                skew[u] = -i
            if v < k:
                skew[v] = i
            for ell in range(m):
                for j, coeff in enumerate(sym):
                    pair = tuple(sorted((j, ell)))
                    row = output*len(monomials)+mono_index[pair]
                    f[row][edge*m+ell] += coeff
            for q in range(k):
                for p, coeff in enumerate(sym):
                    row = (output*m+p)*k+q
                    a[row][edge*k+q] += coeff
            for p in range(m):
                for q, coeff in enumerate(skew):
                    row = (output*m+p)*k+q
                    a[row][count*k+edge*m+p] += coeff
    return a, f


def main():
    prime = 1000003
    rank_minor = rank_tool()
    results = []
    for m in [3, 4, 5, 6]:
        a, f = blocks(m)
        ra, rf = rank_minor(a, prime)[0], rank_minor(f, prime)[0]
        result = {"m": m, "M": m*(m-1)//2,
                  "A_shape": [len(a), len(a[0])], "A_rank": ra,
                  "F_shape": [len(f), len(f[0])], "F_rank": rf,
                  "A_cokernel_dimension": len(a)-ra,
                  "F_kernel_dimension": len(f[0])-rf,
                  "zero_charge_nullity": m*(m-1)//2+len(a)-ra+len(f[0])-rf}
        results.append(result)
        print(json.dumps(result), flush=True)
    source = Path(__file__)
    certificate = {"date_utc": datetime.now(timezone.utc).isoformat(),
                   "reviewer": "/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed",
                   "run": "GCT_KRON_20261120", "prime": prime,
                   "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                   "scope": "Finite structural checks of the separate rank gates in an ordered-parameter limit; no arbitrary-size conclusion.",
                   "results": results}
    source.with_name("residue_ordered_limit_blocks_certificate.json").write_text(json.dumps(certificate, indent=2)+"\n")


if __name__ == "__main__":
    main()

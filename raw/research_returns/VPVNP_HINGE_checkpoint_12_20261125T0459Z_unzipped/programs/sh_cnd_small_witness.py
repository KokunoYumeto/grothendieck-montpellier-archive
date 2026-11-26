#!/usr/bin/env python3
"""Search exact binary linear subspaces for a CND witness to sqrt(rank).

The search uses floating point only to choose candidate characters.  Every
reported witness includes integer rank-stratum counts and an exact SymPy
positivity check.  Failure to find a witness is never a nonexistence proof.
"""
import json
import math
import random
import sys
from pathlib import Path

import numpy as np
import sympy as sp

from sh_rank_roundness import binary_rank


def basis_reduce(vectors):
    rows = {}
    for v in vectors:
        while v:
            bit = v.bit_length() - 1
            if bit in rows:
                v ^= rows[bit]
            else:
                rows[bit] = v
                break
    return [rows[k] for k in sorted(rows)]


def span(basis):
    vals = [0]
    for v in basis:
        vals += [x ^ v for x in vals]
    return vals


def fwht(vals):
    out = np.array(vals, dtype=float)
    h = 1
    while h < len(out):
        blocks = out.reshape(-1, 2 * h)
        left = blocks[:, :h].copy()
        right = blocks[:, h:].copy()
        blocks[:, :h] = left + right
        blocks[:, h:] = left - right
        h *= 2
    return out


def main():
    config = json.loads(Path(sys.argv[1]).read_text())
    n = config['matrix_size']
    rank = [binary_rank(x, n) for x in range(1 << (n*n))]
    rng = random.Random(config['seed'])
    results = []
    structured = {
        'upper_triangular': [1 << (i*n+j) for i in range(n) for j in range(i,n)],
        'symmetric': [1 << (i*n+i) for i in range(n)] +
                     [(1 << (i*n+j)) ^ (1 << (j*n+i))
                      for i in range(n) for j in range(i+1,n)],
        'trace_zero': [(1 << (i*n+j)) for i in range(n) for j in range(n) if i != j] +
                      [(1 << (i*n+i)) ^ 1 for i in range(1,n)],
    }
    best = None
    for name, d, limit in ([('structured:'+k, len(v), 1) for k,v in structured.items()] +
                            [('random', d, config['trials_per_dimension'])
                             for d in config['dimensions']]):
        largest = -math.inf
        hit = None
        for trial in range(limit):
            if name.startswith('structured:'):
                basis = basis_reduce(structured[name.split(':')[1]])
            else:
                basis = []
                while len(basis) < d:
                    basis = basis_reduce(basis + [rng.randrange(1, len(rank))])
            group = span(basis)
            ranks = [rank[x] for x in group]
            f = fwht([math.sqrt(r) for r in ranks])
            char = int(np.argmax(f[1:])) + 1
            value = float(f[char])
            largest = max(largest, value)
            if value <= 1e-8:
                continue
            counts = [0] * (n+1)
            for j, r in enumerate(ranks):
                counts[r] += -1 if (j & char).bit_count() % 2 else 1
            exact = sum(sp.Integer(c)*sp.sqrt(r) for r,c in enumerate(counts))
            assert exact.is_positive is True, (counts, exact)
            assert sum(counts) == 0
            hit = dict(basis=basis, character=char,
                       signed_rank_counts=counts, fourier_value=value,
                       exact_value=str(exact), group_size=len(group),
                       positive_points=[x for j,x in enumerate(group)
                                        if not (j & char).bit_count() % 2],
                       negative_points=[x for j,x in enumerate(group)
                                        if (j & char).bit_count() % 2],
                       trial=trial)
            if best is None or len(group) < best['group_size']:
                best = hit
            break
        results.append(dict(kind=name, dimension=d, trials_run=trial+1,
                            largest_nontrivial_coefficient=largest, witness=hit))
    print(json.dumps(dict(config=config, results=results, best=best), indent=2))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Recompute every maximal dimension-permitted nested-support jet projection.

Run beside check_binary_jets.py; both use only the Python standard library.
"""
from itertools import combinations_with_replacement
from concurrent.futures import ProcessPoolExecutor
import argparse
import hashlib
import json
import time
from check_binary_jets import jacobian, rank_packed, scalar_rank


def check_one(task):
    profile, matrix, indices, prime, scalar = task
    started = time.monotonic()
    submatrix = [matrix[i] for i in indices]
    rank, columns, det = rank_packed(submatrix, prime)
    if scalar:
        assert scalar_rank(submatrix, prime) == rank
    return dict(profile=profile, rows=len(indices), rank=rank,
                full_row_rank=rank == len(indices), selected_rows=indices,
                selected_columns=columns,
                determinant_mod_p=det if rank == len(indices) else None,
                matrix_sha256=hashlib.sha256(b''.join(submatrix)).hexdigest(),
                elapsed_seconds=round(time.monotonic()-started, 3))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('n', type=int)
    parser.add_argument('--prime', type=int, default=101)
    parser.add_argument('--seed', type=int, default=20261122)
    parser.add_argument('--workers', type=int, default=1)
    parser.add_argument('--scalar', action='store_true')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.monotonic()
    matrix, labels = jacobian(args.n, args.n, args.prime, args.seed)
    bound = 2*args.n**2+2
    profiles = [p[::-1] for p in combinations_with_replacement(range(args.n+1), 3)]
    rowsets = {p:[i for i,a in enumerate(labels)
                  if sum(a[1:]) <= p[0] and sum(a[2:]) <= p[1] and a[3] <= p[2]]
               for p in profiles}
    small = {p for p in profiles if len(rowsets[p]) <= bound}
    frontier = [p for p in sorted(small)
                if not any(tuple(p[j]+int(j == i) for j in range(3)) in small
                           for i in range(3))]
    tasks = [(p,matrix,rowsets[p],args.prime,args.scalar) for p in frontier]
    out = dict(n=args.n, prime=args.prime, seed=args.seed, dimension_bound=bound,
               total_profiles=len(profiles), maximal_profiles=len(frontier), results=[])
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        for result in pool.map(check_one, tasks):
            out['results'].append(result)
            out['elapsed_seconds'] = round(time.monotonic()-start, 3)
            with open(args.output, 'w') as stream:
                json.dump(out, stream, indent=2)
                stream.write('\n')
            print(json.dumps({k:v for k,v in result.items()
                              if k not in ('selected_rows','selected_columns')}), flush=True)


if __name__ == '__main__':
    main()

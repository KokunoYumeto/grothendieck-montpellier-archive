#!/usr/bin/env python3
"""Exact signed rank-stratum counts for the F2 matrix rank metric."""
import csv
import json
from pathlib import Path
from sh_rank_roundness import binary_rank

ROOT = Path(__file__).resolve().parents[1]
settings = json.loads((ROOT/'inputs/sh_rank_metric_fourier.json').read_text())
rows = []
for n in settings['matrix_sizes']:
    ranks = [binary_rank(a, n) for a in range(1 << (n*n))]
    for dual_rank in range(1, n+1):
        h = sum(1 << (i*n+i) for i in range(dual_rank))
        counts = [0]*(n+1)
        for a, r in enumerate(ranks):
            counts[r] += -1 if ((a & h).bit_count() & 1) else 1
        assert sum(counts) == 0
        rows.append({'n': n, 'dual_rank': dual_rank,
                     'signed_counts_r0_to_n': json.dumps(counts)})
with (ROOT/'outputs/sh_rank_metric_fourier.tsv').open('w') as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter='\t')
    writer.writeheader(); writer.writerows(rows)
assert next(r for r in rows if r['n']==3 and r['dual_rank']==2)['signed_counts_r0_to_n'] == '[1, 1, -10, 8]'
print('Exact rank-stratum counts completed; Mat3 dual-rank2 = [1,1,-10,8].')

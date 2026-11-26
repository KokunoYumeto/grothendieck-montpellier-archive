#!/usr/bin/env python3
"""Exact certificate for the eight-point sqrt-rank CND obstruction."""
import json
import sys
from pathlib import Path

import sympy as sp

from sh_rank_roundness import binary_rank

config = json.loads(Path(sys.argv[1]).read_text())
n = config['matrix_size']
basis = config['basis_row_major_bitmasks']
group = [0]
for v in basis:
    group += [x ^ v for x in group]
assert len(set(group)) == 8
ranks = [binary_rank(x, n) for x in group]
assert ranks == config['expected_ranks']
counts = [0] * (n+1)
for i,r in enumerate(ranks):
    counts[r] += (-1)**i.bit_count()
assert counts == [1, -2, -1, 2]
eigenvalues = [sp.simplify(sum((-1)**((i&s).bit_count()) * sp.sqrt(ranks[i])
                             for i in range(8))) for s in range(1,8)]
negative = eigenvalues[:-1]
positive = eigenvalues[-1]
assert positive.is_positive is True
assert (sp.Rational(1,6)-positive).is_positive is True
assert all((-1-x).is_positive is True for x in negative)
print(json.dumps(dict(config=config, group=group, ranks=ranks,
                      signed_rank_counts=counts,
                      nonconstant_eigenvalues=[str(x) for x in eigenvalues],
                      positive_eigenvalue=str(positive),
                      full_quadratic_witness=str(8*positive),
                      checks={'positive_eigenvalue':True,
                              'positive_less_than_one_sixth':True,
                              'six_other_eigenvalues_less_than_minus_one':True,
                              'all_proper_subsets_CND_by_Fourier_Cauchy':True}),
                 indent=2))

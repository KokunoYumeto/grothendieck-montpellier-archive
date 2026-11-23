"""Exact finite checks for HD-S29; uniform inequalities are proved in the TeX.

Reads the fresh matrix-generated class data, not an imported table.
The partition formula is constructed directly from eigenvalue multiplicities.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / 'g12_matrix_certificate.json').read_text())
assert data['status'] == 'PASS' and data['group_order'] == 48
classes = data['class_data']

def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    if largest is None:
        largest = n
    for a in range(min(n, largest), 0, -1):
        for tail in partitions(n-a, a):
            yield (a,) + tail

def fixed_power(row, exponent):
    o = row['order']
    return sum(mult for j, mult in enumerate(row['eigenvalue_multiplicities'])
               if j*exponent % o == 0)

checked = 0
rows = {}
for n in range(4, 21):
    min_c, min_h = 2*n, 2*n
    partition_count = 0
    for partition in partitions(n):
        partition_count += 1
        for row in classes:
            c = 2*(n-1) - sum(fixed_power(row, a) for a in partition) + fixed_power(row, 1)
            if row['order'] == 1:
                assert c == 2*(n-len(partition))
                if c:
                    assert c >= 2
            else:
                assert c >= n-2
                assert c >= 2*n*(1-F(1,row['order']))-2
                if row['reflection']:
                    assert c >= n-1
                min_h = min(min_h, c)
            if c:
                min_c = min(min_c, c)
            checked += 1
    rows[str(n)] = dict(partitions=partition_count, minimum_nonidentity_c= min_c,
                        minimum_nontrivial_H_c=min_h)

orders = sorted({row['order'] for row in classes if row['order'] > 1})
genus_zero = []
for k in (1,2,3):
    for profile in combinations_with_replacement(orders, k):
        if sum((1-F(1,o) for o in profile), F(0)) == F(47,24):
            genus_zero.append(profile)
assert not genus_zero
# Four terms already have sum at least two.
assert 4*(1-F(1,min(orders))) > F(47,24)

out = dict(status='PASS', matrix_data='g12_matrix_certificate.json',
           local_spectra_partition_checks=checked, ranks_checked=rows,
           nonidentity_orders=orders, genus_zero_profiles=genus_zero,
           universal_branch_bound=9, universal_period_rank_bound=6,
           proof_scope='The uniform bounds follow from the two k-cases in HD-S29; finite partition checks are supplementary.')
(HERE/'g12_tensor_bounds.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='ranks_checked'}, indent=2))

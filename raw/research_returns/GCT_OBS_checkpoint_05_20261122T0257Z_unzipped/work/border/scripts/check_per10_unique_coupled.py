#!/usr/bin/env python3
"""BR-012: independent stdlib exact coupled-dimension certificates.

Reconstructs both literal permanent tensors, their unique surviving AB
extensions, the full AB/AC intersection, all BC contraction spaces, and
the projection ranks in each torus weight.  A rational dual inequality
then bounds the necessary (111) space by65/4<17.  No numerical optimizer
or floating-point arithmetic is imported or used.

The uniqueness of the AB plane uses the previously completed and reviewed
BR-010 flag computations.  Their full structural coverage is checked here;
those original family ranks are not recomputed by this script.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

from br_linear import rowspace
from permanent_coupled_module import unique_module, weight_dimension_constraints


CASES = {
    13119: ([0, 1, 2, 3, 4, 5, 8, 9, 12, 13], 3, 65),
    13503: ([0, 1, 2, 3, 4, 5, 7, 10, 12, 13], 2, 71),
}


def prior_unique(row, mask):
    subset, extra, families = CASES[mask]
    assert row['mask'] == mask and row['subset'] == subset
    assert row['status'] == 'OPEN' and not row.get('unhandled_error')
    assert not row['unhandled_families'] and len(row['surviving_flags']) == 1
    initial = row['initial']
    assert len(initial['parameter_branches']) == families
    refinements = row['refinements']
    assert sorted(r['index'] for r in refinements) == list(range(families))
    for r in refinements:
        assert r['status'] == 'EXCLUDED'
        if 'continuation' in r:
            c = r['continuation']
            assert not c['survivors'] and not c['open_families']
    key = lambda flag: json.dumps(flag, sort_keys=True)
    rigid = row['rigid_tests']
    assert sorted(key(r['flag']) for r in rigid) == sorted(key(f) for f in initial['surviving_flags'])
    assert [key(r['flag']) for r in rigid if r['failure'] is None] == [key(row['surviving_flags'][0])]
    for r in rigid:
        if r['failure'] is not None:
            f = r['failure']
            assert f['test'] == 'higher_koszul' and f['rank'] > 17*f['cost']
    return {'subset': subset, 'search_complete': True, 'open_families': [],
            'surviving_flags': row['surviving_flags']}


def dual_weights(mask):
    y = {('budget',): Fraction(5, 4), ('block_cap', 16): Fraction(3, 4),
         ('weight_cap', 14): Fraction(1, 2)}
    if mask == 13119:
        y['block_cap', 19] = Fraction(11, 4)
        selected = [(0, 3, 1), (1, 15, '1/2'), (1, 11, '1/4'), (1, 12, '1/4'),
                    (2, 16, 1), (3, 16, 1), (4, 12, 1), (5, 17, 1),
                    (6, 11, 1), (7, 10, '1/4'), (7, 15, '3/4'),
                    (8, 18, 1), (9, 10, 1), (10, 14, 1), (11, 13, 1),
                    (12, 19, 1), (13, 19, 1), (14, 13, '1/4'),
                    (14, 14, '1/4'), (15, 19, 1), (16, 19, 1)]
    else:
        assert mask == 13503
        y['block_cap', 18] = Fraction(11, 4)
        selected = [(0, 4, 1), (1, 10, '1/4'), (1, 15, '1/4'),
                    (1, 11, '1/4'), (1, 12, '1/4'), (2, 16, 1),
                    (3, 17, 1), (4, 12, 1), (5, 16, 1), (6, 11, 1),
                    (7, 15, 1), (8, 19, 1), (9, 10, 1), (10, 14, 1),
                    (11, 18, 1), (12, 13, 1), (13, 18, 1),
                    (14, 13, '1/4'), (14, 14, '1/4'), (15, 18, 1), (16, 18, 1)]
    for w, j, value in selected:
        y['projection', w, j] = Fraction(value)
    return y


def exact_bound(constraints, limits, mask):
    n, m = len(limits), len(constraints)
    rows = {('budget',): ([1]*n+[0]*m, 7)}
    for j, d in enumerate(limits):
        row = [0]*(n+m)
        row[j] = 1
        rows['block_cap', j] = row, d
    for w, c in enumerate(constraints):
        row = [0]*(n+m)
        row[n+w] = 1
        rows['weight_cap', w] = row, c['dimension']
        for j, r in c['projection_ranks'].items():
            row = [0]*(n+m)
            row[n+w], row[j] = 1, -1
            rows['projection', w, j] = row, c['dimension']-r
    weights = dual_weights(mask)
    lhs = [Fraction(0)]*(n+m)
    rhs = Fraction(0)
    for name, coefficient in weights.items():
        assert coefficient >= 0 and name in rows
        row, bound = rows[name]
        rhs += coefficient*bound
        lhs = [x+coefficient*y for x, y in zip(lhs, row)]
    objective = [0]*n+[1]*m
    assert all(x >= y for x, y in zip(lhs, objective))
    assert rhs == Fraction(65, 4) < 17
    return {'dual': [{'constraint': name, 'weight': str(v)} for name, v in weights.items()],
            'weighted_left_coefficients': [str(v) for v in lhs],
            'weighted_right_bound': str(rhs), 'integer_dimension_bound': 16}


def enumerate_dimensions(constraints, limits):
    d = [0]*len(limits)
    histogram, maxima = Counter(), {}
    count = 0
    def visit(i, left):
        nonlocal count
        if i == len(d):
            upper = sum(c['dimension']-max([0]+[r-d[j] for j, r in c['projection_ranks'].items()])
                        for c in constraints)
            histogram[upper] += 1
            maxima[7-left] = max(maxima.get(7-left, -1), upper)
            count += 1
            return
        for value in range(min(limits[i], left)+1):
            d[i] = value
            visit(i+1, left-value)
    visit(0, 7)
    assert count == 253144 and max(histogram) == 16
    return {'count': count, 'upper_bound_histogram': dict(histogram),
            'maximum_by_quotient_dimension': maxima}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--enumerate', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    started = time.time()
    records = []
    for mask, (subset, extra, count) in CASES.items():
        source = root/'certificates/per10_flags'/f'{mask}.json'
        data = source.read_bytes()
        original = json.loads(data)
        normalized = prior_unique(original, mask)
        B = unique_module(normalized)
        M = B['original']
        expected = M['U']+[{(7, M['support'].index(v)): 1} for v in (0, extra)]
        canon = lambda E: rowspace(tuple(tuple(v.items()) for v in E))
        assert canon(B['AB_extension']) == canon(expected)
        limits = [len(v) for w, v in B['blocks']]
        assert len(B['V']) == 27 and limits == [1]*10+[2]*6+[1]*4
        constraints = weight_dimension_constraints(B)
        assert len(constraints) == 17 and sum(c['dimension'] for c in constraints) == 27
        certificate = exact_bound(constraints, limits, mask)
        record = {'mask': mask, 'subset': subset, 'status': 'EXCLUDED',
                  'prior_flag_file_sha256': hashlib.sha256(data).hexdigest(),
                  'prior_family_count': count, 'prior_family_ranks_recomputed': False,
                  'V_dimension': 27, 'R_dimension': 36, 'U_dimension': 10,
                  'BC_quotient_weights': [w for w, v in B['blocks']],
                  'BC_quotient_dimensions': limits, 'weight_constraints': constraints,
                  'exact_dual_certificate': certificate}
        if args.enumerate:
            record['independent_integer_enumeration'] = enumerate_dimensions(constraints, limits)
        records.append(record)
    out = {'claim': 'BR-012', 'status': 'PASS', 'scope': 'Characteristic zero',
           'checked_utc': datetime.now(timezone.utc).isoformat(),
           'new_coupled_ranks_recomputed': True, 'optimization_solver_used': False,
           'integer_enumeration_recomputed': args.enumerate, 'results': records,
           'seconds': time.time()-started}
    path = root/'certificates/per10_unique_coupled.json'
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out, indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps({k: v for k, v in out.items() if k != 'results'}), flush=True)


if __name__ == '__main__':
    main()

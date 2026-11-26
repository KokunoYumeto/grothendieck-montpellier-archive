#!/usr/bin/env python3
"""Independent exact checker for two-minimum rank-profile certificates.

Orbit sizes and allowed pair distances are obtained by exhaustive sign-cube
enumeration, independently of the certificate generator's binomial and
intersection formulas. No optimizer or generator code is imported.
"""
import json
import hashlib
import sys
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


@lru_cache(None)
def geometry(D, h):
    assert 2 <= D <= 18 and 0 <= h <= D // 2
    M = 2 ** (D - 1)
    mask = (1 << h) - 1
    def key(s):
        a = (s & mask).bit_count()
        b = s.bit_count() - a
        return min((a, b), (h - a, D - h - b))
    keys = [key(s) for s in range(M)]
    order = sorted(set(keys))
    indices = {k: i for i, k in enumerate(order)}
    counts = Counter(keys)
    weights = [counts[k] for k in order]
    representative = {}
    for s, k in enumerate(keys):
        representative.setdefault(k, s)
    triples = set()
    for k, s in representative.items():
        o = indices[k]
        for t, kt in enumerate(keys):
            d = (s ^ t).bit_count()
            triples.add((o, indices[kt], min(d, D - d)))
    marks = [indices[key(0)], indices[key(mask)]]
    return order, weights, triples, marks


def check(path):
    data = json.loads(path.read_text())
    D, m, h = data['D'], data['m'], data['marked_distance']
    lo, other = data['low_value'], data['other_low_value']
    assert 3 <= m and 0 <= lo <= (m - 2) * D - 1
    assert lo <= other < (m - 1) * D
    assert 2 ** lo + 2 ** other >= 2 ** (m * (D - h))
    orbits, weights, triples, marks = geometry(D, h)
    assert [list(x) for x in orbits] == data['orbits']
    assert weights == data['weights'] and marks == data['marked_orbits']
    n, M, O = m * D, 2 ** (D - 1), len(orbits)
    totals, rhs = {}, Fraction(0)

    def ix(term, o, t):
        assert term in (0, 1) and 0 <= o < O and 1 <= t <= n
        return (term * O + o) * n + t - 1

    for e in data['certificate']:
        c = Fraction(e['numerator'], e['denominator'])
        assert c >= 0
        kind, *tail = e['label']
        bound = 0
        if kind == 'monotone':
            term, o, t = tail
            terms = [(ix(term, o, t + 1), 1), (ix(term, o, t), -1)]
        elif kind == 'budget':
            term, = tail
            terms = [(ix(term, o, t), weights[o])
                     for o in range(O) for t in range(1, n + 1)]
            bound = (m - 1) * D * M - 1
        elif kind == 'mixed':
            o, p, d, alt = tail
            assert (o, p, d) in triples and alt in (0, 1)
            L = m * (D - d)
            terms = [(ix(0, o, L - 1 + alt), -1),
                     (ix(1, p, L - alt), -1)]
            bound = -1
        elif kind == 'lipschitz':
            term, o, p, t = tail
            assert (o, p, 1) in triples and t > 2 * m
            terms = [(ix(term, o, t), 1), (ix(term, p, t - 2 * m), -1)]
        elif kind in ('minimum_upper', 'minimum_lower'):
            term, o, value = tail
            assert value == (lo, other)[term]
            if kind == 'minimum_upper':
                assert o == marks[term]
                terms = [(ix(term, o, value + 1), 1)]
            else:
                assert value > 0
                terms = [(ix(term, o, value), -1)]
                bound = -1
        elif kind in ('lower', 'upper'):
            j, = tail
            assert 0 <= j < 2 * O * n
            terms = [(j, 1 if kind == 'upper' else -1)]
            bound = 1 if kind == 'upper' else 0
        else:
            raise AssertionError(e['label'])
        for j, v in terms:
            totals[j] = totals.get(j, Fraction(0)) + c * v
        rhs += c * bound
    assert all(v == 0 for v in totals.values())
    assert rhs == -1
    return {'file': str(path), 'dimension': D, 'width': m,
            'certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'first_minimum': lo, 'second_minimum': other, 'distance': h,
            'certificate_entries': len(data['certificate']),
            'orbit_combinatorics_checked_by_full_cube_enumeration': True,
            'all_coefficients_nonnegative': True,
            'exact_variable_cancellation': True, 'exact_rhs': str(rhs),
            'solver_used_by_verifier': False, 'result': 'PASS'}


def check_manifest(path):
    data = json.loads(path.read_text())
    cfg = data['config']
    D, m = cfg['dimension'], cfg['width']
    minima = cfg['first_minima']
    assert len(set(minima)) == len(minima)
    universe = {(t, y, h) for t in minima
                for y in range(t, (m - 1) * D)
                for h in range(D // 2 + 1)}
    expected_pruned = {v for v in universe
                       if 2 ** v[0] + 2 ** v[1] < 2 ** (m * (D - v[2]))}
    pruned = {(e['first'], e['second'], e['distance']) for e in data['pruned']}
    assert pruned == expected_pruned and len(pruned) == len(data['pruned'])
    checks, covered = [], set()
    for name in data['cases']:
        result = check(path.parent / (name + '.json'))
        assert result['dimension'] == D and result['width'] == m
        case = (result['first_minimum'], result['second_minimum'], result['distance'])
        assert case not in covered
        covered.add(case)
        checks.append(result)
    assert covered == universe - expected_pruned
    return {'manifest': str(path), 'dimension': D, 'width': m,
            'first_minima': minima, 'pruned_by_exact_integer_rank_bound': len(pruned),
            'all_admissible_cases_certified': len(checks),
            'complete_branch_coverage': True, 'checks': checks, 'result': 'PASS'}


if __name__ == '__main__':
    config = json.loads(Path(sys.argv[1]).read_text())
    results = [check_manifest(Path(p)) for p in config['manifests']]
    Path(sys.argv[2]).write_text(json.dumps({'results': results}, indent=2) + '\n')
    print(json.dumps([{k: v for k, v in r.items() if k != 'checks'} for r in results], indent=2))

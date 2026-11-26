#!/usr/bin/env python3
"""Independent semantic replay of the D=5,6,7 tail Farkas certificates.

No generator or other verifier is imported.  A certificate's numeric row ID
is used only as a consistency check: the actual inequality is reconstructed
from its human-readable label and the mathematical tail-indicator model.
Folded Q5 expansion is independently enumerated over all 2^16 subsets.
Ordinary-cube expansion is computed from simplicial initial segments using
all-pairs Hamming distances (Harper's vertex-isoperimetric theorem).
All Farkas sums use integers after an exact common-denominator scaling.
"""
from __future__ import annotations

import argparse
import collections
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import time


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path, value):
    tmp = path.with_name(path.name + '.atomic_tmp')
    with tmp.open('w') as f:
        json.dump(value, f, indent=2)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def ordinary_growth(d):
    """Closed neighborhoods of simplicial initial segments of Q_d."""
    M = 1 << d
    order = sorted(range(M), key=lambda x: (
        x.bit_count(), tuple(i for i in range(d) if (x >> i) & 1)))
    balls = [[sum(1 << y for y in range(M)
                  if (x ^ y).bit_count() <= r)
              for x in range(M)] for r in range(d + 1)]
    growth = [[0] * (M + 1) for _ in range(d + 1)]
    for r in range(d + 1):
        mask = 0
        for v, x in enumerate(order, 1):
            mask |= balls[r][x]
            growth[r][v] = mask.bit_count()
    assert growth[0] == list(range(M + 1))
    return growth, order


def folded_growth(D):
    """Exhaust all subsets in Q_D/{x,-x}, represented by D-1 bits."""
    d = D - 1
    M = 1 << d
    # The quotient distance is min(Hamming(x,y), D-Hamming(x,y)).
    dist = [[min((x ^ y).bit_count(), D - (x ^ y).bit_count())
             for y in range(M)] for x in range(M)]
    growth, witnesses = [], []
    for r in range(d + 1):
        balls = [sum(1 << y for y in range(M) if dist[x][y] <= r)
                 for x in range(M)]
        union = [0] * (1 << M)
        minimum = [M + 1] * (M + 1)
        witness = [-1] * (M + 1)
        minimum[0], witness[0] = 0, 0
        for mask in range(1, 1 << M):
            bit = mask & -mask
            union[mask] = union[mask ^ bit] | balls[bit.bit_length() - 1]
            v, size = mask.bit_count(), union[mask].bit_count()
            if size < minimum[v]:
                minimum[v], witness[v] = size, mask
        growth.append(minimum)
        witnesses.append(witness)
    assert growth[0] == list(range(M + 1))
    return growth, witnesses, dist


def decode_row(label, D, M, n, growth, top):
    """Return integer coefficient pairs, RHS, and denominator.

    Every row is written sum(coeff*y)/denominator <= rhs/denominator.
    The rank-average row alone uses denominator 2^n.
    """
    kind, *args = label

    def index(k, v):
        assert 1 <= k <= n and 1 <= v <= M, (label, k, v)
        return (k - 1) * M + v - 1

    if kind in ('upper', 'lower'):
        assert len(args) == 1 and 0 <= args[0] < M * n
        return [(args[0], 1 if kind == 'upper' else -1)], int(kind == 'upper'), 1
    if kind == 'count_order':
        k, v = args
        assert 1 <= v < M
        return [(index(k, v + 1), 1), (index(k, v), -1)], 0, 1
    if kind == 'level_order':
        k, v = args
        assert 1 <= k < n
        return [(index(k + 1, v), 1), (index(k, v), -1)], 0, 1
    if kind == 'neighborhood':
        k, v, r, gr = args
        assert 1 <= r < D and 12 * r < k <= n
        assert gr == growth[r][v], (label, growth[r][v])
        return [(index(k, v), 1), (index(k - 12 * r, gr), -1)], 0, 1
    if kind == 'moment':
        assert not args
        return [(index(k, v), 2 * k - 1)
                for k in range(1, n + 1) for v in range(1, M + 1)], \
            (2809 * D * D * M - 1) // 144, 1
    if kind == 'mean':
        assert not args
        return [(j, 1) for j in range(n * M)], (53 * D * M - 1) // 12, 1
    if kind == 'rank_average':
        assert not args
        required = (M * (1 << n) + 2) // 3
        return [(index(k, v), -(1 << (k - 1)))
                for k in range(1, n + 1) for v in range(1, M + 1)], \
            M - required, 1 << n
    if kind == 'fixed_count_upper':
        k, t = args
        assert top[str(k)] == t and 0 <= t < M
        return [(index(k, t + 1), 1)], 0, 1
    if kind == 'fixed_count_lower':
        k, t = args
        assert top[str(k)] == t and 0 < t <= M
        return [(index(k, t), -1)], -1, 1
    raise AssertionError(('unrecognized row type', label))


def verify_certificate(path, growth, expected_D, expected_top):
    x = json.loads(path.read_text())
    D, M, n = expected_D, 1 << (expected_D - 1), 6 * expected_D
    assert x['dimension'] == D and x['section_dimension'] == D - 1
    assert x['vertices'] == M and x['ceiling'] == n and x['nv'] == M * n
    assert x['required_rank_sum'] == (M * (1 << n) + 2) // 3
    assert x['config']['top_counts'] == expected_top
    expected_expansion = {(v, r, growth[r][v])
                          for v in range(1, M + 1) for r in range(1, D)}
    assert set(map(tuple, x['expansion'])) == expected_expansion
    cert = x['certificate']
    assert isinstance(cert, list) and cert
    scale = 1
    for entry in cert:
        numerator, denominator = entry['numerator'], entry['denominator']
        assert isinstance(numerator, int) and numerator >= 0
        assert isinstance(denominator, int) and denominator > 0
        scale = math.lcm(scale, denominator)
    scale *= 1 << n
    coefficients, rhs = [0] * (n * M), 0
    row_labels, counts = {}, collections.Counter()
    semantics = hashlib.sha256()
    for entry in cert:
        row, label = entry['row'], entry['label']
        assert isinstance(row, int) and 0 <= row < x['constraints']
        if row in row_labels:
            assert row_labels[row] == label
        row_labels[row] = label
        pairs, bound, denominator = decode_row(label, D, M, n, growth, expected_top)
        weight = scale * entry['numerator'] // entry['denominator']
        assert weight * entry['denominator'] == scale * entry['numerator']
        assert weight % denominator == 0
        weight //= denominator
        for j, coefficient in pairs:
            coefficients[j] += weight * coefficient
        rhs += weight * bound
        counts[label[0]] += 1
        semantics.update(json.dumps([label, pairs, bound, denominator],
                                    separators=(',', ':')).encode())
        semantics.update(b'\n')
    nonzero = [(j, z) for j, z in enumerate(coefficients) if z]
    assert not nonzero, (path.name, 'nonzero columns', nonzero[:8])
    assert rhs < 0, (path.name, 'nonnegative RHS')
    exact_rhs = Fraction(rhs, scale)
    return {'path': str(path), 'sha256': sha(path), 'dimension': D,
            'fixed_tail_counts': expected_top, 'variables': M * n,
            'certificate_entries': len(cert), 'row_type_counts': dict(counts),
            'semantic_rows_sha256': semantics.hexdigest(),
            'all_weights_nonnegative': True, 'all_rows_semantically_valid': True,
            'all_columns_cancel': True, 'exact_rhs': str(exact_rhs),
            'contradiction': True, 'integer_scale_bits': scale.bit_length()}


def prune(growth, n, assumptions):
    M = len(growth[0]) - 1
    q = [0] * (n + 1)
    for level, count in assumptions:
        assert 1 <= level <= n and 0 <= count <= M
        for r, row in enumerate(growth):
            lower_level = level - 12 * r
            for k in range(1, max(0, lower_level) + 1):
                q[k] = max(q[k], row[count])
    return q[1:], sum((2 * k - 1) * q[k] for k in range(1, n + 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', default='inputs/ex_top_tail_verification_parameters.json')
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    config_path = root / args.input
    config = json.loads(config_path.read_text())
    start = time.time()
    growth5, witnesses5, distance5 = folded_growth(5)
    supplied_path = root / config['folded_growth']
    supplied = json.loads(supplied_path.read_text())
    assert supplied['exhaustive'] and supplied['subsets_per_radius'] == 65536
    assert supplied['vertices'] == 16
    for r in range(1, 5):
        assert supplied['growth'][str(r)] == growth5[r]
        for v, mask in enumerate(supplied['witness_masks'][str(r)]):
            assert mask.bit_count() == v
            neighborhood = {y for x in range(16) if (mask >> x) & 1
                            for y in range(16) if distance5[x][y] <= r}
            assert len(neighborhood) == growth5[r][v]
    growth6, order6 = ordinary_growth(5)
    growth7, order7 = ordinary_growth(6)
    growths = {5: growth5, 6: growth6, 7: growth7}
    results, input_hashes = [], {str(config_path): sha(config_path),
                               str(supplied_path): sha(supplied_path)}
    for manifest_name in config['manifests']:
        manifest_path = root / manifest_name
        manifest = json.loads(manifest_path.read_text())
        input_hashes[str(manifest_path)] = sha(manifest_path)
        D = manifest['config']['dimension']
        expected = list(range(6 if D == 5 else 22))
        assert D in (5, 7) and manifest['complete']
        assert manifest['config']['counts'] == expected
        assert [e['count'] for e in manifest['results']] == expected
        for entry in manifest['results']:
            path = root / entry['output']
            assert entry['certificate']
            results.append(verify_certificate(path, growths[D], D,
                                              {str(6 * D): entry['count']}))
    coverage_path = root / config['D6_coverage']
    coverage = json.loads(coverage_path.read_text())
    input_hashes[str(coverage_path)] = sha(coverage_path)
    expected = [{'36': t} for t in range(10)] + [{'36': 10, '35': 10}]
    assert [e['conditions'] for e in coverage['selected']] == expected
    for entry in coverage['selected']:
        path = root / entry['certificate']
        assert sha(path) == entry['sha256']
        results.append(verify_certificate(path, growth6, 6, entry['conditions']))
    d6_manifest_path = root / config['D6_manifest']
    d6_manifest = json.loads(d6_manifest_path.read_text())
    input_hashes[str(d6_manifest_path)] = sha(d6_manifest_path)
    assert [e['count'] for e in d6_manifest['results']] == list(range(11))
    assert all(e['certificate'] for e in d6_manifest['results'][:10])
    assert not d6_manifest['results'][10]['certificate']
    # The failed unrefined q36=10 attempt is never used as a certificate.
    direct_prunes = []
    scenarios = [(5, [(30, 6)]), (6, [(36, 11)]),
                 (6, [(36, 10), (35, 11)]), (7, [(42, 22)])]
    for D, assumptions in scenarios:
        tails, lower = prune(growths[D], 6 * D, assumptions)
        upper = (2809 * D * D * (1 << (D - 1)) - 1) // 144
        assert lower > upper
        if D == 6:
            record = next(z for z in coverage['prunes']
                          if z['high_tail_assumptions'] == [list(a) for a in assumptions])
            assert record['lower_tail_counts'] == tails
            assert record['exact_moment_lower'] == lower
            assert record['allowed_moment_upper'] == upper
            assert record['exact_margin'] == lower - upper
        direct_prunes.append({'dimension': D, 'assumptions': assumptions,
                              'tail_lower_bounds': tails, 'moment_lower': lower,
                              'moment_upper': upper, 'positive_margin': lower - upper})
    assert len(results) == 39
    report = {'verifier': str(Path(__file__).resolve()),
              'verifier_sha256': sha(Path(__file__).resolve()),
              'input_hashes': input_hashes,
              'generator_imported': False, 'source_checkers_imported': False,
              'arithmetic': 'integer common denominators; Fraction for final RHS only',
              'folded_enumeration': {'all_subsets_per_radius': 65536,
                  'radii': [0, 1, 2, 3, 4], 'growth': growth5,
                  'independent_minimizers': witnesses5,
                  'supplied_minimizers_verified': True},
              'ordinary_Q5': {'simplicial_order': order6, 'growth': growth6},
              'ordinary_Q6': {'simplicial_order': order7, 'growth': growth7},
              'certificates': results, 'direct_prunes': direct_prunes,
              'coverage': {'D5': 'q30=0..5 certified; q30>=6 pruned',
                  'D6': 'q36=0..9 certified; q36>=11 pruned; q36=10 and q35>=11 pruned; q36=q35=10 certified',
                  'D7': 'q42=0..21 certified; q42>=22 pruned'},
              'complete_coverage': True, 'all_passed': True,
              'scope': 'Finite tail-count necessary conditions only; ordinary growth invokes Harper. No circuit claim.',
              'elapsed_seconds': time.time() - start}
    output_path = root / config['output']
    atomic_json(output_path, report)
    print(json.dumps({'all_passed': True, 'certificate_count': len(results),
                      'all_rhs': sorted(set(z['exact_rhs'] for z in results)),
                      'prunes': [{k: z[k] for k in ['dimension', 'moment_lower', 'moment_upper', 'positive_margin']}
                                 for z in direct_prunes],
                      'output': str(output_path), 'elapsed': report['elapsed_seconds']}))


if __name__ == '__main__':
    main()

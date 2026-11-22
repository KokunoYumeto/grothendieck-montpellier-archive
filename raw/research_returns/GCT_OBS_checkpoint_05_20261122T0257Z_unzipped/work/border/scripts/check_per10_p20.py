#!/usr/bin/env python3
"""Check BR-008, the single P20 permanent tensor of exact border rank 18.

The upper curve and stabilizer identities below use only Python stdlib.
With --rebuild, the previously reviewed flag/Koszul engines regenerate
the entire lower certificate (stdlib plus SymPy).  Without --rebuild,
the file validates the cover's structure and checks its literal tensor
and subgroup identities, but does not claim to recompute its ranks.
"""
import argparse
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import json
import subprocess
import sys
import time

from br_linear import add, tensor, varwt
from probe_per10_p20 import per_p20_module, S


def row_curve(edges):
    """Collect the elementary integral first/second difference curve."""
    points = {(0,): {0: {0: 1}}}
    coefficients = defaultdict(lambda: defaultdict(int))
    vertices = sorted({i for edge in edges for i in edge})
    assert all((0, i) in edges for i in vertices if i)
    for i in vertices:
        if i:
            points[(0, i)] = {0: {0: 1}, i: {1: 1}}
    for a, (i, j) in enumerate(edges):
        if i == 0:
            coefficients[(0, j)][(a, -1)] += 1
            coefficients[(0,)][(a, -1)] -= 1
        else:
            points[(0, i, j)] = {0: {0: 1}, i: {1: 1}, j: {1: 1}}
            for key, scalar in (((0, i, j), 1), ((0, i), -1),
                                ((0, j), -1), ((0,), 1)):
                coefficients[key][(a, -2)] += scalar
    terms = []
    for key, vector in points.items():
        avector = defaultdict(dict)
        for (a, exponent), scalar in coefficients[key].items():
            if scalar:
                avector[a][exponent] = scalar
        terms.append((dict(avector), vector, vector))
    return terms


def kronecker_vector(left, right, right_dimension):
    result = {}
    for i, p in left.items():
        for j, q in right.items():
            poly = defaultdict(int)
            for k, a in p.items():
                for ell, b in q.items():
                    poly[k + ell] += a * b
            result[i * right_dimension + j] = dict(poly)
    return result


def check_upper():
    H = row_curve([(0, 1), (0, 2)])
    G = row_curve([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)])
    terms = [tuple(kronecker_vector(h, g, d)
                   for h, g, d in zip(ht, gt, (5, 4, 4)))
             for ht, gt in product(H, G)]
    total = defaultdict(int)
    for A, B, C in terms:
        for a, ap in A.items():
            for b, bp in B.items():
                for c, cp in C.items():
                    for (i, x), (j, y), (k, z) in product(ap.items(), bp.items(), cp.items()):
                        total[(a, b, c, i + j + k)] += x * y * z
    total = {key: value for key, value in total.items() if value}
    assert all(key[3] >= 0 for key in total)
    _, U, _, _, _ = tensor(S, 1)
    expected = {(a, b, c): x for c, column in enumerate(U)
                for (a, b), x in column.items()}
    constant = {(a, b, c): x for (a, b, c, exponent), x in total.items()
                if exponent == 0}
    assert constant == expected
    assert len(terms) == 18 and len(expected) == 40
    return {'terms': len(terms), 'constant_coefficients': len(constant),
            'negative_powers': 0, 'positive_entries': len(total) - len(constant)}


def check_stabilizer():
    M = per_p20_module(S)
    support, U = M['support'], M['U']
    positions = {value: i for i, value in enumerate(support)}
    terms = {(a, b, c): value for c, v in enumerate(U)
             for (a, b), value in v.items()}
    for a, b, c in terms:
        assert add(add(M['aw'][a], M['bw'][b]), M['bw'][c]) == (0,) * 8
    for root, action in enumerate(M['actions']):
        derivative = defaultdict(int)
        for (a, b, c), value in terms.items():
            for (aa, bb), coefficient in action((a, b)).items():
                derivative[(aa, bb, c)] += coefficient * value
            row, column = divmod(support[c], 4)
            target, scalar = None, 1
            if root < 2 and row == root + 1:
                target, scalar = column, -1
            elif root == 2 and row == 2:
                target = 4 + column
            elif root == 3 and column == 3:
                target = 4 * row + 2
            if target is not None:
                derivative[(a, b, positions[target])] += scalar * value
        assert not any(derivative.values()), root
    return {'torus_weight_checks': len(terms), 'root_identities': 4,
            'support': support, 'quotient_dimension': sum(len(v) for _, v in M['blocks']),
            'weight_blocks': len(M['blocks'])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rebuild', action='store_true')
    args = parser.parse_args()
    start = time.time()
    upper = check_upper()
    stabilizer = check_stabilizer()
    if args.rebuild:
        for name in ('probe_per10_p20.py', 'probe_per10_p20_refine.py'):
            subprocess.run([sys.executable, str(Path(__file__).with_name(name))], check=True)
    gate = json.loads(Path('certificates/per10_p20_gate.json').read_text())
    refined = json.loads(Path('certificates/per10_p20_refined.json').read_text())
    assert gate['subset'] == S and refined['subset'] == S
    assert not gate['surviving_flags'] and not gate['surviving_extensions']
    families = gate['parameter_branches']
    assert len(families) == 392
    assert Counter(f['level'] for f in families) == {2: 5, 3: 53, 4: 239, 5: 95}
    assert all(f['projective_dimension'] == 1 for f in families)
    results = refined['results']
    assert [r['index'] for r in results] == list(range(len(families)))
    assert all(r['status'] == 'EXCLUDED' for r in results)
    assert refined['status'] == 'EXCLUDED'
    assert not refined['unhandled_families'] and not refined['full_survivors']
    out = {'claim': 'BR-008', 'scope': 'Only the permanent P20 coordinate ten-plane; characteristic zero',
           'status': 'PASS', 'ranks_recomputed': args.rebuild,
           'upper': upper, 'stabilizer': stabilizer,
           'initial_families': len(families),
           'finite_continuations': sum('continuation' in r for r in results),
           'unhandled': 0, 'seconds': time.time() - start}
    destination = Path('certificates/per10_p20_summary.json')
    temporary = destination.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(out, indent=2) + '\n')
    temporary.replace(destination)
    print(json.dumps(out), flush=True)


if __name__ == '__main__':
    main()

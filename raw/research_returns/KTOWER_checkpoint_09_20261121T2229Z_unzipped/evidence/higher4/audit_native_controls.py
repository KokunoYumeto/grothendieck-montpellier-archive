#!/usr/bin/env python3
"""Independent small controls: literal Leibniz determinants versus native code.

The matrices, seed, exact expected/observed values, hashes, and compiler command
are recorded. This tests native ring arithmetic; it does not replay large cases.
"""
from pathlib import Path
from itertools import permutations
from hashlib import sha256
import json
import random
import subprocess

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'ring_determinant.cpp'
ORIGINAL = HERE / 'ring_determinant'
REBUILT = HERE / 'audit_ring_determinant'
COMMAND = ['g++', '-O2', '-std=c++17', str(SOURCE), '-o', str(REBUILT),
           '-lgmpxx', '-lgmp']
subprocess.run(COMMAND, check=True, capture_output=True, text=True)


def mul(x, y, m):
    a, b = x
    c, d = y
    return ((a*c-2*b*d) % m, (a*d+b*c+b*d) % m)


def det_leibniz(a, m):
    n = len(a)
    ans = [0, 0]
    for p in permutations(range(n)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(n)
                           for j in range(i+1, n))
        z = (1, 0)
        for i in range(n):
            z = mul(z, a[i][p[i]], m)
        for j in (0, 1):
            ans[j] = (ans[j] + sign*z[j]) % m
    return tuple(ans)


def run(binary, a, m):
    n = len(a)
    payload = f'{m} {n}\n' + ''.join(f'{x} {y}\n' for row in a for x, y in row)
    p = subprocess.run([str(binary)], input=payload, text=True,
                       capture_output=True)
    if p.returncode == 0:
        a, b, pivots = map(int, p.stdout.split())
        assert pivots == max(0, n-1)
        return {'status': 'returned', 'determinant': [a, b], 'pivots': pivots}
    assert p.returncode == 2 and p.stderr.strip() == 'unit pivot unavailable'
    return {'status': 'correctly inconclusive', 'stderr': p.stderr.strip()}


seed = 20261121
rng = random.Random(seed)
fixtures = [
    ('empty', 35, []),
    ('row_swap', 35, [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]),
    ('nonunit_final', 35, [[(1, 0), (4, 2)], [(0, 0), (5, 0)]]),
    # Its determinant is 1 mod6, but neither first-column entry is a unit.
    ('invertible_without_individual_pivot', 6,
     [[(2, 0), (3, 0)], [(3, 0), (2, 0)]]),
]
for m in (8, 25, 35, 49, 77, 697446897311):
    for n in range(1, 6):
        a = [[(rng.randrange(m), rng.randrange(m)) for _ in range(n)]
             for _ in range(n)]
        fixtures.append((f'random_m{m}_n{n}', m, a))

records = []
for name, m, a in fixtures:
    expected = det_leibniz(a, m)
    results = {}
    for key, binary in [('existing_binary', ORIGINAL), ('audit_rebuilt_binary', REBUILT)]:
        result = run(binary, a, m)
        if result['status'] == 'returned':
            assert tuple(result['determinant']) == expected, (name, result, expected)
        results[key] = result
    assert results['existing_binary'] == results['audit_rebuilt_binary']
    records.append({'name': name, 'modulus': m, 'matrix': a,
                    'expected': expected, 'results': results})

malformed = []
for label, payload in [('bad_modulus', '1 1\n0 0\n'),
                       ('short_matrix', '35 2\n1 0\n'),
                       ('trailing_input', '35 1\n1 0\nEXTRA\n')]:
    p = subprocess.run([str(REBUILT)], input=payload, text=True, capture_output=True)
    assert p.returncode == 2
    malformed.append({'name': label, 'input': payload,
                      'returncode': p.returncode, 'stderr': p.stderr.strip()})

out = {
    'status': 'PASS', 'seed': seed, 'algorithm': 'literal Leibniz sum',
    'controls': records, 'malformed_input_checks': malformed,
    'compiler_command': COMMAND,
    'compiler_version': subprocess.run(['g++', '--version'], check=True,
                                      capture_output=True, text=True).stdout.splitlines()[0],
    'sha256': {p.name: sha256(p.read_bytes()).hexdigest()
               for p in (SOURCE, ORIGINAL, REBUILT, Path(__file__))},
    'scope': '34 small exact controls; no large-model numerical replay by this audit.'
}
(HERE/'audit_native_controls.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'controls': len(records),
                  'returned': sum(r['results']['existing_binary']['status']=='returned'
                                  for r in records),
                  'inconclusive': sum(r['results']['existing_binary']['status']!='returned'
                                      for r in records),
                  'source_sha256': out['sha256'][SOURCE.name]}, indent=2))

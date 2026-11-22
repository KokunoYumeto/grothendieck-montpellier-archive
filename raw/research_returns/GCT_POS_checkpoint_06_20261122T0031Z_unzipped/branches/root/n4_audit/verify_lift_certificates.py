"""Independent exact Farkas/primal verifier for all modulus-16 lift cases.

Only standard-library integer and rational arithmetic is used.  The spectral
coverage is checked separately by coverage.cpp using orbit expansion.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'kronecker'
result = []
for order in (8, 16):
    seen = set()
    positives = []
    rejected = 0
    for line in (SOURCE / f'm16_chi{order}_certificates.jsonl').open():
        obj = json.loads(line)
        weights = obj['W']
        key = tuple(map(tuple, weights))
        assert key not in seen
        seen.add(key)
        assert len(weights) == 3
        assert all(len(w) == 4 and w == sorted(w) and w[0] == 0 for w in weights)
        assert sum(map(sum, weights)) % 16 == 16 // order
        values = [sorted(set(w)) for w in weights]
        margins = [Counter(w) for w in weights]
        edges = [e for e in product(*values) if sum(e) % 16 == 0]
        rows = [(j, a) for j in range(3) for a in values[j]]
        if 'y' in obj:
            coefficients = list(map(Fraction, obj['y']))
            assert len(coefficients) == len(rows)
            dual = dict(zip(rows, coefficients))
            assert all(sum(dual[j, e[j]] for j in range(3)) >= 0 for e in edges)
            assert sum(dual[j, a] * margins[j][a] for j, a in rows) < 0
            rejected += 1
        else:
            masses = list(map(Fraction, obj['x']))
            assert obj['E'] == list(map(list, edges))
            assert len(masses) == len(edges) and all(x >= 0 for x in masses)
            for j, a in rows:
                assert sum(x for x, e in zip(masses, edges) if e[j] == a) == margins[j][a]
            assert all(x > 0 for x in masses)
            assert all(a % 2 == 0 for w in weights for a in w)
            positives.append(weights)
    listed = {
        tuple(tuple(map(int, line.split()[i:i+4])) for i in (0, 4, 8))
        for line in (SOURCE / f'm16_chi{order}_spectra.txt').open()
    }
    assert seen == listed
    assert len(positives) == (4 if order == 8 else 0)
    result.append({'character_order': order, 'certificates': len(seen),
                   'exact_exclusions': rejected, 'strictly_positive': positives})
out = {'result': 'PASS', 'method': 'exact Fraction arithmetic; all certificates checked',
       'cases': result}
print(json.dumps(out, indent=2))
(Path(__file__).parent / 'rational_verification.json').write_text(json.dumps(out, indent=2))

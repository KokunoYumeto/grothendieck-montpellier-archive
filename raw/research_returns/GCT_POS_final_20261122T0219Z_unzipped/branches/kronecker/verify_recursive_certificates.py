"""Check recursive spectral certificates with Python integers/Fractions only.

This verifies the rational feasibility/separation certificates, not the
enumerator's orbit coverage.  That separate claim uses recursive_spectra.py
and the lifting argument documented in the branch research notes.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parent
n = int(sys.argv[1])
target = int(sys.argv[2]) if len(sys.argv) > 2 else None
prefix = f"recursive_n{n}" if target is None else f"character_n{n}_t{target}"
total = Counter()
for result_file in sorted(root.glob(f"{prefix}_m*_result.json")):
    result = json.loads(result_file.read_text())
    modulus = result["M"]
    cert_file = root / f"{prefix}_m{modulus}_certificates.jsonl"
    spectra_file = root / f"{prefix}_m{modulus}_spectra.txt"
    spectra_handle = spectra_file.open() if spectra_file.exists() else None
    counts = Counter()
    previous = None
    certificate_count = 0
    positives = []
    with cert_file.open() as handle:
        for line in handle:
            certificate = json.loads(line)
            weights = tuple(tuple(x) for x in certificate["W"])
            assert previous is None or previous < weights
            previous = weights
            certificate_count += 1
            if spectra_handle is not None:
                flat = [v for factor in weights for v in factor]
                assert list(map(int, next(spectra_handle).split())) == flat
            assert len(weights) == 3
            assert all(len(x) == n for x in weights)
            assert all(tuple(sorted(x)) == x and x[0] == 0 for x in weights)
            assert tuple(sorted(weights)) == weights
            assert all(0 <= v < modulus for x in weights for v in x)
            assert sum(map(sum, weights)) % modulus == (1 if target is None else target % modulus)
            values = [sorted(set(x)) for x in weights]
            multiplicities = [Counter(x) for x in weights]
            edges = [e for e in product(*values) if sum(e) % modulus == 0]
            rows = [(a, v) for a in range(3) for v in values[a]]
            rhs = [multiplicities[a][v] for a, v in rows]
            if "x" in certificate:
                assert [tuple(x) for x in certificate["E"]] == edges
                point = [Fraction(x) for x in certificate["x"]]
                assert len(point) == len(edges) and all(x >= 0 for x in point)
                for (a, v), margin_target in zip(rows, rhs):
                    assert sum(x for e, x in zip(edges, point) if e[a] == v) == margin_target
                assert certificate["strict"] == all(x > 0 for x in point)
                counts["feasible"] += 1
                positives.append(certificate)
            else:
                separator = [Fraction(y) for y in certificate["y"]]
                assert len(separator) == len(rows)
                row_index = {row: i for i, row in enumerate(rows)}
                assert all(sum(separator[row_index[(a, e[a])]] for a in range(3)) >= 0 for e in edges)
                assert sum(y * b for y, b in zip(separator, rhs)) < 0
                counts["infeasible"] += 1
    if spectra_handle is not None:
        assert next(spectra_handle, None) is None
        spectra_handle.close()
    assert certificate_count == result["orbits"]
    assert dict(counts) == result["counts"]
    assert positives == result["feasible"]
    total.update(counts)
    print("PASS", n, target, modulus, certificate_count, dict(counts), flush=True)
print("TOTAL PASS", n, target, dict(total), flush=True)

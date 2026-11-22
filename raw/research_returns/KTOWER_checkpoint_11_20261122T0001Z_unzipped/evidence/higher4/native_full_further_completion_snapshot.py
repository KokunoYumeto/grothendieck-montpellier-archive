"""Reconcile actual completed native reports; never certify unfinished cases.

This does not rerun a large row calculation. It verifies the saved report's
input and code hashes, dimensions, full-row count, determinant identity and
all scalar/norm unit conditions using Python integers.
"""
from pathlib import Path
from hashlib import sha256
from math import factorial, gcd
from datetime import datetime, timezone
import json
import sys

sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
CASES = HERE / 'hecke_minus7/higher4'
VERIFIER = CASES / 'verify_ring_schur_parallel.py'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def norm(x, q):
    a, b = x
    return (a*a+a*b+2*b*b) % q


def multiply(x, y, q):
    a, b = x
    c, d = y
    return [(a*c-2*b*d) % q, (a*d+b*c+b*d) % q]


def main():
    source = VERIFIER.read_bytes()
    prefix = source.decode().split('\n\ndef evaluate(z, w):', 1)[0]
    code = {
        'verifier_sha256': digest(HERE / 'ktower_complete_native_ring.py'),
        'archived_verifier_sha256': sha256(source).hexdigest(),
        'unmodified_prefix_sha256': sha256(prefix.encode()).hexdigest(),
        'native_source_sha256': digest(HERE / 'ring_full_evaluator.cpp'),
        'native_executable_sha256': digest(HERE / 'ring_full_evaluator'),
        'frame_sha256': digest(CASES.parent / 'neighbor_frames.json'),
    }
    rows = []
    for e in [38, 40]:
        support_path = HERE/'hecke_general/higher4'/f'residual_support_e{e}.json'
        if not support_path.exists():
            rows.append({'e': e, 'status': 'Initial discovery support not yet complete'})
            continue
        support = json.loads(support_path.read_text())['degrees'][0]
        moduli = support['residual_support_moduli']
        paths = [CASES/f'e{e}_m{m}' for m in moduli]
        assert len(paths) == 2
        for expected_modulus, case in zip(moduli, paths):
            path = case / 'ktower_complete_native_ring.json'
            if not path.exists():
                rows.append({'case': case.name, 'status': 'No completed native report; no unit conclusion'})
                continue
            r = json.loads(path.read_text())
            m = json.loads((case / 'model.json').read_text())
            assert m['q'] == r['modulus'] == expected_modulus
            assert r['status'] == 'PASS: complete exact native quadratic-algebra unit certificate'
            assert r['unit'] is True and r['no_primality_assumption'] is True
            assert r['all_thirteen_frames_per_row'] is True
            assert r['entire_harmonic_kernel_verified'] is True
            assert r['complete_model_text_verified'] is True
            assert (r['e'], r['k'], r['modulus']) == (e, e-1, m['q'])
            assert (m['e'], m['k']) == (e, e-1)
            for key in ['dimension', 'source_dimension', 'target_dimension']:
                assert r[key] == m[key]
            assert r['dimension'] == r['all_recomputed_evaluation_rows'] == len(m['harmonic_basis_sparse_columns'])
            assert r['source_dimension'] == len(m['source_orbits'])
            assert r['target_dimension'] == len(m['target_orbits'])
            assert r['source_dimension']-r['target_dimension'] == r['dimension']
            assert r['frame_counts'] == {'2': [12, 14, 6], '4': [57, 113, 7]}
            for name in ['model.json', 'model.txt']:
                assert r['sha256'][name] == digest(case / name)
            for key, value in code.items():
                assert r[key] == value, (case.name, key)
            q = r['modulus']
            E = (1+2**e+2**(2*e)) % q
            assert r['comparison_point_modulus'] == E
            assert gcd(q, E) == gcd(q, 336*factorial(2*e-1)) == 1
            determinants = [r[key] for key in ['det_evaluation', 'det_schur_evaluations', 'det_schur_operator']]
            assert all(len(x) == 2 and all(type(y) is int and 0 <= y < q for y in x) for x in determinants)
            a, s, d = determinants
            assert a[1] == 0
            assert gcd(norm(a, q), q) == gcd(norm(s, q), q) == gcd(norm(d, q), q) == 1
            assert r['gcd_norm_determinant_modulus'] == 1
            assert multiply(a, d, q) == s
            rows.append({
                'case': case.name, 'status': 'PASS: completed native report reconciled',
                'modulus': q, 'e': e, 'dimension': r['dimension'],
                'source_dimension': r['source_dimension'], 'target_dimension': r['target_dimension'],
                'report_sha256': digest(path), 'input_sha256': r['sha256'],
                'det_evaluation': a, 'det_schur_evaluations': s, 'det_schur_operator': d,
                'all_rows': r['all_recomputed_evaluation_rows'],
                'native_elapsed_seconds': r['native_elapsed_seconds'],
                'preexisting_report_comparisons': r['preexisting_report_comparisons'],
                'scope': 'Report and exact integer reconciliation; no new large-model execution by this collector.',
            })
    report = {
        'checked_utc': datetime.now(timezone.utc).isoformat(),
        'collector_sha256': digest(Path(__file__)),
        'code_sha256': code, 'cases': rows,
        'arithmetic_scope': 'Only completed unitary native reports are reconciled. Complete K-group vanishing also requires the initial-field residual support, classical comparisons, and carried all-prime arithmetic argument.',
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

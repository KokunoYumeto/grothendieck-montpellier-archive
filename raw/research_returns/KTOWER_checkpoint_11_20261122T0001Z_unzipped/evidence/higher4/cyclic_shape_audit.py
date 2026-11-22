"""Explicit shape audit of the three current frozen Hecke datasets.

The frozen verifier checks the entries and algebraic identities. This
separate audit records the full square matrix and identifying-point
cardinalities used in that argument. It does not modify either input
or the active replay code and does not replace full model verification.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
DATA = HERE / 'hecke_general/higher4'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def shape(matrix, rows, columns):
    assert len(matrix) == rows
    assert all(len(row) == columns for row in matrix)


def main():
    records = []
    for e in [32, 34, 36]:
        path = DATA / f'harmonic_hecke_e{e}_exact_data.json'
        content = path.read_bytes()
        data = json.loads(content)
        assert len(data['degrees']) == 1
        degree = data['degrees'][0]
        assert (degree['e'], degree['k']) == (e, e-1)
        h = degree['harmonic_basis_columns']
        n = len(h[0])
        assert n > 0
        source, target = len(degree['source_orbits']), len(degree['target_orbits'])
        assert n == source-target
        shape(h, source, n)
        shape(degree['laplacian'], target, source)
        shape(degree['evaluation_matrix'], n, n)
        points = degree['evaluation_points']
        assert len(points) == len(degree['swap_signs']) == n
        assert all(sign in (-1, 1) for sign in degree['swap_signs'])
        assert all(len(point) == 2 and all(len(side) == 3 for side in point)
                   for point in points)
        assert sorted(r['p'] for r in degree['results']) == [7, 13]
        for record in degree['results']:
            assert record['dimension'] == n
            for key in ['transformed_evaluations_0', 'transformed_evaluations_omega',
                        'operator_0', 'operator_omega', 'rational_real_form_operator']:
                shape(record[key], n, n)
            assert len(record['charpoly_coefficients']) == n+1
        input_hash = sha256(content).hexdigest()
        assert digest(path) == input_hash
        records.append({
            'e': e, 'data_file': path.name, 'data_sha256': input_hash,
            'source_dimension': source, 'target_dimension': target,
            'harmonic_dimension': n, 'identifying_points': len(points),
            'all_shapes': 'PASS', 'primes': [7, 13],
        })
    files = ['cyclic_charpoly_certificate.py', 'replay_cyclic_charpoly.py',
             'replay_integral_faddeev.py']
    report = {
        'status': 'PASS: exact current input shapes and cardinalities',
        'checked_utc': datetime.now(timezone.utc).isoformat(),
        'audit_source_sha256': digest(Path(__file__)),
        'unchanged_replay_code_sha256': {name: digest(DATA / name) for name in files},
        'frozen_verifier_sha256': digest(DATA.parent / 'harmonic_hecke_certificate.py'),
        'records': records,
        'scope': 'Input shapes and hashes only; independent whole-model replay completion remains separate.',
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

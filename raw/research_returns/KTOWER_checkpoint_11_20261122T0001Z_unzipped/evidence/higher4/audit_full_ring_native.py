"""Small exact controls for the new complete-ring evaluator.

Permutation determinants use only Python integers and are independent of
native elimination. A missing unit pivot is an inconclusive computation,
including the explicit example whose determinant is nevertheless a unit.
"""
from pathlib import Path
from itertools import permutations
from math import gcd
from datetime import datetime, timezone
from hashlib import sha256
import json
import random
import subprocess

HERE = Path(__file__).resolve().parent
EXE = HERE / 'ring_full_evaluator'


def mul(x, y, modulus):
    a, b = x
    c, d = y
    return ((a*c-2*b*d) % modulus, (a*d+b*c+b*d) % modulus)


def determinant(matrix, modulus):
    total = [0, 0]
    n = len(matrix)
    for p in permutations(range(n)):
        sign = (-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        value = (1, 0)
        for i in range(n):
            value = mul(value, matrix[i][p[i]], modulus)
        for j in range(2):
            total[j] = (total[j] + sign*value[j]) % modulus
    return tuple(total)


def run(payload):
    p = subprocess.run([str(EXE), '--determinant'], input=payload,
                       text=True, capture_output=True)
    return p.returncode, json.loads(p.stdout)


def matrix_payload(matrix, modulus):
    return f'{modulus} {len(matrix)}\n' + '\n'.join(
        f'{a} {b}' for row in matrix for a, b in row) + '\n'


def main():
    rng = random.Random(2026112101)
    rows = []
    for modulus in [15, 35, 49, 77, 1000003**2, 697446897311]:
        for n in range(1, 5):
            matrix = [[(rng.randrange(modulus), rng.randrange(modulus))
                       for _ in range(n)] for _ in range(n)]
            expected = determinant(matrix, modulus)
            status, result = run(matrix_payload(matrix, modulus))
            if status == 2:
                assert result['status'] == 'INCONCLUSIVE_UNIT_PIVOT'
                outcome = 'correctly inconclusive'
            else:
                assert status in (0, 3)
                assert tuple(result['determinant']) == expected
                a, b = expected
                common = gcd(a*a+a*b+2*b*b, modulus)
                assert result['gcd_norm'] == common
                assert (status == 0) == (common == 1)
                outcome = 'exact determinant and unit status agree'
            rows.append({'modulus': modulus, 'dimension': n,
                         'expected_determinant': expected, 'outcome': outcome})
    # This matrix has determinant one modulo15 although neither entry in
    # its first column is a unit. It must never be declared noninvertible.
    matrix = [[(3, 0), (1, 0)], [(5, 0), (2, 0)]]
    assert determinant(matrix, 15) == (1, 0)
    status, result = run(matrix_payload(matrix, 15))
    assert status == 2 and result['status'] == 'INCONCLUSIVE_UNIT_PIVOT'
    status, result = run('15 1 3 0\n')
    assert status == 3 and result == {
        'status': 'NONUNIT_DETERMINANT', 'determinant': [3, 0], 'gcd_norm': 3}
    malformed = ['1 1 1 0', '15 -1', '15 2 1 0', '15 1 1 0 trailing']
    for payload in malformed:
        status, result = run(payload)
        assert status == 2 and result['status'] == 'ERROR'
    # The complete-model reader must reject malformed counts before any
    # numerical evaluation starts.
    inputs = {
        'bad_modulus': '1 2 1 1',
        'nonunit_denominator': '15 2 1 1',
        'bad_orbit': '101 2 1 1 0 0 0 0 3 1',
        'short_model': '101 2 1 1',
    }
    temporary = HERE / 'native_full_malformed_control.txt'
    for name, payload in inputs.items():
        temporary.write_text(payload)
        p = subprocess.run([str(EXE), str(temporary)], text=True, capture_output=True)
        assert p.returncode == 2 and json.loads(p.stdout)['status'] == 'ERROR', name
    temporary.unlink()
    report = {
        'status': 'PASS', 'date_utc': datetime.now(timezone.utc).isoformat(),
        'source_sha256': sha256((HERE/'ring_full_evaluator.cpp').read_bytes()).hexdigest(),
        'executable_sha256': sha256(EXE.read_bytes()).hexdigest(),
        'random_exact_controls': rows,
        'invertible_no_unit_pivot_correctly_inconclusive': True,
        'explicit_nonunit_final_determinant_detected': True,
        'malformed_determinant_inputs_rejected': len(malformed),
        'malformed_or_nonunit_model_inputs_rejected': len(inputs),
    }
    (HERE/'audit_full_ring_native.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

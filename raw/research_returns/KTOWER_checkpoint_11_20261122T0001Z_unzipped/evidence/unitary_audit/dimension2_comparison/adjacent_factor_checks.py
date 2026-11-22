#!/usr/bin/env python3
"""Exact small algebra checks for the adjacent-factor source-scope note.

This does not model a global Galois deformation or test a main R=T theorem.
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def matrix(rows):
    return tuple(tuple(row) for row in rows)


def transpose(a):
    return tuple(zip(*a))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def elementary(i, j, scalar=1):
    return matrix([[scalar if (r, s) == (i, j) else 0
                    for s in range(3)] for r in range(3)])


identity = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
J = matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
C = matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
Cinv = transpose(C)
sign = matrix([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])


def tau(a):
    return mul(mul(C, transpose(a)), Cinv)


def tau_symmetric(a):
    return mul(mul(J, transpose(a)), J)


checks = {}
checks['C_inverse'] = mul(C, Cinv) == identity == mul(Cinv, C)
checks['centralizer_square'] = mul(C, transpose(Cinv)) == sign
positions = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]
basis = [elementary(i, j) for i, j in positions]
checks['block_centralizer'] = all(mul(sign, x) == mul(x, sign) for x in basis)
checks['block_tau_squared'] = all(tau(tau(x)) == x for x in basis)
checks['block_antimultiplicativity'] = all(tau(mul(x, y)) == mul(tau(y), tau(x))
                                          for x in basis for y in basis)
checks['outer_idempotents'] = tau(elementary(0, 0)) == elementary(2, 2)
checks['middle_idempotent'] = tau(elementary(1, 1)) == elementary(1, 1)
checks['negative_long_13'] = tau(elementary(0, 2)) == elementary(0, 2, -1)
checks['negative_long_31'] = tau(elementary(2, 0)) == elementary(2, 0, -1)
checks['not_full_matrix_involution'] = tau(tau(elementary(0, 1))) != elementary(0, 1)
valuation = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]
checks['order_closed'] = all(valuation[i][k] + valuation[k][j] >= valuation[i][j]
                              for i in range(3) for j in range(3) for k in range(3))
checks['order_tau_stable'] = all(valuation[i][j] == valuation[2-j][2-i]
                                  for i in range(3) for j in range(3))
checks['square_nonzero_basis'] = mul(tau_symmetric(elementary(1, 0)),
                                     elementary(1, 0)) == elementary(2, 0)
checks['square_survives_K'] = 2 < valuation[2][1] + valuation[1][2] + valuation[2][0] == 5
checks['A12_equals_A12prime'] = valuation[0][1] == valuation[0][2] + valuation[2][1]
checks['I_valuation_three'] = min(valuation[i][j] + valuation[j][i]
                                    for i in range(3) for j in range(i+1, 3)) == 3
assert all(checks.values()), checks
root = Path(__file__).resolve().parent
note = root / 'adjacent_factor_attempt.tex'
report = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'Exact finite matrix and GMA-valuation identities only; no arithmetic realization.',
    'checks': checks,
    'check_count': len(checks),
    'passed': all(checks.values()),
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'note_sha256': hashlib.sha256(note.read_bytes()).hexdigest(),
}
out = root / 'adjacent_factor_checks.json'
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))

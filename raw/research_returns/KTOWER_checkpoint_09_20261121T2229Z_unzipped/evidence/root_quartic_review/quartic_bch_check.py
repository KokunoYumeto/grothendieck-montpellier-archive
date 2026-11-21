#!/usr/bin/env python3
"""Compute BCH4 independently via exp/log in bivariate matrix polynomials."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as sp


def main():
    E = lambda i, j: sp.eye(3)[:, i] * sp.eye(3)[j, :]
    X, Y = E(0, 1) + E(1, 2), E(1, 0) - E(2, 1)
    Z = sp.diag(1, -2, 1)
    U, V = E(0, 1) - E(1, 2), E(1, 0) + E(2, 1)
    P, H, Q = E(0, 2), sp.diag(1, 0, -1), E(2, 0)
    A, B, C, M, N, a, b, c, m, n = sp.symbols('A B C M N a b c m n')
    left = {(1, 0): A * X, (0, 1): B * Y, (1, 1): C * Z,
            (2, 1): M * U, (1, 2): N * V}
    right = {(1, 0): a * X, (0, 1): b * Y, (1, 1): c * Z,
             (2, 1): m * U, (1, 2): n * V}

    def add(f, g, scale=1):
        h = dict(f)
        for d, v in g.items():
            h[d] = h.get(d, sp.zeros(3)) + scale * v
        return h

    def mul(f, g):
        h = {}
        for (i, j), v in f.items():
            for (r, s), w in g.items():
                d = (i + r, j + s)
                if sum(d) <= 4:
                    h[d] = h.get(d, sp.zeros(3)) + v * w
        return h

    def exp(f):
        power = {(0, 0): sp.eye(3)}
        out = dict(power)
        for i in range(1, 5):
            power = mul(power, f)
            out = add(out, power, sp.Rational(1, sp.factorial(i)))
        return out

    product = mul(exp(left), exp(right))
    product[(0, 0)] -= sp.eye(3)
    log = {}
    power = {(0, 0): sp.eye(3)}
    for i in range(1, 5):
        power = mul(power, product)
        log = add(log, power, sp.Rational((-1) ** (i + 1), i))

    cross = A * b - B * a
    positive = a * M - A * m + sp.Rational(1, 2) * (A - a) * (A * c - a * C) - A * a * cross / 4
    negative = b * N - B * n - sp.Rational(1, 2) * (B - b) * (B * c - b * C) + B * b * cross / 4
    diagonal = (A * n - B * m + b * M - a * N) / 2 + (A * B * c + a * b * C) / 2 - (C + c) * (A * b + B * a) / 4 - (A * b + B * a) * cross / 8
    expected = {(3, 1): positive * P, (2, 2): diagonal * H, (1, 3): negative * Q,
                (4, 0): sp.zeros(3), (0, 4): sp.zeros(3)}
    for d, v in expected.items():
        assert all(sp.expand(z) == 0 for z in log.get(d, sp.zeros(3)) - v), d

    bracket = lambda x, y: x * y - y * x
    identities = {
        'XXZ': bracket(X, bracket(X, Z)) - 6 * P,
        'YYZ': bracket(Y, bracket(Y, Z)) + 6 * Q,
        'XV': bracket(X, V) - H,
        'YU': bracket(Y, U) + H,
        'XQ': bracket(X, Q) - Y,
        'YP': bracket(Y, P) - X,
    }
    assert all(v == sp.zeros(3) for v in identities.values())
    J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    D = sp.diag(-1, 1, -1)
    kappa = lambda t: -D * J * t.T * J * D
    for vector, sign in ((X, 1), (Y, -1), (P, -1), (H, 1), (Q, -1)):
        assert kappa(vector) == sign * vector

    script = Path(__file__).resolve()
    report = {
        'utc': datetime.now(timezone.utc).isoformat(),
        'status': 'PASS',
        'method': 'Independent truncated matrix exponentials, product, and logarithm; comparison with three proposed BCH4 coefficient expressions',
        'quartic_monomials_checked': ['s4', 's3t', 's2t2', 'st3', 't4'],
        'brackets_checked': list(identities),
        'kappa_signs_checked': 5,
        'positive': str(positive), 'diagonal': str(diagonal), 'negative': str(negative),
        'scope': 'Exact rational polynomial identities only; no Galois class or arithmetic obstruction value evaluated',
        'script_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
    }
    path = script.with_suffix('.json')
    path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'report_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact symbolic certificates for AS-1--AS-3 (no numerical openness test)."""

import sympy as s


def flat(matrix):
    return s.Matrix(list(matrix))


def bracket(left, right):
    return left * right - right * left


def unit(i, j, n=4):
    result = s.zeros(n)
    result[i, j] = 1
    return result


def main():
    eye = s.eye(4)
    zero = s.zeros(2)
    symplectic = zero.row_join(s.eye(2)).col_join((-s.eye(2)).row_join(zero))
    a, b, c, d, e, f, g, h, i, j, t = s.symbols("a b c d e f g h i j t")
    upper = s.Matrix([[a, b], [c, d]])
    symmetric_b = s.Matrix([[e, f], [f, g]])
    symmetric_c = s.Matrix([[h, i], [i, j]])
    x = upper.row_join(symmetric_b).col_join(symmetric_c.row_join(-upper.T))
    assert x.T * symplectic + symplectic * x == s.zeros(4)
    plus, minus = eye + t * x, eye - t * x
    cayley_difference = plus.T * symplectic * plus - minus.T * symplectic * minus
    assert cayley_difference.applyfunc(s.expand) == s.zeros(4)
    print("Sp4 Cayley pulled-back alternating forms: identical polynomial matrices")

    roots = {
        "e1-e2": unit(0, 1) - unit(3, 2),
        "e2-e1": unit(1, 0) - unit(2, 3),
        "e1+e2": unit(0, 3) + unit(1, 2),
        "-e1-e2": unit(2, 1) + unit(3, 0),
        "2e1": unit(0, 2),
        "-2e1": unit(2, 0),
        "2e2": unit(1, 3),
        "-2e2": unit(3, 1),
    }
    for root in roots.values():
        assert root**2 == s.zeros(4)
        assert root.T * symplectic + symplectic * root == s.zeros(4)
        assert ((eye + t * root).T * symplectic * (eye + t * root)
                - symplectic).applyfunc(s.expand) == s.zeros(4)

    torus = s.diag(2, 1, s.Rational(1, 2), 1)
    expected = {"e1-e2": 2, "e1+e2": 2, "2e1": 4}
    for name, scalar in expected.items():
        root = roots[name]
        assert torus * root * torus.inv() == scalar * root
        commutator = torus * (eye + t * root) * torus.inv() * (eye - t * root)
        assert commutator == eye + (scalar - 1) * t * root
    print("Sp4 short/long root commutators: exact coefficients 1 and 3")

    basis = list(roots.values()) + [
        bracket(roots["2e1"], roots["-2e1"]),
        bracket(roots["2e2"], roots["-2e2"]),
    ]
    assert s.Matrix.hstack(*(flat(v) for v in basis)).rank() == 10
    derived = [flat(bracket(v, w)) for v in basis for w in basis]
    assert s.Matrix.hstack(*derived).rank() == 10
    variables = s.symbols("m0:16")
    m = s.Matrix(4, 4, variables)
    equations = [entry for v in basis for entry in bracket(m, v)]
    coefficients, _ = s.linear_eq_to_matrix(equations, variables)
    nullspace = coefficients.nullspace()
    assert len(nullspace) == 1 and nullspace[0] == flat(eye)
    print("sp4 basis rank = derived rank = 10; standard-action centralizer = scalar line")

    u, v, w = s.symbols("u v w")
    x2 = s.Matrix([[u, v], [w, -u]])
    assert x2**2 == (u*u + v*w) * s.eye(2)
    assert s.expand((s.eye(2) + t*x2).det() - (s.eye(2) - t*x2).det()) == 0
    print("RM trace-zero Cayley determinant identity: exact over any characteristic-zero field")

    aa, bb, xx, yy, zz = s.symbols("aa bb xx yy zz")
    # Left multiplication in the quaternion algebra i^2=aa, j^2=bb, ij=-ji.
    qi = s.Matrix([[0, aa, 0, 0], [1, 0, 0, 0], [0, 0, 0, aa], [0, 0, 1, 0]])
    qj = s.Matrix([[0, 0, bb, 0], [0, 0, 0, -bb], [1, 0, 0, 0], [0, -1, 0, 0]])
    assert qi**2 == aa * eye and qj**2 == bb * eye and qi*qj == -qj*qi
    pure = xx*qi + yy*qj + zz*(qi*qj)
    square = aa*xx**2 + bb*yy**2 - aa*bb*zz**2
    assert (pure**2 - square*eye).applyfunc(s.expand) == s.zeros(4)
    assert ((eye+t*pure)*(eye-t*pure) - (1-t*t*square)*eye).applyfunc(s.expand) == s.zeros(4)
    print("QM pure-quaternion Cayley norm identity: exact, including division forms")

    real_i = s.Matrix([[0, -1], [1, 0]])
    r, q = s.symbols("r q", real=True)
    anti = s.Matrix([[r, q], [q, -r]])
    assert anti*real_i == -real_i*anti
    assert anti.trace() == 0 and anti.det() == -r*r-q*q
    assert anti**2 == (r*r+q*q)*s.eye(2)
    print("Real anti-Hodge plane: trace 0, determinant -(r^2+q^2), positive square")
    print("PASS: symbolic identities only; strong approximation and openness are proved in the text")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact identities used in E.2.26; this does not test adelic openness."""

import sympy as s


def bracket(a, b):
    return a * b - b * a


def unit(i, j, n=3):
    a = s.zeros(n)
    a[i, j] = 1
    return a


def main():
    theta, d, x, y, z, j = s.symbols("theta d x y z j")

    def red(a):
        return s.rem(s.expand(a), theta**2 - d, theta)

    def rm(a):
        return a.applyfunc(red)

    def bar(a):
        return a.xreplace({theta: -theta})

    eye = s.eye(3)
    form = s.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    aa = x + y * theta
    bb = -(x*x - d*y*y) / 2 + z * theta
    q = s.Matrix([[1, -bar(aa), bb], [0, 1, aa], [0, 0, 1]])
    qi = s.Matrix([[1, bar(aa), bar(bb)], [0, 1, -aa], [0, 0, 1]])
    assert rm(q * qi) == eye
    assert rm(bar(q).T * form * q) == form
    assert q.det() == 1
    print("SU3 Q(a,b): exact inverse, determinant 1, and Hermitian preservation")

    derivatives = [q.diff(v).subs({x: 0, y: 0, z: 0}) for v in (x, y, z)]
    lower = [form * a * form for a in derivatives]
    h1, h2 = bracket(derivatives[0], lower[0]), bracket(derivatives[0], lower[1])
    assert h1 == s.diag(-1, 0, 1)
    assert h2 == theta * s.diag(-1, 2, -1)
    basis = derivatives + lower + [h1, h2]
    for a in basis:
        assert rm(bar(a).T * form + form * a) == s.zeros(3)
        assert a.trace() == 0

    def coeff_vector(a):
        entries = [red(v) for v in a]
        return s.Matrix([v.coeff(theta, 0) for v in entries]
                        + [v.coeff(theta, 1) for v in entries])

    coefficients = s.Matrix.hstack(*(coeff_vector(a) for a in basis))
    pivots = coefficients.T.rref()[1]
    minor = coefficients[list(pivots), :].det()
    assert minor == -1
    print(f"SU3 six root derivatives and two Cartan brackets: rank 8; exact minor {minor}")

    b_symbols = s.symbols("b0:9")
    b = s.Matrix(3, 3, b_symbols)
    adj = rm(q * b * qi)
    max_degree = max(s.Poly(v, x, y, z).total_degree() for v in adj)
    assert max_degree == 4
    print("SU3 adjoint upper-root family: polynomial degree exactly 4")

    n = theta * unit(0, 2)
    assert n*n == s.zeros(3)
    assert rm(bar(eye+n).T * form * (eye+n)) == form
    adj_power = rm((eye-j*n) * b * (eye+j*n))
    expected = rm(b + j*(b*n-n*b) - j*j*n*b*n)
    assert adj_power == expected
    assert max(s.Poly(v, j).degree() for v in adj_power) <= 2
    ell = s.symbols("ell", integer=True, positive=True)
    sums = [s.summation(j**r, (j, 0, ell-1)) for r in range(3)]
    expected_sums = [ell, ell*(ell-1)/2, ell*(ell-1)*(2*ell-1)/6]
    assert all(s.expand(a-b) == 0 for a, b in zip(sums, expected_sums))
    for value in sums:
        assert s.denom(s.cancel(value/ell)) in (1, 2, 6)
    print("Transvection adjoint power: exact degree-2 formula; sums divisible by ell for ell>=5")

    n6 = 6
    form6 = s.zeros(3).row_join(s.eye(3)).col_join((-s.eye(3)).row_join(s.zeros(3)))
    vectors = [unit(i, 0, n6)[:, 0] for i in range(n6)]
    vectors += [vectors[i] + vectors[k] for i in range(n6) for k in range(i+1, n6)]
    logarithms = [v * v.T * form6 for v in vectors]
    for a in logarithms:
        assert a*a == s.zeros(n6)
        assert a.T * form6 + form6 * a == s.zeros(n6)
    sp_coeff = s.Matrix.hstack(*(s.Matrix(list(a)) for a in logarithms))
    assert sp_coeff.rank() == 21
    print("Sp6 transvection logarithms: 21 independent exact matrices in sp6")

    determinant_map = s.Matrix([[2, 1], [1, 2]])
    hodge_classes = s.Matrix([[2, 1], [1, 1]])
    assert determinant_map.det() == 3 and hodge_classes.det() == 1
    print("CM determinant torus map determinant = 3; individual GU3 cocharacter lattice determinant = 1")
    print("PASS: symbolic identities only; the source theorems and actual arithmetic maps are proved in the work note")


if __name__ == "__main__":
    main()

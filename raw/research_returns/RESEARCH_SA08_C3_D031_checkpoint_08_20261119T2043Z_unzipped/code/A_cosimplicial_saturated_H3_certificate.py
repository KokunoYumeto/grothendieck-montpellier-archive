#!/usr/bin/env python3
"""Exact small certificate for the saturated resolved-tail H3 class.

Uses the signs of A-L11.  All algebra is rational, with odd generators
exterior.  The explicitly listed integral lattices are checked directly;
the nonboundary certificate is a mod-two coordinate functional, not a
numerical rank inference.  Also verifies the actual nonzero twist and
the low normalized quadratic parameter matrices.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import time


NAMES = ["T", "C", "K", "a", "b", "r", "sigma", "x", "y", "g", "l", "E", "F", "old_x", "old_y"]
DEGREES = [0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 1, 2]
INDEX = {name: i for i, name in enumerate(NAMES)}
ZERO_MONOMIAL = (0,) * len(NAMES)


def clean(a):
    return {m: Q(c) for m, c in a.items() if c}


def add(*terms):
    out = {}
    for term in terms:
        for m, c in term.items():
            out[m] = out.get(m, Q(0)) + c
    return clean(out)


def scale(c, a):
    return clean({m: Q(c) * v for m, v in a.items()})


def mul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            if any(DEGREES[i] % 2 and ma[i] and mb[i] for i in range(len(NAMES))):
                continue
            sign = (-1) ** sum(ma[i] * mb[j] for i in range(len(NAMES)) for j in range(i)
                               if DEGREES[i] % 2 and DEGREES[j] % 2)
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, Q(0)) + sign * ca * cb
    return clean(out)


def var(name):
    m = list(ZERO_MONOMIAL)
    m[INDEX[name]] = 1
    return {tuple(m): Q(1)}


V = {name: var(name) for name in NAMES}
T, C, K, a, b, r, sigma, x, y, g, l, E, F, old_x, old_y = [V[n] for n in NAMES]
U = scale(Q(1, 2), mul(T, T))
H = add(K, scale(Q(-1, 2), mul(T, C)))
J = scale(Q(1, 2), mul(T, H))
eta_old = mul(old_x, old_y)
z_old = scale(Q(1, 2), mul(old_y, old_y))


def differential_table(twisted=False):
    table = {
        "T": {},
        "C": add(scale(2, g), mul(T, x), scale(-2, y)),
        "K": add(scale(2, l), mul(U, x), scale(-1, mul(T, y))),
        "a": scale(2, E), "b": scale(2, F),
        "r": add(scale(-1, mul(T, E)), scale(2, F)),
        "sigma": add(scale(-1, mul(U, E)), mul(T, F)),
        "x": add(scale(2, r), mul(T, a), scale(-2, b)),
        "y": add(scale(2, sigma), mul(U, a), scale(-1, mul(T, b))),
        "g": add(scale(-1, mul(T, r)), scale(2, sigma)),
        "l": add(scale(-1, mul(U, r)), mul(T, sigma)),
        "E": {}, "F": {}, "old_x": old_y, "old_y": {},
    }
    if twisted:
        table["a"] = add(table["a"], scale(-1, mul(T, eta_old)))
        table["b"] = add(table["b"], scale(-1, mul(U, eta_old)))
        table["E"] = mul(T, z_old)
        table["F"] = mul(U, z_old)
    return table


def d(poly, table):
    out = {}
    for monomial, coefficient in poly.items():
        prefix_degree = 0
        for i, exponent in enumerate(monomial):
            if not exponent:
                continue
            remaining = list(monomial)
            remaining[i] -= 1
            # The derivative is placed before the remaining ordered monomial.
            sign = (-1) ** prefix_degree
            left = [0] * len(NAMES)
            right = list(remaining)
            for j in range(i):
                left[j], right[j] = right[j], 0
            term = mul(mul({tuple(left): Q(1)}, table[NAMES[i]]), {tuple(right): Q(1)})
            out = add(out, scale(coefficient * exponent * sign, term))
            prefix_degree += exponent * DEGREES[i]
    return out


def coefficient(poly, monomial):
    assert len(monomial) == 1
    key, value = next(iter(monomial.items()))
    return poly.get(key, Q(0)) / value


def serial(poly):
    return [{"coefficient": str(c), "monomial": {
        n: e for n, e in zip(NAMES, m) if e}} for m, c in sorted(poly.items())]


def main():
    started = time.perf_counter()
    plain, twisted = differential_table(), differential_table(True)
    for table in (plain, twisted):
        for name in NAMES:
            assert not d(d(V[name], table), table), (name, table is twisted)

    beta = add(mul(a, H), scale(-1, mul(C, r)), scale(-1, mul(g, x)))
    zeta = add(mul(E, K), scale(-1, mul(F, C)), mul(r, y),
               scale(-1, mul(sigma, x)), scale(-1, mul(g, b)), mul(l, a))
    zeta_tw = add(zeta, scale(-1, mul(J, eta_old)))
    assert d(beta, plain) == scale(2, zeta)
    assert not d(zeta, plain)
    assert d(beta, twisted) == scale(2, zeta_tw)
    assert not d(zeta_tw, twisted)
    assert d(H, plain) == add(scale(-1, mul(T, g)), scale(2, l))
    assert d(J, plain) == add(scale(-1, mul(U, g)), mul(T, l))
    assert mul(T, H) == scale(2, J)

    # This is the entire integral arity-two degree-two lattice in weight 2s+5.
    basis2_names = ["C*r", "g*x", "a*H", "a*K", "b*C", "x*y"]
    basis2 = [mul(C, r), mul(g, x), mul(a, H), mul(a, K), mul(b, C), mul(x, y)]
    # In degree three the independent zero-form/three-form summand has
    # basis E*H,E*K,F*C.  If p=q0 E*H+q1 E*K+q2 F*C+..., then in the
    # rational monomial basis q1=coeff(E*K)+2*coeff(T*E*C).
    def detector_integer(poly):
        value = coefficient(poly, mul(E, K)) + 2 * coefficient(poly, mul(mul(T, E), C))
        assert value.denominator % 2
        return value
    detector_values = [detector_integer(d(v, plain)) for v in basis2]
    assert all(v.numerator % 2 == 0 for v in detector_values)
    assert detector_integer(zeta).numerator % 2 == 1

    chi2 = add(mul(g, x), scale(-1, mul(y, x)), mul(C, r),
               scale(-1, mul(C, b)), mul(add(K, scale(-1, H)), a))
    assert d(mul(C, x), plain) == scale(2, chi2)
    assert not d(chi2, plain)

    # Low normalized parameter complexes, using the quotient by degeneracies.
    # e is the K(Z,2) generator, a=s2(e), b=s1(e), c=s0(e).
    face_values = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 0]]
    pairs = [(0, 1), (0, 2), (1, 2)]
    symmetric_boundary = [sum((-1) ** i * face_values[j][i] * face_values[k][i]
                              for i in range(4)) for j, k in pairs]
    divided_boundary = [2 * x for x in symmetric_boundary]
    tensor_boundary = sum((-1) ** i * face_values[1][i] * face_values[0][i] for i in range(4))
    assert symmetric_boundary == [1, 0, -1]
    assert divided_boundary == [2, 0, -2]
    assert tensor_boundary == 1

    result = {
        "status": "all exact checks passed",
        "coefficient_ring": "Z_(2)",
        "arity": 2, "weight": "2s+5", "s_minimum": 5,
        "integral_C2_basis": basis2_names,
        "boundary_detector_values": [str(v) for v in detector_values],
        "zeta_detector": str(detector_integer(zeta)),
        "beta": serial(beta), "zeta": serial(zeta), "twisted_zeta": serial(zeta_tw),
        "checks": {"d_squared_on_generators_plain_and_twisted": 2 * len(NAMES),
                   "d_beta_equals_2_zeta": True, "zeta_closed": True,
                   "d_beta_equals_2_twisted_zeta": True, "twisted_zeta_closed": True,
                   "T_H_equals_2_J": True, "J_has_integral_differential": True,
                   "mod2_detector_kills_entire_C2_lattice": True,
                   "mod2_detector_detects_zeta": True,
                   "H2_cycle_and_boundary_formula": True},
        "parameter_degree3_to_degree2": {
            "Sym2": symmetric_boundary, "Gamma2": divided_boundary,
            "tensor_b_tensor_a_boundary": tensor_boundary,
            "H2_Sym2": "0", "H2_Gamma2": "Z/2"},
        "saturation_argument": "Arity-one W is exact below3; rational zero-forms of arity>=2 begin weight2s+6. The proof of persistence is in A_saturated_tail_H3.tex, not extrapolated from a finite matrix.",
        "runtime_seconds": time.perf_counter() - started,
    }
    destination = Path(__file__).resolve().parents[1] / "logs" / "A_cosimplicial_saturated_H3_certificate.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "runtime_seconds": result["runtime_seconds"],
                      "boundary_detector_values": result["boundary_detector_values"],
                      "zeta_detector": result["zeta_detector"]}))


if __name__ == "__main__":
    main()

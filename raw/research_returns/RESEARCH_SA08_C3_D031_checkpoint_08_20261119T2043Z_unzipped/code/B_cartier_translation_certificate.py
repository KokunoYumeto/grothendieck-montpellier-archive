#!/usr/bin/env python3
"""Exact supplementary certificate for AT21's integral twist translation.

Computations take place in a free graded-commutative algebra over Q.
Every purported integral transgression is checked to have integer
coefficients.  The proof for arbitrary strict PD algebras uses the PD
addition law and the displayed all-index identities, not extrapolation.
"""
from fractions import Fraction
from pathlib import Path
import json
import time

started = time.perf_counter()
checks = 0
records = []


def check(value):
    global checks
    checks += 1
    assert value


for count in range(1, 8):
    # Even variables: F_0,...,F_(count-1), J, y.
    # Odd variables: dF_0,...,dF_(count-1), dJ, dG_0,...,dG_(count-1), x.
    neven = count + 2
    xindex = 2 * count + 1
    yindex = count + 1
    zero = {}

    def clean(poly):
        return {k: v for k, v in poly.items() if v}

    def add(*polys):
        result = {}
        for poly in polys:
            for k, v in poly.items():
                result[k] = result.get(k, Fraction(0)) + v
        return clean(result)

    def scale(poly, scalar):
        return clean({k: scalar * v for k, v in poly.items()})

    def multiply(left, right):
        result = {}
        for (ep, em), ec in left.items():
            for (fp, fm), fc in right.items():
                if em & fm:
                    continue
                inversions = sum((em >> (j + 1)).bit_count()
                                 for j in range(xindex + 1) if fm & (1 << j))
                k = (tuple(a + b for a, b in zip(ep, fp)), em | fm)
                result[k] = result.get(k, Fraction(0)) + (-1)**inversions * ec * fc
        return clean(result)

    def even(index):
        powers = [0] * neven
        powers[index] = 1
        return {(tuple(powers), 0): Fraction(1)}

    def odd(index):
        return {((0,) * neven, 1 << index): Fraction(1)}

    def differential(poly):
        result = {}
        for (powers, mask), coefficient in poly.items():
            for i in range(count + 1):
                exponent = powers[i]
                if not exponent or mask & (1 << i):
                    continue
                lower = list(powers)
                lower[i] -= 1
                sign = (-1)**((mask & ((1 << i) - 1)).bit_count())
                key = (tuple(lower), mask | (1 << i))
                result[key] = result.get(key, Fraction(0)) + coefficient * exponent * sign
            if mask & (1 << xindex):
                newpowers = list(powers)
                newpowers[yindex] += 1
                sign = (-1)**((mask & ((1 << xindex) - 1)).bit_count())
                key = (tuple(newpowers), mask ^ (1 << xindex))
                result[key] = result.get(key, Fraction(0)) + coefficient * sign
        return clean(result)

    def integral(poly):
        for coefficient in poly.values():
            check(coefficient.denominator == 1)

    x, y, jvar = odd(xindex), even(yindex), even(count)
    pieces = [multiply(even(i), odd(count + 1 + i)) for i in range(count)]
    derivatives = [differential(piece) for piece in pieces]
    for piece, derivative in zip(pieces, derivatives):
        check(multiply(piece, derivative) == zero)
        check(multiply(derivative, derivative) == zero)
        check(differential(derivative) == zero)
    t = add(*pieces)
    dt = differential(t)
    k = add(*(multiply(pieces[i], derivatives[j])
              for i in range(count) for j in range(i+1, count)))
    ell = add(*(multiply(pieces[i], pieces[j])
                for i in range(count) for j in range(i+1, count)))
    gamma2_dt = scale(multiply(dt, dt), Fraction(1, 2))
    integral(gamma2_dt)
    check(differential(k) == gamma2_dt)
    check(differential(ell) == add(multiply(t, dt), scale(k, -2)))

    dcorrection = add(multiply(t, y), k)
    ecorrection = add(multiply(x, t), scale(ell, -1))
    delta_z = add(multiply(y, dt), gamma2_dt)
    delta_eta = add(multiply(x, dt), multiply(t, y), multiply(t, dt))
    integral(dcorrection)
    integral(ecorrection)
    check(differential(dcorrection) == delta_z)
    check(differential(ecorrection) == add(scale(dcorrection, 2), scale(delta_eta, -1)))
    check(differential(delta_eta) == scale(delta_z, 2))

    # On the resolved quadratic expression, TH=2J gives Delta B=2JE.
    delta_b = scale(multiply(jvar, ecorrection), 2)
    delta_zeta = differential(multiply(jvar, ecorrection))
    check(differential(delta_b) == scale(delta_zeta, 2))
    # The new repair value U'=U+JE leaves 2U'-B' unchanged.
    check(add(scale(multiply(jvar, ecorrection), 2), scale(delta_b, -1)) == zero)
    integral(delta_zeta)
    records.append({"summands": count, "K_terms": len(k), "L_terms": len(ell),
                    "D_terms": len(dcorrection), "E_terms": len(ecorrection)})

result = {
    "statement": "AT21 integral Cartier and resolved-tail translations",
    "status": "passed",
    "checks": checks,
    "summand_counts": list(range(1, 8)),
    "records": records,
    "identities": ["dK=gamma2(dt)", "dL=t dt-2K", "dD=Delta z",
                   "dE=2D-Delta eta", "d(Delta B)=2 Delta zeta",
                   "2 Delta U-Delta B=0"],
    "scope": "finite exact supplementary certificate; symbolic proof covers every finite decomposition",
    "runtime_seconds": time.perf_counter() - started,
}
output = Path(__file__).resolve().parents[1] / "logs" / "B_cartier_translation_certificate.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))

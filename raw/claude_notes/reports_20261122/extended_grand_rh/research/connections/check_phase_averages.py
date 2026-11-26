"""Algebraic tests for the phase-average note, plus numerical Hurwitz checks.

SymPy checks discriminants exactly. mpmath checks the leading coefficient at
the first zeta zero numerically. The multiplicity theorem has an analytic proof.
"""

from math import gcd

import mpmath as mp
import sympy as sp


def check_polynomials():
    x, t = sp.symbols("x t")
    for d in (1, 2, 3, 4):
        for m in range(1, 8):
            disc = sp.Poly(sp.discriminant(x**m - t**d, x), t)
            assert len(disc.terms()) == 1 and disc.terms()[0][0] == (d*(m-1),)
            unseen = set(range(m))
            cycles = []
            while unseen:
                start = next(iter(unseen))
                j, length = start, 0
                while j in unseen:
                    unseen.remove(j)
                    length += 1
                    j = (j+d) % m
                assert j == start
                cycles.append(length)
            assert cycles == [m//gcd(m,d)]*gcd(m,d)
        for a, b in ((1, 3), (2, 2), (2, 3)):
            polynomial = (x**a-t**d)*((x-3)**b-2*t**d)
            disc = sp.Poly(sp.discriminant(polynomial, x), t)
            assert min(k[0] for k, _ in disc.terms()) == d*(a+b-2)


def check_hurwitz():
    mp.mp.dps = 75
    rho = mp.zetazero(1)
    t = mp.mpf("0.00001")
    for d in (1, 2, 3):
        root = mp.exp(2*mp.pi*mp.j/d)
        value = sum(mp.zeta(rho, 1+root**j*t) for j in range(d))/d
        expected = (-1)**d*mp.rf(rho,d)*mp.zeta(rho+d)/mp.factorial(d)
        second = mp.rf(rho,2*d)*mp.zeta(rho+2*d)/mp.factorial(2*d)
        error = abs((value-mp.zeta(rho))/t**d-expected)/abs(expected)
        observed_second = (value-mp.zeta(rho)-expected*t**d)/t**(2*d)
        assert abs(observed_second/second-1) < mp.mpf("0.001")
        print(f"d={d}, first-zero leading coefficient relative error {float(error):.3g}")


def check_two_prime_rounding():
    order = 16
    weights = {k: sp.Rational(order-abs(k), order**2) for k in range(1-order, order)}
    assert sum(weights.values()) == 1
    assert sum(w*k**2 for k, w in weights.items()) == sp.Rational(order**2-1, 6)
    mp.mp.dps = 50
    a, b = mp.log(2), mp.log(3)
    other = 2*mp.pi/a
    noise = mp.mpf("0.1")
    chord = abs(mp.exp(mp.j*b*other)-1)
    assert chord > mp.mpf("1.9")
    table = []
    for k, w in weights.items():
        for l, v in weights.items():
            frequency = k*a + l*b
            moment = 2 + mp.exp(mp.j*frequency*other)
            measured = moment + noise*mp.exp(mp.j*(k-l))
            table.append((frequency, float(w*v), measured))
            separation = mp.mpf("0.0001")
            difference = 2*abs(1-mp.cos(frequency*separation))
            assert difference <= ((order-1)*(a+b)*separation)**2
    for ordinate, mass in ((0, 2), (other, 1)):
        for offset in (0, mp.mpf("0.001")):
            target = ordinate + offset
            estimated = mp.re(sum(w*mp.exp(-mp.j*f*target)*value for f, w, value in table))
            remaining = other if ordinate == 0 else 0
            gap = max(abs(mp.exp(mp.j*c*(remaining-target))-1) for c in (a, b))
            error = noise + 3*(order**2-1)*(a*a+b*b)*offset**2/12 + 12/(order**2*gap**2)
            assert abs(estimated-mass) <= error < mp.mpf("0.5")
            assert int(mp.nint(estimated)) == mass
    print("Two-prime model: recovered masses 2 and 1 at exact and displaced targets; "
          "checked the double/split bound at all 961 frequencies.")


if __name__ == "__main__":
    check_polynomials()
    print("28 monodromy/discriminant checks and 12 two-cluster discriminants passed.")
    check_hurwitz()
    check_two_prime_rounding()

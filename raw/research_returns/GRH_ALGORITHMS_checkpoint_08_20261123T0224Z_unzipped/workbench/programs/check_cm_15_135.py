"""Exact finite certificate for the ramified CM class-polynomial gate.

Run with standard-library Python from any working directory. The sibling
module derive_cm_inputs.py obtains H_-15 and Phi_3 from exact q-series and
rational CM intervals. No polynomial coefficient table is required as input.
This checker derives H_-135 by an integer resultant and proves its two
factor patterns by exact Frobenius gcds. It also constructs a degree-three
subfield polynomial at p=17. No factorization oracle is used.

The identity Res_Y(H_-15(Y),Phi_3(X,Y))=H_-15(X)H_-135(X)
uses the ramified 3-isogeny pattern: one horizontal and three descending
isogenies at each of the two maximal-order CM classes, and one ascending
isogeny at each of the six conductor-3 classes. Thus every lower-level
CM value occurs once. This is a certificate of the displayed finite cases,
not a uniform construction of suitable CM discriminants.
"""

from math import gcd, isqrt
import json
from derive_cm_inputs import derive


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([x*c for x in a])


def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def divrem(a, b, p=None):
    a, b = trim(a), trim(b)
    assert b != [0]
    q = [0]*max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        d = len(a)-len(b)
        if p is None:
            assert a[-1] % b[-1] == 0
            c = a[-1]//b[-1]
        else:
            c = a[-1]*pow(b[-1], -1, p) % p
        q[d] = c
        for j, x in enumerate(b):
            a[d+j] -= c*x
            if p is not None:
                a[d+j] %= p
        a = trim(a)
    return trim(q), a


def mod(a, f, p):
    return divrem([x % p for x in a], f, p)[1]


def powmod(a, n, f, p):
    out = [1]
    while n:
        if n & 1:
            out = mod(mul(out, a), f, p)
        a = mod(mul(a, a), f, p)
        n //= 2
    return out


def pgcd(a, b, p):
    while b != [0]:
        a, b = b, divrem(a, b, p)[1]
    return [c*pow(a[-1], -1, p) % p for c in a] if a != [0] else [0]


def reduced_forms(D):
    out = []
    for a in range(1, isqrt((-D)//3)+1):
        for b in range(-a, a+1):
            if (b*b-D) % (4*a):
                continue
            c = (b*b-D)//(4*a)
            if a > c or gcd(gcd(a, b), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            out.append([a, b, c])
    return out


def class_polynomial_135(h15, sparse_phi3):
    # Reduce powers of Y modulo H15(Y): represent each as v + u*Y.
    b, a, _ = h15
    powers = [(1, 0)]
    for _ in range(4):
        v, u = powers[-1]
        powers.append((-b*u, v-a*u))
    v, u = [0], [0]
    for i, j, c in sparse_phi3:
        for ix, iy in ([(i, j)] if i == j else [(i, j), (j, i)]):
            c0, c1 = powers[iy]
            v = add(v, [0]*ix+[c*c0])
            u = add(u, [0]*ix+[c*c1])
    # Norm(v+uY)=v^2-a*u*v+b*u^2.
    resultant = add(add(mul(v, v), scale(mul(u, v), -a)),
                    scale(mul(u, u), b))
    answer, remainder = divrem(resultant, h15)
    assert remainder == [0]
    assert len(answer) == 7 and answer[-1] == 1
    assert mul(h15, answer) == resultant
    return answer


def certificate():
    inputs = derive()
    H15 = inputs['H15_ascending']
    SPARSE_PHI3 = inputs['Phi3_symmetric_sparse_terms']
    H135 = class_polynomial_135(H15, SPARSE_PHI3)
    forms = {str(D): reduced_forms(D) for D in (-15, -135)}
    assert len(forms['-15']) == 2 and len(forms['-135']) == 6
    certificates = []
    for p, t, v, degrees in [(17, 14, 8, [6]),
                              (107, 106, 48, [2, 2, 2])]:
        assert 4*p*p == t*t+15*v*v and t % p != 0
        assert p % 45 == 17
        base = [c % p for c in H15]
        assert powmod([0, 1], p*p, base, p) == [0, 1]
        assert pgcd(base, mod(add(powmod([0, 1], p, base, p),
                                  [0, -1]), base, p), p) == [1]
        f = [c % p for c in H135]
        frobenius = [[0, 1]]
        for _ in range(6):
            frobenius.append(powmod(frobenius[-1], p, f, p))
        x = [0, 1]
        gcds = {str(k): pgcd(f, mod(add(frobenius[k], [0, -1]), f, p), p)
                for k in (1, 2, 3)}
        if p == 17:
            assert frobenius[6] == x
            assert gcds['2'] == [1] and gcds['3'] == [1]
        else:
            assert frobenius[2] == x and gcds['1'] == [1]
        descent = None
        if p == 17:
            # The quadratic relative trace lies in the degree-three subfield.
            beta = mod(add(x, frobenius[3]), f, p)
            orbit = [beta]
            for _ in range(2):
                orbit.append(powmod(orbit[-1], p, f, p))
            assert powmod(orbit[-1], p, f, p) == beta
            assert len({tuple(z) for z in orbit}) == 3
            coefficients = [[1]]
            for z in orbit:
                product = [[0] for _ in range(len(coefficients)+1)]
                for i, c in enumerate(coefficients):
                    product[i] = mod(add(product[i], scale(mul(c, z), -1)), f, p)
                    product[i+1] = mod(add(product[i+1], c), f, p)
                coefficients = product
            assert all(len(c) == 1 for c in coefficients)
            minimal = [c[0] for c in coefficients]
            values = [sum(c*pow(z, i, p) for i, c in enumerate(minimal)) % p
                      for z in range(p)]
            assert len(minimal) == 4 and minimal[-1] == 1 and all(values)
            descent = {
                'element': 'alpha + alpha^(17^3)',
                'element_coefficients_in_power_basis_ascending': beta,
                'frobenius_orbit_coefficients_ascending': orbit,
                'minimal_polynomial_over_F17_ascending': minimal,
                'values_at_0_through_16': values,
            }
        certificates.append({
            'p': p, 't': t, 'v': v, 'v_mod_3': v % 3,
            'H15_mod_p_ascending': base, 'H15_irreducible': True,
            'H135_mod_p_ascending': f,
            'factor_degrees': degrees,
            'frobenius_remainders_ascending': frobenius,
            'gcds_with_X_p_to_k_minus_X': gcds,
            'degree_three_subfield': descent,
        })
    out = {
        'D': -15, 'r': 3, 'H15_ascending': H15,
        'input_derivation': {
            'program': 'derive_cm_inputs.py',
            'method': 'exact modular q-series and rational interval CM evaluation',
            'Phi3_checked_q_exponents': inputs['Phi3_checked_q_exponents'],
            'Phi3_required_by_cusp_pole_bound': inputs['Phi3_required_by_cusp_pole_bound'],
            'H15_interval_certificate': inputs['H15_interval_certificate'],
        },
        'Phi3_symmetric_sparse_terms': SPARSE_PHI3,
        'H135_ascending': H135, 'reduced_primitive_forms': forms,
        'certificates': certificates,
        'verification': 'independently derived inputs, exact integer resultant, finite-field Frobenius gcds, and subfield polynomial',
        'scope': 'Exact certificate for two finite primes; no uniform discriminant-search bound.',
    }
    return out


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))

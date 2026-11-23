"""Exact G166 finite checks; no new analytic or class-number computation.

Integer character sums and floor sums are independent loops.  Global units
are verified in their quartic regular representation before local reduction.
"""
from pathlib import Path
from datetime import datetime, timezone
from math import gcd, isqrt
from fractions import Fraction
import hashlib
import json
import sympy as S

BASE = Path(__file__).resolve().parent
P, F = 269, 48*269
assert all(P % d for d in range(2, isqrt(P)+1))
logs = {pow(2, j, P): j for j in range(P-1)}
assert len(logs) == 268 and pow(2, 67, P) == 187
assert 82**2 % P == P-1
iv = [(1, 0), (0, 1), (-1, 0), (0, -1)]
phi_exponent = {1: 0, 7: 0, 13: 1, 11: 1,
                9: 2, 15: 2, 5: 3, 3: 3}

def mul_gauss(a, b):
    x, y = a
    u, v = b
    return (x*u-y*v, x*v+y*u)

def character(a, tau):
    if gcd(a, F) != 1:
        return (0, 0)
    eta = 1 if a % 3 == 1 else -1
    exponent = phi_exponent[a % 16] - tau*logs[a % P]
    x, y = iv[exponent % 4]
    return (eta*x, eta*y)

assert 3229 % 16 == 13 and 3229 % 3 == 1 and 3229 % P == 1
characters = []
for tau, expected_B, expected_A in [(1, [36, -12], [192, 24]),
                                   (-1, [-24, -20], [-100, 124])]:
    weighted, total = [0, 0], [0, 0]
    for a in range(1, F+1):
        x, y = character(a, tau)
        weighted[0] += a*x
        weighted[1] += a*y
        total[0] += x
        total[1] += y
    assert total == [0, 0]
    B = [Fraction(x, F) for x in weighted]
    assert B == expected_B
    assert character(5, tau) == (0, 1)
    assert character(3229, tau) == (0, 1)
    inverse_floor = [0, 0]
    units = 0
    for a in range(1, F+1):
        if gcd(a, F) == 1:
            units += 1
            x, y = character(a, tau)
            inverse_floor[0] += (5*a//F)*x
            inverse_floor[1] -= (5*a//F)*y
    assert units == 4288
    assert inverse_floor == expected_A
    assert tuple(inverse_floor) == mul_gauss((5, -1), (B[0], -B[1]))
    scalars = [(inverse_floor[0]+sign*82*inverse_floor[1]) % P
               for sign in (1, -1)]
    assert all(scalars)
    characters.append({
        'psi_exponent': tau, 'conductor': F,
        'weighted_sum': weighted, 'B1': list(map(int, B)),
        'B1_norm': int(B[0]**2+B[1]**2),
        'inverse_floor_sum': inverse_floor,
        'annihilator_scalars_character_and_inverse': scalars,
        'character_5': [0, 1], 'character_b0_CRT3229': [0, 1],
        'cyclotomic_degree': units, 'cyclotomic_relative_degree': units//4,
    })
assert [c['annihilator_scalars_character_and_inverse'] for c in characters] == [[8, 107], [115, 223]]

def multiply(a, b):
    out = [0]*4
    for j, x in enumerate(a):
        for k, y in enumerate(b[:4-j]):
            out[j+k] = (out[j+k]+x*y) % P
    return out

def compose(f, a):
    out = [0]*4
    for x in reversed(f):
        out = multiply(out, a)
        out[0] = (out[0]+x) % P
    return out

X = S.Symbol('X')
fields = []
for index, c, A, selected in [(1, 18, 1067, 2), (2, 1058, 547, 3)]:
    source = BASE/f'inputs/G147_field{index}_units.json'
    data = json.loads(source.read_text())
    unit = next(u for u in data['units'] if u['unit'] == selected)
    ns = list(map(int, unit['numerators']))
    den = int(unit['common_denominator'])
    assert len(ns) == 12 and ns[4:] == [0]*8
    assert den % P != 0
    f = X**4-4*P*X**2+c*P
    W = S.Matrix([[0, 0, 0, -c*P], [1, 0, 0, 0],
                  [0, 1, 0, 4*P], [0, 0, 1, 0]])
    I = S.eye(4)
    U = sum((S.Rational(ns[j], den)*W**j for j in range(4)), S.zeros(4))
    polyq = U.charpoly(X).all_coeffs()
    assert all(a.q == 1 for a in polyq) and abs(polyq[-1]) == 1
    poly = list(map(int, polyq))
    evaluation = S.zeros(4)
    for a in poly:
        evaluation = evaluation*U+a*I
    assert evaluation == S.zeros(4)
    assert list(map(int, S.Poly(S.Poly.from_list(poly, X).as_expr()**3, X).all_coeffs())) == list(map(int, unit['monic_annihilator']))
    b = (X**3-A*X)/69
    assert S.rem(f.subs(X, b), f, X) == 0
    assert S.rem(b.subs(X, b)+X, f, X) == 0
    k = 23 if index == 1 else 3
    sq = (W**2-2*P*I)/k
    assert sq**2 == 2*P*I
    fp = X**4+12*P*X**2+9*c*P
    bp = -(X**3+3*A*X)/207
    assert S.rem(fp.subs(X, bp), fp, X) == 0
    assert S.rem(bp.subs(X, bp)+X, fp, X) == 0

    red = [n*pow(den, -1, P) % P for n in ns[:4]]
    assert red[0] != 0
    derivative_log = []
    for n in range(3):
        derivative_log.append(((n+1)*red[n+1]
                               -sum(red[j]*derivative_log[n-j] for j in range(1, n+1)))
                              *pow(red[0], -1, P) % P)
    log = [0]+[a*pow(n+1, -1, P) % P for n, a in enumerate(derivative_log)]
    b_local = [0, -A*pow(69, -1, P) % P, 0, pow(69, -1, P)]
    assert b_local[1] == (82 if index == 1 else 187)
    assert compose(b_local, b_local) == [0, P-1, 0, 0]
    projectors = {}
    for lam in (82, 187):
        out, orbit = [0]*4, log[:]
        for n in range(4):
            out = [(out[j]+pow(lam, -n, P)*orbit[j]) % P for j in range(4)]
            orbit = compose(orbit, b_local)
        assert orbit == log
        assert compose(out, b_local) == [lam*x % P for x in out]
        assert any(out)
        projectors[str(lam)] = out
    fields.append({
        'field_index': index, 'c': c, 'b_parameter': A,
        'real_polynomial': [1, 0, -4*P, 0, c*P],
        'imaginary_companion_polynomial': [1, 0, 12*P, 0, 9*c*P],
        'quadratic_generator': f'(beta^2-{2*P})/{k}',
        'unit_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'unit_index': selected, 'unit_numerators': ns[:4],
        'unit_denominator': den, 'monic_quartic_annihilator': poly,
        'source_degree12_relation_is_cube': True,
        'local_reduction': red, 'local_normalized_log': log,
        'local_b_action': b_local, 'local_quartic_projectors': projectors,
    })

result = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS_EXACT_FINITE_ONLY', 'p': P,
    'character_convention': 'phi(13)=i; psi(2)=-i; i=82 modulo269',
    'companion_characters': characters, 'fields': fields,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope': 'Exact primitive-character sums, integral Stickelberger floor sums, quartic field identities, two actual units and both local projector images. Class/strict deductions require the separately written proof; no new analytic or complete-unit computation.'
}
(BASE/'pure_conductor16_quartic_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))

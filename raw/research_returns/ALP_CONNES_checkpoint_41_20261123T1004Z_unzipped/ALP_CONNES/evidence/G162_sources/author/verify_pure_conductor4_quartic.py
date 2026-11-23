"""Exact G162 finite certificate: Stickelberger sums and one global unit.

No analytic interval, proposed class number or complete unit basis is used.
"""
from pathlib import Path
from datetime import datetime, timezone
from math import gcd, isqrt
from fractions import Fraction
import hashlib
import json
import sympy as S

BASE = Path(__file__).resolve().parent
P, F = 269, 12*269
assert all(P % q for q in range(2, isqrt(P)+1))
logs = {pow(2, j, P): j for j in range(P-1)}
assert len(logs) == 268
assert pow(2, 67, P) == 187 and 82*82 % P == P-1
values = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def chi12(a):
    r = a % 12
    return 1 if r in (1, 11) else -1 if r in (5, 7) else 0

def xi(a):
    d = chi12(a)
    if not d or a % P == 0:
        return (0, 0)
    x, y = values[logs[a % P] % 4]
    return (d*x, d*y)

weighted = [0, 0]
floor_inverse = [0, 0]
character_sum = [0, 0]
residues = []
for a in range(1, F+1):
    x, y = xi(a)
    character_sum[0] += x
    character_sum[1] += y
    weighted[0] += a*x
    weighted[1] += a*y
    if gcd(a, F) == 1:
        residues.append(a)
        # (5-sigma_5)theta has coefficient floor(5a/F) at sigma_a^-1.
        floor_inverse[0] += (5*a//F)*x
        floor_inverse[1] -= (5*a//F)*y
assert character_sum == [0, 0]
assert len(residues) == 1072
assert weighted == [6456, 45192]
B1 = [Fraction(a, F) for a in weighted]
assert B1 == [2, 14] and xi(5) == (-1, 0)
assert 1885 % 12 == 1 and 1885 % P == 2 and xi(1885) == (0, -1)
assert floor_inverse == [12, -84]
scalars = [(12-84*82) % P, (12+84*82) % P]
assert scalars == [118, 175] and all(scalars)
assert (2**2 + 14**2) % P != 0

source = BASE/'inputs/G152_units.json'
data = json.loads(source.read_text())
unit = next(u for u in data['units'] if u['unit'] == 2)
nums = list(map(int, unit['numerators']))
assert nums == [3464441, -655959, -14375, 2721] + [0]*8
assert int(unit['common_denominator']) == 13

X = S.Symbol('X')
f = X**4-P*X**2+25*P
W = S.Matrix([[0, 0, 0, -25*P], [1, 0, 0, 0],
              [0, 1, 0, P], [0, 0, 1, 0]])
I = S.eye(4)
U = sum((S.Rational(nums[j], 13)*W**j for j in range(4)), S.zeros(4))
poly = list(map(int, U.charpoly(X).all_coeffs()))
assert poly == [1, -471078, -107707606, 471078, 1]
assert U.det() == 1
evaluation = S.zeros(4)
for a in poly:
    evaluation = evaluation*U+a*I
assert evaluation == S.zeros(4)
assert list(map(int, S.Poly(S.Poly.from_list(poly, X).as_expr()**3, X).all_coeffs())) == list(map(int, unit['monic_annihilator']))
b = (X**3-219*X)/65
assert S.rem(f.subs(X, b), f, X) == 0
assert S.rem(b.subs(X, b)+X, f, X) == 0
sq = (2*W**2-P*I)/13
assert sq**2 == P*I
fp = X**4+3*P*X**2+225*P
bp = -(X**3+657*X)/195
assert S.rem(fp.subs(X, bp), fp, X) == 0
assert S.rem(bp.subs(X, bp)+X, fp, X) == 0

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

red = [n*pow(13, -1, P) % P for n in nums[:4]]
derivative_log = []
for n in range(3):
    derivative_log.append(((n+1)*red[n+1]
                           -sum(red[j]*derivative_log[n-j] for j in range(1, n+1)))
                          *pow(red[0], -1, P) % P)
log = [0]+[a*pow(n+1, -1, P) % P for n, a in enumerate(derivative_log)]
b_local = [0, -219*pow(65, -1, P) % P, 0, pow(65, -1, P)]
assert red == [82, 155, 53, 230]
assert log == [0, 202, 0, 108]
assert b_local == [0, 187, 0, 149]
projectors = {}
for lam in (82, 187):
    out = [0]*4
    orbit = log[:]
    for n in range(4):
        out = [(out[j]+pow(lam, -n, P)*orbit[j]) % P for j in range(4)]
        orbit = compose(orbit, b_local)
    assert orbit == log
    assert compose(out, b_local) == [lam*x % P for x in out]
    assert any(out)
    projectors[str(lam)] = out
assert projectors == {'82': [0, 0, 0, 241], '187': [0, 1, 0, 191]}

result = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS_EXACT_FINITE_ONLY',
    'p': P,
    'companion_character': 'chi12 * omega269^67; omega269^67(2)=-i',
    'conductor': F,
    'cyclotomic_degree': len(residues),
    'weighted_character_sum': weighted,
    'B1': list(map(str, B1)),
    'B1_norm': 200,
    'xi_5': list(xi(5)),
    'crt_generator_fixing_K_and_i': 1885,
    'generator_character_value': [0, -1],
    'integral_floor_annihilator_inverse_evaluation': floor_inverse,
    'annihilator_scalars_xi_and_inverse_mod_p': scalars,
    'real_quartic_polynomial': [1, 0, -P, 0, 25*P],
    'imaginary_companion_polynomial': [1, 0, 3*P, 0, 225*P],
    'unit_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'source_unit_index': 2,
    'unit_numerators': nums[:4],
    'unit_denominator': 13,
    'monic_quartic_annihilator': poly,
    'source_degree12_relation_is_cube': True,
    'local_reduction': red,
    'local_normalized_log': log,
    'local_b_action': b_local,
    'local_quartic_projectors': projectors,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope': 'Exact finite character sums, integral annihilator evaluations, field identities, one global unit and two local projectors. Class and strict conclusions require the separately written proof.'
}
(BASE/'pure_conductor4_quartic_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))

#!/usr/bin/env python3
"""Exact independent arithmetic for SF-QC01--05.

This does not enumerate the astronomical torsion group, certify a sheaf
construction in a proof assistant, or treat small numerical d as a geometric
example. The sample substitutions below are arithmetic checks only.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb
import json
import sympy as S


def add(*xs):
    out = defaultdict(lambda: S.Integer(0))
    for x in xs:
        for monomial, coefficient in x.items():
            out[monomial] += coefficient
    return {m: S.expand(c) for m, c in out.items() if S.expand(c) != 0}


def scale(c, x):
    return {m: S.expand(c * a) for m, a in x.items() if S.expand(c * a) != 0}


def wedge(x, y):
    out = defaultdict(lambda: S.Integer(0))
    for m, c in x.items():
        for n, e in y.items():
            if m & n:
                continue
            parity = sum((n & ((1 << i) - 1)).bit_count()
                         for i in range(6) if m >> i & 1)
            out[m | n] += (-1) ** parity * c * e
    return {m: S.expand(c) for m, c in out.items() if S.expand(c) != 0}


def expw(x):
    out = {0: S.Integer(1)}
    term = out
    for k in range(1, 4):
        term = scale(S.Rational(1, k), wedge(term, x))
        out = add(out, term)
    return out


s, t = S.symbols('s t')
a, b, c, e, U, Vv = [{1 << i: S.Integer(1)} for i in range(6)]
ab, ce, UV = wedge(a, b), wedge(c, e), wedge(U, Vv)
gamma = add(wedge(a, Vv), scale(-1, wedge(b, U)))
form = add(scale(s, wedge(add(a, c), add(b, e))), scale(t, ce),
           scale(-1, wedge(c, Vv)), wedge(e, U))
raw = expw(form)
integrated = {m ^ 12: co for m, co in raw.items() if m & 12 == 12}
claimed = add({0: s + t}, scale(s*t, ab), scale(s, gamma),
              scale(-1, UV), scale(-s, wedge(ab, UV)))
assert add(integrated, scale(-1, claimed)) == {}

# Opposite roots, s^2=-d: the identity first holds with d=-s^2.
opp = {m: S.expand(co.subs(t, -s)) for m, co in integrated.items()}
Q = wedge(add(scale(s, a), scale(-1, U)),
          add(scale(s, b), scale(-1, Vv)))
assert add(opp, wedge(expw(scale(S.Rational(1, 2), gamma)), Q)) == {}

# Equal roots in the same formal field.
same = {m: S.expand(co.subs(t, s)) for m, co in integrated.items()}
H = add(scale(-s*s, ab), UV)
same_rhs = scale(2*s, expw(add(scale(S.Rational(1, 2), gamma),
                              scale(-1/(2*s), H))))
assert all(S.cancel(co) == 0 for co in add(same, scale(-1, same_rhs)).values())

# The middle-degree determinant pairing has the Hodge--Riemann negative sign.
Qminus = {m: S.expand(co.subs(s, -s)) for m, co in Q.items()}
pairing = wedge(Q, Qminus)
assert pairing == {51: 4*s*s}

d, z, u = S.symbols('d z u', nonzero=True)
aa, bb = (1+1/u)/2, (1-1/u)/2
P_from_roots = S.expand(-8*u**3 * sum(
    (aa**2*(-u/(2*d))**k - bb**2*(u/(2*d))**k)*z**k/S.factorial(k)
    for k in range(7)))
P_from_roots = S.Poly(P_from_roots, u).rem(S.Poly(u*u+d, u)).as_expr()
P_expected = (8*d+2*(d-1)*z-z*z-(d-1)*z**3/(12*d)
              +z**4/(48*d)+(d-1)*z**5/(960*d*d)-z**6/(5760*d*d))
assert S.simplify(P_from_roots-P_expected) == 0

ad = (d-1)/(4*d)
kap = S.series(S.exp(-ad*z)*P_expected, z, 0, 7).removeO().expand()
ck = [S.factor(kap.coeff(z, k)) for k in range(7)]
assert ck[:2] == [8*d, S.Integer(0)]
assert S.simplify(ck[2]+(d+1)**2/(4*d)) == 0
assert S.simplify(ck[3]-(d-1)*(d+1)**2/(24*d*d)) == 0

r = 8*d
R = 224*r*r+r*(d+2)+6
assert S.expand(R) == 14344*d*d+16*d+6
volume = 720*729*d**3
A2 = S.factor(-r**4*ck[2]/9)
A3 = S.factor(2*r**6*ck[3]/27)
assert A2 == 1024*d**3*(d+1)**2/9
assert A3 == 65536*d**4*(d-1)*(d+1)**2/81
comparison = S.Matrix([[d*(d+8), 4*d], [4*d, d+8]])
assert S.factor(comparison.det()) == d*(d*d+64)
J = S.Matrix([[0, -1], [d, 0]])
polar = S.diag(d, 1)
assert J*J == -d*S.eye(2)
assert polar*J+(polar*J).T == S.zeros(2)
assert S.simplify(2*((d+1)/(4*d))**2*(-4*d)**3+8*d*(d+1)**2) == 0

# Independent check of the additional D-SR06 Gaussian integral B-field matrix.
rho = S.symbols('rho', positive=True, real=True)
ss = -1+S.I*rho
RRcm = S.Matrix([[1, 1], [S.conjugate(ss), ss]])
Cswap = S.Matrix([[0, 1], [1, 0]])
assert S.simplify(RRcm.conjugate().T*Cswap*RRcm
                 -2*S.Matrix([[-1, ss], [S.conjugate(ss), -1]])) == S.zeros(2)

# All six Buchsbaum--Rim line classes are strictly positive.
br_minors = []
for k in range(1, 7):
    matrix = (12*(112-7*(8+k))*S.eye(2)
              +(k+7)*S.Matrix([[2, 2], [2, -2]]))
    assert matrix[0, 0] > 0 and matrix.det() > 0
    br_minors.append([k, int(matrix[0, 0]), int(matrix.det())])

# Chern identity for the evaluation kernel, without importing the formula.
rr, kk, RR, A_2, A_3, tau = S.symbols('r k R A2 A3 tau')
chB = rr-A_2*z*z+(A_3/2+tau)*z**3
chF = S.series(S.exp(RR*z)*chB, z, 0, 4).removeO()
chG = S.series(S.exp(7*z)*(kk+rr-chF), z, 0, 4).removeO().expand()
c1 = chG.coeff(z, 1)
c2 = S.expand((c1*c1-2*chG.coeff(z, 2))/2)
c3 = S.expand((6*chG.coeff(z, 3)-c1**3+3*c1*c2)/3)
def C3(q): return q*(q-1)*(q-2)/6
def C2(q): return q*(q-1)/2
Sk = (-A_3+(rr+2)*RR*A_2-C3(rr+2)*RR**3
      +7*(kk-2)*(C2(rr+1)*RR**2-A_2)
      -49*rr*RR*C2(kk-1)+343*C3(kk))
assert S.expand(c3-(-2*tau+Sk)) == 0
drop = (rr+2)*RR*A_2+7*(kk-2)*C2(rr+1)*RR**2+343*C3(kk)
gap = A_3+C3(rr+2)*RR**3+7*(kk-2)*A_2+49*rr*RR*C2(kk-1)
assert S.expand(drop-Sk-gap) == 0

matrix_count = 5**3*81**3
assert matrix_count == 66430125
assert Fraction(216, 499)+Fraction(1, 4) < 1
assert 5832 < 2**13 and 14430 < 2**14
assert 524880 < 2**20 and Fraction(4096, 9) < 2**9
assert Fraction(343, 6) < 2**6
assert 2**47+2**154+2**317 < 2**318

samples = []
for m in [1, 2, 3, 7, 11, 19, 43, 67, 163]:
    # L=6 is an arithmetic-only toy value; it is NOT the torsion-orbit L.
    dd = 144*m
    rv = 8*dd
    Rv = 14344*dd*dd+16*dd+6
    vv = 524880*dd**3
    a2 = Fraction(1024*dd**3*(dd+1)**2, 9)
    a3 = Fraction(65536*dd**4*(dd-1)*(dd+1)**2, 81)
    assert a2.denominator == a3.denominator == 1
    section_count = S.simplify(vv*sum(
        rv**(2*j)*ck[j].subs(d, dd)*Rv**(6-j)/(3**j*S.factorial(6-j))
        for j in range(7)))
    assert section_count.is_Integer
    kval = int(section_count)-rv
    Mv = 729*dd**3*rv*(Rv+rv*rv)**6
    assert 3 <= kval <= Mv
    exactS = (-int(a3)+(rv+2)*Rv*int(a2)-comb(rv+2, 3)*Rv**3
              +7*(kval-2)*(comb(rv+1, 2)*Rv**2-int(a2))
              -49*rv*Rv*comb(kval-1, 2)+343*comb(kval, 3))
    exactD = vv*exactS
    bound = vv*((rv+2)*Rv*int(a2)+7*Mv*comb(rv+1, 2)*Rv**2
                +343*comb(Mv, 3))
    monomial_bound = 2**318*dd**51
    assert 0 < exactD <= bound < monomial_bound
    samples.append({'m': m, 'arithmetic_only_d': dd,
                    'evaluation_rank_integer': True,
                    'chern_degree_positive': True,
                    'exact_degree_le_formula_le_monomial': True,
                    'formula_degree_decimal_digits': len(str(bound))})

print(json.dumps({
    'metadata': {'author': 'GPT-6 Astra Pro', 'effort': 'inherited, not exposed',
                 'run': 'HODGE_DIVISION /root/sixfolds', 'date': '2026-11-21'},
    'single_plane_exterior_identity': 'PASS',
    'opposite_root_factorization': 'PASS',
    'equal_root_factorization': 'PASS',
    'full_polynomial': str(P_expected),
    'normalized_coefficients': [str(c) for c in ck],
    'polarization_and_weil_matrices': 'PASS',
    'positive_rank_weil_self_pairing': '-8*d*(d+1)^2; PASS',
    'D_SR06_gaussian_integral_B_matrix': 'PASS',
    'six_BR_positive_principal_minors': br_minors,
    'chern_evaluation_kernel_identity': 'PASS',
    'positive_upper_bound_decomposition': 'PASS',
    'strengthened_orbit_matrix_count': matrix_count,
    'coarse_detector_bound': '2^318 d^51 = 2^420 m^51 L^102',
    'sample_checks_scope': 'Arithmetic substitutions only, not geometric torsion-orbit examples',
    'samples': samples,
    'limitations': 'No astronomical torsion enumeration; no proof-assistant or sheaf-theoretic formal verification'
}, indent=2))

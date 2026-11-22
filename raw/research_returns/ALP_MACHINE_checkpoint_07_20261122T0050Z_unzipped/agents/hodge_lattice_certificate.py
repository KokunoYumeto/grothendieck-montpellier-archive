"""Exact finite algebra and numerical cross-checks for ALP-LIFT-05/06.

The geometric smoothness, integral-basis, convergence, and Cauchy arguments
are proved in the accompanying manuscripts. This script does not certify
them. Polynomial checks use exact rational cyclotomic arithmetic; numerical
gamma values are explicitly only independent high-precision cross-checks.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s
import mpmath as mp


def algebra():
    z = s.symbols('z')
    phi = sum(z**a for a in range(7))
    red = lambda x: s.rem(s.expand(x), phi, z)
    inv = lambda x: s.invert(red(x), phi, z)
    conj = lambda x: red(red(x).subs(z, z**6))
    matred = lambda A: A.applyfunc(red)
    star = lambda A: A.applyfunc(conj).T
    tr = lambda x: red(sum(red(x).subs(z, z**i) for i in [1, 2, 4]))
    S = z + z**2 + z**4
    T = -1-S
    delta = red(z-z**6)
    u = red(-inv(delta*delta))
    H = s.Matrix(3, 3, lambda a, b: tr(red(u*z**((b-a) % 7))))
    expected = s.Matrix([[2, -1, 1+S], [-1, 2, -1], [-S, -1, 2]])
    assert matred(H-expected) == s.zeros(3)
    assert matred(star(H)-H) == s.zeros(3)
    assert red(H.det()) == 1
    M = s.Matrix([[0, 0, 1], [1, 0, -T], [0, 1, S]])
    assert matred(star(M)*H*M-H) == s.zeros(3)
    V = s.Matrix([[z**(i*a) for a in range(3)] for i in [1, 2, 4]])
    assert matred(V*M-s.diag(z, z**2, z**4)*V) == s.zeros(3)
    deltas = [red(z**i-z**(7-i)) for i in [1, 2, 4]]
    W = matred(s.diag(*[inv(d) for d in deltas])*V)
    vd = red(V.det())
    dp = red(s.prod(deltas))
    assert vd == red(-(2*S+1))
    assert dp == red(2*S+1)
    assert red(W.det()) == -1
    Hinv = matred(H.adjugate())
    assert matred(W*Hinv*star(W)) == s.eye(3)
    assert red(vd*conj(vd)) == 7
    assert [H[:k, :k].det() for k in [1, 2]] == [2, 3]

    X, Y, alpha, iota = s.symbols('X Y alpha iota')
    # Direct substitutions, using alpha^7=-4 and iota^2=-1.
    c2 = -(2*Y+1)**2 - ((-4)*X**7-1)
    assert s.expand(c2) == -4*(Y**2+Y-X**7)
    rho = s.symbols('rho')
    p4 = rho**4-7
    a, b = -s.Rational(5, 16), -rho**2/s.Integer(32)
    disc = s.rem(s.expand(-16*(4*a**3+27*b**2)), p4, rho)
    assert disc == -1
    q2 = sum(F(2*i, 7) for i in [1, 2, 3])
    q7 = 6*F(1, 6)-3*F(7, 12)
    assert q2 == F(12, 7) and q7 == -F(3, 4)
    return {
        'cyclotomic_field': 'Q[z]/(1+z+z^2+z^3+z^4+z^5+z^6)',
        'trace_form_H': [[str(x) for x in row] for row in H.tolist()],
        'principal_minors': [2, 3, 1],
        'det_V': str(vd),
        'product_eigen_denominators': str(dp),
        'det_W': '-1',
        'exact_WHinvWstar': 'I_3',
        'exact_CM_action_isometry': True,
        'exact_CM_eigenvectors': True,
        'B_good7_discriminant': str(disc),
        'J_Hodge_valuation_at_2': str(q2),
        'J_Hodge_valuation_at_7': str(q7),
        'checks': 'passed',
    }


def metrics_and_directional_constants():
    mp.mp.dps = 90
    ell = {a: mp.loggamma(mp.mpf(a)/7) for a in range(1, 7)}
    Q = ell[1]+ell[2]-ell[3]+ell[4]-ell[5]-ell[6]
    GB = mp.pi/7*mp.exp(Q)
    G = [2*mp.pi/7*mp.gamma(mp.mpf(i)/7)
         *mp.gamma(mp.mpf(1)/2-mp.mpf(i)/7)
         /mp.gamma(1-mp.mpf(i)/7)/mp.gamma(mp.mpf(1)/2+mp.mpf(i)/7)
         for i in [1, 2, 3]]
    delta = ell[2]+3*ell[4]-3*ell[3]-ell[5]
    hJ = mp.mpf(12)/7*mp.log(2)-mp.mpf(3)/4*mp.log(7)-mp.log(mp.fprod(G))/2
    hB = -mp.log(7)/4-mp.log(GB)/2
    assert abs(hJ-3*hB-delta) < mp.mpf('1e-85')
    residue_order = [1, 3, 2, 6, 4, 5]
    Z = {}
    for k in [1, 3, 5]:
        char = {a: mp.exp(2*mp.pi*1j*k*j/6) for j, a in enumerate(residue_order)}
        L0 = -sum(a*char[a] for a in range(1, 7))/7
        Z[k] = -mp.log(7)+sum(char[a]*ell[a] for a in range(1, 7))/L0
    rows = []
    for i in [1, 2, 3]:
        b = {a: int((i*a) % 7 not in [1, 2, 3])-int(a not in [1, 2, 4])
             for a in residue_order}
        coeff = {k: sum(b[a]*mp.exp(-2*mp.pi*1j*k*j/6)
                        for j, a in enumerate(residue_order))/6
                 for k in [1, 3, 5]}
        C = mp.re(sum(coeff[k]*Z[6-k] for k in [1, 3, 5]))
        gamma_C = (Q-2*ell[i]+2*ell[7-i]-ell[7-2*i]+ell[2*i])/2
        good_C = C-mp.mpf(2*i)/7*mp.log(2)
        arch = -mp.log(G[i-1]/GB)/2
        assert abs(C-gamma_C) < mp.mpf('1e-85')
        assert abs(good_C-arch) < mp.mpf('1e-85')
        rows.append({'direction': i,
                     'prime_class_coefficient': {str(a): b[a] for a in range(1, 7)},
                     'all_unramified_prime_constant': mp.nstr(C, 70),
                     'good_prime_constant': mp.nstr(good_C, 70),
                     'archimedean_difference': mp.nstr(arch, 70)})
    return {'precision_decimal_digits': 90,
            'G_J_diagonal': [mp.nstr(v, 70) for v in G],
            'G_B': mp.nstr(GB, 70),
            'stable_h_J_L2': mp.nstr(hJ, 70),
            'stable_h_B_L2': mp.nstr(hB, 70),
            'delta7': mp.nstr(delta, 70),
            'directional_constants': rows,
            'numerical_checks': 'passed; not a proof certificate'}


if __name__ == '__main__':
    result = {'exact_finite_algebra': algebra(),
              'numerical_crosschecks': metrics_and_directional_constants()}
    dst = Path(__file__).with_suffix('.json')
    dst.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'file': str(dst), 'exact_algebra': 'passed',
                      'numerical_crosschecks': 'passed'}, indent=2))

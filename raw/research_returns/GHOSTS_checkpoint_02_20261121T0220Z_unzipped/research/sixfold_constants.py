"""Exact arithmetic/exterior-algebra checks for R21--R23; no float arithmetic.

This is a supplementary certificate for explicit identities, not a substitute
for the geometric source hypotheses or an exhaustive cycle minimization.
"""
from fractions import Fraction as Q
from math import factorial, gcd, lcm


def add(*xs):
    out = {}
    for x in xs:
        for key, value in x.items():
            out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value}


def scale(c, x):
    return {key: c * value for key, value in x.items() if c * value}


def wedge(x, y):
    out = {}
    for a, c in x.items():
        for b, d in y.items():
            if set(a) & set(b):
                continue
            sign = (-1) ** sum(i > j for i in a for j in b)
            key = tuple(sorted(a + b))
            out[key] = out.get(key, 0) + sign * c * d
    return {key: value for key, value in out.items() if value}


def form(i):
    return {(i,): Q(1)}


def apply(x, images):
    out = {}
    for key, c in x.items():
        value = {(): c}
        for i in key:
            value = wedge(value, images[i])
        out = add(out, value)
    return out


def graph_scalar(matrix):
    out = {(): Q(1)}
    for k in range(2):
        u, v = form(2*k), form(2*k+1)
        pu = add(scale(matrix[0][0], u), scale(matrix[0][1], v))
        pv = add(scale(matrix[1][0], u), scale(matrix[1][1], v))
        out = wedge(out, add(form(4+2*k), scale(-1, pu)))
        out = wedge(out, add(form(5+2*k), scale(-1, pv)))
    return out


def eisenstein_mul(a, b):
    # (a0+a1*w)(b0+b1*w), w^2=-1-w.
    return (a[0]*b[0]-a[1]*b[1],
            a[0]*b[1]+a[1]*b[0]-a[1]*b[1])


alpha = (2, -1)
alpha3 = eisenstein_mul(eisenstein_mul(alpha, alpha), alpha)
alpha6 = eisenstein_mul(alpha3, alpha3)
assert alpha3 == (1, -18)
assert alpha6 == (-323, -360)
real_alpha6 = Q(alpha6[0]) - Q(alpha6[1], 2)
norm_alpha6 = alpha6[0]**2 - alpha6[0]*alpha6[1] + alpha6[1]**2
gram_det_factor = norm_alpha6 - real_alpha6**2
assert real_alpha6 == -143
assert norm_alpha6 == 117649
assert gram_det_factor == 97200

I = [[1, 0], [0, 1]]
minusI = [[-1, 0], [0, -1]]
omega = [[0, -1], [1, -1]]
minusomega = [[0, 1], [-1, 1]]
tstar = add(graph_scalar(I), graph_scalar(minusI),
            scale(-1, graph_scalar(omega)),
            scale(-1, graph_scalar(minusomega)))
theta = [wedge(form(2*k), form(2*k+1)) for k in range(6)]
D = add(wedge(add(form(10), scale(-1, form(8))),
              add(form(11), scale(-1, form(9)))),
        scale(-1, theta[4]), scale(-1, theta[5]))
R, S = [], []
for k in range(6):
    u, v = form(2*k), form(2*k+1)
    if k in (0, 1, 4):
        R.extend([scale(-1, v), add(u, scale(-1, v))])
        S.extend([add(u, scale(-2, v)), add(scale(2, u), scale(-1, v))])
    else:
        R.extend([add(scale(-1, u), v), scale(-1, u)])
        S.extend([add(scale(-1, u), scale(2, v)), add(scale(-2, u), v)])
tD = wedge(tstar, D)
orbit_sum = add(tD, apply(tD, R), apply(apply(tD, R), R))
Gamma = scale(Q(-1, 3), orbit_sum)
projected = scale(Q(1, 162),
                  add(scale(27, orbit_sum), scale(-1, apply(orbit_sum, S))))
assert projected == scale(-1, Gamma)
assert not wedge(Gamma, add(*theta))
assert wedge(D, D) == {(8, 9, 10, 11): Q(-2)}
assert wedge(tstar, tstar) == {tuple(range(8)): Q(24)}
assert wedge(Gamma, Gamma) == {tuple(range(12)): Q(-24)}
contracted = {}
for key, value in wedge(Gamma, D).items():
    if all(i in key for i in range(8, 12)):
        contracted[tuple(i for i in key if i < 8)] = value
assert contracted == tstar
denominator = lcm(*(value.denominator for value in Gamma.values()))
assert denominator == 3
gamma_num_gcd = gcd(*(abs(int(denominator*value)) for value in Gamma.values()))

degree_W6 = 3**6 * factorial(10) // factorial(4)
degree_B = 3**6 * factorial(6) * 27
assert degree_W6 * degree_B % 27 == 0
D6 = degree_W6 * degree_B // 27
A = 97200 * 729**2
B = 27005076 * 19683
assert A == 51656065200
assert B == 531540910908
common = gcd(A, B)
assert (common, A//common, B//common) == (516560652, 100, 1029)

print('alpha^3 =', alpha3, '(basis 1, omega)')
print('alpha^6 =', alpha6, '(basis 1, omega)')
print('Gram entries: 1,', real_alpha6, ',', norm_alpha6)
print('Gram determinant factor =', gram_det_factor)
print('D^2 = -2; t_star^2 = 24; Gamma^2 = -24')
print('t_star integral coefficient gcd =', gcd(*(abs(int(v)) for v in tstar.values())))
print('Gamma denominator =', denominator)
print('3*Gamma coefficient gcd =', gamma_num_gcd)
print('Contraction by D equals t_star:', contracted == tstar)
print('Gamma primitive under the product polarization:', not wedge(Gamma, add(*theta)))
print('Gamma equals minus the sixfold Weil projector of t_star tensor D:', projected == scale(-1, Gamma))
print('degree_3Theta(W6) =', degree_W6)
print('degree_3Theta(B) =', degree_B)
print('D6 =', D6)
print('C6 = delta*D6^4*(%s + %s*ceil(sqrt(U)))' % (A, B))
print('C6 = %s*delta*D6^4*(%s + %s*ceil(sqrt(U)))' % (common, A//common, B//common))
print('D6^4 =', D6**4)
print('t_star product Gamma: valid delta=3, U=24; C6 =', 3*D6**4*(A+5*B))

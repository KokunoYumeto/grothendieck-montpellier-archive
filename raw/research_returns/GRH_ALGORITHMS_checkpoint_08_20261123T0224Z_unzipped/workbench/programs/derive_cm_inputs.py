"""Derive the CM example's integer polynomials independently.

Python standard library only. No table of modular-polynomial coefficients
or singular moduli is imported. E4 and Delta q-series give j. Exact
Laurent-series elimination gives Phi_3. Rational interval arithmetic at
the two reduced forms of discriminant -15 isolates H_-15's coefficients.

The Phi_3 certificate checks through q^12 after cancelling poles of
order at most 12. The modular function on X_0(3) has only two cusps,
and its possible pole at the other cusp also has order at most 12;
a zero of order at least 13 therefore proves the identity. For H_-15,
CM integrality and the two reduced forms identify the two conjugates.
All numerical error bounds, including the q-series tail, are explicit.
"""

from fractions import Fraction as F
from math import isqrt
import json


def conv(a, b, degree):
    out = [0] * (degree + 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[:degree + 1 - i]):
            out[i+j] += x*y
    return out


def j_coefficients(n=55):
    """Return coefficients of q*j(q) through q^n, exactly."""
    e4 = [1] + [0]*n
    for d in range(1, n+1):
        for k in range(d, n+1, d):
            e4[k] += 240*d**3
    numerator = conv(conv(e4, e4, n), e4, n)
    delta = [1] + [0]*n
    from math import comb
    for d in range(1, n+1):
        factor = [0]*(n+1)
        for k in range(min(24, n//d)+1):
            factor[k*d] = (-1)**k*comb(24, k)
        delta = conv(delta, factor, n)
    answer = [0]*(n+1)
    for k in range(n+1):
        answer[k] = numerator[k] - sum(delta[i]*answer[k-i]
                                      for i in range(1, k+1))
    return answer


def lmul(a, b, ceiling=42):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            if i+j <= ceiling:
                out[i+j] = out.get(i+j, 0) + x*y
    return {i: x for i, x in out.items() if x}


def derive_phi3(jc):
    x = {i-1: c for i, c in enumerate(jc)}
    y = {3*(i-1): c for i, c in enumerate(jc)}
    xp, yp = [{0: 1}], [{0: 1}]
    for _ in range(4):
        xp.append(lmul(xp[-1], x))
        yp.append(lmul(yp[-1], y))
    pairs = [(i, j) for i in range(4) for j in range(i+1)]
    series = []
    for i, j in pairs:
        a = lmul(xp[i], yp[j])
        if i != j:
            for k, v in lmul(xp[j], yp[i]).items():
                a[k] = a.get(k, 0)+v
        series.append(a)
    rhs = {k: -(xp[4].get(k, 0)+yp[4].get(k, 0))
           for k in range(-12, 21)}
    matrix = [[F(a.get(k, 0)) for a in series]+[F(rhs[k])]
              for k in range(-12, 13)]
    row = 0
    pivots = []
    for col in range(len(pairs)):
        pivot = next((i for i in range(row, len(matrix))
                      if matrix[i][col]), None)
        assert pivot is not None, 'Underdetermined q-series relation'
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        lead = matrix[row][col]
        matrix[row] = [v/lead for v in matrix[row]]
        for i in range(len(matrix)):
            if i != row and matrix[i][col]:
                lead = matrix[i][col]
                matrix[i] = [v-lead*w for v, w in zip(matrix[i], matrix[row])]
        pivots.append((row, col))
        row += 1
    assert all(any(a[:-1]) or a[-1] == 0 for a in matrix)
    coefficients = [0]*len(pairs)
    for row, col in pivots:
        assert matrix[row][-1].denominator == 1
        coefficients[col] = int(matrix[row][-1])
    # Additional coefficients beyond those needed for the pole-bound proof.
    for k in range(-12, 21):
        assert sum(c*a.get(k, 0) for c, a in zip(coefficients, series)) == rhs[k]
    return [(4, 0, 1)] + [(i, j, c) for (i, j), c in
                           zip(pairs, coefficients) if c]


GRID = 10**80


def down(x):
    return F((x.numerator*GRID)//x.denominator, GRID)


def up(x):
    return F(-((-x.numerator*GRID)//x.denominator), GRID)


class I:
    """Closed rational interval with outward rounding to a fixed grid."""
    def __init__(self, lo, hi=None):
        self.lo = down(F(lo))
        self.hi = up(F(lo if hi is None else hi))
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        values = [a*b for a in (self.lo, self.hi)
                  for b in (other.lo, other.hi)]
        return I(min(values), max(values))

    __rmul__ = __mul__

    def inv(self):
        assert not self.lo <= 0 <= self.hi
        return I(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        return self*other.inv()

    def integer(self):
        lo = -((-self.lo.numerator)//self.lo.denominator)
        hi = self.hi.numerator//self.hi.denominator
        assert lo == hi, 'Coefficient interval does not isolate an integer'
        return lo

    def bounds(self):
        return [[self.lo.numerator, self.lo.denominator],
                [self.hi.numerator, self.hi.denominator]]


def atan_inverse(m, terms):
    s = sum((F((-1)**k, (2*k+1)*m**(2*k+1))
             for k in range(terms)), F(0))
    nxt = F((-1)**terms, (2*terms+1)*m**(2*terms+1))
    return I(min(s, s+nxt), max(s, s+nxt))


def exp_interval(x, terms=100):
    assert 0 <= x.lo <= x.hi < 7
    term = I(1)
    total = I(1)
    for k in range(1, terms+1):
        term = term*x/k
        total = total+term
    tail = term.hi*F(7, terms+1)/(1-F(7, terms+2))
    return I(total.lo, total.hi+tail)


def cadd(z, w):
    return (z[0]+w[0], z[1]+w[1])


def cmul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def j_interval(q, inverse_q, jc, q_abs, n=50):
    value = cadd(inverse_q, (I(jc[1]), I(0)))
    power = (I(1), I(0))
    for k in range(1, n+1):
        power = cmul(power, q)
        value = cadd(value, (power[0]*jc[k+1], power[1]*jc[k+1]))
    rho = F(1, 100)
    s4 = rho*(1+11*rho+11*rho**2+rho**3)/(1-rho)**5
    u = 24*rho/(1-rho)**2
    assert u < 1 and q_abs < rho
    cauchy = (1+240*s4)**3/(1-u)
    ratio = q_abs/rho
    tail = cauchy/rho*ratio**(n+1)/(1-ratio)
    error = I(-tail, tail)
    return (value[0]+error, value[1]+error)


def derive_h15(jc):
    pi = 16*atan_inverse(5, 40)-4*atan_inverse(239, 12)
    root = isqrt(15*GRID**2)
    sqrt15 = I(F(root, GRID), F(root+1, GRID))
    t = exp_interval(pi*sqrt15/2).inv()
    t2 = t*t
    j1 = j_interval((-t2, I(0)), (-t2.inv(), I(0)), jc, t2.hi)
    j2 = j_interval((I(0), -t), (I(0), t.inv()), jc, t.hi)
    total = cadd(j1, j2)
    product = cmul(j1, j2)
    assert total[1].lo <= 0 <= total[1].hi
    assert product[1].lo <= 0 <= product[1].hi
    result = [product[0].integer(), (-total[0]).integer(), 1]
    cert = {'constant_interval': product[0].bounds(),
            'linear_interval': (-total[0]).bounds(),
            'reduced_forms': [[1, 1, 4], [2, 1, 2]],
            'q_series_tail_method': 'Cauchy bound at radius 1/100',
            'q_series_terms': 50, 'rounding_grid_denominator': GRID}
    return result, cert


def derive():
    jc = j_coefficients()
    phi = derive_phi3(jc)
    h15, intervals = derive_h15(jc)
    return {'Phi3_symmetric_sparse_terms': phi,
            'Phi3_checked_q_exponents': [-12, 20],
            'Phi3_required_by_cusp_pole_bound': [-12, 12],
            'H15_ascending': h15, 'H15_interval_certificate': intervals}


if __name__ == '__main__':
    print(json.dumps(derive(), indent=2))

"""Exact, deliberately finite checks accompanying computations.md.

These checks are not substitutes for the infinite/group-scheme arguments in the
proof file.  All output is reproducible with Python's standard library.
"""
from fractions import Fraction
from math import ceil, comb, prod
import json


def rank(mat, p=None):
    a = [[(x % p if p else Fraction(x)) for x in row] for row in mat]
    if not a:
        return 0
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p) if p else 1 / a[r][j]
        a[r] = [(v * inv) % p if p else v * inv for v in a[r]]
        for i in range(len(a)):
            if i != r:
                q = a[i][j]
                a[i] = [((u-q*v) % p if p else u-q*v)
                        for u, v in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def jordan_t(n):
    return [[int(i == j+1) for j in range(n)] for i in range(n)]


def commutant_dimension(n):
    # Linear equations XT=TX, coordinates x_(i,j).
    t = jordan_t(n)
    eq = []
    for i in range(n):
        for j in range(n):
            row = [0] * (n*n)
            for k in range(n):
                row[i*n+k] += t[k][j]
                row[k*n+j] -= t[i][k]
            eq.append(row)
    return n*n-rank(eq)


def emit(label, data):
    print(label)
    print(json.dumps(data, ensure_ascii=False, sort_keys=True))


# Section 2: finite coordinate unions; this says nothing about uniform infinite
# coordinate bounds.  The proof constructs one variable new at each level.
emit('Finite Witt-coordinate stage bounds (symbolic labels, not Witt arithmetic)',
     [{'length': n, 'variables': [f'x{i}' for i in range(1, n+1)],
       'minimum_containing_stage': n} for n in range(1, 7)])

# Section 10: finite DVR transition is t multiplication A/t^n→A/t^(n+1).
dvr = []
for n in range(1, 9):
    j = [[int(i == k+1) for k in range(n)] for i in range(n+1)]
    assert mm(jordan_t(n+1), j) == mm(j, jordan_t(n))
    assert rank(j) == n
    dim = commutant_dimension(n)
    assert dim == n
    dvr.append({'n': n, 'transition_rank': rank(j),
                'endomorphism_algebra_dimension': dim})
emit('DVR finite module checks over Q (identical equations over every field)', dvr)

# Section 12: F is the linear part of semilinear Frobenius. These are ranks of
# that linear part, not ranks of F-1 over an algebraically closed infinite field.
emit('One-dimensional F matrices over F3, finite-field illustration only',
     [{'case': label, 'rank_F': rank([[f]], 3),
       'dimension_kernel_F': 1-rank([[f]], 3),
       'dimension_cokernel_F': 1-rank([[f]], 3),
       'kernel_dimension_of_F_minus_1_on_F3_points': 1-rank([[f-1]], 3)}
      for label, f in [('ordinary linear part', 1), ('supersingular linear part', 0)]])

# Section 14: sparse multivariate polynomials modulo 3.
def derivative(poly, var):
    ans = {}
    for e, c in poly.items():
        if e[var]:
            f = list(e)
            f[var] -= 1
            value = (c*e[var]) % 3
            if value:
                ans[tuple(f)] = value
    return ans

equation = {(0,2,1): 1, (3,0,0): -1, (1,0,2): 1}
partials = [derivative(equation, v) for v in range(3)]
assert partials == [{(0,0,2): 1}, {(0,1,1): 2},
                    {(0,2,0): 1, (1,0,1): 2}]
f = {3: 1, 1: -1}  # f^(p-1)/2=f for p=3
assert f.get(2, 0) % 3 == 0
emit('E:y²=x³−x in characteristic 3', {
    'partial_X': 'Z^2', 'partial_Y': '2YZ', 'partial_Z': 'Y^2+2XZ',
    'smoothness_certificate': 'partial_X=0 => Z=0; partial_Z=0 => Y=0; equation=0 => X=0',
    'coefficient_x2_of_f': 0,
    'Cartier_exponents_surviving_mod3_equal_2': [i for i in f if i % 3 == 2],
    'rank_full_E3_group_scheme': 3**2,
    'dimension_etale_H1_Z3_from_F_zero': 0})

# Section 18: algebraic rearrangement and integer thresholds.
rows = []
for d in (1, 2, 4):
    for k in range(1, 21):
        threshold = ceil(Fraction(2*(k-1)*d+2, d))
        for n in range(k, 80):
            r = d*(n-k+1)-2
            assert (2*r >= d*n-2) == (n >= threshold)
        rows.append({'d': d, 'k': k, 'minimum_integer_n': threshold})
emit('Atiyah connectivity thresholds, all k=1,...,20 checked', rows)

# Section 19: the module R⊕k has one free summand and one t-killed summand.
emit('Literal inequality does not imply flatness, R⊕k over a DVR', {
    'generic_length': 1, 'special_length': 2,
    'inequality_special_ge_generic': 2 >= 1,
    'dimension_Tor1_Rk_module': 1,
    'flat': False})

# Section 20: concrete bounded cochain complex Q^2→Q^3→Q^2.
d0 = [[1, 0], [0, 0], [0, 0]]
d1 = [[0, 1, 0], [0, 0, 0]]
assert mm(d1, d0) == [[0, 0], [0, 0]]
dims = [2, 3, 2]
rd0, rd1 = rank(d0), rank(d1)
h = [2-rd0, 3-rd0-rd1, 2-rd1]
chi_terms = sum((-1)**i*x for i, x in enumerate(dims))
chi_h = sum((-1)**i*x for i, x in enumerate(h))
assert chi_terms == chi_h
emit('Euler characteristic exact matrix calculation', {
    'term_dimensions': dims, 'differential_ranks': [rd0, rd1],
    'cohomology_dimensions': h, 'chi_terms': chi_terms, 'chi_cohomology': chi_h})

def hilbert(d, n):
    return Fraction(prod(n+i for i in range(1, d+1)), prod(range(1, d+1)))

emit('χ(P^d,O(n)) = product(n+i)/d!, including negative n', [
    {'dimension': d, 'leading_coefficient': str(Fraction(1, prod(range(1,d+1)))),
     'values_n_minus4_to4': [str(hilbert(d,n)) for n in range(-4,5)]}
    for d in range(4)])
emit('Zero-sheaf strict-positivity obstruction', {'Hilbert_polynomial': 0})

# Section 21: finite noncommutative version of the telescoping identity, tested
# on integer 2×2 matrices; this also checks that commutativity is unnecessary.
ident = [[1,0],[0,1]]
aa = [[[1,2],[0,1]], [[0,1],[3,0]], ident]
prefix = ident
total = [[0,0],[0,0]]
for a in aa:
    e = mm(prefix, a)
    total = [[total[i][j]+e[i][j] for j in range(2)] for i in range(2)]
    one_minus_a = [[ident[i][j]-a[i][j] for j in range(2)] for i in range(2)]
    prefix = mm(prefix, one_minus_a)
assert total == ident and prefix == [[0,0],[0,0]]
emit('Ordered partition identity sum_i prod_(j<i)(1-a_j)a_i = 1', {
    'matrix_sum': total, 'remaining_product': prefix})

# Section 22 is an infinite valuation argument; this finite arithmetic record
# only exhibits the independent prime coordinates used in that proof.
emit('Valuation witnesses for independent rational units', {
    'primes': [2,3,5,7,11], 'valuation_matrix':
    [[int(i == j) for j in range(5)] for i in range(5)],
    'Z_1_over_6_unit_coordinates': ['sign', 'v_2', 'v_3']})

print('All finite assertions passed. Infinite conclusions are proved in computations.md, not inferred from these tests.')

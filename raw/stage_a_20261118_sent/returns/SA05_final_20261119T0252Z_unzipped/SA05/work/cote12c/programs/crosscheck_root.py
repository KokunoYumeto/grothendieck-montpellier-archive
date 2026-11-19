"""Independent exact checks of selected root certificates.

This does not rerun or import the root program. General theorems and
all-extension trace identities remain the written/source-checked arguments
in root_crossreview.md; these calculations only certify their finite steps.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]


def rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    if not a:
        return 0
    pivot = 0
    for col in range(len(a[0])):
        row = next((r for r in range(pivot, len(a)) if a[r][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        c = a[pivot][col]
        a[pivot] = [x/c for x in a[pivot]]
        for r in range(len(a)):
            if r != pivot and a[r][col]:
                c = a[r][col]
                a[r] = [x-c*y for x, y in zip(a[r], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def mul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def sub(a, b):
    return [[x-y for x, y in zip(u, v)] for u, v in zip(a, b)]


def transpose(a):
    return [list(c) for c in zip(*a)]


def inverse2(a):
    d = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return [[Fraction(a[1][1], d), Fraction(-a[0][1], d)],
            [Fraction(-a[1][0], d), Fraction(a[0][0], d)]]


def incidence(size):
    source = list(combinations(range(4), size))
    target = list(combinations(range(4), size+1))
    out = []
    for face in target:
        row = [0]*len(source)
        for k in range(size+1):
            row[source.index(face[:k]+face[k+1:])] = (-1)**k
        out.append(row)
    return out


def legendre_symbol(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p-1)//2, p) == 1 else -1


def elliptic_count(a, b, p):
    return 1+sum(1+legendre_symbol(x**3+a*x+b, p) for x in range(p))


result = {}

# Closed SNC cover, freshly constructed signed incidence matrices.
d0, d1 = incidence(1), incidence(2)
assert (rank(d0), rank(d1)) == (3, 3)
assert all(x == 0 for row in mul(d1, d0) for x in row)
rows = {0: ([4, 6, 4], [rank(d0), rank(d1)]),
        2: ([4, 6, 0], [rank(d0), 0]),
        4: ([4, 0, 0], [0, 0])}
cohom_D = {}
row_output = {}
for q, (dims, ranks) in rows.items():
    h = [dims[p]-(ranks[p-1] if p else 0)-(ranks[p] if p < 2 else 0)
         for p in range(3)]
    row_output[q] = dict(dimensions=dims, ranks=ranks, cohomology=h)
    for p, dim in enumerate(h):
        if dim:
            cohom_D.setdefault(p+q, {})[q//2] = dim
cohom_X = {}
for degree, pieces in cohom_D.items():
    for exponent, dimension in pieces.items():
        for shift_degree, shift_exponent in [(0, 0), (2, 1)]:
            dest = cohom_X.setdefault(degree+shift_degree, {})
            e = exponent+shift_exponent
            dest[e] = dest.get(e, 0)+dimension
inv4 = cohom_X[4].get(1, 0)
coinv3 = cohom_X[3].get(1, 0)
assert cohom_X[3] == {1: 3}
assert cohom_X[4] == {2: 5, 1: 1}
assert inv4+coinv3 == 4
result['SNC'] = dict(d0=d0, d1=d1, rows=row_output,
                     geometric_D_by_degree_and_Frobenius_q_power=cohom_D,
                     geometric_X_by_degree_and_Frobenius_q_power=cohom_X,
                     twist=1, arithmetic_H4_invariant_dimension=inv4,
                     arithmetic_H4_coinvariant_dimension=coinv3,
                     arithmetic_H4_dimension=inv4+coinv3)

# One independent point-count check; the source proves the formula for all n.
p = 5
traces = {}
for lam in range(2, p):
    points = 1+sum(1+legendre_symbol(x*(x-1)*(x-lam), p)
                   for x in range(p))
    traces[lam] = p+1-points
assert -sum(traces.values()) == 2
after_dual_coefficient = Fraction(1, p)  # V^vee = V(1)
after_dual_space = 1/after_dual_coefficient
ordinary_eigenvalue = after_dual_space*p  # final twist(-1)
twisted_eigenvalue = ordinary_eigenvalue/Fraction(p**2)
assert ordinary_eigenvalue == 25 and twisted_eigenvalue == 1
result['Legendre'] = dict(q=p, fibre_traces=traces,
                          compact_H1_trace=-sum(traces.values()),
                          ordinary_H1_eigenvalue=str(ordinary_eigenvalue),
                          coefficient_V_twist2_weight=1-2*2,
                          H1_V_twist2_eigenvalue=str(twisted_eigenvalue),
                          all_extensions_formula_source='Stacks tag 03VA, not inferred from this sample')

# Realize the Lie-algebra Frobenius polynomial by a smooth elliptic curve.
curves = [(a, b, elliptic_count(a, b, p))
          for a in range(p) for b in range(p)
          if (4*a**3+27*b**2) % p != 0
          and p+1-elliptic_count(a, b, p) == 1]
assert curves
a, b, count = curves[0]
F = [[0, -5], [1, 1]]  # on geometric H^1 in a suitable rational basis
I = [[1, 0], [0, 1]]
assert sub(mul(F, F), F) == [[-5, 0], [0, -5]]
# Geometric Frobenius on the homological Tate module is the dual action.
A = transpose(inverse2(F))
Ai = inverse2(A)
basis = [[[int(i == u and j == v) for j in range(2)] for i in range(2)]
         for u in range(2) for v in range(2)]
ad_columns = []
for B in basis:
    delta = sub(mul(mul(A, B), Ai), B)
    ad_columns.append([x for row in delta for x in row])
ad_minus_one = transpose(ad_columns)
ad_rank = rank(ad_minus_one)
qA = [[p*x for x in row] for row in A]
IminusqA = sub(I, qA)
assert rank(IminusqA) == 2
assert ad_rank == 2
result['Frobenius_and_constant_Jacobian'] = dict(
    field=5, elliptic_curve=dict(equation=f'y^2=x^3+{a}x+{b}',
                               discriminant_test_mod5=(4*a**3+27*b**2) % 5,
                               point_count=count, trace=6-count),
    polynomial='T^2-T+5', discriminant=-19,
    H1_geometric_Frobenius=F,
    Tate_module_geometric_Frobenius=[[str(x) for x in row] for row in A],
    End_AdF_minus1_rank=ad_rank,
    End_invariant_dimension=4-ad_rank,
    End_coinvariant_dimension=4-ad_rank,
    geometric_H2_with_Tate_coeff_no_invariants_rank=rank(IminusqA),
    arithmetic_H2_Tate_coeff_dimension=4-ad_rank,
    limitation='Analytic/algebraic dimensions and Tate Hom comparison use the written proof, not a matrix-only theorem.')

t = 2
assert t*(t*t-1)*(t*t+1) == 30
result['Howe'] = dict(t=t, excluded_parameter_product=t*(t*t-1)*(t*t+1),
                     characteristic=0, source_genus=2, target_genus=2,
                     RH_equation='2=2d+R, d integer >=1, R>=0',
                     forced_degree=1, forced_ramification=0,
                     existence_source='Howe Theorem 1; not an elementary computational conclusion')

result['residue_rows'] = {r: dict(rank=rank([[1]*r]), kernel_dimension=r-1)
                          for r in range(1, 7)}
assert all(x['rank'] == 1 for x in result['residue_rows'].values())
result['all_assertions_passed'] = True

out = BASE/'outputs'/'crosscheck_root.json'
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))

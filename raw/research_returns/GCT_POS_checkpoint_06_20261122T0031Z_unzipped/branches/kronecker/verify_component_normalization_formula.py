"""Independent finite checks for the K-032 coefficient identity.

The main proof concerns all amplified components and is in the companion
TeX file.  The rank-two examples below check Schur--Weyl/Pieri bookkeeping
against direct monomial weights; they are test representations, not claims
about actual amplified spectra.  The n=58 check uses the already retained
exact prefix certificate to identify all five vector weights and grading.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    if largest is None:
        largest = n
    for a in range(min(largest, n), 0, -1):
        for rest in partitions(n-a, a):
            yield (a,)+rest


def centralizer_order(cycle_type):
    answer = 1
    for a, m in Counter(cycle_type).items():
        answer *= a**m * factorial(m)
    return answer


def two_row_character(second_row, cycle_type):
    """Permutation on b-subsets minus permutation on (b-1)-subsets."""
    counts = [1] + [0]*second_row
    for a in cycle_type:
        for j in range(second_row, a-1, -1):
            counts[j] += counts[j-a]
    return counts[second_row] - (counts[second_row-1] if second_row else 0)


def core_weights(q):
    """Monomial weights in Sym^q(C^2 tensor C^2 tensor C^2)."""
    dp = [dict() for _ in range(q+1)]
    dp[0][(0, 0, 0)] = 1
    for edge in product(range(2), repeat=3):
        for degree in range(1, q+1):
            for weight, count in dp[degree-1].items():
                target = tuple(weight[a]+edge[a] for a in range(3))
                dp[degree][target] = dp[degree].get(target, 0) + count
    return dp[q]


def convolve(left, right):
    result = [0]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] += a*b
    return result


receipts = []
for s in (4, 8, 12):
    # r=2, rho=1/2, alpha1=alpha2=gamma1=gamma2=1/4, beta=1/2.
    q = 3*s//2
    cycles = list(partitions(q))
    bounds = range(s//4+1)
    table = []
    kronecker_sum = Fraction(0)
    for j in bounds:
        row = []
        for v in bounds:
            multiplicity = sum(
                (Fraction(two_row_character(s//2+j, mu)
                          * two_row_character(s//2, mu)
                          * two_row_character(s//2+v, mu),
                          centralizer_order(mu)) for mu in cycles),
                Fraction(0))
            assert multiplicity.denominator == 1 and multiplicity >= 0
            row.append(int(multiplicity))
            kronecker_sum += multiplicity
        table.append(row)

    weights = core_weights(q)
    vector_ac = convolve([1]*(s//4+1), [1]*(s//4+1))
    vector_b = [1]*(s//2+1)
    vector_weights = (vector_ac, vector_b, vector_ac)
    weyl_terms = []
    direct = 0
    for epsilon in product(range(2), repeat=3):
        target = tuple(s+epsilon[a] for a in range(3))
        weight_count = 0
        for weight, count in weights.items():
            leftover = tuple(target[a]-weight[a] for a in range(3))
            if all(0 <= leftover[a] < len(vector_weights[a]) for a in range(3)):
                weight_count += count * vector_ac[leftover[0]] \
                    * vector_b[leftover[1]] * vector_ac[leftover[2]]
        sign = (-1)**sum(epsilon)
        direct += sign*weight_count
        weyl_terms.append({'epsilon': epsilon, 'weight_multiplicity': weight_count,
                           'sign': sign})
    assert direct == kronecker_sum
    receipts.append({'r': 2, 's': s, 'rho': '1/2', 'core_degree': q,
                     'character_cycle_types': len(cycles),
                     'kronecker_table': table, 'kronecker_sum': int(kronecker_sum),
                     'direct_monomial_Weyl_multiplicity': direct,
                     'weyl_terms': weyl_terms})

actual = json.loads((ROOT / 'amplified_collision_component_checks.json').read_text())
support = [tuple(e) for e in actual['prefix_support']]
masses = [Fraction(x) for x in actual['prefix_masses']]
selected = tuple(actual['prefix_selected_edge'])
rho = masses[support.index(selected)]
M = actual['M']
n, m, r = 58, 51, 8
assert rho.denominator == M
assert all(M % p.denominator == 0 for p in masses)
incident = []
for a in range(3):
    pairs = [(edge, p) for edge, p in zip(support, masses)
             if edge != selected and edge[a] == selected[a]]
    assert len(pairs) == (2, 1, 2)[a]
    assert sum((p for _, p in pairs), Fraction(0)) == 1-rho
    incident.append(pairs)
assert all(sum(edge[a] == selected[a] for a in range(3)) <= 1
           for edge in support if edge != selected)
group_degrees = [M*(p+(r-1 if edge == selected else 0))
                 for edge, p in zip(support, masses)]
assert all(d.denominator == 1 for d in group_degrees)
assert sum(group_degrees) == n*M
for a in range(3):
    for j in range(m):
        assert sum(d for edge, d in zip(support, group_degrees) if edge[a] == j) \
            == M*(r if j == selected[a] else 1)
assert r**3+5*r+3*m-8 == actual['complete_fixed_counts']['V']
assert r**3-3*r*r+5*r-2 == actual['complete_fixed_counts']['quotient']

actual_receipt = {
    'n': n, 'prefix_n': m, 'r': r, 'M': M,
    'selected_edge': selected, 'rho': str(rho),
    'other_incident_edges_and_masses': [
        [{'edge': edge, 'mass': str(p)} for edge, p in mode] for mode in incident],
    'first_permitted_degree': M,
    'core_degree_at_s_M': int(M*(r-1+rho)),
    'j_upper_bound_at_s_M': int(M*min(p for _, p in incident[0])),
    'v_upper_bound_at_s_M': int(M*min(p for _, p in incident[2])),
    'dimension': r**3-3*r*r+5*r-2,
    'scope': 'All margin, edge-multiplicity and grading identities checked; no large Kronecker coefficient or Hilbert density evaluated.'
}
receipt = {'finding': 'K-032', 'status': 'PASS', 'rank_two_independent_checks': receipts,
           'actual_amplifier_grading_check': actual_receipt,
           'scope': 'Finite representation-formula verification complements the complete mathematical normalization proof.'}
(ROOT / 'component_normalization_formula_checks.json').write_text(json.dumps(receipt, indent=2)+'\n')
print('PASS K-032: direct rank-two monomial/Weyl counts match exact character sums at s=4,8,12; actual n58 fixed representation and all weighted margins checked.')

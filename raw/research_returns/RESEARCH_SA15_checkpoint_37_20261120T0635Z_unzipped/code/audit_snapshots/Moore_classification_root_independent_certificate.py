"""Universal characteristic-two 9x9 Moore singular-parameter certificate.

All coefficients are reconstructed from the determinant permutation formula.
This classifies the abstract matrix parameter locus, not a Cartier tensor.
Every support exclusion and every noncharacter one-zero exclusion is explicit.
"""
from pathlib import Path
from itertools import product, permutations
from collections import defaultdict, Counter
from datetime import datetime, timezone
import hashlib
import json
import time

start = time.perf_counter()
counts = Counter()
points = list(product(range(3), repeat=2))
index = {a: i for i, a in enumerate(points)}
plus = [[index[tuple((x+y) % 3 for x, y in zip(a, b))]
         for b in points] for a in points]
minus = [[index[tuple((x-y) % 3 for x, y in zip(a, b))]
          for b in points] for a in points]
entries = [[(1 << (36+4*minus[i][j])) + (1 << (4*plus[i][j]))
            for j in range(9)] for i in range(9)]
terms = set()
for perm in permutations(range(9)):
    term = sum(entries[i][j] for i, j in enumerate(perm))
    if term in terms:
        terms.remove(term)
    else:
        terms.add(term)
    counts['determinant_permutations'] += 1
coefficients = defaultdict(set)
for term in terms:
    coefficients[term & ((1 << 36)-1)].add(term >> 36)
assert len(terms) == 55296 and len(coefficients) == 2080
counts['universal_monomials'] = len(terms)
counts['universal_x_coefficients'] = len(coefficients)
decode = lambda x: tuple((x >> (4*i)) & 15 for i in range(9))
monomial = lambda i, n=1: n << (4*i)

def add(*polys):
    result = set()
    for poly in polys:
        result.symmetric_difference_update(poly)
    return result

def multiply(a, b):
    result = set()
    for u in a:
        for v in b:
            term = u+v
            if term in result:
                result.remove(term)
            else:
                result.add(term)
    return result

def power(a, n):
    result = {0}
    for _ in range(n):
        result = multiply(result, a)
    return result

def restrict(support):
    result = {}
    for x, cs in coefficients.items():
        kept = {c for c in cs
                if all(((c >> (4*i)) & 15) == 0 for i in range(9) if i not in support)}
        if kept:
            result[x] = kept
    return result

def find_coefficient(restricted, desired):
    found = [x for x, cs in restricted.items() if cs == desired]
    assert found, ['Missing coefficient', sorted(map(hex, desired))]
    counts['explicit_factor_identities'] += 1
    return {'x_exponents': decode(min(found)),
            'c_terms': [decode(c) for c in sorted(desired)]}

# Every symmetric support consists of opposite pairs about a missing center.
known = {}
center_pairs = {}
for h in points:
    center = index[h]
    pairs = []
    used = {center}
    for i, v in enumerate(points):
        if i in used:
            continue
        j = index[tuple((2*a-b) % 3 for a, b in zip(h, v))]
        pairs.append((i, j))
        used |= {i, j}
    assert len(pairs) == 4
    center_pairs[center] = pairs
    for choices in product((0, 1), repeat=4):
        support = sum((1 << a)+(1 << b) for choice, (a, b) in zip(choices, pairs) if choice)
        if support:
            known.setdefault(support, []).append(center)
assert Counter(s.bit_count() for s in known) == {2: 36, 4: 54, 6: 12, 8: 9}

coefficient_supports = []
for x, cs in coefficients.items():
    coefficient_supports.append((x, [(c, sum(1 << i for i in range(9)
                                            if (c >> (4*i)) & 15)) for c in cs]))
coefficient_supports.sort(key=lambda row: len(row[1]))
excluded_supports = []
survivors = []
for support in range(1, 512):
    witness = None
    for x, cs in coefficient_supports:
        kept = [c for c, s in cs if s & ~support == 0]
        if len(kept) == 1:
            witness = {'x_exponents': decode(x), 'c_exponents': decode(kept[0])}
            break
    if witness is None:
        survivors.append(support)
    else:
        excluded_supports.append({'support_indices': [i for i in range(9) if support >> i & 1],
                                  'single_monomial_coefficient': witness})
    counts['all_nonempty_supports'] += 1
assert set(survivors) == set(known)
assert len(excluded_supports) == 400
counts['excluded_support_monomials'] = len(excluded_supports)

# Exact affine maps cover the four support orbits. Covariance itself is the
# identity M_c(x)_(Ta+h,Tb)=c_(T(a-b)+h)*x_(T(a+b)+h).
representatives = {2: (1, 2), 4: (1, 2, 3, 6), 6: tuple(range(3, 9)), 8: tuple(range(1, 9))}
affine_witnesses = {}
for a, b, c, d in product(range(3), repeat=4):
    if (a*d-b*c) % 3 == 0:
        continue
    for h in points:
        permutation = [index[((a*x+b*y+h[0]) % 3, (c*x+d*y+h[1]) % 3)]
                       for x, y in points]
        assert len(set(permutation)) == 9
        for size, support in representatives.items():
            image = sum(1 << permutation[i] for i in support)
            affine_witnesses.setdefault(image, {'matrix': [[a, b], [c, d]], 'translation': h,
                                                'representative_size': size})
        counts['affine_index_maps'] += 1
assert set(affine_witnesses) == set(known)

# Two-point support: (c1^3+c2^3)^3 times the product of all x coordinates.
r2 = restrict(set(representatives[2]))
two_polynomial = power({monomial(1, 3), monomial(2, 3)}, 3)
assert len(r2) == 1
two_witness = find_coefficient(r2, two_polynomial)
assert two_witness['x_exponents'] == (1,)*9

# Four-point support: two nonzero monomial factors times opposite cube sums.
r4 = restrict(set(representatives[4]))
four_witnesses = [
    find_coefficient(r4, {monomial(1, 3)+monomial(3, 3)+monomial(6, 3),
                         monomial(2, 3)+monomial(3, 3)+monomial(6, 3)}),
    find_coefficient(r4, {monomial(3, 3)+monomial(1, 3)+monomial(2, 3),
                         monomial(6, 3)+monomial(1, 3)+monomial(2, 3)}),
]

# Six-point support A_i=c_(1,i), B_i=c_(2,i).
r6 = restrict(set(representatives[6]))
A = (3, 4, 5)
B = (6, 7, 8)
PA = sum(monomial(i) for i in A)
PB = sum(monomial(i) for i in B)
six_witnesses = {
    'product_equality_cube': find_coefficient(r6, power({PA, PB}, 3)),
    'sum_of_cubes_equality_cube': find_coefficient(r6, power({monomial(i, 3) for i in A+B}, 3)),
    'cyclic_matching_products': [],
}
for shift in range(3):
    polynomial = {0}
    for i in range(3):
        polynomial = multiply(polynomial, {monomial(A[i], 3), monomial(B[(i+shift) % 3], 3)})
    six_witnesses['cyclic_matching_products'].append(find_coefficient(r6, polynomial))

# Exhaust all possible choices of one zero factor in each cyclic product.
# The closure steps encode exactly the elementary sum/product proof in the text.
matching_records = []
for selected_rows in product(range(3), repeat=3):
    parent = list(range(6))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    def union(i, j):
        i, j = find(i), find(j)
        if i != j:
            parent[j] = i
    selected_columns = tuple((i+shift) % 3 for shift, i in enumerate(selected_rows))
    for i, j in zip(selected_rows, selected_columns):
        union(i, 3+j)
    nr, nc = len(set(selected_rows)), len(set(selected_columns))
    if nr == nc == 3:
        reason = 'Already a perfect reflection matching.'
    elif nr == 1 or nc == 1:
        reason = 'Three-edge star: equality of sums makes the two remaining values equal; nonzero product equality then makes their square equal to the common value squared.'
        for i in range(1, 6):
            union(0, i)
    else:
        assert nr == nc == 2
        reason = 'Two rows and two columns: the three edges give one four-vertex equality class; equality of sums identifies the two unused values.'
        unused_row = next(i for i in range(3) if i not in selected_rows)
        unused_col = next(i for i in range(3) if i not in selected_columns)
        used_classes = {find(i) for i in set(selected_rows)} | {find(3+j) for j in set(selected_columns)}
        assert len(used_classes) == 1
        union(unused_row, 3+unused_col)
    shifts = [h for h in range(3) if all(find(i) == find(3+(h-i) % 3) for i in range(3))]
    assert shifts
    matching_records.append({'selected_rows': selected_rows, 'selected_columns': selected_columns,
                             'case': [nr, nc], 'reason': reason, 'reflection_constants': shifts})
    counts['complete_three_factor_choices'] += 1
assert Counter(tuple(r['case']) for r in matching_records) == {(3, 3): 3, (1, 3): 3, (3, 1): 3, (2, 2): 18}

six_phase_records = []
for phase in product(range(3), repeat=3):
    if sum(phase) % 3:
        continue
    alpha, beta = phase[0], (phase[1]-phase[0]) % 3
    assert phase == tuple((alpha+beta*i) % 3 for i in range(3))
    six_phase_records.append({'phase': phase, 'affine_character': [alpha, beta]})
assert len(six_phase_records) == 9

# Eight-point support: four cube ratios, then all 81 possible phase patterns.
r8 = restrict(set(representatives[8]))
pairs = [(1, 2), (3, 6), (4, 8), (5, 7)]
cube_witnesses = []
for a, b in pairs:
    found = None
    for x, cs in sorted(r8.items()):
        if len(cs) != 2:
            continue
        exps = [decode(c) for c in cs]
        common = tuple(min(exps[0][i], exps[1][i]) for i in range(9))
        residual = {tuple(e[i]-common[i] for i in range(9)) for e in exps}
        expected = {tuple(3 if i == a else 0 for i in range(9)),
                    tuple(3 if i == b else 0 for i in range(9))}
        if residual == expected:
            found = {'pair': [a, b], 'x_exponents': decode(x), 'common_c_exponents': common}
            break
    assert found is not None
    cube_witnesses.append(found)
    chosen_x = monomial(0, 7)+monomial(a)+monomial(b)
    common_monomial = sum(monomial(i) for i in range(9) if i not in (0, a, b))
    assert r8[chosen_x] == {common_monomial+monomial(a, 3), common_monomial+monomial(b, 3)}
    counts['eight_uniform_binomial_identities'] += 1
roots = [1, 2, 3]  # 1,z,z^2 in F4=F2[z]/(z^2+z+1); addition is XOR.
characters = {tuple(sum(l*v for l, v in zip(ell, points[a])) % 3 for a, _ in pairs)
              for ell in points}
phase_records = []
decoded_r8 = {x: [decode(c) for c in cs] for x, cs in r8.items()}
for phase in product(range(3), repeat=4):
    nonzero_count = 0
    witness = None
    for x, cs in sorted(decoded_r8.items()):
        result = {}
        for c in cs:
            dmon = tuple(c[a]+c[b] for a, b in pairs)
            exponent = sum(phase[j]*c[a] for j, (a, _) in enumerate(pairs)) % 3
            result[dmon] = result.get(dmon, 0) ^ roots[exponent]
            if result[dmon] == 0:
                del result[dmon]
        if result:
            nonzero_count += 1
            if len(result) == 1 and witness is None:
                dmon, value = next(iter(result.items()))
                witness = {'x_exponents': decode(x), 'd_exponents': dmon,
                           'nonzero_F4_coefficient': value}
    is_character = phase in characters
    assert (nonzero_count == 0) == is_character
    if not is_character:
        assert witness is not None
    phase_records.append({'phase': phase, 'character': is_character,
                          'nonzero_coefficient_count': nonzero_count,
                          'single_monomial_exclusion': witness})
    counts['complete_eight_support_phases'] += 1
assert sum(r['character'] for r in phase_records) == 9

# Universal alternating row-scalings on all 81 proposed planes.
base_pairs = center_pairs[0]
for h in points:
    for ell in points:
        c_form = {index[h]: None}
        for variable, (i, j) in enumerate(base_pairs):
            v = points[i]
            positive = index[tuple((a+b) % 3 for a, b in zip(h, v))]
            negative = index[tuple((a-b) % 3 for a, b in zip(h, v))]
            c_form[positive] = (variable, sum(a*b for a, b in zip(ell, v)) % 3)
            c_form[negative] = (variable, 0)
        for a in points:
            for b in points:
                def entry(row, col):
                    ci = index[tuple((u-v+w) % 3 for u, v, w in zip(row, col, h))]
                    value = c_form[ci]
                    if value is None:
                        return None
                    return (value[0], (value[1]-sum(u*v for u, v in zip(ell, row))) % 3)
                assert entry(a, b) == entry(b, a)
                if a == b:
                    assert entry(a, b) is None
                counts['symbolic_alternating_entries'] += 1

out = {
    'status': 'PASS_UNIVERSAL_SET_THEORETIC_CLASSIFICATION',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'runtime_seconds': time.perf_counter()-start,
    'counts': dict(counts),
    'parameter_index_order': points,
    'support_orbit_counts': dict(sorted(Counter(s.bit_count() for s in known).items())),
    'excluded_supports': excluded_supports,
    'surviving_support_affine_maps': {str(s): affine_witnesses[s] for s in sorted(known)},
    'two_support_factor': two_witness,
    'four_support_factors': four_witnesses,
    'six_support_factors': six_witnesses,
    'six_support_matching_cases': matching_records,
    'six_support_character_phases': six_phase_records,
    'eight_support_cube_factors': cube_witnesses,
    'eight_support_phase_records': phase_records,
    'coefficient_table_sha256': hashlib.sha256(json.dumps({hex(x): sorted(map(hex, cs))
                                                        for x, cs in sorted(coefficients.items())},
                                                       sort_keys=True).encode()).hexdigest(),
    'scope': 'Over any algebraically closed field of characteristic two, the nonzero parameters c with det(c_(a-b)*x_(a+b)) identically zero are exactly the 81 translated character-scaled alternating four-dimensional vector spaces, equivalently 81 projective three-spaces. This is set-theoretic, not a scheme-theoretic ideal assertion. Exhaustive support/phase cases are finite exact symbolic reductions, not finite-field sampling.',
    'geometric_limitation': 'No actual Cartier tensor, theta-value or fixed-surface rank identification is established by this algebraic classification.',
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k: out[k] for k in ('status', 'actual_utc', 'runtime_seconds', 'counts', 'support_orbit_counts')}))

"""Exact one-zero Moore chart: exhaustive root-of-unity substitutions.

All determinant coefficients are reconstructed over F2 from permutations.
The finite phase enumeration is exhaustive after four explicit cube-ratio
relations, rather than a finite sample of geometric parameter values.
The Cartier/theta identification and the charts with several zeros remain open.
"""
from pathlib import Path
from itertools import product, permutations
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import time

start = time.perf_counter()
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
coefficients = defaultdict(list)
for term in terms:
    coefficients[term & ((1 << 36)-1)].append(term >> 36)
assert len(terms) == 55296 and len(coefficients) == 2080
decode = lambda x: tuple((x >> (4*i)) & 15 for i in range(9))
restricted = {x: [decode(c) for c in cs if (c & 15) == 0]
              for x, cs in coefficients.items()}
restricted = {x: cs for x, cs in restricted.items() if cs}
pairs = [(1, 2), (3, 6), (4, 8), (5, 7)]

# Extract an actual determinant coefficient equal to the indicated
# common nonzero monomial times (c_v^3+c_-v^3), for each opposite pair.
cube_witnesses = []
for a, b in pairs:
    found = None
    for x, cs in sorted(restricted.items()):
        if len(cs) != 2:
            continue
        common = tuple(min(cs[0][i], cs[1][i]) for i in range(9))
        residual = {tuple(c[i]-common[i] for i in range(9)) for c in cs}
        ea = tuple(3 if i == a else 0 for i in range(9))
        eb = tuple(3 if i == b else 0 for i in range(9))
        if residual == {ea, eb}:
            found = {'pair': [a, b], 'x_exponents': decode(x),
                     'common_c_exponents': common}
            break
    assert found is not None
    cube_witnesses.append(found)

# A primitive cube root z satisfies z^2+z+1=0 in characteristic two.
# Elements 1,z,z^2 use bit encodings 1,2,3; addition is XOR.
roots = [1, 2, 3]
character_phases = {
    tuple(sum(l*v for l, v in zip(ell, points[a])) % 3 for a, _ in pairs)
    for ell in points
}
records = []
for phase in product(range(3), repeat=4):
    nonzero = []
    witness = None
    for x, cs in sorted(restricted.items()):
        result = {}
        for c in cs:
            dmon = tuple(c[a]+c[b] for a, b in pairs)
            exponent = sum(phase[j]*c[a] for j, (a, _) in enumerate(pairs)) % 3
            result[dmon] = result.get(dmon, 0) ^ roots[exponent]
            if result[dmon] == 0:
                del result[dmon]
        if result:
            nonzero.append(x)
            if len(result) == 1 and witness is None:
                dmon, value = next(iter(result.items()))
                witness = {'x_exponents': decode(x), 'd_exponents': dmon,
                           'nonzero_F4_coefficient': value}
    is_character = phase in character_phases
    assert (len(nonzero) == 0) == is_character
    if not is_character:
        assert witness is not None, ('No monomial exclusion', phase)
    records.append({'phase': phase, 'character_phase': is_character,
                    'nonzero_determinant_coefficient_count': len(nonzero),
                    'monomial_exclusion': witness})
assert sum(r['character_phase'] for r in records) == 9
assert sum(r['monomial_exclusion'] is not None for r in records) == 72

out = {
    'status': 'PASS_EXACT_ONE_ZERO_CHART',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'runtime_seconds': time.perf_counter()-start,
    'matrix': 'M_c(x)_(a,b)=c_(a-b)*x_(a+b), a,b in F3^2, over algebraically closed characteristic two',
    'chart': 'c_0=0; all other eight c coordinates nonzero',
    'universal_permutations': 362880,
    'universal_monomials': len(terms),
    'universal_x_coefficients': len(coefficients),
    'cube_ratio_witnesses': cube_witnesses,
    'phase_count': len(records),
    'zero_character_phase_count': 9,
    'excluded_phase_count': 72,
    'phase_records': records,
    'proof_scope': 'Four actual coefficient binomials force opposite coordinate ratios to lie in the complete three-element root-of-unity group. All 81 ratio patterns are substituted into every universal determinant coefficient. Exactly nine additive-character patterns give zero identically; each of the other 72 has an explicit single nonzero monomial coefficient, which cannot vanish anywhere on the chart. Thus this is an exact chart classification over every algebraically closed characteristic-two field, not an F4-point extrapolation.',
    'limitations': 'Several-zero charts and Clifford covariance have not been classified here. No actual Cartier tensor or theta-value identification is established, and no nonproduct geometric rank assertion follows.',
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k: out[k] for k in ('status', 'actual_utc', 'runtime_seconds',
                                    'phase_count', 'zero_character_phase_count',
                                    'excluded_phase_count')}))

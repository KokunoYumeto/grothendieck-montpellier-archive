"""Independent p=13 reflection/projector traces; imports only this audit's code.

Five monomial-group orbits partition P^2(F_13). All matrices and orbit
partitions are constructed here; no archived neighbor data is imported.
"""
from itertools import product
from pathlib import Path
import json

from character_trace import (
    O, I, W, PERMS, UNITS, add, sub, mul, conj, norm, gram,
    character_averages, full_invariant_count, scale, det,
)

PI = (4, 1)
BARPI = conj(PI)
DELTA = (1, -1)


def residue(x):
    return (x[0] - 4*x[1]) % 13


def normalized_line(v):
    v = tuple(x % 13 for x in v)
    first = next(x for x in v if x)
    inv = pow(first, -1, 13)
    return tuple(x*inv % 13 for x in v)


def projective_orbit(v):
    lines = set()
    for perm in PERMS:
        for units in product(UNITS, repeat=3):
            gv = [0, 0, 0]
            for j in range(3):
                gv[perm[j]] = residue(mul(units[j], v[j]))
            lines.add(normalized_line(gv))
    return lines


def reflection(v, eta):
    n = sum(norm(x) for x in v)
    difference = sub(mul(eta, BARPI), PI)
    assert all(x % n == 0 for x in difference)
    c = tuple(x//n for x in difference)
    A = [[add(PI if i == j else O, mul(c, mul(v[i], conj(v[j]))))
          for j in range(3)] for i in range(3)]
    assert gram(A) == [[(13, 0) if i == j else O for j in range(3)]
                       for i in range(3)]
    assert det(A) == mul(eta, mul(mul(PI, PI), BARPI))
    reduction = [[residue(x) for x in row] for row in A]
    nonzero_columns = [tuple(reduction[i][j] for i in range(3))
                       for j in range(3) if any(reduction[i][j] for i in range(3))]
    assert nonzero_columns
    target = normalized_line(tuple(residue(x) for x in v))
    assert all(normalized_line(col) == target for col in nonzero_columns)
    return A, n, c


def main():
    specifications = [
        ([I, O, O], I, 3),
        ([I, I, O], (1, 1), 18),
        ([I, DELTA, O], (-1, -1), 18),
        ([I, I, I], W, 36),
        ([I, I, DELTA], (0, -1), 108),
    ]
    kmax = 30
    total = [0]*(kmax+1)
    union = set()
    rows = []
    for v, eta, expected_size in specifications:
        A, n, c = reflection(v, eta)
        orbit = projective_orbit(v)
        assert len(orbit) == expected_size
        assert not (union & orbit)
        union |= orbit
        sums = character_averages(A, 13, kmax)
        for k, value in enumerate(sums):
            total[k] += len(orbit)*value
        rows.append({'vector':v, 'eta':eta, 'norm':n, 'rank_one_coefficient':c,
                     'matrix':A, 'orbit_size':len(orbit),
                     'projective_lines':sorted(orbit),
                     'sum_scaled_characters_by_degree':sums})
    all_lines = {normalized_line(v) for v in product(range(13), repeat=3) if any(v)}
    assert union == all_lines and len(union) == 183
    assert all(x % 1296 == 0 for x in total)
    traces = [x//1296 for x in total]
    dimensions = [full_invariant_count(k)-full_invariant_count(k-1)
                  for k in range(kmax+1)]
    out = {'method':'independent rank-one reflection/projector character sum',
           'p':13, 'pi':PI, 'group_order':1296, 'neighbors':183,
           'reflection_orbits':rows, 'dimensions':dimensions,
           'scaled_T13_traces':traces,
           'checks':['exact Gram and determinant identities',
                     'rank-one reductions with specified image lines',
                     'five disjoint orbits exhaust every projective line',
                     'all character averages integral after division by1296']}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'orbit_sizes':[r['orbit_size'] for r in rows],
                      'degree3':traces[3], 'degree5':traces[5],
                      'scaled_T13_traces':traces},indent=2))


if __name__ == '__main__':
    main()

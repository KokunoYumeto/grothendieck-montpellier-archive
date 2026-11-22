"""Finite graph/group-order supplement to the universal powers-three proof.

No geometry or general induction is inferred from these finite cases.
For the heart span use explicit sum-zero shifts, stopping once the proven
upper bound is attained; do not enumerate all 9^(m-1) shifts.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations
from functools import reduce
from operator import xor
import json
import time

started = time.perf_counter()
K = [(a, b) for a in range(3) for b in range(3)]
zero = (0, 0)
def neg(x): return tuple(-a % 3 for a in x)
def sub(x, y): return tuple((a - b) % 3 for a, b in zip(x, y))
def typ(x): return min(x, neg(x))
types = sorted({typ(g) for g in K if g != zero})
def xors(xs): return reduce(xor, xs, 0)

class BinarySpan:
    def __init__(self): self.pivots = {}
    def add(self, x):
        while x:
            i = x.bit_length() - 1
            if i in self.pivots: x ^= self.pivots[i]
            else:
                self.pivots[i] = x
                return True
        return False
    def extend(self, xs):
        for x in xs: self.add(x)
    def __len__(self): return len(self.pivots)

cases = []
for m in (3, 5, 9, 27):
    edges = []
    for i in range(m):
        for h in types:
            for e in range(2): edges.append(('l', i, h, e))
    pairs = list(combinations(range(m), 2))
    for i, j in pairs:
        for g in K:
            for e in range(2): edges.append(('c', i, j, g, e))
    index = {edge: j for j, edge in enumerate(edges)}
    stars = [xors(1 << j for j, edge in enumerate(edges)
                  if edge[0] == 'c' and i in edge[1:3]) for i in range(m)]
    assert xors(stars) == 0
    starspan = BinarySpan(); starspan.extend(stars)
    assert len(starspan) == m - 1
    assert len(edges) == 9 * m * m - m

    def coordinates(r):
        groups = {h: [] for h in types}; selected = []
        for j, edge in enumerate(edges):
            if edge[0] == 'l': groups[edge[2]].append(1 << j)
            else:
                _, i, k, g, _ = edge
                difference = sub(g, sub(r[k], r[i]))
                if difference == zero: selected.append(1 << j)
                else: groups[typ(difference)].append(1 << j)
        return groups, selected

    r0 = [zero] * m
    groups0, selected0 = coordinates(r0)
    assert len(selected0) == m * (m - 1)
    assert all(len(v) == 2 * m * m for v in groups0.values())
    T = BinarySpan(); T.extend(stars)
    T.extend(v for vs in groups0.values() for v in vs)
    assert len(T) - (m - 1) == 8 * m * m
    hearts0 = BinarySpan(); hearts0.extend(stars)
    hearts0.extend(vs[0] ^ v for vs in groups0.values() for v in vs[1:])
    assert len(hearts0) - (m - 1) == 8 * m * m - 4

    for i in range(m):
        qsum = xors(1 << index[('c', min(i, j), max(i, j), zero, e)]
                     for j in range(m) if j != i for e in range(2))
        unselected = xors(1 << j for j, edge in enumerate(edges)
                          if edge[0] == 'c' and i in edge[1:3] and edge[3] != zero)
        assert qsum ^ unselected == stars[i]
        for vs in groups0.values():
            ones = sum(bool(unselected & v) for v in vs)
            assert ones == 4 * (m - 1)
            assert 0 < ones < 2 * m * m

    # The fixed first triangle already kills every possible type constant.
    constants = [xors(groups0[h]) for h in types]
    constraints = BinarySpan()
    for u in K:
        r = [neg(u), zero, u] + [zero] * (m - 3)
        row = 0
        for h, constant in enumerate(constants):
            bit = 0
            for i, j in ((0, 1), (0, 2), (1, 2)):
                bit ^= bool(constant & (1 << index[('c', i, j, sub(r[j], r[i]), 0)]))
            if bit: row |= 1 << h
        constraints.add(row)
    assert len(constraints) == 4

    result = dict(m=m, edges=len(edges), graph_dimension=9*m*m-2*m+1,
                  source_graph_dimension=(m-1)**2, T_dimension=8*m*m,
                  each_type_dimension=2*m*m, each_total_heart_dimension=8*m*m-4,
                  type_constant_constraint_rank=len(constraints),
                  star_ones_per_type=4*(m-1), star_zeroes_per_type=2*m*m-4*(m-1))
    if m <= 9:
        span = BinarySpan(); span.extend(stars)
        tested = []
        # For each pair, a third entry absorbs the sum. These are actual
        # admissible shifts; every individual pair difference ranges over K.
        candidates = [tuple(r0)]
        for i, j in pairs:
            third = next(v for v in range(m) if v not in (i, j))
            for g in K:
                r = [zero] * m
                r[j] = g; r[third] = neg(g)
                candidates.append(tuple(r))
        seen = set()
        for r in candidates:
            if r in seen: continue
            seen.add(r); tested.append(r)
            groups, selected = coordinates(r)
            assert len(selected) == m*(m-1)
            span.extend(vs[0] ^ v for vs in groups.values() for v in vs[1:])
            if len(span) == len(edges)-1: break
        assert len(span) == len(edges)-1
        result['tested_sum_zero_shifts'] = tested
        result['heart_span_dimension_mod_stars'] = len(span)-(m-1)
        assert result['heart_span_dimension_mod_stars'] == result['graph_dimension']-1
    else:
        result['heart_span_scope'] = 'Not numerically enumerated at m27; universal symbolic proof applies.'
    cases.append(result)

orders = []
for m in (3, 5, 9, 15, 27, 81, 243, 729):
    r, s = m*m-1, 2*m*m
    gl_v2 = r*(r-1)//2
    alternating_v2 = s-s.bit_count()-1
    assert gl_v2 > 2*r >= alternating_v2
    R = 9*m*m-1
    summand = r+4*(s-1)
    assert summand == R-4 and 2*summand > R
    orders.append(dict(m=m, r=r, s=s, GL_order_v2=gl_v2,
                       alternating_order_v2=alternating_v2,
                       large_summand_dimension=summand, target_dimension=R))

out = dict(status='PASS', actual_utc=datetime.now(timezone.utc).isoformat(),
           runtime_seconds=time.perf_counter()-started, graph_cases=cases,
           group_order_cases=orders,
           scope='Exact graphs for m3,5,9,27; heart-span calculation onlym3,5,9 using retained admissible shifts. Eight exact group-order/dimension cases. No geometry or universal theorem inferred from finite checks.')
Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_powers_three_independent_certificate.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('graph_cases','group_order_cases')},indent=2))
print(json.dumps([dict(m=c['m'],graph_dimension=c['graph_dimension'],
                      tested_shifts=len(c.get('tested_sum_zero_shifts',[])),
                      heart_span=c.get('heart_span_dimension_mod_stars')) for c in cases]))

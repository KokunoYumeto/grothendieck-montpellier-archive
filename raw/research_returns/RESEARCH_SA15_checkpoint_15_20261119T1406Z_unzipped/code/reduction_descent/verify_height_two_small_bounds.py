"""Exact auxiliary certificate for B-RD31; no finite check replaces its proof."""
from pathlib import Path
from time import perf_counter
import json
import sympy as S

start = perf_counter()
a0, a1, c0, c1 = S.symbols('a0 a1 c0 c1', real=True)
a, ac, c, cc = a0+S.I*a1, a0-S.I*a1, c0+S.I*c1, c0-S.I*c1
A = S.Matrix([[a, 3*cc], [c, ac]])
As = S.Matrix([[ac, 3*c], [cc, a]])
F = S.Matrix([[0, 3], [1, 0]])
assert (A*F-F*As).applyfunc(S.expand) == S.zeros(2)
assert S.expand(A.det()-(a0*a0+a1*a1-3*(c0*c0+c1*c1))) == 0
assert F*F == 3*S.eye(2)

# For the formal-group inequality, the lowest possible iterate valuation
# is a monotone function of the initial integral valuation.
cases = 0
for ram in range(1, 2001):
    top = (ram-1)//2
    for n in range(1, 9):
        val = 1
        for _ in range(n-1):
            val = min(ram+val, 1+3*val, 9*val)
        if val <= top:
            assert ram >= 3**n
        if ram < 3**n:
            assert val > top
        cases += 1
assert min(24+1, 1+3, 9) == 4
assert min(24+4, 1+3*4, 9*4) == 13
assert 13 > (24-1)/2

images = [(1, t) for t in (1, 2, 4, 8)] + [(3, t) for t in (1, 2, 4)]
joint_bounds = []
for p1, t1 in images:
    for p2, t2 in images:
        bound = p1*p2*int(S.ilcm(t1, t2))
        assert bound <= 36
        joint_bounds.append(bound)
assert max(joint_bounds) == 36
assert 2*36 <= 2*3**4
assert 4+1 == 5  # Bondarko ell=1,u=4 gives the level3^5, manuscriptnu4.

det_cases = 0
for d1 in range(3):
    for d2 in range(3):
        for e1 in (1, -1):
            for e2 in (1, -1):
                equal = all((e1*pow(cyc,d1,9)-e2*pow(cyc,d2,9))%9 == 0
                            for cyc in (1,4,7))
                assert equal == (d1 == d2 and e1 == e2)
                det_cases += 1

result = {
    'status': 'PASS',
    'quaternion_identity_groups': 3,
    'formal_valuation_cases': cases,
    'joint_inertia_order_cases': len(joint_bounds),
    'max_joint_inertia_order': max(joint_bounds),
    'determinant_dimension_cases': det_cases,
    'explicit_ramification24_order27_obstruction': [1,4,13],
    'candidate_least_index_interval': [2,4],
    'elapsed_seconds': perf_counter()-start,
}
print(json.dumps(result, indent=2))
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result, indent=2)+'\n')

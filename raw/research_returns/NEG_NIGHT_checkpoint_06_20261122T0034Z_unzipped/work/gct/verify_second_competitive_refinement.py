"""Exact finite projection for the second NN-G036 refinement.

This script verifies row deletion and elementary polynomial remainders.
The arbitrary-degree exclusions themselves are the written proofs:
g036_small_gluing_final_draft.tex and the root w12_exclusions.tex.
"""
from pathlib import Path
import json
import sympy as sp

source = json.loads(Path('work/gct/competitive_mass_refinement_certificate.json').read_text())
rows = source['remaining_rows']

def excluded_small(r):
    return (
        (r['w'] == 8 and (r['g1'], r['g2']) == (128, 80))
        or (r['w'] == 10 and r['g1'] == r['g2'] == 100)
        or (r['w'] == 10 and sorted((r['g1'], r['g2'])) == [84, 100])
    )

def excluded_twelve(r):
    return r['w'] == 12 and (
        (sorted((r['g1'], r['g2'])) == [80, 96] and r['d1'] == r['d2'] == 4)
        or sorted((r['g1'], r['g2'])) == [84, 88]
        or r['g1'] == r['g2'] == 84
    )

small = [r for r in rows if excluded_small(r)]
twelve = [r for r in rows if excluded_twelve(r)]
remaining = [r for r in rows if not (excluded_small(r) or excluded_twelve(r))]
assert len(rows) == 26 and len(small) == 4 and len(twelve) == 5
assert not any(excluded_twelve(r) for r in small)
triples = sorted({(r['g1'], r['d1'], r['u1']) for r in remaining})
assert len(remaining) == 17
assert sum(len(r['allowed_auxiliary_increment_pairs']) for r in remaining) == 26
assert len(triples) == 8
assert min(r['score_min'] for r in remaining) == 2604
assert {r['w'] for r in remaining} == {10, 12}
assert all(
    (r['g1'], r['g2'], r['d1'], r['u1']) == (80, 120, 8, 4)
    for r in remaining if r['w'] == 10
)
assert all((r['u1']-4)*(r['u2']-4) < 64 for r in rows if r['w'] == 12)

D = sp.symbols('D')
psi = D*(D-3)
T1 = D-2
T2 = D**2-4*D+2
T3 = D**3-6*D**2+9*D-2
T4 = D**4-8*D**3+20*D**2-16*D+2
assert psi.subs(D, 2) == -2
assert psi != T2
N = sp.expand(D*(D+2)*(psi+1))
assert N.subs(D, 2) == -8
assert sp.rem(T3, T1, D) == 0
assert sp.rem(N, T2, D) == 16*D-10
assert sp.expand(N-T4) != 0
assert 640 % (4**4) != 0
assert any(int(x) % 4 for x in sp.Poly(2*D*psi, D).all_coeffs())

out = {
    'previous_base_rows': 26,
    'new_small_gluing_exclusions': len(small),
    'new_mass_twelve_exclusions': len(twelve),
    'remaining_base_rows': len(remaining),
    'remaining_auxiliary_increment_pairs': 26,
    'remaining_first_cell_mass_triples': triples,
    'necessary_closed_table_score_lower_bound': 2604,
    'actual_upper_bound': 2744,
    'remaining_rows': remaining,
    'scope': 'Exact finite projection and polynomial identities. Uniform written proofs, not finite support enumeration, justify the deleted rows. No realizability of surviving rows is asserted.'
}
Path('work/gct/second_competitive_refinement_certificate.json').write_text(
    json.dumps(out, indent=2)+'\n')
print(json.dumps({k: v for k, v in out.items() if k != 'remaining_rows'}, indent=2))

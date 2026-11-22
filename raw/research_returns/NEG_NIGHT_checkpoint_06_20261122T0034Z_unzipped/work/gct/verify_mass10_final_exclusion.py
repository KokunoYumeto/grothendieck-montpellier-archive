"""Finite projection and scalar identities for the uniform w=10 exclusion.
The proof in g036_mass10_exclusion_draft.tex covers all support degrees.
"""
from pathlib import Path
import json
import sympy as sp

source = json.loads(Path('work/gct/second_competitive_refinement_certificate.json').read_text())
rows = source['remaining_rows']
removed = [r for r in rows if r['w'] == 10]
remaining = [r for r in rows if r['w'] != 10]
assert len(removed) == 4
assert sum(len(r['allowed_auxiliary_increment_pairs']) for r in removed) == 6
for r in removed:
    assert (r['g1'], r['g2'], r['d1'], r['u1']) == (80, 120, 8, 4)
    for k1, k2 in r['allowed_auxiliary_increment_pairs']:
        assert r['a1_min']+r['modulus1']*k1 == 8
        assert r['v1_max']-r['v_step1']*k1 == 26
        assert r['v2_max']-r['v_step2']*k2 in (56, 58)
triples = sorted({(r['g1'], r['d1'], r['u1']) for r in remaining})
assert len(remaining) == 13
assert sum(len(r['allowed_auxiliary_increment_pairs']) for r in remaining) == 20
assert len(triples) == 7
assert {r['w'] for r in remaining} == {12}
assert min(r['score_min'] for r in remaining) == 2604
D, q = sp.symbols('D q')
A1 = D*(D-2)*(D-3)
laurent = sp.expand(A1.subs(D, q+2+q**-1))
assert [laurent.coeff(q, k) for k in range(4)] == [2, 1, 1, 1]
assert A1.subs(D, 2) == 0
assert [v for v in range(-4, 17) if v % 16 == 0] == [0, 16]
assert [v for v in (-1, 1) if (v-1) % 4 == 0] == [1]
out = {
    'newly_excluded_mass10_base_rows': 4,
    'newly_excluded_auxiliary_increment_pairs': 6,
    'remaining_base_rows': 13,
    'remaining_auxiliary_increment_pairs': 20,
    'remaining_first_cell_mass_triples': triples,
    'necessary_closed_table_score_lower_bound': 2604,
    'actual_upper_bound': 2744,
    'remaining_rows': remaining,
    'scope': 'Exact finite projection and scalar identities only; the written proof excludes every support degree. Remaining mass-twelve rows are not asserted realizable.'
}
Path('work/gct/mass10_final_exclusion_certificate.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k: v for k, v in out.items() if k != 'remaining_rows'}, indent=2))

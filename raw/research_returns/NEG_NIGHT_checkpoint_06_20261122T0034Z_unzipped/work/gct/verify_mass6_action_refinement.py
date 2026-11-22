"""Exact projection for the D+2 divisibility lemma and forward-row exclusion.
Uniform integral arguments are in g036_mass6_action_lemma_draft.tex.
"""
from pathlib import Path
import json
import sympy as sp

source = json.loads(Path('work/gct/mass10_final_exclusion_certificate.json').read_text())
rows = source['remaining_rows']
def mass6_excluded(r):
    return r['w'] % 4 == 0 and (
        (r['u1'] == 6 and r['g2'] % r['w'] != 0)
        or (r['u2'] == 6 and r['g1'] % r['w'] != 0)
    )
def forward_excluded(r):
    return (r['w'],r['g1'],r['g2'],r['d1'],r['d2'],r['u1'],r['u2']) == (12,80,96,12,4,4,12)
eight = [r for r in rows if mass6_excluded(r)]
forward = [r for r in rows if forward_excluded(r)]
remaining = [r for r in rows if not (mass6_excluded(r) or forward_excluded(r))]
assert len(eight) == 8 and len(forward) == 1
assert len(remaining) == 4
assert sum(len(r['allowed_auxiliary_increment_pairs']) for r in remaining) == 7
triples = sorted({(r['g1'],r['d1'],r['u1']) for r in remaining})
assert len(triples) == 3
assert min(r['score_min'] for r in remaining) == 2604
assert [h for h in range(-10,11) if h != 1 and 8 % (h-1) == 0 and h % 8 == 3] == [3]
D,q = sp.symbols('D q')
psi = D*(D-3)
for P in (sp.Integer(2), D-2):
    L = sp.expand(2*psi+6*P)
    first = sp.expand(D**2*(3*psi+6*P))
    assert sp.degree(L,D) == 2 and sp.LC(sp.Poly(L,D)) == 2
    assert sp.degree(first,D) == 4 and sp.LC(sp.Poly(first,D)) == 3
assert sp.expand((2*D*psi).subs(D,q+2+q**-1)).coeff(q,0) == 4
out = {
    'new_mass6_action_exclusions': 8,
    'new_forward_row_exclusion': 1,
    'remaining_base_rows': 4,
    'remaining_auxiliary_increment_pairs': 7,
    'remaining_first_cell_mass_triples': triples,
    'necessary_closed_table_score_lower_bound': 2604,
    'actual_upper_bound': 2744,
    'remaining_rows': remaining,
    'scope': 'Exact finite projection and polynomial identities; the written proofs establish every arbitrary-degree exclusion. Root additional lowest-row exclusions are not yet included.'
}
Path('work/gct/mass6_action_refinement_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='remaining_rows'},indent=2))

"""Check the integer identity using freshly reconstructed supplier rows.

The attributed archive contributes only the integer coefficient list and row
labels. All selected rows below are taken from the fresh subgroup/profile
certificates, and must also equal the corresponding attributed row literally.
"""
from pathlib import Path
import ast
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = HERE.parent / 'archive/qi-m3-certificates/witness/ncb/ncb_witness.g'
raw = SOURCE.read_bytes()
source = raw.decode().replace('\\\n', '')
data = {}
for name in ('W_GEN', 'W_COEF', 'W_TARGET'):
    found = re.search(r'\b' + name + r'\s*:=\s*(\[.*?\]);', source, re.S)
    assert found
    data[name] = ast.literal_eval(found.group(1))
stored, coef, target = (data[k] for k in ('W_GEN', 'W_COEF', 'W_TARGET'))
assert len(stored) == len(coef) == 3296
assert all(type(c) is int for c in coef)
assert all(len(v) == 45 and all(type(a) is int for a in v) for v in stored)

ordinary = json.loads((HERE / 'ordinary_profiles.json').read_text())
rows = {r['rowindex']: r['row'] for r in ordinary['rows']}
assert len(rows) == 95
profiles = []
for wc in (8, 33, 55):
    profile = json.loads((HERE / f'gale{wc}_profile.json').read_text())
    slots = profile['positive_slots']
    row = [sum(s['multiplicity'] * s['row'][j] for s in slots) for j in range(45)]
    assert row == profile['row']
    assert all(s['multiplicity'] > 0 and s['order'] in (4, 12)
               and s['quotient_genus'] >= 1 and s['branch_count'] >= 2 for s in slots)
    h = sum(s['multiplicity'] * s['h'] for s in slots)
    r = sum(s['multiplicity'] for s in slots)
    fdim = sum(s['multiplicity'] * (s['branch_count'] - 2) for s in slots)
    assert (r, h, fdim) == (profile['totalR'], profile['totalH'], profile['fermat_dimension_S'])
    assert h == 2 * profile['quotient_genus'] * r + fdim
    for j in range(4):
        a = sum(s['multiplicity'] * s['hodge_counts'][j][0] for s in slots)
        b = sum(s['multiplicity'] * s['hodge_counts'][j][1] for s in slots)
        assert [a, b] == profile['hodge_totals'][j] and a == b and 2*a == h
    rows[profile['rowindex']] = row
    profiles.append({k: profile[k] for k in ('rowindex', 'quotient_genus', 'totalR',
                      'totalH', 'fermat_dimension_S', 'total_branch_count', 'hodge_totals')})

support = {j + 1 for j, c in enumerate(coef) if c}
assert support == set(rows) and len(support) == 98
assert all(rows[j] == stored[j-1] for j in support)
result = [sum(coef[j-1] * rows[j][k] for j in support) for k in range(45)]
assert result == target == [0, 1] + [0] * 43
out = dict(check='PASS', source_sha256=hashlib.sha256(raw).hexdigest(),
           source_author='Benjamin Severn', source_license='CC BY4.0',
           source_doi='10.5281/zenodo.23549514',
           selected_count=98, ordinary_count=95, product_count=3,
           coefficient_l1=sum(abs(c) for c in coef),
           coefficient_l1_digits=len(str(sum(abs(c) for c in coef))),
           target=result, ordinary_max_h=ordinary['max_h'],
           ordinary_max_character_order=ordinary['max_character_order'],
           product_profiles=profiles,
           scope='Fresh supplier rows in exact archived integer relation; geometry proved separately.')
(HERE / 'complete_identity.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({k: v for k, v in out.items() if k not in ('coefficient_l1', 'product_profiles')}, indent=2))

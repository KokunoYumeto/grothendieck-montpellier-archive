#!/usr/bin/env python3
"""Integrate the independently audited four-dimensional relative fibre."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
receipt = root / 'logs/A135_root_integration.json'
if receipt.exists():
    raise SystemExit('A135 integration already recorded')
proof = root / 'agents/singularities_duality/part_base_four_comparison.tex'
assert proof.exists()
assert proof.read_text().count(r'\begin{saresult}{A.135}') == 1
assert 'one common collar' in proof.read_text()
assert 'extension data' in proof.read_text()
audits = ['notes/root_A135_base_four_comparison_audit.md',
          'agents/higher_comparison/A135_independent_audit.md']
for name in audits:
    assert (root/name).exists(), name

p = root/'parts/part_A.tex'
s = p.read_text()
anchor = r'\input{agents/singularities_duality/part_low_dim_TOP_comparison}'
addition = r'\input{agents/singularities_duality/part_base_four_comparison}'
assert s.count(anchor) == 1 and addition not in s
p.write_text(s.replace(anchor, anchor+'\n'+addition))

p = root/'parts/unchecked_A.tex'
s = p.read_text()
anchor = 'closed three- or four-manifold.\n'
assert s.count(anchor) == 1
addition = (
    'A.135 computes the comparison fibre with both cylinder ends fixed\n'
    'for every closed real PL four-manifold as\n'
    '$\\operatorname{Map}(B,K(\\mathbb Z/2,1))$. It gives a based\n'
    'homotopy-fibre sequence from this explicit space to the free-top\n'
    'comparison fibre and then to the ordinary base-automorphism\n'
    'comparison fibre. The latter space, connecting maps and extension\n'
    'data remain; this exact sequence is not a complete computation\n'
    'of the original free-top comparison.\n')
p.write_text(s.replace(anchor, anchor+addition))

p = root/'code/update_report.py'
lines = p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        line = line.replace('A.119–A.134|','A.119–A.135|')
        anchor = 'The general real comparison now remains only in base dimensions three and four.'
        assert anchor in line
        line = line.replace(anchor, anchor+' A.135 computes the fully boundary-fixed comparison fibre in base dimension four as Map(B,K(Z/2,1)) and gives an exact fibre sequence for the free-top comparison. The base-automorphism comparison and its connecting/extension data remain undetermined; the sequence is not a full free-top calculation.')
        lines[i] = line
p.write_text('\n'.join(lines)+'\n')

now = datetime.now(timezone.utc).isoformat()
record = {
    'statement':'A.135', 'recorded_utc':now,
    'where_proved':str(proof.relative_to(root)), 'audits':audits,
    'scope':'Closed real PL four-manifolds; ordinary jointly PL and continuous finite parameter families',
    'proved':'Both-end-fixed comparison fibre is Map(B,K(Z/2,1)); exact based fibre sequence to free-top comparison and base-automorphism comparison',
    'not_proved':'Full free-top comparison, connecting maps, extension data, or component surjectivity',
    'original_A1b_complete':False,
    'finite_counterexample_claimed':False,
    'early_progress_review_conducted':False
}
receipt.write_text(json.dumps(record,indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A.135\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: full proof, exact joint horn lift, common-collar weak comparison, relative structure orbit component, original KS universal square, two loop shifts and low-degree exact sequence; free-top extension data explicitly retained.\n')
    f.write('A.135\t'+now+'\tGPT-6 Astra, inherited configuration, higher_comparison2\ttargeted proof check\tPASS: independent full audit with original KS229/240/251/252/253 image inspection and241 text; common-collar and unevaluated-connecting-map clarifications incorporated.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A.135 integrated — '+now+'\n\n'
       'We have computed the PL-to-TOP comparison fibre for a closed real four-manifold cylinder with both ends fixed: it is Map(B,K(Z/2,1)). Top restriction gives an exact based fibre sequence into the free-top comparison fibre and then the ordinary four-manifold automorphism comparison fibre. The proof uses actual joint families, a uniform-collar conversion, the correct structure-space component and the original universal Kirby–Siebenmann square. Root and independent audits passed.\n\n'
       'The base-automorphism comparison, connecting maps and extension data remain unevaluated. No original parent task is marked complete. This integration is not a scheduled review and does not independently reset the stopping count. The next attack is to identify the connecting map through the boundary-collar structure diagram, with its precise dimension hypotheses.\n')
print(json.dumps(record,indent=2))

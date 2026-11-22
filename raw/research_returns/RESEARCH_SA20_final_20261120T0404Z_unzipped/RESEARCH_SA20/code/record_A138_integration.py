#!/usr/bin/env python3
"""Integrate the audited fixed-format method theorem without progress credit."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
receipt = root/'logs/A138_root_integration.json'
if receipt.exists():
    raise SystemExit('A138 integration already recorded')
proof = root/'agents/higher_comparison/part_finite_format_metric.tex'
assert proof.exists() and proof.read_text().count(r'\begin{saresult}{A.138}') == 1
audit = 'notes/root_A138_finite_format_audit.md'
assert (root/audit).exists()
p = root/'parts/part_A.tex'
s = p.read_text()
anchor = r'\input{agents/singularities_duality/part_base_four_component_image}'
addition = r'\input{agents/higher_comparison/part_finite_format_metric}'
assert s.count(anchor) == 1 and addition not in s
p.write_text(s.replace(anchor, anchor+'\n'+addition))

p = root/'parts/unchecked_A.tex'
s = p.read_text()
anchor = ('condition, or a class in the kernel of the map to TOP.\n')
addition = ('A.138 supplies local definable contractions inside any fixed finite\n'
            'formula format, using the uniform metric on maps and inverses.\n'
            'Its radius depends on the format, whereas improving a PL\n'
            'approximation can increase that format; the circular dependence\n'
            'is unresolved. Over a non-Archimedean field, finite PL maps\n'
            'cannot even approximate $x\\mapsto x^2$ to positive-infinitesimal\n'
            'accuracy. This method obstruction does not refute the homotopy\n'
            'comparison: that map is explicitly semialgebraically isotopic\n'
            'to the identity.\n')
assert s.count(anchor) == 1 and addition not in s
p.write_text(s.replace(anchor, anchor+addition))

p = root/'code/update_report.py'
lines = p.read_text().splitlines()
for i, line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        line = line.replace('A.119–A.137|', 'A.119–A.138|')
        anchor = 'Higher PL-to-SA/arbitrary-definable comparison remains unsettled.'
        addition = (' A.138 proves local uniform-metric contractions inside each fixed finite '
                    'formula format, but the varying-format radius problem remains. Its exact '
                    '1/(8m²) approximation bound rules out finite PL approximation of x² to '
                    'infinitesimal accuracy over non-Archimedean fields; the explicit isotopy '
                    'to the identity shows that this is a method obstruction, not a homotopy counterexample.')
        assert anchor in line
        lines[i] = line.replace(anchor, anchor+addition)
p.write_text('\n'.join(lines)+'\n')

now = datetime.now(timezone.utc).isoformat()
record = {'statement':'A.138', 'recorded_utc':now,
          'where_proved':str(proof.relative_to(root)), 'audit':audit,
          'scope':'Fixed finite definable formula formats over arbitrary o-minimal real closed fields',
          'proved':'Uniform forward/inverse metric affineness and local pointed contractions; exact quadratic PL error lower bound and infinitesimal obstruction',
          'actual_checker':'agents/higher_comparison/check_A138_metric.json',
          'checks':76, 'failures':0, 'elapsed_seconds':0.04335108300438151,
          'original_row_status_changed':False, 'qualifying_movement':False,
          'reason':'The comparison still lacks a bound controlling approximation complexity against the contraction radius.'}
receipt.write_text(json.dumps(record, indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A.138\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: original Walsberg affineness, all-fields compact graph-cell argument, relative open-star contraction, joint forward/inverse evaluation, exact midpoint bound and endpoint-fixed isotopy; method-only, original gate unchanged.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A.138 integrated as a method theorem — '+now+'\n\n'
        'Fixed finite formula-format homeomorphism spaces, with the uniform forward/inverse metric, are definably affine and locally pointed-contractible over every o-minimal real closed field. The exact quadratic approximation bound also shows that finite PL approximation to infinitesimal accuracy can fail over non-Archimedean fields, although the example is semialgebraically isotopic to the identity. The attached76-check certificate verifies only the stated finite algebraic identities and sharp examples.\n\n'
        'No original row changes and no main gate becomes strictly smaller: the contraction radius still depends on the approximation format. This result receives no qualifying movement credit and does not reset the scheduled stopping count.\n')
print(json.dumps(record, indent=2))

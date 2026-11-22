#!/usr/bin/env python3
"""Record the audited finite-format family lemma; do not claim gate closure."""
from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parents[1]
out=root/'logs/A5017_root_integration.json'
if out.exists():
    raise SystemExit('A5.017 integration already recorded')
proof='agents/maximal_locus/part_A5_uniform_surface_formats.tex'
audits=['notes/root_uniform_surface_format_audit.md',
        'agents/higher_comparison/A5_017_independent_audit.md']
assert (root/proof).exists()
assert r'\begin{saresult}{A5.017}' in (root/proof).read_text()
assert 'part_A5_uniform_surface_formats' in (root/'agents/maximal_locus/part_A5_method.tex').read_text()
for name in audits:
    assert (root/name).exists()
p=root/'parts/unchecked_A.tex'
s=p.read_text()
anchor='real closed field; the maximal-locus gate is unchanged.\n'
addition=('A5.017 supplies a single definable formula choosing arbitrarily\n'
          'close homeomorphisms for every member of a definable family of\n'
          'cell-like maps between fixed closed real surfaces. Its finite\n'
          'format follows from all-model scalar triangulation and logical\n'
          'compactness; it does not assert joint continuity of the choices.\n'
          'Continuous sewing across parameters and the general-field\n'
          'surface conclusion remain separate unproved steps.\n')
assert s.count(anchor)==1 and addition not in s
p.write_text(s.replace(anchor,anchor+addition))
p=root/'code/update_report.py'
lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('A.5 proper-map maximal locus and recursion|'):
        line=line.replace('A5.012–A5.016|','A5.012–A5.017|')
        anchor='so it receives no original-gate movement credit.'
        addition=(' A5.017 proves one finite definable format selecting arbitrarily close '
                  'homeomorphisms for every map in a real-definable family of cell-like '
                  'closed-surface maps. All-model scalar triangulation and logical '
                  'compactness yield the format bound; the selector need not be jointly '
                  'continuous. Continuous parameter sewing and the general-field surface '
                  'conclusion remain unproved; this lemma alone receives no original-gate '
                  'movement credit.')
        assert anchor in line
        lines[i]=line.replace(anchor,anchor+addition)
p.write_text('\n'.join(lines)+'\n')
now=datetime.now(timezone.utc).isoformat()
record={'statement':'A5.017','recorded_utc':now,'where_proved':proof,
        'audits':audits,'original_row_status_changed':False,
        'qualifying_movement':False,
        'remaining':'Joint continuous parameter sewing; arbitrary-RCF surface extension; full maximal bundle-locus gate'}
out.write_text(json.dumps(record,indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A5.017\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: full first-order certificates including ambient dimension, arbitrary-language compactness, all-model o-minimality, finite real PL pairs and collars, rational stellar choices, empty cases and definable error selection. No joint continuity or original-gate closure inferred.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A5.017 integrated without original-gate movement — '+now+'\n\n'
        'A single definable formula now selects arbitrarily close homeomorphisms for all members of a real-definable family of cell-like maps between fixed closed surfaces. The full proof uses all-model scalar triangulation to obtain finitely many certificate formats, then finitely many PL collars over the real field and a definable choice of the error scale. Root and an independent agent audited the complete argument. The selector need not be continuous in the parameters. Continuous sewing, the arbitrary-real-closed-field surface conclusion, and the original maximal-locus gate remain. No original-row status change or qualifying movement is claimed for this lemma alone.\n')
print(json.dumps(record,indent=2))

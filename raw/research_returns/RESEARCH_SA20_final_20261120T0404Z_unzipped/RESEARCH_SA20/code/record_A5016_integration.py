#!/usr/bin/env python3
"""Record the audited individual surface method result without movement credit."""
from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parents[1]
out=root/'logs/A5016_root_integration.json'
if out.exists():
    raise SystemExit('A5.016 integration already recorded')
proof='agents/maximal_locus/part_A5_surface_method.tex'
audit='notes/root_A5016_surface_collar_audit.md'
assert (root/proof).exists() and (root/audit).exists()
assert 'part_A5_surface_method' in (root/'agents/maximal_locus/part_A5_method.tex').read_text()
check=json.loads((root/'agents/maximal_locus/logs/check_surface_collar_parameter_fold.json').read_text())
assert check['status']=='PASS' and check['test_count']==21
p=root/'notes/root_references.bib'
s=p.read_text()
needle='The added A.121 locators were independently reopened by root.'
addition=' Root also reopened Lemma4.23 p.58, Theorem2.25 p.24 and the surface-classification remark following Theorem5.5 p.63 for A5.016.'
assert needle in s and addition not in s
p.write_text(s.replace(needle,needle+addition))
p=root/'parts/unchecked_A.tex'
s=p.read_text()
anchor='and canonical length maps. A5.011 refutes TOP axis-cancellation by an explicit\n'
replacement=('and canonical length maps. A5.016 proves coherent definable approximation\n'
             'for one real-definable cell-like map between closed surfaces, using\n'
             'a finite height-preserving PL collar. It does not give continuous\n'
             'dependence on extra parameters or extend that conclusion to every\n'
             'real closed field; the maximal-locus gate is unchanged.\n'
             'A5.011 refutes TOP axis-cancellation by an explicit\n')
assert anchor in s
p.write_text(s.replace(anchor,replacement))
p=root/'code/update_report.py'
lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('A.5 proper-map maximal locus and recursion|'):
        line=line.replace('A5.012–A5.015|','A5.012–A5.016|')
        anchor='it refutes a proposed method criterion, while leaving this original gate unchanged.'
        addition=(' A5.016 gives a finite height-preserving collar and coherent definable '
                  'homeomorphism approximation for one cell-like map between closed real '
                  'surfaces. Its extra-parameter and arbitrary-field extensions remain '
                  'unproved, so it receives no original-gate movement credit.')
        assert anchor in line
        lines[i]=line.replace(anchor,anchor+addition)
p.write_text('\n'.join(lines)+'\n')
now=datetime.now(timezone.utc).isoformat()
record={'statement':'A5.016','recorded_utc':now,'where_proved':proof,'audit':audit,
        'finite_checks':21,'finite_elapsed_seconds':check['elapsed_seconds'],
        'original_row_status_changed':False,'qualifying_movement':False,
        'remaining':'Joint dependence on additional parameters; arbitrary-RCF extension; full maximal bundle-locus gate'}
out.write_text(json.dumps(record,indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A5.016\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: full finite mixed-simplex leveling, direct3D links and surface doubling, actual Siebenmann endpoint family, scalar triangulation and definable inverse approximation; extra-parameter and arbitrary-field gaps retained.\n')
    f.write('A5.016\t'+now+'\tGPT-6 Astra, inherited configuration, root\tused and rechecked in this run\tRead complete21-check exact fold script/output: all PASS in '+str(check['elapsed_seconds'])+' seconds; certificate concerns finite algebra only, not a family collar theorem.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A5.016 integrated without original-gate movement — '+now+'\n\n'
        'We prove finite prescribed-height PL leveling over every real closed field and coherent definable homeomorphism approximation for one cell-like map between closed real surfaces. The direct3D link argument justifies the PL mapping-cylinder structure. A21-check exact certificate verifies the parameter-fold example that blocks an unrestricted parameter-preserving extension. The special positive-height-product family, continuous extra parameters, and arbitrary-field surface conclusion remain unproved. This is a method/special-model result; no original row or main gate changes and no stopping-count credit is assigned.\n')
print(json.dumps(record,indent=2))

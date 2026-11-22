#!/usr/bin/env python3
"""Integrate two audited method results, with no original-row movement credit."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
record_path = root / 'logs/integrate_A162_A5020.json'
assert not record_path.exists(), 'Integration is recorded once'
sources = {
    'agents/higher_comparison/part_RP3_equivariant_germs.tex': '2b56142c11d6d967f0d056c6a8f67e4205260204521129577d7c59efd369cbb9',
    'agents/maximal_locus/part_A5_polynomial_family.tex': 'b0ce89e514609f1101960201dede3eee18ef462bd141a1b2845a052f0a16fc8a',
}
for rel, digest in sources.items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest() == digest, rel
for rel in [
    'notes/root_A162_promoted_audit.md',
    'agents/singularities_duality/logs/A162_split_kernel_supplement_audit.md',
    'agents/singularities_duality/logs/Jelonek_sign_repair_independent_audit.md',
]:
    assert (root/rel).is_file(), rel
shutil.copy2(root/'RESEARCH_SA20_paper.pdf', '/tmp/RESEARCH_SA20_build32g_before33.pdf')
shutil.copy2(root/'logs/pdf_qa.json', root/'logs/pdf_qa_before_build33.json')

pending = (root/'agents/higher_comparison/A162_references_pending.bib').read_text()
bib = root/'notes/root_references.bib'
allbib = '\n'.join(p.read_text() for p in [bib, *sorted((root/'agents').glob('*/references.bib'))])
keys = re.findall(r'@\w+\s*\{\s*([^,]+),', pending)
assert len(keys) == 5
present = [bool(re.search(r'@\w+\s*\{\s*'+re.escape(key)+r'\s*,', allbib)) for key in keys]
assert all(present) or not any(present), 'Unexpected partial bibliography import'
if not any(present):
    bib.write_text(bib.read_text()+'\n\n'+pending+'\n')
else:
    assert pending in bib.read_text(), 'Imported text differs from the audited pending record'

part = root/'parts/new_concordance_results.tex'
text = part.read_text()
new = '\\input{agents/higher_comparison/part_RP3_equivariant_germs}\n'
assert '\\nocite{' in text
if new not in text:
    part.write_text(text.replace('\\nocite{', new+'\\nocite{', 1))
else:
    assert text.count(new) == 1
part = root/'parts/part_A.tex'
text = part.read_text()
old = '\\input{agents/maximal_locus/part_A5_radial_angular_gate}\n'
new = '\\input{agents/maximal_locus/part_A5_polynomial_family}\n'
assert text.count(old) == 1
if new not in text:
    part.write_text(text.replace(old, old+new))
else:
    assert text.count(new) == 1

checker = root/'agents/maximal_locus/code/check_A5_020_polynomial_family.py'
check_path = root/'logs/check_A5_020_root.json'
if check_path.exists():
    check = json.loads(check_path.read_text())
else:
    run = subprocess.run(['python3', str(checker)], cwd=root, capture_output=True, text=True, check=True)
    check = json.loads(run.stdout)
    check_path.write_text(run.stdout)
assert check['status'] == 'PASS' and check['exact_checks'] == 13

results = root/'notes/root_results.csv'
with results.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
new_row = {
    'id': 'A5.020',
    'statement': 'Proper degree-twelve real polynomial family: opposite signs are equivalent, positive parameters give pairwise inequivalent map types.',
    'status': 'Proved under stated hypotheses',
    'where_proved': 'agents/maximal_locus/part_A5_polynomial_family.tex',
    'depends_on': 'Jelonek2015 p2; elementary circle rotation conjugacy',
    'manuscript_pages': '',
    'notes': 'Complete root and independent literal proof audits; thirteen exact symbolic checks. Source correction and method obstruction only: no constant-fibre example, no maximal-bundle-locus counterexample, no qualifying movement.'
}
old_rows = [r for r in rows if r['id'] == 'A5.020']
if old_rows:
    assert old_rows == [new_row]
else:
    rows.append(new_row)
with results.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader(); writer.writerows(rows)
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode), root; inherited configuration'
events = [
    ('A.162', 'targeted full literal proof check', 'PASS: Complete promoted proof and natural A132 bridge read; exact split forgetful kernel and residual Casson-Sullivan sequence checked. '+sources['agents/higher_comparison/part_RP3_equivariant_germs.tex']+'; no image/kernel evaluation or qualifying movement.'),
    ('A5.020', 'targeted full literal proof check', 'PASS: Complete preserved proof and promoted additions read; unique circle fibre, intrinsic four-point boundary sheet, six rotation graphs and sign-qualified rotation invariant checked. '+sources['agents/maximal_locus/part_A5_polynomial_family.tex']+'; no A5 closure or qualifying movement.'),
    ('A5.020', 'computation or formal certificate', 'PASS: Complete symbolic checker read and rerun; all13 exact checks pass. Runtime '+str(check['runtime_seconds'])+' seconds; logs/check_A5_020_root.json. Algebra only, not a substitute for the topology proof.'),
]
check_events = (root/'notes/root_checks.tsv').read_text()
with (root/'notes/root_checks.tsv').open('a') as f:
    for ident, kind, outcome in events:
        if outcome not in check_events:
            f.write('\t'.join([ident, stamp, who, kind, outcome])+'\n')

report = root/'code/update_report.py'
text = report.read_text()
text = text.replace('A.119–A.161|', 'A.119–A.162|', 1)
needle = 'The explicit RP3 zero-CS⇒PL-image question, the comparison kernel, and whole general3D TOP model remain.'
replacement = needle+' A.162 gives a fully audited odd joint-germ fibre model, proves the RP3 component group abelian and identifies it with the split forgetting kernel. The PL image and the zero-CS quotient remain unevaluated; this structural reexpression is not movement credit.'
assert text.count(needle) == 1
text = text.replace(needle, replacement, 1)
lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith('A.5 proper-map maximal locus and recursion|'):
        lines[i] = line.replace('A5.012–A5.019|', 'A5.012–A5.020|')+' A5.020 repairs the cited real polynomial family: m and -m are equivalent, but positive parameters give pairwise inequivalent proper degree-twelve maps; the full proof and13 exact checks are recorded. Its fibre dimension jumps, so it does not settle the maximal local-triviality locus or the finite-certificate gate.'
        break
else:
    raise AssertionError('Missing A.5 row')
report.write_text('\n'.join(lines)+'\n')

record = {'utc': stamp, 'sources': sources, 'new_bib_keys': keys,
          'root_algebra_check': {'status': check['status'], 'checks': check['exact_checks'], 'runtime_seconds': check['runtime_seconds']},
          'qualifying_movement': False,
          'open_original_rows': ['A.1(b)', 'A.5', 'C.2(b)']}
record['recovery_note'] = 'The first execution completed proof/Bib/check imports and then stopped at an overly narrow A.5 row-name match before writing the report or this record. We corrected that match and resumed idempotently; no duplicate proof, reference, or audit event was added.'
record_path.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))

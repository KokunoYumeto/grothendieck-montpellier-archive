"""Integrate the four-audited global Brauer-zero reduction; no archive creation."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
manifest_path = root / 'parts/D/post16_research/integration_manifest_Brauer_zero_D.json'
manifest = json.loads(manifest_path.read_text())
rel = manifest['path']
source = (root / rel).read_text()
assert hashlib.sha256((root / rel).read_bytes()).hexdigest() == manifest['sha256']
assert set(manifest['audit_scope']) == {'root', 'B', 'C', 'D'}
assert all(e['status'] == 'PASS' for e in manifest['events'])
pattern = re.compile(r'\\begin\{(proposition|corollary|lemma|example|theorem)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
matches = list(pattern.finditer(source))
assert [m[3] for m in matches] == manifest['labels']
assert all(m[2].startswith('Proved:') for m in matches)
cols = ['id', 'statement', 'status', 'where_proved', 'depends_on', 'manuscript_pages', 'notes']
p = root / 'parts/D/results_D.csv'
with p.open() as f:
    rows = list(csv.DictReader(f))
known = {row['id'] for row in rows}
added = []
for m in matches:
    if m[3] in known:
        continue
    row = dict(id=m[3], statement=m[2].split(':', 1)[1].strip(), status='Proved',
               where_proved=rel + ': label ' + m[3],
               depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}', source)))),
               manuscript_pages='29/061,066',
               notes='Four complete actual-file audits. Global normal proper surface scope. Fixed tensor comparison and a quadratic cyclic atlas give q^(C r^2) for Brauer-zero PGL_r(F_q) classes with unbounded scalar centre, including nonzero Kummer lifting obstructions. This is one strict reduction of the main projective-representation gate; requested D.1, D.2(ii), and residual L8 remain open. Complete local punctures and nonzero Brauer classes are not covered by this packet.')
    rows.append(row)
    added.append(row['id'])
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)

p = root / 'parts/D/paper_D.tex'
s = p.read_text()
line = '\\input{' + rel + '}'
if line not in s:
    p.write_text(s + '\n' + line + '\n')

p = root / 'parts/D/references_D.bib'
s = p.read_text()
present = set(re.findall(r'@\w+\{([^,]+),', s))
keys = set(manifest['bibliography_keys'])
assert not (keys & present) or keys <= present, 'Partial duplicate bibliography merge'
if not keys <= present:
    bib = (root / manifest['bibliography']).read_text()
    assert hashlib.sha256(bib.encode()).hexdigest() == manifest['bibliography_sha256']
    p.write_text(s + '\n\n' + bib)

p = root / 'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
for event in manifest['events']:
    if event['label'] not in added:
        continue
    actor = '/root' if event['actor'] == 'root' else '/root/part_' + event['actor'].lower()
    events.append(dict(statement_id=event['label'], date=event['recorded_utc'],
                       who='GPT-6 Astra Pro; ' + actor + '; SA12 run1; effort setting not independently exposed',
                       type=event['kind'], outcome=event['status'] + ': ' + event['scope']))
if added:
    events.append(dict(statement_id='D:Brauer-zero-projective-representation-growth', date=now,
                       who='GPT-6 Astra Pro; /root; SA12 run1; effort setting not independently exposed',
                       type='supplemental complete primary-source read and final correction inspection',
                       outcome='PASS: at12:26UTC root freshly read retained Lieblich math/0511244v4, printed pp5–8, full Section2.2.2 and Proposition3.1.1.4 with Lemmas3.1.1.5,7,8,11,12 and their complete written proofs. The final module-regular-sequence terminology, Gamma-torsor reduction, source locators and exact scope were inspected. This supplements rather than retroactively changes the earlier root event.'))
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['statement_id', 'date', 'who', 'type', 'outcome'], delimiter='\t')
    w.writeheader()
    w.writerows(events)

p = root / 'parts/D/unresolved_D.tex'
s = p.read_text()
old = 'The constant is allowed to depend on that centre bound. Unbounded central\norder, alternating multiplicities, uncovered cross-characteristic Lie families'
new = 'The constant is allowed to depend on that centre bound. The later\nBrauer-zero theorem below removes this dependence for the stated global\nsurface projective representations with zero geometric Brauer class.\nUnbounded central order with nonzero Brauer class in that setting,\nalternating multiplicities, uncovered cross-characteristic Lie families'
if old in s:
    s = s.replace(old, new)
marker = '% Post-checkpoint16 Brauer-zero main-gate reduction'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{Unbounded scalar order with zero geometric Brauer class.}
Theorem~\ref{D:Brauer-zero-projective-representation-growth} proves
$q^{Cr^2}$ growth for all defining-characteristic
$\operatorname{PGL}_r(\mathbf F_q)$ representations of a fixed normal
proper surface original-boundary quotient whose geometric Brauer class
vanishes. Their Kummer lifting class need not vanish, and no bound on
the scalar-centre order is assumed. A fixed finite collection of line
bundles represents every prime-to-$p$ Picard quotient; scalar digits
replace the growing root by one-step Frobenius tensor cycles.
Lemmas and propositions~\ref{D:fixed-tensor-boundary-comparison} and
\ref{D:finite-tensor-cyclic-quadratic-atlas} supply the uniform boundary,
Euler, cohomology and Artinian quadratic-presentation estimates.
This is one strict reduction of the unbounded-centre projective gate:
only representations with nonzero geometric Brauer class remain in that
part of the global normal surface problem. It does not prove a
simple-product or general-crown conclusion for the residual classes.
Complete local punctures, nonnormal transfer of this new theorem,
the remaining cross-characteristic families and alternating
multiplicities require their separate arguments. General D.1,
D.2(ii) and residual L8 remain unresolved.
'''
p.write_text(s)

p = root / 'code/assemble.py'
s = p.read_text()
s = s.replace('projective linear or unitary families with unbounded natural centre, uncovered',
              'projective linear or unitary families with unbounded natural centre and nonzero geometric Brauer class in the newly covered global normal surface setting, uncovered')
paragraph = 'After review10, the fully audited Brauer-zero theorem supplies one strict reduction of the projective-representation gate. On a fixed normal proper surface with its original-divisor tame quotient, all PGL_r(F_q) conjugacy classes with zero geometric Brauer class have growth q^(C r^2), uniformly in rank, field and scalar-centre order. Nonzero Kummer lifting classes are permitted. Fixed Picard generators and bounded scalar digits feed a fixed-tensor Frobenius atlas, with complete boundary, Euler and Artinian arguments. The remaining global normal surface projective classes have nonzero geometric Brauer obstruction. This packet does not yet cover complete local punctures, nonnormal transfer, alternating multiplicities or general crowns, and does not close any requested row. The next scheduled formal review will compare this completed reduction with review10; review10 itself is unchanged.'
if paragraph not in s:
    s = s.replace("'','## Files and continuation','',", repr(paragraph) + ",\n'','## Files and continuation','',")
p.write_text(s)

record = dict(utc=now, labels=manifest['labels'], added_rows=len(added),
              files=[dict(path=rel, sha256=manifest['sha256'])],
              main_movement=True, main_reduction_count=1,
              reduction='Global normal proper-surface unbounded-centre defining-characteristic projective representations with zero geometric Brauer class now have q^(C r^2) conjugacy growth, even for nonzero Kummer lifting class. The residual part of this gate requires nonzero geometric Brauer class.',
              not_claimed=['general finite generation', 'complete-local version', 'nonnormal transfer', 'nonzero Brauer classes', 'general crowns'],
              requested_status_changes=[], requested_open=['general D.1', 'general D.2(ii)', 'residual L8'],
              formal_review_performed=False, archive_created=False)
(root / 'code/output/integrate_Brauer_zero_post16.json').write_text(json.dumps(record, indent=2) + '\n')
if added:
    with (root / 'PROGRESS_LEDGER.md').open('a') as f:
        f.write('\n\n## Post-review10 Brauer-zero projective reduction\n\nINCOMPLETE. Integrated at' + now + '. All four complete actual-file audits passed the three-unit packet. The theorem removes the unbounded scalar-centre order restriction for geometric Brauer-zero projective representations of a fixed normal proper surface original-boundary quotient; nonzero Kummer classes are allowed. This is one completed strict main-gate reduction. No requested row closes. It is recorded between scheduled reviews; the actual review10 record and its then-current no-movement counter remain unchanged until review11. No checkpoint is created by this integration.\n')
print(json.dumps(record, indent=2))

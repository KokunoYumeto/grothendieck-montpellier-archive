"""Apply one exactly audited correction; preserve its erroneous predecessor."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256((root / p).read_bytes()).hexdigest()
mp = 'parts/C/post29_research/correction_manifest_C_A_chain_finite_jet.json'
m = json.loads((root / mp).read_text())
assert sha(m['path']) == m['sha256']
assert sha(m['original']['path']) == m['original']['sha256']
assert sha(m['original']['snapshot']) == m['original']['snapshot_sha256']
assert set(m['audit_scope']) == {'root', 'B', 'C', 'D'}
for actor, audit in m['audit_scope'].items():
    assert audit['verdict'] == 'PASS'
    assert audit['candidate_sha256'] == m['sha256']
    assert sha(audit['record']) == audit['record_sha256']

now = datetime.now(timezone.utc).isoformat()
assert json.loads((root / 'code/output/formal_review20.json').read_text())['consecutive_no_movement_reviews'] == 1
out = root / 'code/output/integrate_A_chain_coordinate_correction.json'
assert not out.exists()
candidate = (root / m['path']).read_text()
edits = [
    ('% Separate post29 correction Candidate. Original fixed-coordinate text is preserved.',
     '% Four complete exact correction audits PASS. Original fixed-coordinate error and source are preserved.'),
    ('[Candidate: finite jets for transverse A-chain framings]',
     '[Proved: finite jets for transverse A-chain framings]'),
    ('[Candidate: a degree-linear total jet budget on A-blocks]',
     '[Proved: a degree-linear total jet budget on A-blocks]')
]
promoted = candidate
for old, new in edits:
    assert promoted.count(old) == 1
    promoted = promoted.replace(old, new)
reverse = promoted
for old, new in reversed(edits):
    assert reverse.count(new) == 1
    reverse = reverse.replace(new, old)
assert reverse == candidate

preserved = []
for old, new in [
    ('code/output/checkpoint30_source_freeze.json', 'code/output/checkpoint30_pre_coordinate_correction_source_freeze.json'),
    ('code/output/checkpoint30_preparation.json', 'code/output/checkpoint30_pre_coordinate_correction_preparation.json'),
    ('qa/checkpoint30_render.json', 'qa/checkpoint30_pre_coordinate_correction_render.json'),
    ('qa/checkpoint30_actual_inspection.json', 'qa/checkpoint30_pre_coordinate_correction_actual_inspection.json'),
    ('qa/pdf_verified_checkpoint30.json', 'qa/pdf_verified_checkpoint30_pre_coordinate_correction.json'),
    ('CHECKPOINT30_SCOPE.md', 'code/output/CHECKPOINT30_pre_coordinate_correction_SCOPE.source.txt'),
    ('code/freeze_checkpoint30.py', 'code/output/freeze_checkpoint30_pre_coordinate_correction.source.txt'),
    ('code/verify_checkpoint30.py', 'code/output/verify_checkpoint30_pre_coordinate_correction.source.txt')
]:
    assert not (root / new).exists()
    shutil.copy2(root / old, root / new)
    preserved.append({'original_path': old, 'preserved_path': new, 'sha256': sha(new)})
shutil.copy2(root / 'build/RESEARCH_SA12_paper.pdf', '/tmp/SA12_build194_pre_coordinate_correction.pdf')
(root / 'code/output/checkpoint30_source_freeze.json').unlink()
(root / m['original']['path']).write_text(promoted)

rp = root / 'parts/D/results_D.csv'
with rp.open() as f:
    reader = csv.DictReader(f)
    cols = reader.fieldnames
    rows = list(reader)
changed = 0
for row in rows:
    if row['id'] in m['labels']:
        row['notes'] += (' Correction at22:10UTC: intrinsic maximal-ideal jets replace the false preassigned-w formula; '
                         'an explicit all-characteristic adapted-coordinate proof preserves all bounds. '
                         'Four exact correction audits and the complete original source are retained in '
                         'parts/C/post29_research/correction_manifest_C_A_chain_finite_jet.json. No new statement or movement.')
        changed += 1
assert changed == 2
with rp.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)

ep = root / 'parts/D/CHECK_EVENTS_D.tsv'
with ep.open() as f:
    reader = csv.DictReader(f, delimiter='\t')
    ecols = reader.fieldnames
    events = list(reader)
for label in m['labels']:
    for actor, audit in m['audit_scope'].items():
        events.append(dict(zip(ecols, [
            label, now, 'GPT-6 Astra Pro; ' + ('/root' if actor == 'root' else '/root/part_' + actor.lower()) + '; effort setting not independently exposed',
            'targeted proof check',
            'CORRECTION PASS on exact candidate ' + m['sha256'] + ': ' + audit['scope'] +
            ' Source scope: ' + audit['source_scope'] + ' Record: ' + audit['record'] +
            '. Original fixed-coordinate counterexample and historical audits retained. Intrinsic jets and all existing numerical bounds preserved; no movement.'
        ])))
with ep.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=ecols, delimiter='\t')
    w.writeheader()
    w.writerows(events)

ap = root / 'code/assemble.py'
lines = ap.read_text().splitlines(keepends=True)
summary = ('The earlier A-chain finite-jet proposition has a substantive coordinate correction. '
           'A preassigned w can vanish on an endpoint branch; the theorem now uses intrinsic maximal-ideal jets '
           'and proves one adapted standard coordinate choice in every characteristic. '
           'All four exact correction audits pass, the numerical bounds and Artinian companion remain valid, '
           'and the original source and mistaken inference are retained. This is not main-gate movement.')
for i, line in enumerate(lines):
    if line.startswith("'Post-checkpoint29 auxiliary integration:"):
        lines.insert(i + 1, repr(summary) + ',\n')
        break
else:
    raise AssertionError('Auxiliary report insertion anchor absent')
ap.write_text(''.join(lines))
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## A-chain coordinate correction\n\nINCOMPLETE. ' + now + '. ' + summary + '\n')
record = dict(utc=now, manifest=mp, manifest_sha256=sha(mp),
              original=m['original'], audited_candidate=m['audited_candidate'],
              integrated_path=m['original']['path'], integrated_sha256=sha(m['original']['path']),
              status_comment_replacements=[{'old': old, 'new': new} for old, new in edits],
              exact_status_reversal_verified=True, preserved_pre_correction_QA=preserved,
              previous_pdf_sha256=hashlib.sha256(Path('/tmp/SA12_build194_pre_coordinate_correction.pdf').read_bytes()).hexdigest(),
              audit_records=m['audit_scope'], new_statement_rows=0, appended_check_events=8,
              requested_status_changes=[], strict_main_gate_reductions=[], movement=False,
              note='Existing manuscript input replaced after all four exact audits. Full prior image files remain in qa; new inspection will use a separate corrected prefix. No archive created.')
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'integrated_path': record['integrated_path'], 'sha256': record['integrated_sha256'],
                  'new_statements': 0, 'new_correction_events': 8, 'movement': False}))

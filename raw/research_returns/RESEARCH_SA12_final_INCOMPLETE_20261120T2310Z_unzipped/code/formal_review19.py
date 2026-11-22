"""Perform review19 no earlier than21:10UTC against the exact staged assessment."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

root = Path(__file__).resolve().parents[1]
due = datetime(2026, 11, 20, 21, 10, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= due, 'Review19 is not due.'
out = root / 'code/output/formal_review19.json'
assert not out.exists(), 'Review19 already recorded.'
prior = json.loads((root / 'code/output/formal_review18.json').read_text())
a = json.loads((root / 'code/output/review19_main_assessment.json').read_text())
assert a['assessment_actor'] == 'root'
for info in a['verified_files']:
    assert hashlib.sha256((root / info['path']).read_bytes()).hexdigest() == info['sha256'], info['path']
    for audit in info['audit_records']:
        assert hashlib.sha256((root / audit['path']).read_bytes()).hexdigest() == audit['sha256'], audit['path']
movement = bool(a['strict_main_gate_reductions'] or a['requested_status_changes'])
assert movement == a['movement'] and a['all_required_proof_audits_completed']
counter = 0 if movement else prior['consecutive_no_movement_reviews'] + 1
stop = counter >= 2
qa = json.loads((root / 'qa/pdf_verified.json').read_text())
archive = json.loads((root / 'code/output/checkpoint27_archive_verification.json').read_text())
saved = json.loads((root / 'code/output/checkpoint27_saved_receipt.json').read_text())
assert archive['full_crc'] == archive['all_manifest_hashes'] == 'PASS'
assert saved['saved_result']['status'] == 'succeeded'
r = dict(
    review_number=19, scheduled_utc=due.isoformat(), actual_utc=now.isoformat(),
    preceding_review_actual_utc=prior['actual_utc'], requested_status_changes=a['requested_status_changes'],
    requested_open=a['requested_open'], movement=movement, consecutive_no_movement_reviews=counter,
    strict_main_gate_reductions=a['strict_main_gate_reductions'], remaining_strongest_gates=a['remaining_strongest_gates'],
    auxiliary_not_movement=a['auxiliary_not_movement'], assessment=a,
    latest_created_and_verified_checkpoint=27, latest_confirmed_persistently_saved_checkpoint=27,
    checkpoint27_delivery_status='Verified, persistently saved, native ZIP link delivered at20:26UTC.',
    latest_completed_visual_verification={key: qa[key] for key in ['build', 'pages', 'sha256']},
    stopping_condition_met=stop, next_review_utc=None if stop else '2026-11-20T22:10:00+00:00',
    scheduled_checkpoint_now=28, next_scheduled_checkpoint_utc=None if stop else '2026-11-20T21:55:00+00:00',
    note=('Two consecutive reviews without movement require research to stop and the final INCOMPLETE package to be prepared.' if stop else 'The completed bounded-period enlargement is one grouped strict main-gate reduction; research continues.')
)
out.write_text(json.dumps(r, indent=2) + '\n')
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Formal review19:20 November2026,21:10UTC\n\nINCOMPLETE. Actual review:' + now.isoformat() + '.\n\n')
    for text in a['strict_main_gate_reductions'] + a['auxiliary_not_movement']:
        f.write(text + '\n\n')
    f.write('Movement:' + ('YES' if movement else 'NO') + '. Consecutive no-movement reviews:' + str(counter) + '. ' + r['note'] + ' Exact requested rows and remaining strongest gates are recorded in code/output/formal_review19.json.\n')
p = root / 'code/assemble.py'
lines = p.read_text().splitlines(keepends=True)
summary = 'Formal review19 was completed during the scheduled21:10UTC period. ' + a['report_summary'] + ' Consecutive no-movement reviews:' + str(counter) + '. ' + r['note'] + ' Exact comparison is in code/output/formal_review19.json. General D.1, general D.2(ii), and residual L8 remain unresolved. Checkpoint28 is being created at this scheduled slot; the next checkpoint is21:55UTC and review20 is22:10UTC.'
for i, line in enumerate(lines):
    if line.startswith("'Formal review18 was completed"):
        lines[i] = repr(summary) + ',\n'
        break
else:
    raise AssertionError('Review18 summary missing.')
p.write_text(''.join(lines))
print(json.dumps(dict(review=19, actual_utc=now.isoformat(), movement=movement,
                     consecutive_no_movement_reviews=counter, stopping_condition_met=stop)))

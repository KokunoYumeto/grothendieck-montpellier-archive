"""Perform review18 no earlier than20:10UTC against the exact staged assessment."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

root = Path(__file__).resolve().parents[1]
due = datetime(2026, 11, 20, 20, 10, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= due, 'Review18 is not due.'
out = root / 'code/output/formal_review18.json'
assert not out.exists(), 'Review18 already recorded.'
prior = json.loads((root / 'code/output/formal_review17.json').read_text())
a = json.loads((root / 'code/output/review18_main_assessment.json').read_text())
assert a['assessment_actor'] == 'root'
for info in a['verified_files']:
    assert hashlib.sha256((root / info['path']).read_bytes()).hexdigest() == info['sha256'], info['path']
movement = bool(a['strict_main_gate_reductions'] or a['requested_status_changes'])
assert movement == a['movement']
assert a['all_required_proof_audits_completed']
counter = 0 if movement else prior['consecutive_no_movement_reviews'] + 1
stop = counter >= 2
qa = json.loads((root / 'qa/pdf_verified.json').read_text())
archive = json.loads((root / 'code/output/checkpoint26_archive_verification.json').read_text())
delivery = json.loads((root / 'code/output/checkpoint26_delivery_receipt.json').read_text())
assert archive['full_crc'] == archive['all_manifest_hashes'] == 'PASS'
saved_path = root / 'code/output/checkpoint26_saved_receipt.json'
latest_saved = 26 if saved_path.exists() and json.loads(saved_path.read_text()).get('status') == 'succeeded' else 25
r = dict(
    review_number=18, scheduled_utc=due.isoformat(), actual_utc=now.isoformat(),
    preceding_review_actual_utc=prior['actual_utc'],
    requested_status_changes=a['requested_status_changes'], requested_open=a['requested_open'],
    movement=movement, consecutive_no_movement_reviews=counter,
    strict_main_gate_reductions=a['strict_main_gate_reductions'],
    remaining_strongest_gates=a['remaining_strongest_gates'],
    auxiliary_not_movement=a['auxiliary_not_movement'], assessment=a,
    latest_created_and_verified_checkpoint=26,
    latest_confirmed_persistently_saved_checkpoint=latest_saved,
    checkpoint26_delivery_status=delivery,
    latest_completed_visual_verification={key: qa[key] for key in ['build', 'pages', 'sha256']},
    stopping_condition_met=stop,
    next_review_utc=None if stop else '2026-11-20T21:10:00+00:00',
    scheduled_checkpoint_now=None,
    next_scheduled_checkpoint_utc=None if stop else '2026-11-20T20:25:00+00:00',
    note=('Two consecutive reviews without movement require research to stop and the final INCOMPLETE package to be prepared.' if stop else 'Completed strict main-gate reductions are grouped by their actual consequences; research continues.')
)
out.write_text(json.dumps(r, indent=2) + '\n')
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Formal review18:20 November2026,20:10UTC\n\nINCOMPLETE. Actual review:' + now.isoformat() + '.\n\n')
    for x in a['strict_main_gate_reductions'] + a['auxiliary_not_movement']:
        f.write(x + '\n\n')
    f.write('Movement:' + ('YES' if movement else 'NO') + '. Consecutive no-movement reviews:' + str(counter) + '. ' + r['note'] + ' Exact requested rows and strongest remaining gates are recorded in code/output/formal_review18.json.\n')
p = root / 'code/assemble.py'
lines = p.read_text().splitlines(keepends=True)
summary = 'Formal review18 was completed during the scheduled20:10UTC period. ' + a['report_summary'] + ' Consecutive no-movement reviews:' + str(counter) + '. ' + r['note'] + ' Exact comparison is in code/output/formal_review18.json. General D.1, general D.2(ii), and residual L8 remain unresolved. Checkpoint26 is the latest created and delivered archive; checkpoint27 is scheduled20:25UTC.'
for i, line in enumerate(lines):
    if line.startswith("'Formal review17 was completed"):
        lines[i] = repr(summary) + ',\n'
        break
else:
    raise AssertionError('Review17 summary missing.')
p.write_text(''.join(lines))
print(json.dumps(dict(review=18, actual_utc=now.isoformat(), movement=movement,
                     consecutive_no_movement_reviews=counter, stopping_condition_met=stop)))

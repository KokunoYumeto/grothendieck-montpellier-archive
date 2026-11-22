"""Perform formal review20 only when due, using a separately staged root assessment."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
due = datetime(2026, 11, 20, 22, 10, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= due, 'Review20 is not due.'
out = root / 'code/output/formal_review20.json'
assert not out.exists(), 'Review20 already recorded.'
prior = json.loads((root / 'code/output/formal_review19.json').read_text())
a = json.loads((root / 'code/output/review20_main_assessment.json').read_text())
assert a['assessment_actor'] == 'root'
assert a['comparison_review'] == 19
assert a['all_required_proof_audits_completed']
for info in a['verified_files']:
    assert hashlib.sha256((root / info['path']).read_bytes()).hexdigest() == info['sha256'], info['path']
    for audit in info.get('audit_records', []):
        assert hashlib.sha256((root / audit['path']).read_bytes()).hexdigest() == audit['sha256'], audit['path']
movement = bool(a['strict_main_gate_reductions'] or a['requested_status_changes'])
assert movement == a['movement']
counter = 0 if movement else prior['consecutive_no_movement_reviews'] + 1
stop = counter >= 2
qa = json.loads((root / 'qa/pdf_verified.json').read_text())
latest_verified = a['latest_verified_checkpoint']
latest_saved = a['latest_confirmed_saved_checkpoint']
archive = json.loads((root / f'code/output/checkpoint{latest_verified}_archive_verification.json').read_text())
saved = json.loads((root / f'code/output/checkpoint{latest_saved}_saved_receipt.json').read_text())
assert archive['full_crc'] == archive['all_manifest_hashes'] == 'PASS'
assert saved['saved_result']['status'] == 'succeeded'
r = dict(
    review_number=20, scheduled_utc=due.isoformat(), actual_utc=now.isoformat(),
    preceding_review_actual_utc=prior['actual_utc'],
    requested_status_changes=a['requested_status_changes'], requested_open=a['requested_open'],
    movement=movement, consecutive_no_movement_reviews=counter,
    strict_main_gate_reductions=a['strict_main_gate_reductions'],
    remaining_strongest_gates=a['remaining_strongest_gates'],
    auxiliary_not_movement=a['auxiliary_not_movement'], assessment=a,
    latest_created_and_verified_checkpoint=latest_verified,
    latest_confirmed_persistently_saved_checkpoint=latest_saved,
    latest_completed_visual_verification={key: qa[key] for key in ['build', 'pages', 'sha256']},
    stopping_condition_met=stop,
    next_review_utc=None if stop else '2026-11-20T23:10:00+00:00',
    next_scheduled_checkpoint_utc=None if stop else '2026-11-20T22:40:00+00:00',
    note=('Two consecutive formal reviews without movement require research to stop and a separate final INCOMPLETE ZIP to be prepared.'
          if stop else 'Research continues under the two-consecutive-review stopping rule.')
)
out.write_text(json.dumps(r, indent=2) + '\n')
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Formal review20:20 November2026,22:10UTC\n\nINCOMPLETE. Actual review:' + now.isoformat() + '.\n\n')
    for item in a['strict_main_gate_reductions'] + a['auxiliary_not_movement']:
        f.write(item + '\n\n')
    f.write('Movement:' + ('YES' if movement else 'NO') + '. Consecutive no-movement reviews:' + str(counter) + '. ' + r['note'] + '\n')
p = root / 'code/assemble.py'
lines = p.read_text().splitlines(keepends=True)
summary = ('Formal review20 was completed during the scheduled22:10UTC period. '
           + a['report_summary'] + ' Consecutive no-movement reviews:' + str(counter) + '. '
           + r['note'] + ' Exact comparison is in code/output/formal_review20.json. '
           + 'General D.1, general D.2(ii), and residual L8 remain unresolved. '
           + f'Checkpoint{latest_verified} is the latest verified archive; checkpoint{latest_saved} is the latest confirmed saved archive. Checkpoint28 remains absent with its failed-slot record. '
           + ('The next checkpoint is22:40UTC and review21 is23:10UTC.' if not stop else 'A separate final ZIP is required.'))
for i, line in enumerate(lines):
    if line.startswith("'Formal review19 was completed"):
        lines[i] = repr(summary) + ',\n'
        break
else:
    raise AssertionError('Review19 summary missing.')
p.write_text(''.join(lines))
print(json.dumps(dict(review=20, actual_utc=now.isoformat(), movement=movement,
                     consecutive_no_movement_reviews=counter, stopping_condition_met=stop)))

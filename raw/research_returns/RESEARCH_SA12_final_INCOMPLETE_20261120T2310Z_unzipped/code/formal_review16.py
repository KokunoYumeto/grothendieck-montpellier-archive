"""Perform scheduled review16 against an explicit, hash-checked assessment."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1]
due=datetime(2026,11,20,18,10,tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
assert now>=due,'Review16 is not due.'
out=root/'code/output/formal_review16.json'
assert not out.exists(),'Review16 already recorded.'
prior=json.loads((root/'code/output/formal_review15.json').read_text())
a=json.loads((root/'code/output/review16_main_assessment.json').read_text())
assert a['assessment_actor']=='root'
for info in a.get('verified_files',[]):
 assert hashlib.sha256((root/info['path']).read_bytes()).hexdigest()==info['sha256'],info['path']
movement=bool(a['strict_main_gate_reductions'] or a['requested_status_changes'])
assert movement==a['movement']
if movement:
 assert a['verified_files'] and a['all_required_proof_audits_completed']
 gates=a['remaining_strongest_gates'];counter=0
else:
 gates=prior['remaining_strongest_gates'];counter=prior['consecutive_no_movement_reviews']+1
stop=counter>=2
qa=json.loads((root/'qa/pdf_verified.json').read_text())
receipt=json.loads((root/'code/output/checkpoint23_saved_receipt.json').read_text())
assert receipt['status']=='succeeded'
r={'review_number':16,'scheduled_utc':due.isoformat(),'actual_utc':now.isoformat(),
 'preceding_review_actual_utc':prior['actual_utc'],
 'requested_status_changes':a['requested_status_changes'],
 'requested_open':a.get('requested_open',prior['requested_open']),
 'movement':movement,'consecutive_no_movement_reviews':counter,
 'strict_main_gate_reductions':a['strict_main_gate_reductions'],
 'remaining_strongest_gates':gates,'auxiliary_not_movement':a['auxiliary_not_movement'],
 'assessment':a,'latest_successful_checkpoint':23,
 'latest_completed_visual_verification':{'build':qa['build'],'pages':qa['pages'],'sha256':qa['sha256']},
 'stopping_condition_met':stop,
 'next_review_utc':None if stop else '2026-11-20T19:10:00+00:00',
 'scheduled_checkpoint_now':24,
 'next_scheduled_checkpoint_utc':None if stop else '2026-11-20T18:55:00+00:00',
 'note':'Two consecutive reviews without movement require research to stop and the final INCOMPLETE package to be prepared.' if stop else 'Completed strict main-gate reductions are counted once; research continues.'}
out.write_text(json.dumps(r,indent=2)+'\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Formal review16:20 November2026,18:10UTC\n\nINCOMPLETE. Actual review:'+now.isoformat()+'.\n\n')
 for x in a['strict_main_gate_reductions']+a['auxiliary_not_movement']:f.write(x+'\n\n')
 f.write('Movement:'+('YES' if movement else 'NO')+'. Consecutive no-movement reviews:'+str(counter)+'. '+r['note']+' Exact requested rows and strongest remaining gates are recorded in code/output/formal_review16.json.\n')
p=root/'code/assemble.py';lines=p.read_text().splitlines(keepends=True)
summary='Formal review16 was completed during the scheduled18:10UTC period. '+a['report_summary']+' Consecutive no-movement reviews:'+str(counter)+'. '+r['note']+' Exact comparison is in code/output/formal_review16.json. General D.1, general D.2(ii), and residual L8 remain unresolved unless explicitly changed there. Checkpoint23 is the most recent saved archive at review time; scheduled checkpoint24 follows this review at18:10UTC.'
for i,line in enumerate(lines):
 if line.startswith("'Formal review15 was completed"):
  lines[i]=repr(summary)+',\n';break
else:raise AssertionError('Review14 summary missing.')
p.write_text(''.join(lines))
print(json.dumps({'review':16,'actual_utc':now.isoformat(),'movement':movement,
 'consecutive_no_movement_reviews':counter,'stopping_condition_met':stop}))

"""Perform scheduled review13 against an explicit, hash-checked assessment."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1];due=datetime(2026,11,20,15,10,tzinfo=timezone.utc);now=datetime.now(timezone.utc)
assert now>=due,'Review13 is not due.'
out=root/'code/output/formal_review13.json';assert not out.exists(),'Review13 already recorded.'
prior=json.loads((root/'code/output/formal_review12.json').read_text())
a=json.loads((root/'code/output/review13_main_assessment.json').read_text())
assert a['assessment_actor']=='root'
for info in a.get('verified_files',[]):assert hashlib.sha256((root/info['path']).read_bytes()).hexdigest()==info['sha256'],info['path']
movement=bool(a['strict_main_gate_reductions'] or a['requested_status_changes'])
assert movement==a['movement']
if movement:
 assert a['verified_files'] and a['all_required_proof_audits_completed']
 gates=a['remaining_strongest_gates'];counter=0
else:
 gates=prior['remaining_strongest_gates'];counter=prior['consecutive_no_movement_reviews']+1
stop=counter>=2
qa=json.loads((root/'qa/pdf_verified.json').read_text());receipt=json.loads((root/'code/output/checkpoint19_saved_receipt.json').read_text());assert receipt['status']=='succeeded'
r={'review_number':13,'scheduled_utc':due.isoformat(),'actual_utc':now.isoformat(),'preceding_review_actual_utc':prior['actual_utc'],'requested_status_changes':a['requested_status_changes'],'requested_open':a.get('requested_open',prior['requested_open']),'movement':movement,'consecutive_no_movement_reviews':counter,'strict_main_gate_reductions':a['strict_main_gate_reductions'],'remaining_strongest_gates':gates,'auxiliary_not_movement':a['auxiliary_not_movement'],'assessment':a,'latest_successful_checkpoint':19,'latest_completed_visual_verification':{'build':qa['build'],'pages':qa['pages'],'sha256':qa['sha256']},'stopping_condition_met':stop,'next_review_utc':None if stop else '2026-11-20T16:10:00+00:00','scheduled_checkpoint_now':20,'next_scheduled_checkpoint_utc':None if stop else '2026-11-20T15:55:00+00:00','note':'Two consecutive reviews without movement require research to stop and the final INCOMPLETE package to be prepared.' if stop else 'A completed strict main-gate reduction is recorded exactly once; research continues.'}
out.write_text(json.dumps(r,indent=2)+'\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Formal review13: 20 November2026,15:10UTC\n\nINCOMPLETE. Actual review:'+now.isoformat()+'.\n\n')
 for x in a['strict_main_gate_reductions']:f.write(x+'\n\n')
 for x in a['auxiliary_not_movement']:f.write(x+'\n\n')
 f.write('Movement:'+('YES' if movement else 'NO')+'. Consecutive no-movement reviews:'+str(counter)+'. '+r['note']+' All requested open rows and strongest gates remain explicitly recorded in code/output/formal_review13.json. The15:10UTC checkpoint20 is created separately after this review.\n')
p=root/'code/assemble.py';lines=p.read_text().splitlines(keepends=True)
summary='Formal review13 was completed during the scheduled15:10UTC period. '+a['report_summary']+' Consecutive no-movement reviews:'+str(counter)+'. '+r['note']+' Exact comparison is in code/output/formal_review13.json. General D.1, general D.2(ii), and residual L8 remain unresolved unless an explicit requested-status change is recorded there. The scheduled checkpoint20 follows this review; checkpoint19 is the most recent saved archive at review time.'
for i,line in enumerate(lines):
 if line.startswith("'Formal review12 was completed"):
  lines[i]=repr(summary)+',\n';break
else:raise AssertionError('Review12 summary missing.')
p.write_text(''.join(lines));print(json.dumps({'review':13,'actual_utc':now.isoformat(),'movement':movement,'consecutive_no_movement_reviews':counter,'stopping_condition_met':stop}))

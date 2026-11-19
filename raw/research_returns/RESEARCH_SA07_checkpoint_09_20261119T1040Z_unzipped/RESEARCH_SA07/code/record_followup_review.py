#!/usr/bin/env python3
"""Record an actual, due hourly review from an explicit proof-based assessment.

This utility computes status differences but never infers mathematical progress.
The root reviewer supplies the assessment after comparing the proved gates.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import csv, json, sys

ROOT=Path(__file__).resolve().parent.parent
assessment=json.loads(Path(sys.argv[1]).read_text())
state_path=ROOT/'PROGRESS_REVIEW_STATE.json'
prior=json.loads(state_path.read_text())
now=datetime.now(timezone.utc)
due=datetime.fromisoformat(prior['next_due_utc'])
assert now>=due, 'The next timed review is not due yet'
assert prior['review_number']==assessment['previous_review_number']
number=prior['review_number']+1
rows=list(csv.DictReader((ROOT/'audit_claims.csv').open()))
current={r['assertion_id']:r['status'] for r in rows}
assert set(current)==set(prior['assertion_states']), 'Inventory changed: inspect before reviewing'
changes=[[k,prior['assertion_states'][k],v] for k,v in current.items() if prior['assertion_states'][k]!=v]
assert changes==assessment['expected_status_changes'], 'Actual status changes require a fresh assessment'
gates=assessment['main_gates']
assert set(gates)==set(prior['main_gates']), 'Every main question must be reviewed'
movement=assessment['movement']
assert type(movement) is bool
assert assessment['reasoning'], 'The explicit progress judgment must be explained'
if not movement:
 assert not changes, 'Changed assertion status requires explicit evaluation before a no-movement review'
streak=0 if movement else prior['consecutive_no_movement']+1
next_due=due+timedelta(hours=1)
counts={}
for row in rows:counts[row['status']]=counts.get(row['status'],0)+1
berlin=now.astimezone(ZoneInfo('Europe/Berlin')).strftime('%d %B %Y %H:%M:%S')
lines=['',f'## Timed review {number:02d} — {berlin} Europe/Berlin','',
 f'Actual review time: {now.isoformat()}. Previous actual review: {prior["actual_utc"]}. This is an actual due review, not a projected future review.','',
 f'**Movement: {"YES" if movement else "NO"}. Consecutive timed reviews without movement: {streak}.**','',assessment['reasoning'],'',
 '### Assertion-state comparison','',
 'Counts: '+', '.join(f'{k}={v}' for k,v in sorted(counts.items()))+'.']
if changes:
 lines+=['','| Assertion | Previous state | Current state |','|---|---|---|']
 for a,b,c in changes:lines.append(f'| {a} | {b} | {c} |')
else:lines+=['','All 307 canonical assertion statuses are unchanged from the preceding timed review.']
lines+=['','### Main questions and strongest proved gates','',
 '| Main question | Current gate and the scope of the intervening results |','|---|---|']
for key,value in gates.items():lines.append(f'| {key} | {value.replace(chr(10)," ").replace("|","/")} |')
lines+=['','### Every unresolved or retained-reading assertion','',
 '| Assertion | State | Exact obligation or retained reading |','|---|---|---|']
for row in rows:
 if row['status'] in {'OPEN','READING','DOCUMENTARY-GAP'}:
  note=row['remaining_obligation_or_scope'].replace('|','/').replace('\n',' ')
  lines.append(f'| {row["assertion_id"]} | {row["status"]} | {note} |')
stop=streak>=2
if stop:
 lines+=['','The two-consecutive-no-movement rule has now been met. Stop the research work and prepare the final package with every item state retained.','']
else:
 lines+=['',f'Next timed review due {next_due.strftime("%H:%M UTC")} ({next_due.astimezone(ZoneInfo("Europe/Berlin")).strftime("%H:%M Berlin")}). The two-consecutive-no-movement rule has not been met; continue the unresolved work.','']
history=ROOT/'review_records';history.mkdir(exist_ok=True)
prior_file=history/f'review_{prior["review_number"]:02d}_state.json'
if not prior_file.exists():prior_file.write_text(json.dumps(prior,indent=2)+'\n')
new={'review_number':number,'actual_utc':now.isoformat(),'movement':movement,
 'consecutive_no_movement':streak,'next_due_utc':next_due.isoformat(),
 'counts':counts,'changed_rows_since_previous_review':changes,
 'main_gates':gates,'assertion_states':current,'reasoning':assessment['reasoning'],
 'stop_rule_reached':stop}
new_file=history/f'review_{number:02d}_state.json'
assert not new_file.exists(), 'This review was already recorded'
with (ROOT/'PROGRESS_LEDGER.md').open('a') as file:file.write('\n'.join(lines))
new_file.write_text(json.dumps(new,indent=2)+'\n')
state_path.write_text(json.dumps(new,indent=2)+'\n')
with (ROOT/'RESEARCH_SA07_report.md').open('a') as file:
 file.write(f'\n\n## Timed review {number:02d} — {berlin} Europe/Berlin\n\n')
 file.write(assessment['reasoning']+'\n\n')
 file.write(f'Movement: {"YES" if movement else "NO"}. Consecutive timed reviews without movement: {streak}. ')
 file.write('The full current unresolved-row inventory and every main gate are recorded in PROGRESS_LEDGER.md. ')
 file.write('The stopping rule is now met; prepare the final package.\n' if stop else f'The next timed review is due at {next_due.astimezone(ZoneInfo("Europe/Berlin")).strftime("%H:%M Berlin")}; continue the research.\n')
print(json.dumps({k:new[k] for k in ['review_number','actual_utc','movement','consecutive_no_movement','next_due_utc','stop_rule_reached']}))

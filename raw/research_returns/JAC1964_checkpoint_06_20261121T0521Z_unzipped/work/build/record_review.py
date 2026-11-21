"""Record a due hourly movement review with explicit human/model judgment.

Text changes and new side findings are reported but never automatically
classified as movement.  The caller supplies the exact mathematical reason.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse, csv, json, time

R=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser()
p.add_argument('--movement',choices=['yes','no'],required=True)
p.add_argument('--reason',required=True)
p.add_argument('--wait',action='store_true')
a=p.parse_args()
state_path=R/'documentation/REVIEW_STATE.json'
state=json.loads(state_path.read_text())
due=datetime.fromisoformat(state['next_review_utc'])
now=datetime.now(timezone.utc)
if now<due and not a.wait:raise SystemExit('Review not due: '+due.isoformat())
while datetime.now(timezone.utc)<due:
    time.sleep(min(30,max(.01,(due-datetime.now(timezone.utc)).total_seconds())))
now=datetime.now(timezone.utc)
if now>=due+timedelta(hours=1):raise SystemExit('Missed review interval; inspect ledger.')
rows=list(csv.DictReader((R/'deliverables/QUESTIONS.tsv').open(),delimiter='\t'))
old={x['id']:x for x in state['baseline_questions']}
new={x['id']:x for x in rows}
changed=[x['id'] for x in rows if x['id'] in old and x!=old[x['id']]]
added=[x['id'] for x in rows if x['id'] not in old]
movement=a.movement=='yes'
flat=0 if movement else state['consecutive_without_movement']+1
number=state['review_number']+1
open_rows=[x for x in rows if any(t in x['state'] for t in ['OPEN','CONDITIONAL','UNRESOLVED'])]
gates=['Q34','QH9-axis','QH9-cover-primitivep','Q35-full','Q35-Bost',
       'QFermat-full','QFermat-AJ','QFermat-algradical','Q6','Q7']
lines=[f'\n## Hourly movement review {number} — due {due.isoformat()}',
       f'\nRecorded {now.isoformat()}. Movement: **{a.movement.upper()}**. '
       f'Consecutive reviews without movement: **{flat}**.',
       '\n### Mathematical judgment\n',a.reason,
       '\nA text difference, an added side result, proof checking, and packaging '
       'are not themselves movement. The stated mathematical reason is the criterion used.',
       '\n### Main questions and strongest current gates\n']
for key in gates:
    x=new[key];lines.append(f"- **{key} — {x['state']}:** {x['finding_or_current_gate']}")
lines+=['\n### Every unresolved or conditional row at review\n',
        '| ID | State | Current gate |','|---|---|---|']
for x in open_rows:
    cell=lambda s:s.replace('|','\\|').replace('\n',' ')
    lines.append('| '+' | '.join(cell(x[k]) for k in ['id','state','finding_or_current_gate'])+' |')
lines+=['\n### Documentary comparison\n',
        'Changed existing rows: '+(', '.join(changed) or 'none')+'.',
        'New question rows: '+(', '.join(added) or 'none')+'.',
        'These lists are audit data, not an automatic movement test.',
        '\nNext scheduled review: '+(due+timedelta(hours=1)).isoformat()+'.',
        'Stopping threshold reached.' if flat>=2 else 'The two-flat-review stopping threshold has not been reached.',
        '']
with (R/'deliverables/LEDGER.md').open('a') as f:f.write('\n'.join(lines))
newstate={'review_number':number,'last_review_due_utc':due.isoformat(),
          'review_recorded_utc':now.isoformat(),'movement':movement,
          'movement_reason':a.reason,'consecutive_without_movement':flat,
          'next_review_utc':(due+timedelta(hours=1)).isoformat(),
          'baseline_questions':rows}
state_path.write_text(json.dumps(newstate,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in newstate.items() if k!='baseline_questions'},indent=2))

"""Record the second actual hourly review using current rows and the preceding review."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,time
B=Path(__file__).resolve().parent
DUE=datetime.fromisoformat('2026-11-21T19:30:46+00:00')
while True:
 r=(DUE-datetime.now(timezone.utc)).total_seconds()
 if r<=0: break
 time.sleep(min(30,r))
now=datetime.now(timezone.utc)
p=B/'PROGRESS_REVIEWS.json';data=json.loads(p.read_text());assert len(data['reviews'])==1
previous=data['reviews'][-1];old={r['id']:r for r in previous['all_question_rows']}
with (B/'QUESTIONS.tsv').open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
closed=[r['id'] for r in rows if r['id'] in old and old[r['id']]['state'].startswith('OPEN') and (r['state'].startswith('PROVED') or r['state'].startswith('REFUTED'))]
assert 'KT-Q1C-NEXT-36' in closed,'The checked K72 row closure must be present.'
opened=[r for r in rows if r['state'].startswith('OPEN')]
review={'number':2,'scheduled_utc':DUE.isoformat(),'observed_utc':now.isoformat(),'reviewer':'/root; GPT-6 Astra Pro; effort setting not exposed','movement':bool(closed),'movement_basis':'Actual prior-open row closures, independently checked; the conditional TypeII exclusion also removes an explicitly documented source gate.','closed_rows':closed,'strictly_smaller_conditional_gates':['Ordinary necessary direction proved: an auxiliary Bernoulli unit excludes actual TypeII points under GD,N2,psi1; normalized adjoint exclusion separately checked.'],'excluded_from_movement':['Bounded exploratory scans','Abstract polarized obstruction and local mixed paths','Reformulations of the rational strict Selmer group','Packaging, source indexing, layout and redundant certificate replays'],'consecutive_reviews_without_movement':0 if closed else previous['consecutive_reviews_without_movement']+1,'main_all_weight_status':'OPEN: simultaneous source-compatible auxiliary units and genuinely rank-three arithmetic exclusion remain.','all_question_rows':rows,'open_question_rows':opened,'decision':'Continue; checked movement since review1.','next_review_due_utc':'2026-11-21T20:30:46Z'}
data['reviews'].append(review);p.write_text(json.dumps(data,indent=2)+'\n')
with (B/'LEDGER.md').open('a') as f:
 f.write('\n\n## Progress review 02 — '+now.isoformat()+'\n\nMovement: YES. Prior open rows now closed: '+', '.join(closed)+'. Consecutive reviews without movement:0. The all-weight target remains open. The conditional ordinary TypeII exclusion removes a previously explicit needed direction; reformulations, side obstructions and packaging do not count.\n\n| Open row | State | Strongest current gate |\n|---|---|---|\n')
 for r in opened:f.write('| '+' | '.join(r[k].replace('|','/') for k in ['id','state','current_gate_or_scope'])+' |\n')
 f.write('\nAll question rows are frozen in PROGRESS_REVIEWS.json. Continue; next review20:30:46UTC.\n')
cp=B/'CHECKPOINTS.json';c=json.loads(cp.read_text());c['next_review_due_utc']='2026-11-21T20:30:46Z';cp.write_text(json.dumps(c,indent=2)+'\n')
print(json.dumps({'review':2,'observed_utc':now.isoformat(),'movement':bool(closed),'closed_rows':closed}),flush=True)

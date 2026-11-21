"""Record the fourth review when root actually invokes it after its due time."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json
B=Path(__file__).resolve().parent
due=datetime.fromisoformat('2026-11-21T21:30:46+00:00')
now=datetime.now(timezone.utc);assert now>=due
p=B/'PROGRESS_REVIEWS.json';data=json.loads(p.read_text());assert len(data['reviews'])==3
previous=data['reviews'][-1];old={r['id']:r for r in previous['all_question_rows']}
with (B/'QUESTIONS.tsv').open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
closed=[r['id'] for r in rows if r['id'] in old and old[r['id']]['state'].startswith('OPEN') and r['state'].startswith(('PROVED','REFUTED'))]
assert closed==['KT-Q1C-FURTHER-40'],closed
opened=[r for r in rows if r['state'].startswith('OPEN')]
review={'number':4,'scheduled_utc':due.isoformat(),'observed_utc':now.isoformat(),'reviewer':'/root; GPT-6 Astra Pro; effort setting not exposed','movement':True,'movement_basis':'Actual closure of prior-open K80 row after all finite computations and three whole-proof readings passed.','closed_rows':closed,'strictly_smaller_conditional_gates':[],'excluded_from_movement':['Cubic proper-system gap repair and exact matched norm formula','Extension to finite coefficient fields','Quadratic modular-symbol and senary genus detectors','Quartic/quintic obstruction-space identification without evaluated arithmetic class','Source-scope audits, bounded scans, duplicate computations, layout and packaging'],'consecutive_reviews_without_movement':0,'main_all_weight_status':'OPEN: simultaneous actual-GD auxiliary units and exclusion of stable nonessentially-selfdual rank3 sources remain. The exact original strict rational class is not killed by the new formulas.','all_question_rows':rows,'open_question_rows':opened,'decision':'Continue. K80 is actual movement; no other new result this hour is counted as a smaller arithmetic gate.','next_review_due_utc':'2026-11-21T22:30:46Z'}
data['reviews'].append(review);p.write_text(json.dumps(data,indent=2)+'\n')
with (B/'LEDGER.md').open('a') as f:
 f.write('\n\n## Progress review04 — '+now.isoformat()+'\n\nMovement: YES, solely KT-Q1C-FURTHER-40 closing with checked K80 vanishing. Consecutive reviews without movement:0. The all-weight, remaining Ihara and all-odd-order cover gates remain open. Cubic repair, exact norm and genus detectors, unevaluated higher obstructions, source audits and packaging are not counted.\n\n| Open row | State | Strongest current gate |\n|---|---|---|\n')
 for r in opened:f.write('| '+' | '.join(r[k].replace('|','/') for k in ['id','state','current_gate_or_scope'])+' |\n')
 f.write('\nAll question rows are frozen in PROGRESS_REVIEWS.json. Next actual review22:30:46UTC.\n')
cp=B/'CHECKPOINTS.json';c=json.loads(cp.read_text());c['next_review_due_utc']='2026-11-21T22:30:46Z';cp.write_text(json.dumps(c,indent=2)+'\n')
print(json.dumps({'review':4,'observed_utc':now.isoformat(),'movement':True,'closed_rows':closed,'nonmovement_streak':0}))

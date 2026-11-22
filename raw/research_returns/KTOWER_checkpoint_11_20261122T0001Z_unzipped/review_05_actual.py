"""Record review05 only when root actually invokes it after the due time."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json
B=Path(__file__).resolve().parent
due=datetime.fromisoformat('2026-11-21T22:30:46+00:00')
now=datetime.now(timezone.utc);assert now>=due
p=B/'PROGRESS_REVIEWS.json';data=json.loads(p.read_text());assert len(data['reviews'])==4
old={r['id']:r for r in data['reviews'][-1]['all_question_rows']}
with (B/'QUESTIONS.tsv').open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
closed=[r['id'] for r in rows if r['id'] in old and old[r['id']]['state'].startswith('OPEN') and r['state'].startswith(('PROVED','REFUTED'))]
assert closed==[],closed
for f in ['evidence/root_sextic_review/review.json','evidence/root_quintic_review/review.json']:
 assert (B/f).exists()
opened=[r for r in rows if r['state'].startswith('OPEN')]
smaller=[{'finding':'KT-ORDER-SIX-COMPONENT-REDUCTION','old_gate':'Rational character order at least5','new_gate':'Order5 or at least7; order6 removed in every weight.'},
 {'finding':'KT-ORDER-FIVE-LENGTH-ONE; KT-ORDER-FIVE-STRICT-CYCLIC','old_gate':'Unrestricted remaining order-five cyclotomic component','new_gate':'At most one order-p ideal-class component among four; strict rational Selmer/K p-part cyclic, exponent unknown.'}]
review={'number':5,'scheduled_utc':due.isoformat(),'observed_utc':now.isoformat(),'reviewer':'/root; GPT-6 Astra Pro; effort setting not exposed','movement':True,'movement_basis':'Completed source-checked order-six elimination and strict restriction of the possible order-five obstruction.','closed_rows':closed,'strictly_smaller_conditional_gates':smaller,'excluded_from_movement':['Sharper first-unit discriminant bounds without simultaneous third unit','Burgess/heat/finite-evaluation limits and fixed residue-kernel counterexample','Neighbor mass/congruence limitation without source transfer','Actual-source and literature scope audits','Layout, source retrieval alone and packaging'],'consecutive_reviews_without_movement':0,'main_all_weight_status':'OPEN: rational orders5 or >=7 remain; order5 has at most one simple class component and cyclic strict/K group of unknown exponent. Simultaneous auxiliary units and the nonessential stable rank3 exclusion are still open.','all_question_rows':rows,'open_question_rows':opened,'decision':'Continue. The checked order-six elimination is by itself a strict main-gate reduction. No full Vandiver or remaining Ihara conclusion.','next_review_due_utc':'2026-11-21T23:30:46Z'}
data['reviews'].append(review);p.write_text(json.dumps(data,indent=2)+'\n')
with (B/'LEDGER.md').open('a') as f:
 f.write('\n\n## Progress review05 — '+now.isoformat()+'\n\nMovement: YES. Order-six components are removed, and the remaining order-five ideal-class obstruction has total length at most1, with cyclic strict/K groups of unknown exponent. No previously open question row closes; these are strictly smaller main arithmetic gates. Consecutive reviews without movement:0. All other bounds, method limitations, source audits and packaging are excluded from movement.\n\n| Open row | State | Strongest current gate |\n|---|---|---|\n')
 for r in opened:f.write('| '+' | '.join(r[k].replace('|','/') for k in ['id','state','current_gate_or_scope'])+' |\n')
 f.write('\nAll question rows are frozen in PROGRESS_REVIEWS.json. Next actual review23:30:46UTC.\n')
cpath=B/'CHECKPOINTS.json';c=json.loads(cpath.read_text());c['next_review_due_utc']='2026-11-21T23:30:46Z';cpath.write_text(json.dumps(c,indent=2)+'\n')
print(json.dumps({'review':5,'observed_utc':now.isoformat(),'movement':True,'nonmovement_streak':0,'next_review':'2026-11-21T23:30:46Z'}))

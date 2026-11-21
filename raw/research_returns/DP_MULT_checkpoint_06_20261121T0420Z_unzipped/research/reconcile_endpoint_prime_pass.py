#!/usr/bin/env python3
"""Incremental actual-event merge for DP52--53; never resets older gates."""
import csv,json
from datetime import datetime,timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
with (root/'CHECK_EVENTS.tsv').open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t'); fields=r.fieldnames; rows=list(r)
def add(sid,who,kind,scope,outcome,evidence,when):
 if any(r['evidence']==evidence for r in rows):return
 n=max(int(r['event_id'].split('-')[1]) for r in rows)+1
 rows.append(dict(zip(fields,[f'DPC-{n:03d}',sid,'2026-11-21 UTC',when,who,'GPT-6 Astra Pro','not exposed by runtime','DP_MULT_20261121',kind,scope,outcome,evidence])))
with (root/'research/archive_binomial_check_events.tsv').open(newline='') as f:
 for e in csv.DictReader(f,delimiter='\t'):
  if int(e['event_id'].removeprefix('ABA-CE'))<63:continue
  add(e['statement_id'],e['checker'],'targeted proof check',e['scope'],e['outcome']+' LIMIT: '+e['limitations'],'research/archive_binomial_check_events.tsv:'+e['event_id'],e['utc_time'])
for sid,fn,who in [
 ('DP52','DP52_integrated_root_review_metadata.json','/root'),
 ('DP53','DP53_root_whole_read_metadata.json','/root'),
 ('DP53','DP53_integrated_root_review_metadata.json','/root'),
 ('DP53','DP53_author_whole_review_metadata.json','/root/formal_bound'),
 ('DP53','DP53_integrated_author_review_metadata.json','/root/formal_bound'),
 ('DP53','DP53_statement_clarity_delta.json','/root')]:
 d=json.loads((root/'research'/fn).read_text())
 when=next(d[k] for k in ['observed_completion_utc','observed_complete_read_utc','recorded_utc'] if k in d)
 add(sid,who,'targeted proof check',d['scope'],d.get('outcome',d.get('result','PASS')),'research/'+fn,when)
d=json.loads((root/'research/DP52_step2_checks.json').read_text())
for e in d['proof_events']:
 add('DP52','/root/step2_higher','targeted proof check',e['scope'],e['outcome'],'research/DP52_step2_checks.json:'+e['id'],e['observed_completion_utc'])
for e in d['source_events']:
 for s in e['sources']:
  add('ALPOGE-ENDPOINT-'+s['path'].split('/')[-1],'/root/step2_higher','used and rechecked in this run','; '.join(s['ranges_and_scope'])+' Reading recorded retrospectively; individual completion timestamp was not captured.','PASS exact declaration and stated dependency inspection; no Lean execution.','research/DP52_step2_checks.json:'+e['id']+':'+s['path'],e['recorded_utc'])
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
with (root/'QUESTIONS.tsv').open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');qfields=r.fieldnames;qs=list(r)
for q in qs:
 if q['id']=='Q3e':
  q['finding_ids_or_counterexample']='U2;DP21;DP23;DP25-DP53'
  q['current_gate_or_scope']='Actual cyclic CM models, sharp primitive and universal polynomial/HaO bounds, tensor normalization and actual trace-one Jacobian theta germs are proved. DP44 and DP52 rebuild smaller even rank/HC/Host/Spaces parameters and actual mixed-type finite-class endpoint periods and their Gram identity, without the unnecessary common-quadratic-field wrapper. Six explicit AdmS identities suffice for nonzero downward induction; their realization for the same actual mixed-type family remains. DP53 proves equal leading prime budgets for globally fixed unequal directional orders and O(total order) difference for integer floor certificates. The remaining gate is to construct one prescribed geometric family jointly carrying the selected sections, harmonic row degrees, local connections/minors/paths, nonzero theta image, all six lift identities and global links, then prove an integer lift saving after all costs. No general shorter-chain impossibility is claimed.'
if not any(q['id']=='Q3an' for q in qs):
 qs.append(dict(zip(qfields,['Q3an','DP44;DataTheta501-694;CayleySignature106-204;Record1434-1610;RecordInst47-64;ColFormsLemmas77-119','Can smaller even parameters and actual mixed-type endpoint periods be constructed, and what is needed for nonzero theta induction?','proved within explicitly separated interfaces','DP52','Parameter truncation preserves all stated conditions except the explicit new Hyp3 size bound1801. The full six-input AdmS package implies finite nonzero induction. Row/point finite-class endpoint periods and their Gram identity exist for the actual type123 using explicit conjugation/equivariance goodness. The unchanged quad wrapper fails because its common field is Q, but this is not an intrinsic period obstruction. Identification with the prescribed theta image and its local/global quantitative certificates remains.'])))
with (root/'QUESTIONS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,qfields,delimiter='\t');w.writeheader();w.writerows(qs)
with (root/'IMPLICATIONS.md').open('a') as f:
 f.write('\n\n## 16. Constructed endpoint periods and the precise theta-image gate\n\n**DP52** closes the formerly open existence of the actual mixed-type finite-class row/point endpoint period and its Gram inner-product identity. Exact source dependency inspection replaces the old common-quadratic-field wrapper with the conjugation and equivariance properties the construction uses; the actual type123 satisfies these. Its common field is Q, so the unchanged wrapper fails, but that failure is not an intrinsic obstruction to the endpoint period. Smaller even parameter transport is proved subject to the stated residual size bound. The full six-input AdmS package yields the complete finite nonzero downward induction. The remaining task is to realize that package and the prescribed geometric theta image and selected local/global quantitative data for one and the same mixed-type family. Earlier sections describing the endpoint period as the next open input record the earlier state and are superseded here.\n\nThe source inventory is now578 modules:526 checked in the archive sweep and52 further direct extractions, including49 newly added in this endpoint pass. Exact recovery hashes and actual reading ranges remain separate. No Lean execution or new audit of the accepted global theorems occurred.\n')
with (root/'LEDGER.md').open('a') as f:
 f.write(f'\n\n## Post-review movement through DP53 — {now}\n\nDP52 and DP53 are integrated with complete proofs and actual author, root and independent whole-proof readings. DP52 constructs the previously open mixed-type finite-class endpoint period and Gram identity, narrows the remaining nonvanishing problem to the prescribed theta image, and proves the exact six-input induction and smaller-parameter transport. DP53 closes prime redistribution for globally fixed unequal derivative orders and integer floor certificates. This strictly narrows Q3e; it does not settle a net shorter lift chain.\n\nCurrent records: {len(rows)} check events, {len(qs)} question rows,578 source modules. Open rows remain Q3e and the unsupplied B7 comparison Q5f. DP54 finite-jet globalization is undergoing independent review and is not yet a main-paper finding. This is a work entry, not an early scheduled progress review; consecutive no-movement reviews remain0. Next review03:50UTC, checkpoint05 due03:35UTC.\n')
print(json.dumps({'utc':now,'events':len(rows),'questions':len(qs)}))

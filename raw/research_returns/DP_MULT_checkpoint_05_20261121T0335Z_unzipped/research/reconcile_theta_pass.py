#!/usr/bin/env python3
"""Reconcile the completed theta pass without rewriting historical events."""
import csv,json
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()

manifest=root/'AUTHOR_SOURCE_MANIFEST.tsv'
with manifest.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t'); mf=r.fieldnames; old={x['path']:x for x in r}
verify=json.loads((root/'research/author_source_verification_theta_pass.json').read_text())
assert not verify['unmatched_targets']
out=[]
for m in verify['matched_files']:
 assert m['byte_equal']
 row=old.get(m['path'],dict(path=m['path'],recovery_method='direct extraction from original 14-part archive',pinned_recovery_url=''))
 row.update(author_archive_member=m['author_archive_member'],bytes=m['bytes'],sha256=m['author_sha256'],byte_equal_to_author_archive=True)
 out.append(row)
with manifest.open('w',newline='') as f:
 w=csv.DictWriter(f,mf,delimiter='\t');w.writeheader();w.writerows(sorted(out,key=lambda x:x['path']))

qp=root/'QUESTIONS.tsv'
with qp.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');qf=r.fieldnames;qr=list(r)
for row in qr:
 if row['id']=='Q3e':
  row['finding_ids_or_counterexample']='U2; DP21;DP23;DP25-DP39'
  row['current_gate_or_scope']='Actual dual, primitive Poincare representative, sharp directional bounds and first primitive jets are proved. Identify the prescribed mixed-type theta normalization, H_h/psi lattice, selected polynomial/minor and path with the quantitative kernel or establish weighted selected-connection bounds; construct the new mixed-type correspondence and prove a net integer global-cost saving. Basic canonical-gauge and integral conjugated-connection existence are supplied source theorems.'
new=[
 ('Q3v','Zink2002 Lemma111,Prop121,(243),Theorem122; actual primitive Poincare class','Can a nonintegral compatible Poincare splitting have merely bounded denominators?','refuted','DP35','Bounded denominators force integrality. A primitive class forces positive linear denominator growth; units and primitive first homogeneous multipliers cannot clear it. This does not estimate selected harmonic jets.'),
 ('Q3w','DP32 actual dual; generalized symmetry/cocycle hypotheses','Does the true dual permit a rigorous weighted kernel estimate?','proved','DP36','Unequal weights restore quantization; sufficient mixed factorial bound and last-dual logarithmic path residual rho_h. Not claimed optimal or an upper bound on geometric gain.'),
 ('Q3x','Tate1967 section4 Cor2 afterTh3 p180; Zink evaluation pairing','Can the DP36 symmetry and primitive-class hypotheses actually be realized locally?','proved','DP37','Exact dual torus embedding; invariant integral frame and unique invariant rational logarithmic splitting. The prescribed global theta normalization/path is not identified by this existence theorem.'),
 ('Q3y','Zink2002 Def19,(22),Th81,(146),Prop106,(218); primitive cyclic display','What is the first actual primitive Poincare denominator and its derivative effect?','proved','DP38','Exact coefficients +1/p and -1/p in degree p+1; unit mixed jets; denominator rate at least1/(p+1). Odd-p,h>2 last-axis logarithmic path has a unit (p+1)st jet for every integral multiplier with unit constant. No asymptotic no-shortening inference.'),
 ('Q3z','RowDeg.lap,harmK,RowInv,RowDeg,HaO; IsThRule.harmA','Does full-series nonintegrality obstruct harmonic values, or does summed harmonicity transfer all bare derivative gain?','both universal shortcuts refuted','DP39(a);DP39(b)','Trivial-gauge example has invisible unbounded denominators; actual primitive-pair HaO example has a unit selected value where every integral-function value is p-divisible. The new geometric selected-connection estimate remains to be constructed.'),
 ('Q2f','CocycleRightZeroThd174-189; ExpConjConnectionIntegral40-90; WickVanishing/Closed22-63; CanonGaugeIndependenceAll23-26','Is the source integral connection/gauge transfer merely an unfilled hypothesis?','refuted; exact supplied theorem interfaces located','Section connection; DP39','Normalized jet is P(D)(f exp(k hL))(0). Integral exponential-conjugated connection, canonical-gauge independence and J^e ordered-column bounds are supplied. Their conclusion is not automatically the positive height-h slope.')]
ids={r['id'] for r in qr}
for row in new:
 if row[0] not in ids:qr.append(dict(zip(qf,row)))
with qp.open('w',newline='') as f:
 w=csv.DictWriter(f,qf,delimiter='\t');w.writeheader();w.writerows(qr)

cp=root/'CHECK_EVENTS.tsv'
with cp.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');cf=r.fieldnames;cr=list(r)
def add(s,who,typ,scope,outcome,evidence,when):
 if any(r['evidence']==evidence for r in cr):return
 eid=f"DPC-{max(int(r['event_id'].split('-')[1]) for r in cr)+1:03d}"
 cr.append(dict(zip(cf,[eid,s,'2026-11-21 Europe/Berlin',when,who,'GPT-6 Astra Pro','not exposed by runtime','DP_MULT_20261121',typ,scope,outcome,evidence])))
with (root/'research/archive_binomial_check_events.tsv').open(newline='') as f:
 for r in csv.DictReader(f,delimiter='\t'):
  n=int(r['event_id'].removeprefix('ABA-CE'))
  if n<31:continue
  typ='used and rechecked in this run' if n==32 else 'targeted proof check'
  add(r['statement_id'],r['checker'],typ,r['scope'],r['outcome']+' LIMIT: '+r['limitations'],'research/archive_binomial_check_events.tsv:'+r['event_id'],r['utc_time'])
d=json.loads((root/'research/theta_normalization_checks.json').read_text())
for e in d['events']:
 source=e['id'].startswith('TN-S')
 subjects=';'.join(e.get('subjects',[])) or e.get('subject',e['id'])
 add(subjects,d['agent'],'used and rechecked in this run' if source else 'targeted proof check',e['scope'],e['status']+'; exact steps and locators in complete memo; no Lean execution.','research/theta_normalization_checks.json:'+e['id'],e['recorded_utc'])
for name,subjects in [('DP35_DP38_review_metadata.json','DP35;DP38'),('DP37_integrated_review_metadata.json','DP37'),('theta_integrated_paper_review.json','DP37;DP38;DP39;SOURCE-CONNECTION')]:
 d=json.loads((root/'research'/name).read_text())
 when=d.get('date_time_utc',d.get('time_utc',d.get('completed_utc')))
 scope=d.get('scope',d.get('event',d.get('kind','Completed proof reading')))
 add(subjects,d.get('reviewer',d.get('agent','/root/formal_bound')),'targeted proof check',scope,d.get('result',d.get('status','PASS'))+'; exact versions and limitations in metadata.','research/'+name,when)
add('AUTHOR-SOURCE-526','/root','computation or formal certificate','Streamed all175190 entries of original14-part archive, comparing every one of526 targeted local Lean files byte for byte; preserved recovery routes of prior105 records.','526 byte-identical; zero unmatched. This is source identity, not proof audit or Lean compilation.','research/author_source_verification_theta_pass.json',verify['completed_utc'])
add('DP35;DP37;DP38;DP39','/root','targeted proof check','Read each complete saved proof: discrete norm/contraction and rational integration; true torus plus integral frame averaging; cyclic display/carry/filtration and both exact coefficients; complete Fischer and two harmonic examples. Reviewed integration while writing; further versioned independent preservation checks recorded separately.','PASS. Subsequent archive review caught a componentwise Witt-negation assertion in the integrated DP38 wording; it was corrected without changing the coefficient argument. Current proof does not use componentwise Witt negation.','research/root_late_check_notes.md:ROOT-DP35-39',now)
add('TATE67-HT-COR2-P180','/root','used and rechecked in this run','Directly viewed original printed p180: Cor2 followingTh3 and natural exact sequence, cotangent/dual-tangent placement; checked precomposition action for DP37.','PASS; classical Hodge-Tate theorem cited, not reproved.','research/late_proof_snapshots/tate_hodge_tate_cor2_p180.png:root-read',now)
with cp.open('w',newline='') as f:
 w=csv.DictWriter(f,cf,delimiter='\t');w.writeheader();w.writerows(cr)

for name in ['README.md','IMPLICATIONS.md']:
 p=root/name;s=p.read_text().replace('the105 targeted','the526 targeted').replace('contains105 targeted','contains526 targeted')
 p.write_text(s)
print(json.dumps({'utc':now,'manifest':len(out),'questions':len(qr),'events':len(cr),'last_event':cr[-1]['event_id']}))

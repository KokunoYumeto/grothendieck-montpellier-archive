"""Bind the actual root complete proof reading and its scope-only successor."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,shutil
B=Path(__file__).resolve().parent
D=B/'evidence/root_quintic_review'
now=datetime.now(timezone.utc).isoformat()
p=B/'evidence/unitary_audit/quintic_strict_cyclicity.tex'
h=hashlib.sha256(p.read_bytes()).hexdigest()
assert h=='c004e006811eafae09df3a79eb2ed93f5244dad8eaff3fdbbc29dbaf701d2db1'
shutil.copyfile(p,D/p.name)
r={'date_utc':now,'who':'/root; run KTOWER','model':'GPT-6 Astra Pro','effort':'setting not exposed',
 'finding_id':'KT-ORDER-FIVE-STRICT-CYCLIC','proof_sha256':h,
 'whole_read_predecessor_sha256':'4f03f9149788b0613c4547600bba5ab69385299497caffb216a882020fe65098',
 'successor_check':'Exact one-sentence scope clarification read: the same restriction argument does not produce an all-level replacement. Mathematical proof unchanged.',
 'outcome':'PASS entire proof and exact successor checked',
 'checks':['Nontrivial residual order5 kills global and local H0 of D.',
 'Long exact sequences preserve strictness atp and unramifiedness elsewhere through p-torsion transport.',
 'Prime-to-p Delta restriction is injective; unramified restricted homomorphism factors through Cl(L)/p with character alpha, not inverse.',
 'Order-five class bound implies p-rank at most1.',
 'Finite strict group and its full Pontryagin dual K-group are cyclic, with no exponent bound.',
 'LTE correctly gives first nontrivial higher coefficient action at p^(v_p(e)+2).',
 'Conditional Urban extra eigenspace is used only with the exact previous hypotheses; rational cyclicity does not give total Selmer dimension1.'],
 'reread_inputs':['Entire supplied K17 VK-PT and VK-LOCAL proof, K17.tex lines788-898 including K5-K7; foundational duality/cohomology and finiteness inputs retained as carried.',
 'Entire previously checked KT-RESIDUAL-CYCLICITY-SCOPE statement and proof, reducible_comparison_results.tex lines219-335; no new Urban source proof claimed.']}
(D/'strict_cyclicity_review.json').write_text(json.dumps(r,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 w.writerow(['KT-ORDER-FIVE-STRICT-CYCLIC',now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','targeted proof check','PASS whole proof and exact scope-only successor at SHA'+h,'evidence/root_quintic_review/strict_cyclicity_review.json'])
 for id in ['K17-VK-PT','K17-VK-LOCAL','KT-RESIDUAL-CYCLICITY-SCOPE']:
  w.writerow([id,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','used and rechecked in this run','PASS entire supplied/previously checked proof reread at the exact scope recorded; foundations carried','evidence/root_quintic_review/strict_cyclicity_review.json'])
q=B/'QUESTIONS.tsv'
with q.open(newline='') as f:rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['id'] in ['KT-Q1B','KT-Q1C']:
  row['finding_ids']+='; KT-ORDER-FIVE-STRICT-CYCLIC'
  row['current_gate_or_scope']+=' Exact finite-coefficient transport and full VK-PT duality make each order-five strict rational Selmer and K p-part cyclic, with unknown exponent. This does not provide total ordinary E-Selmer cyclicity.'
with q.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
with (B/'LEDGER.md').open('a') as f:
 f.write('\n\n## Order-five strict cyclicity — '+now+'\n\nKT-ORDER-FIVE-STRICT-CYCLIC has author, root and independent whole-proof PASS. Exact p-torsion transport, character orientation and full carried VK-PT duality show that an order-five rational strict group and its K-group dual are cyclic. The exponent is unrestricted. The total ordinary E-Selmer group in the inspected comparison can still have its separate opposite-conjugation class, so the required R=T cyclicity hypothesis is not established. This specifies the order-five gate without claiming vanishing.\n')
with (B/'IMPLICATIONS.md').open('a') as f:
 f.write('\n\nThe separately proved KT-ORDER-FIVE-STRICT-CYCLIC supplies the exact transport to arithmetic cohomology: p-torsion rank at most1 makes the finite strict rational Selmer group and its full VK-PT K-group dual cyclic. It supplies no exponent bound and no vanishing. The higher cyclotomic coefficient is nontrivial on Q(mu_p) at level p^(v_p(e)+2), so the same class-group restriction argument does not identify full lengths. The total ordinary E-Selmer cyclicity gate remains distinct.\n')
print(json.dumps({'recorded_utc':now,'proof_sha256':h,'cyclicity':'PASS; exponent unknown'}))

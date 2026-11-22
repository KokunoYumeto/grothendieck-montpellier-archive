"""Record root's actual complete quintic proof and primary-source reading."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,shutil
B=Path(__file__).resolve().parent
D=B/'evidence/root_quintic_review';D.mkdir(exist_ok=True)
now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=B/'evidence/main_gate/order_five_length_bound.tex'
h='65dcdf5622466d68c0ab803e854fc22f1ebd213fe604f6e5787ff024a8543d2e'
assert sha(p)==h
shutil.copyfile(p,D/p.name)
s=B/'evidence/main_gate/literature/quintic_followup/Schoof_Washington_1988.pdf'
assert sha(s)=='dfb47b92b4b530c8083f31d8ad09993aced8f445387e9ee425e1745e72c91a29'
report={'date_utc':now,'who':'/root; run KTOWER','model':'GPT-6 Astra Pro','effort':'setting not exposed',
 'finding_id':'KT-ORDER-FIVE-LENGTH-ONE','proof_sha256':h,'type':'targeted proof check: entire written proof','outcome':'PASS',
 'checks':['All four order-five characters are even for p1mod10; the small-prime HHO use is at its carried scope.',
 'General quintic regulator lower bound is for every cyclic quintic field, not only Lehmer fields.',
 'Ordinary ACNF factor16, discriminantp^4, product of four primitive even L-values and constant25/256 verified.',
 'Exact integer inequality29172150<33362176 and decreasing log-ratio prove h<p^2/6.',
 'Extension and norm give an isomorphism Cl(F){p}=A_p^H and kill the trivial component.',
 'Integral Teichmuller idempotents split exactly four remaining components; sum of lengths is v_p(h)<=1.',
 'No K-group or divisible Selmer integral-length bound is inferred.'],
 'primary_source':{'url':'https://reneschoof.github.io/sw.pdf','sha256':sha(s),'read_scope':'Printed544 complete general-field setup and stated numerical example; entire Theorem2.2 and proof545-546, Cor2.6 and proof546, Cor2.7 and full proof547. All four pages visually inspected from SW1988-03 through06. In the product estimate conjugates may be ordered by absolute value, since discriminant and sum of squared logarithms are invariant under relabeling. Pohst M=16 is an imported input; no new proof of it or numerical class-group recomputation is claimed.'},
 'other_inputs':'Louboutin even-L bound rechecked in root_sextic_review; carried HHO and standard ACNF/class-group norms.',
 'movement':'Strictly restricts the possible order-five cyclotomic ideal-class obstruction to one order-p component; does not remove it.'}
(D/'review.json').write_text(json.dumps(report,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 w.writerow(['KT-ORDER-FIVE-LENGTH-ONE',now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','targeted proof check','PASS entire proof at SHA'+h+'; exact source bounds, constants and class-group isomorphism checked','evidence/root_quintic_review/review.json'])
 w.writerow(['SCHOOF-WASHINGTON-QUINTIC-REGULATOR',now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','used and rechecked in this run','PASS full specified general-field proofs printed544-547 visually read; Pohst bound imported','evidence/root_quintic_review/review.json'])
q=B/'QUESTIONS.tsv'
with q.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
for r in rows:
 if r['id'] in ['KT-Q1B','KT-Q1C']:
  if 'KT-ORDER-FIVE-LENGTH-ONE' not in r['finding_ids']:r['finding_ids']+='; KT-ORDER-FIVE-LENGTH-ONE'
  r['current_gate_or_scope']+=' Among the four order-five cyclotomic ideal-class components, total Zp length is at most1: at most one order-p component remains. This does not assert an integral K/Selmer length bound.'
with q.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
with (B/'LEDGER.md').open('a') as f:
 f.write('\n\n## Order-five class-group size gate — '+now+'\n\nKT-ORDER-FIVE-LENGTH-ONE passes author, root and independent whole-proof checks at SHA'+h+'. The general Schoof-Washington regulator bound and exact even-L estimate give h(F5)<p^2/6 above the carried small-prime cutoff. Norm and ideal extension identify the four order-five cyclotomic components; their total Zp length is at most1. This strictly limits the order-five obstruction without making it zero, and without claiming the same integral length for K-groups or divisible Selmer groups. KT-Q1B and KT-Q1C remain OPEN.\n')
with (B/'IMPLICATIONS.md').open('a') as f:
 f.write('\n\n## Remaining order-five class obstruction\n\nKT-ORDER-FIVE-LENGTH-ONE proves that the four order-five cyclotomic ideal-class components have total Zp length at most1. A surviving component would be a single group of orderp. The explicit h(F5)<p^2/6 bound uses general quintic regulator and primitive-even-L results, followed by exact ideal-class norm/extension. This further restricts the arithmetic class-group gate in KT-Q1B/KT-Q1C. It does not give an integral K-group or divisible-Selmer length comparison, and it does not prove the surviving component is absent.\n')
print(json.dumps({'promoted_utc':now,'review_sha256':sha(D/'review.json'),'order_five_class_total_length':'<=1'}))

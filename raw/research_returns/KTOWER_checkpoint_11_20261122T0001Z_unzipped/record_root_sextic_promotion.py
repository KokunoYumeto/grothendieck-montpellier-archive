"""Record actual whole-proof readings and promote the checked order-six reduction."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil

B=Path(__file__).resolve().parent
D=B/'evidence/root_sextic_review'
D.mkdir(exist_ok=True)
now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proofs=[
 ('evidence/main_gate/sextic_class_product.tex','cd00cb2698d3add71ca7ecb729e2e2812e09d48ae5da54d488114f7e7aea99fc',
  ['KT-SEXTIC-CLASS-PRODUCT','KT-SEXTIC-REGULATOR-RATIO-FOUR']),
 ('evidence/lean_chain/order_six_reduction.tex','36da7f893a98bdf2db26fc39a9c90ff78baa241f062bf291c46deb3e2def9b64',
  ['KT-ORDER-SIX-COMPONENT-REDUCTION'])]
for rel,h,ids in proofs:
 p=B/rel
 assert sha(p)==h,(rel,sha(p),h)
 shutil.copyfile(p,D/p.name)
sources=[]
for name,expected,url,scope in [
 ('Gras_1986','59ea4f150c5a3dc2c132182a44bcca1656e5ba83487d379c5f42087924b3995b',
  'https://www.numdam.org/article/PMB_1986___2_A2_0.pdf',
  'General setup and norm-one module in Section2(a), printed2-3, read as text. Complete Theorem2.5 and Lemma2.6 statement/proofs, printed4-6, read as text and visually on physical PDF5-7. General resolvent-divisibility and lattice inputs cited there remain foundational imports. The source theorem says f>=28; the application uses p>=2^31.'),
 ('Louboutin_2004','87211ce37d1ceed964535d4565019e5bb55dece21120dfdad08eec0609c517fa',
  'https://publi.math.unideb.hu/paper/1169/download/10_5486_PMD_2004_2976.pdf',
  'Section3.1 printed454 definitions, exact regulator determinant; complete Lemma3 and proof455; immediately following product-divisibility statement; exact analytic identity456 read. The separate lower-bound Theorem5 is not used. Cornell-Washington original proof was not retrieved; the required prime-conductor product lemma is proved directly.'),
 ('Louboutin_2002_even','9eb61fd6cc97d0034851a273dd11bfb6c0ee74a9aba453b117bb4511a02b1a4f',
  'https://www.impan.pl/shop/publication/transaction/download/product/82711',
  'Full Theorem1(1), Eq3, printed2; complete Section3 proof printed5-8, including Lemma7, residual term R(f), r=0 and remaining theorem cases. Theta functional equation and previously cited integral identities remain known inputs; no fresh review of every earlier publication is claimed.')]:
 p=B/'evidence/lean_chain/primary/sextic_followup'/f'{name}.pdf'
 assert sha(p)==expected
 sources.append({'name':name,'url':url,'pdf_sha256':expected,'actual_read_scope':scope})
report={'date_utc':now,'who':'/root; run KTOWER','model':'GPT-6 Astra Pro','effort':'setting not exposed',
 'whole_written_proofs':[{'path':r,'sha256':h,'finding_ids':ids,'outcome':'PASS'} for r,h,ids in proofs],
 'checked_steps':[
  'Ordinary Hilbert fields, total ramification, disjointness from F, abelian unramified base change.',
  'The common quotient action factors through bothC2andC3; central extension of cyclicC6 is abelian.',
  'Inertia has order6; its fixed field has discriminant1 and is Q; full class-number product divides h6.',
  'Exact ACNF factors2,4,32, discriminants p,p^2,p^5, regulator factor12 andQ|12.',
  'Norm-sign correction identifies the two relative-unit conventions without any signature index.',
  'Gras bound applies to all real cyclic sextic fields; elementary max-log inequality confirms normalization.',
  'Louboutin bound applies to primitive even nonreal characters; kappa0<1 is sufficient.',
  'For p>=2^31, t=logp>20 and denominator>t-2, yielding J<49p/108<p with J a positive integer.',
  'Already checked quadratic and cubic bounds make all three integer factors p-free.',
  'Norm-extension identity kills invariants because [Q(mu_p):F] is prime to p.',
  'Carried periodic K17-(K2) gives K_{2e}{p}=0 with no e<p restriction.'],
 'primary_sources':sources,
 'carried_inputs':['Hart-Harvey-Ong Vandiver verification for p<2^31','Previously checked quadratic and cyclic cubic class-number bounds','K17-(K2) periodic arithmetic comparison','Standard class field theory, analytic class-number formula and Minkowski discriminant bound'],
 'earlier_attempt_boundary':'The provisional discriminant estimate and uncertainty about integrality were not promoted. Product integrality is now proved directly, and the proof uses the stronger published general Gras bound. No cyclotomic-unit-index identity is needed or asserted.',
 'peer_review_paths':['evidence/unitary_audit/sextic_review/review_manifest.json','evidence/geometry_tower/order_six_peer_review.json','evidence/lean_chain/order_six_review.json'],
 'new_gate':'Rational character order5 or at least7; orders1,2,3,4,6 are excluded.',
 'movement':'A strictly smaller main arithmetic gate, not a full Vandiver or Ihara conclusion.'}
(D/'review.json').write_text(json.dumps(report,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for rel,h,ids in proofs:
  for id in ids:
   w.writerow([id,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','targeted proof check','PASS entire written proof read at SHA'+h+'; all normalizations and divisibility steps checked','evidence/root_sextic_review/review.json'])
 for id in ['GRAS-SEXTIC-RELATIVE-REGULATOR-1986','LOUBOUTIN-EVEN-L1-2002','LOUBOUTIN-SEXTIC-REGULATOR-2004']:
  w.writerow([id,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','used and rechecked in this run','PASS exact primary statements and full specified proof passages read; foundational inputs distinguished','evidence/root_sextic_review/review.json'])
 for id in ['HHO-VANDIVER-VERIFICATION','K17-(K2)','KT-SMALL-ORDER-COMPONENT-REDUCTION']:
  w.writerow([id,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','carried as background without fault found','Used at previously accepted scope in the order-six reduction; no new computation or source re-proof claimed','evidence/root_sextic_review/review.json'])
q=B/'QUESTIONS.tsv'
with q.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for r in rows:
 if r['id'] in ['KT-Q1B','KT-Q1C']:
  for id in ['KT-SEXTIC-CLASS-PRODUCT','KT-SEXTIC-REGULATOR-RATIO-FOUR','KT-ORDER-SIX-COMPONENT-REDUCTION']:
   if id not in r['finding_ids'].split('; '):r['finding_ids']+='; '+id
  r['current_gate_or_scope']=r['current_gate_or_scope'].replace('Known low-degree class-number inputs remove all rational character orders1–4; remaining order≥5.', 'Known low-degree inputs and the checked sextic regulator argument remove rational character orders1,2,3,4,6; remaining order5 or order≥7.')
  if 'remaining order5 or order≥7' not in r['current_gate_or_scope']:
   r['current_gate_or_scope']+=' The checked sextic regulator argument removes order6; remaining rational orders are5 or at least7.'
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
with (B/'LEDGER.md').open('a') as f:
 f.write('\n\n## Order-six rational component removed — '+now+'\n\n')
 f.write('KT-ORDER-SIX-COMPONENT-REDUCTION passes author, root and two independent whole-proof readings at frozen SHA36da7f893a98bdf2db26fc39a9c90ff78baa241f062bf291c46deb3e2def9b64. The ordinary Hilbert-class-field product lemma supplies the essential integral ratio; exact Gras and Louboutin bounds give J<49p/108 for p>=2^31. Carried HHO handles smaller primes. Norm and extension, then the accepted K17-(K2) comparison, give every order-six rational component and K-component zero without a weight bound.\n\n')
 f.write('This strictly reduces the previous main gate from rational order>=5 to order5 or order>=7. KT-Q1B and KT-Q1C remain OPEN. The degree-six class-number conclusion is known; the new work is its precisely sourced application to the report conventions. This actual gate reduction may count at the next scheduled review; no hourly review has been performed early. All-weight vanishing, the remaining Ihara gate and the all-odd-order cover gate stay open.\n')
with (B/'IMPLICATIONS.md').open('a') as f:
 f.write('\n\n## Order-six component and the smaller arithmetic gate\n\n')
 f.write('KT-ORDER-SIX-COMPONENT-REDUCTION removes every rational cyclotomic character of order6. The class-product lemma and exact relative regulator normalization avoid a denominator or signature assumption. Known general regulator and even-L bounds prove the needed positive integer class-number ratio smaller than p; the carried small-prime verification and norm-extension argument complete the implication. Together with orders1–4, the only remaining rational character orders are5 or at least7. This is a strict reduction of KT-Q1B/KT-Q1C, not a proof of all-weight Vandiver. In (FW.1) it removes the corresponding integral arithmetic H2 and motivic K-components for every periodic weight; rational mixed-Tate Ext groups alone do not detect this torsion. The Ihara plus-tower gate and cote149/route2 conclusions do not change.\n')
print(json.dumps({'promoted_utc':now,'review_sha256':sha(D/'review.json'),'gate':'order5 or >=7','all_weight_status':'OPEN'}))

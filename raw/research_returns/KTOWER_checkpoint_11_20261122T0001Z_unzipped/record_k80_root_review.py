"""Freeze the completed root whole-proof and fresh support/report checks."""
from pathlib import Path
import csv, json, math, hashlib, sys
from datetime import datetime,timezone
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parent;H=B/'evidence/higher4'
s=json.loads((H/'hecke_general/higher4/residual_support_e40.json').read_text())['degrees'][0]
m1,m2=s['residual_support_moduli'];fac={2:1237,3:1481,5:30,17:1,19:3,23:1,53:3,61:2,263:3}
assert s['proved_small_prime_factors']=={str(k):v for k,v in fac.items()}
assert s['combined_gcd']==math.prod(p**a for p,a in fac.items())*m1*m2**3
assert math.gcd(m1,m2)==1
for m in [m1,m2]:assert math.gcd(m,336*math.factorial(79))==math.gcd(m,1+2**40+2**80)==1
old=H/'further_vanishing_e40_before_layout.tex';cur=H/'further_vanishing_e40.tex'
assert old.read_text().replace(r'\setlength{\tabcolsep}{3pt}',r'\setlength{\tabcolsep}{0.5pt}')==cur.read_text()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
snap=H/'further_certificate_root_snapshot_e40.json';snap.write_bytes((H/'further_certificate_audit.json').read_bytes())
assert all(x['all_finite_certificates_complete'] for x in json.loads(snap.read_text())['results'])
now=datetime.now(timezone.utc).isoformat()
r={'date_utc':now,'reviewer':'/root; GPT-6 Astra Pro; effort not exposed','type':'targeted proof check','verdict':'PASS','proof_reviewed_sha256':sha(old),'formatting_successor_sha256':sha(cur),'formatting_delta':'Only tabcolsep3pt to0.5pt in full native residue table; exact diff saved.','whole_proof_read':True,'whole_programs_read':['further_certificate_audit.py','native_full_further_completion_snapshot.py'],'fresh_reconciliation':{'snapshot':str(snap.relative_to(B)),'sha256':sha(snap),'complete_degrees':[38,40],'pending':[]},'checks':['Full exact support factorization including residual powers1,3','All completed report and executable/input/source hashes, unchanged initial replay sources','Every scalar, norm, pivot and 336*79! denominator unit','Exact arithmetic implication through stipulated OneChar and carried minus7 source/coverage','Safe positive endpoint20, unchanged negative endpoint-16, full-domain kappa41 only'],'limits':['Not an additional large unitary model execution','No Lean build','No all-weight or Vandiver proof','Foundational carried arithmetic theorems not re-proved'],'operational_retry':'An earlier one-off JSON read hit Python default integer-string digit cap; this saved script explicitly removes that parsing cap. No failed arithmetic assertion.'}
rp=H/'root_e40_completion_review.json';rp.write_text(json.dumps(r,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for i in ['KT-K80-VANISH','KT-COMPONENT-EXTENSION-20']:
  w.writerow([i,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','targeted proof check','PASS whole proof and exact table-spacing successor; carried arithmetic convention retained; no all-weight conclusion.',str(rp.relative_to(B))])
 w.writerow(['KT-K80-COMPLETED-REPORT-AUDIT',now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','computation or formal certificate','PASS fresh hardened exact support/report audit and displayed support factorization; no new large model execution.',str(snap.relative_to(B))])
print(json.dumps({'proof':sha(cur),'audit':sha(snap),'verdict':'PASS'}))

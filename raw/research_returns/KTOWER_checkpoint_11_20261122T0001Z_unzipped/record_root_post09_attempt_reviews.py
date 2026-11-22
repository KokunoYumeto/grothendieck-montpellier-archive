"""Record actual root whole readings and the one exact discriminator replay."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess
import sys

B = Path(__file__).resolve().parent
D = B/'evidence/root_post09_attempt_review'
D.mkdir(exist_ok=True)
now = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
records = []
for rel, ids, checks in [
 ('evidence/main_gate/neighbor_pairing_attempt.tex',
  ['KT-NEIGHBOR-CONSTANT-LINE-LIMIT'],
  ['Entire proposition and proof read, including the final real-diagonalization clarification.',
   'Automorphism orders, rank-six quadric degree, self-adjointness and row-sum verified.',
   'Full-spinor complement is saturated; equal component masses give the primitive residual constant line.',
   'Finite torsion-free commuting Hecke order lifts its character through a minimal prime avoiding p; generic character occurs by simultaneous diagonalization.',
   'The conclusion is a compact orthogonal congruence, with no unitary-source transfer or main arithmetic movement.']),
 ('evidence/lean_chain/weighted_character_attempt.tex',
  ['KT-WEIGHTED-CHARACTER-ATTEMPT'],
  ['Entire 167-line note read; exact prefix representative and all d shifted weighted intervals checked.',
   'Summation-by-parts exponent, integer-parameter minimum87/80 and threshold11/24 independently recalculated.',
   'Positive beta2 formula, Euler-factor lower bound and27p>900 inequality checked.',
   'Only the direct absolute-value estimate is delimited; no nonexistence of a simultaneous field is asserted.']),
 ('evidence/main_gate/weight_two_kernel_discriminator.tex',
  ['KT-WEIGHT-TWO-KERNEL-NONFACTORIZATION'],
  ['Entire proof and full finite script read.',
   'Cusp expansion agrees with the already checked theta and G transformations.',
   'Both integral q-series constructions are independently assembled by the script and agree through q10.',
   'The imported beta3=166 is the previously checked p83,D-43 rational certificate.',
   'The failure concerns only this coefficientwise kernel factorization.'])]:
 p=B/rel
 shutil.copyfile(p,D/p.name)
 records.append({'proof_path':rel,'proof_sha256':sha(p),'finding_ids':ids,
                 'kind':'targeted proof check: whole written proof/note',
                 'outcome':'PASS','checks':checks})
script=B/'evidence/main_gate/weight_two_kernel_discriminator.py'
shutil.copyfile(script,D/script.name)
run=subprocess.run([sys.executable,str(D/script.name)],cwd=D,text=True,capture_output=True,check=True)
(D/'replay_stdout.txt').write_text(run.stdout)
expected=B/'evidence/main_gate/weight_two_kernel_discriminator.json'
actual=D/'weight_two_kernel_discriminator.json'
assert actual.read_bytes()==expected.read_bytes()
report={'date_utc':now,'who':'/root; run KTOWER','model':'GPT-6 Astra Pro',
        'effort':'setting not exposed','whole_readings':records,
        'source_scope':[
          {'source':'Chenevier, Statistics for Kneser p-neighbors, arXiv2104.06846v2',
           'url':'https://arxiv.org/pdf/2104.06846v2',
           'local_pdf_sha256':sha(B/'evidence/main_gate/literature/jacobi_simultaneous/Chenevier_statistics_kneser.pdf'),
           'read':'Printed p3(1.2)-(1.4); pp13-15 full local construction, Lemmas4.1-4.3, Cor4.4 and Hecke-ring setup; p20 full spinor-group setup and Lemma5.6 proof; p21R2-R3; pp22-23(6.1)-(6.2), full Lemma6.1 and self-adjointness/commutativity passage. The asymptotic theorem and Arthur classification proofs remain imported, and are not used for this new proposition.'},
          {'source':'Trevino, The Burgess inequality and the least k-th power non-residue',
           'url':'https://campus.lakeforest.edu/trevino/Burgess.pdf',
           'web_reference':'turn448389197view1',
           'read':'Full classical Burgess statement across pp1-2, including cube-free qualification; exact Theorem1 and Corollary1 on p2. Foundational Burgess proof imported.'}],
        'fresh_replay':{'script_sha256':sha(D/script.name),
                        'report_sha256':sha(actual),
                        'byte_identical_to_author_report':True,
                        'q10':166601228288,'q10_mod83':26},
        'movement':False}
(D/'review.json').write_text(json.dumps(report,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for r in records:
  for id in r['finding_ids']:
   w.writerow([id,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed',
               'targeted proof check','PASS whole written proof/note read at SHA'+r['proof_sha256']+'; precise scope in review; no main movement','evidence/root_post09_attempt_review/review.json'])
 w.writerow(['KT-WEIGHT-TWO-KERNEL-NONFACTORIZATION',now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','computation or formal certificate','PASS fresh frozen-copy exact replay; whole script read; complete JSON byte-identical','evidence/root_post09_attempt_review/weight_two_kernel_discriminator.json'])
 for id in ['CHENEVIER-KNESER-LOCAL-SPINOR-PAIRING','BURGESS-CLASSICAL-PRIME-MODULUS']:
  w.writerow([id,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','used and rechecked in this run','PASS precise primary statement/proof scope recorded; foundational inputs distinguished','evidence/root_post09_attempt_review/review.json'])
print(json.dumps({'review_sha256':sha(D/'review.json'),'whole_readings':len(records),'fresh_replay':'PASS','movement':False}))

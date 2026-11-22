"""Integrate only the whole-reviewed notes after checkpoint10's bytes are frozen."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess
import sys

B = Path(__file__).resolve().parent
archive = B.parent / 'KTOWER_checkpoint_10.zip'
assert archive.exists() and archive.stat().st_size > 0, 'Checkpoint10 source copy must have completed first'
assert datetime.now(timezone.utc) >= datetime.fromisoformat('2026-11-21T23:00:46+00:00')
stamp = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
review = json.loads((B/'evidence/root_post10_review/review.json').read_text())
for r in review['whole_readings']:
 assert sha(B/r['proof_path']) == r['proof_sha256']
old = B/'evidence/checkpoint_receipts/PDF_REVIEW_checkpoint10.json'
assert not old.exists()
shutil.copyfile(B/'PDF_REVIEW.json', old)
assembly = B/'assemble_paper.py'
s = assembly.read_text()
s = s.replace("'evidence/lean_chain/cohen_hecke_support.tex',", "'evidence/lean_chain/cohen_hecke_support.tex',\n'evidence/lean_chain/hadamard_modularity_scope.tex',")
s = s.replace("'evidence/main_gate/order_five_pdiv_weight.tex',", "'evidence/main_gate/order_five_pdiv_weight.tex',\n'evidence/main_gate/order_five_greenberg_gate.tex',\n'evidence/main_gate/order_five_greenberg_abstract_model.tex',\n'evidence/unitary_audit/dimension2_comparison/dimension_two_comparison.tex',")
s = s.replace(r'\newcommand{\Sha}{\operatorname{Sha}}', r'\newcommand{\Sha}{\operatorname{Sha}}'+'\n'+r'\providecommand{\longtwoheadrightarrow}{\relbar\joinrel\twoheadrightarrow}')
assembly.write_text(s)
framework = B/'sections/framework.tex'
fw = framework.read_text()
extra = r'''KT-ORDER-FIVE-GREENBERG-UNIT-GATE;
KT-ORDER-FIVE-ABSTRACT-NORM-LIMIT &
Ideal classes and global units in the cyclotomic tower of
finite covers of $\operatorname{Spec}\mathbf Z[1/p]$;
their integral Iwasawa modules. &
K17-GREENBERG-KERNEL, Q3-IRREG, and Esquisse\S2.
The unit-norm index measures capitulation exactly in the stated
one-prime setting. The abstract module $\Lambda/(T+p)$
shows that a length-one base class and norm identities alone
do not give bounded growth. No arithmetic realization is asserted.
The exact unit-norm index and the remaining kernel gate stay open.\\
KT-SATURATED-RANKIN-COHEN-SCOPE &
Differential operators on modular coefficient sections and
reduction modulo $p$. &
K17-S17-UNIT, Prompt1(b)--(c), and (FW.1)--(FW.2).
The stated saturated order-$p-1$ symbol, even after addition
of the ordinary product, cannot universally select equal indices.
This is a coefficient-algebra limitation; no theorem that other
modular operators fail is asserted. The simultaneous-unit gate remains.\\
KT-GMA-MULTIGENERATOR-CONORMAL &
The conormal of the reducibility locus in an integral
three-character deformation space. &
EGA IV$_4$,16.1.2 is the conormal terminology already used above;
the arithmetic input is the separately cited Berger--Klosin setup.
A $d$-generated adjacent module contributes $d$ copies of the
adjacent Selmer length. The strengthened congruence inequality
and actual-source identification are not proved. This does not
eliminate torsion in the integral motivic realization (FW.1).\\
'''
assert 'KT-ORDER-FIVE-ABSTRACT-NORM-LIMIT' not in fw
fw = fw.replace('Ihara gate &', extra+'Ihara gate &')
framework.write_text(fw)
with (B/'QUESTIONS.tsv').open(newline='') as f:
 reader = csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
ids = ['KT-ORDER-FIVE-GREENBERG-UNIT-GATE','KT-ORDER-FIVE-ABSTRACT-NORM-LIMIT','KT-SATURATED-RANKIN-COHEN-SCOPE','KT-GMA-MULTIGENERATOR-CONORMAL']
for r in rows:
 if r['id'] in ['KT-Q1B','KT-Q1C']:
  existing = [x.strip() for x in r['finding_ids'].split(';') if x.strip()]
  for fid in ids:
   if fid not in existing: existing.append(fid)
  r['finding_ids']='; '.join(existing)
  r['current_gate_or_scope'] += ' The unit-norm/capitulation criterion is not evaluated; an abstract cyclic norm system permits unbounded growth. The specified saturated Rankin-Cohen selector fails, and the d-generator comparison requires an unproved stronger integral congruence inequality. These are NONMOVEMENT: the original remaining class obstruction is unchanged.'
with (B/'QUESTIONS.tsv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)
with (B/'LEDGER.md').open('a') as f:
 f.write('\n\n## Reviewed conditional steps after checkpoint10 — '+stamp+'\n\n')
 f.write('The four additional notes have author, root and independent whole-proof PASS at their frozen hashes: the exact quintic unit-norm/capitulation criterion, an explicitly abstract unbounded cyclic norm system, the saturated Rankin-Cohen symbol limitation, and the d-generator GMA conormal estimate. Root source scope and peer computations are distinguished in evidence/root_post10_review/review.json. No root replay is claimed for the p31 coefficient control.\n\n')
 f.write('These are NONMOVEMENT. No order-five component is eliminated, no simultaneous unit is constructed, and no actual-source R=T comparison is verified. The main arithmetic gate remains order5 or order>=7, the positive-rank Ihara gate is unchanged, and the all-odd-order cover question remains open. The next actual review is23:30:46UTC; no early review was performed.\n')
with (B/'IMPLICATIONS.md').open('a') as f:
 f.write('\n\n## Additional unit-norm and integral-comparison requirements\n\n')
 f.write('For the real cyclic quintic tower, the index of norms of global units equals the capitulation-kernel order. All base units are already norms of field elements; that weaker fact does not settle the index. A separate abstract Lambda/(T+p) example satisfies the stated cyclic base and norm/transfer identities but has lambda1. It has no claimed number-field realization. Thus the order-five class restriction alone supplies neither bounded Iwasawa growth nor a new Ihara-kernel conclusion.\n\n')
 f.write('The new GMA lemma replaces cyclicity by d generators at the cost of multiplying the adjacent Selmer length by d. A matching stronger congruence lower bound remains unproved for the actual Tate triple. The saturated Rankin-Cohen trial also fails its universal diagonal-symbol test. These findings are stated in the integral conormal and modular-section language of the framework crosswalk. They leave the original integral H2 torsion, Vandiver, positive-rank Ihara, and route2 gates unchanged.\n')
subprocess.run([sys.executable, str(B/'merge_checks.py')],cwd=B,check=True)
subprocess.run([sys.executable, str(assembly)],cwd=B,check=True)
print(json.dumps({'integrated_utc':stamp,'findings':ids,'movement':False,'tex_sha256':sha(B/'KTOWER.tex')}))

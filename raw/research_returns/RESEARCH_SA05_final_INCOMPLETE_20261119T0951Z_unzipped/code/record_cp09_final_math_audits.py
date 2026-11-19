"""Record the completed written checks immediately preceding checkpoint09."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
checks=[
 ('cor:B-Milnor-free-quotient','sections/b1_milnor_divisibility.tex',
  'Root read the actual integrated proposition and corollary at clock-confirmed09:22–09:23UTC. Regulator-kernel torsion-freeness makes D_ell ell-divisible and the quotient torsion-free. Restriction to a smooth-projective alteration is injective on the quotient by trace; residues then inductively embed it in a countable direct sum of lower-degree free quotients. The canonical equivariant completion isomorphism follows. No saturation or equivariant permutation basis is obtained.'),
 ('B1:permutation-submodule-completion','part_b/b1_milnor_divisibility_attempt.md',
  'Root read the complete Section7 construction and proof, as well as its program and retained finite output. The cyclic wraparound congruence, surjective map to Z[1/3]/Z, Tor transition by3, exact inverse limit, explicit compatible lambda_r=3^r e_(r,0), eigen4 congruence and exact order3^r all pass. The infinite proof establishes survival after rationalization; the finite levels1–8 certificate is only supplementary. Root did not independently rerun that certificate. This is a formal lattice example, not a Milnor identification or a geometric counterexample.')
]
p=root/'ROOT_CHECK_EVENTS.tsv'
with p.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
for label,filename,outcome in checks:
    if not any(r['statement_id']==label and r['outcome']==outcome for r in rows):
        rows.append(dict(statement_id=label,date=now,who='GPT-6 Astra / root / current run',
                         type='targeted proof check',outcome=outcome))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(rows)
p=root/'ITEM_SCOPE_ADDITIONS.json';scopes=json.loads(p.read_text())
scopes['B.1']['statement_ids']=list(dict.fromkeys(scopes['B.1']['statement_ids']+['cor:B-Milnor-free-quotient']))
extra=' The separated ordinary Milnor quotient is countably free and has the same completion. A fully explicit free submodule of a sum of finite permutation lattices nevertheless acquires eigenvalue4 after3-adic completion, so freeness does not control the missing completed eigenclasses.'
if extra.strip() not in scopes['B.1']['scope_append']:scopes['B.1']['scope_append']+=extra
p.write_text(json.dumps(scopes,indent=2,ensure_ascii=False)+'\n')
note='''

### Separated Milnor quotient and the remaining saturation issue

The all-degree ordinary regulator lemma further proves that the quotient by infinitely ell-divisible elements is a free abelian group of at most countable rank. The kernel is ell-divisible, and quotienting induces a canonical equivariant isomorphism on completions. The proof includes alteration transfer for arbitrary function fields and finite-support residue induction.

This does not supply the missing spectral control. An explicit exact sequence with quotient Z[1/3]/Z gives a free Frobenius-stable subgroup of a countable sum of finite permutation lattices whose3-adic completion contains a nonzero four-eigenvector. Its compatible elements, exact orders and Tor transitions are proved, and a finite congruence program is supplied as a supplementary check. This formal example blocks an inference from freeness or from an unsaturated permutation-submodule embedding; it is not identified with a geometric Milnor group. The B1 universal gate and formal no-movement count are unchanged.
'''
for filename in ['RESEARCH_SA05_report.md','PROGRESS_LEDGER.md']:
    p=root/filename;s=p.read_text()
    if '### Separated Milnor quotient and the remaining saturation issue' not in s:p.write_text(s+note)
out=dict(recorded_utc=now,checks=[dict(statement_id=l,file=f,
    sha256=hashlib.sha256((root/f).read_bytes()).hexdigest(),outcome=o) for l,f,o in checks],
    qualifying_movement=False)
(root/'code/record_cp09_final_math_audits_output.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(recorded_utc=now,checks=len(checks),qualifying_movement=False),indent=2))

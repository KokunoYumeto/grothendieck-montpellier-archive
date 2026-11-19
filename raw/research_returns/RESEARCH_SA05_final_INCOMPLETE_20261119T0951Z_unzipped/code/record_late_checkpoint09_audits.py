"""Preserve the checked Milnor and simple-spectrum sufficient results."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
checks=[
 ('prop:B-Milnor-divisible-kernel','part_b/b1_milnor_divisibility_attempt.md',
  'Root read the complete degree induction and independently reopened the exact primary inputs: CT–Schreieder definitions(2.7)–(2.8),p11,and complete Proposition3.7 local proof,p16; Schreieder complete Theorem2.2 and Corollary2.3 local proofs,pp6–7,and Remark2.4. Ordinary regulator compatibility, finite Frobenius orbit, negative diagonal-twist weights, torsion-freeness and alteration trace descent pass. The kernel statement includes n=0; the residue implication is n>=1. No arbitrary completed eigenclass or degree3/twist2 vanishing is inferred.'),
 ('c:threefold-simple-spectrum','part_c/c4_simple_spectrum_positivity.tex',
  'Root read the entire written fragment at clock-confirmed09:16UTC. Mixed trace nondegeneracy gives the first right-ideal idempotent and the algebraic cohomological projector onto ker((1-p)f); thus the second image is the actual primitive intersection. Rational correspondence traces and the Vandermonde Gram matrix give End_alg(P)=Q[F]; adjoint-fixed field-factor idempotents give nondegeneracy. Fixed-field averaging, whole-target squarefreeness and all stated limitations pass. No new primary-source opening is claimed for the previously checked Katz–Messing input.'),
 ('c:threefold-simple-spectrum-scope','part_c/c4_simple_spectrum_positivity.tex',
  'The proof retains mixed numerical-equals-homological equivalence and a squarefree Frobenius polynomial on the entire primitive surface target over one fixed field. No alteration, constant-field extension or arbitrary-morphism transfer removes these hypotheses. This is a proved sufficient subcase, not qualifying movement on universal C4.')
]
path=root/'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
for label,filename,outcome in checks:
    if not any(r['statement_id']==label and r['outcome']==outcome for r in rows):
        rows.append(dict(statement_id=label,date=now,who='GPT-6 Astra / root / current run',
                         type='targeted proof check',outcome=outcome))
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(rows)
path=root/'ITEM_SCOPE_ADDITIONS.json'
scopes=json.loads(path.read_text())
extras={
 'B.1':(['prop:B-Milnor-divisible-kernel'],
        ' The ordinary Milnor regulator has exactly the infinitely ell-divisible kernel in every degree; the residue criterion holds in positive degree. This uses the diagonal twist and does not remove the weight-zero part of the degree-three/twist-two residue gate.'),
 'C.4':(['c:threefold-simple-spectrum','c:threefold-simple-spectrum-scope'],
        ' A globally squarefree primitive target Frobenius polynomial replaces the target Hodge-positivity hypothesis in a proved sufficient subcase, with mixed numerical=homological equivalence retained. No universal transfer supplies these conditions.')
}
for item,(labels,extra) in extras.items():
    scopes[item]['statement_ids']=list(dict.fromkeys(scopes[item]['statement_ids']+labels))
    if extra.strip() not in scopes[item]['scope_append']:scopes[item]['scope_append']+=extra
path.write_text(json.dumps(scopes,indent=2,ensure_ascii=False)+'\n')
note='''

### Further checked results before checkpoint09

The ordinary Milnor regulator kernel is now proved to be the infinitely ell-divisible subgroup in every degree over an algebraic closure of a finite field. In positive degree, infinitely divisible residues on a smooth projective model force infinite divisibility of the original ordinary element. The proof uses degree induction, the exact ordinary refined-unramified weight interval, finite Frobenius orbits and torsion-freeness. It does not identify an ordinary colimit with its completion and does not exclude the weight-zero interval in the actual degree-three/twist-two B1 residue problem.

For C4, a second sufficient pairing criterion replaces the surface-square positivity hypothesis with squarefreeness of the entire primitive target Frobenius polynomial over the fixed field of definition. Mixed numerical-equals-homological equivalence remains assumed. Two algebraic cohomological image/kernel constructions obtain the actual primitive intersection; the resulting finite étale endomorphism algebra has adjoint-fixed idempotents. The condition is not claimed to hold after an arbitrary extension or for every degeneration.

Both complete arguments have owner and independent written-proof checks. Root also reopened the precise primary inputs for the Milnor argument. Neither result closes an original open row or proves a strictly smaller universal gate, so neither resets the formal no-movement count.
'''
for filename in ['RESEARCH_SA05_report.md','PROGRESS_LEDGER.md']:
    p=root/filename;s=p.read_text()
    if '### Further checked results before checkpoint09' not in s:p.write_text(s+note)
out=dict(recorded_utc=now,checks=[dict(statement_id=l,file=f,
    sha256=hashlib.sha256((root/f).read_bytes()).hexdigest(),outcome=o) for l,f,o in checks],
    qualifying_movement=False)
(root/'code/record_late_checkpoint09_audits_output.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(recorded_utc=now,checks=len(checks),qualifying_movement=False),indent=2))

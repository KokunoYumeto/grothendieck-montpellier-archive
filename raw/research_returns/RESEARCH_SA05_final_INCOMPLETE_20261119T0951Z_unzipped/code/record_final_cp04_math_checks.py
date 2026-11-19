"""Record the final actually read mathematical additions before checkpoint04."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
now = datetime.now(timezone.utc).replace(microsecond=0)
specs = [
 ('thm:B-relative-surface-gate', 'Root wrote the complete equivalence and both independent readers checked it. Surface Tate implies open-variety Tate by Kahn2023 Theorems6,8 and the checked Morrow crystalline reduction. The arithmetic H1(Gamma,H1) term is retained and cancels relatively by fibre weight1. The converse uses a pencil with an extending section, regular Brauer injection, and res/cor descent with arbitrary extension degree. B–S Theorem7.1(1)/Remark7.2 identifies the single H3(F0 P3,Qell2) gate. Cohomological Brauer and regular separated-base scope are explicit.'),
 ('prop:B-diagonal-Chow-gate', 'Root read the complete proof and opened B–S Corollary1.3, Theorem7.1, Remark7.2 and full section7.4. Affine cohomological dimension removes the upper codimensions. The split map z to z times h^t on X times P^t, t=d−2i+1, reduces the remainder to codimension m in dimension2m−1. This is a reduced universal index set, not a claim that the first threefold case implies all dimensions.'),
 ('def:B-corrected-comparison-package', 'Root read the full conjectural formulation and checked its separate finite-field, arithmetic f-admissibility, and global gluing clauses. Requested arithmetic extension/model data are explicit. The definition is a conjecture, not a construction of the proposed categories.'),
 ('prop:B-comparison-specializations', 'Root checked the conditional Geisser finite-field implication and the all-twist unconditional Tate number-ring specialization. The proof does not infer finite-field Beilinson or global gluing from Bloch–Kato degree1 alone. The higher comparisons retain their chosen vector-space splittings.'),
 ('prop:B-Scholbach-finite-support', 'Root checked the stated geometric object i_*1_Fp and adjunction: ordinary motivic degree1 is K_{−1}(Fp)^(0)_Q=0, whereas the Weil point group is Q e_p and continuous ell-adic H1 is Qell. This refutes the full identification, not the source’s separate conditional generic f-cohomology theorems.'),
 ('c:hyperkahler-chow-unramified', 'Root opened the complete Ito–Zou author article dated6October2026 and read Lemmas4.2–4.3 and Theorem4.4 with proof. Root checked purity under tensor products and homogeneous algebraic summands, descent of purity through finite extensions, and the use of the already proved Saito Chow-projector argument at the original place. Strong compatibility after extension is not used to descend unramifiedness.')
]
path = ROOT/'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as stream:
    reader=csv.DictReader(stream,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
added=0
for identifier,outcome in specs:
    if not any(row['statement_id']==identifier and row['outcome']==outcome for row in rows):
        rows.append(dict(statement_id=identifier,date=now.isoformat().replace('+00:00','Z'),
                         who='GPT-6 Astra / root / current run',type='targeted proof check',outcome=outcome));added+=1
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)
marker='## Final mathematical additions before checkpoint04'
text='''

## Final mathematical additions before checkpoint04

B.1 now has a strictly smaller universal cycle gate, under the same universal Tate and semisimplicity hypotheses: only codimension m on varieties of dimension2m−1, m≥2, is required. The published Balkan–Schreieder upper-half reduction and an explicit split projective-space product prove the reduction. The first case is codimension2 on threefolds, equivalently the stated H4(F0 P4,Qell(3)) invariant vanishing under the fixed Tate assumptions. It is not claimed to imply all higher cases by itself.

B.3's intended regular separated-base prime-to-p relative-curve assertion is now equivalent to Tate divisors on smooth projective surfaces over the prime field, with finite constant extensions included. Equivalently its gate is H3(F0 P3_Fbarp,Qell(2))^GammaFp=0. The proof preserves the nonproper arithmetic cohomology term and shows it comes from the base; the pencil converse uses its extending section to kill the base Brauer ambiguity. Arbitrary singular/nonseparated-base equivalence chains remain separately recorded, without promoting this surface reduction to that larger scope.

B.2's requested general conjectural formulation and its specializations are now explicitly supplied. The formulation states the additional finite-field and gluing hypotheses instead of claiming that Bloch–Kato degree1 constructs them. The Tate determination and the two implications are proved. The conjectural global completion is not asserted to exist. B.5's requested general pure-motive duality proof remains open. The specified finite-support object gives a direct refutation of identifying Scholbach's ordinary Hom theory with the entire absolute Weil theory.

C.6 has a further proved case for homogeneous algebraic Chow summands of tensor constructions on hyper-Kähler varieties. The opened Ito–Zou purity theorem supplies the necessary ambient purity at the original local field. This does not settle the general-motive row and is not counted as closing that gate. The new K3 nilpotence and specialization attempts give no smaller proved general K3 gate; their precise failures remain recorded.
'''
for filename in ['PROGRESS_LEDGER.md','RESEARCH_SA05_report.md']:
    path=ROOT/filename
    if marker not in path.read_text():path.write_text(path.read_text()+text)
result={'new_events':added,'root_events':len(rows),'checked_at':now.isoformat(),'seconds':round(time.monotonic()-started,6)}
(ROOT/'code/record_final_cp04_math_checks_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

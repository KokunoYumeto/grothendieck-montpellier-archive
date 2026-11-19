"""Record the completed root proof audit, without changing a universal status."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
proof = root / 'part_d/c6_motivated_rank_reduction.tex'
assert proof.exists()
checks = [
    'The graph-image rank identity is valid with restricted inputs and nonunique internal variables.',
    'Hodge-star normalization gives TLT=Lambda directly on primitive strings. The printed Lefschetz-star equality is not used.',
    'The product sign commutes with even partial Lefschetz maps. Partial grading operators and factor Hodge stars follow from finite polynomials and the Weyl expression, with the degree sign on the input.',
    'Global Hodge stars use only finitely many explicitly typed Hard-Lefschetz inverses on whole products. No tensor comparison for nearby cycles is assumed.',
    'The motivated-correspondence action has final degree i and twist zero; its algebraic presentation is over K under Andre Definition1 and the K-scheme setup in section2.1.',
    'A common Galois field and the disjoint union of conjugate semistable models supply all algebraic E1 blocks and the original finite-inertia quotient action.',
    'Every inverse is restricted by q-image equations. It is not inverted on the entire alteration cohomology, and E1 representatives need not be idempotent.',
    'The normalized row complexes have common index i-b and weight b. Appending N^s shifts the output row by 2s and twist by -s.',
    'Generalized Frobenius weight spaces and FNF^-1=q^-1N recover the actual monodromy rank from graded ranks without Frobenius semisimplicity or weight-monodromy.',
    'After N=0, I_L is trivial. A zero graded sigma-1 is unipotent, and its finite order forces identity in characteristic zero.',
    'The abelian-strata corollary requires actual rational Chow abelian-type presentations for all auxiliary strata. It does not infer geometric positivity from an abstract motive isomorphism.',
    'No converse to the finite-field rank conjecture and no general absolute-Hodge or numerical projector theorem is inferred.'
]
sources = [
    'Andre1996, printed pp10-14: definitions of both involutions, Proposition1.2 as printed, complete Lemma1.3.2 proof, K-scheme setup and Definition1 in section2.1. The initial part only of Proposition2.1 was read in this audit.',
    'Takeshi Saito2003, complete section2.4 pp33-36, Corollary1.2.6 p16, Corollary2.2.4 pp21-22 and Lemma3.7 p42, all with the supplied proofs.',
    'Takeshi Saito2003, complete Lemma3.2 proof pp36-38, Lemma3.3 proof pp38-39 and Theorem3.1 proof p39, including transport of structure and conjugate alterations.',
    'van Dobben de Bruyn2020, Theorem5.1 and Corollary5.2 pp17-18 with the complete supplied proof; published primary PDF /6931/pdf.'
]
result = dict(recorded_at=now, reviewer='GPT-6 Astra / root / current run',
    proof_file=str(proof.relative_to(root)), proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
    outcome='Complete written proof passed in the stated conditional scope',
    checked_steps=checks, primary_read_scope=sources,
    exact_checks=['code/check_rank_diagrams.py', 'code/check_rank_diagrams_output.json',
                  'code/check_lefschetz_factor_operators.py', 'code/check_lefschetz_factor_operators_output.json'],
    retained_derivations=['root_rank_diagram_note.md', 'root_motivated_operator_note.md'],
    classification='Sufficient conditional implication; no universal open row closed and no formal movement counted')
(root/'code/record_motivated_rank_audit_output.json').write_text(json.dumps(result,indent=2)+'\n')
events = root/'ROOT_CHECK_EVENTS.tsv'
with events.open(newline='') as handle:
    rows=list(csv.DictReader(handle,delimiter='\t'))
outcomes = {
 'c:motivated-unramified-rank-reduction': 'Root read the entire written proof and independently proved its finite graph-rank and whole-product Lefschetz constructions. All ten main geometric and operator steps pass; exact source reads and computations are recorded in code/record_motivated_rank_audit_output.json. Sufficient conjectural implication only.',
 'c:motivated-abelian-strata-unramified': 'Root checked the abelian-strata corollary: all auxiliary strata must have actual rational Chow abelian-type presentations. Semisimple numerical images and the current abelian Tate input supply block-rank independence; no geometric positivity is transported.',
 'c:motivated-rank-reduction-scope': 'Root confirmed the stated boundary: arbitrary absolute-Hodge classes are not shown motivated, numerical projectors are not supplied with realization-compatible presentations, and the converse encoding remains unproved.'
}
for label,outcome in outcomes.items():
    if not any(r['statement_id']==label and r['outcome']==outcome for r in rows):
        rows.append(dict(statement_id=label,date=now,who=result['reviewer'],type='targeted proof check',outcome=outcome))
with events.open('w',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    writer.writeheader();writer.writerows(rows)
heading='## Conditional motivated-projector reduction: root audit'
entry='\n\n'+heading+'\n\nAt '+now+', root completed the written proof audit of the finite-field rank implication for Andre motivated motives. The full derivations are preserved in the two root notes, and the numbered proof is in part_d/c6_motivated_rank_reduction.tex. The graph constraints invert Hard-Lefschetz maps only on alteration-projector images, use whole-product operators, and retain the original inertia action through conjugate models. Exact matrix checks support, but do not replace, the general proofs. The source-normalization issue in Andre p11 is recorded in the operator note; the proof uses the directly verified Hodge normalization. The result is conditional on the published finite-field correspondence-rank conjecture. It proves neither that conjecture nor a converse, and it is not counted as closure or a strictly smaller universal gate.\n'
for name in ['RESEARCH_SA05_report.md','PROGRESS_LEDGER.md']:
    path=root/name
    content=path.read_text()
    if heading not in content:path.write_text(content+entry)
print(json.dumps(result,indent=2))

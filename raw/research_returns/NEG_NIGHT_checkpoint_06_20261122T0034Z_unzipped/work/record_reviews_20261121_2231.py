import csv
import json
from pathlib import Path

UTC = '2026-11-21 22:31:13 UTC'
p = Path('work/review_status.json')
d = json.loads(p.read_text())
entries = [
    ('NN-G027', 'Complete original proof and new 3352-pair refinement read, with every displayed coefficient list, generic associative block argument, rational-factor scope and actual geometric coefficient dictionary. Both construction verifiers were read and rerun in this run; those events are separate.', 'work/gct/g027_insert.tex; work/gct/verify_dimension_3352.py'),
    ('NN-G028', 'Complete arbitrary-degree proof read: necessary associativity identities, integral H/J normalization, globally monotone mass bound, m=4/5 reduction, all four J polynomials, every A1/A2 coefficient constraint, independent maximization and exactly two minimizers. Every line of the finite verifier read.', 'work/gct/g028_insert.tex; work/gct/verify_fixed_bottom_optimum.py'),
    ('NN-A027', 'Read the full infinite-alphabet partial-fraction and rectangular determinant proof, all remainder-column estimates, endpoint zero separation, sharp order/window limits, translated unitary angle and explicit determinant-character witness. Required and checked the added strict separation of the limiting real poles; the application already satisfies it.', 'work/analytic/dominant_double_detection.tex; correction message and amended first lemma'),
]
for fid, scope, evidence in entries:
    d[fid] = dict(date_utc=UTC, who='/root', model='GPT-6 Astra Pro', effort='not exposed by runtime', type='targeted proof check', outcome='PASS; complete deduction proof read, with the recorded A027 hypothesis repair incorporated', scope_and_method=scope, limitations='Not formal verification or an independent re-proof. A027 is conditional on its displayed dominant-double hypothesis, not supplied by A.', evidence=evidence)
p.write_text(json.dumps(d, indent=2)+'\n')
p = Path('work/root/CHECK_EVENTS.tsv')
with p.open() as f: fields = next(csv.reader(f, delimiter='\t'))
rows = []
def event(fid, kind, outcome, scope, evidence, limitations):
    rows.append(dict(statement_id=fid, date_utc=UTC, who='/root', model='GPT-6 Astra Pro', effort='not exposed by runtime', type=kind, outcome=outcome, scope_and_method=scope, limitations=limitations, evidence=evidence))
event('NN-G027', 'computation or formal certificate', 'PASS: 3352 total pairs, 2752 bottom pairs; all 132 coefficient positions and 1000 associativity triples', 'Read and reran the exact independent integer-Laurent verifier; no source builder imported.', 'work/gct/dimension_certificate_3352.json', 'A finite exact construction certificate, not an unrestricted optimality proof.')
event('NN-G028', 'computation or formal certificate', 'PASS: four rows have scores 3720,3452,3352,3728; global mass endpoint is11138>11128', 'Read and reran the finite arithmetic verifier. The global unbounded-degree reduction is established in the separately read written proof.', 'work/gct/fixed_bottom_optimum_certificate.json', 'Exact optimum only for W=3D,U1=3D,U2=D in the specified closed table.')
event('SGA4-XVI3.7-3.10a', 'used and rechecked in this run', 'PASS: smooth-pair purity and negative codimension twist confirmed in primary re-edition', 'Read the exact primary PDF text for Theorem3.7, Corollary3.8/3.8.1 and Remark3.10(a), pp11–13. The primary text has mu_n tensor(-c); the web transcription drops this minus sign.', 'https://www.normalesup.org/~forgogozo/SGA4/16/16.pdf', 'Statement and local source audit; no claim to re-prove the imported theorem. The transcription discrepancy is not a change to the mathematics used.')
event('SGA4-XVIII3.2.5-3.2.6.2', 'used and rechecked in this run', 'PASS: smooth Poincare duality and twist convention', 'Read primary re-edition Theorem3.2.5 and equation3.2.6.2, pp77–78, originalpp585–586, and the adjoining proof passage.', 'https://www.normalesup.org/~forgogozo/SGA4/18/18.pdf', 'No complete reading of all prerequisite duality proofs claimed.')
event('Stacks-02RX-02TS-02TY', 'used and rechecked in this run', 'PASS: exact localization, affine-bundle surjectivity and vector-bundle homotopy statements', 'Read official Stacks statements and displayed proof passages. S016 uses only affine-bundle surjectivity where indicated.', 'https://stacks.math.columbia.edu/tag/02RX; https://stacks.math.columbia.edu/tag/02TS; https://stacks.math.columbia.edu/tag/02TY', 'Imported Chow-theory interfaces, not a new proof or general affine-bundle injectivity claim.')
event('Milne-LECv2.21-Th23.4', 'used and rechecked in this run', 'PASS: cycle-map comparison and rational l-adic compatibility', 'Read the author PDF Section23, printedpp141–142, Theorem23.4 and subsequent rational l-adic construction; the notes omit the long proof and explicitly discuss a defect in an earlier proof.', 'https://www.jmilne.org/math/CourseNotes/LECc.pdf', 'Source statement check only; no complete proof reading of this classical theorem claimed.')
with p.open('a', newline='') as f:
    csv.DictWriter(f, fieldnames=fields, delimiter='\t').writerows(rows)
print('Recorded', len(d), 'review entries and', len(rows), 'separate events.')

import csv
import json
from pathlib import Path

UTC = '2026-11-21 22:23:47 UTC'
p = Path('work/review_status.json')
reviews = json.loads(p.read_text())
for fid, scope, evidence in [
    ('NN-C028', 'Read the complete sparse-cubic parameter matching, actual pure Tate comparison, positive-rank PP reduction, equality-sensitive PP membership, analytic orders and original circuit-size E bound.', 'work/complexity/c028_draft.py'),
    ('NN-A026', 'Read the entire Weyl sine-product proof, skew-Schur width dictionary, strict convolution with the infinite positive specialization, both separate normalizations, finite unitary-rank failure, and exact counterexample to the published quadratic-product inference.', 'work/analytic/angle_only_obstruction.tex'),
]:
    reviews[fid] = dict(date_utc=UTC, who='/root', model='GPT-6 Astra Pro', effort='not exposed by runtime', type='targeted proof check', outcome='PASS; complete deduction proof read', scope_and_method=scope, limitations='Not formal verification or an independent re-proof; imported source checks are separate.', evidence=evidence)
p.write_text(json.dumps(reviews, indent=2) + '\n')
p = Path('work/root/CHECK_EVENTS.tsv')
with p.open() as f:
    fields = next(csv.reader(f, delimiter='\t'))
rows = [
    dict(statement_id='Aaronson2005-PP-definition', date_utc=UTC, who='/root', model='GPT-6 Astra Pro', effort='not exposed by runtime', type='used and rechecked in this run', outcome='PASS: strict-majority convention confirmed', scope_and_method='Read primary author manuscript Section 1, printed page 1, definition and majority example. The C028 hardness and tie-handling proofs are supplied separately.', limitations='Definition/source-locator audit, not a reading of the entire paper.', evidence='https://www.scottaaronson.com/papers/pp.pdf'),
    dict(statement_id='Adm-Garloff-Tyaglov2018-Th5.7-5.8', date_utc=UTC, who='/root', model='GPT-6 Astra Pro', effort='not exposed by runtime', type='used and rechecked in this run', outcome='PASS: sharp family and sufficient sector statement verified', scope_and_method='Read primary PDF text, printed page 161, Theorem 5.7 and equation 5.9, and Theorem 5.8 equation 5.10.', limitations='Source statement audit; the specialized Weyl proof is read in A026. No PDF page image inspection asserted.', evidence='https://www-home.htwg-konstanz.de/~garloff/JMAA-3_Adm_Garloff_Tyaglov.pdf'),
    dict(statement_id='Adm-Garloff-Tyaglov2018-product-inference-after5.12', date_utc=UTC, who='/root', model='GPT-6 Astra Pro', effort='not exposed by runtime', type='refuted, with the refined statement\'s id', outcome='REFUTED by NN-A026: q=1+0.9z+z^2 is not PF2 but q^2 is PF2', scope_and_method='Read the exact published inference on printed page 162 and the full rational log-concavity counterexample; the single-factor criterion and sector sufficiency remain valid.', limitations='Refutes the specified inference, not every theorem in the source.', evidence='work/analytic/angle_only_obstruction.tex; primary PDF printed page 162'),
]
with p.open('a', newline='') as f:
    csv.DictWriter(f, fieldnames=fields, delimiter='\t').writerows(rows)
print(f'Recorded {len(reviews)} full-proof review entries and {len(rows)} source events.')

"""Record actual source reads and mathematical audits before checkpoint08."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
checks = [
 ('prop:B-limit-diagnostics', 'sections/b1_limit_diagnostics.tex',
  'Root read the complete integrated proof and independently checked continuous Kummer cohomology, the inverse-limit restricted product, infinite-support invariant class after rationalization, the 3-adic eigenfunction, the valuation induction and the fixed-orbit permutation distinction. This is a full written-proof check, not a new code execution. Audit completed before the measured clock 08:32:01 UTC; earlier estimated message times are superseded.'),
 ('B5:finite-field-coefficient-dependency', 'part_b/b5_finite_field_coefficient_duality.md',
  'Root read the complete written proof. The Chow-heart shifts, higher-Chow indexing, negativity, signed Weil pairing, Beilinson-plus-Parshin equivalence, finite-dimensional numerical pairing, dual idempotents and P1 off-diagonal transfer pass. The stronger coefficient hypothesis is essential. Root separately read Kahn2012 Proposition10.5.1 with complete proof, Remark10.5.2, Theorem11.2.1 and its local argument, Corollary11.2.2, Lemma11.3.1 with proof, full Remark11.3.2 and Remark11.6.2, pp46–52. No full foundational construction audit is claimed.'),
 ('C6:blowup-converse-diagnostic', 'part_d/post07/bgv_semistable_blowup_diagnostic.md',
  'Root read and rechecked the complete blowup and transverse-cut diagnostic: local semistable charts, nonsplit normal exact sequence, projective-bundle restriction surjectivity, dual Gysin injectivity and cancellation of outer E2 columns. Pulled-back prescribed cycles on transverse cuts still extend from a component. The proof excludes this method, not all possible primitive constructions.'),
 ('C4-C6:logarithmic-Tate-source-scope', 'sources/root_post07/KatoNakayamaUsui2025.txt',
  'Root read Conjecture1.10, diagram1.11, the complete internal proof of Theorem2.3 through Lemmas2.4/2.6 and argument2.7, and complete section4 including Proposition4.10 proof. The specified universal logarithmic Tate and semisimplicity assumptions imply weight-monodromy. Conjectures4.2/4.12 remain conjectures, and neither realizes an arbitrary finite-field cycle as monodromy of a pure local algebraic motive. No exact converse is inferred.')
]
path = root/'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as handle:
    rows = list(csv.DictReader(handle, delimiter='\t'))
for label, filename, outcome in checks:
    if not any(r['statement_id']==label and r['outcome']==outcome for r in rows):
        rows.append(dict(statement_id=label, date=now, who='GPT-6 Astra / root / current run',
                         type='targeted proof check', outcome=outcome))
with path.open('w', newline='') as handle:
    writer=csv.DictWriter(handle, fieldnames=['statement_id','date','who','type','outcome'], delimiter='\t')
    writer.writeheader(); writer.writerows(rows)
out = dict(recorded_utc=now, checks=[dict(statement_id=l, file=f,
           sha256=hashlib.sha256((root/f).read_bytes()).hexdigest(), outcome=o) for l,f,o in checks],
           movement='None of these audits closes an open row or proves a strictly smaller universal gate.')
(root/'code/record_root_late_cp08_audits_output.json').write_text(json.dumps(out, indent=2)+'\n')
note='''

## Further proof and source audits before checkpoint08

The integrated B1 proposition gives complete counterexamples to two limit arguments. The first exhibits an invariant infinite-support continuous Kummer class outside the colimit over fixed opens; the second constructs a non-root-of-unity Frobenius eigenvalue after completion. These are method obstructions, not counterexamples to B1 itself. The fixed-orbit direct-sum permutation calculation is separately preserved.

The B5 coefficient note proves the exact Beilinson--Parshin dependency for the specified rational Weil extension of every Chow-heart object, with the point's degree-one pairing and the P1 degree-three pairing. It expressly does not infer the same necessity from homogeneous pure coefficients without actual Chow--Kunneth decompositions. Root checked the complete written argument and the exact Kahn primary-source passages listed in the audit output. The universal arithmetic realization gate remains open.

The complete blowup diagnostic shows why occurrence among semistable strata is insufficient for the C6 converse: the added terms cancel, and the direct pullback of a prescribed cycle still vanishes in the relevant restriction cokernel after transverse cuts. A new primitive construction is not ruled out. Root also read Kato--Nakayama--Usui2025 Theorem2.3 with its full local proof and section4. Its stated logarithmic Tate and semisimplicity assumptions give a sufficient weight--monodromy route, not a pure-local realization of arbitrary cycles. Exact version, pages and read limits are in the bibliography and check ledger.

No qualifying formal-review movement is claimed for these additions. Earlier estimated root message times for the B1/B5 audits are superseded by the actual clock-based records.
'''
for filename in ['RESEARCH_SA05_report.md','PROGRESS_LEDGER.md','ROOT_CURRENT_SOURCE_RECHECK.md']:
    path=root/filename
    text=path.read_text()
    if '## Further proof and source audits before checkpoint08' not in text:
        path.write_text(text+note)
print(json.dumps(out, indent=2))

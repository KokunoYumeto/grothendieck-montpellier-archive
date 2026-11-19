"""Record actual written-proof and primary-source checks after checkpoint07."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
records = [
    ('c:threefold-target-positivity', 'part_c/c4_target_positivity.tex',
     'Root read the complete written proof. The finite-Q numerical corner, right ideal fN, mixed trace pairing, actual primitive intersection, modified adjoint pairing and radical-projector contradiction pass. Root then read Morihiko Saito2003 complete sections4.1–4.3, pp14–16, and Jannsen1992 Theorem1 with Lemmas1–2 and complete proof, pp448–449. No source semisimplicity or rationality of an arbitrary Q_l subspace is inferred.'),
    ('c:local-global-motive-approximation', 'part_d/c6_global_local_reduction.tex',
     'Root read the complete written proof and Kisin Theorem5.1, Proposition5.2 and their full local proofs, authorpp16–17 with surroundingp18. Krasner gives a dense number subfield; regular spreading, lisse projector identities, stable lattices, finite-prime neighbourhood intersection, etale-chart algebraic approximation and exact completion all pass. This does not construct a pure motive from an arbitrary compact analytic object.'),
    ('c:bgv-pure-local-boundary', 'part_d/post06/bgv_converse_scope_audit.md',
     'Root read the complete square-zero analytic encoding and scope audit. Also read complete BGV Lemmas2.13/2.17, Proposition4.13, Corollary4.14, Proposition4.25 and Corollary4.33 with their internal proofs, and Remark4.61. Compactness and the cycle-class monodromy block pass. The analytic weight heart is not all pure generic motives. Original foundational dependencies are not independently reproved.'),
]
path = ROOT/'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as handle:
    rows = list(csv.DictReader(handle, delimiter='\t'))
for label, filename, outcome in records:
    if not any(r['statement_id']==label and r['outcome']==outcome for r in rows):
        rows.append({'statement_id':label,'date':now,'who':'GPT-6 Astra / root / current run',
                     'type':'targeted proof check','outcome':outcome})
with path.open('w',newline='') as handle:
    writer=csv.DictWriter(handle,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    writer.writeheader();writer.writerows(rows)
result = {'recorded_utc':now,'audits':[{'label':label,'file':filename,'sha256':hashlib.sha256((ROOT/filename).read_bytes()).hexdigest(),'outcome':outcome} for label,filename,outcome in records],
          'current_source_checks':{
             'FlachKrauseMorin2026':'Complete section7.1 statements/local proofs, Theorem7.2.3 complete concluding proof, and exact additional locators in root_post07_sources.bib. Global L(X_et,n) and complementary finiteness hypotheses remain; local prismatic comparison does not establish arbitrary prescribed global motivic regulators.',
             'AwadaBolognesiLaterveerPedrini':'Current v3 full Theorems3.5/3.7 local proofs and specified family statements checked. Complex-topological density and high-Picard-rank families do not reverse Chow specialization or prove the general determinant.'},
          'review_scope':'Useful verified refinements and failed-route audits; no new qualifying movement is pre-counted.'}
(ROOT/'code/record_root_post07_audits_output.json').write_text(json.dumps(result,indent=2)+'\n')
entry='''

## Fourth review interval: independently checked refinements

Root read the complete new target-only positivity proof and the exact primary standard-conjecture arguments in Morihiko Saito2003 sections4.1–4.3, pp14–16, and Jannsen1992 Theorem1 with Lemmas1–2, pp448–449. The proof uses a finite-dimensional rational numerical corner and the Lefschetz-modified pairing. It does not infer rationality from a Q_l-linear projector or assume the ordinary intersection form is positive on all H2.

Root also read the complete finite-prime local/global approximation proof and Kisin's original Theorem5.1 and Proposition5.2 with their local proofs. A dense number subfield and an etale chart yield an algebraic nearby point with exactly the original p-adic completion; the projected local system itself is held fixed. This removes a globalization obligation from the analytic converse route, but leaves pure local realization unresolved. The full BGV square-zero encoding and the relevant internal compactness, equivalence and weight-heart proofs were read separately. No arbitrary analytic object is declared pure.

The fresh arithmetic source check opened Flach–Krause–Morin2026. Their local Tate determinant theorem and global syntomic comparison retain the global motivic finite-generation assumptions in Conjecture7.1.1 and Proposition7.1.2. The main B5 prescribed realization gate is therefore unchanged. The current Awada–Bolognesi–Laterveer–Pedrini paper has specified high-rank and four-dimensional families; its density theorem does not reverse specialization and does not settle the general K3 exterior projector. Exact primary locators, actual read scope, failed initial retrieval and successful downloads are recorded. None of these source checks is counted as mathematical movement.
'''
for name in ['RESEARCH_SA05_report.md','PROGRESS_LEDGER.md','ROOT_CURRENT_SOURCE_RECHECK.md']:
    path=ROOT/name
    content=path.read_text()
    if '## Fourth review interval: independently checked refinements' not in content:
        path.write_text(content+entry)
print(json.dumps(result,indent=2))

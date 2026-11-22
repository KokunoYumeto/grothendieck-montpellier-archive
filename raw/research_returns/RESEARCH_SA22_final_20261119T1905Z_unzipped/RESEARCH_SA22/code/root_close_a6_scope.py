"""Record the completed A6 scope repairs and the exact finite-check boundaries."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,time

R=Path(__file__).resolve().parents[1];start=time.perf_counter();now=datetime.now(timezone.utc)
outpath=R/'code/root_close_a6_scope_output.json';assert not outpath.exists()
cert1=json.loads((R/'code/part_c_a6_scope_certificate_output.json').read_text())
cert2=json.loads((R/'code/part_c_a6_frobenius_certificate_output.json').read_text())
assert cert1['assertion_count']==21 and cert2['assertion_count']==20
assert all(x['passed'] for x in cert1['checks']+cert2['checks'])
gaps=json.loads((R/'notes/live_mathematical_scope_gaps.json').read_text())
closures={
 'A6-mixed-characteristic-specialization':(['A6-tame-specialization','A6-wild-counterexample'],'closed: tame comparison and model independence proved; unrestricted finite-etale strengthening refuted'),
 'A6-nonsplit-node-character':(['A6-node-character'],'closed: exact cyclotomic-times-branch-sign character proved and unqualified assertion refuted'),
 'A6-anabelian-specialization-preservation':(['A6-frobenius-counterexample'],'closed: strict preservation refuted by explicit relative-Frobenius pair over F16 with number-field lifts')}
for sid,(statements,status) in closures.items():
 g=next(x for x in gaps if x['id']==sid);assert g['status'].startswith('open:')
 g.update(status=status,closed_utc=now.isoformat(),statements=statements,
  proof='sections/part_a6_scope_supplement.tex',
  audit='notes/root_post_review03_proof_audit.md',
  certificates=['code/part_c_a6_scope_certificate_output.json','code/part_c_a6_frobenius_certificate_output.json'])
(R/'notes/live_mathematical_scope_gaps.json').write_text(json.dumps(gaps,indent=2)+'\n')
with (R/'notes/root_post_review03_proof_audit.md').open('a') as f:
 f.write('''

## Strict anabelian preservation under specialization

Root read the completed fourth proposition and the20-assertion F16 output, then reopened Stacks Proposition58.8.4, Tag0BQN, including its proof (turn551278569view0). The map is relative Frobenius over k, fixing constants and sending w to z²; it is a finite radicial surjection, so the category equivalence commutes with G_k augmentation. The irreducible quartic is T⁴+T+1. The six computed crossratio values exclude a²; the proof also excludes them uniformly by the degree≤3 equations they would imply. The primitive order15 element gives the stated prime of Z[zeta15] over2 with residue F16, and the separable reduction of T¹⁵−1 proves the unramified DVR/lift claim. Both four-point complements lift with disjoint sections. The conclusion refutes preservation of the same strict Isom-anabelian definition; it does not deny formulations which explicitly allow Frobenius ambiguity.

The21 rational/integer assertions and20 finite-field assertions check the advertised counterexample data only. The actual local Kummer, log-category, valuation, stability and source-theorem deductions remain written proofs, not claims that a script verified those theorems. No certificate was rerun by root.
''')
with (R/'checks/root_post_review03_proof_events.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t').writerow(['A6-frobenius-counterexample','2026-11-19','GPT-6 Astra (OpenAI), root, this run','targeted proof check','Read relative-Frobenius argument, all six crossratios, exact F16 certificate and Q(zeta15) good lifts; reopened Stacks0BQN. Strict anabelian preservation is refuted; formulations allowing Frobenius ambiguity are not silently included.'])
with (R/'PROGRESS_LEDGER.md').open('a') as f:
 f.write(f'''\n\n## A6 specialization and branch-character gates closed — {now.isoformat()}

The three live A6 scope rows are closed by the four statements in `sections/part_a6_scope_supplement.tex`. Mixed-characteristic specialization has the precise tame-cover comparison for every existing proper log-regular model, and valuative log-trait pullback proves independence of the chosen model without requiring a common refinement. The constant Q2(sqrt2) cover refutes the all-finite-etale strengthening. The nonsplit nodal cubic has the exact cyclotomic-times-branch-sign inertia character, refuting the unqualified cyclotomic parenthesis. The explicit F16 relative-Frobenius pair, with lifts over Q(zeta15), refutes preservation of the same strict Isom-anabelian definition. The21+20 exact certificate assertions passed; source and non-finite proof deductions are separately documented. These close genuine scope rows opened after review3; the certificates or typesetting alone are not counted as movement.

No general mixed-characteristic resolution theorem, existence of arbitrary regular models, or reconstruction of a chosen special scheme is being asserted. The supplied positive statements and explicit refutations treat these distinctions. The three prescribed original-source readings remain outstanding.
''')
out=dict(recorded_utc=now.isoformat(),closed=list(closures),new_statement_count=4,
 mathematical_certificate_assertions=41,root_reran_certificates=False,
 remaining_live_mathematical_rows=[x['id'] for x in gaps if x['status'].startswith('open:')],
 seconds=time.perf_counter()-start)
outpath.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

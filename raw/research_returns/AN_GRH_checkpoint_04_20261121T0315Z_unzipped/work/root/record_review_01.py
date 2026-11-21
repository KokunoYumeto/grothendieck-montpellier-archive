"""Record the actual first scheduled review, with every row's dated status."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib,shutil

root=Path(__file__).resolve().parents[2]
now=datetime.now(timezone.utc)
due=datetime(2026,11,21,3,15,tzinfo=timezone.utc)
if now<due:raise SystemExit('First scheduled review is not due yet.')
R=root/'final';out=R/'reviews';out.mkdir(exist_ok=True)
meta=out/'review_01.json'
if meta.exists():raise SystemExit('Refusing to overwrite an actual review.')
qpath=R/'QUESTIONS.tsv'
with qpath.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
snapshot=out/'review_01_all_rows.tsv';shutil.copy2(qpath,snapshot)
pending=[
 {'id':'Q-RANK-ONE-AUGMENTATION','source':'AN_GRH A26; recovered A1 B.1-B.2 and Successor A.10,A.35','locator':'proof_sources/rank_one_augmentation.tex','question':'Does even point-count parity yield a weaker prescribed-point rational-cover sufficient criterion?','state':'PROVED and whole-read: |J(FQ)/rJ(FQ)|>#C or r>#C with 2 primitive suffices.','finding_ids':'A26','current_gate':'The existence of a prime meeting the numerical criterion is not forced.','evidence_scope':'Checked proof retained separately; integration into the standalone paper is next.'},
 {'id':'Q-RANK-ONE-AUGMENTATION-UNIVERSAL','source':'AN_GRH A27','locator':'proof_sources/rank_one_augmentation_obstruction.tex','question':'Must the A26 numerical criterion succeed over some constant extension of every rank-one genus-two curve?','state':'REFUTED by y^2+y=u*x^3+x+u/x over F4: quotient size is strictly below the point count for every extension and primitive-2 prime.','finding_ids':'A27','current_gate':'Actual rational covers and theta incidence are not excluded.','evidence_scope':'Whole proof read by root and two same-model readers; finite inputs independently computed. Integration into the standalone paper is next.'}
]
with (out/'review_01_new_checked_rows.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(pending)
scoped=[x for x in rows if x['current_gate']]+pending
with (out/'review_01_open_and_scope_rows.md').open('w') as f:
 f.write('# First scheduled review: complete remaining-gate and scope register\n\nActual review time: '+now.isoformat()+'.\n\nEvery row with a retained gate or evidence limitation is listed below with its exact current state. A nonempty scope limitation does not make an already proved conditional theorem an open mathematical problem. The all-row TSV also retains every closed row.\n\n| ID | Current state | Remaining gate or limitation |\n|---|---|---|\n')
 def esc(s):return s.replace('|','\\|').replace('\n',' ')
 for x in scoped:f.write('| '+esc(x['id'])+' | '+esc(x['state'])+' | '+esc(x['current_gate'])+' |\n')
record=dict(review_number=1,scheduled_utc=due.isoformat(),actual_utc=now.isoformat(),
 elapsed_hours=(now-datetime(2026,11,21,0,15,tzinfo=timezone.utc)).total_seconds()/3600,
 substantive_movement=True,consecutive_reviews_without_movement=0,
 all_rows=len(rows),new_checked_rows=2,rows_with_gates_or_scope=len(scoped),
 questions_sha256=hashlib.sha256(qpath.read_bytes()).hexdigest(),
 movement=['A1 assertion closed unconditionally by A05; requested Hooley route remains separate.',
 'A18 strictly weakens the geometric sufficient gate to arbitrary odd conductor without the elliptic-quotient exception.',
 'A19 closes fixed-support search decidability; A20 and A22 refute fixed-prime and all-fixed-finite-support universal workarounds.',
 'A23 and A27 refute universal forcing of two concrete numerical sufficient tests.',
 'A26 weakens a prescribed-point rational-cover sufficient criterion using even augmentation.',
 'Identified finite GT levels certified and actual LM8 effective-bound question resolved with exact constants.'],
 next_review_utc='2026-11-21T04:15:00+00:00',
 next_steps=['Continue actual rational Fourier-cover existence, beyond failed size tests.',
 'Test new ways to force primitive orbit coverage with curve-dependent unbounded prime support.',
 'Keep missing-source and original-scan gates distinct; do not count repackaging as movement.'])
meta.write_text(json.dumps(record,indent=2)+'\n')
entry='''
## Scheduled progress review 01 — ACTUAL_TIME UTC

This is the first scheduled three-hour review, conducted at the time above, not a backdated earlier progress note. **Substantive movement: yes. Consecutive reviews without movement: 0.** Work continues. The next scheduled review is 04:15 UTC.

### Current gates of the four requested questions

| Main question | Current state | Strongest remaining gate |
|---|---|---|
| A1, with particular priority on the Hooley route | The exact assertion is proved unconditionally by A05. The requested derivation through Hooley remains unproved. | For each positive-rank finite-field genus-two curve, force an odd cyclic cover whose primitive factor has geometric 2-rank zero, equivalently enough theta multiples to meet every primitive doubling orbit; A18 removes the elliptic-double-quotient exception. A26 provides a separate prescribed-point rational Fourier criterion. Hooley supplies candidate orders only. A22 excludes any uniform fixed finite prime support. A23 and A27 show two proposed sufficient size inequalities need not succeed over any extension. |
| Every analytically dependent programme row | Every supplied flag, all 800 recovered full register statements and the 108 curated analytic entries are classified at the available evidence level. | 390 complete statements and 209 further LM7 proof blocks remain unavailable. Term screening is not a proof-independence certificate. Exact arithmetic consequences are proved where reconstructable; no exhaustive proof review of missing sources is claimed. |
| Finite GT cyclotomic certificates | All 53 identified numerical moduli have exact coefficient-2 unit-word certificates; two infinite families are proved. The applicable uniform Bach theorem uses coefficient3. | The missing GT register prevents identifying every original quotient; a multiplier certificate does not certify the noncyclotomic GT relations. The remaining interval below exp300 is not exhaustively checked for a uniform coefficient2 theorem. |
| Effective Galois images and trace separation | Exact G01-G06 consequences and actual LM8 constants are proved with all hypotheses. General Dedekind-GRH consequences are conditional on M; the specified abelian cases use A. | Numerical application to further unavailable rows needs their representations, fields, ramification and discriminants. Trace tests determine semisimplifications, and the stronger extension-class claim is refuted by G04. |

### Every remaining row and the movement decision

The complete dated status snapshot is [review_01_all_rows.tsv](reviews/review_01_all_rows.tsv). The two newly checked A26-A27 rows awaiting paper integration are [review_01_new_checked_rows.tsv](reviews/review_01_new_checked_rows.tsv). Every row with any retained gate or evidence limitation appears individually, with its state and exact gate, in the ledger annex [review_01_open_and_scope_rows.md](reviews/review_01_open_and_scope_rows.md). These are part of this dated review, not a fresh assertion that every scoped row is mathematically open. Source hashes and counts are in [review_01.json](reviews/review_01.json).

Movement is supported by actual closed questions and smaller gates: A05 closes the A1 assertion; A18 removes a geometric exception and permits arbitrary odd conductor; A19 makes each fixed-support search finite; A20 and A22 close proposed fixed-support solutions negatively; A23 and A27 close universal-forcing questions for two numerical tests negatively; A26 removes an extra pair-count inequality from a rational prescribed-point criterion. The identified GT certificate and actual LM8 constant questions have also closed. A24's further necessary congruence restrictions, illustrative examples, compilation and packaging are not needed for this movement decision.

The current standalone source and 74-page PDF match exactly through A25 and pass structural/build validation. A26 and A27 are complete checked proof sources retained alongside them and will be integrated next. Complete same-model proof readings are recorded; effort is not exposed, and no independent-model or formal verification is claimed.

Next work attacks actual rational Fourier witnesses and curve-dependent primitive orbit coverage. Failure of a sufficient numerical test is not treated as absence of covers. Original scans and missing full source rows remain separate evidence gates. No final return is made at this review.
'''.replace('ACTUAL_TIME',now.strftime('%Y-%m-%d %H:%M:%S'))
with (R/'LEDGER.md').open('a') as f:f.write(entry)
with (root/'AN_GRH_SESSION_STATE.md').open('a') as f:
 f.write('\n## Actual first scheduled review\n\n'+now.isoformat()+': review01 recorded, substantive movement yes, consecutive no-movement count0. All-row and every-gate snapshots retained under final/reviews. Next review04:15UTC; checkpoint04 due now03:15. Standalone source and74-page PDF match throughA25; A26/A27 complete whole-read sources await paper/table integration. Root events101; merged events may grow as final audit fragments arrive. Active next route is rational Fourier existence beyond failed size inequalities.\n')
print(json.dumps(record,indent=2))

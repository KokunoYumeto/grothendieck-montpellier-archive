"""Record the proved raw-toric non-descent and the separate anabelian-preservation reading."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,time

R=Path(__file__).resolve().parents[1];start=time.perf_counter();now=datetime.now(timezone.utc)
outpath=R/'code/root_live_scope_update04_output.json';assert not outpath.exists()
gaps=json.loads((R/'notes/live_mathematical_scope_gaps.json').read_text())
g=next(x for x in gaps if x['id']=='A1-raw-toric-isotopy-descent')
assert g['status'].startswith('open:')
g.update(status='closed: refuted with a complete analytic family and exact deterministic phase specification',
 closed_utc=now.isoformat(),statements=['A1-pant-third-jet','A1-four-point-plumbing-jet','A1-toric-nondescent'],
 proof='sections/part_a567_toric_descent.tex',
 audits=['notes/part_b_toric_descent_audit.md','notes/root_post_review03_proof_audit.md'],
 qualification='N=min{n>=1:Delta(exp(i/n))!=0} is proved to exist and specifies the exact phase; N was not numerically evaluated. No finite-group enumeration or numerical welding certificate is claimed.')
new=dict(id='A6-anabelian-specialization-preservation',opened_utc=now.isoformat(),
 status='open: explicit relative-Frobenius counterexample and finite-field certificate being prepared',
 claim='The strict characteristic-zero Isom-anabelian definition is preserved under positive-characteristic arithmetic specialization.',
 issue='Equivalence of tame-cover categories does not imply preservation of strict geometric reconstruction; relative Frobenius preserves etale categories while it can change the curve.',
 gate='Give two nonisomorphic F16 four-punctured lines with a base-compatible relative-Frobenius group isomorphism and verified characteristic-zero lifts.',
 affects=['A.6(a),049(c) stronger reconstruction reading'])
assert not any(x['id']==new['id'] for x in gaps);gaps.append(new)
(R/'notes/live_mathematical_scope_gaps.json').write_text(json.dumps(gaps,indent=2)+'\n')
note='''# Root proof review after hourly review3

## A1 raw toric descent

Root read the entire three-statement fragment and Part B's independent coefficient derivation. The cusp form of the Schwarzian is explicitly justified by the parabolic developing coordinate, rather than silently applying a positive-length-only statement at zero. The third cap jet is 5/16+1/[16(lambda²+4)]. The normalized four-point plumbing coefficient is symmetric in the two third jets; the general hand checks include a single changed coordinate and the Möbius special case. The Laurent calculation is made with small fixed node discs, so evaluation at the marked points is legitimate.

The cap collars give honest coordinate discs of radii r exp(delta/(2lambda)), strictly greater than r. Hence the phase circle lies inside the holomorphic plumbing parameter disc. A nonzero cubic coefficient proves that the two cross-ratio functions differ, and only finitely many unit phases can be exceptional. The exact choice N=min{n>=1:Delta(exp(i/n))!=0} exists by the identity theorem at the accumulation point1. This is a fully specified analytic rule; no numeral for N or numerical cross-ratio value is asserted.

The balanced comparator has a geodesic seam. The unequal surface's own seam and its own unique geodesic are thus the two cuts in the same fixed labelled X: equality of their raw tensor would contradict the already proved injectivity of geodesic reconstruction and the cross-ratio difference. This avoids the invalid inference from fixed-target fiber dimension to fixed-X variation. The case uses stable type(0,4), analytic seams, positive radii in(0,4), fixed external labels and the actual tensor phase. Root found no remaining gap after the two local typing clarifications were applied.

## A6 source and proof review

Root separately read the full three-statement mixed-characteristic/branch-character supplement. The Hoshi author preprint RIMS1558 was reopened directly: Corollary3.9 printedpp31–32 (web lines2451–2478, followed by its proof) and PropositionA.10 printedpp57–58 (lines5201–5329). The latter's definition uses codimension-one boundary valuations, its proof identifies the divisorial log structure, and its essential-surjectivity step invokes log purity. These are the exact hypotheses used in the supplement.

Root checked the valuative comparison between any two existing proper log-regular models, the log morphism from each boundary valuation trait, the tame Galois quotient and uniformizer-framed section, the Q2(sqrt2) constant-cover obstruction, and the nonsplit nodal cubic with branch sign. All are correctly distinguished from full geometric fundamental groups, existence of arbitrary mixed-characteristic regular models and preservation of a strict Isom-anabelian definition. The last issue is being treated as its own explicit relative-Frobenius counterexample, not assumed from the category equivalence.

Source retrieval references for the root reopening: turn824068644view0; turn751185945view0 and turn751185945view1. This note records source access and proof review, not a claim to have checked the entire Hoshi paper. Literature search metadata is in `code/root_a6_scope_literature_search.json`; related Kerz–Schmidt work was identified but not added as an unopened proof premise.
'''
(R/'notes/root_post_review03_proof_audit.md').write_text(note)
with (R/'checks/root_post_review03_proof_events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
 for sid,outcome in [
 ('A1-pant-third-jet','Checked parabolic-cusp extension, Schwarzian coefficient matching and radius inverse; no use of a positive-length-only theorem without its cusp argument.'),
 ('A1-four-point-plumbing-jet','Read full convergent Laurent derivation, small-disc evaluation convention and independent general-coefficient hand audit; coefficient identity is not a numerical approximation.'),
 ('A1-toric-nondescent','Checked exact radius choices, strict cubic gap, honest phase disk, unevaluated deterministic N rule and the unequal-X seam versus its own geodesic. No finite-group or numerical phase certificate is claimed.'),
 ('A6-tame-specialization','Read supplement and reopened Hoshi Cor3.9/PropA.10; checked proper valuative log-trait comparison, tame arithmetic quotient and framed section within the stated existing-model scope.'),
 ('A6-wild-counterexample','Checked Q2(sqrt2) constant etale cover, Eisenstein normalization and ramification index2 at the vertical divisor; no stronger resolution claim used.'),
 ('A6-node-character','Checked branch interchange inverses, cyclotomic-times-sign character, explicit rational nonsplit node and invariant nonzero normal tensor; distinct from the node Dehn-twist character.')]:
  w.writerow([sid,'2026-11-19','GPT-6 Astra (OpenAI), root, this run','targeted proof check',outcome])
with (R/'PROGRESS_LEDGER.md').open('a') as f:
 f.write(f'\n\n## Raw toric isotopy gate closed; separate specialization reading recorded — {now.isoformat()}\n\nA1-raw-toric-isotopy-descent is refuted by the three-statement cap-jet/plumbing comparison in `part_a567_toric_descent.tex`. The source heuristic that reciprocal cap-size changes preserve the welded surface is false. The exact analytic phase rule is explicit and unevaluated; all but finitely many unit phases in the given family also work. Geodesic replacement is the proved positive convention. Independent Part B derivation and root proof checks are saved. This is a real open-row status change after review3.\n\nA6-anabelian-specialization-preservation is recorded as a separate open stronger reading, pending a relative-Frobenius counterexample overF16 and its exact certificate. It is not inferred from, or confused with, the tame cover-category comparison.\n')
out=dict(recorded_utc=now.isoformat(),closed=['A1-raw-toric-isotopy-descent'],opened=[new['id']],
 root_targeted_events=6,seconds=time.perf_counter()-start)
outpath.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

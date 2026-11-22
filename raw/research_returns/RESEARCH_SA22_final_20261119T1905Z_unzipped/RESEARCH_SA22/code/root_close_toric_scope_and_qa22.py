"""Record the completed unequal-toric proof review and actual build22 visual QA."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, time

R=Path(__file__).resolve().parents[1]
started=time.perf_counter()
now=datetime.now(timezone.utc)
target=R/'code/root_close_toric_scope_and_qa22_output.json'
assert not target.exists(), 'This completion record is immutable.'
render=json.loads((R/'code/root_render_current_22_output.json').read_text())
seen=[1,3,12,13,14,15,16,23,34,59,72,80,94,110,127]
assert seen==render['rendered_pages']
assert all(x['exit_code']==0 for x in render['results'])
pdf=R/'RESEARCH_SA22_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==render['pdf_sha256']
log=(R/'logs/RESEARCH_SA22_paper.log').read_text()
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
undefined=len(re.findall(r'Warning:.*(?:Citation|Reference).*undefined|There were undefined references',log))
missing=log.count('Missing character:')
assert not over and not undefined and not missing
qa=dict(build=22,pages=127,pdf_bytes=pdf.stat().st_size,sha256=render['pdf_sha256'],
 build_log='logs/build_22.out',final_tex_log='logs/RESEARCH_SA22_paper.log',
 historical_overfull_above_2pt_before=[26.38113,5.72717],overfull_boxes_after=0,
 undefined_references_or_citations=0,missing_characters=0,rendered_pages=seen,
 visually_inspected_pages=seen,
 visual_result='All fifteen current-build pages were actually displayed and inspected by root. Pages12-16 cover the new unequal-toric proof and its transition; the sample also covers A2, the A6 model-system proof, B1b, Gabber, the B3 catalogue, C2 and the bibliography. No visible clipping, overlap or unreadable text/formulas. The wholly truncated initial attempted display of15,16,23,34,59 was not counted; those pages were displayed again successfully.',
 build_timing_record='code/root_timed_build_22_output.json',
 render_timing_record='code/root_render_current_22_output.json',
 verification_time_utc=now.isoformat())
for name in ['logs/typesetting_current.json','logs/typesetting_build22.json']:
 (R/name).write_text(json.dumps(qa,indent=2)+'\n')
gaps=json.loads((R/'notes/live_mathematical_scope_gaps.json').read_text())
gap=next(g for g in gaps if g['id']=='A1-toric-independent-lengths')
assert gap['status']=='under proof audit'
gap.update(status='closed: proved exact image and fibers, with a counterexample to injectivity',
 closed_utc=now.isoformat(),statements=['A1-toric-domain','A1-toric-noninjective','A1-toric-full-discs'],
 proof='sections/part_a567_toric_unequal.tex; build22 Theorem1.13, Proposition1.14 and Corollary1.15, pp12-15',
 audits=['notes/part_a567_a1_global_domain_audit.md','notes/part_b_unequal_toric_audit.md','notes/root_toric_scope_resolution.md'])
(R/'notes/live_mathematical_scope_gaps.json').write_text(json.dumps(gaps,indent=2)+'\n')
note='''# Unequal-toric definition gap: resolution

Root read the full new proof and the independent Part B audit, then checked the integrated build22. Toric compatibility identifies normalized angular coordinates; it does not equate paired canonical hyperbolic lengths. The previously overbroad scope sentence in `sections/part_a1_cut_choice.tex` now explicitly requires equal lengths before invoking the geodesic theorem.

For independent halfedge squared lengths, the full cap-logarithm map is the proved gradient diffeomorphism F onto D_Y. The projection P_* sums the two logs at each node. Its image is exactly the previously proved support region: component support inequalities give one inclusion, and the equal-length inverse gives the other. Its fibers in cap logs are nonempty open convex affine sections of dimension |E|.

The stronger global real-analytic parameterization by d_e=s_+-s_- was checked separately. For each prescribed d the shifted positive-orthant potential has positive Hessian and unchanged recession slopes. Strict support inequalities exclude unbounded minimizing sequences; an affine lower bound and lower-semicontinuous closure give a minimum; the uniform negative divergence of a vanishing cap's log excludes every finite boundary minimum. The unique interior critical point depends analytically on (y,d), including d=0. Tensor phases determine the seam identifications. Finite automorphisms act by signed edge permutations, so only the marked fiber, not every coarse quotient fiber, is asserted to be a vector space.

The proof uses **all seams geodesic** for its converse identifying d=0. It does not infer inherited canonical metrics from a single geodesic among nongeodesic cuts. Root checked the added dimension calculation, the empty active-set case and the restriction of the universal R^E-fiber statement to tensors plus external shadows. Full external discs require the stated exact matching condition.

The analytic counterexample is completely specified by radius pairs (1,1) and (2,1/2) on two labelled two-cusp pants, with phase1. Both give q=1; their cut-component lengths distinguish the cut objects. It does not assert distinct underlying uncut surfaces. It is not a finite enumeration and no finite mathematical program was run for it.

Root also actually viewed original physical scans67/079-082. These record the nongeodesic qualification, polar-rescaling discussion and the proposed fundamental-group/tangent tests. On these four images the printed archive footers are78-81 and the lower-left handwritten numbers are81-84; locators in this work consistently use the physical PDF scan number. No blanket interpretation of every folio number is inferred from this four-page observation.

Literature-check scope is separately recorded by `code/root_toric_literature_search.json` and `code/root_toric_literature_verify.json`: three preliminary and two verifying queries. They did not identify this exact global fiber statement, and establish no priority or exhaustive absence claim. All proof dependencies are the opened results already used for A1/A2.
'''
(R/'notes/root_toric_scope_resolution.md').write_text(note)
with (R/'checks/root_toric_scope_events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
 for sid, outcome in [
 ('A1-toric-domain','Root checked the projection image, global shifted-potential inverse, boundary/recession arguments, signed automorphisms, dimensions and all-seams geodesic converse; independent Part B audit read; no remaining gap identified in the stated scope.'),
 ('A1-toric-noninjective','Root verified the explicit analytic radius-pair construction, labelled cut-component invariant and distinction between cut objects and underlying uncut surfaces.'),
 ('A1-toric-full-discs','Root verified necessity and sufficiency of external-cap shape matching; the unrestricted R^E fiber is not transferred to a full-shape target.'),
 ('SA22-7','Root visually read original physical scans67/079-082 and checked the nongeodesic, polar-rescaling and tangent/fundamental-group passages against the scope correction.')]:
  w.writerow([sid,'2026-11-19','GPT-6 Astra (OpenAI), root, this run','targeted proof check',outcome])
with (R/'PROGRESS_LEDGER.md').open('a') as f:
 f.write(f'\n\n## A1 definition-scope gap closed — {now.isoformat()}\n\nThe live row A1-toric-independent-lengths is closed by Theorem1.13, Proposition1.14 and Corollary1.15 (build22, pp12–15). Independent-length toric cuts have the exact same tensor/shadow image and global real-analytic R^E fibers; their tangent kernel has dimension E and their equivariant retract preserves the fundamental-group comparison. The explicit q=1 pair refutes injectivity. The original equal-length theorem is retained with its hypothesis made explicit. Full external disc shapes have the separate exact matching criterion. Root and Part B proof reviews are recorded, as are the actual original-scan readings. This resolves a genuinely open definition branch found after checkpoint06, rather than counting typesetting or rechecking as movement.\n')
out=dict(recorded_utc=now.isoformat(),closed_gap=gap['id'],qa=qa,seconds=time.perf_counter()-started)
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(closed_gap=gap['id'],build=22,pages=127,visual_pages=len(seen),seconds=out['seconds']),indent=2))

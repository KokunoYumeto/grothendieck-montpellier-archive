from pathlib import Path
import csv, hashlib
from datetime import datetime, timezone

root=Path(__file__).resolve().parent
stamp=datetime.now(timezone.utc).isoformat()
qpath=root/'QUESTIONS.tsv'
with qpath.open() as f:
 reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
by={r['id']:r for r in rows}
def change(key, **kwargs):
 by[key].update(kwargs)
def add(key, source, question, state, ids, gate, tried, next_step):
 r=dict(zip(fields,[key,source,question,state,ids,gate,tried,next_step]))
 if key in by: by[key].update(r)
 else: rows.append(r); by[key]=r

change('Q1-PH',state='SOURCE_AUDIT_COMPLETE; ATTACHED_HOMOGENEOUS_PH1_REFUTED',finding_ids='A01,F34; cited Kahle–Michałek Theorem5',current_gate='The attached VI v4 homogeneous Ehrhart PH1 is already false by a prior theorem, including an equal-rectangle example. F34 separately refutes its compact dimension bound. Later inhomogeneous formulations are distinct.',approaches_tried='Exact VI definitions and compact encoding; primary Kahle–Michałek source; explicit positive simplex growth family',next_step='Choose a valid replacement positivity/effectivity formulation and its input encoding; do not treat old PH1 as an open theorem.')
change('Q3',finding_ids='F01,F02,F03,F04,F17,F24,F32',current_gate='Finite and admissible-countable signed even-power upper criteria are proved. Opposite path-output signs, pointwise/error bounds, visibility under chosen extensions, and an independently bounded visible dual remain.',approaches_tried='Parseval; spectral poles and Cesaro; real signed even tensor powers; controlled errors; locally finite countable spectra; reciprocal-finiteness theorem')
change('Q3-GCT',finding_ids='F03,F04,F17,F19–F27,F32,F35,F36,F38,F39',current_gate='Actual rank-three action and coherent Frobenius models exist; a stack realizes one complete normalized scalar trace. Its dual is unbounded, trace inversion is not tensor inversion, and the direct collision dg category is not smooth. The missing comparison must retain designated operations, path-output signs, dual bounds and basis data.',approaches_tried='Finite normalized trace; convergent completion; explicit Artin stack; tensor inversion; coherent relative Frobenius and normalization; smooth proper noncommutative Weil test',next_step='Test action-preserving smooth categorical resolutions and fixed-parameter operator comparisons, with an explicit quantum-grade/Weil comparison.')
change('Q3-ALT',state='ORIGINAL_ACTION_MISMATCH_PROVED; SEPARATE_ACTION_REPAIR_PROVED',finding_ids='F16,F27',current_gate='F16 positive algebra map changes the original action. F27 restores that action in a localized four-character mixed Tate model; purity and designated basis remain extra.',next_step='Relate the repaired model to the specified basis and its operations.')
change('Q4',state='RESTRICTED_PURE_OBJECTS_AND_WITNESSES_PROVED; GENERAL_COMPARISON_OPEN',finding_ids='F12,F13,F28,F29,F31,F34,F37; cited IV/IP/BIP/PPS/KM',current_gate='Equal-rectangle two-row coefficients have primitive Tate objects and compressed positive witnesses with listed-row input. Old homogeneous PH1 is false; general designated canonical positivity and strict closure-multiplicity inequalities remain open.',approaches_tried='Exact rectangular sources; Young-orbit obstruction; open-orbit limitation; primitive Grassmannian projectors; compact growth; marked-tree compression',next_step='Construct a based operations comparison in the necessary GCT parameter regions and a strict closure-multiplicity inequality.')
change('Q5',finding_ids='F08,F12,F13,F18,F23,F28,F30',current_gate='An exact theta/GCT functor and endpoint identification remain absent. Integral interlacing and Young-orbit shortcuts are excluded in their stated scopes; actual tower specialization can be repaired by explicit mixing, but whole-algebra projectors do not lift.',approaches_tried='Gram projectors; additive functor chains; rational congruence examples; isolated hooks; actual nonstandard tower and mixing',next_step='Identify a theta functor with the actual module and basis operations, beyond scalar period positivity.')
change('Q6',state='DICTIONARY_INTEGRATED_FOR_CURRENT_PAPER; FINAL_SCOPE_REVIEW_PENDING',finding_ids='F01–F32,F34–F39',current_gate='Every current paper finding has a separate PartIII translation. New source and proof checks must be matched after final integration; archival anchors remain framework locators.',next_step='Fresh-review final PartIII and exact source/version locators after active mathematical additions.')
change('QNEW-H3',finding_ids='F19,F21,F25,F36,F39',current_gate='Actual algebra, right tensor lattice, commutant defect, coherent Frobenius and normalization are explicit. Direct collision category is nonsmooth; an action-preserving smooth corner resolution is being tested.',next_step='Finish the smooth corner construction and compare its Frobenius realization with designated grading and operations.')
change('Q3-NORMALIZATION',current_gate='No fixed finite Weil trace can equal 24+16/D(q^n)^2 for every n. F35 realizes this scalar sequence by an explicit finite-type stack with unbounded compact cohomology.',next_step='Construct actual operators/composition in a suitable realization and test the independent dual bound; scalar masses alone do not do this.')
change('Q4-SPHERICITY',state='PROVED_FOR_SPECIFIED_OPEN_ORBIT_METHOD; PAPER_INTEGRATED',next_step='Test other invariant algebras or geometric models; no general nonexistence theorem is claimed.')
change('Q5-TOWER',state='PROVED_DIAGONAL_OBSTRUCTION_AND_EXPLICIT_MIXING_REPAIR',current_gate='On the actual regular lattice diagonal normalization cannot put path lines into the classical constituents. Two regular 2×2 mixing blocks do repair underlying basis specialization. Classical whole-algebra projectors do not lift because the generic commutant is scalar.',next_step='Relate the repaired basis to VIII global/cell bases and an actual positive functorial structure.')
change('Q4-PRIMITIVE',state='PROVED_WITH_FULL_INDEPENDENT_CHECKS; PAPER_INTEGRATED',current_gate='Explicit rational primitive Grassmannian projector has rank p_r−p_(r−1) and actual pure Tate image. Its Schubert matrix can have negative entries; it does not identify a designated basis.',next_step='Compare primitive motive labels and operations with the requested nonstandard structure.')
change('Q3-COMPLETION',state='PROVED_UPPER_CRITERION_AND_RECIPROCAL_FINITENESS; PAPER_INTEGRATED',next_step='Use F35 actual stack to test output signs, operators and dual bounds outside the excluded finite setting.')
add('Q4-PH1-COMPACT','VI v4 Hyp1.6.4(2) p23; §1.1 p9/§3.4 p53; PPS Lemma1.3 p2','Can the stated compact dimension bound hold, even on positive plethysm rays?','REFUTED_WITH_EXPLICIT_POSITIVE_FAMILY','F34','c_k(N) counts 2x2+…+kxk=N, and every fixed bounded dilation polytope has dimension≥k−2 on O(log k)-bit input. Fully compact binary plethysm is also not #P by output length.','Growth lower bound, coordinate-projection upper bound, explicit binary-choice injection','Use a different encoding or a weaker effective target; this is independent of the prior KM existence refutation.')
add('Q3-STACK','Sun Thm1.1 p49/Ex7.4 p109; LOII §9.1 p198/Thm11.0.14 p204','Can a finite-type stack realize the actual normalized all-extension scalar trace?','PROVED_WITH_EXACT_COHOMOLOGY_AND_DUALITY','F35','X=24 points disjoint union16 copies of A6×Gm8×(BGL2)^4 has the required mass. Compact cohomology is unbounded and mixed; the actual ordinary dual has unbounded spectrum.','Groupoid mass; all compact/ordinary Tate groups; absolute moments; duality','Add actual generator operators, tensor relations and the path sign; the scalar identity alone supplies none.')
add('Q3-COHERENT-FROB','Actual F19/F21 model; F36','Does actual coherent Frobenius survive the branch collision?','OBSTRUCTION_AND_ACTION_PRESERVING_REPAIRS_PROVED','F36','Center/algebra pullback adds torsion length80(p−1) on the actual tensor module; derived pullback has nonzero Tor in every positive degree. Unit structures exist on the parameter base and normalization; finite pushforward loses the unit through that torsion.','Branch ideals and periodic resolution; relative Frobenius; regular row-basis conjugation; normalized bundles and exact Hom pushforward','Supply a coherent-to-Weil comparison retaining grading, designated operations and the path-output sign.')
add('Q4-KOH-COMPRESS','PPS v3 Def3.2 p6, Def4.4/Thm4.5 p10','Can the actual positive marked-tree rule be given polynomial witnesses with binary row lengths?','PROVED_BIJECTIVE_COMPRESSION_AND_VERIFIER','F37','At most k surviving nodes plus binary repeat counts; witness size O(k² log(k+1)+k log(nk+1)). Listed-row input is essential.','Mass-loss skeleton bound; energy identity; maximal unary-chain compression; exact inverse and canonical encoding','Identify a designated cycle/canonical basis if needed; no homogeneous Ehrhart conclusion follows.')
add('Q3-TENSOR-INVERSE','F35 stack; projective bundle formula; F38','Does reciprocal stack trace make the normalization object tensor-invertible?','REFUTED_IN_USUAL_DERIVED_WEIL_REALIZATION','F38','P1×Z has Euler trace1 but unbounded nonzero cohomology. Invertible Weil complexes are one-dimensional shifts, so none has trace q^n+2+q^(-n).','Explicit reciprocal stack; complete Tate cohomology; unbounded Kunneth; invertibility lemma; first/second trace test','Fixed-q scalar division or a different realization is possible, but must supply an independently stated operation comparison.')
add('Q3-NCWEIL','Tabuada arXiv1808.00950v7 §1/§5.1/§6.1/§7; F39','Can the direct actual collision category enter the smooth proper noncommutative Weil framework?','REFUTED_FOR_DIRECT_CATEGORY; RESOLUTION_ROUTE_ACTIVE','F39','Perf(k²×M2(k[ε]/ε²)) is proper but nonsmooth; complete periodic diagonal resolution gives HH_i≠0 in all positive degrees. Split good fibers have four-point TP.','Explicit bimodule resolution; Morita restriction; exact normalized crystalline comparison','Finish and check the Auslander smooth corner resolution retaining the actual collision action.')
with qpath.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

root_checks=[
 ('F34','agent_plethysm_dimension_gate.md','Full corrected report and generated fragment read; rechecked adjacent GL2 weights, growth and all encoding bounds.'),
 ('F34-RAY','agent_plethysm_ray_algebra.md','Whole proof read; checked every polynomial generator, cancellation, triangular inverse, localized kernel and degree-minus-index ray extraction.'),
 ('F35','agent_stack_trace_realization.md','Whole report and generated proof read; all actual Tate groups, absolute moments, Euler grouping and dual twists checked.'),
 ('F36','agent_coherent_frobenius_gate.md','Whole proof read; both pullbacks, every Tor, precise branch actions, Morita multiplicities and transported row formulas checked.'),
 ('F36-NORMALIZATION','agent_coherent_frobenius_normalization.md','Whole supplement read; normalized action equals the original restricted action, Hom pushforward is exact, and Frobenius comparison torsion is computed.'),
 ('F36-FRAGMENT','finding_F36.tex','Whole final fragment read, including normalization proof; order-two coefficient and all base distinctions checked.'),
 ('F37','finding_F37.tex','Whole proof read; rederived compression inverse, telescoping node bound, energy formula, canonical verifier and exponential literal-tree example; source definitions matched.'),
 ('F38','agent_trace_inverse_tensor_gate.md','Whole report and final generated fragment read; reciprocal stack groups, convergence, tensor-invertibility lemma and D-trace obstruction all checked.'),
 ('F39','finding_F39.tex','Complete resolution and proof checked; all kernels, HH parity and Morita restriction verified. Source locator corrected to equations7.1–7.4 and ell math-mode fixed.')
]
review=root/'REVIEW_NEW_REPORTS_ROOT.md'
with review.open('a') as f:
 f.write(f'\n## Additional complete proof checks at {stamp}\n')
 for sid,name,description in root_checks:
  p0=root/name
  if p0.exists():
   sha=hashlib.sha256(p0.read_bytes()).hexdigest()
   f.write(f'\n**{sid}**, `{name}`, SHA256 `{sha}`. PASS. {description}\n')
 f.write('\nAll these are targeted whole-proof checks, not proof-assistant verification or independent re-proofs of cited general source theorems.\n')

epath=root/'CHECK_EVENTS.tsv'
with epath.open() as f:
 er=csv.DictReader(f,delimiter='\t'); ef=er.fieldnames; events=list(er)
def event(sid,who,kind,outcome,locator):
 key=(sid,who,kind,locator)
 if any((e['statement_id'],e['who'],e['type'],e['locator_or_record'])==key for e in events):return
 events.append(dict(zip(ef,[sid,'2026-11-21',who,'GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121',kind,outcome,locator])))
for sid,name,description in root_checks:
 if (root/name).exists():
  sha=hashlib.sha256((root/name).read_bytes()).hexdigest()
  event(sid,'/root','targeted proof check','PASS. '+description+' SHA256 '+sha,'REVIEW_NEW_REPORTS_ROOT.md; '+name)
for sid,name,who in [
 ('F34','REVIEW_PH1_DIMENSION_GCT.md','/root/gct_statements'),
 ('F34-RAY','agent_plethysm_ray_algebra_review.md','/root/grothendieck_dictionary'),
 ('F36','REVIEW_COHERENT_FROBENIUS_THETA.md','/root/rectangular_and_theta'),
 ('F37','REVIEW_KOH_COMPRESSION_GCT.md','/root/gct_statements'),
 ('F39','agent_F39_fresh_review.md','/root/grothendieck_dictionary')]:
 if (root/name).exists():
  sha=hashlib.sha256((root/name).read_bytes()).hexdigest()
  event(sid,who,'targeted proof check','PASS; complete fresh proof review with scopes and version hashes in the named record. Review SHA256 '+sha,name)
for sid,loc,outcome in [
 ('SRC-KM','Kahle–Michałek EJC25(1)(2018)P1.41, Thm5/Remark6 p4; pp2–4,6','Primary theorem, reciprocity argument, version distinction and rectangular identification rechecked. Known refutation of supplied VI v4 homogeneous PH1; not a new finding.'),
 ('SRC-PPS-V3','arXiv2511.02312v3, Lemma1.3 p2; Def3.2/Prop3.4 p6; Lemma4.2 p9; Def4.4/Thm4.5 p10','Exact current v3 definitions, formulas and theorem checked; root read the displayed local proofs of4.2/4.5. General KOH/O’Hara source proof is cited, not independently certified.'),
 ('SRC-SUN-STACKS','Sun ANT6(2012)47–122, Thm1.1 p49; Def4.1 p84; Thm4.2 p85; Ex7.4 p109','Statement/applicability and explicit BGL2 compact cohomology checked; broad trace theorem is cited input, not independently reproved.'),
 ('SRC-LO-II','Laszlo–Olsson II PMIHES107(2008)169–210, §9.1 p198; Thm11.0.14 p204','Primary published source and boundedness conventions inspected; explicit application uses the stack formalism and bounded-above compact complexes.'),
 ('SRC-TABUADA-V7','arXiv1808.00950v7, §1 pp2–3; §5.1 pp13–14; §6.1 pp15–16; §7 eq7.1–7.4 p17','Smooth/proper hypothesis and normalized TP Frobenius comparison checked. Distinct framework from the unformulated Mulmuley finite-field NSRH.')]:
 event(sid,'/root','used and rechecked in this run',outcome,loc)
with epath.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=ef,delimiter='\t');w.writeheader();w.writerows(events)

with (root/'LEDGER.md').open('a') as f:
 f.write(f'''\n## {stamp}: normalized realizations and effective targets\n\nNot a scheduled progress review. No no-movement counter is advanced.\n\n- Closed the scalar stack-realization row (F35) with actual all-extension mass, complete cohomology and explicit unbounded dual. The main remaining gate now demands actual operators and a bounded visible dual, rather than an unspecified source for the scalar sequence.\n- Closed the coherent Frobenius test (F36): center/algebra pullback is nonunit with exact torsion, while parameter-base and normalized action-compatible models are unit. The remaining arithmetic comparison is explicitly distinct.\n- Closed object-level tensor inversion in the usual derived Weil category negatively (F38), and the direct smooth-proper collision-category test negatively (F39). A smooth corner-resolution repair is actively being tried; these scoped failures are not treated as a universal impossibility.\n- Corrected the old PH1 status using the known Kahle–Michałek theorem. The attached homogeneous assertion is refuted, including an equal-rectangle case. F34 separately refutes the compact dimension and fully binary #P targets. Later inhomogeneous formulations are left distinct.\n- Closed the listed-row marked-tree witness-encoding row positively (F37). F29–F32 are fully integrated; the tower mixing repair and primitive Tate object are retained.\n- F34's actual polynomial highest-weight ray algebra is proved and freshly checked; its final fragment is being prepared.\n\nThe first scheduled three-hour review is still due at02:00UTC/03:00Europe-Berlin. Checkpoint03 is due at01:15UTC/02:15Europe-Berlin. Packaging and these prose updates are not counted as mathematical movement.\n''')

readme=(root/'README.md').read_text()
readme=readme.replace('The paper now integrates F01–F28','The paper now integrates F01–F32 and F34–F39')
readme=readme.replace('Further checked reports currently being integrated cover the actual nonstandard branching tower, primitive Grassmannian coefficient motives, and the countable-spectrum/visible-duality extension. They do not settle the designated nonstandard canonical-basis comparison.', 'The actual nonstandard branching tower, primitive Grassmannian coefficient motives, and countable-spectrum/visible-duality extension are integrated. Explicit stack traces, coherent Frobenius repairs, tensor-inversion obstructions and the smooth proper category test now sharpen the realization gate. A smooth corner-resolution repair remains active. The known Kahle–Michałek theorem refutes the attached homogeneous PH1; the current package distinguishes that closed historical target from later formulations. None of these results settles the designated canonical-basis comparison.')
(root/'README.md').write_text(readme)
imp=(root/'IMPLICATIONS.md').read_text().replace('The paper integrates findings F01–F28, with newer reviewed extensions being incorporated','The paper integrates findings F01–F32 and F34–F39')
imp=imp.replace('**Current further work.** Reviewed reports now also treat the failure of diagonal normalization of a specific nonstandard tower path basis at rank4, a rational primitive Grassmannian projector for two-row-output rectangular coefficients, and countable absolutely convergent Euler spectra. These will be integrated with their full proofs and exact final-text check records. The first scheduled three-hour review has not yet occurred.', '''**Tower and primitive objects.** F30 now supplies the complete rank-four mixing repair, while proving that its classical projectors do not lift to whole-algebra projectors. F31 gives the actual primitive Grassmannian Tate motive. F32 extends the signed upper criterion to admissible countable spectra and proves that bounded reciprocal duality forces their visible spectrum to be finite.

## Normalization, actual traces and current effective targets

F35 realizes the entire normalized word-trace sequence by the finite-type stack X=24 points disjoint union16 copies of A6×Gm8×(BGL2)^4. Its computed compact cohomology is unbounded and mixed. Verdier duality exists; its ordinary dual has unbounded positive Frobenius roots. Thus the remaining sign-only gate is the independent dual bound and actual operator/path comparison, not existence of a scalar mass.

F36 computes a second-order coherent Frobenius defect: center/algebra pullback adds torsion of length80(p−1) on the actual tensor module. A unit parameter-base structure and a unit normalized model both preserve the actual action. Pushforward through the collision loses the unit by the calculated torsion. These are coherent statements; they do not identify quantum degree with an ℓ-adic weight.

F38 proves that an inverse convergent Euler trace is not an actual tensor inverse. The explicit reciprocal stack times P1 has trace1 but unbounded nonzero cohomology. In the usual derived Weil category every invertible object is a one-dimensional shift, so none can have trace q^n+2+q^(−n). Fixed-q scalar division remains possible and requires a different comparison. F39 tests the modern smooth proper noncommutative Weil conjecture precisely: the actual collision category is nonsmooth, whereas good split fibers have four-point normalized TP. An action-preserving smooth corner-resolution repair is now being pursued.

The supplied VI v4 homogeneous PH1 is already false by Kahle–Michałek, Theorem5 and Remark6, p4, with its equal-rectangle interpretation on p6. This known refutation is now explicit in the paper and question ledger. Their pp3–4 distinguish later inhomogeneous polytope families; the earlier theorem does not refute every such family. F34 proves a separate compact-dimension obstruction on a positive simplex family and an output-length obstruction to fully compact binary plethysm #P. F37 proves a bijective polynomial-size compression of the known PPS marked-tree witnesses when rectangle rows are explicitly listed. Positive rules, computational encodings and homogeneous Ehrhart models therefore have different exact statuses.

Every current finding has a separate PartIII translation with exact source/framework anchors. The new stack and dg constructions use the named modern extensions of Grothendieck's frameworks; none is attributed to an archival leaf. The first scheduled three-hour review has not yet occurred.''')
(root/'IMPLICATIONS.md').write_text(imp)
print(f'Updated {len(rows)} question rows and {len(events)} check events at {stamp}.')

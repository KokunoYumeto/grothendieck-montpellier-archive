from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv

ROOT=Path(__file__).resolve().parent.parent
stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=ROOT/'work/build_package.py';s=p.read_text()
assert 'work/root/fat_linear_arrangement_model.md' not in s
s=s.replace("'work/theta/outer5/two_row_line_correction_report.md',", "'work/theta/outer5/two_row_line_correction_report.md','work/theta/outer5/stable_defect_cohomology_report.md','work/theta/outer5/three_defect_positive_report.md',")
s=s.replace("'work/root/five_row_interior_nonvanishing.md'])", "'work/root/five_row_interior_nonvanishing.md','work/root/fat_linear_arrangement_model.md','work/theta/fat_arrangement_product_report.md','work/root/first_power_zero_twist_report.md','work/root/five_row_strict_nonvanishing.md'])")
s=s.replace("'work/rectangular/canonical_next_row_below_square.md',", "'work/rectangular/canonical_next_row_below_square.md','work/rectangular/canonical_cofactor_endpoint_strip.md','work/rectangular/canonical_second_cofactor_endpoint.md','work/rectangular/canonical_second_cofactor_strip.md',")
reviews=['HIGHER_IDEAL_POWERS_REVIEW.md','EVEN_INCREMENT_AND_INTERIOR_REVIEW.md','STABLE_DEFECT_REVIEW.md','THREE_DEFECT_REVIEW.md','FAT_ARRANGEMENT_REVIEW.md','FAT_PRODUCT_REVIEW.md','STRICT_NONVANISHING_REVIEW.md']
newreviews=[str(Path('work/archive')/name) for name in reviews if (ROOT/'work/archive'/name).exists()]
s=s.replace("'work/archive/STAIRCASE_PROOF_REVIEW.md'])", "'work/archive/STAIRCASE_PROOF_REVIEW.md',"+','.join(repr(v) for v in newreviews)+"])" )
old="T045 also evaluates c=2k−1 for all valid shapes; T046 evaluates c=2k−2 for k≥5 through its actual line restriction. G023 evaluates every central staircase. Remaining direct region is the strict central cone after these removals; evaluate its remaining actual H1 corrections and finite-group covariants."
new="T045 evaluates all c=2k−1; T046 evaluates c=2k−2 for k≥5; T048 evaluates c=2k−3 for k≥8; G026 evaluates the entire first-power zero-twist two-row slice; G023 evaluates every staircase. G027 and T049 replace every remaining unspecified flag-cohomology rank by an exact fat-arrangement product ideal, diagonal quotient, and48 signed table counts per S5 class. The remaining direct positive-formula gate is cancellation-free evaluation of those explicit bounded tables on the unevaluated walls and central regions. T047 separately evaluates the full stable-defect H1 correction for k≥3s−1."
assert old in s;s=s.replace(old,new)
old="G025 proves all seven multiplicities at least two whenever every consecutive gap is at least two. It also proves the actual symmetric canonical image is nonzero in every such degree, with full target rank at n≥5 and exact image rank1 at the sole n4 shape. Any remaining vanishing label has a gap zero or one; G021,T045,T046 and G023 further evaluate their stated subfamilies."
new="G028 completely classifies support for every strictly decreasing five-row shape. Five middle outer labels always occur. The two extreme labels have exactly two explicit normalized rays and two isolated normalized exceptions, with determinant parity stated in SC1–8. The remaining support classification lies on equal-consecutive-row walls, after the already evaluated G021,T045–48,G026 families. G025 supplies the stronger multiplicity≥2 and actual image result on gaps≥2; G028 records the precise n5 canonical kernel subtraction and the sole strict positive-target/zero-image component."
assert old in s;s=s.replace(old,new)
s=s.replace('R025--R027 remove explicit multiplicity-one cofactor families throughout their below-square intervals', 'R025--R030 remove explicit multiplicity-one cofactor families and both complete endpoint strips throughout their below-square intervals, including the second-cofactor critical component')
needle="      ('Q-NONVANISH5'"
entry="      ('Q-EXACT-FLAG','G-027 FA1–17; T-049 DP1–12','Replace all unspecified flag-ideal cohomology ranks by explicit algebraic maps and known finite character terms','proved','G027 gives the exact normal-order map, signed restriction complex and full stabilizer model in every outer degree. T049 gives the actual diagonal quotient, all-degree saturated product equality and factored character; in outer degree five its character is48 fully specified signed bounded-table counts per cycle class.'),\n"
assert needle in s;s=s.replace(needle,entry+needle)
p.write_text(s)

with (ROOT/'work/root/paper_front.md').open('a') as f:
 f.write('''
## Current completed reductions: exact global models and strict support

G-027 replaces every remaining unspecified flag-ideal cohomology rank by actual normal-order substitution, a saturated arrangement ideal, an exact signed restriction complex and fully known stabilizer modules. T-049 strengthens the comparison to an all-degree equality between the intersection and product ideals and constructs the exact quotient of independent-block ideals by a regular diagonal sequence. Its rank-five character uses48 explicitly signed bounded-table counts per cycle class. These statements evaluate the full character through specified maps; the general positive-formula gate is now the cancellation-free evaluation of these explicit counts.

T-047 computes every stable line-defect correction by an actual finite-normal restriction and gives at most12 positive polytopes for that correction. T-048 evaluates the complete defect-three coefficient family for k≥8. G-026 evaluates every first-power zero-twist two-row quotient with17 selected positive polytopes, exact support, literal constraint matrices and a direct evaluator.

G-028 completes the nonvanishing classification for every strictly decreasing five-row output. All five middle outer labels occur; the two extreme labels vanish exactly on two explicit normalized rays and two isolated normalized shapes, with the stated determinant parity. The remaining unclassified support lies on equal-row walls. At inner degree five, the actual symmetric canonical image loses exactly one copy on each of four strict CIM kernel shapes; the sole strict component with positive target and zero image is (12,5,4,3,1). All inner degrees at least six have full target rank by the exact established degree-five propagation map.

R-028--R-030 establish both full cofactor endpoint strips through exact apolar evaluations and uniform factorial bounds, including a further component on the critical square-minus-one boundary. Every claimed statement above has a complete proof reading recorded separately from its computations and from the source checks.
''')

with (ROOT/'work/root/geometric_dictionary.md').open('a') as f:
 f.write('''
## Exact arrangement, strict support and endpoint-strip transports

**G-027 and T-049.** The local quotient substitution Y0=−xY is an injective normal-order comparison over the fraction field of the generic square matrix. Intersecting its point conditions gives the specified coherent arrangement ideal. The independent-block substitution sends each standard block to ell_i⊗F; its kernel on the product module is exactly the regular diagonal sequence, by the complete Koszul–restriction argument. Its sheaf is the fat frame arrangement, and the local Čech calculation proves saturation. These are explicit morphisms of affine and projective coordinate schemes (EGA I9.5.2; EGA II2.5), with the SGA3 I4.5,4.7.2–4.7.3 comodule action. The Schur operations are SGA6 V4.2,4.4,4.8–4.9 and cote133/024–029 via A010. To enter the locally free K0 of SGA6 VI3.3, take the finite equivariant graded free resolutions specified in G027§6, sheafify, and use their alternating class. Minimal invariant generator lifts and the Koszul Tor bound prove termination; Eisenbud, Lectures on the Geometry of Syzygies, Theorems1.2–1.3,p118 is the exact primary finite-resolution locator. This gives the actual coherent-to-locally-free comparison rather than assigning coherent objects directly to that locator.

**G-026 and T-047--T-048.** G026 extracts the Schur component of the signed coherent restriction complex. Its orientation line is the exterior determinant of the selected subset, fixing the induced stabilizer signs. T047 uses the finite normal substitution w=XYv and the displayed square-zero unipotent bundle automorphism; its global Schur cokernel diagram identifies actual first cohomology with the stated induced bundle sections. T048 evaluates that exact image at defect three. The same finite-resolution map carries their coherent complexes to SGA6 VI3.3, and the exact frame/complement maps carry their positive counts back to cote133/024–029.

**G-028.** Multiplication by the specified invariant sums of squares and determinant sections gives the strict-chamber embeddings as actual sheaf-section maps. The two normalized rays are transported by the explicit complement pairing and the k0 quotient-section isomorphism. Their characters and the exhaustive76-seed/14-generator certificate give the exact zero sets. The degree-five image ranks use the literal canonical kernel, normalized transpose and Schur component maps; they are graded ranks in the EGA I9.5.2 coordinate-image construction, including the zero image at (12,5,4,3,1). These are statements about precisely identified morphisms.

**R-028--R-030.** Every polynomial section is given by actual determinants and cofactors. The perfect complementary-column pairing fixes the source multiplicity and its sign projector; the retained-slot and common-polarization maps are the normalized tensor maps K16–22. Their apolar coefficient evaluations and all scalar signs are computed explicitly. The positive factorial bounds therefore prove actual ranks in the same coordinate-image scheme and representation K0. Scalar extension and ambient inclusion commute with each displayed polynomial map. This supplies the full EGA I9.5.2 / SGA3 / SGA6 transport for both endpoint strips.
''')

with (ROOT/'work/root/remaining_gates.md').open('a') as f:
 f.write('''
## Current gates after the global arrangement and strict-support reductions

This dated update supersedes earlier descriptions that still ask for unspecified flag-cohomology ranks. G027 and T049 now provide actual maps and fully known finite character terms in every outer degree. In degree five there are48 signed bounded-table counts per conjugacy class. The remaining positive-formula problem is to remove cancellation in these explicit expressions on the regions outside the completed positive families. T047 evaluates every stable-defect correction, T048 completes defect three, and G026 completes the first-power zero-twist slice.

G028 completes all strictly decreasing five-row support, with every zero explicitly listed as two rays and two normalized exceptional shapes. The remaining support gate is therefore the equal-consecutive-row walls, further reduced by the already evaluated coefficient families. The strict n5 actual canonical ranks are completely determined by four exact target-minus-kernel calculations; strict n3/n4 ranks retain only their separately proved ranges. The varying-rank map gate excludes both completed cofactor strips R028–R030, including their critical-boundary component.

The general polynomial description-size gate, width-seven boundary valuation gate, archive mathematical inputs and missing named-source comparison maps remain as recorded in QUESTIONS.tsv. No complexity-class separation follows merely from the new exact or fixed-rank positive formulas.
''')

with (ROOT/'deliverables/LEDGER.md').open('a') as f:
 f.write('\n## Further research update — '+stamp+'\n\n')
 f.write('G027/T049 close the exact flag-model row by actual saturated product, diagonal quotient and signed restriction maps; the positive-formula gate is reduced to explicit finite-character cancellation. T047 evaluates every stable-defect correction, T048 completes the defect-three coefficient family, and G026 completes the first-power zero-twist slice. G028 classifies nonvanishing for every strict five-row partition and confines the remaining classification to equal-row walls; its precise n5 canonical ranks include one positive-target/zero-image component. R028–R030 complete both cofactor endpoint strips. These are genuine main-gate reductions after review01. This is a research update, not an extra formal review; review02 remains03:01:08UTC.\n')
with (ROOT/'deliverables/IMPLICATIONS.md').open('a') as f:
 f.write('''
## Global explicit models and complete strict-chamber support

G027 and T049 supply exact morphisms that replace all remaining unspecified flag-ideal cohomology calculations by a product/intersection ideal, a regular diagonal quotient, and known finite character terms. The rank-five formula consists of48 signed bounded-table counts per cycle class. The general positive conversion remains open; its remaining input is now an explicit finite expression. T047,T048 and G026 provide further complete positive specializations and actual cohomology comparisons.

G028 classifies support on the entire strict five-row chamber. All five middle outer labels occur, and the extreme labels have exactly the stated two normalized rays and two isolated normalized exceptions. Thus every further support problem lies on an equal-row wall. The exact n5 canonical kernel calculation gives image ranks1,0,2,1 on its four strict kernel shapes; the zero-image shape (12,5,4,3,1) has target multiplicity1. This is an evaluated component of the specified map. R028–R030 remove both complete cofactor strips from the remaining varying-rank map gate. The exact SGA3, SGA6 and EGA transport of each construction is given in the geometric dictionary, including the finite-resolution map from coherent complexes to locally free K0.
''')

eventpath=ROOT/'work/root/CHECK_EVENTS.tsv'
with eventpath.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;events=list(r)
checks=[
 ('T-047','targeted proof check','Read whole D1–17 proof: actual directional CI resolution, normal substitution, square-zero bundle automorphism, both scalar restrictions, Cox endpoint, full Schur cokernel diagram, line pairing, Clebsch–Gordan maps and9-variable polytope bijection; PASS.'),
 ('T-048','targeted proof check','Read whole F1–11 proof: exact finite-normal specialization, all four correction summands and seven traces, both residue-polynomial branches, degree and support proof, positive finite-constant specification and literal polytopes; PASS. Full fixed constants independently reconstructed by archive.'),
 ('T-049','targeted proof check','Read whole DP1–12 proof: independent-block simplex contraction, Koszul total-degree support, exact quotient injection, graded-Nakayama regularity, block Cech Kunneth vanishing, saturation, actual equivariance, cyclic tensor trace and48 Weyl/exterior shifts; PASS.'),
 ('R-028','targeted proof check','Read whole ES1–18 proof: actual highest polynomial and complement pairing, lower-map inclusion, cofactor matrix and signs, apolar translation, every factorial endpoint/interior inequality and all four low-rank values; PASS.'),
 ('R-029','targeted proof check','Read whole SE1–21 proof: unique highest wedge, exact lower-map input, both w2 contributions, cofactor signs, apolar adjoints, full interval telescoping, binomial endpoint identities and antisymmetrization; PASS. Corrected only SE17 typesetting comma to a multiplication space.'),
 ('R-030','targeted proof check','Read whole CS1–25 proof and all20 low-rank integers: both exact apolar sums, all endpoint and interior factorial ratios, complete second-term bound, numerical-free r≥10 inequalities, r2 endpoint, and canonical map conclusion; PASS.'),
 ('G-026','targeted proof check','Read whole ZT1–11 proof after writing: actual flag and arrangement maps, orientation signs, full period/degree proof, every finite-difference and overflow bound, all support lists, and literal lattice-point bijection; PASS. Independently reconstructed509040 constants and462 actual coefficient cases are separately attributed.'),
 ('G-027','targeted proof check','Read whole FA1–17 proof after writing: exact lowest-normal-order substitution, Young-projector global sections, local product/intersection comparison, saturation bound, entire signed restriction complex, acyclic global-section endpoints, complete balanced dictionary and stabilizer modules; PASS. Revised coherent-to-locally-free K0 transport supplies a finite equivariant resolution with its termination proof.'),
 ('G-028','targeted proof check','Read whole SC1–8 and all five sections after writing: exhaustive minimal parity seeds, proved14-generator monoid, complete70-increment reduction, mixed-axis domination, exact k0 ray and determinant-complement maps, all sign endpoints, and actual n5 target-minus-kernel ranks; PASS.'),
 ('G-026','computation or formal certificate','Executed all504000 bulk plus5040 boundary Newton constants using exact Python inputs and a proved signed64 bound; every constant nonnegative, all nonconstant active orders positive, every zero listed. Executed1554 positive-evaluator versus exact-character comparisons and selected literal witness inequalities; PASS.'),
 ('G-028','computation or formal certificate','Executed all76 minimal seeds, all14 monoid generators and70 badseed increment cases by exact alternant/Pieri characters; exactly71 seeds and66 increment cases fullypositive. Computed the exact seven S321 standard traces and four strict n5 target multiplicities; PASS. Independent reconstruction is separately logged.'),
 ('SRC-CONCA-HERZOG','used and rechecked in this run','Opened/read primary arXiv math/0210065v1 Theorem3.1,Lemma3.2,Corollary3.3p6 and their complete proofsp7. Checked repeated nonzero linear ideals, saturation thresholdmk, and exact application to the frame arrangement; PASS.'),
 ('SRC-DERKSEN-SIDMAN','used and rechecked in this run','Opened/read primary published author PDF, AdvMath172(2002)151–157: Theorem1.2p153 and Theorem2.1p154, proofpp155–156. Applied only the precise regularity/sheaf convention and the reduced arrangement bound; PASS.'),
 ('SRC-EISENBUD-SYZYGY','used and rechecked in this run','Opened/read primary MSRI51 author text, Theorems1.2–1.3printedp118 and the explicit proof-omission noticep119. Used the finite graded resolution statement; no source proof-read claim. G027 separately proves termination for its specified equivariant minimal resolution.'),
]
for sid,typ,outcome in checks:
 row={k:'' for k in fields};row.update(statement_id=sid,date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type=typ,outcome=outcome);events.append(row)
with eventpath.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
print(stamp,'integrated G026–28,T047–49,R028–30;14 precise root events')

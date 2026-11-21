# DELTA23 order-five, level-six, and Krammer workstream

Snapshot: 2026-11-21 00:26 UTC. Actor: `/root/five_level_six`, GPT-6 Astra Pro, effort inherited/not exposed. This is a workstream ledger for integration into the root ledger, not a declaration that an open user item is finished.

## Current gates

| User item | State reached | Exact remaining gate |
|---|---|---|
| A.84, full profinite GT | Undecided. The cubic detector has been reduced to affine216 by the pentagon agent, hence the main joint gate has order5184 and twelve actual necessary states. F22 constructs a cubic descent with a3 after descent equal to Psi3/2; P13 preserves a2 under that descent. | Decide the actual full-GT relation between the two descents, equivalently the remaining d2/e3 equality. Different fillings of the same cubic cover have now been marked explicitly, but their full-GT functorial comparison is unproved. Finite word independence is not an actual-element construction. |
| A.24, order-five passage | An actual norm-one frame character C5 on multiplier-one full GT is constructed; Omega5 and kappa5 are constructed on the gentle group. The Galois comparison C5=(-1)^kappa5 Omega5 is proved with the marked rotation and twist. | Decide whether E5=(-1)^kappa5 C5 Omega5^-1 is trivial on all full GT, and whether any quadratic descendant has a comparison with Delta. No such all-GT equality is asserted. |
| A.86, level-six Atkin-Lehner | The outer defect is well defined on the specified subgroup; it has a marked free basis and an exact two-word criterion. F18 proves every Atkin-Lehner outer defect trivial on the entire congruence completion for every gentle element. An actual mixed-sign witness is also invisible on the whole pronilpotent quotient, conditional on supplied R2. | Evaluate the two literal free-group words in a noncongruence quotient retaining nonnilpotent information. Neither congruence nor pronilpotent tests can establish the proposed equivalence. |

## Findings and proof/check status

| ID | Finding | Proof file | Check state communicated so far |
|---|---|---|---|
| D23.F1 | Rigid sixth-point lift of the order-five frame, with linking-number-zero gauge | order_five_frame.tex | Root whole-proof check passed after explicit profinite Birman exactness addition. |
| D23.F2 | Actual C5 norm-one frame character via symplectic covariance | order_five_frame.tex | Root whole-proof check passed; uses root D23.T1 and T2. |
| D23.F3 | Gentle cyclotomic homology character Omega5 from the degree-ten Belyi cover of y^2=x^5-1 | order_five_arithmetic.tex | Root whole-proof check passed. |
| D23.F4 | Gentle quadratic coefficient kappa5 and Galois Kummer class of zeta5-1 | order_five_arithmetic.tex | Root whole-proof check passed. |
| D23.F5 | No J5-torsion quadratic bit can recover the common cubic/harmonic Galois bit | order_five_arithmetic.tex | Root whole-proof check passed; uses supplied AF.6 field intersection. |
| D23.F6 | Explicit level-six free generators and Atkin-Lehner W3 words | level_six.tex | Root whole-proof check passed; exact certificate rerun by root. |
| D23.F7 | Exact two-word criterion for AL6,3=1, with its correction and conjugator fixed | level_six.tex | Root whole-proof check passed; source FP.17 marking verified. |
| D23.F8 | Rational 2x2 Atkin-Lehner matrices cannot literally generate the division quaternion (2,3) | level_six.tex | Root whole-proof check passed. |
| D23.F9 | Marked Galois comparison C5=(-1)^kappa5 Omega5; relative character E5 on full GT | order_five_comparison_draft.tex | Root whole-proof check passed, including the added explicit positive-rotation sign paragraph. Filename retained for stable references. |
| D23.F10 | The supplied E.58 witness is invisible on the full pro-two level-six quotient | level_six.tex | Author whole-proof reread passed; root has read the full proof. Root check event is maintained by root. |
| D23.F11 | Rank-four symplectic covariance is exactly the old B3 shear, so the proposed sign is always positive | symplectic_collapse.tex | Root whole-proof check and integral matrix recalculation passed. |
| D23.F12 | Under supplied R2, one actual Delta=1 witness is invisible on every nilpotent level-six quotient simultaneously | level_six.tex | Author whole-proof reread passed. Root read the full proof and is checking the precise universal-open-normal R2 input. The original lifting proof is not independently reconstructed. |
| D23.F13 | Krammer first pair: quotient D8 is trivial on gentle f; central C3 phase uniquely fixed by duality; six states | krammer_quotient_extension.tex | Root whole-proof check and independent exact certificate rerun passed. |
| D23.F14 | No S4 quotient of the simultaneous five-pair Krammer word image; V4 harmonic phase independent | krammer_s4_obstruction.tex | Root whole-proof check passed after explicit reversal for pair51; event recorded as requested. |
| D23.F15 | Solvable mixed-block joint image is H108 x H108, derived image 27 x 27; Nielsen kernel invariance fails | krammer_solvable_correlation.tex | Author whole-proof reread and explicit witness calculation passed. Independent whole-proof check requested. |
| D23.F16 | First-pair Krammer plus induced S4 source still has an odd harmonic frame centralizer, even with induced coordinate identity | krammer_induced_frame_ambiguity.tex | Exact finite coordinate certificate passed. Full independent proof check requested. Uses D23.C11. |
| D23.F17 | No S3 quotient of the joint Krammer word image; whole A4 phase independent | krammer_s3_obstruction.tex | Exact H-block action certificate passed. Independent whole-proof check requested. Explicitly uses the new full common-word theorem D23.P9. |
| D23.F18 | Every level-six Atkin-Lehner defect is trivial on the entire congruence completion | level_six_congruence.tex | Root read whole proof without a substantive gap; exact rational conjugation formula independently checked. |
| D23.F19 | Product addition of any two-kernel harmonic cover cannot exclude the rho0, a3=1 Krammer solutions | krammer_harmonic_cover.tex | Root whole-proof reading found no substantive gap; uses P9's full common-word theorem and C12 detector. |
| D23.F20 | The entire relative pro-two Ferrari tower misses the supplied strengthened actual witness | krammer_harmonic_cover.tex | Root whole-proof reading found no substantive gap; supplied FP36 lifting input explicit. |
| D23.F21 | Joint cubic/quartic cyclic degree12 cover is blind at every two-adic and three-adic homology depth | cyclic12_cover.tex | Characters agent independently read whole proof and all code, reran certificate, PASS. Root notified. |
| D23.F22 | Canonical cubic descent on H, with a3 after descent exactly Psi3/2 | cubic_descent.tex | Root read whole proof and found formulas coherent; characters independently checked normalization and composition, PASS. Exact signed certificate passed. |
| D23.F23 | Canonical whole-G extension of cubic descent, and relative extensions of d2,e3 | cubic_descent_full.tex | Author whole-proof check and both finite permutation/symbolic certificates passed. Independent check requested. Uses P13, independently re-proved in this workstream. |

Root subsequently read all of F16-F20 without a substantive gap. F16 now explicitly uses the B3 half-twist lift, whose square is central, rather than claiming a premature B quotient. F17 matrix-action certificate was independently rerun by root. Exact root check events remain in root's ledger.

## Approaches tried and their outcomes

1. **Use the existing order-five torus target without an actual map.** Rejected as insufficient. A.46/FP.19 give the target but no frame character. F1-F2 construct the missing map using the six-point stabilizer `B5/Z5`, the linking gauge and root's symplectic covariance. The genus-two representation does not descend to the five-point sphere group; FP.21 remains valid.

2. **Extract Delta directly from J5 torsion fields.** Ruled out for a single common bit by F5: the common Galois quadratic field Qab(4th root of3) is absent from L5 by AF.6. Matching CM fields or ramification sets is not a comparison of the characters.

3. **Compare the order-five frame with the Belyi homology character.** Successful on Galois after fixing all signs: positive rotation transports `(X,Y)` to `(zeta5 X,-Y)`, whereas the order-five deck map is `(zeta5 X,Y)` and acts by `-q(a)`. Normalization introduces the exact `(zeta5-1)^5` twist. The all-GT equality remains open; only a new relative character E5 is obtained.

4. **Use cusp permutations for Atkin-Lehner.** Already excluded by FP.18: cusp widths1,2,3,6 force each cusp to be fixed. F6-F7 retain free-group paths rather than collapsing to cusp permutations.

5. **Identify the rational Atkin-Lehner algebra with discriminant-six quaternion algebra.** Literal identification refuted by F8. A Brauer-class comparison would require additional construction.

6. **Use a pro-two or pronilpotent level-six test.** F10 kills every pro-two test for the original E.58 witness. F12, conditional on supplied R2, supplies a single actual mixed-sign witness invisible to all pronilpotent tests simultaneously. A.86 therefore needs nonnilpotent information.

7. **Use the sign on the extra rank-four symplectic line.** Refuted by F11. The exact Drinfeld first argument is the partial full twist, or equivalently the usual y_i after removing a commuting central factor. The four evaluated generator formulas already equal the old shear on all gentle elements. No claim is made that arbitrary lifted five-cycle words have trivial evaluation.

8. **Use the Krammer quotient block as the harmonic S4 detector.** Refuted: its pure image is D8, and the three-cycle makes every gentle f trivial there. The residual central C3 is the fourth power of the B3 full twist, and the two-cycle fixes its phase. This yields the six-state first-factor reduction F13.

9. **Couple the harmonic S4 value through the simultaneous common-word Krammer source.** F14 excludes S4 quotients by separating simple unitary factors and a solvable 3/2/3 normal series. F17 strengthens this to no S3 quotient, using P9 and the irreducible order-four action on the solvable derived blocks. Arbitrary commutator words can preserve all Krammer values while changing the entire A4 coordinate. This is not an actual gentle counterexample.

10. **Assume the cyclic Nielsen operation preserves the solvable block's derived kernel.** Refuted by F15. The word `[x^2,y]` is trivial in H34 and nontrivial in H45. The actual gentle relation in C9 remains valid because it uses the genuine two-cycle and three-cycle equations, not kernel invariance.

11. **Add the induced marked S4 quotient and retain level12 to remove the harmonic frame gauge.** F16 shows that the ambiguity survives even after adding first-pair Krammer. Coprime abelianizations make the two derived word images independent, and a literal odd harmonic centralizer remains. The current next route is the characters agent's rank97 relative mod-two homology detector, which attacks the frame centralizer directly.

12. **Use all congruence levels for Atkin-Lehner.** F18 proves the normalized action is inner on the whole congruence completion, because the old shear belongs to the level-six group itself. Rational Atkin-Lehner normalization then makes every outer commutator trivial. The remaining A86 gate is specifically noncongruence.

13. **Combine Krammer with the new harmonic frame detector as a product.** F19 identifies the maximal two-quotient of the Krammer derived image as Q8 x C2 and proves it cannot see the cubic translation/sign at fixed rho. P9's common-word realization therefore leaves mixed candidates even after any such two-kernel cover. F20 rules out the entire corresponding relative pro-two Ferrari tower for the supplied strengthened witness.

14. **Put both elliptic quotients into one cyclic cover.** The degree12 cover with weights9,9,10,4,4 has genus11, a quartic genus-one quotient and a cubic genus-one quotient. F21 derives all braid matrices from exact covering chains. Every adjacent-pair image on every deck socle factor is metabelian at2 and3. The automorphism-kernel lemma promotes this to a pro-p second-derived group at every p-adic depth, killing the supplied FP36 witness simultaneously. This excludes the entire two/three-adic homology route for this cover, not its nonabelian covers.

15. **Use Enriquez distribution directly to compare the cubic frame.** Re-read the full-GT theorem, already used in LM7 E6; no novelty claim. The index-three cover has five punctures, but the distribution and modular-frame constructions fill different pairs. LNS Section6 and HF1 provide the Galois comparison, not full-GT fixedness. Root separately proves that all distribution equations in one fixed small target still admit arbitrary finite mixed states.

16. **Construct the missing cubic descent intrinsically.** Successful as F22: descend through E=C3*C3, extend over its involution, and normalize the cusp with the exact coefficient3Psi3/2. The signed mod3 calculation gives a3 after descent=Psi3/2. P13 independently shows that a2 is unchanged, so Delta after cubic descent=d2. F23 extends the construction to all multipliers and gives canonical relative quadratic extensions of d2,e3. Full-GT fixedness, or the weaker required parity comparison, remains open.

17. **Close the Krammer first pair under all S3 Nielsen substitutions.** Its cyclic substitutions on commutator words are conjugation by K1K2, because the discrepancy in the second generator is the central B3 full twist. All six F13 states satisfy the remaining three-cycle norm. This adds no new first-pair constraint. The other agents are closing the mixed factors under the same operations.

## Source locators retained

- DELTA_ON_GT: conventions; AD.1-AD.2; AF.1-AF.7; agent_five FP.3, FP.6, FP.17-FP.19, FP.21, FP.30, FP.36-FP.37.
- LM7_PUSH: E.58.2, E.58.11-13, E.58.19-23; E.65.4 and E.65.9-10. These are supplied background inputs. The universal relative lifting theorem R2 is not independently re-proved in this workstream.
- Collas, genus-zero GT action, TheoremB; published JTNB24(2012),605-622, DOI10.5802/jtnb.813. Prime-order torsion supplies the order-five pure conjugator.
- Herfort-Ribes, *Torsion elements and centralizers in free products of profinite groups*, TheoremB', Section4, printedp159. Factor centralizer result, including the nonidentity factor case.
- Nakamura, RIMS1691(2010), Section5.4, equation(5.4.2), printedp28. Exact tangential braid base point and arithmetic Drinfeld formula. https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1691.pdf
- Milne, *Lectures on Etale Cohomology*, v2.21, Theorem3.4, printedp28. https://www.jmilne.org/math/CourseNotes/LEC.pdf
- Bigelow, *The Lawrence-Krammer representation*, arXiv:math/0204057, Section4.2. Literal Krammer convention used by D23.P6.
- Hida, *Adjoint L-value as a period integral and the mass formula of Siegel-Shimura*, version20September2023, Section1.3, printedp7, displayed Kubota splitting and paragraph before(1.5). https://www.math.ucla.edu/~hida/PdFinal.pdf
- GAP Character Table Library, *Simple Groups by Group Order*, rowU3(3),6048, and the corresponding PSU(3,3) record. This checks a cited standard simplicity fact, not a new proof of it. Edge1960 original introductory extract was also read; the full article was not available through the publisher page.
- Enriquez, *Quasi-reflection algebras and cyclotomic associators*, arXiv:math/0408035v2, Section8, equation50, Theorem8.1, pp30-32; Section13, pp48-49. Full-GT distribution and cyclotomic orbifold action, not an automatic eigenlocus comparison.
- Lochak--Nakamura--Schneps, *Eigenloci of 5 point configurations*, Theorem2 HF1, author PDF p4; Section6 equations6.3-6.4, author PDF pp30-31. https://webusers.imj-prg.fr/~leila.schneps/LNS.pdf
- Furusho, *Geometric and arithmetic subgroups of the Grothendieck-Teichmuller group*, Theorem3.1 and3.4, printedpp102,104-105; author publisher PDF https://www.math.nagoya-u.ac.jp/~furusho/paper/GTA-mrl.pdf. Extra relationIV remains explicit. The earlier-mentioned Jan2008 correction was not retrieved in this run.

## Independent checks performed for other workstreams

Read all of root proofs D23.L1-L8 as assigned; independently rederived L1-L5 and L6-L8, with exact primary Hida normalization checked for L6. Events are in this workstream CHECK_EVENTS.tsv. E.58/E.65 are explicitly retained as supplied inputs; no check is represented as a reconstruction of the absent original lifting proof.

Independently read and re-proved the whole P8/P9 common-word proofs and reran P9's exact certificate; PASS, with the supplied P7 assignment list and standard simplicity fact explicit. Independently read and re-proved all of P13, reread the exact FP34 marking, and reran every finite translation/normalization case; PASS.

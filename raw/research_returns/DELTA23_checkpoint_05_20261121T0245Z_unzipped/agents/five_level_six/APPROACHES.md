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

## 18. Full solvable Nielsen closure of Krammer (D23.F24)

The simultaneous twelve-marking derived image has order 27^3. Exactly twelve tuples meet two-cycle, positive and negative multiplier three-cycles, and the correctly conjugated reversed cycles. All 216 P7 assignments survive, and all six first-pair values pass both cycles. The first-pair and mixed-solvable finite values can be realized by a common ordinary commutator word, by Goursat. This exhausts this finite necessary-equation refinement; it supplies no actual gentle lift. Proof and exact records: `krammer_solvable_s3.tex/.py/.json/.npz`.

## 19. Orbital exceptional pair and its central phase (D23.F25–F26)

The exceptional Krammer pair (K1K2,K3²) has derived group SU6(3); its full group is the determinant-{±1} subgroup of U6(3). The proof uses an exact transvection orbit of all 22,204 isotropic lines, then elementary generation, perfectness and projective simplicity. The six peripheral Nielsen evaluations have distinct projective action-order pairs and independent SU6 coordinates. They remain independent of all old Krammer and index-three induced data, whose prime divisors are 2,3,7. Two central phase flips preserve every two/three-cycle and generator-automorphism condition. Consequently the exact orbital correction (−I)^b by itself does not force a quadratic comparison. The noncentral periodic-product constraint remains a possible main gate. Proofs: `krammer_orbital_unitary.tex` and `krammer_orbital_sign.tex`; exact certificate `krammer_orbital_unitary.py/.json`.


## 20. Non-Ferrari affine orbital comparison (D23.F27)

The literal exceptional pair (delta,K) in supplied FP31's affine216 B4 representation is exactly conjugate to the C14 marked pair (x,srs). Its f-value is recovered by conjugating the original cubic primitive over F9 before applying the real projection; the outside-E conjugator cannot be dropped. All six original frame states yield three possible translations. Both quadratic residual signs pass every periodic cube test, because the linear part is a two-dimensional nonidentity unipotent in characteristic3 and every affine lift cubes to1. This is a precise obstruction to the isolated periodic test, with no assertion that the full joint orbital identities are tautological. The characters workstream subsequently treats that joint shared-conjugacy question.

## 21. Harmonic and cubic Krammer exceptional factors (D23.F28)

The harmonic exceptional pair (K1K2K1,K3²) generates U6(3), with derived SU6(3), through another complete22204 isotropic-line transvection orbit. Its six projective peripheral order pairs are distinct from all six cubic order pairs. Thus all twelve derived SU6 factors are independent, including their scalar centers. Combining the two orbital relations at this finite Krammer level does not by itself correlate their quadratic central phases. Noncentral compatibility and actual GT realizability remain separate.

## 22. A functorial finite Hurwitz representation (D23.P17–P18, D23.F29 audit)

The new degree1344 orbit in all C^4/ASL2(F3) retains the exact marked cubic216 first-pair quotient and the marked S4 mixed-pair quotient. Independently read the complete P17 proof, constructors, and replay; verified the complete7796-point space,17-orbit list, unique1344, the actual432→36 set map, and both image-group quotient order equalities. Final targets216 and S4 are group quotients, not equivariant set quotients.

Unlike an arbitrary matrix representation, this finite action has a proved multiplier-one full-GT kernel invariance. The standard Drinfeld action on the mixed braid subgroup B_{4,1} preserves the completed free kernel and the standard B4 section. It preserves peripheral conjugacy classes, giving a bijection of the entire finite tuple space that intertwines the twisted B4 action. Uniqueness of the1344 orbit gives actual permutation covariance. The whole P18 proof and exact rightmost-strand Artin certificate were independently checked. F29 stores an independent full derivation with the same orientation and a primary-source scope audit.

Root's H1 exact36-point test was independently re-proved and rerun: the1944 pure image has derived648; nine lifts over each cubic label reduce to exactly one under the two cycles and both three cycles, and the same unique value admits simultaneous permutation conjugacy. All six labels survive. This supplies a concrete first-pair value for the1344 test; it does not decide A84.

Additional primary locators: Harbater–Schneps, HS.pdf, §0.1 equation(1), printedp3/PDFindex2; Lochak–Schneps1994, Fls.pdf, §5 Proposition10, printedpp23–24/PDFindices22–23. Both explicitly supply the full profinite GT braid action. Nakamura RIMS1691§5.4 alone is Galois-scoped and is used only for the arithmetic marking.

## 23. Structure of the twelve orthogonal blocks (D23.F30–F32)

The full block kernel has derived subgroup S^12, where S=PΩ6−(3), using the explicit C23 quadratic-form identification rather than order recognition. Exact Schreier calculations retain all153 distinct full1344-point kernel generators. Both block-pair orbit types project onto PSO6−(3)^2, so simple-group Goursat gives the full direct product. The remaining binary code has dimension9 and equal parity on four parallel triples. Its signed24 quotient is proved, by all331776 generator edges, to be precisely the supplied Burau mod4 representation modulo omega scalars. The extra central minus identity splits by determinant cube and gives no additional commutator information.

For a normalized actual full-GT state rho0,a2=0, supplied FP37 and that exact signed identification force both first and mixed signed values to be identity. Actual covariance propagates one H3 local socle action to all blocks, and the signed equations force every binary coset to vanish. Hence the actual conjugator belongs to S^12 (F32), without presupposing P20 innerness. Root checked F30/F31 completely; pentagon independently checked F32.

## 24. Full mixed solvability (D23.F33)

All16 components of the mixed34 pair and all30 of the mixed45 pair were reconstructed from the full1344 action. Every complete derived series ends in1, with length at most6; the reversed51 pair is checked by the literal reversing braid. Consequently every finite joint Nielsen family of mixed values is solvable. Goursat then makes the first-pair perfect residual independent of all mixed common-word coordinates. This does not preserve the gentle equations or actual canonical conjugator. Pentagon independently checked the whole proof and all46 component certificates; root review was requested.

## 25. Full first-pair covariance (D23.F34)

The complete global candidate lists have72 elements for each normalized cubic bit. Exact membership in the actual full first-B3 image leaves the same36 indices in each list. For every survivor, F=[AB,V] lies in the pure-pair commutator image and agrees with the unique P21 value on all448 detector points. Because V commutes with A and z3, this commutator is simultaneously [ABA,V]; its two-cycle and three-cycle are therefore exact telescoping identities. A fresh complete1344 certificate verifies every equality. The first-pair test does not distinguish the two cubic bits; the joint same-word condition with mixed values remains a separate test.

The full mixed group has order40122452017152 and derived order557256278016. Its abelianization is C6×C12 with literal marked generators C² and z3. All36 first-pair survivors also normalize this full mixed group. The characters workstream proves that every relevant mixed conjugator fiber meets its commutator subgroup; the remaining common-word reduction is being computed through the first pair's maximal solvable quotient.

## 26. The first perfect residual, and a uniqueness lemma (D23.F35–F36)

The exact full P-derived series stabilizes at a center-free perfect group of order16796160000. The first448-plus-signed24 quotient has order93312 and is proved to be P/P∞ by equality of kernel orders and solvability. No abstract A6-product identification is needed.

A root-proposed algebraic lemma then closes a critical completeness issue. Any competing first value is F=cF_V with c∈P∞. Covariance makes c commute with B; the two-cycle makes it commute with F_V A F_V^-1. Those two generators generate the entire firstB3 group, so c lies in the center of P∞, which the exact certificate proves trivial. Thus F_V is the ONLY possible full first value, not just a successful sample. This permits H8/P26 to exclude candidates using subsequent pentagon tests.

## 27. Raw blocks and the genuine central obstruction (D23.F37, P26 audit)

The raw672-point block stabilizer has order39191040 and perfect derived subgroup6531840. Its induced local-abelian72-point quotient is exactly the literal unprojectivized FP36 Burau group overZ4[omega], proved by995328 matched generator edges. It restores centralomegaI, lying in the global commutator subgroup. Every individual five-cycle pair still maps isomorphically to the old signed24 pair, so this quotient alone supplies no new individual pair values. The full raw8064 action retains more information.

Independent whole-proof audits and fresh certificates for P24/P25/P26/P27 pass. The full-GT sphere pentagon lifts exactly to completedB4 because its central discrepancy has zero braid exponent and exp(z4)=12. P26's full raw test therefore gives genuine necessary exclusions: six normalized V indices1,19,23,27,53,61 remain, three mixed values each. P27 verifies that all18 new pairs also satisfy the full canonical linear raw covariance; earlier H7 witnesses could not substitute for these new values.

The joint first-solvable/M34/M45 word image has order10866225302113486007489789952 and abelianizationC12². Its full common-word test retains all36 baseH8 triples, hence all18 raw survivors. This is only finite ordinary-commutator compatibility; full mixed Nielsen and actual-source relations remain.


## 28. Full common-word closure and actual-source normalizations (H9, F38 audit, C30–C33 audits)

The complete first-solvable/full-cyclic-mixed core join on1948 points retains all18 raw survivors. Its exact order is756909033492380793871582030971644411904; every target has source exponents(0,0) modulo12 and hence an ordinary commutator realization. The perfect residual then restores the exact full first value. H9 is the integrated theorem; F38 is a parallel audit proof rather than a duplicate final statement. The full six mixed orientations and the raw five-factor product are retained, without asserting any actual gentle lift.

Actual-source operations improve the existential gate. Cubing gives four forms; complex conjugation gives three; the paired action h→(V_h,R_h^-1V_h) is a homomorphism, and the odd word h(chc^-1)h carries the third form to(27,2). Thus only(1,0),(27,2) need occur if any normalized mixed element exists. All complete finite odd-word closures remain compatible, so no original individual case is excluded by these operations. Independent whole-proof checks and complete replays of C30,C31,C33 pass.

## 29. Full spherical order-five frame (D23.F39, P29 audit)

The literal6720-point spherical extension has60 orthogonal112-point blocks. All240 local transitions lie in PSO6−(3). A single explicit16-letter braid word has block order20; its40th power has local order7 atblock0 and identity atblocks1,9,12, representing allthree distinct-block orbit types. Its normalclosure is therefore the full S^60, by simplicity and pairwise Goursat; this product lies in the derived pure image.

The remaining pure quotient is a solvable5-prime group. Since order-five rotation permutes the60 factors in12 free5cycles, every finite order-five cocycle is a pure coboundary. All18 explicit primitives even lie in S^60 and admit ordinary purecommutator lifts, satisfying zero integral abelianization. The LS97 actual pure-frame condition thus adds no exclusion in this representation. This is a structural finite limitation, not an actualGT lifting theorem. The correct general actualframe abelianconstraint is t(1,1,1,1,1), notzero. P29 and F39 independent proof/certificate checks pass.

## 30. Direct source action on the tuple kernel (ongoing)

For the rightmost free kernel N=F4 inB5, let P=u1u2u3u4=z4^-1z5 andu4=sigma4². StandardDrinfeld marking gives f(y4,u4)=f(P^-1,u4): z3 andz5 commute withbothinputs and disappear in acommutator evaluation. Thus kappa_h(u4)=f(P^-1,u4)^-1u4f(P^-1,u4), whilekappa_h(P)=P. This gives an actual natural map from tupleNielsenclasses to E0-pairclasses, T→[(productT)^-1,lastentry], and a last-entry partition onfixedproduct rawtuples. Root tests the rawcondition; this workstream derives and certifies the exact source formula. No arbitrarypuncture-deletion compatibility is assumed.

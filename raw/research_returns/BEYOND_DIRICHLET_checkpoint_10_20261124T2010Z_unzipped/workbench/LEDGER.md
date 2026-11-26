# Dated research ledger

## 2026-11-24 12:39 UTC — start

The complete attached prompt was read and the archive was unpacked once. No earlier conversation is used. A first checkpoint is due approximately 13:24 UTC, then at 45-minute intervals. The first formal progress review is due approximately 15:39 UTC; subsequent reviews are hourly. No elapsed-time milestone is represented as having occurred before its time.

| Main question | Starting gate | State |
|---|---|---|
| Cubic RH | For each exponent greater than 1/2, the specified one-sided prime or ramp bound on arbitrarily late multiplicative windows | Open |
| Artin S5 without real-zero condition | Remove real poles of the comparison quotient off the central point | Open |
| Exact cubic K-groups | Replay logarithmic class certificates and check integral descent and orientation | Under audit |
| S5 central-zero theorem | Calegari comparison, Booker divisor reduction, Cohen rigidity | Under independent re-proof |

## 2026-11-24 — first structural check

The unit-phase projector suggestion requires correction: a polynomial in a finite-order operator cannot distinguish eigensummands on which it has the same eigenvalue. A complete statement and proof will be recorded in the structural note; this changes the associated question to refuted in its exact-projector interpretation. This does not improve the cubic RH gate.

## 2026-11-24 13:18 UTC — arithmetic and analytic updates

The fresh degree-six and degree-nine full class/unit certifications passed. The degree-eighteen logarithmic upper bound was verified from explicit exact witnesses without assuming a provisional BNF is complete; a compact tower-basis version now prints the necessary inputs in Paper I. The correctly oriented cyclotomic action is multiplication by four. Paper I is consequently unconditional, subject to the cited standard K-theory and Iwasawa theorems, rather than conditional on unreplayed finite data.

The ordinary class-group assertion behind the coefficient-seven work was verified in a separate implementation: Sympy exact ideal relations give h_F<=7; an Arb interval of the class-number ratio gives h_F=7 and the fundamental unit; an elementary unit-lattice and regulator calculation gives h_E=49 and the S3 action forces C7×C7. Root checked G219 steps6–8 and G220, preserving the original coefficient rings and local conditions.

A finite theta certificate proves positivity of the cubic theta kernel and excludes every positive real zero of the associated Hecke L-function. The two coefficient algorithms and an additional root-count implementation agree. This excludes the possible real fixed point at two thirds in the marked-shell converse. It does not prove the square-root arithmetic estimate or cubic RH.

Paper II's central-zero theorem has been independently reconstructed by a separate same-model worker before reading the attached proof, then fully audited. Its exact all-place conclusion is equality of standard local L-factors, including gamma factors. The real-zero hypothesis away one half remains. Three candidate fields satisfy the literal local/Galois hypotheses; their analytic nonvanishing is not certified. A smaller algebraic candidate of discriminant8249 has been found for further testing.

An additional blind reconstruction of Paper I is underway. It first exhibited a module matching the four numerical finite inputs but giving a wrong higher-weight answer, confirming the necessity of the field-specific genus calculation. It then derived a genus constraint and a shorter cyclic-module specialization argument; the exact treatment of primes above three is still being checked. This is not yet recorded as a completed independent reproof.

The strongest current cubic analytic background opened is OpenAI's dated quasi-RH Theorem1.1, which gives the exponent7/8 for finite-order Hecke characters over Q(sqrt(-3)). Its theorem statement has been opened; its199-page proof has not been independently re-proved in this task. It is a cited external input. The fixed-character prime estimate still has a3/8 exponent gap to the requested threshold.

No three-hour progress review has occurred yet. The first checkpoint remains due at13:24 UTC.

## 2026-11-24 13:32 UTC — first checkpoint saved and new reductions

Checkpoint 01 is saved as BEYOND_DIRICHLET_checkpoint_01.zip, SHA-256 ded96840d1400c27c0e0dc23d8cbdced4fa8f9fe887f73610f84b85361f8a6e7. It contains fresh three-pass builds of both papers and the research notes. A source-identity audit removed an unannotated replay transcript whose output matched its input record byte for byte; the regenerated record now states its replay provenance. A first staging build exposed an overlong URL in the structural note, which was corrected before the saved checkpoint. The next scheduled checkpoint is due about 14:09 UTC.

The statement-only reconstruction of the full K-group theorem has finished. It independently derives the genus constraint for the 3-split Iwasawa module and gives a shorter ideal-specialization proof using a residual degree of at least four. Root has read the entire reconstruction and is checking its arithmetic and exact module statements; the paper worker is separately auditing the replacement before restructuring.

The Patterson correlation at the fixed index -269 has an exact Dirichlet series: a removed-prime factor of zeta_K(3s-1) times P(s)/P(2s), where P is the corresponding removed-prime cubic Hecke L-function. A full-index smoothed correlation has a positive X^(2/3) main term and a proved X^(1/2+epsilon) error. Prime extraction leaves an explicit long Liouville-character convolution; the available bounds for that tail are too large. This is a more concrete comparison with the theta period, not a proof of cubic RH.

The S5 real-zero attack now uses the field of discriminant8249 and a compactly supported explicit-formula test whose zero-side weights are nonnegative in the full critical strip. The finite prime sum and rigorous gamma integral are being computed. No analytic nonvanishing certificate is asserted yet.

No scheduled three-hour progress review has occurred.

## 2026-11-24 13:40 UTC — explicit S5 real-zero gate closed for one field

The discriminant8249 field now has a rigorous no-real-zero certificate for B=ζ_H/ζ_F. Its completed degree-six quadratic Hecke function has conductor8249³ and gamma shifts0,0,0,0,1,1. A compact triangular test divided by cosh gives nonnegative real zero-side weights throughout the critical strip. The functional equation has sign+1, so any real zero, including a central zero, contributes at least2H(0).

The author calculation uses exact Python polynomial arithmetic and MPFR directed rounding. Root independently factors every relevant prime with Sympy, counts traces on points and two-subsets, and encloses the integrals with Arb. Both verify S<8.5 and2H(0)>8.9 with room to spare. Root’s complete analytic/local-factor audit passes. This closes the field-specific real-zero row and yields unconditional automorphy for this explicit field. The real-zero removal for the whole family remains open. The method is credited to established explicit-formula and strip-positivity work; no priority is asserted for this example. A fresh statement-only reconstruction is being arranged.

Rubin’s1991 original paper has now been obtained from the public Göttingen digitization, with SHA-25696ca08e8ed1a7646d4bf40e2e088e0ea6e068319978ac7e5c5e3d45cc39ee23a. Its precise main-conjecture statements and module definitions are being read for the7-adic comparison. The PDF is excluded from all deliverable archives.

## 2026-11-24 14:07 UTC — second field, exact seven-adic control, and active certification

The discriminant60061 S5 field now has independent MPFR and Sympy/Arb real-zero certificates. Paper II is19 pages with both unconditional examples. The8249 theorem also has a complete statement-only reconstruction, including a separate strip-positive convolution proof and an independent Arb analytic integral. Its certificate uses no prior numerical data. The general off-central theorem and the30301/48976 cases remain open.

Paper I is24 pages and now uses the checked shorter reconstruction. The split genus quotient is exactly F3[T]/T7, and the first logarithmic layer has additive type C9²×C3². The longer proof is preserved as our earlier own work. All final paper pages have been reviewed by their workers.

Rubin's precise cyclotomic main-conjecture scope has been checked in the original. The seven-adic note now proves the exact strict specialization formula, with the finite multiplication kernel and local/global-unit denominator retained. A separate exact matrix calculation checks epsilon^342=(1,7,28)mod49 and local surjectivity at both primes above7. A full review corrected only closure wording and a duplicate equation label.

A fresh degree21 calculation reports a provisional class group C7 for the first cyclotomic7 layer. Direct unconditional bnfcertify would enumerate primes up to3.68e26; it was interrupted, with no certification claimed. A new route is underway: exact candidate units and seven-saturation, a rigorous analytic L-value product, and an interval regulator. Friedman's Theorem B gives a sufficient unit-index bound. If these certify the7-class number, Fukuda's stability theorem would settle every matched seven-adic length; this remains conditional at this entry. The huge conditional BNF cache is excluded from deliverables, while its exact candidate units and regeneration program are included.

The structural phase lemma, composite Kummer induction, and explicit growing CM family have received a separate targeted proof check. The particular family satisfies its stated numerical constraints but loses every degree-one prime at the scale of interest. The new analytical consequence under development uses the external seven-eighths theorem to improve the prime-inverse short range and examine uniform auxiliary-prime complexity. No uncompleted derivation is counted as proved.

The first scheduled three-hour progress review is still due at15:39 UTC. Checkpoint02 is due at14:09 UTC; the following checkpoint is due at14:54 UTC.

## 2026-11-24 14:11 UTC — second checkpoint saved

Checkpoint02 is immutable: BEYOND_DIRICHLET_checkpoint_02.zip, captured14:10:14UTC, SHA-256 a6877eef71ce75b670c56c0c278782983761565be6b1dbe0fb601baea8af550f, 33,902,039bytes and334 files. The source-identity audit found no unchanged attached file. Its seven-adic pieces were explicitly marked as awaiting the combined proof. The next scheduled checkpoint remains14:54UTC.

## 2026-11-24T14:35:40+00:00 — all matched seven-adic weights determined

The compact exact certificate proves v7(h(F1))=1 without relying on conditional BNF completeness. Thirteen verified units give a residue-character matrix with determinant1 mod7. Independent regulator calculations in degree21 and tensor embeddings, separate logarithmic-sine/digamma residue evaluations, and rigorous seven-twist L-values enclose h/unit-index in [7±1.11e−59]. Friedman's regulator bound gives denominator<3.49e25, making rational isolation exact; seven-saturation then proves the desired class valuation.

A separate worker reconstructed the complete stability/strict-Selmer theorem from its statement and the two finite inputs only. Root and the arithmetic worker read the full reconstruction. It proves A(Fn)=C7 through norm isomorphisms, M^chi=Z7[[T]]/(7,T), and strict groups O/7O for every seven-adic weight, including0 and ramified coefficient fields. The Delta-trivial class component is retained and can grow. Thus s(e)=1 at all matched weights and the exceptional class is empty.

The all-prime matched family now contributes exactly2(T−1)log7. It can be removed in full at a direct additional cost<6P, preserving the old error exponent, same window and exact threshold adjustment. This is a strictly smaller arithmetic gate: the largest matched weight is no longer an unknown. Other mixed and noncritical terms, the uniform realization comparison and the cubic RH prime bound remain open.

The cofactor characterization and projected-coboundary criterion received a separate targeted check; the unprojected implication is refuted by an explicit split algebra. A fresh11-page structural note has no overfull or undefined warnings and every page was viewed, with expert and newcomer readings.

The first formal three-hour review is still due15:39UTC. No scheduled review is claimed here.

## 2026-11-24T14:47:34+00:00 — third field and strengthened analytic reductions

The30301 quintic now has a rigorous A16 autocorrelation real-zero certificate. Exact PARI and independently regenerated FLINT permutation traces agree in all595877 prime-power terms. Arb at192bits with32768 interval cells proves the zero sum<11 and real-zero threshold>111/10. The separate MPFR implementation and manuscript integration are active. The48976 wild-prime case and general off-central problem remain open.

The seven-adic note is restructured around the unconditional all-character theorem, with the complete finite certificate and full proof, exact budget reduction, and specialization explanation. It has18 pages, a fresh two-pass build, no overfull or undefined warnings, every page inspected, and complete expert and newcomer readings. The characteristic ideal is a unit; the strict length1 comes entirely from the finite module Lambda/(7,T).

Independent statement-only reconstruction completes the uniform auxiliary-prime theorem, Gaussian periods in modular characteristic and unconditional pure-cubic promised AM theorem. The latter uses the fixed progression2mod3 and does not require cubic RH. The newer named external Liu theorem reduces the rational zero boundary to3493459/4000000. A full targeted check of the new switched-convolution note passes: all inverse variables up toX^(1-delta) are negligible, leaving a long Mobius-character sum with direct variable<2X^delta. Its bound at square-root strength remains open; separate estimation gives beta+delta(1-beta), and the whole sum recovers only beta. Smooth numerator truncation does not cancel zero poles.

No scheduled formal review has yet occurred; the first remains15:39UTC.

## 2026-11-24 14:55 UTC — third checkpoint saved

Checkpoint03 is immutable: BEYOND_DIRICHLET_checkpoint_03.zip, captured2026-11-24T14:54:56+00:00, SHA-256 ea7d7a115f4a9cbdb3356214551cf107a452a7d106a40fa4103485f5e00f11bf,54,492,692bytes and519files. The source-identity audit found no unchanged attached file. It contains the full36-page PaperI,20-page three-field PaperII and all current proof notes, certificates and records. Its Library file ID is libfile_fde3_f-0160c08fab5881918cac87976196fa84_c6789dc4b4d481919ad633aabe6d84d0. No further checkpoint is due before15:39UTC.

## 2026-11-24T15:10:28+00:00 — fourth S5 field and independent convolution reconstruction

The discriminant48976 example now has a full wild-local proof and independent real-zero certificates. The exact inertia filtration at2 is A4,V4,1; its rank-six conductor exponent is6 and its local denominator1+T. The complete conductor is2^6*3061^3. MPFR and separate Sympy/Arb computations each prove S<61/10,threshold>224/25,gap>14/5. Every one of465 prime-power traces agrees with fresh PARI calculations; an exact pair-field maximal-order certificate separately recovers the conductor. Root read the full added proof. PaperII is now22 pages, fresh two-pass build, no overfull or undefined warnings, and every page visually inspected by its worker.

The switched-convolution assertions have now been re-proved from statements alone by a separate same-model worker. Root read that entire reconstruction. Its zero-avoiding contours, reciprocal growth, multiple-zero residues and compact-uniform cutoff limits pass. This closes the independent-check task, but does not change the remaining long Mobius-character cancellation gate.

The new Q(i) analytic and strict5-adic arithmetic proof is being checked; its main assertions have passed root's complete targeted reading, with the statement-only reconstruction still to arrange. The proposed stronger7-adic local/global-unit quotient vanishing is obstructed by index7 universal norms. Its exact finite norm witness has been obtained, and the full inverse-limit argument is under review. No new infinite-module claim is counted as finished yet.

No formal timed progress review has yet occurred; the first remains15:39UTC, simultaneous with checkpoint04.

## 2026-11-24T15:24:19+00:00 — linear one-prime factor and other-base test cases

The proposed zero local/global-unit quotient is refuted. Full faithful class capitulation and unit cohomology prove an index7 universal-norm subgroup at every level. Compact inverse-limit exactness and explicit zero transitions on the capitulation cohomology prove the global and local faithful unit limits are free of rank1 over Lambda. Their localization is multiplication by f withv7(f(0))=1. The root read this complete proof.

A new exact finite-ring calculation in O/(pi16), withalpha3=269 and pi=beta+1, uses seven projected local generators at grades1,2,3,4,5,6,8. The global basis comes from the seven-saturated compact13-unit certificate. Root's ideal-HNF implementation and a separately written pi-adic carry implementation give identical global coordinates and both7x7matrices. Their determinants are28 and7mod49, proving both finite local-unit indices are7. The independent implementation uses no external arithmetic package and no root program. Root read its entire code and checked the carry relation.

The universal-norm index gives #V/((1+T)^7-1)V=49. Together withv7(f(0))=1 this forcesmu0,lambda1, soV=Lambda/(T-a),v7(a)=1. Rubin's no-finite-submodule theorem gives the same module forone-prime ramifiedX. Its analytic characteristic-generator valuesatT=8^-e-1 have valuation1+v7(e-e*) for aunique7-adicunite*, whereasstricts(e)=1always. The uncorrected characteristic-generator formula is therefore false. Matching a specifically normalized Katz measure remains separate. Full TeX integration and statement-only reconstruction are active; no human or formal verification is claimed.

The10page Q(i) note is now freshly built and visually inspected. It proves real nonvanishing of the quartic Hecke function, and strict cyclotomic Selmer vanishing for everyp=5mod8, all finite coefficient extensions and allcontinuouscyclotomiccharacters. It also proves -23 real nonvanishing using the precise classical eta identity and gives an explicit positive-Mellin-kernel counterexample to the abstract RH inference. Root read every proof. A separate worker is reconstructing the theorem from statements alone.

The cubic RH and the general S5 off-central problem remain open. No timed review has yet occurred; firstreview andcheckpoint04 remain due15:39UTC.

## 15:35 UTC — universal norms integrated

The full universal-norm proof is now in the 25-page Selmer manuscript, with the complete theorem in the opening, both exact local unit matrices, unique U1–U16 equation tags, and the corrected characteristic-generator comparison. A fresh two-pass build has no warnings or overfull boxes; all 25 pages were inspected. The root has read the full new proof and changed framing. Its separate statement-only reconstruction is still pending and is not claimed. Paper I integration is in progress.


# Formal progress review 1

Actual review: 2026-11-24T15:39:06+00:00. Scheduled three-hour review: 15:39 UTC (16:39 Europe/Berlin), 24 November 2026.

## Movement: YES

This is the first timed review, not a retrospective invented review. Since work began, the previously open matched seven-adic maximum has been resolved completely: every principal weight has strict length one. Its entire contribution has been removed from the unknown arithmetic remainder with an exact cost. The two initially open further S5 tests, discriminants30301 and48976, are certified, closing Q02b. The bare one-prime characteristic-generator comparison in Q09e is refuted by the proved linear factor with unbounded weight valuations. Several proposed structural implications have been refuted or corrected. The Q(i) and minus23 explicit tests are now proved at their stated real-nonvanishing and Selmer scope, with independent reconstruction status recorded separately. These are actual open-row changes; packaging, additional numerical checks, and restatements are not counted as movement.

## Main gates

The cubic RH remains open. The strongest arithmetic reduction excludes the entire matched seven-adic family and leaves the other mixed and noncritical terms. Analytically, the switched convolution deletes all inverse variables up to X^(1-delta) with rapid decay and leaves a long Mobius sum coupled to a direct variable below2X^delta; separate known bounds still do not reach square root. The quarter-power ideal-shell estimate remains open.

The general S5 real-zero condition remains open. Four explicit fields are closed. With the named external all-field Hecke theorem, a remaining real comparison pole lies in(1/2,3493459/4000000]. Boundary positive definiteness describes only the outer line; the interior divisor is uncontrolled. The new peeling obstructions and countermodels are research clarifications and are not counted as shrinking this gate.

The 3-primary K-group theorem and its finite certificates are checked, as are the seven-primary class stability theorem and strict specializations. The new universal-norm theorem is proved with two independent local arithmetic implementations and root full targeted reading; its separate statement-only reconstruction remains pending unless completed in the current check records.

## Every question row

| Row | Status | Current gate |
|---|---|---|
| Q01 | open | One-sided prime/ramp bound on arbitrarily late windows; arithmetic remainder excludes the entire matched7 family with exact cost2(T-1)log7 |
| Q01a | open | Exact fixed269 Patterson correlation; explicit long Liouville convolution or switched long Mobius convolution |
| Q01b | open | Uniform tower unit quotient and class-module specialization over growing host characters |
| Q01c | proved limited comparison; full chain open | All formal size and level hypotheses plus transfer of the target character |
| Q02 | open | Exclude comparison real poles alpha in(1/2,3493459/4000000] granting Liu2026 all-field zero-free theorem |
| Q02a | proved for four explicit fields | No remaining real-zero gate for discriminants8249,30301,48976,60061 |
| Q03 | proved reduction; bound open | Uniform lower bound of correct order for m3 |
| Q03a | proved comparison; estimate open | Exact linear centering including higher prime powers |
| Q04 | proved | Finite abelian image after Tate normalization, with converse via cyclotomic H0 |
| Q04a | proved | Actual sum-zero lisse sheaf; rational lifts only at split primes; relative lifts everywhere good |
| Q05 | proved | No remaining finite input or theorem reconstruction gap |
| Q05a | proved | ClE=C7² |
| Q05b | proved and strengthened | No remaining maximum in the matched7 family: s(e)=1 at every weight |
| Q05c | proved source distinction | XII5.1 arbitrary proper Cartesian base change;5.2 geometric stalk/fiber |
| Q06 | proved reduction; bound open | Exponent>1/2, every fixed modulus and delta, arbitrarily late power windows |
| Q07 | proved reduction; bound open | Upper bound for positive composite excess on same late windows |
| Q08a | proved comparison | GL2(F3) trace identity and quartic/sextic quotient |
| Q08b | proved comparison | Two distinct Eisenstein Hecke factors and extra composites |
| Q08c | refuted implication | Error X/log^(A+2)X is too large for square-root precision |
| Q08d | proved scope audit | Only listed coefficient269/tame branches and original hypotheses |
| Q08e | proved reduction; estimate open | Quarter-power error for fixed dyadic weight; available external-input error3493459/8000000+epsilon |
| Q08f | proved identity; bound open | Relative lower bound of order y^(-1/2+epsilon) |
| Q09a | proved factor identification; prime estimate open | Same faithful Kummer Hecke factor controls arithmetic and auxiliary-prime gates |
| Q09b | proved limitation | Centered positive square sum equals original cubic sum |
| Q09c | proved phase lemma; theta application open | A theta remainder whose commuting phase has no balanced multiplicities |
| Q09d | refuted; corrected theorem proved | n>=2 exact projector impossible even rationally; n1 denominator3; quotient-only denominator0 |
| Q09e | strict lengths proved; bare characteristic-generator formula refuted | s(e)=1 for all matched weights; one-prime characteristic factor T-a hasv7(a)=1 |
| Q09f | open | Uniform conductor and host estimates, plus every exceptional input |
| Q09g | proved | Kummer cyclic degree m dividing n with all divisor-order Hecke factors |
| Q09h | proved limited characterization; full algorithm open | Exact P145 hypotheses are absent from the attachments; its full eligible-input and complexity claim is not reconstructed |
| Q09i | proved exact implications with stated promises | Uniform varying-p beta input yields auxiliary prime logarithmic exponent1/(1-beta); fixed269 RH distinguished |
| Q09j | proved explicit analytic and arithmetic test cases; independent reconstruction active | Q(i) real nonvanishing and allp=5mod8 strict cyclotomic vanishing; -23 real nonvanishing |
| Q09k | open | Use any included prompt68 result; do not duplicate |
| Q02b | proved for both candidates | 30301 and48976 real-zero gates closed |

## Decision

Continue research. Consecutive timed reviews without movement:0. The next formal review is due16:39UTC (17:39 Europe/Berlin). A second no-movement review, if it occurs at17:39UTC, triggers finishing and delivery; future movement cannot be assumed or banked. Pending checks and manuscript integration proceed in parallel.

## Checkpoint04 saved

Scheduled15:39UTC; captured2026-11-24T15:39:06+00:00 and saved after the successful ZIP audit. File BEYOND_DIRICHLET_checkpoint_04.zip;68,886,420bytes;641members; SHA2568445939ad1e921aee0440fc448ee0572b24910cdb96520e140b7c3eb849b7647. Library id libfile_fde3_f-52ad5e3cdc0c8191805d238ab4b92c10_c6789dc4b4d481919ad633aabe6d84d0. No unchanged source identity matches; caches and all earlier checkpoints excluded. Next checkpoint16:24UTC; next formal review16:39UTC.


## 2026-11-24T16:13:43+00:00 — completed independent proofs and logarithmic direct range

The independent statement-only reconstructions of the seven-adic universal-norm theorem, the quartic and minus23 tests, and all six off-central S5 method assertions have been received and read in full by the root. They are same-model reproofs, not human or different-model reviews. Arithmetic grants in each packet remain explicitly separated from fresh calculations.

The cubic analytic gate has a stronger exact reduction: for fixed nonnegative nearly analytic weights with derivative growth k!log(e+k)^(rk), r>1, the direct norm is below2L_X, where L_X=(log3X)^2(log(e+log3X))^kappa and kappa>2r. The discarded range is O_M(X^-M) for everyM. Such weights exist in every open subinterval of(1,2), and their square-root remainder estimates are equivalent to cubicRH. The full uniform contour proof, summable-width construction, and independent reconstruction are complete. No square-root cancellation estimate has been proved. This genuinely shortens the direct range from every fixed power X^delta; its status will be assessed at the scheduled16:39UTC review, not by inventing an earlier review.

### Correction to numerical endpoint reporting; not counted as movement

The previous timed review used Liu's rational intermediate3493459/4000000. His already available main theorem gives the smaller algebraic boundary B*=0.873345856106718576801184796065... . The earlier follow-up note had already explicitly mentioned that main theorem while electing the rational intermediate. Therefore applying B* now is a correction and completion of quantitative reporting, not new literature discovery and not movement under the timed rule. Exact substitution, root isolation and mod11 irreducibility are in the new finite certificate. The full101-page analytic proof remains a named external input, not an independently verified theorem of this run. The corresponding shell exponent is B*/2 and the auxiliary-prime exponent is1/(1-B*)=7.895517424543... .

The S5 off-central method results do not shrink its general gate: the boundary does not control the interior divisor. The three countermodels each omit an explicitly identified hypothesis and are not a joint arithmetic counterexample.

## Checkpoint05 — 2026-11-24 16:24:15 UTC

Complete immutable snapshot captured at the scheduled45-minute interval and persisted. File BEYOND_DIRICHLET_checkpoint_05.zip;82,931,842bytes;746members;SHA2566b9f8c2469b7c013ebcb791a020c77ff9936216d904bece9f20dd592b97a3526. LibraryIDlibfile_fde3_f-79275c21defc81918afc4cec3205ce49_c6789dc4b4d481919ad633aabe6d84d0. No unchanged attached source was found by full identity audit; third-party texts and temporary software excluded. Next checkpoint17:09UTC. Next actual progress review16:39UTC. The common-host proof and completed independent reconstruction are in this snapshot, with parent whole-read still pending in its RESUME record.

## 2026-11-24T16:28:52+00:00 — common-host proof and independent reconstruction integrated

BD-R38–41 now record exact common Euler transfer, the conductor-uniform discriminant lower bound under Dirichlet GRH, its incompatibility with the literal scalar/discriminant budget, and the unconditional exponent-two/cyclic-quartic mismatch. The parent read all of both author TeX files, every relevant pinned definition, and the entire602line independent proof. All pass with the necessary proper-host qualification. An unrestricted numerical-only claim was corrected by the explicit F=K counterexample; the literal growing-degree hosts were never affected by that exception. The independent constructor uses a dual binary-kernel construction and effective Rosser–Schoenfeld bounds. The root also independently opened Bach–Sorenson Theorem5.1 and its page image.

Q01c now excludes the exact literal pointwise route under Dirichlet GRH and asks for a nonpointwise/equivariant comparison. Research on signed mixtures and the actual theta-group action continues. The stronger common-subfield obstruction is under investigation and is not yet recorded as a theorem. Q08e's stale next-step rational exponent and Q09j's stale pending-review text were corrected; these are reporting corrections, not movement.

# Formal progress review 2

Actual review: 2026-11-24T16:39:23+00:00. Scheduled hourly review:16:39UTC (17:39 Europe/Berlin),24November2026. Previous actual review:15:39:06UTC.

## Movement: YES

The analytic main gate has become strictly smaller since the preceding review. The earlier direct norm range below2X^delta is now below2(log(3X))^2(log(e+log(3X)))^kappa for every fixed kappa>2, with a discarded error smaller than every negative power ofX. The construction uses fixed nonnegative weights localized in any prescribed dyadic subinterval, and the remaining square-root bound for all such weights is equivalent to cubicRH. The entire full proof and separate statement-only reconstruction were completed and read by the root before this review. This is a support reduction of the existing main gate, not merely a restatement or improved numerical certificate.

The exact literal pointwise CM-host route in Q01c has also been refuted under DirichletGRH: a common multiquadratic host solves the scalar-window and full local-Euler-factor transfer problem, but any proper abelian host with exact transfer has log root discriminant at least c sqrt(x), whereas the literal size hypotheses force at most x^epsilon/72-log2. The proper-host qualification and the unrestricted F=K counterexample are explicit. Full author proofs, a separate statement-only reconstruction, and the exact pinned source definitions have been read in full. The constructed elementary-two group separately fails a required cyclic-quartic quotient; that group claim also has an independent reconstruction. This removes the exact ordinary pointwise route, while leaving a nonpointwise or equivariant theta comparison open.

## Further current mathematics, without extra movement credit

A new rational-content theorem proves large-content boundsY^(1+epsilon)R^(-3/2), and under zetaRH Y^(1+epsilon)R^(-7/4), with uniform moving smooth weights and growing finite Euler corrections. Its complete standalone proof and the integration as Theorem1.3/Section6 of the logarithmic convolution paper have been read by the root. The independent worker reports all five targets pass and is writing the complete record; final PDF QA and central statement integration are in progress. These results further delete the large-content portion at square-root cost, but do not improve the complete prime-sum exponent and leave r=1. No separate credit is needed or banked for their pending documentation.

The continuing literal-source analysis proves a common real two-power cyclotomic subfield, an unconditional obstruction to ordinary signed mixtures, and a highest-weight obstruction to the naive factor-permutation deck action. The root contributed to and has read the common-subfield and size arguments; a new statement-only reconstruction is still to be assigned. The genuine source gain is indexed by rational residue characteristic, not by degree-one prime ideals, so these obstructions do not negate the source theta mechanism. An abstract Artin projector identifies a possible fixed four-dimensional quotient, but neither its actual theta realization nor a projected lower gain has been proved. These findings are recorded as ongoing and not counted separately as a completed main-gate advance at this review.

Completed independent reconstructions of the seven universal-norm theorem, imaginary-quadratic tests, and S5 off-central method results have all been read by the root. Those checks and the fresh manuscripts are not themselves movement. The sharper Liu main constantB*=0.873345856106718576801... was already identified in an earlier follow-up; replacing a displayed intermediate rational value is a reporting correction, explicitly not new mathematical movement.

## Main questions still open

CubicRH remains open. The exact matched-seven arithmetic contribution is fully removed at cost2(T-1)log7. Other mixed/noncritical terms remain. Analytically the new logarithmic direct range and the smaller rational-content range still require the indicated long Mobius cancellation. Its primitive coefficient series has a nonvanishing Euler multiplier times1/P(s), so every possible off-line zero pole remains. The ideal-shell quarter-power estimate remains open; the named external bound isB*/2=0.436672928053359... .

The generalS5 real-zero condition remains open. Four explicit fields are completely certified. With the separately named external all-field Hecke theorem, the remaining comparison real pole lies in(1/2,B*]. Boundary positive definiteness does not control the interior divisor. The complete peeling obstructions and finite-progression sufficient theorem do not shrink this interval. A zero-density literature check supplies no missing argument, since an isolated outer real pole is still permitted by the boundary classification.

## Every question row at the review

| Row | Status | Current gate |
|---|---|---|
| Q01 | open | One-sided prime/ramp bound on arbitrarily late windows; arithmetic remainder excludes the entire matched7 family with exact cost2(T-1)log7 |
| Q01a | open | Exact fixed269 long Mobius convolution with direct norm<2(log3X)^2(log(e+log3X))^kappa, any fixed kappa>2 |
| Q01b | open | Uniform tower unit quotient and class-module specialization over growing host characters |
| Q01c | exact literal pointwise route refuted under Dirichlet GRH; weighted/equivariant chain open | A viable non-pointwise or equivariant theta comparison satisfying every literal host condition |
| Q02 | open | Exclude real comparison poles alpha in(1/2,B*], B*=0.873345856106718576801..., granting Liu2026 main theorem |
| Q02a | proved for four explicit fields | No remaining real-zero gate for discriminants8249,30301,48976,60061 |
| Q03 | proved reduction; bound open | Uniform lower bound of correct order for m3 |
| Q03a | proved comparison; estimate open | Exact linear centering including higher prime powers |
| Q04 | proved | Finite abelian image after Tate normalization, with converse via cyclotomic H0 |
| Q04a | proved | Actual sum-zero lisse sheaf; rational lifts only at split primes; relative lifts everywhere good |
| Q05 | proved | No remaining finite input or theorem reconstruction gap |
| Q05a | proved | ClE=C7² |
| Q05b | proved and strengthened | No remaining maximum in the matched7 family: s(e)=1 at every weight |
| Q05c | proved source distinction | XII5.1 arbitrary proper Cartesian base change;5.2 geometric stalk/fiber |
| Q06 | proved reduction; bound open | Exponent>1/2, every fixed modulus and delta, arbitrarily late power windows |
| Q07 | proved reduction; bound open | Upper bound for positive composite excess on same late windows |
| Q08a | proved comparison | GL2(F3) trace identity and quartic/sextic quotient |
| Q08b | proved comparison | Two distinct Eisenstein Hecke factors and extra composites |
| Q08c | refuted implication | Error X/log^(A+2)X is too large for square-root precision |
| Q08d | proved scope audit | Only listed coefficient269/tame branches and original hypotheses |
| Q08e | proved reduction; estimate open | Quarter-power error for fixed dyadic weight; available named external-input error B*/2+epsilon=0.436672928053359...+epsilon |
| Q08f | proved identity; bound open | Relative lower bound of order y^(-1/2+epsilon) |
| Q09a | proved factor identification; prime estimate open | Same faithful Kummer Hecke factor controls arithmetic and auxiliary-prime gates |
| Q09b | proved limitation | Centered positive square sum equals original cubic sum |
| Q09c | proved phase lemma; theta application open | A theta remainder whose commuting phase has no balanced multiplicities |
| Q09d | refuted; corrected theorem proved | n>=2 exact projector impossible even rationally; n1 denominator3; quotient-only denominator0 |
| Q09e | strict lengths proved; bare characteristic-generator formula refuted | s(e)=1 for all matched weights; one-prime characteristic factor T-a hasv7(a)=1 |
| Q09f | open | Uniform conductor and host estimates, plus every exceptional input |
| Q09g | proved | Kummer cyclic degree m dividing n with all divisor-order Hecke factors |
| Q09h | proved limited characterization; full algorithm open | Exact P145 hypotheses are absent from the attachments; its full eligible-input and complexity claim is not reconstructed |
| Q09i | proved exact implications with stated promises | Uniform varying-p beta input yields auxiliary prime logarithmic exponent1/(1-beta); fixed269 RH distinguished |
| Q09j | proved explicit analytic and arithmetic test cases; complete independent reconstruction | Q(i) real nonvanishing and allp=5mod8 strict cyclotomic vanishing; -23 real nonvanishing |
| Q09k | open | Use any included prompt68 result; do not duplicate |
| Q02b | proved for both candidates | 30301 and48976 real-zero gates closed |

## Decision

Continue research. Consecutive actual timed reviews without movement:0. Next actual review is due17:39UTC (18:39 Europe/Berlin), then18:39UTC. The stopping rule remains two consecutive actual no-movement reviews; no future movement is assumed. Next complete checkpoint is due17:09UTC.


### 2026-11-24T16:51:30+00:00 — complete content verification and integration

BD-R42–44 are now integrated with full author and independent proofs. The root read the entire separate reconstruction and inspected all22 revised pages. The stronger content bound is explicitly conditional on classical zeta RH; no cubic RH is claimed. The proof was already available and read at the16:39 review, so this integration is **not banked as movement for the next review**. The statement-only record is SHA256c0d7b50bc8d1892b930ba30b5e8b65636326d611a36731e8d947d04be74af396.

### 2026-11-24T17:04:13+00:00 — literal-host continuation fully reconstructed

Integrated BD-R45–48. The unconditional ordinary-Euler obstruction and the explicit fixed quotient now have complete author and statement-only independent proofs, read in full by the root. Small-prime order, candidate, penalty and NoGain consequences are one coherent continuation, not separate progress credits. The uniform-inclusion correction is a correction of scope, not a new cancellation estimate. The next actual progress review remains17:39UTC.

### 2026-11-24T17:20:33+00:00 — balanced fixed-k note checked and integrated

BD-R49–51 now have complete author and separate statement-only proofs, both root-read. The fresh two-pass build has no warnings; all10 pages were viewed. The classical identity and support shortening are credited to Heath–Brown. This entry is not an automatic progress credit: the17:39 review must distinguish the new formulation from genuine status changes or removal of a strictly smaller part of the remaining main gate. The joint-content packet has meanwhile received a root statement-only reconstruction, but its author-proof comparison and paper integration are separate pending steps.


# Actual progress review 03

Actual time: **2026-11-24T17:39:52+00:00**. Scheduled time: 17:39 UTC, 24 November 2026. Work began at 12:39 UTC. This is the third actual timed review, after the reviews at 15:39:06 and 16:39:23.

**Movement: YES. Consecutive reviews without movement: 0.** Continue research. The next actual review is due at 18:39 UTC; the next checkpoint is due at 17:54 UTC.

## What changed a main gate since the preceding review

1. **Cubic analytic gate.** The complete smooth-capped two-ideal identity is now combined with a joint rational-content estimate. The part with product of the individual contents exceeding R is bounded by Y^(1+epsilon) R^(-3/2) log(2+U²/Y), or R^(-7/4) under classical zeta RH. At R=Y^(1/3), or Y^(2/7), this removes a nonempty part of the balanced expression at square-root cost. The remaining inverse variables are both of square-root size up to logarithms, and their primitive norm product is greater than Y^(1/3)/4, or Y^(3/7)/4. The complete author proof and a separate root statement-only reconstruction were finished and reciprocally read before this review. The stronger conditional estimate is not called unconditional cubic RH. The 12-page standalone paper prints every dependency; a minor exponent-comma typesetting error was corrected and rebuilt before this review. No estimate for the surviving signed sum is proved.

2. **S5 analytic gate.** Every comparison pole of order r in the open strip is now proved to be a zero of order at least r of BOTH B and the distinct explicit quadratic Hecke function C=ζ_J'/ζ_J, where J and J' have degrees10 and20. The exact exterior-square local discrepancy equals the original positive defect factor, and Belt's odd-rank partial exterior-square holomorphy gives the additional divisor condition. Therefore absence of common off-central real zeros suffices, while arbitrary central multiplicity is still allowed. The new full author proof and separate root statement-only reconstruction are complete and reciprocally read; the prior central-divisor theorem and named published analytic inputs are explicitly granted in that reconstruction. The paper is being reorganized around this stronger criterion. No absence of common zeros and no smaller numerical endpoint is asserted.

These are not credits for merely writing or packaging equivalent formulas: the first establishes cancellation on an explicitly nonempty deleted region; the second proves an additional necessary divisor condition and weakens the sufficient real-zero hypothesis. No example asserting existence of an off-central Hecke zero is claimed.

## Results not counted as separate movement

The fixed-k Heath–Brown identity and variable-balancing formulation alone are not a cancellation estimate. The rational-content proof already available at16:39 is not banked. The later integration of that proof, fresh builds, review completion and checkpoint saving are not movement. The known Pilloni–Stroh removal of the local-five assumption broadens applicability but is not credited as a new advance on the off-central analytic obstruction. The exact source-gain and equivariance obstructions refine the construction audit; no cubic theta realization or trace estimate has resulted. The corrected numerical Liu endpoint is not a new theorem. All components of the joint-content continuation receive one progress credit, not one per displayed predicate or exponent.

## Proof records for this review

- Joint-content author proof: reviews/cubic_joint_content_author_proof.md. Separate root reconstruction: reviews/cubic_joint_content_root_blind.md, SHA-256 e506a1d81ea4581de55b4ae3513575a7bcdd7bc27518ea3b8cc0a46eb6ac46a5. Current standalone PDF SHA-256 82e1c602f5dc54be51acf6de9f9056ec5979d57b5b84b7d1bc8d46bfaeb7963a.
- Common-zero author proof: reviews/s5_common_zero_proof.md. Separate root reconstruction: reviews/s5_common_zero_root_blind.md, SHA-256 3dfc196e0f2ae4ed384f254310ad7aaa120c26038a2090295c97fbf63c7ab090. Every shared input and exposure limit is disclosed.
- Both main questions remain open. The following complete question snapshot supplies each current gate.

## Complete question snapshot

| Question | Status | Current gate | Next step |
|---|---|---|---|
| Q01 | open | Square-root cancellation for the joint-content-reduced balanced fixed269 sum for every localized nearly analytic nonnegative weight, or the exact remaining arithmetic budget after the matched7 family is removed | Estimate the remaining balanced primitive-product expression or construct the missing coherent cubic theta comparison; do not count further support reformulations as cancellation |
| Q01a | open | Two balanced inverse ideals with U/(4L)<Nd_i<2U, U=sqrt(2X), direct norm<2L, L=log^4X loglog^kappaX, and product of primitive norms>(X/Nc)^(1/3)/4, or exponent3/7 under classical zeta RH | Bound the remaining signed sum at square-root scale. Quantify whether the two-ideal variables supply the shift average needed by current quadratic-polynomial estimates; generic rank-one character Cauchy bounds do not suffice. |
| Q01b | open | Uniform tower unit quotient and class-module specialization over growing host characters | Uniform estimates for other growing host characters and coefficient primes; fixed matched7 family is settled |
| Q01c | ordinary literal host-transfer route refuted unconditionally; equivariant theta comparison open | A coherent equivariant theta realization of the fixed four-factor quotient with correct trace, integral-lattice and centering comparison; uniform inclusion would inherit after compatible projection | Construct a coherent enlarged orbit module and maps, identify cubic prime traces and the new centering constant, and verify that the uniform inclusion applies to the needed source lattice. No cubic cancellation estimate exists yet. |
| Q02 | open | Exclude common real zeros of B=zeta_H/zeta_F and C=zeta_Jprime/zeta_J at a possible comparison pole alpha>1/2, with pole order r≤min(ordB,ordC); optional Liu input still limits alpha≤B* | Prove absence of the common-zero obstruction or obtain another independent analytic condition; no new endpoint B* or unconditional common-zero theorem is claimed |
| Q02a | proved for four explicit fields | No remaining real-zero gate for discriminants8249,30301,48976,60061 | General family and off-central-pole theorem remain separate open questions |
| Q03 | proved reduction; bound open | Uniform lower bound of correct order for m3 | Supply arithmetic lower bound with exact quantifiers |
| Q03a | proved comparison; estimate open | Exact linear centering including higher prime powers | Bound centered prime ramp |
| Q04 | proved | Finite abelian image after Tate normalization, with converse via cyclotomic H0 | No remaining step in stated category theorem |
| Q04a | proved | Actual sum-zero lisse sheaf; rational lifts only at split primes; relative lifts everywhere good | Aggregate Frobenius distribution remains Q01 |
| Q05 | proved | No remaining finite input or theorem reconstruction gap | Maintain source and certificate reproducibility |
| Q05a | proved | ClE=C7² | No remaining arithmetic input |
| Q05b | proved and strengthened | No remaining maximum in the matched7 family: s(e)=1 at every weight | Other mixed/noncritical families remain in Q01 |
| Q05c | proved source distinction | XII5.1 arbitrary proper Cartesian base change;5.2 geometric stalk/fiber | No K-theory/RH inference from these alone |
| Q06 | proved reduction; bound open | Exponent>1/2, every fixed modulus and delta, arbitrarily late power windows | Exact arithmetic inequality remains Q01 |
| Q07 | proved reduction; bound open | Upper bound for positive composite excess on same late windows | No arbitrary-weight bilinear saving can hold |
| Q08a | proved comparison | GL2(F3) trace identity and quartic/sextic quotient | Does not bound signed prime excess |
| Q08b | proved comparison | Two distinct Eisenstein Hecke factors and extra composites | Control separate composite term |
| Q08c | refuted implication | Error X/log^(A+2)X is too large for square-root precision | A stronger unweighted estimate is required |
| Q08d | proved scope audit | Only listed coefficient269/tame branches and original hypotheses | Other mixed/noncritical terms remain |
| Q08e | proved reduction; estimate open | Quarter-power error for fixed dyadic weight; available named external-input error B*/2+epsilon=0.436672928053359...+epsilon | Close the remaining exponent gap B*/2-1/4=0.186672928053359...; external101page analytic proof is not independently audited |
| Q08f | proved identity; bound open | Relative lower bound of order y^(-1/2+epsilon) | Need distribution-sensitive determinant/period comparison |
| Q09a | proved factor identification; prime estimate open | Same faithful Kummer Hecke factor controls arithmetic and auxiliary-prime gates | Algorithmic consequences proved with exact promises in Q09i; uniform prime bound remains the shared analytic input |
| Q09b | proved limitation | Centered positive square sum equals original cubic sum | Need centered square-root cancellation |
| Q09c | proved phase lemma; theta application open | A theta remainder whose commuting phase has no balanced multiplicities | Find a noncanceling trace identity for the fixed269 prime statistic |
| Q09d | refuted; corrected theorem proved | n>=2 exact projector impossible even rationally; n1 denominator3; quotient-only denominator0 | Different nonunit projector is a separate question |
| Q09e | strict lengths proved; bare characteristic-generator formula refuted | s(e)=1 for all matched weights; one-prime characteristic factor T-a hasv7(a)=1 | Identify any specifically normalized Katz measure separately; it cannot supply strict length without local denominator and finite-kernel corrections |
| Q09f | open | Uniform conductor and host estimates, plus every exceptional input | Trace field-dependent class/unit assumptions |
| Q09g | proved | Kummer cyclic degree m dividing n with all divisor-order Hecke factors | No gap in stated factorization; RH of nonabelian factors remains open |
| Q09h | proved limited characterization; full algorithm open | Exact P145 hypotheses are absent from the attachments; its full eligible-input and complexity claim is not reconstructed | Obtain complete P145 statement before claiming a classification for that algorithm |
| Q09i | proved exact implications with stated promises | Uniform varying-p beta input yields auxiliary prime logarithmic exponent1/(1-beta); fixed269 RH distinguished | No claim of promise-free complexity or RH is made |
| Q09j | proved explicit analytic and arithmetic test cases; complete independent reconstruction | Q(i) real nonvanishing and allp=5mod8 strict cyclotomic vanishing; -23 real nonvanishing | No remaining proof/check step in the stated tests; a complex-zero RH bound is still absent for either arithmetic function |
| Q09k | open | Use any included prompt68 result; do not duplicate | Inspect exact fixed-sector trace positivity hypotheses; do not infer a Hecke trace limit from rational case |
| Q02b | proved for both candidates | 30301 and48976 real-zero gates closed | No remaining step for these two candidates; pursue the general off-central gate |

### 2026-11-24T17:46:34+00:00 — integration of the already credited continuation

BD-R52–53 and BD-S23–26 now record the joint-content and common-zero results. Their proof statuses are stated individually; root has fully read the new independent scope reconstruction and inspected every page of the joint paper. This is integration of the17:39 mathematical movement, not fresh movement for18:39. The elementary transport analysis has a complete targeted root read; source-interface and independent-review limits are preserved.


### 2026-11-24T18:28:43+00:00 — stronger joint-content theorem completed before review04

BD-R54–56 strengthen the tail estimate by keeping ideal norm and rational content in the same Euler product. The two-input specialization beta=rho=B* reduces the cutoff from1/3 to0.284992750196395; the zeta-RH specialization reduces2/7 to0.249447399928862. Nonzero arithmetic summands and asymptotic support inclusion establish literal strictness. Both complete separate derivations and the targeted audit were read in full by root; the current17-page paper was freshly built through stable references and every page inspected. This is a candidate genuine gate reduction for the18:39 actual review, not a review conducted early.

The transport and GMPP conclusions are now individually registered with their exact checks and qualifications. They do not by themselves establish another main-gate reduction. BD-S27–28 record the conditional transfer identities already present in PaperII, with standalone reproof scope still distinguished. Both main RH/common-zero estimates remain open; the actual no-movement counter is unchanged until the scheduled review.


## Actual progress review04 —24November2026

Actual time: **2026-11-24T18:39:13+00:00**. Scheduled18:39UTC,24November2026. Research began12:39UTC. Previous actual reviews15:39:06,16:39:23,17:39:52 all recorded movement.

**Movement: YES. Consecutive reviews without movement:0.** Continue research. Next actual review19:39UTC. Checkpoint08 is due now; next checkpoint19:24UTC.

## Strict reduction established since review03

The fixed cubic analytic gate has become strictly smaller. Keeping ideal norm and rational content in the same Euler product gives the two-input signed-tail bound Y^(beta+epsilon)R^(-a)log(2+U²/Y), where a=2beta-max(rho/2,1-beta), beta is a cubic-Hecke zero-free exponent and rho is a zeta zero-free exponent. At gamma=(beta-1/2)/a this deleted region has square-root size. The named external Liu input beta=rho=B* yields gamma=0.2849927501963953104291995149000585, below the previous1/3 cutoff, and primitive-product exponent0.430014499607209379141600970199883. With classical zeta RH gamma=0.2494473999288620593275902011805893, below the previous2/7. Fixed split primes and squarefree contents construct nonzero arithmetic summands in the difference of the two regions, while uniform asymptotic support inclusion proves the new remaining support is genuinely smaller. This is a proved cancellation estimate on an additional nonempty region, not merely an equivalent rewriting.

The current17-page paper includes the complete proof. A separate statement-only reconstruction of A-D and an independently derived two-input extension were frozen before their authors saw the new proof; their earlier balanced-identity and zero-detector grants are explicit. Root has read all complete proofs plus both full targeted audits. Exact rational input intervals give outward decimal exponents. All17final pages were viewed after a fresh stable three-pass build. Root receiptreviews/cubic_joint_two_input_root_review.json records exact hashes. The external101-page Liu proof is not independently reconstructed.

## Not counted as further movement

The old joint-content result and S5 common-zero criterion were already credited at17:39. The transport and GMPP companions now have full separate reconstructions and all-page root inspection, but do not prove another main-gate reduction. The recent Asai source audit excludes specific imports by their hypotheses but does not give the missingGL9transfer or common-zero exclusion. The generic secondary Euler-factor refinement currently being written changes a conditional parameter range but gives no improvement at the actualB*input; no progress credit is awarded for it. Fixed-character extraction from the varying-cubic moments has not yet beaten the existing bound. Writing, checking, source integration and checkpointing are not movement.

Both main targets remain OPEN. No absence of complex cubic zeros, no cancellation for the full surviving balanced sum, and no unconditionalS5common-zero exclusion is claimed.

## Complete question snapshot

| Question | Status | Current gate | Next step |
|---|---|---|---|
| Q01 | open | Square-root cancellation for every localized weight in the strictly smaller two-input joint-content balanced fixed269 sum; under imported Liu beta=rho=B*, gamma0.284992750196395, or gamma0.249447399928862 with classical zeta RH | Estimate the remaining balanced primitive-product expression or construct the missing coherent cubic theta comparison; do not count further support reformulations as cancellation |
| Q01a | open | Two balanced inverse ideals with direct norm<2L and product content<2Y^gamma; primitive norm product>Y^(1−2gamma)/4, exponent0.430014499607209 with both Liu inputs or0.501105200142275 under zeta RH | Bound the surviving signed primitive bulk; test the primary varying-cubic moments and genuinely new arithmetic estimates. Asymmetric contour restatements alone are not movement. |
| Q01b | open | Uniform tower unit quotient and class-module specialization over growing host characters | Uniform estimates for other growing host characters and coefficient primes; fixed matched7 family is settled |
| Q01c | ordinary literal host-transfer route refuted unconditionally; equivariant theta comparison open | A coherent equivariant theta realization of the fixed four-factor quotient with correct trace, integral-lattice and centering comparison; uniform inclusion would inherit after compatible projection | Construct a genuinely new theta-chain intertwiner with the fixed cubic Frobenius trace and projected cost; transported regular copies alone do not do so. |
| Q02 | open | Exclude common real zeros of B=zeta_H/zeta_F and C=zeta_Jprime/zeta_J at a possible comparison pole alpha>1/2, with pole order r≤min(ordB,ordC); optional Liu input still limits alpha≤B* | Prove absence of the common-zero obstruction or obtain another independent analytic condition; no new endpoint B* or unconditional common-zero theorem is claimed |
| Q02a | proved for four explicit fields | No remaining real-zero gate for discriminants8249,30301,48976,60061 | General family and off-central-pole theorem remain separate open questions |
| Q03 | proved reduction; bound open | Uniform lower bound of correct order for m3 | Supply arithmetic lower bound with exact quantifiers |
| Q03a | proved comparison; estimate open | Exact linear centering including higher prime powers | Bound centered prime ramp |
| Q04 | proved | Finite abelian image after Tate normalization, with converse via cyclotomic H0 | No remaining step in stated category theorem |
| Q04a | proved | Actual sum-zero lisse sheaf; rational lifts only at split primes; relative lifts everywhere good | Aggregate Frobenius distribution remains Q01 |
| Q05 | proved | No remaining finite input or theorem reconstruction gap | Maintain source and certificate reproducibility |
| Q05a | proved | ClE=C7² | No remaining arithmetic input |
| Q05b | proved and strengthened | No remaining maximum in the matched7 family: s(e)=1 at every weight | Other mixed/noncritical families remain in Q01 |
| Q05c | proved source distinction | XII5.1 arbitrary proper Cartesian base change;5.2 geometric stalk/fiber | No K-theory/RH inference from these alone |
| Q06 | proved reduction; bound open | Exponent>1/2, every fixed modulus and delta, arbitrarily late power windows | Exact arithmetic inequality remains Q01 |
| Q07 | proved reduction; bound open | Upper bound for positive composite excess on same late windows | No arbitrary-weight bilinear saving can hold |
| Q08a | proved comparison | GL2(F3) trace identity and quartic/sextic quotient | Does not bound signed prime excess |
| Q08b | proved comparison | Two distinct Eisenstein Hecke factors and extra composites | Control separate composite term |
| Q08c | refuted implication | Error X/log^(A+2)X is too large for square-root precision | A stronger unweighted estimate is required |
| Q08d | proved scope audit | Only listed coefficient269/tame branches and original hypotheses | Other mixed/noncritical terms remain |
| Q08e | proved reduction; estimate open | Quarter-power error for fixed dyadic weight; available named external-input error B*/2+epsilon=0.436672928053359...+epsilon | Close the remaining exponent gap B*/2-1/4=0.186672928053359...; external101page analytic proof is not independently audited |
| Q08f | proved identity; bound open | Relative lower bound of order y^(-1/2+epsilon) | Need distribution-sensitive determinant/period comparison |
| Q09a | proved factor identification; prime estimate open | Same faithful Kummer Hecke factor controls arithmetic and auxiliary-prime gates | Algorithmic consequences proved with exact promises in Q09i; uniform prime bound remains the shared analytic input |
| Q09b | proved limitation | Centered positive square sum equals original cubic sum | Need centered square-root cancellation |
| Q09c | proved phase lemma; theta application open | A theta remainder whose commuting phase has no balanced multiplicities | Find a noncanceling trace identity for the fixed269 prime statistic |
| Q09d | refuted; corrected theorem proved | n>=2 exact projector impossible even rationally; n1 denominator3; quotient-only denominator0 | Different nonunit projector is a separate question |
| Q09e | strict lengths proved; bare characteristic-generator formula refuted | s(e)=1 for all matched weights; one-prime characteristic factor T-a hasv7(a)=1 | Identify any specifically normalized Katz measure separately; it cannot supply strict length without local denominator and finite-kernel corrections |
| Q09f | open | Uniform conductor and host estimates, plus every exceptional input | Trace field-dependent class/unit assumptions |
| Q09g | proved | Kummer cyclic degree m dividing n with all divisor-order Hecke factors | No gap in stated factorization; RH of nonabelian factors remains open |
| Q09h | proved limited characterization; full algorithm open | Exact P145 hypotheses are absent from the attachments; its full eligible-input and complexity claim is not reconstructed | Obtain complete P145 statement before claiming a classification for that algorithm |
| Q09i | proved exact implications with stated promises | Uniform varying-p beta input yields auxiliary prime logarithmic exponent1/(1-beta); fixed269 RH distinguished | No claim of promise-free complexity or RH is made |
| Q09j | proved explicit analytic and arithmetic test cases; complete independent reconstruction | Q(i) real nonvanishing and allp=5mod8 strict cyclotomic vanishing; -23 real nonvanishing | No remaining proof/check step in the stated tests; a complex-zero RH bound is still absent for either arithmetic function |
| Q09k | open | Use any included prompt68 result; do not duplicate | Inspect exact fixed-sector trace positivity hypotheses; do not infer a Hecke trace limit from rational case |
| Q02b | proved for both candidates | 30301 and48976 real-zero gates closed | No remaining step for these two candidates; pursue the general off-central gate |


# Actual progress review 05

Actual time: **2026-11-24T19:39:03+00:00**. Scheduled19:39UTC,24November2026;20:39Berlin. Research began12:39UTC. Previous actual review04 at18:39:13UTC recorded movement from the stronger two-input joint-content support reduction.

**Movement: NO. Consecutive reviews without movement:1.** Continue research under the user's rule. The next actual review is20:39UTC; only if that review also finds no movement may research stop. The next checkpoint is20:09UTC.

## Main-question gates and comparison with review04

For the cubic function zeta_Q(cuberoot269)/zeta, the remaining theorem is still square-root cancellation for every prescribed localized weight in the balanced fixed-character convolution. The proved content cutoff is gamma=(beta−1/2)/(2beta−rho/2). With the already imported Liu inputs beta=rho=B*, its numerical value remains0.2849927501963953104291995149000585 and the primitive-product exponent remains0.430014499607209379141600970199883. With the already stated classical-zeta-RH input the corresponding values remain0.2494473999288620593275902011805893 and0.501105200142275881344819597638821. These are the same effective gates as at review04.

The general analytic tube now needs no extra mixed real-part restriction. This strengthens the formula for some other hypothetical zero-free input pairs, but no stronger applicable input was proved, so it is not movement. All-mixed Euler extraction proves a quarter-line boundary for a full holomorphic tube and an exact multiplicity-inclusive pole count. It does not bound the signed residues or the remaining balanced sum.

The natural-row cubic moment route has been carried through exact deletion reconstruction, shifted amplification, and unrestricted-block accounting. The character269 is admissible. The complete bounds still retain the absolute-counting exponent, including the principal-row cost P^(1/3)Q². The density exponent remains larger than the P^(1/3) presentation-fiber exponent. These are fully proved applicability and method-scope results, not a closed arithmetic cancellation question. Residue subtraction has also been investigated with both norm caps and the cofactor shift preserved; no better complete double-residue estimate or strict support improvement has been established at this review. Any unfinished independent checking of that research note is not counted as progress.

For the general S5 problem, the absence of the relevant common off-central real zeros remains unproved. The existing main criterion uses the two entire Hecke factors B,C, with the earlier Artin-factor variant L(R),C also available. The proposed symmetric-square third-zero condition was fully independently reconstructed and integrated, but zeta_T=L(V)L(R)zeta_F proves that it is subsumed by that earlier Artin-factor variant. No new field, endpoint, transfer, or nonvanishing theorem was established. The four explicit fields remain certified as before.

No previously open question row has changed mathematical status since review04. Completed checking, exact-source corrections, independent reconstructions, new method boundaries, paper revisions, deposits, and checkpointing are not movement. Both main targets remain OPEN. No cubic RH proof or unconditional general S5 common-zero exclusion is claimed.

## Current documentation and precise check scopes

The joint-content companion is18pages with a full reciprocal-growth lemma; the all-mixed companion is8pages; the natural-row moment companion is17pages; the S5 paper is43pages after its redundancy appendix. Mathematical source readings, separate statement-only proofs and grants are recorded individually. The current S5 amendment has affected-page QA on38–43 only; final all-page QA remains to be performed after the coordinated editorial/provenance revision. Root has read the complete independent cube/amplifier proof, all-mixed proof and manuscript, moment manuscript, symmetric-square independent proof, and current AppendixD. Exact exposure records prevent upgrading targeted checks to independent re-proofs.

Checkpoint09 was captured19:24:05UTC and saved as a complete immutable ZIP, with integrityPASS and zero unchanged-source matches. Final source-manifest/local-git provenance, final editorial opening compliance, remaining deposits and final builds/page inspections are work in progress; they are not mathematical progress.

## Complete question snapshot

| Question | Status | Current gate | Next step |
|---|---|---|---|
| Q01 | open | Square-root cancellation for every localized weight in the strictly smaller two-input joint-content balanced fixed269 sum; under imported Liu beta=rho=B*, gamma0.284992750196395, or gamma0.249447399928862 with classical zeta RH | Estimate the remaining balanced primitive-product expression or construct the missing coherent cubic theta comparison; do not count further support reformulations as cancellation |
| Q01a | open | Two balanced inverse ideals with direct norm<2L and product content<2Y^gamma; primitive norm product>Y^(1−2gamma)/4, exponent0.430014499607209 with both Liu inputs or0.501105200142275 under zeta RH | Bound the surviving signed primitive bulk; test the primary varying-cubic moments and genuinely new arithmetic estimates. Asymmetric contour restatements alone are not movement. |
| Q01b | open | Uniform tower unit quotient and class-module specialization over growing host characters | Uniform estimates for other growing host characters and coefficient primes; fixed matched7 family is settled |
| Q01c | ordinary literal host-transfer route refuted unconditionally; equivariant theta comparison open | A coherent equivariant theta realization of the fixed four-factor quotient with correct trace, integral-lattice and centering comparison; uniform inclusion would inherit after compatible projection | Construct a genuinely new theta-chain intertwiner with the fixed cubic Frobenius trace and projected cost; transported regular copies alone do not do so. |
| Q02 | open | Exclude common real zeros of B=zeta_H/zeta_F and C=zeta_Jprime/zeta_J at a possible comparison pole alpha>1/2, with pole order r≤min(ordB,ordC); optional Liu input still limits alpha≤B* | Prove absence of the common-zero obstruction or obtain another independent analytic condition; no new endpoint B* or unconditional common-zero theorem is claimed |
| Q02a | proved for four explicit fields | No remaining real-zero gate for discriminants8249,30301,48976,60061 | General family and off-central-pole theorem remain separate open questions |
| Q03 | proved reduction; bound open | Uniform lower bound of correct order for m3 | Supply arithmetic lower bound with exact quantifiers |
| Q03a | proved comparison; estimate open | Exact linear centering including higher prime powers | Bound centered prime ramp |
| Q04 | proved | Finite abelian image after Tate normalization, with converse via cyclotomic H0 | No remaining step in stated category theorem |
| Q04a | proved | Actual sum-zero lisse sheaf; rational lifts only at split primes; relative lifts everywhere good | Aggregate Frobenius distribution remains Q01 |
| Q05 | proved | No remaining finite input or theorem reconstruction gap | Maintain source and certificate reproducibility |
| Q05a | proved | ClE=C7² | No remaining arithmetic input |
| Q05b | proved and strengthened | No remaining maximum in the matched7 family: s(e)=1 at every weight | Other mixed/noncritical families remain in Q01 |
| Q05c | proved source distinction | XII5.1 arbitrary proper Cartesian base change;5.2 geometric stalk/fiber | No K-theory/RH inference from these alone |
| Q06 | proved reduction; bound open | Exponent>1/2, every fixed modulus and delta, arbitrarily late power windows | Exact arithmetic inequality remains Q01 |
| Q07 | proved reduction; bound open | Upper bound for positive composite excess on same late windows | No arbitrary-weight bilinear saving can hold |
| Q08a | proved comparison | GL2(F3) trace identity and quartic/sextic quotient | Does not bound signed prime excess |
| Q08b | proved comparison | Two distinct Eisenstein Hecke factors and extra composites | Control separate composite term |
| Q08c | refuted implication | Error X/log^(A+2)X is too large for square-root precision | A stronger unweighted estimate is required |
| Q08d | proved scope audit | Only listed coefficient269/tame branches and original hypotheses | Other mixed/noncritical terms remain |
| Q08e | proved reduction; estimate open | Quarter-power error for fixed dyadic weight; available named external-input error B*/2+epsilon=0.436672928053359...+epsilon | Close the remaining exponent gap B*/2-1/4=0.186672928053359...; external101page analytic proof is not independently audited |
| Q08f | proved identity; bound open | Relative lower bound of order y^(-1/2+epsilon) | Need distribution-sensitive determinant/period comparison |
| Q09a | proved factor identification; prime estimate open | Same faithful Kummer Hecke factor controls arithmetic and auxiliary-prime gates | Algorithmic consequences proved with exact promises in Q09i; uniform prime bound remains the shared analytic input |
| Q09b | proved limitation | Centered positive square sum equals original cubic sum | Need centered square-root cancellation |
| Q09c | proved phase lemma; theta application open | A theta remainder whose commuting phase has no balanced multiplicities | Find a noncanceling trace identity for the fixed269 prime statistic |
| Q09d | refuted; corrected theorem proved | n>=2 exact projector impossible even rationally; n1 denominator3; quotient-only denominator0 | Different nonunit projector is a separate question |
| Q09e | strict lengths proved; bare characteristic-generator formula refuted | s(e)=1 for all matched weights; one-prime characteristic factor T-a hasv7(a)=1 | Identify any specifically normalized Katz measure separately; it cannot supply strict length without local denominator and finite-kernel corrections |
| Q09f | open | Uniform conductor and host estimates, plus every exceptional input | Trace field-dependent class/unit assumptions |
| Q09g | proved | Kummer cyclic degree m dividing n with all divisor-order Hecke factors | No gap in stated factorization; RH of nonabelian factors remains open |
| Q09h | proved limited characterization; full algorithm open | Exact P145 hypotheses are absent from the attachments; its full eligible-input and complexity claim is not reconstructed | Obtain complete P145 statement before claiming a classification for that algorithm |
| Q09i | proved exact implications with stated promises | Uniform varying-p beta input yields auxiliary prime logarithmic exponent1/(1-beta); fixed269 RH distinguished | No claim of promise-free complexity or RH is made |
| Q09j | proved explicit analytic and arithmetic test cases; complete independent reconstruction | Q(i) real nonvanishing and allp=5mod8 strict cyclotomic vanishing; -23 real nonvanishing | No remaining proof/check step in the stated tests; a complex-zero RH bound is still absent for either arithmetic function |
| Q09k | open | Use any included prompt68 result; do not duplicate | Inspect exact fixed-sector trace positivity hypotheses; do not infer a Hecke trace limit from rational case |
| Q02b | proved for both candidates | 30301 and48976 real-zero gates closed | No remaining step for these two candidates; pursue the general off-central gate |

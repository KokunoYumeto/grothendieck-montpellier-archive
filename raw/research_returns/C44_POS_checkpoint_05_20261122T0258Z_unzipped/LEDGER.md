# C44_POS research ledger

Started: 2026-11-22 00:13:48 Europe/Berlin (2026-11-21 23:13:48 UTC).
Run: C44_POS; primary and delegated agents: GPT-6 Astra Pro; effort setting not exposed.

## Rules and source status

The attached prompt is the governing research brief. Prior results are used with their stated check status and statement identifiers. The 032/Milne consequences are conditional on those unrefereed preprints, not treated as independently established in this run. No claim is marked checked until its entire proof has been read. A computation checks only the identity or finite cases it actually tests.

Checkpoint schedule: first due at 00:58:48 Europe/Berlin, 45 minutes after start. Subsequent checkpoints are due at 45-minute intervals, with distinct names and no earlier ZIP nested inside. Three-hour gate review is due at 03:13:48 Europe/Berlin, then hourly. Wall-clock timestamps, not estimated effort, govern these events.

## Initial gates

| Question | State | Strongest input gate | Owner |
|---|---|---|---|
| QH9-axis | Open | Nonnegativity of (-1)^(m-1) integral_B w^2 on Alg^(m-1)(B) intersect ker kappa_* | Root and axis_independent |
| Axis lifting | Open | Actual algebraic lifting of the fixed primitive axis class, not just the ambient abelian variety | axis_independent |
| Axis correspondence | Open | A correspondence that detects the kernel and transfers the geometric pairing | Root and axis_independent |
| Axis Newton route | Open | A slope obstruction applicable to the even fixed-axis space, rather than only the odd variable incidence local system | axis_independent |
| Special covers | Open | H9-T18 variable algebraic intersection form on each special incidence fourfold | Root |
| Fermat AJ5 | Open | Kernel of the scalar-extended Abel-Jacobi map on the whole rational Chow group | fermat_aj |
| Fermat algebraic radical | Open | P18 isolated component on a curve times J; Murre (D) or equivalent componentwise injection | fermat_aj |
| Scan 050 example | Under examination | Need B(X) known and I(X times X) not already known; proposed supersingular Fermat family may not qualify | scan_w |
| Theorem W in characteristic p | Open | Replace archimedean norm bound and define the rational integral Weil lattice and balanced signature at bad primes | scan_w |
| Th. 4 geometric abelian type | Open | Geometric-form transfer in Milne 2022 Proposition 4.2, not only a motivic splitting | Root |
| Th. 4 all special complete intersections | Open | Control special incidence factors beyond generic-last-section H9-T13 | scan_w and Root |
| Th. 5 consolidated form | To assemble | H9-T1/T2/T7/T17/T18 with exact domain and signs | Root |

## Work log

- Initial source read: H9-T7, its full proof, H9-T8/H9-T8a, H9-T5, H9-T17 and the statement and main decomposition of H9-T18; archive cote 44 scans 004 and 008; cote 16 scans 049 and 050. No new check status inferred from the prior intake's statement-only readings.
- H9-T7 gives h_B w=0, not only h_B^2 w=0. The exact signed axis form is (-1)^(m-1) integral_B ww'.
- The ambient pushforward route annihilation was already recorded by JAC1964 H9-T13 and will be cited, not repackaged as a new finding.

## Scheduled reviews

No three-hour review is yet due. No claim of elapsed three-hour work has been made.

## Work state at 2026-11-22T00:54:59.182109+01:00

This is a work-log update, not the scheduled three-hour gate review.

- Main axis: A01 identifies the exact primitive decomposition; A02 proves graph transfers to every abelian target annihilate the kernel; A03 separates the correct even-axis Frobenius test from the odd-pencil witness. A05 closes geometric lifting for every embedded axis, leaving cycle lifting open. A04 gives explicit nonzero positive subspaces, including supersingular products; smoothness forces the bound that prevents its formal Gram matrix from becoming negative. A06 is being developed for arbitrary prescribed smooth centres at sufficiently high degree.
- Covers: C01 corrects the scope of old/new trace-kernel vanishing. C02 proves generic vanishing on every nonextremal Maroni stratum. C03/C04 boundary proofs are written and undergoing independent whole-proof review. No pointwise finite-field sign is inferred.
- Fermat arithmetic: F01–F07 isolate an exact integral projector, one arithmetic model, the unramified Tate module, tensor-to-completion kernel, bounded-denominator tests and an equivalent etale-motivic finiteness gate. Root read the full proofs; no AJ injection or Chow rank theorem is claimed.
- Theorem W: W01 gives an unconditional algebraic degree/intersection bound replacing Wirtinger. W02–W04 prove the characteristic-p detector/division result under explicit 032 and corrected signature hypotheses. W05 shows why the naive Lie-signature phrase at bad order primes is insufficient.
- Th4: W06 proves the finite abelian-cover case. W07/W08 prove fixed-factor and rank-preserving special-fibre statements. New special variable incidence directions remain open. W09 exposes the additional Milne2022 transfer input for the full abelian-type claim.
- Scan050: S01–S03 verify that the suggested supersingular Fermat example already has I, and compute the exact weighted maps and square form. A genuinely I-unknown replacement candidate is being investigated.
- Th5: C44-T05 consolidation drafted with Schur radical gate, injective case, full axis form, finite-cover Albanese-primitive domain and negative Picard complement.

The first checkpoint remains due at 00:58:48 Europe/Berlin. No earlier checkpoint ZIP has been produced.

## Checkpoint 01

Created C44_POS_checkpoint_01.zip at 2026-11-22T00:59:04.842375+01:00, after 45.27 minutes of elapsed work. Scheduled due time: 2026-11-21T23:58:48.738457+00:00 UTC. The ZIP contains current deliverables and work documentation, and no previous ZIP. Durable-save outcome is recorded in the next ledger update. This is not a scheduled gate review.

Checkpoint 01 durable save succeeded at approximately 01:00 Europe/Berlin. The saved ZIP is C44_POS_checkpoint_01.zip; next scheduled checkpoint is 01:43:48 Europe/Berlin. No previous checkpoint was modified.

## Outage recovery and work state at 2026-11-22T01:13:12.820975+00:00

This is a work-log update, not the scheduled three-hour gate review. Execution was unavailable from approximately00:35UTC until01:09:38UTC. Source work and complete proof readings continued; the due01:43:48Berlin checkpoint could not be created. The first checkpoint was CRC-verified on recovery; all newer on-disk files survived, and no missing baseline file required restoration. Unsaved proof texts and dated review events are being reconstructed from their complete conversation records.

- Main axis: A08 supplies a checked relative actual-form transfer criterion. A09/A09a control entire product grids; A10 supplies a genuinely nonliftable individual ambient class but no A_B example; A11 distinguishes smooth complete intersections from strict Lefschetz axes. A03b forces a potential Tate eigenvalue in the first open dimension. The universal axis gate remains open. A new rank-one closed-axis construction via blowup, Lefschetz monodromy and Frobenius exclusion is under investigation, not yet asserted.
- Covers: C05 extends the checked generic result to every characteristic-two conductor partition. Its one-pole conclusion is deliberately limited to the variable incidence kernel. Arbitrary closed points remain open.
- Arithmetic: F01-F07 remain the exact AJ5/finite-generation gates; no arithmetic injectivity is claimed. The distinct geometric Fermat calculation now has explicit new cycles (F13/F14), all-ell Tate/D/I on the degree-seven fourfold, and numerical/13-adic positivity on its square (F12). This does not close the arithmetic question or certify the originally requested historical status.
- W10/W11 prove relative primitive incidence transfer; W12/W13 sharpen the effective-cycle bound and division constants. Their entire-proof reviews, completed during the outage, are now being written with their original timestamps.

The first formal gate review remains due02:13:48UTC /03:13:48Berlin. No three-hour review has yet occurred.

## Checkpoint 02

Created C44_POS_checkpoint_02.zip at 2026-11-22T02:20:43.604795+01:00, after 126.91 minutes of elapsed work. Scheduled due time: 2026-11-22T00:43:48.738457+00:00 UTC. The ZIP contains current deliverables and work documentation, and no previous ZIP. Durable-save outcome is recorded in the next ledger update. This is not a scheduled gate review.

Checkpoint02 durable save succeeded at 2026-11-22T01:21:28.524316+00:00. C44_POS_checkpoint_02.zip has939342bytes and85entries. It was created late because execution failed when its scheduled time arrived; it contains the recovered full work state, without any earlier ZIP. Next original-schedule checkpoint is01:28:48UTC /02:28:48Berlin. No formal three-hour gate review is yet due.

## Closed-axis result checked at 2026-11-22T01:27:05.487049+00:00

C44-A13 passed independent and root whole-proof readings and is promoted to the checked paper. It computes the entire nonzero algebraic kernel on Zariski-dense closed genuine axes in a specified supersingular-sixfold family. The kernel is positive and lifts. General fixed-axis sign, general cycle lifting, and the relative-injection existence gate remain open. This is a work-log entry, not a scheduled three-hour review.

## Checkpoint 03

Created C44_POS_checkpoint_03.zip at 2026-11-22T02:29:01.456431+01:00, after 135.21 minutes of elapsed work. Scheduled due time: 2026-11-22T01:28:48.738457+00:00 UTC. The ZIP contains current deliverables and work documentation, and no previous ZIP. Durable-save outcome is recorded in the next ledger update. This is not a scheduled gate review.

Checkpoint03 durable save succeeded at 2026-11-22T01:29:18.801184+00:00. C44_POS_checkpoint_03.zip has415173bytes and87entries, with checked A13 and its independent audit. No prior ZIP was altered or nested. The next checkpoint is due02:13:48UTC, coinciding with the first formal gate review.

## Strict gate reductions checked at 2026-11-22T01:43:17.520634+00:00

This is a work-log update before the scheduled three-hour review. C44-A15/A15a passed root, author, and independent entire-proof readings. The universal fixed-axis question now reduces to axes with at least two potential Tate directions in the normalized variable Frobenius polynomial; by parity the first open dimension (abelian sixfolds) requires at least three. More strongly, any known positive rational cycle span can be enlarged by one remaining potential Tate direction without a cycle-lifting hypothesis. This is genuine main-gate movement, not just a new positive subspace.

C44-F15/F16 also passed root and author whole-proof readings. The P18 family gate is now confined to singular ample image divisors D⊂J whose resolution has irregularity>3, and to the exact excess-Picard quotient family maps. Smooth/rational-singularity ample divisors and all non-ample divisors contribute zero in rational Chow. The full arithmetic AJ5 finite-generation gate is unchanged.

C44-A14 is checked: it constructs a smooth abstractly nonliftable surface centre and an uncorrected nonliftable axis class; it expressly does not certify primitive nonliftability. A13b is checked for exact positive odd-rank closed-axis kernels. These two additions are kept separate from the strict gate reductions just recorded. First formal review remains02:13:48UTC.

## Scheduled gate review 1

Actual time: 2026-11-22T02:15:19.945623+00:00. Scheduled due time: 2026-11-22T02:13:48.738457+00:00.

Movement: **YES**. Consecutive reviews without movement: **0**.

C44-A15/A15a strictly reduces the original universal fixed-axis gate: after any known positive cycle span, at most one residual potential Tate direction is now settled without Tate, D, semisimplicity or cycle lifting. For sixfold axes the remaining unconditioned cyclotomic multiplicity is at least3. C44-W01–W05 and W12–W13 also close the original characteristic-p TheoremW task with explicit corrected signature/lattice hypotheses and the stated unrefereed032/Milne2026 conditions. These are mathematical changes, not packaging.

C06/C06a closes geometric lifting for every cover map and smooth incidence, but not cycle lifting. F15–F22 remove specified P18 families; the whole Fermat AJ5 finite-generation gate F07 is unchanged. The exact F07 criterion, arithmetic local countermodels, new positive subspaces, source audits and the Th5 compilation are not counted by themselves as movement. A18 constrained-centre moment work, if unfinished, remains pending and is not used in this review.

The register below snapshots every treated question. In particular every still-open original row retains its current strongest gate; auxiliary proved rows do not replace an unresolved original goal.

| Question | State at review | Strongest gate or completed result |
|---|---|---|
| QH9-axis | OPEN | C44-A15/A15a proves the entire axis form positive whenever normalized variable Frobenius has total root-of-unity multiplicity<=1, or a known positive span leaves at most one such direction. General gate now excludes those cases: without a known span it requires multiplicity>=2, and >=3 for every sixfold axis. A13/A13b separately compute positive entire kernels on dense closed supersingular families. No universal sign or wrong-sign class. A17 gives even negative index if the residual Tate block is fully algebraic; A17a/b show why away-p local comparison and full weak admissibility do not fix the remaining sign. Gate unchanged by these method obstructions. |
| QH9-axis-lift | OPEN | A05 lifts every embedded axis. A10 gives a nonliftable ambient class with zero variable projection. A14 gives a smooth abstractly nonliftable surface and an uncorrected nonliftable axis class with nonzero primitive component, but the obstruction cancels on that component. A13/A13b full selected kernels lift. Universal class lifting in A_B remains open. A14a proves that the same zero-stabilizer obstruction cannot survive on variable classes through the ordinary cup ring. |
| QH9-axis-transfer | OPEN | C44-A08 proves actual-form transfer under an explicit relative algebraic injection into abelian cohomology, conditional on unrefereed032/Milne2026. A02/A02b show graph/divisor-generated correspondences annihilate A_B. Existence of the required variable injection is open. |
| QH9-axis-Newton | PARTIALLY_PROVED | A03b forces a potential Tate root in sixfold axes. A15/A15a now proves the sign in the multiplicity-one case by a common-projector and discriminant argument; vanishing need not be proved. Remaining first-dimension Frobenius gate: total cyclotomic multiplicity>=3, or at least2 residual directions after any known positive span. |
| QH9-cover-primitivep | OPEN | C44-C01 separates the positive old kernel. C02/C04 cover all generic triple splitting strata. C05 covers every characteristic2 conductor partition generically; full-new vanishing requires at least two poles. Arbitrary closed special points remain open. C06/C06a lifts every finite cover map with smooth source and every smooth incidence geometrically. C07 proves the whole kernel sign if any known positive span leaves at most one potential Tate direction; no cycle lifting or arbitrary-point sign follows. |
| QFermat-AJ | OPEN | C44-F03/F04 exact completion and unramified obstruction; C44-F07 equivalent finite generation of one projected etale-motivic group on J over Z[1/10]. Not proved. |
| QFermat-algradical | OPEN | F15/F16 annihilate all resolved-image families with inherited Picard variety and all non-ample image surfaces in rational Chow. Remaining P18 gate: maps Hom(Jac(C), Pic0(Dtilde)/im Pic0(J))_Q→(pi1^C tensor p_N)CH2(C×J) for singular ample divisors D with q(Dtilde)>3. F06 still identifies the etale-motivic component as a rational vector space invisible to finite coefficients. No vanishing proved for this smaller family gate. F17 realizes this by one universal cycle on each excess Picard quotient. F18 kills the mixed CM elliptic subcomponent exactly, leaving CH2(N4) on E4 for j1728 elliptic excess factors. F19 further removes every image surface rationally dominated by a product of two curves, by exact Chow vanishing. F20 further kills surfaces whose grade-zero Albanese image class is distinguished; F21 supplies actual nonnormal ample examples with smooth normalization irregularity4. |
| QScan050 | OPEN | Supersingular Fermat is already I-known (S01/S03). F08-F10 give relative Fermat transfer conditional on unrefereed032/Milne2026. For nonsupersingular degree7/char2, F12 gives unconditional I_num and I_13 on the square; F14 gives all-ell Tate,D,I on X itself. The requested prior-unknown-I(XxX) status is not certified. |
| QW-charp | PROVED_CONDITIONALLY_WITH_CORRECTED_HYPOTHESES | C44-W01-W05 prove the corrected rational p-divisible signature and integral numerical-lattice scope, with positivity/Tate conditional on unrefereed032/Milne2026. W12 gives the sharp unconditional replacement for Wirtinger; W13 improves detector/division constants. |
| QT4-abeliantype | OPEN | W06 finite abelian-cover case and W10 relative-injection case are proved conditional on unrefereed032/Milne2026; W11 supplies Fermat products. Arbitrary geometric abelian type remains behind the explicitly unproved Milne2022 P4.2 transfer gate in W09. |
| QT4-specialCI | OPEN | W07/W08 cover fixed and inherited/no-jump factors; W10 gives a relative-correspondence sufficient criterion, all conditional on unrefereed032/Milne2026. Arbitrary new special variable incidence directions remain open. |
| QT5-final | PROVED_SYNTHESIS | C44-T05 whole-proof comparison PASS; the unified corrected formula retains its explicit sign gates, domains and conditional abelian input. |
| QAxis-geometry | PROVED | C44-A05; no cycle-lifting claim. |
| QAxis-explicit | PROVED | C44-A04/A04a/A04b; N<=d_T forced by smoothness, and at equality the only null vector vanishes in Chow. Actual displayed span has strictly positive form. |
| QCover-Maroni-strict | PROVED | C44-C02; positivity conditional032, monodromy vanishing and norm identity unconditional. |
| QCover-AS-simple | PROVED | C44-C03 entire-proof independent PASS. Includes p-rank g-1 divisor; geometric-generic strata only, with conditional032 positivity. |
| QCover-Maroni-boundary | PROVED | C44-C04 entire-proof independent PASS. Extreme splitting O(e)+O(2e), in every characteristic; generic monodromy/norm identities unconditional, positivity conditional032. |
| QScan-Fermat-status | REFUTED_AS_CANDIDATE_STATUS | C44-S01/S03: I(X) and I(X times X) hold unconditionally in the stated congruence family. |
| QW-bad-order | REFUTED | C44-W05 ordinary E over F5, O=Z+5Zi; corrected rational p-divisible hypothesis in W04. |
| QAxis-asymptotic | PROVED | C44-A06 unconditional exact Gram and explicit positivity threshold; polarization changes with N. |
| QAxis-product-curves | PROVED | C44-A07 unconditional strict lower bound on one nonzero axis line in dimension four. |
| QCover-AS-all | PROVED | C44-C05: variable incidence kernel vanishes generically for every partition. Full-new vanishing/norm only for at least two poles. Primitive height conclusion conditional on unrefereed032/Milne2026. |
| QAxis-product-grid | PROVED | C44-A09 gives semidefiniteness of the entire grid span; A09a gives strict positivity when one curve generates its threefold. |
| QAxis-nonliftable-ambient | PROVED_WITH_AMBIENT_SCOPE | C44-A10 explicit divisor-product tensor and determinant certificate; nonliftable even for abstract lifts of the axis. It lies outside A_B and has zero variable projection. |
| QAxis-CI-matching | PROVED | C44-A11/A11a bound N<=2 and give a positive3D complete-intersection subspace at N=2. A11b forces N<=1 under the strict Lefschetz-pencil condition. |
| QTransfer-relative | PROVED_CONDITIONALLY | C44-A08/A08a conditional on unrefereed032/Milne2026; explicit relative injection and self-dual projector required, no cycle-lift assumption. |
| QT4-relative | PROVED_CONDITIONALLY | C44-W10/W11, conditional on unrefereed032/Milne2026; includes stated Fermat product polarizations. |
| QW-sharp-bound | PROVED | C44-W12 in arbitrary characteristic and for singular effective cycles; W13 applies it to sharper division constants. |
| QFermat-geometric-transfer | PROVED_CONDITIONALLY | C44-F08/F09 give unconditional relative Chow retractions and Lefschetz operators; F10 sign is conditional on unrefereed032/Milne2026, with explicit ample-class scope. |
| QFermat7-newcycles | PROVED | C44-F11/F13/F14: explicit ruled surfaces,360 exceptional directions on X and30 on a selected square block; no generic specialization in that model. No claim about every deformation. |
| QFermat7-square-sign | PARTIALLY_PROVED | C44-F12 proves I_num and I_13 unconditionally for every ample class. All-ell cohomological sign follows conditionally from F10. Prior-unknown status not certified; arithmetic AJ5 is a different motive. |
| QAxis-closed-selection | PROVED_CRITERION | C44-A12/A12a criterion and A13 concrete application. Even orthogonal complement with full SO monodromy gives Zariski-dense closed axes with A_B=Qw and w²>0 in supersingular E^6, without Tate or032; all these axis classes lift. |
| QAxis-closed-rank-one | PROVED | C44-A13: for infinitely many supersingular primes, Zariski-dense closed axes have A_B=Qw and w²=6t²−1/(4t²)>0. Entire kernel lifts. General fixed-axis question remains open. A13b extends exact whole-kernel computation and liftability to any prescribed odd rank N, with Gram6t²I_N−J_N/(4t²). |
| QAxis-one-Tate-direction | PROVED | C44-A15/A15a unconditional; known positive span need not lift. Three full-proof readings (root, scan_w, axis_independent); common special-fibre Chow projector repairs cross-ell membership; a positive rational determinant fixes the real sign. |
| QAxis-nonliftable-surface | PROVED_WITH_UNCORRECTED_CLASS_SCOPE | C44-A14 determinantal smooth connected surface in E^4/Fbar3 has zero infinitesimal stabilizer of its intrinsic H1 cup form. It and its uncorrected class on a containing axis cannot lift. Primitive nonliftability remains unproved because the tensor obstruction cancels. |
| QFermat-excess-Picard | PROVED_REDUCTION | C44-F15/F16 exact rational-Chow vanishing reduces the residual P18 family gate to singular ample divisors with resolution irregularity>3 and the stated excess Picard quotient. Full AJ5 remains at F07 finite generation. |
| QAxis-closed-all-ranks | PROVED | C44-A16/A16a: for every N>=0 dense closed fibres have the full axis sign. Odd N has exact whole rankN; even N has rankN or N+1, the possible last algebraic line positive byA15. Known N-span lifts; no extra-line algebraicity/liftability asserted. |
| QFermat-CM-excess | PROVED_REDUCTION | C44-F17 universal residual cycle and Hom(h1(Qdual)(-1),N) formulation; C44-F18 exact Chow elimination of the mixed rank2 component, with CH2(N4) remaining for each j1728 elliptic factor. No full radical or AJ5 injection. |
| QCover-geometric-lifting | PROVED | C44-C06/C06a: every finite map toP1 over perfectk lifts as finite flat with smooth projective source overW(k); no deck-group or branch-stratum claim. Smooth finite-field incidence lifts with ambient product. C07 gives an unconditional one-residual-Tate-direction sign test with even-rank qualification. |
| QFermat-product-surfaces | PROVED | C44-F19 exact rational-Chow vanishing for every surface rationally dominated by a product of two curves, including sums. Does not assume inherited Picard or eliminate every remaining singular ample excess-irregularity surface. |
| QAxis-low-rank-local | PROVED_METHOD_OBSTRUCTION | C44-A17 positive determinant/even negative index under full algebraicity; A17a opposite real signatures with all away-p isometries; A17b full weak admissibility need not make the Tate projector filtered. No geometric counterexample and no sign gate closure. |
| QFermat-Albanese-image | PROVED_REDUCTION | C44-F20 exact Chow vanishing; includes smooth ample CI surface images from higher-dimensional abelian varieties. C44-F21 realizes nonnormal ample divisors inJ with smooth normalization irregularity4 by projection fromJ×E. General remaining surfaces and fullAJ5 are open. |

Decision: continue. The next formal review is due 2026-11-22T03:13:48.738457+00:00. No stopping condition has been met.

## Checkpoint 04

Created C44_POS_checkpoint_04.zip at 2026-11-22T03:15:20.588507+01:00, after 181.53 minutes of elapsed work. Scheduled due time: 2026-11-22T02:13:48.738457+00:00 UTC. The ZIP contains current deliverables and work documentation, and no previous ZIP. Durable-save outcome is recorded in the next ledger update. This is not a scheduled gate review.

## Main-gate refinement 2026-11-22T02:39:16.058917+00:00

A19/A19b and the independently whole-checked A20/A21 construction now strictly extend the earlier one-direction criterion to actual extending orthogonal blocks. The concrete affineS3 family has a known positive rank6 span and still three residual potential Tate directions, with positivity on the whole algebraic kernel proved. The earlier A15 test on that displayed complement does not apply. The universal remaining row is still OPEN; it now excludes these certified block-decomposable cases. This is a candidate movement basis for the next scheduled review, whose comparison remains against review1's stored rows. No unscheduled formal review or checkpoint was created.

Both root and axis_independent independently found the arbitrary initial polarization lift gap in the first A20 draft. It was repaired by choosing an explicit product polarization before taking its group norm; the final proof and exact lift were reread. The old broad assertion was not promoted. All three authors/reviewers read the complete relevant proofs.

## 2026-11-22T02:47:20.679999+00:00 — coherent primitive obstruction calculation

C44-A22 passed author, independent-agent, and root whole-proof readings. It proves the full coherent normal obstruction is retained after passing to the primitive Hodge quotient for high-degree axes containing a smooth surface. Rational crystalline filtration versus integral mixed-characteristic deformation remains a separate unproved compatibility step; no primitive nonliftability claim and no separate movement-clock claim are made.

## 2026-11-22T02:54:00.696858+00:00 — dimensional extension checked

A23 passed author, root and independent whole-proof readings. All r>=2 are covered by the same affine-S3 mechanism, including signed Gram and exact parity. This extension is not separately counted as movement. A totally real coefficient-field variant and an affine-dihedral application are being investigated and are not yet claimed.

## 2026-11-22T02:58:46.693736+00:00 — totally real coefficient criterion checked

A24/A24a passed root and independent whole-proof readings. The determinant argument now works over an actual extending totally real self-adjoint coefficient field, with the norm of every cycle recovered from rational intersection numbers. A D5 geometric family is still a candidate, recorded in the route notes. No original question is claimed closed.

## Checkpoint 05

Created C44_POS_checkpoint_05.zip at 2026-11-22T03:58:56.562445+01:00, after 225.13 minutes of elapsed work. Scheduled due time: 2026-11-22T02:58:48.738457+00:00 UTC. The ZIP contains current deliverables and work documentation, and no previous ZIP. Durable-save outcome is recorded in the next ledger update. This is not a scheduled gate review.

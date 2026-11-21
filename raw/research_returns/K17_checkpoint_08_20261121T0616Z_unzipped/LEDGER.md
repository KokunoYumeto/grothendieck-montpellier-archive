# K17 research ledger

Run: K17-20261121. All dates use Europe/Berlin (CET, UTC+01:00).
Start: 2026-11-21 01:15 CET (00:15 UTC).
Model: GPT-6 Astra Pro. Runtime reasoning-effort label is not exposed.

## Scope and source contract

The RH and Dirichlet-GRH statements supplied in `ALPOGE_Main.lean` are accepted as stipulated. This run does not reopen their proofs. Step 17 and footnote 6 must nevertheless supply their own quantifiers and arithmetic conclusions. The archive was unpacked once. The ZIP contains two Lean files and a textual map/scan, not the 175,187-file formalization. The seven archive items are transcriptions, not images of the handwritten scans.

## Active gates (initial record, 2026-11-21 01:20 CET)

| Question | Status | Current gate / next test |
|---|---|---|
| Q1: exact step 17 | Open: source statement unidentified | Identify fields E, twists e, primes ell, selected classes, twisting maps, and asserted annihilation or bound. The note does not state these. Inspect candidate Lean locations and external source access. |
| Q2: K-groups and Vandiver | Exact literature comparison being checked | For odd ell, obtain the precise eigenspace and the negative-twist localization kernel dual to K_(4k)(Z){ell}; check the two-primary calculation separately. |
| Q3: LM6 A.44-A.45 | Open at requested irregular/2 branches | Separate equality of kernel fields from freeness/generation of the associated graded image; check Sharifi's exact hypotheses and subsequent results. |
| Q4: integral B3 | Stronger generation claim under challenge | Verify the explicit irregular-prime obstruction in McCallum--Sharifi, and distinguish existing integral elements, primitive normalization, and generation. |
| Q5: cote 149 | Transcription and Kummer review active | Establish the actual tangent-vector versus completed-unit problem; record only mathematically supported emendations, with no image verification asserted. |

## Approach log

- Read the supplied prompt in full, inventoried the ZIP, unpacked it once, extracted all four pages of the note, and visually checked page 4.
- Read the complete supplied `Main.lean`, `Statements.lean`, scan TSV, and relevant map sections. The map labels the step-17 match low confidence and gives only candidate paths.
- Delegated independent primary-source reviews of Vandiver/K-theory, pro-ell kernels and integral generators, and the archive/Kummer material.
- Searched for the note and candidate source files. The original note URL and selected GitHub file/tree requests failed in the web retrieval tool. Successful root-repository and Main-file retrievals do not identify the step-17 declaration.
- Began a finite-coefficient Poitou--Tate reduction identifying the precise localization kernel relevant to the even K-groups. Independent mathematical review confirmed the intended twist and the cancellation of global/local H^0 for Q and odd ell; the full source locator is being checked.

## Reviews and checkpoints

No three-hour review is due yet. The first review is due at approximately 04:15 CET; subsequent reviews are hourly. A review counts movement only when an open row changes status or a gate is strictly reduced.

Checkpoints are due at 45-minute intervals from the start (first approximately 02:00 CET), under consecutive new names. None has yet been due. Earlier checkpoint ZIPs will never be nested in later ones. This ledger will record actual saves and their times; no review or save is backdated.

## Gate review during research — 2026-11-21 01:37 CET

This is an ordinary progress entry, not the scheduled three-hour no-movement review.

- **Q1 moved.** Recovered the public mirror at pinned commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`. Its Main.lean is byte-identical to the supplied Main. Retrieved candidate files and checked Git blob hashes. Read `SmallClassNumbers/ClassNumberThree.lean`, `LenEqZeroIff.lean`, and `CorGKOf.lean` in full. Located the unconditional theorem `UpperTheory.V.SmallClassNumbers.bound`, the general `U3.CorGK`, coefficient-ring normalization, and exact local conditions. No Lean build was run. The four-page note alone is underquantified; its source now supplies a concrete arithmetic theorem.
- **Q2 moved.** With the bottom coefficient ring O=Z_l, `eO=1`. The selected Selmer group over Q is dual to K_(2e)(Z){l}. For positive even e, the source bounds the sum of log(l) times its length polynomially in e. All excluded primes `(l-1)|2e` have trivial relevant class-group component: either the trivial character or a quadratic real-field component whose class number is less than l. The two-primary part is known to vanish. Therefore there are absolute existential C,A with log|K_(4k)(Z)| <= C(2k+1)^A. The remaining numerical gate is extraction of useful constants or direct specialized congruence integers; no new specified degree has yet been proved to vanish.
- **Q3 moved at 2, under final write-up check.** A complete moment/Magnus argument has survived the author, root, and two independent whole-proof readings. Primary source inputs checked: Gras--Jaulent Theorem2 (the pro-2 ramification group), Hain--Matsumoto Proposition8.3/Theorem8.4 (actual rational outer image), Brown2019 sections2.1--2.3 (rational Deligne--Ihara for every prime), and the finite-rank Magnus embedding. Clean proof and audit files are being prepared. This is a deduction checked in this run, not a formal certificate, external peer review, or claim of priority. Irregular primes remain under investigation; next approach uses the free pro-p cyclotomic kernel and its Iwasawa module.
- **Q4 moved.** The strong implication from all K_(4k){l}=0 to integral odd-weight generation is refuted at l=37 using McCallum--Sharifi Theorem9.7 and the exact Vandiver37 certificate. Nonzero integral elements, full-domain Soulé primitivity, filtration-level primitivity, and free generation have been separated. The p=37 counterexample does not refute equality of kernel fields.
- **Q5 moved.** Read scans79--85 in the supplied transcription. Established the inverse-limit Kummer statements and a concrete completed-unit class not represented by a unit. The remaining archive question is intrinsic recognition of geometric tangential sections, with a separate general normalizer/formal-tube comparison gate. Transcription corrections remain mathematical flags, not image-verified readings.

### Approaches added

1. Switched from failed web code-page retrieval to pinned public raw-source retrieval, verified against Git blob identifiers; this recovered the theorem rather than leaving the initial source gate open.
2. Traced `Coef`, `QO`, `eO`, `ShaU`, `GD`, `Vlen`, `Vn`, `orb`, and the plus/minus involution. The theorem is a quantitative local-condition Selmer bound, not universal H1 vanishing.
3. Reconstructed the source norm argument: one nonzero congruence integer bounds every eligible prime except its auxiliary prime; two distinct auxiliary primes remove that exception, and prime factorization bounds the weighted sum.
4. Tested the direct Vandiver-to-free-generation route and found the explicit p=37 obstruction. Kept the distinct kernel equality question open.
5. At p=2, abandoned prime-to-2 averaging and instead used a compact orbit of free generators, an integral Magnus expansion with bounded-measure coefficients, and analytic separation by odd-weight cyclotomic moments.
6. Began tracing the constants through congruence-number bounds and began a separate irregular-prime Iwasawa-module analysis.

## Gate movement — 2026-11-21 01:57 CET

Ordinary research entry, not a scheduled review. The exponent gate moved from an unspecified exponent to the explicit exponent7, with an independent full source-chain audit. The constant remains unevaluated. The exact divisor gate |K4k| divides gcd(n7(2k),n11(2k))² is now written, with normalization, indexing multiplicities and auxiliary-prime exceptions checked. Agent vandiver is testing a concrete e6/e8 trace calculation.

The pro2 proof is now typeset and has been read in full by its author, root, and two independent reviewers. No defect was found. The final statement allows complexification at the real place. The general irregular case now reduces to detection of nonlinear lifts of the nonzero even Lambda-torsion abelianized summand; a pole-separation route for lambda-minus1 is being tested and is not a theorem.

All required deliverables have current drafts. The LaTeX runtime lacked its format and font search setup; a local format was rebuilt from installed sources. Rendering remains a verification task, not mathematical progress. The broader host-field PointHV closing dependencies are being traced separately.

## Timed checkpoint 01 — 2026-11-21T02:00:36.683698+01:00

Scheduled interval reached. Creating K17_checkpoint_01.zip with all current deliverables, authored research notes, exact computation, proof audits and pinned Lean source evidence. No prior checkpoint is included. This is not a final answer or a scheduled three-hour progress review.

### Checkpoint01 save confirmed

Saved at the first scheduled45-minute boundary, 2026-11-21 approximately02:01 CET. File K17_checkpoint_01.zip, 2,354,600 bytes, SHA2567b0669546561d11810fa6b7f385c31244bfef32ce986d7d7c23b4b4a02756013. ZIP integrity and six required top-level deliverables checked;540 research/source evidence files;35-page PDF. Persistent save succeeded and the ZIP link was delivered. The earlier ZIP is immutable and will not be nested in another. Next checkpoint due02:45:36 CET.

### Active attempts after checkpoint

The full PointHV source assembly has now been identified; its layer-bound hypotheses remain part of the statement. The archive agent is incorporating the exact closed proof term. A new irregular-prime37 pole-separation candidate is under independent hostile audit by vandiver and root; it is not yet a theorem. Root is independently examining low-weight2 lattice saturation using the rational normal form and exact nilpotent coordinates. The first naive half-bracket test at weight8 does not immediately produce a defect: vanishing of the weight7 coordinate imposes an additional moment divisibility.

## Gate movement — 2026-11-21 approximately02:14 CET

Not a scheduled review. Q1 full Host statement now closes by an inspected forward source composition to PointHV. Its LayerLe bounds remain explicit premises. Q3 irregular prime37 changes from open to proved by K17-37-KERNEL, after author/root and two independent whole-proof audits. The proof detects the even arithmetic direction using quadratic moment poles, without asserting integral odd generation. The general irregular gate is now a multi-direction version plus arithmetic cup-numerator nonvanishing. A published Sharifi2007 surjectivity theorem for primes<1000 has been located and is being checked for the exact necessary form.

At2, an exact class2 prototype finds no integral defect through even weights8 and10; arithmetic interpretation and extension to higher weights are under active independent study. This prototype is not promoted to an all-weight result.

## 2026-11-21 02:38 CET — finite integral comparison and exact computation

K17-OUT-SAT is proved by the free-Lie outer-Johnson argument and HM finite-kernel induction; root read the full proof after the independent author audit and verified the KKL primary theorem. K17-2-FINITE18 proves equality of actual and odd-generated lattices through weight18. Full compact-group collection, rational normalization and code were read; archive reran through14 and root independently checked both integral matrix inclusions through18. The all-weight row remains open with the explicit Hall/Newton correction and Gamma-stability gate. The finite range is a new closed subquestion, not a claim that finite calculations settle the all-weight gate.

T-INTEGRAL691 adds a second checked integral counterexample, with weight12 quotient Z/691, from the exact MCS/Sharifi source chain. VK-POLY-CERT now gives a proved overcount/linear-factor-removal version of the two-prime trace certificate. SGA5 VII Proposition3.4(i) was visually confirmed in the original p291 scan, with its normalization proof p292 and standing invertibility hypothesis p282.

## 2026-11-21 02:40 CET — general pole theorem and odd primes below1000

K17-POLE-GENERAL passed author, root and two independent whole-proof readings. The companion-module construction handles multiple even directions and repeated roots. Root and archive checked the full p-unit parity bridge, and the exact source scope of Sharifi2007 Theorem1.2/Cor5.9 and the published Vandiver range is retained. K17-KERNEL-LT1000 closes the irregular subquestion for all odd primes below1000. The remaining main irregular-prime gate is the arithmetic Vandiver/cup condition (or a weaker divisor noncancellation criterion), with a noncyclic-module extension needed outside Vandiver. This is substantive main-question movement; no scheduled three-hour review has yet occurred.

## Timed checkpoint 02 — 2026-11-21T02:46:09.628817+01:00

Scheduled interval reached. Creating K17_checkpoint_02.zip with all current deliverables, authored research notes, exact computation, proof audits and pinned Lean source evidence. No prior checkpoint is included. This is not a final answer or a scheduled three-hour progress review.

## Substantive movement — 2026-11-21 01:56 UTC

K17-VANDIVER-KERNEL closes the independent cup-surjectivity condition under Vandiver. The FK/WWE integral theorem chain, including character reflection and finite-level passage, was read and independently checked; the elementary tower persistence proof was read in full. The numerical kernel range increases from p<1000 to every prime p<2^31 using the already cited HHO computation plus the separate2 proof. Fable suggestion5 is now split decisively: its kernel implication follows from all relevant K vanishings; its integral-generation implication is refuted at37 and691. The all-prime kernel gate is Vandiver or a non-Vandiver extension.

K17-2-NEWTON-BASIS also closes the former independent Hall/Gamma-stability step once all odd Newton minima are attained. That infinite lifting problem remains open; finite generation through18 is unchanged. These are substantive reductions, not a scheduled three-hour review. Checkpoint02 remains immutable.

## Substantive movement — 2026-11-21 02:24 UTC

K17-2-ALL closes the all-weight integral generation gate at2. The complete parity/central-extension induction and Newton-basis finish have root and two independent whole-proof PASS reviews. It constructs actual adapted generators, rather than extrapolating the weight18 computation or class-two identity. K17-INTEGRAL-CLASSIFICATION then gives the complementary full answer at odd Vandiver primes: regular primes have free odd generation; every irregular Vandiver prime has nonzero finite primary Lie-abelianization in infinitely many even weights. Its compact filtered-abelianization proof and exact Kummer inputs were independently checked.

The K12 gate is reduced to rank9 degree4 and rank10 degree3 Steinberg homology over Z[1/13!]. A current literature check found that MPP2025 already proves the rank11 term integrally and states the uniform localized H2 result. The independently obtained localization argument is therefore recorded as a recheck of known mathematics, not a new theorem. Neither remaining rank vanishing nor a complete trace polynomial has been obtained. A further finite double-building implication is being audited; its three input vanishings remain unproved.

F149-RELATIVE proves the cusp-normalizer and tame-formal-tube comparison in the smooth characteristic-zero setup, retaining the manuscript's explicit homotopy-exactness hypothesis. Its finite obstruction is the Kummer Chern class up to the stated sign convention; finite generation of Pic makes splitting equivalent to a trivial conormal line. The scan85 intrinsic geometric-subset recognition remains open.

All-prime kernel work now tests a Greenberg extension: a cup/Ext residue bridge has a complete candidate and independent audit, but the whole-H bounded-denominator Magnus adaptation is not yet promoted. These entries document substantive progress; they are not the scheduled three-hour review, which remains due at03:15:36UTC.

### Checkpoint02 save confirmation

The second immutable ZIP was saved and delivered after its scheduled boundary. SHA256 356302860802e585d3362955a2d9f32ad9571fe8e13fa31b61aabe58f707919c. Native Library id libfile_5224dab143c08191969eb94452ca4a67. No prior checkpoint was changed.

## Timed checkpoint 03 — 2026-11-21T03:30:48.197500+01:00

Scheduled interval reached. Creating K17_checkpoint_03.zip with all current deliverables, authored research notes, exact computation, proof audits and pinned Lean source evidence. No prior checkpoint is included. This is not a final answer or a scheduled three-hour progress review.

### 2026-11-21 02:32 UTC — third scheduled checkpoint

K17_checkpoint_03.zip created after its 02:30:36 UTC due time and saved successfully. Size 18,535,436 bytes; SHA256 `06f5b495496a0ea757629d5ef2b38aeb57d3a6a50b6d4dc74ade2f2f397b08e8`; 65-page PDF and 276 actual check events. Earlier checkpoints were not altered or nested. The finite-level cup/companion-extension bridge has subsequently passed the root whole-proof read; the combined Greenberg kernel argument is still under construction and is not counted as closed.

### 2026-11-21 02:39 UTC — weaker arithmetic hypothesis for the kernel

K17-GREENBERG-KERNEL has passed author, root, and independent tripod whole-proof readings, including final TeX. The remaining all-prime kernel gate has weakened from Vandiver (Xplus=0) to one-variable Greenberg (Xplus finite). K17-CUP-EXT proves naturality for the actual class-two companion extension; K17-RATIONAL-MAGNUS retains the whole H with bounded coefficients at each degree; K17-ETALE-PROP supplies the exact finite-coefficient group comparison. This is a checked conditional theorem, not a proof of Greenberg. K17-K12-DOUBLE is also a checked alternative sufficient criterion, with all three hypotheses explicitly still open. No new K-group degree has yet vanished.

### 2026-11-21 03:04 UTC — source endpoint correction and concrete remaining work

The new full proof of scan85 recognition is promoted at its explicit full marked-generic-diagram scope (F149-GENERIC and F149-MARKED-RECOGNITION). F149-BARE-EXTENSION refutes recognition from the isolated extension alone. The Greenberg integral classification is also checked and incorporated.

The K12 source audit found that the displayed DEKM cone enumeration stops one rank before its announced endpoint. Earlier two-rank PASS events are preserved as checks using the announced theorem; they are now explicitly qualified. K17-K12-THREE-RANKS retains H5GL8 as an additional hypothesis, and the repaired double-building argument derives H3GL9 from its existing hypothesis. No contradiction to the announced vanishing is claimed. The remaining rank11 term is independently zero by MPP.

Low-excess target cells have exactly13 minimum pairs, with low-index orientation pruning proved. An explicit index-three lattice has only orientation-preserving stabilizers, verified by a standalone exact rational certificate and whole-proof reviews. Thus the orientation-only route is refuted; cycle and boundary work continues.

The full Host/window uniformity has been checked and does not remove the Greenberg or numerical K12 gate by its size inequalities alone. A fully proved abstract Iwasawa compatibility model and exact artificial trace-polynomial pair document this failed inference without asserting arithmetic realizability. This is an interim progress entry, not the scheduled first review at03:15:36UTC.

## First scheduled substantive review — 2026-11-21 03:19:30 UTC

Due 03:15:36 UTC, recorded after the active proof/source checks and checkpoint assembly. This is the first approximately three-hour review required by the prompt. The mathematical movement test is applied to the main questions, not to formatting, certificates alone, or the checkpoint.

| Main question | Current status and strongest checked gate | Movement in the first review period |
|---|---|---|
| Q1: exact Step17 | Closed at the stated arithmetic source contract: strict Selmer classes, fields, twists, character conditions, normalization, exact Host hypotheses and forward source composition. Host/window size inequalities alone do not imply Iwasawa finiteness; the compatibility model refutes that numerical inference only. | Yes: exact statement and closed source chain recovered. |
| Q2: K-groups and Vandiver | Equivalence and finite test range, strict duality, exceptional characters, exponent-seven global bound and exact trace-polynomial divisor criterion proved. Q2-NEWDEG remains open: actual complete trace-polynomial gcd, or H5(GL8;St8), H4(GL9;St9), H3(GL10;St10) over Z[1/13!] all zero. Rank11 is independently removed; three specified double-building vanishings imply the last two ranks. | Yes during the review period from the quantitative and exact-certificate reductions. The source-index correction restores the rank8 hypothesis and is explicitly NOT counted as a positive reduction. No new degree is certified. |
| Q3: tripod kernel | At2 and every odd Vandiver prime, hence every prime below2^31, closed. Q3-IRREG remains open in general: one-variable Greenberg Xplus finite suffices; positive-rank Xplus is not yet handled. | Yes: the2 and Vandiver cases closed, then the sufficient arithmetic hypothesis weakened to Greenberg finiteness. |
| Q4: integral B3 | At2 and odd regular primes the actual graded Lie algebra has primitive odd free generation. At every irregular Greenberg prime infinitely many even Lie-abelianization pieces are nonzero finite primary groups. Full-domain Soulé indices and restricted weight-subgroup normalization are separated. | Yes: all weights at2 closed; the proposed Vandiver-to-integral-generation implication refuted, with a general conditional classification. |
| Q5: cote149 | Kummer limits, relative normalizer, generic descent and recognition from the full marked generic diagram proved. Isolated-extension recognition refuted. Q5-MARKING remains open: whether the omitted generic arithmetic marking can be recovered from the smaller diagram. | Yes: full marked recognition and generic descent closed; scope of the remaining problem isolated. |

Every currently open question-table row is listed here: Q2-NEWDEG, Q3-IRREG, Q5-MARKING. Explicit orientation-only elimination is refuted; both exhibited cycles are now coefficient-one boundaries, but this does not compute the remaining homology groups and is not counted alone as a completed main gate. Current research attacks complete low-index cell coverage and ambient glue, odd Iwasawa torsion via cubic companion residues, and the necessity of generic marking.

Review outcome: MOVEMENT YES. Consecutive scheduled reviews without movement: 0. The next substantive review is due at04:15:36 UTC; the next checkpoint after checkpoint04 is due at04:00:36 UTC. Work continues.

## Timed checkpoint 04 — 2026-11-21T03:19:30.380480+00:00

Scheduled interval reached. Creating K17_checkpoint_04.zip with all current deliverables, authored research notes, exact computation, proof audits and pinned Lean source evidence. No prior checkpoint is included. This is not a final answer or a scheduled three-hour progress review.

### Checkpoint04 save confirmation and rendering qualification

Fourth scheduled immutable ZIP saved at the first review boundary: 28,521,153 bytes; SHA256 7d305ca155221e5c3915e1c8c916c98c9752ab1d2501710a31c9b358d28240f8; Library id libfile_f0077ef6c2f481919de75de4825a33d1. It contains345 merged check events and817 research-evidence files. No earlier checkpoint was changed or nested. The included optional95-page PDF is the last successful rendered version. A final default-format rebuild failed because the runtime requires the explicit cached TeX format; the authoritative K17.tex includes the two subsequent Host quantifier clarifications (finite odd-prime sums in HU.1 and universal WinPair order in HU.3). This minor PDF/source difference is retained honestly rather than overwriting the immutable checkpoint. Rebuild via work/build_pdf.py after saving; no additional off-schedule ZIP.

### Main-question movement after first review — 2026-11-21 03:28:37 UTC

Q5-MARKING changes from current gate to refuted in its precise functorial sense. F149-UNMARKED-CURVE is a full-curve-diagram counterexample over S=Gm/Q, with base-group automorphisms permitted; its noninteger Kummer slope cannot be geometric. The no-functorial-recovery corollary follows from the marked recognition theorem. Root and independent archive whole-proof/source audits passed. This closes an open row and counts as movement for the next scheduled review.

K17-K12-TRIMODULAR-GENERATED further shrinks the rank10 cell gate. Every degree12 minimum-generated cell with maximal basis index<=3 is orientation-zero or the previously filled sigma. The remaining rank10 cycle representatives use maximal index>=4 or proper index3 ambient glue at maximal index3. Root read the entire proof and code, read the published classification procedure and tables, and reran all three literal-record checks. Published completeness is cited, not recomputed; independent whole-proof audit requested. This is a smaller main chain gate, not a claim of full H3GL10 or K12 vanishing.

### Checked rank-eight reduction and conditional cubic extension — 2026-11-21 03:40:31 UTC

K17-K12-R8-NONSIMPLICIAL removes every nonsimplicial rank8 endpoint cell, including ambient glue. Root read final full TeX after the earlier complete proof/code/source check and exact192-class replay; archive independently passed the whole proof and sources. K17-K12-R8-INDEX5 then bounds every residual minimum-frame index by5 and gives the exact necessary quotient types from Martinet section11/Table11.1. The residual rank8 gate is now only simplicial13-pair cells with these small frame quotients. This strictly shrinks the main K12 chain gate, but is not an H5 or K12 vanishing.

K17-CUBIC-ODD is fully checked as a conditional algebraic theorem, with root and independent tripod whole-proof readings. It handles cyclic odd torsion character by character, including repeated roots, under explicit pair and triple nonvanishing conditions. No arithmetic Triple-NV is supplied. It is not counted as a weaker arithmetic all-prime gate by itself. The norm-compatible unit bridge is under active investigation.

Fresh October2026 Steinberg/graph papers were retrieved from primary arXiv PDFs. Their inspected main statements concern rational Hopf structures and rational K-theory; they do not settle the localized integral endpoint. Full source proofs were not audited or used. The next scheduled review remains04:15:36UTC, next checkpoint04:00:36UTC.

### Further main-gate movement — 2026-11-21 03:57:27 UTC

All26 proper-index3 rank10 cycles are classified and filled with coefficient1 (K17-K12-TERNARY-CYCLES; K17-K12-INDEX-THREE-BOUNDARIES). Root read every proof and verifier line and reran both complete exact certificates; vandiver independently passed classification and archive independently passed all fillings. Rank10 representatives now need only maximal basis index>=4. Rank8 proper minimum-generated index5 is impossible by the full F5/binary-matroid argument, independently read by root and archive. These shrink the main K12 chain gates.

The universal norm-family bridge is now fully checked: K17-NORM-TORSION, K17-UNIVERSAL-PAIR, K17-WWE-PAIR. Under the exact WWE rational support/cyclicity conditions it supplies Pair-NV even with odd torsion. It does not verify arithmetic Triple-NV or add an unconditional prime.

A potentially decisive separate arithmetic route is active. The pinned KillsMu definition confirms Level2=Level1, and proposed maximal-level U3 plus level3 GL2 calculations have exact small-prime-factor evaluations. The calculations remain EXPLORATORY pending a complete coverage and normalization proof. They are not used to assert K12 vanishing at this checkpoint.

### Checkpoint05 active frontier

The level-one U3 / level-three GL2 weight13 Hecke calculation is exploratory and not yet promoted to a theorem. Exact reruns agree. Independent global/local coverage and classical modular-form model audits are active. The final missing source interface must justify replacing the source trace class by a finite class containing every actual admissible representation; no divisibility from an oversized source trace product to a smaller product is assumed. All current checked cellular reductions and the universal cyclotomic pair bridge are integrated into the125-page paper.

## Timed checkpoint 05 — 2026-11-21T04:03:08.754697+00:00

Scheduled interval reached. Creating K17_checkpoint_05.zip with all current deliverables, authored research notes, exact computation, proof audits and pinned Lean source evidence. No prior checkpoint is included. This is not a final answer or a scheduled three-hour progress review.

## Second scheduled substantive review — 2026-11-21 04:15:41 UTC

Due04:15:36UTC; recorded at the scheduled boundary. The review counts only closed open rows and strict reductions of main gates. It does not count packaging, source collection, or a promising uncompleted calculation.

| Main question | Current status and strongest checked gate | Movement since the first review |
|---|---|---|
| Q1: exact Step17 | The exact strict Selmer theorem and Host source contract remain closed. A newly recovered intermediate OneCharU_s theorem gives a direct unit-trace vanishing criterion; its complete source proof has now been read. | No independent open row is counted closed here; the new criterion supports the active Q2 route. |
| Q2: K-groups and Vandiver | Q2-NEWDEG remains open at this instant. In the cellular route, every rank10 target cell of maximal minimum-basis index<=3 is eliminated, including all26 proper-index3 glue cycles by coefficient-one boundaries. Rank8 is restricted to simplicial13-pair cells with maximal basis index<=5 and no proper index5 ambient glue. The alternative arithmetic route has fully checked compact-U3 and classical weight13 Hecke models and a checked source-unit criterion; the rank-two conductor interface at the coefficient prime remains under primary-source audit. | YES: the rank10 and rank8 main chain gates are strictly smaller. The pending K12 conclusion is explicitly not counted as proved. |
| Q3: tripod kernel | All primes below2^31 and every odd Greenberg prime remain covered. Q3-IRREG remains open beyond the sufficient Greenberg finiteness condition. The new universal norm-family argument supplies pair nonvanishing under exact WWE rational support/cyclicity hypotheses; the cyclic-odd-torsion extension still requires arithmetic triple nonvanishing. | No unconditional new prime or smaller arithmetic all-prime gate is counted. The new conditional algebraic criteria retain their unverified inputs. |
| Q4: integral B3 | Full odd integral generation at2 and regular odd primes, and its failure at irregular Greenberg primes, remain established at their stated scopes. | No new main row is counted. |
| Q5: cote149 | Q5-MARKING is now refuted by the full constant-tripod diagram with a noninteger profinite scaling of base inertia. Marked generic recognition remains proved. | YES: the remaining open recognition row is closed in its exact functorial scope. |

The complete list of currently open question-table rows is Q2-NEWDEG and Q3-IRREG. The K12 arithmetic route is being pursued first: all trace comparisons at7 have only prime factors<=271, but no K12 vanishing is promoted until every admissible rank-two representation is shown to have conductor3 with the correct normalization. The source's old oversized trace product is not replaced or divided; the direct unit criterion uses pointwise coverage.

Review outcome: MOVEMENT YES. Consecutive scheduled reviews without movement:0. Next substantive review due05:15:36UTC. Next checkpoint due04:45:36UTC. Work continues under the prompt's stop rule.

## Main-question closure — 2026-11-21 04:28:10 UTC

K17-K12-VANISH is promoted after complete author/root and independent archive whole-proof readings. The actual OneCharU_s theorem gives a direct unit condition; full U3 source-level/global coverage, complete compact Hecke space, exact GL2 conductor3 bridge including the coefficient prime, and complete weight13 classical space all pass their whole-proof and exact-certificate checks. The auxiliary7 comparison product has only primes<=271, so strict duality and the cited small-prime range prove K12(Z)=0. The full-domain kappa7 is therefore onto at every odd prime, and the even cyclotomic component A_l^[-6] vanishes. Q2-NEWDEG changes from current gate to proved. This is substantive movement for the next scheduled review, not a new scheduled review or off-cycle checkpoint.

The remaining cellular computations are retained as independent partial results, not premises of the K12 theorem. A separate Q2-HIGHER row records the active K16/K20/K24 calculations. Exact exploratory data suggest K16 and K24 certificates with only small prime factors; K20 retains9496386083, outside the published2^31 range. Generic coverage and whole-code audits are active, and a targeted reflection/Bernoulli test is being considered for that prime. Q3-IRREG remains open at its Greenberg/odd-torsion arithmetic gate. Next checkpoint04:45:36UTC; next scheduled review05:15:36UTC.

## Further main-question closure — 2026-11-21 04:39 UTC

K17-K16-K20-K24 and K17-SIX-DEGREES-PERIOD are promoted after root and archive independent complete proof readings. General source coverage, full compact harmonic spaces and full classical spaces were proved uniformly, all complete finite model certificates were rerun, and the gcd of the combined U3/GL2 products was factored exactly. The sole large factor in degree20,9496386083, is removed by the full reflection proof and two independently implemented complete Bernoulli sums giving3753150554. Thus K4k(Z)=0 for1<=k<=6. Full-domain odd Soulé characters through weight13 are surjective at every odd prime; the corresponding negative even strict Selmer groups through twist−12 vanish. The all-prime Vandiver and irregular kernel gates do not follow from this finite-degree result.

Q2-HIGHER changes to proved. Q2-HIGHER2 records the new active degrees28,32,36. Current complete exploratory products leave only small factors at28, prime25078104767246023 at32, and prime8361790201 at36. These are not yet promoted: exact replays, prime certificates, the second residue calculation and final whole proofs are active. Q3-IRREG retains its explicit Greenberg/odd-torsion arithmetic gate. This is movement after review02, not an unscheduled review. Next checkpoint remains04:45:36UTC and next scheduled review05:15:36UTC.

## Two more degree closures — 2026-11-21 04:42 UTC

K17-K28-K36 is promoted after complete author/root/archive proof readings, complete exact model replays and the independent second Bernoulli computation at8361790201. The proved set is now k=1,2,3,4,5,6,7,9. Q2-HIGHER2 closes; Q2-K32 is the strictly smaller active gate A_q^[-16] at the single q25078104767246023. No all-prime Vandiver or Greenberg conclusion is inferred. The auxiliary19 comparison and alternate Gaussian datum are active. This is additional substantive movement for review03, not an extra scheduled review or checkpoint.

## Timed checkpoint 06 — 2026-11-21T04:45:56.415186+00:00

Scheduled interval reached. Creating K17_checkpoint_06.zip with all current deliverables, authored research notes, exact computation, proof audits and pinned Lean source evidence. No prior checkpoint is included. This is not a final answer or a scheduled three-hour progress review.

## Degree-thirty-two closure — 2026-11-21 05:05 UTC

K17-K32-VANISH and K17-NINE-DEGREES-PERIOD are promoted after complete root and independent archive whole-proof readings. All alternate-field source hypotheses and local/global coverage have separate whole-proof audits. The complete two-class U3 model over Q(sqrt-7), with full171-dimensional Schur operator, gives determinant13187546903051047 modulo25078104767246023; the entire61-dimensional level-seven classical space with all cubic twists gives15133664954664570. Root executed both the complete C++ replay and the independent full Python reconstruction, and independently replayed the distinct integral GL2 implementation. Original possible conductor49 systems are retained and covered by twisting. The exact direct OneCharU_s criterion permits auxiliary2 and yields zero strict Selmer length. The last primary component vanishes.

Q2-K32 changes from current gate to proved. The seven new specified degrees are12,16,20,24,28,32,36, so K4k=0 for1<=k<=9. Full-domain odd Soulé characters through weight19 are onto at every odd prime. This finite range does not settle all-prime Vandiver or the remaining irregular-prime kernel gate.

Q2-HIGHER3 now records the active degrees40,44,48. Exact exploratory E=-3 gcds leave larger residual integers. Full certificate replays and alternate E=-7 tests over composite residue rings are active; no higher3 vanishing is promoted. Q3-IRREG remains at its explicit arithmetic gate. This is a substantive row closure, not an extra scheduled review or checkpoint. Next review05:15:36UTC; next checkpoint05:30:36UTC.

## Third scheduled substantive review — 2026-11-21 05:15:37 UTC

Due05:15:36UTC. The review counts only closed open rows and strict reductions of main-question gates. Exact exploratory data, packaging, and conditional criteria with unchanged missing inputs do not count by themselves.

| Main question | Current status and strongest checked gate | Movement since review02 |
|---|---|---|
| Q1: exact Step17 | Exact quantitative strict Selmer statement and Host source contract remain closed. The stronger actual OneCharU_s direct unit criterion is now fully reconstructed and used with pointwise coverage. | Its new use closes Q2 rows below; no extra movement is double-counted here. |
| Q2: K-groups and Vandiver | K12,K16,K20,K24,K28,K32,K36 are proved zero after full source, model, computation and final whole-proof audits. Together with known K4,K8 this gives K4k=0 for1<=k<=9. The Vandiver equivalence and residue-class extension remain exact. | YES: Q2-NEWDEG, Q2-HIGHER, Q2-HIGHER2 and Q2-K32 have all changed from open gates to proved. |
| Q3: tripod kernel | Every odd Greenberg prime and all primes below2^31 remain covered. New K17-COMPONENT-CONTROL and K17-ODD-COMPANION-EXCLUSION prove all-level plus-component vanishing for exponents−2j, j0..9, and eliminate actual odd torsion companions2j+1. | YES: the remaining module gate is strictly smaller, confined to the other Delta characters. This is not an added entire prime or a proof of Triple-NV there. |
| Q4: integral B3 | All-weight integral odd free generation at2 and regular odd primes remains proved; it fails at irregular Greenberg primes. Full-domain Soulé characters in all odd weights3..19 are now onto at every odd prime. | The strengthened finite-weight character conclusion follows from the Q2 closures; no false integral-generation inference is made. |
| Q5: cote149 | All treated Kummer/recognition rows retain their proved or refuted scopes. The unmarked-diagram counterexample remains explicit. | No new movement in this interval. |

Complete current open-question list: **Q3-IRREG, Q2-HIGHER3, Q2-HIGHER4**. Q3-IRREG now requires Greenberg only in the remaining plus characters, or a valid positive-rank argument there; in the cubic route the remaining characterwise cyclicity, pair support and actual triple nonvanishing are not supplied. Q2-HIGHER3 concerns degrees40,44,48: complete E=-3 comparisons and all five full GL2 alternate-field tests pass, but the complete U3 residual-ring replays and final deduction are not yet promoted; the e24 unit calculation is still running. Q2-HIGHER4 concerns degrees52,56,60 and is exploratory.

Review outcome: **MOVEMENT YES**. Consecutive scheduled reviews without movement: **0**. Next substantive review due **06:15:36UTC**. Next checkpoint due **05:30:36UTC**. No checkpoint is created at this review. Work continues under the prompt's stop rule.

## Three further degree closures and two-sided component control — 2026-11-21 05:25 UTC

K17-K40-K44-K48 and K17-TWELVE-DEGREES-PERIOD are promoted after full root and independent vandiver proof readings. Both full E=-3 models and exact combined gcds pass; all five alternate E=-7 U3 and GL2 comparisons are units over their full integer residue rings. The complete independent Python U3 replays cover333,444,576 identifying points respectively, every one of thirteen actual frames, full invariant kernels and all determinants. No residual primality or squarefree claim enters. Root separately replayed all five full GL2 tests, the combined gcd certificate and a newly compiled333-dimensional U3 case, with actual scope logged. Thus Q2-HIGHER3 closes and all K4k vanish for1<=k<=12.

K17-POSITIVE-COMPONENTS is independently checked by archive, with a second exact Akiyama–Tanigawa Bernoulli computation. Every numerator prime of B2,B4,...,B32 is below2^31. Reflection plus the established small-prime range therefore kills all positive even components2..32 at every prime and every cyclotomic layer, independently of Alpoge. Together with new degree vanishings, the proven K-index residue interval is−16..12, and corresponding actual odd p-ramified components are integrally Lambda-free. This strictly narrows the main all-prime module gate again.

Only Q3-IRREG and Q2-HIGHER4 remain current open table rows. A selected-even-companion PairNV/free-factor argument is being developed using the now-vanished reflected positive components; it is not promoted yet. Higher4 degrees52,56,60 remain exploratory. Two discovery calculations hit Python's integer-to-JSON digit limit after arithmetic; failure logs are preserved and isolated reruns permit the required exact large integers. This is not an unscheduled substantive review or checkpoint. Next checkpoint05:30:36UTC; next substantive review06:15:36UTC.

## Timed checkpoint 07 — 2026-11-21T05:30:42.904995+00:00

Scheduled interval reached. Creating K17_checkpoint_07.zip with all current deliverables, authored research notes, exact computation, proof audits and pinned Lean source evidence. No prior checkpoint is included. This is not a final answer or a scheduled three-hour progress review.

## Selected actual free factor — 2026-11-21 05:32 UTC

K17-SELECTED-PAIR and K17-SELECTED-ARITHMETIC-RANGE are promoted after root whole-proof reading, fresh full WWE setup/Proposition2.2.6/Corollary5.1.2 reads, archive final readback and independent tripod complete audit. The two distinct inputs X^[e]=X^[2−e]=0 give rational cyclicity and actual free-Q Pair-NV in the selected even companion. The theorem proves injectivity on a genuine specified closed free factor of H, without Gamma-stability or hypotheses on omitted even/odd torsion. Its leading-coordinate argument uses actual Gamma conjugates only in the ambient group. Finite odd resonances are removed, then bounded weighted Magnus substitution and repeated-root pair-pole extraction apply to every element of the selected subgroup. The logarithm parity wording is corrected locally in the preceding cubic criterion as well.

The arithmetic range e in{−2j,2j+2:0<=j<=12} follows from the checked negative-degree and positive-Bernoulli component vanishings. It strictly settles the restriction question Q3-SELECTED-PAIR, while Q3-IRREG still asks for the entire kernel including omitted companions and mixed words. No new complete irregular prime is asserted. Next scheduled review/checkpoint both06:15:36UTC; no extra checkpoint is created here.

## Both companion parities and a growing range — 2026-11-21 05:40 UTC

K17-BOTH-COMPANIONS and K17-GROWING-COMPONENT-WINDOW are promoted after root whole-proof readback and archive independent full proof/source reconstruction. The root and archive read the entire mathematical proof of Chen et al, Almost all primes are partially regular, arXiv2602.05090v1, Theorem1.1 with §§2–3, and its reflected Corollary1.4. No Lean build is claimed. For a Bernoulli unit B_a, Herbrand and reflection kill both base characters1−a and a; componentwise control kills both at every layer; the exact DIRECT-limit Kummer isomorphism kills the actual even ramified componentM^[a], while WWE/Coleman makes M^[1−a] integrally free. Thus both companion parities are absent.

This gives even-companion deletion in the fixed positive even range2..32 for all p>2^31 (small numerator primes are expressly excluded from that stronger assertion). On the density-one set supplied by the cited theorem, the simultaneous range grows to floor(sqrt(p)/(logp)^alpha), alpha>1/2, with unchanged O_alpha(x/(logx)^(2alpha)) exceptional-prime count. The main kernel gate is strictly narrower in those actual components; no full-kernel theorem for that density-one set is asserted. Known counting results remain cited source statements rather than new findings. Next review/checkpoint06:15:36UTC.

## Actual cubic cohomology class — 2026-11-21 06:00:24 UTC

K17-CUBIC-TRIANGULAR, K17-CUBIC-TWISTED and K17-CUBIC-CYCLOTOMIC-INPUTS are promoted after author, root and independent tripod entire-proof readings. The actual companion residue equals a specified twisted-coefficient cubic obstruction after algebraic localization of the compact continuous cochain complex. The rank-four coefficient extension and both bounded-lift implications are explicit; no identification with all continuous function-field-valued cochains is assumed. Actual norm-compatible cyclotomic inputs supply nonzero multipliers, with inflated representative differences removed by a single localized coboundary. Arithmetic Triple-NV remains unproved. This exact equivalent description is not counted as additional strict main-gate movement. No scheduled review or checkpoint is created here.

## Fourth scheduled substantive review — 2026-11-21 06:16:01 UTC

Due06:15:36UTC. Only closed open rows and strict reductions of main-question gates count. An equivalent description, a new source interface without a smaller arithmetic gate, packaging and pending computations are not movement.

| Main question | Current status and strongest checked gate | Movement since review03 |
|---|---|---|
| Q1: exact Step17 | Exact strict Selmer theorem, Host contract and actual OneCharU_s unit criterion remain proved. The stronger joint residual-trace criterion has completed author and independent source audits; root final source reading/integration remains pending. | No additional main movement counted here. |
| Q2: K-groups and Vandiver | K40,K44,K48 are now proved zero, giving K4k(Z)=0 for1<=k<=12 under stipulated Alpoge. Q2-HIGHER3 is closed. Degrees52,56,60 remain in Q2-HIGHER4: full level-seven GL2 comparisons pass, and one full U3 residual-ring case passes; other full replays are pending. | YES: Q2-HIGHER3 changed from open to proved. No higher4 vanishing is counted. |
| Q3: tripod kernel | The full kernel is settled at2, at every odd Vandiver prime, hence at every prime below2^31, and more generally under one-variable Greenberg. The remaining plus-character gate is smaller: all-level negative-degree and positive Bernoulli components give K-index representatives−16..12; the selected actual free factor is faithful. For p>2^31 both torsion companion parities vanish in even positive characters2..32, and a density-one growing range is proved. | YES: actual companion deletions strictly shrink the main module gate and Q3-SELECTED-PAIR is proved. No whole new irregular prime or arithmetic Triple-NV is asserted. |
| Q4: integral B3 | Full odd integral generation at2 and regular odd primes, and failure at irregular Greenberg primes, retain their precise scopes. Full-domain Soulé characters in odd weights3..25 are now onto at every odd prime. | Finite-weight improvement follows from Q2; no all-weight generation claim is inferred. |
| Q5: cote149 | Every treated Kummer/recognition row remains proved or refuted at its recorded scope, including the explicit unmarked-diagram counterexample. | No movement this interval. |

Complete current open-question list: **Q3-IRREG, Q2-HIGHER4**. Q3-IRREG requires Greenberg finiteness in the remaining plus characters, or a valid positive-rank argument there. The cubic route retains its cyclicity/support hypotheses and actual rootwise triple nonvanishing. Its new exact twisted cohomology dictionary does not itself reduce that gate. The Gamma-closure countermodels concern formal limitations and do not count as arithmetic movement. Q2-HIGHER4 retains pending complete finite-model replays and final arithmetic proofs; promising determinants are not promoted.

Review outcome: **MOVEMENT YES**. Consecutive scheduled reviews without movement: **0**. Next substantive review due **07:15:36UTC**. Next checkpoint after the concurrently due checkpoint08: **07:00:36UTC**. Work continues under the prompt's stop rule.

## Timed checkpoint 08 — 2026-11-21T06:16:02.647956+00:00

Scheduled interval reached. Creating K17_checkpoint_08.zip with all current deliverables, authored research notes, exact computation, proof audits and pinned Lean source evidence. No prior checkpoint is included. This is not a final answer or a scheduled three-hour progress review.

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

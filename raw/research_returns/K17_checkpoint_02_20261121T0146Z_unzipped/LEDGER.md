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

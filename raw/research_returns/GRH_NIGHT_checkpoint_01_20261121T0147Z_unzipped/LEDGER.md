# GRH_NIGHT ledger

Status: **IN PROGRESS**.

Run began 2026-11-21T01:02:00+00:00. Snapshot 2026-11-21T01:47:38.573928+00:00 (21 November 2026 02:47 CET); elapsed 0.76 hours.

Catalogue: 147 rows; questions: 73; check events: 261.

## Inputs and check discipline

A_D is used as the user-designated cited theorem. M_H remains a conditional claim. Missing imported Lean dependencies were not kernel-checked. A proof-check event states exactly the work performed; reading a source statement is not a full-proof audit.

## Progress reviews and checkpoints

The first movement review is due at three hours, and then hourly. No review is reported before it occurs. Checkpoint ZIPs are made only at 45-minute work intervals, never include earlier checkpoint ZIPs, and are never overwritten.

The first three-hour review is not yet due at this snapshot.

## Dated movement record

- 2026-11-21 01:03 UTC: sources unpacked once, theorem definitions read, domain work separated.
- 2026-11-21 01:07–01:13 UTC: Masullo425/426 source errors isolated; nonzero Gaussian and fixed-kernel counterexamples constructed; exact projection repair proved.
- 2026-11-21 01:13–01:20 UTC: odd rank-two Artin/weight-one GL2 transfer obtained; irrational Euler-deformation criterion proved; A5 monomial-positivity reconstruction rule refuted.
- 2026-11-21 01:20–01:30 UTC: finite geometric complexity transfers, exact path-quadric zeta formula, Artin–Tate recognition, positive determinant moment bounds, and integral Kummer obstruction proved and cross-checked. These are status changes on named questions; they are not a timed three-hour review.

- 2026-11-21 01:35–01:43 UTC: arithmetic local zero-count gate closed for all fixed unitary Hecke characters (NT-Z10/MT-M04); BIMS resolvent defect repaired within polynomial runtime (CX-ALG-016–018); cote34 Q03 literal ambient-group obstruction refuted and intrinsic commutator version proved for all pro-l quotients (AG-C34-TYPE/REPAIR/INDEX); exact-family ordinary 15/16 central nonvanishing deduced with full approximation/deweighting proof (NT-Z12). These are dated status changes, not the scheduled three-hour review.


## Current question states

| ID | State and strongest gate | Source |
|---|---|---|
| NT-Q01 | proved/classical: NT-P05–NT-P09; corrected constants and thresholds retained | User number-theory territory; LLS v3 Thm1.1/Cor1.1/Cor1.2 |
| NT-Q02 | proved here conditional on RH ζ_L: NT-F01–NT-F04; full proofs written and geometry peer review passed, including corrected boundary convention | GM2019 Thm1.1/Cor1.2 |
| NT-Q03 | proved precise formulations NT-H01–NT-H04; unsupported h-alone/lower-loglog claims excluded | RETURN_ZETA_TWO IA02/IA09; SA06 B.4a–e |
| NT-Q04 | refined exact input NT-A01/NT-A02: nonabelian Kummer RH needed; M supplies it conditionally | Hooley1967 final theorem; Lenstra1977 Thm3.1 |
| NT-Q05 | proved/classical NT-A03 conditional on M and PID, \|S\|≥2; norm-Euclidean claim excluded | Lenstra1977 Thm9.1 p218 |
| NT-Q06 | proved/classical NT-Z01–NT-Z05 with support/moment restrictions; full GUE/correlations remain gate NT-Z06 | Montgomery1973 §1; HR2003 Thm3.1/5.1 |
| NT-Q07 | no such implication established; exact additional GL2-GRH gate NT-Z07 retained | ILS2000 p56 and Thm1.1 |
| NT-Q08 | proved here conditional on M: NT-L02/NT-L03, norm twists and constants treated; complete written proofs self-checked 2026-11-21 01:23:50 UTC | Simonič2023 Thm1; standard Hecke functional equation |
| NT-Q09 | resolved via independently retrieved Johnston2022 Theorem3.2 equation(3.6); A meets its finite-height condition; ordinary-count convention checked | Schoenfeld1976 Cor1 |
| NT-Q10 | current gate: original AMS PDF access; inherited CX-N07 statement retained honestly | Bach1990 Thm4 pp375–376 |
| NT-Q11 | resolved for the specified χ_{8d} family by FPS2017 Thm1.1: NT-Z11/12; original1999 all-discriminant locator still uninspected | Özlük–Snyder1999 ActaArith91(3),209–228 |
| NT-Q12 | targeted full-proof check passes core argument; requested separate trivial ζ_K qualification in final standalone equivalence | Root MT-L01/MT-L02 |
| NT-Q13 | proved here unconditionally: NT-Z10; complete written proof self-checked 2026-11-21 01:35:27 UTC | Root MT-M04; Simonič2023 Thm1eq(2) |
| NT-Q14 | proved here under A: NT-P11/12, q≡2mod4 correction included | GM2019 cyclotomic specialization |
| NT-Q15 | proved here: NT-L09/10 under A or M respectively; no conductor uniformity asserted | Titchmarsh Lemma3.12; Simonič2023 Thm1 |
| NT-Q16 | proved in full NT-Z12: Schwartz approximation and deweighting, complete self-check passed 2026-11-21 01:40:12 UTC | FPS2017 Thm1.1p2; functional equation |
| AG-Q01 | proved inherited exact Artin–Tate transfers; M adds identified potentiallyCM factors; residual nonCM continuation/RH and exceptional fibres remain explicit gates | BRIDGES Q01; ZETA_TWO ZT01–ZT07 |
| AG-Q02 | proved divisor support with classical factorization now primaryverified: Anderson1986 §5.7 Cor5.7.2/Rmk5.7.3; Artin holomorphy remains separate; AG-SIGNED supplies an exact extra positivity criterion | BRIDGES Q02; ZETA_TWO CM01,ZT02 |
| AG-Q03 | proved AG-FROB; A abelian, M general; auxiliary prime/local-model constraints explicit | ALPOGE_BRIDGES AQ-FINITE; BS1996 Thm5.1 |
| AG-Q04 | refuted AG-COVER by actual biquadratic Q-schemes; motive multiplication is forgotten | Finite-etale Galois category; CX-GEO-005 companion |
| AG-Q05 | proved AG-LAMBDA; no arbitrary nonCM factorization follows | ZETA_TWO ZT08,SV01; SGA6 V§§2,7 |
| AG-Q06 | proved AG-SIGN/HEIGHT with explicit reality/holomorphy/normalization/height identity; unnormalized inference refuted AG-SIGN-NORM | Hodge sketch§3.5; cote44 scans2,4,6,8–9 |
| AG-Q07 | proved AG-CRITICAL; factorwise nonpolar endpoint condition retained; precise boundary source RV1999 Thm7-28 printed289 and FE Thm7-19 printed279 now verified | ZETA_TWO§4; Deligne1979 critical values |
| AG-Q08 | proved AG-DET/MOMENT/HANKEL and AG-SIGNED finite pole witness; prime-defined cohomological realization and moment positivity for arbitrary Artin quotients remain gates | ALPOGE_BRIDGES BR-TR-01/02; SA23 geo-H-lidskii/geo-H-genus; cote1/79–80,111–112 |
| AG-Q09 | refuted by inherited Kummer extension of2; AG-EXT retains good-prime scope | ALPOGE_BRIDGES BR-MIX-01; ZETA_TWO SV01–02 |
| AG-Q10 | rational-zero implies integral-zero refuted AG-KUMMER-2; finite-level criterion proved AG-KUMMER; actual LM6 group/cohomology comparison remains separately required | ORDER31; original149 PDF80/footer79 through PDF85/footer84 |
| AG-Q11 | original notation recovered: literal openness in pi-prime refuted AG-C34-TYPE; intrinsic closure[P,H] openH proved AG-C34-REPAIR from archive Thm1.1; exact index AG-C34-INDEX; section-dependent alternative meanings separately gated | BRIDGES Q03; cote34/64 Rem1.17; definitions53–63 |
| AG-Q12 | already classical; originalPDF74/footer73 image now checked, multiplicative1=trivial group; full §§2–3 curve/reduction proof route read | BRIDGES Q04; cote34/74 (2.5.5) |
| AG-Q13 | current gate: cycle/rank comparison on X×X plus denominator control; no such construction follows from displayed analytic reductions | Hodge sketch§§3.2–3.3; cote16/14–18 no7,44–50 |
| AG-Q14 | current gate: exact height identity for the given cycles and covered L-function; conditional sign deduction AG-HEIGHT proved | Hodge sketch§3.5; cote44 Theorems4–5 |
| AG-Q15 | finite quadratic branch sign detection gains A bounds; existing maximality refutation unchanged because finite-index subgroups share weights | SA22 run1 A6-node-character; run2 A:inertia-maximality |
| AG-Q16 | finite quotient detection/generation effective AG-FROB,CX-GEO-004/008; full profinite kernel/associator gate remains | ALPOGE_BRIDGES R-GTHAT; SA22 GT lines |
| AG-Q17 | current gate: all-power trace bounds for finite exterior constructions and duals; prior reduction retained | ALPOGE_BRIDGES D-WM,BR-WM-02,CC-WM01–03 |
| AG-Q18 | endpoint A does not itself export an indexed K-group theorem; inherited2026K8 claim not independently certified; integral comparison/class-group components remain gates | BRIDGES Q06; Alpoge step17/fn6; ORDER31 |
| AG-Q19 | targeted whole-proof checks passed; root advised completion-density sentence; exact evidence/events recorded | Masullo originalPDF425,426,804,11; root MT-M01–03 |
| AG-Q20 | targeted whole-proof checks passed; no gap found | Root MT-Q01–02; Fable§3 |
| AG-Q21 | targeted whole-proof checks passed after NT-F03 canonical-model/boundary clarification; no residual gap found | Number theory NT-F01–04; GM2019 Thm1.1/Cor1.2 |
| AG-Q22 | classical AG-CM-REC and AG-CM-PERIOD recovered; whole recognition proof read; no A/M novelty or Chow-algebraicity inferred | Anderson1986 Prop5.7.5 and §5.8 Theorem7 |
| AG-Q23 | proved equivalence with all finite signed Hankel PSD and an explicit finite witness for any negative multiplicity; proving these inequalities from independent arithmetic data remains open | AG-SIGNED; rootMT-ART02; cote1Fredholm framework |
| CX-Q01 | proved: CX-ALG-001,003–008; PRIMES-in-P historical attribution corrected by CX-ALG-002 | Bach1990T2/3; Schoof2008T2.2; CX_GRH CX-N01 |
| CX-Q02 | proved: CX-ALG-005 | HAC Algorithm3.34 p100 |
| CX-Q03 | refuted: CX-ALG-014, N=35,a=2,m=17 | Proposed witness-to-factor shortcut |
| CX-Q04 | proved conditional on M: CX-ALG-009; A_D-only extension gate CX-ALG-010 (high valuation coefficient unit or alternative descent) | CX_GRH CX-N15/CX-U02 |
| CX-Q05 | proved conditional generator transfer CX-ALG-011/013; full polynomial relation-search bound remains gate CX-ALG-012 | Bach1990T4; CX_GRH CX-N07/N08 |
| CX-Q06 | proved/classically located: CX-HN-001/002; M supplies it | Koiran DIMACS§2T2,§5T9/C1,1997erratum |
| CX-Q07 | refuted universal replacement: CX-HN-004 x³−2; bounded promise transfer proved CX-HN-003 | CX_GRH CX-K03/K04; ALPOGE_GCT C-GRH-03 |
| CX-Q08 | proved conditional on M: CX-GEO-001 | HN consequence, constructible formulas |
| CX-Q09 | proved conditional on M: CX-GEO-002 | Rabinowitsch principal-open reduction |
| CX-Q10 | proved conditional on M: CX-GEO-003; scheme-theoretic ideal inclusion not asserted | Explicit equations for X,Y |
| CX-Q11 | proved conditional on stated zeta input: CX-GEO-004, explicit bounds CX.2–CX.4 | Bach–Sorenson1996T5.1 p1729 |
| CX-Q12 | refuted: CX-GEO-005, natural and dual7-element GL3(F2)-sets | Galois-category linearization |
| CX-Q13 | proved conditional on M: CX-GEO-006; orbit-closure boundary remains separate | Explicit algebraic group action |
| CX-Q14 | proved inherited conditional refinement CX-NN-001; historical EXPH and equation-access distinctions CX-NN-002/004; earlier unconditional PSPACE CX-NN-003 | GCT V T3.4; CX_GRH CX-K05 |
| CX-Q15 | current gate: CX-LIM-001, uniform hitting sets or independent border-hardness theorem; no logical nonimplication claimed | GCT V T4.7/L4.8; PIT/BPP questions |
| CX-Q16 | specified earlier counterexamples carried CX-LIM-002; actual quotient ranks and uniform data construction remain | ALPOGE_GCT P-F7/P-F10 and PLETH PLE-F5/F7 |
| CX-Q17 | proved input classification CX-LIM-003: those proofs require separate E | CX_GRH separate premise E |
| CX-Q18 | targeted whole-proof checks passed, recorded in events.tsv; no independent formal proof claim | Root MT-ART01/02 |
| CX-Q19 | proved unconditionally: CX-GEO-007 in PSPACE; explicit ambient coordinates and polynomial parameterization retained | GSS2019 Theorem1.3 p5; Lemma4.1/Theorem4.2 pp15–16 |
| CX-Q20 | proved under exact zeta hypothesis: CX-GEO-008; forbidden-prime refinement CX-GEO-004 | ORDER30; Bach–Sorenson1996 Theorem5.1 p1729 |
| CX-Q21 | proved classical explicit-input form CX-ALG-015: supplied positive multiple of λ′(N), time poly(log N+log T) | Miller1976 Lemma5 and Theorem3 p310 |
| CX-Q22 | refuted by CX-ALG-016: F7[X]/(X³−2), ζ3=4; corrected statement CX-ALG-017 | BIMS17 Theorem3.1 authorPDF p3 |
| CX-Q23 | proved CX-ALG-017: nonzero Frobenius projection found by scanning a power basis | BIMS17 Theorem3.1; inherited CX_GRH CX-N13 |
| CX-Q24 | proved by complete independent re-proof CX-ALG-018; direct anti-invariant branch and explicit norm-one square-root iteration | BIMS17 Corollary1.3 authorPDF p2; inherited CX_GRH CX-N13 |
| CX-Q25 | proved CX-GEO-009: AM via coefficient-system HN; B and syntactic degree D must be unary or polynomially bounded | GSS2019 Theorem4.2; ORDER28 Koiran/GCT |
| CX-Q26 | proved inherited transfer CX-ALG-019: imaginary quadratic fundamental discriminants, Las Vegas expected L(d)^(3/sqrt8+o1); randomness retained | CX_GRH CX-N12; Biasse–Erukulangara MainTheorem p4, Algorithm4 p15, Cor1 p16 |
| Q-MAS-COUNT | refuted by MT-M01; restricted arithmetic repair MT-M04 | Masullo9.3.2.4 PDF425 |
| Q-MAS-PROJ | refuted by MT-M02; exact replacement MT-M03 | Masullo9.3.2.6 PDF426 |
| Q-GL2-ARTIN | proved conditional on M: MT-ART01; general positive-weight GL2 remains outside this transfer | ORDER42; Khare-Wintenberger Cor10.2(ii) |
| Q-ARTIN-POS | current gate MT-ART02: positive semidefinite local Heilbronn matrix at multiple zeta zeros; no proof of that positivity | ORDER42; Alpoge steps4,7 |
| Q-EULER-DAMP | proved MT-L01,MT-L02 | Gun-Hazra-Sahu2025 Theorem5 |
| Q-ARTIN-CONE | refuted as a finite-character inference by MT-ART04; no actual Artin L-order counterexample claimed | Alpoge steps4,7; Brauer induction; ORDER42 |
| Q-PATH-COUNT | proved MT-Q01 for every finite field including characteristic2 | Alpoge steps3,5; Fable EXPLAINED §3 |
| Q-PATH-ZETA | proved MT-Q02; exact factorization unconditional and zero locations use A | MT-Q01; RETURN_ZETA_TWO ZT01 |

## Domain research notes


### number theory

# Number-theory work notes

Owner: `/root/number_theory`; model GPT-6 Astra Pro; effort not exposed; run GRH_NIGHT/number_theory. Current work date 2026-11-21 UTC.

## Scope and evidence discipline

The 50-row current catalogue and `section.tex` are current working deliverables. A is the user-designated Alpöge theorem, without a claim to verify missing Lean imports. Every M result remains conditional. Existing IA02/IA09 and CX-N rows are carried background with precise links, never counted as new discoveries.

`evidence/` contains downloaded external publications and temporary page renderings for reference. **Exclude this directory from checkpoints/final deliverables.** `sources.json` retains URLs, exact locators, hashes where available, and verification scope. No full external publication is being redistributed. Our own proofs and notes are original prose, with no deliberate long literal quotations.

## New useful formulations

- NT-F01: explicit Chebotarev transfers to every class function with normalized L1 error.
- NT-F02: finite étale point-count average has error proportional to the number r of generic components; for a connected cover the main error is independent of degree. Additional removed primes cost at most d|S|log x.
- NT-F03: exact splitting-type counting from unions of conjugacy classes.
- NT-F04: finite-prime avoidance has an explicit count criterion; do not silently append arbitrary exclusions to Bach–Sorenson's least-prime theorem.
- NT-L02/03: a full fixed-character Lindelöf deduction, preserving nonuniform conductor dependence and handling pure norm twists.
- NT-H03 and NT-L06 are short useful formulations of classical inputs, not claims to a new general class-number or cancellation theorem.

## Source details resolved

1. Corrected LLS arXiv v3, not an earlier formula, is used throughout.
2. Grenié–Molteni2019 Theorem1.1/Corollary1.2 constants and unramified conventions inspected on images.
3. Shoup1992 Theorem3 original p4 inspected: r^4(log r+1)^4log²p.
4. Lenstra1977 Theorem9.1 original p218 inspected: #S≥2. OCR >2 was wrong.
5. Hughes–Rudnick first zero is nonnegative, including possible central zero; definition on p1. Mean/variance/low moments are unconditional analytic identities, with A supplying real ordinates.
6. ILS2000 p56 explicitly assumes family GL2-RH as well as Dirichlet GRH. The latter alone does not discharge Theorem1.1.
7. Milne CFT v4.03 VI Cor2.12/Example2.13 p191 confirms the ordinary class-number/full-unit-regulator convention.

## Gates and next routes

- Schoenfeld Corollary1 source gate resolved by an independent directly retrieved primary proof: Johnston2022 Theorem3.2 equation(3.6), with normalization explicitly addressed in §2. It also gives ψ threshold59. Original1976 page remains uninspected, but is not needed to certify the consequence.
- Bach1990 Theorem4 original AMS pages are unavailable; the exact inherited source locator is carried, not mislabelled as freshly inspected. Complexity agent owns the full algorithmic row.
- Hooley original final theorem locator is pp219–220; original endpoint blocked. The fully inspected Lenstra1977 Theorem3.1 already gives the density implication, so this is a bibliography-detail gate rather than a reason to omit the consequence.
- Quadratic-family symplectic low-zero density: the 1993 Özlük–Snyder paper has a smaller support range than the later 1999 theorem. Do not conflate them. The original 1999 download remains unavailable. The directly inspected FPS2017 Theorem1.1 now supplies the exact χ_{8d} family statement in NT-Z11 and the full ≥15/16 nonvanishing deduction NT-Z12.
- Further useful additions: exact quadratic-family nonvanishing proportion after the actual family/weight is checked; Li coefficients; prime-race hypotheses including LI; explicit AP Chebyshev bounds; optimal-density family moment theorems where primary sources are available.

## Peer review

Read root MT-L01 and MT-L02 in their entirety. Core proofs pass: normal convergence, no-invariant cancellation at s=1, meromorphic logarithmic derivative and integer residues. Requested the final standalone equivalence to explicitly include trivial ζ_K or say nontrivial Artin factors. Recorded targeted proof-check events. Geometry agent read NT-F01–04 in full and passed the proofs, with a finite-base interpretation correction in NT-F03 and a TeX typo fixed.

## Programme mapping

Finite étale rows attach to SGA1 V§7 and the inherited cote1 trace programme; class-number rows attach to Pic(Spec O_K), SA06 B.4a–e, REVLOC I.5/I.8b, IA02/IA09. Kummer-density rows extend the finite-field/Kummer mechanisms in CX-N02/CX-N05/CX-N11. Chebotarev rows reach SA07 D.3.2 and E.2/E.3. These are run-level links, not independently verified original archive scans. Root/geometry owns exact archive indexing.

## Expansion at 01:34 UTC

NT-L09/10 prove fixed Dirichlet and Hecke Möbius cancellation by a full truncated-Perron argument. NT-Z10 proves the unconditional fixed-character local zero count, including infinite-order Hecke characters, by Jensen with an explicit Euler-product lower bound. NT-P11/12 give uniform cyclotomic progression bounds and include the q≡2 mod4 prime2 correction. Geometry peer reviewed NT-F01–04; its finite-base interpretation correction has been incorporated.

At 2026-11-21 01:35:27 UTC, complete post-draft self-checks passed for NT-L09/L10, NT-Z10 and NT-P11/P12. The Perron proof specifies every contour and error term; the Jensen proof treats the pure norm pole and bounded-height range; the progression proof retains the modulus-two ramification exception. RV1999 original PDF download is now complete and its theorem statements have been read locally.

At 2026-11-21 01:40:12 UTC, the entire NT-Z12 proof was reread after drafting. Checked quadratic root-number parity, Schwartz Fourier support strictly inside (−2,2), L2-to-L1 approximation, order of the two limits, the 1/8 mean-multiplicity calculation, the even-order factor 1/2, and the positive/negative squarefree counting constants. Weighted and ordinary ≥15/16 assertions pass for the χ_{8d} family exactly. NT-Z11 is a cited theorem statement/locator check, not an independent reproof of FPS2017.

Catalogue hygiene: removed an overbroad generic M-prefix sentence saying only Dedekind RH was required in every row. Each row now states its own narrower input; the infinite-order Hecke growth/cancellation rows retain the actual Hecke-GRH hypothesis.


### geometry programme

# Geometry and Grothendieck programme — working notes

Last substantive source/read checkpoint: 2026-11-21T01:41:57Z, from the clock tool. Model GPT-6 Astra Pro; effort is not exposed. Filesystem mtimes are not used as check-event dates.

## Scope and durable handoff

Own deliverables are section.tex, rows.json, sources.json, events.tsv, questions.tsv and this notes.md. The parent owns the assembled paper, registers, checkpoint ZIPs and persistence. Original archives were already extracted and were not extracted again. Evidence PDFs/page renders under evidence/ are reference material for the source checks, not new deliverables or revised source documents.

The full uploaded prompt was read. A is the user-adopted Alpöge Dirichlet GRH theorem; M is conditional universal unitary Hecke GRH. Neither is presented as certifying every step of the proposed proofs. Source rows explicitly distinguish classical results, new formulations, conditional transfers, inherited conclusions, and unresolved comparison gates.

## Current movement

1. **BRIDGES Q03 is no longer merely restated.** The official cote34 PDF was downloaded in full. Thm1.1 is PDF53/footer52; the crossed-out Rem1.17 is PDF64/footer63. Exact groups are recovered: pi is an open arithmetic fundamental subgroup, I its geometric kernel, pi0 its image in Gk, I(ell) maximal abelian pro-ell quotient. H is a pi-stable pro-ell solvable quotient; earlier Lie-group language was struck out. The literal phrase puts closure[pi0,H] open in pi-prime, impossible with infinite arithmetic quotient. AG-C34-TYPE supplies Gm/Fq as a full example. AG-C34-REPAIR proves the intrinsic correction closure[P,H] open in H, for every pro-ell quotient, from the earlier theorem's finite abelian coinvariants. AG-C34-INDEX adds the torsion/Frobenius determinant index and exact Jacobian rational-torsion quotient. Alternative section-dependent intended meanings are kept separate.
2. **The original proof route was read, not inferred.** Cote34 §§2–3 occur later, PDF70–78. §2.4 dualizes coinvariants to H1 invariants, §2.5 handles compactification and finite-field curves, and §3 reduces normal X to a generic hyperplane curve. Thus the corrected statement uses an already available curve theorem, not new higher-dimensional purity. The literal Q04 equation at PDF74/footer73 was checked: multiplicative1 means trivial invariants. Standard SGA inputs are cited and not claimed re-proved from scratch.
3. **CM source gate closed.** Recovered G.W.Anderson, Cyclotomy and an extension of the Taniyama group, Compositio57(1986),153–217, originalNumdam PDF. Images27–31 were read. §5.3 defines PCM; Theorem6 §5.6 supplies Hecke/inertia/Frobenius comparison; Cor5.7.2/Rmk5.7.3 gives signed same-weight Hecke factorization. The print's internal Cor5.8.2 reference is a numbering error. Prop5.7.5 gives unconditional recognition from whole L-functions, with proof read in full (AG-CM-REC); §5.8 Theorem7 gives the exactly scoped tractible-critical period theorem (AG-CM-PERIOD). None implies arbitrary Chow projectors.
4. **Integral cote149 gate sharpened.** OriginalPDF79–86 were image-read. AG-KUMMER proves finite-level/completed Pic and Brauer exact sequences, carefully using inverse limits rather than silently continuous cohomology. AG-KUMMER-2 constructs the normal bundle from the order-two ideal class over Z[(1+sqrt(-35))/2,1/2]: rational Chern vanishing does not kill its integral2-adic class. This does not claim the separate LM6 group/cohomology comparison.
5. **Trace/determinant gate sharpened.** AG-DET extends the squared-zero trace-class determinant to specified entire selfdual order≤1 completions; AG-MOMENT gives monotone lowest-zero bounds and multiplicity; AG-HANKEL gives every finite positive Hankel minor. AG-SIGNED now characterizes the extra positivity needed in specified meromorphic quotients: a negative isolated divisor multiplicity gives an explicit polynomial witness in a finite Hankel matrix. A/M divisor location alone does not supply this positivity or Artin holomorphy.

## Independent checks and coordination

- Root independently whole-proof checked AG-FROB, COVER, LAMBDA, SIGN, HEIGHT, SIGN-NORM, CRITICAL, DET, MOMENT, HANKEL, KUMMER and KUMMER-2, without a substantive gap. Requested explicit ordering of gamma_j before use of gamma1; fixed.
- number_theory independently whole-proof checked AG-DET/MOMENT/HANKEL/CRITICAL, without a substantive gap; same gamma ordering fixed.
- I independently read and checked root MT-M01–03 whole proofs against original MasulloPDF425,426,804 and normPDF11. The complex-Gaussian zero-density and decreasing fixed-kernel counterexamples pass; the Hilbert projection repair passes. These auxiliary failures do not refute the endpoint M. Events already logged.
- I independently read root MT-Q01/Q02 path-quadric stratification and zeta proofs; both pass, including all characteristics and exact shifted signs. Events logged.
- I independently read NT-F01–04 whole proofs. A harmless Frobenius exponent typo and F03 canonical-model/boundary ambiguity were reported and fixed, then rechecked. NT-F02's sharper finite-etale error is rE_L+d|S|logx, r the number of geometricG-orbits/connected generic components; no square-root replacement needed.
- Complexity owns CX-GEO-004/005/008 finite-prime detection, forbidden-prime bounds, transitive G-set diagnostic and finite Galois-image generation. My AG-COVER is the complementary actual V4/Q disconnected arithmetic-scheme example. Complexity is now adding exact Jao–Miller–Venkatesan class/genus/isogeny graph applications; no duplication planned.
- RV1999 boundary locator supplied by number_theory and directly checked in its downloaded primary text: Theorem7-28 printed289, entire proof289–292; Theorem7-19 printed279 completed continuation/FE. This closes AG-CRITICAL's boundary-source locator.

## Honest residual gates

- General non-CM motivic/GL2 higher-rank RH is not covered by a mere weight normalization. A covers abelian Artin factors; M covers finite Artin divisor support and exact potentiallyCM factors. Higher-rank automorphy/RH and actual exceptional fibres remain separate.
- Artin holomorphy is not proved by universal Hecke GRH plus Brauer. AG-SIGNED and root MT-ART02 identify concrete additional positivity tests, rather than claiming their inequalities.
- The determinant operators here are defined from zeros, not constructed independently from primes or geometric cohomology. The arithmetic realization gate remains.
- Cote16 integral Lefschetz/algebraicity and cote44 arbitrary-cycle arithmetic Hodge index require their specified correspondences, denominators and height identities. AG-SIGN/HEIGHT corrects only the normalized analytic deduction.
- Cote149/LM6 integral comparison and specified class-group components remain; inherited2026 K8(Z)=0 is not certified and is not attributed to A/M. Alpöge step17 does not itself export an indexed K-group theorem.
- Finite Frobenius tests do not recover multiplicative scheme structure, mixed extensions, inertia maximality or a full profinite GT kernel. Rational Deligne–Drinfeld freeness in the intake remains a separate inherited2026 dependency.
- Original Q03 is resolved only as the literal obstruction plus the proved intrinsic repair; a different intended raw section-dependent group requires a fresh precise formulation.

## Evidence retrieval notes

Official cote34 full download:84,513,436bytes,210PDFpages including cover. Webopen refused the large file; a full local download succeeded. A range-download fallback was started but became unnecessary; it must not be mistaken for a different source. SHA256 is in sources.json. Source149:36,211,408bytes,136PDFpages, original equations13–22 at recorded locations, hash in sources.json. Anderson1986 NumdamPDF:66pages. The bibliography and exact locations are in sources.json, preserving web reference IDs and URLs. Local RV1999 PDF belongs to number_theory evidence and is referenced by its exact path.

## Next useful expansion

First finish parent peer checks of AG-SIGNED and AG-C34-REPAIR/INDEX, and fold any corrections into all registers. Then use the recovered Tate/CM source to connect actual theta/Shimura facts with the two-method comparison without promoting the endpoint theorem into a validation of intermediate claims. Continue gate reduction rather than merely adding unchanged archive labels.


### complexity

# Complexity branch: working record

Updated 2026-11-21 01:40 UTC by `/root/complexity`, GPT-6 Astra Pro; effort is not exposed.

## Current state

There are 39 catalogue rows in `rows.json`, 14 source records, 99 check events, and 26 question rows. The parent assembles the paper, merged ledgers, and checkpoints. This branch does not write to the persistent destination independently.

The analytic contract is unchanged: `A_D` is the user-designated Alpöge rational Dirichlet-GRH theorem input; `M` is Masullo's universal number-field Hecke-GRH claim and every use remains conditional. The Lean archive has not been independently imported or compiled here. The independent counting premise `E` used by the attached CX_GRH run is not one of tonight's two inputs.

## Complete proofs written and read

The section contains complete, post-draft-read proofs for CX-ALG-005, CX-ALG-014–018, and CX-GEO-001–009. The check events specify exactly what was read. None is a formal verification. Parent `/root` has independently read CX-ALG-005/014 and CX-GEO-001–006, found no gap, and is recording its own cross-review events. Parent has also completed full reviews of CX-GEO-008 and CX-ALG-015–018 with no gap. CX-GEO-007/009 remain in the parent review queue.

The strongest new formulations are:

- Existential constructible feasibility in AM under M, with polynomial-size Boolean selector encoding; radical membership and reduced algebraic-set containment/equality in coAM.
- Orbit membership under explicit action equations in AM under M; a separate unconditional PSPACE route for explicit-coordinate polynomial GL/SL orbit closures, using APS and a fixed elementary-unipotent parameterization of the SL big cell.
- A finite Frobenius trace test with the exact Bach–Sorenson bound, and an explicit quadratic-compositum refinement excluding any prescribed finite set of primes. It recognizes permutation representations and zeta functions, not finite covers themselves.
- A seven-point transitive GL3(F2) G-set counterexample to trace-to-cover-isomorphism reconstruction, with a full character and stabilizer proof.
- Bounded Frobenius classes detect every proper subgroup of a specified finite Galois group; arbitrary representatives generate it, and a sublist of at most floor(log2|G|) suffices.
- The literal fixed-generator resolvent formula in BIMS17 Theorem 3.1 fails over F7[X]/(X³−2), ζ3=4. A nonzero projection is recovered by scanning a power basis. This is an explicit correction of the formula, not a refutation of the paper's construction conclusions.

CX-ALG-015 is the explicit-input-length form of Miller's classical supplied-exponent factoring reduction, not a new claim of general integer factorization in polynomial time. CX-ALG-018 is an independent re-proof of an inherited theorem, not a new discovery of the even-degree quadratic case. The original CX_GRH CX-N13 retains priority for the supplied-extension nonresidue transfer; it now has a fresh complete proof here after the source audit.

## Source audit that changed the proof state

The full BIMS17 Theorem 3.1 statement and proof were read, and the source PDF page 3 was rendered and inspected. Its fixed choice `L = sum ζ^i α^(q^(ki))` can be zero, so the step dividing by L is unjustified as written. The counterexample uses q=7, r=d=3, f=X³−2, ζ=4: α^7=4α, α^49=2α, and L=0 whereas the claimed final power is 2.

For odd r, or r=2 with 4|(q−1), the corrected linearized map is nonzero because its polynomial degree is less than the field cardinality. It therefore has a nonzero value on a power basis. The exponent congruence and norm calculation then work. This closes that exact gate without enlarging the runtime or analytic input.

The p≡3 mod4, m≡2 mod4 quadratic branch is handled independently in Fp². Trace-zero linear algebra gives an explicit square root i of −1; repeated square roots of norm-one a+bi are obtained from exactly one of (a+1)/2 and (a−1)/2 being a square in Fp. Each step doubles the 2-power order; norm −1 ends the loop and certifies a nonsquare. The odd-degree lift to Fp^m preserves it. If p≡1 mod4 or 4|m, a single anti-invariant under Frobenius^(m/2) already suffices. `/root/number_theory` independently confirmed the construction, with an alternative quadratic-tower formulation.

## Inherited results and limits

The supplied attachment contains prior intakes, questions, implications and ledgers, but not the complete prior `CX_GRH.tex`. Elaborate prior compositions, especially CX-N15 finite-field factoring and CX-K05 normalization search, are carried with exact old IDs and modest check status. They are not claimed as freshly audited complete absent proofs.

The inherited general finite-field polynomial factorization result is quasipolynomial, `(d^(log d) log q)^O(1)`, under the precise Dedekind-zeta family of CX-N15, supplied by M. The A_D-only residual coefficient-field gate remains p>d, r∤p(p−1), and v_r(p^(ord_r(p))−1)>1. The maximal Teichmüller coefficient unit or a replacement descent is still needed. A_D does handle specified r|p−1 in every supplied extension.

The class-group bound supplies a small factor base, not a relation-search runtime. The complete imaginary-quadratic algorithm CX-N12 is now present as CX-ALG-019 with fresh primary-statement and certification checks; the broader class-group relation/saturation gate remains algorithm specific. Hilbert class fields of abelian base fields need not be abelian over Q.

Koiran's exact input is the zeta function of a bounded algebraic solution field, which need not be normal. No Galois closure or Artin holomorphy is inserted. The bounded abelian-witness promise transfers under A_D, while x³−2 refutes the proposed universal abelian-witness replacement. The 1997 erratum was read in full; the main result survives with its prime-count correction.

Historical GCT V equation-access conditions are conditions of that cited route. They are not a proof that all possible algorithms need equations. Earlier unconditional PSPACE separating-parameter constructions receive their original credit. No general PIT derandomization, BPP=P, polynomial-time general integer factoring, or VP≠VNP is claimed.

## Literature access and precise locators

The source registry preserves URLs and web retrieval references. Author-hosted Koiran PostScript and erratum were downloaded and converted; the main theorem is on printed p12/PDF13, not the initially guessed later page. Shoup's font encoding was unreliable, so Theorem 3 was read from a rendered image: O(r^4(log r+1)^4 log²p), r=ω(p−1).

Bach 1990's original publisher PDF remains inaccessible in this session (403). The exact prior Theorem 2–4 locators are carried, not falsely marked newly read. Bach–Sorenson 1996 is available as a primary author-uploaded PDF: §2 p1720 specifies the zeta premise and Theorem 5.1 p1729 gives `(4 logΔ+2.5n+5)^2`. Its stated theorem does not itself exclude an arbitrary extra set S; CX-GEO-004 proves the extension trick needed for that refinement.

The GSS journal PDF was recovered at `theoryofcomputing.org` after a failed alternate host. APS is Theorem 1.3 p5; the image-closure characterization is Lemma 4.1/Theorem 4.2 pp15–16; the exact separating-e.s.o.p. statements are Theorems 1.5–1.6 p6. Miller's original Lemma 5 and Theorem 3 p310 were visually checked; its supplied λ′ multiple and bit-growth hypotheses are explicit.

All cote/scan companions in this section are inherited crosswalk locators unless expressly stated otherwise. No original Grothendieck archive scan was freshly inspected by this branch. SGA/EGA locators serve as geometric frameworks, not as claims that those texts contain the modern complexity bounds.

## Peer review performed for the parent

MT-ART01 was read in full and matched to Khare–Wintenberger Corollary 10.2(ii), author PDF p21: finite-image irreducible odd two-dimensional complex representations are modular of weight one. The independent holomorphy theorem plus M's Brauer divisor support gives GRH, including projective A5 image, without pretending to prove general Artin holomorphy.

MT-ART02 was read in full: the central convolution spectrum is exactly nχ/χ(1), with the stated normalization; cyclic restrictions recover nonnegative Hecke orders, and Θ(1)=ord ζ_L. The whole strengthened MT-ART04 A5 example was independently checked as written. It passes every induced-linear positivity test while retaining a negative irreducible coefficient. It is expressly an abstract character counterexample, not a claimed realization as actual Artin zero orders.

## Next useful steps

Add the exact Jao–Miller–Venkatesan mixing theorem behind the class-group algorithm, retaining randomness and the full Hecke-character input. Complete parent cross-review of the remaining polynomial orbit-closure and bounded Laurent-arc proof paragraphs. Add the exact proof-check events for any subsequent edits rather than rewriting old dates. Preserve the distinction between making a finite-input gate precise and solving the unrestricted gate.


### root

# Root method work

Original Masullo PDF pages425 and426 rendered and visually inspected. DefD.3.3.1 PDF804 inspected in text, and introductory equivalent definition on PDF11. Both counterexamples use the actual exponential-Schwartz definition. The errors are in the original PDF, not only its API transcription.

Existing ALPOGE_BRIDGES F-SM01/02/13 already prove final strip-support/numerical Q transfers; those remain background. New work targets earlier auxiliary errors, their precise functional-analytic repairs, nonmonomial weight-one GL2 consequences, and Adams-trace Euler deformations.


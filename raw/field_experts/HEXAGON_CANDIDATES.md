# Hexagon candidates: results of ours that could go up as posts

Started 21 Nov 2026, ~01:35 UTC, by the main session e0d20ada (Claude Opus 5.5 at effort max), at the user's word
(USER_INPUTS P8640). The user asked to keep track of what should be a Hexagon post. Two points from that message:
- stuff that is "complete, ... and self-contained in such a way as to allow a Hexagon post without feeling concerned
  that, you know, the next day we'll supplant the proof";
- interest: "the stuff that people want to know about right now", and "if there's something that should be
  advertised ... let me know".

Nothing here is rushed. One thing is not optional: an entry that passes all five tests and is timely goes to the user at
once.

## The five tests (all must hold before a post)
1. **Complete.** Every step is proved and written, with no gap. A refutation comes with its counterexample.
2. **Self-contained.** The post reads on its own. Its inputs are published or formalized results, cited with exact
   locators. Alpöge's Lean-checked theorem counts as such an input; Masullo's unrefereed draft does not.
3. **Stable.** Nothing of ours that is running or planned will soon supersede or strengthen it (successor prompts,
   checkpoints still coming). No one else has it either: a literature search is done first
   (memory superseded-results-not-posted).
4. **Checked.** It has an intake's targeted proof check and at least one independent re-proof or computation, recorded
   as check events. Before submission I read every page (memory read-before-submitting).
5. **Of interest now.** Someone would want to know it today.

**Flag at once:** when an entry passes 1-4, or is one gate away, and test 5 is strong, tell the user in that same turn:
what it is, why now, and which gate is left.

The allowance is 5 deposits per UTC day (since 21 Nov 00:29 UTC). Post format: `recent_results_20261114/HEXAGON_POST_FORMAT_20261114.md`.
Series design (S6): `s6_pro_prompts_20261112_work/reviews/S6_SERIES_DESIGN_20261119.md`. The account and the past
deposits: memory hexagon-outlet.

## In hand elsewhere
- **The S6 series.** Paper V is published (hexagon:2611.00742v1). The other papers are with session aacf1302 and the
  S6_SERIES_PUBLISH run.
- **"Double GRH: what does it mean?"** This is a Reddit post for the LLM-mathematics subreddit, not a Hexagon paper: open
  directions people can send their AI after (the user, P8630-P8633, and to this session after P8640). The draft is in
  `reports_20261120/reddit_double_grh/DOUBLE_GRH_REDDIT_DRAFT.md`. It leaves out the entries below that we will post
  ourselves.

## Candidates, newest first

| # | Result | Source | Checks so far | Literature | Stable? | Interest now | Gate left | State |
|---|---|---|---|---|---|---|---|---|
| H01 | **DEPOSITED 21 Nov 2026 02:56 UTC as hexagon:2611.00789 (v1); Alpöge informed by e-mail 03:08 UTC; Katz not e-mailed (the user).** **A sign-only proof of Deligne's purity theorem** (Weil I, Théorème 1.6), and of Weil II 3.3.1 for H_c of constructible sheaves. On U^k, cut by a generic hypersurface built from a bilinear "path form", generic weak Lefschetz (Katz, ACT Cor. 3.4.1, weight-free) turns the trace-formula remainder into an effective class [K_k] + H_c^d(U,F)^{⊗k}. Parseval bounds it at square-root size, up to a loss that does not grow with k, and tensor powers finish. It uses no monodromy, no Lefschetz pencil and no Rankin-Selberg. It is Alpöge's footnote 3 made complete. | HODGE_SIGN final (prompt 32): SG-08-SG-11, HS-01-HS-03 | Intake, every step a targeted proof check (Claude Opus 5.5 at effort high, 21 Nov). The main session (Claude Opus 5.5 at effort max) rederived in outline the remainder identity and the Parseval bound; that is not a full check. | Not searched. The intake believes it is new, from memory. | The idea is Alpöge's footnote of 20 Nov, so he or others may write it up soon: timing matters. | Very high: a new proof of the Weil conjectures, a day after Alpöge. | An independent re-proof; a literature search; a self-contained write-up with every proof; my read of every page. | **FLAGGED; the user, 21 Nov: [the user's words, omitted], Fable may be consulted, correctness first ("It does need to be correct"), and "a nice bounded post on Hexagon that clearly articulates the thing is still valuable anyway", so novelty or a scoop is no reason to hold it. Independent check by a3ccbc11 (Claude Fable 5.2 at effort max) running; paper by the main session. PUBLIC on GitHub since 21 Nov ~03:1x UTC (research/grh_20261120/deligne_sign_only/); Reddit draft reports_20261120/reddit_double_grh/DELIGNE_SIGN_ONLY_REDDIT_DRAFT.md. Fable check DONE: every step re-proved, one fix (Lefschetz input from Katz App. A.5 via the graph immersion), adopted. PAPER WRITTEN, all 11 pages read, 0 overfull: reports_20261120/deligne_sign_only_paper/deligne_sign_only.pdf (also on GitHub as a draft); waiting for the user's check and go before the deposit.** |
| H02 | **GCT VI Theorem 1.6.1(d) fails as printed**: on the Kahle-Michałek plethysm ray, the generating function is the Hilbert series of the D_5 Kleinian singularity. The Cohen-Macaulay form holds and follows from part (c). With it: PH3 ⇒ PH2 for the stretching families, with an explicit polynomial bound; and the homogeneous Ehrhart form of PH1 fails, repaired by a minimal two-dimensional shifted polytope (P-F1). | ALPOGE_GCT cp01 (prompt 23); GCT_PLETH; errata E1 | Intake: proof check, φ(s) recomputed for s = 0-24. The main session checked GCT VI's statements against its source. | Kahle-Michałek still to be read: they may already note the failure of (d). | The counterexample is stable. The successor of prompt 36 (the PH3 degree target) may strengthen the rest. | Moderate (the GCT community). | The KM check; note E1 to Mulmuley first, on the user's yes; the write-up. | candidate |
| H03 | **Border rank by an exact, norm-free reduction** (F-23): min over 0 ≠ u ∈ U_{n,b} of BR(u) = BR(T_b), hence BR(T_n) ≥ C(n,b)^s + BR(T_b) − 1. For the 4×4 determinant and permanent this gives border rank ≥ 39. | GCT_GINEQ final (prompt 27): F-13, F-23 | Intake: all 23 findings confirmed with full proofs; the run's scripts pass on rerun. | The bound 39 needs a proper search. The best figure found so far is 38, for the determinant only and for the weaker symmetric border rank (Farnsworth). | No: GINEQ's successor is to push F-23 asymptotically. Wait for it and post the combined result. | Moderate to high (complexity). | The literature search; the successor; an independent check. | wait |
| H04 | **Grothendieck's cote 44, Th. 5 (scan 004) fails as displayed.** The counterexample is explicit: P²×P², with the flag-threefold pencil diag(λ, λ+μ, λ+2μ). The missing correction comes from the nodal fibres when E = 0. | HODGE_SIGN AR-01; errata E5 | Intake: example rederived. | It corrects an unpublished draft of his, so it is new as a counterexample. | Stable. | Moderate (readers of the archive). | Check the scan image; compute each fibre's contribution (the intake did not); then a companion paper on cote 44 (memory hexagon-outlet, "Companion work as papers"). | later |
| H05 | **RH for every CM motive, under Masullo** (CM01). It needs his claim for unitary Hecke characters of infinite order. The gate left is the non-CM motives. | ZETA_TWO CM01 | Intake: confirmed, given Anderson Cor. 5.7.2 (not opened). | The route is classical (Deligne 1979, Anderson 1986). | It rests on an unrefereed draft. | Moderate. | Masullo's proof refereed or checked. | hold (conditional) |
|  | **H05 VOID (22 Nov 2026):** Masullo's draft is not a proof (Vakil's update; MA-HM-003; the user). "Under Masullo" now means: conditional on GRH for unitary Hecke characters of infinite order, an open hypothesis. Not a post. |  |  |  |

**What Alpöge's theorem makes unconditional**, as a catalogue with classical locators, is material for the Reddit post
and for a possible topical note. It contains no new theorems of ours, and others will make such lists quickly. Its source
is prompt 42's `CONSEQUENCES.tsv` (running), together with the CX_GRH and ZETA_TWO intakes. One entry so far is IA05:
Alpöge removes the Siegel-zero gate in Wei's bound for CM heights (Cor. 4.3, Prop. 4.7); the logic is confirmed, the
constants only at statement level.

**Older candidates** (14 Nov; their state is in `recent_results_20261114/REVIEW_REGISTER_PRO_RESULTS_20261114.md`):
- Q22, Bowditch's dendrite theorem with infinite torsion;
- EXIT_ONE_TYPE.

Q03 is dropped: Jansen, arXiv:2611.09392, proves it with better bounds.

## The back catalogue (not yet swept)
The intake ledger (`field_experts/INTAKE_LEDGER.md`, 21 Nov 01:18 UTC) counts:
- 153 research runs;
- 10,460 statements in their newest registers, of which 3,693 have been checked by an intake.

Candidates sit in the intakes' "What is new" sections. 29 of the 32 intake documents in `field_experts/intake_20261120`,
`field_experts/intake_20261121` and `results_register/horizontal/sweep3` have one. The older Longue Marche, Dérivateurs
and S6 intakes keep theirs in their own folders. The sweep: pull those sections out by script, then judge each against
the five tests.

## How entries get here
- Every intake briefed from now on answers one more question: does any finding pass the five tests, and if not, which
  gate is left? (`intake_20261121/INTAKE_BRIEF_20261121.md`, "Hexagon readiness").
- I add the entry the same turn, and flag a timely one to the user at once.

**Added from intake round 2 (21 Nov ~02:5x-03:1x UTC)**, by the agents' Hexagon-readiness verdicts (each by Claude Opus 5.5
at effort high):

| # | Result | Source | Checks so far | Literature | Stable? | Interest now | Gate left | State |
|---|---|---|---|---|---|---|---|---|
| H06 | **What Alpöge's step 17 proves.** It is a Lean theorem in his archive: a Selmer-group bound giving log\|K_{4k}(Z)\| ≤ C(2k)^7, with C not evaluated. The kernel question is proved at ℓ = 2 and for every odd prime below 1000. At 37 and 691, integral odd generation fails even though the K-groups vanish. | K17 cp02 (prompt 31) | intake: 5 findings checked in full, including the whole ℓ = 2 kernel proof | compare with Soulé 2003 | the run is still going | **high (the agent flags it as timely)** | Soulé comparison; the source chain behind the exponent 7; for ℓ = 2, a re-proof by another model family | candidate, timely |
| H07 | **A1 without GRH** (A05): the anabelian A1 statement proved with no GRH input; a rebuild of our ANABELIAN_A1 cp03, which our records list as open | AN_GRH cp02 (prompt 30) | intake: proof read in full | to search | ? | high for the archive line | literature search; independent re-proof of Steps 1-2; check whether ANABELIAN_A1 cp03 was taken in | candidate (the agent's strongest) |
| H08 | **Grothendieck's 1969 prediction to Kostant fails** (BR-12302): in sp₄, the orbit of dimension dim G − r − 2 has tangent rank r − 1 | ALPOGE_BRIDGES cp03 (cote 123) | intake: confirmed by hand and by its own computation | Brieskorn, Slodowy to check | stable | moderate | literature search | candidate |
| H09 | **Divided powers in Alpöge's step 2** (DP1-DP3 with DP32): the actual Cartier dual of the height-h formal group, with sharp slopes p^i/(p^h−1) summing to c_h; 115 exact checks on three Honda groups | DP_MULT cp01-cp02 (prompt 34) | intake: checked in full plus its own recomputation | to search | the run is still going | moderate to high | literature search; the run's final | one gate away |
| H10 | **Conjecture 1 of Biró's arXiv:2604.11205 (v1) contradicts Louvel's first moment of Salié sums.** With L = 4, K = r = 1, m = 4, n = 1, α = 0, the conjectured C^{1/2+ε} bound fails: by Louvel (Monatsh. Math. 168 (2012), Thm 1.1) the sum has main term (4/π²) C ∫g. Direct sums over c ≡ 1 (mod 4) up to U = 750, 3000, 6000 give 0.4007, 0.4026, 0.4034 against 4/π² ≈ 0.4053 | S6_05_ARITHMETIC, Statement A.5.7 (ari:A.5.7, p. 37). Compendium only: no S6 series paper prints it (checked 21 Nov 03:2x UTC: no Salié, Louvel or Biró in the deposit copies of I and V; the posting plan of 20 Nov says the same) | the main session's sense check (s6_pro_prompts_20261112_work/reviews/S6_INTAKE_CHECKPOINTS_20261115/A57_sense_check/); cleared for the note to Biró (grant_evidence/OUTREACH_CHECK_STATUS_20261119.md) | Biró v1 and Louvel read from their arXiv sources | stable; Biró is preparing a v2 that modifies the conjecture to exclude the case | high for Biró: on 20 Nov he asked whether the PDF stays online so that he can cite A.5.7, and whether he may name the user | only if Biró wants it: the user's draft reply of 21 Nov offers a short Hexagon note for citation ([the user's words, omitted]). If he accepts: write the note (the specialisation, Louvel's main term, the numbers), an independent re-proof, post | on offer to Biró (the user, 21 Nov: a quick Hexagon draft if he wants it cited; otherwise none) |
| H11 | **Grothendieck's 1964 Th. 4 (cote 44) for abelian varieties in every characteristic** (JAC-T4.3). Milne's report does not state it | JAC1964 cp03 (prompt 40) | intake field_experts/intake_20261121/intakes/JAC1964/ (a8d75352, Claude Opus 5.5 at effort high): 7 confirmed, every cote 44 locator matches our text of record | to search | the run is still going | high for the archive line | its input OpenAI 032 Cor. 8.4 (via Milne's report) is unrefereed, so test 2 fails as it stands; an independent re-proof including JAC-P01; a literature search | candidate (conditional) |
| H12 | **Ghost classes: the dichotomy and an explicit bounded division** (GHOSTS B03, P09/P13, R10-R12): an algebraic class has eventually constant complexity across primes, a non-algebraic Hodge class would pass at every prime with complexity going to infinity; the exact minimum is 16 at every good prime; on the principal Q(ω) Weil fourfold component, from Schoen's published construction, D₀ = 132,269,760 | GHOSTS final (prompt 39) | intake field_experts/intake_20261121/intakes/GHOSTS/ (abcaba9b, Claude Opus 5.5 at effort high): 19 findings confirmed by proof check, W04's certificate rerun and passing, 0 refuted | to search (P6 has a 2009 precedent, Brünjes-Serpé) | final | high (the Hodge line) | a literature search; an independent re-proof of R10-R12 | candidate, two gates away (the intake: the strongest Hodge-line candidate after H01) |
| H13 | **Occurrence obstructions for per_n against det_n with no padding** (GCT_KRON A-030): an explicit infinite family, n = m ≥ 3, the relevant Kronecker coefficient being zero; F-025 adds a multiplicity obstruction that is not an occurrence one (q = 6 > K = 5 for per_3 against det_3) | GCT_KRON cp05 (prompt 26) | intake field_experts/intake_20261121/intakes/GCT_KRON/ (a17221e5, Claude Opus 5.5 at effort high): A-030 confirmed by proof check with four computations; F-025's permanent side by computation (Jacobian rank 49) | to search: set it against Bürgisser-Ikenmeyer-Panova (no occurrence obstructions with padding) and Ikenmeyer-Panova | the run is still going | moderate to high (GCT) | a literature search; the run's final | candidate, one gate away |
| H14 | **Four-row multiplicity obstructions under genuine padding** (CUE_GCT R-14), starting with z·per_8 against det_9 | CUE_GCT cp03 (prompt 36) | intake field_experts/intake_20261121/intakes/CUE_GCT/ (a17221e5): R-14 confirmed by proof check; R-13's dimension recomputed for m = 4 to 8 | to search: Dörfler-Ikenmeyer-Panova (multiplicity obstructions are stronger than occurrence obstructions) first | the run is still going | high if new (GCT) | a literature search; the run's final | candidate, one gate away |
| H15 | **Tsimerman's Galois-orbit lower bounds for CM points in A_g, made effective** with explicit exponents (ZETA_NEXT NC03-NC04), from Stark's descent with Alpöge (NX01-NX03: κ_K > 1/(173 log D_K) for every normal field, a transfer of known results); André-Oort itself is not made effective | ZETA_NEXT final (prompt 43) | intake field_experts/intake_20261121/intakes/ZETA_NEXT/ (ad855737, Claude Opus 5.5 at effort high): 8 of 22 findings checked in full, 2 proofs read with cited theorems carried | to search | final | high (timely: Alpöge's GRH) | a full read of NC02 and NC04; a literature search; an independent check of the constants | candidate, one to two gates away (the intake: the strongest new candidate) |
| H16 | **Grothendieck's tangential-section question (cote 149, scan 85) answered**: yes with the marking of scans 83-84, no without it | K17 cp05 (prompt 31) | intake field_experts/intake_20261121/intakes/K17/ part 3 (ad855737): statement level | to search | the run is still going | high for the archive line | an intake read of the proof; a literature search | candidate |
| H17 | **Δ vanishes on GT-hat** (Δ|GT̂ = 0, with d₂ = 0): EXIT_TOWER E.49 with GT_TOWER_CHECK A.3/A.7 and A.5; DELTA23 adds a second route (the cubic descent, Δ∘𝒟_E = d₂: e₃ = 0 on GT̂ would give it without E.49's final step) | EXIT_TOWER cp28, GT_TOWER_CHECK cp10; DELTA23 cp06 (prompt 29) | intake field_experts/intake_20261121/intakes/DELTA23/ (ae4ae3dc, Claude Opus 5.5 at effort max): 19 of 22 read in full confirmed; Claude Fable 5.2 at effort max refereed the two key inputs on 18 Nov, not E.49's final step | to search | stable on our record | high for the Longue Marche line | an independent check of E.49's final step, or a proof of e₃ = 0 on GT̂; a literature search | candidate, one gate away (found by the DELTA23 intake: prompt 29 had not named these rows) |

H03 (border rank ≥ 39): a17221e5 found no published bound of 39 or more for either polynomial. The best known are 38
(Farnsworth, the determinant's symmetric border rank) and 36 (the catalecticant bound, the permanent); Landsberg-Teitler's
40 is a rank bound. The remaining gates are an independent check of F-23 and the GINEQ successor.

H02 (GCT VI): checkpoint 03 adds P-F19 (the canonical clause of PH3 fails for plethysm with inner shape (3): the degree
needed is at least 2^{n−1}, against O(n⁶)) and P-F14/P-F15 (§3.3's SH(a), PH2 and PH3 fail as stated). Note E1 needs a
qualifier on "PH3 ⇒ PH2"; P-F19 and P-F14/P-F15 go in a second note.

Masullo p. 495 (F-SM-19): the formula as printed is identically zero, apparently a typo with an obvious fix (F-SM-20). This
is an erratum for him, not a post.

## Round 3 of the intake (21 Nov 2026, ~03:2x-04:4x UTC): what changed for the earlier entries
From the part-2 intakes in field_experts/intake_20261121/intakes/ (six registry agents, Claude Opus 5.5 at effort high; entered by the main session
e0d20ada, Claude Opus 5.5 at effort max).
- **H02 strengthened and retitled** to P-F31 (ALPOGE_GCT cp05): the existence clause of PH3 (GCT VI, Hypothesis 1.6.7)
  is false for plethysm with inner shape (3); the cubic-invariant series has a simple pole at every primitive
  2^(n-1)-th root of unity, so every positive form needs a denominator weight of at least 2^(n-1), against a parameter
  of size O(n^6). Proof checked in full (P-F23, P-F30, P-F31; P-F30 also by an exhaustive check over about a million
  cubic supports at n = 4; Salmon's invariant series matched at n = 4). Companions: the Theorem 1.6.1(d) erratum and
  P-F14/P-F15. Tests 1, 2 and 4 pass, interest strong; the gate left is stability (the run's final) and a literature
  search. **Flagged to the user (one gate away, strong interest).**
- **H04 met on the quadric example** (JAC1964 H9-C1, H9-T1, H9-T2): Th. 5 fails as displayed on a quadric pencil, and
  H9-T1 corrects it with one term per singular fibre; this finishes the per-fibre computation HODGE_SIGN left open.
- **H06 split.** H06a (what step 17 proves): gates unchanged. H06b (K17 cp03): Vandiver implies a positive answer to
  Ihara's kernel question, so it holds for every prime below 2^31; the cited Fukaya-Kato and Wake-Wang-Erickson inputs
  were not checked against their texts. Gates: a literature search, an intake read of the run's pole-separation
  theorem, an independent re-proof.
- **H09 strengthened** by DP34 and DP42 (DP_MULT cp04: along every mixed line through the formal group and its dual the
  slope is at most 1/(p²-1) at every height). Gates: the run's final, a literature search, a check of DP41.
- **F50 folds into H01** (GCT_NSRH cp05): the Gaussian construction always gives the opposite path sign, so the
  sign-only route's one real input is the pointwise bound on the stalks; as a by-product |Gauss sum| = √q without
  weights. A v2 of hexagon:2611.00789 can carry it.
- **Other candidates named by the intakes, not yet entered as rows:** A05 (= H07, unchanged); the cote 123 letter with
  CC-APG04 (ALPOGE_BRIDGES cp05: an outer-invariant class exists exactly outside type A_{2m}, the existence half
  checked); the factoring reduction CX-ALG-023-026 (GRH_NIGHT, later); DEG_L B19 (witness degree of order √J, not
  urgent).
- **Errata, not posts:** Masullo §9.3.2 (three defects checked against PDF pp. 425-426: 9.3.2.4, 9.3.2.5, 9.3.2.6; to
  the author); Milne's report on OpenAI 032 has a missing sign (GHOSTS C15; to Milne).

## Round 4 of the intake (21 Nov 2026, ~06:0x-06:3x UTC)
From the round-4 intakes in field_experts/intake_20261121/intakes/ (the same six agents, Claude Opus 5.5 at effort high).
- **H15 and H16 added** (ZETA_NEXT, K17 cp05). The agent numbered them H11 and H12, which were already taken.
- **H04 is complete mathematically** (SIGN_NEXT SN-44-01, with JAC1964 H9-T1; the P²×P² nodes rederived: each node
  contributes 1, and 0 = 3 − (1+1+1)). Left: the scan-004 image check, the run's final, the write-up.
- **H01 v2:** add an SN-14 remark (trace data alone cannot give scan 049's positivity), cite cote 16 scans 034-040, and
  fold in F50.
- **H06b strengthened:** Greenberg suffices for Ihara's question (K17 cp05).
- **H09 complete in content** (DP51 closes the last local escape); the gate is the run's final.
- **H02 unchanged** (ALPOGE_GCT cp06: no new check events on P-F31 or its companions).
- **The factoring candidate is superseded** by OpenAI's PF26 (GRH_NIGHT cp04); its gates are a check of PF26, a literature
  search and a re-proof of CX-ALG-028. MT-M20/M23 is a possible new candidate (gates: an intake check of MT-M18/M19, a
  literature search).
- **Possible erratum, unverified:** K17 cp05 reports a gap in DEKM's published enumeration, on which the K₁₂(ℤ)
  reduction had relied. It is to be checked before any message to anyone.
- **H03 strengthened to border rank ≥ 42** for both det_4 and per_4 (BR_PENCIL cp01, prompt 44). The intake (a17221e5,
  Claude Opus 5.5 at effort high) confirmed it independently:
  - every coordinate subset up to size 5 enumerated; minimum 11 over all 376,992 five-subsets for det_4, and for per_4
    except one orbit of 576, settled by R-04, which was recomputed exactly over Q without the run's certificate;
  - 36 − 5 + 11 = 42;
  - 14 findings confirmed by proof check (5 also by computation), the run's verifiers rerun and passing.

  Two literature searches found nothing at 39 or above (Farnsworth 38, the catalecticant 36). It supersedes GCT_GINEQ's
  39 (F-23). The only gate left is the run's final (Q-07: does it reach 43?). **Flagged to the user (one gate away, strong
  interest).**
- **H14:** CUE_GCT cp04 R-22 claims the padding range reaches every fixed ratio below √2 (statement level); the gates are
  unchanged.
- **H12 extended to Q(i)** (the Hodge attack, reports_20261120/hodge_bridge/HODGE_DIVISION_ATTACK_20261121.md §5;
  abcaba9b, Claude Opus 5.5 at effort high, 21 Nov ~08 UTC): on the even half of the principal Q(i) Weil fourfold
  component, D₀(Q(i)) = 914,248,581,120 and C₄(Q(i)) explicit. It rests on Schoen 1988 Theorem 2.0 (pp. 11-12) and
  Corollary 3.1 (p. 25), as printed, and on the attack's own proof of dominance for (h, m) = (4, 4); Schoen's p. 26 lists
  that case only as possible. Gates: an independent check of that dominance proof, and a literature search (Schoen's 1998
  Addendum, Markman). The odd half needs another source. Prompt 46 (v2) carries both.

## Round 5 of the intake (21 Nov 2026, ~12:00-12:20 UTC, clock read): the overnight runs' final returns
The runs of the night ended between 04:20 and 08:21 UTC: by the user's three-hour rule, each newest return is that run's
final. Intakes are in field_experts/intake_20261121/intakes/, by six registry agents (Claude Opus 5.5 at effort high:
abcaba9b, af2a18f6, ad855737, a17221e5, a0805369, a8d75352). They were entered by the main session e0d20ada (Claude Opus
5.5 at effort max).

**New candidates, flagged to the user**
- **H18 (new): K_{4k}(Z) = 0 for 1 <= k <= 12** (K17 final, cp08: K17-K12-VANISH, K16-K20-K24, K28-K36, K32-VANISH,
  K40-K44-K48). K_4 and K_8 were known; K_12 to K_48 are new.
  - Inputs: Alpöge's step-17 machinery (the Lean intermediate theorem `OneCharU_s`, not RH); HHO's Vandiver computation
    below 2^31; Rognes-Weibel; finite Hecke computations on compact U(3) over Q(sqrt(-3)) and Q(sqrt(-7)), and on
    classical forms of level 3 and 7.
  - Intake ad855737 read the K_12 proof and recomputed the GL_2 half of the certificate independently, with an exact
    match. It also confirmed the numerical input: every numerator prime of B_2, ..., B_32 is below 2^31.
  - Gates:
    - an independent check of the U(3) half and of the coverage theorems;
    - the standing of `OneCharU_s` in Alpöge's archive. It is proved there as an implication from nine Props. By our estimated closure, that
      implication and theorems discharging its hypotheses lie in the dependency closure of the archive's riemannHypothesis
      (main-session addendum to the K17 part-4 intake, 21 Nov ~12:45 UTC). A compiled `#print axioms` check is left;
    - a literature search.
  - **Flagged (strong interest; several gates).**
- **H19 (new): bounded division for split Q(ω) Weil eightfolds from published inputs** (HODGE_DIVISION D-G34-01..07,
  checkpoint 01; the run is still going). It replaces the unrefereed premises of Severn's manuscript.
  - The run reports: group G34 (order 39,191,040, 756 roots); K-minor 1728; interior period rank 16; supplier repair and
    Brauer transfer.
  - Statement level so far.
  - Gates: the run's final, a full intake read of D-G34-02..06, a script rerun, and a literature search.
- **H20 (new): GCT_PLETH G-036 with T-037**, a complete positive formula for every outer-degree-five plethysm
  coefficient (539 of 539 agree). **H21 (new): G-037 to G-040**, polynomial-size formulas for stable hooks with varying
  outer degree (790 of 790). Both were confirmed by computation (a0805369). Gates: proof checks and a literature search.

**Changes to existing entries**
- **H02 now headed by P-F57** (ALPOGE_GCT final, cp09). GCT VI's PH2 and SH(a) fail on the cubic plethysm family: both
  indices exceed 2^{cn} for every c < 1/4. With P-F19 and P-F31, all three index hypotheses (PH2, SH(a), PH3) fail for
  plethysm.
  - a0805369 confirmed P-F56 and P-F57 in full. The residue formula matches Salmon's n = 4 value, phase included, and the
    remainder ratio is below 1/4 from n = 8.
  - Gates: a literature search, the write-up, and the user's read. **Flagged.**
  - H02b (P-F60: the canonical PH3 clause in the Kronecker case) is at statement level.
- **H03 reaches 43 over C** (BR_PENCIL final, cp02). BR(det_4) >= 43 and BR(per_4) >= 43 in characteristic 0; 42 over
  every field; 44 open.
  - a17221e5 read R-08, R-10 and P-19 in full and reran the run's 22 verifiers. With its own Koszul code it recounted
    1,543,608 low-support seven-subsets in 1,517 orbits and cleared 1,506 of them; it cleared 11 of the 25 Borel ideals.
  - 25 border-apolarity cases rest on the run's certificates and the intake's reading.
  - Gates: those 25 cases checked independently, the write-up, and the user's read.
- **H13:** A-034 (GCT_KRON final, cp07) was confirmed in full: every stretch of the A-030 family gives a strict gap for
  per_n against det_n with no padding. Gate: a literature search.
- **H14:** R-27 (CUE_GCT final, cp08) makes the four-variable dimension exact. Four-row multiplicity gaps exist exactly
  when n^2 <= 2m^2 - m + 1 (m >= 17).
  - R-13 is confirmed by the intake's own computation for m = 4 to 10 (c_9 = 220, c_10 = 286).
  - Gates: a literature search; proof checks of R-23, R-26 and R-27; R-13 for m = 11 to 16 for the narrower post.
- **H12 (Q(i)) now rests on published inputs** (HODGE_DIVISION checkpoint 01).
  - The run reproduces D_Pr = 914,248,581,120 independently.
  - The dominance is van Geemen, Math. Z. 221 (1996), Theorem 5.3(3), pp. 629-630. The main session checked this against
    the GDZ scan (recent_results_20261110/papers/hodge_sources_20261121/vanGeemen_1996_MathZ221_617-632_GDZ/); it is the
    attack's base-point-free pencil argument.
  - The odd component comes through an isogeny of degree 16: D_all = 3,656,994,324,480 (HD-G06).
  - Theorem W is sharpened to δ_W² (HD-WQ).
  - Gates: the run's final, and a literature search (Markman's n = 2 result, effective versions).
- **H07 stable** (AN_GRH final): A05 is unchanged. Gates: a literature search (anchored on the run's Tamagawa/Faltings
  comparison) and an independent re-proof of A05 Steps 1-2. A46 is a new criterion: one pointed odd cyclic cover
  separates points, in any genus and characteristic.
- **H08 is not a post.** BR-12302 is known: Richardson 1987, Lemma 5.1, after Slodowy. It is kept as a cote 123
  archive note.
- **H09** (DP_MULT final): test 3 is met. Gates: a literature search, reads of DP41 and DP51, and one DP42 computation.
- **H11** (JAC1964 final): test 3 passes, and test 4 is strengthened (JAC-P01 confirmed). Gates: test 2 (032 and Milne's
  report are unrefereed) and a literature search.
  - H9-T17 (after a finite cover the height is not positive on homologically trivial cycles; an explicit E^4 class has
    height -12d^3) qualifies the H04 write-up: Albanese-primitive.
- **H16** (K17): test 3 is met. **H06b:** unchanged. **H04:** unchanged (SIGN_NEXT final: Q6g's global instance is
  open; SN-15 makes the Lefschetz order indices computable in every rank).

**Errata, not posts (drafts only after a full check)**
- **DEKM, arXiv:1910.11598v1:** the gap is real.
  - Tables 3-4 and Prop. 4.4 index cells by cone rank; §1.2.1 and Prop. 1.5 use projective dimension, one less. So the
    top cases of Theorem 4.5 (N = 8, k = 12; N = 9, 10, k = 11) have no enumeration behind them.
  - K_8(Z) = 0 is not affected.
  - Before any note: check the published version and the authors' data repository. As of 21 Nov ~12:40 UTC, the
    published version (J. Inst. Math. Jussieu, online 24 Nov 2025) is paywalled to us, arXiv has v1 only, and no public
    data repository was found. The note stays held. K17's K_12 theorem no longer uses the Voronoi route.
- **Masullo** (GRH_NIGHT final): a table of defects (pp. 425, 426, 480, 495, 514-519, and the blank 13.3.1.2). Every
  literal defect has a repair; his central geometric trace identity is the open point. This goes to the author.
- **Thakur 2020, Prop. 2.9 is refuted** (ALPOGE_BRIDGES final, BR-15-CLASSBOUND). The intake checked half of the
  counterexample; check the rest before any note.

## From the raid of the user's own corpus (21 Nov 2026, ~17:2x UTC; reports_20261120/split_zero/EXTRACTION_20261121.md)



- **H22 (candidate): the adjoined-zero semiring G(R) = R ⊔ {τ}.** Spec G(R) = Spec R plus a Boolean generic point (D + M / Milnor-square form for domains; G(A×B) = G(A) ×_B G(B)); G(R)-semimodules = Clifford monoids with R-linear fibres = support diagrams over join-semilattices; f.g. projectives ↔ posets with projective modules; the two quotient families and the smash-product multiplicativity of the separated count. Proved in the user's papers (01, 02, 12 §2; GPT-5.x Pro by date) and partly formalized (SplitZero.lean); the Clifford and Milnor-square readings are the main session's. Status (21 Nov ~17:3x UTC): items 1-4 (normal form, spectrum, gluing, semimodules = support diagrams) independently re-proved and computed by the main session (reports_20261120/split_zero/H22_CHECK_20261121.md, h22_checks.py, H22_CHECK_EVENTS.tsv); item 5 (projectives) proved by the main session (retracts of Boolean lattices are the distributive lattices; split diagram decomposition), computed for n <= 4; remaining before a note: the literature check (Golan; Lorscheid; Deitmar; Horn-Kimura for the lemma) and writing it out.

- Not candidates (standard or elementary): the velocity split (one-line implicit differentiation), the Thoma/total-positivity form of RH (a standard chain applied), the S6 cusp identity (Eichler-Zagier).

- **H23 (candidate, refutation): GCT VIII's Positivity conjecture fails its unimodality clause at r = 3** (P-F-E3-01; consult a8d75352, Claude Opus 5.5 at effort high, 21 Nov; reports_20261120/split_zero/consults/E4_RANK_FOUR_20261121.md, scripts E4_scripts/e3_fast.py, e3_table.py). With the sign of VIII's Figure fw1w2 (VIII's printed b₂ = +(q+1)²/q is a misprint for −), the 132 nonzero structure constants of E^opp(3) (100 with a = 0, 32 with a = 2) are all positive and bar-invariant, 6 are not unimodal, e.g. c(γ²₁, γ²₂₁; γ²₁) = (v − v⁻¹)²(q + q⁻¹)²(q + 1 + q⁻¹), f-coefficients 1,1,3,2,3,1,1, all in the χ² cell; VIII states its computer verified all constants. Status: needs an independent re-run and a reading of VIII's statement and figure before any note or message to the author; then an erratum draft (drafts only). Positive half (a8d75352, E4 §7): every rank-three constant has a forced (130) or chosen (2) realization as a sign-twisted Tate count with unimodal graded dimensions; the six failures are R² × P², R = Res_{F_{q²}/F_q} P¹, with the swap's sign cancelling the middle trace. Proposed corrected statement: unimodality of dimensions, not of traces. Composition with the multiplication (a categorification) open.

## Round 6 (21 Nov 2026, ~18:4x-19:0x UTC; intakes by Claude Opus 5.5 at effort high, of GPT-6 Astra (ChatGPT Pro mode) runs)
- **H12 (Hodge, Weil classes):** HD-U confirmed (targeted proof check by the author of the attack it supersedes; HODGE_DIVISION cp10): for every imaginary quadratic K and every n, c_t <= ceil(8*16^n/n!)*delta*ceil(sqrt T)*Nm(a)^{2n(n+1)}*delta_W^2 (constants 1024, 5462, 21846 for n = 2, 3, 4); supersedes Theorem W. Add HD-U and the all-determinant fourfold bounds (HD-COMP4: Q(i), Q(sqrt-7), Q(sqrt-2); HD-CM4 every class-number-one field through Perry, a preprint). One gate: literature search and write-up. Intake: field_experts/intake_20261121/intakes/HODGE_DIVISION/INTAKE_HODGE_DIVISION_20261121_part2.md.
- **H19 (Q(omega) Weil eightfolds):** two gates (an intake full read of D-G34-04 to 06; the run's final). D-G34's script reruns with all exact checks (period rank 16, K-minor 1728), agreeing with HECKE_DIV S2's independent reconstruction.
- **H18 (K_{4k}(Z) = 0):** range now k <= 15 (KTOWER cp03, KT-K52-K56-K60-VANISH; deduction and the U(3) halves for e = 26, 28, 30 at statement level). U(3) half of K_12 confirmed two ways (7^5 T_7 = 157899 = 7^6 + 40250, endoscopic); GL_2 inputs recomputed (weights 13, 53, 57, 61 at p = 7; 53 at p = 13). OneCharU_s a closed theorem of the archive by source trace (FOneCharU.lean:75-95; CorGKOf.lean:11-25). Open: compiled #print axioms, two coverage theorems, U(3) for e >= 26, the final. Intake: intakes/KTOWER/INTAKE_KTOWER_20261121.md.
- **New erratum candidate (a note to the author, not a post): Soule 2003, Lemma 9 (pp. 777-778) is false as printed** (KT-SOULE-STAB, confirmed): (0 -1; 1 (sqrt5-1)/2) has order 5 in SL_2(O_{Q(sqrt5)}); corrected bound p <= N[F:Q] + 1; nothing changes over Z. Draft only on the user's word.
- **Masullo (errata row):** the section 12.3-12.4 gate is REDUCED (MAS_ARTIN cp02): the prime-carrying intertwiner exists in Meyer's common space (statement level); under all zeros in the narrow strip the draft's identity is Weil's explicit formula (statement level); the remaining step (the full narrow return for every width and every test with g(0) = 0) is EQUIVALENT TO RH (MA-HM-003, checked in full by af2a18f6). Scope tables: M = "central step equivalent to the hypothesis; no independent input located". New literal slips: p. 500, pp. 243/259, (12.4.1.5)-(12.4.1.7). Defect table updated (old rows kept as notes): TO_SEND/PRO/_staging_20261121/cores/MASULLO_DEFECTS_20261121.md.
- **H23:** the hexagon question refined (E4_RANK_FOUR sections 6a-6b): the six are a hexagon of labels with only a Klein subgroup of its symmetries at generic q; at q = -1 the cell's trace form is monomial and an exact C_3 of cyclic slot rotation appears (fixing the orbit-2 pair, rotating the four orbit-4 failures with the two shortest products).

## Round 7 (22 Nov 2026, ~00:0x-00:4x UTC; full intake, wave A; intakes by Claude Opus 5.5 at effort high, of GPT-6 Astra (ChatGPT Pro mode) runs)
- **H01 v2 remark (ALP_MACHINE AM-S1-S3, confirmed by abcaba9b):** a finite-order phase can replace the sign only if it commutes with Frobenius and the powers taken are divisible by its order; a reflected phase cannot (the reflected traces vanish on the rotating part). Add with F50 and SN-14.
- **H23 becomes a GCT VIII errata note (a8d753525):** N-012 (Conjecture 3.2 as printed has no minimum: already in rank one y_n = q^-n is admissible with degree -n, so it selects no E(4)), with H23 (the unimodality clause fails at r = 3) and the printed b₂ sign; N-014 (label order undefined) at statement level. Gates: a literature check, the note to Mulmuley first (drafts only, on the user's word), an independent re-run of P-F-E3-01.
- **Not candidates:** the dimension-ring optima (internal interest); ALP_MACHINE's Hecke part (AM-H04 would become one only with a proof of the window bound H04.4 for some (p, r)).
- **AN_GRH's register:** the ledger had taken a recovered LM8_PUSH cp17 register as AN_GRH's (found by a28ea31f; builder fixed 22 Nov, `build_check_ledger.py` EXCLUDED_DIRS). AN_GRH's own findings are the 69 "Finding" paragraphs of AN_GRH.tex; its full intake with the re-proof of A05 Steps 1-2 (H07's gate) is running.

### Round 7, wave B and the rest of wave A (22 Nov ~00:3x-01:2x UTC; full statement intakes, Claude Opus 5.5 at effort max or high)
New candidates named by the intakes (none passes all five tests yet; gates as the agents state them):
- **SA12 (a203d72b):** the persistent A.2 counterexample (Grothendieck's margin question on cote 31): tests 1-4 pass, one gate (literature search); L6c, R^1 f_* O_X = 0 in characteristic p without resolution: one gate (literature search); B.1 (the 29/071 theorem in characteristic p): test 2 (the published status of purity for finite flat torsors). Also proved: A.2 for finite-type schemes over a field; A.2 for Z[mu_{p^inf}, 1/p] is equivalent to Iwasawa's mu = 0 (open).
- **SA14_SA19 (a262249a):** counterexamples to Grothendieck's 1964 programme (J5: his Th. 5 fails in codimension 2 on the split quadric fourfold over F3-bar; J2a, J2b, J6C): complete and checked, gate = coordinate with H11 (JAC1964); G1: one gate (literature); A3: test 4 met (certify_A3.py rerun), gate = literature; F11 (metabelian quotients of the local pi_1 finitely generated): test 2 (a preprint input, Krishna-Majumder arXiv:2601.12177v2) and literature.
- **SA23 (acadc29d):** an EGA corrections package (0_IV 19.3.12 wrong proof, true statement; III 4.3.6 and IV 20.1.3 counterexamples; IV 21.2.9's local formula wrong): two gates (printed-page check, independent computation); the Hilbert trace formula proved in Grothendieck's hand (cote 1): one gate (open the print sources).
- **SA20 (acf08879):** Grothendieck's collar and cone conjectures (A.104, A.106, A.111, A.112); Int(k + t^m k[[t]]) projective hence flat (B.022-B.023), answering a nonflatness conjecture attributed to Elliott 2011; the Coxeter normalizer splits in A, B, C, D, G2, E7 and not in F4, E6, E8 (D.002, recomputed): each needs a literature search and a write-up (and independent re-proofs for the first two).
- **SA15 part 2 (a8d07e78):** "Grothendieck's admitted integral weak Lefschetz fails" (8.3; the OC chain): two gates (literature, independent re-proof).
- **SA05 (a7b7747f):** the explicit global class of Grothendieck's F_p gerbe: literature (Milne 2003 may compute it) and a full proof read; not urgent.
- **NEG_NIGHT (a17221e5):** A028 (under A, all zeta zeros simple iff the order of finite detection grows faster than 1/sqrt(a)), A024/A025 (the CUE first heat collision is Weibull-3/2, early collisions Poisson), C023/C030 (the parity of #SAT is the Hasse-Witt scalar of an explicit smooth hypersurface: computing it is ⊕P-hard), C027/S016 (one sparse smooth cubic over Z with class L^{v+h} + N L^h, N = #SAT; recognising affine space is equivalent to unsatisfiability): each needs a proof check and a literature search; the run continues.
- **GCT_POS (a0805369):** K-008/K-014 (Kronecker poles at primitive 8th and 16th roots; summed residues) waits for the all-n result; K-018 (the largest determinant order exceeds 2^{n-1}: 512 at n = 9; drop that premise from later prompts) waits for a comparison with Kravtsov; H02 stronger on test 4; H21 should say G-040's literal construction is superpolynomial (PNEW-010).
Errata found on our side (into the records): consult ad855737 (ZETA_LABELS) Q1 Prop. 1 omits the correction term, Q2 Prop. 4 invalid (NN-A001/A002); corpus paper 16's tensor-inverse identity fails (NN-A012, statement level); prompt 54 item 10(a)'s unrestricted sign-fixed claim false (NN-S001: fibrewise 2-torsion); SA05: our R8 degree (H^{4n}), our D.1 Frobenius wording.

## 22 Nov 2026 08:36 UTC: GCT_POS final (main session e0d20ada, Claude Opus 5.5 at effort max)
- **H02b strengthened:** the existence clause of PH3 (GCT VI, Hypothesis 3.3.4) is refuted for Kronecker coefficients:
  every form for g((s^n),(s^n),(s^n)) has a denominator weight of at least 2^(n-1), against rank n^2+5n (K023, R-NEW004,
  K024, PNEW013). Targeted proof check and computations: reports_20261122/gct_pos_ph3_check/CHECK.md. Not an independent
  re-proof. No literature or Hexagon search. Cite 3.3.4, not only 1.6.7 as the run does.
- This replaces 'waits for the all-n result' of the checkpoint-03 line. Still open for Kronecker: PH2, SH(a), and the
  exact pole order for n >= 6. The plethysm statements of H02 are unchanged.
- **H20:** the outer-six reference table (R-NEW-001) is confirmed, 5,214 of 5,214 rows (agent a0805369, Claude Opus 5.5
  at effort high). It extends the checked range and does not supersede H20.
- The final's intake by diff is with a0805369. Nothing here goes into a prompt, post or e-mail as novel before a search.

## 22 Nov 2026 08:57 UTC: the GCT_POS final's intake, read (main session e0d20ada, Claude Opus 5.5 at effort max)
- Intake: field_experts/intake_20261121/intakes/GCT_POS/INTAKE_GCT_POS_20261122_final.md (a0805369, Claude Opus 5.5 at
  effort high). It replaces the GCT_POS line of checkpoint 03 above.
- **H02b is now 'numerical PH3 fails for Kronecker coefficients'.** P-F60 is no longer needed. Tests: complete yes;
  self-contained no (a post must carry P-F23, P-F27, P-F30 with proofs); stable yes as a statement (r = 0 would
  strengthen it); checked once (targeted proof check + computations, one checker); interest high. Gates: literature
  search with Hexagon, the write-up, the reading of every page. The claim stops at the existence clause.
- **H02:** the gate 'the run's final' is passed. The threshold 79,000 and the n = 9 witness go in only with their
  conditions (PNEW002-004; the exterior identity). 'Stronger on test 4' above overstated the witness check.
  P-F56 was confirmed except the part not used, not 'in full'.
- **H21:** say 'polynomial for each fixed b' for G-040 (PNEW010). **H20:** unchanged.

## Round 8: 22 Nov 2026, ~18:1x UTC (main session e0d20ada, Claude Opus 5.5 at effort max; from the intakes and seeds of 22 Nov, Claude Opus 5.5 at effort high)
Each entry names its research-and-paper prompt (TO_SEND/PRO/1_Archive_research_by_topic/ORDER.md). None is cleared for posting: searches, checks and the reading of every page remain.
- **H24 (new, timely): the hypotheses of GCT VI's flip fail** (RH for every m > n >= 2; PH1 as stated on the determinant side; OH with PH1 for m >= n^25). Independent re-proof: reports_20261122/gct_flip/INDEPENDENT_CHECK_a17221e5.md. Prompt 57, with H02 and H02b.
- **H13, H14:** prompt 58. **H03:** prompt 59. **H20 and H21:** prompt 60; H21's "first with varying outer degree" is withdrawn (Pak-Panova-Swanson; Narayanan). **H23:** prompt 61.
- **H25 (new): the Hodge conjecture for abelian varieties is equivalent to bounded cycle degrees** on reductions of CM points, from published inputs (SEED_HODGE_DIVISION; 22 Nov 18:49 UTC: re-proved by Claude Opus 5.5 at effort high, not blind, with one repair: the map comes from a morphism of Shimura data; reports_20261122/hodge_reduction/INDEPENDENT_CHECK.md; prompt 70 placed). H12's bounds become 48 (Gaussian) and 36 (Eisenstein), given cited sources. Prompt 70, with H12 and H19.
- **H18:** now K_4k(Z) = 0 for k <= 20; H06's "p < 1000" and unevaluated constant are superseded. Prompt 65, with H06a and H06b. **H15:** prompt 66.
- **H26 (new): all standard conjectures (Hodge type for product polarizations) and Tate on every power of explicit non-abelian fourfolds in characteristic p.** Prompt 64, with H04 and H11. H04 and J5 are one finding; H11 is only partly conditional.
- **H27 (new): Connes's trace formula with an explicit cutoff is equivalent to GRH over Q.** Prompt 68. **H28 (new): the 3-primary even K-groups of Q(omega, cbrt 269) in every degree, and Artin for Calegari's S5 family under a real-zero hypothesis.** Prompt 69.
- **H29 (new): what Alpoge's GRH makes unconditional in algorithms.** Prompt 67. **H30 (new): the chain length forced by the size hypotheses of Alpoge's proof.** Prompt 73.
- **H31 (new): cotes 136 and 134-8.** Prompt 71. **H32 (new): cotes 15, 123, 133.** Prompt 72. NEG_NIGHT's analytic and geometric candidates: prompts 62 and 63.

## Round 9: 23 Nov 2026, ~11:1x UTC (main session ed7922ad, Claude Opus 5.5 at effort max; from the intakes of 23 Nov by Claude Opus 5.5 at effort high: abcaba9b, af2a18f6, ad855737)
At the user's word ([the user's words, omitted]; [the user's words, omitted]). Intakes in field_experts/intake_20261121/intakes/. None is cleared for posting.
- **H15: the exponent is now 1/(4g)** (NIGHT_AFTER_ALPOGE A.ORBIT: |Gal x| >= c_g D_x^{1/(4g)}, D_x the discriminant of the centre of End(A_x), explicit constants, all centre orders and products; inputs Gaudron-Remond 2023 and Faltings; Alpoge only through the height bound), checked step by step by ad855737. Effective Andre-Oort for A_g in full is Jaswal (Hexagon 2611.00339) with Cureton-Thorner (Hexagon 2610.00200): cited, not claimed. One gate: the literature comparison with Jaswal's orbit bounds and Gaudron-Remond 2023. The strongest candidate of the round.
- **H18: not ready.** Leo Pintar, Hexagon 2611.00829v1 (21 Nov 2026), conditional certificates for k <= 26: read before any post (it may supersede ours). Also the KMSW background gate (Mok, Chaudouard-Laumon, Moeglin-Waldspurger) and the toClassicalTheorems step, now in the run's paper.
- **H06b (Ihara):** the current text is the run's 19-page Ihara paper (NIGHT_AFTER_ALPOGE cp11, papers/ihara/main.tex); confirmed in the Vandiver case; gate: the literature (Sharifi, Fukaya-Kato, Ishii 2026). Post the Vandiver form first.
- **H25 (Hodge):** HODGE_BOUNDED_CYCLES final: Q10 and Q12 checked (abcaba9b); gates: the 70c fixes, the Schoen 2007 input behind the bound 36, a literature search for Q12. Novelty bounded by Cattani-Deligne-Kaplan and Bhattacharjee-Bhattacharya (cited).
- **H27 (Connes):** ALP_CONNES T51 (Connes's trace formula over Q <=> GRH for Dirichlet L-functions) and S50 checked (af2a18f6); gates: the comparison with Connes 1999 section VIII and Connes-Consani-Marcolli, the analytic inputs T25-T43, Suzuki arXiv:2610.32704 for S50.
- **H29 (algorithms):** GRH_ALGORITHMS cp08: P128/P131 (unconditional, polynomial in r, log p and the part of Phi_d(p) prime to 2r) and P126 (from Alpoge, fixed r and r-adic valuation); gates: Bach-von zur Gathen-Lenstra 2001, an independent check of P126's CM-theta proof, the 67c fixes.
- **H30 (chain length):** the theorem stands (abcaba9b); Lean 4.33.1 certifies the numerical part; one gate: the SizesAt bridge, or the statement for the five certified inequalities. The seed's degree convention is corrected (f is the degree of the totally real subfield).
- **Small, not separate rows:** ALP_CONNES G175 (unconditional vanishing for 2-power conductor characters at every l >= 5; gate: a check and Washington's theorem); G185 is routine, not a candidate.
- Board: field_experts/hexagon/HEXAGON_BOARD.tsv (backup HEXAGON_BOARD_before_intakes_20261123.tsv), 56 candidates.

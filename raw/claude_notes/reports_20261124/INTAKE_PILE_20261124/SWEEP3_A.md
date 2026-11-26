# SWEEP3_A: the archive research runs of sweep 3, first half (RESEARCH_SA05-SA10, SA08_C3_D031, SA12)

Cluster reader of the intake pile of 24-25 Nov 2026: Claude Opus 5.5 at effort high, launched by the main session 329fb1e6
(Claude Opus 5.5 at effort max), written 24 Nov 2026. All eight runs are GPT-6 Astra (ChatGPT Pro mode), on prompts built
from the sweep-3 readings of Grothendieck's Montpellier manuscripts. Running notes:
`agent_notes/20261124T2111Z_Intake_pile_sweep_3_first_half_NOTES.md`; my scripts and their outputs:
`agent_notes/sweep3A_20261124_work/`. The return folders are in
`grothendieck_archive_transcription_20261110/research_returns/`; the earlier intakes are in
`results_register/horizontal/sweep3/SA05` ... `SA12` (named per run below).

## Read this first: these runs are not untaken

The ledger (`field_experts/INTAKE_LEDGER.md` §0) shows SA05, SA08, SA09 and SA10 with 0 statements checked, SA07 with 1,
SA06 with 31, SA12 with 49, SA08_C3_D031 with 4. Apart from SA10, that is wrong. On 21-22 Nov every run except SA10 had a
*full* intake, statement by statement, by Claude Opus 5.5 at effort max (agents a7b7747f, a0012f1f, a9224660, ae4ae3dc,
a34c0444, a203d72b, a3c8d7de). Their events, about 1,750 rows, sit in files named `INTAKE_RESEARCH_SAxx_20261121_full*_CHECK_EVENTS.tsv`
(and `_F332_`, `_F3_inputs_`). `results_register/build_check_register.py` matches intake files with the pattern
`^INTAKE_(.+?)_(20\d{6})(?:_part\d+)?_CHECK_EVENTS\.tsv$`. That pattern misses the `_full` and `_full_partN` suffixes, so
these events go into CHECK_REGISTER.tsv **without the run prefix**. SA05's events are also keyed by their event ids
(`SA05F-E001` ...), because the script prefers an `id` column over `statement_id`. I checked this: CHECK_REGISTER.tsv
holds 278 rows from SA05's full file, all keyed `SA05F-E...`. So the "not checked" lists of §9 are wrong for seven of
these runs. The best level reached per statement (from the intakes' own counts) is roughly:
SA05: re-proof 32, computation 9, targeted 114, background 22 of 177;
SA06: re-proof 9, computation 12, targeted 182, background 11, statement only 4 of 218;
SA07: targeted 107, re-proof 28, background 23, computation 9, statement only 19 of 186;
SA08: all 118 have events, 16 statement only;
SA08_C3_D031: all 112, 3 statement or status paragraphs;
SA09: all 43;
SA12: every one of the 438 listed ids has an event (part 1 194 targeted, 16 re-proof; part 2 148 targeted, 66 re-proof).
**SA10 is the exception:** its only intake (19 Nov, a6d42bf6) has 42 events. It checked Part A and parts of B and C.
About 35 of its B and C rows carry only the run's own checks.

The fix belongs to the main session: widen the pattern, and prefer `statement_id` over `id`. My own event files are named
`INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv` and have no `id` column, so they match as they stand. But this pile folder is not
among the script's ROOTS, so the main session has to add it before the register sees my events.

**Nothing new has come back since those intakes.** The newest returns are SA05 final (19 Nov 09:51), SA06 final
(19 Nov 20:52), SA07 cp12 (19 Nov 12:55), SA08 final (19 Nov 10:27), SA08_C3_D031 cp08 (19 Nov 20:43), SA09 final
(19 Nov 11:46), SA10 final (19 Nov 05:40) and SA12 final (20 Nov 23:10). All of them predate the full intakes. What this
file adds:
- the ranking below;
- the cross-run relations;
- 15 new check events, on 8 runs;
- SA10's first outside checks of two B rows;
- the ledger point above.

## The cluster's most interesting items, ranked by usefulness

1. **An excellent Dedekind domain that refutes Grothendieck's conjecture on cd of affine opens** (RESEARCH_SA12,
   A:A2-persistent-arithmetic-counterexample, with A:A2-quadratic-step, A:A2-wreath-calculation and
   A:A2-sharp-curve-consequences).
   - **The statement:** there is an excellent Dedekind domain R of characteristic 0, with 2 invertible and K = Frac R
     algebraic over Q, such that cd_2(K) = 1 while cd_2(U) = 2 for every nonempty affine open U. In fact Pic(U)/2 is
     infinite.
   - **The construction:** a tower of quadratic steps over Q(√−35) with Galois group (V⊕V)⋊C_2. Each step keeps every
     ideal class mod 2 and doubles the 2-rank, and every rational prime eventually becomes inert.
   - **What it refutes:** Conjecture 1° of 31/085 and its margin "égalité pour les ouverts assez petits ?". It does so
     with no real residue field, the obstruction that earlier counterexamples (SGA 4 X 4.5) used.
   - **Related results:** A.2 holds over fields (A:eventual-field). For Z[μ_{p^∞}, 1/p], A.2 is equivalent to Iwasawa's
     μ = 0 for every number field (A:canonical-Iwasawa), which is open beyond abelian fields.
   - **Status:** proved by the run, with a certificate of 111,784 assertions. The cp23 intake (a203d72b, effort max) made
     a targeted check of the proof and re-proved the wreath lemma; I checked the class-group step.
   - **Gate:** a literature search for an existing persistent Pic/2 example.
   - **Where:** `parts/A/quadratic_tower_A2_post05.tex`.
2. **A wild quasi-étale double cover above one smooth genus-two exceptional curve** (RESEARCH_SA12,
   D:wild-genus2-single-curve, rows 433-435).
   - **The example:** in characteristic 2, S: b² + (t⁵ + t²a²)b + a⁵ = 0 has an isolated Gorenstein singularity. Its
     resolution has one exceptional curve C: y² + y = x⁵, of genus 2, with C² = −1 and discrepancy −3. The double cover
     T is étale off the point and wild along C: e = 1, the residue extension is purely inseparable of degree 2, and the
     different exponent is 1.
   - **What it shows:** the graded-cone tameness theorem (D:graded-cone-tame) needs its formal-linearity hypothesis. The
     weighted-homogeneous germ with the same resolution graph has only tame covers.
   - **Status:** proved by the run. The full intake (a3c8d7de, effort max) re-proved it and reran the certificate. I
     verified it again with my own script over F₂ (`sa12_wild_genus2.py`); every polynomial identity, chart, singular
     locus and the involution hold.
   - **Gate:** the literature search found no such example. The one paper left to read is Cutkosky-Srinivasan, Comment.
     Math. Helv. 68 (1993); the intake could not reach its text.
   - **Where:** `parts/B/D_wild_genus2_curve_B.tex`.
3. **Every abelian surface with an ample line bundle of odd Euler characteristic is a direct summand of a product of
   Jacobians, in every characteristic** (RESEARCH_SA06, C.4n; with C.4i, C.4j, C.4m, C.4p and the residual cases C.4q-x).
   - **The statement:** s_J(A) divides gcd(2, δ(A)) for abelian surfaces and gcd(6, δ(A)) for abelian threefolds, where
     s_J is the least n such that [n] factors through a product of Jacobians and δ(A) = gcd χ(L).
   - **The method:** the unimodular Poincaré bundle on A×Â, Matsusaka's identity, and Beauville's generalized Pryms
     (j*Θ = 2Ξ in dimension 4 and 5), lifted to characteristic 2.
   - **Why it matters:** this is the integral question behind 14:69-71. It meets the 2023-2026 literature on integral
     Hodge classes of curve type on abelian varieties (Beckmann-de Gaay Fortman, Scavia-Suzuki, Voisin,
     Engel-de Gaay Fortman-Schreieder).
   - **Status:** proved by the run. The full intake (a0012f1f, effort max) re-proved C.4i, C.4j, C.4n and C.4p. I made a
     targeted check of C.4i, C.4m and C.4n and verified the interpolation step by computation (`sa06_c4n.py`).
   - **Gate:** a literature search.
   - **Where:** `agents/frobenius/C4_additions.tex`, `C4_prym_addition.tex`, `C4_pt6_addition.tex`.
4. **A published theorem is false: Bhowmik-Pathak, arXiv 2408.00271v1, Theorem 1.11** (RESEARCH_SA07, G.2.2).
   - **The theorem:** trdeg Q̄(e^{2πiτ}, f(τ), g(τ), f̃(τ)) ≥ 3 for a modular form f, a modular function g and a
     quasi-modular f̃ of depth at least 1.
   - **The counterexample:** at τ = i, f = E₄, g = j and f̃ = E₄ + E₂E₆/E₄, one has E₆(i) = 0, so f̃(i) = E₄(i) and the
     field is Q̄(e^{−2π}, Γ(1/4)⁸/π⁶), of transcendence degree 2. With the weight-0 reading f̃ = 1 + E₂E₆/E₄², f̃(i) = 1
     and the same failure.
   - **The failing step:** the first displayed equality of their proof (source `AAfinal.tex`, l. 900-903). Only "≤"
     follows from what precedes it.
   - **The repair:** require f_r(τ) ≠ 0 for some r ≥ 1 in f̃ = Σ f_r E₂^r.
   - **Status:** confirmed against the v1 LaTeX by a922466 (effort max). I confirmed it again, against the printed
     statement and by 40-digit numerics (`sa07_g22.py`).
   - **Next step:** a note to the authors. The source file is named "AAfinal", so the Acta Arithmetica version may carry
     the error; the 23-page journal text has not been checked.
5. **A false lifting proposition in a 2025 preprint: Caradot-Lin, arXiv 2511.22614v4, Prop. 3.10** (RESEARCH_SA08
   D-031, confirmed by RESEARCH_SA08_C3_D031 B-001).
   - **The counterexample:** a termwise-free chain map into a square-zero PD dg algebra, through a surjection that is
     termwise onto on the ideals, has no lift. Take E^{−2} = ku, E^{−1} = kv with du = v, mapped to kε. A lift would
     need c = 1 and c = 0 at once.
   - **Scope:** Theorem 3.15, with its acyclic-target hypothesis, is unaffected. The corrected criteria B-003 and B-004
     ask for contractible or K-projective X.
   - **Status:** the 20 Nov intake checked it against v4. I re-proved it by hand.
   - **Next step:** a note to the authors (outreach plan).
6. **The complete table for local restriction of algebraically trivial cycles on strict-local punctures** (RESEARCH_SA06,
   C.3f-C.3bw; the headline rows are C.3ak and C.3ap).
   - **Over C:** for r ≥ 2, restriction is universally injective iff N ≤ r and universally surjective iff N ≤ r + 1. For
     r = 1, it is injective iff N = 1 or N ≥ 3 and surjective iff N ≤ 2. Every other dimension has an explicit
     counterexample.
   - **In characteristic p:** the integral p-torsion kernels, and rational top vanishing over F̄_p for every excellent
     local domain (C.3be).
   - **Why it matters:** it answers Grothendieck's local Lefschetz questions of 14:106-109, close to Kollár's local
     Picard theory.
   - **Status:** targeted checks by a0012f1f in round 2. Some rows were read only in part: C.3bl's auxiliary
     proposition, C.3bt's totalization file, and C.3bu-bw at statement level.
   - **Gates:** finish those reads, and a literature search. The rational top quotient in characteristic 0 is open.
7. **The 1965 letter's conjectures modulo algebraic equivalence, exactly** (RESEARCH_SA06, C.1f, C.1j, C.1k, with C.1b).
   - **Over C:** "A" holds universally exactly for i = 0 or 2i = n (C.1f). The middle "B" is equivalent to injectivity of
     L on the middle rational Griffiths group (C.1j). Cycle-class injectivity, finite rank and finite generation hold
     universally exactly in codimensions 0, 1 and n (C.1k).
   - **Status:** C.1j and C.1k re-proved by a0012f1f; C.1f had a targeted check.
   - **Gates:** read C.1g, the explicit generic quintic, and a literature search. This is the precise answer to
     Grothendieck's letter (14:44-47; printed letter pp. 232-234).
8. **The CM common-kernel assertion of LM6 A.22, settled in the run** (RESEARCH_SA07, F.3.32, with F.3.20-F.3.34).
   - **The statement:** for X₀ = E₀∖{O} with E₀: y² = x³ − x, every nontrivial closed procyclic subgroup of the geometric
     π₁ whose arithmetic normalizer has open image lies in a conjugate of cusp inertia. Hence no such subgroup lies in the
     intersection R of the kernels to the pro-ℓ completions.
   - **The core:** an all-genus Lie-algebra identity, N₀M₇ = d₀LK in Q[s], with d₀ = 9(2s+3)(4s²+6s−1) > 0.
   - **Status:** ae4ae3dc (effort max) reran the exact certificate and checked F.3.31, F.3.34, Nakamura 1995 (4.3)-(4.4)
     and Hain 1997 against the sources. Not checked outside the run: the arithmetic reduction's use of Nakamura 1996
     pp. 115-117 (only cited statements were checked) and F.3.33 (the general affine hyperbolic curve).
   - **Who should take it:** the Longue Marche expert ae4ae3dc. It closes one half of an open item of LM6_POINTS_AS_SECTIONS.
9. **Grothendieck's birational invariance of Pic^τ in characteristic p, and R¹f_*O_X = 0 without resolution** (RESEARCH_SA12,
   B.1 and L6c; with B.2/B.2u).
   - **The statements:** R¹f_*O_X = 0 for every proper birational f from a normal to a regular noetherian scheme in
     characteristic p (L6c). Pic^τ pullback is an isomorphism for X normal and Y regular proper (B.1, 29/071). h¹(O) is
     bounded over all normal models, with weak upper-cone stabilization over every field (B.2u). The cofinal constant form
     is refuted over an imperfect field (B.2q).
   - **Status:** the cp23 intake re-proved L6c; the full intakes made targeted checks of the B.2 chain.
   - **Gates:** a literature search (Chatzistamatiou-Rülling cover the smooth case). For B.1, the published status of
     purity for finite flat torsors: the run cites "Marrama2026", which no one has opened.
10. **No filtered numerical lift of the divided-power cochains** (RESEARCH_SA08, A-026; with A-023 and A-024).
    - **Part 1:** over R = Int(Z), every filtration-preserving R-bilinear map M₁⊗M₁ → M₂ with gr M_i = I_i (the PD tails)
      is zero.
    - **Part 2:** no natural, exhaustive, filtered numerical cochain algebra has the weighted PD cochains as associated
      graded, derived and E_∞ models included.
    - **Status:** part 1 was re-proved and computed by the 19 Nov intake (a34c0444, effort max), and part 2 checked
      there. I made a targeted check of part 1.
    - **Gate:** a literature check against Horel and Kubrak-Shuklin-Zakharov. It bears on integral models of homotopy
      types through binomial rings (cote 136).
11. **The transcendence of the Hodge splitting, 18:11, decided in corrected form** (RESEARCH_SA07, A.2.2-A.2.6).
    - **The invariant:** v = dim N₂ − dim(N₂ ∩ B⁻) of the joint torsor of M ⊕ c*M gives the full table of image
      dimensions.
    - **The verdict:** Grothendieck's "Conj. de transcendance forte" list is the period-conjecture prediction exactly when
      v = u. Five of its values are false unconditionally when v < u, explicitly for h¹ of y² = x³ − x + 1 over Q (A.2.6).
    - **Related:** a non-computable polarized Hodge pair outside the geometric image (C.1.5), and the p-adic analogue of
      18:13 c, false for ordinary curves (A.4.21).
    - **Open:** two hard transcendence gates (A.3, A.4c).
    - **Status:** the 20 Nov intake checked these rows.
    - **Use:** companion material for cote 18; C.1.5 is a Hexagon candidate after a literature search.
12. **The gluing of tubes, 151/069, corrected** (RESEARCH_SA10, A1.2-A1.5, B2.2, B6.1).
    - **What fails:** his stones do not glue, neither the successor stones nor all pair and triple stones (A1.3; ℂ ⊃ ℝ ⊃
      {0}). They fail at the level of homotopy types too (the 19 Nov intake, E42).
    - **The correct theorem (A1.2):** tubes are pro-objects, glued by the Čech diagram of degrees 0-2 along their actual
      overlaps.
    - **The rest:** van Kampen holds for ∞-topoi and fails for ordinary topoi (B2.1, B2.2). The 151/017 presentation of
      the category of nonempty finite sets misses a relation (B6.1).
    - **Status:** I re-proved B2.2 and B6.1, the first checks of those rows outside the run.
    - **Use:** the cote 151 companion chapter.
13. **The explicit global class of Grothendieck's motivic gerbe over F_p** (RESEARCH_SA05, A:class with A:hasse,
    A:compacthasse and A:valuations).
    - **The statement:** Ш²(Q, H⁰) = 0 for the compact protorus H⁰. The class ξ₀ = (a_p, b_{p,∞}): a_p is the
      p-adic functional m ↦ v_p(m) mod Z, of infinite order; b_{p,∞} is the quaternion class ramified at p and ∞.
    - **Cross-run:** SA06 D.3b proves the infinite order of the Artin- and Tate-rigidified motivic gerbe class over F_q,
      by a different route.
    - **Status:** re-proved in parts by a7b7747f; I made a targeted check of A:class.
    - **Gate:** a literature search, since Milne 2003 and the Langlands-Rapoport literature may compute it.
14. **The integral Weil-étale table of 15:173 is off by Z/2, found by two runs independently** (RESEARCH_SA05
    prop:B-integral-errors and thm:B-SpecZ-Q; RESEARCH_SA06 E.4b and E.4g).
    - **The correction:** in Flach-Morin's theory, H¹_W(Spec Z̄, Z(1)) = Z/2 and H³_W(Spec Z̄, Z) = Z/2. Grothendieck's
      table omits both.
    - **The rational table survives:** it has Borel's ranks, matching the orders of the trivial zeros of ζ.
    - **Agreement:** both runs, on different prompts, give the same values.
    - **Use:** a companion correction for 15:173.

Below these: SA12 D:boundary-neighborhood (the one-point case of D.2(ii) for non-projective X), SA05 c:general-level-bound
(the answer to the margin question of 12:120), SA09 B3.1 (the cellwise holomorphic groups of clean dessins), and the
many archive corrections of each run. The runs list them, and the intakes' sections "Implications" carry them by cote.

---

## RESEARCH_SA05 — "Théorie des motifs I" (cotes 15, 12, 11)

Return: `RESEARCH_SA05_final_INCOMPLETE_20261119T0951Z_unzipped` (report opens INCOMPLETE; 177 statements). Intakes:
`SA05/INTAKE_RESEARCH_SA05_20261119.md` and `..._20261121_full.md` (a7b7747f, Claude Opus 5.5 at effort max).

1. **Useful: yes, moderately.** It works out what Grothendieck's motivic gerbe over F_p actually is, with its band, its
   global class and the Hasse principle, and it corrects a series of his statements and of ours. The larger B and C
   programmes (Weil-étale over Z, tautological rings, levels) are mostly conditional reductions.
2. **What it proved:**
   - A:band and A:P: the band is a compact protorus, not a torus.
   - A:compacthasse and A:hasse: Ш²(Q, H⁰) = 0 and H²(R, H⁰) = 0. For finite v, H²(Q_v, H⁰) = Hom(M^{G_{Q_v}}, Q/Z).
   - A:class: the class ξ₀, with its explicit local components; a_p has infinite order.
   - A:comparison: the strict H/G equivalence is refuted, by component groups.
   - prop:B-continuity: continuity is incompatible with 12:65's vanishing over F̄_q.
   - prop:B-integral-errors: corrects 15:173.
   - thm:B-SpecZ-Q: all rational twists on Spec Z̄.
   - c:level-counterexample and c:general-level-bound: the corrected weight-level bound. Its margin answer: n − 1 is
     right exactly when f has relative dimension ≤ n − 1 near y.
   - c:modified-diagonal: the class lives in H^{4n}, not H^{2n}.
   - thm:d-reflex-image: the image torus of ψ_Σ (15:151).
   - prop:d-metabelian-false: an S₄ Artin counterexample.
   - Checks: a7b7747f made 32 independent re-proofs, 114 targeted checks and 9 computations, and refuted nothing. Mine:
     A:class (targeted).
3. **New since the last intake:** nothing in the run; my one event.
4. **Open:**
   - B.1: under universal Tate and semisimplicity, the comparison reduces to injectivity of CH^m(X)_Q → H^{2m} for
     dim X = 2m − 1. The first case is codimension 2 on threefolds (prop:B-diagonal-Chow-gate).
   - B.3: universal finiteness is undecided.
   - C.1(c): the K3 transcendental gate, and the C.4 higher endpoint.
   - C.6: the general case.
5. **Relations:**
   - SA06, on the same cotes 14-15, agrees on 15:173 (E.4b, E.4g) and on the infinite-order gerbe class (D.3b).
   - Literature: Milne 1994 and 2003; Kisin 2017; Langlands-Rapoport; Flach-Morin 2018; Borel 1974.
   - Grothendieck's frameworks: motives over finite fields, weights, Weil numbers, the Tate conjecture.
6. **Candidates:**
   - Hexagon, later: A:class with A:hasse, gated by a literature search.
   - Source corrections, unchecked against the sources: Keller Lemma 2.17 (rem:B-Keller-closure-error; the counterexample
     is valid) and Kerr-Yang §4D.
   - Next prompt: the codimension-2 Chow gate on threefolds, if B.1 is wanted.
7. **Problems:**
   - Seven statements rest on unrefereed 2026 preprints: van Hoften-Sempliner's exposition of OpenAI's CM Hodge
     preprint, OpenAI's "Milne's rationality conjecture", Ito-Zou, Balkan-Schreieder, Colliot-Thélène-Schreieder.
   - The report's outcome table says, at A.1(a), "abelian part now unconditional via cited CM theorem". That holds only
     as long as the preprint holds, and should say "conditional on".
   - Our errata: R8's degree and the D.1 Frobenius wording.

## RESEARCH_SA06 — cycles, effectivity and Frobenius (cotes 14, 15)

Return: `RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped` (246 statements; ~50 agent files). Intakes:
`SA06/INTAKE_RESEARCH_SA06_20261120.md` (a0012f1f with aaece8bf, Claude Opus 5.5 at effort max and high) and
`..._20261121_full.md` (a0012f1f, effort max, two rounds).

1. **Useful: yes, the most useful run of the cluster after SA12.**
   - Three bodies of work are publishable after a literature search: the Jacobian summands (C.4), the local restriction
     tables (C.3) and the letter conjectures (C.1).
   - Explicit objects of narrower interest: a noncommutative π₀ for the Deuring categories over F₉ (A.5c); an abelian
     threefold over F₂ carrying (3 + √−23)/2 on H³ (B.3b).
2. **What it proved:** items 3, 6, 7 and 14 above, and:
   - E.3e: Theorem 3.1 of 14:38 in every positive characteristic, with the integral premise.
   - E.3u: its converse fails over C even rationally (Walker's phenomenon, made explicit).
   - E.2e: 14:3's "nb fini de types de motifs effectifs" is false for the full category; it holds per finite lattice.
   - B.1a: the "conjecture forte" of 15:100-106 holds in every weight (Milne 1994).
   - D.3b: the infinite-order rigidified gerbe class.
   - Checks: a0012f1f made 9 re-proofs, 12 computations and 182 targeted checks, and refuted nothing. Mine: C.4i, C.4m
     and C.4n (targeted, with computation).
3. **New since the last intake:** nothing in the run; my three events.
4. **Open:**
   - C.3: the rational top quotient in characteristic 0.
   - C.4: the generic End = Z surfaces with δ even, and supersingular threefolds in characteristics 2 and 3.
   - C.1g: statement level only.
   - E.4: an integral all-twist Weil-étale theory is obstructed (E.4d, E.4j-m).
5. **Relations:**
   - SA05, as above.
   - SA14_SA19: Picard and Jacobians, cotes 43-44. Its J5 refutes his Th. 5 in codimension 2; that is a different
     question.
   - Literature: Clemens 1983, Griffiths 1969, Beauville 1977, Mumford 1970 §23, Oort-Ueno 1973, Scavia-Suzuki 2025,
     Kollár on local Picard groups, Walker 2007, Bloch 1979.
   - Grothendieck's frameworks: the standard conjectures, Lefschetz type B, algebraic against numerical equivalence.
6. **Candidates:**
   - Hexagon: C.4 (tests 1, 2 and 4 pass; gate: literature); C.3 (gates: the partial reads and literature); C.1 (gates:
     C.1g and literature).
   - Next prompt: none needed for C.4. A short follow-up would cover the C.3 partial rows.
7. **Problems:**
   - Erratum in C.3ae: `agents/cycles/higher_local_surjectivity.tex` Step 4 prints the Fermat Jacobian ring without
     w₃³. The stated dimensions 16 and 19 are those of the correct four-generator ring.
   - D.4d-D.4g rest on an unrefereed 2026 preprint.
   - STUDY.md §1 still calls the "conjecture forte" open.

## RESEARCH_SA07 — periods, real Frobenius and the integral image (cote 18, with 15:195-228)

Return: `RESEARCH_SA07_checkpoint_12_20261119T1255Z_unzipped/RESEARCH_SA07` (cp12, INCOMPLETE; 186 statements). Intakes:
`SA07/INTAKE_RESEARCH_SA07_20261120.md` and `..._20261121_full.md` (a9224660, Claude Opus 5.5 at effort max);
`..._20261121_F332.md` and `..._20261122_F3_inputs.md` (ae4ae3dc, effort max).

1. **Useful: yes.**
   - It decides 18:11 in corrected form.
   - It corrects a published theorem (G.2.2).
   - It closes a Longue Marche open item in the run (F.3.32).
   - Its integral-comparison counterexamples are clean: D.5.2, a CM obstruction over Q(√−5) with O against I; E.1.2 and
     E.2.1, places that no integral test separates.
2. **What it proved:**
   - Items 4, 8 and 11 above.
   - Twelve refutations of statements on the pages, all confirmed by a9224660: B.1.3, B.4.4, D.5.2, D.5.3, E.1.2, E.1.3,
     E.2.1, E.3.3, E.3.4, F.3.7, F.3.11 and G.2.2.
   - A.4.31: the restricted-Lie formula, certified for p = 5, 7, 11.
   - E.2.19-E.2.31: the integral-image constructions, read in full in round 4.
   - Checks: a9224660 made 107 targeted checks, 28 re-proofs and 9 computations, leaving 19 rows at statement level, all
     in the F.3 chain except D.6.1. ae4ae3dc covered the F.3.32 chain. Mine: G.2.2 (re-proof against the printed
     source).
3. **New since the last intake:** nothing in the run; my G.2.2 event.
4. **Open:**
   - The run stopped at cp12.
   - A.3: trdeg of τ, τ̄ for a curve not isogenous to its conjugate (1 ≤ trdeg ≤ 2).
   - A.4c: the non-CM value of h in 18:13 c, which is the period conjecture itself.
   - F.3.33: the general affine curve.
   - The arithmetic form of H2.
5. **Relations:**
   - LM6_POINTS_AS_SECTIONS A.22 (F.3.32).
   - SA15: G.2.1 and G.2.3 agree with its files.
   - Lead H4: the reconstruction question already appears in the May 1966 letter to Tate (cote 6), so 18:5 is not its
     earliest written form. This rests on a quotation still to be checked against the cote-6 transcription.
   - Literature: Kreutz-Shen-Vial 2026, Nesterenko 1996, Bost 2001, Herblot, Bost-Chambert-Loir 2008, Nakamura
     1994/1995/1996, Hain 1997.
   - Grothendieck's frameworks: periods and motivic torsors, the anabelian program.
6. **Candidates:**
   - Outreach: the G.2.2 note to Bhowmik-Pathak, after checking the journal version.
   - Hexagon: C.1.5, the non-computable Hodge pair, after a literature search.
   - Routing: F.3.32 to the LM expert.
   - Next prompt: a successor of SA07, for A.3 and F.3.33.
7. **Problems:**
   - Two transcription hazards in Spence 2018, Masser's formula (A.4.5).
   - Our R2 converse is false (C.3.1).
   - Our R5 and the sweep-3 event at 18:9: line 14 is off by 2 (F.2.1).

## RESEARCH_SA08 — the divided-power de Rham complex (cote 136)

Return: `RESEARCH_SA08_final_20261119T1027Z_unzipped` (118 statements). Intakes: `SA08/INTAKE_RESEARCH_SA08_20261119.md` and
`..._20261121_full.md` (a34c0444, Claude Opus 5.5 at effort max).

1. **Useful: yes, for integral homotopy theory.**
   - A-026, item 10, is the theorem.
   - The rest answers cote 136 (scans 11-12, 117-121, 174-182, 273, 360, 374-376) precisely: the PD cochains recover
     RΓ(X, Z) and the E_∞ algebra (D006, D006E); no Steenrod squares (B-08, B-10); L4 is false (B-07).
2. **What it proved:**
   - A-001 to A-009: the literal and graded answers to A.1.
   - A-026.
   - B-01 to B-17: the automorphism group Ω.
   - C17: the finite-prime case of the uniqueness conjecture.
   - D013-D021: the Breen comparison, with the missing +1.
   - D-031: Caradot-Lin.
   - Checks: a34c0444 made 26 re-proofs and 68 targeted checks; 16 bar and repair rows are statement only. Mine: A-026
     (targeted).
3. **New since the last intake:** nothing in the run; my one event.
4. **Open:** C.3, his uniqueness conjecture over Z in its groupoid form; the strict form fails (C07). It continues in
   SA08_C3_D031.
5. **Relations:**
   - SA09 A3.3 and SA08 A-018/D006M recover the same homotopy type.
   - SA09 A3.5 is the elementary relative of A-026.
   - Cartan 1976 §7, credited by the run.
   - Mandell 2006, Horel, Toën, Breen 1978.
   - Grothendieck's frameworks: crystalline cohomology and PD structures, schematic homotopy types.
6. **Candidates:**
   - Hexagon: A-026 (gate: a literature check).
   - Outreach: D-031 to Caradot-Lin.
7. **Problems:** none in the mathematics. The register calls A-016 "Refuted" where its paper proves a nonexistence
   theorem. Breen and Mandell were not opened by any intake.

## RESEARCH_SA08_C3_D031 — C.3 over Z, and the Caradot-Lin check

Return: `RESEARCH_SA08_C3_D031_checkpoint_08_20261119T2043Z_unzipped` (cp08, INCOMPLETE; 112 statements). Intakes:
`SA08/INTAKE_RESEARCH_SA08_C3_D031_20261120.md` and Part II of `INTAKE_RESEARCH_SA08_20261121_full.md` (a34c0444, effort
max).

1. **Useful: marginal**, apart from B-001.
   - Most rows are steps of an integral repair construction toward an open question.
   - The PD cotangent complex of Γ_Z(T)/I_N has unbounded prime-local support for every N ≥ 2 (A-S09-09 to A-S09-12,
     given Fu-Nuiten Thm C). That is a small, possibly interesting fact.
2. **What it proved:**
   - B-001: Caradot-Lin Prop. 3.10 is false.
   - B-003 and B-004: the corrected lifting criteria.
   - AT11, AT12 and AT28: obstruction classes, and the refutation of the arithmetic-completion route.
   - A-L20 and A-L21: the period residues vanish at every odd prime.
   - Reductions of both main questions to smaller gates: A-S09-24, -27, -29, -30.
   - Checks: a34c0444 made 92 targeted checks, 10 re-proofs and 5 computations. Mine: B-001 (re-proof).
3. **New since the last intake:** nothing; my one event.
4. **Open:** A-CS (common sources) and A-TL (terminal localization) over Z, now reduced to at most three disks per weight
   and to countable objects.
5. **Relations:** RESEARCH_SA08 (C30, C32, C34 sharpened); SA09 (A2.2, A3.1 and A3.2 re-proved). Literature:
   Nagpal-Snowden, Fu-Nuiten, Bhatt-Lurie-Mathew, Kubrak-Shuklin-Zakharov.
6. **Candidates:**
   - Outreach: B-001.
   - Possibly Nagpal-Snowden: A-L14 says the uniqueness sentence in the proof of their Thm 7.1(a) fails for a zero
     restriction. The theorem itself is unaffected, and the wording has not been checked against the source.
   - No next prompt unless C.3 over Z is wanted.
7. **Problems:** an erratum in (AL.110) of `B_p3_second_repair.tex` and (AL.124) of `B_odd_prime_second_repair.tex`. They
   print dl = −ur + tσ; it should read dl = −ur + t^{p−1}σ. No result uses dl.

## RESEARCH_SA09 — polynomial categories (cote 137) and maps and Galois action (cote 138)

Return: `RESEARCH_SA09_final_20261119T1146Z_unzipped/RESEARCH_SA09` (43 statements; a 43-minute run). Intakes:
`SA09/INTAKE_RESEARCH_SA09_20261119.md` and `..._20261121_full.md` (a34c0444, effort max).

1. **Useful: marginal.**
   - It gives precise corrections of Grothendieck's axioms with classical tools:
     - A1.3: L1 conflates polynomial laws with Γ^d P;
     - A1.5-A1.8: the failures of his ⊗-pd axioms and their comonad repair;
     - A2.2-A2.5: the essential image over all rings.
   - It confirms Schneps' sextic over Q(∛2) (B2).
   - It lists the cellwise holomorphic groups of clean dessins (B3.1), which may be new but are of weak interest.
2. **What it proved:** every item proved or refuted. a34c0444 made 10 re-proofs and 7 computations. Mine: A3.4, the lens
   spaces L(5,1) and L(5,2), re-proved.
3. **New since the last intake:** nothing; my one event.
4. **Open:** nothing.
5. **Relations:**
   - SA08: A3.3 against A-018, and A3.5 against A-026.
   - SA08_C3_D031 re-proves A2.2 and A3.1-A3.2.
   - Literature: Roby, Friedlander-Suslin, Dold-Puppe, Schneps 1994.
6. **Candidates:** none for Hexagon; B3.1 only after a literature search.
7. **Problems:** brisk proofs from the short run. A1.7's equivalence of categories is asserted in two sentences, and the
   B3.1 and B4.4 classifications rest on short proofs.

## RESEARCH_SA10 — the gluing of tubes and the stratified homotopy hypothesis (cotes 150-151)

Return: `RESEARCH_SA10_final_20261119T0540Z_unzipped` (74 statements; complete, no open item). Intake:
`SA10/INTAKE_RESEARCH_SA10_20261119.md` (a6d42bf6, Claude Opus 5.5 at effort max), **the only one: no full intake.**

1. **Useful: yes for the companion, marginal for the field.**
   - A1.2 is elementary open-cover descent once the right cover is written down. Its value is the two counterexamples
     and the right formulation.
   - C5.08 settles the TOP, PL and smooth margins of cote 150.
   - L4 confirms EXIT_TOWER A.2 independently: conditional infima exist exactly for g = 0 (n ≥ 3), g = 1 (1 ≤ n ≤ 3) and
     (g, n) = (2, 0).
2. **What it proved:**
   - A1.1-A1.5: the main question.
   - A4.3: the Corollary of 151/052-053 is false; the cartesian-meet repair.
   - B2.1 and B2.2: van Kampen for ∞-topoi, and its failure for ordinary topoi.
   - B4.3: Hopf S³ against S²×S¹; coherence is needed.
   - B6.1-B6.3: presentations of the nonempty finite sets.
   - C2: π-control must be an axiom; his "donc" on 150/065 is the gap.
   - C3.03: coarse moduli spaces of curves are not manifolds with corners.
   - C5.01-C5.08.
   - Checks: the 19 Nov intake made 42 events, all "holds". Mine: B6.1 and B2.2, both re-proved, both rows unchecked by
     any intake before.
3. **New since the last intake:** my two events.
4. **Open:** no mathematical item. The ink stays unresolved at the subscript of 151/005, the index in (10) of 151/060
   and the bound on 151/060; each is settled for every reading.
5. **Relations:**
   - EXIT_TOWER A.2.
   - Literature: Lurie HTT 7.1.6.15 and HA A.9; Quinn 1988; Treumann; Grandis 2001; Albin 2016; Looijenga.
   - Grothendieck's frameworks: stratified spaces and the "tame topology" of the Esquisse, the Teichmüller tower.
6. **Candidates:**
   - The companion chapter on 151.
   - A full intake of B and C if the companion will cite them. Rows checked by the run only: C1.B1-B3, C4.05, C4.06,
     C5.05, B4.2, B5.6 and B5.10, and B3.1's induction.
7. **Problems:** none found.

## RESEARCH_SA12 — the cd of affine schemes and π₁ (cotes 29, 31)

Return: `RESEARCH_SA12_final_INCOMPLETE_20261120T2310Z_unzipped` (487 statements). Intakes:
`SA12/INTAKE_RESEARCH_SA12_20261120.md` (cp23; a203d72b, Claude Opus 5.5 at effort max) and `..._20261121_full_part1.md`
(a203d72b) and `_part2.md` (a3c8d7de, effort max).

1. **Useful: yes, the strongest run of the cluster.** Items 1, 2 and 9 are real theorems in étale cohomology and the
   theory of singularities. The C-part separates 29/139 (false) from 29/141 (true as written).
2. **What it proved:**
   - Part A:
     - the counterexamples to A.1-A.7: A:realcone; A:mixedreal; A:nagata-* after Gabber; A:double-trait;
       A:wild-affine-counterexample, H³ ≠ 0 for Spec W(F̄₂)[[t]][1/t], conditional on the Kato-filtration locators;
     - A.2 over fields (A:eventual-field);
     - the exact Milnor-K criterion for Dedekind domains (A:Dedekind-Milnor-criterion);
     - A:canonical-Iwasawa.
   - Part B: B.1, L6c, B.2u and B.3a (the rank formula fails at ℓ = p).
   - Part C: C:literal-141 and C:normal-counterexample.
   - Part D:
     - known answers identified for 29/041 (Orgogozo), 29/098 (Schmidt), 29/116 (Deligne) and 29/180 (Rydh);
     - the projective case of 29/061 and 29/066;
     - D:boundary-neighborhood;
     - a large D.1 programme.
   - Checks: the full intakes gave every listed id an event. Mine: D:wild-genus2-single-curve (computation and targeted
     check) and one step of A:A2-persistent-arithmetic-counterexample.
3. **New since the last intake:** nothing in the run; my three events.
4. **Open:**
   - D:fixed-boundary-gate: D.1 for proper non-projective X in characteristic p, reduced to boundaries with no
     quasi-projective neighbourhood.
   - A:canonical-Iwasawa: equivalent to μ = 0, open for non-abelian fields.
5. **Relations:**
   - SA14_SA19 (Picard and Jacobians).
   - Literature: Gabber's 2015 IHES lecture; ILO Exp. XVIII_B; Kato and Suzuki 2024; Chatzistamatiou-Rülling;
     Raynaud 1970; Artin 1975/1977; Lorenzini-Schröer; Carvajal-Rojas-Schwede-Tucker; Cutkosky-Srinivasan 1993;
     Ferrero-Washington.
   - Hexagon: Kisin's note on the Artin character (28 Oct 2026), the nearest existing item.
   - Grothendieck's frameworks: étale cohomological dimension (SGA 4), Pic^τ (FGA, SGA 6), tame π₁ (SGA 1).
6. **Candidates:**
   - Hexagon: items 1 and 2 (one literature gate each); L6c; D:boundary-neighborhood (gates: an independent re-proof and
     literature).
   - Next prompt: the D.1 gate, if wanted.
7. **Problems:**
   - Register rows 388, 390, 400, 405, 423 and 426 list themselves among their own dependencies.
   - A:canonical-Iwasawa has kind "conjecture" and status "Proved": it is a proved equivalence, not a proof of μ = 0.
   - L6c and B.1 cite "Marrama2026", unopened.
   - A:wild-affine-counterexample is conditional on the cited filtration theorems.

---

## My check events (24 Nov 2026), all in this folder

| File | Statement | Type | Outcome |
|---|---|---|---|
| `INTAKE_RESEARCH_SA12_20261124_CHECK_EVENTS.tsv` | D:wild-genus2-single-curve | computation; targeted proof check | holds |
| same | A:A2-persistent-arithmetic-counterexample | targeted (class-group step only) | holds |
| `INTAKE_RESEARCH_SA07_20261124_CHECK_EVENTS.tsv` | G.2.2 | independent re-proof against the printed source | holds: the source theorem is false |
| `INTAKE_RESEARCH_SA06_20261124_CHECK_EVENTS.tsv` | C.4n, C.4m, C.4i | targeted (with computation for C.4n) | hold |
| `INTAKE_RESEARCH_SA10_20261124_CHECK_EVENTS.tsv` | B6.1, B2.2 | independent re-proof | hold |
| `INTAKE_RESEARCH_SA08_20261124_CHECK_EVENTS.tsv` | A-026 (part 1) | targeted | holds |
| `INTAKE_RESEARCH_SA08_C3_D031_20261124_CHECK_EVENTS.tsv` | B-001 | independent re-proof | holds |
| `INTAKE_RESEARCH_SA09_20261124_CHECK_EVENTS.tsv` | A3.4 | independent re-proof | holds |
| `INTAKE_RESEARCH_SA05_20261124_CHECK_EVENTS.tsv` | A:class | targeted | holds |

I found nothing wrong in anything I checked.

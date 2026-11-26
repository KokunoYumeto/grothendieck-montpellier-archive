# Intake: VPVNP_HINGE (run 98), final checkpoint 12 (25 Nov 2026, 04:59 UTC)

By Claude Opus 5.5 at effort max, agent a5ef71dd, a copy of af3258db, which did the gate-1 check. Written for the pequalnp
session 672ae3a0. Run 98 is GPT-6 Astra (ChatGPT Pro mode); its records say "effort not exposed by runtime".
- Return: `grothendieck_archive_transcription_20261110/research_returns/VPVNP_HINGE_checkpoint_12_20261125T0459Z_unzipped`.
- Prompt: `TO_SEND/PRO/1_Archive_research_by_topic/SENT/98_VPVNP_HINGE/PROMPT.md`.
- Spot checks: `INTAKE_VPVNP_HINGE_20261125_CHECK_EVENTS.tsv`, beside this file.

**Notation.** (H_A) is Anthropic's Theorem A.6 (cover duality) together with its Proposition C.3 (the price-space
embedding), from hexagon:2611.00954.

## Most interesting items, ranked by usefulness

1. **The hinge in exact form, checked by a different model.**
   - **SH-08:** a strict shortening exists ⟺ flatness fails, under (H_A).
   - **PG-CROSSPOLY-GATE:** for each fixed D, the D-cross-polytope is a price ⟺ there is no D-shortening ⟺ all finite
     D-configurations are prices. At D = 2 this is the square.
   - **PG-SQUARE-GATE:** the square is a price ⟺ some non-tree price exists, under C.3.
   - Gate 1 (`pequalnp_work/square_note/GATE1_CHECK_20261125.md`) found no fault in any of the three. This is the
     backbone of the square note.
2. **SH-60b, unconditional, over every field:** no strict shortening has width m ≤ 6, in any dimension, with any number of
   terms or any finite layouts.
   - In the plane, two terms need width at least 8 (SH-38).
   - Width 7 is the first width not excluded.
   - This is the run's main new theorem.
3. **The exponent gap.**
   - The two-cut crossing exponent is exactly 1 or √2.
   - The regularized cycle-cover value is exactly 2 or 2^√2 (PG-CYCLE-GAP).
   - Square absence ⟺ one finite dyadic cycle cover of cost below q^√2 (PG-CYCLE-FINITE).
   - Square absence over C ⟺ bounded-width cycle certificates over infinitely many primes, equivalently over all large
     primes (PG-CYCLE-SPECIALIZATION).
   - Run 99 reaches the same gap independently (thm:crossing-exponent-dichotomy).
4. **A finite linear-algebra test for the square over C** (PG-OP-COMPLETE, PG-OP-DETERMINISTIC). The square is absent iff,
   for some dyadic q, one prescribed rational linear system is inconsistent. That system asks for a symmetric equivariant
   operator on a maximum-dimension Specht type, with partial-transpose symmetry and trace 1, supported on types of entropy
   at least (5/4)·log₂q.
   - Related formulations, compressed and fixed-rectangle, are solved explicitly at q = 2, …, 64
     (PG-OP-SLICE-DETERMINANT). The first unresolved value is q = 128.
   - "No member of the original maximum-dimension family has been solved."
5. **Contraction gates.**
   - No square ⇒ contraction with n = 4, s = 15/8 (PG-TREE-CONTRACTION).
   - SH-33: either of two covers would give explicit contraction with n = 3, s² = 3 − 2^−523336:
     - a seven-party cover of exponent ≤ 1/128;
     - a balanced cover K_{r,r} → two r-cliques of exponent ≤ r²/2048.
   - A uniform Izeki–Nayatani invariant bound would suffice too (PG-IN-GATE).
6. **The direct-case exponent.**
   - Fixed-power ceilings of 4/3 hold across broad hub models (EX-29, EX-30, EX-40 to EX-42).
   - The orthogonal equal-width model gives exactly 5/4.
   - The selector gate is reduced to the growth of Γ_k (EX-43).
   - Dropping the fixed topology allows arbitrarily high powers in the abstract geometry, but gives no circuit (EX-39).
7. **Obstructions:**
   - K_{r,r} restricts to two r-cliques neither exactly nor in the border (SH-21, EX-37);
   - PG-CAP-PENT, PG-CAP-HYPER and PG-FIVE-NONL1;
   - PG-SLICE-CLIFFORD: the smaller crossing ranks sum to at least q + 1 for q ≥ 3, over every field.
8. **Corrections to the starting inventory (my prompt).**
   - Fact 5's scale limitation is removed.
   - Route R5's Euclidean assertion is false (PG-HILB2: squared ratio ≤ 3/2 on Mat₂(F₂)).
   - Fact 2's spectral families are not exhaustive.

   These corrections went into our mirror on 24 Nov (commits 3d2aa2f and ba9263c).

## 1. Useful or not

**Useful, strongly.**
- It turns the question the two VP ≠ VNP preprints leave open into exact, conditional equivalences, which a second model
  has checked.
- It adds an unconditional finite-width exclusion and concrete finite targets: width 7, and q = 128.
- No main question is decided. Q1a, Q1b, Q1c, the square in Q2, and Q3 all remain undecided.

## 2. What it proved

Exact forms, with hypotheses. Locators are files in the cp12 folder.

**SH-08** (`shortening.tex` l.427–448).
- Statement: assume (H_A); then over any field a strict shortening exists iff the flat hypothesis fails.
- Gate 1 found no fault. Same-model in-run checks.

**PG-CROSSPOLY-GATE** (`price_geometry.tex` l.583).
- Statement: fix a field and D ≥ 2. Four conditions are equivalent:
  1. the metric on {±e_i} is a price;
  2. that metric with the centre is a price;
  3. every finite subset of R^D is a price;
  4. there is no strict shortening in dimension D.
- At D = 2 these are equivalent to the unit square being a price. A strict planar shortening exists iff every finite
  price is a tree pseudometric.
- Hypotheses: C.3 for (1)⇒(3); A.6 for (4)⇒(3); (3)⇒(4) is unconditional.
- Gate 1 found no fault.

**PG-SQUARE-GATE** (l.515).
- Statement: under C.3, three conditions are equivalent: the square is a price; every finite planar set is a price; some
  finite price is not a tree.
- Gate 1 found no fault.

**PG-FOUR-CONDITIONAL** (l.166). The four-party prices are:
- the tree pseudometrics, if the square is absent;
- the CAT(0)-embeddable four-point metrics, if it is present.

It rests on C.3 and PG-TREE-ALL. Gate 1 found no fault, except that it did not open the outside input of PG-PENDANT
(Wigderson–Zuiddam 2025, Thm 12.23).

**SH-60b** (`shortening.tex` l.5620–5643).
- Statement: over every field there is no strict shortening of width m ≤ 6, in any dimension, with any number of summands
  or layouts. In dimension 2, two summands need width at least 8.
- The proof assembles: SH-28d (widths ≤ 5); Crofton (A = 1); RT-W6-PARAM (A ≥ 4); SH-55d (A = 2); and, for A = 3, SH-38
  (D = 2), SH-46 (D = 3), SH-58 (D = 4), SH-60 (D = 5–7), SH-59 (D = 8–11), SH-57 (D = 12) and SH-55b (D ≥ 13).
- Its run checks include exact rational certificate families. The width-5 proof alone uses 273 one-minimum and 439
  two-minimum certificates, audited "independently" by the same model.
- **My spot check:**
  - the case partition is complete;
  - the dimension-one rank argument holds;
  - every numeric inequality in RT-W6-PARAM holds;
  - its geometric inputs are carried (SH-23, the path-length capacity bound, the sign-frame bound);
  - the component theorems and certificates are not checked.

**PG-OP-DETERMINISTIC** (`price_geometry.tex` l.2357–2449).
- Statement: over C, the square is absent iff (PG-OP-rational-system) is inconsistent for at least one N. This is
  "conditional on the same checked chains as" PG-OP-COMPLETE.
- **My spot check:**
  - termination;
  - √2(m − 1 − √(2m − 1)) > (7/5)k_n;
  - the twentieth-root step;
  - the exact entropy classification n^{4n} ≥ q^{5n}·(∏ν_i^{ν_i})⁴;
  - the converse logic;
  - carried: rt:sos, pg:op-sos-duality, pg:op-signed and PG-OP-COMPLETE.

**Other proved items, at statement level for me.**
- **Small cases:** PG-THREE (every three-point pseudometric is a price, over every field); PG-TREE-ALL; PG-STAR;
  PG-TREE-C.
- **Contraction:** PG-TREE-CONTRACTION; SH-33.
- **Gaps and certificates:** PG-CYCLE-GAP; PG-CYCLE-FINITE; PG-CYCLE-SPECIALIZATION; PG-SLICE-CLIFFORD.
- **Obstructions:** EX-37; SH-21; SH-35 (a refutation).
- **Field:** EX-07 (existence depends only on the characteristic).
- **The direct-case exponent:** EX-19 and EX-20, then EX-29 to EX-43.
- **Route audits:** RT-FINITE; RT-SOS.

**Checks.**
- In-run: 304 independent re-proofs, 180 targeted proof checks, 110 computations or certificates, 33 used and rechecked,
  7 refuted with a refined statement, 6 failed with the exact obstruction. All are by GPT-6 Astra (ChatGPT Pro mode),
  "effort not exposed".
- By others:
  - gate 1 (Claude Opus 5.5 at effort max, af3258db, 25 Nov), as above;
  - this intake's spot checks.

## 3. New since the earlier readings

MAP_COMPLEXITY.md read checkpoint 02, the convener's note read nothing of run 98's TeX, and gate 1 read checkpoint 07.
New since then:
- the whole width program: SH-28d, SH-38, SH-40 to SH-60b;
- PG-OP-COMPLETE, PG-OP-DETERMINISTIC and PG-OP-SLICE-DETERMINANT;
- PG-CYCLE-GAP, PG-CYCLE-FINITE and PG-CYCLE-SPECIALIZATION;
- the exponent gap 1 or √2;
- PG-SLICE-CLIFFORD;
- SH-33 and PG-IN-GATE;
- EX-29 to EX-48 (EX-47 and EX-48 are named in the last reviews; I did not read their statements);
- PG-FIVE-NONL1, PG-CAP-PENT and PG-CAP-HYPER, and EX-37.

Between cp07 and cp12 the statements checked in gate 1 did not move, except for 7 inserted lines in `shortening.tex`
(GATE1 file, top).

## 4. Open, with each main question's gate

- **Q1a (shortening, over C and over F₂).** Width 7 is the first unexcluded width. For width 6 the run stated the remaining
  cases at review 6 as A = 2 with D = 14, or A = 3 with D = 4…12; SH-60b now closes all of width 6. No shortening is
  known at any width.
- **Q1b (flat or contracting).** Undecided over both fields.
  - The gate: one cover at the SH-33 threshold, a uniform bound on the Izeki–Nayatani invariant, or a non-tree spectral
    point.
- **Q1c.** Reduced to whether flatness and contraction exclude each other (SH-09). Open.
- **Q2 (the square).** Open.
  - The gate: the finite cycle-cover certificate at width 7 (q128), or the rational system at q = 128.
  - Five parties are open.
- **Q3.** The growth of Γ_k, and many-hub models with growing hub counts, are open.

## 5. Relations

- **To run 99.**
  - SH-08 and run 99's Q3b prove the same theorem by different proofs (gate 1).
  - PG-SQUARE-GATE corresponds to 99's thm:tree-price-dichotomy.
  - The exponent gap here equals 99's thm:crossing-exponent-dichotomy.
  - PG-CYCLE-SPECIALIZATION runs parallel to 99's Q4a and Q4f.
  - I found no contradiction between the finals.
  - PG-SLICE-CLIFFORD's q + 1 is weaker than Singh's P(q) ≥ 4q/3 for q ≥ 3, which run 99 cites (Singh 2026, Thms 1–4).
    Run 98 should cite Singh.
- **To the literature.**
  - Liu hexagon:2611.00994 ("Two crossing cuts" = RT-SOS);
  - Liu hexagon:2611.00972;
  - Bugár–Vrana, AHP 26 (2025) (the crossing-operator endpoint of PG-OP-COMPLETE);
  - Hrubeš–Wigderson–Yehudayoff, JAMS 24 (2011);
  - Toyoda 2020 and Gromov (four- and five-point CAT(0) conditions);
  - Wigderson–Zuiddam 2025, Thm 12.23 (PG-PENDANT);
  - Alexander–Kapovitch–Petrunin 2011, Thm 5.4 (Kirszbraun);
  - Bridson–Haefliger II.1.15, II.2.2, II.3.6, II.3.19.
- **To the fleet** (mirror of 25 Nov, 8,977 lemmas).
  - No fleet node concerns strict shortenings, prices, the Hurwitz problem or noncommutative circuits. The regex search
    found only incidental matches: L-gct-001/002/005/022/105/134 and L-lib-115.
  - L-gct-011, 026 and 028 are implied by the preprints if they hold. Run 98 does not change them.

## 6. Candidates

- **A Hexagon note other than the square note:** "Strict shortenings need width at least seven" (SH-60b with SH-38). It
  is unconditional over every field. It first needs an audit of the certificate families by a different model or by
  independent code.
- **What the successor 102_VPVNP_SQUARE (queued as Q03a) must carry.** I did not read the 102 prompt, so this is a list of
  needs, not of gaps:
  - the q = 128 rational system and the width-7 cycle-cover search, as concrete first targets;
  - SH-60b's frontier (width 7);
  - the exponent gap, with its carried inputs;
  - the contraction gates SH-33 and PG-IN-GATE;
  - gate 1's verdicts;
  - the hypothesis corrections below.
- **Corrections to report to the run's records.**
  - PG-FOUR-CONDITIONAL's hypothesis line, "the checked price-space chain", should name C.3 and the Wigderson–Zuiddam
    input.
  - PG-SLICE-CLIFFORD should cite Singh.

## 7. Problems

1. **The report opens with "INCOMPLETE"** (`VPVNP_HINGE_report.md` l.1). It says "This is an active research record, not a
   completion claim."
   - The run ended at cp12 by the user's rule, so its report is a snapshot.
   - The last paragraph schedules "checkpoint13 is due05:44:50 UTC" and a review at 05:59:50. Neither will happen.
2. **Same-model checks.** Every in-run "independent re-proof" and certificate audit is by GPT-6 Astra.
   - SH-60b rests on large exact certificate families.
   - It is not note-ready until a different model or independent code audits those families.
3. **PG-OP-SLICE-DETERMINANT** solves only the compressed and fixed-rectangle formulations at q ≤ 64. Its own words: "No
   member of the original maximum-dimension family has been solved." Nothing may describe it as evidence for square
   presence.
4. **PG-FOUR-CONDITIONAL's hypothesis is vague** (item 6 above).
5. **No contradiction with run 99 was found.**

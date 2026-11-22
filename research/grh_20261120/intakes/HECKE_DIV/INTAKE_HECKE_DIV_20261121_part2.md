# Intake of HECKE_DIV, part 2: the final return (prompt 38)

By Claude Opus 5.5 at effort high (the HODGE_SIGN intake agent), 21 Nov 2026, round 3. The brief is
`field_experts\intake_20261121\INTAKE_BRIEF_20261121.md`. Part 1, on checkpoint 01, is `INTAKE_HECKE_DIV_20261121.md`.
Check events: `INTAKE_HECKE_DIV_20261121_part2_CHECK_EVENTS.tsv`.

## 0. What I read, and my scope

**The return:** `research_returns\HECKE_DIV_final_20261121T0204Z_unzipped\`, the final. The run is GPT-6 Astra (ChatGPT
Pro mode); it ran from 00:49 to about 02:04 UTC. The checkpoint-01 folder has since been retired from disk, so I compared
the final against my part-1 notes.

**What I read:**
- `README.md`;
- `QUESTIONS.tsv` (final states);
- `LEDGER.md` (the final status table, and the movement after checkpoint 01);
- the list of statements in the flattened `HECKE_DIV.tex`;
- in full: R24E, R24F and P6;
- the statements of M10, P4, SQ1 and SQ9, with SQ9's proof in full;
- S1–S3 (the run's audit of Severn's manuscript), at the level of the statement.

**New since checkpoint 01:**
- R24E and R24F;
- P6 (stated at checkpoint 01, proved now);
- M5–M10 (Markman made quantitative);
- SQ1–SQ9 (Severn made quantitative);
- S1–S3;
- G1 (the archive);
- U1–U6 (Part II).

**Changed since checkpoint 01:**
- P0 and R21: unchanged, compared with the final text.
- R22–R24C, A1 and A2: same statements.
- Q24-LEFSCHETZ is now worded "invalid inference; final exclusion not established" (R24D). This agrees with my part 1.

**Nothing I confirmed in part 1 is withdrawn or changed.**

## 1. Verdicts on the new and changed findings

- **R24E, order-stable subvarieties have zero Weil projection: confirmed.**
  - The argument: ι(a)(Z) = Z gives a finite map f: Z → Z of degree q^n, from the θ^n degrees; so ι(a)_*cl(Z) = q^n cl(Z).
  - On the Weil lines, pushforward acts by ā^{2n} and a^{2n}, because ι_*ι^* = q^{2n}.
  - Neither equals q^n unless (a/ā)^n = 1. The projection commutes with ι_*, so it is zero.
  - This is an elementary eigenvalue argument, sound.
- **R24F, divisor constructions need not vanish: confirmed** as a consequence of P2b's product identity
  u_n + ωv_n = ±∏(U_j + ωV_j). The identity itself I read only at statement level.
  - It agrees with HODGE_SIGN SG-04 and with HECKE_DIV R24D: on CM elliptic powers, Weil classes are products of
    divisors.
- **P6, arithmetic lifting with varying multipliers: confirmed.** The ingredients:
  - bounded-degree Chow over the base (Suslin–Voevodsky 4.4.11 and 4.4.13; Anderson's flattening);
  - the finitely many non-dominant components lie over finitely many places;
  - a trait through a horizontal component;
  - injectivity of smooth proper specialization (SGA 4 XVI 2.2; cycle classes, SGA 6 X App. 7.13.10);
  - the Betti–étale comparison.

  The same N_v lifts. **In the project's terms:** this is Grothendieck's specialization of cycle classes (SGA 6 X)
  turned into a criterion for lifting. Uniform integral effective degree at infinitely many good primes is equivalent to
  algebraicity in characteristic 0.
  - **It makes exact what 032 Remark 8.5 lacks** (pointwise algebraicity in every characteristic, with no degree bound).
  - The principle is close to folklore, as in specialization arguments for Tate and Hodge. A literature search is
    needed before calling it new.
- **SQ9, the explicit uniform cap on the E⁸ family: the deduction from SQ1–SQ8 is confirmed.**
  - Weil classes are primitive.
  - Hodge–Riemann for primitive (4,4) classes makes the form positive definite on the Weil plane.
  - Mass/comass and Wirtinger give ‖y_i‖ ≤ B.
  - The Gram determinant d satisfies 1 ≤ d ≤ B⁴. Cramer's rule gives the rest.
  - The explicit integer globalizes by R21's closedness.
- **SQ1–SQ8 and M7–M10b: statement level.** These are the numerical extractions, with Schoen's suppliers, Brauer
  transfer, Hermitian-lattice comparisons and Chern-cycle degrees. I did not check them. The run reports independent
  reconstructions and exact scripts.
- **M10, the explicit fourfold template:** N ≤ 1080·q·H₃, and the degrees are bounded by 3240·H₃·B₃·D₆·(|a|+|b|).
  - Statement level.
  - It rests on **Markman** (arXiv 2502.03415v2, Th. 1.5.1 and Cor. 1.6.1), an arXiv preprint.
- **P4 and SQ1: conditional on Severn's Theorem A** (Hexagon 2610.00387v2, internal version 1.5, 21 Oct 2026), an
  unrefereed manuscript.
  - The run's audit S1–S3 is thorough: the finite reflection group, of order 39,191,040, was reconstructed; all
    seventeen monodromy matrices were recomputed; and the nilpotent-orbit dominance argument was read.
  - It is still a run's audit of an unrefereed manuscript. **In our convention P4, SQ1–SQ9 and the E⁸ answer to the main
    question are conditional on Severn.** The README now says "unrefereed manuscript … retained as a geometric input",
    which is accurate; "checked cited input" in P4 should still read "cited, unrefereed".
- **G1: confirmed against our text of record** (part 1). Two Coates letters: our scans 044–047 (4.1.67) and 048–050
  (6.1.1966 as written). Folio = our scan − 1.

**Counts for part 2:**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 4 (R24E, P6, SQ9 as a deduction, G1) |
| Consequence confirmed | 1 (R24F) |
| Statement level | 13 (M5–M10, the five Markman extraction statements counted as one; SQ1–SQ8; S1–S3) |
| A gap | 0 |
| Refuted | 0 |
| Scope corrected | P4, SQ1–SQ9 (conditional on Severn); M1, M10 (conditional on Markman's preprint) |

## 2. What is new

- **Against the literature:**
  - **The explicit integers** in M10 and SQ9 are new: uniform bounds on cycle degrees and multipliers for Weil classes on
    the split fourfold and eightfold families over Q(ω). They are astronomically large (factorials of
    G = 39,191,040), and they are existence-with-a-number, not practical.
  - **P6 and R24E** are new as stated, close to folklore; a search is needed.
- **Against tonight's runs:**
  - THETA3 C13 is the same projector as P1/P3 (a resultant projector; one nonzero projection spans the Weil plane).
  - THETA3 C14 (curve-product constructions miss the Weil space when NS = Qθ) is the generic-fibre mirror of R24E and
    R24F.
  - The three runs agree on one picture:
    - on CM elliptic powers, Weil classes are divisor-generated (HODGE_SIGN SG-04; R24D, R24F);
    - on very general Weil-type members, constructions through divisors or curves miss them (C14; R24D);
    - so the whole difficulty is uniformity along the orbit.
- **Against our results:** the Hodge sketch's Route 2 gate ("are the degrees bounded") is answered **yes** on the split
  fourfold family (conditional on Markman) and on the split E⁸ family (conditional on Severn), with explicit numbers.
  The sketch's ranked prompt 2 is thereby done in that conditional form.

## 3. The two proofs

- No positive result uses RH, Dirichlet GRH or Hecke GRH. The run says so (Q-GRH), and I agree for everything I read.
- Masullo: only the statement index was supplied; nothing is used (Q-MASULLO, U6).
- A2 (Colmez heights grow) stands. Equidistribution under GRH gives nothing alone (A1).
- **H01, the sign-only proof (published as hexagonmath.org/2611.00789):** not used. The run's reading of step 5 found
  "no cycle coercivity" (A3, formal). This agrees with the HODGE_SIGN intake: purity does not see cycles.

## 4. Integration (edits listed, not made)

- **Hodge sketch, Route 2** (`reports_20261120\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md`): after the gate sentence,
  add: "On the split Q(ω) Weil fourfold family, bounded division holds with explicit N and D (HECKE_DIV M10;
  conditional on Markman arXiv 2502.03415v2). On the split E⁸ family the same holds (HECKE_DIV P4, SQ1–SQ9; conditional
  on Severn, Hexagon 2610.00387v2, unrefereed). The arithmetic form of the gate is P6: uniform integral effective degree
  at infinitely many good primes ⟺ algebraicity (checked)."
- **Same file, 2.4:** add "R24E: subvarieties stable under the order have zero Weil projection (checked). R24F: divisor
  products do not vanish on CM elliptic powers (checked)."
- **Same file, Route 5 (032 Remark 8.5):** add "P6 makes exact what Remark 8.5 lacks: a uniform integral degree at
  infinitely many places."
- **Same file, 3.2 and section 5:** the two-letter correction, as in part 1.
- **The project's terms.** The run's archive section (G1 and its crosswalk) ties:
  - R21 to cote 16's correspondence framework;
  - P6 to SGA 4 XVI and SGA 6 X.

  It states these as framework locators, not as content of the pages. That is adequate.

## 5. How it bears on the running Hodge prompts, and the attacks it opens

- **39 (GHOSTS):** P6 is exactly the statement that links "ghost" behaviour (algebraic at every prime, with unbounded
  complexity) to failure in characteristic 0. A class whose reductions are algebraic at every good place, with integral
  effective degrees unbounded along every infinite set of places, is precisely the obstruction. See the GHOSTS intake.
- **40 (JACOBIANS_1964):** none.
- **41 (DEGREES_ARE_L_VALUES):** P0 and SQ9's mass/comass argument are the degree-to-multiplier tools. A Rallis degree
  formula would bound N directly through P0.
- **37 (THETA3):** C13 and C14 duplicate P1, P3 and R24E. THETA3 should cite them.
- **The next attack (successor):**
  1. An unconditional E⁸ route: P2b seeds plus P6 at split ordinary primes, where End(E_v) = End(E).
  2. Or a reproof of Severn's supplier mechanism, which removes the dependence.
  3. Shrink the integers. Optimality is not claimed.

## 6. Hexagon readiness

| Candidate | 1 | 2 | 3 | 4 | 5 | Verdict |
|---|---|---|---|---|---|---|
| M10 + SQ9: explicit bounded division for Weil classes, fourfold and E⁸ | yes, with cited inputs | **no:** Severn is unrefereed, Markman is an arXiv preprint | yes (final) | statement level here | high | not a candidate while it rests on Severn. The fourfold part alone hinges on Markman's status: if Markman counts as published, M10 is **two gates away**: an independent re-check of M7–M10 and a literature search |
| P0 + R21–R23 + R24E + P6 + A1 (exact reductions, unconditional) | yes | yes | yes (final) | targeted checks by me; the run's independent reconstructions | medium | **one gate away from 1–4:** a literature search (Voisin; André; specialization folklore). Test 5 is moderate, so I do not flag it as urgent; worth listing |

**Addendum, after the GHOSTS intake (same agent, 21 Nov).**
- P6's principle has a published precedent: Brünjes–Serpé, *Uniform bounds and ultraproducts of cycles*, arXiv
  0901.4853, Thm 3.4. GHOSTS cites it at B02a. **P6 is therefore not new in principle.** Its varying-multiplier form,
  (iv), is the same as GHOSTS B06.
- GHOSTS R10–R12 prove bounded division on the principal Q(ω) Weil fourfold component from Schoen's published Prym
  construction (Compositio 65, 1988 and 114, 1998; D₀ = 132,269,760). That **supersedes M10's dependence on Markman's
  preprint for that component.**

# Intake of HODGE_FINISH (prompt 70c), checkpoints 01–06 and final

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1, a copy of abcaba9b6ae84b747, the author of the seed and of
both intakes of HODGE_BOUNDED_CYCLES), 23 Nov 2026, evening.

- **Return:** `grothendieck_archive_transcription_20261110\research_returns\HODGE_FINISH_final_20261123T1713Z_unzipped\`
  (17:13 UTC). The papers are at `workbench\work\UNFILED-A\v1\paper\main.tex` (Paper A, 66 pp.) and
  `workbench\work\UNFILED-B\v1\paper\main.tex` (Paper B, 88 pp.).
- **Run:** GPT-6 Astra (ChatGPT Pro mode), effort not exposed by the interface.
- **Prompt:** `TO_SEND\PRO\1_Archive_research_by_topic\SENT\70c_HODGE_FINISH\PROMPT.md`.
- **Also delivered:** check events, the integration table `INTEGRATION_HODGE_FINISH_20261123.tsv`, and
  `PRIMER_HODGE_FINISH_20261123.md`, all beside this file.

## 0. Scope

- **Read:**
  - the prompt (Parts 1–3); CURRENT_STATE.md; QUESTIONS.tsv (32 rows) in full; LEDGER.md (source lines);
    LITERATURE.md (the Schoen line);
  - the Schoen and Q24 rows of CHECK_EVENTS.tsv;
  - **Paper A** lines 36–330 in full (title, abstract, state of the field, Markman, why/what new, Proof overview);
  - **Paper A**, Theorem gaussian-volume-bound (2387–2410), and Lemma gaussian-maximal-lattice with its proof and the
    completion of the theorem (2850–3075), in full;
  - the closing note (3359–3370);
  - **Paper B** lines 36–100 (abstract, introduction); §"The precise additional input" (4770–4810); Corollary
    clifford-cor:canonical-all-powers (4953–4975); Proposition clifford-prop:half-twist-obstruction with its proof and
    the following paragraph (5016–5064).
- **Not read in this pass:** every other section. Paper A's equivalence, extraction, 48/192, stabilization, Q10 and Q12
  are unchanged in mathematics from what I checked in the HODGE_BOUNDED_CYCLES intakes; I spot-read their statements
  in Paper A's §1, but did not diff their proofs line by line.
- **The checkpoints:** 01, 03, 05 and 06 were not read separately. The final supersedes them; their content is in the
  ledger and register.
- **Ran:** both papers rebuilt from fresh copies with MiKTeX latexmk. Paper A: 66 pages; Paper B: 88 pages; 0 overfull
  boxes and 0 undefined references in each. Pages not viewed.
- **Programs:** not run.

## 1. Verdicts

| Item | Verdict |
|---|---|
| Paper A's main theorems (equivalence, Poincaré-pairing bound, extraction, 48/192, stabilization, Q10, Q12) | used and rechecked: the statements are unchanged, the proofs checked in the earlier intakes |
| **Q24 refined** (Paper A, Theorem gaussian-volume-bound, Lemma gaussian-maximal-lattice) | **targeted proof check, no fault** (§2). The bound ℬ rests on Severn's unrefereed E₈ construction, which the paper declares |
| **Q23 refined** (Paper B, half-twist obstruction) | targeted proof check of the obstruction, no fault. The positive all-powers corollary is statement level |
| Q32 (Paper B, Eisenstein transfer, 8,960 exact equations) | statement level |
| Other new rows | statement level |
| Refuted by me | none |

## 2. What is new, usefulness first

1. **Integral Gaussian sixfolds of determinant class [−3] (Q24, now a theorem).**
   - *Good for:* the explicit table of the Weil engine. It gives every integral polarization volume in that nonsplit
     class one bound, (Δ/3)·ℬ, from one source family. It is the first nonsplit Gaussian sixfold row.
   - *Statement:* for every complex sixfold with integral Z[i]-action of signature (3,3) and determinant class [−3],
     3 | Δ and δ_W ≤ (Δ/3)ℬ.
   - *The lattice lemma, which I checked step by step:* every Z[i]-lattice with integral pairings in that Hermitian space
     embeds isometrically into (Z[i]^6, U ⊥ U ⊥ ⟨1,−3⟩).
     - At split primes a maximal lattice is A ⊕ A^∨.
     - At odd inert primes it is diagonal with exponents in {0,1}, at most one equal to 1, exactly at p = 3 by the
       determinant.
     - At 2 a maximal lattice is unimodular. Here N(R^×) = 1 + 4Z₂. Even unimodular rank 6 would be U³, of class [−1],
       which is excluded. Odd lattices reduce by ⟨a⟩ ⊥ U ≅ ⟨a,a,−a⟩ and ⟨1,1⟩ ≅ ⟨−1,−1⟩ through P with P*P = −I.
     - Globally: there is one special genus, the determinant ideal is principal, and strong approximation holds for
       SU(3,3).
   - *Recomputed:*
     - P*P = −I₂ and det P = −1 for P = [[π, c], [−c̄, π̄]], with N(c) = −3;
     - the three orthogonal vectors of ⟨a⟩ ⊥ U;
     - u = N(√(u−4) + 2i) for u ≡ 5 mod 8;
     - **3 | Δ, independently:** Δ/3 is a rational norm from Q(i), so v₃(Δ) is odd and at least 1;
     - the index: det_Z(L) = Δ² = [L₀ : L]²·9, so [L₀ : L] = Δ/3.

   The step "pairing integrality, not only norm integrality" is essential, and the paper's counterexample at 2 is right.
2. **The Clifford/Kuga–Satake criterion (Q23, refined).**
   - *Good for:* Mumford's exceptional classes. If the specified quadratic Lie block 𝔤 → End V is algebraic, the Hodge
     conjecture holds for every power of the Mumford fourfold A (statement level for me). The canonical Clifford
     statement of Bolognesi–Laterveer is a sufficient input.
   - *The obstruction (checked):* the half-twist embedding ν, with commutators and projection to V, cannot produce that
     block, even after Hodge endomorphisms and isogenous powers. The proof is isotypic. On the derived group, H₀ is
     trivial and H₁ contains only (2,1,1), (1,2,1) and (1,1,2), while the Mumford block is (2,2,2); Hodge endomorphisms
     preserve isotypic parts; and Hom_G(U₀, End V) = 0.
   - **Outreach point:** if Bolognesi–Laterveer (Theorem 4.4, Proposition 6.2) derive the Clifford statement from ν by
     such operations, their argument lacks a comparison. The paper says carefully that this is not a disproof. I have
     not opened their paper. **Before anyone writes to them, open it at that locator.**
3. **Q32:** the positive trace network transfers to the Eisenstein field, with 8,960 exact equations. Statement level.
   It is a solved necessary subproblem, not a deformation.

## 3. The finishing fixes (from the HODGE_BOUNDED_CYCLES final intake)

| Fix | Made? |
|---|---|
| 1. State of the field | **yes.** §1 opens with Voisin, Th. 1.3, p. 1248-03: the Hodge conjecture for abelian varieties of dimension ≤ 5 (Markman) |
| 2. Abstract and title | **yes.** Published inputs only; CM theorems not inputs; Weil engine, Q10, 48/192/36, the Q12 test. Title without "after Brünjes and Serpé", justified: "The proof below … does not invoke their Theorem 3.4" |
| 3. "Proof overview" section | **yes**, in Paper A, covering the equivalence, extraction, small detectors, stabilization, Q10, the higher bounds, Q24 and Q12. Paper B has "Why this matters" and "What is new here"; I did not check that its overview covers every theorem |
| 4. Why this matters / What is new | **yes**, with CDK p. 483, Bhattacharjee–Bhattacharya Lemmas 4.2–4.3 and Th. 4.5, pp. 10–12, and Brünjes–Serpé Th. 3.4 |
| 5. Markman exactly; OpenAI withdrawal | **yes.** ICM Th. 1.2, p. 587, paraphrased with its phrase quoted, plus the detailed preprint locator; the OpenAI eightfold withdrawal (6 Oct 2026, sign error) is cited in both papers |
| 6. The rStation step | **yes.** Paper B rests on Cohen and Malle by locator, and the preprint remains a citation |
| 7. Q23, Q24, Q32 | **yes.** Each is checked and in its paper; Q23's formal transfer is refuted and refined |
| 8. Schoen 2007 by exact locator; the Q12 search | **partly.** The paper cites Th. 1.1(i)–(iii), p. 585, but the ledger and LITERATURE.md say the full original Schoen 2007 text was not obtained; the small-detector re-proof keeps "published Schoen geometric statement as exact external input". The Q12 search is complete per the register (not verified by me) |

**Text checks (mine):**
- no run names, ids or paths in either paper (the rStation handle appears only in the bibliography);
- the closing notes name GPT-6 Astra (ChatGPT Pro mode), the same-model re-proofs, the outside reading by Claude Opus
  5.5 at effort high "which found no error in the statements identified in its records", no human, and CC0.

**What remains:**
- obtain Schoen 2007 and check Th. 1.1 at p. 585 for the 36 bound;
- confirm Paper B's Proof overview;
- my page view of both PDFs.

## 4. Scope of the inputs

Paper A's equivalence uses published inputs only. These results carry declared unrefereed inputs:
- Q09 all-field sixfolds (Perry);
- Q28 Eisenstein eightfolds (Severn, G₃₄);
- Q24 (Severn, E₈);
- the Q23 corollary (Bolognesi–Laterveer's published statement).

## 5. Integration (applied; see INTEGRATION_HODGE_FINISH_20261123.tsv)

- `reports_20261122\paper_seeds\SEED_HODGE_DIVISION.md`: appended "Update after HODGE_FINISH", with the superseding
  constants, Q10, Q24 and the state of the field.
- `reports_20261120\hodge_bridge\HODGE_DIVISION_ATTACK_20261121.md`: added a "superseded in part" note after the title.
  It lists the stale and false statements recorded in my 22–23 Nov intakes, which were never applied.

Backups of both are in `integration_backups\20261123\HODGE_FINISH\`.

**For the main session (shared registers, not edited):**
- HEXAGON_CANDIDATES H12/H25: cite the Paper A constants, and add Q24 and Q12.
- The board rows below.
- The fleet map rows below.

## 6. Prompt updates

None needed for this run, which has ended.

For a successor:
- the main question is unchanged: split eightfolds over K ≠ Q(√−3), Q06/Q07;
- obtain Schoen 2007;
- open Bolognesi–Laterveer at Th. 4.4 and Prop. 6.2 and decide whether the Clifford comparison is supplied there.

## 7. Hexagon readiness and board candidates (rows for `field_experts\hexagon\HEXAGON_BOARD.tsv`)

| Title | Statement | What it adds | Gate left |
|---|---|---|---|
| The Hodge conjecture for abelian varieties as a uniform bound over finite fields (Paper A) | Hodge conjecture for abelian varieties ⟺ in every special family one degree bound for cycles on reductions of CM points (published inputs); Poincaré-pairing multiplier bound; quadratic Weil extraction; 48/192/36; stabilization; Q10; Q12; Q24 | the criterion and the explicit Weil engine | my page view; the Schoen 2007 locator for 36 (or state 36 as resting on Schoen's published statement); a final literature check on Hexagon. The five tests: complete yes; self-contained yes, with declared preprint rows; stable yes; checked yes (my targeted checks plus same-model blind re-proofs); of interest yes |
| Integral Gaussian Hermitian lattices of determinant class [−3] (could be a lemma note) | every pairing-integral Z[i]-lattice in signature (3,3), class [−3], embeds isometrically in U ⊥ U ⊥ ⟨1,−3⟩; hence 3 \| Δ | a one-class statement used for exact transport costs | a literature search (Hermitian lattice classification over Z[i]: Jacobowitz, Kirschmer); otherwise ready as part of Paper A |
| Obstructions to cycle constructions and criteria for Mumford's exceptional classes (Paper B) | specified eightfold construction obstructions; Mumford criteria; the half-twist obstruction | which constructions cannot work; what input suffices for Mumford classes | open Bolognesi–Laterveer before posting the half-twist remark; my check of its overview |

## 8. For the P vs NP fleet (maps constructed, not graded)

| Source (ours) | Fleet node(s) | Translation | Work to complete |
|---|---|---|---|
| Paper A equivalence (H25 / HT-07, already in `maps\hodge_theory.md`) | no node; nearest L-lib-015, L-lib-029 | "is this Hodge class algebraic" becomes a bounded search for cycles of degree ≤ D on reductions, a verifier-type problem | Paper A's explicit constants (2·16^n/n!, 48/192/36, (t_K f m_K)^nΔ) now give the size of the certificate in the Weil case: add them to HT-07 and state the decision problem as a node |
| Q11 (35 invariant quadratic relations of the Gaussian minus projection; minimum rank 24 of the induced pairing on ∧²V for translation/sign-invariant alternating four-forms on V indexed by F₂⁴) | L-pcx-092 (rank bounds for alternating forms over F₂) | both bound the rank of an alternating form from symmetry. Q11 is over Q with an F₂⁴ translation group; L-pcx-092 is over F₂ | decide whether the F₂⁴-invariance in Q11 reduces mod 2 to an instance of L-pcx-092's inequality; this needs the explicit 35-dimensional basis (Paper B certificate) |
| Q24 lattice lemma (local maximal lattices plus strong approximation give one class) | no node | — | none proposed |

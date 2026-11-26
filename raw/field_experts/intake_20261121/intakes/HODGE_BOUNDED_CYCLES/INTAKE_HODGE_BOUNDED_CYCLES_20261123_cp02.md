# Intake of HODGE_BOUNDED_CYCLES checkpoint 02 (prompt 70), with a review of its paper

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747, author of the seed and of the division attack), 23 Nov 2026.

- **Return:** `grothendieck_archive_transcription_20261110\research_returns\HODGE_BOUNDED_CYCLES_checkpoint_02_20261123T0005Z_unzipped\HODGE_BOUNDED_CYCLES\`
  (00:05 UTC; checkpoint 01 is retired inside).
- **Run:** GPT-6 Astra (ChatGPT Pro mode), started 22 Nov 22:34:46 UTC, in progress. The first progress review is due
  01:34 UTC.
- **Check events:** `INTAKE_HODGE_BOUNDED_CYCLES_20261123_cp02_CHECK_EVENTS.tsv`.
- **Follow-up drafted (not sent; it waits for the user):**
  `TO_SEND\PRO\1_Archive_research_by_topic\70b_HODGE_FOLLOWUP_1_paper\PROMPT.md`. `push_rule_pro_prompts.py --lint-math`
  PASS.

## 0. What I read, what I ran

- **Read:** HOW.md "What a paper has to be" in full; the run's README, SESSION.json, QUESTIONS.tsv, LEDGER headings,
  LITERATURE.md, the Hexagon rows of search_log.tsv, the head of the statement-only re-proof of the equivalence, the
  register of CHECK_EVENTS.tsv, and the bibliography.
- **Read in the paper:**
  - main.tex in full (title, abstract, §1, the parameter-space lemmas, the Poincaré-pairing bound, lifting and
    spreading, special families and the proof of both theorems, the minimum-degree dichotomy, the closing note);
  - introduction-additional.tex in full;
  - weil.tex in full (extraction, detector loci, the Gaussian constant, qualitative and explicit stabilization);
  - small.tex §§1–2 (48 and 192) and the start of §3 (36);
  - the opening sentences and "what remains open" of research.tex.
- **Not read:** sixfolds.tex, galois.tex, one-prime.tex, theta-eightfolds.tex, equivariant-eightfolds.tex,
  localized-support.tex, the rest of small.tex §3 (the Schoen surface, 36), the records, the programs.
- **Ran:** a rebuild of the paper from a fresh copy of its .tex files with MiKTeX latexmk. The result: 40 pages,
  0 overfull boxes, 0 undefined references. I did not view the pages.
- **Searched the text for banned words** (run names, our ids, checkpoint, intake, agent, prompt, ledger, supplied,
  actual, retained, paths, seed). None visible; only internal LaTeX labels such as `sec:ghosts`.

## 1. The statements (QUESTIONS.tsv)

- **Proved:** Q01 (family and global equivalence); Q02 (Weil extraction, a stronger exponent); Q03 (48/192/36;
  multiplier 3); Q04 (stabilization, qualitative for every K, explicit with factor max(1, Nm τ/Δ)/(n+1)); Q05 (the
  minimum-degree dichotomy).
- **Open:** Q06 (split eightfolds outside Q(√−3)), Q07 (uniform split detectors), Q08 (an exceptional non-Weil
  family).
- **Under audit:** Q09 (the higher-dimensional table).

## 2. The main theorem against the seed and the independent check

| Point | Seed | Independent check | Paper |
|---|---|---|---|
| the map S → A_{g,N} | "a map" | must come from a morphism of Shimura data (R1) | the definition asks for it; CM points are special points of the datum |
| the multiplier | Wirtinger: N ≤ 2D/(d!h) | M²q_t ≤ C(2d,d)(deg Z⁺ + deg Z⁻)² | the same Poincaré-pairing bound, proved, valid in every characteristic |
| ℓ and the place | fixed | may vary; one place outside a finite set suffices | the same |
| family by family | implicit | stated | the family theorem |
| inputs | published | published; no 032, Tate, André–Oort, absolute Hodge | the same, and said so |

**Verdict: the paper's main theorem is the repaired statement, at exact strength, with the check's improvements.** I
read its proof (main.tex 123–310) and found no error.
- The pairing bound: with U = H + P and V′ = H − P nef, P = (U − V′)/2. The text omits the factor 1/2 in one line, but
  the inequality is right: |∫P^{2d}| ≤ 2^{−2d}∫(U + V′)^{2d} = ∫H^{2d}. Positivity of q_t holds because ∧^{2d}J fixes a
  real class of type (p,p).
- The Mumford–Tate datum and the density by real approximation are correct.

## 3. The other main results: my checks

- **Quadratic extraction** (weil.tex 13–126): δ_W ≤ c_t ≤ ⌈2·16^n/n!⌉ δ⌈√T⌉ Nm(a)^{n(2n+1)} δ_W², for every
  polarization type.
  - **Rederived:** with m = [𝒲 : Zu + Zv] and covolume c ≥ 1, mδt = ru + sv with r = δ det(t,v)/c and
    s = δ det(u,t)/c. Then M = δm ≤ δq^n‖u‖², and deg Z^± ≤ 2δ√T q^n L‖u‖, with L = 4^n q^{n²} δ_W.
  - It is correct, and stronger than our HD-U (exponent 2n(n+1) → n(2n+1), coefficient 8 → 2), because it clears the
    lattice index instead of the Gram determinant.
- **48 and 192** (small.tex §2): the residual argument (class 4θ², degree 96, e_W kills it) and the degree-16 isogeny
  match what I checked in the second run of prompt 46. Correct, given van Geemen 1996, Prop. 3.6 and Th. 3.7 (not
  opened).
- **Stabilization:**
  - Qualitative, every K (weil.tex 192–224): λ = rϑ₁ + sϑ₂ gives determinant −d, and the product is split. If the
    three very ample classes Nλ and Nλ + η_i all had contractions without Weil part, Y would be orthogonal to the Weil
    plane. Correct.
  - Explicit (weil.tex 231–262): [Γ_u] + [Γ_{−u}] = 2(ϑ₁ + Nm(u)ϑ₂) ≤ 2κλ, and (n+1)∫_Y θ^nλ ≤ D. Correct, and
    better than our HD-COMP (1 + Nm τ → max(1, Nm τ/Δ)/(n+1)).
- **Not checked:** the 36 bound in this text (I checked the same argument in run B's text earlier); the sixfold
  constants; the eightfold exclusions.

## 4. The paper against "What a paper has to be"

| Box | Present? | Right? |
|---|---|---|
| 1. Title | "Hodge's conjecture for abelian varieties as a uniform bound over finite fields, after Brünjes and Serpé" | Names the conjecture. "Hodge's conjecture" should be "the Hodge conjecture". "After Brünjes and Serpé" is defensible only if their Theorem 3.4 is the engine of the arithmetic direction; the special-family reduction is new. A judgment for the run, put in 70b |
| 2. Abstract | first sentence on Brünjes–Serpé; what is proved; who produced and who checked; no human | **Missing:** "what is granted": it should say that the equivalence uses only published theorems and that the CM theorems are not inputs |
| 3. Theorem in words | both theorems in full; the quantifier display; the famous statement named | yes |
| 4. Why care | one sentence in §1 and the paragraph on quantifiers | thin; needs its own paragraph |
| 5. Credit | Brünjes–Serpé, Cattani–Deligne–Kaplan p. 483, Bhattacharjee–Bhattacharya (Hexagon 2610.00315v2), Voisin | present and honest: the complex half is credited as having antecedents. "What is new here" should be one explicit sentence |
| 6. Context | OpenAI 032 and van Hoften–Sempliner, with status; Markman; André | **Gaps:** (a) Voisin's Bourbaki exposé 1248 (Jan 2026) is titled "La conjecture de Hodge pour les variétés abéliennes de dimension au plus 5", but is cited only for a lemma: the state of the field must be stated from it. (b) Severn's Eisenstein eightfold preprint, Hexagon 2610.00387, opened per the search log, is not cited, although the register treats those eightfolds as settled. (c) Markman's ICM claim should be quoted exactly |
| 7. Scope | "These results do not prove the Hodge conjecture"; ∃D∀x versus ∀x∃D | yes |
| 8. Why the proof works | §1.2 | yes, good |

**Every new result proved in full:** yes for what I read. The run keeps the records still under review out of the
paper. The table beyond fourfolds is under audit (Q09), and I did not read sixfolds.tex.

**Banned text:** none found.

**Closing note:** present. It names GPT-6 Astra (ChatGPT Pro mode), the same-model re-proofs, "earlier checks by Claude
Opus 5.5 at high effort", no human, CC0, and the workbench link. It is right; once this review counts, it should name
it.

**Literature search:** LITERATURE.md and 61 logged queries, eleven of them on Hexagon (Dense Algebraic Loci opened,
Severn opened). Brünjes–Serpé, CDK, Bhattacharjee–Bhattacharya and Voisin were found. Adequate. The exposé's title is
the one finding not drawn into the text.

**Check events and blind re-proofs:** 23 rows. Statement-only re-proofs by the same model exist for the equivalence
and the global theorem (the re-proof file says it saw no project files), for the extraction (two), the small detectors
and the stabilization. **Each main theorem has a blind same-model re-proof.** No re-proof by another model exists
apart from this outside reading.

**Build:** compiles cleanly (my rebuild: 40 pages, 0 overfull, 0 undefined). The visual page check and the two full
readings are still pending, as the run says.

## 5. Verdict

**On course to a postable paper.** The mathematics I read is correct and at the right strength, the text is clean, and
the opening has six of the eight boxes right.

**The fixes,** all in 70b:
1. State the current state of the field from Voisin's exposé (with Markman), before the theorems.
2. Cite and place Severn's Eisenstein eightfold preprint, and the withdrawn OpenAI eightfold manuscript.
3. Quote Markman's ICM statement exactly.
4. Make the abstract say that the inputs are published and the CM theorems are not used. Write "the Hodge conjecture".
5. Give "why care" its own paragraph.
6. Add one explicit sentence on what is new.
7. Decide "after Brünjes and Serpé" in the title on the merits.
8. Keep unreviewed constructions out until proved.
9. State the open gate exactly at the end.
10. Do the visual check, the two readings and the deposit sheet.

**For our records:**
- The paper supersedes our HD-U constant (2·16^n/n! and exponent n(2n+1)) and our HD-COMP factor
  (max(1, Nm τ/Δ)/(n+1)).
- The seed's Wirtinger bound is replaced by the Poincaré-pairing bound.
- The Hexagon register's H12/H25 entries should cite the paper's numbers once it is filed.

# Editor's comments before writing the note H30 (the chain length under Alpöge's size hypotheses)

By Claude Fable 5.2 at effort max (agent a3ccbc11), 23 November 2026, editor under
`pro_prompt_builds\PAPERS_20261122\core\EDITOR_BRIEF.md` and `SHORT_NOTE_EDITORS_20261123.md`.

## What I read

- **The material:** the producing run's paper (`papers\theta-chain\main.tex`, lines 60–345: scope, the numerical
  interface, the main theorem with its proof, the corollary, the family proposition, the section on a bounded-length
  replacement; not its 60 further sections, which are a different and unfinished subject); the run's standalone Lean
  module, its log and run record, its map from the source's hypotheses, and its uncompiled bridge file (all as text;
  nothing run); the intake of Claude Opus 5.5 at effort high with its check events; the seed's theorem.
- **The work it answers, at the source:** Alpöge's remark (all four pages, 20 and 21 Nov); and the definitions of the
  formal development in the copy of the archive distributed with the remark on 20 Nov: `Ranks` (Params.lean 6–38),
  `Scale` (DataParams₂.lean 9–45), `szTh`, `SizeN`, `SizeM`, `SizeK`, `SizeKRel`, `SizeG`, `SizesAt` (ElevenLe.lean
  11–50, 124–138). The five inequalities of the theorem are, word for word, conjuncts or halves of conjuncts there.
- **The neighbouring posts:** hexagon:2611.00799 (Jaswal), 2611.00809 (Zhang), 2611.00812 (Slijepčević), 2611.00828
  (twinheterodox). Fetched as PDFs on 23 Nov, text extracted, **searched by keyword and read at the passages found; not
  read in full.**

## Is this what we want to say, and whom would the material not serve?

**The mathematics is right.** I re-derived all three parts of the theorem and the uniform bounds; they are elementary
and there is no fault. The run's paper cannot be posted as it stands: its abstract is forty lines of internal
milestones, it has no proof overview, and 269 of its 272 pages are an unfinished study of length-two chains. The
theorem is three pages. So the note is written new, around the theorem alone.

What matters most, in this order:

1. **Say what kind of statement this is, in the first paragraph.** It is a fact about the hypotheses under which the
   formal proof is carried out. It is not a defect of the proof: the argument is asymptotic in x, and all three guides
   say "for large x". Without that sentence the expert reads "m > 2^7778" as a criticism, and Alpöge reads it as an
   attack. The abstract and Section 1 say it plainly, and say what the bounds are good for: there are no small
   instances to compute, and a variant with a bounded chain must replace three named hypotheses.
2. **The square-root law is not ours.** Step 8 of the remark takes m like √X. Zhang explains it as the balance of two
   errors of sizes x/m and m (p. 9; Lemma 6.1, p. 58); Jaswal says the error is smallest at m ≈ √x (pp. 2, 6);
   Slijepčević prints the sizes of a scale, with √(xδ₁) ≤ m ≤ 2√(xδ₁) (Definition 6.3, p. 31; Lemma 6.4, p. 32). Part
   (1) of the theorem is the hypothesis (M) rewritten. The credit section says so. What the note adds is parts (2)
   and (3): the floor (log f)² ≤ m/2 − 1, which excludes two lifts, and the absolute bounds, which none of the four
   posts states (by my keyword search).
3. **The gate.** The theorem is stated for the five displayed inequalities, which the standalone Lean module
   certifies. The link to the source is by inspection, with file and line for each inequality; I made that inspection
   myself. The note says exactly what the uncompiled bridge would add: the same conclusions as kernel-checked
   theorems about the source's own objects, with their axiom report, in place of an inspection of four definitions.
4. **The newcomer needs the objects named.** In the run's text n, k, g and f are letters. The note says what each is
   (the order of the group A of the host; the dimension of the first Hermitian space; an auxiliary integer of the
   host; the degree of the maximal totally real subfield, so that the CM field has degree 2f = 4n), with locators in
   Zhang (pp. 25, 43) and Slijepčević (p. 11).
5. **The numbers are artefacts of the constants; the mechanism is not.** The hinge is (G): a lower bound (k e^L)^8 ≤ g
   and an upper bound log g ≤ x^θ L on the same number give 8 < L^{1/100}. The proof overview says this, with the
   example that L = 10^90 is already excluded.
6. **Drop** the run's corollary on f = 42, f = 168 and L = 343: these values come from our own earlier experiments and
   mean nothing to a reader. The general statement covers them.

**One addition of mine** (recorded as a check event in RECORDS.md): from (R) and m ≤ f alone, (log m)² ≤ m/2 − 1, which
fails for every even m ≤ 18 and holds from m = 20 on. So the logarithmic condition by itself already forces twenty
lifts. It shows what each hypothesis does separately.

## Which kind of note

**Needs a pass, and the pass is done.** Three guides to the proof and one simplification paper were posted on
21 November. None overlaps parts (2) and (3); all bear on part (1), and they are credited for it. The simplification
paper takes the lifts and the interval estimates as inputs (its p. 1), so it does not change the size hypotheses.

## What is left before posting

- The user's look and word.
- Optional: compile the bridge against the pinned commit. The theorem as stated does not need it.
- The three guides were searched, not read in full. A full read of Jaswal §4.1, Zhang §6 and Slijepčević §6 would
  make the sentence "none of them states an explicit threshold" firmer.

# Intake of NIGHT_AFTER_ALPOGE checkpoint 11, Part B: the length of Alpöge's theta chain

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 23 Nov 2026. Parts A and C are taken in by agent
ad85573792c61a914.

- **Return:** `research_returns\NIGHT_AFTER_ALPOGE_checkpoint_11_20261123T1024Z_unzipped\` (10:24 UTC; prompt 75,
  which carries prompt 73's question as Part B).
- **Run:** GPT-6 Astra (ChatGPT Pro mode), active. Review 06 at 10:09 UTC recorded movement on Part B.
- **The paper:** `workbench\zeta-and-l-functions-workbench\papers\theta-chain\main.tex`, with 60 inputs, built
  main.pdf, **272 pages**.
- **Check events:** `INTAKE_NIGHT_AFTER_ALPOGE_20261123_cp11_partB_CHECK_EVENTS.tsv`.

## 0. What I read

- **Read:**
  - QUESTIONS.tsv rows B-Q1 and B-Q2 in full;
  - the Part-B ledger rows and progress review 06;
  - the title, abstract, §§1–3 and the main theorem with its proof in main.tex (lines 1–200);
  - the Part-B rows of CHECK_EVENTS.tsv;
  - the statement list of `checks\b_numeric_uniform_complete.lean`, and the head of `b_numeric_source_bridge.lean`.
- **Not read:** the 60 input sections (the length-two analysis, the signed counts, theta quotients, Fischer witness,
  grid–word maps), the Kummer part, every program. **Not run:** the Lean files.

## 1. The main theorem, and what is new

**The paper's main theorem is the chain-length theorem of my ALP_MACHINE seed, at the same strength:**
- x^{1/2−29ε/400} ≤ m ≤ x^{1/2−21ε/400};
- (log f)² ≤ m/2 − 1, so m ≠ 2;
- L > 2^300, m > 2^7778, f > 2^33598, k > 2^73197.

It is proved from five explicit real inequalities (M), (R), (G), (N), (K) abstracted from the source. The proof is the
one I checked on 22 Nov against the Lean definitions (ElevenLe.lean, DataParams₂.lean, Params.lean). It is now
written for a reader with no access to the formal development.

**New since my seed:**
1. **A Lean certificate of the numerical part.** A standalone Lean 4.33.1 module proves the conclusions from the five
   inequalities: ten conclusions, then five uniform ones, with only the standard axioms. The run recorded this as a
   formal certificate. **The bridge from the pinned `SizesAt` to the five inequalities
   (`b_numeric_source_bridge.lean`) is written but not compiled**, because the source build did not finish.
2. **The degree convention is corrected.** f = [F:Q] is the degree of the totally real subfield, and [E:Q] = 2f. My
   seed called f the degree of the CM field. The numbers are unaffected, since the source's f is what the inequalities
   use, but the seed's sentence must be corrected (edit listed below).
3. **The length-two analysis (B-Q1, active).** Both local theta quotients and the two-arrow multiplicity quotient are
   proved; one primitive pair detects the whole function-valued kernel; a bounded Fischer witness of degree ≤ 350 f r²
   b² gives every nonzero Bessel value on the image. The open gate: a signed joint determinant/height estimate, a
   length-two arithmetic host and count, and the Lean bridge. **No bounded-length replacement of step 8 and no
   method-wide divergence is proved.** Statement level for me.

**Verdicts:** the main theorem was used and rechecked (its proof is the one I checked on 22 Nov). The rest is statement
level, and I refuted nothing.

## 2. The paper against HOW.md

- **Box 1, title:** "How long must the chain of theta lifts be? After Alpöge". Good.
- **Box 2, abstract:** fails readability. It is a 40-line list of internal milestones ("A primitive finite family
  survives all ordered local flips", "the terminal Bessel circle selects one finite raising grade") which a reader
  cannot place.
- **Boxes 3, 7:** met for the main theorem. **Box 8, "Proof overview":** absent.
- **Length:** 272 pages against a three-page main theorem. The main theorem with its Lean certificate is a short,
  complete note. The length-two programme is unfinished research and belongs in a separate paper once it proves
  something about the chain.

## 3. Hexagon readiness

| Candidate | Proved | Checked by me | New | The one gate left |
|---|---|---|---|---|
| **The chain-length theorem** (with the two-sided M bound and the exact floor (log f)² ≤ m/2 − 1) | yes | yes (22 Nov, against the Lean definitions; reread here) | as a statement about Alpöge's formal interface, yes; a literature and Hexagon search on Alpöge's step 8 is still to be done | **compile the SizesAt bridge against the pinned commit** (or state the theorem for the five displayed inequalities only, which the standalone Lean module already certifies), and write it as a short note with its own abstract |

## 4. How it bears on ALP_MACHINE and on 49b

The theorem is settled, and the run has gone on to the length-two arithmetic, which is the bounded-chain question of
49b. ALP_MACHINE itself has not taken up 49b (its checkpoint-48 intake). So the bounded-chain question is being worked
here, in Part B, not there.

## 5. Edits I suggest outside my folder (not made)

- `reports_20261122\paper_seeds\SEED_ALP_MACHINE.md`, "Setting": replace "the CM field has degree f = 2n" with "f = 2n is
  the degree of the totally real subfield F, and the CM field E has degree 2f".

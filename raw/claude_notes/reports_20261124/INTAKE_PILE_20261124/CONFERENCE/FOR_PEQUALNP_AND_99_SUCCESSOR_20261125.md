**CORRECTION (main session 329fb1e6, 25 Nov ~02:2x UTC):** run 99 had not ended. Its checkpoint 06 was filed at 02:17 UTC (an executor outage had blocked the 01:32 slot), with a 141-page paper and its final readings still outstanding. This note was written from checkpoint 03; reread it against checkpoint 06 and against the final when it comes.

# Rows 17 and 22 of the program: what run 99's final gives

Written 25 Nov 2026 by the conference convener, Claude Fable 5.2 at effort max, for the main session 329fb1e6 (Claude
Opus 5.5 at effort max) to relay. I contacted no other session.

**What I read.** Run 99 (VPVNP_WIRE_GEOMETRY, GPT-6 Astra, ChatGPT Pro mode) at its checkpoint 03 of 24 Nov 23:15 UTC,
which is its final by the user's rule of 25 Nov: `QUESTIONS.tsv` (59 rows; the key rows and every OPEN row in full) and
the review lines of `LEDGER.md`. I did not read its 92-page paper or its proofs. Folder:
`grothendieck_archive_transcription_20261110/research_returns/VPVNP_WIRE_GEOMETRY_checkpoint_03_20261124T2315Z_unzipped`.
Everything else here is from `MAP_COMPLEXITY.md` (Claude Opus 5.5 at effort max), which I read in full.

**Standing hypothesis.** (H_A): Anthropic's Theorem A.6 (cover duality) and Proposition C.3 (the CAT(0) embedding of
prices), from hexagon:2611.00954. Run 99 calls the second "C3" or "the price-space theorem".

## 1. The final state of run 99, row by row

| Row | Final status | Content |
|---|---|---|
| Q1, the square over C | OPEN | Under C3: the unit square is a price ⟺ no planar strict shortening ⟺ lim log_q P_C(q) = √2, the complex Hurwitz exponent. New at the final: a fixed exponent improvement on an unbounded sequence forces a uniform eventual improvement and a four-terminal side-wire cover. Membership undecided. |
| Q2, the centred square | OPEN | Equivalent to Q1. |
| Q1d-7, dimension D ≥ 2 | OPEN | Under C3: the cross-polytope, its centred version, all finite Euclidean D-configurations and the absence of a D-strict shortening are equivalent. Named star and tree families sit at gap 1 − 1/√2. |
| Q3a, shortening ⇒ nonflat | PROVED | Over every field, with the closure version. |
| Q3b, nonflat ⇒ shortening | PROVED_CONDITIONALLY | Dimension by dimension, assuming C3; "independent statement-only reconstruction passed" (the run's own). |
| Q3c, shortening ⇒ contraction | PROVED_CONDITIONALLY | From Q3a and Anthropic's Theorem D.2. |
| Q3d, contraction ⇒ shortening | OPEN | Contraction ⟺ √rank(A − B) on Mat_μ(F₂) is not a price for some μ ≥ 3. That metric embeds in CAT(0); Euclidean maps have sharp squared ratio 2(1 − 2^(−μ)). No passage from this nonprice to a Euclidean one. |
| Q4a | PROVED | A finite complex nonprice has a number-field certificate valid outside the primes dividing an integer D. |
| Q4b | OPEN | The excluded primes for the square: needs a nonprice certificate first. |
| Q4c | OPEN | The bad-prime converse for prices. |
| Q4d, characteristic 2 | OPEN | A Fermat-curve deformation gives exact local rank bounds and a finite two-point reconstruction. A generic count budget cannot improve √2. The full one-particle coefficient span has rank exponent 2. A size-2 span has a smaller finite jet budget and no improving sequence. Left: charged bad-branch recursions and larger symbol classes. |
| Q4e | PROVED | The price cone depends only on the characteristic. |
| Q5c | OPEN | No bound for accounting rules beyond those stated. |
| Q6e | PROVED_CONDITIONALLY | In characteristic 0 a homogeneous highest-weight equation separates at some orbit translate; no occurrence or multiplicity mismatch follows from noncontainment alone. |
| Q7b, Anthropic's Appendices C and D | PROOF_CHECKED_NO_FAULT | Targeted reconstructions; not a rerun of the Lean development. |
| Q7c, OpenAI's direct step | PROOF_CHECKED_NO_FAULT | The cost terms, the selector cost and the 5/4 threshold; not the whole preprint. |

Counts at the final: 23 PROVED, 11 OPEN, 7 PROVED_CONDITIONALLY, 4 PROOF_CHECKED_NO_FAULT, 14 with other labels.

## 2. Row 17: "The square decides", for the pequalnp session

**What changed since `MAP_COMPLEXITY.md` was written.**
1. **The two runs no longer disagree.** The map's problem 1 was that run 98 proves "nonflat ⇒ strict shortening"
   (SH-08) while run 99 listed it as open. Run 99's final has it as Q3b, proved under C3. So the equivalence
   (a) a crossing tensor has a strict shortening ⟺ (b) the Euclidean unit square is not a price ⟺ (c) every price is a
   tree pseudometric now rests on two runs that agree, both under (H_A).
2. **Run 99 audited Anthropic's Appendices C and D** and found no failed step (Q7b). That is a targeted
   reconstruction by the same run, not an outside check.
3. **The square itself is still open** (Q1, Q2), and so is the converse "contraction ⇒ shortening" (Q3d). A note must
   not say that the two papers' dichotomies coincide.
4. **A classical form of the hinge.** Q1 is equivalent, under C3, to the complex Hurwitz exponent being exactly √2.
   The map has the same statement from Liu's hexagon:2611.00994 and run 98's RT-SOS.

**Is the note worth writing now?** Its use: both VP ≠ VNP texts and Liu's noncommutative theorem split on one hinge,
and the note says that the planar hinge is one question about one four-point metric, with a classical equivalent.
Against it: Liu's post of 24 Nov already states the case split, so the increment is the price formulation, (b) ⟺ (c),
and the reduction to four points; and every statement is conditional on unrefereed appendices. My verdict stays: a
short note, after the gates below, by the pequalnp session.

**Gates before a note.**
- A check by a different model of run 98's PG-CROSSPOLY-GATE (`price_geometry.tex` l.583), PG-FOUR-CONDITIONAL (l.166)
  and SH-08 (`shortening.tex` l.417-432), and of run 99's Q3b and its planar reduction. Each run's own
  "independent" reconstruction is by the same model.
- A search of Hexagon and arXiv since 24 Nov for the same equivalence. The field moves in days.
- The abstract names (H_A) and both preprints as unrefereed inputs (`SESSION_2.md`, the rule for abstracts).
- The three bullets of our public mirror that runs 98 and 99 correct (`MAP_COMPLEXITY.md` section 2.6) are corrected
  first, or in the same step. That commit is the main session's decision.

## 3. Row 22: what a successor of run 99 needs

**Why run 99 stopped.** Its ledger set "two successive reviews without movement trigger closure". Its last checkpoint
reports new checked results (the rank-metric price criterion for contraction, the characteristic-two identities with
their finite-cover obstruction), and Q1 and Q4d stayed open.

**What a successor should not repeat.** The reductions are done: Q1 ⟺ Q2 ⟺ no planar shortening ⟺ Hurwitz exponent
√2; nonprices have finite certificates (Q1a-4: an integer-load maximum-linear inequality and a finite cover with a
strict selector gap); the price cone depends only on the characteristic (Q4e); the named star and tree families are at
exact distance (√2 − 1)/2 from the square (Q2c); border-rank and pencil methods cannot decide the square (Q1b-7).

**Three main questions a successor could take, in my order.**
1. **The characteristic-2 square** (proposal 21 of INDEX section 8; Q4d). The permanent equals the determinant there,
   so the hinge has its own form. Run 99 left exact partial results (above) and names what remains: charged bad-branch
   recursions and larger symbol classes. By Q4a and Q4e a nonprice certificate for the square over C would hold in all
   but finitely many characteristics, so characteristic 2 is the one place where the answer may differ. Main
   question: decide whether the unit square is a price in characteristic 2.
2. **Contraction ⇒ strict shortening** (Q3d). It decides whether the two papers' dichotomies coincide. The exact
   obstacle is stated: pass from the nonprice of √rank on Mat_μ(F₂) to a Euclidean nonprice.
3. **A finite certificate for the square over C** (Q1c-4 with Q1a-4), or the proof that none exists. In classical
   terms: is the complex sums-of-squares exponent smaller than √2? By the map's NK-1, a single complex
   sums-of-squares formula with q = 2^r and ⌈log₂ R⌉ < √2·r − 2√(2r) settles it. Since R ≥ q, that needs
   (√2 − 1)r > 2√(2r), that is r ≥ 47: the witness is an asymptotic family, not a small computation.

**Proposal 21 said to give the successor run 98's proof of SH-08.** That is no longer needed as a missing step, since
run 99 has Q3b. Give it both proofs, 98's SH-08 and 99's Q3b, with the instruction to compare them and to state the
result once, in its strongest form.

**What to attach.** Run 99's final (this checkpoint), run 98's newest return, the two preprints, Liu's two posts, and
`MAP_COMPLEXITY.md` with its check events. Which runs are still producing is in `STATE/STATE.md`; VPVNP_HINGE (run 98)
was at checkpoint 07 at 01:14 UTC on 25 Nov.

## 4. What I did not do

- I built no prompt for a successor of run 99. That line belongs to the pequalnp session, and the main question
  should be chosen after run 98 ends.
- I did not read the proofs of runs 98 and 99, the two preprints, or Liu's posts.

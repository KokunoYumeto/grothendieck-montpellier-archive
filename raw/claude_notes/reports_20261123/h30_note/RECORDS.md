# Records for the note H30: the length of the chain of theta lifts

Kept by the editor, Claude Fable 5.2 at effort max (agent a3ccbc11), 23 November 2026. Nothing was sent, posted or pushed.

## The note

- `h30_note.tex`, `h30_note.pdf`: "The length of the chain of theta lifts in Alpöge's proof of the Riemann hypothesis",
  7 pages. pdfLaTeX, three passes (`build_1.log` to `build_3.log`); no overfull box, no undefined reference. All seven
  pages of the first build were rendered at 95 dpi and read; after two small changes (the definition unnumbered; one
  sentence at the end of Section 2) pages 2 and 4 were rendered and read again, and the references checked in the text.
- Statements: Theorem 1 (three parts), Proposition 2 (uniform bounds). Section 2 lists the five inequalities with file
  and line in the source; Section 4 says what the Lean module certifies and what the uncompiled bridge would add.
- Suggested deposit fields: subject math.NT; keywords: Riemann hypothesis, Dirichlet L-functions, theta lifts, unitary
  groups, CM fields, Lean formalization, size hypotheses. Text origin and human understanding as for our first deposit.

## Literature, with locators

| Source | Locators used | How it was read |
|---|---|---|
| L. Alpöge, *Remark*, 20 Nov 2026, alpo.ge/remark.pdf | p. 1 (multiplicity from chained theta lifts; a chain of length √X for the von Mangoldt sum of length X); p. 3 (he expects short arguments to follow); p. 4, step 8 (the chain between totally definite unitary groups; m like √X) | all four pages, by me (20 and 21 Nov) |
| The Lean development (repository CocoSgt/riemann-hypothesis-lean, revision 7cbf7a0c32fca1badf05931879a37c3f8a2b03b4), `src/Formalism/` | `LocalRingCardinality/Params.lean` 6–24 (structure Ranks), 28 (n), 30 (f), 38 (rS); `LocalRingCardinality/DataParams₂.lean` 9–16 (structure Scale), 27 (L), 29 (b), 45 (delta1); `SharpRestriction/ElevenLe.lean` 11 (szTh), 24–25 (SizeN), 27–29 (SizeM), 31–33 (SizeK), 35–49 (SizeKRel; line 44), 123–125 (SizeG), 134–138 (SizesAt) | by me, as text, in the copy distributed at alpo.ge on 20 Nov (`literature\alpoge_rh_20261120\lean_tree`). The pinned revision was inspected by the producing run and by the first checker; its recorded line ranges agree. Nothing was built or run. |
| M. Jaswal, hexagon:2611.00799v1 (54 pp.) | p. 2 (error smallest at m ≈ √x; his Remark 3.6); p. 6 ("Why m ≈ √x"; Section 4.1); p. 4 ("for large x" means beyond a threshold depending on the family, ε and the character) | PDF fetched 23 Nov from hexagonmath.org/pdf/2611.00799v1; text extracted; keyword search; the passages read. Not read in full. |
| R. Zhang, hexagon:2611.00809 (65 pp.; the file served is stamped v2) | p. 4 (bounds on arbitrarily large intervals suffice); p. 9 (errors of sizes x/m and m; m close to √x); pp. 10, 58 (Lemma 6.1; x^{1/2−ε} ≤ m ≤ x^{1/2+ε/2}); p. 25 (k = dim X₀; m the number of lifts; both even); pp. 43, 51 (f = [E⁺:Q]) | as above |
| S. Slijepčević, hexagon:2611.00812v1 (94 pp.) | p. 4 (chain of length about √y); p. 11, (H3) ([E:Q] = 4·#A); p. 31, Definition 6.3 (the scale; (Sc1) x^{2+8ε} ≤ #A ≤ 2x^{2+8ε}; (Sc2) √(xδ₁) ≤ m ≤ 2√(xδ₁)); p. 32, Lemma 6.4 (m ≤ 2x^{1/2−ε/16}) | as above |
| twinheterodox, hexagon:2611.00828v1 (10 pp.) | p. 1 (the construction of the lifts and the estimates producing the intervals enter as inputs); p. 2 (the original argument supplies the fields and the estimates for the lifts) | as above; searched for "lift", "input", "size" |
| Our note hexagon:2611.00789 | cited as a companion on another passage of the remark | written by me |

The list of neighbouring Hexagon posts is the main session's (public list checked 23 Nov, about 12:35 UTC; nothing
newer than 2611.00829 is public). I made no search of my own on Hexagon or arXiv.

## The pass: how the note stands to the neighbouring posts

- **Overlap.** Part (1) of Theorem 1, the square-root size of m. It is Alpöge's choice (step 8), and all three guides
  explain it; Slijepčević prints the size conditions of a scale. The note credits them and claims only the exact
  exponents of the cited revision. His (Sc2) has the window [1, 2]·√(xδ₁), the hypothesis (M) has
  [x^{−θ}, x^{θ}]·√(xδ₁); they are consistent, since x^θ = L^{1/100} > 8 for admissible data.
- **Beyond them.** Part (2) (the bound (log f)² ≤ m/2 − 1; no chain of two lifts; m ≥ 20), part (3) (the absolute
  bounds) and Proposition 2. Not found in any of the four texts by keyword search (patterns for SizesAt, the
  logarithmic condition, explicit thresholds, bounded or short chains, m = 2).
- **Superseded or corrected.** Nothing either way.
- **2611.00828** takes the lifts as inputs, so its three simplifications leave the size hypotheses as they are.
- **Kind of note:** needs a pass; the pass is done.

## Checks, by model and effort

| Statement | Date | Who | Type | Outcome |
|---|---|---|---|---|
| Theorem 1 in its first form (absolute bounds; two-sided bound for m) | 22 Nov 2026 | Claude Opus 5.5 at effort high (abcaba9b) | targeted proof check, against the Lean definitions | confirmed (as its intake of 23 Nov records) |
| Theorem 1 in the run's final text | 23 Nov 2026 | Claude Opus 5.5 at effort high (abcaba9b) | used and rechecked | no fault |
| The numerical implication, 15 statements | 23 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode), the producing run | computation or formal certificate | standalone module, Lean 4.33.1 with the Mathlib of the pinned revision; exit 0; axioms propext, Classical.choice, Quot.sound; module sha256 f6219e24…0950ad (the run's log and run record, read by me as text) |
| The same module | 23 Nov 2026 | Claude Opus 5.5 at effort high (abcaba9b) | carried as background without fault found | statement list read; not built |
| Theorem 1 (1)–(3) and Proposition 2 | 23 Nov 2026 | Claude Fable 5.2 at effort max (a3ccbc11) | independent re-proof | confirmed; every exponent recomputed by hand |
| The five inequalities against the source | 23 Nov 2026 | Claude Fable 5.2 at effort max (a3ccbc11) | targeted proof check | confirmed: each is a conjunct or half of a conjunct of SizesAt, with the unfoldings szTh = ε/100, delta1 = x^{−ε/8}, b = exp L, L = x^ε, f = 2n, rS = m/2 − 1 in ℕ |
| The fields of the Lean module's structure against the displayed hypotheses | 23 Nov 2026 | Claude Fable 5.2 at effort max (a3ccbc11) | targeted proof check | they are the same hypotheses |
| "m ≥ 20" in Theorem 1 (2) (editor's addition) | 23 Nov 2026 | Claude Fable 5.2 at effort max (a3ccbc11) | computation or formal certificate | by hand: (log m)² = 1.92, 3.21, 4.32, 5.30, 6.17, 6.96, 7.69, 8.35 for m = 4, …, 18, each above m/2 − 1; (log 20)² = 8.974 ≤ 9 |
| The bridge from SizesAt to the module's structure | 23 Nov 2026 | Claude Fable 5.2 at effort max (a3ccbc11) | carried as background without fault found | read as text; agrees field by field with the table of Section 2; **not compiled by anyone** |

**Faults found:** none. **Changes against the run's text,** all in presentation or by addition: the corollary on
f = 42, f = 168 and L = 343 is dropped (values from our own experiments); the family statement is given in its simple
form, with the threshold form in Section 4; x > 2^15600 and L > (36 log x)^{100/101}, which the Lean module proves,
are stated; "m ≥ 20" is added; each symbol is named with a locator in the guides.

## Whom to write to when it is posted (information only, no request; the user's call)

- **L. Alpöge.** The note concerns the hypotheses of his formal development. A line should say that it is a remark on
  the size of the parameters, not on the proof.
- **R. Zhang, M. Jaswal, S. Slijepčević.** Their guides are cited for the square-root law and for the meaning of the
  parameters. Optional.

## What is left before posting

1. The user's look at the PDF, and the user's word.
2. The deposit sheet (the fields above; the abstract as printed).
3. Optional: compile the bridge against the pinned revision. The theorem as stated does not depend on it.
4. Optional: a full read of Jaswal §4.1, Zhang §6 and Slijepčević §6, to firm up "not found in them".

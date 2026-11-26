# SQUARE: provenance, checks and literature search

The note: "The square decides: one four-point price for strict shortening, flatness and the crossing exponent".
- Row 17 of the conference program.
- Files: `src/SQUARE_paper.tex`, and `SQUARE_paper.pdf` (9 pages).
- Written on 25 Nov 2026 by Claude Opus 5.5 at effort max (copy af3258db of agent a4348514), for the pequalnp session
  672ae3a0 (Claude Opus 5.5 at effort max).
- The user gave that session the VP/VNP line and said to go ahead; the main session 329fb1e6 relayed this.
- Nothing has been posted or sent.

## Who produced what

**The runs.** Both are runs of GPT-6 Astra (OpenAI, ChatGPT Pro mode). Their prompts were written by Claude Opus 5.5 at
effort max: run 98 by agent a4348514, and run 99 by the main session.
- **Run 98**, `VPVNP_HINGE`: final checkpoint 12, 25 Nov 2026 04:59 UTC.
  Folder: `research_returns/VPVNP_HINGE_checkpoint_12_20261125T0459Z_unzipped`.
- **Run 99**, `VPVNP_WIRE_GEOMETRY`: final checkpoint 09, 25 Nov 2026 04:32 UTC.
  Folder: `research_returns/VPVNP_WIRE_GEOMETRY_checkpoint_09_20261125T0432Z_unzipped`.

**Where each result comes from, and which proof the note gives.**

| Note | Run 98 | Run 99 | Proof given here |
|---|---|---|---|
| Theorem A | SH-02, SH-03, SH-04 (`shortening.tex` l.178-279) | Q3a, lem:terminal-selector, thm:shortening-nonflat (`shortening.tex` l.10, l.97) | run 99's selector argument, with the simpler bound M_ν ≤ A^n by the writer |
| Theorem B | PG-SQUARE-GATE (`price_geometry.tex` l.515) | thm:tree-price-dichotomy (`tree_prices.tex` l.23); thm:introplanar (`planar.tex`, Remark 2.3) | run 98's tangent-cone argument |
| Lemma 2.4, flat rectangles | — | lem:rectangle (`planar.tex` l.12) | run 99's |
| Lemma 2.6, rigid ball | SH-07 (`shortening.tex` l.360) | — | run 98's |
| Proposition 2.7, extremal | — | thm:crosspolytope-shortening, Q3b (`shortening.tex` l.196); thm:square-shortening-equivalence (l.115) for D = 2 | run 99's |
| Proposition 2.8 | PG-CROSSPOLY-GATE (1)⇒(3) (`price_geometry.tex` l.583), with Kirszbraun | lem:cross-polytope-flat (`planar.tex` l.103), by tangent cones and parallel sets | run 98's, which is shorter |
| Theorem C | PG-CROSSPOLY-GATE; SH-08 (`shortening.tex` l.427) | Q3b; thm:cross-polytope-price-flat | — |
| Theorem D | — | thm:crossing-exponent-dichotomy (`crossing_exponent_gap.tex` l.13); thm:square-pt-exponent (`cycle_search.tex` l.102); lem:pt-upper (l.52); cor:square-hurwitz (l.194) | run 99's |

**Due to the writer:**
- **Lemma 2.10, two hubs.** The explicit bound F(β) ≤ 4 − (1 − β/√2)², with hubs at ±(t,t) and t = (1 − β/√2)/2. It
  replaces run 99's prop:optimal-crossing-hubs, which the gate-1 check had carried as an unchecked input.
- **The separation of hypotheses in Theorem D:**
  - (ii), "square a price ⇒ lim inf ≥ √2", needs only C3;
  - (i), "square not a price ⇒ ρ = 1", needs C3 and A6;
  - (U) enters only for (iii).
- **The cycle of implications in Theorem B,** (1)⇒(5)⇒(4)⇒(3)⇒(2)⇒(1).
- **The text.**

## Checks

**Gate 1** (25 Nov 2026, the writer, as a different model from the runs). Recorded in
`<local>/pequalnp_work/square_note/GATE1_CHECK_20261125.md` and `CHECK_EVENTS_GATE1_20261125.tsv`, 18 events.
- Every run proof condensed here was checked step by step on the runs' texts.
- Each final was compared with the version first read.

**Anthropic's statements opened by the writer at their locators** (text of hexagon:2611.00954):
- Def. 2.1 and Def. D.1, Def. A.1, Lemma A.2, Def. A.4;
- Thm A.6, Prop. C.3 (with the definition of a price space just before it), Lemma C.4(a),(b),(f);
- §D.3.

**OpenAI's statement opened by the writer:** Definition 2.1, `build/Paper.tex` l.203-211.

**Corrections of record,** also stated in the note:
- Run 99's register row Q3b says "assuming the price-space theorem", that is, C3 alone. The proof,
  thm:crosspolytope-shortening, also uses cover duality, A6.
- The header of run 99's thm:square-pt-exponent ("the unit square is a price iff the crossing exponent is √2") names C3
  alone. Its first direction uses A6, through the cover in thm:square-shortening-equivalence.

Run 99 reconstructed A6 itself (Q1c-1). That reconstruction is by the same model, so the note treats A6 as an input.

**Not checked by the writer:**
- The upper bound (U), P(q) ≤ q^{√2+o(1)}. Run 99 derives it from Anthropic's Prop. B.2 (the integral crossing identity)
  and Khoruzhii's symbol-class counting.
- Run 98's width bounds SH-60b and SH-38, and its exponent items, which the note does not use.

**Writing.** Every proof in the note was re-derived while writing. Two of them differ from the runs' texts:
- Lemma 2.1 uses M_ν ≤ A^n in place of the multinomial bound.
- Theorem D(ii) uses Lemma 2.10 in place of run 99's hub proposition.

**Build.**
- Three pdflatex runs until stable: 9 pages, no errors, no undefined references, no overfull boxes.
- Every page was rendered at 72 dpi and looked at.
- One wording fix and a small bibliography font were applied after the first look.

No human has checked the note.

## Literature search (25 Nov 2026, about 15:50-15:55 UTC, the writer)

**Hexagon catalogue**, `https://hexagonmath.org/api/v1/works?q=<word>`. The number of works returned per query:

| Query | Works |
|---|---|
| VNP | 2 |
| permanent | 20 |
| price | 8 |
| shortening | 1 |
| Hurwitz | 14 |
| squares | 20 |
| spectral | 20 |
| flatness | 3 |

Hits bearing on the subject:
- **hexagon:2611.00954**, Anthropic, "VP ≠ VNP over every field": the source of C3 and A6.
- **hexagon:2611.00994**, Liu, "Stretched-exponential circuit lower bounds for the noncommutative permanent and
  determinant".
  - It states the case split on a planar strict shortening.
  - It derives the √2 lower bound for the two-cut (sums-of-squares) quantity from the absence of a planar strict
    shortening (TeX l.132-143), with Khoruzhii's upper bound.
  - It does not state the price form, the planar-flatness equivalence or the exponent-one branch.
- **hexagon:2611.00972**, Liu, "A uniform exponent bound for asymptotic tensor rank". It applies Anthropic's price
  machinery (Def. A.4, Thm A.6, Prop. A.7) to asymptotic rank; it is not about the square.

The other hits are unrelated: Hurwitz polynomials, Markoff–Hurwitz equations, the mean-field matching "price", spectral
gaps, and so on. 2611.00149 (ETH refutations) and 2611.00090 are about counting algorithms.

**Web search**, two queries:
- *"strict shortening" Euclidean square price spectral point VP VNP crossing exponent*: nothing relevant.
- *partial transpose rank crossing tensor exponent sqrt 2 Hurwitz sum of squares complex 2026*: found Rossman–Zhu,
  "Multiquadratic sum-of-squares lower bounds imply VNC¹ ≠ VNP" (arXiv:2512.01227, ITCS 2026, LIPIcs 362, art. 113).
  - It covers PT-rank and the correspondence of multiquadratic polynomials with partially transpose-symmetric matrices.
  - It reports a complex sums-of-squares construction of Hrubeš with O(n^{1.62}) terms, which the note does not cite: the
    writer did not open it.

No statement of Theorem B, Theorem C or Theorem D(i) was found.

The search covered titles and abstracts (Hexagon) and search-engine results (web), not full texts. Earlier in the day the
pequalnp session's search, at 02:1x UTC, had found nothing beyond Liu's two posts.

## Citations

| Opened by the writer | Not opened by the writer |
|---|---|
| [Ant] at the statements listed above | [BH]: locators Ex. II.1.15(5), Prop. II.2.2, Cor. II.3.6 and Thm II.3.19 as given by run 98; Prop. II.3.1, the strong limit of comparison angles, recalled by the writer |
| [OAI], Def. 2.1 | [BN], the quadrilateral inequality; the note also cites [Ant, Lemma C.4(b)] for it |
| [Liu1], TeX l.45-52, l.74-76, l.132-143 | [LS] and [AKP, Thm 5.4], the Kirszbraun theorem, as given by run 98 |
| [Liu2], abstract and l.57-73 | [HWY], as cited by run 99 and [Liu1] |
| [RZ], the abstract through the search engine | [Kh], as cited by [Liu1] |

## Open items

**Not claimed by the note:**
- which branch holds, over any field;
- that the two preprints' dichotomies coincide. Q3d, contraction ⇒ shortening, is open, and [Ant, §D.3] says the cases
  are not shown to exclude each other;
- any explicit decomposition in the exponent-one branch.

**Inputs:** C3 and A6 (unrefereed), and (U) for Theorem D(iii).

**Possible additions,** not made:
- Run 98's statement-level width bounds: no strict shortening of width m ≤ 6, in any dimension (SH-60b); planar two-term
  shortenings need width ≥ 8 (SH-38).
- Run 98's four-point classification, PG-FOUR-CONDITIONAL. It relies on an outside theorem, Wigderson–Zuiddam 2025
  Thm 12.23, which was not opened.

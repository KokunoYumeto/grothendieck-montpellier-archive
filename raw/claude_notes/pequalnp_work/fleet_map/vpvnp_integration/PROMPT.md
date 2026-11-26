# VP ≠ VNP: decide the wire geometry that both proofs leave open

Prepared by Claude (Claude Opus 5.5 at effort max, agent a4348514ce0275bbf) on 24 November 2026, for a research run
that writes its paper as it goes. The attachments are listed at the end. Read them before you start.

## What this is about

Two proofs of VP ≠ VNP appeared on 23 and 24 November 2026. No human mathematician has checked either; read them as
claims.

- **Anthropic, "VP ≠ VNP over every field"** (attached `anthropic_vp_vnp_paper.pdf`, 70 pages; its Lean statement
  `Statement.lean`).
  - Theorem 1.1: every circuit for HC_m, and for PERM_m outside characteristic two, has more than m^{c (log m)^{1/3}}
    gates.
  - Theorem 1.4: the same holds for circuits over k((ε)) that approximate.
- **OpenAI, "VP and VNP are different"** (attached `openai_vp_vnp_Paper.tex`).
  - Theorem 1.1: border circuits for its family f_n need exp(Ω((log n)^{5/4})) gates.
  - Corollary 1.2: the permanent, the Hamiltonian cycle polynomial, border determinantal complexity, and the padded
    permanent against the determinant orbit closure.

**Both proofs trade the same two kinds of hardness against each other.**

- **If wires in tensor networks cannot be priced below Euclidean length** (Anthropic: the *flat* hypothesis, Definition
  2.1; OpenAI: *no strict shortening*, Definition in Section 2, lines 203-211 of the TeX), the argument is direct. A small
  circuit splits the coefficient tensor of a clause sum over balanced cuts. A hub moved toward the resultant of the wires
  crossing a cut then saves length, which is impossible.
- **If wire can be saved** (Anthropic: *contracting*; OpenAI: *strict shortening*), a small circuit accelerates sums over
  the runs of short programs, and a diagonal argument refutes it.
  - Anthropic's contracting case gives 2^{Ω((log m)^2/log log m)}.
  - OpenAI's Theorem 1.3 (stretch) gives 2^{n^σ}.

**Neither paper decides which case holds.** Anthropic: "We do not know which of the two hypotheses holds, even over R,
nor do we show that the two are mutually exclusive." OpenAI states its stretch theorem conditionally. This run decides it.

## The questions

**Q1 (main question).** Over the complex numbers, and over the field with two elements, decide the following:

- **(Q1a)** Construct a strict shortening in the sense of OpenAI's Definition, or prove that none exists for any D ≥ 2
  and m ≥ 1. The definition: a finite sum identity, using A networks in the unit ball each of cost at most w, for the
  tensor C_{D,m} of width-m cables on the D coordinate diameters, with w + 2D log₂ A < 2Dm.
- **(Q1b)** Which of Anthropic's two hypotheses of Definition 2.1 holds:
  - *contracting*: for some n ≥ 2, every price on Mat_n(F_2) falls short of a Euclidean rectangle by a fixed factor in
    the mean squared distances of rank-n against rank-1 steps;
  - *flat*: every finite subset of a Euclidean space is a price up to ε and scale.

  Decide also whether the two hypotheses exclude each other.
- **(Q1c)** Whether the two dichotomies coincide, that is, whether a strict shortening exists exactly when the
  contracting hypothesis holds.

**Q2.** Determine exactly which pseudometrics are prices over C, and over F_2:

- on three, four and five parties;
- on the cross-polytope {±e_1, …, ±e_D} together with its centre.

Prices are pointwise limits of scaled wire metrics of spectral points, Anthropic `def_price` and `lem_exponents`. Decide in
particular whether the Euclidean unit square (sides 1, diagonals √2) is a price.

**Q3.** Determine the exact supremum of the exponents α for which the direct case of either proof yields
2^{Ω((log m)^α)}. Prove the construction that attains it and the limit beyond which the hub-displacement method cannot go.
The stated values are 4/3 (Anthropic, complete network) and 5/4 (OpenAI, expander).

## The state on 24 November 2026

These facts are on record. Check each before you build on it, and record the check in `CHECK_EVENTS.tsv`.

1. **Theorem 2.2 of Anthropic (`thm_alt`):** one of the two hypotheses holds over every field. The route is the
   following. Prices satisfy the Bruhat-Tits inequality (`thm_cn`, from the crossing identity `prop_identity` and
   `prop_crossing`). They are induced by maps into CAT(0) spaces (`prop_random`, `prop_space`). If contraction fails,
   compactness gives flat quadrilaterals, and the flat-rectangle property puts cubes into prices.
2. **The explicit spectral points over C** are the flattening ranks and the quantum functionals of Christandl, Vrana and
   Zuiddam. On a product of wires all marginals are uniform, so a quantum functional with weights θ gives the wire metric
   δ(x, y) = θ_x + θ_y, a star metric. A flattening rank across A gives the cut metric of A.
   - Neither realizes a Euclidean square up to scale. A star metric would need θ_1 + θ_2 = 1 from the sides and
     θ_1 + θ_2 = √2 from the diagonals. Cut metrics take only the values 0 and 1.
   - On Mat_n(F_2) a star metric has 2E[θ^2] ≤ E[δ(x, x+y)^2] ≤ 4E[θ^2] at every rank of y. So its rank ratio is at
     most 2, which is the contracting side.
   - So the flat case needs spectral points beyond the known families. Anthropic's come from Zorn's lemma
     (`prop_gauge`).
3. **Matrix multiplication does not contradict flatness.** ⟨n,n,n⟩ is a restriction of a star of rank n^ω, which forces
   perimeter ≤ ω min_h Σ_x |x h| on triangles. In Euclidean space perimeter ≤ 2 min_h Σ_x |x h|, and ω ≥ 2.
4. **One network cannot shorten C_{D,m}.** Crofton's formula bounds the integral over hyperplanes of log rank across
   each hyperplane. The bits of the diameters cross every hyperplane through the ball, and the integral gives the direct
   cost 2Dm. A shortening must therefore be a sum of networks whose cheap cuts differ from term to term.
5. **A shortening and flatness meet only at small scales.** A spectral point realizing the ball configuration at scale
   λ (δ = |x - y|/λ) is subadditive over the A networks of a shortening, so λ ≥ (2Dm - w)/log₂ A. A strict shortening
   therefore excludes flat realizations only at scales λ ≤ 2D. Whether the two dichotomies coincide is Q1c.
6. **The exponent of OpenAI's direct case.** The saving is m·u·√(γd) with u = b/√d. Selection costs O(d^2) and must stay
   below a constant times m = c log n, so d ≍ √(log n), and the bridge must exceed (log n)^{5/4}. Anthropic's 4/3 comes
   from the complete network, where every balanced set is crossed by ≥ 2n^2/9 wires, and a sharper count of the bits
   that name a balanced set (`lem_few`, `prop_cube`).

Facts 2 to 6 are paper arguments by Claude Opus 5.5 at effort max, made on 24 November 2026 and not yet checked by a
second reader. Treat them as statements to check, not as known results.

## Routes

Take them in this order. Move to the next whenever one stalls.

- **R1, identities that beat Euclidean length (toward contracting and a shortening).** Search for asymptotic
  restrictions among wire networks with hubs, placed in R^D. The sources of identities are:
  - matrix multiplication and its border degenerations;
  - the graph tensors of Christandl, Vrana and Zuiddam;
  - W- and GHZ-type degenerations;
  - the explicit 18-, 19- and 20-term curves of the attached `border_rank.tex`;
  - sums over A layouts with selectors, OpenAI's device;
  - Anthropic's two-crossing-wire identity as the two-dimensional building block.

  For each identity compute the inequality it forces on prices, and test it against Euclidean metrics on the
  configuration. One configuration on which the Euclidean metric fails the inequality proves contracting through
  Theorem 2.2. Then decide whether it also yields a strict shortening (Q1c).
- **R2, new spectral points (toward flat).** Construct spectral points beyond the quantum functionals on graph tensors.
  - Candidates:
    - moment polytopes of the tensor on enlarged party sets;
    - limits along one-parameter subgroups;
    - Kempf-Ness functions and geodesics in the symmetric space GL/U, which is CAT(0) like Anthropic's prices;
    - Strassen's support functionals beyond oblique tensors.
  - Test each on the Euclidean square first (Q2), then on the cross-polytope with its centre.
  - The attached invariant theory of 3-tensors computes exactly these polytopes and their vertices: the three `GCT_POS_*`
    files (polystable tensors, grading stabilizers, SL_n^3-invariants) and the vertex-denominator results.
- **R3, certificates that no identity exists (toward flat), or that every spectral point contracts.** To prove the flat
  hypothesis on a configuration, show that no asymptotic restriction violates its Euclidean inequality. The lower-bound
  tools are:
  - border apolarity, Koszul flattenings, and the substitution and torus-degeneration methods of `border_rank.tex` and
    the BR_PENCIL sections;
  - the image substitution with an injective-norm certificate (GCT_GINEQ F-13) and its exact reduction F-23.

  Strassen's duality, in Anthropic's form `thm_duality`, is the bridge between identities and spectral points. State
  precisely the version you use: in particular, whether a point on the subsemiring of wire networks extends to all
  tensors.
- **R4, the field.** Decide the question first in characteristic two, where Mat_n(F_2) and the field meet, then over C.
  - Our attached bridges ALPOGE_GCT B7.1-B7.2 transfer separations from characteristic zero to all but finitely many
    primes. B7.3 shows the reverse transfer can fail. Use them for the passage between characteristics.
  - If the answer depends on the field, prove both answers.
- **R5, metric geometry.** The contracting hypothesis is a strict Enflo-type (Poincaré) inequality for rank steps on
  Mat_n(F_2), required of every price. Use what is known about Enflo type and Markov type of CAT(0) spaces. A Euclidean
  cube is CAT(0) and fails the strict inequality, so the decisive class is the prices, not all CAT(0) metrics.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of
the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the
smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach
stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter
search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then
push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step:
mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three
hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every
checkpoint): every open row with its status, and for each main question its current gate (the strongest proved
reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller
gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two
consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it;
this check takes precedence over the sentence above about untried approaches.

**Each item is decided only by a proof.**

- Q1a is decided by an explicit shortening with every coefficient and every cost checked, or by a proof that none
  exists.
- Q1b is decided by a proof of the contracting hypothesis for an explicit n and an explicit factor, or by a proof of the
  flat hypothesis. Add a proof or a refutation that the two exclude each other.
- Q1c is decided by a proof of the equivalence, or by a field and a configuration that separate the two dichotomies.
- Q2 is decided by the exact description of the price cone on each listed configuration, with proofs of both
  inclusions.
- Q3 is decided by the exact supremum, with the construction and the matching limit.

**When the work is finished.** Only when every item and every lettered part is proved (a) or refuted (b). Keep working
until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much
has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of
`VPVNP_HINGE_report.md` reads INCOMPLETE. Its table then marks every undecided line with the state reached, every approach
tried with where it failed, and the next step you would take. Never present such a return as complete or as following an
allowed alternative: there is none.

**What follows from your results.** If either claimed proof is correct, record what your answers give it. A shortening
gives OpenAI's 2^{n^σ}. Contraction gives Anthropic's 2^{Ω((log m)^2/log log m)}. Flatness gives a shortened proof through
the direct case alone. Each consequence carries the hypothesis "if the claimed theorem is correct".

**If you find an error in either claimed proof,** state it exactly: the passage, the statement it needs, and a
counterexample or the missing step. It is a result of this run.

## The paper

Write the paper as you work, in LaTeX: `VPVNP_HINGE.tex` and its PDF.

- **Every finding goes in with its full proof:** every new statement of this run, positive or negative, and every
  computation with the program that produced it.
- **Known results are cited with exact locators, never re-proved.** Each citation names the theorem, section and page of
  the source: the two claimed papers, Strassen's asymptotic spectrum, Christandl-Vrana-Zuiddam, the border-rank
  literature, and the CAT(0) and Enflo-type literature. Write a short proof only of a form that the source does not state.
- **Keep checked and unchecked findings in separate parts.**
- **Every proof is checked before the final package.** The check is a targeted proof check, an independent re-proof, or a
  computation or formal certificate, recorded in `CHECK_EVENTS.tsv`. A proof that fails its check goes into the paper as
  a failed proof, with its gap.
- **The two claimed papers are cited as unrefereed claims.** No priority claim is made for anything.

**Check events.** For every statement, record its check events in CHECK_EVENTS.tsv: statement id, date, who (model,
effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked
in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. Each type
says what happened, neither overclaimed nor understated.

## Deliverables and checkpoints

- **The final package** is one ZIP holding:
  - `VPVNP_HINGE.tex` and `VPVNP_HINGE.pdf`;
  - `VPVNP_HINGE_report.md`: a table of every item and lettered part with its outcome and the location of its proof;
  - `PROGRESS_LEDGER.md`;
  - `CHECK_EVENTS.tsv`;
  - every program, with its input and output files.
- **Checkpoints.** Save a checkpoint ZIP once every 45 minutes of work. Save it as a ZIP, never a JSON file. Checkpoints
  are written at one rhythm: once every 45 minutes and at no other time. Each checkpoint ZIP holds the current
  deliverables and documentation; earlier checkpoints are not copied into it. Name them `VPVNP_HINGE_checkpoint_NN.zip`,
  numbered in order.
- **If the session breaks.** If the session breaks or a checkpoint fails to save, the last saved checkpoint ZIP is the
  state of the work. Start again from it and redo what you had done after that checkpoint.
- **No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
  copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
  fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
  deliver (proofs, programs, tables, the paper) always goes in.

## Attachments

- `openai_vp_vnp_Paper.tex`: OpenAI's paper, the LaTeX source from openai/math, commit of 24 November 2026.
- `openai_vp_vnp_references.tex`: its bibliography, `build/references.tex` of the same folder.
- `anthropic_vp_vnp_paper.pdf`: Anthropic's paper. No TeX was released.
- `anthropic_vp_vnp_Statement.lean`: Anthropic's Lean statements.
- `GCT_GINEQ.tex`: norms, image substitution (F-13) and the exact residual reduction (F-23).
- `border_rank.tex`: the border rank of the det_4 and per_4 coefficient tensors. It contains the substitution
  inequality, the torus and lower-ideal reductions, border apolarity and the explicit degenerations.
- `BR_PENCIL_substitution.tex`, `BR_PENCIL_pencils.tex`, `BR_PENCIL_permanent_apolar.tex`: three sections of BR_PENCIL.
  They hold the generalized border substitution (R-01), coordinate minima (P-01), order ideals (P-07), and the
  necessary-prolongation condition proved before R-04.
- `GCT_POS_KRONECKER_FINDINGS.tex`, `GCT_POS_AMPLIFYING_GADGET.tex`, `GCT_POS_AMPLIFIER_FULL_STABILIZERS.tex`: three files
  of GCT_POS. They hold the invariant theory of 3-tensors (the K-series) and the vertex denominators of Kronecker
  polytopes (K-018, K-020).
- `ALPOGE_GCT_bridges.tex`: the bridges B3.1 to B7.3, on norm obstructions and the transfer of separations between
  characteristics.
- `VPVNP_INTEGRATION_20261124.md`: our reading of the two claims against our material, from which facts 2 to 6 above
  are taken.

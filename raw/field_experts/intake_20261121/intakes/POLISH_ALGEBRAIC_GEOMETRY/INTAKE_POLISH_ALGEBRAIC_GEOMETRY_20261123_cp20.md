# Intake by diff: POLISH_ALGEBRAIC_GEOMETRY, checkpoint 12 → checkpoint 20

By Claude Opus 5.5 at effort high (agent a018e2d2, the field expert of this run), 23 Nov 2026, ~18:30–19:40 UTC, in
the evening intake wave (`INTAKE_WAVE_20261123_EVENING.md`). The run is GPT-6 Astra (ChatGPT Pro mode); its records
give its effort only as "inherited reasoning settings". It is **still running**: review 12 (15:00 UTC) found movement,
checkpoint 20 was saved at 16:00 UTC, and the no-movement streak is 0.

The previous intake is `INTAKE_POLISH_ALGEBRAIC_GEOMETRY_20261123_cp12.md`. Since then, P90a was posted as
hexagon:2611.00936 (WB-0003). Work file: `agent_notes/a018e2d2e3e7a279f_NOTES.md`.

## 0. Scope: what I read

Checkpoints present: 16, 17, 18, 20. Checkpoint 19 was not downloaded. I read **checkpoint 20**, diffed against
checkpoint 12. I read the ledger entries of checkpoints 13–20 in full (from "Checkpoint12 saved" to "Stronger adjoint
draft installed", 15:53 UTC).

**Diff of the papers' TeX:**
- Papers 1, 3, 4 and 5 are **byte-identical** to checkpoint 12.
- Paper 2 grew from 49 to 85 pages:
  - eight new inputs;
  - `projective_bundles.tex` rewritten (567 diff lines);
  - `main.tex` revised (abstract, Section 1, Further questions, method, bibliography);
  - `k3_picard_constraints.tex` touched (5 lines).

**Read in full, every step rederived:**
- `canonical_subsystem_strictness.tex`, all of it: Prop. residual-adjoint, Lemma negative-cotangent-adjoint, Cor.
  divided-differential subsystem, and the **proof of Theorem strict-picard-all**;
- the two proofs in `very_ample_picard_constraints.tex` (the small-degree curve-genus lemma; the numerical
  obstruction, through the cases r ≤ 3 — the r = 4 case is not shown in my excerpt);
- the `main.tex` additions.

**Statement level:** the statements of every proposition, corollary and lemma in:
- `positive_genus_picard_fibration.tex`;
- `equality_torsor_euler.tex` (I recomputed its Euler formula independently; see §1);
- `characteristic_two_rational_cover.tex`;
- `rational_canonical_equality.tex`;
- `positive_genus_separable_picard.tex`;
- `ruled_picard_cover.tex`.

**Not read:** the rewritten proof in `projective_bundles.tex` (the arbitrary-base theorem), statement only.

**Opened at the source:** Kweon, arXiv:2008.01908v2, §7, pp. 17–19
(SHA-256 6b51c49d120ff37682ddacc8e40e3ae1a64bf129b2d886476be8122b7970d9f9).

**Not opened:** Langer (Ann. Inst. Fourier 2011), Zhang (JPAA 2023), Kadets (arXiv:1809.07293), Catanese–Oguiso, and
Gu–Sun–Zhou. They are cited by the run; I took them at statement level.

The register (REGISTER.tsv, now 1,570+ rows) was not checked row by row, as before.

## 1. What is new, usefulness first, with verdicts

### 1.1 Theorem strict-picard-all (Paper 2, Section 1; proof in `canonical_subsystem_strictness.tex`)

**Statement.**
- Hypotheses: X is a smooth projective surface over an algebraically closed k of characteristic p > 0, and Y ⊂ X is a
  smooth integral very ample curve.
- Conclusion: if a line bundle M ≠ O_X of order p restricts trivially to Y, then
  - 2g(Y) − 2 > pY²;
  - |K_X − (p−2)Y| contains a subsystem with two-dimensional image;
  - so K_X − (p−2)Y is big, X is of general type, and its canonical map has surface image.

**What it is good for.** It gives necessary conditions for the one open half of Kweon's Question 7.7: is restriction of
Picard groups to a smooth hyperplane section injective on points? That is also Grothendieck's Picard-point question
(A2), which the run carries from the Montpellier dossiers. A reader working on Lefschetz theorems for Pic in
characteristic p (Kweon; Cotner–Zavyalov; Langer) would want it.

It is not an answer: no example and no exclusion. Its two parts are:
- the strict inequality excludes the equality 2g − 2 = pY² allowed by the conductor identity;
- the adjoint part forces the surface to be of general type with a "big" canonical map.

The general-type consequence alone is a known deduction (Ekedahl II.1.6; Langer–Zhang); the run credits it.

**My check (targeted proof check, confirmed for the parts below).**
- **Prop. residual-adjoint, in full.** I checked:
  - p | m, from the order-(m−1) term m·dt∧η of dω;
  - the gluing identity t_i du_i − u_i dt_i = v²(t_j du_j − u_j dt_j);
  - d((u/s)ω) = s^{m−2}γ(u), using m − 1 ≡ −1 (mod p);
  - the kernel of u ↦ γ′(u) is ks;
  - no fixed curve, and nefness;
  - the surface-image argument: a curve image B ≅ Y with g ≥ 2 makes the generic fibre Γ ≅ P¹_F, with ω_R|_Γ of degree
    −2, against a nonzero section of degree −2 − (m−2) − deg Z|_Γ < 0;
  - A² = P² − E_b² > 0.
- **The final assembly of the theorem.**
  - In equality the divided form is nowhere vanishing (degree 0), so Z = 0 and L = K − (p−2)Y has L² > 0.
  - Positive-genus base:
    - L² = −12(g−1)/p − (p−2)d − c₂ ≤ 4(p−3)(g−1)/p − (p−2)d (I recomputed it, using c₂ ≥ 4(1−g), b₁ = 2g,
      b₂ ≥ 2);
    - p = 2 gives ≤ −2(g−1);
    - p = 3 gives −d;
    - p ≥ 5, with Riemann–Hurwitz pd ≥ 2b(g−1) and b ≥ p+2, gives ≤ −((p−1)² + 1)d/(p+2).
  - Rational base:
    - p ≥ 5 is excluded by the rational-canonical proposition;
    - p = 2 lands in the numerical obstruction;
    - p = 3, ε = 0 gives L² = 4 − d − c₂ ≤ 1 − d;
    - p = 3, ε = 1 gives c₂ = 8 − 2d ≥ 3, so d = 2 and g = 4, against a very ample degree-2 bundle on Y.

  All the arithmetic checks.
- **Euler formula** χ(O_N) = pχ(O_X) − p(p−1)a((p+1)a−3)Y²/12: I recomputed it independently. Graded pieces of
  numerical class (aY)^i for 0 ≤ i < p, with K·Y = (ap−1)Y², summed by Riemann–Roch, give exactly this formula.
- **Inputs used at statement level** (not checked by me):
  - the conductor identity (Prop. normalized-mup-conductor, from checkpoint 12);
  - Ekedahl's reduction to an almost ruled surface and the K3 exclusion (Kadets);
  - the distinguished ruled cover;
  - the positive-genus fibration and its separability;
  - the rational-canonical proposition;
  - the r = 4 case of the numerical obstruction.

**Verdict:** confirmed given those inputs, which the run has checked (its CHECK_EVENTS: targeted proof checks PASS; the
characteristic-2 strict case has a statement-only reconstruction; the **odd-characteristic statement-only
reconstruction is still pending**).

### 1.2 Lemma negative-cotangent-adjoint (new, general)

**Statement.** H very ample on a smooth projective surface S, a > 0, Z ≥ 0, and 0 ≠ α ∈ H⁰(Ω¹(−aH−Z)). Then
|K + (2−a)H − Z| has a subsystem with surface image.

**Mechanism.** The wedges α∧(s_i ds_j − s_j ds_i) are the Plücker coordinates of the tangent line ker α_x. A curve image
would sweep S by lines, and on such a line the twisted cotangent bundle Ω¹(−aH−Z) has no section.

**Verdict:** targeted proof check, confirmed. It is short and self-contained.

**Use:** a clean bigness criterion from negatively twisted 1-forms in characteristic p. Its novelty has not been
searched.

### 1.3 Theorem torsor-projective-bundle (Paper 2, `projective_bundles.tex`)

**Statement.** Over **every** base scheme (before checkpoint 12: only normal bases), P_Q(E) is a scheme iff the abelian
torsor Q is a scheme.

**Use:** it closes the projective-bundle route to counterexamples for Picard schematicity (E4).

**Verdict:** statement only. The run has a successful second isolated reconstruction (using that worker's own
normal-base proof); two attempts are frozen as unsuccessful.

### 1.4 The P90a surface and Kweon's question (the integration of this wave)

The run's Section 1 now cites Kweon. I read Kweon §7 at the source:
- Thm 7.6 (p. 18): for a smooth ample effective D, the restriction r(α_p) is injective iff H¹(O(−D)) = 0;
- p. 18: he expects Pic X → Pic H can fail to be a closed embedding in characteristic p;
- p. 19: he knows no very ample D with H¹(O(−D)) ≠ 0;
- Q7.7.

**So our posted P90a answers the closed-embedding half of Kweon's Q7.7 negatively, and supplies the example he did not
know.** This raises P90a's usefulness. Both arguments are confirmed by me: the tangent kernel H¹(L⁻¹) ≠ 0 rules out a
closed immersion, and Thm 7.6 gives a nonzero α_p in the kernel. The integration is applied: `p90a_note_v2` (see §4).
Kweon should be written to.

### 1.5 Other changes

- **The run's own refinements**: the distinguished ruled cover, the positive-genus fibration (rational double points,
  separability, Albanese map an isomorphism, M nonzero in NS[p], nontrivial on the generic fibre), the degree
  filtration, the rational-cover canonical defect ≤ 1, the characteristic-2 strict bound g ≥ Y² + 2, and a p = 3
  projection step. All are **subsumed** by Theorem strict-picard-all for very ample Y. Several remain conditional
  statements for merely ample Y, at the scope given in the paper's last section. The superseded p = 3 projection
  branch was removed from the paper and kept in the records.
- **New dossier entries** (the run's, not checked by me; CORRECTIONS_FOR_AUTHORS.md):
  - Catanese–Oguiso (author copy, three intermediate slips, pp. 16–17);
  - Kleiman, *The Picard scheme*, Remark 5.8 (precision);
  - Gu–Sun–Zhou, p. 620 (a sign and an omitted fixed divisor) and locators;
  - Shepherd-Barron, genus-change subtraction;
  - FGA Exposé 221, Lemma 3.5 (already published);
  - Stacks Tag 0AGS (a reversed quotient; theorem unchanged);
  - two composition-order slips in our attached EGA edition (IV 8.10.5(xii), 8.5.2(ii));
  - Stacks 54.12, case I.
- **Withdrawn or refuted since checkpoint 12:** no statement of the papers. Earlier failed reconstruction attempts are
  preserved as failures.

**Verdict counts** (my events in this wave): 7 targeted proof checks confirmed, 1 computation (the Euler formula
recomputed), 1 source check (Kweon), 0 refuted, and 8 statements at statement level only.

## 2. Scope of the inputs

- The strict theorem rests on Ekedahl I.2.4(ii) (read by the run and by our cp12 intake at the dossier level) and on
  Kadets, Prop. 2.8.
- Langer, Theorem 9.1 gives the neighbouring slope bound pY² ≤ μ_max,Y(Ω¹) under the same hypotheses; the run
  compares the two correctly in the text.
- Cotner–Zavyalov, Cor. 3.1.2 needs a Hodge 1-equivalence, which P90a shows very ampleness does not give.
- Every one of these is published. Kadets's arXiv v4 is the published JLMS paper.

## 3. Integration

**Applied by me** (with backups in `integration_backups/20261123/POLISH_ALGEBRAIC_GEOMETRY/`; the rows are in
`INTEGRATION_POLISH_ALGEBRAIC_GEOMETRY_20261123.tsv`):
1. `reports_20261123/p90a_note/p90a_note_v2.tex` and `.pdf`: a new file made from the posted text, with the Kweon
   paragraph, Corollary 2, the open item, the method note and the bibliography. 10 pages, 0 overfull boxes. v1 is left
   as posted.
2. `reports_20261123/p90a_note/RECORDS.md`: §6, the Kweon addendum and whom to write to.
3. `intakes/POLISH_ALGEBRAIC_GEOMETRY/INTAKE_POLISH_ALGEBRAIC_GEOMETRY_20261123_cp12.md`: a status addendum.

**For the main session** (shared registers, returns and prompts; not edited):
- the board: update P90a and add rows P90b–P90d (§5);
- whether to post `p90a_note_v2` as v2 of hexagon:2611.00936, and to write to Kweon;
- the cp12 intake's edits to our earlier runs' files, all still unapplied, because they lie inside returns:
  - SA17 `A_finish_L1_general.tex:248` (fixed-base openness refuted);
  - SA12 `paper_A.tex:33,94` (31/085 → sheet 84);
  - the SA06 "14:38" locators;
  - E4 57:315 → 57:314;
- HEXAGON_CANDIDATES: P90a has been posted.

## 4. Prompt updates (for a finishing prompt of this run)

1. Complete the odd-characteristic statement-only reconstruction of Theorem strict-picard-all and the current-PDF
   readings (85 pages).
2. Split Paper 2. The A2 / Picard-kernel material (now about 35 pages) is a coherent paper on its own: "Picard kernels
   of very ample curves in characteristic p, after Kweon's Question 7.7". It should open with Kweon Q7.7 and P90a's
   answer to its second half.
3. Paper 2 should cite hexagon:2611.00936 for the very ample surface, rather than repeating it in full, once the run
   knows it is posted (the run cannot be reached after 1–2 h; this belongs in a finishing prompt).
4. "Proof overview" sections are still missing in all five papers (HOW box 8).

## 5. Hexagon readiness and board candidates

| id | Title | Statement | What it adds | Tests | Gate left |
|---|---|---|---|---|---|
| P90a (update) | A very ample counterexample to Kodaira vanishing on a surface, answering a question of Raynaud | as posted, plus Cor. 2: Pic_Y → Pic_H is not a closed immersion; a nonzero α_p in the kernel | answers Kweon Q7.7(ii) negatively and gives the example Kweon (p. 19) did not know | all five pass for v2 (checked: tangent argument + Kweon Thm 7.6 at source) | the user's word to post v2; an e-mail to Kweon |
| P90b | Picard kernels of very ample curves: a strict genus bound in every characteristic | Thm strict-picard-all (above) | necessary conditions for Kweon Q7.7(i) / Grothendieck's Picard-point question | complete: yes; self-contained: yes; **stable: no** (the run is still moving on A2; the theorem was restructured three times today); checked: assembly and adjoint by me, inputs by the run only | the run's final; an intake read of the inputs (conductor identity, Ekedahl reduction, positive-genus fibration, rational canonical); the odd-p reconstruction |
| P90c | Big adjoints from negatively twisted one-forms on surfaces | Lemma negative-cotangent-adjoint plus Prop. residual-adjoint | a tangent-line criterion for bigness of K + (2−a)H − Z in any characteristic | complete, self-contained, stable, checked (by me) | a literature search (Shepherd-Barron and Langer on unstable cotangent sheaves; Ekedahl II); interest is moderate |
| P90d | Projective bundles over abelian torsors are schemes only over schematic torsors, over every base | Thm torsor-projective-bundle | closes a route to counterexamples to Picard schematicity | checked by the run only | an intake read of the proof; literature (Raynaud 1970; Brion) |

P90a's posted v1 stays correct. v2 only adds.

## 6. For the P vs NP fleet

No new result of this wave bears on complexity. The Picard kernels, adjoint systems and torsor schematicity have no
node in `PROOF_GRAPH.tsv`. The existing map **AG-06** (`maps/algebraic_geometry.md`: P90a and Theorem 2/3 marking where
characteristic-2 vanishing fails, onto L-gct-025, the reduction mod 2 and specialization of smoothness) stands
unchanged.

One constructed map, for completeness:
- **Source:** Paper 2 Theorem 1.1 (G1, unchanged since checkpoint 12): the integral transvections T_v act on quadratic
  refinements of the Weil pairing on A[2]; no refinement is invariant once the rank is at least 4.
- **Target:** the AG-05 bridge onto **L-pcx-071** (route M, node M3: Arf maps on theta characteristics).
- **Translation:** G1's invariance argument is the statement that Sp(2h, 𝔽₂)-transvections act on refinements with two
  orbits (Arf 0 and 1), and with no fixed point for h ≥ 2.
- **Work to complete:** state pcx's covering statement on affine flats of odd theta characteristics as an assertion
  about transvection orbits.

Not graded.

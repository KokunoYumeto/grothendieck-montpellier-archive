# Concrete editorial corrections: dossier sections 3.4–3.5, 6.1–6.4, 7–8

Reviewed against the numbered transcriptions and saved B/root/C proof checks on 19 November 2026. The main dossier was not edited. These are typing and hypothesis corrections to the text presented for review; they do not change the proved conclusions or require new proofs.

## 1. Section 3.4: identify the disputed domain correctly

The phrase “between all one-forms and all holomorphic functions” misidentifies the Pro/Codex disagreement. The target is the one-form sheaf in both witnesses. Pro reads the source as the local-coordinate sheaf `E_X`; Codex reads it as all holomorphic functions `O_X`.

Suggested replacement: “The Pro/Codex disagreement between local coordinates and arbitrary holomorphic functions as the domain of g ↦ dg−df changes the surjectivity statement.”

Evidence: `pro/MPL_93_047-091_transcription.tex:1033–1034`; `codex/K93-08_transcription.tex:504`; C-SA04-206; `parts/b/proof_checks.md`, §1. For fixed coordinate f, the form −df cannot be dg−df with g a coordinate, whereas local integration proves surjectivity with g an arbitrary holomorphic function.

## 2. Section 3.4: state the domain of the root/primitive formula

Before displaying c_n, specify a nowhere-vanishing local differential `f(dt)^n` with `n ≠ 0`. The displayed denominators and n-th-root construction have these hypotheses. This is especially useful because the following paragraph discusses a separate conditional zero-index interpretation.

Suggested replacement: “For a nowhere-vanishing local n-differential f(dt)^n with n a nonzero integer, in the complex analytic setting, the root-and-primitive construction gives …”

Evidence: `parts/b/proof_checks.md`, §2; C-SA04-213–214. The displayed coefficient itself is correct.

## 3. Section 3.5: distinguish D from its composite with the quotient

The display `D=Δd_E` is not correctly typed for the Manin equality. The source first defines `D₀=Δ∘d_E:E→F`, then descends it through the quotient `v:E→E″` to `D:E″→F`.

Suggested display: `ν(Δ)=μ(D),  D∘v=Δ∘d_E`, with v identified as the quotient. Equivalently retain the source's D₀ notation and write `D₀=D∘v`.

Evidence: `codex/K93-02_transcription.tex:211–215`; `parts/c/analysis.md`, §11.1; `parts/root_computation_notes.md`, Manin comparison. Both proof notes already use the correctly typed relation. The statement and present-status fields of C-SA04-620 repeated the same shorthand at the review snapshot and should receive the same correction. The root agent acknowledged this correction during the review.

## 4. Section 3.5: state the scalar Jacobson-formula hypotheses

The displayed formula `(D+c)^p=D^p+c^p+D^(p−1)(c)` should explicitly take D to be a derivation of a commutative characteristic-p ring and c to act by scalar multiplication. Read immediately after a paragraph about general integrable connections, an unqualified c could be mistaken for an arbitrary endomorphism-valued connection coefficient, for which this scalar formula is not the stated theorem.

Suggested introduction: “For a derivation D of a commutative ring of characteristic p and c acting by multiplication, the Jacobson formula …”

Evidence: the universal commutator/Bell-coefficient proof in `parts/root_computation_notes.md`, Cartier section, explicitly imposes exactly these hypotheses. No change to that proof or its finite certificates is needed.

## 5. Section 3.5: distinguish the two pairing cases

Start the pairing paragraph with “For a smooth curve in characteristic p …”. Qualify the Pfaffian comparison by “for odd p”. In characteristic two the quotient has rank one and its perfect self-duality instead gives the theta-characteristic relation `Q² ≅ ω_(X′)`; a Pfaffian on an even-rank alternating bundle is not that case.

Evidence: C-SA04-632 and C-SA04-634; `parts/root_computation_notes.md`, Cartier section; Raynaud1982 §4.1. The antidiagonal condition and the p=5 determinant counterexample are correctly stated in the dossier.

## Event-refinement clarification requested during this review

All nine B main-ledger refinement targets are intentionally **item IDs**. They are not missing `C-` prefixes. Each named item contains the corrected or precisely qualified statement. No new claim IDs were needed.

| Refuted formulation record | Refinement item | Exact content of the refinement |
|---|---|---|
| C-SA04-201 | SA04-202 | The unused direct summand defeats unrestricted target isomorphism; target generation must be specified, without claiming it alone proves classification. |
| C-SA04-208 | SA04-209 | Horizontal-frame connection differences have the minus-dlog sign. |
| C-SA04-210 | SA04-211 | The logarithmic-ratio factor is f/g, and the later square is inversion-invariant. |
| C-SA04-214 | SA04-215 | The second input in the mixed coefficient uses f′/f. |
| C-SA04-227 | SA04-228 | The quadratic-input coefficient includes the linear f term and coefficient 5/4. |
| C-SA04-232 | SA04-242 | The canonical equivariant jet/matrix comparison is obstructed at two and splits via trace/2 after inverting two. |
| C-SA04-235 | SA04-244 | The non-two field comparison survives; the characteristic-two Lie automorphism group has dimension six. |
| C-SA04-242 | SA04-250 | Killing duality needs two invertible; the elliptic extension gives a counterexample otherwise. |
| C-SA04-246 | SA04-255 | The source's later two-invertible restriction restores innerness; the characteristic-two derivation is outer. |

`programs/b_events.py` and `parts/b/CHECK_EVENTS.tsv` were updated to label these targets explicitly as items and state the corresponding refinement in each outcome. The generator now uses the straight-apostrophe event enum. There are still 234 main B events, and the refreshed generator output is `outputs/b_events.json`. In particular, SA04-255 exists and is the intended item; no C-SA04-255 was invented.

# C.3bl: complete combined source and finite-check scope

The final combined proof is `C3_full_higher_integral_kernel.tex`, promoted and registered 2026-11-19T15:25:24.043590+00:00; it inputs the complete final `agents/frobenius/C3_primitive_exceptional_boundary.tex`. The mathematical claim is exact-order-p ordinary integral restriction kernels for all r≥2,N≥2r over every algebraically closed field of characteristic p. The universal integral injectivity corollary uses C.3aw in its exact lower-field scope and C.3bh for divisors. No rational conclusion is drawn.

## Exact proof provenance

The geometric/Picard construction and its original seven-step proof are fully written in C.3bk. The new combined proof checks each auxiliary hypothesis and supplies the arbitrary-r,m=0 tensor witness and very-ample Bertini argument. All choices occur in nonempty finite-type opens over finite fields, which provides a terminating specification rather than an executed uniform search.

The included primitive-boundary auxiliary proves its entire five-step assertion. It reduces the exact exceptional kernel to integral Smith torsion, annihilates the saturation through the free lattice tensor(Pic(W_i)/Z A_i), and treats the remaining canonical-curve-line products by a lift-independent additive relative differential on divisible Pic⁰(C)(k). The literal Chow projection identity and finite smooth-model Milnor product comparison are explicit. This replaces the safe-range assumption of C.3bk; it does not discard exceptional torsion or substitute numerical equivalence.

Our full independent proof/source review is `C3bl_primitive_boundary_independent_REVIEW.md`. It includes a separate pass of the retained Witt-lift alternate, while identifying the integral quotient as the proof actually used in the final auxiliary. The old Witt draft and its compiled artifact remain under the Frobenius agent directory. No invalid inference was silently removed; the final proof uses fewer inputs.

## Fresh primary source inspections for the auxiliary

The reviewer `/root/real_weil` freshly read the complete exact primary statements and proofs:

1. Stacks37.4.1, Tag0C6R, the square-zero Picard obstruction sequence: https://stacks.math.columbia.edu/tag/0C6R . It is applied one first-order stage at a time.
2. Stacks30.24.3, Tag0885, projective formal existence over a Noetherian complete ring: https://stacks.math.columbia.edu/tag/0885 . Invertibility is checked on the closed fibre and then everywhere by properness.
3. Stacks30.8.1–30.8.2, Tag01XS, full projective-space cohomology and base-change calculation: https://stacks.math.columbia.edu/tag/01XS . Together with the cubic equation/Euler sequence this gives the ambient twisted-cotangent H¹ vanishing and hence μ_A=0. The same source also validates the retained alternate Witt calculation, not required by the final proof.
4. Stacks15.51.14, Tag0AH2, regularity of completion of a G-ring: https://stacks.math.columbia.edu/tag/0AH2 . The base is excellent.
5. Stacks16.12.1, Tag07GC, Popescu: https://stacks.math.columbia.edu/tag/07GC . This is the exact regular-to-filtered-smooth theorem used.
6. Stacks32.10.3(2), Tag0B8W, invertible-sheaf descent with inverse/isomorphism: https://stacks.math.columbia.edu/tag/0B8W . The finite data include the prescribed first jet.
7. Stacks15.13.3, Tag0H74, smooth henselian lifting: https://stacks.math.columbia.edu/tag/0H74 . Applied to the henselian pair (R,m²), it preserves the specified quotient map.

Fresh retrievals: turn977473220view0–2 and turn842242711view0–3. The source statements are not claimed to contain this combined local-cycle theorem verbatim.

## Exact earlier-this-window source inputs reused

`C3bk_SOURCE_AUDIT.md` records the newly opened Jiang published Theorems2.4/2.8(3) and Section1.2 integral/ground-field conventions, Stacks02TX, and the exact prior Rost/Kerz/Braunling source inspections. The individual Bertini lemma is Stacks33.47.3, Tag0FD6, not merely its containing section0FD4. Its immersion hypothesis holds for the complete external very-ample system, including m=0.

The all-characteristic ordinary-quartic, Brion integral Ext, Illusie mixed obstruction, actual Poincare curve family and Elkik endpoint comparisons were proved and source-audited in C.3bg/bj/bk; the new combined proof checks the dimension-independent hypotheses explicitly. The final primitive quotient uses only the integral cubic Picard lattice and μ_A=0; no crystalline/characteristic-zero comparison is imported.

Existing bibliography files are reused without duplicate keys: `agents/cycles/references.bib`, `agents/cycles/k2_cohomology_references.bib`, `agents/real_weil/C3bi_references.bib`, `C3bj_references.bib`, `C3bf_references.bib`, `agents/frobenius/K2_relative_Milnor_references.bib`, `C3_smooth_exceptional_references.bib`, and `C3_primitive_exceptional_references.bib`.

## Retained exact finite computation

Program: `code/check_C3bl_primitive_boundary.py`.
Complete output: `code/check_C3bl_primitive_boundary.out`.
Structured output: `output/C3bl_primitive_boundary_certificate.json`.

Run started2026-11-19T15:22:58.888027UTC and finished15:22:58.932012UTC; runtime0.04399013499642024seconds;44passes,0failures. It directly multiplies the integral primitive quotient Ψ by every one of the nine retained ample-multiplication matrices from the cycles lattice certificate, including the cases with Smith factors3,9,27. It checks exact local positive-adjoint chains and the no-projective-space tensor witnesses for s1..9. It retains hashes of the precise input matrices/certificate and does not rerun or overwrite those inputs.

These are finite coefficient checks. The arbitrary-dimensional lattice argument, actual families, cohomology divisibility, finite-stage descent and existence of smooth geometric choices are proved in prose and independently audited. No universal theorem is inferred solely from the numerical samples.

## Standalone assembly

The complete combined draft and included auxiliary compiled in four successful passes at2026-11-19T15:23:13.376604UTC, runtime3.36067072100559seconds, with no undefined citations or overfull diagnostics. Full pass outputs and the machine-readable build record are retained under output. This is an assembly check, not a substitute for the complete proof audits.

# Independent whole-proof and final-fragment review: F56 formal bar

Reviewer: /root/gct_statements, GPT-6 Astra Pro. Inherited effort setting is not exposed. Date: 2026-11-21 UTC.

## Exact reviewed texts

- agent_formal_bar_kernel.md, SHA256 6dbc03af0b390d8b671e31b8b26ce45fa66937d5cc1497e111bed06c1f457c6c.
- finding_F56_bar.tex, SHA256 df2c113c5ea3c152e12795b8687e17aff7af22216c29ebb4c9778b39d118424c.

Verdict: **PASS**, with no mathematical correction requested. I read both complete texts directly, reconstructed all displayed tensor and evaluation maps, and matched the entire generated fragment to the report. This is a mathematical proof review, not formal verification or an automated theorem check.

## Independently reconstructed checks

1. **Variance and matrix order.** For entrywise finite graded duality, the pairing of \(\phi\otimes\psi\) with \(u\otimes w\) gives the stated tensorator on each fixed intermediate-state summand. It preserves the state indices and the order \(K,L\). The contravariant naturality identity (B3) has correctly typed source and target. A state transpose is not concealed in the coefficient symmetry.

2. **Strong monoidality and the involution.** Both triple-product coherence routes give the same product of three scalar evaluations on the same flattened path; the unit maps are compatible. The tensorator
\[
\mu^{(2)}_{K,L}=B(\mu_{K,L})^{-1}\mu_{BK,BL}
\]
has the correct variance. Evaluation \(K\to B^2K\) is monoidal, and \(B(\eta_K)\eta_{BK}=1\) follows by actual evaluation, not by merely selecting abstract double-dual isomorphisms.

3. **Specified forms.** The forms on \(A_1,A_2\) pair opposite degrees and are symmetric, nondegenerate, and degree zero. Their tensor product on \(D=A_1^{\otimes2}\) pairs the two separate degree-zero labels with each other. The formulas retain those labels. Product and orthogonal-sum forms yield self-dual identifications for each unshifted word. General shifts reverse, so closure of the positive word categories is valid without claiming every shifted object is self-dual.

4. **Quadratic, degree-five, and ordered-overlap maps.** The F56 maps are built from path flattening, summand permutations, and ordinary coefficient permutations. Each preserves the relevant product pairing. I checked the first-branch permutation \((1\,2)(3\,4)\), the second-branch position map \(1,2,3,4\mapsto3,4,1,2\), and its two \(U,V\) interchanges. The isometry equation rearranges to
\[
\theta_C^{-1}B(r)\theta_{C'}=r^{-1}
\]
with the correct directions. In arbitrary shifted contexts, the report correctly uses the dual contexts \(BH,BJ\). Only unshifted word contexts receive the displayed self-dual forms. This fixes the possible overstatement that all contexts are self-dual.

5. **Actual algebra and state bar.** The character of the entrywise dual substitutes \(v^{-1}\) for \(v\), without reversing matrix multiplication. The row-category comparison has the same state-path tensorator and satisfies the same coherence. F43's already proved bar-fixed tensor basis therefore identifies the resulting decategorified bar with the actual semilinear bar on the specified localized lattice. No statement about VIII's original unlocalized lattice is inferred.

6. **Adjoint and arithmetic boundaries.** The transpose-dual adjoint has different matrix support, so F56's exclusion of those adjoints is unaffected. The coefficient forms are symmetric bilinear forms, not positive Hermitian forms. The arithmetic transport is the internal coefficient duality transported through F53; the report correctly avoids identifying it with ambient Verdier duality or a single-weight estimate for a mixed object.

## Scope of this review

The proof check used the complete F56 construction and the previously checked F43 bar comparison. I did not rerun a numerical computation because these new identities are tensor-evaluation identities proved directly. The exact EGA/SGA/archival framework locators in the dictionary were matched between report and fragment, but their original pages were not newly reopened during this review. No new source theorem is attributed to those framework locators.

The final paragraph leaves the correct open comparison: global/local lattices, designated simple labels, and compatible graded constructions through all ranks are not supplied by the formal bar.

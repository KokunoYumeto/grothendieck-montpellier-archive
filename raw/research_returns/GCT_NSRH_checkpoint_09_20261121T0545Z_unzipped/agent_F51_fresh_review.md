# F51 independent complete proof and fragment review

Reviewer: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; reasoning effort not exposed.
Date: 2026-11-21 UTC.

Targets read in full:

- `agent_algebraic_trace_gate.md`, SHA256 `b1401f002d2c4857fe7dc8b0e995f9f4165065beac08680e06e0a98a1dc4405f`.
- `agent_algebraic_integral_weight_supplement.md`, SHA256 `a65c96a19617bb74fc159a619642e1dd3be7dea5bfc08331fd3be1b6fe5f3f56`.
- Complete generated `finding_F51.tex`, SHA256 `dd6ff1c0c6f89999e5307dc85ba4f5defbe6d47dd9aa803e1cd2953f5ebfd3e1`, including its separate Grothendieck dictionary and all scope paragraphs.

## Result

**PASS. No mathematical correction required.** I independently reconstructed every proof in the base report, the several-integral-weight supplement, and the generated fragment. The fragment contains the complete stated arguments and preserves their distinct hypotheses.

## Independent reconstruction

1. For the radial lemma, expanding each polynomial `P_i(u_n)` produces a finite power sum on unit-modulus roots. Multiplication by `b^{in}` places different `i` in disjoint absolute-value classes. Equal roots are grouped first. A relation at every sufficiently large consecutive integer has zero coefficients by an ordinary Vandermonde argument, including the nonzero diagonal factor from the starting exponent. Therefore every grouped subrelation vanishes for all integer sequence indices. Evaluation at the auxiliary index zero yields `P_i(u_0)=0`, so `Y-u_0` divides the irreducible polynomial. The coefficient multiplying this factor is a nonzero constant because the polynomial is irreducible in `C[v,Y]`. This proves the asserted constant relation without selecting a branch or using an asymptotic expansion.

2. The genuine spectrum inference is correct: the normalized ordinary trace is eventually the dimension, and equality in the triangle inequality makes every unit-modulus summand equal one at each such exponent. Two consecutive exponents give each eigenvalue one. Equivalently, grouped positive multiplicities cannot cancel. The proof explicitly avoids claiming recovery of virtual eigenvalues that cancel between degrees.

3. The normalization `v^{-w}` is an algebraic/rational operation because the single weight is integral. A regular evaluation of the fixed algebraic trace satisfies its one irreducible relation even if a different allowed sheet is selected at each extension parameter. The trace comparison becomes precisely the power trace of the normalized base operator. The resulting nilpotent `G_b-I` lies in the center of its full centralizer. A semisimple finite-dimensional complex algebra has reduced center, so this nilpotent vanishes and the full centralizer is a single matrix algebra. This excludes the actual nonsimple semisimple generic algebra under the stated additional comparison, at every auxiliary rank.

4. For several integral weights, the expanded relation groups by the integer exponent `r=i+sum(w_j)`. Within each group all remaining factors have modulus one, so the same uniqueness argument applies. At sequence index zero, the group coefficient is exactly the coefficient of `v^r` in `P(v,p(v))`. Thus the Laurent polynomial `p(v)=sum(c_j v^{w_j})` is a rational root of the irreducible minimal polynomial, and the algebraic trace itself equals `p`. The argument is correctly conducted over `C(v)` when weights are negative; it does not silently discard Laurent denominators. Positive genuine multiplicities then exclude every nontrivial phase. This extension is valid for signed coefficients at the level of the visible grouped sequence as well, with exactly the stated limitation.

5. Trace retuning alone does not determine the other characteristic coefficients. The fragment separately imposes full spectral retuning to identify them. For each algebraic coefficient, substitution of the corresponding Laurent coefficient into its polynomial relation vanishes at infinitely many distinct `b^n`, hence vanishes as a rational function. Irreducibility identifies the coefficient. This gives the displayed characteristic polynomial without a continuous sheet, common eigenvalue labeling, or fixed diagonalizing basis.

6. At a regular fixed-rank specialization above `v=1`, that characteristic polynomial becomes `(T-1)^N`. The previously checked cyclic-module argument for a nilpotent centralizer gives a local center, so it cannot be the actual collision center with three components. The proof requires the full centralizer and regular fixed-rank model. It does not exclude faithful subalgebra actions, decorated objects, the fixed-parameter constructions, or a different arithmetic comparison.

## Scope and source check

The fragment clearly distinguishes the trace-only single-weight conclusion from the full-spectrum collision conclusion. It does not claim family-wide unipotence from the trace-only hypothesis. All evaluations remain values of one irreducible algebraic relation with fixed constants. The auxiliary sequence index zero is correctly separated from a nonexistent degree-zero finite-field extension. The inverse quantum-parameter convention changes the normalization as stated.

The integral-weight hypothesis is substantive and correctly retained. The example of a Kummer family with fractional spectral exponents is explicitly outside this supplement, rather than being mislabeled as an object with integral Deligne weights. Arbitrary magnitudes and collision contact orders are not classified here.

The separate dictionary uses the already audited exact EGA I affine locators, SGA3 I 4.7.2–3/cote90 scan17 action vocabulary, and BBD weight conventions. VIII §2.2 p7 is the previously directly inspected source for its allowed algebraic parameter-field extension. No new historical attribution, external theorem proof, numerical experiment, or formal proof-kernel verification is claimed. The proof itself uses only the displayed elementary polynomial and matrix arguments, together with previously proved F19/F48 inputs.

No main TeX was edited. This review does not cover the later F52 theorem under construction.

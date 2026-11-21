# Fresh review of F51: algebraic trace retuning

Reviewer: /root/rectangular_and_theta. Review date: 21 November 2026 UTC.

Reviewed report: agent_algebraic_trace_gate.md.

Reviewed SHA256: b1401f002d2c4857fe7dc8b0e995f9f4165065beac08680e06e0a98a1dc4405f.

## Verdict and scope

**PASS.** I freshly read the entire report, including the evaluation convention, every proof, the actual-centralizer application, and the limits in Section 5. I independently reconstructed the radial-separation argument and the nilpotent-centralizer deduction. No mathematical correction is needed.

This review checks the new elementary deductions, not a new independent proof of the previously reviewed F19 structure theorem. F19's actual generic rank-three algebra is used exactly in its established form. No numerical test, formal proof kernel, or unreviewed algebraic-function continuation theorem is involved.

## 1. Irreducible algebraic relation and arbitrary branches

A finite collection of algebraic matrix entries generates a finite extension of the rational function field. Its trace is therefore algebraic. Clearing the minimal polynomial's denominators and taking the primitive irreducible representative gives a single relation in C[v,Y]. Every regular evaluation of the same algebraic family satisfies this relation. The proof needs neither continuous branch selection nor compatible eigenvalue labeling.

This distinction is substantive: changing branches of the same irreducible relation is permitted; changing the relation with the extension degree is not. The report states exactly this boundary.

## 2. Radial separation reconstructed

For each polynomial coefficient P_i, expansion of P_i(u_n) produces a finite sum of powers of products of the unit-modulus roots. These products are nonzero and still have modulus one. The polynomial's constant term is represented by the root one. Grouping equal products leaves finitely many distinct roots.

After multiplying by b^(in), roots coming from different indices i have distinct moduli b^i, because b>1. Roots within one index were already grouped. The assumed identity for all sufficiently large consecutive integers consequently vanishes as a finite exponential sequence: a Vandermonde matrix on a sufficiently long consecutive interval is invertible after multiplication by a nonzero diagonal matrix.

Thus every grouped coefficient is zero, and each expression P_i(u_n) vanishes for every integer n. Evaluating the finite sequence at n=0 gives P_i(u_0)=0. Polynomial division by the monic polynomial Y-u_0 then shows that it divides P(v,Y) in C[v,Y]. Irreducibility makes the quotient a nonzero constant. Hence the algebraic function is constant and the original finite sequence is identically u_0.

No asymptotic limit or choice of a branch at infinity is hidden in this argument. The value at zero is only a value of an explicitly defined exponential sequence; no finite-field extension of degree zero is asserted. The hypothesis of all sufficiently large extension degrees is used in the Vandermonde step and is not silently weakened to an arbitrary unbounded subsequence.

## 3. Genuine spectrum and normalization

For an actual rank-N matrix with unit-modulus eigenvalues, the trace sequence has u_0=N. The equality of its sum to the real number N forces each summand to be one, by equality in the triangle inequality. Applying this at two consecutive sufficiently large integers gives each eigenvalue equal to one. Equivalently, grouped finite-power-sum uniqueness proves the same statement.

Positive genuine multiplicities are exactly what recovers all eigenvalues. A virtual trace may hide cancelling eigenvalues; the report does not apply this conclusion to such a trace.

For a single integral weight w and Q=b^2, multiplication of the family by v^(-w) is an allowed algebraic operation. At v=b^n, its trace becomes b^(-nw) Tr(F_b^n), which is the power trace of b^(-w) F_b. The radial lemma therefore applies to the normalized trace relation, yielding the constant normalized family trace N and a unipotent normalized base operator.

The report correctly stops short of claiming that trace retuning alone determines the characteristic polynomial at every other parameter.

## 4. Full centralizer consequence

The nilpotent G_b-I lies in the center of the full intertwiner algebra of G_b: every intertwiner commutes with both G_b and the identity. If that algebra is semisimple, its center has no nonzero nilpotents, so G_b=I. Its full centralizer is then the single simple algebra M_N(C).

For b>1, the actual F19 algebra is the semisimple nonsimple product C × C × M_2(C) × M_2(C). It therefore cannot be this full centralizer under the stated trace-retuning and single-weight conditions, at any auxiliary rank.

This uses the full centralizer, not an arbitrary subalgebra of an endomorphism algebra. It does not rule out the fixed-parameter F46 realization, a faithful action in pure coefficients, a mixed-weight algebraic family, or a family of varying coefficient objects.

## 5. Final scope checks

- The same irreducible algebraic family is retained throughout.
- Different allowed branches at different parameters are genuinely covered.
- Only ordinary trace retuning is assumed; spectral retuning is sufficient but unnecessary.
- Single integral weight is imposed only at the base operator.
- No regularity at the collision parameter is used.
- Neither mixed-weight algebraic classification nor generic unipotence of the entire matrix family is claimed.
- The inverse-parameter version is a change of coordinate followed by the same integral normalization.
- The entire argument is compatible with algebraic extensions of Q(v) after a complex realization of the finitely many coefficient data.

These qualifications match the report's stated use for VIII's algebraic coefficient conventions. The result strengthens the prior rational single-weight gate without asserting a general nonstandard RH or a general obstruction to tensor coefficient realizations.

## 6. Fresh review of the several-integral-weight supplement

Entire supplement freshly read: agent_algebraic_integral_weight_supplement.md, SHA256 a65c96a19617bb74fc159a619642e1dd3be7dea5bfc08331fd3be1b6fe5f3f56.

**PASS.** I independently expanded the polynomial relation and checked every step I1--I8. A term with exponent r=i+sum(w_j) has root modulus b^r. Equal r terms may have coincident phases, but grouping those phases and finite-power uniqueness makes the entire unit-circle coefficient sequence S_r vanish. Evaluation at zero then gives precisely the coefficient of v^r in P(v,sum c_j v^(w_j)). Integrality is what makes the latter a Laurent polynomial and hence a rational function. Its being a root of the irreducible relation forces the algebraic element to equal that rational function.

For genuine spectra, positive multiplicities exclude surviving nontrivial phases, since they would be roots absent from the Laurent expression and could not cancel. For virtual coefficients only visible grouped roots are controlled; the supplement states this correctly.

With the additionally imposed full spectral comparison, each algebraic characteristic-polynomial coefficient takes the prescribed Laurent values at infinitely many distinct parameters. Substitution in its minimal polynomial gives a rational function with infinitely many zeros, hence the zero function. A rational root of an irreducible polynomial over C(v) identifies that coefficient itself. Thus the whole characteristic polynomial is the asserted product, even when the permitted evaluation sheets vary.

The regular fixed-rank specialization above v=1 then has only eigenvalue one. The previously reviewed F48 centralizer-center lemma gives a local center, whereas the actual F19 collision center has three components. The distinction between trace-only conclusions and the extra full-spectrum/regular-specialization hypotheses is retained throughout. Nonintegral weights and the displayed fractional Kummer example are correctly excluded from this integral-weight statement.

## 7. Full final-fragment match

Entire generated fragment freshly read: finding_F51.tex, SHA256 dd6ff1c0c6f89999e5307dc85ba4f5defbe6d47dd9aa803e1cd2953f5ebfd3e1.

**PASS.** The statement, both complete algebraic proofs, full-centralizer deductions, inverse-coordinate convention, same-family sheet restriction, and separate Grothendieck paragraph match the reviewed base and supplement. No proof was reduced to a heading, and the stronger characteristic-polynomial conclusion remains explicitly conditional on full spectral retuning.

I additionally read the supplied VIII TeX passage in the opening of its subsection “Nonstandard triple,” around lines 490--502, which explicitly allows the algebraic coefficient extension and its regularity subrings. This is a direct source-context check of the applicability; the primary PDF's printed-page locator is retained from the author rather than represented as a newly repeated page audit. The EGA/SGA/BBD locators in the dictionary are framework anchors, not asserted sources for the new radial-separation theorem.

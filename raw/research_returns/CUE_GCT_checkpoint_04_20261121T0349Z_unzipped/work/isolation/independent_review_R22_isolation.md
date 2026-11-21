# Independent complete proof review of R-22

Reviewer: GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I

Actual completion: 2026-11-21T03:34:06+00:00

Reviewed file: work/rectangular/r22_fragment.tex

Reviewed SHA256: 35bce7dd2ec295d623487b942eb1030f302a50c53fe6a5dd574b41b004f7ccbd

## Outcome

**PASS for the complete new mathematical argument.** One statement-level wording repair was requested: the integer grid applies to the untwisted motif parameters; translated copies have the prescribed root-of-unity twists. The proof already uses that scope correctly. Previously proved cyclic-base and padding facts R15/R16/R17/R14 and the stated G-series consequences are treated as dependencies, not independently reproved in this event.

## Full checks performed

1. Counted all permitted positions and verified both exact supported-row/column cofactor factorizations with all translated blocks present. Shared boundary columns do not enter the protected middle supports.

2. Rederived the signed determinant/permanent agreement through first order and the endpoint second-order cancellation. A single forward/backward pair makes the stated cycle and has the correct parity; deleting the other endpoint and transposing preserves the assigned signs.

3. Rederived the top E_j component by comparing target sets with the all-superdiagonal matching. The backward target must be zero, the forward row is j-1, and its target is h+1. Its sign is opposite the assigned product, giving the exact factor2. The row relation and original-index R forms follow; reflection gives the displayed S forms with the reversed overall sign.

4. Checked both outside cyclic-matching products and all external-index ranges. The alignments give degree (m-k,k). Recomputed the row and column root completions of A(x,y), the shifts in coefficient normalization, and the residual Fourier transforms, including X powers and q-scalings.

5. Checked every row/column degree1 and degree2 interpolation basis. Their triangular evaluations require only the listed nonzero factors; no parameter- or X-dependent denominators are introduced.

6. For the row specialization, recomputed the first b-3 diagonal evaluation columns and both final columns. The X^2 coefficient of the final2x2 determinant is exactly the displayed product. All exponent coincidences that could kill a factor lie outside the interior k range, including b=3. The specialization has X-degree at most2b-3.

7. The reflected parameter domain is exactly invariant: the position map preserves forward/backward type and the excluded corner. q^-1, y'=q^b y and w'=q^(b-1)w are invertible changes. The external column becomes the correctly aligned new row at the same bidegree. Character coefficient coordinates are only rescaled, not mixed. A nonzero row specialization at one interior character therefore proves that the column determinant is nonzero in the same fixed Q(q)[theta,X,X^-1] domain. No simultaneous row/column specialization is assumed prematurely.

8. Independently checked the joint-space intersection: the two degree-(b-1) residual factors are coprime; their intersection is their product times Sym1, exactly the base. The combined space is H Sym^(2b-1), of dimension2b.

9. Checked the allowed coefficient interval length, e<=N, dual Jacobi--Trudi shape, and root-of-unity nonvanishing by Weyl exponents in[0,k] with k<m. The N=0 boundary and the analogous row-only restriction are covered.

10. Verified both determinant Laurent exponent bounds and the degree bounds for F_k. Each factor is nonzero at fixed q,k, so their product is nonzero over Q(q)(X). Tensor-grid interpolation gives one integer theta choice that works for all k, though not necessarily all m or primitive q. This is an existence/finite-search assertion, not a polynomial-time claim.

11. Good characters lose at most2b per k. The map t -> q^(bt) has fibers of size gcd(b,m)<=b, so at least h distinct translation eigenvalues remain. The resulting degree-(h-1) Vandermonde equations force every translated normal coefficient to vanish. Different k values are combined through the highest-(z,w)-degree filtration, retaining lower terms correctly.

12. The local relation times its common outside permanent is in the differential image of the same deformed pencil. Divisibility by epsilon^2 persists with every block present; dividing yields a polynomial family. Appending these limits to base differential columns gives one nonzero minor and hence one common generic nonzero epsilon. No ranks from different pencils are added.

13. Recomputed the bounds J >= (2-2/b)m^2-22bm, b=floor(sqrt(m/11)), the constant6sqrt(11)<20, the ratio threshold100/(2-rho^2)^2, the value2025 at rho=4/3, and the sqrt2 ceiling. The final m>=169 sufficient example checks by direct squaring.

No numerical script, external formal certificate, or independent rereading of every cited background source is claimed in this event.

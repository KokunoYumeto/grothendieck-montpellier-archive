# A51 transitive-deck supplement: independent whole-proof review

Date: 2026-11-21.

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Source: `work/row_audit/A51_TRANSITIVE_DECK_SUPPLEMENT.tex`.

SHA256: `2d127609310816ba0388587bb9b72c55789e892cb74ce1938884b2afbf8b85c3`.

**PASS: separate-reader review of the entire supplement.** This is not a new independent construction or arithmetic computation.

The full cyclotomic reduction is a finite product of finite fields. Transitivity on primitive geometric roots makes its invariant algebra F2 and permutes its field factors transitively. Bijective semilinearity forces equal module ranks over these factors, so the actual geometric two-torsion module has dimension an integer multiple of phi(n). The genus-two primitive dimension bound leaves only ranks zero and one.

In rank one, writing Frobenius as c times tau gives its phi(n)-th power as the norm of c. That norm lies in F2 units and is one. The finite-etale torsor descent previously checked in A45 therefore applies even when the group order is even and the algebra is not a field. It proves exactly one rational two-torsion generator in the ordinary case. I checked that the proof never averages by the group order.

The auxiliary-adic two-dimensional character blocks are cyclically permuted, so basis transport gives the determinant in T to the power phi(n). The integral abelian-variety polynomial fixes the top coefficient and integer middle coefficient. The rational two-torsion conclusion determines its parity; a finite two-group with one generator is cyclic, giving the exact displayed exponent from the rational group order. No bounded valuation is inferred.

For the fixed rank-one tower, the minimal deck extension grows exponentially in the conductor exponent. The curve and Jacobian Weil bounds then make the prescribed quotient smaller than the number of rational base points, and its kernel unbounded. These are the precise reasons the unrestricted-quotient nonuniformity argument does not target that quotient. Proper-quotient norms and individual generator bounds do not identify an uncontrolled unit packet with the remaining faithful component.

Known A45 descent, A51 norm formulas, genus-two character dimensions, and the Weil bounds were checked for applicability. I did not newly reopen their external primary-source proofs during this particular reading. No actual curve example, numerical execution, or universal witness existence is claimed. All geometric and rational assertions refer to the actual primitive factor; the scope of the remaining supply gap is correct.

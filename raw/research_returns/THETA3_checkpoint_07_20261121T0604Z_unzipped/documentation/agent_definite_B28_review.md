# THETA3-B28 independent whole-proof review

Reviewer: GPT-6 Astra Pro, `/root/definite_bridge`; reasoning effort inherited and not exposed. Date: 2026-11-21.

**Result: PASS for the stated fixed-input certificate.** I read the entire saved `paper_B28.tex` and reconstructed all the proof and normalization steps.

The coefficient functions are independent because the chosen target vectors form a basis of the actual kernel image. The B26 finite source-CM orbit separation therefore supplies a full-column-rank evaluation matrix. Passing to a deeper neat level does not alter the adelic measure: its finite compact-volume and covering-degree adjustments are explicitly contained in the chart measure conversions. Duplicate geometric points give proportional line-bundle evaluation rows and can be removed without changing their span.

At a chart centre moved to `i`, the Cayley identities give `y=(1-|w|^2)/|1-w|^2` and hyperbolic area `4 dudv/(1-|w|^2)^2`. Writing the actual holomorphic weight-three coefficient as `F(z)=(1-w)^3 A(w)` therefore gives the exact density `4 |A(w)|^2(1-|w|^2) dudv`. All constant CM and determinant-line factors can and must remain in `A`; at zero its value is the actual unitary-frame coefficient. On the polydisk, angular integration kills mixed monomials, and the constant term contributes exactly `(4 pi)^s product(rho_j^2-rho_j^4/2)`. Disjoint chart images allow their contributions to be added. The limiting argument from smaller compact polydisks is valid.

In the conjugate-linear-first convention the integral Gram of the source sections is `hat(W)=W^t`. Thus the evaluation inequality first gives `hat(W) >= |Cx/tx|^2 H`, then transposition gives the displayed bound for `W`. Transposition preserves positivity of Hermitian matrices. Positive inversion reverses the order, yielding the stated inverse bound.

The genuine theta operator satisfies `Q_T=T T*=W G`. Its least-norm right inverse is `T* Q_T^-1`; its image is perpendicular to `ker(T)`, and the exact squared source norm is `q* W^-1 q`. Conjugation by `G^(1/2)` identifies the target operator with the positive Hermitian matrix `G^(1/2) W G^(1/2)`, proving the operator-norm inequality in the stated metric. No finite restriction operator has been substituted for the actual theta operator.

The singular-value lower bound follows from an invertible square row minor and the product of its singular values; bounding the other singular values by the Frobenius norm gives the exact displayed exponent. For the arithmetic determinant bound, `d0^r det(M)` is a nonzero algebraic integer, whose field norm has absolute value at least one. Applying the stated Hadamard bound at every other embedding yields exactly `d0^(-r [K:Q])` times the reciprocal conjugate bounds. No missing complex-conjugate or square factor occurs.

Finally, B26's coherent scalar is `gamma=Cx/(tx ty)` and the source CM evaluation multiplies by `ty`. Their product is exactly `Cx/tx`; hence the bound needs no separate estimate of `ty` or the unknown source period scalars. Target normalization, chart radii, measure conversions, algebraic denominators and conjugate bounds remain explicit inputs, as the statement requires. The result makes no new algebraicity or uniform-height assertion.

This review uses the already independently checked B17, B25 and B26 identities as inputs. The new local mean-value calculation and all linear-algebra inequalities are proved directly in B28 and were checked in their entirety. No additional external theorem or uninspected source body is invoked by this review.

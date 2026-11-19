# Independent review of the integral Walker obstruction

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent /root/frobenius. Date: 19 November 2026.

## Scope and conclusion

We independently read research/agents/cycles/walker_obstruction.tex, particularly E.3j–k, and reopened the primary Ottem–Suzuki paper. The stated integral conclusion follows. No mathematical correction was identified in the reviewed argument.

## The diagonal decomposition

The complex support hypothesis on zero-cycles suffices. Choose a countable algebraically closed field of definition and embed its function field in the complex numbers. The support relation for the resulting geometric generic point involves finitely many cycles and rational functions. Spreading those data over the algebraic closure of the function field and choosing a closed point in a good open gives the relation over that algebraic closure. Finite descent and trace then give a positive integer multiple of the generic point supported on the chosen curve. Closing the relation and using localization on the first factor gives
\[
M\Delta_X=\Gamma_C+\Gamma_D,
\qquad
\operatorname{supp}\Gamma_C\subset X\times C,\quad
\operatorname{supp}\Gamma_D\subset D\times X .
\]
Universal support over arbitrary extensions is not required.

The contribution supported on \(X\times C\) lifts integrally to divisor correspondences on \(X\times\widetilde C\), after normalizing each curve component. A component dominating a curve component lifts with degree one under the normalization; a component over a singular point lifts after choosing a point of its normalization, again with degree one over the algebraically closed base. The resulting action on \(\mathrm{CH}^{n-1}(X)\) factors through \(\mathrm{CH}^0(\widetilde C)\). This group has no algebraically trivial part. Components supported at isolated points have a still simpler zero action.

For a projective resolution \(f_j:T_j\to D_j\to X\), every component supported on \(D_j\times X\) has a generically finite multisection in its inverse image. Thus it lifts after rational coefficients, including components over singular strata. Clearing the finitely many denominators gives integral \(G_j\in\mathrm{CH}^{n-1}(T_j\times X)\), with \(\dim T_j=n-1\), and the exact action
\[
M\operatorname{id}=\sum_j(G_j)_*f_j^*
\]
on algebraically trivial codimension-\((n-1)\) cycles. The degrees are correct: \(f_j^*\) produces zero-cycles on \(T_j\), and \(G_j\) has exactly the codimension needed to return codimension-\((n-1)\) cycles on \(X\).

## The integral family conclusion

Functoriality of Albanese equivalence makes this action factor through
\[
\prod_j P^{n-1}(T_j)
=\prod_j\operatorname{Alb}(T_j)(\mathbf C).
\]
For a family whose cylinder map is zero, the pullback family on \(T_j\) has zero cylinder in
\(H^{2n-3}(T_j,\mathbf Q)=H^{2\dim T_j-1}(T_j,\mathbf Q)\).
Faithfulness of the homology realization on homomorphisms of abelian varieties implies that the induced homomorphism to \(\operatorname{Alb}(T_j)\) is zero. Consequently \(M u_Z=0\).

This is sufficient integrally. For each \(a\in A(\mathbf C)\), divisibility supplies \(b\) with \(Mb=a\), and hence \(u_Z(a)=M u_Z(b)=0\). No assertion that the target \(P^{n-1}(X)\) is torsion-free is used.

## The same fourfold separates the assertions

Ottem and Suzuki, Lemma 2.4, printed author p. 4, proves \(\mathrm{CH}_0(W)=\mathbf Z\) for the threefold used in their construction. Therefore \(\mathrm{CH}_0(W\times E)\) is supported on \(\{w_0\}\times E\), by applying the equality of point classes in each fibre \(W\times\{e\}\). E.3j applies to every codimension-three abelian family on this same fourfold.

Corollary 4.2, printed author p. 10, supplies a surjective regular Walker map and a nontrivial finite kernel in the isogeny from the Walker intermediate Jacobian to the ordinary algebraic intermediate Jacobian. A point lifting a nonzero element of that kernel is ordinarily Abel–Jacobi trivial but not Albanese equivalent to zero, since regular homomorphisms annihilate the defining subgroup of Albanese equivalence. E.3g supplies an integral abelian-family parameterization of this individual point.

Thus the family-map converse holds and the proposed integral equality of point equivalence relations fails on the same fourfold. This refutes the literal integral biconditional without asserting that its family-map side fails. The rational formulation is unaffected.

## Related surface-radical calculation

We also checked the direct composition argument communicated by /root/cycles. For \(S=C^2\), let the homologically trivial modified diagonal be the degree-zero correspondence \(\gamma:S\to C\), and let \(\pi^*:C\to S\) be the transpose graph of a projection. Then \(a=\pi^*\gamma\in\operatorname{End}(S)\). For every endomorphism \(b\), the composite \(\gamma b\pi^*\) is a homologically trivial divisor correspondence on \(C\times C\), so it is zero modulo algebraic equivalence. Hence \(aba=0\), and \((ba)^2=0\); the inverse of \(1-ba\) is \(1+ba\). Thus \(a\) lies in the Jacobson radical. A fixed-point section in the fourth factor recovers \(\gamma\) from \(\gamma\times C\), so a nonzero modified-diagonal class gives a nonzero radical element. The remaining nonvanishing input is the primary Ceresa theorem, owned and audited by /root/cycles; we do not claim to have independently opened that source in this review.

## Opened primary source

Ottem, J. C., & Suzuki, F. (2020). *A pencil of Enriques surfaces with non-algebraic integral Hodge classes*. arXiv:1906.08994v2. Opened https://arxiv.org/pdf/1906.08994. Checked Lemma 2.4, author p. 4; Theorem 3.1 and its construction data, author pp. 6–8; Theorem 4.1, Corollary 4.2, and Remarks 4.3–4.4, author p. 10. We use the stated construction and Walker results as primary theorem inputs; this targeted review does not independently reprove their degeneration argument.

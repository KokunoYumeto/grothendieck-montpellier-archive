# Conditional review of the proposed rank-two Steinberg construction

Actor: GPT-6 Astra Pro, subagent `/root/lvalue_bounds`; effort not exposed. Date: 21 November 2026. This is an independent review of two proposed analytic implications. It does not establish the required global representation, the full collection of finite local theta conditions, or a new global Steinberg-wedge theorem.

## Archimedean implication

Assume the rank-two skew-Hermitian space is the orthogonal sum of two negative lines at every real place. The target has signature $(2,1)$ at the active place and $(3,0)$ elsewhere. Choose one splitting character $\gamma$ so that the rank-one holomorphic cocycle at the active place and the Gaussians at the other places are actual relative cochains for the target unitary group. On the rank-two pair the source splitting is $\gamma^3$ and the target splitting is $\gamma^2$.

The active wedge cocycle has one-dimensional compact source type by BMM Proposition 5.17(8). Changing from the polynomial action to the actual Weil splitting only multiplies this by a determinant character. At nonactive places the Gaussian also has a one-dimensional compact source type. Haan Remark 2.1 identifies the central action of the target with that of each one-dimensional source. Tensoring the two identities, with the direct-sum compatibility of the splittings, identifies $zI_2$ in the source with $zI_3$ in the target on the tensor model.

A genuine relative target cochain has trivial target-center action, because the center acts trivially on the tangent and cotangent representations. Its one-dimensional genuine $U(2)$ source type therefore has trivial center. Every one-dimensional representation of $U(2)$ is an integral determinant power; triviality on $zI_2$ forces that power to be zero. The source type is consequently trivial. Source action is on the Schwartz factor, so evaluating the cocycle in a canonical-frame vector preserves this invariance. BMM Proposition 5.19 identifies that scalar coefficient with a nonzero determinant polynomial.

For the trivial source representation, the compact local doubling integral at the critical parameter $s_m=(3-2)/2$ is therefore the positive number $\operatorname{vol}(U(2))\|\phi\|^2$. This verifies the proposed archimedean nonvanishing under the stated compatible-cochain hypotheses. An arbitrary preselected $\gamma$ need not make all the compact-place Gaussians relative cochains. If the source were indefinite at some real place, trivial center and a one-dimensional maximal-compact type would not imply invariance under the full source group; definiteness at every real place is used here.

Sources actually read: BMM, *The Hodge conjecture and arithmetic quotients of complex balls*, Acta Math.216 (2016), Proposition 5.17(8), Lemma 5.18 and Proposition 5.19, printed pp.48--50, including the adjoining complete proofs; Haan, arXiv:1403.5061v7, §2.1 Remark 2.1 p.4 and §3.2 equation (3.3) p.8; Wu, arXiv:1409.0770v1, §2.2 splitting-change formula (2.9) p.5. The cited Weil representation and cocycle theory is imported background.

## Conditional toric extraction

Suppose an actual irreducible global source realization $\pi$ with $\pi_\infty=1$ has a nonzero theta lift with this fixed nonzero archimedean cocycle. Let the finite Schwartz input and the target argument vary. The source projections of the resulting theta kernels into $\pi$ form a nonzero $H(\mathbf A_f)$-stable span. Since the archimedean representation is trivial, the smooth $H(\mathbf A_f)$-module $\pi$ is irreducible; that span is all of $\pi$.

Some finite translate of a nonzero smooth vector is nonzero at the identity: a point of nonvanishing may be moved there, and its archimedean coordinate is irrelevant because $\pi_\infty$ is trivial. Restriction to the compact adelic quotient of the two-line torus is then nonzero. Fourier completeness on that compact abelian quotient supplies a torus character with nonzero period. The character can be taken trivial at infinity because the restricted vector is invariant there. By linearity, one source-projected theta kernel already has a nonzero such period.

At finite places, Schwartz functions on a direct sum are finite sums of pure tensor Schwartz functions. Combining this with the fixed archimedean cocycle product expresses that toric theta period as a finite sum of wedges of integrated rank-one holomorphic theta forms. At least one term has nonzero contribution from the selected source realization. T6.12's mixed-source orthogonality is needed at this point to rule out cancellation with other source realizations in the target. Under that already-checked orthogonality, the implication is valid.

This conditional argument does not supply the global $\pi$, the specified Steinberg component, or the remaining local nonvanishing conditions. Those are independent hypotheses still requiring the separate globalization argument.

## The CM-motive consistency issue

The CM nature of the Albanese implies that the cup-product image of its first cohomology is a CM Hodge structure. It does not by itself identify the geometric Galois constituent of an endoscopic $U(3)$ automorphic realization with the full standard representation appearing in a Rallis formula.

Chenevier--Harris, *Construction of automorphic Galois representations, II*, introduction p.2, explicitly describes examples where endoscopic transfer from $U(2)\times U(1)$ contributes a one-dimensional Galois representation from the $U(1)$ factor. Primary source: <https://webusers.imj-prg.fr/~michael.harris/ConstructionII.pdf>. The exact example assumes even degree of the totally real field and an everywhere-unramified Hilbert modular form. It does not itself settle the proposed case with a finite Steinberg component. The introduction was read at that exact passage; no complete geometric Galois computation for the proposed construction is asserted here.

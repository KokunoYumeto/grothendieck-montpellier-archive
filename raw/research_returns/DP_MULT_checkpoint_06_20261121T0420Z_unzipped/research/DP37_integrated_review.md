# Independent review of integrated DP37

Reviewer: `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. The complete integrated statement and proof in `DP_MULT.tex`, from `begin{proposition}[DP37:…]` through the following `end{proof}`, were read and independently challenged after the observed clock **01:55:07 UTC**. The exact snapshot and capture time are in `DP37_integrated_review_metadata.json`; the reviewed block is saved as `DP37_integrated_review_snapshot.tex`.

**Verdict: PASS, no mathematical correction required.**

I read the entire companion memo `exact_torus_compatibility_DP37.md`, the full integrated invariant-frame and averaging argument, and all hypotheses of DP36 against which the final claim is made. I also directly viewed the primary Tate scan at printed p.180, containing Corollary2 immediately following Theorem3 and its exact sequence. This is the correct corollary; the same spread has a different Corollary2 on p.181, which is not being substituted.

The Hodge–Tate exact sequence has the stated terms and dimensions. Endomorphism naturality acts by precomposition on the Hom space and pullback on the cotangent factor, so its characteristic polynomial is the transpose polynomial and the tangent scalar is `λ`, not `λ^(−1)`. The displayed Lie eigenvalues account for `h−1` roots. A primitive `(p^h−1)`st root has unramified degree exactly `h`, including the cases `p=2` and `h=2`; consequently its minimal polynomial forces precisely the missing root `ζ`. The characteristic-zero logarithm then identifies the endomorphism itself. This determines the exact embedding rather than just its Frobenius orbit or slope.

For the second half, preservation of the evaluation pairing gives a coherent torus action on the rigidified Poincaré biextension. With the stated cocycle convention `c_(σg)=σ(c_g)c_σ`, the product satisfies `σ(∏c_g)=(∏c_g)/c_σ^N`. The root with constant term one is integral because `N=q−1` is a unit; uniqueness gives `σ(u)=u/c_σ`, and therefore `u e` is invariant. The axes remain normalized. This is an actual invariant frame, not an inference from a fixed isomorphism class alone.

Averaging the rational logarithmic splitting preserves both logarithms of the same invariant integral cocycles. Its coefficients remain in the stated fraction field. Axes remain zero. The characters exclude all bidegree-`(1,1)` monomials, and the characteristic-zero uniqueness-up-to-bilinear result from DP35 proves uniqueness of the invariant representative. Thus the precise beta hypotheses of DP36 are obtained for the primitive formal class, with the odd-prime restriction of DP36 left intact.

The last scope sentence is essential and correct: this does not identify the particular global theta section, its connection gauge, chosen path, or selected harmonic operator. The independent cyclic-display construction in DP38 gives another realization and confirms the same action on its Teichmüller coordinates, but it is not needed to complete the argument checked here.

No numerical test, Lean compilation, or machine formalization was performed or claimed in this review.

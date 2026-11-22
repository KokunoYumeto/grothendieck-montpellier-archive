# Whole-proof review of K-029

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS.** Read all of `AMPLIFIED_COLLISION_COMPONENTS.tex` and all of
`verify_amplified_collision_component.py`. Independently replayed the
verifier successfully. Also reread K-021's complete spectral-collapse proof
and checked the use of K-020 and K-025, whose full proofs were previously
reviewed in this continuation.

The same-component assertion is justified: at an effectively free closed
orbit the quotient differential is surjective and equivariant. Taking
fixed vectors for a finite-order element preserves exactness. The source
fixed vector space and target fixed germ are smooth, so the restricted
map is smooth at the point and its image contains a neighborhood in that
unique component. Its irreducible image closure is contained in the fixed
scheme and contains that component, hence equals it. Thus every point
from the entire fixed vector space maps into that same component closure.

The decomposition k=8l+s gives D_(k-l)=2^s M exactly. Reduction through
the final l gadgets makes each new coordinate equal in spectral weight
to the selected old coordinate; the product of the three scalar weights
is one. The further 2^s power leaves an old prefix character of exact
order M. Hence the critical prefix tensor direct-summed with an arbitrary
critical tensor on the new block is fixed by the same h.

The chosen three-dimensional tight-frame block has identity marginals
and a fixing element with primitive cubic determinant character. Adding
one-dimensional diagonal blocks retains criticality. The new element
commutes with h because h is scalar in each new factor. Their determinant
characters have coprime orders three and M, so their product has order3M.
The direct sum is nonzero and critical, hence gives a nonzero polystable
quotient point. The fixed-vector image argument places it in the original
amplified component.

The independent exact n58 replay checks positive prefix masses and every
margin, freeness, the symbolic three-block marginals, complete collapsed
spectra, all fixing equations, and the primitive determinant character of
order3*2^57. It gives the exact fixed dimensions697−339=358. The all-stage
component dimensions are the previously proved K-021 formula, not an
extrapolation of that numerical case. No global Hilbert pole or specific
three-adic density denominator is inferred from the collision point.

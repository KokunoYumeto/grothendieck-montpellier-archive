# Independent whole-proof audit of SF-E818

**Outcome: PASS.** Reviewer `/root/imprimitive`, GPT-6 Astra Pro, inherited reasoning effort not exposed, HODGE_DIVISION, 2026-11-21. I read the entire `agents/sixfolds/rm_positive_defect_obstruction_draft.md`, including its added leading-character source paragraph, and independently reconstructed all new arguments. No author file was changed. Reviewed SHA-256: `444d17195fb465777c0394faaea9d1a4b64242a1686c7a433014faeaf7484a02`.

## Exact scope checked

The hull H=E** is locally free and has an actual filtration by subbundles with stable locally free quotients of the same polarization slope. The underlying fourfold has genuine Rosati real multiplication of type (2,2). The normalized character is the stated balanced class with q>0. Neither stability of E nor local freeness of its own stable factors is assumed. The theorem does not assert that every semistable locally free hull has such a filtration, and it does not address singular reflexive hulls. The finite action is an actual specified coherent translation/tensor action.

## Strict surface positivity

I independently verified the tangent-plane argument. The semipositive form θ+θ− evaluates as a positive sum of squares of the mixed holomorphic two-form restrictions. A zero integral on an effective surface therefore makes all mixed Plücker coordinates zero on its smooth locus. A nonzero decomposable bivector lying in Λ²V+ ⊕ Λ²V− has only one nonzero component: its square is twice the product of the two components, which cannot vanish if both are nonzero. Thus its tangent plane is exactly one of V+, V−. The irreducible Gauss image is constant.

The Albanese step then rules out either possibility without a simplicity assumption on X. All invariant one-forms annihilating the constant tangent plane pull back to zero on a smooth projective resolution. The induced Albanese homomorphism has nonzero abelian image with tangent space contained in that eigenspace. Such an image has nonzero rational homology, while a genuine irrational real-multiplication eigenspace has no nonzero rational vector. This proves strict positivity for every nonzero effective surface cycle, including singular components and positive multiplicities.

## Elimination of the support dimensions

The torsion-free double-dual quotient has codimension at least two. The first Chern component correctly forces B=−c1(E)/r. I checked both discriminant identities with their signs:

Δ(E)=Δ(H)+ch2(T), and Δ(H)=ΣΔ(Qj)−(1/2)Σ rj(αj−α)².

The balanced character gives zero mixed pairing on the left. Each stable locally free factor has nonnegative mixed discriminant pairing by the precisely stated previously reviewed SF-E811; each variance term has the same sign by its elementary mixed quadratic identity. Strict surface positivity consequently removes all dimension-two support and forces equality in every nonnegative summand.

The equality conclusions used are exactly those previously proved: every Qj is projectively flat and each normalized first-Chern difference δj is block diagonal and separately primitive in the two complex two-planes. No splitting of H or equivariance of individual stable factors is needed here. Additivity of the full character along a filtration suffices.

I expanded θδj³ independently. The only possible terms are 3δj,+²δj,− and 3δj,+δj,−²; wedging with θ+ + θ− kills each term by either excess block degree or the separate primitive identities. Hence the normalized degree-three character of H has zero θ pairing. Since T now has support dimension at most one, exponential normalization changes no degree-three term of its character. Its leading character is therefore an effective curve cycle of zero ample degree, forcing that cycle to vanish. This leaves precisely T=0 or a zero-dimensional quotient.

For T nonzero, the canonical equivariance is the one already verified in SF-E817, and its quantitative kernel bound 1+3s applies. For T=0 the hypotheses are exactly those of SF-E813. Both uses preserve their full previously checked scopes. No Hermitian–Einstein metric on a singular sheaf and no extension across a singular reflexive hull is used.

## Fresh primary-source check

I opened and read the complete relevant passages of Fulton, *Intersection Theory*, second edition (1998), Example 18.3.11, printed p.363, and Theorem 18.3(3), printed p.353, in the indexed scan at <https://djvu.online/file/Pl4avuZzLcI6I>. The former states that the highest-dimensional term is the support cycle with generic stalk lengths; the latter identifies the transformation with the Chern-character/Todd expression on a smooth ambient variety. For this abelian variety the tangent Todd class is one, so the stated lower vanishing and effective leading character follow exactly. I also freshly read Stacks Project Definition 42.10.2 and the preceding finite-length lemma at <https://stacks.math.columbia.edu/tag/02QV>.

The new theorem only needs these precise standard Riemann–Roch inputs; I do not claim a fresh proof of the entire Riemann–Roch theorem. SF-E811 and SF-E813 were independently whole-reviewed earlier in this session, and SF-E817 was independently whole-reviewed and computationally reconstructed just before this audit. No new numerical certificate is needed for the elementary dimension-elimination argument.

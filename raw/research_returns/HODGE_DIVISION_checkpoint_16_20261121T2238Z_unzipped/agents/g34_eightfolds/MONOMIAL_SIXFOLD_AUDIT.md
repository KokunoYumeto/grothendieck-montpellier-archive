# Independent whole-proof audit: D-MON-01–03

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed. Run: HODGE_DIVISION. Date: 2026-11-21, approximately 12:37–12:40 UTC.

**Verdict: PASS.** I read the complete `agents/imprimitive/monomial_sixfold_section.tex`, not just its statements. I also read Looijenga's author text: Proposition 2.2 and Theorem 2.4 on page 5; the cyclic cut-surface construction and proof of Proposition 2.2 on pages 8–9; the elementary unitary generation, lifted symplectic subgroup, and genus-at-least-three proof of Theorem 2.4 on pages 10–12. The original PS and its converted PDF/text are retained by the authoring agent. This audit uses published monodromy surjectivity as an input; it does not claim to reprove that theorem or the earlier group-theoretic sources it cites.

## 1. Primitive factors and rational induction

The corner division algebra D acts faithfully on the K-vector space H¹(B,Q). A nonzero finite-dimensional left D-module is free over D, so its K-dimension is divisible by dim_K D=s². In dimension six this forces s=1. This justifies the realization over K and the use of a matrix-algebra primitive factor; the proof does not silently assume Schur index one.

For L=Q(ζ_d), all embeddings of L induce either ρ or its conjugate, according to restriction to its exact character field K. Semisimplicity therefore gives Ind_H^G L ≅ V_Q^[L:K]. Frobenius reciprocity identifies the Hom Hodge structure with the primitive cyclic summand on C/kerχ. Evaluation at 1 identifies Hom_L(L,W) with W as a rational Hodge structure, so there is no missing field-degree factor. The resulting isogeny P_d ∼ B^[L:K] has the asserted dimensions and is induced by fixed rational maps in families.

At any genuine branch point of the cyclic quotient, a faithful character has no inertia invariants. Adding its two Chevalley–Weil multiplicities yields 6=2h−2+R. The moduli dimensions 5,6,7,8,9 for h=0,1,2,3,4 follow from the pointed-base dimensions and the finite choices of a dth root line bundle. The unstable genus-zero and genus-one exceptions do not arise.

The differential of a direct sum of copies of a Hodge variation has the same kernel as that of one copy. The cyclic variation is a pullback from cyclic-cover moduli. Consequently period rank nine forces h=4 and R=0 and forces an open image in a component of the connected étale cyclic-cover moduli. This argument concerns actual differentials; it does not infer dominance merely from equality of dimensions.

## 2. Full rational endomorphism algebra

Looijenga's Proposition 2.2 gives the stated rank-six hyperbolic skew-Hermitian module. His Theorem 2.4 gives the lifted mapping-class image U₆#(R_d). Passing to a finite level structure changes the image by finite index, which is enough for the argument.

The finite-index commutant calculation is valid. Powers of square-zero symplectic transvections imply commutation with their logarithms. Coordinate transvections and their products force every commuting rational map on L⁶ to act as the same rational endomorphism f of L in every coordinate. The upper-unipotent block with Hermitian entries B₁₂=ζ_d and B₂₁=barζ_d has determinant one and preserves the displayed skew-Hermitian form. Commutation with a positive power forces f to commute with ζ_d and hence with all of L. Thus the rational commutant is exactly L, including maps not initially assumed L-linear.

The passage from this commutant to the full very-general End⁰ is sound. The algebra E of rational endomorphisms preserving the Hodge filtration at every point of the connected universal cover is stable under monodromy. At any fixed fiber these maps are Hodge endomorphisms, so the polarization's Rosati trace form is positive definite on E. Its adjoint is defined by the fixed rational alternating form, and monodromy preserves that form. Therefore conjugation preserves both the integral lattice in E and a positive definite form; its image is finite. A finite-index subgroup centralizes E, whence E⊂L by the computed commutant. Deck transformations supply the reverse inclusion. Countably many proper closed analytic Hodge loci cannot exhaust an analytic open set, so a point with full End⁰=L occurs in every nonempty open set. This addresses the required full endomorphism algebra, rather than only the deck-action commutant.

## 3. Contradiction and actual polarization

If [L:K]>1, the isogeny to B^[L:K] inserts a noncommutative matrix algebra into End⁰(P_d)=L. This contradiction proves L=K. Hence d=3,4,6.

For these degrees the displayed rational projector is Rosati fixed and primitive: Frobenius reciprocity gives multiplicity one of χ in ρ|_H, and irreducibility of Indχ rules out other irreducible constituents containing χ. The conjugate character supplies precisely the other complex realization of the same rational primitive factor. Pullback from C/kerχ multiplies the Jacobian polarization by |kerχ|. Looijenga's hyperbolic cyclic form therefore gives a half-dimensional isotropic K-subspace for the actual primitive-factor polarization. A different Rosati-fixed primitive line changes the multiplicity form by a positive rational scalar, preserving this property. Thus the final splitness assertion concerns the specified induced polarization.

## Scope

The proof excludes dominant nonsplit sixfold sources for every monomial irreducible representation with imaginary quadratic exact character field, even when the inducing linear character initially has larger cyclotomic field. It does not exclude unrelated quadratic actions on real-character factors. No finite group enumeration or new numerical period computation is asserted by this audit.

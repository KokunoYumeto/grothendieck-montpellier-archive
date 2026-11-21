# Effective input regularity for Markman's genus-three seed

Run HECKE_DIV_20261121, checked 2026-11-21 by /root/markman, GPT-6 Astra Pro; effort setting not exposed. This note proves an explicit regularity and presentation bound for the **input** secant sheaf. It does not claim a regularity bound for its Fourier–Mukai transform, its twisted deformation, or the final Chern cycles.

## MR1. Geometry and Hilbert polynomials

Let X be the Jacobian of a smooth nonhyperelliptic genus-three curve C, with principal polarization Θ. Put L=3Θ, and use its complete embedding i:X→P^26. Indeed h⁰(X,L)=27 and L³=27·6=162. Let Z be the union of thirteen pairwise disjoint translates of the Abel–Jacobi curve, as in Markman's d=12 construction, and F=I_(Z/X)(Θ). The supplied source is `source/LIT_Markman_Hodge_abelian_fourfolds_2502.03415/250531.tex`: genus-three seed and its Chern character at lines3743–3776; disjointness and genericity hypotheses at lines5124–5135; the two input sheaves at lines5403–5410, equation labelled `eq-F-1-and-F-2`.

The Abel–Jacobi curve has class Θ²/2, hence Θ-degree3 and L-degree9. Its genus is3, so

    P_C(t)=9t−2,
    P_Z(t)=13(9t−2)=117t−26.

Since Todd(X)=1 and χ(O_X(kΘ))=k³, Riemann–Roch and the defining exact sequence give

    P_F(t)=(3t+1)³−13(9t+1)
          =27t³+27t²−108t−12.

The same formulas hold for reflected and translated copies used for F₂. They do not require a special arithmetic model of C.

## MR2. Gotzmann and a direct regularity bound of 445

We use the convention that a sheaf Q on projective space is m-regular if H^j(Q(m−j))=0 for all j>0.

For P(t)=dt+c the Gotzmann representation starts with d terms binom(t+1−j,1), j=0,…,d−1. Their sum is dt+d−d(d−1)/2; the remaining terms are constants. Thus its length is binom(d,2)+c, whenever the resulting constant count is nonnegative, as it is here.

For the entire union, the 117 linear terms sum to117t−6669; adding6643 constant terms gives117t−26. Its Gotzmann number is therefore6760, **not6877**. Gotzmann's regularity theorem gives reg(I_(Z/P26))≤6760.

A stronger bound uses disjointness. Each individual curve has Gotzmann representation with nine linear terms, whose sum is9t−27, followed by25 constants. Consequently reg(I_(C_j/P26))≤34. Sidman, *On the Castelnuovo–Mumford regularity of products of ideal sheaves* (arXiv:math/0110184v2), Corollary1.6, pp.4–5, implies

    reg(I_(Z/P26)) ≤ Σ_j reg(I_(C_j/P26)) ≤ 13·34 = 442.

Its proof is especially transparent here: at each stalk at most one factor ideal differs from the structure sheaf, so the tensor product of all thirteen ideals equals their intersection. Repeated application of the tensor regularity proposition proves the asserted sum bound.

Set A=I_(Z/P26) and B=i_*O_X(Θ). The sheaf B is3-regular: for j=1,2,3,

    H^j(P26,B(3−j)) = H^j(X,O_X((10−3j)Θ)) = 0,

by Kodaira vanishing, since the coefficients are7,4,1. Higher cohomology vanishes by support dimension. The sheaf A is locally free outside Z, a subset of dimension1. Sidman's Proposition1.5, pp.4–5, therefore gives

    reg(A⊗B) ≤ 442+3 = 445.

For completeness, the mechanism in that proposition is a linear resolution of A: after tensoring with B, the higher homology sheaves are the higher Tor sheaves, all supported on Z. Sidman's Lemma1.4 gives regularity of the zeroth homology whenever those higher homologies have support dimension at most2. Our support dimension1 satisfies this hypothesis strictly.

Tensor 0→A→O_P26→O_Z→0 with B. Its image in B is i_*F, hence there is an exact sequence

    0 → T → A⊗B → i_*F → 0,

where T is the image of Tor₁(O_Z,B) and is supported on Z. For every j≥1 and every twist, H^(j+1)(T)=0. The long exact cohomology sequence, applied at twist445−j, now proves

    reg_P26(i_*F) ≤ 445.

The weaker union-only calculation would give6763 by the identical argument. Neither step assumes semistability.

## MR3. An explicit locally free presentation of the input

Put m=445 and N=P_F(m)=2384568978. Regularity implies that F(mL) is globally generated and has no higher cohomology. Its canonical evaluation therefore gives

    0 → K → O_X(−445L)^N → F → 0.

The kernel K is locally free of rank N−1. Indeed Z is a disjoint union of smooth curves in the smooth threefold X, hence is a local complete intersection of codimension2. Its ideal, and therefore F, has projective dimension at most1 at every point. The first kernel of a surjection from a locally free module to such a module is locally free.

One also has reg_P26(i_*K)≤449. For j≥2, the relevant cohomology follows from the displayed sequence, the445-regularity of F, and the4-regularity of i_*O_X. For j=1 one needs surjectivity on sections at twist448. This is supplied by the regularity multiplication theorem: H⁰(F(445L))⊗Sym³H⁰(P26,O(1))→H⁰(F(448L)) is surjective, and this factors through H⁰(F(445L))⊗H⁰(X,3L), the section map for the displayed evaluation sequence. The same argument works at all larger twists. Thus the presentation includes numerical ranks and a regularity bound for its kernel.

The count N is arithmetic in `markman_regularity.py`; it is a deliberately safe count rather than a minimal number of generators.

## MR4. The first uncompleted transform computation

Markman's output is not F itself. On X_y×X_x×Xhat_α, put

    H = π₁*F₁ ⊗ a*F₂ ⊗ P_(y,α)^(-1),
    G = Rπ_(x,α),* H,
    E = G^∨[−1].

The supplied source's Proposition `prop-local-freeness`, lines5450–5465, proves that E is reflexive of rank96. Its proof, lines5846–5902, invokes a finite locally free complex K^bullet representing the direct image, then removes terms using the fibre cohomology vanishings to obtain K¹→K² and

    0 → (K²)* → (K¹)* → E → 0.

No ranks, base-direction twists, or effective presentations of K¹ and K² are specified. Input regularity by itself bounds neither the regularity of these base bundles nor that of the dual cokernel. A quantitative continuation must construct this derived direct image in the two base variables with numerical presentation bounds, or produce a different explicit presentation of E. This is a concrete finite algebraic computation, not a new Hodge-algebraicity assertion; however it has not been completed here.

An output bound for the seed E must then be tracked through the quotient isogeny and determinant-preserving untwisting. If one has a locally flat family of the resulting ordinary sheaves with a fixed relative ample line bundle, a seed regularity bound persists on an analytic neighbourhood by upper semicontinuity of the finitely many cohomology groups defining regularity. That supplies the analytic-open input for the bounded-Chow/Baire argument, without global semistability. Thus the missing issue is an effective presentation of the appropriate seed sheaf, together with tracking these concrete isogeny and polarization operations; it is not necessarily a new global boundedness theorem. Fixed Chern character alone would not provide the effective seed presentation.

## References and verification events

- Markman, E. (2025). *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*. arXiv:2502.03415v2, supplied LaTeX source dated250531; exact title at source lines199–200. https://arxiv.org/abs/2502.03415
- Sidman, J. (2001/2002). *On the Castelnuovo–Mumford regularity of products of ideal sheaves*. arXiv:math/0110184v2; Lemma1.4, Proposition1.5, Corollary1.6. https://arxiv.org/pdf/math/0110184
- Gotzmann's regularity theorem is used in its standard saturated ideal form; the exact Gotzmann decompositions in this note are independently recomputed by the supplied script.

MR1: targeted proof check, Hilbert polynomials via curve Riemann–Roch and abelian Riemann–Roch; passed. MR2: independent re-proof plus primary-source check of Sidman Lemma1.4/Proposition1.5/Corollary1.6; passed. MR3: targeted proof check of local projective dimension and each regularity vanishing, including the H⁰ multiplication condition; passed. MR4: targeted reading of Markman's direct-image construction; quantitative output step remains open. None of these are formal proof-assistant checks. A separate agent /root/arithmetic independently checked both the original6763 tensor/Tor argument and the strengthened445 bound; both passed.

# Period triangle: rigorous research contribution

AI-produced by GPT-6 Astra, OpenAI; sub-agent `/root/period_triangle`, 19 November 2026. No priority claim. This file supplies proofs and bounds for A.1–A.3; it does not claim the unresolved numerical period conjectures.

## 0. Sources actually opened and scope

We read both supplied transcriptions of 18:11, the first transcription of 18:12–13, notes [I] P10–P17, and the relevant parts of the prompt. The scans themselves were not supplied. We do not silently replace the frozen readings.

Primary sources opened through the web:

* Yves André, *Pour une théorie inconditionnelle des motifs*, Publ. Math. IHÉS 83 (1996), 5–49, Theorem 0.4, §2.5, §4.6, and its remark (ii): https://www.numdam.org/item/10.1007/BF02698643.pdf. Web refs `turn514126977view0`, `turn278352404view1`, `turn278352404view2`. Theorem 0.4 supplies a semisimple graded Tannakian category and its classical realization functors. §2.5 supplies the Hodge property of motivated tensors. §4.6 supplies the motivic group and central weight cocharacter. Remark (ii) expressly warns that general geometric connectedness is not established by the older Deligne–Milne argument.
* Bost–Charles, *Some remarks concerning the Grothendieck period conjecture*, author PDF: https://www.math.ens.psl.eu/~charles/crelle-periods.pdf, Definitions 2.4, 2.9, Corollary 2.11, Conjecture 2.12, Propositions 2.13–2.14. Web refs `turn609151199view0`, `turn514126977view2`. We also read the supplied TeX source at the corresponding labels. Conjecture 2.12 is equality of the comparison point's Zariski closure with the algebraic-cycle period torsor. Corollary 2.11 gives the intervening motivated torsor. Consequently Conjecture 2.12 for a smooth projective variety generating a motive implies genericity in the motivated torsor of that motive by the dominant projection of comparison torsors.
* Andrew Sutherland, MIT 18.783, Lecture 20 (20 April 2022), *The Hilbert class polynomial*: https://math.mit.edu/classes/18.783/2022/LectureNotes20.pdf, Theorem 20.12 and Corollary 20.13, printed p. 6 (PDF p. 6), opened and checked; web refs `turn171591086view0`, `turn171591086view1`. Corollary 20.13 explicitly states that the j-invariant of a complex elliptic curve with CM is an algebraic integer. Lecture 21 was also opened and recalls that the monic Hilbert class polynomial has integral coefficients.

Searches run: “periods complex conjugates Hodge splitting Grothendieck strong period conjecture”; “André Pour une théorie inconditionnelle des motifs 0.4 semisimple Tannakian PDF”; “Silverman Advanced Topics Arithmetic Elliptic Curves II 6.1 j algebraic integer”; “Bost Charles Some remarks Grothendieck period conjecture Conjecture 2.12 PDF”. We have found no source stating the image-dimension table below in this notation. We claim no novelty.

Our ambient category is André's category of **pure** motivated motives with rational coefficients over an algebraic subfield of C. All conclusions also apply to another semisimple graded Tannakian category with the same faithful realizations, central weight cocharacter, and Hodge tensors. The page's reductive/parabolic/Levi setting is essential. These proofs do not establish the same table for arbitrary mixed motives.

## 1. The base field and algebraic extension

Let k be an algebraic subfield of C with its given embedding, M a pure motivated motive over k, and G_k its Betti motivic group. Passing from k to an algebraic extension changes neither its dimension nor the dimensions of the Hodge parabolic and its unipotent radical.

Here is a proof of the group-dimension assertion, including the needed direction. A motivated tensor after algebraic extension is defined using finitely many varieties, cycles and coefficients, hence over a finite extension L/k. Enlarge L to a finite Galois extension. Its conjugates form a finite set of rational Betti tensors. The elementary symmetric tensors in this finite set descend to k: finite push-forward/traces of the algebraic cycles in the motivated construction give that descent. Equivalently, the polynomial whose factors are z minus these tensors has coefficients among the motivated tensors over k. G_k therefore permutes the finite set of factors. Its identity component fixes every factor. Thus G_k^0 fixes every motivated tensor available after algebraic extension. The group after extension is a closed subgroup of G_k on the same Betti vector space, so the two identity components agree. Their Lie algebras, dimensions and Hodge-weight decompositions agree. This proves the claimed transfer without assuming geometric connectedness.

For every tuple z of complex coordinates, adjoining Qbar to k(z) is algebraic. Consequently trdeg_k k(z) = trdeg_Qbar Qbar(z), and the corresponding relative transcendence degrees agree as well. We shall construct the joint torsor over Qbar and then transfer the numerical bounds to the original k. This also avoids an untyped direct sum between a motive over k and one over c(k): both are first extended to Qbar. The smaller compositum k c(k) can be used before making this algebraic extension.

## 2. Objects and exact maps (A.1)

Write V=T_B, D=T_dR, and H=gr_F D, with the grading p and the motivic weight n supplying the bidegree (p,n−p). Thus the Hodge fibre functor in this interpretation is the associated-graded de Rham tensor functor, over k. Strictness and tensor compatibility of the Hodge filtration make gr_F an exact tensor fibre functor. We use the ordinary, sign-adjusted Tannakian commutativity convention for pure motives.

The comparison isomorphism is the C-linear tensor map

    α: V⊗_Q C → D⊗_k C.

For each weight n the pure Hodge decomposition splits F. Projecting H_dR^{p,n−p} isomorphically to gr_F^p D gives the C-linear tensor isomorphism

    β: D⊗_k C → H⊗_k C,

and γ=(βα)^{-1}: H_C→V_C. These types prove all three triangle identities.

Let G'=Aut^⊗(D), B'=Aut^⊗(D,F), and U'=ker(B'→Aut^⊗(gr_F D)). A split tensor grading is described by a cocharacter μ; B'=P(μ), L'=Z(μ), and U'=R_u(B'). On Lie algebras the nonzero μ-weights occur in opposite pairs. Therefore

    g=l+2u,    b=l+u,    g−b=u.

In particular the apparently separate dimensions g−b and u in the page coincide in this pure reductive setting.

Define Q to be the tensor isomorphisms D→gr_F D preserving filtration and inducing the identity on gr_F. Precomposition gives a simply transitive U'-action on Q. To verify freeness, two such isomorphisms differ by exactly an automorphism in the displayed kernel U'. To verify transitivity, the same quotient of the two isomorphisms is that element. Existence after algebraic closure follows from a Levi decomposition. In characteristic zero this unipotent torsor is also trivial over the base field; no preferred rational trivialization is being selected.

The tensor filtration orbit is geometrically G/B and the tensor splitting orbit is geometrically G/L. They have the canonical forms furnished by their moduli definitions; a Q-defined stabilizer B inside the Betti group is not being silently selected. A filtration type may have a number field of definition (the field of its Galois-stable cocharacter class). Over that field one has the corresponding homogeneous variety; over Q the finite union of conjugate types is the relevant Q-form. Over k the quotient P/B', for the left B'-action on P=Isom^⊗(V_k,D), gives the chosen filtration form. Its morphism is

    q(a)=a^{-1}F_D.

The map Big→Fil forgets the splitting. Over each filtration its group is the unipotent radical of its stabilizer, so this is a torsor under the relative unipotent group U_Fil, not a claim that one fixed constant group U acts globally. A point γ in Isom^⊗(H,V_k) transports the fixed grading of H to V, giving r(γ). Thus φ=q(α), ψ=r(γ), and p(ψ)=φ.

The map from a normalized splitting to its Levi subgroup sends β to the stabilizer of the grading β^{-1}gr_F. It is an isomorphism from Q to the Levi-subgroup space: all Levi subgroups are U'-conjugate, and the stabilizer in U' is trivial because it centralizes the grading cocharacter, whose weights on Lie U' are strictly positive.

### 2.1. The two Q readings

The transcription has both an H'-reduction and the Levi-subgroup space. If H' is the inverse image in B' of a nontrivial central one-dimensional torus j(G_m)⊂B'/U', then dim H'=u+1. An H'-torsor cannot equal the u-dimensional normalized-splitting torsor just constructed. The exact relation is to allow the associated-graded map to equal j(t), rather than the identity. This enlarged space Q_H is an H'-torsor and has a morphism

    Q_H → G_m,    s ↦ t,     Q = fibre over 1.

In a chosen splitting Q_H is Q×G_m. This is the explicit normalization needed to pass between the two readings. The actual canonical Hodge splitting β has associated-graded map the identity and hence lies in the fibre Q. If one retains the page's H'-reduction reading literally, it is Q_H that appears in the contracted-product description P'=Q_H×^{H'}G'; the displayed dimension u concerns its normalized fibre. The two constructions are related by this morphism, but cannot be interchanged without it.

### 2.2. The margin arrow

The natural map is Φ→F, forgetting a grading. It induces an isomorphism on the étale spaces of types, whose inverse may be written from F/G to Φ/G. Reading the margin F→Φ as that inverse on types is mathematically consistent. Reading it as a natural splitting on the full parameter spaces is false when u>0. Indeed a G-equivariant section G/B→G/L would give a B-fixed point in B/L; the subgroup U acts simply transitively there, so such a point forces U=1. In GL_2 even an arbitrary regular section P^1→(P^1×P^1)\diagonal is impossible: it would be a morphism f:P^1→P^1 with no fixed point; writing f in homogeneous polynomials yields a homogeneous fixed-point equation of positive degree, which has a zero over an algebraic closure. Thus the literal reversed arrow on parameter spaces is not a valid replacement for the forgetful map. No scan reading is changed by this conclusion.

### 2.3. Tate period membership and denominator reading

For Q(−1)=H^2(P^1), let u be the positively oriented Betti generator and v the algebraic de Rham generator normalized by dlog. With α pointing Betti→de Rham, α(u)=(2πi)^{-1}v; on Q(−n) its coefficient is (2πi)^{-n}. A summand of a tensor construction in M has comparison coordinates rational in those of α, because the algebraic projectors and inclusion/projection maps have coefficients in k and Q and inverse matrices are rational functions. Therefore (2πi)^{-n}, and hence its inverse (2πi)^n, belongs to k(α) whenever Q(−n) belongs to the generated category. This proves the membership in the direction written on the page without reversing α.

For P17 [I], lowercase k gives ordinary field extensions and is the reading supported by the second witness. Uppercase K in trdeg k(α)/K or k(β)/K is not a field extension in the indicated direction, since K contains both fields. In exceptional cases where K equals the numerator field, that transcendence degree is zero. Thus the uppercase reading is undefined in general and cannot express the displayed positive values. This addresses both frozen readings.

## 3. The joint comparison construction (A.2)

Work over Qbar after §1. Set N=M⊕c^*M. Let V_c,D_c denote the Betti and de Rham functors for c^*M. Conjugation of the complex varieties induces a Q-linear tensor isomorphism

    j_B: V→V_c,

natural for conjugation of motivated correspondences, including the usual (−1)^n action on Tate factors. Conjugation of algebraic de Rham coefficients is a c-semilinear map j_D:D→D_c. Upon extending scalars to C it remains conjugate-semilinear. If κ_V denotes coordinatewise conjugation on V_C, the comparisons satisfy

    α_c j_B = j_D α κ_V.

Both sides are C-linear. In a Betti basis carried by j_B and a de Rham basis carried by j_D, the matrix of α_c is the complex conjugate of the matrix of α. This fixes the semilinearity in the construction.

Let T=P_N be the motivated comparison torsor and let

    a:T→P_M,       d:T→P_c

be its two projection morphisms of torsors. We identify the second Betti motivic group with the first through j_B. The joint Betti group is then a closed subgroup

    J⊂G×G

with surjective projections; h denotes dim J. Put N_2=ker(pr_1), regarded as a normal subgroup of the second G.

On T define the pair of tensor filtrations on V by

    F_1(t)=a(t)^{-1}F_D,
    F_2(t)=j_B^{-1}d(t)^{-1}F_{D_c}.

Let T° be the open locus where these filtrations are opposed in each motivic weight. At the actual comparison t=(α,α_c), the second equals the complex conjugate of the first. Pure Hodge theory therefore proves that this open locus is nonempty. This is a proof of nonemptiness; no algebraic comparison point is assumed. A nonempty open variety over Qbar has Qbar-points, should one be needed for algebraic trivializations.

For t∈T°, the intersections F_1^p∩F_2^{n−p} give a tensor bigrading. Transporting it by a(t) to D and projecting to gr_F D gives a unique normalized tensor splitting β(t)∈Q. Define

    γ(t)=(β(t)a(t))^{-1},
    φ(t)=F_1(t),
    ψ(t)=the bigrading of (F_1(t),F_2(t)).

All five maps are regular on T° (and therefore rational on T): matrix expressions for intersections and projections use nonvanishing minors on the opposed open set. They take values respectively in P_M,Q,P'',Fil,Big. At the comparison point they recover the page's α,β,γ,φ,ψ. In particular

    K=k(α,β) ⊂ Qbar(α,overline{α})

after the stated algebraic base extension, with the unextended inclusion into the compositum k(α)c(k(α)) obtained directly from the same formulas. This proves the precise relation behind Lead H2; it does not assert equivalence of maximality for one projection with genericity of the entire joint point.

## 4. Image dimensions

Choose the actual complex comparison only to identify the geometric groups and stabilizers; dimensions are unchanged by this C-base change. Let μ be the Hodge cocharacter of M, w the central weight cocharacter, B=P(μ), B^−=P(wμ^{-1}), L=Z(μ), U=R_u(B). The Hodge cocharacter of N, after the j_B identification, is

    λ=(μ,wμ^{-1})∈J_C.

Therefore

    B_J=P_J(λ)=J∩(B×B^−)

is a parabolic in the identity component (with the evident componentwise stabilizer in the general case). The projection B_J→B is surjective on identity components. One verification is to decompose Lie J and Lie G into cocharacter weights: surjectivity of Lie J→Lie G is surjective in every weight, hence on the nonnegative weights defining the two parabolics; the image is a closed subgroup of the connected parabolic with full Lie algebra. The same argument gives surjectivity on their Levi quotients.

Define

    n=dim N_2,  n_B=dim(N_2∩B^−),  v=n−n_B.

Equivalently v is the dimension of the strictly positive (or strictly negative) Hodge-weight part of Lie N_2. It satisfies 0≤v≤u. It is also the dimension of the N_2-orbit in G/B^−. Normality of N_2 makes this orbit dimension the same at every flag in that G-orbit.

### The image-dimension theorem

The dimensions of the Zariski closures of the indicated images of the component of T° containing the comparison are

| Image | Dimension |
|---|---:|
| α | g |
| β | u |
| γ | b+v |
| φ | u=g−b |
| ψ | u+v |
| (α,β), or equivalently (β,γ) | g+v |

**Proof.** Projection onto α is surjective on the corresponding torsor component, giving g. Projection onto φ is its filtration quotient, giving g−b=u. The ψ-map is the orbit of the pair (F,overline F), restricted to opposed pairs, and its stabilizer is B_J. The map B_J→B has kernel N_2∩B^−, hence dim B_J=b+n_B. Since h=g+n,

    dim image ψ = h−dim B_J = u+v.

For the two remaining fibre computations it is preferable to use the de Rham form of J and its Hodge parabolics, which are defined algebraically. Identify these geometrically with the displayed groups. Set

    S_γ=J∩(U×B^−),       S_K=J∩(1×B^−).

We prove the asserted fibres rather than count parameters. If t'=(xa,yd) for (x,y)∈S_γ, the second de Rham flag changes by x and the normalized splitter changes from β to βx^{-1}. Thus γ(t')=γ(t). Conversely, γ(t')=γ(t) implies β'a'=βa, so x=a'a^{-1}=β'^{-1}β∈U. The equality of γ's also identifies the opposite Betti flags; the formula for F_2 then gives y∈B^−. Hence the fibres of γ are exactly S_γ-cosets. The same argument, with a'=a and β'=β, shows that the fibres of (a,β) are exactly S_K-cosets.

The projection S_γ→U is surjective: it is the preimage of U under the surjection B_J→B. Its kernel is S_K. Consequently

    dim S_K=n_B,
    dim S_γ=u+n_B,
    dim image(a,β)=h−n_B=g+v,
    dim image γ=h−u−n_B=b+v.

Moreover each fibre of the last map carries the full simply transitive U-action on normalized splittings. Under the algebraic isomorphism

    P×Q → Q×P'',   (a,β)↦(β,(βa)^{-1}),

whose inverse is (β,γ)↦(β^{-1}γ^{-1},β), the image is Q times the γ-image. Its Zariski closure is therefore Q×Γ, where Γ is the γ-image closure. This proves dim image β=u, without assuming the actual β transcendental. Every calculation concerns identity components; the finite set of other components changes none of these dimensions. ∎

The criterion for v=u is explicit in the common quotient. Let C=G/N_2^0 (or use the scheme quotient by all N_2; finite kernels do not affect the assertion). Then u−v is the dimension of the positive Hodge-weight part of Lie C. Thus v=u precisely when the projected Hodge cocharacter is central in C^0, equivalently its Hodge parabolic has full dimension dim C. This is exactly the criterion that the closure of the (α,β)-image fill the appropriate component of P×Q. The common quotient may retain a Tate or other central torus; independent noncentral Hodge directions are what matter.

## 5. Actual transcendence degrees and genericity

Every image above is defined over an algebraic field, so the actual coordinate transcendence degree is at most its dimension. In the notation of the theorem, unconditionally:

    trdeg_k k(α)≤g,      trdeg_k k(β)≤u,
    trdeg_k k(γ)≤b+v,    trdeg_Q Q(φ)≤u,
    trdeg_Q Q(ψ)≤u+v,    trdeg_k K≤g+v.

There are also uniform relative bounds:

    trdeg_{k(α)} K≤v,
    trdeg_{k(β)} K≤b+v,
    trdeg_{k(γ)} K≤u.

The middle and last bounds follow from the product Q×Γ just proved. For the first, fix a: the remaining second comparison varies under the normal subgroup N_2, and its flag image is an open subset of an N_2-orbit in G/B^−. All such orbits have dimension v by normality. Equivalently the quotient T/S_K is a homogeneous bundle over P with fibres N_2/(N_2∩B^−), and the opposed condition removes an open complement. This proves the bound for the fibre over the actual coordinate field, including nongeneric actual points; a generic-fibre estimate alone would not have sufficed.

Let PG(N) denote the assertion that the actual comparison of N is generic in its component of the motivated comparison torsor, or equivalently that its coordinate field has transcendence degree dim J. This is the motivated-torsor genericity consequence of the Grothendieck period conjecture discussed in §0. A rational map defined at a generic point sends it to the generic point of its image: the inclusion of function fields into the comparison field is injective. Applying this to the six maps proves all equalities in the image table under PG(N). Subtracting the absolute degrees in field towers gives

| Degree | Value under PG(N) |
|---|---:|
| trdeg_k k(α) | g |
| trdeg_k k(β) | u |
| trdeg_k k(γ) | b+v |
| trdeg_Q Q(φ) | u |
| trdeg_Q Q(ψ) | u+v |
| trdeg_k K | g+v |
| trdeg_{k(α)} K | v |
| trdeg_{k(β)} K | b+v |
| trdeg_{k(γ)} K | u |

This is a proved implication for the named motive N, as explicitly requested in A.2; it is not an unconditional assertion of genericity.

Thus the original α and φ values follow from PG(M) alone by the corresponding dominant maps. All the original values follow from PG(N) exactly in the case v=u. For v<u the original values for γ, ψ, K, K/k(α), and K/k(β) are false unconditionally, since their unconditional upper bounds are already strictly smaller. The β value and the K/k(γ) value agree with the corrected prediction for every v. The calculations do not establish their actual values in every motive.

PG(M) alone also implies useful exact lower bounds, without assuming PG(N): trdeg_k k(β)≥u−v and trdeg_k k(γ)≥b, by combining trdeg_k K≥g with the uniform relative bounds. In particular when v=0 it gives the entire corrected table, because K has degree g, β then has degree u, and γ has degree b. We do not claim that no additional arithmetic theorem could imply further statements from PG(M) in other cases.

Lead H2, read as saying that joint period genericity **implies** the β prediction, is proved by the β-map. Its grounds specifically say that the conjugate periods add exactly u new transcendentals. That assertion is false for the real non-CM elliptic example: the conjugate period field is the same period field and adds zero, while u=1. The exact corrected object is the image T°→P×Q, of dimension g+v; it has not in general been identified with the whole joint torsor. A claim that algebraic genericity of the β projection is logically equivalent to joint comparison genericity is not proved by a dominant projection. The image and fibre calculations above state exactly the established relation. We have not supplied a motive for which one of those two arithmetic genericity properties is proved and the other disproved; an equivalence interpreted in that stronger literal truth-value sense remains unsettled here.

## 6. Real models: exact field identities and stronger refutation

Suppose M=M_0⊗_{k_0}k with k_0⊂R. The real Frobenius f_∞ on the rational Betti realization of M_0 exchanges the two Hodge indices. Hence

    overline{φ}=f_∞φ,
    opposite(F_D)=α f_∞ α^{-1}F_D.

These are equations of filtrations. The first shows that the bigrading ψ is rational over Q(φ); the forgetful map proves the opposite containment, giving

    Q(ψ)=Q(φ).

The second constructs β by rational operations in α over k, hence

    β∈Q(k(α)),     γ∈P''(k(α)),     K=k(α).

This proves Lead A's field identities. The rational involution f_∞ need not belong to the smaller motivic group over a nonreal extension k; it normalizes that group through conjugation of the relevant tensors, which is sufficient. We do not assume that extra membership.

Over Qbar, c^*M is isomorphic to M, so the joint group is a graph and N_2 is trivial: v=0. The unconditional bounds strengthen to

    trdeg_k k(γ)≤b=g−u,
    trdeg_{k(β)}K≤b,
    trdeg_Q Q(ψ)≤u,
    trdeg_k K≤g,
    trdeg_{k(α)}K=0.

For u>0 these individually refute the original proposed values g, g, 2u, g+u, u in those five positions. Under PG(M) the exact corrected table is

    (α,β,γ,φ,ψ,K; K/α,K/β,K/γ)
       = (g,u,b,u,u,g; 0,b,u).

The same dimension result v=0 holds when M is isomorphic to c^*M over Qbar without a chosen real model. Field equality over the original k may then require an algebraic extension to define the isomorphism; transcendence degrees transfer by §1. If such an isomorphism is fixed, its rational Betti map identifies the two Hodge flags, proving Q(ψ)=Q(φ) in that case as well.

## 7. An explicit elliptic counterexample and exact computation

Let k=Q with its usual embedding and let

    E: y^2=x^3−x+1,      M=h^1(E).

The discriminant is −368 and j(E)=−6912/23. The latter is not an algebraic integer, so E has no complex multiplication by integrality of CM j-invariants. For a non-CM elliptic curve its Hodge group together with homotheties is GL_2: the Hodge realization is irreducible, its Hodge endomorphism algebra is End(E)⊗Q=Q (the lattice description of complex torus homomorphisms proves this equality), and a connected reductive subgroup of GL_2 containing the scalar torus with that irreducible representation is GL_2. Motivated tensors are Hodge, so the motivated group contains this GL_2 and is therefore exactly GL_2. Thus

    g=4, b=3, l=2, u=1.

Choose a rational Betti eigenbasis of f_∞, with matrix diag(1,−1), and a de Rham basis whose first vector spans F^1. Put

    A=α=[[a,b],[c,d]],    D=ad−bc.

At the actual comparison c and d are nonzero: otherwise F^1_B would be an eigenline of f_∞, contrary to F^1_B∩overline{F^1_B}=0. Direct multiplication gives

    A f_∞ A^{-1} = D^{-1}[[ad+bc,−2ab],[2cd,−ad−bc]],
    β=[[1,−(ad+bc)/(2cd)],[0,1]],
    βα=[[D/(2d),−D/(2c)],[c,d]],
    γ=[[d/D,1/(2c)],[−c/D,1/(2d)]].

In particular

    γ11 γ22 + γ12 γ21 = 0.

This nonzero polynomial relation on GL_2 proves trdeg_Q Q(γ)≤3. The corresponding rational map has rank three, checked symbolically, so its image dimension is exactly three. Together with K=Q(α), this gives an unconditional explicit counterexample to every failed value listed in §6, including the γ assertion itself.

Computation: `work/code_triangle/real_gl2.py`, output `work/code_triangle/real_gl2.output.txt`; SymPy 1.14.0; exact rational functions in Q(a,b,c,d); no numerical precision parameter; open chart (ad−bc)cd≠0; all identities and Jacobian rank checked; discriminant and j computed exactly; wall time approximately 0.35 seconds. The program verifies symbolic algebra and the rational invariants of the curve. It makes no numerical algebraicity or transcendence claim.

## 8. Elliptic filtration fields and known cases

For any E/Qbar, choose a nonzero algebraic holomorphic differential and an oriented integral homology basis with periods ω1,ω2. Then F^1_B is the line spanned by (ω1,ω2); with τ=ω2/ω1,

    Q(φ)=Q(τ),       Q(ψ)=Q(τ,overline τ).

If E is isogenous to its conjugate, the lattice criterion for isogenies supplies a GL_2(Q) fractional-linear relation between τ and overline τ. Hence Q(ψ)=Q(φ). With a real model the lattice relation can be taken integral after compatible choices. Schneider's theorem (to be supplied by the elliptic-source agent with its opened locator) gives degree one in the non-CM case, while CM gives an imaginary quadratic τ and degree zero. These facts prove the original φ value for elliptic curves and refute the original ψ value for real non-CM elliptic curves with its exact actual value, not only an upper bound.

For CM elliptic M, u=0 and g=2, and c^*M belongs to the same generated category because conjugate CM elliptic curves are isogenous over Qbar. Thus PG(M), supplied by Chudnovsky in the normalization checked by the elliptic agent, yields the actual tuple

    (α,β,γ,φ,ψ,K; K/α,K/β,K/γ)=(2,0,2,0,0,2;0,2,0).

Genericity passes to any tensor subcategory by the dominant projection of torsors. This proves the corresponding table for every motive in the tensor category generated by that CM elliptic motive and Artin motives. We do not infer the period conjecture for arbitrary products of nonisogenous CM elliptic curves or general CM abelian varieties from the one-curve case.

For u=0 in any pure motive, Q is a point, β is algebraic, K=k(α)=k(γ), and φ,ψ are algebraic. Their zero degrees and zero relative degrees are unconditional. The remaining common degree is the ordinary period degree of M; its value g still requires its own genericity theorem or conjecture.

## 9. Unsettled statements that these proofs do not close

1. The universal numerical value of trdeg k(α) includes the ordinary period conjecture for motives. This contribution proves the upper bound and the exact requested implication from named genericity; it does not prove that conjecture.
2. For a non-CM elliptic curve not isogenous to its conjugate, the joint group has the determinant-fibre-product form once the usual product Mumford–Tate calculation is supplied, giving v=1 and predicted ψ-degree 2. The actual algebraic independence of τ and overline τ is not proved here.
3. The algebraicity/transcendence of the actual non-CM splitting β remains the A.4(c) gate handled by the elliptic agent. The dominance calculation dim image β=u does not prove genericity of the actual β.
4. H2's grounds about adding u transcendental conjugate periods are explicitly refuted by the real example. H2 interpreted as a literal arithmetic equivalence between β-genericity and joint genericity is not established or refuted here.
5. Exact general classification of what follows from PG(M) alone beyond the implications and lower bounds of §5 is not supplied by the geometry. No failed deduction is represented as a counterexample to a statement about actual motives.


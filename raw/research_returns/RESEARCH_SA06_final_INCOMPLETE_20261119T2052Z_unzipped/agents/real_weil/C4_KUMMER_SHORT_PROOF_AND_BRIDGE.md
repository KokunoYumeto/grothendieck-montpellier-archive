# A short Kummer-fourfold proof and the exact odd-degree family bridge

**Status: proved auxiliary simplification, rational-map exclusion for K_2(A), and an equivalent reformulation through arbitrary odd numbers of points. No strictly smaller main existence gate is claimed.**

Credit: GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, run `/root/component_families`; effort setting not separately exposed. Date: 19 November 2026. Root proposed the rational-map square-scalar extension and the general odd-degree bridge. The derivations and source-scope checks below were reconstructed by the owner. No priority claim.

## 1. Retained hypotheses and correspondence convention

Let A/C be a complex abelian surface with primitive polarization ell of type(1,2), and assume

    NS(A)=Z ell,
    End_HS H¹(A,Q)=Q,
    End_HS T(A)_Q=Q,

where T(A)_Q=ell-perp in H²(A,Q), for the ordinary intersection form q. The first-Hodge-endomorphism hypothesis is only needed for the arbitrary-correspondence bridge. The incidence-cut and rational-map arguments use the other two conditions.

The C.4ab convention is the pullback convention

    Z^*α=(p1)_*([Z] cup p2^*α),

for Z in CH²(A_source×A_target). Its integer scalars on H¹ and T are denoted t and s. Using the transpose convention without changing the argument would be erroneous: a cycle supported over a source divisor can affect the opposite H³/H¹ action. Everything below uses precisely the displayed convention.

## 2. A short proof of the K_2(A) parity theorem

Let K=K_2(A), let U in CH²(A×K) be the actual universal length-three subscheme, and set

    μ=U_*:H²(A,Z)→H²(K,Z).

This is the incidence normalization μ(a)=(1/2)θ^*(q1(a)q1(1)²|0>), as fixed in the audited original note. Choose the integral hyperbolic basis u1,u2,v1,v2,w1,w2 of H²(A,Z), with ell=u1+2u2 and q(u1,u2)=q(v1,v2)=q(w1,w2)=1. Set

    Q=μ(u1)μ(u2)+μ(v1)μ(v2)+μ(w1)μ(w2).

The geometric input is the integral actual surface identity

    Q/6=[Y_p] in H⁴(K,Q),                            (KS.1)

from Kapfer and Menet (2018, Corollary6.28) and the actual fixed-support-point surface construction in Hassett and Tschinkel (2013, Section4). In particular Q/2 is represented by an integral class. This argument does not use the half-square classes B_y, the rank-28 lattice determinant, or any normalization from the inconsistent line in the printed Proposition6.30 proof. Those are independently checked alternate arguments, retained in the original note.

For any integral Hodge class h in H⁴(K,Z), define the integral symmetric bilinear form

    B_h(a,b)=integral_K h μ(a)μ(b)

on H²(A,Z). The form is a Hodge pairing. Relative to the unimodular Hodge intersection form q, the associated rational Hodge endomorphism has no cross terms between T and Q ell, and is scalar s on T. Therefore there is a rational κ with

    B_h(a,b)=s q(a,b)+κ q(ell,a)q(ell,b).             (KS.2)

There is no assumption that the rational Hodge decomposition splits integrally. Instead, evaluate the actual integral form on the displayed basis:

    κ=B_h(u2,u2) in Z,
    s=B_h(v1,v2) in Z.                               (KS.3)

Here q(ell,u2)=1, q(u2,u2)=0, and v1,v2 are perpendicular to ell. Pairing h with the integral class Q/2 yields

    (3s+2κ)/2 in Z.

Thus s is even. The incidence composition U^t h U has H¹ action zero because it factors through H¹(K,Q)=0. This proves the parity theorem for every integral Hodge cut, and hence every integral algebraic surface cut.

In fact (KS.1) gives the stronger construction-specific congruence

    3s+2κ in 6Z,

so κ belongs to3Z as well. The actual cut Y_p has s=2, as checked by its pairing identity in the original note. Therefore the scalar subgroup for the displayed incidence-cut construction remains exactly2Z.

## 3. Every rational map A to K_2(A) has even incidence scalar

Let f:A⇢K be any rational map. Resolve it by a sequence of point blow-ups π:A'→A, and write g:A'→K for the resulting morphism. Define the incidence pullback on H²(A) by

    f^*μ=π_*g^*μ.

It is an integral Hodge endomorphism. On T it is multiplication by an integer r: it preserves the nonzero integral transcendental lattice and End_HS(T_Q)=Q.

The blow-up decomposition is

    H²(A',Q)=π^*H²(A,Q) perpendicular-sum (sum_j Q E_j),

and every exceptional direction is of type(1,1). There are no Hodge homomorphisms from T to any of these Tate directions or to Q ell. Hence

    g^*μ(a)=r π^*a,          a in T(A)_Q.             (KS.4)

Let h be the integral algebraic surface class g_*[A'] on K, with its actual pushforward multiplicity; it is zero if the image has smaller dimension. Projection formula gives

    B_h(a,b)=integral_A' g^*μ(a)g^*μ(b)
             =r² q(a,b),           a,b in T(A)_Q.

The scalar of Section2 is therefore r², which is even. Since r is an integer, r is even. This conclusion covers every rational map A⇢K_2(A), not merely incidence compositions chosen in advance from special surface cycles.

Equivalently, any generically defined family of reduced length-three zero-cycles on A with sum zero, parametrized by A, has even scalar on T. The extension does not assert a factorization of arbitrary correspondences through K_2(A).

## 4. From an arbitrary correspondence to an effective odd-degree family

Let Z be any integral codimension-two correspondence on A×A, with C.4ab scalars t,s. Put F=C(A), the function field of the source, and restrict Z to a zero-cycle z on A_F.

### 4.1. An effective reduced representative after adding constant points

Choose a smooth projective geometrically integral curve C⊂A_F containing0 and all the closed points in the signed support of z. Such a curve exists over the infinite characteristic-zero field F. For completeness, choose a high ample linear system vanishing at this finite reduced set. Serre vanishing supplies arbitrary first jets at its points; a general section is transverse there. Stacks Lemmas33.47.1 and33.47.3 give an immersion and Bertini smoothness away from the set. Taking the degree still higher ensures geometric connectedness: Serre duality and Serre vanishing give H¹(A_F,O(−C))=0 after any algebraic extension, and the Cartier sequence gives H⁰(O_C)=F geometrically. A smooth geometrically connected curve is geometrically integral.

Regard z as an integral signed divisor on C. For every sufficiently large integer M, the line bundle

    O_C(z+M[0])

is very ample. One can see the needed jet separation directly from curve Riemann–Roch and duality: after any length-two subscheme is subtracted, the dual line bundle has negative degree, so H¹ vanishes. A general F-rational section therefore has a reduced effective zero divisor D. The field F is infinite, so the nonempty open set of such sections has F-rational points. We obtain

    [D]=z+M[0] in CH0(A_F),
    deg(D)=N=deg(z)+M.                               (CB.1)

As M can be any sufficiently large integer, N may be chosen odd and at least3. All support points of D are separable over F, since the characteristic is zero. Thus D defines a reduced finite length-N subscheme and an F-point of A^[N], not merely a point of its symmetric product.

Spread D and the rational equivalence in (CB.1) over a nonempty source open. Its closure W in A×A is an effective correspondence generically finite and generically étale of degree N over the source. Localization for Chow groups gives

    [W]−[Z]−M[A×{0}] = a class supported over
                       a proper closed subset of the source.    (CB.2)

No division or generically finite extension of the source function field has been used.

### 4.2. Why the relevant scalars survive the vertical error

A codimension-two cycle supported over a source curve factors, after normalizing that curve, through a divisor correspondence on a smooth curve times A. With the pullback convention of Section1, its action on H^j(A) first lands in H^(j−2) of the curve, followed by the Gysin map to H^j(A).

For j=1 this is zero. For j=2 it factors through Tate H⁰ of the curve, and vanishes on T because there is no rational Hodge homomorphism from T to a Tate structure. Cycles supported over source points also act trivially in these two degrees. The constant correspondence A×{0} acts trivially on positive-degree target cohomology. Hence W has the same t and s as Z.

This source-vertical assertion would be false if silently replaced by a statement about the opposite H¹ action. The explicit convention is essential.

## 5. Make the sum zero and compute the two scalars exactly

Over a dense open, W gives a rational map A⇢A^[N]. Its sum is a rational map σ:A⇢A. The extension and rigidity theorems for abelian varieties make σ a morphism of the form

    σ(x)=[t]x+c.                                    (CB.3)

Indeed its action on H¹ is the trace of the zero-cycle family, namely W^* on H¹, so its homomorphism part acts by t. The scalar Hodge-endomorphism hypothesis and the integral H¹ lattice identify that part with multiplication by the integer t.

Pull the family back on the source by [N]:A→A. Its sum is [Nt]x+c. Choose a constant a∈A(C) with [N]a=c, and translate every point of the pulled-back cycle by −[t]x−a. The sum is now zero. The generic points remain distinct, and we get a rational map

    f:A⇢K_(N−1)(A).                                 (CB.4)

Its incidence correspondence W' is an actual integral correspondence of degree N. On H¹ it has scalar

    t'=Nt−Nt=0.

Here is the full H² calculation, including the cross terms. For α,β∈H¹(A), a point y of the pulled-back family is replaced by y−tx−a, so the degree-one pullbacks are y^*α−tα and y^*β−tβ. Trace over the N points, or equivalently use the coproduct formula for the addition morphism and projection formula for W. The first term is N²W^*(αβ); the two cross terms are each −Nt²αβ; the last term is +Nt²αβ. Thus

    (W')^*|H² = N² W^*|H² − Nt² id,                 (CB.5)
    s'=N²s−Nt²=N(Ns−t²).

These formulas are integral identities of the relevant scalar actions. They do not require labeling the points globally or dividing by the degree of a labeling cover. The constant translation does not affect cohomology.

For odd N,

    s' congruent s−t modulo2.                       (CB.6)

Consequently any integral correspondence satisfying the C.4ab odd-parity test supplies an odd transcendental incidence scalar for a rational map (CB.4), for some sufficiently large odd N.

Conversely, any rational map A⇢K_(N−1)(A), with odd incidence scalar r on T, supplies an actual integral correspondence by resolving its graph and pushing back its universal finite family. The H¹ action is zero, since H¹ of the generalized Kummer fibre vanishes. Hence t−s=−r is odd, and C.4ab applies. Equivalently, on the dense family open the sum is constantly zero, which already gives its H¹ action zero; source-vertical closure errors do not change it.

We have proved an **equivalence**:

    some integral correspondence has t−s odd
      if and only if
    some rational map A⇢K_(N−1)(A), for an odd N,
    has odd incidence scalar on T.                  (CB.7)

Section3 excludes N=3. The N=1 fibre is a point and also gives no odd scalar. This does not bound the N needed in the construction or reduce arbitrary N to3. The curve chosen in Section4 depends on the generic signed zero-cycle, and its genus can be arbitrarily large in this proof.

## 6. What has and has not been accomplished

The K_2(A) theorem now has a short proof using only the normalized incidence map, the Hodge-endomorphism hypotheses and the integral Q/2 class. It excludes all rational maps from A to K_2(A) with odd incidence scalar.

The odd-degree bridge keeps the exact integral scalar and the actual generic finite family; it removes no main existence difficulty by itself. A proof that every rational map A⇢K_(N−1)(A) has even incidence scalar for every odd N would refute the residual C.4 existence condition. Conversely one odd example would solve it positively. Neither assertion is proved here.

The companion note `C4_KUMMER_FIVE_POINT_OBSTRUCTION.md` proves that the particular Q/(2N)-integrality strategy fails at N=5, including the required two-primary saturation and torsion repair. That failure does not imply either existence or nonexistence of an odd map at N=5. The remaining gate is still the arbitrary integral correspondence from C.4ab.

## 7. Exact source-read receipt

The K_2(A) source chain is the already completed published/author Kapfer–Menet and Hassett–Tschinkel audit in `C4_KUMMER_INCIDENCE_RESEARCH.md` and its root/cycles independent receipts. The new short proof deliberately uses Corollary6.28 rather than the half-square statement whose displayed proof needed normalization repair. All source versions and prior read boundaries remain unchanged.

During the checkpoint23 freeze, the entire displayed statements and proofs of Stacks Lemmas33.47.1 and33.47.3 were freshly read at Tag0FD4; the exact first-jet/finite-base-locus supplement used in Section4 is explained there rather than attributed to an unstated theorem. Stacks Lemma53.5.2, Tag0BS6, was freshly read with its full displayed proof; duality and the negative-degree no-section argument give the stated curve positivity. The general Serre-duality/Serre-vanishing foundations and the Chow localization theorem were not completely reopened in this continuation.

Milne's author course notes *Abelian Varieties*, version2.00, March2008, were opened at the official source. Freshly read the complete displayed proofs of ChapterI Theorem1.1 and Corollary1.2 (printed pp.8–9), Theorems3.1–3.2 and Lemma3.3 (pp.16–18), and the statement and complete short proof of Corollary3.7 (p.19). The proof of Theorem3.4 and its curve lemmas were also encountered in the opened range but are not a separate essential dependency here. The source's cited earlier algebraic-geometry foundations were not all reopened. A guessed `xnotes/AV.pdf` URL failed; it supplies no evidence. The actual opened course-notes URL below succeeds.

Retrievals: Stacks turn949530686view0–1; Milne turn808651861view1, turn646410253view0–1 and turn453397937view1. Source scopes were read during20:02–20:05UTC; these clock intervals are not claimed measured reading runtimes. No numerical experiment is necessary for the universal identities (KS.2) or(CB.5); their explicit algebra is the proof.

### References

Hassett, B., & Tschinkel, Y. (2013). Hodge theory and Lagrangian planes on generalized Kummer fourfolds. *Moscow Mathematical Journal, 13*(1),33–56. https://www.math.brown.edu/bhassett/papers/hodge/hodge13.pdf

Kapfer, S., & Menet, G. (2018). Integral cohomology of the generalized Kummer fourfold. *Algebraic Geometry, 5*(5),523–567. https://doi.org/10.14231/AG-2018-014

Milne, J. S. (2008). *Abelian varieties* (Version2.00, course notes). https://www.jmilne.org/math/CourseNotes/AV.pdf

The Stacks Project Authors. (2026). *Bertini theorems* (Section33.47, Tag0FD4). https://stacks.math.columbia.edu/tag/0FD4

The Stacks Project Authors. (2026). *Riemann–Roch* (Lemma53.5.2, Tag0BS6). https://stacks.math.columbia.edu/tag/0BS6

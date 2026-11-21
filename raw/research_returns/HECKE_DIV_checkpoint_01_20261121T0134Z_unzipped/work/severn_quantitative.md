# Explicit quantitative extraction from the Severn supplier construction

Run HECKE_DIV_20261121; checker /root/markman, GPT-6 Astra Pro, 2026-11-21; effort setting not exposed. This is a new derivation, not a numerical claim made by the cited manuscript. The small arithmetic is independently executable in `severn_quantitative.py`. The geometric inputs are Schoen's actual cycles, with the local repair in Severn where needed, the classical invariant theory used in Milne, and the independently checked dominance certificate. The parent is independently checking the new degree estimates.

Throughout K=Q(ω), ω²+ω+1=0, and O=Z[ω], a principal ideal domain. A polarization is measured by its integral first Chern class θ, without dividing by a factorial. For a cycle of dimension d, degree means ∫θ^d over the cycle. A signed cycle's **degree mass** is the sum of the absolute multiplicities times the degrees of its irreducible components. This bounds the degrees of its positive and negative parts separately.

## SQ1. The explicit integer expression

Write

    G = 39,191,040,
    g = 4G+1 = 156,764,161,
    R = (2G+1) G! G^G,
    L = 2gR,
    S0 = G^(2g) (g!)²,
    SB = (L/2)! S0^R,
    k = L/2+4,
    B0 = (40G)^k binom(k,4) SB · 8! · G^8.

Let Δ be the product of the elementary divisors of the fixed target polarization. Assume the K-action preserves the target integral lattice, as it does for the balanced principal E⁸ datum and for the integral block action of type (1⁴,3⁴). Put

    N = 4 G^8 Δ,
    D = N^8 B0.

The derivation below supplies, on a nonempty analytic open subset of the fixed split unitary moduli family, an **effective integral four-dimensional cycle Z of degree at most D whose rational projection onto the Weil plane is nonzero**. It gives a finite collection of such effective cycles whose projected classes span that plane. For the balanced principal datum Δ=1. All quantities are explicit integers; their factorial notation is intentional. No claim of practicality or optimality is made.

The parent's explicit principal-lattice projector and two-dimensional calculation can convert D into a bound for any fixed flat rational Weil section. An independent, more general Gram-matrix conversion is also recorded in SQ9 below.

## SQ2. Group order, genus, and a common projector denominator

The exact group certificate is in `severn_group.py`: the ten printed reflections generate a faithful permutation group of order G. The monodromy tuple has twenty terms, each an involution, not ten order-three terms. Riemann–Hurwitz gives

    2g(C)−2 = G(−2+20(1−1/2)) = 8G.

Let σ be the six-dimensional K-representation, χ its character, and s one of its reflections. The rational central idempotent for the pair σ,σbar is

    ε = (6/G) Σ_(a∈G) Tr_(K/Q)(χ(a⁻¹)) a.

Each trace is a rational algebraic integer and therefore an integer. The exact group certificate also verifies membership of all six scalar units, in particular ω·I₆, in G. Since the permutation action is faithful, this element is central in G. The Rosati-symmetric primitive idempotent

    e = ε(1−s)/2

acts on the σ block as projection onto the one-dimensional negative eigenspace of s. Its conjugate block is the same rational simple factor M₆(K). Consequently G e belongs to Z[G]: the factor6/2 is3. This constructs the eight-dimensional Prym–Tyurin factor A=im(G e) with a denominator at most G, rather than an unspecified denominator. The central element ω·I₆ commutes with e and preserves A as an abelian subvariety; its action on A satisfies ω²+ω+1=0. Hence the source lattice H₁(A,Z) is O-stable. This is the source-side integrality used in SQ7.

For a supplier (H′,χ′) of order m, the primitive rational idempotent in Q[H′] has coefficients

    (1/|H′|) Σ_(t∈(Z/m)*) χ′(a)^(−t),

which are integer Ramanujan sums divided by |H′|. Since |H′| divides G, G also clears every supplier projector. The later construction will keep the cycles on powers of quotient curves, so it does not require degree estimates for the supplier Prym factors.

### Polarization consequence

Let Λ=H₁(J(C),Z), with its unimodular alternating form E, and let Λ_A=Λ∩e(Λ_Q). Orthogonal projection identifies the dual lattice Λ_A^# for E|_A with eΛ. Indeed, every integral functional on the primitive sublattice Λ_A extends to Λ, and unimodularity then identifies it with pairing against an element of Λ; projecting that element gives the desired representative. Hence

    G Λ_A^# = G eΛ ⊂ Λ_A.

Thus the exponent of the polarization kernel on A divides G. Each elementary divisor d_i divides G, and

    Δ_A=∏_(i=1)^8 d_i divides G^8,
    ∫_A θ_A^8 = 8! Δ_A ≤ 8! G^8.

This proof uses that e is Rosati symmetric. An arbitrary nonsymmetric projector would not give this lattice assertion.

## SQ3. An explicit size bound for an integral supplier identity

Brauer induction and Severn's real-branch argument show that the target determinant character e_σ is an integer combination of admissible supplier character columns, in a group Z^a⊕(Z/2)^b. This is Severn's Theorem `thm:brauer`, source lines310–326. The optional reported84-row identity is unnecessary for the following numerical bound.

The discarded Brauer terms are harmless for a precise reason. A linear character of order1 or2 is real, so its restriction multiplicities for a nonreal pair τ,τbar agree, and its free determinant coordinates vanish. For a quaternionic τ, the τ-representation has a nondegenerate invariant alternating form. The isotypic summand of a real one-dimensional character is orthogonal to every other isotypic summand and has a nondegenerate alternating restriction, so its multiplicity is even; the coordinate modulo2 also vanishes. If a character of order at least3 has h=0, then h=Σ_τ m_τ mult_χ(τ|H′) is a sum of nonnegative integers, forcing every multiplicity with m_τ>0 to vanish, so its entire determinant column is zero. Every remaining character has m≥3 and h>0. For the present involution branch data, any nonzero cyclic branch exponent is m/2; the global cyclic relation makes their number even. Thus the exponents pair with their negatives, and h=2q−2+s is even. These are exactly the supplier hypotheses used below.

Adjoin columns2e_j for the torsion coordinates and work in Z^(a+b). Every supplier column has absolute entries at most G: its free entries are differences of multiplicities in restrictions of irreducible representations, and each multiplicity is at most the representation's dimension, itself at most G. There are at most G irreducible representations, so the row dimension is at most G.

Here is an elementary integer-linear-algebra bound. Let an integer matrix have entries of absolute value at most M, rank r, and let a vector b of coordinate size at most1 lie in its integral column lattice. Select r independent rows and r independent columns, giving an invertible square matrix B. Projection to these rows is injective on the rational column span. Put d=|det B|≤r!M^r. The subgroup of Z^r/BZ^r generated by the remaining columns has at most d elements. A shortest path from0 to the class of b in its Cayley graph, using columns and their negatives, has at most d−1 steps. Thus, after subtracting at most d−1 signed columns, the residual v lies in BZ^r and satisfies

    |v|_∞ ≤ 1+(d−1)M ≤ dM.

Cramer's rule and the cofactor bound (r−1)!M^(r−1) give |(B⁻¹v)_i|≤r!M^r. Therefore a solution exists with total absolute coefficient at most (r+1)r!M^r. Taking r≤G and M=G is bounded by R=(2G+1)G!G^G. Removing the auxiliary torsion columns can only reduce the supplier coefficient sum.

There consequently exists an admissible identity

    e_σ = Σ_i n_i a(χ_i),     Σ_i |n_i| ≤ R.

The proof is an explicit a priori bound, even though enumerating the resulting enormous finite matrices would be impractical. It does not assert that the optional231-coefficient witness has been verified.

## SQ4. Effective cycles on the powers of each supplier curve

Fix a supplier and set C′=C/kerχ, X=C/H′. Write m=ordχ and h for the primitive eigenspace dimension. Then m≤G. Since φ(m)h is the dimension of the primitive part of H¹(C′),

    φ(m)h ≤ 2g(C′),     h≤g(C′)≤g,

because m≥3 gives φ(m)≥2. The admissibility argument makes h positive and even.

Schoen's construction in Theorem2.0, Lemmas2.3–2.6 (1988, printed pp.11–17), has a finite quotient

    q:C′^h → W₀=C′^h/G₀ → Sym^h X,
    |G₀|=m^(h−1) h!,

where G₀ is the kernel-of-sum subgroup in (Z/m)^h, extended by S_h. It constructs a linear projective space P₀ of dimension h/2 inside an Abel–Jacobi fibre of Sym^hX. After the specified blow-ups the cover splits over its strict transform, and a chosen component pushes to a subvariety Q₀⊂W₀ mapping birationally, indeed with degree one, onto P₀. The blow-up map restricts to an isomorphism on the strict transform of P₀. The primitive character components of [Q₀] are all nonzero; this is precisely the nonvanishing proved by Schoen's normal-bundle calculation and, when necessary, Severn's repair of the exceptional-divisor argument.

For a general point x∈X, the point-incidence divisor x+Sym^(h−1)X restricts to the hyperplane class on P₀. If H is the sum of the degree-one point classes on the h factors of C′^h, its pullback to C′^h is numerically mH. Hence

    ∫_(Q₀) β₀^*[x+Sym^(h−1)X]^(h/2)=1.

Choose an irreducible component Z₀ of q⁻¹(Q₀), and let e₀ be its degree over Q₀. Then e₀≤|G₀| and

    deg_H Z₀ = e₀ / m^(h/2).

Use the **integral** orbit sum R₀=Σ_(a∈G₀) a_*Z₀, retaining repetitions. Its class equals e₀ q^*[Q₀], by the finite-quotient transfer identity q^*q_* = Σ a_*. This avoids any assumption that q is flat along Q₀. Therefore

    deg_H R₀ = |G₀| e₀ / m^(h/2) ≤ |G₀|² / m^(h/2).

Let δ(t) denote the residual cyclic action. The Ramanujan sum c_m(t)=Σ_(u∈(Z/m)*) exp(−2πiut/m) is an integer of absolute value at mostφ(m). Define

    Y = Σ_(t=0)^(m−1) c_m(t) δ(t)_*R₀.

This is an integral signed cycle. It is m times the rational primitive-character projector applied to R₀, so its class belongs to the determinant space U⊂H^h(C′^h), is nonzero, and has nonzero component in every primitive determinant eigenline. All the automorphisms preserve the numerical point class H. Its degree mass is bounded by

    m φ(m) |G₀|² / m^(h/2)
    ≤ m^(3h/2) (h!)²
    ≤ G^(2g)(g!)² = S0.

The additional factor |G₀| in this bound is deliberately retained to make the integral transfer indisputable. No effective desingularization or bound for an exceptional divisor is needed: the cycles are pushed to W₀ before being pulled back by transfer to the smooth product C′^h, and their degrees are measured against a class pulled back from Sym^hX.

## SQ5. Keeping the suppliers on curve powers avoids inverse hard Lefschetz

For the identity in SQ3, put a copy of C_i′^h_i in a product for each of the |n_i| occurrences, and let

    B = product_i (C_i′^h_i)^|n_i|,
    ℓ = dimB = Σ_i |n_i|h_i ≤ gR ≤ L,
    Y_B = external product of the signed cycles Y_i.

Here ℓ is even. With H_B the sum of the degree-one point classes on all curve factors, the external-product degree formula gives

    mass_(H_B)(Y_B)
      ≤ ((ℓ/2)! / product_i ((h_i/2)!)^|n_i|) product_i S0^|n_i|
      ≤ (L/2)! S0^R = SB.

The selected determinant line in H^h_i(C_i′^h_i) has U-character sign(n_i)a(χ_i); its Poincaré-dual line has the negative character and also lies in H¹(C_i′)^⊗h_i. The pairing is nonzero because the cup-product pairing on the relevant primitive eigenspaces is nondegenerate and exterior determinant pairing is perfect. Choose a vector z_i in that dual line pairing nontrivially with Y_i. If x is a generator of the chosen Weil eigenline of H⁸(A), then

    Γ = (external product of the z_i) external product x

is U-invariant, has cohomological degree ℓ+8, and its correspondence action sends Y_B to a nonzero multiple of x. Its algebraic codimension is c=ℓ/2+4. Taking the conjugate selected lines treats the other Weil eigenline as well.

This is the same character cancellation as Severn's Proposition `prop:supply`, but the ambient supplier varieties are curve powers, whose determinant classes are in middle cohomology. Consequently no inverse hard-Lefschetz correspondence from Schoen's Corollary3.1 is needed. This modification is part of the present derivation.

## SQ6. Explicit divisors suffice for the invariant contraction

For a quotient π:C→C′ of degree a=|kerχ|, the morphism

    η:C′ → J(C′) → J(C)

is Abel–Jacobi followed by π^*. On rational first cohomology its pullback is surjective onto H¹(C′), and it has a U-equivariant right inverse, using the averaging idempotent for kerχ and π_*π^*=[a]. The inclusion A→J(C) likewise has a rational U-equivariant retraction supplied by e. Thus Γ lifts to a U-invariant class on J(C)^(ℓ+1), in degree ℓ+8, whose restriction to B×A is Γ.

Here is the needed explicit version of the invariant-theory step. Let V=H¹(J(C),Q), with its alternating polarization form E, and let D=Q[G] be its image in End(V). The centralizer U of D in Sp(E) is a product of symplectic, full orthogonal, and paired general linear groups after scalar extension. The classical first fundamental theorems imply that invariants in the exterior algebra of any number of copies of V are generated by degree-two invariants. The proof is exactly the linear invariant-theory part of Milne (1999), Proposition3.6 and Remark3.7, printed preprint pp.16–18; it does not need the full geometric endomorphism algebra.

More explicitly, the commutant of U on V is D. One can apply Milne's Lemma3.5 to the semisimple algebra End_D(V) with its adjoint involution: its unitary elements generate that algebra, and double centralizers give the assertion. On V^(ℓ+1), invariant alternating forms are E composed with self-adjoint matrices in M_(ℓ+1)(D). These matrices are spanned by diagonal identity blocks, diagonal g+g⁻¹ blocks, and off-diagonal g,g⁻¹ pairs, with g∈G. Their divisor classes are spanned by the following **effective nef divisors** on J(C)^(ℓ+1):

    pr_i^*(2Θ),
    (pr_i+g pr_j)^*(2Θ)  (including i=j).

Indeed, after harmless division by2 in the rational span, for i≠j subtract the two individual polarization classes to obtain the off-diagonal pair; for i=j subtract2pr_i^*Θ to obtain g+g⁻¹. The line bundle2Θ on a principally polarized abelian variety is globally generated, so every displayed pullback is globally generated. Therefore the lift of Γ is a complex linear combination of monomials of c=ℓ/2+4 of these explicitly specified divisor classes. No bound for the complex coefficients is needed, since only a spanning set of resulting integral cycles will be used.

This is an invariant-theory argument for U, not averaging over the finite group G. Averaging over G would project to the wrong invariant space.

### Degree of the curve-to-Jacobian maps

For π:C→C′ of degree a, one has (π^*)^*Θ_J(C) numerically aΘ_J(C′), by the norm/pullback identity and the canonical polarizations. The Abel–Jacobi curve has Θ-degree g(C′). Riemann–Hurwitz gives a(g(C′)−1)≤g(C)−1=4G. Hence

    deg η^*Θ_J(C) = a g(C′) ≤ 4G+a ≤ 5G.

On T=B×A, put H₀=H_B+θ_A. The restriction of the product polarization of J(C)^(ℓ+1) is at most5G H₀ in the nef order. For any of the displayed divisors D_j, the theorem of the square gives

    D_j ≤ 8(product polarization),

also when i=j, since (1+g)^*Θ+(1−g)^*Θ=4Θ. Consequently

    D_j|_T ≤ 40G H₀.

Global generation permits choosing successive divisors that do not contain any component of the preceding effective intersection. If a restricted section has no zeros, the resulting divisor is empty. Thus the monomial action can be represented by effective proper intersections, with integer multiplicities, without invoking a non-effective moving-degree bound.

For each monomial Γ_j, intersect it with every effective term of Y_B×A and push to A. The resulting effective four-cycles, with their integer signs when recombined, have total degree mass bounded by

    (40G)^c ∫_(Y_B in mass × A) (H_B+θ_A)^c θ_A^4
    = (40G)^c binom(c,4) mass_(H_B)(Y_B) ∫_A θ_A^8
    ≤ (40G)^k binom(k,4) SB ·8!·G^8 = B0.

Only the term H_B^(ℓ/2)θ_A^4 survives in the binomial expansion. This is the reason for binom(c,4), rather than a bound depending on the huge ambient Jacobian dimension.

The correspondence calculation in SQ5 shows that the complex span of the cohomology classes of these finitely many effective four-cycles contains both Weil eigenlines after rational projection to W_K(A). Hence at least one of these effective integral cycles has nonzero Weil projection, and the projected classes of the collection span W_K(A). Every member has degree at most B0. This establishes the source-fibre version of SQ1.

## SQ7. Quantitative comparison of the integral Hermitian lattices

For an O-stable lattice Λ with alternating form E and compatible O-action, use the integral Hermitian form

    h(x,y)=E(x,ωy)−ωbar E(x,y).

Its entries lie in O, it is conjugate-linear in x and linear in y, and E(x,y) is the coefficient of ω in h(x,y). In an O-basis, the absolute determinant Δ_h of its Hermitian matrix equals the product of the polarization elementary divisors. To verify the normalization, the Hermitian identity matrix on O^8 gives a unimodular alternating form on the Z-basis (v_i,ωv_i); replacing the identity by H multiplies its determinant by Norm(detH)=(detH)². Thus det(E)=Δ_h².

Assume the Hermitian space is split. Its rational isotropic K-subspace I of dimension4 meets Λ in a primitive O-submodule. Because O is a PID, a basis v of I∩Λ extends to a basis (v,w) of Λ. In that basis

    H = [[0,B],[B*,D]],       Δ=detH=Norm(detB)>0.

Write b=detB, and let X=(B*)⁻¹D/2. The change w′=w−vX kills the lower-right Hermitian block. Then u=w′B⁻¹ satisfies h(v,u)=I₄, so (v,u) has standard hyperbolic Gram matrix.

Both this K-isometry μ:Λ_Q→K^8 with the standard hyperbolic form and its inverse have denominators dividing2Δ relative to the indicated O-bases. Indeed, entries of X have denominator2bbar, entries of B⁻¹ have denominator b, and entries of XB⁻¹ have denominator2bbar b=2Δ. The formulas

    μ(v)=e,       μ(w)=fB+eX,
    μ⁻¹(e)=v,     μ⁻¹(f)=wB⁻¹−vXB⁻¹

make both denominator assertions explicit. There is no coefficient-size assumption on B or D.

Apply this separately to the source lattice, with Δ_A dividing G^8, and the fixed target lattice, with product Δ. Their comparison therefore has denominator dividing4Δ_AΔ, and the uniform integer N=4G^8Δ clears it. Transport the rational comparison over a simply connected Hurwitz polydisc. Multiplying it by N gives a K-linear isogeny φ:A_source→A_target at every corresponding point of the period image. Since the unscaled comparison is an isometry,

    φ^*θ_target = N² θ_source.

For a dimension-four effective cycle Z,

    deg_(θ_target)(φ_*Z)=N^8 deg_(θ_source)Z.

Its projected Weil class is nonzero whenever the source projection was nonzero, since isogeny pushforward induces an isomorphism of rational Weil planes up to a nonzero scalar. The dominance proof supplies a nonempty analytic open period image; hence D=N^8B0 works there. This establishes SQ1.

The O-stability hypothesis is essential to this particularly simple bound. A target whose K-action is only rational needs a further denominator for making its lattice O-stable. The fixed integral E⁸ families in the present task already satisfy O-stability.

## SQ8. A checked explicit rational projector onto the Weil plane

For completeness, on any such integral K-eightfold let a=[3]+[ω]. Then a†a=[7], so a^*θ=7θ. On H⁸ its nine K-multiplicity eigenvalues are

    λ_j=(3+ω)^(8−j)(3+ωbar)^j,   0≤j≤8.

They are distinct. The Weil plane is the sum of the j=0 and j=8 eigenspaces. The script computes the rational polynomial P of degree8 that is1 on these two eigenvalues and0 on the other seven. Its integral numerator Q=δP has

    δ=411891354565851759965785179617340330000.

The nine coefficients of Q, in ascending order, are

    55139367181591318902655856665347132526,
    −23659781552033798345269599858690875,
    6177440678618900865149838094771,
    −74787357945320146306888400,
    −1124625943239818173006244,
    877467858933519076300,
    −463126331859245054,
    191445325672975,
    −58750145999.

Every value Q(λ_j) is checked exactly in Q[ω]/(ω²+ω+1). Pullback of a four-cycle by a^j multiplies its θ-degree by7^(4j). Therefore applying Q(a^*) to an effective four-cycle of degree D gives an integral signed cycle in W with degree mass at most M D, where

    M=Σ_j |Q_j|7^(4j)
     =497657009489489182584908205353846834744.

This supplies an entirely explicit projector. Its denominator, all nine integral coefficients, and the weighted degree multiplier agree with the parent's independently computed n=4 entry in `projectors.json`.

## SQ9. Independent two-dimensional Gram conversion and globalization

This section gives a general conversion for a fixed target polarization, independent of a special basis of the principal Weil lattice. Apply the projector in SQ8 to the effective cycles in SQ1. Their integral classes span the Weil plane and each has a signed representative of mass at most B=M D. Select two independent classes y₁,y₂.

Every Weil class is primitive: θ belongs to the mixed K-eigenspace, while a Weil determinant already fills all eight dimensions of one K-eigenspace, so θ∧y=0. For a primitive (4,4)-class on an eightfold, the Hodge star is +1. Thus the intersection form is positive definite on W.

Here is the degree-to-norm estimate with its normalization. Choose the invariant Kähler metric with Kähler class θ. Its volume is Δ=∫θ⁸/8!≥1. Averaging the current of an effective four-cycle under translations gives a constant strongly positive (4,4)-form representing its class. At each point, the Euclidean norm of a strongly positive form is at most its trace against ω⁴/4!, by decomposing it into positive rank-one forms. Consequently

    ||[Z]||_(L²) ≤ degθ(Z)/(4! sqrtΔ) ≤ degθ(Z).

The triangle inequality gives ||y_i||≤B for the signed representatives. Therefore the integral Gram matrix A=((y_i,y_j)) has entries of absolute value at most B², and its determinant d is a positive integer at most B⁴.

Let q_t be any positive integer clearing the denominator of the fixed nonzero flat section t, and put T=(q_t t,q_t t), a positive integer independent of the fibre. Then b_i=(q_t t,y_i) are integers with |b_i|≤B sqrtT. Cramer's rule yields

    d q_t t=n₁y₁+n₂y₂,
    |n₁|+|n₂|≤4B³ sqrtT.

Thus the left-hand multiplier is at most q_t B⁴ and the resulting signed-cycle degree mass is at most4B⁴sqrtT. A convenient single integral bound is

    C=B⁴(q_t+4T+4).

This bound holds on the analytic open subset supplied by SQ7. If the corrected relative-Chow argument in the parent establishes that the locus c(s)≤C is closed algebraic on the fixed irreducible moduli component, the analytic open subset forces that locus to be the entire component. It follows that the same explicit C holds on its Hecke orbit. The global argument does not change C. For t=0 take N=1 and the zero cycle.

## Source locators and checks

Severn, B. (2026). *Weil classes on abelian sixfolds and eightfolds of Weil type for Q(sqrt(−3))* (version1.5, 21October2026; Hexagon2610.00387v2), source `weil-qsqrt3-v1.5.tex`: §§3–5, `def:pt` lines175–190; `lem:schoen`/`lem:schoenR` lines228–249; `prop:supply` lines269–296; `thm:brauer` lines310–326; §6 `thm:transfer` lines343–351; reflection tuple and genus at lines496–520. https://hexagonmath.org/api/v1/works/2610.00387v2/source?path=weil-qsqrt3-v1.5.tex

Schoen, C. (1988). Hodge classes on self-products of a variety with an automorphism. *Compositio Mathematica,65*,3–32. Theorem2.0; Lemma2.3(v), Lemmas2.4–2.6, printed pp.11–17; quotient-transfer context and primitive nonvanishing pp.18–19. The inverse hard-Lefschetz step of Corollary3.1, p.25, is deliberately unnecessary in the present modified transfer. https://www.numdam.org/item/CM_1988__65_1_3_0.pdf

Milne, J.S. (1999). Lefschetz classes on abelian varieties. *Duke Mathematical Journal,96*,639–675. Preprint Lemma3.5, Proposition3.6, Remark3.7, pp.15–18, for the semisimple algebra with involution and invariant-tensor assertions. https://jmilne.org/math/articles/1999aP.pdf

Check events in this note: SQ2 exact group/branch arithmetic plus independent lattice proof; SQ3 independent integer-linear-algebra proof, also independently checked by the parent; SQ4 targeted reading of Schoen's actual projective-space construction followed by new integral orbit-transfer degree calculation; SQ5–SQ6 independent re-proof of the modified supplier transfer and all mixed-degree estimates; SQ7 independent denominator calculation read in both directions; SQ8 exact computation of all nine polynomial values; SQ9 independent positive-current/Gram calculation. These are targeted mathematical checks and ordinary exact computations, not formal proof-assistant verification. The new composite bound should be called independently audited only after the parent has completed its requested second reading.

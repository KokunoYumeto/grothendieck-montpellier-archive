# BR_PENCIL side-task results: DPS and orbit optimization

Author: GPT-6 Astra Pro, run `BR_PENCIL-20261121-R1/sdp_orbits`; inherited reasoning effort is not separately exposed by the runtime. Date: 2026-11-21. All vector spaces in the analytic statements are finite-dimensional complex Hermitian spaces. These statements are proved below; historical novelty is not claimed.

## S-01. An exact DPS certificate for a residual image outside the four families

Let A=C², B=C³ with orthonormal bases, write `|ij>=a_i⊗b_j`, and set

`u0=(|00>+|11>)/sqrt(2)`, `u1=(|01>+|12>)/sqrt(2)`, `U=span(u0,u1)`.

Then `alpha(U)=3/4`. The first PPT level of the DPS hierarchy already certifies this value with a rational primal/dual pair. Every higher PPT symmetric-extension level has the same value, so the certified error is exactly zero at every level.

### Complete proof and certificate

The two displayed vectors are orthonormal. Thus `P=|u0><u0|+|u1><u1|` is their orthogonal projector. For a normalized vector `c u0+d u1` in U, its coefficient matrix is

`M(c,d)=1/sqrt(2) [[c,d,0],[0,c,d]]`, with `|c|²+|d|²=1`.

Consequently `M M*=1/2 [[1,d conjugate(c)],[c conjugate(d),1]]`. Its largest eigenvalue is `(1+|cd|)/2 <=3/4`, with equality at `c=d=1/sqrt(2)`. The elementary identity `alpha(U)=max_{v∈U,||v||=1} epsilon(v)²` (GCT_GINEQ F-13) shows `alpha(U)=3/4`. Alternatively, the following primal and dual certificates prove both inequalities without that identity.

Let Γ denote partial transpose on B in the displayed basis. Define positive semidefinite matrices

`X=(1/16)(|2·00-11><2·00-11|+|01-2·12><01-2·12|)`,

`Y=(3/16)(|01-2·10><01-2·10|+|2·02-11><2·02-11|)`.

Here `|2·00-11>` means `2|00>-|11>`, etc. Direct expansion gives the exact identity

`(3/4)I_6-P = X+Y^Γ`.                                           (S1)

All matrix entries are rational. Positivity requires no floating-point tolerance: X and Y are displayed sums of positive multiples of outer products. For any density matrix ρ satisfying `ρ>=0` and `ρ^Γ>=0`,

`3/4-Tr(Pρ)=Tr(Xρ)+Tr(Yρ^Γ)>=0`.

This is a feasible dual certificate for the SDP

`beta_1=max Tr(Pρ) subject to Trρ=1, ρ>=0, ρ^Γ>=0`.

For the product vector

`x=(a0+a1)/sqrt(2)`, `y=(b0+2b1+b2)/sqrt(6)`,

put `z=x⊗y` and `ρ0=|z><z|`. Its coordinates are `(1,2,1,1,2,1)/sqrt(12)`. It is primal-feasible and `Tr(Pρ0)=3/4`, as follows either by direct multiplication or by the vanishing of Xz and Yz in (S1). Thus the primal and dual objectives agree exactly. In particular, product states give `alpha(U)>=3/4`, and all product states are PPT, giving the reverse inequality.

At level k, use a density operator Ω on `A⊗Sym^k(B)` whose `A⊗B` marginal is ρ, and impose positivity of partial transposes for all cuts (the standard PPT Bose-symmetric variant of DPS). Such a marginal is PPT, so the preceding dual certificate remains an upper bound. The product extension `|x><x|⊗(|y><y|)^⊗k` is feasible at every k and achieves 3/4. Therefore `beta_k=alpha(U)=3/4` and `0<=beta_k-alpha(U)<=0` for all k>=1. This is an exact finite-level certificate, not a numerical convergence assertion.

### A tensor having U as residual image

Let C=C², with basis c0,c1, and

`T=c0⊗(a0b0+a1b1)+c1⊗(a0b1+a1b2)`.

The `C* -> A⊗B` image is exactly U (normalizing basis vectors does not change the image). Its concise format is 2×2×3. None of the four source families has this concise format, so this is outside those families. It is the elementary binary-linear multiplication tensor. The identity

`T=c0 a0 (b0-b1)+c1 a1 (b2-b1)+(c0+c1)(a0+a1)b1`             (S2)

is a three-term rank decomposition over Z. The B-mode flattening has the independent columns/matrices `c0a0`, `c0a1+c1a0`, `c1a1`, so it has rank three. Hence `R(T)=BR(T)=3` over every field. Over C the residual alpha certificate and GCT_GINEQ F-13 give `BR(T)>=2+ceil(4/3)-1=3`, meeting (S2). This illustrates the pipeline with a fully inspectable dual certificate; it is not a general efficient algorithm for Q-30.

### Exact executed verification

`check_certificates.py` uses SymPy rational arithmetic to verify: P²=P and Tr(P)=2; (S1); positive eigenvalues of X and Y (5/16 and 15/16, respectively, each twice, with four zero eigenvalues); trace-one/product/PPT primal state; primal objective 3/4; complementary slackness; (S2); B-flattening rank3. Output is `certificate.json`. No solver output, approximate rank threshold, or formal theorem prover is used.

## S-02. A proved general error bound for the same hierarchy

For any subspace V⊂A⊗B, with d=dim B, let beta_k(V) denote the above PPT Bose-symmetric-extension upper bound. Then

`0 <= beta_k(V)-alpha(V) <= (d-1)/(k+d-1)`.

For the example S-01, the sharper exact error is zero. For its dimension d=3, the generic bound is `2/(k+2)`.

### Precise known input

Navascués–Owari–Plenio, *The power of symmetric extensions for entanglement detection*, arXiv:0906.2731v1, Theorem 2, equation (7), printed page 3, states: if ρ_AB admits a k-Bose-symmetric extension, then

`σ=(kρ+ρ_A⊗I_B)/(k+d)`

is separable. Their Corollary 5, equation (16), gives the associated trace-distance bound. We use Theorem 2 as known input, not as a finding of this run. The primary PDF was opened and the stated theorem and its hypotheses were checked against Definition 1 (printed page 2). The PPT hierarchy is a subset of this Bose-symmetric hierarchy, so the theorem applies to every feasible marginal.

### Proof of the alpha form and its bound

For a feasible trace-one ρ, let σ be as above. Both have marginal ρ_A. Because σ is separable, the operator `R=ρ_A⊗I_B-σ` is positive semidefinite: express σ as a convex combination of product density operators and use `I_B-τ_B>=0` in each summand. Its trace is d-1. Rearranging the formula for σ gives

`ρ-σ = ((d-1)ρ-R)/(k+d-1)`.

Since `0<=P_V<=I`,

`Tr(P_Vρ)-Tr(P_Vσ) <= (d-1)/(k+d-1)`.

The second objective is at most alpha(V), because σ is separable. Take the maximum over feasible ρ. The reverse inequality follows from feasible product-state extensions. If d=1 the same argument yields zero and all states are separable. Compactness ensures maxima exist: Ω ranges over a closed subset of trace-one positive matrices in finite dimension. This proves the claimed error bound, without claiming polynomial complexity in d or in the requested accuracy.

## O-01. The proposed maximum of alpha over the full GL orbit

Let 0≠U⊂H1⊗...⊗Hb and G=Π_i GL(Hi). Then

`sup_{g∈G} alpha(gU)=1`.

This supremum is a maximum if and only if U contains a nonzero product tensor. In that case `alpha(gU)=1` for every g. If U contains no product tensor, every finite g satisfies `alpha(gU)<1`, and the supremum is not attained. The same assertions hold with G=Π_i SL(Hi).

### Complete proof

Choose 0≠u∈U and a nonzero coordinate coefficient `c` in any product orthonormal basis. Relabel that coordinate as `(0,...,0)`. Let `g_i(t)` fix the distinguished basis vector and multiply every other basis vector by t, with 0<t<1. Then `g(t)u` tends to `c z`, where `z=e0⊗...⊗e0` is a unit product vector. Thus `v_t=g(t)u/||g(t)u||∈g(t)U` tends to a scalar of modulus one times z. Since

`alpha(g(t)U) >= |<v_t,z>|²`,

the supremum is at least one and hence exactly one. If `alpha(W)=1`, compactness of the product of unit spheres gives a unit product vector z with `||P_W z||=1`; the Pythagorean identity forces z∈W. Conversely such a vector plainly gives alpha(W)=1. Finally invertible product maps preserve the property of containing a product tensor. These facts prove the attainment assertion.

Over C, every product-GL map differs from a product-SL map by an overall nonzero scalar (choose determinant roots). Scalars do not change subspaces. The two orbit sets in the Grassmannian are therefore identical, which proves the SL statement. Equivalently one can use determinant-one diagonal one-parameter subgroups and reparametrize t.

### Diagonal polynomial action

If 0≠U⊂Sym^b(H) is regarded as a subspace of H^⊗b in characteristic zero, then also

`sup_{g∈GL(H)} alpha(g^⊗b U)=1`.

Indeed, for any nonzero u∈U the homogeneous polynomial `ℓ -> ℓ^⊗b(u)` is nonzero; choose ℓ with nonzero value and a unit basis vector representing ℓ. The common diagonal degeneration fixing that vector and shrinking its orthogonal complement selects the nonzero coefficient of its b-th power. The preceding argument applies. Attainment again holds exactly when U contains a product vector, which for a symmetric subspace is a pure power. The same orbit statement holds for SL(H). This covers the residual images of the polynomial determinant and permanent, and the row permanent, under their common-factor action.

Do not apply this diagonal-action assertion to arbitrary nonsymmetric subspaces. In particular the row determinant residual `U=Λ^b(H)` is fixed by diagonal GL(H), and its alpha remains `1/b!` for b>=2 (GCT_GINEQ F-14). Thus the acting group must always be named.

### Consequence for the intake's proposal

The intake's statement that the **maximum** of alpha over a GL orbit supplies a Kempf–Ness bridge is false as stated. On product-free residual subspaces the maximum does not exist; replacing it by the supremum gives the constant one. In F-13 this would yield only the original image-dimension bound q. Maximizing alpha is also the wrong direction for improving the norm certificate, whose residual lower bound increases when alpha decreases. These conclusions do not assert that every orbit optimization is useless; they refute this specific proposed quantity.

## O-02. The actual Plücker norm-minimization condition

Let q=dim U, choose an orthonormal basis u1,...,uq, and let `w=u1∧...∧uq∈Λ^q(W)`, where W=⊗_i Hi. This is a unit Plücker vector. The group G=Π_i SL(Hi) acts on Λ^q(W). For Hermitian traceless endomorphisms H_i on Hi, write `H_W=Σ_i I⊗...⊗H_i⊗...⊗I`. Then

`d/dt|_{t=0} log ||exp(t H_W)w||² = 2 Σ_i Tr(H_i Tr_{others}P_U)`.

It follows that w is critical for the orbit norm exactly when

`Tr_{others}(P_U)=(q/dim Hi) I_Hi` for every i.                (O1)

Moreover (O1) is equivalent to w minimizing its norm over this G orbit.

### Complete proof of the stated form

Differentiate the exterior power action: H_W acts on w by the sum of q terms replacing uj by H_W uj. Pairing with w, orthonormality kills all terms except the diagonal inner products, giving `sum_j <uj,H_W uj>=Tr(P_U H_W)`. Differentiating the squared norm supplies the factor two, and the defining property of partial trace gives the displayed derivative. A Hermitian matrix pairs to zero with all traceless Hermitian matrices exactly when it is scalar; taking traces forces the scalar q/dim Hi. This proves the critical equation.

For sufficiency, each g∈G has a polar decomposition `g=k exp(H)` with k unitary and H belonging to the indicated traceless Hermitian Lie algebra. In a unitary eigenbasis for the induced Hermitian generator on Λ^q(W),

`f(t)=log ||exp(tH)w||² = log Σ_j |w_j|² exp(2t λ_j)`

is convex (its second derivative is four times the variance of the λ_j under positive normalized weights). Equation (O1) gives f'(0)=0, so f(1)>=f(0). The unitary factor k does not change the norm, proving global minimality. Necessity follows by differentiating at a minimum. This is the minimal-vector part of the Kempf–Ness framework in explicit residual-subspace coordinates. It makes no unsupported claim that alpha itself equals the capacity or that a minimum always lies in the original orbit.

For a primary reference to the corresponding tensor-scaling theorem, use Bürgisser–Garg–Oliveira–Walter–Wigderson, *Alternating minimization, scaling algorithms, and the null-cone problem from invariant theory*, arXiv:1711.08039v1, equation (1.3) for capacity and Theorem 3.2 (printed page 13) for the Kempf–Ness moment-map criterion in the **orbit closure**. The closure is essential. Section 3 explains the general reductive-group norm interpretation.

### Explicit separation of the two objectives

Let U be the line through the unit maximally entangled vector `Omega_d=(sum_i e_i⊗e_i)/sqrt(d)`, d>=2. Its projector has both marginals I/d, so (O1) proves that its Plücker vector minimizes its SL_d×SL_d orbit norm. Its alpha is 1/d by its equal Schmidt coefficients. Nevertheless O-01 gives supremum one, unattained, on exactly the same orbit. Thus the moment-map minimum and the alpha supremum cannot be identified.

For the S-01 subspace, a diagonal change in B carries it to

`U_bal=span{(sqrt2|00>+|11>)/sqrt3,(|01>+sqrt2|12>)/sqrt3}`.

Its projector marginals are I_2 and `(2/3)I_3`, so it satisfies (O1). Every unit vector `c v0+d v1` in this balanced subspace has Schmidt eigenvalues 2/3 and 1/3: the 2×2 row Gram matrix has trace one, diagonal difference `(|c|²-|d|²)/3`, and off-diagonal `d conjugate(c)/3`; its eigenvalue difference is 1/3. Thus `alpha(U_bal)=2/3`, whereas S-01 gives alpha(U)=3/4 and O-01 gives orbit supremum one. No assertion that 2/3 is the orbit-infimum of alpha is needed or made.

## Algebraic-geometric and Grothendieck dictionary

These are exact translations and boundaries, not claims that complex Hermitian positivity exists in every characteristic.

* **S-01:** the tensor T and its rank-three decomposition are morphisms of free Z-modules. Its residual image defines a rank-two direct summand of the free rank-six module (the two disjoint-support generators have primitive coefficients) and hence a Z-point of Gr(2,6). The rank-three flattening lower bound is the nonvanishing of an integral 3×3 minor. The projector and rational witness matrices live on the complex fiber with a chosen Hermitian metric; their identities are rational identities over Z[1/2], and their positivity is a real/Hermitian statement certified by Gram factorizations. They are not invariant classes in algebraic K_0.
* **S-02:** Sym^k(B) is the Schur functor for the one-row partition (k), applied to a locally free sheaf. Its rank is binomial(k+d-1,d-1). In K_0, its generating operation is `sigma_t([B])=lambda_{-t}([B])^{-1}`. The extension constraints are linear constraints and Hermitian PSD inequalities on endomorphisms of A⊗Sym^k(B) in an archimedean fiber. Underlying bundle classes alone neither certify positivity nor compute alpha, consistently with predecessor F-20 and F-21. No use of gamma-filtration, l-adic weights, purity, or motives is needed to prove this analytic estimate, and no rank conclusion follows from them alone.
* **O-01:** the group scheme Π GL(Hi) acts on the relative Grassmannian and on the Segre scheme. The condition `P(U) meets Segre` is precisely predecessor F-18's closed incidence locus I_{q,1}, the proper image of the universal line-in-subspace incidence. The displayed one-parameter subgroup gives a Grassmannian limit U0 in that incidence: the accompanying line [g(t)u] tends to a Segre point, and incidence is closed. The assertion sup alpha=1 is the archimedean metric reading of this algebraic degeneration. Its nonattainment says that the actual orbit is disjoint from I_{q,1} while its closure meets it.
* **O-02:** the Plücker vector is a generator of det(U)=Λ^q U, a line in Λ^q W. This is an exterior-power operation on the tautological subbundle; its K_0 class and group action are integral constructions. The Hermitian metric, partial traces and moment map are additional analytic data on the complex fiber. Formula (O1) is not a statement of equality of K_0 classes and is not an l-adic purity test.

Relevant exact locators inherited from the predecessor (to be independently verified by the root's source audit before upgraded status): SGA 3, Exposé I §§4.5–4.6 for group/module schemes; EGA II Definition 5.4.1 and Proposition 5.4.2 for properness/universal closedness and base change, Theorem 5.5.3(i) for projective morphisms being proper; GCT_GINEQ F-18, F-19, F-20, F-21. None of S-01–O-02 is asserted to appear at a specific manuscript cote or scan. No archive locator should be invented: the new conclusions belong to this run, and the modern scheme/bundle framework is given above.

## Primary source audit and URLs

1. Doherty–Parrilo–Spedalieri, *A complete family of separability criteria*, arXiv:quant-ph/0308032v3, Theorem 1 (Completeness), printed p.7; §II defines hierarchy; first PPT level described in abstract and introduction. PDF: https://arxiv.org/pdf/quant-ph/0308032 . The PDF's body carries a regenerated date in one line, so cite its arXiv version and printed statement rather than that incidental typesetting date.
2. Navascués–Owari–Plenio, *The power of symmetric extensions for entanglement detection*, arXiv:0906.2731v1, Definition 1 (Bose symmetric extensions), p.2; Theorem 2, eq.(7), p.3; Corollary 5, eq.(16), p.4. PDF: https://arxiv.org/pdf/0906.2731 . Only Theorem 2 is used as mathematical input in S-02.
3. Bürgisser–Garg–Oliveira–Walter–Wigderson, *Alternating minimization, scaling algorithms, and the null-cone problem from invariant theory*, arXiv:1711.08039v1, eq.(1.3), printed p.4, Theorem 3.2, printed p.13. PDF: https://www.math.ias.edu/~avi/PUBLICATIONS/BurgisserGaOlWaWi_Nov2017.pdf . The theorem concerns an element of the orbit closure, not necessarily the orbit; the eigenvalue/marginal condition in our O-02 is proved directly, so the source theorem is background rather than an unverified dependency.

Web refs for parent to reopen before citing: `turn923621637view0` (NOP), `turn877801141view0` (NOP Theorem 2), `turn923621637view1` (DPS), `turn877801141view2` (DPS Theorem 1), `turn923621637view2` (BGO), `turn877801141view4` (BGO Theorem 3.2). Root must open/search these itself if citing in final chat.

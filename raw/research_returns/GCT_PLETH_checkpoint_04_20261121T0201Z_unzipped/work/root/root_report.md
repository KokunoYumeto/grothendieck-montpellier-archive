# Additional exact constructions and limits

Run `GCT_PLETH_20261121_run01`; model GPT-6 Astra Pro; effort setting not exposed. Findings below are proved formulations for this investigation; no priority claim is made. All vector spaces in the representation calculations have characteristic zero unless an integral model is explicitly specified.

## G-001. A balanced weight space with no monomial basis

Let `E=C^5`, `lambda=(5,2,1,1,1)`, and let permutation matrices act on
\[
M=(S_{(5,2,1,1,1)}E)_{(2,2,2,2,2)}.
\]
Then `M` is isomorphic as an `S_5` representation to `sgn tensor U_5`, where `U_5={(z_1,...,z_5):sum z_i=0}`. There is no basis of `M` that `S_5` permutes up to nonzero scalar factors. In particular there is no such basis indexed by its four balanced Gelfand--Tsetlin patterns.

**Proof.** The multiplication map
\[
\operatorname{Sym}^{4}E\otimes E\longrightarrow\operatorname{Sym}^{5}E
\]
is surjective, and its kernel is `S_(4,1)E`, by the degree-one Pieri rule. On weight `(1^5)` the source has basis
\[
v_i=\left(\prod_{j\ne i}e_j\right)\otimes e_i\quad(1\le i\le5).
\]
Permutation matrices permute these five vectors, and multiplication sends all of them to `e_1e_2e_3e_4e_5`. The kernel on this weight is exactly `U_5`. Tensoring with `det E` shifts the highest weight from `(4,1,0,0,0)` to `(5,2,1,1,1)` and the balanced weight from `(1^5)` to `(2^5)`; its restriction to permutation matrices is the sign character. This gives the stated isomorphism, including the character twist.

A monomial basis of size four would give a homomorphism `A_5→S_4`. The group `A_5` is simple: its conjugacy-class sizes are `1,15,20,12,12`, and no sum containing 1 of a proper nonempty subcollection of the four nonidentity classes is a proper divisor of 60. To verify these class sizes, the double transpositions number 15 and have centralizer of order 4 in `A_5`; the 3-cycles number 20 and have centralizer of order 3; the 24 five-cycles split into two classes of size 12 since their centralizer has order 5. Lagrange's theorem proves simplicity from the listed sizes. The homomorphism to `S_4` therefore has trivial image, since 60 exceeds 24. Thus every element of `A_5` would act diagonally in the proposed basis. The resulting image is abelian. A nonabelian simple group has trivial abelian image, so `A_5` would act trivially on `M`. But `(123)` acts nontrivially on `e_1-e_2` in `U_5`. On `A_5` the sign twist is trivial. This is a contradiction.

The argument identifies a specific failure of an orbit-counting approach to the balanced-weight normalizer action. It makes no assertion excluding other lattice-point descriptions. The exact group-scheme map is `S_5→GL(E)` by permutation matrices, followed by `S_lambda`; the determinant character records its passage through `SL(E)`.

## G-002. Exact nonnegative determinant certificates for plethysm and the canonical map

Let `N=mn`, let `[lambda]_Z` be the integral Specht lattice in its standard polytabloid basis, and let `rho` be its permutation action. Let `H=S_n wr S_m` be the row wreath subgroup of `S_N`, and `K=S_m wr S_n` the column wreath subgroup, with cells indexed by the same `m by n` grid. Set
\[
A_H=\sum_{h\in H}\rho(h),\qquad A_K=\sum_{k\in K}\rho(k),\qquad B=A_KA_H.
\tag{G2.1}
\]
These are finite integer matrices. Their ranks over `Q` are respectively
\[
\operatorname{rank} A_H=a_{m,n}^{\lambda},\qquad
\operatorname{rank} B=r_{m,n}^{\lambda},
\tag{G2.2}
\]
where `r` is the multiplicity of `S_lambda` in the image of the normalized Hadamard--Howe map. For either `C=A_H` or `C=B`,
\[
\det(I+tCC^{\mathsf T})=
\sum_{j\ge0}t^j
\sum_{\substack{|I|=|J|=j}}\det(C_{I,J})^2.
\tag{G2.3}
\]
Its degree is the corresponding rank. This gives exact finite sums of squares as certificates for every multiplicity and every map rank.

**Proof.** Averaging `P_H=A_H/|H|` is an idempotent with image `[lambda]^H`, because left multiplication permutes the terms of the average, and the average fixes every invariant vector. Schur--Weyl duality followed by row symmetrization identifies this invariant space with the multiplicity space of `S_lambda` in `Sym^m(Sym^n V)`. The normalized grid map on that multiplicity space is `P_K|_[lambda]^H`; hence `P_KP_H` has the same image, and multiplication by the positive nonzero integers `|K||H|` does not change its rank. This proves (G2.2) with the specified map, rather than an arbitrary equivariant map having the same source and target.

The coefficient of `t^j` in `det(I+tD)` is the sum of all principal `j by j` minors of `D`, by multilinearity of determinant. Apply this to `D=CC^T` and then apply Cauchy--Binet to each principal minor. The result is (G2.3). A real matrix of rank `s` has a nonzero `s by s` minor and every larger minor vanishes. The coefficient at `t^s` is consequently positive and all coefficients above it are zero. This proves the degree assertion without relying on a choice of invariant inner product for the Specht basis.

The finite sum in (G2.3) includes determinants that must themselves be evaluated. The formula therefore records the exact remaining nonzero-minor test; no efficient lattice-point rule or complexity-class containment is inferred from it. In scheme language the rank conditions are the determinantal closed subschemes of the affine space of matrices, cut out by these minors. The displayed integral matrices give actual integral points of those schemes.

## G-003. The integral Chow pullback, divided powers, and the image algebra

Let `E=Z^r`, and let
\[
\mu:E^{\times n}\longrightarrow\operatorname{Sym}^n E,
\qquad(v_1,\ldots,v_n)\longmapsto v_1\cdots v_n
\tag{G3.1}
\]
be the multiplication morphism of affine schemes over `Z`. Its degree-`d` coordinate pullback is
\[
\mu_d^*:
\operatorname{Sym}^d\bigl((\operatorname{Sym}^nE)^\vee\bigr)
\longrightarrow
\left((\operatorname{Sym}^d E^\vee)^{\otimes n}\right)^{S_n}
=\Gamma^n(\operatorname{Sym}^dE^\vee).
\tag{G3.2}
\]
Here `(Sym^n E)^vee=Gamma^n(E^vee)` and the right equality is the divided-power identification for a finite free module. With the rational norm isomorphisms `Sym^s(F)→(F^tensor s)^{S_s}`, normalized by `1/s!`, equation (G3.2) becomes the canonical grid map
\[
h_{d,n}:\operatorname{Sym}^d(\operatorname{Sym}^n E_{\mathbb Q}^\vee)
\longrightarrow\operatorname{Sym}^n(\operatorname{Sym}^d E_{\mathbb Q}^\vee).
\tag{G3.3}
\]

**Proof.** A homogeneous degree-`d` function on `Sym^n E` pulls back to a polynomial of multidegree `(d,...,d)` in the `n` input vectors. The multidegree component of the polynomial ring is `(Sym^d E^vee)^tensor n`. The map (G3.1) is unchanged by permuting input vectors, so its pullback belongs to its `S_n` invariants. For a free module, the orbit sums of tensor basis words give both a basis of symmetric tensors and the defining basis of divided powers; this proves the integral equality in (G3.2). The dual of coinvariant symmetric powers is the invariant tensor module, yielding the other divided-power identification.

Over `Q`, the inverse of the quotient from invariant tensors to coinvariant symmetric tensors is normalized averaging. Apply that explicit map in both the `d`-row and `n`-column tensor arrangements. Coordinate pullback multiplies entries along the transposed arrangement; the resulting invariant tensor is precisely column averaging of the row-invariant tensor. This is the grid definition of (G3.3), with no unrecorded integral identification of symmetric and divided powers.

Set `A_Z=im(mu^*)` inside the polynomial ring `Z[E^times n]`, with the grading just specified. Its kernel is an ideal in the polynomial coordinate ring of `Sym^n E`, and
\[
\mathcal C_{n,r}=\operatorname{Spec}A_{\mathbb Z}
\]
is the scheme-theoretic image of (G3.1). This is EGA I, Proposition 9.5.1 and Corollary 9.5.2, printed p.176, with Definition 9.5.3 on p.177. The image is a subring of a torsion-free abelian group, hence is torsion-free, hence is flat over `Z`: for a principal ideal domain, a module is flat precisely when it is torsion-free. One proof of the latter statement writes a torsion-free module as the filtered union of its finitely generated free submodules and uses preservation of flatness under filtered colimits. Each graded part is finite free as a subgroup of a finite free multidegree component. This proves flatness of this specific integral model. It does not identify every special fiber with the scheme-theoretic image of the corresponding fiber map; the precise specialization map is `A_Z tensor k→im(mu_k^*)`, and injectivity of that map remains a separate saturation question.

Over `Q`, the degree-`d` Schur multiplicities of `A_Q` are the ranks `r_(d,n)^lambda` of G-002, with the usual dual convention for coordinate functions. The rank equation thus has an explicit morphism to the orbit-closure coordinate ring. The generic span of `n` independent linear factors identifies the dense product orbit with that of `x_1...x_n` when `r>=n`, so this is the affine Chow cone in that range. The construction of (G3.1) is valid for every `r`.

The projective Hilbert and Quot functors with fixed Hilbert polynomial are represented by the schemes of FGA, Bourbaki exposé 221, Theorems 3.1 and 3.2, pp.259--260; the Hilbert specialization is after Proposition 3.8, p.265. They parametrize flat families of projective closed subschemes and coherent quotient sheaves with that Hilbert polynomial. The finite matrices in (G3.2) remain the explicitly identified maps whose minors determine the graded ranks; the representing property alone supplies no new nonzero minor.

## G-004. Purity and the invariant projector on a finite étale example

Let `X=Spec F_(q^2)` over `F_q`, let `ell` be prime to `q`, and let `sigma` generate its two-element Galois group. The degree-zero étale cohomology of `X` after base change to an algebraic closure is `Q_ell e_0 directsum Q_ell e_1`; Frobenius interchanges the two basis vectors. The two idempotents
\[
e_+=\tfrac12(1+\sigma),\qquad e_-=\tfrac12(1-\sigma)
\tag{G4.1}
\]
have one-dimensional images with Frobenius eigenvalues `1` and `-1` respectively. Both are pure of weight zero, since both eigenvalues have complex absolute value one, but their Galois-invariant dimensions are respectively one and zero.

**Proof.** The étale cohomology of a two-point geometric scheme in degree zero is its functions, and higher cohomology vanishes. The Frobenius action permutes the two embeddings of the degree-two finite field extension, so its eigenvectors are `e_0+e_1` and `e_0-e_1`. Formula (G4.1), the two eigenvalues, and the invariant dimensions follow by direct matrix multiplication. This works also for `ell=2`, since the coefficient field is `Q_2` and `1/2` exists. In the category of rational Artin motives the same idempotents are the two projectors on this finite étale motive.

This supplies an exact test of the proposed passage from a pure cohomological object to a symmetric-group-invariant multiplicity: the group projector must be carried along the realization. Purity alone assigns the same weight to the two displayed lines while the invariant projector has ranks one and zero. The example does not rule out a geometric construction that includes that projector. The motivic interpretation applies to this explicit finite étale object, without assuming a general category of motives has been specified for archive cote12/scan041.

## G-005. A positive polytope formulation for every two-row output

This section carries the known marked-tree theorem of Pak--Panova--Swanson, *A combinatorial interpretation for certain plethysm and Kronecker coefficients* (4 November 2025), Theorems 1.1/4.5 and 1.2/5.2, into explicit polytope language. The known combinatorial interpretation is not claimed as a new theorem of this run.

For a nonempty outer partition `mu`, inner row `(k)` with `k>=1`, and output `(N-r,r)` where `N=k|mu|` and `0<=r<=N/2`, take the finite set of unmarked GOH trees `G(mu,k)` defined in that work, Definitions 3.5 and 3.8. The empty outer partition has the sole coefficient one at the empty output. The definition, including all integer partition labels, is reproduced below so that the formula is executable from the paper. For a tree `T` order its leaves in the prescribed lexicographic depth-first order, and write their nonnegative labels as `a_1,...,a_t`. Put
\[
s(T)=\frac{N-\sum_i a_i}{2}.
\]
Define the bounded rational polytope `P_T(r)` in coordinates `z_1,...,z_t` by
\[
z_1=0,\qquad z_t=r-s(T),\qquad z_i\le z_{i+1},
\tag{G5.1}
\]
\[
z_{i+1}-z_i\le a_{i+1},\qquad
z_{i+1}+z_i\le a_1+\cdots+a_i
\quad(1\le i<t).
\tag{G5.2}
\]
Then
\[
p_{\mu,(k)}^{(N-r,r)}
=\sum_{T\in G(\mu,k)}\#(P_T(r)\cap\mathbb Z^t).
\tag{G5.3}
\]
For the symmetric outer index `(m)`, one may instead use the KOH trees `T(n,m)` for `N=mn`, and the same formula also equals
\[
g((mn-r,r),(n^m),(n^m)).
\tag{G5.4}
\]

**Proof of the asserted form.** The marks of Pak--Panova--Swanson, Definitions 4.4 and 5.1, satisfy `0=z_1<=...<=z_t=r-s(T)` and
`z_(i+1)-z_i<=min(sum_(j<=i)a_j-2z_i,a_(i+1))`.
Separating this minimum into its two linear inequalities gives exactly (G5.2). Thus the identity map on mark vectors is a bijection between their marked trees with fixed underlying tree and the integer points of `P_T(r)`. The endpoint and monotonicity bound every coordinate between zero and `r-s(T)`; a negative endpoint gives the empty polytope. Summing the cited theorem over underlying trees proves (G5.3) and (G5.4). The proof of the change of language is complete and uses no subtraction of lattice-point counts.

For a general inner partition `nu`, evaluation in rank two gives the following exact transfer. Partitions with three or more rows have `S_nu(C^2)=0`. For `nu=(b+k,b)`, the isomorphism
\[
S_{(b+k,b)}(\mathbb C^2)=\det^b\otimes\operatorname{Sym}^k\mathbb C^2
\]
and homogeneity of `S_mu` give the determinant shift by `b|mu|` in each output row. This is precisely Pak--Panova--Swanson, Lemma 2.1. The shifted output with negative second row has coefficient zero. For `k=0`, the inner representation is a line, and its outer Schur functor is zero for `ell(mu)>1` and is `det^(b|mu|)` for `mu=(|mu|)`. This covers the rank-one edge case without invoking a zero-parameter tree convention.

The corresponding vector-bundle statement is obtained from the rank-two frame torsor and the above determinant-line isomorphism. Every polytope computes the coefficient of the associated Schur functor in `K_0(BGL_2)` over a characteristic-zero field. The `SL_2` Clebsch--Gordan branching chain behind the marks is an exact chain of interlacing inequalities; it supplies a successful instance of the branching approach outside the stable-tail range.

### Explicit tree indexing

For a partition `alpha`, write `m_j(alpha)` for the multiplicity of its part `j`, `alpha'` for its conjugate, and `Q_j(alpha)=sum_(x<=j)alpha'_x`. A KOH vertex is labeled `(alpha,a,b)` with `a>=0`, `b>=1`, `alpha partition of b`. A vertex with `b=1` is a leaf with scalar label `a`. A vertex with `b>=2` has one child for each distinct part `j` of `alpha`, in increasing order, with parameters
\[
a^{(j)}=(a+2)j-2Q_j(\alpha),\qquad
b^{(j)}=m_j(\alpha),
\]
and its partition label ranges over the partitions of `b^(j)`. A negative `a^(j)` gives no tree. The root parameters of `T(n,m)` are `(a,b)=(n,m)`.

A GOH root of type `(mu,k)`, for `ell=ell(mu)` and `n=|mu|`, carries a sequence of partitions `nu^(0),...,nu^(ell)` with
\[
\nu^{(0)}=(1^n),\qquad
|\nu^{(i)}|=\sum_{j\ge i+1}\mu_j,
\]
\[
P_j^i=Q_j(\nu^{(i+1)})-2Q_j(\nu^{(i)})+Q_j(\nu^{(i-1)})\ge0
\quad(1\le i<\ell,\ 1\le j\le n).
\]
Let `m=(nu^(1))'_1`, with `m=0` for an empty partition, and retain configurations with `m<=k`. For every pair `(i,j)` with `m_j(nu^(i))>0`, attach a KOH tree of type `(P_j^i,m_j(nu^(i)))`, ordered lexicographically. For `m<k`, attach also a final KOH tree of type `(n,k-m)`. This defines the complete finite index set in (G5.3). Finiteness and the equal-center property `s(T)` are the cited Proposition 3.4 and Proposition 3.9; their proofs are repeated application of the KOH and GOH identities, Theorems 3.1 and 3.6.

The printed induction proof of Lemma 4.2 has a local indexing slip: its last inequality writes `|a|-2k_t`, whereas substitution into Lemma 4.1 gives `|a|-2k_(t-1)`. The statement of Lemma 4.2 and both marking definitions have the correct latter index. The polytope above uses those correct statements.


A second local correction concerns Lemma 4.1, printed p.8. Put \(L=\min(r-2i,s-2j)\). Direct multiplication of finite geometric sums gives
\[
(1-q)(q^i+\cdots+q^{r-i})(q^j+\cdots+q^{s-j})
=q^{i+j}(1+\cdots+q^L)-q^{r+s-i-j+1}(1+\cdots+q^{-L}).
\]
The printed negative leading exponent omits the final one. For \(r=s=1,i=j=0\), the left side is \(1+q-q^2-q^3\), while the printed expression is \(1-q^2\). The smallest exponent in the corrected negative term is \(i+j+\max(r-2i,s-2j)+1>(r+s)/2\). Thus its actual coefficient assertion below the midpoint follows, and the corrected Lemma 4.2 induction and the tree formulas retain their stated conclusions. The independent reviewer inspected the PDF page visually and checked this entire repair.

# Positive lattice-point formulas from explicit invariant presentations

## G-008. A repeated-odd-part nonvanishing family in unbounded width

Put `S=<4,6,7>={0,4,6,7,8} union {k:k>=10}`. For every `k in S` with `k>=4` and every `j>=0`,
\[
\boxed{c((k^{4j}))\ge1.}
\tag{G8.1}
\]
The empty partition has coefficient one. More generally, let `lambda` be a partition with no part one. Its even parts have arbitrary multiplicities. For each odd part `i in S`, its multiplicity has the form `4q_i+epsilon_i`, with `q_i>=0` and `epsilon_i in {0,1}`; for the remaining odd parts `3,5,9`, its multiplicity is at most one. Then
\[
\boxed{c(\lambda)\ge1.}
\tag{G8.2}
\]
The finite plethysm coefficients in T-010's stability range have the same positive value. The theorem concerns a specified sufficient family; it does not assert an exhaustive support classification.

**Proof, including the exact finite seeds.** Let `W=C^4`. The invariant algebra `Sym(Sym^4 W)^(SL_4)` is a subalgebra of a polynomial algebra and therefore a domain. The exact seed multiplicities in degrees `4,6,7` are each one. The finite certificates are supplied in `QUATERNARY_QUARTIC_INVARIANTS.tsv` and independently in `QUARTIC_SEEDS_INDEPENDENT_CHECK.tsv`, with the three complete class-sum files. Here is the precise mathematical verification of those finite numbers. The torus character is the coefficient of `t^k` in
\[
\prod_{\substack{\alpha\in\mathbb Z_{\ge0}^4\\|\alpha|=4}}
(1-tx^\alpha)^{-1}.
\tag{G8.3}
\]
There are 35 factors. With `rho=(3,2,1,0)` and `M_k(w)` its integer weight coefficients, Weyl's alternant identity gives the invariant multiplicity
\[
\sum_{\sigma\in S_4}\operatorname{sgn}(\sigma)
M_k((k,k,k,k)+\rho-\sigma\rho).
\tag{G8.4}
\]
The supplied program expands the 35 geometric series by integer dynamic programming, computes all 24 terms of (G8.4), and obtains one in each of the three asserted degrees. Only coordinates at most `k+3` can contribute; all factor weights are nonnegative, so truncation beyond that box preserves all required coefficients. The independent program instead expands the wreath-product cycle index and sums symmetric-group characters by Murnaghan--Nakayama; it obtains the same three values. This is an exact finite computation certificate, not a proof-assistant claim.

Choose nonzero invariant seed vectors. Their products are nonzero, so every degree in `S` contains an invariant. The displayed description of `S` follows because `10=4+6`, `11=4+7`, `12=6+6`, `13=6+7`, and adding four covers every subsequent integer; direct checking settles `0,...,9`.

Under the symmetric-function involution `omega`, the even inner degree four gives
\[
\omega(h_k[h_4])=h_k[e_4].
\tag{G8.5}
\]
Thus the coefficient of `(k^4)` in `Sym^k(Sym^4 W)` equals the coefficient of `(4^k)` in `Sym^k(Lambda^4 C^k)`. This is the determinant representation `det^4`, so a nonzero highest vector of weight `4 omega_k` exists in that symmetric algebra. Its `j`th power is nonzero and has highest weight `4j omega_k`. This is the constituent for tail `(k^(4j))` in the exact module M_k of T-010, proving (G8.1).

For (G8.2), work in rank `r=lambda_1`. Embed every seed highest vector from rank `i` using the first `i` coordinates into `Sym^i(Lambda^4 C^r)`. It remains highest for `GL_r`: positive root operators involving a basis coordinate beyond `i` annihilate it, and the operators within the first `i` coordinates already do so. Multiply the prescribed powers of all these vectors inside the single polynomial algebra `Sym(Lambda^4 C^r)`. This product is nonzero. The additional pure highest vectors for the arbitrary even parts live in their corresponding symmetric-algebra factors; the part four contributes another power in the same domain. The residual odd parts with multiplicities `epsilon_i=0,1` select scalars or highest wedge vectors in the corresponding exterior-algebra factors. Their tensor product is nonzero, highest, and has total highest weight `lambda'`. T-010 proves (G8.2). This proof records the factor in which multiplication occurs, so that no unsupported domain assertion about the full tensor product of exterior algebras is used.

## G-009. A terminating positive-polytope procedure for all symmetric plethysm

For every positive integer `m`, the following finite procedure computes an integer matrix `D_m` with columns `d_j=(n_j,lambda^(j))`, all `n_j>=1`, and a finite collection `C_m` of pairs `(u,S)` with `u in Z_{≥0}^q`, `S subset {1,...,q}`. The output depends only on `m`. For all `n>=0` and partitions `lambda` of `mn`, of length at most `m`, it gives
\[
\boxed{
a_{m,n}^{\lambda}=
\sum_{(u,S)\in C_m}
\#\left\{z\in\mathbb Z_{\ge0}^{S}:
D_{m,S}z=(n,\lambda)-D_m u\right\}.
}
\tag{G9.1}
\]
Each summand is the integer-point count of a bounded rational polytope. The construction uses flag minors, a finitely generated monoid of balanced exponents, Reynolds averages of bounded ordinary degree, and polynomial elimination. It makes no assumption about any unknown plethysm coefficient, any canonical basis, or the sign of any character sum. No polynomial bound in the varying parameter `m` for its output size or running time is asserted.

### The finite construction

Let `X=(x_ij)` be an `m by m` matrix of indeterminates over `Q`. For every nonempty subset `I subset {1,...,m}`, let `p_I(X)` be the minor with row set `I` and first `|I|` columns. Introduce a formal variable `z_I` for each such subset. Let
\[
\mathcal H_m=\left\{b\in\mathbb Z_{\ge0}^{2^m-1}:
\sum_{I\ni1}b_I=\cdots=\sum_{I\ni m}b_I\right\}.
\tag{G9.2}
\]
Compute its finite Hilbert basis `b^(1),...,b^(s)`, and put `q_l=product_I p_I^{b_I^(l)}`. The common sum in (G9.2) is its positive integer `n_l`; its right-torus highest weight is
\[
\lambda^{(l)}=\sum_I b_I^{(l)}\omega_{|I|},
\quad\omega_j=(1^j,0^{m-j}).
\tag{G9.3}
\]

Row permutation matrices send each formal `z_I` to `epsilon(sigma,I) z_(sigma I)`, where `epsilon` is the sign needed to sort the permuted row indices. They consequently permute Hilbert-basis monomials up to signs. Let `Y_1,...,Y_s` carry this signed permutation action and map `Y_l` to `q_l`. Form every Reynolds average
\[
\mathcal R(Y^v)=\frac1{m!}\sum_{\sigma\in S_m}\sigma(Y^v),
\qquad1\le|v|\le m!.
\tag{G9.4}
\]
Substitute `Y_l=q_l(X)` and discard zero polynomials. Denote the remaining explicit polynomials by `f_1,...,f_q`; duplicates may be retained. Their degrees `(n_j,lambda^(j))` give the columns of `D_m`.

Compute the elimination ideal
\[
J=\bigl(Z_j-f_j(X):1\le j\le q\bigr)
\cap\mathbb Q[Z_1,\ldots,Z_q].
\tag{G9.5}
\]
Use any fixed monomial order to compute a homogeneous Gröbner basis of `J`, and let `J_0` be the monomial ideal of its leading terms. Let `B_j` be the largest exponent of `Z_j` in the finite minimal monomial generating set of `J_0`, with `B_j=0` when it never occurs. Partition the nonnegative exponent lattice, independently in each coordinate, into the singleton cells `0,...,B_j-1` and the final interval `B_j+Z_{≥0}`. A resulting cell is uniquely `u+Z_{≥0}^S`, with `u_j=B_j` on its free coordinates and a selected smaller integer on the other coordinates. Retain exactly those cells with `Z^u notin J_0`. These retained pairs form `C_m`.

All steps are finite and effective: Gordan's lemma and Hilbert-basis algorithms apply to (G9.2), finite-group Noether generation applies to (G9.4), and Buchberger elimination terminates for (G9.5). Exact cited locators are supplied in the background register. The Gröbner-basis step uses only the explicitly constructed polynomials `f_j(X)`.

### Proof of the invariant-ring realization

Let `E=F=Q^m`, with left and right general linear actions on
`P=Sym(E tensor F)`. Let `U` be the upper unipotent group on the right, and let `T_0` be the determinant-one diagonal torus on the left. Cauchy duality gives
\[
R=P^U=\bigoplus_\lambda S_\lambda E\otimes L_\lambda,
\tag{G9.6}
\]
where `L_lambda` is the right highest-weight line. The subalgebra generated by the flag minors is all of `R`. To see this, the flag minors of size `j` span its component `Lambda^j E tensor L_(omega_j)`. The product of components with multiplicities `lambda_j-lambda_(j+1)` has right weight `lambda`. It is nonzero because `R` is a domain. Its image is a nonzero left `GL(E)` submodule of the irreducible right-weight component `S_lambda E tensor L_lambda`, hence it equals that whole component. Every partition is a sum of these fundamental weights. This proves the claimed generation, including the concrete generators used above.

The torus `T_0` fixes exactly the equal left-weight components `(n^m)`. Therefore
\[
R^{T_0}=\bigoplus_{n,\lambda}
M_{\lambda,n}\otimes L_\lambda.
\tag{G9.7}
\]
The left permutation matrices normalize `T_0` and commute with the right action. Taking their invariants gives the actual finitely generated algebra
\[
A_m=(R^{T_0})^{S_m},\qquad
\dim(A_m)_{(n,\lambda)}=a_{m,n}^{\lambda}.
\tag{G9.8}
\]
The equality of dimensions is T-002 with its literal permutation action.

For completeness, the finite presentation above indeed generates this exact algebra. The polynomial ring in formal flag-minor variables surjects equivariantly onto `R`. Extracting a torus weight is exact: a preimage of a homogeneous invariant decomposes into weight components, and its zero-weight component still maps to that invariant. The torus-invariant monomials are exactly (G9.2); their Hilbert basis consequently gives the surjection `Q[Y_1,...,Y_s]→R^{T_0}`. The basis is preserved by the signed permutation action because indecomposability in the monoid is preserved by coordinate permutations. Averaging over `S_m` makes invariants exact as well. Noether's degree bound says that the averages of monomials of ordinary `Y`-degree at most `m!` generate `Q[Y]^{S_m}`. Their images thus generate precisely `A_m`. Their explicit image kernel is (G9.5). Every image generator is homogeneous for `(n,lambda)`, and `n_j>0`, because every nonconstant monomial in (G9.2) has positive common row sum.

### Proof of the positive count

Residue classes of monomials outside `J_0` form a basis of `Q[Z]/J`, by Gröbner division. The ideal is multihomogeneous for `D_m`, so division preserves the grading and this is a homogeneous basis of `A_m`. For any monomial generator `Z^a` of `J_0`, the test `v_j>=a_j` is constant throughout each cell of the above partition: a fixed coordinate is constant, and a free coordinate satisfies `v_j>=B_j>=a_j`. Consequently membership in `J_0` is constant on the entire cell. Retaining its lower corner outside `J_0` retains exactly the standard monomials, with no overlaps. Its exponents have the unique form `u+z`, `z in Z_{≥0}^S`, and its degree is `D_m u+D_(m,S)z`. Taking degree `(n,lambda)` proves (G9.1).

Finally its first degree equation is
\[
\sum_{j\in S}n_j z_j=n-\sum_j n_j u_j,
\]
with every `n_j>=1`. Every nonnegative real solution has each coordinate at most `n` when the right side is nonnegative; a negative right side gives an empty set. Thus the real polyhedra being counted are bounded. This completes the proof for all parameters, including vanishing coefficients.

### The fully computed rank-two instance

For `m=2`, the flag algebra is `Q[x_1,x_2,delta]`; the right highest weights are `(1,0),(1,0),(1,1)`. The balanced torus algebra is `Q[u,v]`, with `u=x_1x_2`, `v=delta`. The transposition fixes `u` and negates `v`, so
\[
A_2=\mathbb Q[u,v^2],\qquad
\deg u=(1;2,0),\quad\deg v^2=(2;2,2).
\]
Its initial ideal is zero, and G-009 gives the single polytope
\[
\{(a,b)\in\mathbb R_{\ge0}^2:
a+2b=n,\ (2a+2b,2b)=\lambda\}.
\]
This recovers T-006 through the exact invariant-algebra morphism. It is also an explicit check that the row-permutation determinant sign has survived the construction.

### Geometric and complexity content

The generators and relations define affine schemes over `Q`; the maps are given by the flag minors, the torus monomial morphism, and the finite-group Reynolds morphism. Clearing the finitely many rational denominators gives models over a localization of `Z`, with the characteristic-zero fiber stated above. The initial ideal gives a multigraded flat Gröbner degeneration, and its standard monomials are the lattice points used in (G9.1). The count is the class multiplicity in the same representation `K_0` and same balanced normalizer module as T-002, now evaluated by a finite presentation.

The process includes a Hilbert-basis computation in `2^m-1` variables, Reynolds enumeration through ordinary degree `m!`, polynomial elimination, and a finite cell list depending on an initial ideal. No bound polynomial in the varying input size has been proved for any of those complete precomputation data. Thus this supplies a terminating positive-polytope construction in the literal counting sense. The smaller formulas T-012--T-013 and G-007 avoid that precomputation in their stated families. GCT questions asking for efficiently constructed polytopes or uniform nonvanishing certificates retain those additional requirements; neither a complexity-class separation nor their failure follows from the construction.

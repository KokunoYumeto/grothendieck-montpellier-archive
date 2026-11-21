# General Schur coefficients and canonical-map ranks

## G-010. The positive-polytope construction for general Schur plethysm

Let `mu` be a partition of `m>=1`, `nu` a partition of `n>=1`, and `N=mn`. Let `H=S_n wr S_m subset S_N` act on its grid of `N` letters, and let
\[
W=[\nu]^{\otimes m}\otimes\operatorname{Inf}_{S_m}^H[\mu].
\]
Use integral standard polytabloid Specht matrices and their rational duals to specify the `H` action on `W^vee` exactly. There is a terminating construction of a finite set of bounded rational polytopes whose lattice-point counts sum to `p_(mu,nu)^lambda`, for every output partition `lambda` of `N`. The data use no unknown multiplicities. They are constructed as follows from G-009.

Take the flag algebra `R_N` and its balanced torus algebra `B_N=R_N^(T_0)`. Introduce variables spanning `W^vee`, each of auxiliary degree one, and form
\[
C_{N,H,W}=(B_N\otimes\operatorname{Sym}(W^\vee))^H.
\tag{G10.1}
\]
Its grading is `(b,lambda,k)`: balanced left weight `(b^N)`, right highest weight `lambda`, and auxiliary degree `k`. It has
\[
\boxed{\dim(C_{N,H,W})_{(1,\lambda,1)}=p_{\mu,\nu}^{\lambda}.}
\tag{G10.2}
\]

To produce its finite presentation, take the same Hilbert-basis variables `Y` used for `B_N`, add the `W^vee` variables `Z`, average every monomial of ordinary `(Y,Z)` degree from one through `|H|`, and substitute the flag-minor expressions for `Y`. The group action on `Z` is its explicit rational Specht action; it need not permute these variables. Discard zero images and introduce presentation variables `T_j` for the remaining polynomials `f_j(X,Z)`. Compute the graph ideal `(T_j-f_j(X,Z))` and eliminate **both** the matrix variables `X` and the auxiliary variables `Z`, leaving its intersection with `Q[T]`. Apply the threshold-cell construction of G-009 to this exact presentation kernel. The resulting matrix has columns `(b_j,lambda^(j),k_j)` with `b_j+k_j>=1`. For each retained cell the polytope is
\[
\{z\in\mathbb R_{\ge0}^{S}:
D_Sz=(1,\lambda,1)-Du\}.
\tag{G10.3}
\]
The sum of its lattice-point counts is the coefficient in (G10.2).

**Proof.** The multilinear weight space `(S_lambda Q^N)_(1^N)` is the Specht representation `[lambda]` under literal permutation matrices. This is the multilinear Schur--Weyl identification used in T-003 and recorded in Landsberg, Corollary 3.8(1). Thus the auxiliary-degree-one component of (G10.1) in balanced degree one is
\[
([\lambda]\otimes W^\vee)^H
=\operatorname{Hom}_H(W,[\lambda]),
\]
which is the exact wreath-product formula T-003. This proves (G10.2).

The map from the polynomial ring on `Y,Z` to `B_N tensor Sym(W^vee)` is equivariant and surjective. Characteristic-zero averaging is exact, and Noether's degree bound for the finite group `H` supplies exactly the stated invariant generators. Its proof only requires a linear action, so the Specht matrices on `Z` cause no additional assumption. Each average is homogeneous in all three gradings: `H` preserves the two gradings of every Hilbert-basis orbit, and preserves ordinary degree in `Z`. Thus elimination and the standard-monomial cell argument of G-009 apply. The linear functional `b+k` is positive on every nonconstant generator, and has value two on the target. This bounds every coordinate of every polytope by two divided by that generator's positive grading. It proves boundedness and completes the positive count. Many pieces are consequently empty; retaining them does not change the formula.

For arbitrary outer Schur type and a row inner index, a smaller construction uses `R_m`, `H=S_m`, and `W=[mu]`, with target `(n,lambda,1)`. It gives the same coefficient by T-003 and has the positive grading bound `n+1`. Thus the general construction includes both exact oscillator descriptions already established.

The algebraic-geometric statement is the invariant affine scheme (G10.1) with the indicated finite-group quotient. Its auxiliary-degree-one component is the covariant module for the explicit representation `W`; its specified graded component dimension is transported by the given wreath-product Hom isomorphism. All operations, equations, and rational actions are specified, and after clearing denominators give models over a localization of `Z`. No polynomial-size bound for the construction as `m,n,mu,nu` vary is proved.

## G-011. A positive-polytope construction for each canonical-map image multiplicity

For fixed `m,n>=1`, put `N=mn`, let `G=S_N`, and take the row and column wreath subgroups `H,K` used in G-002. There is a terminating finite-presentation procedure, independent of the output partition `lambda`, giving a finite sum of bounded rational-polytope counts for
\[
r_{m,n}^{\lambda}=\operatorname{rank}(P_K|_{[\lambda]^H}).
\tag{G11.1}
\]
The procedure constructs the image of the specified canonical map, including its possibly vanishing scalar on a multiplicity-one component.

### Explicit module construction

Let `B=R_N^(T_0)` be the balanced flag algebra, and let `C=B^G=A_N`, with its explicit homogeneous invariant generators `c_1(X),...,c_q(X)` from G-009. Let `q_1(X),...,q_s(X)` be the Hilbert-basis generators of `B`. Put `h=|G|=N!`, and let `u` range over the finite box `0<=u_i<h`. Compute the polynomial vectors, here ordinary scalar polynomials,
\[
g_u(X)=P_KP_H\bigl(q_1(X)^{u_1}\cdots q_s(X)^{u_s}\bigr),
\tag{G11.2}
\]
and discard zero images. Each retained generator has its explicitly known degree `delta_u=(b_u,lambda^(u))`. Define the `C`-module
\[
M=P_K(B^H)\subseteq B^K.
\tag{G11.3}
\]
Its degree `(1,lambda)` is the image in (G11.1). Equations (G11.2) generate the entire module (G11.3), not merely the degree under consideration.

To compute a finite presentation over `Q[Z_1,...,Z_q]`, set `Z_j=c_j(X)`. The kernel of
\[
\bigoplus_u\mathbb Q[Z]e_u\longrightarrow\mathbb Q[X],
\qquad e_u\longmapsto g_u(X)
\tag{G11.4}
\]
is computable by syzygies and elimination. Explicitly, in `Q[Z,X]` compute the syzygy module of the row
\[
(g_{u_1},\ldots,g_{u_t},Z_1-c_1(X),\ldots,Z_q-c_q(X)).
\]
Project onto its first `t` components and intersect with `Q[Z]^t` by a module elimination order. This yields exactly the kernel in (G11.4). Use a homogeneous module Gröbner basis. Its leading submodule has the form `directsum_u J_u e_u`, with each `J_u` a monomial ideal. Decompose the standard monomials for each `J_u` into the threshold cells of G-009; discard a summand with `J_u=(1)`. For each retained pair `(u;v,S)` count
\[
\{z\in\mathbb Z_{\ge0}^{S}:
D_Sz=(1,\lambda)-\delta_u-Dv\}.
\tag{G11.5}
\]
The sum of these nonnegative counts is (G11.1).

### Proof of generation and the rank identity

Every element `q_i` satisfies the monic equation
\[
\prod_{g\in G}(t-gq_i)=0\quad\text{at }t=q_i,
\]
whose coefficients are in `C`. Reducing one exponent at a time shows that the monomials `q^u`, `0<=u_i<h`, generate `B` as a module over `C`. An invariant coefficient commutes with both averages: `P_H(cf)=cP_H(f)` and `P_K(cf)=cP_K(f)` for `c in C`. Averaging the finite generating expression first by `H` and then by `K` consequently proves that (G11.2) generates (G11.3).

All actions commute with the right highest-weight grading and preserve the balanced left grading. In degree `(1,lambda)`, `B` is `[lambda]` by the multilinear identification used in G-010. Thus (G11.3) in that degree is exactly `P_K([lambda]^H)`, with no substitution of an arbitrary map. This proves the asserted rank identity.

The syzygy-elimination description is exact because a vector `(a_u)` belongs to (G11.4)'s kernel precisely when `sum a_u(Z) g_u(X)` belongs to the ideal `(Z_j-c_j(X))`. Adding the coefficients expressing that ideal membership produces a syzygy of the displayed row, and projecting a syzygy gives such an ideal membership. The intersection enforces that the coefficients contain no `X` variables. These two implications prove the claimed kernel equality. Buchberger's module algorithm and elimination terminate over the polynomial ring.

Assign `deg e_u=delta_u`. The kernel is homogeneous because (G11.4) respects degrees. Standard module monomials therefore give a homogeneous vector-space basis of `M`. The threshold-cell argument proves (G11.5) exactly as in G-009. Every coefficient variable `Z_j` has positive balanced degree, so the first equation in (G11.5) bounds all nonnegative real coordinates; a negative remaining degree gives the empty set. This proves both positivity and boundedness.

The same finite data give the kernel and cokernel blocks: use the presentation of `B^H` with generators `P_H(q^u)`, the presentation of `B^K` with generators `P_K(q^u)`, and the explicit images (G11.2). Module kernels and quotients have homogeneous finite presentations over `Q[Z]`, so the same standard-monomial construction counts their multiplicities. This is a terminating determination for each specified pair `(m,n)`. The theorem does not give a uniform inequality proving all open parameter families of canonical injectivity or surjectivity.

In scheme language, (G11.3) is a coherent module on `Spec C`; (G11.4) is a finite presentation of its associated coherent sheaf, and the two idempotents are the precise averaging correspondences. Module Gröbner degeneration preserves the graded Hilbert function. Thus the positive lattice counts are transported through an explicit coherent-module presentation to the canonical map, rather than through its source and target dimensions alone.

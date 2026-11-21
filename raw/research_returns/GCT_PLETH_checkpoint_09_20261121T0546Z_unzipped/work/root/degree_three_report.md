# Outer degree three and the canonical two-row blocks

## G-006. Canonical-map isomorphisms on every two-row block

For every `m,n>=1`, the canonical map `h_(m,n)` is an isomorphism on each isotypic multiplicity space indexed by a partition with at most two rows. In particular
\[
r_{m,n}^{\lambda}=a_{m,n}^{\lambda}=a_{n,m}^{\lambda}
\quad(\ell(\lambda)\le2).
\]
This is the natural-transformation form of the classical canonical Hermite reciprocity theorem, stated in the supplied Landsberg survey, Theorem 7.21, §7.7. Its precise transfer to arbitrary ambient dimension is as follows.

**Proof of the transfer.** A natural transformation between homogeneous characteristic-zero polynomial functors is the direct sum, over partitions `lambda`, of the identity on `S_lambda` tensored with a fixed linear map between its multiplicity spaces. Evaluation on `C^2` kills exactly the summands of length greater than two. Canonical Hermite reciprocity says the evaluated transformation is an isomorphism. Consequently every retained multiplicity map is invertible, and those same maps occur after evaluation in every larger dimension. This proves the displayed rank equality, including the specified canonical map.

The geometric realization is the multiplication morphism of G-003 in rank two: every binary form factors into linear forms over `C`, so the Chow image is the whole affine space of binary forms. Its coordinate pullback is injective. Both sides have dimension `binom(m+n,m)`, giving the canonical isomorphism. This is the exact morphism relating the factorization statement, the coordinate ring, and the canonical map; the source theorem is known.

## G-007. Explicit one-dimensional lattice counts for every outer Schur index of size three

The coefficients in this family are classical (Thrall and Chen). Their explicit current primary presentation is Maas--Gariépy and Tétreault, *3-Plethysms of homogeneous and elementary symmetric functions*, arXiv:2209.14942v1, §4.2, pp.8--9; their tableau realization is Theorem 1, §7.3, p.20. Here the formula is put in the literal permutation-matrix realization of T-002, retaining the two finite-character corrections.

Let `lambda=(lambda_1,lambda_2,lambda_3)` be a partition of `3n`, padded by zeros. Set
\[
L=\max(\lambda_3,2n-\lambda_1),\qquad
U=\min(\lambda_2,2n-\lambda_2,n),\qquad K=U-L+1.
\]
Define `d_2=0` for even `K` and `d_2=(-1)^L` for odd `K`. Let
\[
(b_1,b_2,b_3)=(\lambda_1+2,\lambda_2+1,\lambda_3)\pmod3.
\]
Set `d_3=0` for repeated residues; for three distinct residues set `d_3` equal to the sign of the permutation carrying the ordered residue list `(2,1,0)` to `(b_1,b_2,b_3)`. Then
\[
p_{(3),(n)}^{\lambda}=\frac{K+3d_2+2d_3}{6},\qquad
p_{(1,1,1),(n)}^{\lambda}=\frac{K-3d_2+2d_3}{6},\qquad
p_{(2,1),(n)}^{\lambda}=\frac{K-d_3}{3}.
\tag{G7.1}
\]
Each quotient is the following positive lattice-point formula: for its numerator `B` and denominator `D`,
\[
\boxed{\#\{z\in\mathbb Z:1\le z,\ Dz\le B\}.}
\tag{G7.2}
\]
The residue tests are finite case selection, and within each selected chamber the displayed bounds are affine linear in `lambda,n`. The intervals are allowed to be empty. The statement imposes no homogeneous-dilation requirement.

**Proof of the normalizer dictionary.** The balanced space `M=(S_lambda C^3)_(n,n,n)` is a representation of `S_3`. Restricting first to `GL_2 times GL_1`, the interlacing highest weights contributing balanced degree are `(2n-k,k)` for exactly `L<=k<=U`. Each contributes a single `(n,n)` weight line. The transposition of the first two basis vectors acts on this line by `(-1)^k`, as the explicit determinant calculation in T-006 shows. Thus its trace is `sum_(k=L)^U(-1)^k=d_2` and the identity trace is `K`.

A three-cycle permutes the torus weight spaces of `S_lambda C^3`. Only a weight constant on all three coordinates contributes to its trace; the total degree `3n` makes that weight `(n,n,n)`. Its trace on `M` therefore equals its trace on the whole representation. The cycle has eigenvalues `1,zeta,zeta^2` for a primitive cube root `zeta`. The Weyl alternant formula evaluates its character as
\[
\frac{\det(x_j^{\lambda_i+3-i})_{1\le i,j\le3}}
{\det(x_j^{3-i})_{1\le i,j\le3}},
\qquad(x_1,x_2,x_3)=(1,\zeta,\zeta^2).
\]
The denominator is nonzero. Repeated exponent residues give two equal rows and value zero; distinct residues give the stated row-permutation sign. Thus the three-cycle trace is `d_3`.

The three irreducible characters of `S_3` have values `(1,1,1)`, `(1,-1,1)`, and `(2,0,-1)` on identity, transpositions and three-cycles, whose class sizes are `1,3,2`. Taking these character inner products proves (G7.1), via T-003. Each is consequently a nonnegative integer. For `B=Dc` with `c` that nonnegative multiplicity, the integer solutions of (G7.2) are exactly `1,...,c`; the interval endpoints were computed by the explicit bounded trace calculation, rather than by a general coefficient oracle. This proves (G7.2). The interlacing interval is nonempty for every partition of `3n` of length at most three; this also follows from the inequalities `lambda_1>=n>=lambda_3` and `lambda_1+lambda_2+lambda_3=3n` in the definitions of `L,U`.

The geometric statement is the equality in the characteristic-zero representation ring `K_0(BGL_r)` and its pullback along the frame torsor of a locally free rank-`r` sheaf. The two traces are taken along the explicit constant subgroup scheme `S_3→GL_3` of permutation matrices, and the determinant factor in the transposition action is retained. Hence this evaluates, rather than omits, the normalizer projector for the entire outer-degree-three family.

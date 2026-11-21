# Independent whole-proof review: G-15

Reviewer: `/root/rectangular_bridge`, GPT-6 Astra Pro; effort inherited/not exposed; run `CUE_GCT-20261121`.

**PASS.** I read the complete `g15_fragment.tex` proof and the complete `g14_fragment.tex` coefficient-weight argument on which its final multiplicity consequence depends. I found no mathematical gap. This is an independent-agent mathematical review, not formal verification or an external referee certification. I did not rerun the finite-size Jacobian computations; those remain separate root checks.

## Harmonic covariants and normalization

The chosen three generators do give the standard invariant quadratic form: in the defining representation, the matrix of `A(z)` squares to `(z1^2+z2^2+z3^2)I`. The Hermitian normalization is compatible with the compact form, so distinct irreducible summands of `End(V)` are orthogonal for the normalized trace form.

The map `pi_l(rho(A)^l)` is nonzero: the highest-weight vector maps to `rho(E)^l`, which is nonzero for `l<m` and lies in the highest-weight `2l` summand. Its coefficient functions are harmonic of degree l by the multiplicity-one harmonic decomposition. Its value at H cannot vanish, because equivariance and homogeneity would then make the entire map vanish on the dense semisimple locus `q!=0`. This also proves that its diagonal value gives the nonzero top piece of `rho(H)^l`.

The triangular span argument identifying the zero-weight vector in `E_l` with the orthogonal polynomial `p_l(rho(H))` is sound. The powers `H^r` lie in irreducible summands indexed at most r, their top projections are nonzero, and the diagonal zero-weight spaces are one dimensional. Normalized trace on diagonal matrices is precisely the uniform inner product on the m distinct spectral nodes. Therefore Gram-Schmidt identifies the successive components with the stated `p_l`, including the nonzero normalization constant.

The adjugate decomposition `pi_l adj(M)=T_l(A)F_l(t,q)` follows from equivariance and the harmonic decomposition in each homogeneous degree. It permits several invariant monomials in F, as it must, and its weighted degree is exactly `m-1-l`.

## Jacobi factors

Multiplication by x in the finite orthonormal polynomial basis is real symmetric and tridiagonal. Its off-diagonal entries are positive leading-coefficient ratios; parity of the symmetric node distribution forces its diagonal entries to be zero. The spectral formula for the `(l,0)` resolvent entry contains `p_l(lambda_j)p_0(lambda_j)/m`, with `p_0=1`, exactly matching the trace coefficient of the adjugate. The cofactor sign cancels the l negative off-diagonal entries in `tI-J`, giving the positive product `b1...bl` times the trailing determinant. Thus equation G15:jacobi has the correct factor and trailing index.

Every trailing block retains positive off-diagonal entries. The eigenvector recurrence establishes simple eigenvalues, alternating signs give spectral symmetry, and the even-size determinant at zero is a nonzero product of alternate squared entries. Consequently odd-degree trailing characteristic polynomials have a simple zero at zero, while even-degree ones have a nonzero constant coefficient. The empty and one-dimensional cases have the stated conventions.

## The linear cofactor space and all third-jet components

The space C_m is indeed the differential image of the determinant-pencil map, since varying each matrix entry by an arbitrary linear form gives all linear-form multiples of complementary determinants. It is invariant for the same SL2 action. Constant projections of the adjugate entries first give every `F_l H_l`, so multiplication by t gives the first family in the proof.

For the second family, multiplying `H_(l+1)` by the three linear forms has a nonzero component in `q H_l`. The derivative identity for the Laplacian verifies nonvanishing, and irreducibility gives the entire H_l. Applying the SL2 isotypic projection to these particular products isolates that component: those products have only types `H_(l+2)` and `H_l`. Other H_l copies elsewhere in C_m do not invalidate this projection. Multiplication by the invariant scalar polynomial F preserves the argument. Thus `q F_(l+1) H_l` really lies in C_m. The highest product similarly supplies H_m.

The quotient by t^4 decomposes exactly as stated. For D=m-l equal to 0 or 1, the single required multiplicity component is already supplied. For D>=2, there are exactly two admissible t powers of the relevant parity. Specialization q=1 is injective on that fixed multiplicity space, because the q exponent is determined by the t exponent.

In the even-D case, `t Q_l` has a nonzero t^2 coefficient and no constant term, while `Q_(l+1)` has a nonzero constant term. In the odd-D case, the trailing even block K is invertible. The diagonal resolvent cofactor is `Q_(l+1)/Q_l`. Alternating-sign symmetry makes the odd inverse-power diagonal entries zero, and the expansion gives the coefficient `-e^T K^-4 e` of t^2 in `Q_(l+1)/(t Q_l)`. This coefficient is strictly negative because it is minus a squared nonzero norm. Since `t Q_l` has a nonzero linear coefficient, a nonconstant t^2 term in that ratio is exactly the obstruction to proportionality modulo t^4. This proves the required two-dimensional span in every remaining case.

## Dominance, maximal order, and multiplicities

Surjectivity of the differential to the third-jet affine target proves dominance over C. The dimension sum is `2m^2+2` for m>=4. Adding the next jet contributes `binom(m-2,2)>0`, so the established determinant-image upper bound excludes fourth-jet and higher full dominance. Small m have all available jets and are covered by the proof.

I also read the full G14 weight argument. In the positive weight convention each coordinate of a weight of shape lambda is at most lambda1. After substituting `x0^a q`, a surviving degree-d coefficient monomial has x0 weight `ad+sum j_i`. Under `lambda1<=ad+3`, its evaluation therefore depends only on the first four coefficient forms. Dense determinant realization of those data, followed by block padding, gives vanishing for every q; GL4 changes allow an arbitrary padding linear form. This gives the claimed determinant-isotypic ideal containment and hence the multiplicity inequality. The highest-weight restriction to four variables is the already established ambient convention, not a new unstated restriction.

For a rectangle, a positive gap requires `nd/4>ad+3`, hence `d(4m-3n)>12`. The quantity is divisible by four when the rectangle is integral, so the equivalent threshold is at least 16. This agrees with the earlier G12 boundary.

No literature-priority claim or unsupported strong Lefschetz assertion is needed. The standard Clebsch-Gordan background remains cited background; the new uniform rank argument is fully established in the fragment.

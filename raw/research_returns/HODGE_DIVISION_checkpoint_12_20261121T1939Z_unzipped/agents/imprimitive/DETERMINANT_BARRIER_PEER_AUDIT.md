# Whole-proof audit of D-DET-01--03

Run HODGE_DIVISION; 2026-11-21, completed about 12:27 UTC.
Reader: `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed.

**PASS.** I read the complete current `agents/g34_eightfolds/barrier/determinant_barrier.tex`, reconstructed the linear algebra and both universal source barriers, and checked the exact geometric cup-form convention against the primary paper. This is a whole-proof mathematical audit, not a proof-assistant certificate. I did not independently rerun the sibling's finite unpaired-tuple enumeration in this check.

## D-DET-01: actual cup form and determinant

For the right-action convention, the transported coboundary satisfies
`sum_(j<i) d(a)_j = a-a g_i q_i`. On the moving space,
`(g_i-1)(1-g_i^-1)^-1 = g_i`. Extending the inverse by zero on the fixed space adds exactly the orthogonal projector occurring in the proof. Thus the diagonal term together with the preceding sum pairs with `z_i` as `h(a,z_i)`. This proves the identity `S(d(a),z)=h(a,Rz)` with the stated sign.

The diagonal operators obey `A_i+A_i^*=1`, so `S+S^*=R^*hR`. The triangular form is nondegenerate, and injectivity of the coboundary map implies surjectivity of R by the displayed pairing identity. On `ker R` both-sided orthogonality to `dV` follows from these two identities. Nondegeneracy on the full space and the codimension of `ker R` show that its radical is exactly `dV`; there is no unproved quotient nondegeneracy assumption.

I read Dettweiler--Wewers, *Variation of parabolic cohomology and Poincare duality*, author version arXiv:math/0411119, Theorem 2.5 on PDF page 12 and its complete proof on pages 13--14. The right-module convention and cocycle relation are on pages 2--3. The primary PDF was opened directly at <https://arxiv.org/pdf/math/0411119>; browser reference `turn734901050view0`. Published metadata are Seminaire et Congres 13 (2006), 145--164, confirmed at the publisher <https://smf.emath.fr/node/43624>.

Under the invariant-Hermitian duality, the theorem's double-sum term is
`h(u_j g_(j+1)...g_(i-1)(g_i-1), v_i(g_i-1)^-1)`.
Moving the first-argument operator to the second argument gives
`-h(u_j, v_i(g_(j+1)...g_i)^-1)`. Transport by the tails therefore gives the negative of the off-diagonal part of S. The diagonal term becomes
`-h(u_i(1-g_i^-1)^-1,v_i)`, hence the negative of its diagonal part. The geometric cup form is exactly `-S_P` in these conventions. The even dimension removes the global sign from the determinant.

For the basis consisting of coboundaries, quotient representatives and an R-isomorphic complement, the Schur complement has the block matrix `[0 B; -B^* J']`. Its determinant is `N(det B)`: the column permutation sign `(-1)^(m^2)` cancels the factor `(-1)^m` from the lower-left block. Thus there is no missing factor `(-1)^m` in the claimed determinant class. The diagonal blocks of the triangular form give `prod det(h_i)/b`, since the first argument is conjugate-linear. The relation `bar b=(-1)^D(prod det g_i)^-1 b=b` is valid because D is even and the product is one.

Finally, for a purely imaginary eta, `(-1)^n eta^(2n)=N(eta^n)`, exactly as required for the signed Hermitian discriminant. The scalar changes from the multiplicity pairing to the selected geometric one-copy factor contribute an even power of a rational number, hence a K-norm. Conjugation or duality also preserves the class. The formula therefore concerns the actual polarization, not merely an auxiliary invariant form.

## D-DET-02: the G24 barrier

The norm-two reflection line has norm determinant because `N(tau)=2`. For a rank-two involution, negation is a rank-one reflection, and orthogonal decomposition with `det H=1` gives plane determinant class `1/2`, again a norm. The central negative identity has full determinant one. These assertions use the already checked natural G24 group and root realization.

The base-genus argument is a necessary-dimension argument with the correct exceptional dimensions: for genus one, `D=6` and the pointed-base moduli dimension is at most six; for genus two, `D=0`, leaving only the three-dimensional unramified-base moduli; larger genus is impossible. For genus zero, `D=12`, and rank-nine dominance forces twelve branch points with all moving dimensions equal to one. The nontrivial eigenvalue is the trace minus two and lies in K; it is consequently -1. Thus every potentially dominant tuple falls under the local involution determinant calculation. No sufficiency of parameter dimension is asserted.

## D-DET-03: the F4-extension barrier

For an outside involution `g=tA`, the equations of unitarity and involutivity imply `A^t=-A` and `A^2=-I/2`. The rational map `x -> (1-tA)x` is injective by comparing rational and t parts, lands in the negative eigenspace, and has the full rational dimension four. Its diagonal Hermitian form is `2 x^t x`: the cross terms vanish by skew symmetry and the final term uses `A^t A=I/2`.

The trace-Witt argument is valid over Q, not just over R. If two rational diagonal forms are isometric, their difference is rationally hyperbolic. A rational isotropic vector in the underlying vector space is a K-isotropic vector. Splitting a Hermitian hyperbolic plane splits a rational hyperbolic four-space; rational Witt cancellation leaves a hyperbolic complement. Induction proves that the Hermitian difference is hyperbolic. Its even-dimensional determinant identity implies that the two original determinant classes differ by a norm. The explicit negative plane of z has determinant two, `N(t)=2`, so every outside involution has norm moving-plane determinant.

The numerical dominance argument is also exact. Genus one gives `D=6` and at most six parameters; larger genus is impossible. Over P1, `D=14`. Generating monodromy contains a positive even number of elements outside W. Since `bar g=-g`, its +1 and -1 eigenspaces have equal dimension, forcing each outside moving dimension to be at least two. Thus there are at most twelve branch points. Rank nine forces precisely twelve: ten rank-one elements of W and two outside elements of moving rank two. Each of the latter then has two +1 and two -1 eigenvalues and is an involution. All local determinants are norms, so the actual signed discriminant is split.

The final boundary statement is appropriately limited to these two natural representations and genuinely generating curve-cover sources. It does not purport to classify every finite group or every nonlinear geometric source.

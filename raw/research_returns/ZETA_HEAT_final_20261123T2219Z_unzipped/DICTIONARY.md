# Exact mathematical dictionaries

These dated records distinguish exact proven maps from background and from open quantitative estimates. No priority claim is made.

# Exact algebraic dictionary for the finite tests

The constructions below are the explicit morphisms used in these sections. They assign no additional arithmetic or motivic estimate to the analytic formulas.

## Exterior powers, Schur functors and Toeplitz minors

For a finite alphabet beta_1,...,beta_d, let T be the diagonal endomorphism of V=C^d with these eigenvalues. Direct expansion in the exterior basis gives

    det(I+wT) = sum_k Tr(exterior^k T) w^k = product_j(1+beta_j w).

Thus elementary coefficients are the evaluations of exterior-power characters. The representation-ring specialization sends the universal elementary symmetric function e_k to Tr(exterior^k T). Dual Jacobi–Trudi sends every allowed coefficient Toeplitz minor to the corresponding skew Schur character, with the exact row/column index transformation proved in the paper. Direct sums send the determinant polynomial to a product; their exterior-power decomposition proves the coefficient convolution formula. This is the concrete lambda-ring relation: SGA6, ExposéV, Example2.2(b) and Lemma2.2.1 construct exterior-power operations from the filtration of an exact sequence and explicitly include representation rings. The primary text was opened at https://grothendiecksga.com/read/sga6/fr/V-2.html.

For the entire product, finite alphabets converge coefficientwise and on compact sets because the reciprocal parameters are absolutely summable. Every fixed Schur determinant therefore has a well-defined limiting specialization. Its nonnegative real evaluation is the finite positivity property proved here. No integrality of these evaluated real numbers is needed in this morphism.

Archive cote: ours/NEG_NIGHT_analytic/pf_characters.tex and finite_rank_characters.tex explicitly give the exterior-power/SGA6 connection. The paper gives the analytic parameter map beta -> beta/(1-beta) and the exact unitary character expansion, so the coefficient cone is related to an explicit probability mixture of irreducible polynomial representations.

## Finite schemes and the heat weights

A fixed contour with d enclosed zeros gives a monic polynomial P_a through its argument-principle power sums and Newton identities. The quotient C[w]/(P_a) is a length-d finite scheme algebra. Its companion endomorphism has the contour power sums as traces. This proves the passage from contour integration to the finite algebra, without choosing individual roots through a multiple endpoint.

At a zero of multiplicity m, the local analytic algebra over the time ring is finite free of rank m by Weierstrass preparation. Give a=z-time parameter weight2 and z-x weight1; after the base change a=q^2 and the blowup chart z-x=qu, its lowest-weight equation is the Hermite polynomial e^(D_u^2)u^m. The weighted calculation in the Jensen proof adds the principal operator -w0^2 D_u^2/(2N), and the coefficient 4*a*x^2-x^4/(2N) is the exact local comparison. These are filtrations and associated graded equations of the stated finite analytic algebras; their weights are defined by this scaling.

Archive cote: multiplicity_detection_equivalence.tex, orbital_detection_constants.tex and the G039 paragraphs in ours/NEG_NIGHT_paper/checked.tex contain the corresponding finite-algebra and character translations. No Frobenius-weight theorem is an input to the analytic scaling argument.

## Derivative moments as traces and a projector

For a packet polynomial P with zeros x of multiplicity m_x, put A=C[z]/(P). For any analytic observable g on the packet, multiplication by g on A has trace sum_x m_x*g(x): in each local factor C[epsilon]/(epsilon^m), its matrix is triangular with diagonal g(x). Applying this to g=(f')^2 proves that the contour moments are exactly Tr_A(M_g^k). The trace factors through evaluation on the reduced support, because multiplication by a nilpotent has trace zero.

Let B be the reduced algebra of the distinct derivative values: B=R[U]/product_v(U-v). The functional L(h)=sum_v w_v*h(v), with weights inherited from the lengths m_x, is the moment functional. Its Gram form is L(PQ), and its matrix on 1,U,...,U^d is the Hankel moment matrix. The polynomial product_{v>0}(1-U/v) represents in B the idempotent supported at the zero derivative value. Its squared norm and weighted trace are M0, the total length of the multiple-endpoint fibers. This explicitly carries the Christoffel minimum to a finite support projector. The integer threshold2 uses that each nonreduced zero has length at least2.

These trace and evaluation maps are proved here. They identify the finite scheme length being measured. A construction over Spec Z, a correspondence acting on a motivic realization, or a Frobenius estimate reaching the all-height error threshold would require an additional specified object and a compatible comparison map; none is asserted by these finite identities.

## Finite zero surgery as an effective-divisor operation

The rational function R(s)=((s-1/2)^2+v^2)/((s-1/2)^2+u^2) changes the analytic zero divisor by

    [1/2+iv]+[1/2-iv]-[1/2+iu]-[1/2-iu].

Its product with the completed zeta function is entire because the two negative divisor terms cancel certified simple zeros. The exact derivative multiplication formula transports every divergent leading positive absolute moment. The endpoint determinant product cancels one factor and repeats another. The proof also computes the nonzero sigma^(-2) tail that obstructs an ordinary absolutely convergent Dirichlet series for this transformed function. These are the explicit divisor and character-specialization maps used in the information comparison.


# Exact mathematical translations for the motion and collision sections

These are explicit morphisms and finite-algebra constructions used by the proofs. They make no assertion that an unrelated geometric or motivic construction cannot exist. No archive cote is assigned where the mathematical input was derived directly here.

## Reduced zero divisors and the tangent map

Let F(s,q) be holomorphic and apply Weierstrass preparation near a zero. The zero family is locally the finite analytic algebra A=O_q[w]/(P(w,q)), with P monic. Its relative differentials are Ω_(A/O_q)=A/(∂P/∂w) dw. At a simple endpoint root, ∂P/∂w is a unit and the implicit branch has derivative −F_q/F_s. For F(s,q)=ζ(s,1+q), the differentiated Hurwitz series makes this derivative ρζ(ρ+1)/ζ′(ρ). For the heat family the exact coordinate morphism s=1/2+ix/2 carries x′=Hzz/Hz into s′=iHzz/(2Hz). The two displayed morphisms, not a terminology-based separation, identify which tangent is counted.

At an endpoint of multiplicity m the fiber algebra is C[w]/(w^m). Its nonzero nilpotents record nonreducedness; the derivative-weighted signed statistic vanishes there because F_s=0. Positive weighted counts in the density theorem therefore count reduced endpoint fibers. The proof is analytic counting plus this finite-algebra identity.

## Heat Hankel minors as trace forms

For a monic Weierstrass factor P(z,t) enclosing M roots, multiplication by z on A_t=C[z]/P has trace S_j=Tr(m_z^j), counted with algebraic multiplicity. This is the same trace obtained by the argument-principle contour integral. The matrix (S_(u+v)) is the bilinear trace form on 1,z,…,z^(k−1). Over the splitting cover its factorization VV^T identifies the minor with a sum of squared Vandermondes by Cauchy–Binet. The heat ramification t=q² maps each local root cluster to the Hermite model. The exact Jacobi spectral measure gives the coefficient C(m,a). Thus the minors and their orders are valuations of explicit trace-form determinants in the one-parameter analytic algebra. This is a local discriminant calculation, with a concrete trace morphism; no Frobenius weight interpretation is needed for its proof.

## Rotation averages and cyclic covers

Averaging the Hurwitz parameter over μ_d is the projection onto the invariant subring C{q^d}⊂C{q}. The quotient map of bases is u=q^d. At a multiplicity-m endpoint the local equation has the form cw^m+βu+…, β≠0. Passing to the cover u=v^m separates the m branches. Pullback along u=q^d gives the monodromy permutation j↦j+d modm and discriminant valuation d(m−1). For a product of local factors on disjoint disks, the resultant identity Disc(PQ)=Disc(P)Disc(Q)Res(P,Q)^2 makes the total order dΣ(m_i−1), because the cross-resultants are units. This is the exact finite-cover and invariant-ring construction behind the comparison.

## CUE determinants and exterior powers

The Haar unitary density is the squared Vandermonde, and integration of its two alternating determinants gives det(PuP) for multiplication by u on a finite Fourier space. This determinant is the action on its top exterior power. Conditioning on a marked angle removes the evaluation line from the projection, an explicit rank-one quotient. The determinant bound is governed by the Hilbert–Schmidt norm of (1−P)uP. The sine-process Fredholm determinant is the trace of the corresponding completed exterior-power expansion. The numerical certificate replaces the Fourier feature map by a polynomial feature map and controls the trace-norm difference. These identifications are the precise linear-algebra maps used; they do not assign a motive or an arithmetic weight to the probability.

## Character averaging and the common moment constant

The additive function χ(m)e(−m/(qk′)) on the finite group (Z/(qk′)Z)^× is decomposed into its one-dimensional characters. The principal projection has a Gauss scalar μ(k′)/(φ(q)φ(k′)) after multiplication by the functional-equation scalar. Character orthogonality bounds the remaining projections in L². At the Euler-product level, removing primes dividing q replaces ζ by Z_q, whose residue is φ(q)/q; these factors cancel against the same Gauss scalar. This proves the common moment constant by an explicit representation-theoretic projection and residue calculation. It is not a bare analogy between conductor-one and conductor-q formulas.

## No all-height conclusion from the recorded densities

The quantifier in the density theorem is liminf over dyadic blocks for a fixed character. A local Weierstrass algebra is reduced at every counted center, and the theorem gives a positive proportion of these centers. It does not quantify over every maximal ideal in the infinite endpoint zero divisor. Moving from the counting quantifier to all fibers would require the still-open growth estimate of the global detection criterion. The exact distinction is the difference between the two stated quantifiers, with the allowed uncounted divisor left unconstrained by the inequality.


# Spectral results: exact algebraic translations

These entries identify explicit maps carrying the analytic quantities to algebraic ones. They assert only the stated translations. No attached archive cote has been located for an additional motivic or weight-theoretic realization of the Weil operator; none is supplied here.

## SPEC-PARITY and SPEC-LIMINF: the reduced support and the length at a zero

At an ordinate gamma with multiplicity m, the analytic local algebra of the zero divisor is A_gamma = C{u}/(u^m), u=z−gamma. Its reduction map A_gamma → C sends u to 0. The source has C-dimension m, with basis 1,u,...,u^(m−1); the target has dimension 1. Thus reduction sends the zero scheme of Xi to the divisor with each distinct ordinate once. On any bounded disk avoiding zeros on its boundary, the direct sum of these maps realizes this passage for the whole finite zero scheme.

The proved product limit of the parity theorem is the entire function Delta_Gamma with local zero algebra C{u}/(u), while Xi has local algebra A_gamma. The analytic identity Delta_Gamma=Xi/Xi(0) obtained from the liminf Rayleigh estimate identifies their local principal ideals. Therefore (u)=(u^m) in C{u}, which holds precisely when m=1: for m>1, u is absent from (u^m). This is the exact local-algebra transport of the simplicity conclusion; no arbitrary normalization is used, since evaluation at zero fixes the scalar Xi(0).

## SPEC-PROBE-FIXED and SPEC-ROUNDING: recovering length by a trace weight

The sampling map sends f to the coordinate family (fhat(gamma)) in l²(Gamma,m), with norm squared sum m|fhat(gamma)|². The compact inverse C acts on that Hilbert space by the scalar 1/gamma in its gamma-coordinate. Its coordinate eigenspace has dimension 1, while the norm of the projected probe is m|phihat(gamma)|². Division by the proved nonzero probe factor therefore recovers dim_C A_gamma. This is an explicit equality between a Hilbert-space mass and the length of the local zero algebra, not an inference from the dimension of the eigenspace.

The underlying finite-dimensional C-vector space of A_gamma defines [A_gamma]=m[C] in K_0(C). This follows by the filtration 0⊂(u^(m−1))⊂...⊂(u)⊂A_gamma, whose successive quotients are C. Equivalently the exact forgetful functor from finite-length A_gamma-modules to C-vector spaces sends its Grothendieck class to m[C]. In the usual lambda-ring K_0(C), lambda_t([A_gamma])=(1+t)^m, because the kth exterior power has dimension binomial(m,k). No monoidal structure for tensor product over A_gamma is transported by this forgetful functor; the displayed lambda operations are the exterior powers over C explicitly stated here.

The numerical rounding proof certifies the integer m only after the analytic spectral projection and scalar-division errors total less than 1/2. It consequently certifies this K_0(C) class for the enclosed fixed coordinate. It does not prove a bound uniform over all coordinates.

## SPEC-TRACE-DEFECT: weighted length excess

For a finite set of ordinates, the direct sum of the reduction kernels has dimension sum(m_gamma−1). In the exact trace-defect identity the same nonnegative local lengths occur with weights gamma^(−2). The equality
D_N = ||C−P_NCP_N||_HS² + sum_signed_gamma (m_gamma−1)/gamma²
is proved by matrix-entry orthogonality and the paired Hadamard product. Since every weight is positive, a vanishing limit forces every reduction kernel to be zero. The signed convention doubles the sum over positive ordinates. No estimate making D_N tend to zero has been proved.

## SPEC-PROBE-TENT: an integral norm in a quadratic order

Let R=Z[s]/(s²−2), a finite free rank-two Z-algebra. Multiplication by m−ns in the basis (1,s) is the integer matrix [[m,−2n],[−n,m]], with determinant m²−2n². For a nonzero pair (m,n), this determinant is a nonzero integer, because rational sqrt(2) would otherwise equal m/n; the familiar parity descent proves irrationality. Its absolute value is at least 1. Under the two real embeddings s↦±sqrt(2), this determinant equals (m−sqrt(2)n)(m+sqrt(2)n). This exact norm identity supplies the separation estimate in the two-tent Fourier lower bound. It also identifies the determinant as the finite index of (m−ns)R in R when that quotient is nonzero. The quantitative trigonometric inequality then follows from the two real embeddings and sine concavity, as proved in the paper.

## SPEC-ROUNDING and the local Hankel comparison

The spectral projection calculation uses the eigenvalue separation |gamma^(−1)−eta^(−1)|=|gamma−eta|/|gamma eta|. The contour calculation uses separation of the corresponding closed points in the complex analytic zero divisor. The displayed identity is the precise change of coordinates linking those two separations on a bounded region away from zero. It supplies no additional arithmetic separation estimate. All-height certification still requires quantitative bounds for that separation and for the analytic approximation errors.

## SPEC-TRACE-HEIGHT: certifying reduction on a finite analytic subscheme

Let Z_T be the finite analytic zero scheme for 0<gamma≤T. Its reduction map has kernel of C-dimension E(T)=sum(m_gamma−1), as the direct sum of the local filtrations above shows. The exact trace inequality E(T)≤T²D_N/2 implies this kernel is zero once the right side is below1. This uses the discreteness of length and proves reducedness of Z_T. A certified bound on the global weighted length excess therefore certifies a finite subscheme without choosing an individual isolating circle for each point. The morphism being certified is the direct-sum reduction map already defined; no morphism to an unspecified motive is assumed.

## The exact multiplicity-copy isometry behind the trace defect

Define K=direct_sum_gamma C^(m_gamma), with ordinary Euclidean inner product on each summand, and define I:l²(Gamma,m)→K by I(v)_gamma=(v_gamma,...,v_gamma). Its norm squared is sum_gamma m_gamma|v_gamma|², exactly the original sampling norm. Its image is the closed diagonal subspace D, and the orthogonal projection in each block is the averaging matrix (1/m_gamma) times the all-ones matrix. The orthogonal complement has dimension m_gamma−1 in that block. Let C_full act by gamma^(−1) times identity on each block. Then I C=C_full I exactly; both subspaces D and D-perpendicular are invariant. Consequently tr(C_full²)=sum_signed m_gamma/gamma²=S, tr(C_full² on D)=sum_signed1/gamma², and tr(C_full² on D-perpendicular)=sum_signed(m_gamma−1)/gamma². This explicit isometry and invariant orthogonal decomposition realize the weighted multiplicity excess as a trace. They do not postulate a cohomology theory with these dimensions.

## A published geometric realization for curves

Suzuki, *A spectral theory of zeta functions of function fields*, arXiv:2610.41115v1, Proposition 8.1 and Corollary 8.2 (pp.24–25), Proposition 9.2 and Theorem 9.3 (pp.25–26), give an explicit comparison for a smooth projective curve C/F_q. Put h=log q, F=q^(−1/2)Frob, and E=span_C{F^k}, with Rosati trace inner product tau(XY*). The map U[u](t)=sqrt(h)sum_k u(t+kh)F^k is unitary onto L²((0,h),E), because its inner product expands exactly to the discrete Weil form. It satisfies U exp(ihD) U^(−1)=multiplication by F. Lemma 9.4 (p.26) gives the algebra isometry P(F)↦(P(zeta_1),...,P(zeta_d)), with norm sum_j m_j|P(zeta_j)|²; injectivity follows from the trace norm and surjectivity from Lagrange interpolation. These explicit morphisms provide a geometric instance of the same weighted-coordinate mechanism used above. The theorem is cited for curves; no corresponding zeta-function realization is asserted here.

## Higher trace powers and the reduced divisor

At a bounded divisor, take the exact local algebra A_gamma=C[e]/(e^m_gamma) and its quotient A_gamma→C. Its nilradical has dimensionm_gamma−1. Multiplication by (gamma+e)^(−2k) has upper triangular matrix with diagonal gamma^(−2k), so its trace is m_gamma gamma^(−2k). On the quotient its trace is gamma^(−2k); the difference is (m_gamma−1)gamma^(−2k). This is precisely the local contribution to the limit of D_{N,k}. In K0 of finite-dimensional vector spaces the exact sequence0→(e)→A_gamma→C→0 gives[A_gamma]−[C]=[(e)], with this weighted trace realization. Exterior-power generating series of the multiplication operator has determinant(1+t/gamma)^m_gamma and quotient(1+t/gamma); the nilradical ratio is(1+t/gamma)^(m_gamma−1). Logarithmic coefficients reproduce all inverse-power trace differences. These are explicit finite-algebra and lambda-operation maps; no unspecified motivic realization is used.

The l^(2k) norm of the repeated reciprocal ordinates tends to its largest entry. This exact norm map carries the higher trace defects to the first nonreduced point gamma_* and then, through x_*=2gamma_*, to the Jensen constant gamma_*²/2. The bounded-height certificate therefore detects whether the restricted finite divisor equals its reduced divisor.

## Orbital positivity and finite arithmetic separation

Haar conjugation of X maps to its corner eigenvalues on the Gelfand–Tsetlin polytope. Diagonal entries are successive row-trace differences, so Tr(D_mUXU*) is the explicit linear functional Σh_{m,k}(s_k−s_{k−1}). Section concavity and spectral reversal make its density even and unimodal. This exact pushforward, followed by the sinc inequality, gives(m−1)r_m²≥pi². The analytic trace-to-detection map is L_T≥pi/sqrt(D_N), L_J≥1/D_N.

For separation, the map f→(fhat(gamma1)−fhat(gamma2))/sqrt2 is the coordinate contrast of two reduced points. The mean-value Fourier bound on support[-N,N] gives its norm≤|gamma1−gamma2|sqrt(N³/(3alpha_N)). Convexity of the even spectral trace measures the lost coordinate projection. The resulting finite separation inequality and its rational height90 certificate are proved in paper/sections/arithmetic_separation.tex. This is a quantitative map between sampling evaluation and the ideal of the diagonal on a finite pair of points.

## Positive-kernel surgery

The rational replacement multiplies the entire completed function by((s−1/2)²+v²)/((s−1/2)²+u²). At the divisor level it subtracts the reduced pair±u and adds a second copy at±v. In the heat coordinate U=2u,V=2v, the inverse transform of division by1−z²/U² is Ψ_U(x)=U∫_x^∞sin(U(t−x))Phi(t)dt. It solves Ψ_U″+U²Ψ_U=U²Phi and has Ψ_U′(0)=0. Strict kernel monotonicity gives Ψ_U>0 by half-period pairing. The replacement kernel is Phi+(V²/U²−1)Ψ_U, positive even analytic with the stated superexponential tails. Its real-zero times are exactly[0,∞), proved by polynomial heat preservation and the local double-zero splitting. The exact loss of an ordinary absolutely convergent Dirichlet series is witnessed by its nonzero sigma^(−2) term. These identities specify both what the divisor surgery transports and which arithmetic datum it changes.

## New exact maps at checkpoint 3

The theta lift is Theta(psi)(x)=exp(x/2) sum_{n>=1} psi(n exp x), and intertwines d/dx with E=u d/du+1/2. The raw Mellin divisor Mh(s)/[i(s-s_gamma)] maps exactly to Xi(t)/(t-gamma); its nonzero raw u^(-1/2+i gamma) endpoint term is canceled after multiplication by zeta(s). Repeated and paired divisors, their physical tails and exact sampling norms are in theta_kernel_hierarchy.tex. The one-mode coercivity b_L satisfies a1+a2-q(v_L)<=b_L<=a2.

For surviving packets P(w)=product(1+w/x_j(t)^2), convolution maps Toeplitz minors by finite Cauchy-Binet, and reversal maps Jensen polynomials to P(D) E(D) x^N. This yields all three finite-detection index comparisons.

The contour rectangle is 0<Re z<2T, |Im z|<1/4, with z=2 gamma on the endpoint line. The executed spectral and contour certificates share T=20; the contour alone reaches T=45, and the trace certificates reach T=97.632.

The Poisson multiplicity map is P_a(t)=a Re xi'/xi(1/2+a+it)=sum m_gamma a^2/[a^2+(t-gamma)^2]. The prime-ramp map and frequency Cesaro coefficients recover m_gamma/(1/4+gamma^2). Scalar-normalized primitive L-functions of conductors tending to infinity have no nonzero holomorphic local limit at a critical-line point; functional reflection proves the exact obstruction.

## Consolidated finite_detection dictionary
# Exact algebraic dictionary for the finite tests

The constructions below are the explicit morphisms used in these sections. They assign no additional arithmetic or motivic estimate to the analytic formulas.

## Exterior powers, Schur functors and Toeplitz minors

For a finite alphabet beta_1,...,beta_d, let T be the diagonal endomorphism of V=C^d with these eigenvalues. Direct expansion in the exterior basis gives

    det(I+wT) = sum_k Tr(exterior^k T) w^k = product_j(1+beta_j w).

Thus elementary coefficients are the evaluations of exterior-power characters. The representation-ring specialization sends the universal elementary symmetric function e_k to Tr(exterior^k T). Dual Jacobi–Trudi sends every allowed coefficient Toeplitz minor to the corresponding skew Schur character, with the exact row/column index transformation proved in the paper. Direct sums send the determinant polynomial to a product; their exterior-power decomposition proves the coefficient convolution formula. This is the concrete lambda-ring relation: SGA6, ExposéV, Example2.2(b) and Lemma2.2.1 construct exterior-power operations from the filtration of an exact sequence and explicitly include representation rings. The primary text was opened at https://grothendiecksga.com/read/sga6/fr/V-2.html.

For the entire product, finite alphabets converge coefficientwise and on compact sets because the reciprocal parameters are absolutely summable. Every fixed Schur determinant therefore has a well-defined limiting specialization. Its nonnegative real evaluation is the finite positivity property proved here. No integrality of these evaluated real numbers is needed in this morphism.

Archive cote: ours/NEG_NIGHT_analytic/pf_characters.tex and finite_rank_characters.tex explicitly give the exterior-power/SGA6 connection. The paper gives the analytic parameter map beta -> beta/(1-beta) and the exact unitary character expansion, so the coefficient cone is related to an explicit probability mixture of irreducible polynomial representations.

## Finite schemes and the heat weights

A fixed contour with d enclosed zeros gives a monic polynomial P_a through its argument-principle power sums and Newton identities. The quotient C[w]/(P_a) is a length-d finite scheme algebra. Its companion endomorphism has the contour power sums as traces. This proves the passage from contour integration to the finite algebra, without choosing individual roots through a multiple endpoint.

At a zero of multiplicity m, the local analytic algebra over the time ring is finite free of rank m by Weierstrass preparation. Give a=z-time parameter weight2 and z-x weight1; after the base change a=q^2 and the blowup chart z-x=qu, its lowest-weight equation is the Hermite polynomial e^(D_u^2)u^m. The weighted calculation in the Jensen proof adds the principal operator -w0^2 D_u^2/(2N), and the coefficient 4*a*x^2-x^4/(2N) is the exact local comparison. These are filtrations and associated graded equations of the stated finite analytic algebras; their weights are defined by this scaling.

Archive cote: multiplicity_detection_equivalence.tex, orbital_detection_constants.tex and the G039 paragraphs in ours/NEG_NIGHT_paper/checked.tex contain the corresponding finite-algebra and character translations. No Frobenius-weight theorem is an input to the analytic scaling argument.

## Derivative moments as traces and a projector

For a packet polynomial P with zeros x of multiplicity m_x, put A=C[z]/(P). For any analytic observable g on the packet, multiplication by g on A has trace sum_x m_x*g(x): in each local factor C[epsilon]/(epsilon^m), its matrix is triangular with diagonal g(x). Applying this to g=(f')^2 proves that the contour moments are exactly Tr_A(M_g^k). The trace factors through evaluation on the reduced support, because multiplication by a nilpotent has trace zero.

Let B be the reduced algebra of the distinct derivative values: B=R[U]/product_v(U-v). The functional L(h)=sum_v w_v*h(v), with weights inherited from the lengths m_x, is the moment functional. Its Gram form is L(PQ), and its matrix on 1,U,...,U^d is the Hankel moment matrix. The polynomial product_{v>0}(1-U/v) represents in B the idempotent supported at the zero derivative value. Its squared norm and weighted trace are M0, the total length of the multiple-endpoint fibers. This explicitly carries the Christoffel minimum to a finite support projector. The integer threshold2 uses that each nonreduced zero has length at least2.

These trace and evaluation maps are proved here. They identify the finite scheme length being measured. A construction over Spec Z, a correspondence acting on a motivic realization, or a Frobenius estimate reaching the all-height error threshold would require an additional specified object and a compatible comparison map; none is asserted by these finite identities.

## Finite zero surgery as an effective-divisor operation

The rational function R(s)=((s-1/2)^2+v^2)/((s-1/2)^2+u^2) changes the analytic zero divisor by

    [1/2+iv]+[1/2-iv]-[1/2+iu]-[1/2-iu].

Its product with the completed zeta function is entire because the two negative divisor terms cancel certified simple zeros. The exact derivative multiplication formula transports every divergent leading positive absolute moment. The endpoint determinant product cancels one factor and repeats another. The proof also computes the nonzero sigma^(-2) tail that obstructs an ordinary absolutely convergent Dirichlet series for this transformed function. These are the explicit divisor and character-specialization maps used in the information comparison.


## Consolidated spectral_audit dictionary
# Spectral results: exact algebraic translations

These entries identify explicit maps carrying the analytic quantities to algebraic ones. They assert only the stated translations. No attached archive cote has been located for an additional motivic or weight-theoretic realization of the Weil operator; none is supplied here.

## SPEC-PARITY and SPEC-LIMINF: the reduced support and the length at a zero

At an ordinate gamma with multiplicity m, the analytic local algebra of the zero divisor is A_gamma = C{u}/(u^m), u=z−gamma. Its reduction map A_gamma → C sends u to 0. The source has C-dimension m, with basis 1,u,...,u^(m−1); the target has dimension 1. Thus reduction sends the zero scheme of Xi to the divisor with each distinct ordinate once. On any bounded disk avoiding zeros on its boundary, the direct sum of these maps realizes this passage for the whole finite zero scheme.

The proved product limit of the parity theorem is the entire function Delta_Gamma with local zero algebra C{u}/(u), while Xi has local algebra A_gamma. The analytic identity Delta_Gamma=Xi/Xi(0) obtained from the liminf Rayleigh estimate identifies their local principal ideals. Therefore (u)=(u^m) in C{u}, which holds precisely when m=1: for m>1, u is absent from (u^m). This is the exact local-algebra transport of the simplicity conclusion; no arbitrary normalization is used, since evaluation at zero fixes the scalar Xi(0).

## SPEC-PROBE-FIXED and SPEC-ROUNDING: recovering length by a trace weight

The sampling map sends f to the coordinate family (fhat(gamma)) in l²(Gamma,m), with norm squared sum m|fhat(gamma)|². The compact inverse C acts on that Hilbert space by the scalar 1/gamma in its gamma-coordinate. Its coordinate eigenspace has dimension 1, while the norm of the projected probe is m|phihat(gamma)|². Division by the proved nonzero probe factor therefore recovers dim_C A_gamma. This is an explicit equality between a Hilbert-space mass and the length of the local zero algebra, not an inference from the dimension of the eigenspace.

The underlying finite-dimensional C-vector space of A_gamma defines [A_gamma]=m[C] in K_0(C). This follows by the filtration 0⊂(u^(m−1))⊂...⊂(u)⊂A_gamma, whose successive quotients are C. Equivalently the exact forgetful functor from finite-length A_gamma-modules to C-vector spaces sends its Grothendieck class to m[C]. In the usual lambda-ring K_0(C), lambda_t([A_gamma])=(1+t)^m, because the kth exterior power has dimension binomial(m,k). No monoidal structure for tensor product over A_gamma is transported by this forgetful functor; the displayed lambda operations are the exterior powers over C explicitly stated here.

The numerical rounding proof certifies the integer m only after the analytic spectral projection and scalar-division errors total less than 1/2. It consequently certifies this K_0(C) class for the enclosed fixed coordinate. It does not prove a bound uniform over all coordinates.

## SPEC-TRACE-DEFECT: weighted length excess

For a finite set of ordinates, the direct sum of the reduction kernels has dimension sum(m_gamma−1). In the exact trace-defect identity the same nonnegative local lengths occur with weights gamma^(−2). The equality
D_N = ||C−P_NCP_N||_HS² + sum_signed_gamma (m_gamma−1)/gamma²
is proved by matrix-entry orthogonality and the paired Hadamard product. Since every weight is positive, a vanishing limit forces every reduction kernel to be zero. The signed convention doubles the sum over positive ordinates. No estimate making D_N tend to zero has been proved.

## SPEC-PROBE-TENT: an integral norm in a quadratic order

Let R=Z[s]/(s²−2), a finite free rank-two Z-algebra. Multiplication by m−ns in the basis (1,s) is the integer matrix [[m,−2n],[−n,m]], with determinant m²−2n². For a nonzero pair (m,n), this determinant is a nonzero integer, because rational sqrt(2) would otherwise equal m/n; the familiar parity descent proves irrationality. Its absolute value is at least 1. Under the two real embeddings s↦±sqrt(2), this determinant equals (m−sqrt(2)n)(m+sqrt(2)n). This exact norm identity supplies the separation estimate in the two-tent Fourier lower bound. It also identifies the determinant as the finite index of (m−ns)R in R when that quotient is nonzero. The quantitative trigonometric inequality then follows from the two real embeddings and sine concavity, as proved in the paper.

## SPEC-ROUNDING and the local Hankel comparison

The spectral projection calculation uses the eigenvalue separation |gamma^(−1)−eta^(−1)|=|gamma−eta|/|gamma eta|. The contour calculation uses separation of the corresponding closed points in the complex analytic zero divisor. The displayed identity is the precise change of coordinates linking those two separations on a bounded region away from zero. It supplies no additional arithmetic separation estimate. All-height certification still requires quantitative bounds for that separation and for the analytic approximation errors.

## SPEC-TRACE-HEIGHT: certifying reduction on a finite analytic subscheme

Let Z_T be the finite analytic zero scheme for 0<gamma≤T. Its reduction map has kernel of C-dimension E(T)=sum(m_gamma−1), as the direct sum of the local filtrations above shows. The exact trace inequality E(T)≤T²D_N/2 implies this kernel is zero once the right side is below1. This uses the discreteness of length and proves reducedness of Z_T. A certified bound on the global weighted length excess therefore certifies a finite subscheme without choosing an individual isolating circle for each point. The morphism being certified is the direct-sum reduction map already defined; no morphism to an unspecified motive is assumed.

## The exact multiplicity-copy isometry behind the trace defect

Define K=direct_sum_gamma C^(m_gamma), with ordinary Euclidean inner product on each summand, and define I:l²(Gamma,m)→K by I(v)_gamma=(v_gamma,...,v_gamma). Its norm squared is sum_gamma m_gamma|v_gamma|², exactly the original sampling norm. Its image is the closed diagonal subspace D, and the orthogonal projection in each block is the averaging matrix (1/m_gamma) times the all-ones matrix. The orthogonal complement has dimension m_gamma−1 in that block. Let C_full act by gamma^(−1) times identity on each block. Then I C=C_full I exactly; both subspaces D and D-perpendicular are invariant. Consequently tr(C_full²)=sum_signed m_gamma/gamma²=S, tr(C_full² on D)=sum_signed1/gamma², and tr(C_full² on D-perpendicular)=sum_signed(m_gamma−1)/gamma². This explicit isometry and invariant orthogonal decomposition realize the weighted multiplicity excess as a trace. They do not postulate a cohomology theory with these dimensions.

## A published geometric realization for curves

Suzuki, *A spectral theory of zeta functions of function fields*, arXiv:2610.41115v1, Proposition 8.1 and Corollary 8.2 (pp.24–25), Proposition 9.2 and Theorem 9.3 (pp.25–26), give an explicit comparison for a smooth projective curve C/F_q. Put h=log q, F=q^(−1/2)Frob, and E=span_C{F^k}, with Rosati trace inner product tau(XY*). The map U[u](t)=sqrt(h)sum_k u(t+kh)F^k is unitary onto L²((0,h),E), because its inner product expands exactly to the discrete Weil form. It satisfies U exp(ihD) U^(−1)=multiplication by F. Lemma 9.4 (p.26) gives the algebra isometry P(F)↦(P(zeta_1),...,P(zeta_d)), with norm sum_j m_j|P(zeta_j)|²; injectivity follows from the trace norm and surjectivity from Lagrange interpolation. These explicit morphisms provide a geometric instance of the same weighted-coordinate mechanism used above. The theorem is cited for curves; no corresponding zeta-function realization is asserted here.

## Orbital trace and a convex polytope

For a real diagonal matrix X with distinct eigenvalues, the map from its unitary orbit to the spectra of all leading principal corners pushes Haar measure to uniform measure on the Gelfand–Tsetlin polytope (Olshanski, Corollary 3.2). The map to the orbital random variable is exactly

\[
(y^{(1)},\ldots,y^{(m-1)})\longmapsto
\sum_{k=1}^{m}h_{m,k}\left(\sum_jy_j^{(k)}-\sum_jy_j^{(k-1)}\right).
\]

The row sums are traces of principal corners, so their successive differences equal matrix diagonal entries. This proves that the orbital measure used in the Hermite detection constant is the linear pushforward of an explicit convex-polytope measure. Symmetry and Brunn–Minkowski give a symmetric unimodal density. The uniform-mixture formula and the proved sinc minorant then give (m−1)r_m²≥π². Through the exact signed trace identity D_N≥2(m_gamma−1)/gamma², this carries finite compression data to L_Toeplitz≥π/sqrt(D_N) and L_Jensen≥1/D_N. This is a measure-theoretic pushforward of the representation-theoretic interlacing polytope; no scheme, motive, or lambda-ring realization beyond the exact maps just displayed is asserted.

## Exact finite-dimensional lower certificate

The geometric explicit formula realizes the local form as a rank-two pole term plus a Fourier multiplier. Cutting at T where the multiplier exceeds b gives the form inequality q>=bI+B_T. The orthogonal Legendre projection P_N is the displayed finite-dimensional morphism; its head is bI+P_NB_TP_N, its tail and mixed block have the explicitly proved bounds c and z. Excluding one lowest head eigenvector carries the full second minmax problem to the quadratic form [[a,-z],[-z,c]], where a is the second head eigenvalue. This is the exact morphism behind the finite inertia certificate. All entries are finite prime-power sums and bounded-interval archimedean integrals; no identification with a geometric motive or a Grothendieck-group rank is asserted. The still-open input is the stated asymptotic lower inequality for these arithmetic matrices, with the exponent map beta=9+alpha proved separately.

## Executed arithmetic local projection and packet coverage

The coefficient map x↦Σ_j x_j b_j from C^126 into the window space carries the q metric to G and the primitive metric to J. For H=−iB and x=a+ib, its exact Rayleigh numerator is2a^T B b, its primitive squared norm is a^T J a+b^T J b, and the probe functional is x* c. These identities give the residual and mass used in the certificate. The completed moment S7/2=Σ_positive m_j λ_j^14 and the same Rayleigh value μ give b7=(S7/2−μ14)^(1/14), which bounds every positive eigenvalue except the largest. The exact inequality μ>1/20>b7 identifies the entire finite positive packet through height20. The full signed gap exceeds μ−b7>9/400, so the residual vector determines its rank-one coordinate projection with norm error below0.018022. Dividing that projection mass by the explicit probe transform gives an integer interval contained in(1/2,3/2). All numerical maps in this chain are finite arithmetic Weil pairings or completed derivatives atzero; the final certificate has no indexed-zero input. The moment inequality also proves the first multiplicity directly, and this logical overlap is stated in the paper.


## Theta division and the exact one-mode restriction

The map Theta(psi)(x)=exp(x/2) sum_{n>=1} psi(n exp x) intertwines the Euler operator E=u d/du+1/2 with physical differentiation. At each actual ordinate gamma, the raw first-order inverse psi_gamma(u)=−i u^(−s_gamma) integral_u^infinity h(v)v^(s_gamma−1)dv has theta image R_gamma K, where (−i d/dx−gamma)R_gamma K=K and its Fourier transform is Xi(t)/(t−gamma). The raw Mellin multiplier 1/[i(s−s_gamma)] and the paired multiplier 1/[−(s−1/2)^2−gamma^2] identify the exact division morphisms. The nonzero raw endpoint coefficient produces a u^(−1/2+i gamma) term, whereas the theta image has two Gaussian tails because Xi(gamma)=0. The paper proves both facts directly, including their constants. Repeated paired division has zero sampling norm through order m_gamma−1 and the explicit positive terminal norm at order m_gamma.

The physical orthogonal restriction to v_L^perpendicular has bottom value b_L. The exact comparison a1+a2−q(v_L)<=b_L<=a2 follows from the two-dimensional Ky Fan inequality and intersection with the first two eigenspaces. Thus this particular codimension-one restriction differs from the actual second eigenvalue by at most the already bounded trial energy. The raw endpoint estimates and the direct cutoff bounds do not prove the remaining lower estimate for that restriction.

## Quantitative arithmetic inertia and uniform sampling

For each window, the coefficient map from the dyadic mean-zero tent basis to the Weil Hilbert space carries the quadratic form q((TC−I)f,f) exactly to the Hermitian matrix TH_N−G_N. A positive subspace of dimension M therefore gives M positive eigenvalues of that arithmetic matrix. The occurrence graph first supplies mutually separated distinct coordinates; their multiplicity weights are retained in the sampling identity and help its positive part. The constructed modulated-tent map and its mean-corrected dyadic interpolant preserve positivity, giving the quantitative count (d_MT−eta)n(T) with N=ceil(A_eta logT). No map from this distinct-coordinate count to the same fraction of simple zeros is asserted.

The uniform cosine-weight pair calculation yields a global h-separated subset Gamma_h with a proved lower count in every interval. Hall matching maps an oversampled grid injectively into this subset with bounded displacement. Dilation then puts the matched samples within Voss's exact Paley–Wiener theorem. The final physical map is F(x)=fhat(pi x/L), with ||F||²=2L||f||² and sample points x=L gamma/pi. Thus the sampling lower constant is a lower bound for the same actual Weil Rayleigh quotient, with no model replacement. The exact scale is mu=exp(2L)=lambda² and p_MT=1/d_MT; the proved exponent is C mu^p_MT log(mu)(1+loglog(mu)). This all-window bound is weaker than the exponential exp(−4pi mu) required by the prolate ratio, as shown by substituting the two exponents into the ratio bound.

## The integer inertia defect as a length defect

At a fixed zero-free height T, the finite zero algebra is A_T=direct_sum_{0<gamma<T} C[u]/(u^{m_gamma}). Its reduced algebra is B_T=direct_sum C, and the reduction A_T→B_T has kernel of dimension n(T)−n_dist(T). The positive spectral subspace 1_{(1/T,infinity)}(C)H is canonically the coordinate space of B_T, by the sampling map f↦(sqrt(m_gamma)fhat(gamma)). The coefficient map from the dyadic hat basis transports q((TC−I)f,f) exactly to TH_N−G_N. Its positive inertia increases to dim B_T, while dim A_T remains n(T). Consequently the limiting integer deficit is precisely the length of the reduction kernel.

The layer-cake identity lambda^{2k}=2k integral_{1/lambda}^infinity t^{−2k−1}dt, applied to the paired reciprocal roots and to the parity-paired compression eigenvalues, gives D_N,k=4k integral_0^infinity (n(t)−iota_N(t))t^{−2k−1}dt. This is the exact integral transporting integer lengths to trace weights. The four-evaluation change for divisor replacement −[u]−[−u]+[v]+[−v] gives two positive and two negative rank-one corrections to TH_N−G_N atT>v. Its finite inertia changes by at most2; its eventual integer length deficit increases by1. The same replacement preserves the proved fractional rank lower bound.

For the finite spectral multiplicity-copy space with endomorphism C_full already defined above, the determinant identity det(1−zC_full)=sum_j(−z)^j Tr(exterior^j C_full) realizes the trace powers as the ghost components −k[z^k]log det(1−zC_full). Restriction to the diagonal reduced-support subspace gives the corresponding reduced determinant. Subtraction of their ghost components is the weighted length excess. These identities follow by multiplying the eigenvalue factors, and so give the precise lambda-operation map on every finite packet.

## The double cover of the phase circle

The quotient map R/2Z→R/Z sends y mod2 to y mod1; its kernel is the two-element group generated by1. Its pullback sends the integer character exp(2pi i ell y) to the even character on the double cover. Let G be a standard Gaussian and U uniform on(0,1), independently, and put X_sigma=2floor(sigma G/2)+U. Then |X_sigma−sigma G|≤2. Expansion of every power proves convergence of all normalized moments to the Gaussian moments, and integration in U kills every nonzero pulled-back character even after a fixed normalized moment is inserted, up to terms tending tozero. The sign sin(pi X_sigma) is positive with probabilityone. Replacing U byU+1 preserves the pushforward to R/Z and changes the sign everywhere. This gives the exact measure pushforward underlying the phase-information calculation.

The odd sine characters on R/2Z are multiplied by−1 under the nontrivial deck transformation. The finite Abel inequality in the paper bounds the sign average using those odd characters and the mass near integer phases. Thus the missing arithmetic data are specified on this cover rather than inferred from the Gaussian scaling limit.

## A primitive finite-field character under constant-field extension

Let `q=3` or `9`, let `eta` be the nontrivial quadratic character of `F_q`, extended by zero at zero, and put

\[
f(t)=t(t-1)(t+1),\qquad
\chi(A)=\eta(A(0)A(1)A(-1)).
\]

The Chinese remainder isomorphism identifies the unit group modulo `f` with three copies of `F_q^*`. On it, the character is the product of three nontrivial characters. It cannot factor through a proper divisor of the squarefree modulus: omitting any one local factor would make the character independent of that coordinate, whereas varying that coordinate between a square and a nonsquare changes its value. Its conductor is therefore exactly `f`.

Complete multiplicativity and unique factorization of monic polynomials give, as formal power series,

\[
L_\chi(u)=\sum_{A\text{ monic}}\chi(A)u^{\deg A}
=\prod_{P\text{ monic irreducible}}
(1-\chi(P)u^{\deg P})^{-1}.
\]

For every degree `n>=3`, each residue class modulo `f` has exactly `q^{n-3}` monic representatives of degree `n`. The complete residue character sum equals

\[
\sum_{a,b,c\in\mathbb F_q}\eta(abc)
=\left(\sum_{a\in\mathbb F_q}\eta(a)\right)^3=0.
\]

Thus the Euler-product series is a polynomial of degree at most two. Its constant coefficient is one. The linear coefficient is

\[
c_1=\sum_{b\in\mathbb F_q}\eta(b^3-b).
\]

For `q=3`, every summand is zero. For `q=9`, write `b=a+ci`, with `a,c in F_3` and `i^2=-1`. In characteristic three,

\[
b^3-b=ci.
\]

Both `i` and `-i` are squares in `F_9`, since their fourth powers are one. The three values with `c=0` contribute zero and the six values with `c!=0` contribute one. Hence `c_1=6`.

For a monic quadratic `t^2+bt+c`, its three evaluations have product `c((1+c)^2-b^2)`. The elementary quadratic-character sum

\[
\sum_{b\in\mathbb F_q}\eta(d-b^2)
=\eta(-1)\left(q\mathbf1_{d=0}-1\right)
\]

follows from counting the solutions to `x^2=b^2-d`: when `d!=0`, the factorization `(b-x)(b+x)=d` gives exactly `q-1` solutions, and the character sum is `-1` before the factor `eta(-1)`; when `d=0`, it is immediate. It follows that

\[
\begin{split}
c_2
&=\eta(-1)\sum_c\eta(c)
       \left(q\mathbf1_{c=-1}-1\right)\\
&=q\eta(-1)^2=q.
\end{split}
\]

Consequently

\[
L_{\chi,\mathbb F_3}(u)=1+3u^2,
\qquad
L_{\chi,\mathbb F_9}(u)=1+6u+9u^2=(1+3u)^2.
\]

This proves the primitive-character, genuine Euler-product and repeated-root claims without a geometric input.

For the exact geometric map, the smooth projective model of `y^2=x^3-x` has one point at infinity and is a double cover of `P^1` by the `x` coordinate. Its affine equation is smooth because the derivative of `x^3-x` is `-1`; its Weierstrass discriminant is `64`, nonzero in characteristic three. Its point count is

\[
\#E(\mathbb F_q)=q+1+\sum_{x\in\mathbb F_q}\eta(x^3-x)=q+1+c_1.
\]

There is a normalization issue in identifying the local characters, which the exact resultant map resolves. For a monic irreducible polynomial `P` of degree `r`, the defined character is `eta(Res(f,P))`. The double-cover character is `eta(Res(P,f))`, equivalently the quadratic character of `f` evaluated at a root of `P` in `F_{q^r}`. The resultant identity gives

\[
\chi(P)=\eta(-1)^r\chi_{\rm cover}(P).
\]

Thus over `F_3` the defined character is the constant quadratic twist of the cover character, and `L_chi,3(u)=L_cover,3(-u)`. Over `F_9` the characters agree. The standard elliptic-curve Frobenius identity gives `L_cover,3(u)=1+3u^2` from the point count `#E(F_3)=4`, so the degree-three polynomial's constant twist has the same polynomial in this example. Over `F_9`, the point count `#E(F_9)=16` gives `L_cover,9(u)=(1+3u)^2` directly.

Under extension from `F_3` to `F_9`, Frobenius becomes its square, and the constant quadratic twist disappears. The two reciprocal roots over `F_3` are `+i sqrt(3)` and `-i sqrt(3)`; both square to `-3`. Therefore their precise base-change image is the double reciprocal root of `(1+3u)^2`. The only external geometric ingredient in this last identification is the standard Frobenius/point-count identity, not the elementary character computation. An author-hosted reference is J. S. Milne, *Elliptic Curves*, second edition, Chapter IV, Section 9, Theorem 9.10 and Remark 9.11, printed pp.156--157, https://www.jmilne.org/math/Books/EC2.pdf. Theorem 9.10 states the exact zeta numerator `1+(#E(F_p)-p-1)u+pu^2`; the same section explains the extension-field point counts.

The comparison concerns the explicitly constructed finite-field character and its constant-field extension. No implication from this example to the multiplicities of the number-field zeta function is asserted.


The character's constant-field map can also be written without a choice of reciprocal roots. For A∈F_9[t], let A^(3) denote coefficientwise cubing and put Norm(A)=A A^(3)∈F_3[t]. For z∈F_9, eta_9(z)=eta_3(z^4)=eta_3(Norm(z)), includingzero. Evaluating Norm(A) at0,1,−1 gives chi_9(A)=chi_3(Norm(A)). This proves the exact norm pullback of the primitive character.

On a rational two-dimensional space the matrix F=[[0,−3],[1,0]] satisfies F²=−3I. Direct determinants give det(I−uF)=1+3u² and det(I−uF²)=(1+3u)². For the elliptic curve the standard Frobenius identity identifies its characteristic polynomial with the first determinant; Cayley–Hamilton gives the same square relation. The constant twist overF_3 changesF to−F, whose square isagain−3I. The second Adams operation on the eigenvalue character squares both eigenvalues, and the exterior-power determinant records their coincidence. Both original eigenvalues have modulus sqrt3; both squared eigenvalues have modulus3=sqrt9. These equalities preserve the respective weight-one absolute values while producing the repeated reciprocal root by the explicit squaring map.

The function-field variable u=q^{−s} maps the repeated root u=−1/3 forq=9 to s=1/2+(2k+1)pi i/log9, k∈Z, each of multiplicitytwo. The primitivity, Euler product, point-count numerator, weight absolute values and repetition have therefore been checked in one concrete example. The arithmetic question for the Riemann divisor continues to be the zero length defect specified above; this example supplies the stated geometric comparison and no unproved transfer of its multiplicities.


## Exact Möbius and normalized-Mertens transport

For compact smooth f, the finite arithmetic map Mf(u)=sum mu_M(n)(nu)^(-1/2)f(log(nu)) is the pointwise inverse of the theta summation. Its Mellin transform is exactly F(i(s−1/2))/zeta(s). The direct fixed-halfstrip contour proof extends this equality and physical Plancherel to every positive critical shift. At a pole with surviving order r=m−ord_gamma F, the normalized local square integral has coefficient Gamma(r−1/2)/(2sqrt(pi)Gamma(r)) times the squared Laurent coefficient; completion and every derivative factor are displayed in the paper.

With m(y)=exp(−y/2)M(exp y), the physical endpoint function exp(−Y/2)Mf(exp(−Y)) is exactly the convolution integral m(Y+z)(f(z)/2−fprime(z))dz. This is the explicit morphism to the classical weak-Mertens mean-square mechanism. The fixed-shift estimates retain their epsilon-dependent constants; no uniform first-order Abel bound is supplied. The divided theta functions use the separate pointwise inverse and local Abel identities, with their noncompact physical domain stated explicitly.


## Coprime, Nyman and local-jet comparison maps

For Re epsilon>1/2 the weighted physical Möbius norm is A_epsilon= zeta(1+2epsilon) R_epsilon / zeta(2+4epsilon). The map n=da,m=db with gcd(a,b)=1 gives mu(da)mu(db)=mu(a)mu(b)mu(d)^2 1_{gcd(d,ab)=1}. Summation over d produces the exact Euler correction product over p dividing ab of (1+p^(-1-2epsilon))^(-1). The proved smoothed physical bound extends A holomorphically to Re epsilon>0; R in that half-plane means the displayed analytic quotient, without an assertion of ordinary coprime-series convergence there. Near a surviving Mellin pole of order r, the local lower mass transfers through zeta(2+4epsilon)/zeta(1+2epsilon)~2 zeta(2)epsilon to the displayed order epsilon^(2-2r) in R.

For theta_n(x)={1/(nx)}, Mellin(theta_n)(s)=−n^(−s)zeta(s)/s. Thus chi_(0,1)+sum a_n theta_n maps exactly to [1−zeta(s)D_N(s)]/s. The finite Gram minimum is 1−b^T G^(−1)b with b_n=(1−gamma_E+log n)/n. Burnol's larger continuous parameter space contains the discrete points1/n, so its lower bound transfers in the stated direction. The squared-multiplicity sum splits exactly as C0+sum m(m−1)/|rho|². The source upper estimate discussed in the paper has an input already containing simplicity, and no use of it without that input is made.

The half-value sawtooth B is1−2{x} away from integers and0 at integers. Its period sum at h/k is zero. Pairing residue classes proves g_B(h/k)=−pi V(h,k)/k for coprime h,k. Substitution u=1/(hx) gives G_hk=h^(−1) A(h/k), converting the classical BBLS autocorrelation formula to the exact Gram identity. For h=da,k=db, the physical change y=dx gives G_da,db=d^(−1)G_ab, and every term of the g_B formula has the same scaling. Its symmetric arithmetic contribution is exactly sum a_h a_k g_B(h/k)/h. For the stated Möbius weights this is the signed two-variable sum printed in the paper. The cited long-numerator range maps to h>=k² and its transpose to k>=h²; comparable compact-correlation pairs above e^(2L) lie in h<k²,k<h². The required estimate in that region remains open.

The unitary map Jf(x)=e^(x/2)f(e^x) converts Mellin values at1/2−i nu to Fourier values at nu. Burnol's V becomes the unit-modulus multiplier v(1/2−i nu). For a fixed ordinate and fixed jet orders, normalized local jets have physical Gram limit1/(j+k+1), whereas their leading Weil Gram is R m_gamma/((j+1)(k+1)). A coefficient vector orthogonal to (1,1/2,1/3,...) cancels this leading value coordinate. The resulting q norm is O(1/R), while its physical norm tends to the positive polynomial integral. The further exact comparison JX_k=R^(−k−1/2)(−x)^k exp(i gamma x)1_[−R,0]+O_L2(R^(−1/2)) proves the stated window-mass law. A uniform q bound on the discarded physical tail is still required.


## Finite algebra models for the new endpoint comparisons

The common-divisor Euler factor has an exact exterior-power interpretation at each prime. On a one-dimensional space E let the formal weight be u=p^(−1−2epsilon). Then sum_j mu(p^j)^2 u^j=1+u=det(1+u Id_E)=lambda_u(E). Requiring p not to divide the common divisor removes the positive-degree term; division by1+u is precisely the correction in the coprime factor. Multiplication over primes gives zeta(1+2epsilon)/zeta(2+4epsilon) in the proved absolute half-plane. This uses the exterior character identity already proved above; the analytic continuation is the separate quotient identity in the paper. No archive cote beyond that already stated for exterior operations is assigned to this new calculation.

For each finite N, the map a in C^N to sum a_n theta_n pulls the physical Hermitian form back to the matrix G. The augmentation a to chi+sum a_n theta_n has norm1+2 Re(b* a)+a*Ga. Completing the square is the exact affine translation a to a+G^(−1)b; its constant is1−b*G^(−1)b. Written in real and imaginary coordinates this is an affine morphism over Spec R and an identity of quadratic polynomials. The sawtooth formula computes the entries of this same pulled-back form, and the dilation x to dx multiplies it by d^(−1). The sign change c=−b is the displayed linear automorphism of its coefficient vector.

A concrete finite-algebra model of the local-jet comparison is obtained as follows. Let A_r=C[epsilon]/(epsilon^r), and identify its vector space with polynomials in t of degree below r by the invertible linear map T(1)=1 and T(epsilon^k)=t^k−1/(k+1) for1<=k<r. The functional ell(P)=integral_0^1 P(t)dt obeys ell(Ta)=a(0). Equip the polynomial vector space with the transported product (Ta) star (Tb)=T(ab modulo epsilon^r). Then ell is exactly the quotient algebra morphism A_r to C in these coordinates, and its kernel is the transported nilpotent ideal. This explicitly defines the multiplication being used. The positive physical form is the pullback of integral P(t)conj(Q(t))dt; the leading Weil form is the rank-one pullback m_gamma ell(P)conj(ell(Q)). The matrix limits proved in the paper give precisely these two forms. The physical window at L/R=eta replaces the Hilbert matrix entry1/(j+k+1) by eta^(j+k+1)/(j+k+1), an explicit polynomial Gram matrix in eta. The statement about L=o(R) follows from its entries tending to zero and the proved norm error. These finite-algebra and quadratic-form maps assign no additional uniform estimate to the discarded Weil tail.


## Removing certified reduced components

The finite-deflation research attempt has an exact length map. Chinese remainder decomposition of a finite zero algebra gives A=A_S times A_rem. For a certified simple set S, A_S is reduced, so its length contributes equally to A and A_red and cancels from their difference. In the Weil realization this is the removal of the same signed unit coordinate lines; the reciprocal-power divisor trace and ordinary trace both decrease by2 sum_(gamma in S)gamma^(−2k). Their difference is unchanged. The finite Gram and primitive matrices change by the displayed evaluation rank-one forms in drafts/root/finite_deflation_attempt.md. The growing-set cross-term estimate needed for an iteration was not proved.


## Boundary divisor, conductor minorant, and finite deletion maps

For F=Xi and E=F+iF', put G=product_(gamma>0)(1-z²/gamma²)^(m_gamma-1). Multiplication by G is the exact norm-preserving map H((F+iF')/G)->H(E); its inverse cancels the common real divisor forced by boundary square integrability. The kernel transforms by K_E(w,z)=G(z)conj(G(w))K_(E/G)(w,z). The model inner function Theta=E#/E is unchanged by that cancellation, and Theta'(gamma)=-2i/m_gamma. Hence its Clark atom is pi m_gamma and the inverse multiplication trace excess is sum (2/|Theta'(gamma)|-1)/gamma^(2k). The weighted sampling unitary sends Fourier evaluation at gamma to (m_gamma-1)-st derivative evaluation by (Uh)^(m-1)(gamma)=i F^(m)(gamma) hhat(gamma)/sqrt(pi). The coordinate remains one-dimensional, while its entire-function image has the displayed vanishing order. For the imaginary shift E_omega=F(z+i omega), its diagonal at gamma is m|c_gamma|² omega^(2m-1)/pi times1+O(omega²). Thus the unresolved linear boundary margin retains exactly the multiplicity question.

The conductor minorant is h(t)=(1-((t-t0)/r)²)sinc^4((t-t0)/r), bounded above by the strict interval indicator. Its integral pi r/6 converts the conductor coefficient log(q/pi)/(2pi) in the explicit formula to (r/12)log q. Fourier support[-4/r,4/r] leaves finitely many prime terms, independently of q. Multiplication by a zero-free holomorphic factor preserves the local zero divisor. Rouche transports local uniform convergence to equality of finite divisor lengths on a disk, which contradicts the growing local lower count for a nonzero limit on the component containing the critical-line point.

Deleting finitely many certified simple signed coordinates is the orthogonal projection of the weighted sampling space onto their complement. The evaluation row e_u gives exactly the rank-one Gram subtraction e_u*e_u and reciprocal-form subtraction u^(-1)e_u*e_u. Since each removed zero has m=1, its contribution cancels equally from the counted logarithmic trace and the distinct spectral trace. In a bounded zero algebra the same operation is the Chinese-remainder splitting off of reduced length-one factors; length(A)-length(A_red) is unchanged. No estimate for a growing remainder's arithmetic cross terms is supplied by this identity.

## Coupled cutoff and endpoint-jet maps

For M>=1 the algebra map C[t] -> C[t]/(t^M) times C[t]/((t-1)^M) is surjective by the Chinese remainder theorem; its kernel is (t^M(t-1)^M). Thus the two endpoint vanishing conditions are precisely membership in that ideal. At zero the leading coefficient a is the image in the one-dimensional graded piece (t^M)/(t^(M+1)). The physical rescaling t -> (L/R)t acts on that piece by (L/R)^M. The condition integral_0^1 P=0 is separately a linear functional on the fixed polynomial vector space; no multiplicative property of this integral is assumed. For M=0 the endpoint conditions impose no vanishing and a=P(0).

The exact Mellin-to-Fourier unitary and Burnol multiplier give both endpoint sums in equation burnol-endpoint-transform. The derivatives at one cancel the low orders of the translated multiplier term; those at zero cancel the low orders of the unshifted rational term. The quotient-symbol at zero then contributes a A_(chi,M)L^(M+1)/R^(M+1/2) to Fourier evaluation at gamma. The squared Weil norm has coefficient m_gamma|a|^2 A^2, while the physical squared norm has coefficient |a|^2 B and one fewer power of L. Their ratio is therefore asymptotic to m_gamma(A^2/B)L. The sampling unitary carries this coordinate to the global derivative evaluation (Uh)^(m-1)(gamma)=i F^(m)(gamma) hhat(gamma)/sqrt(pi). These are exact quotient, linear, and Hilbert-space maps; no additional motivic or weight theorem is inferred.

The inverse multiplier kernel on x>0 is obtained by shifting s from real part1/2 to5/2. The rational summand has inverse support x<=0; the remaining integral and its first derivative have absolute majorants. Multiplication by exp(iR(nu-gamma)) translates the physical kernel to exp(-iRgamma)kappa(x+R). This exact direction gives the exponential local error on |x|<=L<=R/2. It is compatible with the larger cutoff sampling term because that term comes from the polynomial's nonzero endpoint symbol. The uniform-height and growing-number-of-jets gate remains open.

The primitive Gauss identity is the finite Fourier orthogonality identity |tau(chi)|^2=q. Its exact q^(-1/2) outer scalar multiplies the two Perron error forms; the resulting bounds are sqrt(qT)y and sqrt(T)y, with the other explicit errors inside sqrt(qT)y for q<=T. This sharpens a bound already used in the analytic proof without altering the established conductor range.

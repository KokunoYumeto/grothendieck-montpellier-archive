# THETA3 quantitative arguments (root working record)

Run THETA3-20261121. Author: GPT-6 Astra Pro; reasoning-effort setting not exposed.
All arguments below are new formulations for this comparison; no claim of research priority is made.

## THETA3-Q1. A quantitative fixed-input period

Fix the compact surface X, the total finite input, and all constant-line trivializations in 032 Proposition 4.6. Let H=L²(X,K_X), with norm defined so that for holomorphic top forms ||xi||²=int_X xi wedge conjugate(xi). Let xi=Xi(t0) be nonzero and let xi'=Xi(t). If ||xi'-xi|| <= eta ||xi|| for 0<=eta<1, then

    |int_X xi wedge conjugate(xi')| >= (1-eta)||xi||².

Proof: the difference from ||xi||² is the Hermitian pairing (xi,xi'-xi); apply Cauchy–Schwarz and the reverse triangle inequality. The same inequality applies to smooth (2,0)-forms along the intermediate parameter path, using the L² Hermitian pairing. Holomorphy is needed only at the endpoints to identify the cohomology classes. If t lies in a convex coordinate neighborhood and ||D Xi||_op <= L there, then ||xi'-xi|| <= L||t-t0|| by integrating the derivative on the line segment. Thus ||t-t0|| <= eta sqrt(A)/L suffices when A=||xi||²; if L=0 the assertion is immediate. If only A>=A0>0 and A<=A1 are certified, one may require ||xi'-xi||<=eta sqrt(A0), giving the same fractional bound.

On a finite étale cover pi:Y->X of degree d, the unnormalized period and the squared norm are multiplied by d. If pi*xi=sum_r a_r alpha_r wedge beta_r and pi*xi'=sum_s b_s gamma_s wedge delta_s, put S=(sum|a_r|)(sum|b_s|). Nonzero xi implies S>0 for any such expansion. At least one individual four-form period has absolute value >= d(1-eta)||xi||²/S, by the triangle inequality applied to the finite double sum.

This is a quantitative refinement of 032 Corollary 4.7, not a conductor bound: A, L, the rational decomposition and S must be supplied or bounded. Root whole-proof rereading: passed; independent check requested.

## THETA3-Q2. Explicit lattice tail for the first theta tensor

Let Lambda in R^d be a full lattice with minimum nonzero norm >=rho>0, and let the imaginary part of the period matrix satisfy Im Z >=lambda I, lambda>0. For x0 in Lambda nonzero and integer k>=2||x0||/rho, the first theta tensor on x0+kLambda differs from its x0 term by a vector of norm at most

    E(k) = 2 sqrt(pi/(e lambda)) sum_{j>=1} (2j+3)^d exp(-b j²),
    b = pi lambda k² rho²/8.

Proof: if m!=0 then ||x0+km||>=k||m||/2. The summand norm is at most 2pi r exp(-pi lambda r²), r=||x0+km||. Since r exp(-pi lambda r²/2)<=1/sqrt(pi e lambda), it is at most 2sqrt(pi/(e lambda))exp(-pi lambda k²||m||²/8). Points of Lambda are rho-separated. The disjoint balls of radius rho/2 centered at points with jrho<=||m||<(j+1)rho lie in a ball of radius (j+3/2)rho; hence their number is at most (2j+3)^d. Sum over shells. No lattice covolume bound is required.

This bound is numerically certifiable: f_j=(2j+3)^d exp(-bj²) has successive ratio <=q_J=((2J+5)/(2J+3))^d exp(-b(2J+1)) for j>=J. If q_J<1, the tail beginning with J is <=f_J/(1-q_J). Choose any J with q_J<1 and sum the earlier finite terms.

For a projected gradient P T1, multiply E(k) by ||P||. To select two non-collinear projected gradients u,v, let u0,v0 be their limiting leading terms with |u0 wedge v0|=Delta>0. If errors are bounded by e1,e2, then

    |u wedge v-u0 wedge v0| <=e1||v0||+e2||u0||+e1e2.

An error smaller than Delta certifies nonvanishing. This gives a finite numerical stopping condition for the input choice in 032 Proposition 4.5; it does not bound the final arithmetic cycle degree.

Root whole-proof rereading: passed; independent check requested. The factor 2pi and minimum-norm dimension d are in the actual rational Minkowski position space.

## THETA3-Q3. Rational approximation with an explicit denominator

Fix an integral Q-basis of the number field E, and express W(E) of E-dimension2 in that basis. The diagonal real embedding identifies W(E tensor_Q R) with R^D, D=2[E:Q]. Let B be the invertible real embedding matrix from the chosen Q-coordinates. For any prescribed archimedean vector u and any integer N>=1, round each coordinate of N B^{-1}u to the nearest integer to obtain a in Z^D. Then w=B a/N belongs to W(E) and

    ||w-u|| <= ||B|| sqrt(D)/(2N).

Proof: each rounded coordinate has error at most 1/2; apply the Euclidean norm and the operator norm of B.

At a chosen place, write the Hermitian matrix as H, with ||H||=h, target vector u of norm <=U, and |u*Hu|>=eta>0. Suppose epsilon=||w-u||<=1 and h(2U+1)epsilon<=eta/2. Then |w*Hw|>=eta/2, so its sign agrees with that of u*Hu. The orthogonal projectors P(w)=w(w*H)/(w*Hw) and P(u) satisfy

    ||P(w)-P(u)|| <= [2h(2U+1)/eta] [1+hU²/eta] epsilon.

Proof: numerator and denominator differences have norms at most h(2Uepsilon+epsilon²). Use P(w)-P(u)=(N(w)-N(u))/q(w)+N(u)(q(u)-q(w))/(q(w)q(u)), where ||N(u)||<=hU². This proves the displayed bound. Apply at all real places. The prescribed signed-line domain remains unchanged, and the orthogonal complementary line varies with the same bound. An explicit N therefore places the rational endpoint in any prescribed projector neighborhood. This is the finite weak-approximation step used in 032 Corollary 4.7 with an explicit denominator relative to a specified field basis and target vectors. It is deliberately not a uniform arithmetic complexity result.

Root whole-proof rereading: passed; independent check requested.

## THETA3-Q4. Quantitative zero-orbit nonvanishing

Notation as in vHS Lemma4.2.7; all [G] and unipotent-quotient measures have mass1. Let Phi=Phi_infty tensor Phi_f with Phi_f(0)=1 and a=Phi_infty(0)!=0. Let T(h) be its theta integral on the doubled unitary group. The constant-term identity gives int_[N]T(n)dn=a. Then for every epsilon in (0,1), there exists h_f in N(A_f) such that

    |I_{Phi_infty}(omega_f(h_f)Phi_f)| >= (1-epsilon)|a|,
    ||omega_f(h_f)Phi_f||_2=||Phi_f||_2.

Proof: [N] is compact; T is continuous. Hence |a|<=max_[N]|T|. Choose a representative n=(n_infty,n_f) of a maximizing point. Weak approximation gives gamma_j in N(F) tending to n_infty at infinity. Left N(F)-automorphy gives T(gamma_j,infty,n_f)=T(1,gamma_j,f^{-1}n_f). Continuity makes the latter tend to T(n), so the inequality holds for some j. The commuting Weil actions identify this value with the displayed I; Weil unitarity proves the norm identity.

The theta032 agent independently read this whole proof and confirmed it. A direct proof using the Siegel unipotent N=Herm_2(E) is being supplied by that agent: the averaging kills all Gram matrices other than0, and anisotropy of V leaves only x=0. This avoids an appeal to iterated full-flag constant terms. The argument also works on totally definite V with the same zero-value normalization.

This lower bound permits a finite-adelic translate, hence a varying finite level. It does not assert that a fixed unaveraged period has this lower bound, nor that the translating element has bounded denominator.

## THETA3-Q5. Loss when extracting a fourfold theta period

Let a total finite input after the doubling intertwiner have a specified finite decomposition sum_a c_a tensor_{i=1}^4 phi_{i,a}. Let the corresponding i-th unintegrated theta form for term a have a finite automorphic-character expansion with at most N_{i,a} permitted terms (vHS Lemma4.2.10); zero coefficients may be retained in this count. The normalized total period is then a sum of individual integrated fourfold periods P_{a,j1,j2,j3,j4}, with coefficients c_a. Put

    S=sum_a |c_a| product_i N_{i,a}.

If the total period has absolute value >=b>0, then S>0 and at least one constituent period has absolute value >=b/S.

Proof: expand the finite products and apply |sum c_a P|<=S max|P|. Complex conjugation on the last two factors conjugates the relevant scalar coefficients and does not change absolute values. The measure conversion C_K of vHS §4.2.8 multiplies the unnormalized geometric period by its known positive factor; it must be retained if using actual integrals over Sh_K instead of the probability-normalized adelic integral.

Each N_{i,a} is computable from the finite compact torus quotient at the common finite stabilizer, with the specified archimedean character: at most the order of that quotient. No uniform bound for S or for that quotient is asserted.

## THETA3-Q6. Local Gaussian determinant and normalization

On C^2 use the probability Gaussian dgamma(z)=pi^{-2} exp(-||z||²)dz. For u,v in C² put l_u(z)=sum u_i z_i and, on two independent copies z,w, P_{u,v}=l_u(z)l_v(w)-l_v(z)l_u(w). Then

    ||P_{u,v}||²_{L²(dgamma(z)dgamma(w))}=2 det [[||u||²,<u,v>],[<v,u>,||v||²]].

Proof: E[z_i conjugate(z_j)]=delta_ij. The two diagonal terms of |P|² each integrate to ||u||²||v||²; the two mixed terms each integrate to |<u,v>|², with negative sign. This proves the formula. In particular for orthonormal u,v, P/sqrt2 has norm1. The standard unitary Bargmann transform transfers this normalization to a Schwartz vector; the doubling intertwiner identity delta(f tensor conjugate f)(0)=||f||² then gives value1. Normalize every remaining compact Gaussian to norm1. This describes an explicit local tensor normalization, not the unmodified numerical normalization of any cited paper.

In the q=1, p=2 polynomial Fock cocycles (published BMM Prop5.17(1)-(3)), the coefficient of the wedge of two holomorphic one-form cocycles has this determinant shape, with separate oscillator variables for the two multiplicity lines. A claim identifying numerical a0=1 in the global period requires retaining the chosen Bargmann, volume and constant-line conventions. Without them the safe quantity is a0=Phi_{infty,split}(0)!=0 of vHS Lemma4.2.9. Strong continuity and rational isometry approximation give |a|>=(1-eta)|a0| for a chosen eta; THETA3-Q4 then gives lower bound (1-epsilon)(1-eta)|a0|, and THETA3-Q5 divides by S for an individual period.

The local determinant has a positive value when u,v are linearly independent. It does not identify a global Alpoge determinant or Bessel period.

## Checks pending

- Independent whole-proof check of Q1–Q3 and Q5–Q6.
- Source/image verification of BMM exact cocycle convention before claiming more than determinant shape.
- Exact h_f conductor bounds are not established; they remain a gate rather than an implicit constant.

## THETA3-Q7: an explicit finite grid for the averaged theta coefficient

Let N be the additive Siegel unipotent in A1, viewed over Q as a vector group of dimension d. Let Phi_f be fixed and let K_N be a compact open additive subgroup of N(A_f) fixing Phi_f in the Weil representation. Define

    F(b)=T_Phi(n(b),1_f),  b in N(R).

Put Lambda=N(Q) intersect K_N. Additive strong approximation identifies N(Q)\N(A)/K_N with the real torus N(R)/Lambda, and normalized Haar integration gives its mean a=Phi(0) by A1. Choose a Z-basis lambda_1,...,lambda_d of Lambda and let B:R^d→N(R) have those columns, using Euclidean norms. Suppose F is L-Lipschitz on this torus. For an integer N0≥1 let

    Gamma_N0={sum_i (j_i/N0)lambda_i : 0≤j_i<N0}.

Then some gamma in Gamma_N0 satisfies

    |T_Phi(1,n_f(-gamma))| ≥ |a| − L ||B|| sqrt(d)/(2 N0).

In particular for 0<epsilon<1, a!=0, choosing

    N0 ≥ max(1, ceil(L ||B|| sqrt(d)/(2 epsilon |a|)))

gives the bound (1−epsilon)|a| among exactly N0^d explicit finite-adelic translates. The finite Schwartz L2 norm is unchanged. The translate of the doubled input retains every compact subgroup of U(V)(A_f) that fixed Phi_f, since the two members of the dual pair commute. A decomposition into individual four-factor inputs can still require a common smaller level; no bound for that decomposition is asserted by this observation.

Proof. The continuous function |F| attains its maximum on the compact torus, and its maximum is at least the absolute value of the normalized mean a. Choose a maximum point b. Round the coordinates of B^(-1)b modulo Z^d to the nearest grid coordinates j_i/N0. The resulting gamma has torus distance at most ||B||sqrt(d)/(2N0), because each rounded coordinate changes by at most 1/(2N0). The reverse triangle inequality and the Lipschitz bound give |F(gamma)|≥|a|−L||B||sqrt(d)/(2N0). Global theta automorphy under N(Q) gives F(gamma)=T_Phi(1,n_f(-gamma)). The finite Weil action is unitary. The final compact-level assertion follows from its commuting with U(V)(A_f). This proves all claims.

An explicit sufficient Lipschitz constant can be obtained without differentiating an unknown period. Fix coordinates on the rational Schrödinger space of real dimension D. Suppose all rational supports occurring in the finite parts of the chosen fundamental set are contained in one lattice L0⊂R^D of minimum at least rho>0; assume the integrand vanishes outside this lattice. Suppose one has a compact fundamental set for the anisotropic U(V) quotient and explicit constants C,lambda>0 and integer m≥0 such that uniformly there

    |omega(g)Phi(x)| ≤ C(1+||x||)^m exp(−lambda||x||²),  x in L0.

Write the Siegel-unipotent phase as exp(2 pi i <b,Q(x)>), and assume ||Q(x)||≤c_Q ||x||². Then it suffices to take

    L = 2 pi c_Q C sum_(j≥1) (2j+3)^D ((j+1)rho)^2
                              (1+(j+1)rho)^m exp(−lambda j²rho²).

Indeed, differentiate termwise in a unit b-direction; absolute value of the derivative is at most 2pi c_Q ||x||² times the displayed envelope. Normalized quotient integration does not increase its bound. Balls of radius rho/2 around lattice points are disjoint. The number with jrho≤||x||<(j+1)rho is at most (2j+3)^D by a volume comparison, giving the stated series. Uniform convergence of the differentiated series justifies differentiation and integration. Its terms are polynomial times exp(−lambda rho²j²); after any J for which successive term ratios are bounded above by q_J<1, its remaining tail is at most term_J/(1−q_J). Thus the constant admits certified upper bounds from finitely many arithmetic operations and an explicit geometric tail. The existence of a compact fundamental set follows from anisotropy; for numerical use, its coordinates or the stated envelope constants must actually be supplied. No undisplayed effective reduction-theory bound is assumed.

Combining Q6, rational weak approximation, and Q7: normalize the initial doubled Fock vector to a0=1. Choose the rational compact-place isometry so that |a|≥1/2. Choose N0≥max(1,ceil(2L||B||sqrt(d))) to make the grid error at most1/4. Then one explicit finite translate has |I|≥1/4. If its four-factor, character, and connected-component extraction is the exact finite identity I=sum_lambda b_lambda J_lambda with S=sum_lambda |b_lambda|>0, then some geometric mixed period satisfies |J_lambda|≥1/(4S). This is an explicit selection certificate depending on completely named normalizations and coefficients; it is not a uniform lower bound for preassigned inputs or for algebraic cycle degree.

## THETA3-Q8: a pointwise certificate for the fixed-input positive norm

Let X be a smooth projective complex surface and xi a holomorphic2-form. Suppose an injective holomorphic chart contains the Euclidean ball B_R⊂C², and xi=f(z)dz1∧dz2 there. Suppose |f(0)|≥b>0 and the real differential of f has operator norm at most M throughout B_R. For any 0<r<R with Mr≤b/2,

    integral_X xi∧bar(xi) ≥ (pi²/2)b²r⁴.

Proof. The segment from0 toz stays in the ball and the differential bound gives |f(z)−f(0)|≤M||z||. Thus |f(z)|≥b/2 on B_r. In the standard complex orientation dz1∧dz2∧dbarz1∧dbarz2=4 dvol_R4. Consequently the integral on B_r is at least4(b²/4)vol(B_r)=b²(pi²r⁴/2). The integrand is nonnegative elsewhere, proving the inequality. If M=0 choose any r<R. This converts Q2's certified nonzero wedge coefficient, plus a derivative bound from differentiated theta series, into a numerical lower bound for A in Q1; the chart and injectivity radius are required input data.

## THETA3-Q9: an explicit denominator certificate for Hecke extraction

Let X be a smooth projective surface, Lambda=H1(X,Z)/torsion, and let T_j be commuting integral Hodge endomorphisms of Lambda, induced by rational algebraic correspondences (the integral action is an explicit hypothesis). Suppose f_j,g_j∈Z[t] are monic, coprime over Q, and f_j(T_j)g_j(T_j)=0. Put R_j=Res(f_j,g_j)!=0. There are u_j,v_j∈Z[t] with

    u_j f_j+v_j g_j=R_j.

Define e_j=v_j(T_j)g_j(T_j)/R_j and e=product_j e_j. Then e is a rational Hodge projector, it is induced by a rational algebraic correspondence, and e(Lambda)⊂R^(-1)Lambda for R=product_j |R_j|. Its image is the intersection of the f_j-primary factors. This gives an explicit denominator for a finite chosen Hecke-isotypic extraction; it does not assume that an unspecified infinite Hecke algebra has already been made effective.

Now let K be a number field of degree n. For i=1,...,4 let e_i be projectors of this kind, with denominator R_i, and let u_i∈Lambda⊗K have d_i u_i∈Lambda⊗O_K for positive integers d_i. Put alpha_i=e_i u_i and

    P=integral_X alpha_1 cup alpha_2 cup alpha_3 cup alpha_4 ∈K,
    D=product_i R_i d_i.

Then D P is an algebraic integer. If P!=0 and for all embeddings sigma≠sigma0 known bounds |sigma(P)|≤M_sigma hold with M_sigma>0, then

    |sigma0(P)| ≥ D^(−n) product_(sigma≠sigma0) M_sigma^(−1).

If K is CM and P lies in K0, the same argument can be made in K0 with its smaller degree and real conjugates. For a Hermitian Gram determinant, B7 supplies a stronger positive-matrix version when all its real conjugates are positive.

Proof. The adjugate of the Sylvester matrix gives the displayed resultant Bezout identity over Z. By the Chinese remainder theorem over Q, e_j is1 on ker f_j(T_j),0 on ker g_j(T_j), and is idempotent. More explicitly e_j^2−e_j is a rational polynomial multiple of f_jg_j, so it vanishes on Lambda_Q. Commutativity of the T_j makes the e_j commute; their product is the projector onto the intersection of their images. The integral polynomial numerator proves the denominator assertion. Each polynomial in a Hodge endomorphism is Hodge, and addition/composition of algebraic correspondences realizes the rational polynomial, proving the geometric assertions.

The cup product and evaluation on the integral fundamental class give a Z-valued multilinear form on Lambda. Multiplying its four arguments by R_i d_i makes all four integral over O_K, so D P∈O_K. Since P!=0, its algebraic norm satisfies |N_K/Q(DP)|≥1. Therefore product_sigma |sigma(P)|≥D^(−n); divide by the specified upper bounds to obtain the inequality. No positivity hypothesis is required for this scalar norm argument.

In the 032 application one first uses the cited Hecke/Frobenius/weak-admissibility statements to know that the selected eigenspaces are the required CM Hodge sources. Pure CM eigenvectors can be chosen over a number field in Lambda⊗K; their holomorphic or antiholomorphic harmonic representatives have exactly the same cup products as these Betti vectors. Thus the certificate applies to their normalized mixed period. Arbitrarily scaled analytic theta forms need not be algebraic Betti vectors, and their scalar comparison factors must be retained. The theorem supplies explicit denominators from specified finite Hecke matrices; the source papers do not supply numerical matrices, resultant bounds or uniform cycle-degree estimates for arbitrary CM types. These remain input requirements, not implicit constants.

# An explicit conditional spectral bridge on Masullo’s actual Hilbert quotient

Run TRACE_DET_20261121; agent `/root/masullo_spectral_bridge`; GPT-6 Astra Pro (inherited developer model label); effort setting not exposed. Date: 21 November 2026. These are new deductions from the stated draft hypotheses, not an audit or acceptance of the draft’s long proofs.

## Status update after the independent Green route

The provisional ordinary trace-class gate in MAS-08 below was subsequently **closed by MAS-10**, proved in masullo_traceideal_gate.md. The explicit Green operator gives R_+ in S1 using the spectral-jet quotient claim and stipulated RH, without the draft nuclearity theorem or a small-time heat trace-norm estimate. The earlier gate discussion is retained as research history and is not the final state. The convolution-integral and generalized-eigenspace wording below has also been corrected following independent checking.

## Scope and exact source hypotheses

Specialize to F=Q, the trivial character of C_Q^1, center a=1/2, I=[−alpha,alpha] with 0<alpha<1/2, and s>1. The compact norm-one factor has Haar mass1; put u=log|g|. The ambient radial space is

H=L²(R,w(u)du),   w(u)=exp(2alpha|u|)(1+u²)^(s/2).

Let V be the closed, centered theta-image in H and E=H/V. Use the stipulated Alpöge RH theorem, so the nontrivial zeta zeros are 1/2+i gamma, with real nonzero gamma, paired by gamma↔−gamma and with multiplicity N_gamma. The restriction alpha<1/2 keeps the closed strip away from the two poles; all nontrivial zeros lie in its interior, so no boundary multiplicity cap enters.

Only the following Masullo claims are used, conditionally:

* Definition10.1.1.1 and equation(10.2.2.1), PDF pp434,445: the stated Hilbert quotient; the radial norm is (9.2.2.34), (9.2.2.40)–(9.2.2.41), p417.
* Theorem10.2.2.1, equations(10.2.2.4)–(10.2.2.6), p446: the full interior spectral-jet functionals
  ell_(gamma,m)(f)=integral f(u)exp(i gamma u)u^m du, 0≤m<N_gamma,
  lie in the continuous annihilator of V and their linear span is dense in E'. The basis statement is used for density and full jet multiplicity, not as a Riesz-basis assertion. The explanation of norm density for Hilbert duals is Remark10.2.1.2, pp440–441.
* Theorem10.3.2.1(2), equation(10.3.2.2), pp453–454: compact smooth convolution descends to E and the map A:D(C_Q)→S1(E) is continuous in trace norm.

The convolution/jet action is displayed directly in the draft’s equations(10.3.1.8)–(10.3.1.14), p449. The centered quotient’s relation to Connes’s infinitesimal generator D_chi is stated in §10.2.1, p439. The nonunitary translation action and its growth are discussed before Lemma9.3.1.5, pp420–421; the estimates needed below are proved independently, rather than using the printed bound at the identity.

The only zeta input beyond stipulated RH is the usual zero count N(T)~(T/(2pi))logT and Xi(0)≠0 already used in B-01 (Titchmarsh, Theorem9.4/(9.4.3), p214; §2.12). No simplicity hypothesis is imposed.

## MAS-07: a single compact smooth test cannot be the reciprocal-square multiplier

**Statement.** No phi in D(C_Q) has, in the trivial compact-character component, Mellin values

Mphi(|·|^(i gamma))=1/gamma²

for every positive zeta ordinate. More generally this is impossible with target 1/(gamma²+c²) for any fixed c≥0, hence also with target1/[rho(1−rho)] at rho=1/2+i gamma (c=1/2).

**Proof.** Average phi over the compact norm-one factor, obtaining h in C_c^infinity(R). Its Mellin transform on the centered unitary line is the ordinary Fourier transform

F(t)=integral h(u)exp(i t u)du.

Three integrations by parts, with no boundary term because h is smooth and compactly supported, give |F(t)|≤||h'''||_1 |t|^(−3) for t≠0. There are positive ordinates gamma→infinity. At them gamma³/(gamma²+c²)→infinity, whereas gamma³|F(gamma)| is bounded. This contradiction proves the statement. The averaging step is legitimate because the compact factor has finite mass and phi has compact radial support; its derivatives remain smooth and compactly supported. QED.

This refutes only the literal one-test construction with the indicated spectral multiplier. A subsequent functional calculus or a less rapidly decaying test kernel remains possible. Equality of an unordered eigenvalue multiset after an unspecified permutation is a different assertion; this proof concerns the designated zero-by-zero multiplier.

## MAS-08: actual trace-class heat operators and a compact inverse-square operator

### 1. Bounded weighted translations

Let U(v)f(u)=f(u−v). Since

1+(u+v)²≤2(1+u²)(1+v²),

we have

w(u+v)/w(u)≤exp(2alpha|v|)[2(1+v²)]^(s/2).

Thus U(v) is bounded on H, and on its quotient E, with

||U(v)||≤2^(s/4)exp(alpha|v|)(1+v²)^(s/4).                 (1)

Translation invariance of V makes the quotient action well-defined. Translation is strongly continuous on compact smooth functions by dominated convergence, and these are dense in H; the bound is locally uniform in v, so U is a strongly continuous group on H and E. If h is integrable against the right side of(1), the strong integrated operator A(h)f=integral h(v)U(v)f dv (a vector-valued Bochner integral for each f) is bounded. Its norm is at most the integral of |h(v)| times that bound.

### 2. Extension of the conditional S1 theorem to Gaussian kernels

For t>0 define

k_t(v)=(4pi t)^(−1/2)exp(−v²/(4t)),   H_t=A(k_t).

Then, conditional on the stated draft continuity D→S1, H_t belongs to S1(E).

**Proof.** Choose chi in C_c^infinity((−1,1)) with sum_(n in Z) chi(v−n)=1. Such a partition is obtained by normalizing a nonnegative bump that is positive on [−1/2,1/2] by the positive periodic sum of its translates. For each n put

q_(n,t)(v)=chi(v)k_t(v+n).

Then k_t=sum_n U(n)q_(n,t), pointwise and in weighted L1. The restriction of the continuous linear map D→S1 to the fixed compact-support Fréchet space D_[−1,1] has constants C and an integer M such that

||A(q)||_1≤C sum_(j=0)^M ||q^(j)||_infinity.              (2)

For fixed t>0, Gaussian differentiation and |v|≤1 give

sum_(j=0)^M ||q_(n,t)^(j)||_infinity
 ≤C_t(1+|n|)^M exp(−(|n|−1)²/(4t)).

The constants can be chosen uniformly when t ranges over a compact interval in (0,infinity). Since A(U(n)q)=U(n)A(q), the ideal inequality, (1), and (2) show that sum_n||U(n)A(q_(n,t))||_1 is finite. Its sum is the bounded integrated operator H_t, since the same decomposition converges in weighted L1 and therefore operator norm. Hence H_t is trace class. The uniform estimates also show that t↦H_t is trace-norm continuous on every compact subinterval of (0,infinity). QED.

Gaussian convolution gives H_t H_r=H_(t+r), by the group law and vectorwise Fubini; (1) supplies an integrable bound on the vector norms for each input. No operator-norm Bochner measurability of the translation map is asserted. Also H_t→I strongly as t↓0. In particular,

sup_(0<t≤1)||H_t||<infinity.                              (3)

For(3), substitute v=sqrt(t)y in the weighted integral bound and dominate it uniformly by a Gaussian times exp(alpha|y|)(1+y²)^(s/4). Strong convergence follows from the approximate identity and strong continuity of U.

### 3. Spectrum and full multiplicities

On the continuous dual the jet action is

H_t' ell_(gamma,m)=sum_(j=0)^m binom(m,j) F_t^(j)(i gamma) ell_(gamma,m−j),

where F_t(z)=exp(t z²). This follows either by differentiating the Gaussian Mellin integral or by the binomial expansion of (u+v)^m, exactly the operation in the cited p449 source formula. All differentiations and integrals are dominated by a Gaussian times an exponential times a polynomial.

Consequently H_t' has eigenfunctional ell_(gamma,0) with eigenvalue exp(−t gamma²). These are exactly the nonzero spectral values of H_t, and the algebraic multiplicity at exp(−t gamma²), for gamma>0, is 2N_gamma.

**Proof of completeness of this spectrum.** A compact operator has only eigenvalues off0. If H_t f=lambda f and lambda differs from all the displayed values, evaluation by ell_(gamma,0), then by the higher jets successively, forces every ell_(gamma,m)(f)=0. Density of their span in E' gives f=0. Conversely a nonzero eigenfunctional makes H_t−lambda noninvertible, hence lambda is a nonzero spectral value. For algebraic multiplicity, use the finite-rank Riesz projection for the isolated nonzero value lambda. On each finite jet block its transpose is identity if the block’s eigenvalue is lambda, and zero otherwise; this is the ordinary finite triangular-matrix contour calculation. The blocks with this lambda are exactly the two blocks gamma,−gamma. Their total dimension is2N_gamma. Their span is closed. Density of all jets shows that the projection’s whole range is exactly this finite span: it contains these blocks and the image of a dense subspace is contained in them, so continuity puts every image in them. This proves the algebraic multiplicity. The compact-operator spectral theorem and the Riesz projection are the standard Hilbert Fredholm spectral facts already used in cote1/B-01; no diagonalizability is assumed.

### 4. The actual compact inverse-square operator

Set

Q=integral_0^1 H_t dt,        R=Q(I−H_1)^(−1).             (4)

The first integral exists in operator norm. Indeed H_t is norm continuous for t>0, has separable norm range there, and is bounded near0 by(3). For epsilon>0, its integral over [epsilon,1] is trace class by trace-norm continuity; the omitted [0,epsilon] piece has operator norm at most C epsilon. Thus Q is a norm limit of compact operators and is compact. Since all nonzero spectral values of H_1 are exp(−gamma²)<1, I−H_1 is invertible. Therefore R is an actual bounded compact operator on the specified quotient E.

Its action on the dual jets is the multiplier of

F(z)=[integral_0^1 exp(t z²)dt]/[1−exp(z²)]=−1/z²

near each z=i gamma. Thus R' ell_(gamma,0)=gamma^(−2)ell_(gamma,0). Its nonzero spectrum is precisely {gamma^(−2):gamma>0}, with algebraic multiplicity2N_gamma, by the same total-jet and Riesz-projection argument. Formula(4) does not assert that R is trace class.

### 5. A canonical parity reduction removes the double counting

Let Jf(u)=f(−u). The weight is even, so J is a unitary selfadjoint involution on H. Its transpose sends

J' ell_(gamma,m)=(−1)^m ell_(−gamma,m).

The complete spectral-annihilator description and the functional equation’s pairing therefore show that J preserves V: every annihilating jet vanishes on Jf when f is in V, and the closed subspace V is the annihilator of its annihilator. Thus J descends to a unitary selfadjoint involution on E. Put E_+=ker(J−I). This is an actual orthogonal summand, not an arbitrary selection of zero coordinates.

Each Gaussian kernel is even, so H_t commutes with J, as do Q and R. Define

H_(t,+)=H_t|E_+,      R_+=R|E_+.

Then H_(t,+) is trace class and R_+ is compact. In the dual generalized eigenspace (Riesz spectral subspace) at gamma^(−2), J pairs the gamma and −gamma blocks; its plus-eigenspace has basis

ell_(gamma,m)+(−1)^m ell_(−gamma,m), 0≤m<N_gamma.

It has dimension N_gamma. Thus R_+ has precisely the eigenvalues gamma^(−2) once per ±pair, with the full zeta multiplicity. In particular, it has exactly the spectral list used to define B-01, on a specified actual quotient summand.

### 6. The ordinary determinant gate is now precise

If the compact operator R_+ is trace class, cote1 gives

det_(E_+)(I−wR_+)=product_(gamma>0)(1−w/gamma²)^(N_gamma)=G(w).

A sufficient condition for that trace-class property is

integral_0^1 ||H_(t,+)||_1 dt < infinity.                  (5)

Indeed(5) makes Q|E_+ trace class by a Bochner integral in S1, and multiplication by the bounded inverse in(4) preserves S1. Condition(5) is sufficient; necessity is not asserted.

The draft’s compact-test nuclearity alone supplies no bound of this stated form as t↓0. The scalar integral is already finite:

integral_0^1 Tr H_(t,+) dt
 =sum_(gamma>0) N_gamma(1−exp(−gamma²))/gamma² < infinity.

Here the trace at each positive t follows from trace class plus the just-proved spectrum; Tonelli applies to the nonnegative scalar terms, and convergence follows from the usual zero count. It cannot be replaced by(5), since the actual heat operator is not positive in the quotient metric, as the next result proves.

This is a genuine reduction of the earlier vague “choose a special test or intertwiner” gate: (4), followed by the canonical even summand, specifies a compact operator on the draft’s actual quotient with the correct full paired spectrum. The remaining ordinary-Fredholm gate is its S1 property, for which(5) is one explicit sufficient estimate. Positivity and a bounded metric repair are separately obstructed below.

## MAS-09: positivity is impossible in the actual quotient metric, and no bounded similarity repairs R_+

### 1. Strict positivity of the dual correlation kernel

Define

K(x)=integral_R exp(i x u)/w(u)du.

Then K(x) is a strictly positive real number for every real x. It is continuous, K(0)>0, and K(x)→0 as |x|→infinity.

**Proof.** Integrability follows from alpha>0; the latter two assertions are the elementary continuity and Riemann–Lebesgue properties of an L1 Fourier transform. Write a=2alpha>0 and use the Gamma integral

(1+u²)^(−s/2)=Gamma(s/2)^(−1) integral_0^infinity r^(s/2−1) exp(−r) exp(−r u²)dr.

For each r>0, the Fourier transform of exp(−a|u|)exp(−r u²) is strictly positive. Indeed the elementary Cauchy Fourier identity

exp(−a|u|)=(a/pi) integral_R exp(i y u)/(a²+y²)dy

and the Gaussian Fourier integral express that transform at x as

(a/pi)sqrt(pi/r) integral_R exp(−(x+y)²/(4r))/(a²+y²)dy >0.

The Cauchy identity follows by closing the contour in the half-plane with decaying exponential, with its single pole at ia or −ia; at u=0 it is the elementary arctangent integral. Fubini is justified by the Gaussian and integrable Cauchy density. Integrating this strictly positive expression against the positive Gamma measure proves K(x)>0. All changes of order are justified also before taking the Fourier integral by the integrable absolute majorant exp(−a|u|)(1+u²)^(−s/2). QED.

### 2. The actual Riesz representatives are nonorthogonal

Use the convention that the Hilbert inner product is conjugate-linear in its first argument. The Riesz vector in H for ell_(gamma,0) is

v_gamma(u)=exp(−i gamma u)/w(u).

Because ell_(gamma,0) annihilates V, v_gamma lies in V^perp, hence represents the same functional isometrically on the quotient E. Therefore

<v_gamma,v_delta>=K(gamma−delta)>0.

In the even summand, the Riesz representative for the even evaluation functional is

c_gamma(u)=cos(gamma u)/w(u),

and

<c_gamma,c_delta>=[K(gamma−delta)+K(gamma+delta)]/2 >0.      (6)

This is an actual quotient-inner-product calculation, not an abstract counterexample with another metric.

A selfadjoint bounded operator has orthogonal eigenvectors at distinct real eigenvalues. But R_+^* c_gamma=gamma^(−2)c_gamma, and H_(t,+)^* c_gamma=exp(−t gamma²)c_gamma. There are distinct positive ordinates gamma and delta, giving distinct real eigenvalues and the nonzero inner product(6). Hence neither R_+ nor any H_(t,+), t>0, is selfadjoint or positive in this quotient metric. The same observation refutes positivity of any bounded multiplier whose real values differ at two positive ordinates. This conclusion is conditional on the stated quotient/spectral assumptions, but the displayed obstruction is proved independently from its norm.

### 3. R_+ cannot even be boundedly similar to a selfadjoint operator

This stronger assertion does not assume simplicity of the zeta zeros.

**Case A: some zero has multiplicity at least2.** On the two-dimensional even jet subspace generated by

e_0=ell_(gamma,0)+ell_(−gamma,0),
e_1=ell_(gamma,1)−ell_(−gamma,1),

we have

R_+'e_0=gamma^(−2)e_0,
R_+'e_1=gamma^(−2)e_1+F'(i gamma)e_0,

where F(z)=−1/z² and F'(i gamma)=2/(i gamma)^3≠0. Both jets are present because alpha>0 makes the zero interior; they are independent by the cited spectral basis. This is a nontrivial generalized eigenvector. Selfadjoint operators have no such vector: if (A−lambda)y=x and (A−lambda)x=0 with real lambda, then ||x||²=<x,(A−lambda)y>=<(A−lambda)x,y>=0. Similarity preserves this obstruction. Thus R_+ is not boundedly similar to a selfadjoint operator.

**Case B: every zero is simple.** The positive zero count grows like T logT, so there exist distinct positive ordinates gamma_n,delta_n→infinity with |gamma_n−delta_n|→0. Otherwise some positive lower gap would hold eventually and the count would be O(T). A precise extraction uses the pigeonhole principle among successive ordinates below T with their number divided by T tending to infinity; discreteness of zeros ensures the selected small-gap pairs escape every fixed compact interval.

By continuity of K at0, its decay at infinity, and(6), the unit vectors

u_n=c_(gamma_n)/||c_(gamma_n)||,  v_n=c_(delta_n)/||c_(delta_n)||

satisfy <u_n,v_n>→1, hence ||u_n−v_n||→0. They are eigenvectors of R_+^* with distinct eigenvalues.

If R_+^* were S A S^(−1) for a bounded invertible S and a selfadjoint A, S^(−1)u_n and S^(−1)v_n would be orthogonal. Their individual norms are at least1/||S||, so the norm of their difference is at least sqrt(2)/||S||. But it is at most||S^(−1)|| ||u_n−v_n||→0, a contradiction. Bounded similarity of R_+ to a selfadjoint operator would give one for its adjoint, so it too is impossible. QED.

Consequently the missing route is not a bounded change to an equivalent Hilbert norm that makes this particular inverse-square operator positive. One can still build the separate positive diagonal zero-space B, or change the realization through an unbounded/non-equivalent completion, or use a different arithmetic construction. None of these alternatives is identified by the present proof.

## Framework and effect on the main question

The construction lives in the analytic Hilbert quotient of functions on C_Q attached to Spec Z. It uses the involution of the radial group and functional calculus of its convolution action. It is not an étale cohomology, crystal, or motive. Cote1 (scans79–80,111–112) supplies the ordinary Fredholm conclusion only after the remaining S1 hypothesis for R_+ is met. The gamma↔−gamma parity reduction plays the same zero-pairing role as B-01 but is realized on this specific analytic quotient. No SGA5 or EGA theorem is being asserted to construct it.

The sharp answer is now: conditional on the draft’s quoted spectral and nuclearity claims, an explicit compact R_+ on the actual quotient has exactly B’s full paired spectrum, but its positivity is refuted in the actual metric, and even bounded similarity to a selfadjoint operator is impossible. Its ordinary Fredholm determinant equalsG if R_+∈S1; a concrete sufficient remaining gate is the small-time heat trace-norm integral(5). A single compact smooth test is impossible for the reciprocal-square multiplier. This is more than the original family-scaling observation MAS-02, while preserving the distinction between scalar spectral equality, trace class, and positivity.

## Whole-proof check performed in this run

After composition the entire argument was reread, checking the centered trivial-character specialization, full interior multiplicities, translation-norm inequality, unit-interval partition and finite-order trace-norm continuity estimate, Gaussian derivative domination, semigroup composition and near-zero operator bound, compactness of Q, invertibility of I−H1 using Xi(0)≠0, complete-spectrum and algebraic-multiplicity arguments, invariance of V under parity from the annihilator description, half multiplicities, the distinction between scalar trace and trace norm, the actual quotient Riesz representatives, strict positivity of K, and both branches of the no-bounded-similarity argument. No new gap was found in that reading. The required source claims remain conditional; S1 of R_+ is not asserted. Separate check events record this as a targeted whole-proof check, not an independent re-proof.

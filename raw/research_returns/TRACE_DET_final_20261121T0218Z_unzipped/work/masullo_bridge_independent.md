# Independent check of the actual Masullo quotient bridge

Run TRACE_DET_20261121, 21 November 2026. Checker: /root/masullo_bridge_check, GPT-6 Astra Pro (inherited developer model label); effort setting not exposed.

## Verdict and scope

I read the whole of masullo_bridge.md, all its proofs and final qualifications, and the existing paper_masullo.tex. I independently recomputed the translation estimates, Gaussian extension, jet actions and algebraic multiplicities, parity reduction, dual correlation kernel and both no-bounded-similarity cases. I checked the cited draft statements directly in the supplied text.

**MAS-07 and MAS-09 pass. MAS-08 passes after two exposition corrections below. Its initially open trace-class gate is superseded by the independently verified Green-resolvent argument, MAS-10, in Part II of this note.** Part III strengthens that argument: with the full strip I=[−1/2,1/2], the actual determinant construction does not require RH at all. It is conditional only on the stated full spectral-jet description of the actual quotient. Neither version requires the draft's separate nuclearity theorem.

All dependence on the draft remains conditional. This check does not verify the draft's proof of its spectral-annihilator theorem or the proposed general-Hecke GRH theorem.

Two corrections to the original bridge note are necessary:

1. The integral of h(v)U(v) must initially be a **strong operator integral**, defined by a Bochner integral in the Hilbert space for each fixed input vector. Strong continuity of U does not assert Bochner measurability of v ↦ U(v) as a function with values in the operator-norm Banach space. Gaussian semigroup Fubini is likewise justified vectorwise with the displayed norm majorant. Once t ↦ H_t is norm continuous for t>0, the integral Q=∫_0^1 H_t dt really is an operator-norm Bochner integral. Thus the conclusion is unchanged, but the two types of integration must be distinguished.
2. In the parity/multiplicity argument, the full jet block is a **generalized eigenspace**, equivalently a Riesz spectral subspace. It is not the ordinary eigenspace if a zero has multiplicity greater than one.

## Source checks

The following statements were read directly:

- Definition 10.1.1.1, (10.1.1.1)–(10.1.1.3), PDF p.434: the centered theta image and its closure in the weighted Hilbert space. The displayed equivariance also supplies translation invariance of that closed image.
- (10.2.2.1)–(10.2.2.3), p.445: the quotient, its trivial compact-character isotype and the bilinear dual pairing ∫f(g)η(g)dμ(g).
- Theorem 10.2.2.1, (10.2.2.4)–(10.2.2.6), p.446: the full interior jet list and the Markushevich-basis assertion. Only its finite independence and norm-dense totality in the Hilbert dual are used; no Riesz-basis estimate or uniform biorthogonal bound is assumed.
- Theorem 10.3.2.1(2), (10.3.2.2), p.454: the map from compact smooth tests to S1 is expressly claimed continuous in trace norm. It is not merely continuity in the operator-norm topology.
- The displayed convolution/jet computation (10.3.1.8)–(10.3.1.14), p.449, and the matrix (10.3.1.17), p.450: derivatives of the Mellin multiplier act by the triangular jet formula used below.
- The weighted norm (9.2.2.34), (9.2.2.40)–(9.2.2.41), p.417, as already transcribed in paper_masullo.tex.

Fix F=Q, the trivial compact-character component, center 1/2, 0<α<1/2 and s>1. Its radial Hilbert space and closed theta subspace are

\[
H=L^2(\mathbb R,w(u)\,du),\qquad
w(u)=e^{2\alpha|u|}(1+u^2)^{s/2},\qquad E=H/V.
\]

Under stipulated RH the relevant zeros are 1/2+iγ, γ real and nonzero. All lie in the interior of this strip, so the boundary-cap issue is absent and every jet order m<Nγ is retained. The two poles are outside the strip. The full spectral assumption says that

\[
\ell_{\gamma,m}(f)=\int_{\mathbb R}f(u)e^{i\gamma u}u^m\,du,
\qquad 0\le m<N_\gamma,
\]

annihilate V and have dense linear span in E′. Each is bounded because ∫|u|^{2m}/w(u)du<∞. The bilinear dual pairing is distinct from the conjugate-linear-first Hilbert inner product.

## Part I. Independent verification of MAS-07–09

### A. A compact smooth test cannot give the designated reciprocal-square multiplier

Averaging a test on C_Q over its compact norm-one factor produces h∈C_c^∞(R). The centered Mellin value is

\[
F(t)=\int h(u)e^{itu}\,du.
\]

Three integrations by parts give |F(t)|≤||h'''||_1|t|^{-3}. All boundary terms vanish because h is compactly supported and smooth. Since there are ordinates γ→∞, the equality F(γ)=1/(γ²+c²) would imply

\[
\frac{\gamma^3}{\gamma^2+c^2}\le\|h'''\|_1,
\]

contradicting divergence of the left side, for every fixed c≥0. Compact-factor averaging preserves smoothness and compact radial support. This proves MAS-07 exactly in its designated-zero-by-zero sense. It does not prove a claim about arbitrary permutations of a spectral list.

### B. Weighted translations and the Gaussian extension

For U(v)f(u)=f(u-v), substitution shows

\[
\|U(v)f\|_H^2=\int|f(u)|^2w(u+v)\,du.
\]

The inequalities |u+v|−|u|≤|v| and 1+(u+v)²≤2(1+u²)(1+v²) yield

\[
\|U(v)\|\le 2^{s/4}e^{\alpha|v|}(1+v^2)^{s/4}.
\]

The group is strongly continuous on H: first use dominated convergence for compact smooth functions, then density and the locally uniform norm bound. The source gives invariance of V; it also follows from the total-jet assumption, because

\[
\ell_{\gamma,m}(U(v)f)=
e^{i\gamma v}\sum_{j=0}^m\binom mjv^j\ell_{\gamma,m-j}(f).
\]

Every jet therefore vanishes on U(v)f if f∈V. Totality and closedness identify V with the common annihilator, giving U(v)V⊂V. The quotient action is strongly continuous with the same bound.

For h integrable against that bound, define A(h)f=∫h(v)U(v)f dv by a Hilbert-valued Bochner integral. The norm estimate gives a bounded operator and convergence in operator norm when h converges in the corresponding weighted L1 space. This is the precise strong-integral meaning needed in the original note.

Let k_t(v)=(4πt)^{-1/2}e^{-v²/(4t)}. Choose χ∈C_c^∞((-1,1)) with Σ_nχ(v-n)=1, and put q_{n,t}(v)=χ(v)k_t(v+n). Direct substitution gives

\[
k_t(v)=\sum_nq_{n,t}(v-n).
\]

Continuity of the conditional map D→S1, restricted to tests supported in [-1,1], gives constants C,M with

\[
\|A(q)\|_1\le C\sum_{j=0}^M\|q^{(j)}\|_\infty.
\]

This follows from continuity of a linear map from the fixed-support Fréchet space to a Banach space, whose increasing derivative seminorms define its topology. For t in a compact subinterval of (0,∞), differentiation of the Gaussian gives a uniform bound

\[
\sum_{j=0}^M\|q_{n,t}^{(j)}\|_\infty
\le C_{t_0,t_1}(1+|n|)^M
e^{-(|n|-1)^2/(4t_1)}.
\]

A harmless increase of the constant handles n=0. Multiplying this by the exponential-polynomial translation bound leaves a summable sequence in n. Since A(q(·-n))=U(n)A(q), the resulting series converges in S1. Weighted-L1 convergence identifies its sum with H_t=A(k_t). This proves H_t∈S1 for every t>0. Continuity of q_{n,t} in every fixed-support derivative seminorm, and uniform convergence of the S1 series on compact t-intervals, prove trace-norm continuity there.

Vector-valued Fubini and the group law give H_tH_r=H_{t+r}. Absolute domination is by a constant times |k_t(v)k_r(y)| ||U(v)|| ||U(y)|| ||f|| for each f. Substitution v=√t y in the weighted-L1 bound gives sup_{0<t≤1}||H_t||<∞. The same substitution and strong continuity of U give H_t f→f by dominated convergence.

### C. Jet action, complete spectrum and multiplicity

For an analytic multiplier F, write its jet action as

\[
M_F\ell_{\gamma,m}
=\sum_{j=0}^m\binom mjF^{(j)}(i\gamma)\ell_{\gamma,m-j}.
\]

Direct binomial expansion under the Gaussian integral proves H_t′=M_{F_t} on each finite jet block, where F_t(z)=e^{tz²}. Gaussian decay justifies all moment integrals. The identity M_FM_G=M_{FG} follows from Leibniz's rule.

If λ≠0 is an eigenvalue of the compact H_t and differs from every e^{-tγ²}, applying the order-zero jets to H_tx=λx gives all order-zero evaluations zero. Induction on m gives every higher jet zero. Totality gives x=0, a contradiction. Conversely an order-zero eigenfunctional at e^{-tγ²} makes H_t−e^{-tγ²} noninvertible. Thus those are exactly the nonzero spectral values.

For an isolated nonzero value λ, the transpose of the Riesz projection acts on each finite jet block as the identity when its diagonal value is λ and as zero otherwise. This follows by integrating the finite triangular resolvent; the finite block is resolvent-invariant. There are exactly two matching blocks, at γ and −γ, of dimensions Nγ each. The image of the dense span of all jets is their finite span. Continuity of the projection then makes its entire range equal that span. Hence the algebraic multiplicity is 2Nγ. No diagonalizability or Riesz-basis assumption appears.

### D. Compact inverse-square operator and parity

The map t↦H_t is operator-norm continuous for t>0 and uniformly bounded on (0,1]. Consequently

\[
Q=\int_0^1H_t\,dt
\]

exists as an operator-norm Bochner integral. Its integrals over [ε,1] are S1, and the omitted interval contributes at most Cε in operator norm. Thus Q is compact. Since 1 is not a nonzero spectral value of H_1, I−H_1 has a bounded inverse. The operator R=Q(I−H_1)^{-1} is compact.

Its jet multiplier is

\[
\frac{\int_0^1e^{tz^2}dt}{1-e^{z^2}}
=-\frac1{z^2}
\]

near every z=iγ. The denominator is nonzero there and γ≠0. The same complete-jet and Riesz-projection argument gives eigenvalues γ^{-2}, with algebraic multiplicity 2Nγ.

Jf(u)=f(-u) is a unitary selfadjoint involution because w is even. Its transpose sends ℓγ,m to (-1)^mℓ−γ,m. Therefore J preserves V by the common-annihilator characterization and descends to E. Even convolution kernels commute with J, so R and H_t restrict to E_+=ker(J−I). In the **generalized** dual spectral subspace at γ^{-2}, the plus subspace has the Nγ-dimensional basis

\[
\ell_{\gamma,m}+(-1)^m\ell_{-\gamma,m},
\quad 0\le m<N_\gamma.
\]

Thus R_+ has the correct paired spectrum with full multiplicity. The original sufficient criterion ∫_0^1||H_{t,+}||_1dt<∞ would imply R_+∈S1, but it was not proved by the heat argument. Scalar heat-trace integrability alone is insufficient. Part II below closes S1 by a different argument.

### E. Actual metric obstruction

Let

\[
K(x)=\int_{\mathbb R}e^{ixu}e^{-2\alpha|u|}(1+u^2)^{-s/2}du.
\]

It is continuous and tends to zero at infinity by the L1 Fourier theorem. It is strictly positive for every real x. For completeness, put a=2α and β=s/2. The Gamma identity writes (1+u²)^−β as a positive mixture of e^{-ru²}, r>0. The Fourier transform of e^{-a|u|}e^{-ru²} is

\[
\frac a\pi\sqrt{\frac\pi r}
\int_{\mathbb R}\frac{e^{-(x+y)^2/(4r)}}{a^2+y^2}\,dy>0.
\]

Here the Cauchy integral represents e^{-a|u|}; its density is integrable and nonnegative. Fubini for each r is justified by the Gaussian and Cauchy density. Integrating against the positive Gamma measure is justified by the integrable absolute majorant e^{-a|u|}(1+u²)^−β. This gives K(x)>0, with no possible cancellation.

The Riesz vector for ℓγ,0, under a conjugate-linear-first inner product, is vγ=e^{-iγu}/w(u). Because ℓγ,0 annihilates V, vγ∈V⊥. Therefore the quotient inner product is the ambient one on these representatives. On E_+, the even representative cγ=cos(γu)/w(u) gives

\[
\langle c_\gamma,c_\delta\rangle
=\tfrac12[K(\gamma-\delta)+K(\gamma+\delta)]>0.
\]

Since R_+^*cγ=γ^−2cγ, and H_{t,+}^*cγ=e^{-tγ²}cγ, distinct positive ordinates give nonorthogonal eigenvectors with distinct real eigenvalues. Such an operator cannot be selfadjoint. Hence it cannot be positive in the specified quotient metric.

### F. No bounded similarity to a selfadjoint operator

If Nγ≥2 for some zero, set e0=ℓγ,0+ℓ−γ,0 and e1=ℓγ,1−ℓ−γ,1. For F(z)=−1/z²,

\[
R_+'e_1=\gamma^{-2}e_1+F'(i\gamma)e_0,\qquad
R_+'e_0=\gamma^{-2}e_0,
\]

where F'(iγ)=2/(iγ)^3≠0. The two functionals are independent. Thus the adjoint, through the Riesz identification, has a nontrivial generalized eigenvector at a real eigenvalue. A selfadjoint operator cannot have one: if (A−λ)y=x and (A−λ)x=0, then ||x||²=⟨x,(A−λ)y⟩=⟨(A−λ)x,y⟩=0. Bounded similarity preserves this obstruction.

If all zeros are simple, the zero count N(T)∼T logT/(2π) forces pairs of distinct positive ordinates γ_n,δ_n→∞ with |γ_n−δ_n|→0. Otherwise a positive eventual minimum gap would force N(T)=O(T). Discreteness of zeros makes small-gap pairs escape every fixed bounded interval.

Now ||cγ||²=[K(0)+K(2γ)]/2→K(0)/2, while the inner product for such a pair tends to K(0)/2. Their normalized representatives u_n,v_n therefore have ⟨u_n,v_n⟩→1 and ||u_n−v_n||→0. If R_+^*=SAS^{-1} with A selfadjoint and S boundedly invertible, S^{-1}u_n and S^{-1}v_n must be orthogonal, each of norm at least 1/||S||. Their difference then has norm at least √2/||S||, contradicting its upper bound ||S^{-1}|| ||u_n−v_n||→0.

The two cases exhaust all multiplicity possibilities. The argument does not assume simplicity.

## Part II. MAS-10: independent proof closing the S1 gate by a Green resolvent

This part independently verifies the route proposed by /root/step1_history_route and communicated by the parent. It does not depend on compact-test nuclearity or Gaussian trace-class operators. The only deep draft input is the full interior spectral-jet description of E′ already stated.

### G. Bounded Green convolution

Let

\[
b(u)=\alpha\,\operatorname{sgn}(u)
+\frac{s}{2}\frac{u}{1+u^2},\qquad
B_0=\alpha+s/4.
\]

The value of b at zero is irrelevant. Since b=(log w)'/2 almost everywhere and |b|≤B0, log w is globally 2B0-Lipschitz. Hence the sharper translation estimate is

\[
\|U(v)\|\le e^{B_0|v|}.
\]

Fix μ>B0 and define

\[
g_\mu(v)=\frac{e^{-\mu|v|}}{2\mu},\qquad
\mathcal K_\mu f=\int_{\mathbb R}g_\mu(v)U(v)f\,dv.
\]

The integral is strong, vectorwise Bochner. The weighted-L1 estimates

\[
\int g_\mu(v)e^{B_0|v|}dv=\frac1{\mu(\mu-B_0)},\qquad
\int|g_\mu'(v)|e^{B_0|v|}dv=\frac1{\mu-B_0}
\]

prove boundedness of convolution by gμ and by its first weak derivative. Since

\[
g_\mu''=\mu^2g_\mu-\delta_0
\]

as distributions, if u=Kμf then u,u′,u″=μ²u−f all lie in H. This can also be checked first on compact smooth f and passed to weighted-L2 limits using the displayed bounds.

Its Mellin multiplier is

\[
F_\mu(z)=\int g_\mu(v)e^{zv}dv=\frac1{\mu^2-z^2},
\qquad |\Re z|<\mu.
\]

Thus Kμ′ acts on each jet block by M_{Fμ}. The weighted-L1 bound justifies moving every bounded jet functional through the strong integral; finite binomial expansion gives the derivative formula. In particular Kμ preserves V, since all jets vanish on Kμf whenever they vanish on f. Let Kμ denote its induced bounded operator on E as well.

### H. Direct numerical-range estimate, including the weight cusp

Let T:H→L²(R) be multiplication by √w, a unitary map. Put D=∂−b. If u=Kμf and g=Tu, the weak derivative identities from G give

\[
g\in H^1,\quad Dg=Tu'\in H^1,\quad
D^2g=Tu''\in L^2,\quad
(\mu^2-D^2)g=Tf.
\]

Indeed g′=Tu′+bg∈L²; similarly (Dg)′=Tu″+bDg∈L². This uses only b∈L∞. It never differentiates the jump of b at zero.

Integration by parts for H1 functions gives, with L=μ²−D²,

\[
\langle g,Lg\rangle
=\|g'\|^2+\mu^2\|g\|^2-\|bg\|^2
+\langle bg,g'\rangle-\langle g',bg\rangle.
\]

The last two terms are purely imaginary. Therefore, putting c²=μ²−B0²>0,

\[
\Re\langle g,Lg\rangle
\ge\|g'\|^2+c^2\|g\|^2,
\]

\[
|\Im\langle g,Lg\rangle|
\le2B_0\|g\|\|g'\|
\le\frac{B_0}{c}\Re\langle g,Lg\rangle.
\]

For x=Tf=Lg, the scalar ⟨x,TKμT^{-1}x⟩=⟨Lg,g⟩ is the conjugate of ⟨g,Lg⟩. Thus the bounded ambient Green operator has its numerical range in the closed sector

\[
\Re z\ge0,\qquad |\Im z|\le\beta\Re z,
\quad\beta=\frac{B_0}{\sqrt{\mu^2-B_0^2}}.
\]

This proof needs no m-sectorial representation theorem and no assumption about smoothness of w at zero.

Identify E isometrically with V⊥. Since Kμ preserves V, its quotient operator is the compression P_{V⊥}Kμ|_{V⊥}. Quadratic forms on V⊥ are unchanged by this compression. Hence the same sector bound holds for the quotient operator. Its adjoint has the reflected numerical range, which obeys the same bound.

### I. Complete invariant flags and a trace-class real part

Enumerate the nonzero ordinates block by block, and within each finite block enumerate m=0,1,...,Nγ−1. Take the Riesz representatives of these functionals. They are finite-linearly independent by the spectral-basis statement (also directly by independence of exponential polynomials). Their span is dense in E, since the original jets have norm-dense span in E′.

Each initial finite span is invariant under Kμ*: the jet action only introduces lower orders at the same ordinate. Gram–Schmidt therefore gives a complete orthonormal basis e_n whose initial spans are invariant. If e_n was obtained from the order-m jet at γ, then

\[
K_\mu^*e_n=\lambda_\gamma e_n+
\text{a vector in the preceding span},\qquad
\lambda_\gamma=\frac1{\mu^2+\gamma^2}>0.
\]

The equality follows by reducing the triangular jet equation modulo the preceding invariant span. It does not require a Riesz-basis bound on the original jets.

Let P=(Kμ+Kμ*)/2. The numerical-range estimate makes P positive. Its diagonal in this ONbasis is λγ, including each full multiplicity. The usual zero count gives

\[
\sum_n\langle e_n,Pe_n\rangle
=\sum_{\gamma} \frac{N_\gamma}{\mu^2+\gamma^2}<\infty,
\]

where this sum runs over both signs of γ. Indeed the tail is bounded by a constant times ΣNγ/γ².

For clarity, the positive-operator trace criterion here is immediate: Σ||P^{1/2}e_n||² is the displayed finite sum, so P^{1/2} is Hilbert–Schmidt. Its product with its adjoint is P, which is trace class. Thus TrP equals the displayed sum. No compactness of Kμ was assumed to reach this conclusion.

### J. Sectorial control makes the imaginary part trace class

Write Q=(Kμ−Kμ*)/(2i), a bounded selfadjoint operator. The sector inequality says

\[
|\langle x,Qx\rangle|\le\beta\langle x,Px\rangle.
\]

Equivalently −βP≤Q≤βP. There exists a bounded selfadjoint T0 on the closure of Ran(P^{1/2}), of norm at most β, such that

\[
Q=P^{1/2}T_0P^{1/2}.
\]

Here is the form argument, so this is not an unstated similarity assumption. Define a sesquilinear form initially by

\[
b_0(P^{1/2}x,P^{1/2}y)=\langle x,Qy\rangle.
\]

The inequalities βP±Q≥0, and Cauchy–Schwarz for these positive forms, show that Q kills kerP and that the form is independent of representatives. Its Hermitian quadratic bound is |b0(z,z)|≤β||z||². Polarization and scaling yield a bounded Hermitian form, of operator norm at most β, on Ran(P^{1/2}); it extends to its closure. Riesz representation gives the bounded selfadjoint T0. Extending it by zero on the orthogonal complement gives the displayed factorization on all of E.

Since P^{1/2} is Hilbert–Schmidt, this factorization proves Q∈S1. More precisely,

\[
K_\mu=P^{1/2}(I+iT_0)P^{1/2},
\]

and T0 selfadjoint implies ||I+iT0||≤√(1+β²). The Hilbert–Schmidt product inequality therefore gives

\[
\|K_\mu\|_1
\le\frac{\mu}{\sqrt{\mu^2-B_0^2}}
\sum_{\gamma}\frac{N_\gamma}{\mu^2+\gamma^2}.
\]

Thus the actual quotient Green operator is trace class, and consequently compact. The argument is not circular: compactness is obtained only here, after the complete invariant-flag and sector estimates.

### K. Inverting the scalar shift and recovering the Xi determinant

Suppose (I−μ²Kμ)x=0. Applying the order-zero jets gives

\[
\left(1-\frac{\mu^2}{\mu^2+\gamma^2}\right)
\ell_{\gamma,0}(x)=0.
\]

Its coefficient is γ²/(μ²+γ²)>0. Induction on the jet order then gives every jet zero, since lower-order terms have already vanished. Totality gives x=0. Since Kμ is compact, the Hilbert Fredholm alternative makes I−μ²Kμ invertible with bounded inverse.

Define

\[
R=K_\mu(I-\mu^2K_\mu)^{-1}.
\]

It is trace class. On every jet block its multiplier is

\[
\frac{F_\mu(z)}{1-\mu^2F_\mu(z)}
=-\frac1{z^2}.
\]

This is exactly the multiplier of the earlier heat construction. If that construction is retained, the two bounded operators agree because their transpose actions agree on the dense jet span. The same observation proves independence of the auxiliary μ.

The kernel gμ is even, so Kμ and R commute with the involution J. The actual even summand therefore carries R_+∈S1. The complete-jet/Riesz-projection proof in C–D applies and shows that its nonzero eigenvalues are γ^−2 for positive γ, each with full multiplicity Nγ. Cote 1's Hilbert trace/determinant theorem now gives

\[
\det_{E_+}(I-wR_+)
=\prod_{\gamma>0}(1-w/\gamma^2)^{N_\gamma}
=\frac{\Xi(\sqrt w)}{\Xi(0)}.
\]

The equality is of the actual ordinary Fredholm determinant, not a regularized determinant or an abstract spectral product alone. It is conditional on the specified draft spectral-annihilator claim. The actual norm obstruction in E–F still applies: R_+ is not selfadjoint, is not positive and is not boundedly similar to a selfadjoint operator. Equality of its determinant with B's therefore does not identify their positive Hilbert realizations.

## Part III. MAS-10 on the full strip: the construction does not require RH

The initial proof in Part II used RH to put every zero on the central line. This use can be removed. Choose α=1/2, center 1/2, and the same s>1. Let ρ range over the distinct nontrivial zeros, let Nρ denote their full multiplicities, and put

\[
z_\rho=\rho-\tfrac12,\qquad \gamma_\rho=-iz_\rho.
\]

Classically, 0<Reρ<1, ξ(1/2)≠0, and ξ(0)=ξ(1)=1/2. Thus |Re zρ|<1/2 and zρ≠0. Every zero is interior to the chosen strip. The two boundary points at heights zero are not zeros; no boundary-cap term enters.

The draft's actual Theorem 10.2.2.1 now supplies, conditionally, the full dual jet system

\[
\ell_{\rho,m}(f)=\int f(u)e^{z_\rho u}u^m\,du,
\qquad 0\le m<N_\rho.
\]

These are continuous on H because the strict interior condition leaves exponential decay at both ends in their squared dual-norm integrals. Every individual jet is bounded; no uniform bound as ρ varies is asserted or needed.

The translation bound, Green kernel, weak derivative argument and numerical-range sector estimate from G–H are unchanged. Here B0=1/2+s/4 and μ>B0. The Green jet multiplier remains Fμ(z)=1/(μ²−z²), but the diagonal values are now possibly complex:

\[
\lambda_\rho=\frac1{\mu^2-z_\rho^2}.
\]

If zρ=b+it, then

\[
\Re(\mu^2-z_\rho^2)=\mu^2-b^2+t^2
>\mu^2-\tfrac14+t^2>0.
\]

Consequently Reλρ>0 and

\[
|\lambda_\rho|\le\frac1{\mu^2-\tfrac14+t^2}.
\]

The classical zero count gives ΣρNρ|λρ|<∞. Under the conjugate-linear Riesz correspondence, the invariant-flag diagonal of K* is now the **complex conjugate** of λρ. Its real part is nevertheless Reλρ. Thus the positive operator P=ReK has finite ON diagonal sum ΣρNρReλρ. The sector factorization in I–J proves K∈S1, with

\[
\|K\|_1\le
\frac{\mu}{\sqrt{\mu^2-B_0^2}}
\sum_\rho N_\rho\Re\lambda_\rho.
\]

This explicitly checks the only change needed in the trace-ideal argument; it does not silently retain real diagonal entries.

The coefficient

\[
1-\mu^2\lambda_\rho
=-\frac{z_\rho^2}{\mu^2-z_\rho^2}
\]

is nonzero. The same jet induction and compact Fredholm argument therefore make I−μ²K invertible. The actual trace-class operator R=K(I−μ²K)^{-1} has jet multiplier −1/z² and eigenvalues −1/zρ²=1/γρ².

The functional equation pairs zρ with −zρ, with equal multiplicity. Reflection still preserves V and commutes with the even Green kernel. The Riesz spectral subspace for a fixed value −1/zρ² consists of precisely that pair of jet blocks: equality of two such values forces equality of the squares and hence zσ=±zρ. There is no fixed point because zρ≠0. Its plus subspace has dimension Nρ. Thus the even operator R+ has exactly one copy per reflection pair, with full multiplicity.

The resulting determinant is

\[
\det(I-wR_+)
=\prod_{\{z,-z\}}\left(1+\frac{w}{z^2}\right)^{N_z}
=\prod_{\{\gamma,-\gamma\}}\left(1-\frac{w}{\gamma^2}\right)^{N_\gamma}
=G(w).
\]

The convergence is the unconditional inverse-square convergence already proved in B-01. No RH assumption and no nuclearity theorem is used in this full-strip construction. Its only substantive draft input remains the exact full spectral-annihilator assertion. The statement must retain that conditional label.

### The no-bounded-similarity conclusion also extends across the RH case split

If RH holds, the proof in E–F applies unchanged to α=1/2: the correlation-kernel argument only needs α>0, and all zeros are still interior. It gives no bounded similarity of R+ to a selfadjoint operator.

If RH fails, choose a nontrivial zero ρ=β+it with β≠1/2. Its imaginary part is nonzero. To recall the elementary reason, for real 0<σ<1 the alternating eta series has strictly positive sum (group its successive odd-even pairs), while 1−2^{1−σ}<0; hence ζ(σ)=η(σ)/(1−2^{1−σ})<0 and there is no real zero in this interval. Therefore b=β−1/2 and t are both nonzero, so zρ² has imaginary part 2bt≠0. The eigenvalue −1/zρ² of R+ is nonreal. Spectrum is invariant under bounded similarity, whereas a selfadjoint operator has real spectrum. This rules out bounded similarity in the non-RH case as well.

Thus the no-bounded-similarity conclusion is itself conditional only on the full-strip spectral-quotient assertion, without assuming RH. Under the task's stipulated RH it has the more informative actual-metric and coalescing-eigenvector proof given above.

## Final whole-proof reread

After writing this independent derivation I reread it from the source assumptions through the final determinant conclusion. I checked the operator-integral distinction; all convolution/Fubini bounds; invariance and completeness; the conjugate-linear Riesz convention; finite flag ordering; full algebraic multiplicities; H1 weak derivatives at the weight cusp; the sector constant; compression to the quotient; the positive-diagonal trace criterion and sector factorization; compact Fredholm invertibility; μ-independence; parity; and both branches of the no-similarity proof. The full-strip strengthening was separately checked for complex conjugation of the GS diagonal, positivity of Reλ, absolute summability, the absence of boundary zeros and the precise ±z multiplicity reduction. No mathematical gap remains in these conditional deductions. The deep draft assumption itself has not been independently established by this check.

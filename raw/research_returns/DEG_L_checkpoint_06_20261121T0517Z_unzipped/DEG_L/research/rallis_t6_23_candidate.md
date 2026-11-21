# Candidate T6.23: intrinsic norm and degree growth in the principal four-factor family

Status: promoted after author, root and bounds whole-proof reviews all passed. This file retains the candidate history. Date 2026-11-21. Actor: GPT-6 Astra Pro; effort not exposed; /root/rallis_t6. Unlike T6.19 and T6.22, the degree bound below applies to every cycle with the specified integral orbit class or projection. It remains a statement about the full four-factor CM orbit.

## Proposed theorem T6.23

Use the actual all-four principal-polarization family of T6.19 and T6.21 at one fixed good completely split prime \(p\). Let \(B_r=\prod_{i=1}^4B_{i,r}\), let \(g=[E:\mathbf Q]/2\), and put \(n=\dim_{\mathbf C}B_r=4g\). Each factor has a fixed rational Riemann form and fixed complex structure; only its integral homology lattice varies. Give \(B_r\) the product principal polarization \(L_r\), with invariant positive form
\[
 \omega=c_1(L_r),\qquad
 V=\int_{B_r}\frac{\omega^n}{n!}=1.
 \tag{T23.1}
\]
Here \(\omega\) and the associated flat metric are the same forms on the common universal real vector space for every \(r\). We use the Kähler convention \(\omega=\sum_j dx_j\wedge dy_j\) in a real orthonormal unitary frame, so the Riemannian volume form is \(\omega^n/n!\).

Let \(W\) be the common rational diagonal four-factor orbit, let \(\Theta:E\to W\) be T6.21's trace identification, and let
\[
 \mathcal A_r=M_r^\vee,\qquad
 W_{\mathbf Z,r}=\Theta(\mathcal A_r)
                =W\cap H^4(B_r,\mathbf Z).
 \tag{T23.2}
\]
The superscript \(\vee\) is the field-trace dual. The common metric gives a positive definite, \(r\)-independent \(L^2\) norm on \(W_{\mathbf R}\).

### A. Every nonzero integral orbit class has growing norm

There is an inclusion of global additive lattices
\[
 \mathcal A_r\subseteq p^r\mathcal A_0.
 \tag{T23.3}
\]
Choose any integral basis \(a_1,\ldots,a_d\) of \(\mathcal A_0\), and let \(G\) be the positive definite real Gram matrix of \(\Theta(a_1),\ldots,\Theta(a_d)\) for the fixed \(L^2\) norm. Put
\[
 \sigma_0=\sqrt{\lambda_{\min}(G)}>0.
 \tag{T23.4}
\]
Every nonzero \(w\in W_{\mathbf Z,r}\) satisfies
\[
 \|w\|_{L^2}\ge \sigma_0 p^r.
 \tag{T23.5}
\]
Thus the conclusion concerns even the smallest available nonzero integral orbit class at each target, not merely a sequence chosen with unnecessarily large coefficients.

### B. An explicit primitive family and its exact ambient integral denominator

Choose a nonzero
\[
 \eta\in E^-\cap\mathcal A_0,\qquad c(\eta)=-\eta,
\]
primitive in \(\mathcal A_0\). Choose \(p\) outside the additional finite set where \(\eta\) is not a local unit; this is compatible with the earlier completely split choice. Then
\[
 t_0=\Theta(\eta),\qquad w_r=p^r t_0
 \tag{T23.6}
\]
has the following properties:

1. \(w_r\) is a primitive integral Hodge class in \(H^4(B_r,\mathbf Z)\);
2. its image in \((W_{\mathbf Z,r}\otimes\mathbf Z_p)/\Theta(L^{\mathrm{fact}}_{r,p})\) has order \(p^r\);
3. \(\|w_r\|_{L^2}=p^r\|t_0\|_{L^2}\);
4. the least positive integer \(N\) for which the fixed rational class \(Nt_0\) is integral on \(B_r\) is exactly \(p^r\).

The last statement is an ambient integral-cohomology denominator, not a claim about an integral Hodge conjecture obstruction for the already integral class \(w_r\).

### C. Every representing cycle has growing total absolute degree

For an algebraic codimension-two cycle
\[
 \Gamma=\sum_j m_j[Z_j],\qquad m_j\in\mathbf Z,
\]
with distinct integral subvarieties \(Z_j\), write
\[
 D_{\mathrm{abs},L_r}(\Gamma)
       =\sum_j |m_j|\deg_{L_r}Z_j,
 \qquad
 \deg_{L_r}Z_j=\int_{Z_j}\omega^{n-2}.
 \tag{T23.7}
\]
Let \(\pi_W\) be the canonical diagonal orbit projection of T6.21. For the product polarization metric this projection is orthogonal. For every \(\Gamma\),
\[
 D_{\mathrm{abs},L_r}(\Gamma)
       \ge (n-2)!\sqrt V\,
                    \|\pi_W\operatorname{cl}(\Gamma)\|_{L^2}.
 \tag{T23.8}
\]
Consequently, whenever \(w\in W_{\mathbf Z,r}\setminus\{0\}\), \(N>0\), and
\[
 \pi_W\operatorname{cl}(\Gamma)=Nw,
\]
one has the intrinsic bound
\[
 \frac{D_{\mathrm{abs},L_r}(\Gamma)}{N}
       \ge (n-2)!\sqrt V\,\sigma_0p^r.
 \tag{T23.9}
\]
For the explicit primitive class \(w_r\), the sharper right side is
\[
 (n-2)!\sqrt V\,p^r\|t_0\|_{L^2}.
 \tag{T23.10}
\]
These inequalities hold for every cycle representative and every construction. In particular no uniform total-degree bound exists for integral multiples of nonzero primitive integral classes in this orbit, even if the multiplier is allowed to vary. The same lower bound applies to the total absolute degree of the normalized rational representative \(\Gamma/N\).

## Proof

### 1. Global lattice containment

At every prime \(\ell\ne p\), the four homology lattices are unchanged. Their product lattice and trace dual are therefore unchanged:
\[
 \mathcal A_r\otimes\mathbf Z_\ell
       =\mathcal A_0\otimes\mathbf Z_\ell.
\]
Since \(p\) is a unit in \(\mathbf Z_\ell\), this also equals
\(p^r\mathcal A_0\otimes\mathbf Z_\ell\).

At \(p\), the base homology lattices are the full maximal-order product lattice and the trace pairing is the standard split coordinate pairing. Thus
\[
 \mathcal A_0\otimes\mathbf Z_p
       =\mathcal O_E\otimes\mathbf Z_p.
\]
T6.21 computes, in every conjugate pair,
\[
 \mathcal A_r\otimes\mathbf Z_p
 =\bigoplus_{\text{pairs}}
   \{(x,y)\in p^r\mathbf Z_p^2:x+y\in p^{2r}\mathbf Z_p\}.
 \tag{T23.11}
\]
This is contained in \(p^r(\mathcal O_E\otimes\mathbf Z_p)\). Local inclusions at all primes give the global additive-lattice inclusion (T23.3): in integral coordinates relative to a basis of \(\mathcal A_0\), an element lying in \(p^r\mathcal A_0\) at every completion has integral coordinates divisible by \(p^r\).

### 2. Fixed metric and the norm lower bound

The complex structure on each rational real vector space \(E\otimes\mathbf R\) is fixed by its CM type. The alternating rational Riemann form is fixed by construction. Hence its associated invariant positive \((1,1)\)-form and flat metric are fixed on the universal covering vector space. The sheared lattices remain self-dual for this form. An integral symplectic basis therefore gives
\(\int_{B_{i,r}}\omega_i^g/g!=1\); taking the product gives (T23.1).

Every invariant differential form on a flat torus is harmonic, and these forms represent the whole exterior algebra on its first cohomology. Their pointwise metric inner products are fixed. Their integrals are those inner products times the fixed total volume. Consequently the \(L^2\) Gram matrix on the common rational cohomology, and in particular on \(W\), is independent of \(r\).

For \(0\ne w=\Theta(\kappa)\in W_{\mathbf Z,r}\), write \(\kappa=p^r\sum_j n_ja_j\) by (T23.3), with a nonzero integer vector \(n=(n_j)\). Then
\[
 \|w\|_{L^2}^2
   =p^{2r}n^{\mathsf T}Gn
   \ge p^{2r}\lambda_{\min}(G)\sum_j n_j^2
   \ge p^{2r}\lambda_{\min}(G).
\]
This proves (T23.5).

### 3. Exact primitive normalization

The lattice \(E^-\cap\mathcal A_0\) has positive rank and is saturated in \(\mathcal A_0\), since it is the intersection with a rational subspace. A primitive nonzero vector in it is therefore primitive in \(\mathcal A_0\); this supplies \(\eta\). Excluding its finitely many nonunit primes is permitted when choosing the completely split prime.

At \(p\), the two coordinates of \(\eta\) in each conjugate pair are \((a,-a)\), with \(a\in\mathbf Z_p^\times\). Thus \(p^r\eta\) satisfies (T23.11), while \(p^{r-1}\eta\) does not. Away from \(p\), multiplication by \(p^r\) is a unit and the lattice is unchanged. It follows that \(w_r\) is integral and is not divisible by \(p\) in the integral orbit lattice. If a prime \(\ell\ne p\) divided \(w_r\) in that lattice, it would divide \(\eta\) in \(\mathcal A_0\), contradicting primitivity. Hence \(w_r\) is primitive in \(W_{\mathbf Z,r}\), and also in ambient integral cohomology because intersection with a rational subspace is saturated.

The factorized coefficient lattice at \(p\) is \(p^{2r}\mathcal O_{E,p}\). The coefficient \(p^r\eta\), with unit coordinates after division by \(p^r\), has exact order \(p^r\) modulo it. Linearity in the fixed norm proves the third assertion of part (B).

For a positive integer \(N\), membership \(N\eta\in\mathcal A_r\) forces \(v_p(N)\ge r\) from the coordinate valuations in (T23.11). That condition is sufficient at \(p\), because the sums of the conjugate coordinates vanish identically. It is sufficient at every other prime as well. Therefore the least such integer is \(p^r\). This proves all assertions of part (B).

### 4. Orthogonality of the selected orbit

For each factor, Rosati conjugation says that the adjoint of the rational \(E\)-action for the polarization metric is the action of \(c(a)\). After complexification, if two eigenlines have distinct labels \(\tau,\nu\), their Hermitian pairing satisfies
\[
 \tau(a)\langle v_\tau,v_\nu\rangle
  =\overline{\nu(c(a))}\langle v_\tau,v_\nu\rangle
  =\nu(a)\langle v_\tau,v_\nu\rangle .
\]
Choosing \(a\) with \(\tau(a)\ne\nu(a)\) proves their orthogonality. The induced exterior and product metrics consequently make distinct eigenmonomials and distinct product Kunneth multidegrees orthogonal. The rational Galois-stable span \(W\) is therefore orthogonal to the other monomials, and the specified \(\pi_W\) is the orthogonal projection for the fixed metric.

### 5. Degree from the comass bound

Put \(v=\pi_W\operatorname{cl}(\Gamma)\). If \(v=0\), (T23.8) is immediate. Otherwise let \(u=v/\|v\|_{L^2}\), viewed as its real invariant harmonic degree-four form. Orthogonality gives
\[
 \|v\|_{L^2}
  =\int_{B_r}\operatorname{cl}(\Gamma)\wedge *u
  =\sum_j m_j\int_{Z_j}*u.
 \tag{T23.12}
\]
The pointwise norm of \(*u\) is the constant \(1/\sqrt V\), because the Hodge star is an isometry and \(u\) has \(L^2\) norm one. The absolute value of a differential form on a unit oriented simple multivector is no larger than its pointwise Euclidean norm. Therefore its comass is at most \(1/\sqrt V\).

On the smooth locus of a complex subvariety of dimension \(n-2\), the chosen Kähler convention gives the volume form \(\omega^{n-2}/(n-2)!\). The same integration formula applies to the integration current of an integral possibly singular subvariety; the singular locus contributes no top-dimensional mass. Consequently
\[
 \left|\int_{Z_j}*u\right|
 \le \frac{1}{\sqrt V}\operatorname{Vol}(Z_j)
 =\frac{\deg_{L_r}Z_j}{(n-2)!\sqrt V}.
\]
Insert this inequality into (T23.12) and sum with the absolute coefficients. This proves (T23.8). Substituting \(v=Nw\), then applying (T23.5) or the exact norm of \(w_r\), proves (T23.9)--(T23.10). The argument is independent of the representative, and remains valid for rational coefficients by using their absolute values. QED.

## What is and is not ruled out

This family has fixed field, fixed CM types, fixed rational Hodge space, and fixed principal polarization forms. It shows a precise tradeoff: keeping the rational metric class \(t_0\) fixed requires the ambient integrality multiplier \(p^r\); choosing its primitive integral normalization \(w_r\) forces the normalized total absolute cycle degree to grow at least proportionally to \(p^r\).

The degree obstruction is intrinsic for the stated class or exact integral orbit projection. It is stronger in scope than T6.22's obstruction for specified kernels. It is not a lower bound for the intrinsic Chow denominator of the integral Hodge class \(w_r\), and it does not show that an integral representative of \(w_r\) fails to exist.

The requirement on the projection matters. A bounded-degree integral cycle may have a nonzero **nonintegral** projection into \(W\); the canonical eigenprojector need not preserve the integral lattice on these varying CM varieties. Such a cycle does not contradict (T23.9), which requires the exact projection \(Nw\) with \(w\) integral.

Finally this is the full degree-four CM orbit on a product of dimension \(4g\). In the explicit indecomposable example \(g=4\), that dimension is sixteen. It is not automatically the rank-two middle \(K\)-Weil plane on an abelian fourfold. Transferring this lower bound to that target would require the actual correspondence and quantitative comparison of its integral and metric actions.

## Primary sources and exact normalization

The arithmetic lattice formula and actual principal family are the fully checked T6.19 and T6.21. The metric and orthogonality arguments are proved above directly from the fixed Riemann form and finite-dimensional linear algebra.

For the volume and singular integration facts, Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, Chapter III, formula (1.24) and Wirtinger's inequality (1.25), printed pp.136--137, give the complex-subvariety volume identity; their full displayed proof was read. Demailly's displayed fundamental form is twice the convention used here, and his factor \(2^{n-2}\) is therefore absorbed by \(\omega_{\mathrm{here}}=\omega_{\mathrm{Demailly}}/2\). Chapter III, Section 2.B, formula (2.5), Lemma (2.6) and Theorem (2.7), printed p.140, give the integration current over the regular locus and its finite mass. Those exact statements and displayed proofs were read; the background extension theorem used there is imported. Author source: <https://www-fourier.ujf-grenoble.fr/~demailly/manuscripts/agbook.pdf>.

## Check status

The author, root and bounds have each read the complete saved proof; all reviews passed before promotion. Exact primary-source reads and normalization checks are recorded in the accompanying audit. No computation in a proof assistant is claimed.

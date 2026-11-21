# DEG_L research: L-value bounds, fixed Weil projector, bounded witness theorem

Date: 21 November 2026. Actor: GPT-6 Astra Pro, subagent `/root/lvalue_bounds`; effort setting not exposed. Run: DEG_L_20261121. This is a working research contribution to the root paper, not a claim to solve T6 or T7. Every assertion below is either explicitly conditional, an elementary derived finding with proof, or an identified cited background result. All degrees are geometric intersection degrees, without factorial normalization.

## Executive finding

The strongest positive reduction obtained here is **B8**: in a polarized family of abelian varieties of Weil type of dimension $2n$, a uniformly bounded-degree effective $n$-cycle with *any nonzero Weil component* supplies a bounded-division representative of every fixed flat rational Weil class. The multiplier and both signed degrees are $O(D^2)$, with explicit constants depending only on the fixed family, polarization type, field action, and target class. No varying full CM field or varying Hecke projector is required. The proof gives a fixed polynomial correspondence in the generic imaginary-quadratic action, a comass estimate on invariant harmonic forms, and an integral two-dimensional Cramer calculation. This removes the denominator and isolation gates once bounded geometric witnesses exist; the existence of those witnesses in the open families remains an actual hypothesis.

The analytic findings are complementary. The genuine $U(1)\to U(3)$ Rallis formula uses $L_E(3/2,\chi)$, not $L_E(1,\chi)$; its global factor has elementary conductor-independent upper/lower bounds for fixed field degree. It does not compute the degree of the unnormalized 032 image surface. Edge-of-strip bounds under the admitted Alpöge input and conditional Masullo input apply only after identifying the correct normalized $L$-function, special point, local vectors, measure, and CM extraction coefficients.

## Source findings and exact scope

**S032.** OpenAI family 032, *The rational Hodge conjecture for CM abelian varieties*, §4.4 Lemma 4.4 (printed pp.20–21) fixes finite Schwartz data and permits all sufficiently deep principal levels; §7 proof of Theorem 2.5, printed p.46, explicitly states that pulling to a deeper principal cover multiplies the mixed integral by the cover degree. The theorem then selects a nonzero term and rational Hodge maps by span and finite expansion; it supplies no estimate for coefficients of those maps. These are statements used and rechecked in this run, not independent reproofs of 032.

**S-Rallis1.** Jaeho Haan, *The Bessel Period of U(3) and U(2) involving a non-tempered representation*, arXiv:1403.5061v7, §3.3, Theorem 3.4, printed p.8, gives, in that paper's Tamagawa and splitting conventions,
\[
\langle\theta(\bar f_1,\varphi_1),\theta(\bar f_2,\varphi_2)\rangle
 = \frac{L_E(3/2,\operatorname{BC}(\tau)\otimes\gamma^3)}{L_F(3,\epsilon_{E/F})}
 \prod_v Z_v^{\#}(1,f_{1,v},f_{2,v},\Phi_{1,v}).
\]
Here $\tau$ is an automorphic character of $U(1)$ and $\gamma$ is the chosen unitary splitting character; §3.1 (3.1)–(3.2) defines the normalization of local zeta integrals. §3.6.1, printed p.9, explicitly records absolute convergence and nonvanishing of the numerator at $3/2$. This is a formula for integrated theta lifts with source character, and cannot be substituted for an arbitrary theta-kernel evaluation or wedge in 032 without comparison.

URL: https://arxiv.org/pdf/1403.5061 . Retrieved primary ref: `turn140259939view0`; exact locator find: `turn301895159view3`.

**S-Rallis2.** Gan–Qiu–Takeda, *The Regularized Siegel–Weil Formula (The Second Term Identity) and the Rallis Inner Product Formula*, arXiv:1207.4709v3, Theorem 11.4, printed pp.54–55, under its explicit range and cuspidality/first-occurrence hypotheses, gives the unitary point $(m-n+1)/2$, with twisting character and normalized doubling integrals. Its range $n<m\leq2n$ excludes $U(1)\to U(3)$. The $U(2)\to U(3)$ point is $1$, but the standard degree-two $L$-function is not thereby a Hecke-character $L$-function. A source spectral decomposition or endoscopic factorization must be supplied. The theorem is used as background and its range checked, not reproved.

URL: https://arxiv.org/pdf/1207.4709 . Refs: `turn640628982view1`, `turn819750783view0`.

**S-Alpöge.** The user's Dirichlet GRH input is admitted. Exact supplied Lean declarations: `ALPOGE_Main.lean`, `LFunction_eq_zero_re_of_isPrimitive : PrimitiveDirichletLZerosOnLine`, and `LFunction_ne_zero_of_half_lt_re : DirichletLNonvanishingRightOfHalf`; definitions in `ALPOGE_Statements.lean`. The supplied *Remark*, step 20, printed p.4, announces GRH; steps 9, 12, 18 concern lift norms, Rallis, and indices respectively. The full imported archive is not supplied, and this run did not compile it. No claimed new divisibility theorem is inferred from those steps or from the mapping file.

**S-Masullo.** The full draft is not supplied. The prompt attributes Hecke GRH to §1.2. The supplied `MASULLO_STATEMENTS_INDEX.md` is an index of openings, not theorem statements or proofs. It records Chapter 12, Theorem 12.5.1.1, PDF p.519, and Chapter 13, Theorem 13.3.1.1, PDF p.522, as trace formulas, and records an unfinished-looking opening labelled 13.3.1.2 (at the text-layer level). None is silently promoted to a precise theorem of Hecke GRH in this report. All use of Hecke GRH is conditional on the claim specified by the user, not certified from the index.

## B1. Elementary uniform bounds in the absolutely convergent half-plane

**Statement.** Let $K$ have degree $d$, and let $\chi$ be a unitary Hecke character. For real $\sigma>1$, using the finite Euler product with ramified factors equal to one,
\[
 \left(\frac{\zeta(2\sigma)}{\zeta(\sigma)}\right)^d
 \leq |L_K(\sigma,\chi)|\leq \zeta(\sigma)^d.
\]
More sharply, $\zeta_K(2\sigma)/\zeta_K(\sigma)\leq|L_K(\sigma,\chi)|\leq\zeta_K(\sigma)$. No RH or GRH is needed.

**Proof.** For every unramified prime ideal $\mathfrak p$, unitarity gives $|\chi(\mathfrak p)|=1$. Thus
\[
 (1+N\mathfrak p^{-\sigma})^{-1}\leq
 |1-\chi(\mathfrak p)N\mathfrak p^{-\sigma}|^{-1}
 \leq(1-N\mathfrak p^{-\sigma})^{-1}.
\]
The same inequalities hold with the middle term replaced by one at ramified primes. Absolute convergence permits multiplication. The left product is $\zeta_K(2\sigma)/\zeta_K(\sigma)$. Above each rational prime there are at most $d$ prime ideals, each with norm at least that prime. Comparing each factor gives the stated bounds by rational zeta functions. All factors are positive and the products converge. QED.

**Application.** In S-Rallis1 with $[F:\mathbb Q]=d$ and $[E:\mathbb Q]=2d$, the absolute value of the global ratio lies between
\[
 \frac{\zeta(3)^d}{\zeta(3/2)^{2d}}
 \quad\hbox{and}\quad
 \zeta(3/2)^{2d}\left(\frac{\zeta(3)}{\zeta(6)}\right)^d.
\]
This follows by applying B1 separately to numerator and denominator. It controls no local $Z_v^\#$ and no change of measure, input scale, or cycle normalization.

## B2. Exact edge bounds and what each GRH input buys

Lamzouri–Li–Soundararajan, *Conditional bounds for the least quadratic non-residue and related problems*, arXiv:1309.3595v3, Theorem 1.5 (printed pp.3–4), gives for primitive Dirichlet characters of conductor $q\geq10^{10}$ under GRH, with
\[
 A(q)=\log\log q-\log2+\tfrac12+1/\log\log q,
\]
\[
 |L(1,\chi)|\leq 2e^\gamma A(q),\qquad
 |L(1,\chi)|^{-1}\leq\frac{12e^\gamma}{\pi^2}
 \left(A(q)+\frac{14\log\log q}{\log q}\right).
\]
The constant in the second inequality is $12e^\gamma/\pi^2$, not $12e^{2\gamma}/\pi^2$. An older hosted text extraction returned the latter; the latest arXiv version and Lumley's Theorem 1.1 provide the correct former value. Small conductors require their own finite verification or a separate bound. Under the user's admitted Alpöge theorem, this consequence no longer has a GRH condition. URL: https://arxiv.org/pdf/1309.3595 ; ref `turn301895159view0`.

For primitive nontrivial unitary Hecke characters whose completed $L$-function is entire, write the completed function in degree $d=[K:\mathbb Q]$ over $\mathbb Q$, with conductor $q(\chi)=|D_K|N\mathfrak f_\chi$ and archimedean parameters $\kappa_j$. Allysa Lumley, *Explicit bounds for L-functions on the edge of the critical strip*, arXiv:1804.09850v1, §1.1 and Theorems 2.1–2.2 (printed pp.3–4), applies to
\[
 C(\chi)=\frac{q(\chi)}{\pi^d}\prod_{j=1}^d\left|\frac{1+\kappa_j}{2}\right|.
\]
For fixed degree, its bounds have orders $(\log\log C)^{d}$ and $(\log\log C)^{-d}$; its explicit formulas apply when $\log C\geq23d$. Unit modulus of unramified Hecke parameters supplies the required Ramanujan hypothesis; the remaining GRH input is conditional on Masullo for general $K$. Pole cases (including the trivial character) are excluded. Field degree and archimedean type cannot be hidden while allowing them to vary. URL: https://arxiv.org/pdf/1804.09850 ; ref `turn347054114view0`.

These are known results applied, not new theorems. In particular, this report does not assert an edge bound for a nonabelian $U(2)$ standard $L$-function from Hecke GRH. Nor does GRH give a positive lower bound at the center: the functional equation can force a central zero when a self-dual root number is $-1$.

## B3. Level, vector scale, and arithmetic conductor are distinct

**Statement.** If $\pi:Y\to X$ is a finite étale cover of degree $d$ and $\eta$ is a top-degree form on $X$, then $\int_Y\pi^*\eta=d\int_X\eta$. Consequently a nonzero pulled-back theta form has unnormalized Petersson norm squared multiplied by $d$. If its underlying automorphic representation, infinity type, and finite vector are fixed, the representation's arithmetic and analytic conductors stay fixed.

**Proof.** Integration over evenly covered coordinate sets and a partition of unity gives the integral identity. Apply it to the positive top form defining the norm. Conductors are invariants of the fixed representation and archimedean parameters, not of which smaller compact open subgroup happens to fix its vector. QED.

This is also explicitly recorded for the mixed period in 032 §7 p.46. It is an exact level-growth statement for a chosen presentation, not a lower bound for the intrinsic minimum complexity $c(s)$ in Route 2. Similarly scaling a Schwartz input by $u$ scales a theta lift by $u$ and its norm squared by $|u|^2$, while leaving its representation's $L$-function unchanged. The local integrals and/or input pairing carry that factor.

## B4. Polarized isogenies: rational degree can stay fixed while denominators grow

**Statement.** Let $\psi:A\to B$ be an isogeny of $g$-dimensional polarized abelian varieties. Suppose $\psi^*c_1(L_B)=c\,c_1(L_A)$ and $L_A,L_B$ have the same polarization degree. For a codimension-$p$ cycle $Z$,
\[
 \deg\psi=c^g,\qquad
 \deg_{L_A}(\psi^*Z)=c^p\deg_{L_B}Z.
\]

**Proof.** Integrating the $g$th power of the polarization identity gives the first equality. By projection formula,
\[
 \int_A\psi^*[Z]c_1(L_A)^{g-p}
 =c^{-(g-p)}\deg\psi\int_B[Z]c_1(L_B)^{g-p},
\]
which is the second. QED.

The rational cycle $c^{-p}\psi^*Z$ has unchanged degree but its displayed coefficient has denominator $c^p$ when $c$ is an integer. For multiplication by $m$ on a fixed variety, $c=m^2$. This is not a proof that all representatives have large denominators: it is a precise diagnosis of the natural pullback representative.

## B5. A rigorous norm-to-degree bridge for surface maps

**Statement.** Let $Y$ be a smooth projective surface, $\omega$ a Kähler class, $V=\int_Y\omega^2$, and $f:Y\to A$ a morphism with two-dimensional image $Z$ and generic degree $\delta$. Choose a translation-invariant representative $\omega_A\in c_1(L)$ of a polarization, and invariant holomorphic forms $\alpha_1,\ldots,\alpha_g$ such that $\omega_A=i\sum_j\alpha_j\wedge\bar\alpha_j$. Put
\[
 E_f=\int_Y f^*\omega_A\wedge\omega
 =\sum_j\|f^*\alpha_j\|_\omega^2,\qquad
 \|u\|_\omega^2=i\int_Yu\wedge\bar u\wedge\omega.
\]
Then
\[
 \deg_L Z=\frac{\int_Y(f^*\omega_A)^2}{\delta}
 \leq\frac{E_f^2}{\delta V}.
\]

**Proof.** Proper pushforward gives $f_*[Y]=\delta[Z]$ and projection formula gives the equality. With $\beta=f^*\omega_A$, decompose $\beta=(E_f/V)\omega+\beta_0$, where $\int\beta_0\omega=0$. The Hodge index theorem on the surface gives $\int\beta_0^2\leq0$, so $\int\beta^2\leq E_f^2/V$. The displayed energy identity follows by linearity from the specified polarization representative. QED.

This is a direct application of the classical surface Hodge index theorem in a form adapted to the present problem, not a claim to reprove that theorem. Under a cover of degree $d$, $E_f$ and $V$ both scale by $d$. Thus the bound $E_f^2/V$ for the degree of the pushforward class scales by $d$. For the reduced image, the generic mapping degree $\delta$ also scales by $d$, and the displayed bound remains unchanged; this matches B3 exactly.

For the sufficiently deep principal ball-quotient surfaces used in 032, the actual pullbacks $f^*\alpha_j$ do have finite expansions $\sum_a b_{ja}\theta_a$ in genuine integrated theta lifts from characters of one-dimensional unitary groups. The existence of these expansions is supplied by Bergeron--Millson--Mœglin, *The Hodge conjecture and arithmetic quotients of complex balls*, Acta Math.216 (2016), Theorem 9.1, pp.73--75, with the range in §9.1, p.72: for $m=3$ and $(a,b)=(0,1)$, its condition is $4<6$. The supplied van Hoften--Sempliner paper makes the all-$H^{1,0}$ spanning conclusion explicit in the proof of Proposition 4.1.8, pp.15--16; Proposition 3.1.7, p.11, identifies the oscillator constituents. The published BMM proof and the supplied Proposition 4.1.8 proof were read. This is imported classification/spanning, not a new proof of those theorems.

For completeness, only finitely many direct-limit theta vectors are needed for each fixed form. Put them at a common finer level and average over the desired compact open subgroup. The original form is invariant, and equivariance moves the finite average to the Schwartz inputs, so the expansion exists at that level. Equality in $H^{1,0}$ is equality of holomorphic forms by the injectivity into Betti cohomology for a compact Kähler variety. If necessary one first deepens the principal level so the arithmetic $U$ and $SU$ groups agree: their determinant values are norm-one algebraic units, hence roots of unity, and sufficiently deep congruence kills the finite set of nontrivial roots. T6.9 gives the full argument and its scope.

With norm squares $Q_a$ computed by a valid rank-one Rallis formula, and with the scalar/geometric metric and measure conversions included in $Q_a$, the triangle inequality gives the concrete bound
\[
 \deg_L Z\leq\frac{1}{\delta V}
 \left\{\sum_j\left(\sum_a|b_{ja}|\sqrt{Q_a}\right)^2\right\}^2.
\]
The existence gate is therefore removed. What remains is a quantitative bound on the coefficients $b_{ja}$ relative to the integral Hom lattice, together with CM periods, test-vector factors and metric/measure normalization. Orthonormalizing the theta basis does not control those integral coefficients. B10 below reduces them to an integral energy-lattice covolume estimate, and B11 shows exactly why that estimate cannot be inferred from finite generation or orthonormalization alone.

## B6. Fixed generic-field projector onto Weil classes

**Setup.** Let $A$ be a polarized abelian variety of dimension $2n$, carrying an action of an order $\mathcal O\subset K$ in an imaginary quadratic field. Assume the Rosati involution restricts to conjugation on $K$ and the two eigenspaces in $H^{1,0}$ both have dimension $n$ (Weil type). Let
\[
 W=\bigwedge_K^{2n}H^1(A,\mathbb Q)\subset H^{2n}(A,\mathbb Q).
\]
Here the inclusion means the rational rank-two subspace whose complexification is the sum of the two extreme $K$-eigenlines. Choose a nonzero $a\in\mathcal O$ such that $a/\bar a$ is not a root of unity, and let $T=[a]^*$ on cohomology. Such an $a$ exists: only finitely many arguments arise from roots of unity in $K$, whereas the arguments of nonreal elements $M+\tau$ for a fixed nonreal $\tau\in\mathcal O$ vary with integers $M$ and tend to zero.

**Statement.** There is a polynomial $P(X)\in\mathbb Z[X]$ and a positive integer $R$, depending only on $(K,n,a)$, such that $e=P(T)/R$ is the projector onto $W$ on $H^{2n}$. It is induced by a fixed rational algebraic correspondence and is self-adjoint for the Poincaré pairing on that degree. Its denominator is independent of the CM point or Hecke level. One possible choice is
\[
 \lambda_r=a^r\bar a^{2n-r}\ (0\leq r\leq2n),\quad
 f_W(X)=(X-a^{2n})(X-\bar a^{2n}),\quad
 f_R(X)=\prod_{r=1}^{2n-1}(X-\lambda_r),\quad
 R=\operatorname{Res}(f_W,f_R)>0,
\]
with $P=vf_R$ for integral polynomials satisfying $u f_W+v f_R=R$.

**Proof.** Decomposing $H^1_\mathbb C=V_a\oplus V_{\bar a}$, each summand has dimension $2n$, and
\[
 H^{2n}_\mathbb C=\bigoplus_{r=0}^{2n}\bigwedge^rV_a\otimes\bigwedge^{2n-r}V_{\bar a}.
\]
The corresponding eigenvalues are $\lambda_r$. They are distinct since $a/\bar a$ has infinite order. Each polynomial displayed is fixed by conjugation and has algebraic-integer coefficients, hence lies in $\mathbb Z[X]$; the two factors are coprime. The Sylvester matrix for these monic polynomials has determinant their resultant. Multiplying that matrix by its integral adjugate and extracting the column corresponding to the constant polynomial gives integral $u,v$ with $u f_W+v f_R=R$ (a simultaneous sign change adjusts the determinant convention). Thus $P/R$ takes value one at the two extreme eigenvalues and zero at every other eigenvalue. Since $T$ is diagonalizable, it is the asserted projector.

Every power $T^j$ is induced by pullback along the algebraic isogeny $[a^j]$, so the polynomial defines an algebraic correspondence. Its cohomological projector property is what is asserted: **no Chow-group identity $e^2=e$ is claimed** merely from this calculation. For a full homological-motive statement, compose it with the algebraic degree projector $\pi_{2n}=\prod_{j\ne2n}([2]^*-2^j)/(2^{2n}-2^j)$, where $0\leq j\leq4n$; this acts as the identity on $H^{2n}$ and as zero in all other degrees. Thus it defines an idempotent on $h^{2n}$ in homological motives, and on numerical cycle classes, without claiming a Chow idempotence relation.

To prove self-adjointness on this degree, the Poincaré pairing of two $T$-eigenvectors can be nonzero only if $\lambda_r\lambda_s=\deg[a]=N(a)^{2n}$: this follows by applying $[a]^*$ to their product in top degree. Infinite order of $a/\bar a$ makes this condition exactly $r+s=2n$. Consequently the two extreme eigenlines pair only with each other and are orthogonal to all the intervening eigenspaces. Projection onto their sum is Poincaré-self-adjoint. Finally, $R=f_R(a^{2n})\overline{f_R(a^{2n})}>0$. QED.

A useful explicit expression is
\[
 R=N(a)^{n(2n-1)}\prod_{k=1}^{2n-1}|a^k-\bar a^k|^2.
\]
It follows by factoring $f_R(a^{2n})=a^{n(2n-1)}\prod_{k=1}^{2n-1}(a^k-\bar a^k)$ and taking the field norm.

If $P=\sum_jb_jX^j$, put
\[
 B_P=\sum_j|b_j|N(a)^{jn}.
\]
For effective codimension-$n$ cycles $Z$ of degree $D$, $P([a]^*)Z$ is an integral signed cycle whose positive and negative parts both have degree at most $B_PD$. Indeed $[a]^*c_1(L)=N(a)c_1(L)$ by the Rosati condition, so B4 gives degree multiplier $N(a)^n$ for pullback on codimension $n$; use it term by term. This works fibrewise in any family with the fixed action and polarization data.

## B7. Uniform Weil-component bound from effective degree

**Statement.** In B6 put $\omega=c_1(L)$, $V_A=\int_A\omega^{2n}/(2n)!=\chi(L)$, and
\[
 q(u,v)=(-1)^n\int_Au\wedge v\quad(u,v\in W_\mathbb R).
\]
Then $q$ is positive definite. For every effective $n$-cycle $Z$ of degree $D=\int_Z\omega^n$,
\[
 \|e[Z]\|_q\leq\frac{D}{n!\sqrt{V_A}}.
\]
The constant depends only on polarization type and $n$, hence is uniform on the whole Weil family, without a compactness restriction on its base.

**Proof.** The Rosati identity makes $\omega$ a mixed-eigenvalue class in $V_a\otimes V_{\bar a}$: its $[a]^*$ eigenvalue is $N(a)$ on degree two, different from $a^2$ and $\bar a^2$. Wedge product by $\omega$ kills each extreme degree-$2n$ eigenline because it would require $2n+1$ vectors in one $2n$-dimensional eigenspace. Thus $W$ is primitive. Weil type makes both lines of Hodge type $(n,n)$. The Hodge–Riemann bilinear relations give positivity of $q$; the Hodge star on these primitive middle-degree real classes is $*=(-1)^n$.

Give $A$ its flat translation-invariant metric associated with $\omega$. Every harmonic form is translation invariant, so for its harmonic representative $\eta\in W_\mathbb R$, the pointwise Euclidean norm is constant and equals $\|\eta\|_q/\sqrt{V_A}$. Its comass is at most its Euclidean norm. The complex analytic cycle $Z$ has volume $D/n!$ by Wirtinger's identity, with multiplicities; its singular locus has measure zero. Therefore
\[
 \left|\int_Z\eta\right|\leq\frac{D}{n!\sqrt{V_A}}\|\eta\|_q.
\]
By B6, $e$ is self-adjoint for Poincaré pairing, so for $w=e[Z]$,
\[
 \|w\|_q^2=|q(w,w)|=\left|\int_A[Z]\wedge w\right|=\left|\int_Zw\right|.
\]
If $w=0$ the result holds; otherwise apply the preceding inequality with $\eta=w$ and divide by $\|w\|_q$. QED.

## B8. Effective witness implies bounded division, with quadratic bounds

**Statement.** Keep a connected polarized Weil-type family as in B6, with a globally defined $\mathcal O$-action (after finite base change if necessary), fixed $n,K,a,L$, and fixed rational flat target $t\in W$. Put
\[
 \Lambda=W\cap H^{2n}(A,\mathbb Z),\qquad \delta_\Lambda=\det(q(e_i,e_j))>0
\]
for any integral basis of this rank-two saturated lattice. Choose $b\geq1$ with $\tau=bt\in\Lambda$, and write $h=N(a)^n$. The constants $V_A$, $\delta_\Lambda$, and $\|\tau\|_q$ are locally constant along the family and so fixed on a connected base.

Suppose a fibre contains an effective $n$-cycle $Z$ of degree $D$ with $e[Z]\ne0$. Then there are an integer $N\geq1$ and effective $Z^+,Z^-$ with
\[
 Nt=[Z^+]-[Z^-],
\]
where, with $M=RD/(n!\sqrt{V_A})$,
\[
 N\leq\frac{b h M^2}{\sqrt{\delta_\Lambda}},\qquad
 \deg Z^\pm\leq\frac{2h\|\tau\|_q M B_P D}{\sqrt{\delta_\Lambda}}.
\]
Thus both are $O(D^2)$, uniformly in the fibre. In particular a uniform bound for degrees of nonzero Weil witnesses on a Zariski-dense set gives bounded division on that set. The proper parameter-space argument of Route 2 then applies, once supplied separately with its stated hypotheses.

**Proof.** Let $V_Z=P([a]^*)Z$ as an integral signed cycle and $v=[V_Z]=R e[Z]$. This is a nonzero element of $\Lambda$, with $\|v\|_q\leq M$ by B7. The characteristic polynomial of $T$ on $W$ is $f_W$. Since $a/\bar a$ is not a root of unity, $a^{2n}$ is nonreal, so $f_W$ is irreducible over $\mathbb Q$. Hence $v,Tv$ are a rational basis of $W$: otherwise $v$ would be a rational eigenvector of $T$ with a rational eigenvalue.

Use any oriented integral basis of $\Lambda$. Its determinant
\[
 \Delta=\det(v,Tv)\in\mathbb Z\setminus\{0\}
\]
therefore satisfies $\Delta\tau=m v+\ell Tv$, where the integral Cramer numerators are $m=\det(\tau,Tv)$ and $\ell=\det(v,\tau)$. On $W$, $T$ is a similitude of $q$ of multiplier $\deg[a]=N(a)^{2n}=h^2$, so $\|Tv\|_q=h\|v\|_q$. The area of a parallelogram in this metric is $\sqrt{\delta_\Lambda}$ times its lattice determinant. The elementary area bound consequently gives
\[
 |\Delta|\leq hM^2/\sqrt{\delta_\Lambda},\quad
 |m|\leq\|\tau\|_q hM/\sqrt{\delta_\Lambda},\quad
 |\ell|\leq\|\tau\|_q M/\sqrt{\delta_\Lambda}.
\]
Let $N=b|\Delta|$, and let $C=\operatorname{sgn}(\Delta)(mV_Z+\ell[a]^*V_Z)$. Then $[C]=Nt$. By the final part of B6 the positive and negative degrees of $V_Z$ are at most $B_PD$, and those of $[a]^*V_Z$ are at most $hB_PD$. Splitting the signed cycle $C$ into positive and negative parts thus bounds each by
\[
 (|m|+h|\ell|)B_PD\leq 2h\|\tau\|_q M B_PD/\sqrt{\delta_\Lambda}.
\]
This proves the claim. The intersection lattice and its pairing vary as an integral local system, so its discriminant and the norm of a fixed flat target are constant; $V_A$ is fixed by polarization type. No choice of a global basis is needed to make the constants uniform. QED.

**Stronger exact index identity.** If $\mu=a^{2n}$ under the fixed complex embedding, then
\[
 |\Delta|=\frac{|\operatorname{Im}\mu|}{\sqrt{\delta_\Lambda}}\,\|v\|_q^2.
\]
Indeed $T$ is multiplication by the nonreal scalar $\mu$ on the real plane $W$, its characteristic polynomial has trace $2\operatorname{Re}\mu$, and it is a positive-orientation $q$-similitude. In a $q$-orthonormal basis it is the rotation-dilation matrix for $\mu$ or $\bar\mu$; the area of $(v,Tv)$ is $|\operatorname{Im}\mu|\|v\|^2$. Dividing by the lattice covolume proves the formula. This makes the last arithmetic index precise, without claiming it is automatically an automorphic $L$-value.

**The quadratic size is sharp for extraction from one lattice vector.** In the positive lattice $\Lambda=\mathbb Z[i]$, let $v=m+i$ and target $\tau=1$. If $N\tau$ belongs to the principal ideal $v\mathbb Z[i]$, then
\[
 \frac{N}{m+i}=\frac{Nm}{m^2+1}-i\frac{N}{m^2+1}\in\mathbb Z[i],
\]
so $m^2+1\mid N$. Since $\|v\|^2=m^2+1$, extraction using $v$ and any fixed integral multiplication operator can require an integer of quadratic size in $\|v\|$. This is an arithmetic sharpness statement for that extraction method. It does not establish growth of intrinsic cycle complexity, since other geometric cycles might represent the target more efficiently.

**What remains.** The theorem does not create $Z$ in the non-CM fibres, and 032 gives neither a uniform degree bound for such $Z$ on a dense orbit nor a deformation of one actual full cycle class. It proves that a separate unbounded full-CM-field projector is unnecessary in the Weil-family route. Once geometric witness degrees are bounded, the two-dimensional integral extraction is automatically bounded.

## B9. A precise failure of archimedean norm control for arbitrary projectors

On the lattice $\mathbb Z^2$ with Euclidean pairing, the orthogonal projector to $\mathbb Q(m,1)$ is
\[
 E_m=\frac1{m^2+1}\begin{pmatrix}m^2&m\\m&1\end{pmatrix}.
\]
It has operator norm one, while its exact common denominator is $m^2+1$, because its lower-right entry is $1/(m^2+1)$. The calculation follows by the rank-one projector formula $vv^t/(v^tv)$. This example already lives in $\operatorname{End}(\mathbf1\oplus\mathbf1)$ in homological or numerical motives: all matrices are algebraic correspondences between two copies of a point. It refutes any abstract inference from bounded archimedean projector norm to bounded integral denominator. It does not refute B6, which fixes the generic-field projector, or the existence of other bounded representatives in a geometric family.

Similarly $x_m=(1,1/m)$ has norm in $[1,\sqrt2]$ while its pairing with $(0,1)$ is $1/m$. Lower bounds for two individual norms therefore give no lower bound for the mixed period needed in 032. The positive continuous comparison used by 032 is a separate input, whose quantitative approximation costs must be controlled.

## B10. An integral Hom covolume bound replaces individual coefficient bounds

**Setup.** Let $Y$ be a smooth projective variety of dimension $d\ge1$, with an integral ample class $H$, and fix a base point for its Albanese map $\alpha:Y\to B=\operatorname{Alb}(Y)$. Let $(A_i,L_i)$ be polarized abelian varieties, for $1\le i\le k$. Put
\[
 \Lambda_i=\operatorname{Hom}(B,A_i),\qquad
 E_i(u)=\int_Y (u\alpha)^*c_1(L_i)H^{d-1},\qquad
 V=\int_YH^d.
\]
Here maps are homomorphisms; translations do not affect the forms, energies or degrees. Assume $r_i=\operatorname{rank}\Lambda_i>0$. Let $q_i$ be the real quadratic metric with square norm $E_i$, let $C_i$ be the Euclidean covolume of $\Lambda_i$ for $q_i$, and let $\mu_i>0$ be any known lower bound for $E_i(u)$ for nonzero integral $u$. One may always take $\mu_i=1$. Set
\[
 v_r=\frac{\pi^{r/2}}{\Gamma(1+r/2)},\qquad
 R_i=\frac{2^{r_i}}{v_{r_i}}\frac{C_i}{\mu_i^{(r_i-1)/2}}.
\]

**Statement.** The lattice $\Lambda_i$ contains $r_i$ independent homomorphisms $u_{ij}$, spanning $\Lambda_i\otimes\mathbb Q$, such that $E_i(u_{ij})\le R_i^2$. Suppose a specified real-multilinear period $P$ on $\prod_i(\Lambda_i\otimes\mathbb R)$ is nonzero. Some tuple of these homomorphisms has $P(u_{1j_1},\ldots,u_{kj_k})\ne0$. If the period is the integral of a wedge of $2d$ pulled-back one-forms, its nonvanishing implies that the product map
\[
 F=(u_{1j_1}\alpha,\ldots,u_{kj_k}\alpha):Y\longrightarrow\prod_i A_i
\]
has a $d$-dimensional image $Z$. For the product polarization $L=\bigotimes_i\operatorname{pr}_i^*L_i$, and the actual generic degree $\delta_F$ of $F$ onto $Z$,
\[
 \deg_L Z\le\frac{(\sum_iR_i^2)^d}{\delta_F V^{d-1}}.
\tag{B10.1}
\]
For 032, $d=2$ and $k=4$. More generally, if a target polarization $L'$ satisfies $B c_1(L)-c_1(L')$ nef for a known $B>0$, the right side is multiplied by $B^d$.

**Proof.** Homomorphisms inject into homomorphisms of their integral first homology lattices, so $\Lambda_i$ is a finitely generated free abelian group. Pullback on invariant one-forms depends linearly on the homomorphism. Writing a polarization as a positive sum of $i\eta\wedge\bar\eta$ shows that $E_i$ is a positive semidefinite real quadratic form. There is no nonzero integral vector in its kernel: if all pulled-back one-forms vanish on $Y$, the map $u\alpha$ has zero derivative and is constant; because $\alpha(Y)$ generates $B$ and both maps preserve the chosen origins, $u=0$. The intersection expression for $E_i$ is integral, so polarization gives a rational Gram matrix in every integral basis. A nonzero real kernel of a rational matrix contains a nonzero rational vector, and clearing its denominator would give a nonzero integral kernel vector. Thus the real kernel is zero and $q_i$ is positive definite. Its positive values on nonzero lattice vectors are at least one.

Let $\lambda_1\le\cdots\le\lambda_{r_i}$ be the successive minima of the Euclidean unit ball for this metric. Minkowski's second theorem gives
\[
 v_{r_i}\prod_j\lambda_j\le 2^{r_i}C_i.
\]
Since every $\lambda_j\ge\sqrt{\mu_i}$, one obtains $\lambda_{r_i}\le R_i$. The minima are attained, giving the required independent maps. They need not be an integral basis, and none is asserted: a rational spanning set is enough. If $P$ vanished on every tuple from these spanning sets, multilinearity would make it vanish identically, a contradiction. A map with image dimension smaller than $d$ pulls every smooth real $2d$-form back to zero, so the nonzero wedge period gives the image-dimension assertion.

For the degree bound, write $\beta=F^*c_1(L)$, a nef class. Its energy is $E=\beta H^{d-1}=\sum_iE_i(u_{ij_i})\le\sum_iR_i^2$. The mixed-intersection inequality
\[
 \beta^d\le\frac{(\beta H^{d-1})^d}{(H^d)^{d-1}}
\tag{B10.2}
\]
follows directly from surface Hodge index: for rational ample $\beta,H$, take smooth complete-intersection surfaces of suitable very ample multiples of $j-1$ copies of $\beta$ and $d-j-1$ copies of $H$, for $1\le j\le d-1$. Hodge index on each surface gives $a_j^2\ge a_{j-1}a_{j+1}$ for $a_j=\beta^jH^{d-j}$. These inequalities imply $a_d\le a_1^d/a_0^{d-1}$. Approximating nef $\beta$ by $\beta+\varepsilon H$ proves the required nef case by continuity. For $d=1$ it is equality, and for $d=2$ it is B5. Projection formula gives $\beta^d=\delta_F\deg_L Z$, proving (B10.1). Finally nefness of $Bc_1(L)-c_1(L')$ gives $E_{L'}\le B E_L$ after pullback and intersection with $H^{d-1}$, so the same argument proves the last assertion. QED.

**Exact imported lattice source.** Martin Henk, *Successive minima and lattice points*, arXiv:math/0204158v1, Theorem 1.3, printed p.2, and its proof in §3, printed pp.5--7, <https://arxiv.org/pdf/math/0204158>. The statement and complete proof were read; only the displayed upper-product inequality is imported here.

**What determinant is required.** On the real Hom space, let $w_1,\ldots,w_r$ be a basis of normalized analytic vectors, with real Gram matrix $G$. If the columns of $B$ express an integral basis of $\Lambda$ in these coordinates, then exactly
\[
 C_\Lambda^2=\det(B^{\mathsf t}GB)=|\det B|^2\det G.
\tag{B10.3}
\]
Replacing the analytic basis by an orthonormal one replaces $B$ by $G^{1/2}B$ and preserves this covolume. Rallis can contribute to $G$ after the CM-period and measure comparisons are fixed; it does not identify $B$. If $\Gamma=\sum\mathbb Zw_j$ is commensurable with $\Lambda$, then
\[
 \frac{C_\Lambda}{C_\Gamma}
 =\frac{[\Gamma:\Gamma\cap\Lambda]}{[\Lambda:\Gamma\cap\Lambda]}.
\]
Thus a proved integral analytic sublattice $\Gamma\subset\Lambda$ with bounded Gram determinant already gives $C_\Lambda\le C_\Gamma$; no saturation-index upper bound is then needed. If instead $\Lambda\subset\Gamma$, its index contributes in the numerator and must be bounded. A uniform integer $M$ with $M\Gamma\subset\Lambda$ gives the sufficient bound $C_\Lambda\le M^r\sqrt{\det G}$. This identifies the exact direction of the integral comparison that a theta-index theorem would have to supply.

**Variation and normalization.** The ranks $r_i$ may grow when genuinely new cohomology appears at deeper source levels. Neither a rank-independent constant nor a uniform covolume is supplied by finite generation. For the fixed sublattice of old maps pulled through a degree-$e$ cover of the source, pull back $H$ as well. Then $E_i\mapsto eE_i$, $C_i\mapsto e^{r_i/2}C_i$, and a known $\mu_i$ becomes $e\mu_i$. Consequently $R_i\mapsto\sqrt e R_i$, $V\mapsto eV$, and $\delta_F\mapsto e\delta_F$; the reduced-image bound (B10.1) is unchanged. The actual generic degree in that bound must be retained. Replacing it by the trivial lower bound one can lose an essential cancellation. This proposition gives a sufficient determinant criterion for producing a small witness from prescribed source lattices. It is not a necessary condition for intrinsic bounded witness degree.

## B11. A fixed-order CM Hecke example separates the Hom regulator from witness degree

Let
\[
 E=\mathbb C/(\mathbb Z+i\mathbb Z),\qquad
 E_m=\mathbb C/(\mathbb Z+mi\mathbb Z),\quad m\ge1,
\]
with their degree-one polarizations. Then
\[
 \operatorname{Hom}(E,E_m)=m\mathbb Z[i],\qquad
 \deg(m(a+bi))=m(a^2+b^2).
\tag{B11.1}
\]
In particular the least positive degree grows with $m$, despite fixed rank and fixed CM field.

**Proof.** A homomorphism is multiplication by a complex number $\gamma$ with $\gamma\mathbb Z[i]\subset\mathbb Z+mi\mathbb Z$. Write $\gamma=x+mi y$ with $x,y\in\mathbb Z$. The further requirement $i\gamma\in\mathbb Z+mi\mathbb Z$ forces $m\mid x$. Thus $\gamma=m(a+bi)$, and the converse is immediate. The degree is the index of $\gamma\mathbb Z[i]$ in the target lattice, namely $|\gamma|^2/m=m(a^2+b^2)$. These elliptic curves are algebraic and have CM; multiplication by $m$ gives a degree-$m$ isogeny, so they lie in one polarized Hecke orbit. QED.

Here is a version with a fixed integral quadratic action and actual Weil witnesses. Put $A_m=E_m^4$ with product principal polarization $L_m$, and let $\mathbb Z[i]$ act by sending $i$ to
\[
 J=\operatorname{diag}\left(
 \begin{pmatrix}0&-1\\1&0\end{pmatrix},
 \begin{pmatrix}0&-1\\1&0\end{pmatrix}\right).
\]
This is an integral action for every $m$, has Rosati involution $J^\dagger=-J$, and has multiplicities $(2,2)$ on $H^{1,0}$, so $A_m$ is of Weil type for the same order. The diagonal isogeny $E^4\to E_m^4$ given by multiplication by $m$ commutes with this action and pulls the target polarization back to $m$ times the source polarization. Thus the example stays in the corresponding polarized quadratic-action Hecke orbit.

Let $Y=E^2$, $H$ its product degree-one polarization, and consider
\[
 f_m(x,y)=(mx,0,my,0),\qquad
 Z_m=E_m\times\{0\}\times E_m\times\{0\}\subset A_m.
\]
The image has $\deg_{L_m}Z_m=2$. Its Weil projection is nonzero: the extreme $i$-eigenline contains the nonzero $(2,2)$-form
\[
 (dz_1+i\,dz_2)\wedge(dz_3+i\,dz_4)
 \wedge(d\bar z_1+i\,d\bar z_2)
 \wedge(d\bar z_3+i\,d\bar z_4),
\]
whose restriction to $Z_m$ is $dz_1\wedge dz_3\wedge d\bar z_1\wedge d\bar z_3$ and has nonzero integral. Pairing with this Weil form detects the nonzero projection, by the Poincaré self-adjoint projector in B6.

The full fixed-source Hom lattice is
\[
 \operatorname{Hom}(E^2,A_m)=M_{4\times2}(m\mathbb Z[i]),
\]
of rank $16$. In the integral basis furnished by the real and imaginary matrix units, its energy metric is $m I_{16}$: the polarization form on $E_m$ is $\frac{i}{2m}dz\wedge d\bar z$, so multiplication by $m\gamma$ contributes $m|\gamma|^2$ to the energy. Consequently its least nonzero energy is $m$, its Gram determinant is $m^{16}$, and its metric covolume is $m^8$. Orthonormalizing the analytic coordinates transfers the factor $\sqrt m$ to the integral coefficients and changes none of these intrinsic metric quantities.

For the selected two-dimensional map, however,
\[
 f_m^*c_1(L_m)=mH,\quad
 E_{f_m}=2m,\quad V=H^2=2,\quad \delta_{f_m}=m^2,
\]
and therefore
\[
 \frac{E_{f_m}^2}{\delta_{f_m}V}=2=\deg_{L_m}Z_m.
\]
All assertions follow by the lattice-index calculation, product intersection, and the displayed invariant form. This supplies a precise counterexample to any claim that finite generation or an orthonormal analytic basis uniformly bounds integral map energy on a CM Hecke orbit. At the same time it supplies bounded nonzero Weil witnesses. It therefore does **not** refute intrinsic bounded division; it shows that a raw Hom-regulator bound is sufficient but unnecessary, and that generic-degree cancellation is mathematically essential.

## B12. The exact geometric quantity is an infimum of normalized energies

For a polarized Weil-type abelian $2n$-fold $(A,L)$, let $D_W(A,L)$ be the least degree of an effective integral $n$-cycle with nonzero Weil projection, or $+\infty$ if none exists. Then
\[
 D_W(A,L)=\inf_{(Y,f,H)}
 \frac{\bigl(f^*c_1(L)\cdot H^{n-1}\bigr)^n}
 {\delta_f (H^n)^{n-1}},
\tag{B12.1}
\]
where $Y$ runs over smooth projective $n$-folds, $f:Y\to A$ over morphisms generically finite onto an image $Z$ with nonzero Weil projection, $\delta_f$ is the generic mapping degree, and $H$ runs over integral ample classes on $Y$. The infimum of the empty set is understood to be $+\infty$.

**Proof.** The mixed-intersection inequality B10.2 and projection formula show that every expression on the right is at least $\deg_L Z\ge D_W(A,L)$. If a witness exists, at least one irreducible component has nonzero Weil projection and no larger degree. Positive degrees are integers, so a least-degree irreducible witness $Z$ exists. Take a projective resolution $f:Y\to Z\subset A$, with $\delta_f=1$, and put $\beta=f^*c_1(L)$. This is integral, big and nef, and $\beta^n=\deg_L Z=D_W(A,L)$. Fix an integral ample $H_0$. The classes $H_j=j\beta+H_0$ are integral ample. As $j\to\infty$,
\[
 \beta H_j^{n-1}=j^{n-1}D_W+O(j^{n-2}),\qquad
 H_j^n=j^nD_W+O(j^{n-1}).
\]
For $n=1$ the expression is already equality; for $n\ge2$ the quotient in B12.1 tends to $D_W$. This proves the reverse inequality and hence equality. QED.

This is an exact variational characterization, not an effective construction. It explains what a successful automorphic estimate would have to control: normalized energies for some witnesses, allowing their actual mapping degrees and source volumes. Requiring every theta coefficient or the entire Hom regulator to remain bounded is stronger than necessary. B10 provides one workable sufficient criterion with explicit constants. B11 shows why it is not an equivalence on a prescribed source. The infimum in B12 allows resolutions and polarizations of the unknown witnesses, so it does not close the open existence or uniformity problem by itself.

## B13. A fixed general-type surface bounds mapping degree to a simple target

**Statement.** Let $Y$ be a fixed smooth projective surface of general type, and let $f:Y\to A$ have surface image $Z$ in a simple abelian variety of dimension strictly greater than two. Then
\[
 \delta_f\operatorname{vol}(K_{\widetilde Z})
 \le \operatorname{vol}(K_Y),\qquad
 \delta_f\le \operatorname{vol}(K_Y),
\tag{B13.1}
\]
where $\widetilde Z$ is any smooth projective model of $Z$. In particular, if $Y$ is a compact ball quotient, then $\delta_f\le K_Y^2$. No smoothness assumption on $Z$ and no unramifiedness assumption on $f$ is required.

**Proof.** A proper positive-dimensional subvariety of a simple abelian variety is of general type by Ueno's theorem. Its Kodaira dimension is defined using a nonsingular model, so this applies even when $Z$ is singular. The induced dominant rational map $Y\dashrightarrow\widetilde Z$ has degree $\delta_f$. The canonical-volume inequality for generically finite rational maps of varieties of general type gives the first inequality in (B13.1). One way to see the mechanism is to resolve the map, use the effective ramification divisor to compare the canonical class with the pullback of the target canonical class, and then use birational invariance, monotonicity, and finite-map scaling of volume. A smooth minimal model of a surface of general type has nef and big canonical divisor, whose square is a positive integer; its canonical volume is that square. Hence $\operatorname{vol}(K_{\widetilde Z})\ge1$, proving the second inequality. For a compact ball quotient, $K_Y$ is ample and its volume is $K_Y^2$. QED.

**Exact imported sources.** Kenji Ueno, *On Kodaira Dimensions of Certain Algebraic Varieties*, Proc. Japan Acad.47 (1971), pp.157--159, §3, Corollary after Proposition 2, printed p.158; the birational definition appears in §2, p.157. The note announces the theorem and says details will appear elsewhere; the whole note and the exact corollary were read, without claiming to have checked an absent full proof. Primary original: <https://www.jstage.jst.go.jp/article/pjab1945/47/2/47_2_157/_pdf>. The word "proper" is retained explicitly here, since the ambient abelian variety itself is not of general type. Lucio Guerra and Gian Pietro Pirola, *On the finiteness theorem for rational maps on a variety of general type*, arXiv:0807.2980v2, §3.2, Proposition 3.2(2), printed pp.10--11, gives the canonical-volume inequality; its complete short proof was read. Primary: <https://arxiv.org/pdf/0807.2980>. Their later paper *Parametrization of rational maps on a variety of general type, and the finiteness theorem*, arXiv:1203.2246v1, §1(b), printed pp.2--3, explicitly records the surface lower bound $\epsilon_2=1$ and the degree-volume inequality. Primary: <https://arxiv.org/pdf/1203.2246>.

This is a strict refinement for a fixed ball-quotient source and a simple target: the unbounded generic-degree cancellation in B11 cannot occur there. It is not an energy estimate or a bound for all image degrees. For an étale source cover of degree $e$, the canonical volume itself scales by $e$, consistently with B3 and B10. The actual 032 target is generally a product, so simplicity is an additional hypothesis and must not be silently imposed. More generally the first inequality holds whenever the image has a general-type smooth model, without assuming the ambient target is simple.


## Computation attached to B6

`weil_projector_certificate.py` constructs the projector for $K=\mathbb Q(\omega)$, $\omega^2+\omega+1=0$, $a=3+\omega$ (trace 5, norm 7), for $n=2,3,4$, and checks exact polynomial idempotence modulo $f_W f_R$. It also checks the norm-product resultant formula. This is a computation checking those examples, not a formal proof of B6 for all $n$. For $n=2$, for example,
\[
 f_W=X^2-23X+2401,\quad f_R=X^3-126X^2+6174X-117649,
\]
\[
 R=25\,729\,836\,300.
\]
Reducing rational polynomial coefficients gives a smaller possible denominator $476\,478\,450$ in this example. Minimality here means the least common denominator of this unique degree-$\leq4$ interpolation polynomial, not a claim of a minimal denominator among all algebraic projector correspondences.

## Review of approach paths

1. Tried direct GRH bound at the asserted edge. Refined by checking the actual Rallis dimensions: genuine torus-to-three-dimensional lift is at $3/2$, and B1 is stronger and unconditional for the global factor.
2. Tried transfer from theta norm to degree. Direct identity is not justified; B5 supplies a valid inequality conditional on controlling all actual polarization coordinate pullbacks.
3. Tried conductor control along principal levels. B3 gives exact presentation growth and shows conductor is not level; no inference to intrinsic $c(s)$ is made.
4. Tried use of bounded arbitrary projector norms. B9 refutes it. Replaced it by the fixed polynomial projector B6 in the generic $K$-action.
5. Tried treating the resulting rank-two coefficient index as a separate unbounded gate. B7 and B8 remove it once an effective degree bound is given, with explicit quadratic bounds. The residual gate is uniformly bounded effective witnesses with nonzero Weil component, or deformation of a full class that supplies them.

## Suggested exact Grothendieck placement, to be independently source-checked by root

B6 concerns algebraic correspondences and primitive projectors in homological/numerical motives; B7 uses the Hodge standard positivity and the primitive Lefschetz decomposition; B8 concerns integral lattices underlying those motives together with proper cycle parameter spaces. The attached sketch points to cote 16 scans 44–50 for the standard-conjecture correspondence framework. No original archive scans are supplied here; this report does not claim to have read or corrected their transcription. Root must cite exact EGA/SGA/FGA and archive locators only after actual verification.

## Additional checked classical sources for B5 and B7

- Eduardo Cattani, *Introduction to Kähler manifolds*, ICTP June 2010 preliminary notes, §5.3, Proposition 5.15 and Theorem 5.17, printed p.38: the primitive Hodge-star formula and Hodge–Riemann positivity. Example 5.19 and equation (5.23), printed pp.39–40, specialize to the surface Hodge inequality. The displayed statements and the adjoining positivity proof were read. Source: <https://people.maths.ox.ac.uk/joyce/Nairobi2019/CattaniKahlerManifolds.pdf>. These are classical imported results; this report does not claim an independent proof of the full Hodge–Riemann theorem.
- Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, version 21 June 2012, Chapter III, §1.D, equation (1.24) and Wirtinger's inequality (1.25), printed pp.136–137: analytic-cycle volume and its linear-algebra proof. Source: <https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf>. Demailly uses $\omega_D=i\sum h_{jk}dz_j\wedge d\bar z_k$ and the real metric $\operatorname{Re}h$, giving $\omega_D^p/(2^p p!)$. For the same real metric our convention is $\omega=\omega_D/2$, so this is precisely $\omega^p/p!$ as used in B7. The formula and proof were read and the factor of two checked.

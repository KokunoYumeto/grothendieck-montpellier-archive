# T6 research report — DEG_L / rallis_t6

Date: 2026-11-21. Actor: GPT-6 Astra Pro, effort not exposed, child run `/root/rallis_t6`.
This report records checked reductions, not a claimed proof of T6 as originally phrased. The later T6.9 strengthens the early analytic gate: all needed one-form theta expansions do exist by the supplied human proof and checked literature; their coefficients and integral normalization remain to be bounded.

## 1. What the attached 032 construction actually supplies

Source: `OPENAI_032_The-rational-Hodge-conjecture-for-CM-abelian-varieties.pdf`, Proposition 3.1, printed pp. 11–12, equations (3.1)–(3.5); Corollary 3.2, p. 12; Proposition 4.6, p. 23; Corollary 4.7, pp. 24–25, equations (4.18)–(4.19); Corollary 6.7, p. 45; proof of Theorem 2.5, p. 46, equation (7.1).

Write $A=\prod_{i=1}^4B_i$, with each $B_i=B(v_i)$ of dimension $s$, and $n=4s$. In the nontrivial surface construction $s\ge2$, so $n\ge8$. The surface $S$ is a smooth projective ball quotient. The paper obtains rational Hodge maps $h_i:H^1(B_i,\mathbf Q)\to H^1(S,\mathbf Q)$ and integers $m_i>0$ so that $f_i:S\to B_i$ has $f_i^*=m_i h_i$. It defines
\[
f=(f_i),\quad z=f_*[S]\in CH^{n-2}(A),\quad
k=\int_S f_1^*\alpha_1\,f_2^*\alpha_2\,f_3^*\alpha_3\,f_4^*\alpha_4\ne0.
\]
The generators $\alpha_1,\alpha_2$ are holomorphic and $\alpha_3,\alpha_4$ antiholomorphic; their Betti coefficients are algebraic. With copied factors $B_i'$ and divisor kernels $D_i$ having pure class $\alpha_i\otimes\beta_i$, the correspondence $K=\prod_i q_i^*D_i$ gives
\[
\operatorname{cl}(K_*z)=k\,t_\beta,
\qquad t_\beta=\beta_1\otimes\beta_2\otimes\beta_3\otimes\beta_4.
\]
Thus three different quantities must be distinguished: the degree of the effective pushforward surface $z$; a mixed period $k$ detecting a switch line; and the codimension-two output $K_*z/k$ with algebraic coefficients. They have different degrees, codimensions, and positivity properties. The paper itself explicitly says that $z$ is a functional on the line, not a vector on it. It only proves $\dim f(S)=2$, not that $f$ embeds $S$.

The theta construction first supplies nonzero total two-forms and their mixed pairing. Section 7 then expands finite wedges, chooses a nonzero summand, expands each theta class in rational CM-map images, and chooses another nonzero summand. The final $k$ is not stated to be the total theta norm. No Rallis formula is stated in the attached 032 paper.

## 2. Checked findings

### DEG-L.T6.1 — Exact geometric degree and its positive Gram expression

Let $H$ be an ample line bundle on a complex abelian variety $A$ of dimension $n$, and let $f:S\to A$ be a morphism from a smooth projective surface with two-dimensional image. Put $z=f_*[S]$. Choose translation-invariant holomorphic one-forms $\omega_1,\ldots,\omega_n$ such that the invariant positive representative of $c_1(H)$ is
\[
\Omega_H={i\over2}\sum_{a=1}^n\omega_a\wedge\overline{\omega_a}.
\]
For $\eta_a=f^*\omega_a$ and $\xi_{ab}=\eta_a\wedge\eta_b$, one has
\[
\deg_H(z)=\int_S(f^*\Omega_H)^2
={1\over2}\sum_{a<b}\int_S\xi_{ab}\wedge\overline{\xi_{ab}}.
\tag{G1}
\]
If $e=[\mathbf C(S):\mathbf C(f(S))]$, then $z=e[f(S)]$ and $\deg_H(f(S))=\deg_H(z)/e$.

**Proof.** The projection formula gives the first equality. A positive definite Hermitian form can be diagonalized, giving the displayed expression for $\Omega_H$. Expanding its square and moving each antiholomorphic factor past the next holomorphic factor yields
\[
(f^*\Omega_H)^2={1\over4}\sum_{a,b}\eta_a\wedge\eta_b\wedge\overline{\eta_a}\wedge\overline{\eta_b}.
\]
The terms with $a=b$ vanish; the terms with $(a,b)$ and $(b,a)$ agree. This proves (G1). In local holomorphic coordinates, if $\xi=u\,dz_1\wedge dz_2$, then $\xi\wedge\bar\xi=4|u|^2dx_1dy_1dx_2dy_2$, so every summand is nonnegative. The assertion about $e$ is the definition of proper pushforward of an integral cycle. QED.

**Check.** Read the entire proof, independently recomputed both exterior-algebra signs and the factor $1/2$, and compared $A=S$ of dimension two with the standard Euclidean Kähler form. In that test, $\Omega_H^2=2\,dV$ and $\xi_{12}\bar\xi_{12}=4\,dV$.

**Meaning.** A degree is a positive sum of norms of all polarization-coordinate wedges. It is not the selected mixed period of four CM lines. Even when Rallis computes certain wedge norms, it takes additional data to identify every wedge in (G1), its automorphic spectral projections, and the conversion from invariant forms to algebraic Betti generators.

### DEG-L.T6.2 — Zero degree of the pure switch class

Give $A=\prod_{i=1}^4B_i$ the product polarization $H=\bigotimes_i\operatorname{pr}_i^*H_i$, where each $H_i$ is ample. Every class
\[
w\in H^1(B_1)\otimes H^1(B_2)\otimes H^1(B_3)\otimes H^1(B_4)\subset H^4(A)
\]
has
\[
\int_A w\,c_1(H)^{n-2}=0.
\tag{G2}
\]
Consequently a nonzero rational switch class cannot be the cohomology class of an effective codimension-two cycle for this polarization. A nonzero pure tensor $t_\beta$ also satisfies $t_\beta^2=0$.

**Proof.** Expand $c_1(H)^{n-2}$ into products $\prod_i\operatorname{pr}_i^*c_1(H_i)^{a_i}$. In factor $i$, the product with $w$ has degree $1+2a_i$, which is odd. Integration on $B_i$, of even real dimension $2\dim B_i$, therefore vanishes. Every term vanishes. Every nonzero effective cycle has strictly positive degree against an ample polarization, so (G2) rules out effectivity. For the last assertion, squaring a pure tensor repeats the same degree-one class in every factor, and the square of a degree-one class vanishes in characteristic zero. QED.

**Check.** Entire proof reread; parity argument checked separately for unequal factor dimensions and arbitrary sums of pure tensors. It does not say that a rational combination of conjugate switch lines has zero polarized self-pairing; that would be false. The statement about $t_\beta^2$ concerns one pure algebraic-coefficient tensor only.

**Meaning.** The output of 032, Proposition 3.1, has degree zero for a natural ample polarization. Therefore an equality between its degree and a nonzero positive theta norm cannot hold. The complexity $D$ in Route 2 is the separate degree of positive and negative effective representatives; (G2) does not bound it. For the input surface $z$, the ordinary square is already zero by codimension when $n\ge8$, since $2(n-2)>n$. A numerical self-intersection would require a different pairing and an explicit dualizing correspondence.

### DEG-L.T6.3 — Level alone does not determine the raw surface degree

Fix every datum through the rational maps $h_i$ and the source surface $S$ in 032, Proposition 3.1. Replacing all clearing integers $m_i$ by $Mm_i$ and $f_i$ by $[M]\circ f_i$ is still an allowed construction on exactly the same source level and with the same initial theta inputs. If $H$ is symmetric, then
\[
\deg_H(z_M)=M^4\deg_H(z),\qquad k_M=M^4k.
\tag{G3}
\]
Thus there is no degree of the raw pushforward surface determined by the level alone under the choices specified in 032.

**Proof.** Multiplication by $M$ acts as $M$ on $H^1(A)$ and as $M^2$ on $H^2(A)$, so $[M]^*c_1(H)=M^2c_1(H)$. Applying the projection formula twice gives $\deg_H([M]_*z)=\int_S f^*[M]^*c_1(H)^2=M^4\deg_H(z)$. Each of the four factors in the period acquires $M$. Positivity in T6.1 and the nonzero period guarantee $\deg_H(z)>0$. QED.

**Check.** Entire proof reread. The assertion concerns $f_*[S]$, the cycle defined by 032, not the reduced image $[f(S)]$; the generic mapping degree can change. Even a symmetric assumption is unnecessary for the cohomological degree identity, but retained for a standard polarization normalization.

### DEG-L.T6.4 — Auxiliary-cover division cancels in Chow

Keep the target $A$, kernels $K$, and algebraic generators fixed. For a finite surjective morphism $\pi:S'\to S$ of degree $d$ between smooth projective surfaces, use $f'=f\pi$ and the pulled one-forms. Then
\[
z'=d z,\quad k'=d k,\quad {K_*z'\over k'}={K_*z\over k}
\quad\hbox{in }CH^2(A')\otimes\overline{\mathbf Q}.
\tag{G4}
\]
In particular this applies to every deeper principal cover used in 032. Every fixed rational coefficient-descent combination gives one identical rational Chow class throughout the tower. A single rational representative therefore gives bounded $N,D$ throughout this auxiliary tower.

**Proof.** Proper pushforward gives $\pi_*[S']=d[S]$, and functoriality gives $z'=f_*\pi_*[S']=dz$. The integration formula for a finite map gives $k'=dk$; alternatively use its projection formula with the degree-four class on $S$. The correspondence action is linear, so the quotient is identical before taking any cycle-class map. Coefficient trace and rational linear combination commute with this identity. Once such a fixed rational cycle is written as a difference of effective cycles after clearing denominators, the same $N,D$ work at every cover. QED.

**Check.** Entire proof reread; arbitrary finite surjective maps work, although the 032 covers are finite étale. This proves division for auxiliary covers at a fixed abelian target. It does not transport a cycle to new targets in a dense Hecke orbit.

### DEG-L.T6.5 — Clearing-map division also cancels with biextension kernels

The divisor kernels in Proposition 3.1 may be chosen as algebraic linear combinations of birigidified Poincaré-type line bundles, without changing their Betti classes. For these choices, write $u=\prod_i[M_i]$ on $A$, with $M_i>0$. Then
\[
(u\times1)^*K=\Bigl(\prod_i M_i\Bigr)K
\quad\hbox{in }CH^4(A\times A')\otimes\overline{\mathbf Q}.
\]
Replacing $f_i$ by $[M_i]f_i$ leaves $K_*z/k$ unchanged in Chow.

**Proof.** For a divisor class $D$ on $B\times B'$, replace any representative line bundle $L$ by its birigidified part
\[
L^{\mathrm b}=L\otimes\operatorname{pr}_1^*(L|_{B\times0})^{-1}
\otimes\operatorname{pr}_2^*(L|_{0\times B'})^{-1},
\]
with the evident normalization of the fiber at $(0,0)$. Extend this operation linearly to the algebraic-coefficient divisor kernel. Since its prescribed Betti class is purely in $H^1(B)\otimes H^1(B')$, this operation leaves that class unchanged. A birigidified line bundle corresponds to a morphism $B'\to\widehat B$ sending zero to zero, hence to a homomorphism, and is the pullback of the Poincaré bundle. Its biextension property gives $([M]\times1)^*D=M D$ in $CH^1$. Multiplying the four kernel identities yields the displayed formula.

The projection formula for $u\times1$ then gives
\[
K_*u_*z=p'_*\bigl(p^*z\cdot(u\times1)^*K\bigr)
=\Bigl(\prod_iM_i\Bigr)K_*z.
\]
The period is multiplied by exactly the same product, because the four pullbacks on $H^1$ multiply by $M_i$. Division cancels in Chow. QED.

**Check.** Entire proof reread. The factor is $\prod_iM_i$, not $\prod_iM_i^2$. For common $M$ this is $M^4$, consistent with T6.3. The permitted change of representatives may alter the original unnormalized Chow class, but preserves its required Betti class and gives a valid 032 construction. The claim is not that an arbitrary representative of a pure cohomology divisor automatically has the exact biextension scaling in Chow.

**Grothendieck locator.** SGA 7 I, Exposé VII, §2.4, printed pp.164–165, states additivity in the three arguments; equation (2.4.2) specifically states additivity in the third argument. Example 2.9.5, printed p.175 (PDF p.180; internal VII43), identifies birigidified line bundles on a product of abelian schemes with \(\mathbf G_m\)-biextensions. Remark 2.9.6, printed p.176 (PDF p.181; internal VII44), gives \(\operatorname{Corr}(P,Q)\simeq\operatorname{Hom}(P,Q^\vee)\simeq\operatorname{Hom}(Q,P^\vee)\). Root visually verified these original scans in this run; this agent checked the transmitted locators against the claims used here and does not claim a separate scan inspection. Primary scan: <https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf>.

### DEG-L.T6.6 — A mixed period gives a lower, not upper, surface-degree estimate

Use a product polarization on $A$. Let the four chosen forms in the 032 period be supported on their four distinct factors, and let $r_i$ be their norms in the invariant Hermitian cotangent metric for $H$ (use $\bar\alpha_i$ for the last two holomorphic cotangent vectors). Then
\[
|k|\le (r_1r_2r_3r_4)\deg_H(z).
\tag{G5}
\]
There is no upper degree estimate from this single linear period over the cone of effective surface cycles.

**Proof.** The four unit forms $\alpha_1/r_1,\alpha_2/r_2,\bar\alpha_3/r_3,\bar\alpha_4/r_4$ are orthonormal because they lie on different polarized factors. Extend them to an orthonormal cotangent basis in T6.1. Cauchy–Schwarz and $2ab\le a^2+b^2$ give
\[
{|k|\over\prod_i r_i}\le {1\over2}(\|\xi_{12}\|^2+\|\xi_{34}\|^2)
\le\deg_H(z).
\]
For the final assertion, take a nonzero effective complete-intersection surface $Y$ with class a positive multiple of $c_1(H)^{n-2}$. Its pairing with the switch tensor is zero by T6.2, while its degree is positive. The effective cycles $z+mY$ all give the same mixed period and have degrees tending to infinity. QED.

**Check.** Entire proof reread; this is a statement about all effective cycles, not necessarily individual connected 032 ball-quotient images. The common-source scaling counterexample T6.3 addresses the actual construction's nonuniqueness separately. The lower bound depends on metric norms/CM periods of the generators; an L-value estimate for $k$ alone does not eliminate them.

## 3. What Rallis can actually compute, and the remaining explicit gate

Primary source: W. T. Gan, Y. Qiu, S. Takeda, *The regularized Siegel–Weil formula (the second term identity) and the Rallis inner product formula*, arXiv:1207.4709v3, §1.1, §11.6, §11.7 Theorem 11.4, printed pp. 54–55. URL: <https://arxiv.org/pdf/1207.4709>.

The theorem is about theta **integrals of specified automorphic representations**, not a kernel evaluated at an unspecified source point. For a unitary source of dimension $n_0$ and target of dimension $m$, its normalization uses $s_{m,n_0}=(m-n_0)/2$ and the standard value at $s_{m,n_0}+1/2$, retaining the splitting-character twist and normalized doubling integrals. In the rank-two source / rank-three target case it gives
\[
\langle\theta(\phi_1,f_1),\theta(\phi_2,f_2)\rangle
=2L(1,\pi\times\chi_V)\,Z^*(1/2,\phi_1\otimes\bar\phi_2,f_1,f_2),
\tag{R1}
\]
when the theorem's hypotheses and conventions hold. Here the target is globally anisotropic in 032, hence has Witt index zero, so the lower-tower vanishing condition is empty. The scalar automorphic inner product is converted exactly to the differential-form inner product in T6.10 below, including component/level volume.

For the rank-one source / rank-three target, the formal point is $3/2$ in unitary normalization; it lies outside the displayed dimensional range of Theorem 11.4. A convergent-range theorem must be used instead. The bounds agent located, and this agent independently opened and checked, J. Haan, *The Bessel period of U(3) and U(2) involving a non-tempered representation*, arXiv:1403.5061v7, §3.3, Theorem 3.4, printed p. 8. In its conventions the character-lift norm is
\[
\langle\theta(\bar f_1,\phi_1),\theta(\bar f_2,\phi_2)\rangle
={L_E(3/2,\mathrm{BC}(\tau)\otimes\gamma^3)\over L_F(3,\epsilon_{E/F})}
\prod_v Z_v^\#(1,f_{1,v},f_{2,v},\Phi_{1,v}).
\]
Its §3.6.1, p. 9, states absolute convergence and nonvanishing of the numerator Euler product at $3/2$. Thus this particular global factor does not require GRH. The version is identified in the PDF itself; use the unversioned URL <https://arxiv.org/pdf/1403.5061>. Do not cite GQT §11.7, Theorem 11.4 for the rank-one/rank-three case.

The total theta tensor in 032, Proposition 4.6, uses a Hermitian plane $W$. Its dual partner is $U(W)$, not $U(1)$. Spectral projection can therefore require a representation of a unitary group of rank two. Its degree-two standard $L$-function is not automatically a Hecke-character $L$-function. No claim is made here that a particular nonabelian constituent must occur in the paper's chosen tensor: rather, character-only decomposition is a specific additional theorem to be proved, not a consequence of the mere existence of the theta kernel. All local zeta factors, level volume, input scalars and CM-period comparisons remain part of the equality.

The further attacks below complete the existential analytic comparison: T6.9 supplies every one-form theta expansion, T6.10 fixes the scalar/geometric normalization, T6.11 gives an exact finite Hecke-$L(3/2)$ energy formula and degree upper bound, and T6.12–T6.13 give an exact finite standard-$L(1)$ degree expression with all comparison/input data retained. What is still not supplied is an effective bound for those actual integral realization/input data on a varying target orbit. T6.7–T6.8 separately control period division and signed correspondence degrees once the geometric and kernel data are bounded.

The exact-cancellation findings T6.4 and T6.5 remove two avoidable sources of apparent denominator/level growth **before** pursuing that harder gate. They leave the meaningful quantities: primitive integral CM maps, their polarizations and periods, the genuinely new choices of source/correspondence, and their behavior when the abelian target varies on a Hecke orbit.

## 4. Approaches tried and their disposition

1. Direct identification of the final 032 class with a positive Rallis norm: refuted for product polarization by T6.2.
2. Identifying the selected four-form period with geometric degree: refuted in that form; exact replacement is T6.1, and T6.6 shows the selected period is only a lower-bound witness.
3. Defining raw degree as a function only of principal level: refuted without further normalization by T6.3.
4. Treating source-cover degree growth as a genuine obstruction to division: removed by the exact Chow cancellation T6.4.
5. Treating enlarged denominator-clearing maps as a genuine obstruction: removed after a legitimate biextension choice by T6.5.
6. Applying a rank-one Rallis formula directly to a rank-two wedge tensor: not justified. T6.12–T6.13 instead prove a finite cuspidal rank-two spectral expansion and standard-$L(1)$ identity. No character-only or single-value equality has been proved.
7. Bounding the surface degree using only one-form norms: positive alternative sent to the bounds agent. Subsequently strengthened by T6.9 below: existence of every needed theta expansion is established from the human proof, and T6.10 fixes the scalar/geometric measure conversion. Effective coefficient/integral and test-input bounds remain. Hodge index gives $\deg_H(z)\le E_f^2/\operatorname{vol}(S)$, where $E_f=\int_Sf^*\Omega_H\wedge\omega_S$. This could use rank-one theta decompositions, but the rational CM extraction does not by itself identify all polarization-coordinate pullbacks as theta lifts with controlled coefficients.

## 5. Source-check ledger

- 032 Proposition 3.1 and Corollary 3.2, pp.11–12: read entire statements and proofs, equations and codimension checked in this run. Imported CM theorem itself is background, not independently reproved.
- 032 Proposition 4.6 and Corollary 4.7, pp.23–25: read entire proofs to check fixed input, finite decomposition, dependence on arbitrary constant-line trivializations, and covering formula. No independent proof of analytic theta construction claimed.
- 032 Theorem 5.1 proof and Corollary 6.7, pp.44–45; Theorem 2.5 proof, p.46: read to track extraction from complex theta classes into algebraic Betti vectors and then rational maps. Extraction supplies spans, not a normalized unique cycle or coefficient bound.
- Gan–Qiu–Takeda §11.6 and Theorem 11.4: primary arXiv PDF read via web, with theorem range and normalized factors checked. This is use-and-recheck, not a reproof.
- SGA 7 I original scan: root visually verified Exposé VII §2.4 pp.164–165, Example 2.9.5 p.175 and Remark 2.9.6 p.176. This agent records that communicated check; no separate scan inspection or transcription correction is claimed.


## 6. Further checked attack: algebraic norm clears the period without a lower bound

### DEG-L.T6.7 — Integral coefficient normalization and trace division

Retain the 032 hypothesis that **every scalar conjugate** of each tensor $\alpha_i\otimes\beta_i$ is of type $(1,1)$; one algebraic-coefficient Hodge class without this hypothesis would not suffice. After rescaling the chosen algebraic Betti generators, fix a finite Galois field $L/\mathbf Q$, of degree $d$, containing all their coefficients. They may be taken in $H^1(B_i,\mathbf Z)\otimes\mathcal O_L$ and $H^1(B_i',\mathbf Z)\otimes\mathcal O_L$. The divisor kernels can then be chosen in $CH^1(B_i\times B_i')\otimes\mathcal O_L$, their product $K$ in $CH^4(A\times A')\otimes\mathcal O_L$, and the nonzero period $k$ lies in $\mathcal O_L$.

Let $N=|N_{L/\mathbf Q}(k)|$. For every $a\in\mathcal O_L$ the cycle
\[
C_a=\operatorname{Tr}_{L/\mathbf Q}\bigl(a(N/k)K_*z\bigr)\in CH^2(A')
\]
is integral and satisfies
\[
\operatorname{cl}(C_a)=N\,\operatorname{Tr}_{L/\mathbf Q}(a t_\beta).
\tag{G6}
\]
Thus clearing the algebraic period needs **no analytic lower bound** for $|k|$.

More explicitly, write $K=\sum_{j=1}^J a_j\Gamma_j$ with $a_j\in\mathcal O_L$ and integral Chow correspondences $\Gamma_j$. Put
\[
M=\max_\sigma|\sigma k|,\qquad B_j=\max_\sigma|\sigma(a a_j)|.
\]
Then $M\ge1$, $N\le M^d$, and the integral coefficient
\[
c_j=\operatorname{Tr}_{L/\mathbf Q}\bigl(a a_j N/k\bigr)
\]
satisfies $|c_j|\le d B_jM^{d-1}$. If $\Gamma_{j*}z=W_j^+-W_j^-$ with effective cycles of degrees at most $D_j$, then $C_a$ admits effective positive and negative parts of degrees at most
\[
dM^{d-1}\sum_j B_jD_j.
\tag{G7}
\]

**Proof.** The finitely many algebraic coordinates of the generators have a common integer denominator, so multiplying the generators clears it. For each $i$ the class $\alpha_i\otimes\beta_i$ is then an integral $\mathcal O_L$-linear combination of Betti classes. Expand it in an integral basis of $\mathcal O_L$. Its coefficient classes in integral cohomology are all of type $(1,1)$: scalar conjugation preserves the Hodge property of the whole tensor, and the embedding matrix of the integral basis is invertible, so each coefficient is a complex linear combination of these conjugate $(1,1)$ classes. The integral Lefschetz $(1,1)$ theorem supplies line bundles for the integral coefficient classes. Choosing their birigidified parts as in T6.5 preserves the required class. This produces the integral-coefficient kernels. Pullback by actual morphisms, cup product and evaluation on the integral fundamental class show $k\in\mathcal O_L$.

The monic characteristic polynomial of the algebraic integer $k$ shows $N/k\in\mathcal O_L$ (equivalently, up to sign it is the product of all conjugates except the identity embedding). Hence every $c_j$ is an integer, and taking traces of $\operatorname{cl}(K_*z)=kt_\beta$ proves (G6). Since $N$ is a nonzero integer and $N\le M^d$, one has $M\ge1$. For each embedding $\sigma$,
\[
|\sigma(N/k)|=\prod_{\tau\ne\sigma}|\tau(k)|\le M^{d-1}.
\]
Triangle inequality for the trace gives the coefficient estimate. Replace $c_jW_j$ by $|c_j|W_j^+-|c_j|W_j^-$ if $c_j\ge0$, and interchange signs if $c_j<0$. Adding all positive and negative parts proves (G7). QED.

**Check.** Entire proof reread, including integral coefficient descent, the distinction between an integral basis of $\mathcal O_L$ and a basis of eigenvectors, and the trace bound when $k$ lies in a proper subfield. Repeated conjugates cause no problem. No lower bound for any individual $\sigma k$ was used.

**Scope.** The targets $\operatorname{Tr}(a t_\beta)$ are integral Hodge classes. An arbitrary prescribed rational class in their rational span may require a further rational coefficient $a$ and a clearing integer. Bounding that integral spanning index is a remaining lattice problem; it is not suppressed by this theorem. Rescaling the generators changes their metric sizes and the kernels, so it is not a uniformity argument by itself.

### DEG-L.T6.8 — Explicit signed-degree bound for the four divisor kernels

Let $A,A'$ have dimension $n$, with polarizations $H,H'$, and put $\mathscr L=p^*H\otimes p'^*H'$ on $A\times A'$. Let $D_1,\ldots,D_4$ be integral divisor classes. Choose expressions $D_i=D_i^+-D_i^-$ with $D_i^\pm$ represented by basepoint-free effective divisors, and positive integers $b_i$ such that both $D_i^\pm$ and $b_i c_1(\mathscr L)-D_i^\pm$ are nef. Such choices exist for every fixed divisor class after tensoring with a sufficiently high power of an ample bundle. Let $z$ be an effective surface cycle on $A$. Then
\[
(D_1D_2D_3D_4)_*z=W^+-W^-,
\]
with effective codimension-two cycles on $A'$ satisfying
\[
\deg_{H'}W^\pm\le48\Bigl(\prod_i b_i\Bigr)\,(H'^n)\,\deg_H z.
\tag{G8}
\]

**Proof.** Expand the product of four differences into sixteen signed products. For each product choose the four divisors successively in their basepoint-free linear systems so that they meet each component of $z\times A'$ properly. The resulting intersection cycle is effective; proper pushforward is effective, with components whose dimension drops contributing zero. Its degree is the intersection of that product with $p'^*c_1(H')^{n-2}$ on $z\times A'$.

Replacing one nef divisor $D_i^\pm$ by $b_i c_1(\mathscr L)$ increases or preserves this intersection, since the difference and the other divisors are nef. Iterating bounds the degree by
\[
\Bigl(\prod_i b_i\Bigr)
\int_{z\times A'}(p^*c_1(H)+p'^*c_1(H'))^4p'^*c_1(H')^{n-2}.
\]
Only the term with two factors from $A$ and two from $A'$ contributes. Its binomial coefficient is $\binom42=6$, and its integral is $6\deg_H(z)(H'^n)$. There are eight terms of each sign. Summing them proves (G8). QED.

**Check.** Entire proof reread; dimensions are $\dim(z\times A')=n+2$, four divisor intersections leave dimension $n-2$, and the final degree uses exactly $n-2$ target hyperplanes. Coefficient $48=8\binom42$ checked. Nef intersection monotonicity is used only on an effective cycle with all remaining factors nef. The assertion is a bound for a selected signed representative, not for every rationally equivalent cycle.

Combining T6.7 and T6.8 gives a completely explicit denominator/degree bound from the source surface degree, the finitely many integral divisor-kernel choices, their coefficient embeddings, the coefficient-field degree, and the Galois conjugate periods. By T6.6 applied to each conjugate (reordering the two holomorphic and two antiholomorphic factors as necessary),
\[
M\le G\deg_H z,\qquad
G=\max_\sigma\prod_{i=1}^4\|\sigma\alpha_i\|_H.
\]
For fixed $L$, generators, and kernel data, the displayed bounds are polynomial of degree at most $d$ in $\deg_H z$. This is an actual sufficient criterion for bounded division if those data are uniformly bounded on the chosen target orbit. It does not prove their uniform boundedness. It removes the separate purported need for a lower bound on the extracted algebraic period; the remaining nonvanishing input is exactly the already established $k\ne0$.


## 7. Further checked attack: the human proof supplies every one-form theta expansion

### DEG-L.T6.9 — Finite-level theta spanning removes the existence gate

For a sufficiently deep principal ball-quotient surface in the 032 construction, **every** holomorphic one-form, hence every pullback of a polarization coordinate under its actual map to an abelian variety, is a finite complex linear combination of genuine integrated theta lifts from automorphic characters of one-dimensional unitary groups. The finite combination can be made at the chosen common principal level. This is an existence statement; it does not give bounds on its coefficients or on its comparison with the integral Betti/Hom lattice.

**Sources.** The supplied van Hoften–Sempliner paper, Proposition 3.1.7 and Theorem 3.1.11, printed p.11; proof of Proposition 4.1.8, printed p.15, especially its explicit all-$H^{1,0}$ spanning assertion. Primary literature checked: Bergeron–Millson–Mœglin, *The Hodge conjecture and arithmetic quotients of complex balls*, Acta Mathematica 216 (2016), Theorem 9.1, pp.73–75, with the range stated in §9.1, p.72; $3(a+b)+|a-b|<2m$ holds for $m=3$, $(a,b)=(0,1)$ because $4<6$. The older arXiv:1306.1515v2 has different numbering, Theorem 9.3, pp.57–59. Also Y. Liu, arXiv:2102.11518v2, Proposition 4.13, printed p.29, and Theorem 4.18, pp.32–33. The actual printed hypothesis in Proposition 4.13 is $n\ge3$, confirmed by rendering the page: web extraction incorrectly displays $n>3$.

**Proof of the finite-level form needed here.** First pass, if necessary, to a deeper principal level. For an integral isometry of the Hermitian lattice, its determinant is an algebraic unit all of whose complex absolute values are one. Hence it is a root of unity. The group of roots of unity of $E$ is finite, so a sufficiently deep principal congruence condition kills every nontrivial determinant. At that level the principal arithmetic groups for $U(V)$ and $SU(V)$ coincide. The ball quotient in question is therefore a connected component of the compact unitary Shimura variety at that level. The extra cover is harmless for the normalized Chow construction by T6.4.

Extend a holomorphic one-form on this connected component by zero on the other components. The cited spanning theorem on the direct-limit cohomology writes its class as a finite sum of integrated cohomological theta classes; in degree one the source has dimension one, so the source representations are automorphic characters. Take a common deeper level on which all finitely many inputs are fixed, and average over the original compact open level subgroup. The class to be expressed is already invariant, and equivariance of the theta lift moves this averaging to its finite Schwartz input. Each such average is a finite sum, since a smooth finite-adelic input has an open stabilizer. Thus every summand can be taken at the original level. Restrict to the chosen component. Equality of classes gives equality of holomorphic forms because $H^0(S,\Omega^1_S)\to H^1(S,\mathbf C)$ is injective on a compact Kähler variety. QED.

**Check.** Entire argument reread. The pro-level span is used only for a finite collection of vectors; compact averaging is finite on each smooth input. The determinant argument uses norm-one **units**, not arbitrary norm-one elements of $E^\times$, which need not be roots of unity. No claim that arbitrary arithmetic finite covers are principal was used. It suffices to deepen within the principal tower already authorized by 032. Published BMM theorem and its whole proof were read; the classification theorem itself is cited background, not independently reproved.

**Concrete energy consequence.** Let $\omega_S$ be an invariant Kähler form and let $\eta_j=f^*\omega_j=\sum_a c_{ja}\theta_a$ be one of these finite expansions. Define the geometric Gram form
\[
G_{ab}=\int_S {i\over2}\theta_a\wedge\bar\theta_b\wedge\omega_S.
\]
Then the energy is exactly $E_f=\sum_j\sum_{a,b}c_{ja}\bar c_{jb}G_{ab}$. Each full-Shimura-variety diagonal norm can be expressed by the rank-one Rallis formula (Haan, Theorem 3.4), after its explicitly chosen scalar-cohomological and measure normalization. Restricting to one component only lowers that nonnegative norm, so with those full norms denoted by $Q_a$ one has
\[
E_f\le\sum_j\left(\sum_a|c_{ja}|\sqrt{Q_a}\right)^2,
\qquad
\deg_H f_*[S]\le{1\over\int_S\omega_S^2}
\left\{\sum_j\left(\sum_a|c_{ja}|\sqrt{Q_a}\right)^2\right\}^{\!2}.
\tag{G9}
\]
The last inequality is the Hodge-index bound proved in the bounds report. This is an unconditional finite-character-$L(3/2)$ comparison after specifying the geometric realization coefficients and all local/measure factors. It is not an effective degree bound in the level alone until those quantities are controlled. The actual existence of the expansions, formerly left as a gate in the earlier analysis, is now resolved.

A further exact identity locates what prevents one-form norms from giving the degree itself. Put $\beta=f^*c_1(H)$, $V=\int_S\omega_S^2$, and $\beta_0=\beta-(E_f/V)\omega_S$. The class $\beta_0$ is primitive of type $(1,1)$, so with its Hodge norm $\|\beta_0\|^2=-\int_S\beta_0^2$,
\[
\deg_H f_*[S]={E_f^2\over V}-\|\beta_0\|^2.
\tag{G10}
\]
This follows by expanding the square and using $\beta_0\cdot\omega_S=0$. Thus the precise missing datum for an equality is the primitive degree-two component of the pulled polarization. The rank-two theta/see-saw approach is relevant to this remaining fourth-moment term; the rank-one Rallis norms already suffice for the upper comparison (G9).

## 8. Exact scalar normalization and the finite-character energy formula

### DEG-L.T6.10 — The scalar/differential-form norm conversion is explicit

Let $G=U(V)$ be the compact-quotient unitary group used above, let $K_f$ be neat, and put
\[
X_K=G(F)\backslash(D\times G(\mathbf A_f)/K_f).
\]
The notation includes every connected component. Choose the invariant metric on the two-dimensional ball so that an orthonormal holomorphic coframe satisfies
\[
\omega={i\over2}(e_1\wedge\bar e_1+e_2\wedge\bar e_2),\qquad dV={\omega^2\over2}.
\]
Normalize Haar measure on $K_\infty$ to have mass one. Write the archimedean Haar factor in the chosen Tamagawa factorization as $dg_\infty=c_\infty\,dV\,dk$, and set
\[
a_K=c_\infty\operatorname{vol}_{dg_f}(K_f).
\]
For a holomorphic one-form $\eta$, let $F_\eta(g)\in E=(\mathfrak p^{1,0})^*$ be its moving-frame automorphic realization and $F_{\eta,e}(g)$ its coefficient along any fixed unit vector $e\in E$. Then
\[
\int_{X_K}{i\over2}\eta\wedge\bar\eta\wedge\omega
={2\over a_K}\int_{[G]}|F_{\eta,e}(g)|^2\,dg.
\tag{G11}
\]
For a holomorphic two-form $\xi$, let $F_\xi$ denote its scalar coefficient along the unit frame $e_1\wedge e_2$. Then
\[
\int_{X_K}\xi\wedge\bar\xi
={4\over a_K}\int_{[G]}|F_\xi(g)|^2\,dg.
\tag{G12}
\]
Consequently, extend each $\eta_j=f^*\omega_j$ by zero from the chosen component $S$ to $X_K$. Its wedge extension is also zero on the other components, and the degree formula becomes
\[
\deg_H f_*[S]={2\over a_K}\sum_{j<k}\|F_{\eta_j\wedge\eta_k}\|_{L^2([G],dg)}^2.
\tag{G13}
\]

**Proof.** More generally, let $E$ be an irreducible unitary representation of $K_\infty$ of dimension $r$, and let $F(gk)=\rho(k)^{-1}F(g)$ realize a section of the corresponding homogeneous bundle. For a unit vector $e$, Schur averaging gives
\[
\int_{K_\infty}|\langle\rho(k)^{-1}v,e\rangle|^2dk={\|v\|^2\over r}.
\]
Indeed, the average of the rank-one orthogonal projector onto $\mathbf Ce$ commutes with $\rho$; its trace is one, so it is $r^{-1}\operatorname{id}_E$. Right invariance of Haar measure and the quotient measure formula now give
\[
\int_{[G]}|F_e|^2dg={a_K\over r}\int_{X_K}\|F\|^2dV.
\]
Neatness removes finite stabilizer weights; alternatively the same equality holds with the usual orbifold weights consistently on both sides. The cotangent representation of $U(2)\times U(1)$ is irreducible of dimension two, while its determinant has dimension one. In the stated coframe,
\[
{i\over2}\eta\wedge\bar\eta\wedge\omega=\|\eta\|^2dV,
\qquad
\xi\wedge\bar\xi=4\|\xi\|^2dV.
\]
These pointwise identities prove (G11) and (G12). Insert (G12) into (G1) to obtain (G13). QED.

**Normalization consequence.** If a cohomological theta cocycle is written $\varphi=\varphi_1\otimes e_1+\varphi_2\otimes e_2$, the scalar theta lift with Schwartz input $\varphi_1$ is exactly $F_{\eta,e_1}$. Thus no unspecified scalar/cohomological comparison remains once the unit coframe, actual cocycle, Haar factorization and $K_f$ are specified. The lemma does not require the entire form to belong to a single irreducible automorphic representation. The supplied human paper uses probability measures on adelic class sets (§4.1, printed p.12); Haan and GQT use their stated Tamagawa normalizations. These choices must be converted, not silently equated.

**Check.** Entire proof reread. The Schur argument applies to the fiber representation, not to an assumed irreducible global representation. Both pointwise constants were recomputed in a unit coframe; $4$ in (G12), $2$ in (G13), and the factor $a_K^{-1}$ agree with T6.1. Finite stabilizers and all connected components are included explicitly.

### DEG-L.T6.11 — An exact finite Hecke-$L(3/2)$ energy formula

Use the actual morphism $f:S\to A$, its polarized coordinate forms, and their zero extensions to $X_K$. The oscillator decomposition in van Hoften–Sempliner, Proposition 3.1.7 and §4.1.7–Proposition 4.1.8 (equivalently the cited Liu and BMM results), gives an orthogonal finite decomposition of these forms into their actual automorphic summands. For each occurring summand $\sigma$, choose its rank-one theta realization, a nonzero source character vector $f_\sigma\in\tau_\sigma$, and scalar Schwartz inputs $\phi_{j\sigma}$ such that the coefficient of the $\sigma$-part of $\eta_j$ along the unit cotangent vector is
\[
F_{j\sigma}=\theta(\bar f_\sigma,\phi_{j\sigma}).
\]
Finite sums of inputs are allowed. The multiplicity-free oscillator decomposition and the uniqueness of $(W,\pi)$ with the auxiliary source splitting fixed are exactly the facts used here; a general multiplicity-one assertion for all automorphic representations is not needed.

To use Haan's notation, take $\gamma_\sigma$ to be the splitting character on the $U(V)$ side. Changing the source-side splitting to $\gamma_\sigma^3$ twists $\tau_\sigma$ by the corresponding determinant character and preserves the displayed actual theta lift. This follows from the splitting-change formula, Wu §2.2, equation (2.9), printed p.5. Thus each summand can be put into Haan's convention without changing the form. Define
\[
\mathcal Q_{j\sigma}=
{L_E(3/2,\operatorname{BC}(\tau_\sigma)\otimes\gamma_\sigma^3)
 \over L_F(3,\epsilon_{E/F})}
\,\mathcal Z^\#_\sigma(1;\phi_{j\sigma},\phi_{j\sigma};f_\sigma,f_\sigma),
\tag{G14}
\]
where $\mathcal Z^\#$ is Haan's product of normalized local integrals for pure tensors and its sesquilinear extension to finite sums. The source vector's norm is included in this expression. Haan, Theorem 3.4, identifies $\mathcal Q_{j\sigma}$ with $\|F_{j\sigma}\|^2_{L^2([G])}$; in particular the whole expression is real and nonnegative, without any claim that each displayed factor separately is positive.

**Inner forms and archimedean conventions.** Haan's §2.1, printed pp.3–4, starts with arbitrary Hermitian and skew-Hermitian spaces; §3.3, Theorem 3.4 imposes dimensions one and three, without a signature or quasi-split condition. Its use here is with the actual inner form $G$: signature $(2,1)$ at the active place and definite at every other real place. The line source is compact $U(1)$ at every real place; its active skew-Hermitian signature is $(0,1)$, and its other signs are those of the chosen CM theta datum. To match Haan's convention in which the source is Hermitian and the target skew-Hermitian, choose $\delta\in E^\times$ with $\bar\delta=-\delta$ and multiply the source and target forms by $\delta^{-1}$ and $\delta$, respectively. Under the tensor-factor exchange this preserves the symplectic space; the same additive character and transported Schrödinger/Fock polarization are used. Equivalently one may use the explicit role exchange of Wu §2.2, printed pp.5–6. The groups themselves are unchanged.

At the active place take the actual BMM cohomological cocycle $\varphi^{1,0}$ and its coefficient along a unit cotangent vector, rather than replacing it by a spherical Gaussian. At a compact target place take the prescribed invariant Gaussian factor of that cocycle, with its matching splitting character. All these archimedean inputs and their local zeta factors remain in $\mathcal Z^\#$. The already nonzero global theta summand ensures that its local realization exists; no unsupported assertion that arbitrary character/sign data give a nonzero lift is used. The dyadic restriction in Haan's main Bessel-period Theorem 1.2 is not a hypothesis of the Rallis statement in §3.3: the latter is stated for the arbitrary spaces of §§2.1 and3.1 and follows there from Li's convergent-range theorem. In the present case the target is globally anisotropic, so the scalar lifts are square integrable and cuspidal automatically. The Weil symplectic form convention includes the trace factor and additive character; if these are changed, the Schwartz input and local factors must be transported as well.

**Exact infinity type and the all-place ratio.** For an actual oscillator summand, van Hoften--Sempliner §4.1.7 permits the choice $\gamma_\sigma=\mu_\sigma$ from §3.1.3, whose angular weight at each real place is $\varepsilon_v\in\{1,-1\}$. After the preceding compatible splitting change, $\tau_{\sigma,v}=1$ at every archimedean place. Indeed, the center of the target acts trivially on its symmetric domain and cotangent representation (and the compact target places have the trivial coefficient representation); Haan, Remark 2.1, printed p.4, identifies the image of the line member with that central image under his power-compatible splittings. Hence its character is trivial, independently of the convention that inverts the source character. Thus the Hecke character in (G14) has infinity type $(z/|z|)^{3\varepsilon_v}$. With the explicit standard local factors $\Gamma_{\mathbf C}(s)=2(2\pi)^{-s}\Gamma(s)$ and $\Gamma_{\mathbf R}(s)=\pi^{-s/2}\Gamma(s/2)$, the numerator factor at $s=3/2$ is $\Gamma_{\mathbf C}(3)$ and the denominator factor is $\Gamma_{\mathbf R}(4)$. Their ratio is $1/(2\pi)$ at each real place. Consequently the all-place local-product ratio is $(2\pi)^{-[F:\mathbf Q]}$ times its finite Euler-product ratio. This fixes the archimedean $L$ factors; it does not remove the archimedean zeta inputs. A conductor-completed functional-equation symbol $\Lambda$ is a different normalization and is not silently substituted here. Writing $\gamma=\psi\|\cdot\|_E^{1/2}$ as in van Hoften--Sempliner Lemma 3.1.5 gives the arithmetic shift $L(s,\operatorname{BC}(\tau)\gamma^3)=L(s+3/2,\operatorname{BC}(\tau)\psi^3)$: the value is at arithmetic argument $3$, with weight-three center $2$. The complete normalization proof and finite Euler-product bounds are also recorded as bounds B1--B1a, independently checked in this run.

One then has the **exact** finite formula
\[
E_f={2\over a_K}\sum_{j,\sigma}\mathcal Q_{j\sigma},
\qquad
\deg_H f_*[S]\le
{4\over a_K^2\int_S\omega^2}
\left(\sum_{j,\sigma}\mathcal Q_{j\sigma}\right)^2.
\tag{G15}
\]
The corresponding equality with the primitive defect is
\[
\deg_H f_*[S]=
{4\over a_K^2\int_S\omega^2}
\left(\sum_{j,\sigma}\mathcal Q_{j\sigma}\right)^2
-\|\beta_0\|^2.
\tag{G16}
\]

**Proof.** T6.9 supplies actual finite expansions of the zero extensions. Project them to the oscillator summands in the cited direct-sum decomposition, and choose one rank-one model for each summand. The theta image spans that summand; finite linearity of the Schwartz input absorbs the finite expansion, with the one-dimensional source vector fixed. Distinct actual summands are orthogonal for the adelic invariant inner product. Therefore the norm of each scalar coefficient is the sum of the norms of its summands. Apply Haan's bilinear formula to each norm and (G11) to the differential form. Zero extension makes the full geometric norm equal to the norm on $S$, so there is no component restriction inequality at this stage. Finally apply the Hodge-index identity (G10). QED.

**Check and scope.** Entire proof reread, including zero extension, representation orthogonality, finite linearity, source twists, and the constants in (G15)–(G16). Haan's actual theorem is bilinear, so it applies to Gram entries before finite inputs are combined. Its global character factor is absolutely convergent and nonzero at $3/2$ (§3.6.1, printed p.9). This proves an exact energy expression and a degree inequality in terms of finitely many Hecke values, rather than an asserted equality of the degree with one Hecke value. It is not yet an effective level bound: the finite geometric/theta realization coefficients and the finite and archimedean Schwartz inputs are actual additional data whose size must be bounded. Their existence and the scalar norm conversion are no longer missing hypotheses.

## 9. Rank-two attack: the wedge has a genuinely finite cuspidal spectrum

### DEG-L.T6.12 — Product, toric period, and finite Rallis expansion

Let $\Theta_i$ be two genuine integrated holomorphic one-form theta lifts from characters $\chi_i$ of $T_i=U(W_i)$, with compatible Weil splittings. Both $W_i$ have signature $(0,1)$ at the active real place. Put
\[
W=W_1\perp W_2,\quad H=U(W),\quad T=T_1\times T_2\subset H,\quad \chi=\chi_1\boxtimes\chi_2.
\]
Choose the rank-two cocycle $\varphi$ to be the tensor/wedge product of the actual rank-one cocycles, under the direct-sum identification of Weil representations. This definition includes its normalization. Let $\mathcal K_\varphi(g,h)$ be the resulting holomorphic two-form theta kernel. Then
\[
\Theta_1\wedge\Theta_2
=\int_{[T]}\mathcal K_\varphi(-,t)\,\overline{\chi(t)}\,dt.
\tag{G17}
\]
This is the theta transform of a toric-period functional on $H$, rather than the theta lift of a single character of $H$.

Assume the finite input is fixed by an open compact subgroup of $H(\mathbf A_f)$ and the archimedean input is $K_{H,\infty}$-finite, as holds for the polynomial-Gaussian cocycles just specified. Fix a common neat $G$-level $K_f$. There are finitely many irreducible cuspidal **realizations** $\pi_\lambda\subset L^2([H])$ and finitely many orthonormal vectors $b_{\lambda r}\in\pi_\lambda$ for which
\[
\mathcal K_\varphi(g,h)=
\sum_{\lambda,r}\Theta_\varphi(b_{\lambda r})(g)b_{\lambda r}(h),
\qquad
\Theta_\varphi(b)(g)=\int_{[H]}\mathcal K_\varphi(g,h)\bar b(h)\,dh.
\tag{G18}
\]
The equality is an equality of smooth two-form-valued functions, and the sum is genuinely finite. Write
\[
p_{\lambda r}=\int_{[T]}b_{\lambda r}(t)\overline{\chi(t)}\,dt.
\]
Thus the wedge is the finite sum $\sum_{\lambda,r}p_{\lambda r}\Theta_\varphi(b_{\lambda r})$.

Let $\phi$ denote the scalar coefficient of $\varphi$ in the unit canonical frame from T6.10. With inner products linear in the first variable, its exact norm on the full Shimura variety is
\[
\int_{X_K}(\Theta_1\wedge\Theta_2)\wedge
                 \overline{(\Theta_1\wedge\Theta_2)}
={8\over a_K}\sum_\lambda L(1,\pi_\lambda\times\chi_V)
\sum_{r,s}p_{\lambda r}\bar p_{\lambda s}
\mathcal Z^*_{\lambda}(1/2;\phi,\phi;b_{\lambda r},b_{\lambda s}).
\tag{G19}
\]
Here $\chi_V$ is the retained source-side splitting character in GQT's notation; $\mathcal Z^*$ is precisely its normalized doubling form, extended to finite sums of pure tensors. Its unramified denominators are retained. The standard $L$-function has degree two. It is not in general a Hecke-character $L$-function. No lower-tower, continuous-spectrum, or residual-spectrum term has been omitted.

**Proof.** The direct-sum Schrödinger model is the tensor product of the two models. At a point of $T$, its theta sum is the product of the two theta sums; applying the wedge map to the differential-form factors gives the identity of kernels. Absolute convergence and compactness of the two torus quotients allow their integrations to be combined. This proves (G17). Compatibility of the splitting is substantive: the character on the $G$ side is the product of the two rank-one characters, and the character on the $H$ side is common to both lines. More explicitly, if the original line models use source-side characters \(\chi_{V,1},\chi_{V,2}\) and target-side characters \(\gamma_1,\gamma_2\), choose one \(\chi_{V,0}\) restricting to \(\epsilon_{E/F}^{3}\) on \(\mathbf A_F^\times\). The ratios \(\chi_{V,0}/\chi_{V,i}\) are trivial there and descend through \(x\mapsto x/\bar x\) to automorphic characters of \(U(1)\). Changing only the source-side splittings and retwisting the two source vectors by these characters preserves each theta integral: the unitary character multiplying its kernel cancels the conjugate character multiplying its source vector. Keep \(\gamma_1,\gamma_2\) unchanged. The direct-sum model has source-side character \(\chi_{V,0}\) and target-side character \(\gamma_1\gamma_2\). This works when their infinity types differ. Forcing a common target-side character instead would introduce a target determinant twist and would require tracking a changed automorphic form; that operation is not being used. See Wu, Proposition 2.2 and §2.2 equations (2.8)–(2.9), printed pp.4–5; the corresponding common auxiliary choice is explicit in the human paper §4.1.7, printed p.15. The direct-sum theta-product argument also appears in 032, Remark 4.3 and Proposition 4.6.

The form $W$ is definite at the active real place, so it has no nonzero rational isotropic vector. Thus $H$ is anisotropic over $F$. The target $V$ is definite at a nonactive real place, so $G$ is anisotropic as well. Their centers are norm-one tori. Hence both adelic quotients are compact and their automorphic $L^2$ spectra are discrete and cuspidal; cuspidality here is vacuous because there is no proper $F$-parabolic. In particular there is no continuous or residual contribution from an Eisenstein series on $H$. Use the standard discrete admissible decomposition of this compact automorphic quotient, with finite multiplicities.

We give the orthogonality step explicitly, including distinct copies of an isomorphic representation. For two orthogonal irreducible subrepresentations $\mathcal V_1,\mathcal V_2\subset L^2([H])$, the mixed convergent-range doubling identity gives the inner product of theta lifts from $f_i\in\mathcal V_i$ as the value of a mixed doubling zeta integral. The identity is the kernel/see-saw identity underlying GQT, Proposition 11.1(ii) and Proposition 11.2, before an irreducible representation is fixed. For large $\operatorname{Re}s$, unfold that integral. Every rational maximal isotropic plane in $W\oplus(-W)$ is the graph of an isometry of $W$: its projection to either copy of $W$ is injective, since a kernel vector would be isotropic in $W$, and dimensions then make it an isomorphism. There is therefore only the graph orbit. The unfolded integral is an integral of a Siegel section against a matrix coefficient
\[
\langle R(h)f_1,f_2\rangle_{L^2([H])}
\]
(up to the fixed splitting characters, which cancel in the usual doubling normalization). This coefficient is zero because $\mathcal V_1$ is invariant and orthogonal to $\mathcal V_2$. The zeta integral is identically zero and stays zero on meromorphic continuation. The mixed theta inner product is zero. This argument works for distinct orthogonal realization copies as well as inequivalent representations; it does not assume global multiplicity one.

For each $h$, the two-form $\mathcal K_\varphi(-,h)$ belongs to the fixed finite-dimensional space $\mathcal F=H^0(X_K,\Omega^2)$. The $H$ action commutes with the $G$ action and the cohomological differential, so varying $h$ preserves this property and the chosen $G$-level. The spectral coefficients $\Theta_\varphi(b)$ also lie in $\mathcal F$. By the preceding orthogonality, the nonzero images belonging to distinct orthogonal irreducible source realizations are mutually orthogonal nonzero subspaces of $\mathcal F$. There can therefore be only finitely many such realizations. Within each one, the fixed finite level and the finitely many archimedean compact types of $\varphi$ select a finite-dimensional subspace by admissibility. All other spectral coefficients vanish. The $L^2$ expansion is consequently finite; both sides are smooth, so the equality holds everywhere, proving (G18). Applying the toric functional to this finite equality is legitimate and introduces no Sobolev convergence issue.

For every retained $\pi_\lambda$, the global theta lift is nonzero, hence all its local theta lifts are nonzero. In GQT, the dimensions are $n=2,m=3$, $\epsilon_0=0$, and the target Witt index is $r=0$. Thus $2<3\le4$, $r\le n$, and the lower-tower hypothesis is empty. Theorem 11.4(ii), printed pp.54–55, applies at $s_{m,n}=1/2$ and gives
\[
\langle\Theta_\phi(b_{\lambda r}),\Theta_\phi(b_{\lambda s})\rangle
=2L(1,\pi_\lambda\times\chi_V)
\mathcal Z^*_{\lambda}(1/2;\phi,\phi;b_{\lambda r},b_{\lambda s}).
\]
The $L$-value here is holomorphic; a residue is not required. Expand the finite squared norm, use the orthogonality already proved, and apply (G12). This proves (G19). QED.

**Check.** Entire proof reread. Definite-at-one-place anisotropy, the graph-orbit argument, orthogonal-copy issue, and the finite-dimensional-image argument were checked separately. Finite image alone would not imply finite spectral support: orthogonality and admissibility are essential. The toric functional is applied only after finiteness has been proved. The conjugate in the definition of $\Theta_\varphi$ agrees with the rendered GQT §11.2, printed p.52; web extraction omits that overbar. The factor $8/a_K=4/a_K\times2$ in (G19) was checked. This proof uses the standard discrete admissible spectral decomposition and the cited convergent Siegel–Weil/doubling identity as background theorems, rather than claiming to reprove them.

### DEG-L.T6.13 — General degree as a finite standard-$L(1)$ norm sum

The preceding statement extends to every actual map $f$ in the 032 construction in the following precise, non-effective form. There exist finitely many rank-two skew-Hermitian spaces $W_\lambda$, irreducible cuspidal representations $\pi_\lambda$ of $U(W_\lambda)$ with nonzero lift to $G$, and finite theta input tensors $q_{jk,\lambda}$ such that
\[
\deg_H f_*[S]
={4\over a_K}\sum_{j<k}\sum_\lambda
 L(1,\pi_\lambda\times\chi_{V,\lambda})
 \mathcal Z^*_{\lambda}(1/2;q_{jk,\lambda},q_{jk,\lambda}).
\tag{G20}
\]
To make this a defined equality, the data include unitary $G(\mathbf A)$-intertwiners when isomorphic target representations occur through different theta models or in several copies. The input tensors encode the actual zero-extended wedge forms through these identifications. They are not normalized to have size one. The formula retains the local factors and all input coefficients; it does not assert that these quantities can be recovered or bounded from the source level alone.

**Proof.** Expand the zero extension of each $\eta_j$ by T6.9. Each $\eta_j\wedge\eta_k$ is a finite sum of products of rank-one theta forms. Apply T6.12 separately to every such product, taking a common $G$-level; all relevant rank-two source groups are anisotropic at the active place. This places all the scalar wedge coefficients in the sum of finitely many global rank-two theta images. Every nonzero such image is an irreducible cuspidal representation by Wu, Theorem 5.3, printed p.15, since the target is anisotropic. Their sum is a finite-length unitary representation. Decompose it into orthogonal irreducible actual copies.

For each resulting copy choose one theta image isomorphic to it and a unitary intertwiner from that image to the chosen copy. Transport the orthogonal component of every scalar wedge coefficient back by this isometry. It is a smooth vector of finite compact type in that theta image, and hence a finite sum of theta integrals by the definition of the global theta image (equivalently its irreducibility as an admissible module). Denote the resulting finite input tensor by $q_{jk,\lambda}$. Unitary transport and orthogonality express the squared norm of the scalar wedge as the sum of squared norms of these theta integrals. Apply GQT §11.7, Theorem 11.4(ii) to each sum, extending its bilinear identity by finite linearity, and insert the result into (G13). The factor is $2/a_K$ from (G13) times $2$ from Rallis. QED.

**Check and practical distinction.** Entire proof reread, including the finite-length span and the possible repetition of an abstract target representation. The unitary identifications are explicitly retained; simply declaring different source groups or source characters orthogonal would be invalid. In the special case of one common rank-two source and splitting, (G20) has the concrete toric-period/input Gram coefficients of (G19). With different source models, the isotypic comparison data are additional data. The theorem gives a finite spectral identity and locates the exact analytic factors; it does not give a canonical single Hecke value, an effective closed formula in level/conductor alone, or a bound for the integral realization coefficients. For the desired upper degree estimate, T6.11 is stronger operationally: it already avoids rank-two comparison data and uses only Hecke-character values at $3/2$.


### DEG-L.T6.14 — Exact level-index dependence for fixed adelic data

Keep the group, invariant metric, additive character, splittings and all automorphic/Schwartz inputs fixed. Let $K_f'\subset K_f$ be neat compact open subgroups fixing those inputs, of index $d=[K_f:K_f']$. For the full Shimura varieties, the finite étale map $X_{K'}\to X_K$ has degree $d$, and
\[
a_{K'}={a_K\over d},\qquad
E_{K'}=dE_K,\qquad
\int_{X_{K'}}\xi\wedge\bar\xi
=d\int_{X_K}\xi\wedge\bar\xi.
\tag{G21}
\]
The scalar automorphic functions on $[G]$, their Rallis norms, their global $L$-values and their local integrals are unchanged. Thus (G11)–(G20) have exactly the required factor $d$ from $a_K^{-1}$. If the maps to the abelian variety are pulled back through this cover, the raw pushforward surface degree also multiplies by $d$. On a selected connected component the analogous factor is its actual covering degree, which need not equal the index for the full disconnected Shimura variety.

**Proof.** Haar measure gives $\operatorname{vol}(K_f')=\operatorname{vol}(K_f)/d$, with $c_\infty$ unchanged. A fixed right-$K_f$-invariant automorphic function is the same function when regarded as right-$K_f'$-invariant, so its adelic norm does not change. Apply T6.10, or integrate pulled-back forms over the finite étale cover, to obtain the displayed identities. Proper pushforward of the fundamental cycle gives the degree assertion. The statement for one component uses its own finite covering degree. QED.

**Check and limit.** Entire proof reread. The source-volume factor in the Hodge-index bound also scales by $d$, so $E^2/\int\omega^2$ scales by $d$, not $d^2$. This is the same cover growth that cancels exactly in the normalized Chow output by T6.4. It describes fixed-data level change; allowing new Schwartz vectors, primitive integral maps or target polarizations changes additional data and is not covered by this invariance assertion.

## 10. A nonmonomial rank-two constituent can actually occur in a holomorphic wedge

### DEG-L.T6.15 — Existence of a Steinberg constituent in an admissible balanced wedge

There exist a CM extension \(E/F\) with \([F:\mathbf Q]=2\), a Hermitian space \(V\) of dimension three with signatures \((2,1)\) and \((3,0)\), a neat compact unitary Shimura surface \(X_K\) attached to \(G=U(V)\), and two integrated holomorphic one-form theta lifts \(\eta_1,\eta_2\) from unitary characters of \(U(1)\), with the following property. In the finite rank-two Rallis decomposition of
\[
\eta_1\wedge\eta_2\ne0
\]
from T6.12, an actual source realization \(\pi\) occurs with nonzero contribution, and its stable base change \(\Pi\) to \(\mathrm{GL}_2(\mathbf A_E)\) is cuspidal and has a twist of the Steinberg representation at a finite place of \(E\). In particular the Weil–Deligne monodromy operator there is nonzero. Twisting by the fixed character in the Rallis standard \(L\)-function does not remove this monodromy.

Consequently the standard automorphic \(L\)-function of this contributing source cannot be replaced, by an identity of automorphic parameters or of almost-everywhere Euler factors, by the \(L\)-function of a Hecke character of a quadratic extension of \(E\), or by the product of two Hecke-character \(L\)-functions over \(E\). This gives an actual counterexample to a universal **character-only spectral reduction** for holomorphic rank-one theta wedges of this kind. It does not rule out an accidental numerical identity at the single point \(s=1\), and it does not make an assertion about one preselected indecomposable four-factor CM relation.

The pair and its complex conjugate give a nonzero balanced four-factor period on a connected component of \(X_K\). Thus the example lies in the geometric class of compact unitary surfaces and CM one-forms used by 032. The four-factor relation obtained this way is decomposable; a claim that this construction produces a distinct indecomposable switch relation would require an additional argument and is not made.

**Imported results and precise scope.** The proof uses the following established results as background, together with the previously checked theta-product and mixed-orthogonality identities. It does not purport to reprove the trace formula or local Langlands correspondence.

- Gan–Gross–Prasad, *Restrictions of representations of classical groups: examples*, Astérisque 346 (2012), §15, printed p.161 and Lemma 15.4 p.162: the local/global classification of Hermitian spaces, and existence of a dimension-two definite space whose unitary group is quasi-split at every finite place when the totally real degree is even.
- Shin, *Automorphic Plancherel density theorem*, author version §5.2, Example 5.6 and Theorem 5.7, printed pp.26–27: existence with a prescribed positive-Plancherel family of local discrete-series representations, one auxiliary variable finite level, fixed algebraic coefficient representation at infinity, and unramifiedness elsewhere.
- Labesse, *Changement de base CM et séries discrètes*, author version Remark 5.2 p.42, Corollary 5.3 pp.43–44, and Theorem 5.9 p.49: weak base change, compatibility at every split place, and strong local compatibility at finite quasi-split places once the base change is cuspidal. The extra unramifiedness restrictions in §5.2 concern Theorems 5.4–5.5 and are not hypotheses of these statements.
- Atobe–Gan, arXiv:1602.01299v1, Appendix D, Theorem D.2(i), printed p.43, citing Gan–Ichino for the unitary case: for \(m=n+1\), if the source parameter does not contain the one-dimensional summand \(\chi_V\), both target pure inner forms have nonzero local theta lift. Mínguez, Ann. Sci. Éc. Norm. Supér. 41 (2008), Theorem 1(2), p.718, gives nonzero local theta lift for every irreducible representation in the split \(\mathrm{GL}_2\)-to-\(\mathrm{GL}_3\) case.
- BMM, *Hodge type theorems for arithmetic manifolds associated to orthogonal and unitary groups*, Proposition 5.17 and its proof, Lemma 5.18, and Proposition 5.19, printed pp.48–50: the product cocycle is closed and holomorphic, its definite source type is a determinant character, and its top polynomial is a nonzero determinant. Haan, Remark 2.1, p.4, and Wu, Proposition 2.2 and equations (2.8)–(2.9), pp.4–5, supply the central and direct-sum splitting compatibility.
- GQT §11.6, p.54, gives the unramified doubling integral; §11.7, Theorem 11.4, pp.54–55, and §11.8, Proposition 11.6, pp.55–56, give the required inner product and local nonvanishing statements. The resulting local/global criterion is Theorem 11.7(ii), pp.56–57; its additional condition \(m=d(n)+1\) holds here.
- The standard \(L\)-function of a unitary cuspidal \(\mathrm{GL}_2\) representation, twisted by a unitary Hecke character, is nonzero at \(1\). A primary accessible formulation is Shahidi, *On nonvanishing of L-functions*, Bull. Amer. Math. Soc. 2 (1980), the Theorem on p.462, with proof outline pp.462–463, applied to \(\mathrm{GL}_2\times\mathrm{GL}_1\). The finite omitted local factors are nonzero and finite at \(1\) for these generic unitary local representations. No GRH is used here.

**Proof.** We separate the choices, the exact archimedean vector, and the passage from a rank-two lift to a rank-one product.

**1. The global source and its finite components.** Choose a real quadratic field \(F\) and a CM quadratic extension \(E/F\); one may take a biquadratic CM field \(E=F(i)\). The cited Hermitian classification gives a dimension-two space that is negative definite at both real places and quasi-split at every finite place. Multiply its form by a fixed trace-zero element when converting it to the skew-Hermitian convention for a theta source. Denote the resulting space by \(W\) and its group by \(H=U(W)\). Orthogonal diagonalization over \(E\) gives
\[
W=W_1\perp W_2,
\]
where both lines are negative at every real place. The definiteness implies that \(H\) is anisotropic over \(F\), with compact adelic quotient and compact real groups.

Choose a unitary splitting character \(\gamma\) of \(\mathbf A_E^\times/E^\times\) restricting to \(\epsilon_{E/F}\), with its weight-one CM infinity type chosen for these negative lines. At the active real place use the actual holomorphic one-form cocycle, and at the other real place use the invariant Gaussian for the compact target. The character is chosen to make these genuine relative cochains; an arbitrary previously fixed infinity type would not suffice. Existence of the required CM character is the construction in van Hoften–Sempliner, §3.1.3 and Lemma 3.1.5. Each line uses source-side character \(\gamma^3\) and target-side character \(\gamma\); the sum uses source-side character \(\gamma^3\) and target-side character \(\gamma^2\).

Choose a finite split place \(v_s\) of \(F\), a finite nonsplit place \(v_i\), and another split place \(v_0\). Take a finite set \(S\), containing \(v_s,v_i\) but not \(v_0\), that includes every place where the extension, source lattices, splitting or additive character is ramified. At every place in \(S\), prescribe the unitary unramified-twist orbit of the Steinberg representation of the quasi-split group \(H(F_v)\). At a split place this is the usual \(\mathrm{GL}_2(F_v)\) orbit. These families satisfy Shin's positive-Plancherel and regularity hypotheses by Example 5.6, taking the Levi subgroup to be the group itself. Apply Theorem 5.7 with auxiliary place \(v_0\) and trivial algebraic coefficient representation \(\xi=1\).

The real groups are compact, so being \(\xi\)-cohomological means exactly that the real representation is trivial: the relative Lie algebra quotient is zero, and degree-zero relative cohomology is the invariant subspace. Thus we obtain an actual cuspidal automorphic realization \(\pi\subset L^2([H])\) with
\[
\begin{aligned}
\pi_\infty&=1,\\
\pi_v&\text{ is a unitary Steinberg twist for }v\in S,\\
\pi_v&\text{ is unramified for }v\notin S\cup\{v_0\}.
\end{aligned}
\]
Shin's center condition holds because both the global and real split ranks of this norm-one center are zero. The remaining group-unramifiedness hypothesis holds by the choice of \(S\). Compactness also makes cuspidality automatic in this case.

Labesse applies because \([F:\mathbf Q]\ge2\), the real representations are discrete series of compact groups, and his hypothesis \((*)\) holds automatically for a compact real group. Let \(\Pi\) be the resulting isobaric base change. At either place \(w_s\mid v_s\) of \(E\), local compatibility gives a unitary Steinberg twist. It follows that \(\Pi\) is cuspidal: in rank two the other possibilities in the discrete/isobaric classification are a sum of two characters or a residual representation induced from a repeated character; their split local parameters have zero monodromy and cannot be Steinberg. Labesse's Theorem 5.9 now gives local base-change compatibility at every finite place, since \(H\) is quasi-split there. This also identifies the source standard \(L\)-function used by GQT with the standard \(\mathrm{GL}_2\) function of \(\Pi\), retaining its specified splitting-character twist.

**2. A coherent target with all finite lifts nonzero.** At every nonsplit place in \(S\), the source parameter is a twist of \(S_2\). It contains no \(\chi_V\otimes S_1\) summand as a Weil–Deligne parameter, even when its semisimplified Weil characters happen to have a related twist. Theorem D.2(i) therefore makes the lift nonzero for both dimension-three Hermitian spaces. At a split place, including \(v_0\), Mínguez gives nonvanishing without a restriction on \(\pi_v\).

Outside \(S\cup\{v_0\}\), take the unramified target Hermitian space and the spherical Schwartz data. The unramified local doubling calculation gives a nonzero normalized integral at \(s_{3,2}=1/2\); hence the local theta lift is nonzero. The normalizing denominator has no pole there. Equivalently, this is the unramified theta correspondence. All the relevant characters and lattices are unramified at these places by construction.

Prescribe signature \((2,1)\) at one real place and \((3,0)\) at the other. Choose one of the allowed finite target forms at each remaining place. The local/global Hermitian product condition can be corrected at \(v_i\), where both choices give nonzero lift. The exact norm-class sequence recalled by Gan–Gross–Prasad on p.161, together with the Hermitian classification there, then gives a global target \(V\) with all these localizations. It is anisotropic over \(F\), since it is definite at one real place. Consequently its Shimura varieties at neat level are compact smooth surfaces. Notice that the two odd-dimensional local Hermitian spaces may have isomorphic unitary groups; the choice is a choice of Hermitian space and Weil model and must still be retained.

**3. The prescribed holomorphic cocycle survives at infinity.** At the active place take the product of the two rank-one holomorphic cocycles, and at the other place their Gaussian product. The resulting rank-two relative cocycle \(\varphi_\infty\) is closed and has type \((2,0)\). BMM's Proposition 5.19 evaluates its scalar top component as a nonzero two-by-two determinant polynomial times the Gaussian. Proposition 5.17(8) says that its source \(U(2)\) type is one dimensional; changing from the polynomial normalization to the actual Weil splitting only changes this type by a determinant character. At the compact target place the Gaussian likewise has a one-dimensional source type.

Under the compatible power splittings, Haan's central identity on each line, followed by Wu's direct-sum identity, identifies the action of \(zI_2\) in the source with that of \(zI_3\) in the target. The properly twisted relative target cochain has trivial target central action. Hence this one-dimensional source type has trivial central action. Every genuine one-dimensional representation of compact \(U(2)\) is a power of its determinant, and its value on \(zI_2\) is \(z^{2k}\); triviality for all \(z\) forces \(k=0\). Therefore \(\varphi_\infty\) is invariant under all of \(H(F_\infty)\), rather than merely under a subgroup. Source action is on the Schwartz factor, so its nonzero scalar canonical-frame component is invariant as well.

For \(\pi_\infty=1\), the corresponding raw compact local doubling pairing of this scalar component with itself is
\[
\int_{H(F_v)}\langle\omega_v(h)\phi_v,\phi_v\rangle\,dh
=\operatorname{vol}(H(F_v))\,\|\phi_v\|^2>0.
\]
The splitting factors in the standard doubled section are those of this same Weil model. Division by its nonzero local \(L\) factor does not change nonvanishing. Thus it is this exact holomorphic cocycle, not just an unspecified local theta vector, that survives.

At the finitely many finite places requiring a choice, GQT Proposition 11.6 supplies nonzero local doubled matrix entries from the actual target Weil representation. At almost all places use the spherical entries. Pair the same fixed scalar archimedean component on both sides. The source standard value \(L(1,\pi\times\chi_V)\) is nonzero by the cuspidal \(\mathrm{GL}_2\) nonvanishing theorem; its holomorphy also follows from GQT once all the local lifts are nonzero. In GQT the dimensions are \(n=2,m=3\) and the global target Witt index is \(r=0\), so the dimensional range holds and the lower-tower condition is empty. Theorem 11.4 makes the resulting global theta inner product nonzero. Some global lift with the fixed \(\varphi_\infty\) and suitable finite Schwartz input is therefore a nonzero holomorphic two-form. This argument only needs nonzero bilinear finite entries; it does not assume a positivity assertion about each normalized finite local factor.

**4. A toric character detects this source image.** Put \(T=U(W_1)\times U(W_2)\). The quotient \([T]\) is a compact abelian group. For any nonzero smooth \(b\in\pi\), there is a finite-adelic translate \(b'\) with \(b'(1)\ne0\): choose a point where \(b\) is nonzero and use \(\pi_\infty=1\) to remove its real component. The restriction \(b'|_{[T]}\) is nonzero. It is invariant under \(T(F_\infty)\) and an open compact subgroup at the finite places, so it factors through a finite abelian quotient. Fourier completeness on that quotient gives a finite-order automorphic character
\[
\chi=\chi_1\boxtimes\chi_2,\qquad \chi_\infty=1,
\]
whose toric functional \(\ell_\chi(b)=\int_{[T]}b(t)\overline{\chi(t)}\,dt\) is nonzero on \(\pi\). There is no need to prescribe this character before constructing \(\pi\), and no distinguished-globalization theorem is being assumed.

Let \(P_\pi\) be the orthogonal projection to this chosen actual source realization. Form the span
\[
\mathcal I=\operatorname{span}\{P_\pi\mathcal K_{\varphi_\infty\otimes\phi_f}(g,-):
                  g\in G(\mathbf A),\ \phi_f\in\mathcal S_f\}.
\]
Here scalar canonical-frame coefficients are understood when evaluating the two-form kernel. The nonzero theta lift just proved shows that \(\mathcal I\ne0\). Right translation by \(h_f\in H(\mathbf A_f)\) replaces \(\phi_f\) by \(\omega(h_f)\phi_f\); hence \(\mathcal I\) is an invariant subspace of \(\pi\). Because \(\pi_\infty=1\), its smooth \(H(\mathbf A_f)\)-module is irreducible. Thus \(\mathcal I=\pi^\infty\). Some projected kernel therefore has a nonzero \(\ell_\chi\)-period. T6.12's orthogonality for distinct actual source realizations implies that its nonzero target theta contribution cannot cancel against the other source terms after this toric integration.

**5. Extract a product of two rank-one forms.** Finite-adelic Schwartz functions on a direct sum are algebraic finite sums of products of Schwartz functions on the two summands. To see finiteness directly at one place, a locally constant compactly supported function is constant on finitely many product cosets inside a compact support; their indicator functions are products. At almost all places use the factorized standard lattice indicator. Therefore the chosen \(\phi_f\) is a finite sum of decomposable inputs. The archimedean cocycle was already defined as the product/wedge of the line cocycles. Apply the exact theta-product identity (G17) with \(\chi=\chi_1\boxtimes\chi_2\). The resulting toric period is a finite sum of wedges of actual integrated holomorphic line theta forms. Since its \(\pi\)-contribution is nonzero, at least one such wedge has nonzero \(\pi\)-contribution. Call its factors \(\eta_1,\eta_2\). In particular neither line lift is zero; this conclusion is obtained from the nonzero product and is not an unverified separate local/global assertion about the two chosen torus characters.

Choose a common sufficiently small neat target level fixing these two inputs. A nonzero holomorphic top form has
\[
\int_{X_K}(\eta_1\wedge\eta_2)\wedge
                  \overline{(\eta_1\wedge\eta_2)}>0,
\]
so some connected component has a nonzero balanced four-factor period. These are CM one-forms by the oscillator description used in T6.9. Their span is contained in the CM part of the Albanese cohomology, exactly the Hodge-theoretic input of the 032 map construction. The claim here concerns these actual theta forms and their wedge. It does not assert that their initially chosen analytic normalizations are integral Betti generators, nor does it remove the integral-realization gate in the quantitative problem.

Finally \(\Pi_{w_s}\) has parameter \(\nu\otimes S_2\), with nonzero monodromy. A one-dimensional Weil–Deligne representation has zero nilpotent operator; a direct sum of such characters, or induction of a character through a quadratic extension, also has zero operator. Twisting preserves whether this operator is zero. Thus the relevant rank-two parameter is neither a sum nor a quadratic induction of characters. An equality of almost-everywhere Euler factors with such an automorphic induction or isobaric sum would imply equality of the corresponding automorphic representations by strong multiplicity one, contradicting this local parameter. The nonzero \(\pi\)-component contributes a nonzero norm term in (G19), so it is a genuinely occurring standard factor. QED.

**CM-motive consistency check.** The conclusion concerns the standard \(L\)-function of the **source in a theta norm formula**. It does not identify that degree-two source parameter with the Galois representation carried by the image of \(\Lambda^2H^1\) in the surface's \(H^2\). The target transfer is endoscopic: its parameter has a rank-two part and a character part. An individual endoscopic cohomological packet contribution need not contain the full standard transfer. Chenevier–Harris, *Construction of automorphic Galois representations, II*, Introduction, printed p.2, gives explicit even-degree examples in which the \(U(2)\times U(1)\)-to-\(U(3)\) transfer contributes only the one-dimensional Galois representation from \(U(1)\). This directly rules out treating the full standard transfer as automatically equal to each geometric cohomology contribution. No packet-specific Galois calculation for the present Steinberg example is asserted here. The CM nature of the cup image therefore does not negate any step of the analytic proof; it remains compatible with a different, nonmonomial source factor in its norm expression.

**Check and limitation.** The entire proof has been read as one chain, with separate checks of Shin's real/center hypotheses, base-change cuspidality at the split Steinberg place, global Hermitian coherence at the nonsplit Steinberg place, exact archimedean invariance, nonzero bilinear local/global theta pairing, toric Fourier detection, irreducible-source spanning, and the finite tensor extraction. Bounds independently checked the archimedean argument and the conditional toric/kernel argument, including the mixed-orthogonality requirement. The global existence step imports the cited theorems with their hypotheses as stated. The example proves a spectral obstruction for an admissible balanced wedge; it does not prove a corresponding obstruction for every indecomposable 032 switch relation, or disprove a numerical identity with unrestricted auxiliary coefficients.

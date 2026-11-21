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

Consequently its local standard parameter at this place is neither a direct sum of one-dimensional parameters nor the induction of a one-dimensional parameter from a quadratic extension. Thus this contributing source cannot be replaced, at the level of compatible local parameters, by those Hecke-character data. This gives an actual counterexample to a universal **character-only spectral reduction** for holomorphic rank-one theta wedges of this kind. No equality or inequality of isolated numerical \(L\)-values is being inferred from monodromy. The stronger refinement concerning equality of almost-everywhere Euler factors is not claimed here; it would additionally use a precisely sourced strong multiplicity-one and automorphic-induction theorem. Nor is a statement being made about one preselected indecomposable four-factor CM relation.

The pair and its complex conjugate give a nonzero balanced four-factor period on a connected component of \(X_K\). Thus the example lies in the geometric class of compact unitary surfaces and CM one-forms used by 032. The four-factor relation obtained this way is decomposable; a claim that this construction produces a distinct indecomposable switch relation would require an additional argument and is not made.

**Imported results and precise scope.** The proof uses the following established results as background, together with the previously checked theta-product and mixed-orthogonality identities. It does not purport to reprove the trace formula or local Langlands correspondence.

- Gan–Gross–Prasad, *Restrictions of representations of classical groups: examples*, Astérisque 346 (2012), §15, printed p.161 and Lemma 15.4 p.162: the local/global classification of Hermitian spaces, and existence of a dimension-two definite space whose unitary group is quasi-split at every finite place when the totally real degree is even.
- Shin, *Automorphic Plancherel density theorem*, author version §5.2, Example 5.6 and Theorem 5.7, printed pp.26–27: existence with a prescribed positive-Plancherel family of local discrete-series representations, one auxiliary variable finite level, fixed algebraic coefficient representation at infinity, and unramifiedness elsewhere.
- Labesse, *Changement de base CM et séries discrètes*, author version Remark 5.2 p.42, Corollary 5.3 pp.43–44, and Theorem 5.9 p.49: weak base change, compatibility at every split place, and strong local compatibility at finite quasi-split places once the base change is cuspidal. The extra unramifiedness restrictions in §5.2 concern Theorems 5.4–5.5 and are not hypotheses of these statements.
- Atobe–Gan, arXiv:1602.01299v1, Appendix D, Theorem D.2(i), printed p.43, citing Gan–Ichino for the unitary case: for \(m=n+1\), if the source parameter does not contain the one-dimensional summand \(\chi_V\), both target pure inner forms have nonzero local theta lift. Mínguez, Ann. Sci. Éc. Norm. Supér. 41 (2008), Theorem 1(2), p.718, gives nonzero local theta lift for every irreducible representation in the split \(\mathrm{GL}_2\)-to-\(\mathrm{GL}_3\) case.
- BMM, *The Hodge conjecture and arithmetic quotients of complex balls*, Acta Mathematica 216 (2016), Proposition 5.17 and its proof, Lemma 5.18, and Proposition 5.19, printed pp.48–50: the product cocycle is closed and holomorphic, its definite source type is a determinant character, and its top polynomial is a nonzero determinant. Haan, Remark 2.1, p.4, and Wu, Proposition 2.2 and equations (2.8)–(2.9), pp.4–5, supply the central and direct-sum splitting compatibility.
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

Labesse applies because \([F:\mathbf Q]\ge2\), the real representations are discrete series of compact groups, and his hypothesis \((*)\) holds automatically for a compact real group. Let \(\Pi\) be the resulting isobaric base change. At either place \(w_s\mid v_s\) of \(E\), local compatibility gives a unitary Steinberg twist. It follows that \(\Pi\) is cuspidal: in rank two the other possibilities in the discrete/isobaric classification are an isobaric sum of two characters, with a sum of one-dimensional local parameters, or the residual representation obtained from a repeated character. The latter has local Langlands quotient of the form \(\nu\circ\det\), again with zero monodromy. Neither can have the matched Steinberg parameter. This uses the discrete-spectrum classification already invoked in the proof of Labesse's Corollary 5.3. Labesse's Theorem 5.9 now gives local base-change compatibility at every finite place, since \(H\) is quasi-split there. This also identifies the source standard \(L\)-function used by GQT with the standard \(\mathrm{GL}_2\) function of \(\Pi\), retaining its specified splitting-character twist.

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
For precision, GQT §11.3, printed p.52, normalizes the doubling intertwiner by \(\delta(\phi_1\otimes\bar\phi_2)(0)=\langle\phi_1,\phi_2\rangle\). Its extra \(\chi_V\circ\det\) character is on the second source factor. At \((h,1)\) that character is one, so the Siegel–Weil section at \(s_{3,2}\) is exactly \(\langle\omega_v(h)\phi_v,\phi_v\rangle\). GQT §11.6, p.54, integrates it against the source matrix coefficient; take the trivial source vector to have norm one. This verifies the displayed compact integral without an unspecified scalar or character. Division by its nonzero local \(L\) factor does not change nonvanishing. Thus it is this exact holomorphic cocycle, not just an unspecified local theta vector, that survives.

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

Finally \(\Pi_{w_s}\) has parameter \(\nu\otimes S_2\), with nonzero monodromy. A one-dimensional Weil–Deligne representation has zero nilpotent operator; a direct sum of such characters, or induction of a character through a quadratic extension, also has zero operator. Twisting preserves whether this operator is zero. Thus the relevant rank-two parameter is neither a sum nor a quadratic induction of characters. The nonzero \(\pi\)-component contributes a nonzero norm term in (G19), so it is a genuinely occurring standard factor. QED.

**Albanese degree corollary.** The same construction yields an actual morphism \(f:S\to A\) to a polarized CM abelian variety, with surface image, for which the finite exact degree identity T6.13 has a nonzero contribution from a nonmonomial rank-two source.

**Proof of the corollary.** Fix the ambient full Shimura variety and the actual irreducible target theta realization \(\sigma\) coming from the chosen source \(\pi\). It is irreducible by the global theta theorem used in T6.13. Write the original scalar wedge coefficient as \(F_\xi\), and let \(P_\sigma\) denote orthogonal projection in this full automorphic Hilbert space. The construction proves \(P_\sigma F_\xi\ne0\). Decompose the geometric form into its zero extensions from connected components,
\[
F_\xi=\sum_S F_{\xi,S}.
\]
There are finitely many components, so at least one satisfies \(P_\sigma F_{\xi,S}\ne0\). Fix this \(S\). This is an assertion about a specified ambient projection; it does not assign an intrinsic automorphic action to one isolated connected component. In particular the restricted wedge on \(S\) is nonzero.

If the full CM description of \(H^1\) in T6.9 is used, take \(A=\operatorname{Alb}(S)\). For the weaker input that only the two chosen forms lie in its CM part, take the corresponding CM isogeny quotient of \(\operatorname{Alb}(S)\). This quotient exists because polarizable rational Hodge structures of weight one are semisimple and correspond to abelian varieties up to isogeny. Clear one isogeny denominator to obtain an actual morphism \(f:S\to A\). Its pullback on holomorphic forms contains the plane spanned by \(\eta_1|_S,\eta_2|_S\). Consequently \(\dim f(S)=2\).

Choose any ample polarization on \(A\). Gram–Schmidt applied to the preimage of this two-dimensional plane, using the Hermitian form of its invariant polarization, gives the first two members \(\omega_1,\omega_2\) of a unit invariant coframe. Their pulled-back wedge is \(c\,\xi|_S\) for some \(c\ne0\). Extend to a full unit coframe. Its term in T6.1 therefore has a nonzero \(\sigma\)-projection after zero extension, and T6.13 may use the original \(\pi\)-theta model for that projection. The associated norm term is nonzero.

At the split Steinberg place, Mínguez's parameter formula identifies the local target parameter, up to the fixed characters, with the contragredient rank-two parameter plus a one-dimensional summand. Its monodromy is therefore nonzero. A rank-two theta model with zero-monodromy source could not produce this same target representation at that place. Thus merely changing the rank-two model for this actual target summand does not turn it into an induction or a sum of characters. This corollary is an actual-map degree statement; the target is not asserted to be the four particular \(B_i\) of a prescribed indecomposable switch relation. QED.

**CM-motive consistency check.** The conclusion concerns the standard \(L\)-function of the **source in a theta norm formula**. It does not identify that degree-two source parameter with the Galois representation carried by the image of \(\Lambda^2H^1\) in the surface's \(H^2\). The target transfer is endoscopic: its parameter has a rank-two part and a character part. An individual endoscopic cohomological packet contribution need not contain the full standard transfer. Chenevier–Harris, *Construction of automorphic Galois representations, II*, Introduction, printed p.2, gives explicit even-degree examples in which the \(U(2)\times U(1)\)-to-\(U(3)\) transfer contributes only the one-dimensional Galois representation from \(U(1)\). This directly rules out treating the full standard transfer as automatically equal to each geometric cohomology contribution. No packet-specific Galois calculation for the present Steinberg example is asserted here. The CM nature of the cup image therefore does not negate any step of the analytic proof; it remains compatible with a different, nonmonomial source factor in its norm expression.

**Check and limitation.** The entire proof has been read as one chain, with separate checks of Shin's real/center hypotheses, base-change cuspidality at the split Steinberg place, global Hermitian coherence at the nonsplit Steinberg place, exact archimedean invariance, nonzero bilinear local/global theta pairing, toric Fourier detection, irreducible-source spanning, and the finite tensor extraction. Bounds independently checked the archimedean argument and the conditional toric/kernel argument, including the mixed-orthogonality requirement. The global existence step imports the cited theorems with their hypotheses as stated. The example proves a spectral obstruction for an admissible balanced wedge; it does not prove a corresponding obstruction for every indecomposable 032 switch relation, or disprove a numerical identity with unrestricted auxiliary coefficients.

## 11. The distinct indecomposable switch gate is closed for an explicit relation

### DEG-L.T6.16 — A distinct indecomposable switch with a Steinberg source

There exist a Galois CM field \(E\) of degree eight, four **distinct** odd CM sign functions \(v_i\), and an actual four-map surface witness in the framework of 032, Proposition 3.1, with the following properties.

1. \(v_1+v_2=v_3+v_4\), and the selected balanced list \(v_1,v_2,-v_3,-v_4\) has no nonempty proper balanced sublist. Thus this is an indecomposable four-factor switch in the literal tensor sense, rather than a wedge paired with its own conjugate. Distinctness here concerns the labeled CM types; it does not assert that the four abelian varieties are pairwise nonisogenous or simple.
2. There are a smooth connected projective compact ball quotient \(Y\), actual morphisms \(f_i:Y\to B(v_i)\), and nonzero eigenforms \(\alpha_i\in U(v_i)_1\), chosen with algebraic Betti coefficients, such that
   \[
   \int_Y f_1^*\alpha_1\wedge f_2^*\alpha_2
          \wedge\overline{f_3^*\alpha_3\wedge f_4^*\alpha_4}\ne0.
   \tag{T16.1}
   \]
3. In a specified full unitary Shimura variety containing \(Y\) as a connected component at a sufficiently deep level, the zero extension of the first wedge in (T16.1) has nonzero projection to an actual target automorphic isotypic space whose dimension-two theta source has cuspidal base change with a Steinberg local component. In particular its Weil–Deligne monodromy is nonzero at a fixed finite split place.
4. For the actual product morphism \(f=(f_1,f_2,f_3,f_4)\), some nonzero term in the exact degree formula T6.13 has such a rank-two source. The image of \(f\) is a surface. A product polarization can be used. The source parameter cannot be a sum of characters or a quadratic induction of a character.

The assertion is existential for this explicit switch, not for every prescribed indecomposable relation. It concerns the actual source in an exact theta-norm expansion of the degree; it does not identify that source standard parameter with a geometric Galois constituent of the CM cup image.

**Proof.**

**1. The four sign functions and the rational spaces**

Take a totally real biquadratic field \(F\), for example \(\mathbf Q(\sqrt2,\sqrt3)\), and put \(E=F(i)\). Choose the four representatives of \(\operatorname{Gal}(E/\mathbf Q)/\langle c\rangle\) that fix \(i\), and label them \(\mu,a,b,c_0\), with \(\mu=1\). (The label \(c_0\) is a real place and is not complex conjugation.) On these representatives set
\[
\begin{array}{c|rrrr}
 &\mu&a&b&c_0\\\hline
v_1&+1&+1&+1&+1\\
v_2&+1&-1&-1&+1\\
v_3&+1&+1&-1&+1\\
v_4&+1&-1&+1&+1.
\end{array}
\tag{T16.2}
\]
Extend each function oddly under complex conjugation. The equality of the two pair sums is immediate. The four functions are distinct. A proper balanced sublist cannot have one element. It cannot have three, since the sum of all four is zero and the omitted sign function is nonzero. It cannot have two: the two positive functions cannot cancel, since both take value \(+1\) at \(\mu\); the two negative functions cannot cancel; and a positive and a negative could cancel only if two of the four displayed functions were equal. This proves indecomposability. Since every element of this Galois group has order two, the inversion in 032's convention \(d_i(\tau)=v_i(\tau^{-1})\) makes no change.

Use \(\delta=i\) in 032 §4.2, so its imaginary coefficient is positive at all four chosen representatives. Accordingly \(d_i=+1\) means a negative Hermitian multiplicity line in the Fock convention used here. Choose a dimension-two Hermitian space \(W\) which is negative definite at \(\mu,c_0\), has signature \((1,1)\) at \(a,b\), and is quasi-split at every finite place. Such a space exists by the Hermitian classification and the norm-class product sequence in Gan–Gross–Prasad §15, printed p.161: a quasi-split plane has determinant class \(-1\), and the number of definite real places in this prescription is even. This uses the general classification there, rather than applying their all-definite Lemma 15.4 to the mixed signature prescription.

Choose by weak approximation a vector in \(W(E)\) of negative norm at all real places. Its line \(W_1\) and orthogonal complement \(W_2\) have precisely the signs \(d_1,d_2\) of (T16.2). Thus \(W=W_1\perp W_2\). Convert to a skew-Hermitian theta source by the same fixed trace-zero scalar as in T6.15. Write \(H=U(W)\). It is anisotropic over \(F\), because it is definite at \(\mu\); hence \([H]\) is compact, although two of its real factors are noncompact.

Choose weight-one unitary splitting characters \(\gamma_1,\gamma_2,\gamma_3\) for the first three line types, all restricting to \(\epsilon_{E/F}\), by the CM-character construction used in T6.15. Set
\[
\gamma_4=\gamma_1\gamma_2\gamma_3^{-1},\qquad
\chi_W=\gamma_1\gamma_2=\gamma_3\gamma_4,\qquad
\chi_V=\gamma_1^3.
\tag{T16.3}
\]
The infinity type of \(\gamma_4\) is the required fourth type, and its restriction is again \(\epsilon_{E/F}\). Use the common source splitting \(\chi_V\) for every line and the target splitting \(\gamma_i\) for that line. The source-splitting retwist in T6.12 changes only the source vector and preserves the actual rank-one theta form. For unintegrated kernels evaluated at the source identity, the retwisting character has value one. Crucially the two pairs have exactly the same total target splitting \(\chi_W\), not merely the same infinity type.

**2. The required real representation, including its exact Gaussian vector**

At \(\mu\) take the product of the two holomorphic one-form cocycles, with its nonzero determinant polynomial. At \(c_0\) take the product Gaussian. The same BMM and Haan central-action calculation as in T6.15 makes their source \(U(2)\) representations trivial.

At each of \(a,b\), the target is compact \(U(3)\) and the source is \(U(1,1)\). The total target splitting has zero angular exponent there. The common source splitting is calibrated by the all-negative choice \(\gamma_1^3\): in BMM's notation the twist is \(k=0,\ell=-3\). One can fix this calibration without any ambiguity in the notation for an angular character: at a compact target with a negative definite source plane, the same common splitting makes the Gaussian source invariant, and Proposition 4.15 gives its exponent \((\ell+3)/2\), hence \(\ell=-3\). At a mixed source the Gaussian therefore has maximal-compact character
\[
(z_+,z_-)\longmapsto z_+^{-3},
\tag{T16.4}
\]
where the positive source line is written first. Its character on the ordered pair \((W_1,W_2)\) is consequently \((0,-3)\).

Here is an elementary verification of the entire source representation generated by this vector. In the Fock space write \(x_1,x_2,x_3\) and \(y_1,y_2,y_3\) for the positive and negative variables, and put
\[
R=\sum_{j=1}^3x_jy_j,
\quad E_+=R,
\quad E_-=-\sum_{j=1}^3\partial_{x_j}\partial_{y_j},
\quad H_0=\operatorname{Euler}+3.
\tag{T16.5}
\]
After the usual Fock-unit normalization these are the source \(\mathfrak{sl}_2\) generators; BMM Proposition 5.1, printed p.40, gives the lowering operator, and the raising operator is its negative adjoint. Direct differentiation gives
\[
[E_+,E_-]=H_0,\quad [H_0,E_\pm]=\pm2E_\pm,
\qquad E_-R^j=-j(j+2)R^{j-1}.
\tag{T16.6}
\]
Thus the Gaussian generates \(\mathbf C[R]\), whose genuine \(U(1)\times U(1)\) weights are \((-3-j,j)\), \(j\ge0\), and whose squared monomial norms are \(j!(3)_j\) times the squared vacuum norm. The lowering coefficients are nonzero for every \(j>0\), so this is an irreducible highest-weight module. It is the discrete series \(D_3^-\) specified by these weights. For example, its disk model has reproducing kernel \((1-z\bar w)^{-3}\), or equivalently weighted area norm \(\int_{|z|<1}|f(z)|^2(1-|z|^2)\,dx\,dy\). The automorphy factor of exponent three gives the vacuum coefficient of modulus \((\cosh t)^{-3}\) on a Cartan element with entries \(\cosh t,\sinh t\). Its square is integrable against the Cartan density proportional to \(\sinh(2t)\,dt\). This also verifies square integrability directly.

The real source representation to be globalized is therefore
\[
\pi_\infty=1_{\mu}\boxtimes D_{3,a}^-\boxtimes D_{3,b}^-\boxtimes1_{c_0}.
\tag{T16.7}
\]
Its chosen archimedean vector is the product of the invariant vectors and the two lowest compact-type vectors. That compact-type space is one dimensional.

We also check the extra base-change hypothesis which was automatic in T6.15. For the derived \(\mathfrak{sl}_2\) at a mixed place, use the Casimir
\(C=H_0^2-2H_0+4E_+E_-\). It acts by \(3\). Since \(E_-=-E_+^*\), a unit vector of \(H_0\)-weight \(m\) in any unitary representation with this infinitesimal character satisfies
\[
\|E_-v_m\|^2=\frac{(m-3)(m+1)}4,
\qquad
\|E_+v_m\|^2=\frac{(m-1)(m+3)}4.
\tag{T16.8}
\]
The fixed central character imposes odd parity. Weights \(1,-1\) are impossible by nonnegativity. Starting from any nonzero compact-weight vector, the ladder identities and irreducibility force either the weights \(3,5,\ldots\), or \(-3,-5,\ldots\). They are exactly the two discrete-series members with this central and infinitesimal character. At the compact places the specified infinitesimal character permits only the trivial representation. Labesse's criterion in Remark 5.2, printed p.42, therefore gives hypothesis \((*)\) for (T16.7). This is an explicit verification; no assertion that arbitrary noncompact cohomological infinity types satisfy \((*)\) is used.

Finally the local doubling integral detects the **same** Gaussian vector. GQT §11.3, p.52, normalizes the Siegel–Weil section at \((h,1)\) as the oscillator matrix coefficient. In §11.6, p.54, its other factor is the **complex conjugate** of the source matrix coefficient (the overbar is visible in the original PDF). Identify the cyclic Gaussian module unitarily with \(D_3^-\) and choose its corresponding source vector of norm one. Schur orthogonality gives
\[
Z_v(1/2)=\|\phi_v\|^2\int_{H(F_v)}
       |\langle\pi_v(h)f_v,f_v\rangle|^2\,dh
       =d(\pi_v)^{-1}\|\phi_v\|^2>0.
\tag{T16.9}
\]
The compact-place version is the positive compact integral of T6.15. Thus every factor of this exact archimedean cocycle has nonzero local pairing.

**3. Globalization, base change, and a nonzero holomorphic rank-two lift**

Choose a finite split Steinberg place \(v_s\), a finite nonsplit Steinberg place \(v_i\), and two additional split places \(u_1,u_2\). Let \(S\) contain all real places, \(v_s,v_i\), and all finite bad places for the source, extension, characters and additive character, but exclude \(u_1,u_2\). At the finite places of \(S\), prescribe the unitary unramified-twist Steinberg orbits, as in T6.15. At infinity prescribe (T16.7).

Apply Shin Theorem 5.13, printed p.28, based on §4.3 and Theorem 4.8, pp.19–21. That version explicitly permits \(S\) to contain **all** infinite places and prescribes actual representations there. Its two auxiliary places can be chosen split. To make the local test precise, the characteristic function of the desired archimedean discrete-series tuple belongs to Shin's space \(\mathcal F\): its infinitesimal-character support is a point; twisting a representation of the full real group by an unramified unitary character does not change it, because its center is compact; and unitary parabolic induction from a proper real Levi cannot contain these strict discrete series. The latter assertion also follows from (T16.8) and the distinct infinitesimal characters of tempered principal series. Products with the finite discrete-series-orbit indicators of Example 5.6 remain in \(\mathcal F\). Their Plancherel integral is positive. Thus one may apply Theorem 4.8 directly to this indicator and use the proof of Theorem 5.13. This avoids an unproved selection of a member merely from a cohomological packet.

We obtain a cuspidal automorphic \(\pi\) with exactly (T16.7), Steinberg twists at all finite places of \(S\), unramified outside \(S\cup\{u_1,u_2\}\), square-integrable at \(u_1\), and supercuspidal at \(u_2\). Labesse Corollary 5.3 applies by the preceding verification of \((*)\). Its local compatibility at the split place \(v_s\) implies that its rank-two isobaric base change \(\Pi\) is cuspidal, by exactly the rank-two argument in T6.15. Theorem 5.9 then identifies all finite local base changes, since the source is quasi-split at every finite place.

Choose the dimension-three target with signature \((2,1)\) at \(\mu\), and positive definite at \(a,b,c_0\). At the nonsplit bad places Atobe–Gan Theorem D.2(i) permits both target spaces for a Steinberg source: its Weil–Deligne parameter has no \(\chi_V\otimes S_1\) summand. At every split place, including both auxiliary places, Mínguez's theorem makes the lift nonzero for every source representation. At the remaining places use the unramified theta lift. Correct global Hermitian coherence at \(v_i\), where both choices are allowed. The resulting \(V\) is anisotropic over \(F\), because it is definite at three real places.

The fixed real cocycle survives by (T16.9). Choose the finite bilinear local entries by GQT Proposition 11.6. The twisted unitary cuspidal \(\mathrm{GL}_2\) value at \(1\) is nonzero by the theorem cited in T6.15. GQT Theorem 11.4, with \(n=2,m=3,r=0\), therefore gives a nonzero global theta lift with this **fixed** real cocycle. Fix an actual source realization and a corresponding actual irreducible target realization \(\sigma\). The latter is irreducible by Wu's theorem as used in T6.13. At \(v_s\), its local parameter has nonzero monodromy by Mínguez's formula. These are precisely the compatibility conditions checked in T6.15, with the real step replaced by (T16.7)–(T16.9).

**4. A total 032 theta input retaining this constituent**

We first obtain a total unintegrated theta form with nonzero \(\sigma\) projection. Let \(\mathcal K_{\phi}(g,h)\) denote the rank-two kernel with the fixed real cochain and variable finite Schwartz input. Project in the source variable to the chosen actual realization of \(\pi\). The span of all scalar canonical-frame coefficients
\[
\mathcal I=\operatorname{span}_{\phi_f,g}
 P_\pi\mathcal K_{\phi_\infty\otimes\phi_f}(g,-)
\tag{T16.10}
\]
is nonzero by the nonzero global lift. It is stable under \(H(\mathbf A_f)\), by replacing \(\phi_f\) with its source translate. Its archimedean compact-type space is the one-dimensional space just specified. Thus irreducibility of the smooth finite representation gives \(\mathcal I=\pi_f^\infty\otimes\ell_\infty\).

Evaluation at the source identity is nonzero on this space after a suitable finite translate. Here is the needed density argument, since \(\pi_\infty\) is no longer trivial. The Cayley transform from skew-adjoint endomorphisms to \(U(W)\) gives a rational open chart. Weak approximation in its affine coordinates shows that \(H(F)\) is dense in \(H(F_\infty)\). For a point represented by \((h_\infty,h_f)\), choose \(q_n\in H(F)\) with \(q_{n,\infty}\to h_\infty\). The classes of \((1,q_{n,f}^{-1}h_f)\), represented also by \((q_{n,\infty},h_f)\), approach that point. Consequently the image of \(H(\mathbf A_f)\) is dense in \([H]\). A nonzero continuous automorphic vector in \(\pi_f^\infty\otimes\ell_\infty\) is nonzero at some such finite point; a finite right translate then has nonzero value at the identity and still lies in the same archimedean line.

It follows from (T16.10) that some projected kernel has nonzero value at \(h=1\). The mixed-source orthogonality and finite holomorphic spectral support established in T6.12 imply that this yields a nonzero target \(\sigma\) contribution in \(\mathcal K_\phi(-,1)\); the other source realization terms cannot cancel it. At infinity this unintegrated form is exactly the double-alternating degree-two theta tensor of 032, up to its allowed nonzero constant-line trivialization. Indeed the compact-place factors are its Gaussians and the active factor is the determinant obtained from the product of the two first tensors; this is the explicit coefficient calculation in 032, Proposition 4.6(i), pp.23–24, and BMM Proposition 5.19. Thus choose a finite total input for which
\[
\xi=\Xi_W(\phi;t_0),\qquad P_\sigma\xi\ne0.
\tag{T16.11}
\]
Take a sufficiently deep neat finite level fixing this input. One may work with the finite disjoint union of connected components of the full unitary Shimura variety. Each component admits a further principal special-unitary cover of the kind used in 032: the integral determinant subgroup is finite and is killed by a sufficiently deep neat level. Only finitely many components and inputs will be needed.

**5. A Hecke projector preserves the two pair-type spans**

At the fixed finite level let \(\mathcal H\) be the finite-dimensional space of holomorphic top forms on the full Shimura variety. The image of the finite-level Hecke algebra on \(\mathcal H\) is a finite-dimensional star algebra, with adjoints for the Petersson pairing. Its central orthogonal idempotents project to its irreducible isotypic spaces. In particular there is a finite Hecke operator \(Q\) equal to the orthogonal projection to the \(\sigma_f\)-isotypic space. This includes all its actual multiplicity copies, which is sufficient.

For precision, an irreducible smooth finite-adelic representation with nonzero level invariants is determined by its irreducible module for that level Hecke algebra: the full representation is generated by those invariants, and a module isomorphism extends through compact induction and its irreducible quotient. All target representations occurring in \(\mathcal H\) have the same holomorphic top-degree real representation, with trivial compact factors. Equivalently their scalar canonical coefficients are annihilated by the antiholomorphic lowering algebra and have the prescribed canonical compact type, whose irreducible highest-weight quotient is unique. Hence the relevant Hecke isotypic space consists of copies of the same full target representation \(\sigma\). At the Steinberg place every one of these copies has nonzero local monodromy. In particular \(Q\xi\ne0\).

Let \(\mathcal U_{12}\) be the span of products of theta one-forms of the first two line types, allowing all finite Schwartz inputs, and define \(\mathcal U_{34}\) similarly. A finite target translate of a product is the product of the same simultaneous translates of its two factors. Convolution by a compactly supported bi-level-invariant Hecke function is a finite sum of these translates on a fixed smooth vector. It follows that every finite Hecke operator, in particular \(Q\), preserves each of these two pair-type spans. This statement does not assert that it preserves one individual product. The translated individual factors may require a deeper common level than the final Hecke output; the finite expansions are first understood adelically, and all their factors descend together at the principal level chosen in the next step.

Apply 032, Proposition 4.6(iii) and Corollary 4.7, to the single input chosen in (T16.11). The rational decompositions \(W=W_3\perp W_4\) with signs \(d_3,d_4\) approach the first decomposition in total compact-place period data, with the active data exactly fixed. The global splitting choices agree by (T16.3). On the fixed quotient the resulting \(\xi'\) approach \(\xi\) smoothly. The operator \(Q\) is bounded, so
\[
\langle Q\xi,Q\xi'\rangle\longrightarrow\|Q\xi\|^2>0.
\tag{T16.12}
\]
Choose a sufficiently close rational endpoint. Both endpoint forms are holomorphic, and the finite wedge expansions of 032 give
\[
x=Q\xi\in\mathcal U_{12},\qquad
y=Q\xi'\in\mathcal U_{34},\qquad
\langle x,y\rangle\ne0,
\tag{T16.13}
\]
with \(x,y\) in the full \(\sigma\)-isotypic space. Continuity can be applied on the finitely many components at once; the same Gaussian estimates prove it on each compact component, so their finite sum has (T16.12).

**6. Extract actual CM maps without losing the first constituent**

Choose a connected component \(S\) on which the pairing of \(x|_S,y|_S\) is nonzero. There are only finitely many terms in their translated line-theta expansions. Apply 032, Corollary 6.7, printed p.45, to these finite families for all four sign functions and pass to one connected common principal cover \(Y\to S\). The pairing remains nonzero because it is multiplied by the degree of the finite étale cover. At the new full finite level the pullback of the global form \(y\) is still in the same full automorphic \(\sigma\)-isotypic space; pulling back has not changed the scalar adelic function.

Fix nonzero generators of the four selected eigenlines. The finite-family CM extraction and equality of harmonic representatives on a compact Kähler variety write
\[
x|_Y=\sum_r a_r A_r,\quad
A_r=h_{1r}^*\alpha_1\wedge h_{2r}^*\alpha_2;
\qquad
y|_Y=\sum_s b_s B_s,\quad
B_s=h_{3s}^*\alpha_3\wedge h_{4s}^*\alpha_4,
\tag{T16.14}
\]
where the \(h_{ir}\) denote rational Hodge maps, or corresponding rational homomorphisms from the Albanese. Since \(\langle x|_Y,y|_Y\rangle\ne0\), some \(r\) satisfies \(\langle A_r,y|_Y\rangle\ne0\). The zero extension \(A_r^0\) to the new full Shimura variety then has nonzero \(\sigma\)-projection, because its geometric pairing with the global \(\sigma\)-form \(y\) is that same nonzero number. If scalar Petersson conventions are used instead, T6.10 multiplies this pairing by the fixed positive Haar/geometric conversion factor, so nonvanishing is unchanged. Next expand only \(y|_Y\) in (T16.14); some \(s\) satisfies \(\langle A_r,B_s\rangle\ne0\).

This sequential choice is necessary: a nonzero projected pairing alone would not justify choosing an individual pair whose unprojected period and projected first wedge are both nonzero. Here the first choice guarantees survival of its constituent before the second choice supplies the full period.

Clear the four rational-homomorphism denominators. By 032, Lemma 2.2 and Proposition 3.1, this gives actual morphisms \(f_i:Y\to B(v_i)\). Multiplication by the four nonzero integers scales each selected wedge and period by nonzero factors. It preserves the first wedge's nonzero \(\sigma\)-projection and proves (T16.1).

Finally choose a product ample polarization on \(\prod_i B(v_i)\). In each factor its chosen eigenform can be rescaled to be the first vector of a unit invariant coframe and then extended to such a coframe. The first two factors yield a coordinate wedge proportional to \(A_r\). The exact degree identity T6.1 therefore has a term with nonzero \(\sigma\)-projection; T6.13 can use the rank-two theta model already constructed for that projection. Mínguez's split-place formula prevents any rank-two source with zero monodromy from giving this same target local representation. A one-dimensional Weil–Deligne parameter, its direct sum with another, or its quadratic induction has zero monodromy, while the actual source has Steinberg monodromy. The first wedge is nonzero, so \(f\) has surface image. This proves all four assertions. QED.

**Exact additional source locators.**

- Shin, <https://math.berkeley.edu/~swshin/Plancherel.pdf>: Definition 2.1 and Example 2.3, pp.8–9; §4.3 and Theorem 4.8, pp.19–21; Example 5.6, p.26; §5.3 and Theorem 5.13, p.28. The crucial version includes infinity in the prescribed set. Its full short proof and the scope of §4.3 have been read.
- Labesse, <https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf>: Remark 5.2, p.42, Corollary 5.3, pp.43–44, Theorem 5.9, p.49. The new elementary Casimir computation supplies the specific sufficient condition in Remark 5.2.
- BMM, <https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6812-11511_2016_Article_136.pdf>: Proposition 4.15, p.38, and its adjoining proof; Proposition 5.1, p.40; Proposition 5.19, pp.49–50. The local real proof above imports the Fock action, then computes its cyclic module explicitly.
- GQT, <https://arxiv.org/pdf/1207.4709>: §11.3, p.52, and §11.6, p.54. Original p.54 visually checked for the overbar on the source matrix coefficient. The remaining local/global source locators are those already in T6.15.
- Gan–Gross–Prasad, <https://www.numdam.org/item/AST_2012__346__111_0.pdf>: §15, printed p.161, general Hermitian classification and product exact sequence. The new signature prescription uses two definite and two indefinite real places.
- Supplied 032: §4.1–4.2, pp.13–14; Proposition 4.6 and Corollary 4.7, pp.23–25, entire proofs reread; Corollary 6.7, p.45, entire proof reread. Their fixed-input continuity and finite CM extraction are imported with their stated hypotheses.

The entire proof was read and checked by this agent and independently by root and the bounds agent. The checks covered the real splitting calibration, direct Shin indicator application, fixed archimedean-line source spanning, identification with the 032 total tensor, finite Hecke projector and preservation of pair-type spans, and the component/cover/zero-extension order in the last extraction. The listed primary inputs were read at their exact locators. These checks import the cited background theorems; they are not reproofs of the trace formula or theta-correspondence theorems. T6.15 is retained with its original narrower scope.

## 12. Positive analytic normalization in a fixed CM isogeny construction

### DEG-L.T6.17 — A fixed CM tensor admits bounded analytic normalization

For \(1\le i\le4\), fix a CM field \(E_i\) of degree \(2g_i\), a CM type \(\Phi_i\) (not necessarily primitive), an invertible fractional \(\mathcal O_{E_i}\)-ideal \(I_{i,0}\), and a polarized abelian variety
\[
A_{i,0}=\mathbf C^{g_i}/\Phi_i(I_{i,0}),\qquad L_{i,0},\qquad
V_{i,0}=\chi(L_{i,0}).
\tag{T17.1}
\]
Assume the \(E_i\) action has rank one on rational homology and the Rosati involution restricts to complex conjugation. Fix a smooth projective surface \(Y\), a Kähler form \(\omega_Y\), actual morphisms \(f_{i,0}:Y\to A_{i,0}\), and one holomorphic CM eigenline in each factor. Choose polarization-unit invariant eigenforms \(\beta_{i,0}\) in these four lines and suppose that
\[
p_0=\int_Y f_{1,0}^*\beta_{1,0}\wedge f_{2,0}^*\beta_{2,0}
            \wedge\overline{f_{3,0}^*\beta_{3,0}\wedge f_{4,0}^*\beta_{4,0}}
\ne0.
\tag{T17.2}
\]
The metric normalization and the chosen lines are fixed starting data.

Let the targets \((A_i,L_i)\) vary through the corresponding \(E_i\)-linear CM isogeny classes, with the same Rosati condition. In compatible CM coordinates write \(A_i=\mathbf C^{g_i}/\Phi_i(\Lambda_i)\), put \(V_i=\chi(L_i)\), and set
\[
\Lambda_i^- =\{x\in\Lambda_i:\mathcal O_{E_i}x\subset\Lambda_i\},\quad
J_i=[\Lambda_i:\Lambda_i^-],\quad
x_i=\frac{V_i}{V_{i,0}}J_i,\quad t_i=x_i^{1/g_i}.
\tag{T17.3}
\]
Define field constants
\[
K_i=\frac2\pi\bigl(g_i!\sqrt{|D_{E_i}|}\bigr)^{1/g_i},\qquad
c_i=
\begin{cases}
1,&g_i=1,\\
\bigl((g_i-1)/K_i\bigr)^{g_i-1},&g_i\ge2.
\end{cases}
\tag{T17.4}
\]
There exist actual \(E_i\)-linear isogenies \(h_i:A_{i,0}\to A_i\) and positive integers \(M_i\) such that the actual maps
\[
f_i=[M_i]\circ h_i\circ f_{i,0},\qquad f=(f_i):Y\to\prod_iA_i
\tag{T17.5}
\]
have a nonzero selected four-factor period and uniformly bounded period-normalized energy. Precisely, write \(\omega_i,\omega_{i,0}\) for invariant polarization representatives, let \(\beta_i\) be any polarization-unit eigenform in the corresponding target line, and put
\[
\begin{aligned}
p&=\int_Yf_1^*\beta_1\wedge f_2^*\beta_2
                   \wedge\overline{f_3^*\beta_3\wedge f_4^*\beta_4},\\
E&=\int_Y\Bigl(\sum_i f_i^*\omega_i\Bigr)\wedge\omega_Y,\qquad
E_{i,0}=\int_Y f_{i,0}^*\omega_{i,0}\wedge\omega_Y,\\
C_E&=\frac{4\sum_iK_iE_{i,0}}
               {|p_0|^{1/2}\bigl(\prod_i c_i\bigr)^{1/4}},\qquad
V_Y=\int_Y\omega_Y^2.
\end{aligned}
\tag{T17.6}
\]
Then
\[
p\ne0,\qquad \frac{E}{|p|^{1/2}}\le C_E,
\qquad
\frac{\deg_{\boxtimes_iL_i}(f_*[Y])}{|p|}
\le\frac{C_E^2}{V_Y}.
\tag{T17.7}
\]
The constants depend only on the fixed fields, polarized source factors, source surface and its four maps; they are independent of the target lattices, their endomorphism orders, and their polarization volumes. The denominator in (T17.7) is the specified metric period \(p\). These inequalities do not bound the unnormalized integral degree.

If the finitely many source coordinate pullbacks lie in the span of a fixed finite basis of genuine rank-one theta forms on \(Y\), then the common normalization \(|p|^{-1/4}\) gives theta presentations of all target polarization coordinates with uniformly bounded coefficients and every fixed Schwartz seminorm. Any one finite cover needed for theta spanning is taken at the outset and included in the fixed data.

**Proof.**

**1. Every CM metric eigenvalue is controlled by a short integral isogeny**

For each factor choose a nonzero integral \(E_i\)-linear homomorphism minimizing the squared complex Hilbert–Schmidt norm
\[
Q_i(h)=\operatorname{tr}_{\omega_{i,0}}(h^*\omega_i).
\]
The ideal-lattice argument of B19.1–B19.2 applies without primitivity. Indeed rank-one \(E_i\)-homology identifies every \(E_i\)-linear rational homomorphism with multiplication by an element of \(E_i\). The integral Hom lattice is \((\Lambda_i:I_{i,0})\), and its product with \(I_{i,0}\) is \(\Lambda_i^-\). The Rosati condition diagonalizes the polarization metrics. None of these statements uses simplicity. Every nonzero such field scalar is an isogeny. The exact covolume and minimum bound are therefore
\[
\operatorname{covol}_{Q_i}\operatorname{Hom}_{E_i}(A_{i,0},A_i)
=2^{-g_i}\sqrt{|D_{E_i}|}\,x_i,
\qquad Q_i(h_i)\le K_i t_i,
\qquad \deg h_i\ge J_i.
\tag{T17.8}
\]
Here the last inequality is the elementary inclusion \(h_i I_{i,0}\subset\Lambda_i^-\). The constant in the middle inequality is the Minkowski ball constant computed in B19.2.

Let \(\lambda_{i,\sigma}\) be the positive eigenvalues of \(h_i^*\omega_i\) relative to \(\omega_{i,0}\) in the CM eigenlines. They satisfy
\[
\sum_\sigma\lambda_{i,\sigma}\le K_i t_i,
\qquad
\prod_\sigma\lambda_{i,\sigma}
=\deg h_i\frac{V_i}{V_{i,0}}\ge x_i=t_i^{g_i}.
\tag{T17.9}
\]
For \(g_i\ge2\), arithmetic–geometric mean on the other \(g_i-1\) eigenvalues gives
\[
\lambda_{i,\sigma}
\ge\frac{t_i^{g_i}}
           {(K_i t_i/(g_i-1))^{g_i-1}}
=c_i t_i.
\]
For \(g_i=1\) the product inequality gives the same bound with \(c_i=1\). The trace gives the upper bound. Thus
\[
c_i t_i\,\omega_{i,0}
\le h_i^*\omega_i\le K_i t_i\,\omega_{i,0}.
\tag{T17.10}
\]
This is a bound in every CM eigenline, not merely a trace estimate.

**2. Integral multiplication balances the four factors**

Put
\[
T=\max_i t_i,\qquad
M_i=\left\lceil\sqrt{T/t_i}\right\rceil.
\tag{T17.11}
\]
Since \(T/t_i\ge1\),
\[
T\le M_i^2t_i\le4T.
\]
Multiplication by \(M_i\) is an actual endomorphism, so every map in (T17.5) is integral. The corresponding metric eigenvalues satisfy
\[
c_iT\le M_i^2\lambda_{i,\sigma}\le4K_iT.
\tag{T17.12}
\]
Pullback preserves the inequalities of positive forms, and integration on \(Y\) gives
\[
T\sum_i c_i E_{i,0}\le E\le4T\sum_iK_iE_{i,0}.
\tag{T17.13}
\]

Because the chosen period is a **fixed eigenmonomial**, there is no sum of potentially canceling scalars under this transport. Write
\[
([M_i]h_i)^*\beta_i=b_i\beta_{i,0}.
\]
The rank-one eigenline and the polarization-unit convention give
\[
|b_i|^2=M_i^2\lambda_{i,\sigma_i},\qquad
p=b_1b_2\overline{b_3b_4}\,p_0.
\tag{T17.14}
\]
Consequently
\[
|p_0|\bigl(\prod_i c_i\bigr)^{1/2}T^2
\le |p|
\le16|p_0|\bigl(\prod_iK_i\bigr)^{1/2}T^2.
\tag{T17.15}
\]
The lower bound proves nonvanishing and, together with the upper energy bound in (T17.13), gives the first inequality in (T17.7). Set \(\beta=\sum_i f_i^*\omega_i\). The Hodge index inequality on the fixed Kähler surface gives
\[
\int_Y\beta^2\le\frac{(\int_Y\beta\wedge\omega_Y)^2}{V_Y}.
\]
The left side is the degree of the effective pushforward, with its actual generic multiplicity, by T6.1. Dividing by \(|p|\) proves the second inequality in (T17.7). No division by an unverified generic degree has occurred. Also \(p\ne0\) implies that the first pulled-back wedge is nonzero, so \(f(Y)\) is a surface.

**3. A single common analytic normalization bounds every theta coordinate**

Choose a polarization-unit invariant CM coframe in every target. Multiply **all** its pulled-back one-forms by
\[
r=|p|^{-1/4}.
\]
The selected four-factor period then has absolute value one. The sum of the coordinate energies is exactly \(r^2E\), hence at most \(C_E\). This is a common scalar normalization of the four actual maps constructed above; the preceding balancing was by integral endomorphisms.

Now assume the fixed source coordinate pullbacks have a finite theta expansion, as supplied by T6.9 in its stated setting. Since each \(h_i\) is diagonal in the CM eigenlines, all varying target coordinate pullbacks lie in the same fixed finite-dimensional space. Take the span of the finitely many actual theta forms used in expansions of its fixed generators; this is a possibly larger finite-dimensional space containing all the pullbacks. Select a basis \(\theta_1,\ldots,\theta_q\) from those actual theta generators. Let \(G\) be its positive energy Gram matrix, using the convention
\[
\mathcal E(\eta)=\int_Y\frac i2\eta\wedge\bar\eta\wedge\omega_Y.
\]
If the normalized coordinate forms are \(\eta_j=\sum_k a_{jk}\theta_k\), then
\[
\lambda_{\min}(G)\sum_{j,k}|a_{jk}|^2
\le\sum_j\mathcal E(\eta_j)
=r^2E\le C_E.
\tag{T17.16}
\]
Fix once and for all one theta presentation for each basis vector. Linear combination gives a linear section from this finite coefficient space to a finite collection of Schwartz/source-vector spaces. Every fixed seminorm on its finite-dimensional image is bounded by a constant times the coefficient norm. Thus the normalized inputs have uniformly bounded seminorms, including the weighted local shell seminorms of B14a at the finitely many nonstandard places. The standard tails, global characters, and levels come from a fixed finite list. This proves the analytic-presentation assertion. QED.

**Exact scope and relation to the arithmetic construction.**

The initial data required here exist for the explicit T6.16 witness. Each of its four CM factors can first be replaced, once and for all, by an \(E\)-linearly isogenous factor with maximal-order action; composing the initial maps with those fixed isogenies preserves the nonzero selected period and the first wedge's automorphic constituent. The two imprimitive types in (T16.2) cause no difficulty because the proof above only uses rank-one \(E\)-homology, not simplicity. A single further fixed cover may supply the theta spanning statement. Thereafter the target lattices and their conductors may vary arbitrarily inside these four fixed \(E\)-linear isogeny classes.

The multiplication factors \(M_i\) do not introduce a new normalized divisor-kernel Chow class. Under the exact birigidified-kernel hypotheses of T6.5, they multiply both the kernel output and its selected **algebraically normalized Betti period** by \(\prod_iM_i\), so the quotient cancels exactly. This assertion only concerns the integral multiplications at a fixed target; it does not claim cancellation of the varying isogenies \(h_i\).

The period \(p\) in (T17.7) is instead defined by polarization-unit eigenforms. It need not equal the Betti-algebraic coefficient used to divide a Chow correspondence. The final common scalar \(|p|^{-1/4}\) generally changes the integral Betti lattice. Accordingly the theorem supplies bounded analytic theta presentations in a fixed-source construction and a uniform ratio of degree to metric period. It does not supply a conductor-independent effective integral degree, a bounded denominator for the Betti-algebraic normalization, or bounds uniform over varying CM fields or initial witnesses. In particular T6.16's actual nonmonomial rank-two constituent remains compatible with the finite rank-one Hecke-energy upper bound: the latter is an inequality using all normalized coordinates, not an identity that replaces the rank-two spectral factor by a character.

**Whole-proof check.**

The proof imports the checked exact CM Hom covolume and Minkowski bound of B19.1–B19.2, and the already checked geometric degree/Hodge-index and theta-spanning statements T6.1/T6.9. The entire proof was read by this agent and independently by root and the bounds agent. These checks recomputed the lower bound for each metric eigenvalue, the integer balancing inequalities, the noncanceling eigenmonomial period, the common fourth-root normalization, and the distinction between metric and Betti period. All three reviews passed before promotion to this module.


## 13. Exact integral coefficient content of the four-factor switch

### DEG-L.T6.18 — Exact integral eigenline content

Use a fixed Galois CM field \(E\), \(\mathcal O=\mathcal O_E\), and four CM types as in T6.16. Fix reference factors
\[
A_{i,0}=\mathbf C^s/\Phi_i(I_{i,0})
\]
with invertible fractional \(\mathcal O\)-ideals \(I_{i,0}\), and actual maps \(f_{i,0}:Y\to A_{i,0}\) from a fixed smooth projective surface. Assume their selected \((1,1,c,c)\) four-factor Betti period is nonzero. Let
\[
A_i=\mathbf C^s/\Phi_i(\Lambda_i),\qquad
\Lambda_i^+=\mathcal O\Lambda_i,\qquad
\Lambda_i^-=\{x\in\Lambda_i:\mathcal O x\subset\Lambda_i\},
\]
where the full target lattices need not be \(\mathcal O\)-stable. Put
\[
I_i=(\Lambda_i:I_{i,0})=\Lambda_i^-I_{i,0}^{-1},\qquad
\mathfrak r_i=\Lambda_i^-(\Lambda_i^+)^{-1}\subseteq\mathcal O,
\quad J_i=[\Lambda_i:\Lambda_i^-],\quad H_i=[\Lambda_i^+:\Lambda_i].
\tag{T18.1}
\]

Identify \(H^1(A_i,E)\) with \(\operatorname{Hom}_{\mathbf Q}(E,E)\). For \(\tau\in\operatorname{Gal}(E/\mathbf Q)\), write \(e_{i,\tau}(x)=\tau(x)\), and define the **actual integral coefficient eigenline**
\[
\mathcal L_{i,\tau}
=Ee_{i,\tau}\cap\bigl(H^1(A_i,\mathbf Z)\otimes_{\mathbf Z}\mathcal O\bigr).
\tag{T18.2}
\]
Use \(\mathcal L_{i,0,\tau}\) for the corresponding reference lattice. Then
\[
\begin{aligned}
\mathcal L_{i,\tau}
&=\tau(\Lambda_i^+)^{-1}e_{i,\tau},\\
\sum_{h_i\in\operatorname{Hom}_E(A_{i,0},A_i)}h_i^*\mathcal L_{i,\tau}
&=\tau(\mathfrak r_i)\mathcal L_{i,0,\tau},\\
[\mathcal L_{i,0,\tau}:\sum_{h_i}h_i^*\mathcal L_{i,\tau}]
&=N_{E/\mathbf Q}(\mathfrak r_i)=J_iH_i.
\end{aligned}
\tag{T18.3}
\]
The sums are additive subgroup sums; each image is already an \(\mathcal O\)-submodule. If the target polarization is principal and its Rosati involution restricts to conjugation on \(E\), then \(H_i=J_i\), so the last index is \(J_i^2\).

Let \(\mathfrak P_0\subseteq\mathcal O\) be the additive group generated by the selected four-factor periods of the fixed maps \(f_{i,0}\) as the four eigenvectors range through
\[
\mathcal L_{1,0,1},\quad\mathcal L_{2,0,1},\quad
\mathcal L_{3,0,c},\quad\mathcal L_{4,0,c}.
\]
It is a nonzero integral ideal. Let \(\mathfrak P_A\) be the additive group of periods obtained by varying all actual integral \(E\)-linear maps \(h_i:A_{i,0}\to A_i\) and all eigenvectors in the four corresponding target integral coefficient eigenlines, with maps \(h_if_{i,0}\). Then
\[
\mathfrak P_A
=\mathfrak r_1\mathfrak r_2\overline{\mathfrak r_3}\,
             \overline{\mathfrak r_4}\,\mathfrak P_0,
\qquad
[\mathfrak P_0:\mathfrak P_A]=\prod_{i=1}^4J_iH_i.
\tag{T18.4}
\]
For principal compatible targets this index is \(\prod_iJ_i^2\). These are exact ideal and additive-index identities, not just bounds on absolute values under one complex embedding.

**Proof.**

Integral first cohomology is \(\operatorname{Hom}_{\mathbf Z}(\Lambda_i,\mathbf Z)\). Since \(\Lambda_i\) is finite free over \(\mathbf Z\), tensoring with \(\mathcal O\) identifies its integral coefficient lattice with \(\operatorname{Hom}_{\mathbf Z}(\Lambda_i,\mathcal O)\). Thus \(u e_{i,\tau}\) is integral exactly when
\[
u\tau(\Lambda_i)\subseteq\mathcal O.
\]
Because \(\mathcal O\) is a ring, this is equivalent to \(u\tau(\mathcal O\Lambda_i)\subseteq\mathcal O\). The maximal-order lattice \(\Lambda_i^+\) is an invertible fractional ideal, so this condition is exactly \(u\in\tau(\Lambda_i^+)^{-1}\). This proves the first formula of (T18.3), with no discriminant denominator or saturation assumption.

The map corresponding to \(\alpha\in I_i\) acts on the selected eigenline by
\[
h_\alpha^*e_{i,\tau}=\tau(\alpha)e_{i,0,\tau}.
\]
The additive sum of the pullback lattices is therefore
\[
\begin{aligned}
\tau(I_i)\tau(\Lambda_i^+)^{-1}e_{i,0,\tau}
&=\tau(\Lambda_i^-(\Lambda_i^+)^{-1})
  \tau(I_{i,0})^{-1}e_{i,0,\tau}\\
&=\tau(\mathfrak r_i)\mathcal L_{i,0,\tau}.
\end{aligned}
\]
Taking the index in a rank-one projective \(\mathcal O\)-module gives \(N(\mathfrak r_i)\). The usual ideal-index formula gives
\[
N(\mathfrak r_i)=[\Lambda_i^+:\Lambda_i^-]=H_iJ_i.
\]
These identities hold for fractional ideals as well as integral ones.

For the principal-polarization assertion, use the alternating Riemann form to define the dual lattice \(M^\#\). Principal polarization says \(\Lambda_i^\#=\Lambda_i\). Rosati conjugation gives \(\langle ax,y\rangle=\langle x,\bar a y\rangle\) for every \(a\in E\), including rational endomorphisms. Since \(\bar{\mathcal O}=\mathcal O\),
\[
(\mathcal O\Lambda_i)^\#=(\Lambda_i^\#)^-=\Lambda_i^-.
\]
Duality reverses lattice indices, so
\[
H_i=[\Lambda_i^+:\Lambda_i]
=[\Lambda_i^\#:(\Lambda_i^+)^\#]
=[\Lambda_i:\Lambda_i^-]=J_i.
\]
This proves all of (T18.3).

For the period statement, put
\[
k_0=\int_Y f_{1,0}^*e_{1,0,1}\wedge f_{2,0}^*e_{2,0,1}
                  \wedge f_{3,0}^*e_{3,0,c}\wedge f_{4,0}^*e_{4,0,c}
\in E^\times.
\tag{T18.5}
\]
The maps have integral pullback on first cohomology and the fundamental class is integral, so evaluation of four integral \(\mathcal O\)-coefficient classes belongs to \(\mathcal O\). Multilinearity gives the exact reference ideal
\[
\mathfrak P_0
=k_0 I_{1,0}^{-1}I_{2,0}^{-1}
          \overline{I_{3,0}}^{-1}\overline{I_{4,0}}^{-1}
\subseteq\mathcal O.
\tag{T18.6}
\]
It is nonzero by the initial period hypothesis.

Each varying pulled-back eigenvector lies in the transport module in (T18.3). Conversely every element of that transport module is a finite sum of actual pullbacks. Expanding a fourfold product of such sums shows that the additive period group is exactly the image of the four transport modules under the fixed multilinear functional. Substituting (T18.3) proves the ideal identity (T18.4). This is equality for the additive span actually specified, not an enlargement introduced without justification: multiplication of one allowed target eigenvector by \(a\in\mathcal O\) already gives another allowed vector. Even with fixed target eigenvectors, varying \(h_1\) by precomposition with the actual reference endomorphism \([a]\) multiplies its period by \(a\); the maximal-order reference action is used here. The ideal-index formula now proves the final equality. QED.

**Fixed compatible generators versus integral target eigenvectors.**

If the four target rational eigenvectors are fixed to be the universal \(e_{i,\tau_i}\), without imposing integrality, the additive span of their transported periods is instead
\[
k_0 I_1I_2\overline{I_3}\,\overline{I_4}.
\tag{T18.7}
\]
Passing from (T18.7) to the genuinely integral eigenline statement inserts the four dual hull ideals. Thus neither a choice of complex unit forms nor a compatible rational basis can be substituted for the integral target eigenvectors without recording that change of lattice.

In T6.16 all source and target eigenline coefficients can be kept in this same fixed Galois CM field \(E\): the maps selected after CM extraction are rational Hodge maps and, after denominator clearing, integral morphisms; the eigenvectors are the \(E\)-valued embedding functionals above. The auxiliary theta spectral projector may require a larger field for its own description, but it does not enlarge the field of the final four-factor Betti coefficient \(k_0\). No rationality of an analytic theta normalization is asserted.

**What this does and does not force on integer normalization.**

Fix \(0\ne\kappa\in\mathfrak P_0\), and put \(d=[E:\mathbf Q]\) and \(c_\kappa=[\mathfrak P_0:\mathcal O\kappa]\). If an integral linear combination of the allowed period values equals \(N\kappa\) for a positive integer \(N\), then
\[
\prod_iJ_iH_i\ \mid\ N^d c_\kappa,
\qquad
N\ge\left(\frac{\prod_iJ_iH_i}{c_\kappa}\right)^{1/d}.
\tag{T18.8}
\]
Indeed \(\mathcal O(N\kappa)\subseteq\mathfrak P_A\subseteq\mathfrak P_0\), and multiplication by the rational integer \(N\) has index \(N^d\). This is a membership obstruction for the stated coefficient module. It is not a lower bound for arbitrary target cycles or for every possible trace construction with varying correspondences.

Even taking a trace to \(\mathbf Q\) can lose information from an ideal-index obstruction. For example, in \(\mathbf Z[i]\), all ideals \((2+i)^r\) have trace ideal \(2\mathbf Z\), although their indices are \(5^r\). To check this, write \((2+i)^r=a+bi\). Any common prime divisor of \(a,b\) must divide \(a^2+b^2=5^r\); divisibility by \(5=(2+i)(2-i)\) is impossible because the two Gaussian prime ideals are distinct. Hence \(\gcd(a,b)=1\), and the traces of \((a+bi)(u+vi)\) generate \(2\mathbf Z\). Therefore one cannot infer an unbounded rational trace denominator from (T18.4) alone. A trace argument must retain its full target tensor or cycle lattice.

**Relation with B23.**

B23 concerns middle-degree **pushforwards** on the rank-two generic \(K\)-Weil determinant line and includes its relative target determinant ideal. Its common content is the conjugate ideal \(\bar{\mathfrak j}\), of norm \(J\). The present result concerns four independent **pullbacks** into specified full-CM eigenlines and has the core/hull ideals \(\mathfrak r_i\). The auxiliary product in T6.16 has dimension sixteen and its tested switch tensor has degree four, so it is not itself B23's middle Weil plane. Passing from that switch to a specified generic Weil target must retain the actual correspondence and its integral lattice map. The two formulas explain different arithmetic costs and must not be identified without that additional map.

The ideal-index input is Milne, *Algebraic Number Theory*, v3.08, Proposition 4.2, printed pp.69–70, <https://www.jmilne.org/math/CourseNotes/ANT.pdf>; its statement and complete short proof have been read. The Hom-ideal and Rosati duality identities are the checked B19/T6.17 identities, restated and proved in the needed form above. The entire saved proof was read by the author and independently by root and the bounds agent; all three reviews passed before promotion. The checks verified the actual integral coefficient lattice, the core/hull index and principal-polarization duality, the multilinear additive-span equality, and the scope of the integer and trace obstructions.


## 14. Exact trace presentation and actual principal CM families

### DEG-L.T6.19 — Exact scalar and tensor trace presentation indices

Let \(E\) be a Galois CM field of degree \(d=2g\), let \(\mathcal O\) be its ma\(\xi\)mal order, and let \(c\) be complex conjugation. Retain the four fixed CM types, ma\(\xi\)mal-order references, fixed surface, and nonzero four-factor Betti period of T6.18. Write \(\mathfrak P_A\) for its exact integral period ideal. The following statements hold.

##### 1. Scalar trace has an exact minimum-valuation formula

Let \(\mathfrak a\) be any nonzero fractional \(\mathcal O\)-ideal. Write \(\mathfrak D\) for the different of \(E/\mathbf Q\) and write
\[
 a_{\mathfrak p}=v_{\mathfrak p}(\mathfrak a),\qquad
 d_{\mathfrak p}=v_{\mathfrak p}(\mathfrak D),\qquad
 e_{\mathfrak p}=e(\mathfrak p/p).
\]
The nonzero fractional ideal of \(\mathbf Q\) generated by the scalar traces is
\[
 \operatorname{Tr}_{E/\mathbf Q}(\mathfrak a)
 =\prod_p p^{\,\min_{\mathfrak p\mid p}
       \lfloor(a_{\mathfrak p}+d_{\mathfrak p})/e_{\mathfrak p}\rfloor}\mathbf Z.
 \tag{T19.1}
\]
In particular, when \(\mathfrak a\) is integral and its trace ideal is \(m\mathbf Z\), the least positive common rational denominator needed to obtain the scalar 1 from finite rational linear combinations of traces of elements of a is exactly m. This assertion concerns a scalar trace, not the full rational tensor obtained by tracing a coefficient-valued cycle.

##### 2. Principal CM lattices impose conjugation symmetry

For a principally polarized CM target with rational E-action and Rosati conjugation, let
\[
 \mathfrak r=\Lambda^-(\Lambda^+)^{-1}
\]
be the core/hull ideal of T6.18. Then
\[
 \overline{\mathfrak r}=\mathfrak r.
 \tag{T19.2}
\]
Thus the Gaussian-prime ideal in T6.18's abstract trace example is not itself a possible principal-target core/hull ideal. This restriction does not force trace content to grow with its norm when \(g\ge2\).

##### 3. Two actual principal-polarization families

Fix, for each of the four CM types, any principally polarized lattice \(\Lambda_{i,*}\) with Rosati conjugation. Such a lattice e\(\xi\)sts in each of the relevant rational CM isogeny classes. Let \(\mathfrak P_*\) be the period ideal of T6.18 for these four targets. Choose a rational prime p that splits completely in E and avoids a fixed finite set: the discriminant, all places where the four base lattices are not ma\(\xi\)mal-order-stable, and the numerator and denominator ideals occurring in the fixed data. Additional fixed nonzero coefficients may also be required to be units at p.

For every integer \(r\ge0\) there are actual principally polarized target lattices \(\Lambda_{i,r}\), with the same CM types, the same rational E-actions, and the same polarization volumes, with either of the following properties.

**Uniform family.** Modify all \(g\) conjugate pairs at p in all four factors. Then
\[
 \mathfrak r_{i,r}=p^r\mathfrak r_{i,*},\qquad
 J_{i,r}=p^{gr}J_{i,*},\qquad
 \mathfrak P_r=p^{4r}\mathfrak P_*.
 \tag{T19.3}
\]
Consequently
\[
 \operatorname{Tr}(\mathfrak P_r)
   =p^{4r}\operatorname{Tr}(\mathfrak P_*).
 \tag{T19.4}
\]
The least denominator for scalar trace normalization therefore grows by exactly \(p^{4r}\).

**Concentrated family, \(g\ge2\).** Modify only one conjugate pair in the first factor and leave the other factors fixed. If \(\mathfrak q=\mathfrak p\,c(\mathfrak p)\) denotes the product of the corresponding two primes above p, then
\[
 \mathfrak r_{1,r}=\mathfrak q^r\mathfrak r_{1,*},\qquad
 J_{1,r}=p^rJ_{1,*},\qquad
 \mathfrak P_r=\mathfrak q^r\mathfrak P_*.
 \tag{T19.5}
\]
Although its additive index grows by \(p^{2r}\),
\[
 \operatorname{Tr}(\mathfrak P_r)
    =\operatorname{Tr}(\mathfrak P_*).
 \tag{T19.6}
\]
These are realized CM abelian varieties, rather than arbitrary ideal examples.

##### 4. Full four-factor trace retains the coefficient ideal

Fix output CM factors \(B_i\) of the four reference types, and fix nonzero integral \(\mathcal O\)-coefficient eigenvectors \(\beta_i\) whose types are opposite to those of the corresponding input eigenvectors \(\alpha_i\). Thus every scalar conjugate of \(\alpha_i\otimes\beta_i\) is of type (1,1). Put
\[
 t=\beta_1\otimes\beta_2\otimes\beta_3\otimes\beta_4.
\]
The tensor lies in the degree-four Kunneth summand of \(B=\prod_iB_i\). Its \(d\) scalar Galois conjugates lie in distinct eigenspaces and are linearly independent over \(E\). Let \(W\) be their rational descent and define
\[
 \mathcal T_t:E\longrightarrow W,\qquad
 a\longmapsto\sum_{\sigma\in\operatorname{Gal}(E/\mathbf Q)}
                      \sigma(a)\sigma(t).
 \tag{T19.7}
\]
Then \(\mathcal T_t\) is a \(\mathbf Q\)-linear isomorphism.

For each integral input eigenvector and each actual integral map admitted by T6.18, choose \(\mathcal O\)-coefficient divisor kernels with pure classes \(\alpha_i\otimes\beta_i\) and apply their product to the surface pushforward. The additive group of rational cohomology classes obtained by coefficientwise trace and integral linear combinations is exactly
\[
 \mathcal T_t(\mathfrak P_A).
 \tag{T19.8}
\]
In particular, integral \(\mathcal O\) multipliers inside the traces do not enlarge this group. For fixed \(0\ne\kappa\in\mathfrak P_*\) and \(w=\mathcal T_t(\kappa)\), the least positive common denominator of a rational linear combination of these traced classes that equals w is exactly the positive generator of
\[
 (\kappa^{-1}\mathfrak P_A)\cap\mathbf Z.
 \tag{T19.9}
\]
Equivalently its p-valuation is
\[
 \max\left(0,\max_{\mathfrak p\mid p}
     \left\lceil\frac{v_{\mathfrak p}(\mathfrak P_A)
                           -v_{\mathfrak p}(\kappa)}{e_{\mathfrak p}}\right\rceil\right).
 \tag{T19.10}
\]
This is a ma\(\xi\)mum over primes above p, in contrast to the minimum in the scalar trace formula.

Take \(p\) additionally prime to \(\kappa\). In the uniform family (T19.3) the exact denominator is \(p^{4r}\). In the concentrated family (T19.5) it is \(p^r\), even though the scalar trace ideal is constant. Dividing w once by its fixed integral cohomology content gives a fixed primitive rational Hodge class; excluding the primes dividing that fixed content preserves these exact p-valuations. Thus a primitive scalar trace does not supply a bounded-denominator presentation of the primitive four-factor tensor in the specified unscaled output group. This does not preclude Chow divisibility and cancellation after normalization.

#### Proof

##### Scalar traces and dual ideals

Define the inverse different by
\[
 \mathfrak D^{-1}=\{x\in E:\operatorname{Tr}(x\mathcal O)\subseteq\mathbf Z\}.
\]
For an \(\mathcal O\)-ideal \(\mathfrak a\) and a rational prime \(p\), localization gives
\[
 \operatorname{Tr}(\mathfrak a)\subseteq p^m\mathbf Z_{(p)}
 \quad\Longleftrightarrow\quad
 \mathfrak a\mathcal O_{(p)}\subseteq p^m\mathfrak D^{-1}\mathcal O_{(p)}.
 \tag{T19.11}
\]
The reverse implication follows by taking the product with 1. For the forward implication, every \(x\in\mathfrak a\) and every \(b\in\mathcal O\) satisfy \(xb\in\mathfrak a\), so the trace condition holds for \(\operatorname{Tr}(xb)\), which is exactly membership in the trace dual. The same argument after localization handles fractional ideals and every integer m. Comparing ideal valuations in (T19.11) gives
\[
 a_{\mathfrak p}\ge me_{\mathfrak p}-d_{\mathfrak p}
 \quad\hbox{for every }\mathfrak p\mid p.
\]
The largest permitted \(m\) is the exponent in (T19.1). This proves the formula.

The trace image of an integral ideal is a nonzero subgroup \(m\mathbf Z\). Its generator is attained as a finite integral combination of traces; indeed the trace image itself is already an additive subgroup. If a common denominator \(D\) produces \(1\), clearing it gives \(D\in m\mathbf Z\), so \(m\mid D\). Conversely dividing a trace equal to \(m\) by \(m\) produces \(1\). This proves the asserted optimal scalar denominator.

##### Conjugation symmetry of the core/hull ideal

Write the rational Riemann form as
\[
 \psi(x,y)=\operatorname{Tr}_{E/\mathbf Q}(\xi x\bar y),
 \qquad \bar\xi=-\xi.
 \tag{T19.12}
\]
Such a form follows directly from Rosati conjugation: \(\psi(x,y)=\ell(x\bar y)\), the nondegenerate trace pairing writes \(\ell(z)=\operatorname{Tr}(\xi z)\), and alternatingness makes \(\bar\xi=-\xi\). For any fractional \(\mathcal O\)-ideal \(I\), its \(\psi\)-dual is
\[
 I^\#=\xi^{-1}\mathfrak D^{-1}\bar I^{-1}.
\]
The sign convention for the alternating form can insert a minus sign, which does not alter this ideal. Principal polarization and T6.18 give \(\Lambda^-=(\Lambda^+)^\#\), whence
\[
 \mathfrak r
 =\xi^{-1}\mathfrak D^{-1}(\Lambda^+\overline{\Lambda^+})^{-1}.
 \tag{T19.13}
\]
The different is conjugation-stable, the last factor is manifestly so, and conjugating \(\xi^{-1}\) changes its sign. This proves (T19.2).

##### Constructing the actual lattices

First, there is no e\(\xi\)stence assumption on a principal ma\(\xi\)mal-order polarization. Start with a rational Riemann form of the CM type on E tensor R. One can choose \(\xi\) in the purely imaginary part of E with the required signs at the finitely many archimedean embeddings: write \(\xi=\delta a\) with a in \(E^+\), and use density of \(E^+\) in its product of real embeddings to prescribe the signs. A rational symplectic basis for this nondegenerate alternating Q-form spans a lattice \(\Lambda_*\) on which \(\psi\) is integral and unimodular. The positivity and complex-structure compatibility of \(\psi\) are unchanged. Thus the Riemann criterion gives a principally polarized complex abelian variety of the specified CM type, with rational E-action and Rosati conjugation. It need not have integral ma\(\xi\)mal-order action, which is not needed.

There are only finitely many rational primes at which \(\Lambda_*\) differs locally from a fractional ma\(\xi\)mal-order ideal or at which its fixed rational Riemann coefficients are not units. Choose p split completely and outside all these exceptional sets for all four factors. Infinitely many completely split primes e\(\xi\)st; only this qualitative classical fact is used, with no effective or GRH input.

At p the algebra E tensor Q_p is a product of 2g copies of Q_p, and O tensor \(\mathbf Z_p\) is the corresponding product of \(\mathbf Z_p\). Complex conjugation pairs the factors. Choose unit generators e_j,f_j of each pair so that the local base lattice and Riemann form are
\[
 \Lambda_{*,p}=\bigoplus_{j=1}^g(\mathbf Z_p e_j\oplus\mathbf Z_p f_j),
 \qquad \psi(e_j,f_k)=\delta_{jk},
\]
with every other pairing between generators zero. The unit rescalings do not change the local ma\(\xi\)mal-order lattice.

Replace one selected pair by
\[
 L_r=\mathbf Z_p e\ +\ \mathbf Z_p(f+p^{-r}e).
 \tag{T19.14}
\]
The displayed basis has symplectic pairing 1, so \(L_r\) is self-dual. Its ma\(\xi\)mal-order hull and core are, respectively,
\[
 L_r^+=p^{-r}\mathbf Z_p e\oplus\mathbf Z_p f,
 \qquad
 L_r^-=\mathbf Z_p e\oplus p^r\mathbf Z_p f.
 \tag{T19.15}
\]
For the core, the e-a\(\xi\)s intersection is \(\mathbf Z_p e\), while a vector b f belongs to \(L_r\) exactly when \(p^{-r}b\) lies in \(\mathbf Z_p\). These a\(\xi\)s intersections give the largest submodule for the product ring \(\mathbf Z_p\times\mathbf Z_p\). The hull follows by projecting the two generators onto the two axes. Therefore
\[
 [L_r:L_r^-]=[L_r^+:L_r]=p^r,
 \qquad L_r^-(L_r^+)^{-1}=(p^r,p^r).
 \tag{T19.16}
\]

Keep the base lattice at every other finite prime. These local prescriptions determine a global full lattice in E. Concretely, for sufficiently large a, the new local lattice lies between \(p^a\Lambda_{*,p}\) and \(p^{-a}\Lambda_{*,p}\); its image in the finite quotient \(p^{-a}\Lambda_{*,p}/p^a\Lambda_{*,p}\) corresponds to a subgroup of \(p^{-a}\Lambda_*/p^a\Lambda_*\). Its inverse image is the required global lattice. Its completions are exactly the prescribed ones. Duality commutes with completion, so it remains self-dual everywhere and hence globally. The fixed Riemann form remains positive for the fixed CM type, giving actual principally polarized CM abelian varieties. This also proves all required isogeny and fixed-volume assertions.

Applying (T19.16) in every pair gives a local core/hull ideal \(p^r\mathcal O_p\) and core index \(p^{gr}\); outside p the ideal and index are unchanged. Applying it in a single pair gives \(\mathfrak q^r\) and core index \(p^r\). Core and hull commute with localization because their defining lattice conditions involve a finite integral basis of O. T6.18 now gives (T19.3) and (T19.5). In the uniform family the period ideal is multiplied by the rational integer \(p^{4r}\), proving (T19.4). In the concentrated family the p-adic trace is the sum of the 2g coordinates. At least one unmodified coordinate remains when g is at least two, so its trace image is \(\mathbf Z_p\), just as at r=0. At every other prime the ideals are unchanged. This proves (T19.6).

##### Full tensor trace and divisor-kernel outputs

Choose \(\beta_i\) in the opposite embedding line of the fixed output factor of the same CM type. Every scalar conjugate of \(\alpha_i\otimes\beta_i\) is then a (1,1) class. The first factor alone distinguishes all Galois conjugates of t: applying \(\sigma\) changes its embedding label by \(\sigma\), and no nonidentity automorphism fixes that label. Thus the d tensors \(\sigma(t)\) are E-linearly independent. Their span is Galois-stable. An invariant vector in it has coefficients \(\sigma(a)\) for one a in E, because invariance identifies every coefficient with the corresponding conjugate of the identity coefficient. This proves surjectivity of (T19.7) onto its rational descent W. Injectivity follows because a zero sum of the independent conjugates forces every \(\sigma(a)\) to vanish. The switch relation makes every conjugate tensor of type (2,2), so W consists of rational Hodge classes.

For completeness, the integral divisor-kernel step uses exactly the all-conjugates hypothesis of T6.7. The pure class \(\alpha_i\otimes\beta_i\) belongs to integral cohomology tensored with O. Every scalar conjugate has type (1,1), so its rational coefficient components lie in the rational Neron--Severi space. The integral Neron--Severi lattice is saturated in integral \(H^2\), by the integral (1,1) theorem and the absence of torsion for an abelian variety. Intersecting with the integral coefficient lattice therefore puts the class in \(\operatorname{NS}\otimes\mathcal O\). Choose an O-linear combination of divisor classes representing it. This introduces no varying denominator. Its pure mixed Kunneth component permits the usual birigidified representative; this is the same divisor-kernel framework as T6.5 and T6.7.

Let K be the product of these four kernels, and z the actual surface pushforward. The projection formula gives \(\operatorname{cl}(K_*z)=kt\), where k is the selected integral coefficient period. Taking the trace in the coefficient ring gives an integral cycle whose class is \(\mathcal T_t(k)\). Here scalar Galois acts on the coefficient field, not on the complex algebraic cycles themselves. By T6.18 the additive period group is exactly \(\mathfrak P_A\), so expanding finite sums proves both inclusions in (T19.8). Multipliers in O preserve \(\mathfrak P_A\) and hence do not enlarge the image.

If a rational combination with common denominator D represents \(w=\mathcal T_t(\kappa)\), clearing denominators gives \(Dw\in\mathcal T_t(\mathfrak P_A)\). Injectivity is equivalent to \(D\kappa\in\mathfrak P_A\). Conversely that membership and (T19.8) produce such an integral combination after multiplying w by D. Hence the least denominator is (T19.9). Ideal valuations give (T19.10), including the ma\(\xi\)mum with zero because D must be an integer.

Choose p avoiding the fixed nonzero coefficient \(\kappa\) and the fixed base ideal. In the uniform family the condition is \(D\kappa\in p^{4r}\mathfrak P_*\), whose least positive solution is D=\(p^{4r}\). In the concentrated family the two selected p-adic valuations require \(v_p(D)\) at least r, while D=\(p^r\) satisfies every ideal inclusion; the least denominator is \(p^r\). The fixed primitive normalization of w changes these valuations by at most a fixed constant, and by none when p is chosen away from its fixed content. This proves all assertions. QED.

#### What this resolves and the remaining scope

The metric-normalized maps of T6.17 e\(\xi\)st along both families: the surface, CM fields and types, fixed theta presentations, and output tensor remain fixed. Their bounded analytic energies and bounded Schwartz seminorms coe\(\xi\)st with unbounded denominators of presentations in the additive group of **unscaled** traced outputs. The exact local formula measures the saturation needed to pass from that group to a fixed rational tensor. It does not measure the intrinsic denominator of the resulting Chow class.

Indeed, there is exact cancellation at fixed output. Choose fixed source pure birigidified divisor kernels \(D_{i,0}\). If \(h_i^*\alpha_i=\lambda_i\alpha_{i,0}\), then injectivity of the first Chern class on the birigidified Picard group, after extension of coefficients to E, gives
\[
 (h_i\times1)^*D_i=\lambda_iD_{i,0}
 \quad\hbox{in }\operatorname{CH}^1\otimes E.
\]
This is an equality of the entire coefficient-valued class, not just one complex embedding. Projection and multiplication give raw output \(C_A=(\prod_i\lambda_i)C_0\), while its selected period is \(k_A=(\prod_i\lambda_i)k_0\). Therefore
\[
 \frac{C_A}{k_A}=\frac{C_0}{k_0}
 \quad\hbox{in }\operatorname{CH}^2(B)\otimes E.
\]
Coefficientwise trace after this cancellation is fixed, so it has a fixed intrinsic rational Chow denominator. Candidate T6.20 proves this carefully and treats simultaneous variation of the output. The growing index in (T19.8) is fully compatible with this cancellation: an unscaled output may be divisible in the larger Chow group even though its division is unavailable inside the chosen unscaled subgroup.

The exact formulas identify a positive arithmetic mechanism as well: scalar trace presentation is possible with precisely the trace-ideal generator, and full-tensor presentation is possible with precisely the integer ideal-membership generator. They do not bound the sizes of integer coefficients in a chosen Bezout presentation or the degrees of the signed cycles. Allowing weights in a fixed fractional coefficient lattice changes only a fixed set of prime denominators; it cannot change (T19.10) at the chosen good prime. Allowing variable weights whose denominators contain p is precisely the division being measured.

The full tensor trace must not be replaced by scalar trace. Its injectivity preserves the coefficient ideal before saturation. The concentrated principal family has unchanged scalar trace ideal but unbounded tensor-presentation index. Any claim about an intrinsic moving-output denominator requires the actual Chow transport and divisibility calculation, rather than this index alone.

#### Primary sources used and exact check scope

1. Keith Conrad, *The Different Ideal*, Definition 3.2, printed p.4; Theorem 3.9 and complete proof, and Theorem 3.10 and complete proof, printed p.8; Definition 4.1, printed p.9. Author source: <https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf>. These give the trace-dual conventions. Formula (T19.1) and its local proof are supplied above, not asserted to be a quotation of a numbered result there.
2. J.S. Milne, *Abelian Varieties*, v2.00, Chapter I, Theorems 2.8--2.9, printed p.14, and the polarization construction and definition, printed p.15. Author source: <https://www.jmilne.org/math/CourseNotes/AV.pdf>. The Riemann criterion and algebraicity of the complex-torus maps are imported; the principal CM lattice and deformation constructions above are proved directly.
3. J.S. Milne, *Algebraic Number Theory*, v3.08, Theorem 8.31 and Corollary 8.32, printed p.147. Author source: <https://www.jmilne.org/math/CourseNotes/ANT.pdf>. Only the e\(\xi\)stence of a completely split prime outside a finite set is imported. This is qualitative Chebotarev; no quantitative estimate or GRH audit is involved.
4. T6.7 and T6.18 supply the already checked integral divisor-kernel descent and exact period ideal. T6.17 supplies the independently checked bounded metric normalization in the fixed-source setting. Their proofs are not silently strengthened here.

#### Check status

Author, root, and bounds have read the complete initial arithmetic proof and found no gap in the formulas. The scope has been revised to distinguish presentation denominators from intrinsic Chow denominators; the fixed-output cancellation was independently checked with bounds. The revised complete proof and its scope/cancellation addition passed final root and bounds review before promotion. No local compilation is claimed.

## 15. Chow cancellation removes input-period denominators

### DEG-L.T6.20 — Exact Chow cancellation and simultaneous input/output transport

Work over the complex numbers and fix the Galois CM coefficient field \(E\). All eigenvectors below are \(E\)-coefficient Betti vectors, not polarization-unit vectors obtained by arbitrary complex rescaling. For four factors let
\[
 h_i:A_{i,0}\longrightarrow A_i,\qquad
 g_i:B_{i,0}\longrightarrow B_i
\]
be actual \(E\)-linear isogenies between fixed-type CM abelian varieties. Write \(h=\prod_i h_i\), \(g=\prod_i g_i\), and let \(z_0=f_{0*}[Y]\) for fixed actual maps from a smooth projective surface to \(A_0=\prod_iA_{i,0}\). Choose nonzero eigenvectors with
\[
 h_i^*\alpha_i=\lambda_i\alpha_{i,0},\qquad
 g_i^*\beta_i=\mu_i\beta_{i,0},\qquad
 \lambda_i,\mu_i\in E^\times.
 \tag{T20.1}
\]
Assume every scalar conjugate of each \(\alpha_i\otimes\beta_i\) has Hodge type \((1,1)\), and similarly for the reference vectors. Choose the uniquely determined birigidified divisor-correspondence classes
\[
 D_i\in\operatorname{CH}^1(A_i\times B_i)\otimes E,
 \qquad
 D_{i,0}\in\operatorname{CH}^1(A_{i,0}\times B_{i,0})\otimes E
\]
with these pure mixed Betti classes. Let \(K=\prod_iD_i\), \(K_0=\prod_iD_{i,0}\), with the usual pullbacks to the full products. Assume
\[
 k_0=\int_Y f_{1,0}^*\alpha_{1,0}\wedge\cdots\wedge
                         f_{4,0}^*\alpha_{4,0}\ne0,
 \qquad C_0=K_{0*}z_0/k_0.
\]
Set
\[
 \Lambda=\prod_i\lambda_i,\qquad M=\prod_i\mu_i,
 \qquad k_h=\Lambda k_0,\qquad
 C_{A,B}=K_*h_*z_0/k_h.
\]
All surface pushforwards retain their actual multiplicities.

##### A. Exact cancellation and simultaneous transport

There are identities in Chow groups with \(E\) coefficients
\[
 (h_i\times g_i)^*D_i=\lambda_i\mu_iD_{i,0},
 \tag{T20.2}
\]
\[
 g^*C_{A,B}=M C_0,
 \qquad
 C_{A,B}=\frac{M}{\deg g}\,g_*C_0.
 \tag{T20.3}
\]
Every input factor \(\lambda_i\) cancels. In particular, at fixed output \(B=B_0\), with fixed output eigenvectors and \(g=1\),
\[
 C_{A,B_0}=C_0.
 \tag{T20.4}
\]
This extends T6.5 from clearing integers to arbitrary actual \(E\)-linear input isogenies, provided that the source surface maps and output are fixed and the kernels are the pure birigidified classes stated here. Coefficientwise traces of the normalized cycle are then fixed rational Chow classes and have fixed intrinsic rational denominators. A growing index of the unscaled outputs, as in T6.19, does not contradict (T20.4).

##### B. Genuine dual outputs and the direction of the dual isogeny

Suppose \(B_i=A_i^\vee\), \(B_{i,0}=A_{i,0}^\vee\), and \(D_i\), \(D_{i,0}\) are the selected \(E\)-eigencomponents of the normalized Poincare bundles. Normalize \(\beta_i\), \(\beta_{i,0}\) by these Poincare components, so their pure classes are exactly \(\alpha_i\otimes\beta_i\) and \(\alpha_{i,0}\otimes\beta_{i,0}\). Then the actual dual isogeny points in the reverse direction:
\[
 q=\prod_i h_i^\vee:B=\prod_iA_i^\vee
                      \longrightarrow B_0=\prod_iA_{i,0}^\vee.
\]
The exact formulas are
\[
 (h_i^\vee)^*\beta_{i,0}=\lambda_i\beta_i,
 \qquad
 K_*h_*z_0=q^*(K_{0*}z_0),
 \tag{T20.5}
\]
\[
 C_{A,B}=\Lambda^{-1}q^*C_0,
 \qquad
 q_*C_{A,B}=\frac{\deg q}{\Lambda}\,C_0.
 \tag{T20.6}
\]
Thus the moving-output problem is an actual isogeny pullback followed by a specified coefficient division. It is not a residual input-period ambiguity.

##### C. Uniform denominator for factorwise integral output tensors

There is a useful construction that does not require varying the input factors at all. Fix integral \(\mathcal O_E\)-coefficient input eigenvectors \(\alpha_{i,0}\), fixed actual \(f_{i,0}\), and their nonzero period \(k_0\in\mathcal O_E\). Let the output CM factors \(B_i\) vary arbitrarily within the required fixed CM types. For every choice of integral \(\mathcal O_E\)-coefficient output eigenvectors \(\beta_i\) of the opposite types, there exist integral \(\mathcal O_E\)-coefficient birigidified divisor kernels on \(A_{i,0}\times B_i\) with class \(\alpha_{i,0}\otimes\beta_i\).

Put
\[
 Z_B=K_{B*}z_0\in\operatorname{CH}^2(B)\otimes\mathcal O_E,
 \qquad C_B=Z_B/k_0.
\]
For every fixed \(a\in\mathcal O_E\), the rational Chow class
\[
 \Gamma_B(a)=\operatorname{Tr}_{E/\mathbf Q}(a C_B)
\]
has an integral multiple with the same denominator for all output lattices:
\[
 N_0\Gamma_B(a)\in\operatorname{im}
 \bigl(\operatorname{CH}^2(B)\longrightarrow
                 \operatorname{CH}^2(B)\otimes\mathbf Q\bigr),
 \qquad
 N_0=|N_{E/\mathbf Q}(k_0)|.
 \tag{T20.7}
\]
A fixed finite set of fractional coefficient weights only adds one fixed clearing integer. This proves a genuine uniform Chow denominator for these **factorwise integral eigenvector tensors**. It does not by itself make their rational Galois-orbit lattice saturated in integral cohomology or give a degree bound for the signed cycles.

##### D. Exact denominator of the displayed dual-pullback representative

Choose a finite representative
\[
 C_0=\sum_{\ell=1}^u c_\ell[Z_\ell],\qquad c_\ell\in E,
 \tag{T20.8}
\]
with distinct integral subvarieties \(Z_\ell\subset B_0\). In the dual situation (B), a representative of \(\Gamma_B(a)\) has coefficient
\[
 \operatorname{Tr}_{E/\mathbf Q}(a c_\ell/\Lambda)
 \tag{T20.9}
\]
on every irreducible component of \(q^{-1}(Z_\ell)\). Therefore the exact common denominator of this displayed rational cycle is the least common multiple of the denominators of (T20.9).

Let \(\mathfrak C=\sum_\ell\mathcal O_Ec_\ell\) and let \(\mathfrak D\) be the different of \(E/\mathbf Q\). The least positive integer clearing this representative simultaneously for every \(a\in\mathcal O_E\) is the positive generator of
\[
 (\Lambda\mathfrak D^{-1}\mathfrak C^{-1})\cap\mathbf Z.
 \tag{T20.10}
\]
Its exponent at a rational prime \(p\) is
\[
 \max\left(0,\max_{\mathfrak p\mid p}
 \left\lceil\frac{v_{\mathfrak p}(\Lambda)
                      -v_{\mathfrak p}(\mathfrak D)
                      -v_{\mathfrak p}(\mathfrak C)}{e_{\mathfrak p}}\right\rceil\right).
 \tag{T20.11}
\]
These are exact representative denominators and hence upper bounds for the intrinsic Chow denominator. Rational equivalence or divisibility in the Chow group may reduce the latter; no converse lower bound is asserted.

#### Proof

##### Birigidification makes the entire divisor class faithful

For complex abelian varieties \(U,V\), write \(\operatorname{Pic}^{\mathrm b}(U\times V)\) for divisor-correspondence classes trivialized along the two zero axes. Its first Chern class is injective. Indeed, a class in its kernel lies in \(\operatorname{Pic}^0(U\times V)\), and
\[
 \operatorname{Pic}^0(U\times V)
 =\operatorname{pr}_U^*\operatorname{Pic}^0(U)
  \oplus\operatorname{pr}_V^*\operatorname{Pic}^0(V).
\]
Restriction to the two axes recovers these two summands, so birigidification makes both trivial. Equivalently, the divisor-correspondence group is \(\operatorname{Hom}(U,V^\vee)\), and the induced map on first cohomology detects a homomorphism. This is the correspondence/biextension identification of SGA7 I, Expose VII, Examples 2.9.5--2.9.6. Tensoring the injective first Chern class map with the characteristic-zero field \(E\) preserves injectivity.

Pullback by a homomorphism in either argument preserves birigidification. The first Chern class of the left side of (T20.2) is, in the full \(E\)-coefficient Betti space,
\[
 h_i^*\alpha_i\otimes g_i^*\beta_i
   =\lambda_i\mu_i(\alpha_{i,0}\otimes\beta_{i,0}).
\]
This is not merely an equality after evaluating one complex embedding. Applying the just-proved injectivity gives (T20.2) in the entire birigidified Picard group with \(E\) coefficients, and hence in \(\operatorname{CH}^1\otimes E\).

##### Projection and flat base change

Let \(p_A,p_B\) denote the two projections from \(A\times B\). By definition,
\[
 K_*h_*z_0=(p_B)_*\bigl(p_A^*h_*z_0\cdot K\bigr).
\]
Flat base change along \(g\) and then along the product square for \(h\), followed by the projection formula, gives
\[
 \begin{aligned}
 g^*(K_*h_*z_0)
 &= (K|_{A\times B_0})_*h_*z_0\\
 &= ((h\times g)^*K)_*z_0\\
 &=\Lambda M\,K_{0*}z_0.
 \end{aligned}
 \tag{T20.12}
\]
Here the first kernel is the pullback by \(1\times g\), not a literal restriction to a subvariety. All isogenies in characteristic zero are finite etale, hence flat, so these are ordinary Chow pullbacks and proper pushforwards. The product of the four identities (T20.2) proves the last equality. The period scales by \(\Lambda\), proving the first equation of (T20.3). Applying \(g_*\) and using \(g_*g^*=(\deg g)\operatorname{id}\) proves the second. This also proves (T20.4).

The fixed rational Chow denominator in (T20.4) is concrete. Choose a finite cycle representative of \(\operatorname{Tr}(a C_0)\) and clear its finitely many rational coefficients once. The same representative on the same output works for every input isogeny. This is stronger than a bound on the selected period and is not contradicted by the nonsaturation of an unscaled subgroup of Chow classes.

##### Duality and the reversed map

For a homomorphism \(h_i:A_{i,0}\to A_i\), the normalized Poincare bundles satisfy
\[
 (h_i\times1)^*\mathcal P_{A_i}
   \simeq (1\times h_i^\vee)^*\mathcal P_{A_{i,0}}.
 \tag{T20.13}
\]
This is the defining universal property of the dual homomorphism. The selected \(E\)-eigencomponents agree because \(h_i\) is \(E\)-linear. In Betti cohomology, the selected equality reads
\[
 \lambda_i\alpha_{i,0}\otimes\beta_i
   =\alpha_{i,0}\otimes(h_i^\vee)^*\beta_{i,0},
\]
so it gives the first identity of (T20.5). Birigidified Chern-class injectivity also gives (T20.13) for the selected divisor components themselves. These components are legitimate \(E\)-coefficient divisor classes even when their projection from the integral Poincare class has denominators. This part does not assert their integrality.

Taking the fourfold product of (T20.13), pulling it against \(z_0\), and applying flat base change on the output gives the second identity of (T20.5). Divide by \(k_h=\Lambda k_0\) to obtain the first identity of (T20.6). Its pushforward follows from \(q_*q^*=(\deg q)\operatorname{id}\). In particular the scalar in (T20.6) is \(\Lambda\), not an assumed field norm or an arbitrarily chosen complex metric period.

##### Integral factorwise tensors require only one fixed period denominator

For part (C), each pure mixed class \(\alpha_{i,0}\otimes\beta_i\) belongs to integral cohomology tensored with \(\mathcal O_E\), and all its scalar conjugates are of type \((1,1)\). The integral descent argument of T6.7 and T6.18 puts it in the saturated mixed Neron--Severi lattice tensored with \(\mathcal O_E\). Passing to the birigidified representative removes axis restrictions and introduces no coefficient denominator. Products and proper pushforward preserve integral \(\mathcal O_E\)-coefficient cycles, proving that \(Z_B\) has the stated coefficients.

For a nonzero algebraic integer \(k_0\), the element \(N_0/k_0\) is an algebraic integer: up to the sign of its rational norm it is the product of the other scalar conjugates. Consequently
\[
 N_0\Gamma_B(a)
   =\operatorname{Tr}_{E/\mathbf Q}
       \bigl(a(N_0/k_0)Z_B\bigr)
\]
is an integral cycle class, proving (T20.7). This argument is uniform over the target lattices and does not use a bound for an isogeny degree. It proves uniform division for the explicitly stated factorwise integral tensors; primitivity in a larger rational orbit lattice is a separate question.

##### The explicit representative and the trace dual

A finite etale pullback of an integral subvariety is generically reduced; each irreducible component has multiplicity one in the flat pullback cycle. Every component maps onto the original subvariety. Thus the inverse images of distinct \(Z_\ell\) have no common irreducible components. Apply (T20.6) to the representative (T20.8) and then trace the coefficients. This gives exactly (T20.9), with no cancellation among supports of different \(Z_\ell\).

An integer \(D>0\) clears these coefficients for all \(a\in\mathcal O_E\) if and only if
\[
 D c_\ell/\Lambda\in\mathfrak D^{-1}
 \quad\hbox{for every }\ell.
\]
Equivalently, \(D\mathfrak C\subseteq\Lambda\mathfrak D^{-1}\). Since \(\mathfrak C\) is an invertible fractional maximal-order ideal, this is precisely \(D\in\Lambda\mathfrak D^{-1}\mathfrak C^{-1}\). Taking its intersection with the integers proves (T20.10); comparing valuations gives (T20.11). The denominator of a particular representative always clears its Chow class. The proof supplies no reason that a rationally equivalent representative cannot have a smaller denominator. This completes the proof. QED.

#### Comparison with the fixed-K Weil determinant plane

In B23 the coefficient space is a rank-one module over an imaginary quadratic field \(K\), hence a two-dimensional rational Weil plane. For an \(E\)-linear isogeny with scalar \(\alpha\), the pullback scalar on that determinant line is
\[
 s=N_{E/K}(\alpha).
\]
If \(\nu\) is the homology covolume ratio, its degree is \(\delta=\nu^{-1}s\bar s\). A normalization compatible with the chosen target determinant generator therefore has the same general form
\[
 C_A=\frac{s}{\delta}\,h_*C_0
     =\frac{\nu}{\bar s}\,h_*C_0.
 \tag{T20.14}
\]
This is the formal comparison of scalar conventions; it does not identify B23's determinant plane with the four-factor switch orbit. B23's common integral pushforward content \(\bar{\mathfrak j}\) records the image before saturation. Multiplication by \(s/\delta\) can leave that integral image, and a claim that the result is integral in Chow would require an additional divisibility argument. Conversely, the image index alone does not prove that the normalized class has an unbounded intrinsic denominator.

For the four separate CM factors, the scalar \(M\) in (T20.3) is a product of four selected embedding eigenvalues; it is generally not \(N_{E/K}(\alpha)\). Its full rational Galois orbit has dimension \([E:\mathbf Q]\), rather than two. Any comparison with a generic \(K\)-Weil target must retain the actual correspondence and its integral lattice map.

The positive conclusion is precise: all varying input isogenies and their period normalization cancel in Chow, and direct kernels with fixed integral input vectors give a uniform denominator for every factorwise integral output tensor. The unresolved moving-output primitive question is whether the integral orbit classes needed for the intended Weil target can be represented by these tensors with uniformly controlled saturation, or whether their normalized isogeny pullbacks have additional Chow divisibility. Neither a metric Rallis norm nor scalar trace contraction settles that question.

#### Primary sources and exact locators

- Grothendieck, SGA7 I, Expose VII, Example 2.9.5, printed p.175 (PDF p.180; VII43), and Remark 2.9.6, printed p.176 (PDF p.181; VII44), identify birigidified line bundles, biextensions and divisor correspondences \(\operatorname{Hom}(U,V^\vee)\). Original scan: <https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf>. This agent independently read both original page images in this phase.
- Milne, *Abelian Varieties*, v2.00, Chapter I, Poincare universal property and Remark 8.7, printed p.37, and the opening paragraph of Section 9, printed p.41. The latter explicitly states (T20.13) and defines the dual homomorphism. <https://www.jmilne.org/math/CourseNotes/AV.pdf>.
- Stacks Project, Lemma 42.15.1 (tag 02RG) and Lemma 42.15.2 (tag 02RH), in Section 42.15 (tag 02RF), state flat base change and finite locally free push-pull. <https://stacks.math.columbia.edu/tag/02RF>. Exact statements and complete short proofs read.
- Stacks Project, Lemma 43.22.1 (tag 0B10), supplies the flat proper projection formula. <https://stacks.math.columbia.edu/tag/0B10>. Statement and full displayed proof read; on Chow groups the usual moving/intersection formalism gives the formula used above.
- Conrad, *The Different Ideal*, Definition 3.2 p.4, Theorems 3.9--3.10 p.8 and Definition 4.1 p.9, supplies the trace-dual convention in (T20.10). <https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf>. The denominator calculation itself is proved here.

#### Check status

The entire saved proof was read by the author, root and bounds; all reviews passed before promotion. Source checks are recorded separately. No local compilation is claimed.


## 16. The full integral orbit lattice and uniform division with one maximal-order factor

### DEG-L.T6.21 — Exact four-factor saturation and uniform division with an anchor

Let \(E\) be a Galois CM field, \(\mathcal O=\mathcal O_E\), \(d=[E:\mathbf Q]=2g\), and let \(c\) denote complex conjugation. Let
\[
 B_i=\mathbf C^g/\Phi_i(\Lambda_i),\qquad i=1,2,3,4,
\]
where each \(\Lambda_i\subset E\) is a full \(\mathbf Z\)-lattice. The four CM types satisfy the switch relation, so the diagonal orbit specified below consists of Hodge classes. The first homology has rank one over \(E\); simplicity and primitivity of the types are unnecessary.

Inside the degree-four Kunneth summand \(\bigotimes_i H^1(B_i,\mathbf Q)\), identify the rational diagonal orbit \(W\) with \(E\) by the injective map
\[
 \Theta(\kappa)(x_1,x_2,x_3,x_4)
   =\operatorname{Tr}_{E/\mathbf Q}
       (\kappa x_1x_2\bar x_3\bar x_4).
 \tag{T21.1}
\]
Exchanging the barred and unbarred labels gives the equivalent opposite switch convention. Put
\[
 \begin{aligned}
 M&=\left\langle x_1x_2\bar x_3\bar x_4:
                         x_i\in\Lambda_i\right\rangle_{\mathbf Z},\\
 M^+&=\mathcal O M
   =\Lambda_1^+\Lambda_2^+\overline{\Lambda_3^+}\,
                                  \overline{\Lambda_4^+},\\
 L&=(M^+)^{-1},\qquad
 M^\vee=\{\kappa\in E:\operatorname{Tr}(\kappa M)\subseteq\mathbf Z\}.
 \end{aligned}
 \tag{T21.2}
\]
Here \(M\) is a full additive lattice, \(M^+\) is an invertible fractional maximal-order ideal, and \(L\) is its ideal inverse.

##### A. The two integral lattices and their exact index

The actual integral intersection lattice of the rational orbit is
\[
 W\cap H^4(B_1\times\cdots\times B_4,\mathbf Z)
     =\Theta(M^\vee).
 \tag{T21.3}
\]
The additive span of coefficient traces of products of the four **individually integral \(\mathcal O\)-coefficient eigenvectors** is exactly
\[
 \Theta(L).
 \tag{T21.4}
\]
Consequently
\[
 [M^\vee:L]
   =|\operatorname{Disc}(E)|\,[M^+:M].
 \tag{T21.5}
\]
This is an equality of actual integral intersection lattices, including at ramified primes; it does not assume integral eigenprojectors on the varying factors.

##### B. Exact saturation exponent and a uniform anchor case

Let \(n(M)\) be the exponent of the finite group \(M^\vee/L\), equivalently the least positive integer with \(n(M)M^\vee\subseteq L\). If \(\mathfrak D\) is the different of \(E/\mathbf Q\), then
\[
 n(M)\mathbf Z
 =\{n\in\mathbf Z:n\mathfrak D^{-1}M^+\subseteq M\}.
 \tag{T21.6}
\]
Let \(e(M)\) be the exponent of \(M^+/M\), and let \(d_E>0\) generate \(\mathfrak D\cap\mathbf Z\). Then
\[
 e(M)\mid n(M)\mid d_E e(M).
 \tag{T21.7}
\]
In particular, at every prime unramified in \(E\), the saturation exponent equals the exponent of the corresponding part of the product-lattice hull quotient.

If **at least one** \(\Lambda_i\) is stable under \(\mathcal O\), then
\[
 M=M^+,
 \qquad [M^\vee:L]=|\operatorname{Disc}(E)|,
 \qquad n(M)=d_E.
 \tag{T21.8}
\]
Thus fixing one maximal-order factor eliminates every target-dependent saturation cost, even if the other three lattices have arbitrarily large core indices.

##### C. Uniform integral division of primitive orbit classes with one anchor

Fix the input surface maps and integral input eigenvectors of T6.20(C), with nonzero period \(k_0\in\mathcal O\), and put \(N_0=|N_{E/\mathbf Q}(k_0)|\). Every integral class \(w\) in the orbit (T21.3), primitive or otherwise, has
\[
 N_0 n(M)\,w
\]
as the cohomology class of an integral algebraic cycle constructed from the fixed surface and the divisor kernels of T6.20(C). If one output factor has maximal-order action, the same integer
\[
 N_0d_E
 \tag{T21.9}
\]
works for every primitive integral orbit class and every choice of the other three output lattices. In particular it is at most \(N_0|\operatorname{Disc}(E)|\). This supplies a genuine uniform division bound for this stated family of integral Hodge classes; it does not bound the degrees or the sizes of integer coefficients in a chosen cycle representative.

##### D. All four mixed principal lattices can have growing saturation

Take the actual principal-polarization families of T6.19, at a completely split prime \(p\) outside the fixed bad set. In one conjugate pair use, for all four output homology lattices,
\[
 L_r=\mathbf Z_p(1,0)+\mathbf Z_p(p^{-r},1),
\]
with complex conjugation swapping the two coordinates. Apply the bars in (T21.2) to the third and fourth factors. The resulting product lattice and hull in this pair are
\[
 M_{r,p}
   =p^{-r}\mathbf Z_p^2+
           \mathbf Z_p p^{-2r}(1,1),
 \qquad
 M_{r,p}^+=p^{-2r}\mathbf Z_p^2.
 \tag{T21.10}
\]
Their quotient is cyclic of order \(p^r\). Equivalently,
\[
 \begin{aligned}
 M_{r,p}^\vee
  &=\{(x,y)\in p^r\mathbf Z_p^2:x+y\in p^{2r}\mathbf Z_p\},\\
 L_{r,p}^{\mathrm{fact}}&=p^{2r}\mathbf Z_p^2,\\
 M_{r,p}^\vee/L_{r,p}^{\mathrm{fact}}&\simeq\mathbf Z/p^r\mathbf Z.
 \end{aligned}
 \tag{T21.11}
\]
The class of \(p^r(1,-1)\) generates the last quotient. Modifying all \(g\) conjugate pairs gives a direct sum of \(g\) such quotients. Thus
\[
 v_p([M_r^+:M_r])=gr,
 \qquad v_p(n(M_r))=r.
 \tag{T21.12}
\]
All other prime contributions are fixed. There exist globally primitive integral Hodge classes whose image in this saturation quotient has order \(p^r\). Their expression in the factorwise integral trace lattice requires that \(p\)-denominator. This is a sharp statement about the factorized construction and its saturation, not a lower bound for the intrinsic algebraic-cycle denominator over all possible constructions.

#### Proof

##### The orbit as an integral multilinear form

Each \(H^1(B_i,\mathbf Q)\) is \(\operatorname{Hom}_{\mathbf Q}(E,\mathbf Q)\). Its integral lattice is \(\operatorname{Hom}_{\mathbf Z}(\Lambda_i,\mathbf Z)\). Since the four lattices are free of finite rank, their tensor product identifies with the integral multilinear forms on \(\Lambda_1\times\cdots\times\Lambda_4\). Integral Kunneth makes this tensor product a direct summand of \(H^4(\prod_i B_i,\mathbf Z)\), with no factorial or torsion correction.

Formula (T21.1) is injective: if it vanishes identically, set the last three rational arguments equal to 1 and use nondegeneracy of the field trace pairing on the first argument. After extending coefficients to \(E\), it is the sum of the Galois conjugates of the tensor with embedding labels \((1,1,c,c)\). These conjugates lie in distinct eigenspaces, so its image is exactly the specified rational diagonal orbit. The switch relation says that every one of these conjugates has type \((2,2)\).

Integrality of the multilinear form is precisely the condition \(\operatorname{Tr}(\kappa M)\subseteq\mathbf Z\), proving (T21.3). The lattice \(M\) is finitely generated by products of four chosen integral bases. It has full rational rank: fixing nonzero elements in three factors puts a nonzero scalar multiple of the full first lattice inside it. Expanding the maximal-order hulls shows directly that \(\mathcal O M\) is the displayed product ideal in (T21.2).

##### Individually integral eigenvectors and the index

By T6.18, the actual integral coefficient line for the identity embedding in the first factor is \((\Lambda_1^+)^{-1}e_1\); the second is analogous. The conjugate lines in the last two factors have coefficient ideals \(\overline{\Lambda_3^+}^{-1}\) and \(\overline{\Lambda_4^+}^{-1}\). The additive span of products of their coefficients is exactly the product of these four ideals, namely \(L\). Coefficientwise field trace of their tensor products is \(\Theta\) applied to those products. This proves (T21.4), as equality of the actual additive spans. No division by \([E:\mathbf Q]\) is used in this trace convention.

Trace duality reverses indices of full additive lattices, giving
\[
 [M^\vee:(M^+)^\vee]=[M^+:M].
\]
For the fractional maximal-order ideal \(M^+\), trace duality gives
\[
 (M^+)^\vee=\mathfrak D^{-1}(M^+)^{-1}
                    =\mathfrak D^{-1}L.
\]
Therefore
\[
 [(M^+)^\vee:L]=N_{E/\mathbf Q}(\mathfrak D)
                     =|\operatorname{Disc}(E)|.
\]
Multiplying the two indices proves (T21.5). This argument incorporates the different exactly, so it remains valid at ramified primes.

##### The saturation exponent and an integral maximal-order factor

For a positive integer \(n\), dualizing the inclusion \(nM^\vee\subseteq L\) gives
\[
 L^\vee\subseteq n^{-1}M.
\]
The fractional ideal duality formula says \(L^\vee=\mathfrak D^{-1}M^+\). This proves (T21.6). Since \(\mathfrak D^{-1}\supseteq\mathcal O\), any such \(n\) also satisfies \(nM^+\subseteq M\); hence \(e(M)\mid n(M)\). Conversely,
\[
 d_E e(M)\mathfrak D^{-1}M^+
  \subseteq e(M)M^+\subseteq M,
\]
so \(n(M)\mid d_E e(M)\). This proves (T21.7).

If, for example, \(\Lambda_1\) is \(\mathcal O\)-stable, multiplication of a generating product in \(M\) by any \(a\in\mathcal O\) can be absorbed into its first factor. Thus \(M\) itself is \(\mathcal O\)-stable and equals \(M^+\). The same argument works in a barred factor because conjugation preserves \(\mathcal O\). Since this ideal is invertible, condition (T21.6) then reduces to
\[
 n\mathfrak D^{-1}\subseteq\mathcal O,
 \quad\hbox{equivalently }n\in\mathfrak D.
\]
Its least positive integer is exactly \(d_E\), proving (T21.8). The bound \(d_E\le|\operatorname{Disc}(E)|\), and indeed divisibility by it, follows because the finite group \(\mathcal O/\mathfrak D\) has order \(|\operatorname{Disc}(E)|\), so its order kills it.

For part (C), write \(w=\Theta(\kappa)\) with \(\kappa\in M^\vee\). By definition, \(n(M)\kappa\in L\). Formula (T21.4) writes \(n(M)w\) as a finite integral sum of coefficient traces of factorwise integral eigenvector products. T6.20(C) supplies, for each term, a rational algebraic cycle whose class is that term and whose denominator divides the same \(N_0\). Summing these cycles proves that \(N_0n(M)w\) is represented by an integral algebraic cycle. In the anchor case \(n(M)=d_E\), proving (T21.9). No bounds on the finite sum's coefficients or degrees are inferred.

##### The explicit principal family and its saturation quotient

Choose the split prime outside the finitely many primes at which any base lattice differs from \(\mathcal O\), or any fixed Riemann form is not unimodular on that lattice. Use the common idempotent coordinates of \(E\otimes\mathbf Q_p\); the trace is the sum of these coordinates and conjugation swaps each conjugate pair. On a given pair the four Riemann forms have matrices \(u_i\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), with possibly different units \(u_i\in\mathbf Z_p^\times\). The determinant-one shear defining \(L_r\) preserves each such form, so the same displayed \(L_r\) is self-dual for all four pairings. Thus no separate unit rescaling of the four coordinate systems is needed. The local-to-global construction of T6.19 realizes exactly these four modifications by actual principally polarized CM varieties.

In one pair let \(e=(1,0)\), \(f=(0,1)\), and \(q=p^{-r}\). The first two factors have generators \(e\) and \((q,1)\), and the conjugated last two have generators \(f\) and \((1,q)\). Multiply componentwise. A product containing both an \(e\) and an \(f\) is zero. The remaining products generate \(qe\), \(qf\), and \(q^2(e+f)\); they also generate \(e,f\), which already belong to \(q\mathbf Z_p^2\). This proves (T21.10).

After multiplication by \(p^{2r}\), the hull becomes \(\mathbf Z_p^2\) and the product lattice becomes
\[
 p^r\mathbf Z_p^2+\mathbf Z_p(1,1).
\]
The quotient is identified with \(\mathbf Z/p^r\mathbf Z\) by subtracting the two coordinates. This proves the hull quotient assertion. Taking its trace dual before scaling gives the first formula of (T21.11): pairing with \(p^{-r}e,p^{-r}f\) forces \(x,y\in p^r\mathbf Z_p\), and pairing with \(p^{-2r}(e+f)\) forces \(x+y\in p^{2r}\mathbf Z_p\). The inverse hull ideal is \(p^{2r}\mathbf Z_p^2\). Its quotient in the trace dual is generated by \(p^r(1,-1)\) and has order \(p^r\).

Different coordinate pairs contribute independent direct summands. The base lattice at \(p\) is the full product maximal-order lattice, so vectors supported on a single pair are available in every factor. Thus the local product module is the direct sum of the computed modules. Its hull index is \(p^{gr}\) and its quotient exponent is \(p^r\), proving (T21.12). Outside \(p\), all input lattices in this product calculation remain fixed.

Finally, the global finite group \(M^\vee/L\) has this prescribed \(p\)-primary part. Lift an element whose \(p\)-primary order is \(p^r\) to the integral global orbit lattice. The lift is not divisible by \(p\): otherwise its image would be \(p\) times an element in a group whose \(p\)-primary exponent is only \(p^r\), so its \(p\)-primary order would be at most \(p^{r-1}\). Divide the lift by its full integral content. That content is prime to \(p\), so the order \(p^r\) in the saturation quotient is preserved. The resulting class is primitive in the orbit intersection lattice, and hence in ambient integral cohomology because intersection with a rational subspace is saturated. This gives a globally primitive integral Hodge class with the claimed necessary presentation denominator. It does not prove that every algebraic cycle representing this class has that denominator. QED.

#### Relation to the main normalization question

T6.20 removes every variable input-isogeny period denominator and gives a fixed denominator on the factorized integral trace lattice. T6.21 identifies the remaining integral-lattice comparison exactly. It closes the primitive-division gate when one output factor has maximal-order action, and it isolates a computable product-lattice exponent when none does.

This is a four-factor full-CM orbit. It is not B23's middle \(K\)-Weil determinant plane, whose integral pushforward content is a relative norm ideal. The exact comparison with such a target still requires its actual correspondence. Nor does a growing factorized-lattice saturation exponent prove an intrinsic integral Hodge obstruction: an additional Chow divisibility relation or a different cycle construction can enlarge the available integral cycle lattice.

#### Primary sources and checks

The new identities are proved above from integral Kunneth, the field trace pairing and lattice duality. The trace-dual conventions and fractional-ideal duality are Keith Conrad, *The Different Ideal*, Definition 3.2 p.4, Theorem 3.9 p.8, Definition 4.1 p.9; the norm of the different equals the absolute discriminant by Theorem 4.8 p.11, whose full trace-Gram-determinant proof was independently read. Author URL: <https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf>.

Actual principal lattice realization is the complete local-to-global construction in candidate T6.19; no additional moduli existence assertion is imported. The uniform cycle denominator uses precisely part (C) of candidate T6.20. Both predecessor candidates retain their stated coefficient and Chow-divisibility scope.

#### Check status

The entire revised saved proof was read by the author, root and bounds; all reviews passed before promotion. The common-idempotent and global primitivity refinements were included in the final reads. No computation in a proof assistant is claimed.


## 17. Mixed kernels and every proper block of auxiliary maximal-order factors

### DEG-L.T6.22 — Mixed divisor kernels and proper-block correspondences retain the saturation cost

Let \(E\) be the Galois CM field of T6.21, of degree \(d=2g\), and let \(c\) be complex conjugation. Retain an **indecomposable** four-factor switch: the selected eigenlines have CM sign functions \(s_1,s_2,s_3,s_4\) with
\[
 s_1+s_2+s_3+s_4=0,
 \qquad
 \sum_{i\in I}s_i\ne0
 \quad(\varnothing\ne I\subsetneq\{1,2,3,4\}).
 \tag{T22.1}
\]
These are equalities and inequalities of functions on the scalar Galois group, not merely at one complex place. The actual four types in T6.16 satisfy this hypothesis.

Choose a completely split prime \(p\) as in T6.21. On each conjugate pair of coordinates in \(E\otimes\mathbf Q_p\), all four output homology lattices are
\[
 L_r=\mathbf Z_p e+\mathbf Z_p(p^{-r}e+f),
 \qquad r\ge1,
 \tag{T22.2}
\]
in the common idempotent coordinates, and conjugation interchanges \(e,f\). These are the actual principally polarized CM varieties constructed in T6.19 and T6.21. Put \(B_r=\prod_{i=1}^4B_{i,r}\). Let \(W_r\) be the rational diagonal orbit with labels \((1,1,c,c)\), identified with \(E\) by T6.21's trace map \(\Theta\). Write \(\pi_W\) for the rational projection which first selects the degree-\((1,1,1,1)\) Kunneth summand and then selects this diagonal orbit. This is the specified eigencomponent projection; no integrality or bounded denominator of a correspondence representing \(\pi_W\) is assumed.

At \(p\), the factorwise trace lattice is
\[
 L^{\mathrm{fact}}_{r,p}=p^{2r}(\mathcal O_E\otimes\mathbf Z_p),
 \tag{T22.3}
\]
and the quotient of the integral orbit lattice by it is
\((\mathbf Z/p^r\mathbf Z)^g\), as proved in T6.21.

##### A. Arbitrary integral mixed divisor kernels still have the same local content

Let \(U\) be a fixed product of CM abelian varieties whose rational first homologies have rank one over \(E\). Choose \(p\) also outside the fixed bad set for these source lattices. Thus
\[
 H^1(U,\mathbf Z_p)
\]
has a basis of pure CM Hodge eigenlines for the separate source \(E\)-actions. This basis assertion is part of the hypothesis; an unspecified higher-rank \(E\)-module with mixed Hodge multiplicities would not suffice.

Let \(z\in\operatorname{CH}_2(U)\) be any integral algebraic cycle. The cycle and its degree need not be fixed. Let \(K\in\operatorname{CH}^4(U\times B_r)\) belong to the integral subring generated by divisor classes. Thus \(K\) is a finite integral sum of products of four integral divisor classes. The divisors may have arbitrary mixed components, need not be \(E\)-linear, and may connect any source factor to any output factor. Source-source and output-output components are also permitted.

Then
\[
 \pi_W\operatorname{cl}(K_*z)
       \in\Theta(L^{\mathrm{fact}}_{r,p})
       \subset W_r\otimes\mathbf Q_p.
 \tag{T22.4}
\]
In particular, allowing impure eigencomponents, imprimitive CM types, or cancellations between off-orbit terms does not enlarge this local image.

Let \(w_r\) be one of the primitive integral orbit classes of T6.21 whose saturation-quotient image has order \(p^r\). If a rational linear combination of the classes in (T22.4), with common scalar denominator \(D\), equals \(w_r\), then
\[
 v_p(D)\ge r.
 \tag{T22.5}
\]
More generally, if it equals \(Nw_r\) for an integer \(N>0\), then
\[
 v_p(D)+v_p(N)\ge r.
 \tag{T22.6}
\]
The same conclusion holds for any finite sum of such constructions, even with unbounded source-cycle degrees. Multiplying or dividing by fixed rational normalization constants changes the inequalities only by their fixed \(p\)-valuations.

The assertion also holds for \(z\in\operatorname{CH}_m(U)\) of any dimension and an integral divisor polynomial \(K\in\operatorname{CH}^{m+2}(U\times B_r)\), so that its output still has codimension two. Source-only divisor factors merely enter the same integral contraction. If \(m<2\), the selected output is zero.

##### B. No proper block of maximal-order factors can be returned with bounded denominator

Let \(I\subset\{1,2,3,4\}\) be nonempty and proper, and put \(k=|I|\). For \(i\in I\), let \(C_i\) be a CM abelian variety with rank-one rational \(E\)-homology and integral maximal-order action at \(p\). These varieties may vary. Put
\[
 H_I=\bigotimes_{i\in I}H^1(C_i,\mathbf Q),\qquad
 V_I=\bigotimes_{i\in I}H^1(B_{i,r},\mathbf Q),\qquad
 V_{I^c}=\bigotimes_{j\notin I}H^1(B_{j,r},\mathbf Q).
 \tag{T22.7}
\]
Let \(u\in H_I\otimes V_{I^c}\) be a rational Hodge class of type \((2,2)\) that is integral at \(p\). No assumption that \(u\) comes from the divisor-kernel construction is needed.

Suppose the rational Hodge homomorphism \(F:H_I\to V_I\) satisfies
\[
 F(H_{I,\mathbf Z_p})\subseteq p^{-a}V_{I,\mathbf Z_p},
 \qquad a\ge0,
 \tag{T22.8}
\]
where the lattices are the tensor products of the corresponding integral first cohomologies. Then
\[
 \pi_W(F\otimes1)u
       \in p^{-a}\Theta(L^{\mathrm{fact}}_{r,p}).
 \tag{T22.9}
\]
Consequently this procedure cannot produce \(w_r\) when \(r>a\). If \(u\) itself has an additional denominator of valuation \(b\), the necessary inequality is \(r\le a+b\).

This permits an arbitrary **joint** rational Hodge map on a block of one, two or three factors. In particular it applies to a degree-preserving algebraic correspondence on that block whose coefficient denominator is bounded at \(p\): take its degree-\(k\) action and the indicated Kunneth component. Integral Kunneth projections preserve the cohomology lattice, even though no integral Chow projector is being asserted. The first-factor isogeny pullbacks and pushforwards of the original one-factor case are included. Thus the positive uniform division result with maximal-order factors does not automatically transport back to all four mixed factors by bounded-denominator correspondences acting on a proper block.

#### Proof

##### 1. The local dual lattice and pure Hodge rows

Write \(e^\vee,f^\vee\) for the coordinate functionals on a single conjugate pair. Direct evaluation on the two generators in (T22.2) gives
\[
 L_r^*=
 \{a e^\vee+b f^\vee:
       a\in\mathbf Z_p,\quad p^{-r}a+b\in\mathbf Z_p\}.
 \tag{T22.10}
\]
The intersections with the two pure coordinate lines are therefore
\[
 L_r^*\cap\mathbf Q_p e^\vee=p^r\mathbf Z_p e^\vee,
 \qquad
 L_r^*\cap\mathbf Q_p f^\vee=\mathbf Z_p f^\vee.
 \tag{T22.11}
\]
Their direct sum is the dual of the maximal-order hull. The larger lattice (T22.10) allows cancellation between the two conjugate coordinates, whereas (T22.11) records precisely the individual integrality conditions.

Let \(D\) be an integral divisor on \(U\times B_{i,r}\), and take its mixed \(H^1(U)\otimes H^1(B_{i,r})\) component. Integral Kunneth makes this an integral tensor. Expand it in the pure integral source eigenbasis. Each source row is then an integral functional on the target lattice.

For a fixed source eigenline, that row cannot have nonzero entries in both of a target's conjugate eigenlines. Indeed, after extending scalars to \(E\) and then to \(\mathbf C\), all these tensor components are independent eigenspaces. The source eigenline has one pure type, either \((1,0)\) or \((0,1)\), while the two conjugate target lines have opposite types. At most one of their tensor products with that source line has type \((1,1)\). Since a divisor class is of type \((1,1)\), the other component vanishes. The same assertion is preserved under scalar conjugation. The coefficients are algebraic, so a vanished complex component is also zero in the split \(p\)-adic eigenbasis.

Thus, on each target conjugate pair, the row is supported on at most one coordinate. Substituting \(b=0\) or \(a=0\) in (T22.10) proves that every row lies in the direct sum (T22.11), pair by pair. In particular every individual target eigencomponent of the mixed divisor is integral separately, at \(p\).

This argument does not claim that a fixed source projector selects exactly one target eigenline. That claim could fail for imprimitive types. A row can contain several target eigenlines; the point is that it contains no conjugate pair, and the particular target lattice (T22.2) couples only conjugate pairs.

##### 2. Four source-output divisors

First suppose that each of four divisor factors has one source \(H^1\) leg and one output \(H^1\) leg, with the four output legs in the four distinct factors. By the preceding argument, every target eigencomponent of each factor lies in the appropriate pure integral line (T22.11).

Expand their product and contract the four source legs against the integral cycle class of \(z\). All contraction coefficients are \(p\)-adic integers: the source eigenbasis is integral, cup product is integral, and evaluation on an integral cycle is integral. Reordering the exterior factors only introduces signs. Thus each surviving output eigenmonomial has its coefficient in the product of its four individual pure-line coefficient lattices.

For a monomial in the selected diagonal orbit, a given conjugate pair has two \(e^\vee\) entries and two \(f^\vee\) entries, because its labels are \((1,1,c,c)\). Formula (T22.11) therefore forces its coefficient into
\[
 (p^r)^2\mathbf Z_p=p^{2r}\mathbf Z_p.
\]
This holds in all \(g\) pairs and for the conjugate monomials. The trace identification \(\Theta\) has no division by \(d\); its coefficients in these monomials are exactly the split coordinates of the field coefficient. Hence the selected projection belongs to \(\Theta(L^{\mathrm{fact}}_{r,p})\).

The same conclusion holds if a mixed divisor initially couples one output factor to several source factors: expand the finite sum of source rows and apply the preceding argument term by term. No \(E\)-linearity of the divisor correspondence was used.

##### 3. General divisor polynomials and off-orbit cancellation

The degree-four output Kunneth block under consideration has degree one in each \(B_{i,r}\). A divisor component with two legs in a single output factor cannot contribute to this block. A component with one leg in each of two distinct output factors can contribute only if its two selected eigenlabels form a rational \((1,1)\) subrelation.

More explicitly, a rational divisor component in the two selected lines is nonzero only if each scalar conjugate of their product has type \((1,1)\). In sign-function notation, this is exactly \(s_i+s_j=0\) as functions. Hypothesis (T22.1) excludes it. Every output-output divisor component therefore has zero contribution to the selected orbit.

There are four divisors, giving eight cohomological legs in total. To contribute after contraction with the surface cycle, four legs must lie on the source and four on the output. If there are \(a\) source-source components, \(b\) source-output components and \(c\) output-output components, then
\[
 a+b+c=4,\qquad 2a+b=4,\qquad b+2c=4,
\]
so \(a=c\). Once output-output components have been excluded, source-source components are excluded as well. The only possible contribution is therefore the four source-output case already treated. For the extension with source dimension \(m\) and \(m+2\) divisors, the output-leg condition is still \(b+2c=4\). The same indecomposability excludes \(c>0\), leaving \(b=4\) and \(a=m-2\). The extra source-source factors have integral cohomology and simply multiply the source cup product before evaluation on \(z\). The same target coefficient bound follows; when \(m<2\), no such nonnegative leg count is possible.

Integral Kunneth decompositions and finite sums preserve the asserted containment, which proves (T22.4) for any integral degree-four divisor polynomial. The calculation is performed before applying the selected eigenprojection. It neither assumes an integral projector on the varying output nor pays an unspecified target-dependent projector denominator. Cancellation of off-orbit components in a sum cannot change the local coefficient containment of the orbit components themselves.

If a rational combination with common denominator \(D\) equals \(Nw_r\), clearing its scalar denominators gives
\[
 DNw_r\in\Theta(L^{\mathrm{fact}}_{r,p}).
\]
The class of \(w_r\) in the saturation quotient has exact order \(p^r\), so \(p^r\mid DN\) in \(\mathbf Z_p\). This proves (T22.5) and (T22.6).

##### 4. Returning any proper block of maximal-order factors

Multiply \(F\) by \(p^a\); it suffices to prove (T22.9) for \(a=0\). Since every \(C_i\) has maximal-order action at the split prime, \(H_{I,\mathbf Z_p}\) has a basis \(\{v_\tau\}\) of pure tensor eigenlines. Expand
\[
 u=\sum_\tau v_\tau\otimes u_\tau .
\]
Each \(u_\tau\) is integral in \(V_{I^c}\). Fix one selected diagonal monomial in the target and write
\[
 S_I=\sum_{i\in I}s_i.
\]
Only source rows with a nonzero coefficient in that selected block can contribute. For such a row, the complete Hodge sign function of \(v_\tau\) equals \(S_I\), because every scalar conjugate of the rational Hodge map \(F\) preserves its pure type. Since both source and target have weight \(k\), equality of sign sums is exactly equality of Hodge types.

Restrict the target block homology to the conjugate coordinate pair containing the selected label in each factor \(i\in I\). The product lattices are direct sums by these pairs, so the restriction retains integrality. Changing the selected labels to their conjugates in a nonempty subset \(J\subseteq I\) changes the sign function by
\[
 -2\sum_{j\in J}s_j.
 \tag{T22.12}
\]
Every such \(J\) is a proper subset of all four factors. Indecomposability therefore says that the selected vertex is the **unique vertex with its own sign function** in this block's conjugate-coordinate cube. No assertion about arbitrary pairs of other vertices is needed. The restricted vector \(F(v_\tau)\) consequently has only the selected coordinate monomial.

An integral multilinear form on a product of the lattices (T22.2) supported on one coordinate monomial has coefficient in the product of the individual pure coefficient lattices (T22.11). For necessity, insert \(p^{-r}e+f\) in every factor where the selected coordinate is \(e^\vee\), and a vector on which \(f^\vee\) is a unit in every selected \(f^\vee\) factor. If there are \(m\) selected \(e^\vee\) coordinates, the value is the coefficient times \(p^{-mr}\). Integrality forces the coefficient into \(p^{mr}\mathbf Z_p\). Sufficiency follows by multiplying the individual bounds. Thus the selected coefficient of \(F(v_\tau)\) has the product dual-hull weight for the factors in \(I\).

Now restrict \(u_\tau\) to the selected conjugate pairs in the complementary factors. The original complementary vertex has sign function \(-S_I\), because \(u\) has type \((2,2)\). Flipping a nonempty subset \(J\subseteq I^c\) again changes this function by (T22.12); every such subset is proper because \(I\ne\varnothing\). Thus the selected complementary vertex is also the only allowed vertex. Integrality of \(u_\tau\) forces its coefficient into the product of the complementary individual pure-line lattices by the same direct evaluation.

Multiplying the two coefficients gives the full fourfold pure-line bound. Summing over \(\tau\) preserves it. For the selected diagonal orbit this is exactly \(p^{2r}\) in every split coordinate, proving (T22.9) for integral \(F\), and hence for general \(a\). A denominator of \(u\) is handled by first multiplying \(u\) by its clearing integer.

An actual integral correspondence induces an integral cohomological map because its class, cup product and proper pushforward are integral. It is a Hodge map in the appropriate degree. Taking the indicated Kunneth components preserves these assertions, so the geometric applications follow with the correspondence's coefficient denominator as a permissible bound for \(a\). QED.

#### Exact scope of this additional reduction

The theorem rules out two specific escapes from the computed saturation defect on the actual indecomposable principal family:

1. replacing pure divisor kernels by arbitrary integral divisor kernels, while using the specified diagonal eigenprojection;
2. first constructing integral Hodge classes with a proper block of maximal-order output factors and then returning that block by a joint Hodge correspondence of bounded coefficient denominator.

It does not prove that \(w_r\) lacks an integral algebraic-cycle representative. It does not control arbitrary correspondences acting jointly on all four output factors. For that full block, the selected vertex and its antipode are both balanced, so the unique-vertex argument fails at exactly that point. It also does not replace the missing actual integral map from the four-factor full-CM orbit to a generic \(K\)-Weil determinant plane. Such a map may have its own lattice content and is not supplied by a formal scalar relative trace.

An arbitrary non-diagonal rational projector that mixes other Hodge orbits into this one is not covered merely by calling it a projector. Its actual algebraic correspondence and its integral lattice map would have to be specified. The canonical diagonal eigenprojection in this theorem has been specified explicitly, and its integrality has not been assumed.

#### Inputs and check status

The proof uses the explicitly checked T6.16 indecomposable sign relation, the actual principal lattice realization of T6.19, and the exact lattice and primitive quotient classes of T6.21. The scalar-conjugate CM type convention is the supplied 032 paper, Section 2.2, printed p.7, equations (2.2)--(2.3); Lemma 2.4 and its complete proof, printed p.8, give the corresponding complete-type criterion for degree-one Hodge maps. Those exact passages were reread for this candidate. The remaining arguments are integral Kunneth, pure Hodge types of CM eigenlines, the \((1,1)\) property of divisor classes, and the displayed direct evaluations. No additional analytic or automorphic input is used.

The author has read the complete saved proof, including the general proper-block extension and the arbitrary-source-dimension divisor-kernel extension. The original one-factor version passed root and bounds review. The strengthened version passed author and root whole-proof review before promotion; the bounds strengthened review was pending at that time. No computation in a proof assistant is claimed.

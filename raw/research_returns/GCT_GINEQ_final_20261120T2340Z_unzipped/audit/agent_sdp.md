# SDP / Grothendieck subtask notes

Run: GCT_GINEQ, 2026-11-20 (initiated UTC). Agent: `/root/grothendieck_sdp`.
Model: GPT-6 Astra Pro, inherited. Reasoning-effort setting: not exposed; do not invent one.
These are intermediate research notes for root, not the final deliverable.

## Main conclusions for integration

1. The standard Grothendieck SDP approximates the real sign/cube norm of a matrix, not the injective norm on a product of Hilbert unit spheres. Its lower and upper certificates must be used in the correct direction.
2. The unscaled coefficient-matrix SDP, used directly as an upper bound on a Hilbert tensor's injective norm, yields only a bound at most one from the norm/support-rank inequalities. Its dual-witness use to lower-bound Hilbert nuclear norm is likewise at most the operator norm of the same coefficient flattening.
3. SDP nuclear/operator certificates for a linear flattening are valid rank and border-rank certificates, but their strength is bounded by the exact rank of that flattening divided by its rank-one cost. The same statement covers Koszul flattenings.
4. There is also a genuinely Grothendieck-specific, rank-sensitive certificate: if a matrix has rank at most s, its Grothendieck SDP optimum has a realization with vector dimension at most s. Thus `SDP(A) <= K_G(s) Q(A)`. A certified violation using an independently certified upper bound on `Q(A)` proves matrix rank greater than s. It remains a flattening certificate. The global constant by itself gives no such rank separation, and the basic SDP used on both sides cannot supply it.
5. Exact constants are not known. Searches as of 2026-11-20 UTC located substantial new 2026 results; do not give Pisier's historical bounds as current records. Precise primary-source locators are below. These numerical results are cited background; their large computational certificates have not been rerun here.
6. RS09's author-hosted PDF contains an apparent sign typo in its displayed Theorem 1.2. Its proof in Section 3.3 supplies the correct reciprocal approximation guarantee. Cite that proof, not the erroneous literal `K_G-eta` factor.

## Definitions

For a real `m x n` matrix A, put

\[
Q(A)=\max_{x_i,y_j\in\{-1,1\}}\sum_{ij}a_{ij}x_i y_j,
\qquad
S(A)=\max_{\|u_i\|=\|v_j\|=1}\sum_{ij}a_{ij}\langle u_i,v_j\rangle.
\]

Allowing vector norms at most one gives the same maximum: pad the `u` and `v` vectors with mutually orthogonal private coordinates. The maximum is attained in dimension at most `m+n`, by using a Gram matrix. Absolute values do not change either optimum because one can negate all variables on one side.

The known classical theorem is `Q(A) <= S(A) <= K_G^R Q(A)`; cite Pisier, Theorem 2.4, equations (2.4)-(2.5), or the supplied source label `thm1.2bis` in `grothendieck.bams-june3.tex`. The finite-dimensional constant `K_G^R(s)` means vectors restricted to `R^s` and is Pisier equation (4.4), with `K_G^R(1)=1`, `K_G^R(2)=sqrt(2)` and `K_G^R(4)<=pi/2` stated just after (4.4). The latter two are cited classical results, not reproved.

**Exact Banach-space dictionary.** Under the coefficient identification `A=sum a_ij e_i tensor e_j`,

\[
Q(A)=\|A\|_{\ell_1^m\otimes_\varepsilon\ell_1^n}
=\|A:\ell_\infty^n\to\ell_1^m\|.
\]

Define `gamma_2(B)=inf (max_i||p_i||)(max_j||q_j||)` over factorizations `b_ij=<p_i,q_j>`. This is the Hilbert-factorization norm of `B:ell_1^n -> ell_infinity^m`. Its unit ball consists of cross-Gram matrices of vectors of norm at most one. Therefore, for the coefficient Hilbert-Schmidt dual pairing, `S(A)=gamma_2^*(A)`. The dual of Q is the projective norm `pi_infinity` on `ell_infinity^m tensor ell_infinity^n`. The polar form of Grothendieck is

\[
\gamma_2(B)\le\pi_\infty(B)\le K_G\gamma_2(B).
\]

These statements follow directly from the injective/projective definitions and polar duality, using the standard gamma_2 convention explicitly specified here. They do not identify Q with `ell_2` injective/operator norm or `pi_infinity` with Hilbert nuclear norm.

For tensors, `sigma` and `pi` below mean Hilbert injective and projective/nuclear norms. A coordinate flattening F is the isometric reshaping of all entries into a matrix for a bipartition. It preserves the Frobenius inner product and norm.

## S-01. Exact directional Grothendieck SDP certificates

**Statement.** Let

\[
C_A=\frac12\begin{pmatrix}0&A\\A^T&0\end{pmatrix}.
\]

If `X` is a real symmetric PSD `(m+n) x (m+n)` matrix with diagonal one, and if `z` satisfies `Diag(z)-C_A >= 0`, then with

\[
L=\langle C_A,X\rangle,\qquad U=\sum_i z_i
\]

one has

\[
L\le S(A)\le U,
\qquad L/K\le Q(A)\le U
\]

for every proved upper bound `K >= K_G^R`.

**Proof.** Factor X as a Gram matrix. Its first m and last n unit vectors give objective L, so `L<=S(A)`. For any feasible Gram matrix Y,

\[
\langle C_A,Y\rangle=\langle\operatorname{Diag}z,Y\rangle
-\langle\operatorname{Diag}z-C_A,Y\rangle\le\sum_i z_i,
\]

because the trace inner product of two PSD matrices is nonnegative. This proves the upper bound without needing strong duality. Then apply `Q<=S<=KQ`. If L is negative its lower bound is simply uninformative; no sign issue invalidates the assertion. QED.

**Certificate implementation.** With rational A, rational Gram factors for X and a rational LDL-transpose/Gram factorization for `Diag(z)-C_A`, all checks are exact rational arithmetic. For algebraic constants, exact algebraic or interval enclosures with the correct directed inequalities also suffice. An approximate optimizer value alone is not the certificate. This is not an assertion that exact optimum witnesses are always rational; strict inequalities can be certified at suitably accurate interior approximations.

**Meaning.** A primal solution L gives a *lower* bound `Q>=L/K`. It must not be divided by K and then advertised as an upper bound on Q, on a Hilbert injective norm, or on rank-one summands.

## S-02. The cube/Hilbert mismatch and a precise triviality result

**Statement.** For every real tensor W and coordinate flattening F,

\[
\sigma_{\mathbb C}(W)\le\|F(W)\|_{\mathrm{op}}
\le Q(F(W))\le S(F(W)),
\qquad
S(F(W))\ge\|F(W)\|_*.
\]

Here `sigma_C` allows complex unit factor vectors even if W is real; hence the conclusion applies over both fields. Moreover `Q(A)>=||A||_F`. Consequently:

(a) inserting the upper bound `U=S(F(T))` into a valid support-dimension estimate of the form `border_rank(T)>=(||T||_F/U)^(2/(d-1))` gives a right side at most one;

(b) every witness certified only by `S(F(W))<=1` satisfies

\[
|\langle T,W\rangle|\le\|F(T)\|_{\mathrm{op}}\le\|T\|_F.
\]

Thus such witnesses cannot obtain a nuclear-norm lower bound exceeding the Frobenius norm and cannot turn the analogous support bound `border_rank(T)>=(pi(T)/||T||_F)^(2/(d-1))` into a nontrivial bound by themselves.

**Proof.** Grouping unit tensor factors gives two unit vectors, so `sigma_C(W)<=||F(W)||op`. A real matrix has the same real and complex Hilbert operator norm. Real unit vectors have coordinates in `[-1,1]`, so their bilinear value is bounded by Q. The last inequality `Q<=S` is immediate from one-dimensional feasible vectors. For `Q>=||A||F`, average `(x^TAy)^2` over independent uniform signs. All cross terms vanish and the expectation is `sum a_ij^2`; the maximum of its square root is at least its root-mean-square.

To prove `S(A)>=||A||*`, write a thin SVD `A=U Sigma V^T`. The rows of U and V have norm at most one. Treat them as vector choices in the SDP, padding to unit vectors in orthogonal extra coordinates if needed. Their objective is `tr(U^T A V)=tr Sigma=||A||*`. Finally, if `S(F(W))<=1`, then `||F(W)||*<=1`, and matrix nuclear/operator duality gives

\[
|\langle T,W\rangle|=|\langle F(T),F(W)\rangle|
\le\|F(T)\|_{\mathrm{op}}\|F(W)\|_*\le\|F(T)\|_{\mathrm{op}}.
\]

This proves (b), and (a) follows from `U>=Q(F(T))>=||F(T)||F=||T||F`. QED.

**Scope limitation.** This proposition is about the unscaled standard coefficient SDP and the stated witness rule. It does not rule out preconditioned, problem-specific, noncommutative, or higher SDP/SOS methods. No impossibility claim for all SDP lower bounds follows.

**Simple diagnostic.** The Hilbert matrix tensor `I_N` has nuclear norm N and injective norm 1. A dimension-free inequality `pi_2<=K_G sigma_2` is therefore false. By contrast, `I_N` has projective norm 1 in `ell_infinity^N tensor ell_infinity^N`: average `s tensor s` over all signs s, and use a diagonal coordinate functional for the lower bound. These are different Banach-space norms.

## S-03. Exact SDP norm certificates for arbitrary linear flattenings

**Statement.** Let c be a positive integer. Let `Phi:V_1 tensor ... tensor V_d -> Mat_{a,b}` be a fixed linear map over R or C, with `rank Phi(a_1 tensor ... tensor a_d)<=c` for every simple tensor. Put `M=Phi(T) !=0`. Suppose one has certified

\[
N\le\|M\|_*,\qquad \|M\|_{\mathrm{op}}\le U,
\qquad N\ge0,\ U>0.
\]

Then

\[
\underline R(T)\ge
\left\lceil\frac{N^2}{c\|M\|_F^2}\right\rceil,
\quad
\underline R(T)\ge
\left\lceil\frac{\|M\|_F^2}{cU^2}\right\rceil,
\quad
\underline R(T)\ge\left\lceil\frac{N}{cU}\right\rceil.
\]

Every right side is at most `ceil(rank(M)/c)`, the exact bound from that same map.

**Proof.** A sum of r simple tensors maps to a sum of matrices of rank at most c, hence to rank at most cr. The `(cr+1)` minors vanish on all tensors of rank at most r and therefore on their Zariski closure (or use continuity for analytic border rank). Thus `rank M<=c border_rank(T)`. If the nonzero singular values of M are `s_1,...,s_q`, Cauchy-Schwarz and `s_i<=||M||op` give

\[
\frac{\|M\|_*^2}{\|M\|_F^2}\le q,
\qquad \frac{\|M\|_F^2}{\|M\|_{\mathrm{op}}^2}\le q,
\qquad \frac{\|M\|_*}{\|M\|_{\mathrm{op}}}\le q.
\]

Substitute the certified inequalities, divide by c, and use integrality of border rank. The same inequalities prove the comparison to exact map rank. QED.

**Concrete PSD certificates.** A witness Z with

\[
\begin{pmatrix}I_a&Z\\Z^*&I_b\end{pmatrix}\succeq0
\]

has `||Z||op<=1`, so `N=Re tr(Z^*M)` is a valid nuclear lower bound. The condition

\[
\begin{pmatrix}U I_a&M\\M^*&U I_b\end{pmatrix}\succeq0
\]

is equivalent, for U>0, to `||M||op<=U` by a Schur complement. These are genuinely SDP certificates, but their validity uses Hilbert matrix duality, not the Grothendieck constant. Ordinary flattenings have c=1; the relevant Koszul flattening has its known simple-tensor cost c. Root can insert the exact Koszul formula from the literature.

## S-04. A rank-sensitive Grothendieck gap certificate

**Statement.** If A is a nonzero real matrix of rank q, the vector optimum S(A) is attained by vectors in `R^q`. Consequently

\[
S(A)\le K_G^{\mathbb R}(q)Q(A).
\]

Suppose `L<=S(A)` is certified, `Q(A)<=U` is independently certified, and `kappa_s>=K_G^R(s)` is known. Then

\[
L>\kappa_s U\quad\Longrightarrow\quad\operatorname{rank}(A)>s.
\]

For `A=Phi(T)` with simple-tensor matrix rank at most c, the test `L>kappa_{cr}U` proves `border_rank_C(T)>r` whenever T and Phi have real entries (and proves the analogous real bound).

**Full proof.** Start with a maximizing family `u_i,v_j` in a finite-dimensional real Hilbert space, whose existence follows from compactness of the Gram spectrahedron. Set `w_i=sum_j a_ij v_j`. The span E of the w_i has dimension at most q, since the map from the row space of A sending a row `(b_j)` to `sum b_j v_j` is linear. Holding the v_j fixed, the maximum over unit u_i is `sum_i ||w_i||`. The original family is globally maximizing, so replacing every u_i with `w_i/||w_i||` when nonzero preserves the global optimum. For zero w_i choose any unit vector in E; E is nonzero, because otherwise the original objective is zero whereas S(A)>0 for A nonzero. All new u_i belong to E. Now set `z_j=sum_i a_ij u_i`, which belongs to E. Holding the u_i fixed, replace each v_j with `z_j/||z_j||`, choosing any unit vector of E if z_j=0. This cannot decrease the objective and cannot exceed the global maximum, so preserves it. All new vectors lie in E. An isometric identification `E -> R^q` proves the first claim. The definition and monotonicity of `K_G(s)` then imply `rank(A)<=s => S(A)<=K_G(s)Q(A)<=kappa_s U`, contradicting L. For a real matrix, rank over R equals rank over C. Combine with the minor argument in S-03. QED.

**What it does not imply.** Taking `kappa_s=K_G` independent of s cannot yield a strict violation because the universal Grothendieck inequality forbids one. Nor can one take U to be the same basic SDP upper value: then `L<=S(A)<=U` and `kappa_s>=1` prevent a violation. One needs a sufficiently sharp separate upper certificate for Q (a Boolean SOS certificate, exact enumeration, or a special structural argument). This rank test cannot exceed the exact rank of the chosen flattening. It is a reformulation/certificate mechanism, not an improved rank theorem for the GCT tensors.

**Boolean SOS format.** With `z=(x_1,...,x_m,y_1,...,y_n)` and `f(z)=sum a_ij x_i y_j`, an identity

\[
U-f(z)=v(z)^T H v(z)+\sum_k h_k(z)(z_k^2-1),\qquad H\succeq0,
\]

is an exact upper certificate `Q(A)<=U`. Its coefficient identities and Gram positivity are finite checks. This observation asserts validity, not uniform polynomial-size availability.

## S-05. Fully rational, nontrivial worked certificate

Take

\[
A=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
u_1=(1,0),\ u_2=(0,1),\quad
v_1=(3/5,4/5),\ v_2=(3/5,-4/5).
\]

These are rational unit vectors and their SDP objective is `14/5`. For signs,

\[
Q(A)=\max_{y_1,y_2=\pm1}\bigl(|y_1+y_2|+|y_1-y_2|\bigr)=2.
\]

Since `K_G(1)=1`, S-04 proves `rank A>1`. The bound is attained because A is a 2 by 2 matrix.

There is also a degree-four SOS upper certificate. Put `f=x_1(y_1+y_2)+x_2(y_1-y_2)` and

\[
H_0=(x_1^2-1)(y_1+y_2)^2+(x_2^2-1)(y_1-y_2)^2
+(2+2x_1x_2)(y_1^2-1)+(2-2x_1x_2)(y_2^2-1).
\]

Direct expansion gives `f^2-4=H_0`, and hence the exact identity

\[
2-f=\tfrac14(2-f)^2-\tfrac14 H_0.
\]

Modulo the Boolean equations, the right side is a square. This is a small exact SDP/SOS certificate for the Q upper bound, independent of the basic Grothendieck vector relaxation. No numerical solver is needed.

## S-06. Bounded-weight and approximation certificate (root owns final proof)

Assume U,B>0 and delta>=0. If a tensor witness Z has certified `sigma(Z)<=U`, then nuclear duality gives

\[
\pi(T)\ge\frac{|\langle Z,T\rangle|}{U}.
\]

If `T'=sum_{j=1}^r lambda_j a_j` with unit simple atoms and `|lambda_j|<=B`, and `||T-T'||F<=delta`, then

\[
r\ge\frac{\bigl(|\langle Z,T\rangle|-\delta\|Z\|_F\bigr)_+}{UB}.
\]

Proof: `|<Z,T'>|<=U sum |lambda_j|<=UrB` and `|<Z,T-T'>|<=delta||Z||F`. If fixed-r decompositions converge to a tensor of rank greater than r, their total normalized term weight necessarily tends to infinity: a bounded subsequence would have a convergent subsequence of all coefficients and unit atoms by compactness and give a rank-r limiting decomposition. This is the exact reason one cannot impose a uniform B in a border-rank degeneration.

## S-07. Tensor-power obstruction to any fixed constant repair (root/tensor agent owns final proof)

For the matrix multiplication tensor `M_n`, `sigma=1`, `||M_n||F^2=n^3`, and `pi=n^3`. Therefore the three candidate ratios `pi/sigma`, `pi^2/F^2`, and `F^2/sigma^2` all equal `n^3`. Strassen's seven-term formula gives `R(M_2)<=7<8`. Under grouped tensor products `M_2^{tensor k}=M_{2^k}` and `R<=7^k`, whereas all three ratios equal `8^k`. For any fixed positive C, choose k with `(8/7)^k>C`; then the assertion `rank >= ratio/C` fails, and so does the corresponding border-rank assertion. In particular no fixed factor made from powers of `K_G` repairs those false inequalities.

## S-08. No Grothendieck gap on the natural target flattenings

**Statement.** For every natural coordinate bipartition of the matrix multiplication tensor, row permanent tensor, or row determinant tensor, and for the ordinary symmetric tensor flattenings/catalecticants of determinant or permanent, the matrix A satisfies

\[
Q(A)=S(A)=\sum_{ij}|a_{ij}|.
\]

The determinant matrices are understood with any of the usual ordered-tensor, monomial, or orthonormal symmetric monomial bases, whose normalization factors are positive. In particular, the gap test S-04 is uninformative for these natural matrices, even when their matrix ranks are large. This statement is not made for arbitrary preconditioned matrices or arbitrary Koszul flattenings.

**Proof.** First suppose `D_1 A D_2` is entrywise nonnegative for diagonal sign matrices `D_1,D_2`. Q and S are unchanged by those row and column sign switches. For a nonnegative matrix B, every scalar sign product and every inner product of unit vectors is at most one, while choosing every sign +1 or every vector equal attains `sum b_ij`. Hence `Q(A)=S(A)=sum|a_ij|`.

The matrix multiplication tensor has all coefficients zero or one in its standard matrix-unit bases, so every coordinate flattening is already nonnegative. The permanent tensors have nonnegative coefficients in all the specified bases for the same reason.

For the row determinant tensor, consider first a `k | (n-k)` grouping of the ordered row factors. Nonzero rows are ordered injective k-tuples alpha with image S, and their only nonzero columns are ordered injective `(n-k)`-tuples beta with image `S^c`. Thus, after row/column permutations, the support decomposes into disjoint blocks indexed by k-subsets S. Let `eta_S` be the sign of the shuffle listing S increasingly followed by `S^c` increasingly; let `epsilon_alpha` and `epsilon_beta` be the signs of the two tuple orderings relative to those increasing lists. The concatenated full permutation has sign

\[
\operatorname{sgn}(\alpha,\beta)=\eta_S\epsilon_\alpha\epsilon_\beta.
\]

Multiply the row alpha by `eta_S epsilon_alpha` and the column beta by `epsilon_beta`. Every nonzero entry becomes +1. Each row/column is in only one block, so the choices are globally compatible. An arbitrary factor bipartition differs from the contiguous grouping by a fixed permutation of tensor factors, which only changes a global determinant sign, so the same conclusion follows.

For the symmetric determinant polynomial tensor, a nonzero row of the k-flattening is an ordered partial matching, or its symmetric monomial, between a k-subset R of matrix rows and a k-subset C of matrix columns. The corresponding columns are precisely the complementary partial matchings between `R^c` and `C^c`. Again the support decomposes into disjoint blocks indexed by `(R,C)`. If tau is the row partial bijection in increasing coordinates and upsilon is the complementary one, the full permutation sign is the Laplace sign factorization

\[
\operatorname{sgn}(\tau\sqcup\upsilon)
=(-1)^{\sum_{i\in R}i+\sum_{j\in C}j}
\operatorname{sgn}(\tau)\operatorname{sgn}(\upsilon).
\]

To verify it directly, permute the full matrix's rows to list R then `R^c`, and its columns to list C then `C^c`. The determinant sign of these two reorderings has product `(-1)^(sum R+sum C)` because their individual exponents subtract the same `k(k+1)/2`. The resulting matching permutation is block diagonal, with signs `sgn tau` and `sgn upsilon`. This proves the displayed factorization. Place the fixed block sign and `sgn tau` in the row switch and `sgn upsilon` in the column switch. Normalizations in passing between ordered, monomial, and normalized symmetric bases only multiply entries by positive row/column weights (and an overall positive scalar), so they do not alter this signability conclusion. In a differential catalecticant basis the differentiation factorials are also positive. The first paragraph now proves the claimed equality. QED.

**Implication.** For these matrices, any certified `L<=S(A)` and `U>=Q(A)` have `L<=U`. Since `kappa_s>=1`, the strict inequality required in S-04 is impossible. This is a target-specific conclusion with a complete proof, stronger than merely saying that the rank-gap method is bounded by flattening rank.

## Literature and exact locators

### Pisier / supplied file

* Gilles Pisier, *Grothendieck's Theorem, past and present*, arXiv:1101.4195v3 (2011). Primary PDF: https://arxiv.org/pdf/1101.4195 . Supplied `grothendieck.bams-june3.tex` is sufficient for full text. Printed locators: Theorem 1.1 (initial elementary form); Theorem 2.4, (2.4)-(2.5) (discrete GT); Theorem 3.1, (3.13)-(3.14) (projective-vs-Hilbertian norm on `C(S) tensor C(T)`); equation (4.4) and following paragraph (`K_G(s)`, `K_G^R(2)=sqrt2`, `K_G^R(4)<=pi/2`); Theorem 12.12 and Section 19 (real quantum correlations/Tsirelson); Section 20 (failure of a naive trilinear quantum analogue); Section 22 (computational applications). The PDF has a re-render date 2024 but its arXiv footer/version is v3, 4 June 2011. Do not interpret its historical bounds as current.

### Alon--Naor

* Noga Alon and Assaf Naor, *Approximating the Cut-Norm via Grothendieck's Inequality*, SIAM J. Comput. 35(4) (2006), 787-803. Author PDF https://web.math.princeton.edu/~nalon/PDFS/cutnorm3.pdf . Theorem 4.3 (PDF p.13): randomized rounding has expected value `(2 log(1+sqrt2)/pi)` times the given vector value. Section 4.4 applies it to cut norm. Lemma 2.1 supplies the exact augmented-matrix reduction (root can inspect if desired). Theorem 3.3 gives a deterministic constant guarantee. This is approximation of the sign/cut problem, not tensor CP rank.

### Raghavendra--Steurer

* Prasad Raghavendra and David Steurer, *Towards Computing the Grothendieck Constant*, SODA 2009, 525-534. Author PDF https://www.dsteurer.org/paper/grothendieck.pdf ; author overview https://www.dsteurer.org/paper/grothendieck/ . Theorem 1.1 (PDF p.2) gives UGC-based hardness below `K_G` in the loss-factor convention. Theorem 1.3 (same page) gives effective approximation of the constant to prescribed error. **The displayed Theorem 1.2 prints `K_G-eta`, apparently a sign typo** under its stated factor convention. Its proof, Section 3.3, equations (3.5)-(3.7), explicitly gives returned expected objective at least `(1/K_G-4eta) SDP(A)` before discretization. State the guarantee as `1/K_G-epsilon`, or factor `K_G+epsilon`, and cite Section 3.3 rather than reproducing the incorrect minus sign. No stronger conditional claim is needed. Their UGC threshold concerns *real* bipartite quadratic optimization, not complex CP rank, nuclear tensor norm, tensor decomposition, nor algebraic circuit lower bounds.

### Current constant bounds: source-checked, not independently verified computations

The following are date-specific literature reports; the final paper can use a short two-row table and disclose that the computational certificates are cited, not rerun.

* Steven Heilman, Chris Jones, Giulio Malavolta, *Primal/Dual Method for the Grothendieck Constant*, arXiv:2610.10477v2, 14 November 2026. Primary full text https://arxiv.org/pdf/2610.10477 ; author PDF https://www.stevenheilman.org/~heilman/papers/grothprimal.pdf . Theorem 1.1, PDF p.1: `1.773 <= K_G^R <= 1.7799`. Section 4, Theorems 4.1 and 4.2, identify the lower/upper certifications; supporting certificates are on GitHub. The numerical heuristic near 1.779 is not an exact value.
* Bo Peng, *Certified Fourier rounding for the real Grothendieck inequality*, arXiv:2610.24417 (17 October 2026), primary author-posted text https://hub.valency.io/works/W_uhkyapjd . Theorem 1.1: `K_G^R < 44496791/25000000 = 1.77987164`. Section 6, equations (41)-(43), gives the final exact rational comparison after interval head/tail certification. The arXiv abstract was search-retrieved; its PDF could not be opened with the web tool in this run. The author-posted full text was opened and exact theorem/formula locators checked. The work mentions Ren's reported still stronger value 1.779754412112, but that stronger report was NOT independently source-verified here. Therefore say 'a source-verified current published/preprint bound is...' or 'the located certified preprint bounds include...', not an exhaustive global-best claim.
* Steven Heilman, Chris Jones, Giulio Malavolta, *Sharper Bounds for the Complex Grothendieck Constant*, arXiv:2609.25462 (21 September 2026). Primary author PDF https://www.stevenheilman.org/~heilman/papers/grothcx.pdf . Theorem 1.1, equation (1.2), PDF p.2: `1.4 < K_G^C < 1.404898554746`. Theorem 7.1 and equation (7.1) actually imply the slightly sharper lower bound `K_G^C>4000/2857>1.4`. Section 6.5 and (6.35)-(6.36) yield the stated upper bound. Supporting code commands appear on PDF p.20. Neither that code nor all analytic reductions were rerun here; record as cited background without a detected fault, with source-statement check, not as independently proved.
* Historical bridge if needed: Saha--Li--Xue--Chaudhuri--Klivans--Kothari--Meka, *New Lower and Upper Bounds for the Grothendieck Constant*, arXiv:2608.11158v2, https://arxiv.org/html/2608.11158v2 . Its abstract reports `6pi/11 <= K_G <= Krivine-10^-4`, while Introduction item 1 gives the sharper construction `Krivine-3.47*10^-4`. These are superseded by the previous located bounds. Song--Yue, SSRN 7469740 (September 2026) reports `1.77128<=K_G<=1.78052`; also superseded. No need to include these historical steps in the main theorem table.

### Web references available to root (must reopen before citing in chat)

* `turn891622278view1`: arXiv full real HJM PDF; theorem 1.1 and v2 date visible.
* `turn387349652view1`, `turn757542525view0`: full complex HJM author PDF, theorem 1.1 and equations.
* `turn891622278view3`: Peng full author-posted work, Theorem 1.1 and (41)-(43).
* `turn164280996academia8`: arXiv:2610.24417 abstract metadata.
* `turn289937647view2`, `turn891622278view0`, `turn862482296view4`: RS09 PDF, theorem statements and correct reciprocal proof guarantee.
* `turn387349652view0`, `turn757542525view1`: Alon--Naor PDF, Theorem 4.3.
* `turn160590846view0`, `turn862482296view2`, `turn757542525view2`: Pisier PDF and exact locators.

## Algebraic-geometric dictionary for these statements

S-01 and S-05 live on real semialgebraic Gram/PSD cones, with polynomial equations over Q for the exact rational certificates. For complex Hermitian PSD constraints one separates real and imaginary parts to obtain real algebraic coordinates; positivity is an archimedean condition, not a property of a scheme over Z alone.

S-03 and S-04 use an algebraic linear morphism `Phi` of vector bundles after bases are chosen. The locus `rank Phi<=cr` is the determinantal closed subscheme defined by `(cr+1)` minors. A rank-one parameterization factors through that locus on r-fold sums; hence its scheme-theoretic image and every relevant geometric fiber of the reduced secant closure lie there. The certificate is ultimately detecting nonmembership in this determinantal locus. The metric SDP is a way to establish that nonmembership on a chosen real/complex fiber.

For S-06, unit atoms and bounded coefficient balls are compact real semialgebraic sets after choosing Hermitian metrics; they are not G-stable secant varieties. Projection/properness of this compact parameter domain gives the limiting argument, whereas the unrestricted algebraic parameter space is nonproper and admits degenerations with coefficients escaping to infinity. This precisely distinguishes the metric statement from the algebraic border-rank statement. No lambda-ring, K_0, gamma-filtration, weight, purity, or motivic assertion follows from the inequalities without additional constructions; root should give the relevant dictionary and state this limitation explicitly.

## Check events (completed so far)

All mathematical new forms S-01 through S-06 and S-08 were read in full and checked by the authoring agent after drafting. This is a targeted proof check, not an independent reproof and not formal verification. S-05's rational/SOS identities were computer-checked in `agent_sdp_checks.py`; the exact output is `agent_sdp_checks_result.json` and reports PASS. S-07 was subsequently checked in full as the identical amplification argument N-02 in the independent-agent audit `agent_sdp_audit.md`.

Every cited source above was statement-checked at its exact locator where expressly noted. The full proofs/computational packages of RS09, current constants, and Tsirelson were not rerun or independently reproved. Label those events as carried background without fault found, plus the precise source check description; do not upgrade them to proof checks.

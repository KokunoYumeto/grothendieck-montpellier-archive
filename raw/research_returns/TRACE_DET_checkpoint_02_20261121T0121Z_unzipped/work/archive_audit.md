# Archive and toy audit — TRACE_DET, 2026-11-21

Checker: GPT-6 Astra Pro, `/root/determinants_audit`, effort setting not exposed. Full source transcriptions of cote 1 scans 110–113 read on 2026-11-21 Europe/Berlin. These are mathematical audits of the supplied text of record. The actual scan images were not provided: no row below is a claim about what Grothendieck's handwriting actually says. A mathematical repair may reflect a transcription error, an authorial slip, or an implicit convention; those alternatives require a later comparison to the manuscript.

## ARC-01. Corrected genus-zero lemma

**Statement.** Let f(z)=∑a_nz^n be a nonzero entire function. Suppose h(z)=∑b_nz^n is an entire function of genus zero, b_n≥0, and |a_n|≤b_n for all n. If the nonzero zeros z_j of f, with multiplicities, satisfy ∑_j|z_j|^{-1}<∞, then f has genus zero.

**Proof.** Every nonzero genus-zero function is of the form C z^m∏_j(1−z/u_j) with ∑|u_j|^{-1}<∞. It has minimal exponential type: for any ε>0, choose N with ∑_{j>N}|u_j|^{-1}<ε/2. For r=|z| the tail product has modulus at most exp(r∑_{j>N}|u_j|^{-1})≤exp(εr/2), using 1+x≤e^x. The remaining finite product times |C|r^m is bounded by C_εexp(εr/2). Hence |h(z)|≤C_εexp(ε|z|). This argument also applies to any genus-zero canonical product below, and includes finite products and zero-free constants.

Coefficient domination gives |f(z)|≤∑|a_n||z|^n≤h(|z|)≤C_εexp(ε|z|). Thus f has order at most one and minimal exponential type. The standard Hadamard factorization theorem, together with the assumed reciprocal-zero summability, writes

\[
f(z)=C e^{bz}g(z),\qquad g(z)=z^m\prod_j(1-z/z_j),\quad C\ne0.
\]

This is the only use of Hadamard's known factorization theorem; it is not a new theorem of this run. If the canonical factorization at order one is first written with E_1 factors, the convergent sum ∑1/z_j is absorbed into the coefficient b. It remains to prove b=0.

If b≠0, replace z by Θz, with Θ=conj(b)/|b|, so that bΘ=|b|. Absorb the harmless constant Θ^m into C and rename the rotated canonical product g. Its reciprocal-zero summability and minimal exponential type are unchanged. Choose π/3<θ<π/2. In the sector |arg z|≤θ, Re z≥cos(θ)|z|. Using the bound for f with ε=|b|cos(θ)/2 gives

\[
|g(z)|=|C|^{-1} e^{-|b|\Re z}|f(z)|
\le A e^{-a|z|},\quad a=|b|\cos(\theta)/2>0.
\]

The genus-zero bound for g also gives |g(z)|≤B exp(a|z|/3) everywhere. Put ω=e^{2πi/3} and G(z)=g(z)g(ωz)g(ω²z). For every nonzero z, at least one of z,ωz,ω²z has principal argument in [−π/3,π/3], hence lies in the above sector. Therefore

\[
|G(z)|\le AB^2e^{-a|z|/3}
\]

for every z, with the value at zero covered by increasing the constant if necessary. G is entire and bounded, so Liouville's theorem makes it constant. The displayed decay makes that constant zero. But g is a nonzero entire function and so is each rotated factor; a finite product of nonzero entire functions is not identically zero. This contradiction proves b=0. Thus f=Cg is genus zero. ∎

**Hidden-assumption audit.** f≠0 is needed because the zero function has no canonical product of the displayed type. The zeros are repeated with multiplicity. Zero at the origin is represented by finite m; it is excluded from the reciprocal sum. Nonnegative b_n is needed to pass from coefficient domination to h(|z|), not |h(z)|. If a source begins with an arbitrary genus-zero majorant and bounds by the absolute values of its coefficients, it may be replaced coefficientwise by a positive-coefficient genus-zero product |C|(1+z)^m∏(1+z/|u_j|); this justifies the reduction to positive factors. No assumption that the zeros of f lie on a line, no RH, and no positive-operator assumption is used.

**Complete check.** The whole proof was reread after composition: tail estimate, finite polynomial absorption, rotation direction, sector coverage, equal radii of the three rotations, choice a/3, nonzero product, and treatment of a zero at the origin all checked. The source's weaker final step through a nonzero constant G is unnecessary; its word “constante” is not by itself a mathematical mistranscription.

## ARC-02. Exact order of the product in scan 110

For α>1 let P_α(z)=∏_{n≥1}(1−z/n^α). It has genus zero and order 1/α, not 1.

**Proof.** The reciprocal zeros form the convergent series ∑n^{-α}, which gives the genus-zero product. Let r≥2 and N=⌊r^{1/α}⌋. At z=−r every factor is positive and the first N factors are at least 2, so log M(r)≥log P_α(−r)≥N log2. For the upper bound,

\[
\log M(r)\le\sum_{n\le N}\log(1+r/n^\alpha)+r\sum_{n>N}n^{-\alpha}.
\]

For n≤N, 1+r/n^α≤2r/n^α, so the first sum is at most Nlog(2r)−αlog(N!). The elementary bound log(N!)≥Nlog N−N and r<(N+1)^α show this is O_α(N). The integral bound for the tail gives r∑_{n>N}n^{-α}≤rN^{1−α}/(α−1)=O_α(N). Thus c_αr^{1/α}≤log M(r)≤C_αr^{1/α} for large r, and the order is exactly 1/α. ∎

Source locus: cote 1/110, lines 2–3. The words “sauf erreur” make an authorial tentative error particularly possible; mathematical certainty of the correction is high, paleographic attribution is undetermined.

## ARC-03. The liminf and decay-exponent identity in scan 113

Let α_n>0 decrease to zero. Define

\[
\rho=\inf\{s>0:\alpha_n=O(n^{-1/s})\},\qquad
\sigma=\inf\{s>0:\sum_n\alpha_n^s<\infty\}.
\]

Then

\[
\frac1\rho=\liminf_{n\to\infty}\frac{\log(1/\alpha_n)}{\log n},\qquad \rho=\sigma,
\]

with the extended conventions 1/0=∞ and 1/∞=0.

**Proof of liminf identity.** Write β for the displayed liminf. If α_n≤Cn^{-1/s}, then log(1/α_n)/log n≥1/s−log C/log n, hence β≥1/s. Conversely, if 1/s<β, the definition of liminf gives α_n≤n^{-1/s} for all sufficiently large n; the finite initial terms can be absorbed into a constant. Taking the threshold over s proves ρ=1/β, including β=0,∞. Monotonicity is not needed for this identity itself.

**Proof of equality ρ=σ and the little-o lemma.** If α_n=O(n^{-1/s}), then ∑α_n^t<∞ for every t>s, by comparison with ∑n^{-t/s}; therefore σ≤ρ. Conversely, if ∑α_n^s<∞, the sequence b_n=α_n^s is nonnegative, decreasing, and summable. For n≥2,

\[
\lfloor n/2\rfloor b_n\le\sum_{j=\lceil n/2\rceil}^{n}b_j\longrightarrow0.
\]

Hence n b_n→0 and α_n=o(n^{-1/s}); thus ρ≤s for every summability exponent s, so ρ≤σ. ∎

**Explicit refutation of limsup.** Let n_k=2^{2^k}, set α_1=1, and α_n=n_k^{-1} for n_k≤n<n_{k+1}=n_k². This sequence is positive, nonincreasing, and tends to zero. Along n=n_k the logarithmic ratio equals 1; along n=n_{k+1}−1 it tends to 1/2; throughout each block it lies between quantities tending to 1/2 and 1. Thus limsup=1 and liminf=1/2. The definition gives ρ=2: α_n≤n^{-1/2}, while at the end of a block α_nn^{1/s} tends to infinity whenever s<2. Also the kth block contributes asymptotically n_k^{2−s} to ∑α_n^s, giving σ=2. The displayed limsup in scan 113 would wrongly assert 1/ρ=1. ∎

## ARC-04. Repair of scan 113's telescoping-product proof

Suppose, after rescaling, α_{n_i}≥1/n_i for a strictly increasing sequence n_i and a summable decreasing α_n. For i≥2,

\[
\sum_{j=n_{i-1}+1}^{n_i}\alpha_j\ge\frac{n_i-n_{i-1}}{n_i}=\varepsilon_i\in(0,1).
\]

Thus ∑_{i≥2}ε_i<∞ and the recurrence is n_i=n_{i-1}/(1−ε_i), whence

\[
n_i=\frac{n_1}{\prod_{j=2}^i(1-\varepsilon_j)}
\le\frac{n_1}{\prod_{j=2}^{\infty}(1-\varepsilon_j)}<\infty.
\]

The last product is positive: eventually ε_j≤1/2 and −log(1−ε_j)≤2ε_j, so the logarithmic series converges, while the finite initial product is positive. This contradicts strict increase of the integer n_i. To deduce little-o, if nα_n does not tend to zero, take a positive threshold c and a subsequence n_iα_{n_i}≥c, then replace α_n by α_n/c. The source's unit threshold needs this rescaling or an arbitrary-threshold statement.

Source 113, line 22, may instead be written n_i=n_0/∏_{j=1}^i(1−ε_j) if n_0≥1 is explicitly defined. Its numerator 1 is correct only with an explicit n_0=1 convention. Setting n_0=0 would make ε_1=1 and invalidate the product argument. Accordingly the repair is mathematically clear but does not establish whether the manuscript omitted a prefactor or assumed a starting convention.

## Transcription candidates, with confidence separated

| cote/scan/line | Supplied reading | Mathematically valid reading | Mathematical confidence / paleographic qualification |
|---|---|---|---|
| 1/110/2–3 | order 1 for ∏(1−z/n^α), α>1 | order 1/α | Certain by ARC-02; “sauf erreur” permits authorial slip. |
| 1/111/9 | C·∑_{i=1}∞(1+α_i z) | C·∏_i(1+α_i z) | Certain: the sum has infinite constant term; only product matches genus-zero use. |
| 1/111/16 | Θ=β/|β| in f(Θz) | Θ=conj(β)/|β| | Certain for the displayed substitution; inverse-substitution notation would change the interpretation. |
| 1/112/3 | θ between π/3 and π | π/3<θ<π/2 (endpoint π/3 also works) | Certain for asserted positive lower bound Re z≥c|z| and three-sector coverage; actual glyph unverified. |
| 1/112/6 | |f(z)|≥exp(c|z|)|g(z)| | retain a positive multiplicative constant, or normalize C=1 first | Exact inequality needs constant/normalization; harmless for subsequent estimate; may be an implicit normalization rather than misreading. |
| 1/112/7 | |f(z)|≤|h(z)| | |f(z)|≤h(|z|) | Certain from coefficient domination; latter is the radial majorant. |
| 1/112/17 | ω^{2 or 3} | ω² | Certain to produce all three cube roots and product identity. |
| 1/113/8 | 1/ρ=limsup log(1/α_n)/log n | liminf | Certain; ARC-03 includes monotone counterexample. |
| 1/113/19 | α_{n_i}≥1/n_i | after rescaling from arbitrary positive threshold | An explanatory repair of little-o proof; not a certain transcription error. |
| 1/113/22 | numerator 1, ambiguous initial/final indices | n_1/∏_{j=2}^i(1−ε_j), or n_0/∏_{j=1}^i with n_0 specified | Certain safe form; numerator1 could be an unstated n_0=1 convention. |

One additional contextual qualifier in 1/110, lines 1–2: exp(z^ω) is an entire function only when ω is a nonnegative integer (apart from special constant conventions). Earlier omitted text may already impose this; do not call it a definite transcription error without the preceding context.

## ARC-TOY-01. Independent re-proof of the toy with precise domain

Let k≥2, q prime, t:F_q→[0,∞), M=∑_xt(x), and Q(x_1,…,x_k)=∑_{j=1}^{k-1}x_jx_{j+1}. Let N_k=∑_{Q=0}∏t(x_j), using counting measure, so ||t||_2²=∑t(x)² and ||t||_∞=max t(x). Additive-character orthogonality gives

\[
qN_k=M^k+R_k,\quad R_k=\sum_{h\ne0}S_k(h),\qquad
S_k(h)=t^T K_hD_tK_h\cdots D_tK_ht.
\]

There are k−1 Fourier matrices K_h(x,y)=exp(2πihxy/q) and k−2 multipliers. For h≠0, (K_hK_h*)_{x,x'}=∑_yexp(2πih(x−x')y/q)=qδ_{x,x'}, so ||K_h||=√q. Also ||D_t||=||t||_∞. Cauchy–Schwarz and submultiplicativity yield

\[
|S_k(h)|\le ||t||_2^2 q^{(k-1)/2}||t||_\infty^{k-2},
\]

and summing over h≠0 proves the claimed bound. For k=2 the factor ||t||_∞^0 is omitted, so t≡0 causes no 0^0 issue. Exactly the same proof works for any finite field F_q with a nontrivial additive character, because multiplication by h≠0 is bijective. The assumption t≥0 ensures that N_k and M are nonnegative; the norm estimate extends to complex weights by using transpose Cauchy–Schwarz.

For t≡1 and odd k≥3, K_h²=qJ with Jf(x)=f(−x), hence S_k(h)=q^{(k+1)/2}. The bound is attained after summing over h, so its constant and exponent cannot be uniformly improved in this domain.

## ARC-TOY-02. Composite cyclic moduli and k=1

The prompt's shorthand “on Z/q” needs either q prime or the following modified bound. For q≥2 arbitrary and d_h=gcd(h,q), the matrix K_hK_h* has entries q when x−x' is divisible by q/d_h and zero otherwise. It consists, after permutation, of q/d_h all-one blocks of size d_h, multiplied by q. Therefore ||K_h||=√(q d_h), and

\[
|R_k|\le q^{(k-1)/2}||t||_2^2||t||_\infty^{k-2}
\sum_{h=1}^{q-1}d_h^{(k-1)/2}.
\]

**Counterexample to the prime bound on Z/4.** Take t≡1,k=3. Since Q=x_2(x_1+x_3), fixing x_2=0,1,2,3 gives 16,4,8,4 solutions, respectively. Thus N_3=32, M³=64, and R_3=4·32−64=64. The claimed prime-form right side is (4−1)4^{(3−1)/2}||1||_2²=3·4·4=48. The corrected gcd bound gives 4·4·(1+2+1)=64, with equality.

**Counterexample at k=1 even over a prime field.** Q is the empty sum, N_1=M, and R_1=(q−1)M. For q=2 and t=(1,1/2), R_1=3/2, but the proposed bound equals (q−1)||t||_2²/||t||_∞=5/4. Thus k≥2 is necessary for the stated formula. For k=1 the exact identity is R_1=(q−1)M; it should be stated separately.

**Independent proof check.** The entire toy proof and both counterexamples were reread after composition, including matrix counts, endpoint weights, q prime versus finite field versus composite ring, and k=2/k=1 boundary cases. This is a proof independent of the root agent's derivation; symbolic enumeration is recorded separately below.

## Retrieval failure record for absent Alpöge determinant source

Search service opens of these exact attempted source routes returned `DisabledError`:

1. `https://github.com/CocoSgt/riemann-hypothesis-lean/blob/main/src/Formalism/PeriodIntegrals/BesselPeriodGGP.lean`
2. `https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/main/src/Formalism/PeriodIntegrals/BesselPeriodGGP.lean`

Both were inferred from the observed mirror root plus the supplied prior map's exact path; neither was successfully retrieved. System-1 follow-up searches for the exact filename and determinant/PeriodIntegrals combinations yielded no needed source body. These failures are evidence of the run's retrieval limit, not evidence that the underlying files or statements do not exist. The root may attempt the original author's archive route separately.


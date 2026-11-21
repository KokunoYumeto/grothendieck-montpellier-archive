# F32 proposal: countable admissible spectra and visible duality

Author/checker: `/root/gct_statements`, GPT-6 Astra Pro; reasoning effort inherited and not exposed. Date: 2026-11-21 UTC. Verification type: complete independent proof reconstruction of the parent's message-level F32 proposal, including convergence, finite tensor grouping, the signed top-radius argument, the integer-coefficient refinement, and the actual F26 completion. No numerical sampling or formal proof assistant was used. This report does not yet certify a separately generated paper version.

**Result: PASS with the conventions and precise scope below.** The moment index should be a nonnegative integer; the top spectrum must remain visible for any finite-extension version. Boundedness of the full visible reciprocal support already forces finiteness, without requiring a second local-finiteness assumption on that reciprocal support.

## 1. Definition and elementary consequences

An admissible weighted spectrum is a possibly finite or countably infinite collection

\[
\mathcal A=\{(\alpha,c_\alpha):\alpha\in A\},
\qquad A\subset\mathbb C^*,\quad c_\alpha\in\mathbb C^*,
\]

with distinct roots, such that:

1. `A` is bounded;
2. for every `epsilon>0`, the set `{alpha in A: |alpha|>=epsilon}` is finite;
3. for some **nonnegative integer** `N`,

\[
S_N(\mathcal A)=\sum_{\alpha\in A}|c_\alpha|\,|\alpha|^N<\infty.
\tag{A1}
\]

Thus zero is the only permitted accumulation point of the nonzero support. The empty spectrum is harmless and represents the zero sequence; spectral-radius statements below assume a nonempty spectrum. Equal roots are grouped and zero total coefficients are removed before calling the collection visible.

If `A` is nonempty, its supremum radius is a positive attained maximum `R`. Indeed, choose one root `alpha_0`; all roots capable of exceeding its radius lie in the finite nonempty set `|alpha|>=|alpha_0|`. The top circle `A_R={alpha:|alpha|=R}` is finite. For every integer `n>=N`,

\[
u_n=\sum_\alpha c_\alpha\alpha^n
\quad\text{converges absolutely, and}\quad
|u_n|\le S_N R^{n-N}.
\tag{A2}
\]

The choice of `N` can be increased to any larger integer, because the support is bounded. In particular two admissible spectra can always be compared at a common sufficiently large moment index.

If the initial definition permits an arbitrary integer moment index but separately assumes boundedness, one may increase it to a nonnegative index. For the automatic integer-coefficient implication in section 6, however, a nonnegative moment index must be part of the hypothesis: `alpha_j=2^j`, `c_j=1` has a convergent moment at index `−1` but unbounded support.

## 2. Exact countable power-sum lemma

**Lemma A.** For every nonempty admissible weighted spectrum,

\[
\limsup_{n\to\infty}|u_n|^{1/n}=\max_{\alpha\in A}|\alpha|=R.
\tag{A3}
\]

Consequently, if `|u_n|<=C n^s L^n` for all sufficiently large `n`, with fixed `C>0`, real `s` and `L>=0`, every visible root has modulus at most `L`. In the nonempty case the estimate with `L=0` is impossible.

**Proof.** Consider

\[
H_N(T)=\sum_{m\ge0}u_{N+m}T^m
=\sum_{\alpha\in A}\frac{c_\alpha\alpha^N}{1-\alpha T}.
\tag{A4}
\]

For `|T|<1/R`, the equality follows from absolute summation: its double absolute sum is at most `S_N/(1−R|T|)`. The right side extends meromorphically to the complex plane, with locally normal convergence off

\[
\mathcal P=\{1/\alpha:\alpha\in A\}.
\]

Here is the full convergence check. The set `mathcal P` is locally finite because roots bounded away from zero are finite. On a compact set `K` avoiding these poles, let `L_K=max_(T in K)|T|`. All roots with `|alpha|<=1/(2 max(1,L_K))` have `|1−alpha T|>=1/2` throughout `K`; the sum of their absolute terms is at most `2 S_N`. The omitted roots form a finite set and have denominators bounded away from zero on `K`. The Weierstrass criterion therefore gives uniform absolute convergence of the infinite tail, and local holomorphy away from `mathcal P`.

For a fixed root `alpha`, its own summand has residue `−c_alpha alpha^(N−1)` at `T=1/alpha`, which is nonzero. All other summands are holomorphic in a sufficiently small neighborhood of that point, by the local finiteness and the same convergence argument. Thus this pole is genuine and cannot be canceled by the infinite tail. In particular, there is a genuine singularity at distance `1/R` from the origin, while (A4) is holomorphic inside that disk. Its Taylor series has radius exactly `1/R`.

Cauchy–Hadamard gives `limsup_m |u_(N+m)|^(1/m)=R`; the fixed shift changes neither the finite positive exponential rate nor its value when rewritten with exponent `1/(N+m)`. This proves (A3). The estimate by `C n^s L^n` has upper exponential rate `L`, proving the consequence. The argument does not require real coefficients. ∎

**Uniqueness.** An eventual trace sequence has at most one admissible visible weighted spectrum. To compare two such spectra, take their union, subtract coefficients at common roots, remove zero differences, and choose a common moment index. The result remains admissible. If it were nonempty, Lemma A would give a positive spectral radius, contradicting that its sequence is eventually zero. Thus both supports and all grouped coefficients agree.

This uniqueness is within the stated absolutely convergent discrete class. It is not a statement about regularized expansions or non-atomic measures.

## 3. Closure under tensor powers, finite sums and powering

For a fixed positive integer `k`, expand

\[
u_n^k=\sum_{(\alpha_1,\ldots,\alpha_k)\in A^k}
  c_{\alpha_1}\cdots c_{\alpha_k}
  (\alpha_1\cdots\alpha_k)^n
=\sum_\rho d_{k,\rho}\rho^n.
\tag{A5}
\]

This expansion is justified by absolute convergence for `n>=N`. Each nonzero product coefficient is a **finite** sum. More precisely, a tuple with product of modulus at least `epsilon` must have every factor of modulus at least `epsilon/R^(k−1)`. There are only finitely many choices for those factors. It follows simultaneously that every exact nonzero product has finitely many factorizations from `A^k` and that the product support is finite outside every disk around zero. Its radius is at most `R^k`.

The grouped coefficients satisfy

\[
\sum_\rho |d_{k,\rho}|\,|\rho|^N
\le\sum_{A^k}\prod_{i=1}^k
     \bigl(|c_{\alpha_i}|\,|\alpha_i|^N\bigr)
=S_N^k<\infty.
\tag{A6}
\]

After deleting zero coefficients, the tensor spectrum is therefore admissible. This proof also covers all multiplicative relations among the roots. Finite unions/sums of admissible spectra are admissible after grouping, using a common moment index and the triangle inequality.

For an integer `e>=1`, the subsequence `u_(er)` has powered roots `gamma=alpha^e` and coefficients

\[
d_{e,\gamma}=\sum_{\alpha^e=\gamma}c_\alpha.
\tag{A7}
\]

Each fiber has at most `e` roots. The powered support is bounded and locally finite away from zero. Choosing an integer moment `N'` with `eN'>=N` proves the corresponding weighted absolute convergence. Thus the powered visible spectrum is admissible, although all roots on the original top circle may cancel. The finite F24 counterexample `q^n−(−q)^n` already proves that this visibility condition cannot be dropped in the countable version.

## 4. Signed even-power criterion with countable spectra

Keep the pointwise trace functions, path identity and remainder estimate of F01/F03/F24. Write `w=a+d` and suppose

\[
M_n=\sum_{\alpha\in A}c_\alpha\alpha^n,
\qquad c_\alpha\in\mathbb R\setminus\{0\},
\tag{A8}
\]

with a nonempty admissible visible spectrum. Assume that for an unbounded set of even integers `k>=2` there is a positive admissible spectrum `B_k`, meaning grouped coefficients `b_(k,beta)>0`, such that

\[
q^nN_{k,n}=-\sum_{\beta\in B_k}b_{k,\beta}\beta^n+E_{k,n}
\tag{A9}
\]

for all sufficiently large `n`. The threshold may depend on `k`. Assume the same error budget as F04:

\[
|E_{k,n}|\le C_k n^{s_k}
q^{n(kw/2+\eta_k)},\qquad \eta_k/k\longrightarrow0
\tag{A10}
\]

along the allowed unbounded even set. Then

\[
|\alpha|\le q^{w/2}\qquad(\alpha\in A).
\tag{A11}
\]

**Full proof.** The top circle `A_R` is finite, so the finite group-algebra argument of F24 applies without modification to

\[
F=\sum_{\alpha\in A_R}c_\alpha[\alpha].
\]

For even `k`, the sum of the grouped coefficients of `F^k` is `(sum_(A_R)c_alpha)^k>=0`. The element `F^k` is nonzero: otherwise every evaluation `[alpha] -> alpha^n` would show `(sum_(A_R)c_alpha alpha^n)^k=0`, and the finite Vandermonde matrix would force all `c_alpha=0`. Hence at least one grouped coefficient of `F^k` is strictly positive. This argument uses nonnilpotence, not an incorrect assertion that a group algebra with torsion is a domain.

The corresponding root `rho` has modulus `R^k`. A product using even one smaller-radius root has strictly smaller modulus, so none can contribute to or cancel its coefficient. The positive spectrum `B_k` cannot cancel it either. The exact path identity gives

\[
M_n^k+\sum_{\beta\in B_k}b_{k,\beta}\beta^n
=E_{k,n}-R_{k,n}.
\tag{A12}
\]

By section 3 the left side, after grouping, is an admissible weighted spectrum with at least the surviving root `rho`. Its other coefficients may have either sign. The path remainder satisfies

\[
|R_{k,n}|\le B^kq^{n(kw/2+d/2+1)}.
\]

For fixed `k`, Lemma A applied to (A12) and (A10) therefore gives

\[
R^k\le q^{kw/2+\max(d/2+1,\eta_k)}.
\]

Take the `k`th root, then let `k` tend to infinity through the allowed even set. All `k`-dependent constants and polynomial-in-`n` factors have already disappeared in the preceding fixed-`k` spectral-radius limit. This proves (A11). ∎

The full finite-extension and all-embeddings refinements are as follows. At `n=e_k r`, first use (A7). If at least one grouped class on the original top circle remains nonzero for an unbounded allowed set of even `k`, the same argument in `r` gives the original bound: the factor `e_k` occurs on both sides of the spectral-radius inequality and cancels. Without that retained-top-radius hypothesis the statement is false already for finite spectra. For an all-embedding conclusion, each embedding must supply the corresponding admissibility, real transformed coefficients, pointwise and output bounds, and any required top-radius visibility. Integer Euler coefficients are unchanged by embeddings, but absolute convergence and boundedness of the transformed roots must still be checked for each embedding.

## 5. Bounded visible reciprocal support forces finiteness

**Lemma B.** Let `A` be admissible and nonempty, and let `kappa!=0`. If every reciprocal `kappa/alpha`, `alpha in A`, is visible in some bounded support `D`, then `A` is finite.

**Proof.** Put `R_D=sup_(delta in D)|delta|<infinity`. Since `A` is nonempty and `kappa!=0`, `R_D>0`. Every original root satisfies

\[
|\alpha|\ge |\kappa|/R_D>0.
\]

The defining local finiteness of `A` outside every disk now makes `A` finite. No convergence or local-finiteness assumption on `D` is needed for this deduction beyond its boundedness and the stated visible containment. ∎

Thus a duality-stable class of admissible visible supports with a fixed nonzero reciprocal factor contains only finite supports whenever duality retains every reciprocal root visibly. Once independent upper bounds on both systems are established, the usual F03/F17 lower-bound calculation remains valid, but the resulting support is automatically finite. For example, an upper bound `q^((d+a)/2)` for `A` and an independent upper bound `q^((d−a)/2)` for a visible dual containing `q^d/A` give equality `|alpha|=q^((d+a)/2)` and imply finiteness.

This is a statement about the **visible** reciprocal spectrum. If cohomological cancellations erase some reciprocals, one cannot use an invisible root for the lower bound or for this finiteness claim. Infinite invisible pairs of cohomology are not excluded.

## 6. Automatic admissibility constraints for integer Euler coefficients

Suppose the distinct grouped coefficients are nonzero integers and (A1) holds for some nonnegative integer `N`, but boundedness and local finiteness have not been separately assumed.

If `N=0`, each summand `|c_alpha|` is at least one, so the support is finite. If `N>=1`, then for every `epsilon>0`,

\[
\#\{\alpha:|\alpha|\ge\epsilon\}
\le S_N\epsilon^{-N}<\infty,
\qquad
|\alpha|\le S_N^{1/N}.
\tag{A13}
\]

The first inequality follows because each such summand contributes at least `epsilon^N`; the second follows by applying the total-sum bound to a single summand. Therefore both boundedness and local finiteness are automatic. The same conclusion holds when the absolute values of nonzero coefficients have any common positive lower bound.

For arbitrary nonzero real or complex coefficients that may tend to zero, these two support conditions are not consequences of moment convergence alone and should remain explicit. For example a summable positive coefficient sequence can be placed at distinct roots accumulating at one. This example only shows why the support hypotheses cannot be silently inferred; no assertion about a broader spectral theorem is being made.

## 7. Application to the actual F26 normalized-word trace

The actual rank-three tensor module in F21/F26 gives, under either substitution `v=q^(n/2)` or `v=q^(−n/2)`,

\[
h_n=24+\frac{16q^{-2n}}{(1+q^{-n})^4}
=24+16\sum_{j\ge0}(-1)^j\binom{j+3}{3}
       \bigl(q^{-(j+2)}\bigr)^n.
\tag{A14}
\]

This is an admissible integer-coefficient spectrum with support

\[
A=\{1,q^{-2},q^{-3},q^{-4},\ldots\}.
\tag{A15}
\]

The coefficient at one is `24`; the coefficient at `q^(−j−2)` is `16 (−1)^j binom(j+3,3)`, which is nonzero. A concrete absolute moment is

\[
S_1=24+\frac{16q^{-2}}{(1-q^{-1})^4}<\infty.
\]

Its maximum radius is one, so Lemma A gives `limsup |h_n|^(1/n)=1`, also immediate from `h_n ->24`. Thus the natural completion is compatible with an **upper weight-zero radius bound**. This numerical observation does not by itself establish the pointwise/path-output hypotheses of section 4 for a geometric model.

For every fixed nonzero reciprocal factor `kappa`, its full visible reciprocal support would be

\[
\{\kappa,\kappa q^2,\kappa q^3,\ldots\},
\]

which is unbounded. In particular the completion cannot supply two-sided purity of weight zero within a trace category that requires bounded visible spectra and visibly retains the reciprocal dual roots. With the same nonzero integer multiplicities, the reciprocal series also has no absolutely convergent moment of nonnegative index: its terms do not even tend to zero. Lemma B gives the structural reason, and uniqueness in section 2 rules out an alternative admissible visible expansion of the same eventual sequence with a different finite support. The earlier F26 rationality obstruction independently excludes a finite-spectrum realization.

This addresses one precise completion escape from F26: admitting an ordinary absolutely convergent countable integer Euler spectrum repairs the finiteness assumption for an upper-bound theorem, but it does not make this particular trace compatible with bounded visible reciprocal duality. It does **not** exclude completed categories whose duals leave this convergence class, regularized traces, non-atomic spectral formalisms, or trace comparisons different from F26's all-extension arithmetic substitution. It also does not replace the still-required comparison between a fixed geometric correspondence traced against Frobenius and the formal varying-parameter matrix trace.

## 8. Suggested check-event scope

Suggested event: `F32-PROPOSAL-INDEPENDENT-COUNTABLE`, complete analytic/algebraic proof reconstruction, PASS with a nonnegative moment convention and the already necessary signed top-visibility condition for restricted extension degrees.

What was checked: the attained maximum; absolute convergence; local normal convergence and genuine poles; the exact exponential rate; uniqueness; finite product grouping and moment control; the real top-radius positivity argument; the order of the `n` and `k` limits; admissibility after root powering; the independent all-embedding/dual requirements; the automatic integer-coefficient support bounds; and the explicit F26 coefficients and reciprocal obstruction.

What was not checked or asserted: a formal kernel proof, an actual new GCT geometric realization, regularized/non-atomic traces, or a final generated F32 paper statement not yet present at the time of this report.

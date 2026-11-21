# Signed visible spectra and even tensor powers: proof audit

Checker: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date: 2026-11-21 Europe/Berlin. Review type: independent full proof reconstruction of the parent's proposed strengthening of F03/F04, with a counterexample to the initially proposed unrestricted F17 extension. No proof assistant or numerical sampling was used.

## 1. Valid full-degree theorem

Fix the F01/F03 pointwise setup: `q>1` a prime power, `d≥1`, real/integer weight parameter `a` as appropriate, and functions `t_n:F_(q^n)^d→C` with

\[
|t_n(x)|\le Bq^{na/2}.
\]

Let

\[
M_n=\sum_x t_n(x)=\sum_{\alpha\in A}c_\alpha\alpha^n,
\tag{S1}
\]

where `A` is a finite set of distinct nonzero complex numbers and every `c_alpha` is a **nonzero real number**. Algebraicity of the roots is required only for the all-embeddings/Weil-weight interpretation, not for the one-complex-embedding bound. Here `A` is the **visible** spectrum: equal roots have already been grouped and every zero total coefficient has been deleted.

Suppose that for an unbounded set of **even** positive integers `k≥2`, there is a finite positive spectral sum

\[
Q N_{k,n}=-\sum_{\beta\in B_k}b_{k,\beta}\beta^n+E_{k,n},
\qquad Q=q^n,
\tag{S2}
\]

for **every** `n≥1`. The nonzero roots in `B_k` may be grouped, with real coefficients `b_(k,beta)>0`; positive integer multiplicities are a sufficient special case. The error satisfies

\[
|E_{k,n}|\le C_k n^{A_k}q^{n(kw/2+\eta_k)},
\quad w=a+d,\quad\eta_k/k\longrightarrow0.
\tag{S3}
\]

The claim is that every `alpha∈A` satisfies `|alpha|≤q^(w/2)`. **This claim is correct.**

## 2. The exact real-coefficient lemma

Let `A_R={alpha∈A:|alpha|=R}`, where `R=max|alpha|`. In the finite formal sum of top-radius roots, put

\[
F=\sum_{\alpha\in A_R}c_\alpha[\alpha].
\]

The multiplication rule is `[alpha][gamma]=[alpha gamma]`; collect equal products in `F^k`. Write the resulting real coefficients as `d_(k,rho)`.

**Lemma.** For every even `k≥2`, at least one of the grouped coefficients `d_(k,rho)` is strictly positive.

**Proof.** The sum of all coefficients is the augmentation

\[
\sum_\rho d_{k,\rho}=
\left(\sum_{\alpha\in A_R}c_\alpha\right)^k\ge0.
\]

It remains to show `F^k≠0`. If all its coefficients vanished, then evaluating `[alpha]↦alpha^n` for every positive integer `n` would give

\[
\left(\sum_{\alpha\in A_R}c_\alpha\alpha^n\right)^k=0,
\]

so the expression in parentheses would vanish for every `n≥1`. The finite distinct nonzero roots have an invertible Vandermonde evaluation matrix for `n=1,...,|A_R|`; hence all `c_alpha=0`, a contradiction. Equivalently F02 implies that a nonempty finite visible spectrum cannot have all power sums zero. Thus some grouped coefficient is nonzero. If none were positive, all would be nonpositive and at least one strictly negative, contradicting their nonnegative sum. ∎

The possibility that the augmentation is zero causes no difficulty: then a nonzero collection summing to zero has both signs. Nor do multiplicative relations or root-of-unity ratios among the roots invalidate the argument for the **full** sequence of extension degrees.

The proof uses nonnilpotence of this particular element in the multiplicative group algebra; it does not assert that the group algebra has no zero divisors. Zero divisors can exist when roots of unity occur. The Vandermonde argument is the correct direct proof of nonnilpotence.

## 3. Full purity-bound proof

The exact path identity is

\[
Q N_{k,n}=M_n^k+R_{k,n}.
\]

Combining it with (S2),

\[
M_n^k+\sum_\beta b_{k,\beta}\beta^n
=E_{k,n}-R_{k,n}.
\tag{S4}
\]

F01 supplies, for fixed `k`,

\[
|R_{k,n}|\le B^kq^{n(kw/2+d/2+1)}.
\]

By the lemma there is a grouped root `rho` of `M_n^k` with coefficient `d_(k,rho)>0` and absolute value exactly `R^k`. A tensor product containing any root of modulus strictly below `R` has modulus strictly below `R^k`, so such terms cannot merge with or cancel this root. Adding the `B_k` sum also cannot cancel it, since that sum has positive coefficients. Therefore the left side of (S4) is a finite spectral sum with **at least one surviving root of modulus `R^k`**. Its other coefficients need not be positive.

F02 applies to arbitrary nonzero complex coefficients after grouping, so (S3) and the Parseval bound give

\[
R^k\le q^{kw/2+\max(d/2+1,\eta_k)}.
\]

Take the `k`th root and let `k→∞` through the unbounded even set. This gives `R≤q^(w/2)` and bounds every visible root. The constants depending on `k` disappear in the fixed-`k`, `n→∞` spectral-radius step before the limit in `k` is taken.

This proof does not require each diagonal tensor root `alpha^k` to survive. It proves survival of **some top-modulus product root** for every allowed even `k`, which is sufficient to bound the entire original spectrum's maximum modulus.

## 4. All embeddings and duality

For an all-conjugate claim, each embedding must have its own trace system satisfying the same pointwise and opposite-sign/error estimates. The grouped coefficients in that system must be real. Integer Euler coefficients, transported without changing the integers, satisfy this automatically; arbitrary algebraic coefficients need not remain real under every embedding.

As before, an explicit reciprocal relation among the **visible spectra**, or a separate dual system with an independently proved upper bound, supplies the lower bound. In the separate-system formulation, every reciprocal `q^d/alpha` used in the lower-bound argument must actually be visible in the dual trace system. A statement merely about an underlying cohomological eigenvalue that cancels in its Euler trace would not suffice. The F17 numerical calculation then remains correct.

The theorem does not bound eigenvalues canceled between cohomological degrees before (S1). For example the complex `Q_l(-1)⊕Q_l(-1)[-1]` has zero alternating trace for every extension, so its eigenvalue `q` is absent from the visible spectrum. No upper bound for that hidden eigenvalue follows from the theorem.

## 5. Blocker: unrestricted finite extensions do not carry over

The positive-multiset F17 proof crucially used positivity when roots were raised to the extension degree. Signed visible coefficients can cancel after that operation, even if the entire original spectrum is visible.

**Exact counterexample.** Let `a=0`, `d=1`, and `B=2`. For every `n≥1` define the constant function

\[
t_n(x)=\begin{cases}0,&n\text{ even},\\2,&n\text{ odd}.
\end{cases}
\]

Then `|t_n|≤2` and

\[
M_n=q^n-(-q)^n.
\]

The two distinct roots `q,−q` have nonzero real coefficients `1,−1`; both are visible and both have modulus `q>q^(1/2)`. For every even path length `k`, choose `e_k=2`. At every required degree `n=e_k r=2r`, the function is identically zero, hence `N_(k,n)=R_(k,n)=0`. The proposed opposite-sign hypothesis holds with the empty positive spectrum and zero error. Thus all proposed subsequence hypotheses hold but the intended upper bound fails.

The failure is exactly

\[
q^{2r}-(-q)^{2r}=0.
\]

This is not a counterexample to the original F17 with positive multiplicities, and it is not a counterexample to §§1–3, where (S2) holds for every `n`.

## 6. Precise finite-extension repairs

For `e≥1`, group the powered roots by

\[
d_{e,\gamma}=\sum_{\alpha^e=\gamma}c_\alpha,
\qquad
M_{er}=\sum_\gamma d_{e,\gamma}\gamma^r.
\tag{S5}
\]

Delete zero coefficients and let `R_e=max{|gamma|^(1/e):d_(e,gamma)≠0}`, with the empty case giving no information. The same even-power argument applied in the variable `r` bounds `R_(e_k)`, not automatically the original `R`:

\[
R_{e_k}\le q^{w/2+\max(d/2+1,\eta_k)/k}.
\tag{S6}
\]

The original conclusion follows if the top radius remains visible for an unbounded set of allowed even `k`, namely `R_(e_k)=R`. Sufficient explicit conditions include:

- for those `k`, at least one powered-root class of original modulus `R` has nonzero coefficient sum;
- all coefficients on the top-radius spectrum have one common sign;
- no ratio of two distinct top-radius roots is a root of unity, so powering never merges them;
- more generally, choose the `e_k` so that no canceled grouping removes every top-radius class.

These are additional hypotheses. Arbitrary `e_k` without a visibility requirement is false. For an all-embeddings conclusion, apply the appropriate visibility condition separately to the maximum-radius spectrum in each embedding.

The grouped-root method may be the cleanest theorem wording: state the full-degree signed theorem first, and then state the extension version with its explicit retained-top-radius condition. There is no need to alter the earlier positive-multiset F17, whose stronger automatic noncancellation remains valid.

## 7. Complex coefficients can defeat the full-degree version

The real-coefficient hypothesis has a concrete role and cannot simply be deleted from this formulation. The parent supplied the following countermodel, and I independently verified its counting formula in full.

Let `d=1`, `a=0`, `B=1`, and take `t_n(x)=i` for every `x∈F_(q^n)` and every `n`. Then

\[
M_n=i q^n,
\]

with the visible root `alpha=q` and coefficient `i`. This root violates the proposed bound `q^(1/2)`.

Take the unbounded set `k≡2 mod4`, and write `k=2m`. Split the coordinates into odd and even positions, `a_j=x_(2j−1)` and `b_j=x_(2j)`. The path polynomial is

\[
P_k=\sum_{j=1}^m a_jb_j+\sum_{j=1}^{m-1}a_{j+1}b_j.
\]

Its coefficient matrix between the `a` and `b` variables is triangular with diagonal entries one. An invertible linear change of the `a` coordinates therefore takes it to the standard nondegenerate bilinear pairing. The number of zeros is

\[
Q^m+(Q^m-1)Q^{m-1}
=Q^{2m-1}+Q^m-Q^{m-1}.
\]

This argument works in every characteristic. Since `i^k=−1`, the weighted count satisfies

\[
Q N_{k,n}=-Q^k-Q^{k/2+1}+Q^{k/2}.
\]

Thus (S2) holds for **all** extension degrees with positive spectrum `B_k={q^k,q^(k/2+1)}` and error `E_(k,n)=Q^(k/2)`. The error has `eta_k=0` because `w=a+d=1`. All assumptions except real coefficients hold, but the upper bound fails. In the formal-power argument every top coefficient here is `i^k=−1`, so the positive `B_k` root cancels it exactly.

This proves that the real-coefficient condition is not dispensable **in this theorem with its prescribed unbounded even set and opposite-sign hypothesis**. It does not exclude other complex-coefficient criteria with additional phase controls or different path-length hypotheses.

## 8. Check result

- Full-degree signed even-tensor theorem: **PASS**, including controlled errors.
- Original all-embedding convention: **PASS with real transformed coefficients and the stated independent systems**.
- Reciprocal lower bound: **PASS for reciprocal visible spectra / independently bounded visible dual system**.
- Arbitrary finite-extension refinement copied from positive F17: **FAIL**, exact counterexample in §5.
- Finite-extension refinement with retained top-radius visibility: **PASS**, proved by grouping (S5) before the even-power argument.
- Dropping the real-coefficient hypothesis in the full-degree error version: **FAIL**, exact split-bilinear counting countermodel in §7.

This review concerns the message-level proposal. A final generated theorem file requires a separate direct text match before its check event should be called a final-text proof audit.

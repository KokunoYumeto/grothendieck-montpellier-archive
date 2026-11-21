# A-086. Whole-proof audit of G037

**Status: PASS.** I read the whole `work/root/stable_hook_report.md`, HK.1–HK.19 and all seven sections, and every line of `stable_hook_positive.py`. The actual stable-chart/Koszul comparison, cancellation, one-polytope construction, sharp support and uniform binary-degree bounds pass.

## 1. Stable module and exact Koszul maps

The first gap is $m(n-a-t)+(m-2)a-r\ge0$, including $a=1,r=m-2,n=a+t$. The stable flag map applies because the second part is $a+t\le n$. Its balanced substitution and inverse, followed by the perfect determinant-column pairing, identify the actual balanced module with $\operatorname{sgn}^t\otimes S_{(a,1^r)}\mathfrak h_m$. The outer-label transpose for odd $t$ is therefore exact.

On total degree $D$, the Koszul multiplication differential and exterior derivative satisfy $\partial d_P+d_P\partial=D$. This follows on monomial wedges by cancelling the off-diagonal product/exterior terms and summing the polynomial and exterior Euler degrees. Thus $d_P/D$ gives an actual contracting homotopy for every degree used here.

Exterior Pieri gives the two rational Young images in $\operatorname{Sym}^{D-r}W\otimes\Lambda^rW$. The differential has a nonzero term on the displayed highest vector of shape $(D-r+1,1^{r-1})$, and its target has no copy of $(D-r,1^r)$. Its kernel is exactly the latter image. At $r=0$ the positive-degree identity applies; at $a=1,r=m-2$ the kernel is the top exterior power. Thus no hook-length endpoint is omitted.

## 2. Positive cancellation and exact finite-set count

The cycle eigenvalues give HK.7 directly. Macdonald's virtual principal specialization, with $z=-u$, evaluates precisely those power sums. Removing the factor at $(1,1)$ accounts for the fixed line in the permutation representation. Replacing $u$ by $qu$ correctly changes from polynomial degree to total degree.

The Koszul short exact sequences give
$(1+u)\sum_j\operatorname{Hilb}_\nu(Z_j)u^j
=\operatorname{Hilb}_\nu(P\otimes\Lambda W;q,qu)-\mathbf1_{\nu=(m)}$.
For a non-row label the cell $(2,1)$ exists, has content $-1$, and contributes exactly the factor $1+u$. Cancelling that specified factor leaves the elementary sum over the remaining cells in HK.12.

The fake-degree series has the actual standard-tableau comajor count. Each elementary monomial records a literal subset of distinct cells, even when weights coincide. The identity

$$
b(\nu)+\sum_{(i,j)\in J}(j-i+1)
=\sum_{(i,j)\notin J}(i-1)+\sum_{(i,j)\in J}j
$$

proves nonnegative exponents. The numerator is consequently a positive finite tableau/subset count, and the denominator is the explicit coin count. The original representation comparison has already been supplied by the preceding actual maps.

## 3. Trivial branch and its exact basis

Solomon's differential-form map and the invariant rational dot form identify the invariant complex with the weighted Koszul complex on $e_2,\ldots,e_m$, with $\xi_j=de_j/j$ and $\partial\xi_j=e_j$. Exact rational averaging identifies its cycles with the original invariant cycles.

In a fixed multidegree $\beta$, writing $i$ for the least positive exponent identifies the differential with contraction taking every available basis vector to one. The change of basis to $v_i$ and $v_j-v_i$ shows directly that the kernel basis is the wedge basis in the latter vectors. Every denominator in HK.14 cancels against a positive exponent and appears at most once in a nonzero wedge term. At exterior degree zero the positive-degree convention gives $I_+$.

Thus least index, subset and remaining monomial exponents give the exact basis count HK.15, including $r=0$ and $r=m-2$.

## 4. One bounded polytope and its inverse encoding

In the nontrivial branch, the binary assignment variables assign each label exactly once to each cell. Adjacent row/column inequalities are exactly the standard-tableau partial order. For the row difference $R_{j+1}-R_j$, HK.17 permits precisely the nonpositive range when the descent bit is zero and the positive range when it is one; all possible row differences lie within its bounds. Hence the descent bits are uniquely determined.

The subset bits specify distinct retained cells, and the degree equation is exactly the comajor-plus-cell-weight-plus-coin decomposition. Negative cell weights have total absolute contribution below $m^2$, so the stated coin upper bounds follow. Each tableau, subset and coin solution determines every variable, and conversely every integer point recovers exactly that data. The variable count is $m^2+(m-1)+(m-2)+(m-1)=m^2+3m-4$.

In the trivial branch, the unique nonzero $z_i$ forces all lower exponents to zero and $\beta_i\ge1$. The selected $y$-indices are above $i$ and have positive exponents. Thus $z,y,\beta$ recover exactly the least-support-index basis of HK.14. The reverse construction is unique. All $3m-3$ variables have explicit finite bounds. Both are single bounded rational polytopes, including zero-count cases.

## 5. Exact support

The lowest fake-degree coefficient is one. Its next coefficient is the number of removable corners minus one, directly from the first two coefficients of the hook product. Therefore every nonrectangular label has the next numerator degree.

For a non-row rectangle, the retained weights have consecutive support. The column, height-two and larger-rectangle cases listed in the report give this explicitly. For a nonempty proper minimum-cardinality subset, either the cut is strict, the cut value has a successor, or the cut is at the maximum. In these cases replacing one selected cell weight by an available weight one higher raises the sum by one. The only cases with no such subset are $r=0,m-2$; retained multisets of size at most one have no proper nonempty subset.

Coin weights two and three give every increment at least two. Thus the sole possible next-degree gap is exactly the rectangular endpoint exception in HK.2.

For the trivial branch the minimum tag is $i=2$, $T=\{3,\ldots,r+2\}$. A nonmaximal leg can increase the largest selected index by one; for $r=0$ one uses $i=3$. At the maximal leg there is only one tag, and the coin increments omit one. This proves HK.3, including all $m=3$ endpoints.

## 6. Uniform construction and binary-degree evaluation

Hook-product and cardinality-indexed elementary multiplication require polynomially many operations in $m$; their degrees are $O(m^2)$ and coefficient bit lengths are polynomial in $m$. The exact parity identity is valid for the full numerator polynomial, without discarding high terms. Each step halves the requested degree and keeps polynomial degree $O(m^2)$.

The denominator roots remain roots of unity after squaring. With constant term one, the absolute values of its coefficients are bounded by binomial coefficients in its degree, hence by $2^{O(m^2)}$. Multiplying the numerator by this denominator adds only $O(m^2)$ coefficient bits per step. There are $O(\log(D+1))$ steps. This proves polynomial bit complexity directly.

Every polytope witness has polynomial binary length and is checked by integer matrix multiplication. The encoding qualification is necessary and correctly stated: polynomial dependence on $m$ is polynomial in the ordinary listed partition input when $t\ge1$; the report does not replace $m$ by $\log m$ for a compressed $t=0$ input.

## 7. Independent executed checks and primary sources

`check_stable_hook_independent.py` enumerates standard tableaux by removable-corner recursion, expands actual retained-cell subsets and uses direct coin counts. For $m=3,\ldots,6$ it checks 633 coefficient counts and support cases, all 633 exported matrices, and 348 literal bounded witnesses, including all hook-leg endpoints and the predicted support gaps.

An independent binary-power calculation modulo the denominator recurrence polynomial checks twelve values at degrees $10^{12}+17$ and $10^{30}+21$. This uses a recurrence companion algebra rather than parity extraction. All comparisons pass; the receipt is `STABLE_HOOK_INDEPENDENT_RECEIPT.json`. The parent's separate original-cycle and Murnaghan–Nakayama sweeps were read and are not claimed as my executions.

I independently read Macdonald, second edition, I§3 Examples 1–3, printed pp44–45, including the finite Vandermonde specialization and the polynomial interpolation proof of the virtual specialization. The local primary copy is work/archive/Macdonald.pdf; the public source is https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf.

I independently opened Solomon's primary published PDF and read §2 and the full §3 theorem and proof, printed pp59–61, together with the Hilbert-series formula (4), p62. The theorem's characteristic-zero domain and its actual differential generators match the use here. Source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/160748DDB7C9D17C5379F6FF65BB5B98/S0027763000011028a.pdf/invariants_of_finite_reflection_groups.pdf.

I also read Bostan–Mori, §2.1, the proof of Theorem 1 and Algorithm 1, author-PDF pp4–5, at https://specfun.inria.fr/bostan/BoMo21.pdf. Its parity identity is the one proved directly here; the report supplies its own bounded-degree and integer-bit analysis for this family.

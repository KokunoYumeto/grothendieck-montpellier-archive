# Fresh review of the countable-spectrum extension F32

Reviewer: /root/rectangular_and_theta, GPT-6 Astra Pro. Date: 2026-11-21 UTC.

## Checked snapshot and verdict

The complete agent_countable_spectrum_audit.md was read, including all eight sections and every displayed proof. SHA-256:

6b97d03f1354c909583facd123177f943ec4caf6af3b1035942d94a1c1e9c71b.

**PASS. No mathematical blocker found.** This is a fresh analytic/algebraic check of the report, together with an independent proof of its central spectral-radius lemma below. It does not certify a subsequently generated F32 paper fragment, any actual nonstandard realization, or traces outside the stated convergence class. The finite F24 path identity and sign argument were also read in their paper context to check the transfer of the hypotheses.

## 1. Admissibility and the report's pole proof

The support conditions ensure an attained positive maximum radius for a nonempty support. Choosing any existing root reduces the candidates above its radius to a finite nonempty set. They also ensure a finite outer circle and a strict gap from that circle to the remaining radii. The weighted moment gives absolute convergence at every integer index at least N, with the stated bound \(S_N R^{n-N}\). A larger common nonnegative moment can always be chosen because the support is bounded.

The generating-series argument is valid. Inside \(|T|<R^{-1}\), absolute double summation follows from the geometric bound. On a compact set avoiding the reciprocal support, the roots sufficiently close to zero have denominators uniformly bounded below by \(1/2\); their individual majorants \(2|c_\alpha||\alpha|^N\) form a summable series. The other roots form a finite set. This proves normal convergence, not merely pointwise convergence. The reciprocal pole set is locally finite. At each reciprocal root the single corresponding summand has the nonzero residue \(-c_\alpha\alpha^{N-1}\), while all remaining summands are holomorphic in a neighborhood after deleting that root. Thus every asserted pole is genuine.

Consequently the Taylor radius is exactly \(R^{-1}\), and Cauchy–Hadamard gives the asserted exponential rate. The fixed index shift does not change a finite positive exponential rate. The estimate with \(L=0\) makes the sequence eventually zero and is incompatible with a nonempty visible admissible spectrum.

## 2. Independent proof by separation of the outer circle

Here is a second proof of Lemma A that uses no meromorphic continuation.

Let \(A_R=\{\alpha_1,\ldots,\alpha_m\}\) be the outer circle, with \(|\alpha_j|=R>0\). If there are any remaining roots, there is an \(r<R\) bounding all their moduli: only finitely many roots have modulus at least \(R/2\), so take the maximum of \(R/2\) and the finitely many radii strictly below R in that set. Write
\[
u_n=R^n T_n+v_n,\qquad
T_n=\sum_{j=1}^{m}c_j\zeta_j^n,\qquad
\zeta_j=\alpha_j/R.
\]
The \(\zeta_j\) are distinct points of the unit circle. The moment hypothesis gives
\[
|v_n|\le S_N r^{n-N}\quad(n\ge N).
\]
If there are no remaining roots, take \(v_n=0\).

Finite geometric summation gives
\[
\lim_{L\to\infty}\frac1L\sum_{n=1}^{L}|T_n|^2
=\sum_{j=1}^{m}|c_j|^2>0.
\]
Indeed, the diagonal terms have average one and each off-diagonal ratio
\(\zeta_i\overline{\zeta_j}\ne1\) has Cesàro average zero. It follows that
\[
|T_n|\ge
\left(\frac12\sum_{j=1}^{m}|c_j|^2\right)^{1/2}
\]
for infinitely many n. Along such a subsequence, \(|v_n|/R^n\to0\). Hence for some fixed \(c>0\), \(|u_n|\ge cR^n\) on an infinite subsequence. This proves
\(\limsup |u_n|^{1/n}\ge R\).
The general bound \(|u_n|\le S_N R^{n-N}\) proves the reverse inequality.

This is a separate reconstruction of the countable lemma. It uses both the finite outer circle and the strict radius gap supplied by local finiteness away from zero; neither is silently deduced from convergence of an arbitrary weighted series.

## 3. Uniqueness and products

The difference of two admissible expansions remains admissible after taking a common moment and grouping common roots. If any visible difference survives, the spectral-radius lemma contradicts eventual vanishing. Thus uniqueness is correct within this discrete, absolutely convergent class.

For a fixed tensor power k, the support is bounded by \(R^k\). A product of modulus at least epsilon has every factor of modulus at least \(\epsilon/R^{k-1}\), so only finitely many tuples can contribute. In particular each exact nonzero product has finitely many factorizations, even if the roots satisfy multiplicative relations. The coefficient grouping is therefore finite at each product root. The weighted triangle bound by \(S_N^k\) verifies the needed absolute moment for the grouped product spectrum.

Finite sums use a common moment. Powering by e has finite fibers of size at most e, and any integer \(N'\) satisfying \(eN'\ge N\) gives a valid absolute moment. Powering can erase a whole top circle because signed coefficients may cancel, so the visibility qualification is essential and correctly retained.

## 4. Signed even powers and the order of limits

On the finite outer circle, the real coefficient group-algebra element F has nonzero even powers. Evaluation at all positive integer powers followed by a finite Vandermonde argument proves this directly, even in the presence of torsion relations among the roots. The proof does not assume a torsion group algebra is a domain.

The augmentation of \(F^k\) is nonnegative when k is even. Since \(F^k\ne0\), at least one grouped coefficient is positive. Products involving a smaller-radius root cannot have that outer product's modulus; adding a positive output spectrum cannot cancel its positive coefficient. These facts are unchanged in the countable setting because all exact product groupings were proved finite.

The path identity has the required sign:
\[
M_n^k+\sum_{\beta\in B_k}b_{k,\beta}\beta^n
=E_{k,n}-R_{k,n}.
\]
The left side is admissible and retains a root of modulus \(R^k\). Taking the spectral-radius limit in n for each fixed k first yields
\[
R^k\le q^{kw/2+\max(d/2+1,\eta_k)}.
\]
Only after this limit is taken does the proof send k through the unbounded allowed even set. Thus all k-dependent constants and polynomial factors are harmless; no uniform bound in k was smuggled in.

For the restricted-extension form, the powered input must retain an original top-radius class for an unbounded allowed set of k. The factor e appears in both exponents and cancels exactly. The report also correctly makes admissibility, real transformed coefficients, output bounds and visibility separate requirements at each embedding. Integer coefficients help only with their transformation, not with convergence under all embeddings.

## 5. Reciprocal duality and integer coefficients

If every \(\kappa/\alpha\) is visible in a bounded dual support, then
\[
|\alpha|\ge|\kappa|/R_D>0.
\]
Local finiteness of the original support immediately makes it finite. The argument needs neither a dual moment nor dual local finiteness; the report correctly states only the hypotheses actually used. It also correctly excludes invisible canceled reciprocal roots from the conclusion.

For nonzero integer coefficients and a nonnegative absolute moment, the support bounds are automatic. At N=0 the support is finite because each summand is at least one. At N>0, every root above epsilon contributes at least \(\epsilon^N\), and every single root contributes at least \(|\alpha|^N\). This gives both inequalities in (A13). A negative moment alone would permit unbounded support, as in the report's explicit example, so the nonnegative convention is necessary for this particular automatic implication.

## 6. Actual normalized-trace application and its limit

The F26 binomial expansion has support
\(\{1,q^{-2},q^{-3},\ldots\}\), with the coefficient 24 at one and the nonzero integer coefficients
\(16(-1)^j\binom{j+3}{3}\) at \(q^{-j-2}\). Its stated first absolute moment is correct, by the generating function \(\sum_{j\ge0}\binom{j+3}{3}x^j=(1-x)^{-4}\). Hence it is admissible and has outer radius one.

The reciprocal support for any fixed nonzero factor is unbounded. With the same nonzero integer coefficients it has no absolute moment of nonnegative index, since its individual terms fail to tend to zero. The completion therefore permits this scalar upper-radius behavior but cannot retain bounded visible reciprocal duality for the same trace.

This is a precise restriction on an ordinary countable discrete completion. It does not assert the path/output hypotheses for an actual geometric model, does not exclude regularized or non-atomic traces, and does not identify formal quantum-parameter substitution with fixed geometric Frobenius. Those qualifications are all present in the report.

## Check event

Suggested identifier: F32-COUNTABLE-THETA-FRESH.

Scope: complete read and fresh proof check of the stated report; independent outer-circle/Cesàro proof of Lemma A; exact check of finite product grouping, signed even-power survival, moment conventions, reciprocal finiteness and the F26 series. Verdict: PASS. No formal-kernel verification or final-fragment review is claimed.


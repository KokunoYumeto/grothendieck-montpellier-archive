# DP42: independent complete mixed-line radius review

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Actual review interval **02:23:43–02:25:47 UTC**. Event **ABA-CE41**. No main-paper edits.

## Outcome

**PASS.** I read the complete saved memo, all §§1–10, and independently checked the exact coefficient congruence, arbitrary primitive-vector reduction, restricted-p chain length, multiplier lemma, both radius endpoints, and the factorial liminf. No mathematical correction was required.

The theorem proves the stated exact threshold for the fixed invariant primitive Poincaré splitting along every logarithmic line with primitive scalar and dual projections in the specified unramified lattices, including every integral prefactor with nonzero restriction. In particular the best factorial slope in this family is \(1/(p^2-1)\). It does not supply the identification of a geometric theta expression or selected harmonic value with this kernel/path family.

## 1. Weight interval and all strict inequalities

For \(k=h-j\), the interval endpoints give

\[
\frac{s}{p^k+1}\le\delta=s-w\le\frac{2s}{p^k+1},
\qquad
\tau=(p^k+1)w-S_k\in[0,s].
\]

I checked the strict inequality \(\delta<p^j\rho_h\), including p=3 where \(2s=1\). It implies every dual coordinate weight strictly dominates its known contraction weight. The lower endpoint satisfies \(w\ge1/(p+1)>\rho_h\). Thus both strict cycle bounds in (PL13) hold. The smallest right-hand bound for the second is \((q-p)/(p-1)>h-1\), as claimed.

The ordinary dual arrows have exact weight defect one. The exceptional defect is

\[
p^2\omega_d-\omega_1=p+1-p^{1-j}(q-1)\delta>1.
\]

Iterating those defects makes every logarithm term of at least two arrows strictly positive after its denominator is removed. The line's nonlinear logarithm terms are also strictly positive. Consequently the contracted reduction is precisely the triangular additive map in (PL15), with coefficients exactly one on its surviving arrows because the scales use a common root \(\pi^e=p\).

## 2. Arbitrary primitive-vector input

The coordinate input at index i has valuation \(v(v_i)+w-\omega_i\). For \(i>j\) the weight difference is positive. For \(i<j\), the unramified assumption gives \(v(v_i)\ge1\), while \(0<\omega_i-w<s<1\). Thus these coefficients are also strictly positive. Only the first unit index j survives reduction.

The integral inverse of the triangular map gives the stated chain

\[
0\ (i<j),\qquad
(-1)^{i-j}\bar v_j^{p^{i-j}}T^{p^{i-j}}\ (i\ge j).
\]

This proves the reduction for the entire inverse map and primitive vector, rather than just for a single coordinate axis. The use of an unramified lattice is genuine: a nonunit coefficient over a ramified base need not have valuation at least one, so the proof does not silently cover that case.

## 3. The unique initial monomial

Starting with the already checked full DP41 formula, I recomputed the first-family baseline and obtained exactly

\[
A_1-1-\tau=\delta(p^k-p+1-p^{1-j}).
\]

It is strictly positive: for k=1, h>2 forces j>1; for k>1 the p-power difference is already positive. This is a necessary use of h≥3. The baselines increase with i, and every positive n or l in (PL19) increases the valuation strictly.

For the product family, its baseline excess is

\[
\frac{p^{h-i}-1}{p-1}-(h-i),
\]

which vanishes exactly at i=d. Every higher line or cycle index gives strictly positive excess by (PL13). Therefore the sole term at valuation \(\tau\) is \(+SY_d^p/p\). No cancellation between the two displayed families can remove it.

Composing the resulting integral normalized series with the integral contracted inverse maps has nonzero reduction

\[
(-1)^{k-1}\bar u\bar v_j^{p^k}T^{p^k+1}.
\]

Its derivative is nonzero in residue characteristic p. This checks the complete initial form after restriction, which is essential for the exponential obstruction.

## 4. Exact congruence, including its original coefficient ring

The scaling identity is exact, not just a valuation identity:

\[
\mu=\frac{\alpha_0\alpha_d^p}{p}
=\frac{\gamma^{p^k+1}}{p^{S_k}},
\]

because \(p\omega_d-1-p^kw=-S_k\) and all scales are powers of the same \(\pi\). Hence the normalized coefficient of \(T^{p^k+1}\) is exactly \(p^{S_k}[t^{p^k+1}]\beta(ut,\mathbf vt)\).

The reduction initially occurs in the ramified extension used to express rational weights. This coefficient and the proposed unit residue expression both belong to the original unramified field. Their difference has positive valuation there, hence integer valuation at least one. Thus the stated congruence is genuinely modulo p in the original ring, not merely modulo the auxiliary uniformizer. Its unit right-hand side proves the exact valuation \(-S_k\).

## 5. Multiplier, radius endpoints, and liminf

The fraction-field multiplier proof agrees with the complete lemma independently proved in `DP41_bounded_multiplier_lemma.md`. The bounded-series Gauss valuation extends to its fraction field with residue field \(\operatorname{Frac}(k[[T]])\). If a nonzero bounded f cleared the exponential, the reduction of \(E^p=\exp(pz)\) would give \(\bar E=1\); both binomial cases contradict the initial derivative. The proof requires neither a unit constant coefficient nor a primitive leading term of f.

For each weight in the half-open interval \([w_k^-,w_k)\), the logarithmic restriction has minimum \(\tau\in[0,s)\), so this lemma applies. The prefactor is integral after contraction by the full inverse-map calculation and is nonzero by assumption. Monotonicity then supplies all smaller nonnegative weights.

At the endpoint \(w_k\), the logarithmic minimum is exactly s. The factorial estimate gives an integral exponential with constant term one. Gauss multiplicativity gives the exact equality \(\nu_{w_k}(\Theta)=\nu_{w_k}(V)\), which is finite and nonnegative. At greater weights, monotonicity retains boundedness and the exponential minimum remains zero, so the same equality holds. This carefully distinguishes a nonzero prefactor from a unit prefactor: only the latter is asserted to have finite minimum zero.

The finite endpoint gives \(v(a_n)\ge-w_kn\). A strictly larger coefficient liminf would produce a bounded weighted norm at some rational weight below \(w_k\), contradicting the proved unboundedness. Therefore the coefficient liminf is exactly \(-w_k\). Adding Legendre's factorial valuation gives the stated exact factorial liminf and coefficientwise lower bound. Zero coefficients assigned valuation infinity cause no difficulty, and the negative-infinity alternative forces infinitely many nonzero coefficients.

## 6. Restricted p-power length and scope

The source degree-p translation coefficient gives \(D_i^p\) equal modulo p to a nonzero scalar multiple of \(D_{i+1}\) for i<d, while \(D_d^p\equiv0\). The invariant directions commute, so the restricted p-map is additive and Frobenius-semilinear on constant combinations. A first nonzero component at j survives through the (k−1)st restricted power and dies at the kth; later components cannot cancel the surviving last component. Thus k has the stated intrinsic meaning, independent of the coordinate description of its first nonzero entry.

The function \(s/(p^k+1)\) is maximized exactly at k=1, giving \(1/(p^2-1)\). The theorem correctly excludes h=2, nonprimitive or zero projections, a nonunit exponential scalar, other rational gauges and selected harmonic operators. It supplies no identification of a global theta normalization or numerical global cost.

## Exact checked version

| Scope | SHA-256 |
|---|---|
| Complete memo, all §§1–10 | `e172a02e92074d66c4dbe3381eac5ba445f735060b1a87278168fa00d2eec0e7` |
| Complete statement and proofs, §§1–9 | `f7515953253c8f345e07855307f77c204b786608300c66db5832fbee79cce183` |

The snapshot and metadata are `late_proof_snapshots/DP42_complete_checked.md` and `DP42_check_metadata.json`. The proof-scope hash begins at `## 1. Statement` and ends immediately before `## 10. Scope`, preserving whitespace. This is an independent manual whole-proof review; it does not certify a later integrated block or claim machine formalization.

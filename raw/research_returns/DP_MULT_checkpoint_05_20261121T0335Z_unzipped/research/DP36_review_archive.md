# DP36: independent whole-proof review

Reviewer: `/root/archive_binomial`, GPT-6 Astra Pro, inherited model; runtime reasoning effort not exposed. Date: 2026-11-21 UTC. Review interval: **01:33:56--01:36:15 UTC**. Event: **ABA-CE30**. No main-paper edits were made by this reviewer.

## Result and actual scope

**PASS. The complete draft proves the stated sufficient analytic implication from its explicit hypotheses.** I read the whole statement, hypotheses, proof sections 2--4 and scope discussion in section 5, then read the exact saved version again. I challenged the torus actions with duplicated variables, all inverse substitutions, the boundary logarithm estimate, the vector binomial extraction, the change of weights, the factorial normalization and the selected one-variable path. No mathematical correction or counterexample was found.

This is a review of the exact draft `actual_dual_kernel_weights_DP36.md`, using the inverse bounds already proved in DP2 and DP32. It is not an independent construction of a geometric theta section, a check of a particular geometric cocycle against the hypotheses, or certification of a later edited integration.

## 1. Torus characters and quantized positive degree

For a nonzero coefficient of a torus-invariant monomial, the exact character condition is

\[
a-\sum_i p^i b_i\equiv0\pmod{q-1}.
\]

The identity

\[
r_0a+\sum_i r_i b_i
=\rho\Bigl(a-\sum_i p^i b_i\Bigr)+s|b|
\in s\mathbf Z
\]

is correct. The first term is an integer and hence a multiple of $s=1/(p-1)$. Every coordinate weight is positive, so every nonconstant invariant monomial has weighted degree at least $s$. This inference concerns the monomial degree before its coefficient valuation; the proof correctly keeps those two quantities separate when it later increases the weights.

Duplicating $x$ gives both copies the same character and weight, so their exponents enter the same sum. Duplicating the $y$ vector gives each paired coordinate the same character and weight, so again the summed exponents give the identical quantization. No separate, independent torus action on the two copies is assumed.

The Honda logarithm commutes with the indicated Teichmüller multiplication. For the actual-dual model, the monomial cycle commutes with the diagonal characters from DP32/DP34; replacing the primitive root by its inverse gives the negative powers in this hypothesis. The inverse maps and formal laws therefore commute with these actions too. Since the addition coboundaries are taken in additive coordinates, they inherit the simultaneous torus symmetry. Thus the original-coordinate integral series $C_X-1$ and $C_Y-1$ indeed have weight at least $s$.

The claimed redundancy of the no-bidegree-$(1,1)$ hypothesis is also correct: $1-p^i$ is nonzero modulo $q-1$ for every $1\le i<h$. Keeping that hypothesis explicit causes no problem.

## 2. Inverse substitution and the logarithm threshold

The bounds $w_r(E_0)\ge r_0$ and $w_r(E_{H,i})\ge r_i$ are exactly the component bounds established by the preceding inverse constructions. A monomial of the original-coordinate coboundary has its coefficient valuation plus the sum of its source weights; substituting the corresponding inverses cannot decrease that quantity. The repeated variables have the repeated weights, so the same reasoning applies to both coboundaries.

After substitution, the logarithm is **exactly** the addition coboundary of $\beta$ in additive variables, because logarithm and exponential are inverse formal series over $K$, and $L_0E_0$ and $L_HE_H$ are identity maps. In particular, the later coefficient extraction is not being attempted before an uncontrolled nonlinear change of variables.

The boundary threshold $s$, without a strict inequality, is sufficient for the formal logarithm. For every $m\ge1$,

\[
ms-v_p(m)\ge s,
\]

because $p^{v_p(m)}\le m$ and $p^e-1\ge e(p-1)$. Equality can occur; it creates no convergence problem. The series under the logarithm is $1$ plus a series of positive ordinary degree, so each coefficient uses only finitely many logarithm terms. No weighted analytic convergence is implicitly required. This yields both claimed lower bounds for the additive coboundaries.

## 3. Unique binomial extraction in all cases

For an integer $a\ge2$ that is not a power of $p$, a nonzero base-$p$ digit supplies an exponent $j=p^e<a$ with $\binom aj$ nonzero modulo $p$. If $a=p^e$, the chosen interior exponent $p^{e-1}$ gives valuation exactly one. One direct verification is

\[
\binom{p^e}{p^{e-1}}
=p\binom{p^e-1}{p^{e-1}-1},
\]

whose second factor is a unit modulo $p$. Thus the stated valuation-at-most-one claim covers every $a\ge2$.

When the $x$-degree is one, the hypothesis leaves total $y$-degree at least two. If two or more components of the $y$ multiindex are positive, putting one whole component in the first vector and the remaining components in the second gives a genuinely interior split and multiplier one. If there is only one positive component, the preceding one-variable argument applies.

Each selected coefficient has exactly one source coefficient of $\beta$: recombining the two split multiindices recovers the original multiindex, while all unsplit exponents are fixed. The endpoint terms subtracted in the coboundary do not contribute to this interior split. Hence there is no hidden cancellation with another monomial. The split preserves weighted degree, and the multiplier loses at most one unit of valuation. This proves $w_r(\beta)\ge s-1$ coefficient by coefficient.

## 4. Increasing the weights and extracting factorial coefficients

Every nonzero monomial of $\beta$ has unvalued weighted degree at least $s$, by its exact torus invariance. Multiplying all coordinate weights by $p$ therefore adds at least $(p-1)s=1$ to its coefficient weight. Combining this fact with the previously proved lower bound gives $w_{pr}(\beta)\ge s$. This step does not assume that the coefficients of $\beta$ are integral.

Since $p$ is odd, $\sigma/2$ is a unit in the base ring. Formal exponentiation has nonnegative weight because

\[
ms-v_p(m!)=s\,s_p(m)\ge0
\]

for $m\ge0$. Again ordinary positive degree makes the coefficientwise formal calculation finite. The integral factor $U(E_0,E_H)$ has nonnegative weight already at $r$, and raising the positive coordinate weights preserves that lower bound. The product consequently satisfies exactly the coefficient estimate displayed in the draft.

Adding the valuation of the **multiindex factorial** gives $\gamma_j=s-pr_j$. The simplifications

\[
\gamma_0=s-p\rho,\qquad
\gamma_i=p^{i+1}\rho-1
\]

are correct. For $i<d$ the latter number is negative; for $i=d$ it is $\rho>0$. A negative sufficient lower bound is not a claim that the coefficient attains a negative valuation. The statement expressly preserves that distinction.

## 5. The selected diagonal path

The exact identity

\[
r_d=\rho\frac{p^{h-1}-1}{p-1}
\]

gives $r_d\ge r_0$, with equality precisely at height two. Giving $t$ weight $pr_d$ therefore makes the substitutions $x=t$ and $y_d=\varepsilon t$ satisfy both of their required lower weights. The unit $\varepsilon$ contributes no valuation, and the remaining coordinates are set to zero, so they create no constraint. At each degree only finitely many monomials survive the path substitution.

The resulting one-variable coefficient is bounded below by $-pr_dn$. The final factorial is now **$n!$**, not a product of multiindex factorials; applying its exact digit-sum valuation gives

\[
v_p\bigl(n![t^n]\Theta(t,0,\ldots,0,\varepsilon t)\bigr)
\ge (s-pr_d)n-\frac{s_p(n)}{p-1}
=\rho n-\frac{s_p(n)}{p-1}.
\]

This proves the path estimate with the stated normalization, including $n=0$. At $h=2$, the two original coordinate weights coincide and both factorial slopes equal $\rho$, as claimed.

## 6. Limits retained

The result is a sufficient implication from explicit hypotheses on a formal series for the actual line and its actual dual. It does not establish that the prescribed normalized Poincaré/theta expression satisfies these hypotheses, including the exact torus equivariance and integral coboundaries. Nor does it identify the selected path with the source's geometric path or frame normalization.

There is no witness proving optimality of this kernel estimate. In particular the decreasing residual $\rho$ is a lower-bound coefficient and provides no upper bound on actual geometric gain. It cannot by itself rule out a sharper estimate, differently weighted construction or shorter chain. The final section of the draft states these limits correctly.

## Exact reviewed version

The whole reviewed file is preserved as `late_proof_snapshots/DP36_draft_checked.md` (7,754 bytes). Hashes preserve the exact original UTF-8 bytes and intervening whitespace.

| Scope | SHA-256 |
|---|---|
| Entire draft | `a739cc12ef17d53f2befdd33f4a6e4ccb595ec923ffe6a9838ea4844a8ca32dd` |
| Statement and hypotheses, §1 | `d187484c246049d113845e31f9dbfc056c59fce036844aa0c3ef56f42a95afbd` |
| Complete proof and scope, §§2--5 | `c538cd809159187a85aaa34abb17e1f2f5b55370cc2268524a7fc7bb31d8e055` |

The section hashes begin at their respective Markdown headings and stop immediately before the next excluded heading: §1 stops before §2; §§2--5 stop before `## Check status`. Actual event **ABA-CE30** is recorded in both reviewer logs. No prospective review is counted as completed.

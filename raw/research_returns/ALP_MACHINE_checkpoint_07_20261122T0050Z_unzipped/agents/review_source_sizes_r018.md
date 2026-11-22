# Independent review of the numerical Sizes component in AM-R-018

Reviewer: /root/kummer_extension, GPT-6 Astra Pro; inherited effort not separately exposed. 22 November2026UTC.

**Result: PASS after the literal spread correction.** The reviewer independently whole-read the completed parent file selected_fixed_prime_size_intervals.md and its exact certificate, reconstructed the argument from the literal source, and replayed the certificate. The complete R018 numerical Sizes argument and its scope are sound. R017's separate prime certificate is not repeated here.

## Literal source and correction

In Formalism/LocalRingCardinality/DataCoeff.lean:34–35,
\[
 \operatorname{spread}(w)=w_0-w_{N-1}+N\qquad(N>0).
\]
Thus a calculation of the first-minus-last difference alone is insufficient. The source Sizes record has exactly the four clauses g_big, T_gt, a_gt, spread_le at Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean:486–494. The shift defining lamTrue is at464–465; the actual recurrences are BaseLemmas.lean:496–530.

The initially proposed three differences omitted the added ranks. Before any promotion, the correction was communicated to the parent and accepted. The corrected literal spreads are proved below.

## Independent derivation of all extrema

Write \(d=t+1\), \(m=2\), and use the fixed K031/K032 baseline
\[
 u_i=(2(k-i)+1)C+\tfrac12,\qquad e_0=0,\quad e_1=4C.
\]
The source starting weight and exact recurrence give
\[
 \begin{aligned}
 w_{0,i}&=(2k-2i+1)C+1-\tfrac k2+i,\\
 w_1&=(w_0-\tfrac d2,\;(\tfrac k2)^d),\\
 w_2&=(w_1-\tfrac d2,\;(-4C+\tfrac{k+d}{2})^d).
 \end{aligned}
\]
Here exponent d denotes repeated entries. The initial consecutive differences are \(2C-1>0\). Its endpoints are
\[
  w_{0,0}=(2k+1)C+1-\tfrac k2,\qquad
  w_{0,k-1}=3C+\tfrac k2.
 \]
At stage1 the appended constant \(k/2\) is the minimum, because the last old entry exceeds it by \(3C-d/2>0\). At stage2 the appended constant \(-4C+(k+d)/2\) is the minimum, because the previous minimum after shifting exceeds it by \(4C-d>0\). The first original entry remains the maximum at every stage. These inequalities hold with the explicit positive margins of both baselines.

Adding the actual rank \(N_j=k+jd\) to each first-minus-last difference yields
\[
 \boxed{
 S_0=2(k-1)C+1,\qquad
 S_1=(2k+1)C+1+\tfrac d2,\qquad
 S_2=(2k+5)C+1+\tfrac d2.}
 \tag{RV1}
\]
In particular \(S_1-S_0=3C+d/2>0\) and \(S_2-S_1=4C>0\).

If \(u_0\) is increased by any \(n\ge0\), only the first entry in every \(w_j\) changes, by n. No minimum changes. The spread at each of the three stages therefore increases by exactly n. K033 raises \(u_0\) by \(11^r\) and \(121\,11^r\) at its two specified CM labels, uniformly across all words. The exact maximum over all words, places and \(j\le2\) is consequently
\[
                       S_2+121\,11^r.
\tag{RV2}
\]
Choosing
\[
                a_r=\left\lceil\frac{S_2+121\,11^r}{2}\right\rceil
\tag{RV3}
\]
is the least integer size satisfying spread_le.

## All four Sizes clauses and exact finite ranges

The exact baseline numbers are

| Host | \(S_0\) | \(S_1\) | \(S_2\) | \(N_2\) |
|---|---:|---:|---:|---:|
| J14 |3,702,796,042,027|3,838,264,190,786|4,018,888,387,958|3562|
| J56 |13,537,133,455,459|13,658,724,475,337|13,820,845,834,085|3436|

The g_big inequalities are the unchanged K031/K032 comparisons \(2fk<g_i-1\). At r=0, \(4a_r\) is respectively 8,037,776,776,160 and 27,641,691,668,412, whereas \(2fN_2+1\) is respectively299,209 and1,154,497. Thus a_gt holds at0 and hence for every larger r. Formula(RV2) proves spread_le.

For the exact T-primes of R017, integer comparison of \(4a_r<T\) gives exactly
\[
     0\le r\le55\quad\text{for J14},\qquad
     0\le r\le90\quad\text{for J56}.
\tag{RV4}
\]
The certificate compares every r through the first failure, and records the full endpoint integers. These tests also have a direct proof of completeness: \(a_r\) increases with r. At r=56 and91, respectively, even \(2(S_2+121\,11^r)\ge T\). Hence no real size parameter, including a nonintegral one smaller than the ceiling, can satisfy both spread_le and T_gt at that next exponent or any larger one.

The same fixed T can be used for all words here: the literal Primes.Ok clauses at AbelianHostFieldConditions.lean:224–236 require T-primality, the stated norms/congruences and T distinct from g_i, but contain no injectivity condition on the word-indexed map T. This observation does not repair piT_Kq, which remains the known field obstruction.

Consequently all four numerical Sizes clauses are verified on(RV4). This is not a proof of full SizeData2, a fixed-T unbounded family, the unchanged Fields.Kq constructor, or a MainX every-epsilon window.

## Finite sharpness visible inside these ranges

This optional arithmetic consequence retains only the raw selected local content normalization. Let \(\mathfrak I_r\) be K033's selected ideal, or K034's auxiliary ideal when its coefficient content is a unit. With the actual constants \(D_0,c_0,K_0\) already recorded there, their proved bounds at the final exponents imply
\[
 \begin{aligned}
 r=55,\ J14:\quad&
 \frac1{1220}-4\cdot10^{-54}
 <\frac{v(\mathfrak I_r)}{T_r}
 <\frac1{1220}+2\cdot10^{-45},\\
 r=90,\ J56:\quad&
 \frac1{1220}-10^{-88}
 <\frac{v(\mathfrak I_r)}{T_r}
 <\frac1{1220}+3\cdot10^{-80}.
 \end{aligned}
\tag{RV5}
\]
These inequalities follow by dividing the exact constant-error sandwich by \(T_r=122\,11^r+D_0\); the companion certificate uses rational arithmetic. They do not include target metric, source class, finite norm, or archimedean Schwartz normalization. In particular the full archimedean factorial cost and any later-image restrictions remain separate.

## Recorded check

The executable review_source_sizes_r018_certificate.py independently constructs the complete lamTrue arrays by the source recurrence for representative nonnegative first-entry increments, checks their dominance and all three literal spread identities, checks all four numerical inequalities for every exponent in(RV4), and verifies the first impossible exponent. Its T inputs are the actual parent R017 integers; it does not run or claim another primality proof. No Lean build was performed.

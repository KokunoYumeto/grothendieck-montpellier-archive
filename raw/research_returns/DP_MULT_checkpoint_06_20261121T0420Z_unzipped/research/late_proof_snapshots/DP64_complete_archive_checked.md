# DP64 — Every fixed cyclotomic CM type has the same leading bare budget

Author: `/root`, GPT-6 Astra Pro; reasoning effort not exposed by the runtime. This is a new deduction from the checked cyclic-display formulas DP40/43 and a known fixed-modulus prime-sum theorem. It is not a theorem about normalized theta-selected values.

## 1. Exact statement

Fix an integer m and a CM subfield E of Q(zeta_m). Let G=Gal(E/Q), let Omega=Hom(E,C), and let Phi be a CM type. Thus |Omega|=2g, |Phi|=g, and the action of G on Omega is simply transitive. Let S be a fixed finite set of primes containing the divisors of m. For p outside S let sigma_p be the restriction to E of zeta_m -> zeta_m^p. The group is abelian, so this element does not depend on a choice of a prime over p.

For i in Phi define

\[
 c_{i,p}=\sum_{r\ge1}{\mathbf1_{\sigma_p^r i\notin\Phi}\over p^r},
 \qquad
 E_{i,p}(n)=\sum_{r\ge1}\mathbf1_{\sigma_p^r i\notin\Phi}
                 \left\lfloor {n\over p^r}\right\rfloor.
 \tag{CB1}
\]

The second sum is finite. These are the directional slope and the integer lower certificate of DP40/43 for the corresponding cyclic rank-one CM display. On an entirely selected orbit both expressions are zero. The theorem below is an arithmetic theorem about these explicitly defined quantities; applying them to a geometric family requires the integral display and the fixed global primitive eigendirections, as in DP45/49/53.

For arbitrary nonnegative integers n_i, fixed as p varies, put N=sum_i n_i. For all X>=2,

\[
 \sum_{\substack{p\le X\\p\notin S}}\log p\sum_{i\in\Phi}n_i c_{i,p}
     ={N\over2}\log X+O_{m,S}(N).
 \tag{CB2}
\]

More precisely, the integer certificate satisfies the uniformly saturated formula

\[
 \sum_{\substack{p\le X\\p\notin S}}\log p\sum_{i\in\Phi}E_{i,p}(n_i)
   ={1\over2}\sum_{i\in\Phi}n_i
       \log\!\bigl(\max\{1,\min(X,n_i)\}\bigr)+O_{m,S}(N).
 \tag{CB3}
\]

The constants are uniform in the type, the direction labels, the derivative orders and X when m and S are fixed. Consequently two such type/direction data with the same multiset of orders have integer-budget difference O(N), uniformly in X. The fields can differ inside the same fixed cyclotomic field. Their linear budgets also differ by O(N).

If the number of directions d is fixed and only the total N is held fixed, the difference of the integer budgets for arbitrary partitions of N among at most d directions is O_{m,S,d}(N): equivalently,

\[
 \sum_{p\le X,p\notin S}\log p\sum_iE_{i,p}(n_i)
 = {N\over2}\log\!\bigl(\max\{1,\min(X,N)\}\bigr)
   +O_{m,S,d}(N).
 \tag{CB4}
\]

There is no uniformity in a growing conductor m, growing exceptional set S or growing number of directions d asserted here. The orders may vary with an outer parameter, provided they remain fixed throughout each prime sum.

## 2. The exact known analytic input

Zeév Rudnick, *Primes in Arithmetic Progressions: Fixed Modulus*, May 26, 2015, §2, printed p.2, equation (1), gives for fixed m and (a,m)=1:

\[
 \sum_{p\le Y,\ p\equiv a\ (m)}{\log p\over p}
       ={1\over\varphi(m)}\log Y+O_m(1).
 \tag{CB5}
\]

The preceding paragraph states quantitative fixed-modulus PNT. It also gives theta(Y)=sum_{p<=Y}log p=O(Y). These known analytic facts are cited, not reproved. The root directly reopened and read this exact page in this pass, including its fixed-modulus qualification. Primary URL:

https://www.math.tau.ac.il/~rudnick/courses/sieves2015/fixed%20progressions.pdf

No RH premise is needed. The constants below are allowed to depend on this fixed modulus.

## 3. The first coefficient has mean one half

For a unit residue a modulo m set

\[
 b_i(a)=\mathbf1_{(\sigma_a i)\notin\Phi}.
\]

Restriction from Gal(Q(zeta_m)/Q) to G is surjective. Its fibres have equal size, because it is a surjective homomorphism of finite groups. The map G -> Omega, sigma -> sigma i, is bijective. Exactly g of the 2g targets lie outside Phi. Thus

\[
 {1\over\varphi(m)}\sum_{a\in(\mathbf Z/m)^\times}b_i(a)={1\over2}.
 \tag{CB6}
\]

Applying (CB5) in the finitely many classes and omitting S gives

\[
 \sum_{p\le Y,p\notin S}b_i(p){\log p\over p}
       ={1\over2}\log Y+O_{m,S}(1).
 \tag{CB7}
\]

Uniformity in i and Phi follows without an extra geometric assertion: every b_i(a) is either zero or one, so the sum of the absolute class errors is bounded by the same finite sum of the class constants. There are no class-function issues here because G is abelian and sigma_p is specified by the actual residue class.

For the tail of (CB1),

\[
 0\le c_{i,p}-{b_i(p)\over p}
       \le\sum_{r\ge2}p^{-r}={1\over p(p-1)}.
 \tag{CB8}
\]

The series sum_p log p/[p(p-1)] converges by comparison with sum_{n>=2}log n/(n(n-1)). Combining (CB7) and (CB8), then multiplying by n_i and adding, proves (CB2). This includes completely selected orbits, which contribute zero, and all partially selected cyclic patterns.

## 4. Rounding and saturation at every order

Fix i and write n=n_i. If n=0 or 1, every floor vanishes and the proposed main term is zero. Suppose n>=2 and put Y=min(X,n). The first-power contribution is

\[
 \begin{aligned}
 \sum_{p\le Y,p\notin S} b_i(p)\left\lfloor{n\over p}\right\rfloor\log p
 &= n\sum_{p\le Y,p\notin S}b_i(p){\log p\over p}
       +O\!\left(\sum_{p\le Y}\log p\right)\\
 &= {n\over2}\log Y+O_{m,S}(n).
 \end{aligned}
 \tag{CB9}
\]

The floor error is bounded by one for each prime, and theta(Y)=O(Y)=O(n). The entire higher-power contribution is nonnegative and at most

\[
 n\sum_p\log p\sum_{r\ge2}p^{-r}=O(n).
 \tag{CB10}
\]

This proves (CB3) for one direction and then for all directions after addition. No claim that a fixed-order floor sum grows indefinitely with X is made: its main term saturates at X=n for each direction, exactly as the finite sums do. Subtracting (CB3) for the same order multiset proves the stated difference estimate.

## 5. Unequal distributions of a fixed total order

Assume N>0 and let I be the set of positive n_i, of size at most d. Put L=min(X,N), which is at least one. Since n_i<=N, each log(min(X,n_i)) is at most log L. Moreover,

\[
 0\le\log L-\log\min(X,n_i)\le\log(N/n_i).
 \tag{CB11}
\]

To check the upper inequality, if X<=n_i both left terms equal log X. If n_i<X, the difference is log(L/n_i), and L<=N. Thus

\[
 0\le N\log L-\sum_{i\in I}n_i\log\min(X,n_i)
       \le N\sum_{i\in I}w_i\log(1/w_i)\le N\log d,
 \tag{CB12}
\]

where w_i=n_i/N. The last inequality follows from concavity of log:

sum_i w_i log(1/w_i) <= log(sum_i w_i/w_i)=log|I|<=log d.

For N=0 every term is zero. Formula (CB4) now follows from (CB3); this proves its uniformity and the exact dependence on the number of directions. It does not identify the total derivative order N with an automorphic cost parameter.

## 6. What the theorem closes, and what it does not

For a fixed cyclotomic CM field and integral cyclic models, passing to another CM type or redistributing a fixed total order among finitely many globally fixed primitive directions cannot increase the leading bare certificate. It changes the full integer prime budget by O(N), including rounding and saturation. This extends the particular mod7 calculation of DP53 and closes the corresponding alternative in every fixed cyclotomic modulus.

It remains a lower-certificate comparison. It is not an upper bound on a selected theta value or a global LinkG gain, and an O(N) change may matter after leading terms cancel. Neither source normalization nor theta-image nonvanishing is supplied by the prime theorem. Changing the conductor with N requires quantitative constants absent here.

Prime-dependent selection is a different operation. The theorem explicitly fixes the n_i during the prime sum. For Phi={1,2,3} in (Z/7)^times, the maximum over i in Phi of 1_(a i outside Phi) equals zero for a=1 and one for each of the other five classes: the five products aPhi are respectively {2,4,6}, {2,3,6}, {1,4,5}, {1,3,5}, {4,5,6}. Thus its class mean is 5/6, not 1/2. This is a finite set calculation, not an arithmetic construction of a free varying direction. A global object realizing these varying local choices and its cost must be analyzed separately.

Nonabelian and reflex-field prime sampling also remain outside the stated arithmetic hypotheses. The proof relies on the actual fixed-modulus residue distribution, not only an abstract group average.

## 7. Proof status

Author whole-proof reading and independent challenge are to be recorded only after they occur. The analytical and finite-set proofs above are complete drafts; no software or Lean certificate is asserted.

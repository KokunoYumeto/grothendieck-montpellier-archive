# K17-BERNOULLI-9496386083 — one exact residue

Date: 2026-11-21. Author: /root/vandiver_k, GPT-6 Astra Pro.
Effort: not exposed. Run: K17.
Status: complete self-check and independent root/archive whole-code
checks; root's different-generator replay completed with the same residue.
The present author read that complete independent program and report.
Reflection and the
class-group/K-group comparison are separate inputs and are not asserted
by this numerical certificate.

## 1. Statement

With \(p=9496386083\) and \(n=p-11=9496386072\), the Bernoulli number in
the convention \(B_1=-1/2\) satisfies

\[
 B_n\equiv 3753150554\ne0\pmod p.
\]

The complete standard C++17 program is
work/hecke_general/bernoulli_9496386083.cpp. Its actual output is
bernoulli_9496386083.json, with a final checkpoint alongside it.
It enumerates exactly 4,748,193,041 half-orbit terms in constant memory.
The completed run took 20.652811385 seconds in this workspace.

## 2. Congruence derived without a large Bernoulli table

For \(0\le m\le p-2\), the Bernoulli recurrence

\[
 \sum_{j=0}^{m}\binom{m+1}{j}B_j=0 \qquad(m\ge1)
\]

proves inductively that \(B_m\) is \(p\)-integral: the coefficient
of \(B_m\) is \(m+1\), a unit modulo \(p\).
For \(2\le n\le p-3\), Faulhaber's identity therefore gives

\[
 T_n:=\sum_{a=1}^{p-1}a^n\equiv pB_n\pmod {p^2}.
\]

For an integer \(g\) prime to \(p\), write
\(ga=r_a+pq_a\), where \(1\le r_a\le p-1\) and
\(q_a=\lfloor ga/p\rfloor\).
The \(r_a\) permute the nonzero residues. Expanding modulo \(p^2\) gives

\[
 T_n=\sum r_a^n
 \equiv g^nT_n-np g^{n-1}
       \sum_{a=1}^{p-1}q_a a^{n-1}\pmod {p^2}.
\]

Thus, whenever \(g^n\not\equiv1\pmod p\),

\[
 B_n\equiv
 \frac{n g^{n-1}}{g^n-1}
 \sum_{a=1}^{p-1}\left\lfloor\frac{ga}{p}\right\rfloor
 a^{n-1}\pmod p. \tag{B1}
\]

This is the precise Voronoi-type congruence used; its factor and sign
have been derived here rather than inferred from another convention.
As an implementation check, before the large run the formula was
compared with exact rational Bernoulli numbers for every even
\(2\le n\le p-3\) at each prime \(13\le p<80\); all comparisons passed.
That small check supports implementation only; (B1) is proved above.

## 3. Primitive-root and half-orbit reduction

The program proves primality by exhaustive trial division and verifies

\[
 p-1=2\cdot17\cdot293\cdot953261.
\]

It proves primality of these four factors and verifies
\(2^{(p-1)/q}\ne1\pmod p\) for each of them, as well as
\(2^{p-1}=1\). Hence 2 has exact order \(p-1\).

Set \(h=(p-1)/2\), \(a_i=2^i\bmod p\), chosen in \(\{1,\ldots,p-1\}\).
The first \(h\) powers give exactly one representative of each pair
\(\{a,-a\}\), because \(2^h=-1\).
Our exponent \(n\) is even, so \(n-1\) is odd. For \(g=2\),
\(q_a=\lfloor2a/p\rfloor\) is zero or one and \(q_{p-a}=1-q_a\).
The two summands in a signed pair combine to

\[
 q_a a^{n-1}+q_{p-a}(p-a)^{n-1}
 =(2q_a-1)a^{n-1}.
\]

Consequently the complete sum in (B1) is

\[
 S=\sum_{i=0}^{h-1}
   \left(2\left\lfloor\frac{2a_i}{p}\right\rfloor-1\right)w_i,
 \qquad w_i=a_i^{n-1}=a_i^{-11}.
 \tag{B2}
\]

The state is updated by \(a_{i+1}=2a_i\bmod p\) and
\(w_{i+1}=c w_i\bmod p\), where

\[
 c=2^{-11}=2916614671\pmod p.
\]

The factor in (B1) simplifies, using \(n\equiv-11\pmod p\), to

\[
 \frac{n\,2^{n-1}}{2^n-1}
 =\frac{(-11)2^{-11}}{2^{-10}-1}
 =\frac{11}{2046}
 =5565086468\pmod p.
 \tag{B3}
\]

The denominator is nonzero. The program independently calculates the
unsimplified factor and asserts its equality to \(11/2046\).

## 4. Exact arithmetic and overflow bounds

The loop uses Montgomery residues with radix \(R_0=2^{64}\).
The stored value of \(x\) is \(xR_0\bmod p\). Put
\(v=-p^{-1}\bmod R_0\). For \(0\le a,b<p\), it computes

\[
 t=ab,\quad m=(t\bmod R_0)v\bmod R_0,\quad
 u=(t+mp)/R_0.
\]

By construction the numerator is divisible by \(R_0\), and
\(u\equiv abR_0^{-1}\pmod p\). Also \(0\le u<2p\);
one conditional subtraction gives the least nonnegative residue.
The program uses exact unsigned 128-bit products. Since \(p<2^{34}\),
\[
 t+mp<p^2+2^{64}p<2^{100}<2^{128}.
\]
The deliberate unsigned 64-bit wrap in computing \(m\), the inverse,
and the negative inverse implements reduction modulo \(2^{64}\).
No other overflow is used. The orbit update \(2a-pq\), and each sum
update, are smaller than \(2p<2^{35}\).

The computed constants, also checked by direct modular arithmetic, are

\[
 R_0\bmod p=5348718361,\qquad
 -p^{-1}\bmod2^{64}=11207749152621910645.
\]

At iteration \(i\), the invariant is:
the variable j equals \(a_i\), w is the Montgomery encoding of
\(w_i\), and sum encodes the first \(i\) terms of (B2).
The signed addition and the Montgomery multiplication preserve it.
At the exact half-orbit endpoint, the program asserts
\(a_h=-1\) and \(w_h=-1\), independently of the accumulated sum.

Floating-point numbers occur only in elapsed-time and progress estimates;
they never enter residues, exponents, iteration counts, or comparisons.
All loop bounds and counts are 64-bit integers.

## 5. Actual completed output and scope

The exhaustive half-orbit run returned

\[
 S=4849818985,\qquad
 \frac{11S}{2046}=3753150554\pmod p,
\]

and both endpoint residues were \(p-1=9496386082\).
Every runtime assertion passed.
The output is a nonzero Bernoulli residue, without a claim to have
checked full Vandiver at this prime. The separate reflection argument
only needs this single residue and the specified character component.

The exact replay commands are:

    g++ -O3 -std=c++17 work/hecke_general/bernoulli_9496386083.cpp -o work/hecke_general/bernoulli_9496386083
    work/hecke_general/bernoulli_9496386083

The optional first argument is a smaller term count for a benchmark;
such output is explicitly labelled BENCHMARK and does not certify
the full sum. The actual result above is labelled COMPLETE.

## 6. Independent different-generator replay

Root independently wrote and executed bernoulli_root_g5.cpp, using the
primitive root 5 and ordinary unsigned 128-bit modular division instead
of Montgomery reduction. The complete code and output have been read
and reconstructed in this audit.

For general positive primitive \(g\), the pair formula is
\[
 q_{p-a}=g-1-q_a,\qquad
 q_a a^{n-1}+q_{p-a}(p-a)^{n-1}
 =(2q_a-(g-1))a^{n-1}.
\]
For \(g=5\), the coefficients lie in \(\{-4,-2,0,2,4\}\).
The program verifies primality and primitive order independently,
enumerates all 4,748,193,041 half-orbit terms, and uses the unsimplified
factor from (B1). Its complete output is
\[
 S_5=7110767128,\qquad
 \frac{n5^{n-1}}{5^n-1}=9130328994,\qquad
 B_n=3753150554\pmod p.
\]
Both endpoint states again equal \(-1\). This second run took
41.0857 seconds. Its integer products have explicit safe bounds:
the orbit update is below \(5p<2^{36}\), each signed coefficient times
a weight is below \(4p<2^{36}\), and the modular multiplication uses
an unsigned 128-bit product below \(p^2<2^{68}\).
The two implementations use different traversals, different conversion
factors, and different exact reduction methods, and agree on the final
Bernoulli residue.

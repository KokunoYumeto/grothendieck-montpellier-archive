# Negative endpoints −17, −18 and −19: exact remaining tests

**Outcome: no negative endpoint extension has been proved.** The smallest remaining exceptional prime is **151628697551**, for the component $A_p^{[34]}$. The ordinary reciprocal-power sum that admits a square-root-size polynomial method computes the opposite component's Bernoulli test. It does not settle this exceptional component. No linear scan or new Hecke calculation was started.

## Exact exceptional primes

The standard-library certificate `negative_endpoint_certificate.py` recomputes the Bernoulli numbers by their exact rational recurrence. It proves the complete numerator factorizations, including primality of every displayed factor, using trial division for the small factors and the full-factor Lucas criterion for the large ones. Its report is `negative_endpoint_certificate.json`.

| Endpoint | Required component | Exact Bernoulli number | Only exceptional prime above $2^{31}$ |
|---|---|---|---:|
| −17 | $A_p^{[34]}$ | $B_{34}=17\cdot151628697551/6$ | 151628697551 |
| −18 | $A_p^{[36]}$ | $B_{36}=-26315271553053477373/1919190$ | 26315271553053477373 |
| −19 | $A_p^{[38]}$ | $B_{38}=19\cdot154210205991661/6$ | 154210205991661 |

Each exceptional prime divides the indicated numerator exactly once. The small factors 17 and 19 are already within the stipulated checked range. These computations give precise outstanding cases, not their vanishing.

The primality witnesses for the three exceptional primes are respectively 7, 29 and 10, with complete factorizations of $p-1$:

\[
\begin{aligned}
151628697550&=2\cdot5^2\cdot11\cdot17\cdot16216973,\\
26315271553053477372&=2^2\cdot3\cdot7\cdot17\cdot41\cdot59
 \cdot743\cdot8011\cdot1279877,\\
154210205991660&=2^2\cdot3\cdot5\cdot7\cdot13\cdot19
 \cdot37\cdot367\cdot109471.
\end{aligned}
\]

All factors on the right are trial-proved prime. For each prime factor $r\mid p-1$, the certificate checks $g^{p-1}=1\pmod p$ and $\gcd(g^{(p-1)/r}-1,p)=1$. Every prime divisor of $p$ must therefore support an element of order $p-1$, forcing that divisor to equal $p$. No probable-prime test is used in this verification.

## Character orientation is decisive

The carried reflection proof applies to an even component of exponent $i$ through its odd mirror $1-i$. For $i=n\in\{34,36,38\}$, the needed rational Bernoulli condition is $p\nmid B_n$. At the displayed prime that condition fails exactly.

In contrast, the companion value $B_{p-1-n}$ controls the mirror $1+n$ and hence $A_p^{[-n]}$. Even if this companion value is nonzero, it establishes the component already supplied by $K_{2n}(\mathbf Z)=0$, namely K68, K72 or K76. It supplies no implication to $A_p^{[n]}$. Congruence of these two character exponents would require $p-1\mid2n$, which fails at all three exceptional primes.

The inspected carried source is `input/RETURN_K17_checkpoint_08_20261121T0616Z/evidence/work/hecke_general/reflection_bernoulli_section.tex`, the complete K17-REFLECTOR proof. The separate carried `higher2/bernoulli_8361790201_section.tex` explains the multiplier-two harmonic formula and its former linear enumeration. The current `main_gate/bernoulli_prefix_formula.tex` was also read in full: its rearrangement gives $O(f+p)$ terms, and by itself supplies no sublinear test of a cyclotomic-unit residue.

## A proved finite Vandiver test, with exact ready inputs

Buhler–Harvey, *Irregular primes to 163 million*, Section 4, author pages 4–5, gives the following componentwise sufficient test. For prime $q=Mp+1$, choose $z\in\mathbf F_q^\times$ of order $p$. Put

\[
V_{p,n}=\prod_{c=1}^{(p-1)/2}(z^c-z^{-c})^{c^{p-1-n}}\pmod q.
\]

If $V_{p,n}^{M}\ne1\pmod q$, the component $A_p^{[n]}$ vanishes. The final $M$-th power makes it valid to reduce the exponents modulo $p$. The source distinguishes this unit test from its separate harmonic-sum criteria for the Iwasawa lambda invariant; the latter must not be substituted for a Vandiver proof.

The complete source Section 4 was read, along with the implementation discussion in Section 6. The cyclotomic-unit/class-component comparison is a stated primary input, not reproved here. Primary URL: <https://arxiv.org/pdf/0912.2121>; the PDF and extracted text are saved under `lean_chain/primary/buhler_harvey_irregular_2009.*`.

Our small certificate proves the following usable auxiliary primes and order-$p$ roots. No product $V_{p,n}$ was evaluated.

| $n$ | $M$ | Prime $q=Mp+1$ | Root $z\pmod q$ |
|---:|---:|---:|---:|
| 34 | 12 | 1819544370613 | 2176782336 |
| 36 | 64 | 1684177379395422551873 | 1161898535434908469692 |
| 38 | 10 | 1542102059916611 | 1024 |

Their full-factor Lucas witnesses are 6, 3 and 2. The certificate verifies exact order $p$ by $z^p=1\pmod q$ and $z\ne1\pmod q$, after proving (p,q) prime. These are certified auxiliary inputs; minimality of $q$ is not asserted.

The direct finite tests still have respectively

\[
75{,}814{,}348{,}775,\quad
13{,}157{,}635{,}776{,}526{,}738{,}686,\quad
77{,}105{,}102{,}995{,}830
\]

factors. The primary Section 6 implementation reduces the per-factor exponent-update cost but still visits the complete multiplicative orbit. No $O(\sqrt p)$ evaluation of this weighted unit product was established in the sources examined. This is a bounded method audit, not a claim that no such algorithm can exist.

## What a square-root polynomial harmonic method can actually compute

For fixed $r<p$, let $H_r(N)=\sum_{a=1}^{N}a^{-r}$ in $\mathbf F_p$, with $N<p$. Choose block size $b$ and set $P(X)=\prod_{j=1}^{b}(X+j)$. For every complete block with starting point $t$,

\[
[T^r]\log\frac{P(t+T)}{P(t)}
 =\frac{(-1)^{r-1}}r\sum_{j=1}^{b}(t+j)^{-r}.
\]

This follows by expanding each $\log(1+T/(t+j))$. The divisions are valid since all block entries and $1,\ldots,r$ are nonzero modulo $p$. Evaluating $P,P',\ldots,P^{(r)}$ at all block starts, then taking their truncated local series logarithms, computes every block sum exactly; an incomplete final block is handled directly. Standard product and remainder trees with $b\asymp\sqrt N$ give a sublinear polynomial-arithmetic route for fixed $r$. This elementary identity is sufficient to explain the proposed size estimate; no large implementation or performance claim is made.

For the companion Bernoulli test at exponent $n$, the carried multiplier-two identity specializes to

\[
B_{p-1-n}\equiv
-\frac{n+1}{2^{n+1}-2}\,
H_{n+1}\bigl((p-1)/2\bigr)\pmod p,
\]

provided the displayed denominator is a unit. Thus the method applies to a reciprocal-power sum of orders 35, 37 or 39. It computes the opposite-character test described above.

| Exceptional prime | $\lfloor\sqrt p\rfloor$ | $\lfloor\sqrt{(p-1)/2}\rfloor$ | One block polynomial, 8 bytes per coefficient |
|---:|---:|---:|---:|
| 151628697551 | 389395 | 275344 | about 2.2 MB |
| 26315271553053477373 | 5129841279 | 3627345555 | at least 29 GB; this modulus actually needs more than one 64-bit word |
| 154210205991661 | 12418140 | 8780951 | about 70 MB |

At the first prime the polynomial sizes are practically modest; retaining 36 derivative arrays of this length would use about 79 MB before tree and arithmetic overhead. At the third prime the analogous 40 arrays use about 2.8 GB before overhead. At the middle prime even one polynomial is enormous, and its 65-bit modulus increases the coefficient cost. Streaming can reduce derivative storage but cannot remove the length of the underlying block polynomial.

These are exact dimension/storage counts, not benchmark timings. The useful first-prime polynomial scale does not bridge the missing mathematical reduction from the Vandiver unit product to an ordinary harmonic sum.

## Scope of the additional literature check

Gras, arXiv:1808.03443v4, provides a Gauss/Jacobi-sum reformulation. Theorem 1.2 and the explicit Section 4.2.1 program were inspected for algorithmic scope. That program forms degree-$p-1$ cyclotomic polynomials and loops through the auxiliary finite field; it does not give the needed square-root shortcut. No full proof or new arithmetic conclusion from that paper is imported here. Its Remark 4.11 and Theorem 5.2 discussion also distinguish local $p$-primarity from the needed non-$p$-th-power test at an auxiliary prime. At an irregular index, local $p$-primarity of the relevant cyclotomic unit is compatible with Vandiver, so it cannot replace the auxiliary test.

**Decision:** retain the safe negative endpoint −16. The exact next target is the single component $A_{151628697551}^{[34]}$. Its finite auxiliary-prime inputs are now certified, but a fast evaluated unit certificate or another arithmetic argument is still needed.

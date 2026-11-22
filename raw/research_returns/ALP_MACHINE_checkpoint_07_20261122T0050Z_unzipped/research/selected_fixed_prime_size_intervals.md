# AM-R-018: complete numerical Sizes for the explicit fixed-prime selected families

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 22 November2026UTC.
Reasoning effort is not externally exposed.

This result checks the remaining spread condition left explicit in
R017. It gives all four clauses of the literal numerical `Sizes` record
on the K031/K032 baselines and on finite, explicitly bounded portions
of the K033 growing selected family. It does not construct `Dat.Ok`,
the global `SizeData₂`, or a net lift saving. In particular the
common-type-field obstruction remains. The fixed T-primes cannot
support an unbounded growing-weight family under this record.

## 1. Literal source spread, including the rank term

Use the actual m=2 data of K031/K032. Thus

\[
 d=t+1,\quad N_j=k+jd,\quad
 u_i=(2(k-i)+1)C+\tfrac12,\quad
 e_0=0,\quad e_1=4C.
 \tag{R18.1}
\]

Here k is42 or168, d is1760 or1634, and C is respectively
45156049293 or40530339687. The selected dominant weights are
the actual `lamTrue`, with their source determinant shifts.
Write these weights as \(w_j\). The checked source recurrence is

\[
 \begin{aligned}
 w_{0,i}&=(2(k-i)+1)C+1-k/2+i,\\
 w_{1}&=(w_0-d/2,\ (k/2)^d),\\
 w_{2}&=(w_1-d/2,\ (-4C+(k+d)/2)^d).
 \end{aligned}
 \tag{R18.2}
\]

The notation \(x^d\) in a weight list means d repeated entries.
These equations follow directly from `lamTrue_old` and
`lamTrue_new` in `Columns/BaseLemmas.lean`496–530, with
`hcToWeightQ` at stage zero. They are the already checked
recurrence, used here to compute its extrema.

The source does **not** define spread as first minus last alone.
`LocalRingCardinality/DataCoeff.lean`34–35 defines it, for
positive rank N, by

\[
              \operatorname{spread}(w)=w_0-w_{N-1}+N.
 \tag{R18.3}
\]

All rank terms in the following calculation are retained.
The three exact baseline spreads are

\[
 \begin{aligned}
 S_0&=2(k-1)C+1,\\
 S_1&=(2k+1)C+1+d/2,\\
 S_2&=(2k+5)C+1+d/2.
 \end{aligned}
 \tag{R18.4}
\]

**Proof.** The entries of \(w_0\) decrease by \(2C-1>0\).
Its last entry is \(3C+k/2\). In \(w_1\) the old last entry
is \(3C+k/2-d/2>k/2\), since \(3C>d/2\), so the new
constant block is the minimum. In \(w_2\) the smallest old
entry is \(k/2-d/2\), which exceeds the new last entry
\(-4C+(k+d)/2\) by \(4C-d>0\). At both steps the first
entry remains the shifted old first entry. These observations
also verify dominance at the block joins. Substituting these
first and last entries and the ranks \(k,k+d,k+2d\) into
(R18.3) gives(R18.4). Finally
\(S_1-S_0=3C+d/2>0\) and \(S_2-S_1=4C>0\). Thus
\(S_2\) is the largest baseline spread. ∎

If \(u_0\) at one embedding is increased by any integer
\(n\ge0\), every weight in(R18.2) changes only in its
first entry, which increases by n. Dominance persists, and
each literal spread is exactly \(S_j+n\). The same extrema
hold for any interlaced changes of the middle u entries that
retain the first and last entries and the same row data.
Consequently the calculation applies simultaneously to any
finite source word collection with those common extremes.

## 2. The growing K033 family and an exact size parameter

At K033's two distinguished embeddings the first u entry
is increased by

\[
                   A_r=11^r,\qquad B_r=121\,11^r
                         \quad(r\ge0),
 \tag{R18.5}
\]

respectively. Other embeddings have no increase. The fixed
row data, finite characters, G-primes, ranks and source
interlacing remain those already checked in K033. The
largest literal spread over all stages and embeddings is
therefore exactly

\[
                        S(r)=S_2+B_r.
 \tag{R18.6}
\]

Choose the integral real size parameter

\[
                 a(r)=\left\lceil\frac{S_2+B_r}{2}\right\rceil.
 \tag{R18.7}
\]

This a is the `Sizes` real parameter, not the source rank,
the lift count, or the ordinary differential degree.
The exact record `AbelianHostFieldConditions.lean`486–494 is

\[
 \begin{gathered}
 2fk<g_i-1\ (i=0,1),\qquad 4a<T,\\
             2fN_2+1<4a,\qquad
 \operatorname{spread}(w_{j,\tau})\le2a\quad(0\le j\le2).
 \end{gathered}
 \tag{R18.8}
\]

The first inequalities were checked in K031/K032. The last
follows exactly from(R18.6)–(R18.7). The middle lower bound
holds already at r=0 by the exact values below and continues
to hold because a(r) increases. Thus the only remaining
condition on r is \(4a(r)<T\), with T the corresponding
explicit prime of R017.

| Host | \(S_0\) | \(S_1\) | \(S_2\) | Exact permitted r interval |
|---|---:|---:|---:|---:|
| \(J^{14}\) | 3,702,796,042,027 | 3,838,264,190,786 | 4,018,888,387,958 | \(0\le r\le55\) |
| \(J^{56}\) | 13,537,133,455,459 | 13,658,724,475,337 | 13,820,845,834,085 | \(0\le r\le90\) |

For complete reproducibility, these endpoints are certified
by the integer inequalities

\[
 \begin{split}
 121\,11^{R_*}&\le
       2\left\lfloor\frac{T-1}{4}\right\rfloor-S_2
                         <121\,11^{R_*+1},\\
 R_*&=55\text{ for }J^{14},\qquad
 R_*=90\text{ for }J^{56}.
 \end{split}
 \tag{R18.9}
\]

**Proof of the endpoints.** For positive integers S and T,
\(4\lceil S/2\rceil<T\) is equivalent to
\(S\le2\lfloor(T-1)/4\rfloor\). Substitute
\(S=S_2+121\,11^r\), and use strict increase in r.
The two exact boundary comparisons in(R18.9), all four
clauses of(R18.8) throughout the stated intervals, and the
failed next endpoint are verified by integer arithmetic in
the saved certificate. The primality certificates for T are
carried from R017; they are not replaced by a numerical
primality screen here. ∎

At the first excluded r, even allowing a real size parameter
cannot restore this particular fixed-T family. Indeed its
spread condition forces \(a\ge S(r)/2\), and the certificate
also verifies \(2S(r)\ge T\) there. The strict inequality
\(4a<T\) is then impossible. This excludes only that fixed
T and growing-weight choice. It does not exclude choosing
a new T-prime as the weights grow.

The K033 growing degree first exceeds its fixed baseline
degree at r=13 on \(J^{14}\) and r=15 on \(J^{56}\).
Accordingly the nonempty ranges13–55 and15–90 also meet
the entire numerical(R18.8). The large fixed valuation
errors and all finite and real normalization costs in
K033/K034 are unchanged; baseline domination is not a
MainX gain/error inequality.

## 3. Scope and exact sources

R017 now has the missing `spread_le` check for the stated
baselines and these growing selected weights. The result
supplies a complete numerical `Sizes` witness, conditional
only on the already specified weight/prime data. It does
not make the primitive CM type satisfy `Fields.Ok.quad`,
identify the integral row and previous-image lattices, or
compute the global DP44 budget. K033/K034's unbounded
sharp-slope assertion concerns their selected section
modules; its use with this fixed T is restricted to the
explicit finite intervals just proved.

Exact stipulated source locators, pinned to commit
`7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`, are
`Formalism/LocalRingCardinality/DataCoeff.lean`34–39,
`Formalism/LocalToGlobal/Columns/BaseLemmas.lean`467–530,
and `Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean`
443–494. K031 HC3–10, K032 QH rank/weight data, K033
CS20–35 and R017 R17.1–5 are carried at their recorded
checked scope. The script is
`scripts/selected_fixed_prime_sizes_certificate.py`;
its complete arithmetic output is in
`checks/selected_fixed_prime_sizes_certificate.json`.
This is a mathematical source/parameter verification,
not a Lean build. Whole-proof readings are recorded
separately from the finite certificate.

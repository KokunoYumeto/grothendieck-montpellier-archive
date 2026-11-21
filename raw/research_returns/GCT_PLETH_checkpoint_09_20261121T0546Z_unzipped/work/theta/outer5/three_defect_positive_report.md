# Every two-row quotient three degrees below the quadratic ray

## T-048. A complete positive family

Let \(k\ge8\), \(x,b,d\ge0\), and \(2b+x+k\ge9\). Put
\[
\begin{aligned}
n&=d+b+x+k-3,\\
\lambda&=(d+3b+2x+3k-12,d+b+x+2k-3,d+b+x,d+x,d).
\end{aligned}
\tag{F.1}
\]
For every \(\mu\vdash5\), the coefficient
\(p_{\mu,(n)}^\lambda\) has the following explicit positive count.
For \(b\ge1\), selecting three residues modulo 60 leaves at most
55 polytopes with at most ten integer variables. For \(b=0\),
selecting two residues leaves at most fifteen polytopes with at most
eight variables. Every coefficient in the \(b\ge1\) branch is
strictly positive. The complete seven valid exceptions for the
\(b=0\) branch are listed in §5.

The theorem uses the actual cohomology isomorphism T-047 and then
proves a positive formula for this entire defect-three
zeroth-cohomology family. It does not infer positivity from an
alternating resolution alone. No historical novelty claim is made.

## 1. The exact module and its evaluated cohomology

Write \(a=b+x\), \(E=\mathfrak h_5\), and retain the specified
five-point ideal and tautological quotient. The flag chart and
complementary exterior-column pairing in (D.13) give
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+b+x}
H^0(\mathcal I^k(2k-3)S_{(b+x,b)}Q).}
\tag{F.2}
\]
The first-line twist before complement is \(b+x+2k-3\), and the
relative quotient weight is \((b+x,x,0)\) on \(Q^*\).
Contraction by \((\det Q^*)^{b+x}\), with
\(\det Q^*=\det E^*\mathcal O(-1)\), leaves twist \(2k-3\)
and the displayed sign. The point order is \(\lambda_2-n=k\),
with inverse chart map \(F\mapsto u^{-k}F(v(X))\). The inequality
in (F.1) is exactly \(\lambda_1\ge\lambda_2\).

T-047 applies with \(s=3\), since \(k\ge3s-1=8\). Its actual
finite normal restriction, substitution \(w=XYv\), and symmetric
square-zero bundle automorphism identify the entire first
cohomology with (D.2), induced over the ten pairs. All higher
cohomology in degrees at least two vanishes. Consequently the trace
of the actual zeroth cohomology is
\[
P_g(x,b,k;2k-3)+J^{(3)}_g(x,b),
\tag{F.3}
\]
where \(P_g\) is the three-term Schur/Euler expression (R.7), and
\(J^{(3)}\) is now evaluated explicitly.

## 2. All seven correction traces

On one pair, the four possible terms of (D.2) at \(s=3\) are
\[
\det P\otimes P\otimes S_{(a,b)}W,
\quad\det P\otimes W^*\otimes S_{(a,b)}W,
\quad S_{(a-1,b)}W,
\quad S_{(a,b-1)}W,
\tag{F.4}
\]
where the third term is omitted at \(x=0\), and the fourth at
\(b=0\). These are actual summands of the cohomology isomorphism,
not formal correction symbols. At a fixed pair, let its endpoint
sign be \(\delta\), let the complementary determinant sign be
\(\eta\), and let the complementary standard trace be \(e\).
Writing \(h_r\) for its rank-two symmetric-power trace, (F.4)
has trace
\[
(1+\delta+\delta e)\eta^b h_x+
\eta^b h_{x-1}+\mathbf1_{b\ge1}\eta^{b-1}h_{x+1}.
\tag{F.5}
\]
At \(x=0\), the convention \(h_{-1}=0\) implements the omitted
term. The three rank-two traces are \(x+1\),
\(\mathbf1_{2\mid x}\), and \(\tau(x)=(1,-1,0)_{x\bmod3}\).
Counting the literal fixed pairs in each \(S_5\) cycle type gives,
in the class order \(1^5,21^3,2^21,31^2,32,41,5\),
\[
\boxed{J^{(3)}(x,b)=
(60(x+1),\ 6(-1)^b\mathbf1_{2\mid x},\ 0,0,0,0,0)
\quad(b\ge1),}
\tag{F.6}
\]
and
\[
\boxed{J^{(3)}(x,0)=
(50x+40,\ 1+3\mathbf1_{2\mid x}-x,\ 2\mathbf1_{2\nmid x},
 -\tau(x+1),-\tau(x+1),0,0).}
\tag{F.7}
\]
For example, the transposition has three fixed-point pairs and its
one two-cycle pair. Substitution in (F.5) gives (F.6) or (F.7)
according to whether its fourth summand is present. For a three-cycle
on the complement, \(\tau(x-1)+\tau(x)+\tau(x+1)=0\), yielding
the displayed cancellations. Double transpositions have two
two-cycle pairs, and four- and five-cycles have no fixed pair.
This verifies all seven entries and their signs.

## 3. The branch \(b\ge1\)

Set \(b=B+1\), \(k=K+8\), with \(x,B,K\ge0\).
The actual multiplicity of \([\nu]\) is the inner product of
(F.3),(F.6) with the seven fixed character rows in T-044. These
closed elementary expressions are polynomial on every residue class
modulo 60, of separate degrees \((3,4,3)\).
At the identity the dimension is
\[
\begin{aligned}
&\frac{(x+1)(B+x+3)(B+2)}{12}
\bigl[(2K+14)(B+2K+16)(B+x+2K+17)\\
&\hspace{40mm}-5(K+8)(K+9)(K+10)\bigr]+60(x+1).
\end{aligned}
\tag{F.8}
\]
Its ordinary coefficients are positive; its total degree is six and
its active difference downset is the 55-element set (R.10).
Substitution of the fixed parity and third-residue formulas into
the nonidentity traces proves total degree at most three, and at
most one for a three-cycle. These exact symbolic identities are
included in the certificate. The trace formulas at \(-1,-2\)
already equal zero, so no initial residue exception is needed.

Define constants by the finite difference (R.9), using parameters
\((x,B,K)\) and the actual multiplicity just specified.
`two_row_three_defect_certificate.py` checks all 120,960,000 integers.
The 25 inactive orders vanish, and every constant at each of the
55 active orders is positive. Their minimum is one; their maximum
is 177897162600, below \(2^{38}\). The proved bound on every
weighted signed-64-bit intermediate is 21347661132000. The symbolic
degrees, exact divisibility checks, extrema, stream hashes and
empty zero lists are retained in `TWO_ROW_THREE_DEFECT_SUMMARY.json`.

For \(\nu=\mu\) when \(d+b+x\) is even and \(\nu=\mu^t\)
otherwise, the positive formula is precisely (R.11), with
\((x,B,K)\) in place of \((x,b,k)\). The literal polytopes are
(R.12). Newton's finite polynomial identity proves the equality
for every parameter; the exhaustive fixed integer certificate proves
the signs of all its constants. The zeroth constant is positive for
every residue, proving the full-support assertion for this branch.

## 4. The branch \(b=0\)

Set \(k=K+8\). The validity condition is \(x+K\ge1\).
The actual trace is
\[
h_g(x)\bigl(h_g(2K+13)-f_gh_g(K+7)\bigr)
-h_g(x-1)\bigl(h_g(2K+12)-f_gh_g(K+7)\bigr)
+J^{(3)}_g(x,0).
\tag{F.9}
\]
Every factor is an elementary residue polynomial. The separate
degrees in \((x,K)\) are at most three. At the identity the total
degree is five; at every nonidentity class the \(x\)-degree is
at most two. Thus the order \((3,3)\) vanishes identically, and
the other fifteen orders are the complete active set. The initial
negative index \(x-1=-1\) is correctly zero in every closed trace.

The constants are the two-variable finite differences of the
irreducible inner product of (F.9), with residues in
\(\{0,\ldots,59\}^2\). `symmetric_three_defect_certificate.py`
checks all 403,200 constants. They are all nonnegative; every
nonconstant active order is positive, with minimum 1054. Their
maximum is 646806600, below \(2^{30}\). Exact extrema, zero pairs,
stream hashes and the precomputed overflow bound are retained in
`SYMMETRIC_THREE_DEFECT_SUMMARY.json`.

The exact positive formula is
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{\substack{0\le i,j\le3\\(i,j)\ne(3,3)}}
C_{\nu,r;i,j}\binom{q_1}{i}\binom{q_2}{j},
\qquad(x,K)=r+60q.}
\tag{F.10}
\]
Its polytopes have two residue-quotient variables, one coefficient
interval variable, and two increasing chains of total length at
most five. This gives the stated bound of eight variables and
fifteen contributing tags. The subset-chain bijection is the one
proved in (R.12), with no signed terms.

## 5. Complete support, direct evaluator and checks

For \(b=0\), every first-order constant is positive, so all zeros
are inside the residue square. Excluding the invalid origin
\((x,K)=(0,0)\), the entire zero set is
\[
\begin{array}{c|c}
\nu&(x,K)\\\hline
(5)&(0,1),(1,0)\\
(2,2,1)&(0,1)\\
(1^5)&(0,1),(0,2),(0,3),(1,0).
\end{array}
\tag{F.11}
\]
The other four labels have no valid zeros. The \(b\ge1\) branch
has no zero for any effective label. Apply the sign conversion
preceding (F.10) to obtain the support for any actual outer label.

`two_row_positive.py --ray three` is the direct positive evaluator
and complete constraint-matrix exporter for both branches. Its
constants use only the fixed bounded arguments of the finite
differences, then are cached. Its operations at input size are a
fixed number of bounded-order binomials, multiplications and sums;
no representation library, coefficient oracle or elimination is
used. All witness coordinates have logarithmic bit length in the
parameters plus the absolute constant bounds above.

The two closed correction characters were independently compared
with the literal fixed-pair sum (D.2) in 3360 cases, including both
\(b=0\) and \(b\ge1\), and all agreed. The rectangular agent
independently checked all 84 valid actual plethysm coefficients with
\(s=3,n\le7\), for every outer label. Its proposed side summed
the actual permutation action on \(P\), its determinant, and the
complementary rank-two Schur traces, without using (F.6),(F.7) or
the Newton constants. All passed; the receipt is
`work/rectangular/OUTER5_STABLE_DEFECT_INDEPENDENT_CHECK.tsv`.

The full proof has subsequently been read and checked independently
by the root, rectangular and archive agents. The rectangular agent
independently reconstructed all 403,200 constants in the \(b=0\)
branch and all 3360 correction values, matching every hash, extremum
and zero pair; its receipt is
`work/rectangular/SYMMETRIC_THREE_DEFECT_INDEPENDENT_CHECK.txt`.
The archive agent independently reconstructed the entire
120,960,000-entry \(b\ge1\) stream by ambient three-by-three
Jacobi–Trudi characters, point jets, residue polynomials and Stirling
differences. Every per-label hash and extremum agrees. It also proved
coefficientwise character-triangle domination for all 54 positive
active orders, with minimum constant margin 411165; the zeroth order
was checked on the full residue cube. Its receipt is
`work/archive/THREE_DEFECT_INDEPENDENT_RECEIPT.json`.
These are separate checks of the two branches, not a repeated claim
that a single short sample verifies the exhaustive certificates.

The standalone four-ray evaluator passed 2288 exact comparisons and
79 literal constraint-matrix witness checks, recorded in
`TWO_ROW_EVALUATOR_CHECK.txt`. This covers its continuation formulas
and all branch dispatches, including both branches of the present
theorem.

The geometric inputs and their primary locators are fully stated
and applied in T-047. The new work in this specialization is the
explicit four-summand correction evaluation, its two exact
residue-polynomial specifications, both exhaustive positive integer
certificates, the bounded polytope formulas and the complete support.

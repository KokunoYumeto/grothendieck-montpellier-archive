# The remaining upper strip on the one-twist wall

## T-056. Positive formula at b=3k−4

Letk≥5,x,d≥0 andb=3k−4. Use the partition and degree
in T055/(OT.1), namely

\[
n=d+b+x+1-k,\qquad
\lambda=(d+3b+2x+4-5k,d+b+x+1,d+b+x,d+x,d).
\tag{OS.1}
\]

Every coefficientp_{μ,(n)}^λ, μ⊢5, is strictly positive.
It has a fixed positive formula with17 disjoint bounded
polytopes, at most nine integer variables each, given below.
The determinant parity is the same as T055:ν=μ orμ′
according asd+b+x+1 is even or odd.

## 1. Exact extension of the restriction trace

The actual module and normal-order maps are exactly
T055/(OT.3). Its degree isN=2b+x+3, and

\[
N-5k=k-5+x\ge0.
\tag{OS.2}
\]

Terms with at least four selected points still vanish by
the quotient degree4(k−1)<N. The three-point term also
vanishes, now by the full horizontal-strip inequalities:
forα=(b+x+1,b+1,1), a nonzero complementary-line skew
factor requiresρ1≥b+1 andρ2≥1. Hence

\[
|\rho|\ge b+2=3k-2>3(k-1),
\]

contrary to the normal-degree bound. This is the additional
degree argument needed at the strip endpoint; the weaker
bound onρ1 alone would not suffice.

The singleton proof in T055 only requiresb≥k−1, which holds.
Its triangle and shifted triangle have ordersk andk−1≥4.
The two-row exterior comparisons in the pair proof require
p≤2(k−1)<b+1=3k−3, which also holds. Consequently every
actual quotient map, determinant contraction and character
identity (OT.4)–(OT.9) remains valid on this strip. This
proves the exact representation comparison before using
the polynomial substitution below.

## 2. Fixed polynomial certificate and exact support

PutX=x andK=k−5. The substitution into the T055 coordinates
is

\[
(X_{\rm old},B_{\rm old},K_{\rm old})=(X,-1,K+2).
\tag{OS.3}
\]

The previous paragraph proves the character identity at
these parameters, so this substitution is justified through
the actual restriction complex. Phase keys remain the
residues of the physical parameters(a,b,k), with
a=3K+11+X,b=3K+11,k=K+5. All449 fixed phases are
retained; no phase relabeling is inferred from a change of
variable without these explicit formulas.

The resulting identity trace is

\[
\begin{aligned}
P_1={}&60+107K+59K^2+13K^3+K^4\\
&+X\left(144+\frac{572}{3}K+84K^2+
                     \frac{46}{3}K^3+K^4\right)\\
&+X^2\left(112+\frac{290}{3}K+\frac{53}{2}K^2+
                                      \frac73K^3\right)\\
&+X^3\left(28+13K+\frac32K^2\right).
\end{aligned}
\tag{OS.4}
\]

Its coefficients are positive. The active two-variable
Newton orders, including zero, are

\[
\mathcal D=\{(0,j):0\le j\le4\}
\cup\{(i,j):1\le i\le3,\ 0\le j,\ i+j\le5\}.
\tag{OS.5}
\]

There are17 orders. Nonidentity traces have total degree
at most two. Their five nontrivial coefficientwise
character-triangle comparisons give:

| Order in(X,K) | Constant margin | Minimum coefficient |
|---|---:|---:|
| (0,1) | 15985520 | 180 |
| (0,2) | 198712800 | 10800 |
| (1,0) | 6450290 | 60 |
| (1,1) | 4508750400 | 14400 |
| (2,0) | 37076400 | 16800 |

Each complete rational margin polynomial is saved in
`ONE_TWIST_STRIP_POLYNOMIALS.json`. Every remaining positive
order differentiates only (OS.4), which has a positive
coefficient at every active exponent. Its difference has
nonnegative coefficients and strictly positive constant.
All omitted orders are zero by the displayed support.

The invariant Hermitian character bound|χν(g)|≤dim[ν]
therefore proves every positive-order multiplicity
difference is strictly positive. Order-zero values are
actual module multiplicities. All25200 base values for
0≤X,K<60 were evaluated with unbounded integer/rational
arithmetic: every one is positive. AtX=K=0, their vector
in label order5,41,32,311,221,2111,11111 is

\[
(1,2,3,2,3,2,1).
\]

The positive first differences imply that any zero outside
the base box is impossible as well. This proves the stated
complete nonvanishing result on the strip.

## 3. Positive formula and literal constraints

ForZ=(X,K), writer=Z mod60 andq=(Z−r)/60. Withfν(Z)
the exact class inner product, define the fixed nonnegative
integers

\[
D_{\nu,r,(i,j)}=
\sum_{u=0}^{i}\sum_{v=0}^{j}
 (-1)^{i+j-u-v}\binom iu\binom jv
 f_\nu(r_1+60u,r_2+60v).
\]

The complete formula is

\[
\boxed{
p_{\mu,(n)}^\lambda=
\sum_{(i,j)\in\mathcal D}
D_{\nu,r,(i,j)}\binom{q_1}{i}\binom{q_2}{j}.}
\tag{OS.6}
\]

Every evaluation has fixed bounded arguments. For each tag,
take a selector in[0,D−1], an increasingi-subset of
[0,q1−1], an increasingj-subset of[0,q2−1], and the two
equalities60q=Z−r. These choices give the exact lattice
point bijection. This requires at most3+i+j≤8 variables.
The supplied implementation retains one redundant coordinate
qB=0 to reuse the already verified matrix constructor, so
its literal matrices have at most nine variables. Deleting
that variable and its equality gives the eight-variable
version by an explicit coordinate projection and its
zero-coordinate inverse.

`one_twist_strip.py` exports`coefficient(x,k,d,mu)` and
`polytopes(x,k,d,mu)` and contains the exact rational
substitution/difference constructor. No input-dependent
representation calculation appears in the positive evaluator.

## 4. Executed checks and scope

`check_one_twist_strip.py` checked all25200 base constants,
63 complete rank-three restriction class traces,84 actual
balanced cycle/Pieri coefficients,224 Newton continuation
and parity cases, and118 literal matrix witnesses. Every
comparison passed. The exact ranges and base hash are in
`ONE_TWIST_STRIP_RECEIPT.json`.

These are executed checks by this agent using the specified
separate comparison implementations. The archive agent has
read the entire proof and checked every map, endpoint,
polynomial substitution and positive-count argument; that
whole-proof review passed. The root has checked (OS.1)–(OS.6)
and was completing the trailing verification references at
the latest report. The archive independently reconstructed
all16 margins and all25200 base constants from its literal
rank-three normal-Weyl phase data, with identical hashes,
extrema and support, and checked140 further actual strip
traces. Its exact review and receipts are
`work/archive/ONE_TWIST_STRIP_REVIEW.md`,
`work/archive/ONE_TWIST_INDEPENDENT_RECEIPT.json` and
`work/archive/ONE_TWIST_EVALUATOR_RECEIPT.json`.

For the full one-twist-wall routing, the strip withk≤5 lies
inb≤2k+1 and is already treated by the complementary branch
of the established general-twist and small-defect formulas.
Thus no unproved low-order endpoint is needed to use this
strip together with T055 and the two lower cones.

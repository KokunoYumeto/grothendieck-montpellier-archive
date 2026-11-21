# The complete complementary normalized twist region

## T-059. A positive formula for k≤c<2k and b+c≥2k

LetX,B,K,U,d≥0. Define

\[
\begin{gathered}
x=X,\quad b=K+B+1,\quad k=K+U+1,\quad c=K+2U+1,\\
n=d+K+B+U+X+1,\\
\lambda=(d+2K+3B+2X+3U+2,
 d+2K+B+X+2U+2,\\
\hspace{32mm}d+K+B+X+1,d+X,d).
\end{gathered}
\tag{HT.1}
\]

For everyμ⊢5, the coefficientp_{μ,(n)}^λ has the fixed
positive formula (HT.10). It uses151 disjoint bounded
rational polytopes with at most eleven integer variables
each. The complete zero list consists of the nineteen
effective-label cases in §6.

The parameterization is exactly the entire normalized
region

\[
k\le c<2k,\qquad b+c\ge2k,\qquad x,d\ge0.
\tag{HT.2}
\]

Indeed its inverse isK=2k−c−1,U=c−k,B=b−2k+c,X=x.
All these coordinates are nonnegative. The first
partition gap is2B+X+U≥0, so every point in this
orthant is valid, including the origin.

## 1. The exact module and all vanishing restriction terms

Seta=b+x andα=(a+c,b+c,c). The actual section and
normalizer maps of G027/T049 identify

\[
\begin{aligned}
M&=\operatorname{Hom}_{GL(F)}
 \bigl(S_\alpha F,(J_k)_{|\alpha|}\bigr),
\quad F=Q^3,\quad J_k=\bigcap_i(\ell_i\otimes F)^k,\\
(S_\lambda Q^5)_{(n^5)}
&\simeq\operatorname{sgn}^{d+b+x+c}\otimes M.
\end{aligned}
\tag{HT.3}
\]

The map is the specified normal substitution and its
balanced inverseu^{-k}F(v(X)), with the Young projector
retained. Normal-order equality proves the extension.
Writeν=μ for even d+b+x+c, andν=μ′ for odd parity.

One has|α|−5k=2B+X+U≥0. Hence all restriction
terms with four or more selected points vanish by
their degree bound4(k−1). PutR=2k−c=K+1. For a
selected triple, a nonzero complementary-line Pieri
projection would requireρ1≥b+c andρ2≥c. But

\[
b+2c-3(k-1)=B+U+3>0.
\tag{HT.4}
\]

The normal degree is at most3(k−1), so every triple
term vanishes as well. Thus the actual oriented
restriction complex is

\[
0\longrightarrow M\longrightarrow S_\alpha\mathfrak h_5
\longrightarrow C_1\longrightarrow C_2\longrightarrow0.
\tag{HT.5}
\]

This holds on the entire orthant, includingk=c=1.
The following character calculation evaluates these
specific maps.

## 2. The full three-row singleton simplex

LetV be the complementary standard module of dimension
three. The actual one-slot Pieri projection gives the
horizontal-strip decomposition ofSα(V⊕z), with normal
degree less thank. The complete-function identity

\[
h_j(V\oplus z)=\sum_{r\ge0}h_{j-r}(V)z^r
\]

and multilinearity of the three Jacobi–Trudi rows give
its exact character as

\[
\boxed{
\sum_{r_1,r_2,r_3\ge0,\ r_1+r_2+r_3<k}
\det\bigl[h_{\alpha_i-i+j-r_i}(V)\bigr]_{1\le i,j\le3}.}
\tag{HT.6}
\]

This retains the full three-row polynomial determinant.
It is T057/(RT.8), withc≥k ensuringr3<k≤c. Its
equivariant meaning is exactly the preceding
one-dimensional torus branching and Young projection;
no termwise determinant removal is used.

The first two determinant rows have only nonnegative
complete-function indices: their respective minima
are at leastk+1 andk. The last-row minimum is
c−k−1=U−1≥−1. The complete-character phase extension
for a three-dimensional standard module has exact
zerosh(−1)=h(−2)=0: its generating function is the
reciprocal of a degree-three polynomial with nonzero
leading coefficient, and the backwards recurrence
forces precisely these two initial values. Thus the
same quasipolynomial expression evaluates every
entry in (HT.6), even atU=0.

For a complementary periodL, writer_i=s_i+Lq_i,
0≤s_i<L. Every determinant summand becomes a
polynomial in the threeq_i. Expanding powers into
falling binomials and using

\[
\sum_{q_1+q_2+q_3\le M}
\binom{q_1}{j_1}\binom{q_2}{j_2}\binom{q_3}{j_3}
=\binom{M+3}{j_1+j_2+j_3+3}
\tag{HT.7}
\]

evaluates the sum in a fixed number of rational
operations. HereM=floor((k−1−Σs_i)/L)≥−3.
AtM=−1,−2,−3 the left side is empty and the right
side is zero, since its upper binomial argument is
2,1,0 while its lower argument is at least three.
This proves every initial endpoint in the residue
construction, not only an eventual polynomial range.

## 3. Pair terms depending only on R=2k−c

The exact general pair comparison is T058/(GU.6)–(GU.8).
It is proved by the three actual exterior-dual minor
maps, the full three-variable alternant, the
commuting replacement operators, and the displayed
rational highest-space isomorphism. It applies because
the normal shapeρ=(p,q) satisfiesp≤2(k−1)<b+c.
Its common factor is

\[
(\det W)^{b+c}\operatorname{Sym}^x(W),
\qquad W=\mathfrak h_3.
\]

For an individually fixed pair, the coefficient ofz^c
inT_k(W*⊕z)^2 has summation range
c−k+1≤l≤k−1. Sincec−k=U andR=k−U,
putl=U+s to obtain exactly

\[
\sum_{s=1}^{R-1}T_{R-s}(W^*)T_s(W^*).
\tag{HT.8}
\]

AtR=1 this is empty. For an interchange, the normal
trace has only even powers ofz. It is zero for oddR,
and for evenR it isT_{R/2}(W^{*2}), with the actual
squared permutation action. The orientation of the
selected pair contributes−1 in the interchanged
case and+1 in the individually fixed case.

The rational invariant dot product identifiesW* withW
as anS3 module. Furthermoreb+c=2R+B+2U, and
(detW)^2 is the trivialS3 line: choose an ordered
rational volumeω and sendω⊗ω to1. Every permutation
acts onω by±1, so this is an actual equivariant
trivialization. Thus the external determinant factor
on these finite-group traces is exactly(detW)^B.

The sum in (HT.8) is evaluated by splitting s into
the at most three complementary residue classes
and summing its polynomial entries. Equivalently it
is T058's fixed-pair expression withk′=R−1,c′=R−2.
AtR=1 the latter hasc′=−1; every residue upper bound
is−1 and the binomial summation is exactly zero.
This is a verified empty-sum endpoint, not an
extension of a nonexistent negative symmetric power.

## 4. Complete phase construction and positivity certificate

The full character is the ambient3×3 Jacobi–Trudi
trace on\(\mathfrak h_5\), minus the singleton
induction (HT.6), plus the literal invariant-pair
induction (HT.8) and its interchange term. Every
selected subset and orientation is explicitly
retained. The ambient complete functions require
at worst index−1, where the degree-four recurrence
gives the exact initial zero as in T058.

`generic_high_twist_polynomials.py` constructs all
2291 rational phase polynomials. Their periods are
1,2,2,3,6,4,5, with respective counts
1,16,16,81,1296,256,625. Their total degrees are
(6,3,2,1,0,0,0), and there are respectively
1,14,10,25,3,3,3 distinct polynomials. All coefficients
and every difference margin are saved in
`GENERIC_HIGH_TWIST_POLYNOMIALS.json`.

Write an order as(i,j,l,h), forX,B,K,U. The exact
active set, including zero, is

\[
\begin{gathered}
\mathcal A=\{(i,j,l,h)\in\mathbf Z_{\ge0}^4:
i\le3,\ j\le4,\ l\le4,\ h\le3,\\
i+j+l+h\le6,\ j+l+h\le5,\ i+j\le5,\ i+h\le5\}.
\end{gathered}
\tag{HT.9}
\]

It contains151 orders. The identity polynomial has
exactly these151 monomials, all positive. Its constant
is5 and its factorization isP1=(X+1)Q/12. To make
its sign explicit, this table gives the coefficient
ofB^iU^j inQ; every displayed coefficient is positive.

| (i,j) | Coefficient |
|---|---|
| (0,0) | \(K^4X\) + \(K^4\) + \(2K^3X^2\) + \(12K^3X\) + \(10K^3\) + \(12K^2X^2\) + \(53K^2X\) + \(41K^2\) + \(24KX^2\) + \(100KX\) + \(80K\) + \(16X^2\) + \(68X\) + \(60\) |
| (0,1) | \(K^4\) + \(7K^3X\) + \(15K^3\) + \(6K^2X^2\) + \(54K^2X\) + \(77K^2\) + \(24KX^2\) + \(137KX\) + \(165K\) + \(24X^2\) + \(114X\) + \(126\) |
| (0,2) | \(5K^3\) + \(9K^2X\) + \(39K^2\) + \(4KX^2\) + \(44KX\) + \(100K\) + \(8X^2\) + \(52X\) + \(84\) |
| (0,3) | \(3K^2\) + \(3KX\) + \(15K\) + \(6X\) + \(18\) |
| (1,0) | \(2K^4\) + \(8K^3X\) + \(24K^3\) + \(3K^2X^2\) + \(54K^2X\) + \(109K^2\) + \(12KX^2\) + \(125KX\) + \(217K\) + \(12X^2\) + \(98X\) + \(158\) |
| (1,1) | \(14K^3\) + \(27K^2X\) + \(111K^2\) + \(8KX^2\) + \(124KX\) + \(294K\) + \(16X^2\) + \(145X\) + \(261\) |
| (1,2) | \(18K^2\) + \(21KX\) + \(93K\) + \(4X^2\) + \(50X\) + \(118\) |
| (1,3) | \(6K\) + \(3X\) + \(15\) |
| (2,0) | \(8K^3\) + \(9K^2X\) + \(57K^2\) + \(KX^2\) + \(38KX\) + \(138K\) + \(2X^2\) + \(40X\) + \(112\) |
| (2,1) | \(27K^2\) + \(24KX\) + \(132K\) + \(2X^2\) + \(52X\) + \(163\) |
| (2,2) | \(21K\) + \(12X\) + \(54\) |
| (2,3) | \(3\) |
| (3,0) | \(6K^2\) + \(2KX\) + \(26K\) + \(4X\) + \(28\) |
| (3,1) | \(16K\) + \(4X\) + \(36\) |
| (3,2) | \(8\) |
| (4,0) | \(K\) + \(2\) |
| (4,1) | \(2\) |

For each nonzero orderδ, the exact rational
domination polynomial subtracts fromΔ60^δP1 the
sum of class sizes times the coefficientwise maximum
of|Δ60^δPγ| over every nonidentity phase. All150
polynomials have nonnegative coefficients and positive
constant. Only the34 orders of total degree at most
three require a nontrivial comparison; the rest use
the identity polynomial alone. The least constant
margin is293640, atδ=(1,0,0,0); the smallest
coefficient in the low-order margins is5. Every
complete rational margin is saved in the certificate.
The active inequalities (HT.9) equal the downward
closure of all monomial supports, so no omitted
difference is nonzero.

The invariant Hermitian bound|χν(g)|≤dim[ν] proves
that every positive-order multiplicity difference
is strictly positive throughout the orthant.
Order-zero values are the actual multiplicities
of (HT.3), hence nonnegative. All finite differences
are integers. This proves positivity of the constants
used in the next formula without a large base-cube
enumeration.

## 5. The positive formula and every inequality

WriteZ=(X,B,K,U)=r+60q,0≤ri<60. Letfν(Z) be the
class inner product of the exact phase trace, and
defineDν,r,δ=Δ60^δfν(r). The fixed formula is

\[
\boxed{
p_{\mu,(n)}^\lambda=
\sum_{\delta\in\mathcal A}
D_{\nu,r,\delta}\prod_{i=1}^4\binom{q_i}{\delta_i}.}
\tag{HT.10}
\]

Every constant uses only bounded argumentsr+60h,
0≤h≤δ; all coordinates are at most419. Its
construction uses the fixed rational polynomials,
not an input-dependent representation computation.
For each positive constant, the literal constraints
are

\[
60q_i=Z_i-r_i,\quad q_i\ge0,\quad0\le y<D_{\nu,r,\delta},
\qquad0\le u_{i1}<\cdots<u_{i,\delta_i}<q_i.
\tag{HT.11}
\]

Replace strict inequalities by gaps of one. The
selector and increasing subsets give a bijection
with the summand. There are at most5+|δ|≤11
variables withO(log(X+B+K+U+2)) input bits. The
determinant parameter only selects the stated
outer-label parity.

`generic_high_twist_positive.py` validates (HT.2),
evaluates (HT.10), exports all integer matrices
and lazily enumerates witnesses. Its physical
arguments are(x,b,k,c,d,μ), so the inverse
parameter map is explicit at the entry point.

## 6. Complete support from four actual multiplication maps

Increasing one coordinate by two adds an even
partition toλ and two ton. The corresponding
half-increments and tableaux are:

| Coordinate | Half-incrementη | Tableau columns |
|---|---|---|
| X | (2,1,1,1) | (1,3,4,5),(2) |
| B | (3,1,1) | (1,4,5),(2),(3) |
| K | (2,2,1) | (1,3,5),(2,4) |
| U | (3,2) | (1,4),(2,5),(3) |

For each row of the table, let hη be the product
of its oriented flag minors and set

\[
f_\eta=\sum_{\sigma\in S_5}(\sigma h_\eta)^2.
\tag{HT.12}
\]

Every term has balanced row degree two, right
highest weight2η, and the sum is invariant. At
the rational Vandermonde matrix it is a strictly
positive sum of squares. Multiplication in the
single flag-polynomial domain is therefore an
injectiveS5 map on every balanced component.
This is the actual G024 map, here with all four
tableaux written explicitly. Each increment changes
λ2 by an even number, so the effective label is
preserved.

For each axis, consider its coordinate equal to
3 or4 and the other coordinates equal to0 or1.
There are64 such boundary parity vectors. Every
one of their seven effective multiplicities is
positive, as verified by exact traces and actual
balanced-cycle computations. Their full vectors
are saved in`GENERIC_HIGH_TWIST_RECEIPT.json`.

For anyZ with some coordinate at least three,
reduce that coordinate to3 or4 of the same parity
and every other coordinate to0 or1 of the same
parity. Every difference is nonnegative and even.
Successively apply the four multiplication maps
(HT.12). Hence all suchZ have every label positive.
It remains only the81 points of{0,1,2}^4. Their
complete exact check gives these nineteen zeros:

| Coordinates(X,B,K,U) | All zero effective labels |
|---|---|
| (0,0,0,0) | (5),(4,1),(3,2),(3,1,1),(2,1,1,1),(1^5) |
| (0,0,0,1) | (5),(1^5) |
| (0,0,1,0) | (3,1,1),(2,1,1,1) |
| (0,1,0,0) | (5),(1^5) |
| (0,1,0,1) | (5) |
| (0,1,1,0) | (5),(1^5) |
| (1,0,0,0) | (5),(1^5) |
| (1,0,1,0) | (1^5) |
| (2,0,0,0) | (5) |

Every other parameter and label in (HT.2) is
positive. This support proof uses the displayed
injective morphisms and1015 fixed coefficient
comparisons, rather than an unproved extrapolation
from a small grid.

## 7. Exact verification scopes and current status

The rational generator constructed all2291 phases,
all150 positive-order margins and the exact151-order
support. The displayed factorization and the
inequalities (HT.9) were checked against every
identity monomial.

`check_generic_high_twist.py` compared all1015
coefficients in the64 boundary vectors and81
small-cube vectors with actual balanced-cycle
characters. It additionally checked112 complete
rank-three restriction traces,140 Newton
continuation/parity cases and271 literal matrix
witnesses. Every comparison passed. The full
receipt is`GENERIC_HIGH_TWIST_RECEIPT.json`.

No60⁴ residue cube was enumerated or claimed.
Actual multiplicities prove the zero-order signs;
the four explicit multiplication maps and the
printed finite support proof settle nonvanishing.
The root agent read the entire proof (HT.1)–(HT.12),
including the support and verification sections; that
whole-proof review passed. The rectangular agent separately
compared all1764 coefficients with
\(X,B,K,U,d\ge0\), \(n=d+X+B+K+U+1\le6\), and every
outer label. Its independent side used literal cycle-stable
pair induction, the complete3×3 singleton simplex and
Murnaghan–Nakayama plethysm; every comparison passed.
The receipt is
`work/rectangular/OUTER5_GENERIC_HIGH_TWIST_MN_CHECK.tsv`.
This is a finite coefficient check; it is separate from a
rectangular whole-proof reading.

The archive agent subsequently read the complete proof and
independently reconstructed all2291 phases from16166 original
interlacing/skew-determinant traces. All150 margins, their
minimum293640, all1015 support coefficients, the19 zeros and
the four Vandermonde sums241920,8400,27840,2480 agreed.
Its separate evaluator audit checked all17 printed factor
rows,210 both-parity coefficients,31672 matrices and5030
literal witnesses. The reports and receipts are
`work/archive/GENERIC_HIGH_TWIST_REVIEW.md`,
`GENERIC_HIGH_INDEPENDENT_RECEIPT.json` and
`GENERIC_HIGH_EVALUATOR_RECEIPT.json`. These independent
checks passed without a60⁴ residue-cube claim.

The determinant/branching identities are the
already read Macdonald I§5(5.1)–(5.8), pp70–71.
The actual schemes, normalizer and representation
classes use the proved G027/T049 and G024 maps
with their recorded EGA/SGA locators. T057 gives
the exact full-simplex refinement that prevents
the invalid determinant removal in this region.

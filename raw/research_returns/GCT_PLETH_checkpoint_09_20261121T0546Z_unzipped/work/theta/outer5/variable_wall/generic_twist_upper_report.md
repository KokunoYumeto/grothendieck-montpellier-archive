# A four-parameter positive formula with unbounded quotient twist

## T-058. The normalized upper chamber with c<k

LetX,B,K,C,d≥0 and put

\[
\begin{gathered}
x=X,\quad c=C,\quad k=C+K+4,\quad b=C+3K+10+B,\\
n=d+C+2K+6+B+X,\\
\lambda=(d+2C+4K+10+3B+2X,
 d+2C+3K+10+B+X,\\
\hspace{29mm}d+C+3K+10+B+X,d+X,d).
\end{gathered}
\tag{GU.1}
\]

For everyμ⊢5, the coefficientp_{μ,(n)}^λ has the fixed
positive formula (GU.12). It is a sum of144 disjoint
bounded rational-polytope counts, with at most eleven
integer variables in each polytope. No representation or
elimination calculation of input-dependent size is used.

Equivalently the actual parameters satisfy

\[
c\ge0,\quad k\ge c+4,\quad b\ge3k-2-2c,\quad x,d\ge0.
\tag{GU.2}
\]

All coefficients withC>0 are strictly positive. AtC=0,
the complete zero list is given in §6. The proof uses
actual module maps and a fixed polynomial certificate;
it does not assume the sign of an alternating character
formula.

## 1. Exact representation and retained restriction terms

Set \(a=b+x\), \(E=\mathfrak h_5\), \(F=\mathbf Q^3\) and \(\alpha=(a+c,b+c,c)\).
The first partition gap isK+2B+X≥0. Also

\[
b+c-2k=K+B+2\ge0,\qquad c<k,
\qquad |\alpha|-5k=K+2B+X\ge0.
\]

G027/T049's actual normal substitution, balanced
homogenization and Young projection identify

\[
\begin{aligned}
M&=\operatorname{Hom}_{GL(F)}
 \bigl(S_\alpha F,(J_k)_{|\alpha|}\bigr),
\qquad J_k=\bigcap_i(\ell_i\otimes F)^k,\\
(S_\lambda Q^5)_{(n^5)}
&\simeq\operatorname{sgn}^{d+b+x+c}\otimes M.
\end{aligned}
\tag{GU.3}
\]

The inverse balanced map isu^{-k}F(v(X)); its polynomial
extension is the proved normal-order statement. The
normalizer/outer Schur projection is therefore retained
with its exact determinant parity. Writeν=μ for even
d+b+x+c, andν=μ′ for odd parity.

Terms of size at least four in the oriented restriction
complex vanish in degree|α|≥5k. For a three-subset,
the complementary standard module is a line. Its actual
Pieri projection requiresρ1≥b+c andρ2≥c, hence

\[
|\rho|\ge b+2c\ge3k-2>3(k-1).
\]

The normal degree is at most3(k−1), so every triple
component is zero. The actual quotient complex therefore
gives

\[
0\longrightarrow M\longrightarrow S_\alpha E
\longrightarrow C_1\longrightarrow C_2\longrightarrow0.
\tag{GU.4}
\]

Every arrow and orientation line is the one in G027's
explicit restriction complex. This degree argument proves
the truncation of that complex before its character is
evaluated.

## 2. The exact singleton sum in the proved domain

For a singleton, letV be the complementary standard
module of dimension three. The actual Pieri branches are

\[
(a+c-i,b+c-j,c-l),\quad i+j+l<k,
\quad0\le i\le x,\ 0\le j\le b,\ 0\le l\le c.
\]

Sincec<k andb+c≥2k, one hasb≥k+1. Thus thej cutoff
is automatic. For each fixedl, the first-row cutoff is
removed by the exact involution
(i,j)↦(x+j+1,i−x−1). Its paired two-row determinants
have opposite signs and fixed points are zero. Every
shifted second part satisfiesb+l−j≥b−k+1+2l≥2.
Consequently the actual full-column exterior pairing
removesdet(V)^{c−l} with no negative-part boundary.
This is the corrected T057 domain, not the refuted
larger-domain candidate.

Define the finite formal triangle

\[
\Theta_{V,r}(A,B)=
\sum_{i,j\ge0,\ i+j<r}s_{(A-i,B-j)}(V).
\]

The exact singleton character is

\[
\boxed{
\sum_{l=0}^{c}\det(V)^{c-l}
 \Theta_{V,k-l}(a+l,b+l).}
\tag{GU.5}
\]

It is induced from the singleton stabilizer and subtracted
in (GU.4). All its actual tensor maps are the preceding
Pieri projection, involution identity and exterior-column
pairing. The indexk−l is at leastk−c≥4 throughout.

## 3. General pair comparison, including its explicit maps

Put \(W=\mathfrak h_3\), \(D=\det(W)\), and \(\rho=(p,q)\), \(p\ge q\ge0\).
The two normal symmetric slots have no Schur shapes with
more than two rows. Moreoverp≤2(k−1)<b+c. PutA=a+c
andH=b+c. Expand the three-row skew Jacobi–Trudi
determinant along its final row. Each of its2×2 minors
is one of T054's exact exterior-dual/Clebsch–Gordan
comparisons. After taking out the common factor
D^H Sym^x(W), the remaining character is

\[
\begin{aligned}
R_c={}&h_c(W)S_{(p,q)}(W^*)\\
&-D h_{c-q-1}(W)\operatorname{Sym}^{p+1}(W^*)\\
&+D h_{c-p-2}(W)\operatorname{Sym}^{q}(W^*).
\end{aligned}
\tag{GU.6}
\]

The three outer/inner pairs for those minors are
((A,H),(p,q)), ((A+1,H+1),(p+1,0)), and
((A+1,H+1),(q,0)). Their stable inequalities hold by
p<H. Thus the exterior and Young contraction maps
used in the reduction are the actual maps already
proved for these minors.

Sum (GU.6) in an auxiliary degreez. Its series is

\[
\frac{S_{(p,q)}W^*
 -D z^{q+1}\operatorname{Sym}^{p+1}W^*
 +D z^{p+2}\operatorname{Sym}^qW^*}
 {\det(1-zW)}.
\tag{GU.7}
\]

This is exactlys_{(p,q,0)}(W*⊕z). To verify it, let
u,v be the eigenvalues ofW*, soD=(uv)^{-1}. Expanding
the three-variable alternant along itsz row gives

\[
\frac{uv\,s_{(p,q)}(u,v)
 -z^{q+1}h_{p+1}(u,v)+z^{p+2}h_q(u,v)}
 {(u-z)(v-z)}.
\]

Dividing numerator and denominator byuv is (GU.7).
This proves the precise character identity

\[
\boxed{
s_{(a+c,b+c,c)/(p,q)}(W)
=D^{b+c}\operatorname{Sym}^{x}(W)
 [z^c]s_{(p,q,0)}(W^*\oplus z).}
\tag{GU.8}
\]

The right-hand coefficient is an actual torus-weight
subspace with its Young projector. Its graded generating
map can be specified directly: forw∈W, letEw replace
a covectorξ∈W* byξ(w)z in tensor space, summing over
slots and then applying the Young projector. TheseEw
commute, and

\[
\operatorname{Sym}(W)\otimes S_\rho(W^*)
\longrightarrow S_\rho(W^*\oplus z),
\qquad f\otimes v\longmapsto f(E)v
\]

preserves the displayed grading andGL(W) action.
It is onto: a Young tensor inW*⊕z is obtained from
its Levi highest type by the commuting root operators
replacingW* letters byz; ordering these operators and
the internalGL(W*) lowerings gives the elementary
triangular tensor spanning argument. Equivalently this
is the PBW ordering of the three explicit matrix-unit
root operators. The normal-slot permutation acts on
its separate Schur multiplicity space, so these maps
retain that action as well. Formula (GU.8) computes
the trace of these specified projections; no unnamed
module comparison is required.

For completeness, an actual rational isomorphism in (GU.8)
can be specified without leaving the comparison at its character.
Realize its left side by the skew Young space, equivalently the
`GL(F)` Hom space in the preceding actual Cauchy decomposition;
realize its right side by the displayed tensor and torus-weight
space. Use the ordered rational tensor bases and their Young
matrices. In each `GL(W)` weight \((r,s)\), take the reduced-row-
echelon ordered basis of the kernel of the raising operator
\(E_{12}\). The proved character identity gives equal dimensions
of these highest spaces. Match their ordered bases, and extend by
\[
\frac{E_{21}^j}{j!}v\longmapsto
\frac{E_{21}^j}{j!}v',\qquad0\le j\le r-s.
\]
The finite `sl_2` strings form bases: their raising formula is
\(E_{12}E_{21}^jv=j(r-s-j+1)E_{21}^{j-1}v\), and complete
reducibility gives the direct sum of these strings. Thus the map
is invertible, rational, and commutes with both matrix-unit
operators and the diagonal torus. It consequently commutes with
their finite exponentials and, by Gaussian decomposition, with
`GL(W)`. Tensoring the identity on every normal Schur multiplicity
space retains the selected-slot permutations. This explicitly
specifies the full equivariant comparison. The positive evaluator
uses the fixed trace polynomials, not this input-sized auxiliary
basis construction.

For a permutation fixing the selected pair individually,
writeT_r(W)=⊕_{j<r}Sym^jW. The actual coefficient in
(GU.8) is

\[
\sum_{l=0}^{c}T_{k-l}(W^*)T_{k-c+l}(W^*).
\tag{GU.9}
\]

Both orders are positive becausec<k. A permutation
interchanging the pair has zero coefficient for oddc.
For even c, it has traceT_{k-c/2}(W^{*2}), where the
superscript2 means the actual squared permutation
action. The pair orientation multiplies that trace by−1.
In the individually fixed case the orientation is+1.
The invariant rational dot product identifiesW* withW
as anS3 module, so these traces use the explicit
standard-module functions of T054.

## 4. Fixed construction of all rational phase polynomials

For a full cycle typeγ⊢5,
hγ(j)=[z^j](1−z)/∏ℓ∈γ(1−z^ℓ). The ambient trace is
the3×3 Jacobi–Trudi determinant ofα=(a+c,b+c,c).
Subtract the fixed-singleton induction of (GU.5), and
add the literal invariant-pair traces (GU.8)–(GU.9),
including their swap and orientation actions. This
is the complete class formulaPγ.

All needed complete-function phase polynomials start
at their initial nonnegative index by partial fractions.
The ambient last row can also require indices−1 and−2.
These are exactly zero in the same phase extension:
the generating function is1/Dγ(z), where
Dγ=∏ℓ(1−z^ℓ)/(1−z) has degree four and nonzero
leading coefficient. Its recurrence uniquely extends
the sequence backwards; comparison at degrees3,2,1
forceshγ(−1)=hγ(−2)=hγ(−3)=0. The quasipolynomial
solution satisfies this recurrence on every integer,
so it has these precise initial zeros.

The outer sums in (GU.5) and (GU.9) have a fixed
arithmetic construction. For complementary periodL,
writel=s+Lq,0≤s<L. Every summand is a polynomial
inq with rational polynomial coefficients in the
physical parameters. Its upper bound is
(c−s−((c−s) mod L))/L≥−1. Expandq^j into
falling binomials and use

\[
\sum_{q=0}^{M}\binom qj=\binom{M+1}{j+1}.
\tag{GU.10}
\]

AtM=−1 both sides are zero. The inner triangles use
the already proved T054 triangular-binomial identity.
Thus every sum is evaluated with a fixed number of
rational operations, including its initial endpoint.

The script`generic_twist_upper_polynomials.py` implements
these exact constructions and substitutes (GU.1).
There are2291 physical phases with periods
1,2,2,3,6,4,5; their counts are1,16,16,81,1296,256,625.
The total degrees are(6,3,2,1,0,0,0). There are only
1,14,10,25,3,3,3 distinct phase polynomials respectively.
All rational coefficients and every positivity margin
are saved in`GENERIC_TWIST_UPPER_POLYNOMIALS.json`.

## 5. Positive differences and literal polytopes

Write an order asδ=(i,j,l,h), corresponding toX,B,K,C.
The complete active set, including zero, is

\[
\begin{gathered}
\mathcal A=\{(i,j,l,h)\in\mathbf Z_{\ge0}^4:
i\le3, h\le4, j+l\le4,\\
i+j+l\le5, j+l+h\le5, i+j+l+h\le6\}.
\end{gathered}
\tag{GU.11}
\]

It has144 elements. The identity polynomial has exactly
these144 monomials, all with positive coefficients;
its constant is16. Its exact factorization is
P1=(X+1)(C+1)Q/12, whereQ is the following explicit
polynomial with positive coefficients. The table gives
the coefficient ofB^iC^j inQ.

| (i,j) | Coefficient |
|---|---|
| (0,0) | \(6K^4\) + \(14K^3X\) + \(66K^3\) + \(9K^2X^2\) + \(129K^2X\) + \(252K^2\) + \(69KX^2\) + \(367KX\) + \(384K\) + \(132X^2\) + \(300X\) + \(192\) |
| (0,1) | \(12K^3\) + \(21K^2X\) + \(95K^2\) + \(9KX^2\) + \(126KX\) + \(225K\) + \(34X^2\) + \(176X\) + \(142\) |
| (0,2) | \(7K^2\) + \(9KX\) + \(32K\) + \(2X^2\) + \(27X\) + \(25\) |
| (0,3) | \(K\) + \(X\) + \(1\) |
| (1,0) | \(28K^3\) + \(39K^2X\) + \(261K^2\) + \(6KX^2\) + \(291KX\) + \(743K\) + \(23X^2\) + \(539X\) + \(588\) |
| (1,1) | \(42K^2\) + \(39KX\) + \(255K\) + \(3X^2\) + \(142X\) + \(355\) |
| (1,2) | \(18K\) + \(8X\) + \(54\) |
| (1,3) | \(2\) |
| (2,0) | \(39K^2\) + \(18KX\) + \(297K\) + \(X^2\) + \(71X\) + \(563\) |
| (2,1) | \(39K\) + \(9X\) + \(145\) |
| (2,2) | \(8\) |
| (3,0) | \(12K\) + \(2X\) + \(48\) |
| (3,1) | \(6\) |
| (4,0) | \(1\) |

For each positive orderδ, form the exact domination
polynomial by subtracting fromΔ60^δP1 the sum of
class sizes times the coefficientwise maximum of
|Δ60^δPγ| over all nonidentity phases. All143
polynomials have nonnegative coefficients and positive
constant. Nonidentity degrees are at most three, so
only the34 orders of total degree at most three
require a nontrivial comparison. The smallest constant
margin is1583020, attained at(0,0,0,1); the smallest
coefficient among these low-order margins is5.
Every complete rational margin and order is in the
certificate. The other109 positive orders use only
the displayed identity polynomial; its monomial atδ
proves strict positivity of the constant difference.
All omitted differences are zero by (GU.11).

For every irreducible character, the invariant positive
Hermitian form gives|χν(g)|≤dim[ν]. The preceding
termwise bounds prove every positive-order multiplicity
difference is strictly positive at every nonnegative
coordinate vector. Order-zero values are multiplicities
of the actual module (GU.3), hence nonnegative. All
differences are integers.

Write \(Z=(X,B,K,C)=r+60q\), with \(0\le r_i<60\), and define the fixed nonnegative constants \(D_{\nu,r,\delta}=\Delta_{60}^{\delta}f_\nu(r)\), where \(f_\nu\) is the exact class inner product. The polynomial Newton
identity gives

\[
\boxed{
p_{\mu,(n)}^\lambda=
\sum_{\delta\in\mathcal A}
D_{\nu,r,\delta}\prod_{i=1}^4\binom{q_i}{\delta_i}.}
\tag{GU.12}
\]

Each constant uses only the bounded argumentsr+60h,
0≤h≤δ; every coordinate is at most419. Its definition
contains no input-sized multiplicity oracle. For each
positive constant, the literal polytope constraints are

\[
60q_i=Z_i-r_i,\quad q_i\ge0,\quad0\le y<D_{\nu,r,\delta},
\qquad0\le u_{i1}<\cdots<u_{i,\delta_i}<q_i.
\tag{GU.13}
\]

The selector and increasing subsets give a bijection
with that summand. Replace strict inequalities by gaps
of one. There are at most5+|δ|≤11 variables, with
O(log(X+B+K+C+2)) input bits; fixed constants contribute
only fixed bit lengths. The evaluator
`generic_twist_upper_positive.py` exports coefficients,
all integer matrices, and lazy witnesses. It validates
the actual parameter domain (GU.2).

## 6. Complete support by an explicit invariant multiplication

IncreasingC by two adds(4,4,2,0,0) toλ and two ton,
with unchanged effective-label parity. Use flag minors
pI and the actual invariant polynomial

\[
f=\sum_{\sigma\in S_5}
 \bigl(p_{\sigma(1),\sigma(3),\sigma(5)}
       p_{\sigma(2),\sigma(4)}\bigr)^2.
\tag{GU.14}
\]

The minors are oriented in their displayed order.
Each term has balanced row degree two and right
weight(4,4,2). The group permutes the terms, so
f is invariant. At the real Vandermonde matrix,
all these ordered minors are nonzero and the sum
of squares is positive; its exact value in the
chosen five-row evaluation is27840.

Multiplication byf in the single flag-polynomial
domain gives an injectiveS5 map from every balanced
module atC to the one atC+2. This is the specified
G024 map with tableau columns(1,3,5),(2,4), not
only a numerical semigroup comparison.

AtC=0, T054 applies with its coordinates(X,B,K+1).
Its complete zero list in the present coordinates is:

| Effective labelν | Zero triples(X,B,K), withC=0 |
|---|---|
| (5) | (0,0,1),(0,1,0) |
| (3,1,1) | (0,0,0) |
| (2,1,1,1) | (0,0,0) |
| (1^5) | (0,0,1),(0,1,0),(1,0,0) |

All other labels and triples are positive. AtC=1,
B=0 is T056 andB≥1 is T055; both are entirely
positive in the present parameter rangek≥5. AtC=2,
the four parameter triples supporting the above
exceptions have these exact effective vectors, in
label order5,41,32,311,221,2111,11111:

| (X,B,K) | Effective vector atC=2 |
|---|---|
| (0,0,0) | (3,5,8,5,7,4,2) |
| (0,0,1) | (4,18,22,28,21,17,3) |
| (0,1,0) | (5,26,30,42,30,25,4) |
| (1,0,0) | (7,27,33,39,32,25,6) |

The vectors were evaluated from the fixed exact trace
and checked against actual balanced cycle characters.
Every entry is positive. Multiplication byf transports
every oddC fromC=1, and every evenC≥2 from either a
positiveC=0 entry or one of these positiveC=2 seeds.
This proves the asserted full support, without an
exhaustive four-dimensional base-cube enumeration.

## 7. Executed verification and remaining review status

The exact symbolic generator constructed all2291
phases and143 domination polynomials; every rational
coefficient and the complete active support were
checked. The identity factorization and the
inequalities in (GU.11) reproduce its144 monomials.

`check_generic_twist_upper.py` compared224 full
rank-three restriction class traces,336 actual balanced
coefficients,140 Newton continuation/parity cases,
and291 literal matrix witnesses. It separately
checked all28 entries in the fourC=2 seed vectors
and the Vandermonde value in (GU.14). Every check
passed. The exact receipt is
`GENERIC_TWIST_UPPER_RECEIPT.json`.

No full60⁴ residue cube was enumerated or claimed:
actual representation multiplicities prove the
zeroth-order signs, and (GU.14) with the printed
seeds proves complete support. The root and archive agents each read the complete
proof, including the added rational highest-space map;
both whole-proof reviews passed. The archive independently
reconstructed all2291 phases from16166 literal normal
traces, all143 margins, all28 C2 seed entries and the
Vandermonde value27840. Its separate evaluator checks
passed168 both-parity coefficients,24178 matrices and
4828 witnesses, and matched all fourteen factor rows,
the144-order support and seven C0 zeros. Exact records
are `work/archive/GENERIC_UPPER_CHAMBER_REVIEW.md`,
`work/archive/GENERIC_UPPER_INDEPENDENT_RECEIPT.json`
and `work/archive/GENERIC_UPPER_EVALUATOR_RECEIPT.json`.

The primary determinant and branching identities
used in the trace calculation are Macdonald,
*Symmetric Functions and Hall Polynomials*, second
edition, I§5(5.1)–(5.8), printedpp70–71, already
opened and read in this run. The exact scheme,
normalizer and representation-class maps are the
proved G027/T049 and G024 constructions with their
recorded EGA/SGA locators.

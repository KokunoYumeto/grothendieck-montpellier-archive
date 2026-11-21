# A positive formula on the first adjacent central-wall chamber

## T-055. Unbounded ideal order with one unit of first quotient twist

Letk≥3, x,d≥0 andb≥3k−3. Put

\[
\begin{aligned}
n&=d+b+x+1-k,\\
\lambda&=(d+3b+2x+4-5k,
 d+b+x+1,d+b+x,d+x,d).
\end{aligned}
\tag{OT.1}
\]

For everyμ⊢5, the coefficientp_{μ,(n)}^λ is given by the
positive formula (OT.11), using at most46 disjoint bounded
rational polytopes, each with at most nine integer variables.
The complete formula uses fixed rational data and no
input-dependent character or elimination computation. This
evaluates the chamberc=λ2−λ3=1 with unbounded ideal order.

Set

\[
X=x,\qquad B=b-3k+3,\qquad K=k-3.
\tag{OT.2}
\]

These coordinates range independently over nonnegative integers.
The first partition gap is2b+x+3−5k=K+2B+X, so every such
triple, including the origin, gives a valid partition. The
effective outer label isν=μ when d+b+x+1 is even andν=μ′
when it is odd.

The only zero coefficients, after this label conversion, occur
at \(X=B=K=0\) and \(\nu\in\{(5),(2,2,1),(1^5)\}\). Every other coefficient
in the stated chamber is positive.

## 1. Exact section and restriction maps

Write \(a=b+x,E=\mathfrak h_5,F=\mathbb Q^3\) and
\(\alpha=(a+1,b+1,1)\). LetJk be the intersection of thekth powers
of the five block ideals(ℓi⊗F) inSym(E⊗F). The actual
normal substitution, balanced homogenization and Young
projection of G027 and T049 give

\[
M_{a,b,k}=\operatorname{Hom}_{GL(F)}
 \bigl(S_{(a+1,b+1,1)}F,(J_k)_{a+b+3}\bigr),
\qquad
(S_\lambda Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a+1}\otimes M_{a,b,k}.
\tag{OT.3}
\]

The inverse balanced map isu^{-k}F(v(X)); T049's exact
normal-order comparison proves its polynomial extension.
The determinant twist isλ2=d+a+1. Thus the character used
below belongs to this specified actual module.

Herea+b+3≥5k. G027's exact signed restriction complex has
literal quotient arrows and subset-orientation lines. A term
with at least four selected points is zero in this degree,
because four independent block directions give quotient degree
at most4(k−1). A three-subset has a one-dimensional remaining
standard module. Its skew Schur factor can be nonzero only
whenα/ρ is a horizontal strip, which requires

\[
\rho_1\ge\alpha_2=b+1\ge3k-2>3(k-1).
\]

The selected normal degree is at most3(k−1), so this is
impossible. Consequently the actual complex reduces to

\[
0\longrightarrow M_{a,b,k}\longrightarrow S_{(a+1,b+1,1)}E
\longrightarrow C_1\longrightarrow C_2\longrightarrow0.
\tag{OT.4}
\]

This uses the all-degree product/intersection theorem and its
equivariant quotient complex, not a dimension-based deletion of
an unknown map.

## 2. The singleton term and its exact straightening

For a selected singleton, the complementary standard moduleV
has dimension three. The actual one-slot Pieri projection
removes a horizontal strip of size less thank. It produces
shapes

\[
(a+1-i,b+1-j,1-l),\qquad
i,j\ge0,\quad l\in\{0,1\},\quad i+j+l<k,
\quad i\le x,\quad j\le b.
\]

Thej bound is automatic becauseb≥3k−3≥k−1. Forl=0,
the exterior-column pairing removes the full-height first
column and givesdet(V)⊗S_{(a−i,b−j)}V. Forl=1, it gives
S_{(a+1−i,b+1−j)}V. These are the specified actual Pieri
and determinant maps before any trace simplification.

To compute the character, remove thei≤x cutoff by pairing
every extra(i,j) with

\[
(i',j')=(x+j+1,i-x-1).
\tag{OT.5}
\]

Both entries are nonnegative, the total is unchanged, and both
paired indices havei>x. The two-row Jacobi–Trudi determinant
changes sign; a fixed point has equal shifted rows and is zero.
All complete-function indices used in the original triangles
are nonnegative in this chamber. The same involution applies
to the shiftedl=1 shapes, since their row difference is stillx.
Thus, with

\[
\Theta_{V,k}(a,b)=
\sum_{i,j\ge0,\ i+j<k}s_{(a-i,b-j)}(V),
\]

the exact singleton character is the induction of

\[
\det(V)\Theta_{V,k}(a,b)
 +\Theta_{V,k-1}(a+1,b+1).
\tag{OT.6}
\]

Both terms are subtracted from the ambient trace in (OT.4).
The determinant occurs only in the first term.

## 3. A rank-three pair trace through actual exterior and Pieri maps

For a selected pair, put \(W=\mathfrak h_3\), of dimension two.
Every normal Schur shapeρ=(p,q) has length at most two, because
the two slots are symmetric powers. Moreoverp≤2(k−1)<b+1.
We claim the exact skew-character identity

\[
s_{(a+1,b+1,1)/(p,q)}(W)
=(\det W)^{b+1}\operatorname{Sym}^x(W)
 [z]s_{(p,q)}(W^*\oplus z).
\tag{OT.7}
\]

Here[z] is the actual weight-one subspace for the last line,
and the normal Schur factor is selected by its Young
idempotent. The equality is verified as follows, with the
maps underlying its two determinant reductions specified.

Forq≥1, the last row of the three-row skew Jacobi–Trudi
determinant is(0,0,h1(W)). Its remaining two-row determinant
is the exterior-dual/Clebsch–Gordan comparison proved in
T054/VW7, now with outer shape(a+1,b+1). It equals
(detW)^{b+1}Sym^x(W)S_{(p,q)}(W*). Multiplication byW
removes one corner ofρ by the dual Pieri maps. Those maps
are contraction followed by the corresponding Young
projection; the highest tensors normalize their nonzero
scalars. Their direct sum is exactly[z]Sρ(W*⊕z).

Forq=0, expansion along the last determinant row additionally
subtracts

\[
h_{a+1-p}(W)h_{b+2}(W)-h_{a+3}(W)h_{b-p}(W).
\]

This is the two-row skew determinant for outer(a+2,b+2)
and inner(p+1,0), so the same actual exterior-dual comparison
identifies it with(detW)^{b+2}Sym^x(W)Sym^{p+1}(W*).
The remaining identity is the exact binary contraction
sequence

\[
0\longrightarrow\det(W)\otimes\operatorname{Sym}^{p+1}(W^*)
\longrightarrow W\otimes\operatorname{Sym}^{p}(W^*)
\xrightarrow{\;w\otimes f\mapsto\partial_w f\;}
\operatorname{Sym}^{p-1}(W^*)\longrightarrow0.
\]

In a basisu,v, its first map is
(u∧v)⊗f↦u⊗∂vf−v⊗∂uf. It is injective because a
positive-degree homogeneous polynomial with both derivatives
zero is zero. The contraction is onto whenp≥1 by integrating
monomials; dimensions then give exactness. Forp=0 its target
is zero and the first map is an isomorphism. This proves the
q=0 case, includingρ empty. Thus every exterior-dual and
Pieri operation used in (OT.7) has its actual tensor map.

For a permutation fixing both selected points individually,
the normal trace isT_k(W*⊕z)^2, where
T_k(V)=⊕_{j<k}Sym^jV. Its coefficient ofz is
2T_k(W*)T_{k−1}(W*). A permutation interchanging the two
points has normal trace∑_{j<k}h_j(W^{*2}⊕z²), so its
coefficient ofz is zero. The invariant rational dot product
on the complementary standard module identifiesW* withW
as an actualS3 module. The fixed-pair trace in (OT.4) is
therefore

\[
2(\det W)^{b+1}\operatorname{Sym}^x(W)
 T_k(W)T_{k-1}(W).
\tag{OT.8}
\]

The selected-pair orientation is+1 in this case. Its−1 value
for an interchange multiplies zero. This retains both the
factor-permutation and orientation actions.

## 4. Explicit fixed phase polynomials

For a permutation cycle typeγ, write

\[
h_\gamma(j)=[z^j]\frac{1-z}{\prod_{\ell\in\gamma}(1-z^\ell)}.
\]

The ambient trace in (OT.4), obtained by its three-row
Jacobi–Trudi determinant, is

\[
\begin{aligned}
P^0_\gamma={}&(m_1(\gamma)-1)
 \bigl(h_\gamma(a+1)h_\gamma(b+1)
      -h_\gamma(a+2)h_\gamma(b)\bigr)\\
&-h_\gamma(a+1)h_\gamma(b+2)
 +h_\gamma(a+3)h_\gamma(b).
\end{aligned}
\tag{OT.9}
\]

Subtractm1 copies of (OT.6), using the complementary cycle
type obtained by deleting a fixed point. Add (OT.8) for every
literal invariant pair consisting of two fixed points. These
instructions are the complete trace formulaPγ.

The partial-fraction interpolation and triangular summation
are exactly T054/VW10–12. Thel=1 triangle has orderk−1≥2.
Its residue boundM can equal−2; the summation identity still
holds there because both the empty triangle and
binom(M+2,p+q+2)=binom(0,p+q+2) are zero. This checks the
additional initial endpoint directly. No eventual-polynomial
assumption is used.

Substitutea=3K+6+B+X,b=3K+6+B,k=K+3. The seven class
periods are1,2,2,3,6,4,5; their phase counts are
1,8,8,27,216,64,125, totaling449. Their total degrees are
(5,2,1,1,0,0,0). The exact script
`one_twist_polynomials.py` constructs every rational coefficient
from (OT.6), (OT.8) and (OT.9), and saves them in
`ONE_TWIST_POLYNOMIALS.json`.

To exhibit the identity polynomial explicitly, the following
table gives the coefficient ofX^iB^j in6P1 as a polynomial
inK. Its coefficients are all positive.

| (i,j) | Coefficient in6P1 |
|---|---|
| (0,0) | 150+302K+204K²+58K³+6K⁴ |
| (0,1) | 449+536K+213K²+28K³ |
| (0,2) | 296+216K+39K² |
| (0,3) | 34+12K |
| (0,4) | 1 |
| (1,0) | 369+564K+309K²+72K³+6K⁴ |
| (1,1) | 728+746K+252K²+28K³ |
| (1,2) | 346+234K+39K² |
| (1,3) | 36+12K |
| (1,4) | 1 |
| (2,0) | 282+310K+114K²+14K³ |
| (2,1) | 295+216K+39K² |
| (2,2) | 51+18K |
| (2,3) | 2 |
| (3,0) | 63+48K+9K² |
| (3,1) | 16+6K |
| (3,2) | 1 |

## 5. Positive differences and the full bounded formula

The active Newton orders, including zero, are

\[
\mathcal A=
\{(0,j,l):j+l\le4\}
\ \cup\
\{(i,j,l):1\le i\le3,\ 0\le j\le4,\ i+j+l\le5\}.
\tag{OT.10}
\]

There are46 orders. For each nonzero orderδ, subtract from
Δ60^δP1 the class-size-weighted coefficientwise maximum of
|Δ60^δPγ| over all nonidentity phases, exactly as in T054§4.
Nonidentity degrees are at most two, so only nine orders need
a nontrivial comparison. Their complete rational polynomials
are saved in the certificate; the exact constant and minimum
coefficient in each are:

| δ | Constant margin | Minimum coefficient |
|---|---:|---:|
| (0,0,1) | 15172120 | 60 |
| (0,0,2) | 194212800 | 10800 |
| (0,1,0) | 3556240 | 20 |
| (0,1,1) | 186405600 | 3600 |
| (0,2,0) | 37921200 | 1200 |
| (1,0,0) | 2431040 | 10 |
| (1,0,1) | 4286462400 | 7200 |
| (1,1,0) | 764374800 | 2400 |
| (2,0,0) | 13928400 | 2400 |

All remaining nonzero orders differentiate only the identity
polynomial. Its displayed positive monomials include every
active exponentδ, so each such difference has nonnegative
coefficients and strictly positive constant term. The same
finite expansion checks that all omitted orders are zero.

For an irreducible characterχν, the invariant positive
Hermitian form gives|χν(g)|≤dim[ν]. The rational domination
polynomials therefore prove every nonzero Newton difference
of the multiplicity is strictly positive on this orthant.
The zero-order values are multiplicities of the actual module
(OT.3), hence nonnegative. All differences are integers.

WriteZ=(X,B,K)=r+60q with0≤ri<60. Letfν(Z) be the class
inner product ofPγ withχν, and define the fixed constants

\[
D_{\nu,r,\delta}=
\sum_{0\le h\le\delta}(-1)^{|\delta|-|h|}
\binom\delta h f_\nu(r+60h).
\]

The exact polynomial Newton identity is

\[
\boxed{
p_{\mu,(n)}^\lambda=
\sum_{\delta\in\mathcal A}
D_{\nu,r,\delta}\prod_{i=1}^3\binom{q_i}{\delta_i}.}
\tag{OT.11}
\]

All constants are nonnegative, and every evaluation coordinate
is bounded by359. Thus the formula requires only fixed-size
rational evaluations, not a coefficient oracle depending on
the input. For every positive constant, its literal bounded
polytope is

\[
60q_i=Z_i-r_i,\quad q_i\ge0,\quad
0\le y<D_{\nu,r,\delta},\qquad
0\le u_{i1}<\cdots<u_{i,\delta_i}<q_i.
\tag{OT.12}
\]

Replace strict inequalities by integer gaps of one. The
selector and the three increasing subsets give the required
bijection. There are at most4+|δ|≤9 variables. Their bit
size isO(log(x+b+k+1));d only determines the specified label
parity. `positive_one_twist_chamber.py` evaluates the formula,
exports every integer matrix and lazily lists its witnesses.

## 6. Support and actual verification scopes

The first differences in all three coordinates are strictly
positive, so a zero can occur only at quotientq=0. The full
60³ residue cube has only three effective-label zeros, all
atZ=0 andν=(5),(2,2,1),(1^5). At that valid origin the
effective multiplicity vector in label order
5,41,32,311,221,2111,11111 is

\[
(0,1,1,2,0,1,0).
\]

`check_one_twist_residue.py` evaluates all1512000 constants.
It proves every intermediate signed-integer bound before its
vectorized arithmetic. The largest class numerator bound is
139284866700; the largest weighted-character bound is
139284870294, both below2^63. Every residue value is a
nonnegative integer. Per-label hashes, extrema and all zeros
are in `ONE_TWIST_RESIDUE_RECEIPT.json`.

The separate `check_one_twist_formula.py` compared the proposed
trace with252 complete rank-three G027 restriction characters
and168 actual balanced cycle/Pieri coefficients. It also
checked182 exact Newton continuation/parity cases and197
literal matrix witnesses. All passed; the receipt is
`ONE_TWIST_COMPARISON_RECEIPT.json`. Those comparisons use
separate implementations under the root's directory; this
execution is not described as an independent-agent audit.

The rectangular agent independently checked168 actual
cycle-index/Murnaghan–Nakayama coefficients throughn=7,
with literal fixed-pair induction. Its receipt is
`work/rectangular/OUTER5_ONE_TWIST_BULK_MN_CHECK.tsv`.
The root and archive agents have each read the complete proof
and checked every map, endpoint and positivity deduction;
both whole-proof reviews passed. The archive also reconstructed
all449 phase polynomials from1747 literal rank-three normal
Weyl traces, every45 domination margins and all1512000
base constants, with identical hashes, extrema and zeros.
Its separate table/evaluator checks are recorded in
`work/archive/ONE_TWIST_CHAMBER_REVIEW.md`,
`work/archive/ONE_TWIST_INDEPENDENT_RECEIPT.json` and
`work/archive/ONE_TWIST_EVALUATOR_RECEIPT.json`.
The primary
skew determinant and horizontal-strip source used here was read
in full at Macdonald, *Symmetric Functions and Hall Polynomials*,
second edition, I§5(5.1)–(5.8), printedpp70–71. The actual
polynomial and section morphisms are G027/T049, with the
precise EGA/SGA transport locators already recorded there.

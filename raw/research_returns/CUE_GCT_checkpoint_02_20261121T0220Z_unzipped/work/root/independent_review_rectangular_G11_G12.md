# Independent agent proof review of G-11 and G-12

Reviewer: `/root/rectangular_bridge`, GPT-6 Astra Pro, inherited effort
(not exposed), run CUE_GCT-20261121, 2026-11-21.

## Conclusion and scope

I read the complete statements and proofs in `g11_g12_fragment.tex`.
Both pass mathematically. I independently checked the specific
Derksen bound in the original paper, in addition to my earlier
primary-source check of Chardin used by G-10. The general
Kempf–Ness and affine-GIT quotient theorems are used as cited
background; this review does not claim to reprove those theories
or to have reread the entire cited books and papers.

## Stability and dimensions

The binary-factor cyclic pencil realizes each Fermat form on both
sides. Its unit-monomial moment matrix is scalar, with mean exponent
n/4, and root operators do not connect its supported monomials.
The derivative stabilizer calculation forces every matrix entry
to zero for n≥3, so the closed orbit has finite stabilizer.

For padding a=n−m with 3a<m, the four positive weights sum to one
and give mean exponent n/4 in each variable. Supported exponent
differences are m times roots, so off-diagonal moment terms vanish.
In the finite-stabilizer calculation, reduction modulo x0 legitimately
forces L0=d0*x0 because q modulo x0 is nonzero and the polynomial
ring is a domain. Distinct mixed monomials remove off-diagonal
entries; the x0^m coefficient gives n*d0=0, then all other diagonals
vanish. The nonempty stable open subset therefore has 15-dimensional
quotient fibers. The dimension subtraction is valid for the reduced
irreducible cones used here.

## Generator bound

Primary source opened:
https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.7.pdf
(web reference `turn380193798view0`). On printed p.956,
Theorem1.1 gives β(V)≤max(2,(3/8)sσ(V)^2); Proposition1.2
and Example2.1 give σ(Sym^n C^q)≤q*n^(q^2−1).
Taking q=4 and s≤b_n yields exactly β_n=6*b_n*n^30.
This exceeds2 in the stated range. The contragredient automorphism
preserves the set of acting group elements and the invariant algebra,
so it does not multiply the bound by the coordinate degree of an
inverse-matrix formula.

The count T_n=binom(b_n+β_n,b_n)−1 is an upper bound for
the number of homogeneous generators: a homogeneous vector-space
basis of all invariant polynomials in the allowed degrees is enough,
and its dimension is bounded by that of the ambient coefficient ring.
Exactness of invariants makes the orbit-image invariant rings
homogeneous quotients, retaining this degree and generator bound.

## Explicit Veronese argument

Every generator degree divides B0=β_n!. For a monomial of degree
k*E_n, taking the maximal pure blocks leaves residual degree h*B0
with integer 0≤h<T_n. There are 4*k*T_n−h blocks available, at
least 4*T_n−h when k≥1. Combining that many with the residual
monomial leaves precisely 4*(k−1)*T_n blocks. The proposed
factorization into k degree-E_n monomials is therefore valid,
including h=0. Algebra relations do not interfere because these
monomials span each homogeneous component. This proves first-degree
generation of both Veronese rings, rather than merely assuming that
a common multiple of generator degrees is enough.

The Veronese rings remain domains and have unchanged Krull
dimension. Their regraded degree-k pieces are exactly the original
degree-E_n*k pieces, so the subsequent Hilbert-function indices
are correct.

## Quotient image degree and effective threshold

Representatives of a basis of (A_D)_(E_n) are degree-E_n invariant
polynomials on V_n. Composing with the pencil map gives homogeneous
forms of degree n*E_n. The resulting map is dominant onto the
projective quotient image: equivalently, the coordinate algebra
map from A_D^(E_n) into the parameter polynomial ring is injective,
with grading multiplied by n*E_n. Its projective closure is the
specified Proj. The common vanishing locus of these forms is a
base locus, handled by the already reviewed G-10 degree argument.
Thus the bound (n*E_n)^s≤Q_n has the right exponent and degree.

Chardin applies to the standard graded determinant quotient domain.
Linear Noether normalization applies to the competing standard
graded domain of dimension at least u_n+1. The binomial ratio is
(k+u_n)/u_n, which at K_n=u_n(Q_n−1)+1 is strictly greater
than Q_n and remains so for every larger k.

## Identification of the rectangular multiplicity

The degree-d coordinate representation is polynomial of total
GL4 weight nd. An irreducible polynomial GL4 representation is
SL4-trivial exactly when it is det^t. It is then one-dimensional
and nd=4t. As E_n is divisible by4, there is exactly one such
label in the relevant degree, λ=(nd/4)^4. Consequently the
invariant dimension is its multiplicity, with no Schur-dimension
factor and no sum over several determinant powers. Highest-weight
support transfers the projected coordinate multiplicity to the
original orbit closure in the established convention.

## G-12, including the boundary

For η(t)=diag(t^3,t^−1,t^−1,t^−1), a supported monomial has
weight 3a−m+4j. Strict 3a>m sends every projected padded form
to zero, so every positive-degree invariant vanishes on it.
Exactness then makes all its positive-degree invariant coordinate
pieces zero.

At 3a=m the limit is x0^a*q(0,x1,x2,x3). G-05 supplies the
ternary determinantal closure inclusion; the polynomial block-padding
map preserves that inclusion. Every invariant equation of the
determinant therefore vanishes on every padded restriction. The
invariant-ideal containment has the direction stated and yields
a quotient from the determinant invariant ring to the padded one.
It proves the degreewise inequality, rather than merely comparing
the nonvanishing of a single invariant.

One optional wording repair: replace “identifies its invariant
coordinate ring with the constants in positive degrees” by
“identifies its invariant coordinate ring with C, whose
positive-degree pieces vanish.” The mathematics is unambiguous
from the surrounding proof.

## Concrete cross-check of scope

R-14 proves a four-row multiplicity gap at (m,n)=(15,20)
and at (16,22). G-12 excludes the rectangular label at the
first pair (the equality boundary) and makes every rectangular
padded multiplicity zero at the second pair (strict boundary).
The proven four-row gaps at those two pairs must therefore be
nonrectangular. This does not contradict G-11, whose padded
hypotheses explicitly require n<4m/3.

No mathematical correction was required.

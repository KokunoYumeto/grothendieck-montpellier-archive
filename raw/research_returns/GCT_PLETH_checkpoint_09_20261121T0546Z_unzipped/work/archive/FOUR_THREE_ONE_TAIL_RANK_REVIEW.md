# A-075. Complete independent audit of R-040

**Status: PASS.** Reviewer: GPT-6 Astra Pro; effort not exposed; run
/root/archive_audit. The complete four_three_one_tail_canonical_rank_law.md,
HC.1–HC.18 and all six sections, was read and checked. This event is
a whole-proof check. The report's finite scalar/MN sweeps were not
rerun by this agent and are not claimed here.

The range is $m\ge3$, $a\ge m+2$, $n\ge3$, with
$\nu=(4,3,2^{m-3},1)$ and
$\lambda=(an-2m-2,\nu)$. Its first part is at least $m+4$.
The claimed target multiplicity is one, and the actual canonical
image multiplicity is one exactly for $n\ge m+2$.

## 1. The unit bound and the extra finite-row zero

The signed row-power-sum algebra map of R039, independently checked
in A-071, gives the specified equivariant surjection onto
$\Lambda(\mathfrak h_a\otimes T)^{S_a}$ for $\dim T=4$.
The desired transpose is $\gamma=(m,m-1,2,1)$.
Only even exterior degrees of $\Lambda(\Lambda^3T)$ can occur.
Exterior degree zero has paired rows and misses $\gamma$.
Exterior degree four is $(\det T)^3$ and its fourth row is too long.

The actual perfect-pairing maps give

$$
\Lambda^2(\Lambda^3T)
\simeq(\det T)^2\otimes\Lambda^2T^*
\simeq\det T\otimes\Lambda^2T.
$$

Thus exterior degree two is the vertical-two-strip problem with
base $(p+l+1,p+l+1,q+l+1,q+l+1)$. The fourth part one
forces $q=l=0$ and no added fourth-row box. The unequal first
two parts force $p=m-2$ and the first added box in row one;
the remaining box is in row three. This is a valid unique strip
also at $m=3$. The actual exterior Pieri maps followed by Young
projection therefore give the uniform unit upper bound.

For $a=m+1$, $W=\mathfrak h_a$ has rank $m$. Complementation
in the rectangle $(4^m)$ gives
$S_\nu W\simeq(\det W)^4\otimes
S_{(3,2^{m-3},1,0)}W^*$. The four exterior-column pairings
specify the map. The determinant fourth power is trivial on $S_a$,
and the invariant dot product identifies $W^*$ with $W$.
The exact three-column invariant algebra, checked in A-066,
has only tails $(2^j)$ and $(3,2^j)$. It excludes the displayed
tail with a final one, including $(3,1)$ at $m=3$.
This proves the required finite-row vanishing independently of
the value of a candidate vector.

## 2. The tensor, highest weight and exact affine identity

The complementary-minor tensor

$$
A_{ij,kl}=\det(S)(G_{ik}G_{jl}-G_{il}G_{jk}),\qquad G=S^{-1},
$$

is polynomial at singular $S$ by its complementary-minor expansion.
It transforms as $\det^2$ times four contravariant indices.
Contracting it with two third-moment tensors leaves three covariant
and one contravariant indices. In
$F=\mathcal F_{112}^{\,m}-\mathcal F_{121}^{\,m}$, the
$E_{12}$ action sends both terms to the same $\mathcal F_{111}^{\,m}$.
All other raising operators kill the two terms: the only covariant
labels are one and two, while the dual label is already $m$.
The exact weight is
$(2,\ldots,2)+2e_1+e_2-e_m=\nu$.
Centering proves translation invariance and the row sums prove
row-permutation invariance.

The weighted determinant identity has the reported sign and factor.
After centering, the upper-left entry of $R^tB_t$ is $a$,
its bottom first column is zero, and its remaining bottom columns
are the first $m-1$ columns of $S$ followed by $v_t$.
Weighting rows by $1+\epsilon z_{i2}$ for $B_1$ and
$1+\epsilon z_{i1}$ for $B_2$ gives identical fourth-moment
last-column variations, which cancel. The Schur-complement
corrections in the last column are multiples of $S_{:2}$ and
$S_{:1}$; both are among the retained columns because $m\ge3$.
Their determinants vanish separately.

The remaining derivative is

$$
a\left(v_1^t(d\,\operatorname{adj}_S[C_2])e_m
-v_2^t(d\,\operatorname{adj}_S[C_1])e_m\right)=-aF.
$$

Substituting
$d\,\operatorname{adj}_S[M]
=\det S\{\operatorname{tr}(GM)G-GMG\}$
gives exactly the negative of the two stated cofactor contractions.
Polynomiality then extends the identity to singular matrices.

Weighted Cauchy–Binet computes that derivative as the subset sum
with inside weights $\sum_{i\in I}z_{ip}$. Multiplication by $a$
and substitution $z=w-\bar w$ gives
$a\sum_{i\in I}w_{ip}-(m+1)\sum_iw_{ip}$, exactly the
displayed $L_{I,p}$. Thus $D=-a^2F$ with no omitted scalar.

The per-row degree-four cancellation is termwise. Such a term
must use that row's linear entry in $R$, its quadratic last-column
entry in $B_t$, and its own entry in $L_{I,p}$. The two last-column
cofactors coincide; the residual row factors
$w_{i2}w_{i1}^2$ and $w_{i1}(w_{i1}w_{i2})$ coincide.
Their signs and coefficient $a-m-1$ are the same, so the
difference cancels. All other terms have row degree at most three.
Consequently the homogenized polynomial extends for every $n\ge3$.

## 3. Independent derivation of the six specialization entries

For the displayed centered configuration,
$v=e_1+2e_2$, $u=\mathbf1+v$,
$S=I+vv^t+uu^t$, and $\Delta=6m+8$.
The two-column inverse calculation gives

$$
Gv=\frac{(m+12)v-8u}{\Delta},\qquad
Gu=\frac{-8v+6u}{\Delta},
$$

and

$$
Ge_1=e_1-\frac{(m-4)v+4u}{\Delta},\qquad
Ge_2=e_2-\frac{2mv+2u}{\Delta}.
$$

These identities follow directly from
$I+[v,u]^t[v,u]=\begin{pmatrix}6&8\\8&m+12\end{pmatrix}$.
They give, independently of the printed six-entry table,

$$
Gv_1=e_1+\frac{48v-36u}{\Delta},\qquad
Gv_2=\frac{(2m+72)v-52u}{\Delta}.
$$

Since $v_m=0$ and $u_m=1$, their last coordinates are
$-36/\Delta$ and $-52/\Delta$.
The scalar products give
$\operatorname{tr}(GC_1)=(-2m-4)/\Delta$ and
$\operatorname{tr}(GC_2)=(-6m-12)/\Delta$.
Using $C_2=e_2e_2^t+2vv^t-3uu^t$ and
$C_1=e_1e_1^t+vv^t-2uu^t$ then yields

$$
(GC_2Gv_1)_m=\frac{336m+592}{\Delta^2},\qquad
(GC_1Gv_2)_m=\frac{344m+528}{\Delta^2}.
$$

Thus every printed entry is correct. In the expression for $F$,
the combined numerator is
$-120m-160=-20\Delta$, so $F=-20$ and $D=20a^2$.
Appending zero rows preserves these centered moments. The
homogenized highest vector is therefore nonzero in the full range.
Together with the unit upper bound and the exact dehomogenization
injection, this proves target multiplicity one.

## 4. The normalized canonical scalar and every endpoint

For an independent-row functional with zero first moments,
all outside-row weights in HC.10 have expectation zero.
For a fixed inside subset, the two-determinant permutation expansion
gives $(m+1)!$ times the moment determinant. Its upper-left entry
is now one, so the preceding derivative calculation gives
$-(m+1)!F(U,C)$. The fourth moments cancel before specialization,
and the Schur-complement columns again repeat retained columns.

There are $\binom a{m+1}$ subsets and inside coefficient
$a-m-1$. Their product with $(m+1)!$ is exactly $(a)_{m+2}$.
Hence HC.16 is correct. It uses only moments through degree three
after cancellation, so the $n=3$ endpoint assigns no unsupported
fourth moment.

Substituting the normalized split-form moments
$U=-S_n/[n(n-1)]$ and
$C=2C_n/[n(n-1)(n-2)]$ scales $F$ by

$$
\frac{4(-1)^{m-2}}{n^m(n-1)^m(n-2)^2}.
$$

Since $D_{n,m}=-n^2F_{n,m}$, the actual grid-map scalar is

$$
\frac{4(-1)^{m-2}(a)_{m+2}}
{n^{m+2}(n-1)^m(n-2)^2}.
$$

Its transpose-parameter reciprocal is precisely HC.18.
The scalar-one grid normalization, checked in A-065/A-071,
and the dense first-coordinate chart extend this to the global
polynomial identity. All numerators and denominators are valid
in the declared range.

For $a,n\ge m+2$, both generators and the scalar are nonzero,
giving the explicit actual preimage. For $n\le m$, the source
has at most $n$ rows while $\lambda$ has $m+1$ rows. For
$n=m+1$, the exact complementary-column invariant exclusion
from section 1 gives source multiplicity zero. The affine subset
formula agrees: it is empty below $m+1$, and at exactly $m+1$
its inside coefficient and outside sum both vanish.

All maps are rational tensor, exterior-pairing, determinant and
Young maps, compatible with the stated finite-rank transport.
The Chow coordinate-ring interpretation uses the already checked
algebra pullback R037/EP.3–EP.5, rather than an unstated map.
This completes the independent full-proof check of HC.1–HC.18.

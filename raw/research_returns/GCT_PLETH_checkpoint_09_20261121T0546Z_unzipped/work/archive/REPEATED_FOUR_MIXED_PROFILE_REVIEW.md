# A091. Repeated-four mixed tails: complete actual-map audit

**Result: PASS.** The complete R047 report, RF.1–RF.20 and
all five sections, was read, together with its coefficient
verification program. The relevant R046 moment maps, R039
exterior generator/Pfaffian proof, and R036 three-column
surjection were reread. The author accepted and inserted the
stable-character precision described below; that insertion
was then read and checked.

The reviewed report is
work/rectangular/repeated_four_mixed_tail_profile.md.
For
$$
\nu=(4^h,3,2^j,1),\quad
D=4h+2j+4,\quad K=2h+j+3,\quad
r_s=\min\{h,\max(0,s-h-j-3)\},
$$
the finite target multiplicity for inner degree at least four
is exactly $r_a$. The actual canonical image multiplicity is
$\min(r_a,r_n)$ when $a,n\ge4$ and $\max(a,n)\ge K$.
The whole-target statement for $a\ge2,n\ge K$ includes the
zero targets at the smaller values of $a$.

## 1. The entire final row layer and its actual restriction

Set $N=K+1=(D+4)/2$ and take $T=\mathbb Q^4$.
In the ordered-row exterior decomposition of
$C_s=(\Lambda(\mathbb Q^s\otimes T))^{S_s}$, a degree-$D$
term occupying $N$ nonempty rows has
$$
D\ge 2N-e_1\ge 2N-4=D.
$$
Equality forces $e_1=4$ and every other occupied row to have
exterior degree two. Thus $e_2=N-4=2h+j$. These are all
the new terms between row counts $K$ and $N$ in degree $D$.
Their module is exactly
$$
\det T\otimes\operatorname{Sym}^{2h+j}(\Lambda^2T).
$$
There are no changes at any scalar degree below $D$, since
the occupancy bound there is at most $K$.

The actual splitting
$C_s=\Lambda T\otimes B_s$, with
$B_s=(\Lambda(W_s\otimes T))^{S_s}$, has constant term one
in its first factor. Recursive comparison of degrees first
gives equality below $D$, then gives the same displayed
difference in degree $D$ for the two $B_s$.

The proof then uses a specified map. Zero-padding
$W_K\hookrightarrow W_N$ has orthogonal transpose $q$,
and direct coordinate computation gives
$q(P_Ne_i)=P_Ke_i$ for $i\le K$ and $q(P_Ne_N)=0$.
Every exterior row power sum therefore maps with scalar
one to its corresponding generator at row count $K$.
The full finite-row orbit spanning proof makes the
restriction $B_N\to B_K$ surjective. Its kernel has exactly
the character just computed.

The relevant skew-Cauchy highest weight is
$\gamma=(h+j+2,h+j+1,h+1,h)$. The retained Pfaffian and
standard-monomial proof decomposes
$\operatorname{Sym}^d(\Lambda^2T)$ into the shapes
$(P,P,Q,Q)$ with $P+Q=d$. Every kernel summand therefore
has equal first two parts and equal last two parts, whereas
both corresponding gaps of $\gamma$ are one. The actual
restriction has no kernel on this Schur multiplicity space.

The same argument together with R046 stability at $s\ge N$
proves that every restriction from $S\ge s\ge K$ is an
isomorphism on $(S_\nu W_s)^{S_s}$. The ordinary and
exterior realizations use the same Schur morphism $S_\nu(q)$:
the rational tensor projectors commute with every tensor
power of $q$. Choosing $S\ge\max(s,D)$ gives the commuting
identity $p_s=S_\nu(q)p_S$, so the particular ordinary
moment map $p_s$ is faithful. This is the exact map needed
for the canonical-factorization argument.

## 2. Stable multiplicity and the recorded clarification

The free stable generator algebra is
$$
\operatorname{Sym}(\Lambda^2T\oplus\Lambda^4T)
\otimes\Lambda(\Lambda^3T).
$$
Its only possible exterior degrees contributing to the
even scalar degree $D$ are zero, two and four. Exterior
degrees zero and four give determinant twists of paired
shapes and cannot give $\gamma$. The actual contraction
isomorphism
$$
\Lambda^2(\Lambda^3T)\simeq\det T\otimes\Lambda^2T
$$
reduces the remaining contribution to a vertical two-strip
and a determinant shift. The two gaps of $\gamma$ force
the strip to occupy rows one and three. With $l$ additional
determinant generators, the paired starting shape is
$$
(h+j-l,h+j-l,h-l-1,h-l-1),
$$
which is allowed exactly for $0\le l\le h-1$.
These are $h$ distinct multiplicity-one Pieri contributions.

The audit requested one precision: HO.3 is initially a
surjection, so its source count alone would supply only
an upper bound. The revised paragraph supplies the already
available equality argument. At sufficiently large row count,
TM.8 gives the stable row-orbit character as $\Lambda T$
times the displayed free generator algebra. Cancelling
$\Lambda T$ degree by degree through the actual splitting
shows equal source and target characters for HO.3. Its
surjectivity therefore makes it an isomorphism in each fixed
stable degree. This inserted argument was read after editing.
It justifies exactly $h$ copies, with the actual generator
morphism retained.

The primary retained Sarkar source was also reread through
all of §7: Proposition 7.1 and its proof, the three-column
corollary and its proof, Theorem 7.3 labelled
thm-four-columns and its complete proof and final table.
The section theorem counters confirm the numeric locator.
The row $(m_1,m_3)=(1,1)$ gives $m_4=h$ exactly.
Source: work/theta/sarkar/main.tex, public primary archive
https://arxiv.org/src/2610.07929v2.
This is attribution of the established stable count; the
finite restriction and canonical map are checked above and
below through their given morphisms.

## 3. Every finite row count through the perfect pairing

The tail length is $m=h+j+2$. For $s\le m$ the Schur
functor vanishes because $\dim W_s=s-1<m$.
For $s\ge m+1$, write $q=s-h-j-3$. Padding to exactly
$s-1$ rows and complementing in $4^{s-1}$ gives
$$
\nu^c=(4^q,3,2^j,1,0^h).
$$
This follows by reversing the padded list and subtracting
each entry from four, so it includes the exact zero-row count.

The comparison is the perfect column pairing
$$
S_\nu W_s\otimes S_{\nu^c}W_s\longrightarrow(\det W_s)^4.
$$
Column $i$ of the first tensor pairs by exterior multiplication
with column $5-i$ of the other. Their heights add to $s-1$.
Applying the rational Young projectors gives the usual
complementary highest/lowest pairing, which is nonzero.
The induced irreducible Schur map to the determinant twist
of the dual is therefore an isomorphism. The invariant dot
form then identifies the dual with the same Schur functor
on $W_s$. The determinant character is $\operatorname{sgn}$,
so its fourth power is trivial. A fixed rational volume
trivializes that fourth power. These are actual
$S_s$-equivariant maps, not only a dimension identity.

At $q=0$, the complementary shape $(3,2^j,1)$ is excluded
by the proved three-column algebra surjection: its only
possible families are $(2^v)$ and $(3,2^v)$.
For $1\le q<h$, the complement is the same family with
$h$ replaced by $q$. Its stable threshold is
$K_q=2q+j+3$, and
$$
s-K_q=K-s=h-q>0.
$$
The already proved uniform stable layer calculation applies
to this smaller positive parameter and gives multiplicity
$q$. There is no circular finite-profile induction.
For $s\ge K$ the multiplicity is $h$. Combining the dimension,
zero-complement, intermediate-complement and stable ranges
gives exactly $r_s$.

## 4. Homogenization and the full canonical rank

The Young-column inclusion into $S_\nu\mathbb Q^a$ uses
four columns. Every fixed row letter can occur at most once
in each column, hence every corresponding invariant has
separate row degree at most four. For inner degree $n\ge4$,
the inverse highest-space chart
$$
f\longmapsto\left(\prod_i x_i\right)^n
f(y_1/x_1,\ldots,y_a/x_a)
$$
extends polynomially. The stipulated first-row partition
condition is exactly the remaining highest-weight condition.
Thus the target multiplicity is $r_a$.

For $n\ge K$, R046 gives the actual opposite canonical map
in the exact order
$$
h_{a,n}|_\nu=p_n\Psi_n E_a.
$$
The independent-row expectation $E_a$ is injective on the
translation-invariant highest space. The all-degree split
moments give the equivariant triangular automorphism
$\Psi_n$ in generator degrees two through four. Since
$K\ge5$, all its normalized falling-factorial denominators
are nonzero. The final particular evaluation $p_n$ is
faithful by §1. Their composition is injective on the
whole multiplicity space.

The established scalar-one transpose identity therefore
makes $h_{n,a}$ surjective on its whole target. This gives
rank $r_a$ for $n\ge K$. Interchanging $a,n$ gives rank
$r_n$ for $a\ge K,n\ge4$. At every parameter at least
$K$, the profile is $h$, so these ranks agree where both
arguments apply and equal $\min(r_a,r_n)$ throughout RF.3.
For $a=2,3$ the whole-target assertion is the actual zero
Schur component, as its length is at least four.

All maps are rational and natural under the relevant Young
tensor operations. They extend to every characteristic-zero
field, and to every ambient rank that supports $S_\lambda$.
The coherent/local-free, frame-torsor and Chow-coordinate
transport follows the already checked maps cited in §5.

## 5. Independent execution and precise scope

A fresh implementation is saved as
work/archive/check_repeated_four_profile_independent.py;
its receipt is
work/archive/REPEATED_FOUR_PROFILE_INDEPENDENT_RECEIPT.json.
It imports no source implementation.

For each permutation cycle type $\rho$ of $S_s$, it constructs
the actual standard-module exterior character from
$$
\det(1+zg_{W_s})=
\frac{\prod_{\ell\in\rho}(1-(-z)^\ell)}{1+z}.
$$
The four-by-four dual Jacobi–Trudi determinant at the
conjugate shape $\gamma$ gives $\operatorname{tr}(g;S_\nu W_s)$.
An exact rational class average then gives its invariant
dimension. This comparison uses no profile formula internally.

All 168 coefficient cases at $h=1,\ldots,4$,
$j=0,\ldots,3$, $s=2,\ldots,K+2$ pass.
They involve 4,847 literal cycle trace calculations.
Forty finite complementary shapes and their resulting
dimensions also pass, including $q=0$.
These are checks of the finite invariant profile.
The actual canonical rank was audited through the complete
restriction/polarization/substitution factorization, not
inferred from these coefficients.

The author's separate 60 original plethysm/Murnaghan–Nakayama
checks were read with their code and scope, and were not
rerun as part of this receipt. The whole R047 proof and its
revised stable-count paragraph have no remaining mathematical
gate in the stated range.

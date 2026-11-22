# SF-E841 candidate: a common linear factor map for actual companions

**Status:** new derivation, not independently reviewed and not promoted.
The universal argument below is complete as a proposed necessary condition.
Its strictness against *all* previously accepted gates is unresolved. In
particular, the boundary example in section 6 fails an earlier scalar
cross-minor test. No new main-gate movement is claimed for that example or
for the finite searches.

## 1. Exact algebraic setup

Let A be a commutative local complex Artinian algebra with maximal ideal n.
Assume its multiplication through degree two is that of a homogeneous
regular intersection of four quadrics:

\[
 V=\mathfrak n/\mathfrak n^2,\quad \dim V=4,\qquad
 W=\mathfrak n^2/\mathfrak n^3
   =\operatorname{Sym}^2V/Q,\quad \dim W=6.
 \tag{E841.1}
\]

Here Q is four-dimensional and has no common nonzero projective zero.
Write mu for multiplication from V tensor V to W. The regularity
hypothesis has two consequences used below:

* If dim L>=2, then dim mu(VL)>=5, by the complete proof of E840.2.
* If vV has zero image in W, then v=0. Indeed, for nonzero v the
  four-dimensional space vV in Sym²V would equal Q, and the hyperplane
  v=0 would consist of common projective zeros.

Let P_+,P_- be two six-tuples of elements of n² whose initial tuples
P_+^0,P_-^0 in W^6 are linearly independent. Suppose there are actual
m-by-m matrices C_+,C_-,B_j over A, with m>0 and 1<=j<=6, satisfying

\[
 C_\pm B_j=B_jC_\pm=P_{\pm,j}I_m.
 \tag{E841.2}
\]

These are hypotheses about the matrices themselves, not just the scalar
cross-minor consequences. In the geometric application they are exactly
the two companion orders already derived in E836. Arbitrary higher
terms in the algebra, brackets and matrices remain allowed.

Assume some nonzero linear combination P_0=aP_++bP_- has initial
coefficient span of dimension four. Put C_0=aC_++bC_-.

## 2. Even a partial constant pivot is impossible

In fact every matrix C_t=aC_++bC_- for a nonzero pair (a,b) has zero
constant matrix. The initial tuple P_t^0 is nonzero by independence.
Suppose the constant rank of C_t were r>0. Ordinary invertible row
and column operations over the local ring split its unit pivots:

\[
 R C_t S=\begin{pmatrix}I_r&0\\0&C'\end{pmatrix}=:D_t,
 \qquad B'_j=S^{-1}B_jR^{-1},\qquad
 D_\pm=R C_\pm S.
 \tag{E841.3}
\]

Both orders are retained:

\[
 D_t B'_j=B'_jD_t=P_{t,j}I_m,\qquad
 D_\pm B'_j=B'_jD_\pm=P_{\pm,j}I_m.
 \tag{E841.4}
\]

From the first two equalities, the upper-left block of B'_j is
P_{t,j}I_r, and both off-diagonal blocks vanish. Thus the upper-left
block of the plus or minus equation gives

\[
 (D_\pm)_{11}P_{t,j}=P_{\pm,j}I_r.
 \tag{E841.5}
\]

Taking degree-two initial classes uses only the constant matrix
(D_\pm)_{11}(0). Choose one j and a linear functional on W not
vanishing on P_{t,j}^0. Applying it to (E841.5) shows that this
constant matrix is a scalar matrix. The remaining six equations
then show that the entire tuple P_\pm^0 is the same scalar times
P_t^0. Both initial tuples would be proportional, a contradiction.

Therefore C_t(0)=0 for every nonzero direction. In particular

\[
                         C_+(0)=C_-(0)=0.
 \tag{E841.6}
\]

This argument rules out partial unit blocks as well as invertibility.
It uses no quotient of a deformation and makes no flat-base-change claim.

## 3. A rank-four direction determines the common first-order matrix

Apply the equality proof in E840 to C_0. Its cokernel is annihilated
by the six P_{0,j}, whose initial span J_0 has dimension four.
There are no unit pivots by section 2. E840's dimension equality
therefore gives

\[
 C_{0,1}=\ell A_0,\quad A_0\in\operatorname{GL}_m(\mathbf C),
 \qquad J_0=\mu(\ell V),\qquad
 \mu(\ell,-):V\longrightarrow W\text{ is injective}.
 \tag{E841.7}
\]

The suffix 1 denotes the class in n/n². To see the matrix conclusion
explicitly, E840 gives im(C_{0,1})=ell tensor C^m and says that its
constant-source map is injective. Hence its coefficient matrix A_0
is an invertible constant matrix, not merely a matrix of maximal
rank on some quotient.

Set

\[
 \widehat C_\pm=A_0^{-1}C_\pm,\quad
 \widehat C_0=A_0^{-1}C_0,\quad
 \widehat B_j=B_jA_0.
 \tag{E841.8}
\]

The two orders in (E841.2) are again preserved, and the first-order
part of the new C_0 is ell times the identity. The degree-one part
of \widehat C_0\widehat B_j=P_{0,j}I is
ell times \widehat B_j(0). Since ell is nonzero in V, this forces
\widehat B_j(0)=0. Taking degree two next gives

\[
 \mu(\ell,\widehat B_{j,1})=P_{0,j}^0 I_m.
 \tag{E841.9}
\]

Injectivity of mu(ell,-) kills every off-diagonal entry of
\widehat B_{j,1} and every difference of two diagonal entries.
There is therefore a linear form b_j in V such that

\[
 \widehat B_{j,1}=b_jI_m,
 \qquad P_{0,j}^0=\mu(\ell,b_j).
 \tag{E841.10}
\]

The six b_j span V: their products with ell span the four-dimensional
J_0, and mu(ell,-) is injective on the four-dimensional domain.

## 4. The second companion must use the same six forms

Take degree two in the two remaining equations. By (E841.6) and
the vanishing of \widehat B_j(0), there are no constant-times-quadratic
terms. One obtains

\[
             \mu(\widehat C_{\pm,1},b_j)=P_{\pm,j}^0 I_m
                         \quad(1\le j\le6).
 \tag{E841.11}
\]

An off-diagonal entry v of \widehat C_{\pm,1} annihilates every b_j.
Since they span V, mu(v,V)=0, so v=0 by section 1. The same argument
applied to a difference of diagonal entries shows that all diagonal
entries agree. Thus

\[
 \widehat C_{+,1}=\ell_+I_m,\qquad
 \widehat C_{-,1}=\ell_-I_m,
 \qquad P_{\pm,j}^0=\mu(\ell_\pm,b_j).
 \tag{E841.12}
\]

The two linear forms ell_+,ell_- are independent. A proportionality
between them would give the same proportionality between the full
initial tuples, contrary to hypothesis. Consequently the proposed
new necessary condition is

\[
 \boxed{\ P_+^0=\mu(\ell_+,b),\quad
 P_-^0=\mu(\ell_-,b),\quad
 \ell_+,\ell_-\text{ independent},\quad
 b:\mathbf C^6\twoheadrightarrow V.\ }
 \tag{E841.13}
\]

This uses the same b for both tuples and every pencil direction.
It is stronger in formal content than assigning a possibly unrelated
principal line to the image of each rank-four direction.

## 5. Intrinsic tests and exact remaining scope

For every pencil direction one has

\[
 P_{[s:t]}^0=\mu(s\ell_++t\ell_-,b).
 \tag{E841.14}
\]

At each rank-four direction mu(s ell_++t ell_-,-) is injective.
The kernel of P_t^0 is then the same two-plane ker b. The unique
principal line found by E840 is [s ell_++t ell_-], so these lines
form an injective projective line, rather than a constant map or
a rational map of higher degree. Rank drops are allowed precisely
where multiplication by the corresponding nonzero form fails to
be injective. No conclusion about directions of rank at most three
without any rank-four direction is made.

There is a direct exact linear test once a rank-four direction has
passed E840. Choose its unique ell up to scalar and recover the
six b_j uniquely from P_{0,j}^0=mu(ell,b_j). Solve the two ordinary
linear systems mu(ell_+,b_j)=P_{+,j}^0 and
mu(ell_-,b_j)=P_{-,j}^0 in the four coefficients of each ell_\pm.
Their solvability, independence and the common-kernel condition
are invariant under changes of relation basis and local coordinates.
No unknown multiplicity or companion matrix enters this test.

The geometric hypotheses and conclusions remain exactly those of
E840/E836: the specified balanced point-modification category, same
free Artin algebra on torsion and hull quotient, positive equal
multiplicity, coherent finite action, and the already justified
ordinary vanishing and algebraic B-field passage. This is not an
arbitrary point-sheaf or arbitrary complete-intersection theorem.

## 6. Strictness gate and unsuccessful examples

The condition has not yet been shown to cut a new point of the locus
surviving *all* earlier conditions. For example the regular quadratic
intersection

`(y²+xw, z²+xw, w²+x(y+z), yz+x²)`

with transverse bivectors `partial_x wedge partial_w` and
`partial_y wedge partial_z` has generic pencil image xV, of dimension
four. Here is a direct verification so that the example does not rely
on a finite-field search.

There is no nonzero common projective zero. If x=0, the other three
squares force y=z=w=0. Otherwise set x=1. Then y²=z²=-w and yz=-1.
If z=y, one has y²=-1 and w=1, whereas the third equation requires
y=-1/2, a contradiction. If z=-y, one has y²=1 and w=-1, whereas
the third equation becomes 1=0. Thus the four quadrics form a regular
sequence. Their homogeneous Hilbert series is (1+t)^4. The four
classes x²,xy,xz,xw are independent: in any linear combination of
the four defining relations which belongs to xV, the y²,z²,w²,yz
coefficients force all four relation coefficients to be zero.

For the ordered relation pairs (12,13,14,23,24,34), direct
 differentiation followed by these relations gives

\[
\begin{split}
 P_+^0&=x\,(0,-3(y+z),-2x,-3(y+z),-2x,-4w),\
 P_-^0&=x\,(-4x,2y,-2w,-2z,2w,y-z).
\end{split}
\tag{E841.15}
\]

The second tuple has image xV. For a finite parameter t!=0, the
first, third and fifth columns of P_++tP_- supply x² and xw, while
the second and fourth columns have determinant -4t² on xy,xz.
Thus every such direction has rank four and image xV; the pure
minus direction also has rank four and the pure plus direction
has rank three. All rank-four images therefore pass E840 with the
same line Cx and violate the independent-line conclusion (E841.13).

However an earlier scalar cross minor is nonzero. The identities
xw²=w³, x²w²=w⁴, x⁴=w⁴ and x³w=-3w⁴/2 follow directly from the
four quadrics. The determinant of their displayed derivative matrix
reduces to -40w⁴: its expansion is

`4w²(y²+z²)-16wxyz+4x³(y+z)-2x(y+z)(y²+z²)`.

The characteristic-zero complete-intersection Jacobian is the nonzero
top socle, so w⁴ is nonzero. The scalar cross minor between the first
and second tuple entries is

`0*(2xy)-(-4x²)*(-3x(y+z))=12w⁴`.

This example is therefore **not** a strict witness beyond the full
collection of accepted gates. Its purpose is only to distinguish the
formal image condition from the proposed common-factor condition.

The separate exploratory F101 searches preserve all candidates and
filter stages. They are finite searches, not proofs of nonexistence.
The initial weak filter checked dim K(J)=1 without separately requiring
rank mu(ell,-)=4; that insufficient filter is retained with its output.
The subsequent corrected filters impose the full principal-image
condition and the scalar cross minors in degree four. No candidate
from those searches is being asserted to lift to characteristic zero.

The outstanding task is either an actual regular quadratic witness
that passes all earlier gates and fails (E841.13), or a genuinely new
universal argument showing what the combined conditions imply. Until
then, this derivation remains separate and is not counted as main-gate
movement. No successful seed has been constructed.

# SF-E831. Every block must meet enough actual exceptional support

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** independently whole-reviewed by /root and /root/g34_eightfolds;
both mathematical reviews PASS on the frozen draft
`870daf7349d51f72253507005b5048dbf6e3e9e3232d9cbc55175d85d50eed45`.
All reviewers: GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION,
21 November2026. Both new dependencies E829/E830 have also received complete
independent whole-proof reviews. The peer supplied a separate exact
exterior/incidence supplement. This is a
strict blockwise strengthening of their common-space bounds. It supplies
necessary incidence and rank conditions on an actual balanced extension;
it constructs no balanced semiregular object.

## 1. Separate support spaces at the actual vertices

Use the actual coherent extension and its specified coherent finite action
from E830, with actual equivariant blocks

\[
 0\to A\xrightarrow{i}E\xrightarrow{p}B\to0,
 \quad A=A_0\oplus\bigoplus_{a=1}^u L_a^{n_a},\quad
 B=\bigoplus_{b=1}^v M_b^{m_b}.
 \tag{E831.1}
\]

For each actual matrix component e_ab, choose the subspace Z_ab from the
full E830 support table. All that is required in the proof is the two
properties proved there: its diagonal products with reverse degree-one
classes lie in Z_ab, and its entries are killed into degree3 by every
two-vector in Z_ab perpendicular for the wedge pairing. Put Z_ab=0 when
e_ab is zero. Let J be any subset with Ext3(M_b,A0)=0. Define

\[
 Z_a=\sum_bZ_{ab},\qquad Z_b=\sum_aZ_{ab}\ (b\in J),
 \quad w_v=6-\dim Z_v-
       \dim\operatorname{rad}(q_{\mathrm{wedge}}|_{Z_v}).
 \tag{E831.2}
\]

Here v denotes one selected vertex: every positive line block, or a negative
block in J. There is no identification of Z_a and Z_b on different
vertices. Then

\[
 \operatorname{ext}^2_\Gamma(E,E)
      \ge\sum_{a=1}^u w_a+\sum_{b\in J}w_b.
 \tag{E831.3}
\]

This statement depends on the actual extension entries, and not merely on
which Ext1 spaces could be nonzero. A component set to zero does not remove
any diagonal classes in this bound.

## 2. Full proof through the two actual boundary maps

For each selected vertex choose W_v inside Z_v perpendicular complementary
to its intersection with Z_v. It has dimension w_v and intersects Z_v
trivially. Because the allowed functors act trivially on H2(O_X), these
choices are automatically invariant. Take

\[
 D_A=\bigoplus_a W_a\operatorname{Id}_{n_a}
           \subset\operatorname{Ext}^2(A,A).
 \tag{E831.4}
\]

The a-th diagonal coefficient of the image of gamma in Ext1(A,B) is
sum_b e_ab[1] gamma_ba. It lies in Z_a tensor End(C^{n_a}). Thus that
image has zero intersection with D_A, separately on each diagonal.
The map Ext2(A,A) to Ext2(A,E) is consequently injective on D_A.

On d in D_A, the outgoing boundary from Ext2(A,E) in Hom(-,E) is
 i[3]d[1]e. Its (a,b) line component is multiplication of the actual
entry e_ab by the scalar class d_a in W_a. Since
W_a lies in Z_a perpendicular and Z_ab is contained in Z_a, this class
is in Z_ab perpendicular and kills the entry. The A0 target is zero
because d has zero A0 block. Thus all of D_A lies in the actual image I
of Ext2(E,E) in Ext2(A,E).

For the selected negative vertices, take

\[
 D_B=\bigoplus_{b\in J}W_b\operatorname{Id}_{m_b}
           \subset\operatorname{Ext}^2(B,B).
 \tag{E831.5}
\]

The boundary to Ext3(B,A) is e[2]h. For b in J, its line-target components
are killed because W_b lies in every incident Z_ab perpendicular.
Its A0 component vanishes by Ext3(M_b,A0)=0. Hence D_B lifts into
Ext2(B,E).

Project the preceding boundary from Ext1(A,E) to Ext2(B,B). Its b-diagonal
is the sum of reverse degree-one classes multiplied by the actual e_ab
entries, with the specified multiplicity-matrix compositions. The line
terms belong to Z_b tensor End(C^{m_b}). The A0 term is zero by Serre
duality from the same selected vanishing. For each b independently,
normalized matrix trace modulo Z_b kills this boundary and is the identity
on W_b times the identity matrix. Therefore the quotient

\[
 Q=\operatorname{Ext}^2(B,E)\big/
 \operatorname{im}\bigl(\operatorname{Ext}^1(A,E)
                   \to\operatorname{Ext}^2(B,E)\bigr)
 \tag{E831.6}
\]

has dimension at least sum_b in J w_b and injects into Ext2(E,E).
Its quotient there is I, which already contains D_A. The two bounds add.
Every boundary, projection and trace is equivariant. The identity
multiplicity matrices are fixed even if their chosen descriptions are
projective. Finite invariants are exact, and the invariant diagonal lifts
exist by averaging. Thus the same argument proves(E831.3) after invariants.
No spectral-sequence degeneration or vanishing of uncomputed higher
products is used.

## 3. A necessary coverage condition and a weighted edge budget

Suppose the full normalized character is a nonzero multiple of balanced
v_q, with any rational algebraic B field. The reviewed cap rank and full
supplied invariant CY4 adjunction require invariant Ext2 dimension18
under weak semiregularity. Put

\[
 N=u+|J|,\qquad
 \ell_v=\dim Z_v+
       \dim\operatorname{rad}(q_{\mathrm{wedge}}|_{Z_v})=6-w_v.
 \tag{E831.7}
\]

The exact necessary inequality is

\[
 \sum_v\ell_v\ge6N-18.
 \tag{E831.8}
\]

In particular a selected vertex with Z_v=0 contributes six surviving
classes. At most three selected vertices can have no nonzero exceptional
component. Thus at least N-3 selected vertices must actually meet a pair
with Z_ab nonzero. A merely available but unused Ext1 class does not
qualify. This remains true when other vertices have full rank-three
elliptic components: they cannot erase classes at an unrelated vertex.

For an explicit coarse budget put r_ab=dim Z_ab. Since
rad(q|Z_v) is a subspace of Z_v,

\[
 \ell_v\le2\dim Z_v\le2\sum_{ab\text{ incident to }v}r_{ab}.
 \tag{E831.9}
\]

Each pair is incident to its positive vertex, and also to its negative
vertex exactly when b belongs to J. Consequently

\[
 \sum_{a,b}(1+\mathbf1_{b\in J})r_{ab}\ge3N-9
 \tag{E831.10}
\]

is another necessary condition for weak balance. The precise vertexwise
bound(E831.8) is stronger and remains available whenever the actual
subspaces can be computed.

In the opposite-slope setting, numerical cross differences are nonzero.
The table in E830 then has r_ab at most3: a surface index-one component
has r_ab=1, a positive elliptic component has r_ab equal to its actual
kernel coefficient rank, and all harmless pairs have r_ab=0. An active
pair meets at most two selected vertices. If N exceeds3, at least
ceil((N-3)/2) active exceptional pairs are necessary, even allowing
rank-three elliptic entries. More precisely the one- or two-endpoint
weight in(E831.10) should be used when some negative vertices are not in J.
If all active exceptional pairs are surface components, or elliptic
components of coefficient rank at most1, then r_ab at most1 and the
number of pairs must be at least ceil(3(N-3)/2). These bounds are stated
only for N greater than3; for smaller N they give no additional condition.

For the32 distinct line blocks in the E826 example, if all those negative
blocks remain selected, the necessary coarse budgets would be at least15
active maximal elliptic pairs, or at least44 pairs with dim Z_ab=1.
The original E826 pair differences are nondegenerate and have no such
support. These integers are consequences of the general inequality, not
an assertion that the proposed exceptional pairs can be realized while
preserving its full character or its selected unit vanishings.

## 4. Correlated surface directions needed to remove every local class

There is also a useful exact incidence test when dim Z_v is at most3.
Since its radical has dimension at most dim Z_v, w_v=0 implies
dim Z_v at least3. Under this dimension bound it is therefore equivalent
to dim Z_v=3 and q_wedge vanishing identically on Z_v. Such a three-space
is maximal isotropic in the six-dimensional wedge space.

For completeness its elementary classification is as follows. Every
nonzero element z in it is decomposable, because on a four-dimensional
space z wedge z=0 is equivalent to skew rank at most2. Choose two
independent elements a wedge b and a wedge c: their support planes
intersect because their mutual wedge is zero, and independence makes
a,b,c linearly independent. If every support plane contains a, the
three-space equals a wedge V. Otherwise choose a third support plane
not containing a. Its intersection lines with span(a,b) and span(a,c)
are distinct and span it, so it lies in H=span(a,b,c). Its two-vector
has a nonzero b wedge c coefficient, and the whole three-space equals
Lambda2 H. Thus the only possibilities are

\[
 Z_v=a\wedge V\quad(\dim\mathbf Ca=1),
 \qquad\hbox{or}\qquad
 Z_v=\Lambda^2H\quad(\dim H=3).
 \tag{E831.11}
\]

Conversely both displayed spaces are three-dimensional and totally
isotropic, so both give w_v=0. This is a complete linear-algebra proof;
no unproved general-position assertion is used.

In the surface-only case, if at most three independent active support
lines meet a vertex, removing all six diagonal directions therefore
requires their support planes to be of this correlated type: a common
one-dimensional direction, or containment in a common three-dimensional
direction. Two complementary surface planes do not suffice, since their
wedge pairing is nonzero and they leave w_v=4. If more than three
independent support lines meet the vertex, use(E831.2); the above
three-space classification is not silently extended to that case.
These are cohomological support planes from actual degenerate line forms,
not irrational RM eigenspaces. For elliptic entry coefficients a support
subspace may be complex rather than rational; no extra rationality is
inferred from the classification.

## 5. Scope and verification boundary

This result applies only when the actual equivariant filtration and line
blocks are present. E826 and E828 explain when their intrinsic HN/evaluation
arguments provide them; a genuinely nonsplit positive factor is still not
a direct sum by assertion. The selected negative vertices continue to
require the exact Ext3(M_b,A0) vanishing. No numerical count substitutes
for that condition.

The full proof uses the actual-entry support table of E830 and its explicit
finite-isogeny cup-product calculation from E829. The finite-action,
published BF and supplied S21 statuses are exactly those already stated
there. There is no new external classification premise. The exact script
rm_vertexwise_wedge_certificate.py actually passed nine wedge-space tests,
a separately labelled hypothetical six-vertex incidence test, and all97
closed-form budgets for N=4 through100. Runtime was0.0258956120015s.
The initial output-serialization failure for exact SymPy integers is
retained; only an exact-integer JSON encoder was added. These finite
checks supplement the infinite proof above and do not assert geometric
realizability of the hypothetical incidence data. No semiregular seed, period-map rank or generic
extension-product rank is claimed.

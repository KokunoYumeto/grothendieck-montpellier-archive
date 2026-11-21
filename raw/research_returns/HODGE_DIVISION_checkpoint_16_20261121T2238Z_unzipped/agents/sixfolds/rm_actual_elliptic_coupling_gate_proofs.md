# SF-E830. The actual extension class controls elliptic escape directions

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** independently whole-reviewed by /root and /root/g34_eightfolds;
both mathematical reviews PASS on the frozen draft
`dbe5e856356e49ece65aa9a41cb77851a1eac411bfff5088e4090f3fa9f581a4`.
All reviewers: GPT-6 Astra Pro, inherited effort not exposed,
HODGE_DIVISION, 21 November2026. The peer also supplied an independently
written supplementary exact exterior certificate; the infinite theorem
is the complete proof below, not an extrapolation from finite checks. This replaces E827's hypotheses on every degree-one class by
hypotheses on the entries of the actual extension class. It includes the
rank-one directions deliberately outside E829, but gives a necessary rank
gate rather than general nonexistence. An actual full-rank example is
constructed at the end and is explicitly not a balanced RM seed.

## 1. The extension-specific diagonal lemma

Let X be an abelian fourfold and consider the same actual coherent
extension with actual equivariant block decompositions:

\[
 0\to A\xrightarrow{i}E\xrightarrow{p}B\to0,
 \quad e:B\to A[1],\quad
 A=A_0\oplus\bigoplus_a L_a^{n_a},\quad
 B=\bigoplus_b M_b^{m_b}.
 \tag{E830.1}
\]

Write N_ab=L_a tensor M_b inverse. The matrix of the line-to-line
component e_ab has entries in H1(N_ab). Let E_ab be the span of all those
entries; equivalently it is the image obtained by contracting e_ab with
the dual of its multiplicity-matrix space. This definition does not depend
on bases of the two multiplicity spaces or on scalar choices identifying
the lines. It records the particular extension, not the whole Ext1 group.

Let W,Z be subspaces of H2(O_X) with W intersect Z zero. Assume for every
pair:

- the products of E_ab with all of H1(N_ab inverse), in either order,
  belong to Z;
- multiplication by W kills E_ab into H3(N_ab).

There is deliberately no hypothesis about multiplication of W on the
whole reverse group H1(N_ab inverse). Let J consist of any B indices for
which Ext3(M_b,A0)=0. Then

\[
 \operatorname{ext}^2_\Gamma(E,E)\ge(\dim W)(u+|J|).
 \tag{E830.2}
\]

Here u is the number of positive line blocks, and the finite coherent
action is required to preserve the actual sequence and blocks, as in
E827. No such decomposition of the middle object is asserted.

We prove the altered hypothesis suffices, retaining every boundary map.
The diagonal identity subspace D_A=direct sum_a W Id_n in Ext2(A,A) is
fixed by the action. The kernel of Ext2(A,A) to Ext2(A,E) comes from
Ext1(A,B). Its a-th diagonal is the sum of e_ab[1] gamma_ba. Every
coefficient contains an entry of the actual e_ab and a reverse degree-one
class, and is therefore in Z. Thus D_A injects. Its outgoing boundary in
Hom(-,E) is i[3]d[1]e. Every line-target component is multiplication of an
entry of e_ab by the corresponding W identity class. The second hypothesis
kills exactly these entries; no other reverse Ext1 class occurs in this
boundary. Consequently the image I of Ext2(E,E) in Ext2(A,E) contains D_A.

For the B-side, take D_B=direct sum_b in J W Id_m inside Ext2(B,B).
Its boundary to Ext3(B,A) is e[2]h. Again only entries of the actual e_ab
are multiplied by W. They vanish by the second hypothesis, while the A0
component vanishes by the defining condition on J. Thus D_B lifts to
Ext2(B,E).

The preceding boundary from Ext1(A,E), projected to Ext2(B,B), is
(p[1]alpha)[1]e. Its selected b-diagonal is a sum of reverse degree-one
classes multiplied by entries of e_ab. All such coefficients lie in Z.
The possible A0 term is zero because Ext1(A0,M_b) is dual to
Ext3(M_b,A0). Normalized diagonal matrix trace modulo Z therefore kills
this boundary and detects the lifted W identities. It follows that the
quotient Q of Ext2(B,E) by this boundary has dimension at least dim(W)|J|
and injects into Ext2(E,E). Its quotient there is I, which already
contains D_A. These contributions add.

All the actual maps are equivariant. H2(O_X) is fixed under translations
and degree-zero tensor functors, and conjugation fixes identity matrices
and normalized trace, including projective multiplicity descriptions.
Invariant lifts are obtained by averaging; taking invariants is exact.
The same dimension sum proves(E830.2) in the specified finite-action
scope. This is an actual triangle calculation, with no formality or
higher-product vanishing assumption.

## 2. A support space for the actual entries, in every positive rank

For each difference with nonzero first Chern class, use the Riemann-form
product isogeny and cohomology identification proved in E829:

\[
 f:C\times K\to X,\qquad f^*N=N_C\boxtimes P_K,
 \quad V=H^1(O_X)=V_C\oplus V_K.
 \tag{E830.3}
\]

The complement is fixed by the polarization. Pullback on the line
cohomology is injective and products commute with pullback. If P_K is
nontrivial, all the groups vanish; also omit a pair whose actual component
e_ab is zero. For the remaining cases define a subspace Z_ab of Lambda2 V
as follows.

For rank(N) at least3, put Z_ab=0. For rank2 with surface index0 or2,
also put Z_ab=0. The complete calculations in E829 show in these cases
that the products of all degree-one classes with their reverses are zero
and all H2(O_X) kills degree1 into3. Thus these choices satisfy the new
entry-specific conditions a fortiori.

For rank2 with surface index1, put

\[
 Z_{ab}=\Lambda^2V_C.
 \tag{E830.4}
\]

The degree-one product lies in this line. Any w0 orthogonal to this line
under the four-dimensional wedge pairing has zero Lambda2 V_K component,
so it kills every pulled-back entry of e_ab into degree3. This is the
same surface calculation as E829, now ignoring zero actual components.

For rank1 with elliptic index0, the pulled-back entries lie in
H0(N_C) tensor V_K, with dim V_K=3. Define S_ab to be their coefficient
span in V_K:

\[
 S_{ab}=\operatorname{im}\left(
   H^0(N_C)^*\otimes E_{ab}\longrightarrow V_K\right),
 \qquad Z_{ab}=V_C\wedge S_{ab}.
 \tag{E830.5}
\]

The displayed contraction includes all matrix entries of e_ab. If the
pullback is not onto all line cohomology, only the pulled-back entries are
used. Thus no unproved surjectivity of an isogeny pullback is required.
The span is basis independent. Degree-one classes of the inverse line
pull back to H1(N_C inverse) tensor C. Their products with the entries of
e_ab lie in V_C wedge S_ab, by the elliptic Serre pairing. If w0 is
orthogonal to Z_ab under wedge pairing, then

\[
 (\operatorname{pr}_{\Lambda^2V_K} w_0)\wedge s=0
       \quad\hbox{for every }s\in S_{ab}.
 \tag{E830.6}
\]

This is precisely the condition that multiplication by w0 kills the
pulled-back entries H0(N_C) tensor S_ab into H0(N_C) tensor Lambda3 V_K.
All terms of w0 containing V_C raise the C index and vanish. Finite trace
then gives both the product containment and the required entry vanishing
on X itself.

For rank1 with elliptic index1, put

\[
 Z_{ab}=V_C\wedge V_K.
 \tag{E830.7}
\]

Here the entries lie in H1(N_C) tensor C, and their reverse degree-one
classes lie in H0(N_C inverse) tensor V_K. Products lie in the displayed
three-space. That space is maximal isotropic for the wedge pairing and
is its own perpendicular. Consequently its perpendicular has zero
Lambda2 V_K component and kills the entries into degree3. This case
may contribute no surviving space, but it still satisfies the theorem.
In the opposite-slope architecture a rank-one difference has positive
polarization degree and therefore elliptic index0; index1 is included
only for the stated general extension lemma.

These computations exhaust every nonzero numerical difference. A
numerically trivial but nontrivial flat difference is acyclic and can
also be ignored. For completeness, if N is the trivial line, put
Z_ab=E_ab wedge V, where E_ab is now a subspace of V. Then the product
containment is literal exterior multiplication. Orthogonality to Z_ab
means w0 wedge xi wedge v=0 for every xi in E_ab and v in V, equivalently
w0 wedge xi=0 in Lambda3 V. It therefore kills those actual entries.
A nonzero trivial-line extension may again force a zero bound; no
opposite-slope application relies on this case.

## 3. The uniform wedge formula and its elliptic rank consequence

Set

\[
 Z_e=\sum_{a,b}Z_{ab},\qquad z_e=\dim Z_e,\qquad
 \rho_e=\dim\operatorname{rad}(q_{\mathrm{wedge}}|_{Z_e}),
 \quad w_e=6-z_e-\rho_e.
 \tag{E830.8}
\]

The product calculations show that all incoming products containing the
actual entries lie in Z_e, and Z_e perpendicular kills all those entries
into degree3. Choose a complement W to Z_e intersect Z_e perpendicular
inside Z_e perpendicular. Then W intersects Z_e trivially and dim W=w_e.
All these cohomological subspaces are fixed under the allowed functors,
which act trivially on H2(O_X). This does not require a choice of
individual linearizations of the line bundles. Applying section1 gives

\[
 \operatorname{ext}^2_\Gamma(E,E)\ge w_e(u+|J|).
 \tag{E830.9}
\]

Under the full balanced character and the same supplied invariant CY4
adjunction as E826/E827, weak semiregularity therefore requires
w_e(u+|J|) at most18. The rational algebraic B field acts by the already
proved invertible shear and changes none of these cap dimensions.

Suppose all the nonzero exceptional components are positive elliptic
components along a single fixed elliptic support direction V_C; every
other pair is one of the harmless cases above. Let S be the sum of their
coefficient spans in the common three-dimensional V_K, with r_e=dim S.
Then Z_e=V_C wedge S is totally isotropic, of dimension r_e, and

\[
 w_e=6-2r_e.
 \tag{E830.10}
\]

Thus ranks0,1,2,3 give respectively6,4,2,0 surviving classes per selected
block. In particular, if u+|J| is at least10, weak balanced semiregularity
in this precise situation requires r_e=3. If u+|J| is between5 and9,
it requires r_e at least2. If u+|J| is4, it at least requires a nonzero
elliptic component. These are necessary statements about the actual
extension matrices; choosing a possible Ext1 space of large dimension
does not meet them by itself.

## 4. An actual full-rank elliptic extension, with its exact limitation

The last rank condition can be realized by an actual ordinary gluable
object. This example records the boundary of the method and is not a
balanced RM construction. Take X=C times K, with C an elliptic curve and
K any abelian threefold. Let N_C have degree3 and put N=p_C^*N_C.
Riemann--Roch and the elliptic index theorem give h0(N_C)=3. Choose a basis
s1,s2,s3 of H0(N_C), and a basis eta1,eta2,eta3 of H1(O_K). Then

\[
 e=s_1\otimes\eta_1+s_2\otimes\eta_2+s_3\otimes\eta_3
       \in\operatorname{Ext}^1(O_X,N)
 \tag{E830.11}
\]

defines an actual locally free extension

\[
 0\longrightarrow N\longrightarrow E_e\longrightarrow O_X
 \longrightarrow0.
 \tag{E830.12}
\]

Local freeness follows because the quotient is free over every local ring,
so the sequence splits there. Equivalently an actual additive Cech cocycle
for e gives upper triangular transition matrices. Their strictly upper
blocks square to zero, so no additional Maurer--Cartan condition is needed.
The object is coherent and hence has no negative self-Ext. Its coefficient
span S is all of H1(O_K), so r_e=3 exactly.

It is indecomposable. Hom(N,O_X)=0, so every endomorphism preserves the
subline N. Restrictions to N and O_X are scalars a,b with ae=eb; e nonzero
forces a=b. The kernel is Hom(O_X,N)=H0(N_C), a square-zero ideal, and all
common scalar identities lift. Thus End(E_e) has quotient C by a square-zero
ideal of dimension3 and has no nontrivial idempotent, by the same direct
idempotent calculation used in E826. No simplicity is claimed.

Since c1(N)^2=0, its entire character is

\[
 \operatorname{ch}(E_e)=1+e^{c_1(N)}
       =2e^{c_1(N)/2}.
 \tag{E830.13}
\]

It is a pure exponential character, not the balanced RM character with
cap rank18. No weak semiregularity or finite action is asserted for this
example. Its purpose is only to demonstrate that the required full-rank
elliptic component is attainable by an actual indecomposable extension;
the numerical and categorical balanced seed gate remains open.

## 5. Sources and check boundary

The exact triangle proof in section1 is given in full and differs from
E827 only in following the actual entries instead of the whole Ext1 group.
The rational Riemann-form product isogeny and finite-trace product descent
are the full E829 proof. The sole new elliptic ingredients are the original
Mumford index theorem, ordinary curve Serre duality and elliptic
Riemann--Roch, used in the elementary forms written above. Previously read
published BF and supplied S21 retain their exact original scopes. No
uncomputed generic rank, dg formality, constructed finite action or
semiregular seed is assumed. This is a symbolic proof with a direct actual
extension example, not a numerical computation claim.

# The actual diagonal quotient of the frame product ideal

## T-049. All-degree equality and a factored character

Work over \(\mathbf Q\). Let \(m\ge3\), \(1\le r\le m-2\),
\(F=\mathbf Q^r\), and \(E=\mathfrak h_m\). In
\(S=\operatorname{Sym}(E\otimes F)\), put
\[
I_i=(\ell_i\otimes F),\qquad \ell_i=e_i-\tfrac1m\mathbf1,
\qquad P_k=\prod_{i=1}^m I_i^k,
\qquad J_k=\bigcap_{i=1}^m I_i^k.
\tag{DP.1}
\]
For every \(k\ge0\), there is an actual
\(S_m\times GL(F)\)-equivariant isomorphism
\[
\boxed{P_k=J_k\simeq
\left(\bigotimes_{i=1}^m\operatorname{Sym}^{\ge k}F\right)
\big/\left(\sum_iY_{i1},\ldots,\sum_iY_{ir}\right)
\left(\bigotimes_{i=1}^m\operatorname{Sym}^{\ge k}F\right).}
\tag{DP.2}
\]
The quotient in (DP.2) is a module quotient inside the polynomial
ring on all \(m\) blocks. Its map to \(S\) substitutes the
\(i\)-th block by \(\ell_i\otimes F\); the image is exactly
the product ideal. The displayed diagonal linear forms form a
regular sequence on the tensor product module. Their Koszul complex
therefore gives an actual finite equivariant resolution of this
quotient.

In particular, \((J_k)_N=0\) for \(N<mk\). For a permutation
\(g\in S_m\) with cycle lengths \(c_1,\ldots,c_v\), its full
graded \(GL(F)\)-character on the ideal is
\[
\boxed{\operatorname{ch}_X(g\mid J_k)
=\prod_{a=1}^r(1-X_a)
\prod_{j=1}^v\left(\sum_{t\ge k}
h_t(X_1^{c_j},\ldots,X_r^{c_j})\right).}
\tag{DP.3}
\]
This equality holds in every polynomial degree. The exterior factor
in (DP.3) is evaluated by the exact Koszul complex; it is not
discarded. No assertion of a universally positive Schur-coefficient
formula is made here.

The case \(r=m-2\) is the frame model in G-027. The result strengthens
its high-degree product/intersection equality by giving the actual
diagonal quotient and proving saturation in every degree.

## 1. The independent-block ring and its exact restriction complex

Set
\[
R=\mathbf Q[Y_{ia}:1\le i\le m,1\le a\le r],\qquad
\mathfrak a_i=(Y_{i1},\ldots,Y_{ir}),\qquad
D=\prod_i\mathfrak a_i^k.
\tag{DP.4}
\]
For \(k\ge1\), the variables are disjoint, so a monomial belongs
to \(D\) exactly when its degree in each block is at least \(k\).
Thus \(D=\bigcap_i\mathfrak a_i^k\), and its underlying graded
module is the tensor product in (DP.2).

For a nonempty subset \(A\), let
\(R_A=R/\sum_{i\in A}\mathfrak a_i^k\). The signed restriction
maps give a resolution of \(R/D\) in cohomological degrees
\(0,\ldots,m-1\):
\[
0\longrightarrow R/D\longrightarrow
\bigoplus_{|A|=1}R_A\longrightarrow\cdots
\longrightarrow R_{\{1,\ldots,m\}}\longrightarrow0.
\tag{DP.5}
\]
For a monomial outside \(D\), let \(B\) be the nonempty set of
blocks in which its degree is below \(k\). Its terms in (DP.5)
are precisely the cochains of the simplex on \(B\). Inserting
the least element of \(B\), with its ordered sign, contracts this
augmented simplex. A monomial in \(D\) has no terms. The direct
sum of these contractions proves exactness. Frame permutations act
by reordering the subset with the corresponding orientation sign;
this makes every differential \(S_m\times GL(F)\)-equivariant.

Write \(L_a=\sum_iY_{ia}\) and \(L=(L_1,\ldots,L_r)\).
Then \(R/(L)=S\), by the linear map \(e_i\mapsto\ell_i\).
If \(A\) is proper, choose one block \(i_0\notin A\).
Replacing its variables by \(L_a\) is an invertible linear change
of variables and does not change the relations in the selected
blocks. Consequently
\[
R_A\simeq B_A[L_1,\ldots,L_r]
\tag{DP.6}
\]
for an explicitly given ring \(B_A\). Its Koszul homology for
\(L\) is therefore zero in every positive homological degree.

## 2. The Koszul–restriction bicomplex and the degree check

Tensor the resolution (DP.5) with the free Koszul complex
\(K_R(L)\). Put the restriction term for subsets of size \(s\)
in cohomological degree \(q=s-1\), and a Koszul homological term
of degree \(i\) in cohomological degree \(-i\). The total degree
is \(q-i\).

First taking restriction cohomology identifies this bounded
bicomplex with \(K_R(L;R/D)\). First taking Koszul homology gives
the following complete list of possible positions:

* For every proper subset, only \(i=0\) survives, hence total
  degree \(q\ge0\).
* For the full subset, \(q=m-1\) and \(0\le i\le r\), hence
  total degree at least \(m-1-r\ge1\).

There are no first-page entries of negative total degree, and no
later page can acquire such an entry. Thus the total cohomology in
every negative degree is zero. Equivalently,
\[
\operatorname{Tor}_{i>0}^R(R/D,S)=0.
\tag{DP.7}
\]
This proof also establishes (DP.7) at \(r=m-1\), although
saturation below will use \(r\le m-2\).

The exact sequence \(0\to D\to R\to R/D\to0\) now gives
\[
0\longrightarrow D/LD\longrightarrow S\longrightarrow
(R/D)\otimes_RS\longrightarrow0,
\qquad
\operatorname{Tor}_{i>0}^R(D,S)=0.
\tag{DP.8}
\]
The first map is literal substitution and its image is \(P_k\),
so it proves the quotient isomorphism in (DP.2).

For completeness, positive Koszul homology vanishing here implies
that the ordered linear sequence is regular on \(D\). This follows
by induction on its length. Regard the final Koszul complex as the
mapping cone of multiplication by the last linear form on the
preceding one. The resulting exact homology sequence says that this
linear form acts surjectively on every positive homology module of
the preceding complex. These modules are finitely generated and
bounded below in degree, so graded Nakayama forces them to be zero.
Induction proves regularity of the preceding sequence, and the same
exact sequence proves injectivity of the last form on its zeroth
homology. This also supplies a direct algebraic proof of the
regular-sequence assertion, rather than an inference from Euler
characteristics.

All constructions used above are equivariant. The span of the
\(L_a\) is the trivial \(S_m\) representation tensored with
\(F\), the maps are induced by its inclusion into \(R_1\), and
the tensor and restriction differentials carry the ordinary Koszul
and ordered-subset signs. The coordinate choice in (DP.6) proves
vanishing; it is not used to define any equivariant map.

## 3. Saturation in every degree

We prove the exact local-cohomology bound needed for saturation.
For one block ring \(A_i=\operatorname{Sym}F\), its ideal
\(D_i=\mathfrak a_i^k\) has no local cohomology below degree one.
Indeed it has no element killed by a power of its homogeneous
maximal ideal. The same assertion follows immediately from the
Čech complex or from \(0\to D_i\to A_i\to A_i/D_i\to0\).
The block Čech complexes tensor over \(\mathbf Q\), and their
tensor is the Čech complex for all variables on \(D\). The
Künneth formula for complexes of vector spaces consequently gives
\[
H^j_{R_+}(D)=0\quad(j<m).
\tag{DP.9}
\]
Only this vanishing is needed; no Cohen–Macaulay assertion is being
made.

For a regular homogeneous linear form, the local-cohomology sequence
of \(0\to M(-1)\to M\to M/LM\to0\) lowers this vanishing
bound by at most one. Apply it successively to the regular sequence
proved in §2. Under (DP.8),
\[
H^j_{S_+}(P_k)=0\quad(j<m-r),
\tag{DP.10}
\]
in particular for \(j=0,1\), since \(r\le m-2\).
Čech local cohomology is unchanged by regarding an \(S\)-module
as an \(R\)-module along the quotient: the images of the full
variable set generate \(S_+\).

The ideal sequence in \(S\), together with (DP.10), gives
\(H^0_{S_+}(S/P_k)=0\). This is precisely saturation: a class in
\(S/P_k\) is killed by a power of \(S_+\) exactly when its
representative lies in \(P_k^{\mathrm{sat}}\). Thus \(P_k\)
is saturated.

To identify its sheaf with \(J_k\), take any nonzero point of
\(\operatorname{Spec}S\). At most \(m-2\) of the ideals
\(I_i\) vanish there, because any \(m-1\) frame vectors span
\(E\). Their vectors are independent, so their variable blocks
can be made disjoint. The other ideals become units. Intersection
and product of the specified powers then agree by monomial block
degrees. Each \(I_i^k\) is saturated, since a complementary
variable preserves membership in that block power. Their
intersection is saturated. Thus the two saturated ideals with the
same ideal sheaf are equal, proving \(P_k=J_k\).

At \(k=0\), all ideals and tensor modules in (DP.2) are the full
rings, and the same quotient is the ordinary polynomial quotient
by the diagonal subspace. This proves that endpoint directly.

## 4. Factored character and rank-five coefficient formula

The regular Koszul resolution of (DP.2) has terms
\(D\otimes\Lambda^jF\), with the degree of each exterior
generator counted as one. Its Euler character supplies the factor
\(\prod_a(1-X_a)\). A cycle of length \(c\) permuting tensor
factors of \(D\) has trace
\(\sum_{t\ge k}h_t(X_1^c,\ldots,X_r^c)\): only equal basis
elements around the cycle contribute to the tensor trace. This
proves (DP.3) with the stated actual resolution.

It can also be checked directly against G-027. For a stable subset
of cycles, its Euler sign times orientation is minus one per
selected cycle. Summing all subsets factors into the difference
between the full symmetric algebra and its degree-\(<k\)
truncation for each cycle. The artificial empty-complement term has
degree at most \(m(k-1)+r\le mk-2\), and terms with a complement
of size one have degree at most \((m-1)(k-1)\). They contribute
nothing in degrees \(N\ge mk\). This recovers the same factored
formula from the already verified restriction complex.

For \(m=5,r=3\), let \(\rho=(2,1,0)\), and for cycle lengths
\(c=(c_1,\ldots,c_v)\) define
\[
C_{c,k}(\beta)=\#\left\{(z_{ja})\in\mathbf Z_{\ge0}^{v\times3}:
\sum_a z_{ja}\ge k\ (1\le j\le v),\quad
\sum_j c_jz_{ja}=\beta_a\ (1\le a\le3)\right\}.
\tag{DP.11}
\]
It is zero if any \(\beta_a<0\). These are explicit bounded
integer polytopes with at most fifteen variables. Expanding the
Weyl determinant and the exterior factor in (DP.3) gives
\[
\boxed{\operatorname{tr}\left(g\mid
\operatorname{Hom}_{GL_3}(S_\alpha F,(J_k)_{|\alpha|})\right)
=\sum_{\sigma\in S_3}\sum_{\delta\in\{0,1\}^3}
(-1)^{\sigma+|\delta|}
C_{c,k}(\alpha+\rho-\sigma\rho-\delta).}
\tag{DP.12}
\]
Indeed the coefficient of \(X^{\alpha+\rho}\) in the product
of the Schur character and \(\det(X_i^{3-j})\) is its
\(S_\alpha\) multiplicity. Distinct dominant weights have
distinct strictly decreasing leading exponent vectors; the
alternant expansion proves the coefficient statement directly.

For a balanced input \(\lambda\vdash5n\), use
\(\alpha=(\lambda_2-\lambda_5,\lambda_2-\lambda_4,
\lambda_2-\lambda_3)\), \(k=\max(0,\lambda_2-n)\), and
the exact \(\operatorname{sgn}^{\lambda_2}\) transport in
G-027. Pairing (DP.12) with the seven ordinary \(S_5\)
character rows therefore evaluates every outer Schur plethysm
coefficient in rank five. It retains explicitly displayed signs;
it is an evaluated character formula, not a positive coefficient
count. The standalone program `outer5/arrangement_tail_character.py`
implements these literal bounded-table counts and the 48 shifts.

## 5. Powers and the exact normal Rees algebra

The all-degree equality immediately identifies the actual powers:
\[
J_k=(J_1)^k=\bigcap_i I_i^k.
\tag{DP.13}
\]
Here the first equality follows by regrouping the ordinary product
\(\prod_i I_i^k=(\prod_i I_i)^k\), followed by (DP.2) at
\(k\) and at one. All the maps are multiplication inside the
same polynomial ring; no symbolic-power convention is needed.

For an explicit integral-closure proof, choose coordinates splitting
the generators of \(I_i\) from a complementary block. For a
nonzero polynomial \(f\), define \(v_i(f)\) to be its least
total degree in the \(I_i\) block. The lowest homogeneous pieces
multiply without cancellation in a polynomial domain, so
\(v_i(fg)=v_i(f)+v_i(g)\). This extends to a discrete valuation
of \(K=\operatorname{Frac}S\), and
\(I_i^k=\{f\in S:v_i(f)\ge k\}\).
If \(f\in S\) is integral over \(J_k\), its monic ideal
equation has coefficients \(a_j\in(J_k)^j\), hence
\(v_i(a_j)\ge kj\). If \(v_i(f)<k\), the leading power of
\(f\) is the unique term of least valuation, which cannot sum
to zero. Thus \(v_i(f)\ge k\) for every \(i\), proving
\(f\in J_k\). Every power in (DP.13) is integrally closed.

Define the Rees algebra by its specified multiplication embedding
\[
\mathcal R=\bigoplus_{k\ge0}(J_1)^k t^k\subset S[t].
\tag{DP.14}
\]
Extend \(v_i\) to the Gauss valuation \(w_i\) on \(K(t)\)
with \(w_i(t)=-1\): on a nonzero polynomial,
\(w_i(\sum_k f_kt^k)=\min_k(v_i(f_k)-k)\).
Multiplicativity follows by choosing a valuation-one element
\(\pi_i\), putting \(u=\pi_i t\), and multiplying the
nonzero leading polynomials in the residue variable \(u\).
Equation (DP.13) proves the literal intersection identity
\[
\boxed{\mathcal R=S[t]\cap\bigcap_{i=1}^m
\{z\in K(t):w_i(z)\ge0\}.}
\tag{DP.15}
\]
Indeed membership on the right is equivalent to every coefficient
\(f_k\) belonging to every \(I_i^k\). A valuation ring is
integrally closed by the same unique-lowest-term argument for a
monic equation. The polynomial ring \(S[t]\) is integrally
closed: an irreducible denominator would give a negative
irreducible-factor valuation in such an equation. Their intersection
is therefore integrally closed. This proves normality of the actual
Rees algebra (DP.14), with its embedding and action explicitly fixed.

## 6. The smallest necessary auxiliary rank

For an output partition \(\alpha\) in G-027, one can take
\(\dim F=\ell(\alpha)\), rather than always \(m-2\).
The same quotient map proves the statement directly. In the
normal-order calculation the generic matrix of the remaining
\(m-2\) rows now has \(\ell(\alpha)\) columns. A nonzero
maximal minor makes the images of the normal variables independent
linear forms over its fraction field; the polynomial substitution
is injective and preserves least normal degree. The Young complex
still has only twists \(-1,\ldots,-\ell(\alpha)\), all
acyclic on \(\mathbf P^{m-2}\). Cauchy extraction consequently
identifies the same section space by its actual evaluation map.
An empty \(\alpha\) is handled directly: the section is the
constant module at \(k=0\) and zero at positive \(k\).

Thus the rank-five face \(\lambda_2=\lambda_3\) uses only
two columns: its analog of (DP.12) has eight shifts and at most ten
integer variables. If
\(\lambda_2=\cdots=\lambda_{m-1}\), then \(\alpha=(A)\),
where \(A=\lambda_2-\lambda_m\), and the rank-one product is
principal. Put \(\Delta=\prod_i\ell_i\in\operatorname{Sym}E\).
Frame permutations fix this product literally. Multiplication gives
the exact module formula
\[
(S_\lambda\mathbf Q^m)_{(n^m)}
\simeq\operatorname{sgn}^{\lambda_2}\otimes
\Delta^k\operatorname{Sym}^{A-mk}E,
\qquad k=\max(0,\lambda_2-n),
\tag{DP.16}
\]
with a negative symmetric degree interpreted as zero. This recovers
the already proved end-node families T-024–T-028 by an additional
explicit multiplication map. Their positive coinvariant/tableau
formulas apply to the remaining symmetric power; no new historical
coefficient family is asserted here.

## 7. The corresponding graded scheme and action

The Rees algebra is generated over \(S\) by the finite-dimensional
degree-one space \((J_1)_m t\); multiplication of those specified
generators produces every graded piece by (DP.13). Apply the
affine-base Proj construction of **EGA II, 2.4.1–2.4.2, p.28** to this actual graded
algebra. On a chart determined by a nonzero degree-one generator
\(ft\), its ring is
\[
\mathcal R[(ft)^{-1}]_0=S[J_1/f]\subset\operatorname{Frac}S,
\qquad (gt)/(ft)\longmapsto g/f.
\tag{DP.17}
\]
These specified ring inclusions give the morphism to
\(\operatorname{Spec}S\) and the chart transition maps. The
localized Rees algebra is integrally closed by (DP.15); its degree
zero part is integrally closed in its degree-zero fraction field.
Indeed an integral element lies in the localized algebra by
normality and in its degree-zero part by its grading. Hence every
chart (DP.17), and therefore this relative Proj, is normal. This is
proved from its chart rings, without invoking an additional blowup
comparison or an unverified source locator.

The linear frame and column actions on \(Y_{ia}\), together with
\(t\mapsto t\), restrict to the Rees algebra because they
permute the \(I_i\) and preserve each block order. Their explicit
coaction consequently defines the action on this relative Proj
and on all its ideal and quotient modules. This uses precisely the
comodule/action conventions of **SGA 3 I, 4.5 and 4.7.2–4.7.3**
already checked in the common source dictionary. The exact
Koszul–restriction complexes above are complexes of the specified
equivariant modules over \(S\). Resolve their finitely generated
graded terms by the finite equivariant \(S\)-free resolutions
described in G-027. On \(\operatorname{Spec}S\), or after the
exact associated-sheaf construction on \(\operatorname{Proj}S\)
of **EGA II, 2.5.2 and 2.5.4**, these give the actual
coherent-to-vector-bundle comparison used in **SGA 6 VI, 3.3**.
This transport is on those stated bases; it makes no assertion that
pulling the resolutions to the Rees Proj preserves exactness.
The Schur projectors and exterior terms are
the transported operations of **SGA 6 V, 4.2, 4.4 and 4.8–4.9**,
with the actual rational idempotent and tensor-slot maps fixed in
the preceding reports. Thus the representation identities here
are images of the displayed exact complexes under that verified
finite-resolution transport.

## 8. Source and review scope

The exact normal-order substitution, balanced-flag dictionary and
signed restriction complex are G-027. I independently read its
complete proof, including every endpoint, before this extension.
I also opened and read Conca–Herzog, *Castelnuovo–Mumford regularity
of products of ideals*, Theorem 3.1, Lemma 3.2 and Corollary 3.3
on preprint pp.6–7, with their complete proofs:
[arXiv:math/0210065v1](https://arxiv.org/pdf/math/0210065).
Those primary results justify G-027's original high-degree bound.
The present all-degree equality is proved by the explicit
independent-block quotient and Koszul–restriction argument above;
it is not attributed to an unquoted strengthening of that source.
No claim of historical novelty is made.

The archive agent has independently read and checked the complete
proof (DP.1)–(DP.12), including the spectral-sequence support,
regularity, saturation and all action conventions. The direct
rank-five implementation passed all 2198 outer-Schur coefficient
comparisons and 2198 class traces for the 314 partitions of
\(5n\) with at most five rows, \(0\le n\le4\), against
independent cycle-index/Murnaghan–Nakayama calculations. These
include 188 inputs of positive \(k\). It also passed 768 literal
bounded-table enumerations and 1477 zero-trace checks below degree
\(5k\). The exact receipt is
`outer5/ARRANGEMENT_TAIL_RECEIPT.json`, with coefficient rows in
`outer5/ARRANGEMENT_TAIL_CHECK.tsv`. Separately, the archive agent
implemented all selected subsets of G-027 with their orientation
signs and passed 4823 class-trace checks in ranks three, four and
five. Its method does not use (DP.3); the receipt is
`work/archive/FAT_ARRANGEMENT_INDEPENDENT_RECEIPT.json`.

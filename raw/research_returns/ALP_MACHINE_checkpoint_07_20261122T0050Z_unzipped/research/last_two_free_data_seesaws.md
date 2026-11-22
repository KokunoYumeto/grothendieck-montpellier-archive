# AM-R-016: the final two free-data transfers, and all six analytic predicates at lift count two

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 21 November2026UTC.

This finding proves the third analytic predicate for the final two
edges of the concrete genuine tower of R014. Consequently, when m=2,
it supplies the entire `ThetaUnfoldingFreeData` predicate. Together
with R013--015 it gives all six mathematical analytic predicates in
that interpretation. The conclusion concerns freely chosen Schwartz
data. It does not supply the source's arithmetic host constructor,
its prescribed raw Xi maps, an integral row identification, or the
cost difference of DP44.

The point is that these two edges involve only ordinary compact
restriction and rank-zero Fourier--Jacobi periods. There is no
positive-rank unipotent unfolding in this case. We retain the
conjugations, the odd splitting character and the Haar measures.

## 1. Spaces, characters and oriented kernels

Let E/F be the CM extension used by the genuine analytic construction,
with its fixed trace-zero coefficient xi and standard additive
character. Let eta be its chosen unitary odd splitting character,
with restriction epsilon_(E/F) to the base-field ideles. Let mu be
any even splitting character, trivial on the base-field ideles.
The finite conductor of eta is allowed in this analytic assertion.
On the old host its everywhere-unramified pin is obstructed by K028;
K029 supplies that pin on its larger field.

Use the standard rational spaces of R014, with k,m even and t odd.
Put d=t+1. At the final three indices write

\[
 A=X_{m-2}=I_a,\quad B=X_{m-1}=I_b,\quad
 C=X_m=I_c,\qquad b=a+d,\quad c=b+d.
 \tag{R16.1}
\]

Let L be the last positive coordinate line of C and put H=L^perp.
The corresponding vertical spaces and embeddings are exactly

\[
 Y_{m-2}=A\perp(-L),\qquad Y_{m-1}=B,\qquad Y_m=H.
 \tag{R16.2}
\]

Here L and -L have Gram matrices 1 and -1. Thus their dimensions
and signatures agree with R014: the first space in(R16.2) has
signature(a,1), the second is positive of rank b, and the last
is positive of rank c-1. The positive embeddings are the first
summand A, the identity of B, and H into C, respectively.
All the quotients [U(A)], [U(B)] and [U(H)] are compact.

Write theta_(S,T)^(alpha,beta)(g,h;Phi) for the oriented Hom
theta kernel, where alpha is the splitting character attached
to S and beta the character attached to T. Its Hom symplectic
form and action are

\[
 \mathcal B_{S,T}(X,Y)
   =-\operatorname{Tr}_{E/F}\bigl(\xi\operatorname{tr}(Y^*X)\bigr),
 \qquad X\longmapsto hXg^{-1}.
 \tag{R16.3}
\]

The adjoint is taken for the indicated Hermitian forms. We use
the actual compatible global Weil splittings and self-dual
additive measures. Orthogonal sums have product measures and
the tensor product theta distribution. Every automorphic
quotient carries the same fixed Haar measure at each occurrence
below; its total volume is not set to one unless already so
normalized.

The downward operator uses this smaller-first kernel without
conjugation:

\[
 D_{S,T}(\Phi,F)(g)
       =\int_{[U(T)]}\theta_{S,T}(g,h;\Phi)F(h)\,dh.
 \tag{R16.4}
\]

This is R015's convention, and agrees with the actual downward
operator after the source's rank-dependent transpose transport.
We do not replace it by a Hermitian adjoint.

For edge j=m-2, which is even, `car` prescribes characters
(mu eta^(-1),mu) on (Y_(m-2),B). The horizontal pair(A,B)
has characters(mu,mu). For edge j=m-1, which is odd, it
prescribes(mu,mu eta^(-1)) on(B,H), while(B,C) has(mu,mu).
Here mu is the character for the particular edge; the two
edge characters need not coincide.

## 2. The one common rank-zero Fourier--Jacobi kernel

On the pair(B,-L) choose a Weil representation with character
eta^(-1) attached to -L. Its other splitting character may be
any character trivial on the base field. Define

\[
 \vartheta_-(g;s)=\theta_{B,-L}(g,1;s),\qquad
 \mathcal J_B(\phi,F;s)
       =\int_{[U(B)]}\phi(g)F(g)
                         \overline{\vartheta_-(g;s)}\,dg.
 \tag{R16.5}
\]

The restriction g->theta_(B,-L)(g,1;s) is independent of that
other splitting character after the standard character-change
identification: changing the character attached to B multiplies
the action of U(-L), and that argument is the identity. Therefore
the same space of kernels(R16.5) can be used on both adjacent
edges even when their mu characters differ.

This is precisely the rank-zero Fourier--Jacobi period: its
unipotent group is trivial, its rational quotient has volume1,
and its auxiliary theta factor is conjugated. The source formula
is `LastSeesawPeriodNonvanishing.lean`, theorem `per_zero`,
lines58--94, together with `fjSrcFun` in
`WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean`,
lines228--233. In the source theta-function model, evaluation of
the transformed theta function at zero is the displayed theta
kernel; it is not evaluation of a bare Schrödinger function.

We require two elementary compatible realizations of this same
auxiliary kernel. First, conjugating the Hom Weil representation
for(B,L) changes L to -L and inverts both splitting characters.
For its character pair(mu,eta), it gives a conjugate-linear
Schwartz isomorphism C_L with

\[
 \theta_{B,L}^{\mu,\eta}(g,1;q)
          =\overline{\vartheta_-(g;C_Lq)}.
 \tag{R16.6}
\]

Second, Hermitian adjoint is anti-symplectic between
Hom(-L,B) and Hom(B,-L). Indeed
tr((Y^*)^*X^*)=overline(tr(Y^*X)), and bar(xi)=-xi;
substitution in(R16.3) changes the sign of the form.
Adjoint also interchanges the two group actions. Composing its
Schwartz transport with complex conjugation therefore gives
a conjugate-linear isomorphism C_ad satisfying

\[
 \theta_{-L,B}^{\eta^{-1},\mu}(1,g;q)
             =\overline{\vartheta_-(g;C_{\rm ad}q)}.
 \tag{R16.7}
\]

Under this conjugate-adjoint exchange the splitting characters
are exchanged, giving(mu,eta^(-1)); they are not both inverted
again. The interchange of source and target determinant actions
cancels those inversions. At a split place the source scalar
is chi_T(det g)^(-1) and the target scalar is chi_S(det h),
which verifies this cancellation directly. At infinity the
auxiliary U(B) vacuum weight is 1/2+h when eta has half-angular
weight h; the two unbarred line kernels in(R16.6)--(R16.7)
both have weight -1/2-h. This also checks the odd baseline.

For completeness, the normalization of(R16.6)--(R16.7) has
no free scalar. Negating one Hermitian form negates the
Heisenberg form; complex conjugation changes psi to psi^(-1),
so the two changes cancel. Adjoint carries rational position
points to rational position points when the polarizations are
transported with it. Hence conjugation commutes with the
rational theta sum. The self-dual measures are transported
at the same time. The linear, quadratic and Fourier generators
of the Weil representation respect these maps; the Fourier
identity is the usual conjugation of its integral kernel.
Thus the equality includes the theta distribution itself,
not just an abstract representation isomorphism.

These are also the exact general theta identities recorded in
`IsWeilDatumConjNegHermitianSpaces.lean`, `weil_conjTarget`,
and `ConjWeilDatumViaAdjointExchangedPairStatement.lean`.
They are used as accepted source identities within their
scope. The Hom computation above explains their identical
normalization for the genuine E/F model without asserting
that the arithmetic D7 record has been constructed.

## 3. Terminal transfer: a positive line and a rank-zero period

Fix a smooth cusp form phi on U(B) and a smooth cusp form F
on U(H). The source's terminal bilinear period is

\[
 \mathcal P_H(f,F)=\int_{[U(H)]}f(\iota h)F(h)\,dh
                 =B_{\rm top}(\overline f,F).
 \tag{R16.8}
\]

Orthogonal factorization C=H perp L, with the character identity
(mu eta^(-1))*eta=mu, gives the exact theta identity

\[
 \theta_{B,C}^{\mu,\mu}(g,(h,1);\Phi\boxtimes q)
  =\theta_{B,H}^{\mu,\mu\eta^{-1}}(g,h;\Phi)
                    \overline{\vartheta_-(g;C_Lq)}.
 \tag{R16.9}
\]

To check factorization, the Hom space is the symplectic direct
sum Hom(B,H) plus Hom(B,L). Its chosen position lattice over F
is the corresponding direct sum; the rational theta sum of a
product is the product of the two absolutely convergent sums.
The tensor Weil action restricts to the displayed product.
The target character multiplication above is exactly its
splitting requirement. This is the standard orthogonal-sum
theta tensor rule, with no index or volume factor.

Fubini on the two compact automorphic quotients now gives

\[
 \boxed{
 \mathcal P_H\bigl(\Theta_{B,C}(\phi;\Phi\boxtimes q),F\bigr)
       =\mathcal J_B\bigl(\phi,D_{B,H}(\Phi,F);C_Lq\bigr).}
 \tag{R16.10}
\]

This equality retains the two fixed Haar measures on both
sides. The vertical kernel is unbarred; only the auxiliary
rank-zero kernel is conjugated.

Suppose the left terminal period is nonzero for an arbitrary
Schwartz input Phi'. Then it is nonzero for some input
Phi boxtimes q with Phi factorizable and real compact-finite,
and q likewise. Here is the needed free-data argument. The
left side is a continuous linear functional of Phi' on the
Schwartz space. At finite places, compactly supported locally
constant functions on a direct sum are finite sums of products.
At real places, finite sums of product Hermite functions are
dense in the Schwartz topology. For the positive spaces B,H,L,
these polynomial-Gaussian functions are finite under the
relevant compact unitary groups. Finite sums of global restricted
pure tensors of such functions are therefore dense. If the
functional vanished on every pure product it would vanish on
this dense span and hence on Phi', a contradiction. Choose one
product on which it is nonzero. Equation(R16.10) then gives the
required nonzero lower Fourier--Jacobi period.

The continuity assertion can be seen directly without an
interchange of a merely formal series. At fixed finite support
and period, the adelic quotients have finitely many charts with
compact real parameters. The rational theta series and all
fixed-order derivatives are uniformly bounded on those charts
by a Schwartz seminorm and a convergent lattice majorant.
Multiplying by the fixed smooth forms and integrating over the
compact quotients is continuous. The finite-place Schwartz
space is the union of these fixed support/period spaces.

## 4. Penultimate transfer: ordinary Bessel restriction

Write V=A perp(-L), as in(R16.2), and fix a horizontal
factorizable compact-finite input Phi' for(A,B). The source
decomposition and the character identity
mu*eta^(-1)=mu eta^(-1) give

\[
 \theta_{V,B}^{\mu\eta^{-1},\mu}((g,1),h;
                                      \Phi'\boxtimes q)
   =\theta_{A,B}^{\mu,\mu}(g,h;\Phi')
                         \overline{\vartheta_-(h;C_{\rm ad}q)}.
 \tag{R16.11}
\]

Let phi be a smooth cusp form on U(A), F one on U(B), and
define the ordinary codimension-one Bessel period by

\[
 \mathcal B_A(\phi,G)=\int_{[U(A)]}\phi(g)G((g,1))\,dg.
 \tag{R16.12}
\]

The Bessel unipotent rank is zero. Thus there is no nontrivial
unipotent character or hidden unipotent volume in(R16.12).
Fubini gives the exact identity

\[
 \boxed{
 \mathcal B_A\bigl(\phi,D_{V,B}(\Phi'\boxtimes q,F)\bigr)
   =\mathcal J_B\bigl(\Theta_{A,B}(\phi;\Phi'),F;
                                                    C_{\rm ad}q\bigr).}
 \tag{R16.13}
\]

If the right side is nonzero for some auxiliary datum s,
it is nonzero for some factorizable compact-finite s. The
same continuity argument applies, now to the auxiliary
Schwartz space alone. Polynomial-Gaussian functions for
the pair(B,-L) are finite under U(B) times U(1), and their
span is dense. Choose one global pure tensor with nonzero
period and take q=C_ad^(-1)s. The induced rational adjoint
transport preserves pure tensors and compact finiteness.
Then Phi' boxtimes q is factorizable and finite under
K_V times K_B. At infinity K_V=U(A) times U(1), and the
diagonal U(B) action on the tensor product of two finite
modules is finite. Equation(R16.13) is the required lower
nonzero Bessel period.

No cuspidality claim for the noncompact group U(V) has been
inserted into Fubini: only its restriction to U(A) is integrated.
For the selected input type, R015 gives vanishing at all
smaller targets and R014 then gives cuspidality of this
actual downward lift. Thus the constructed form belongs to
the genuine cusp domain when that is required by the source.
Independently, the literal free-data predicate quantifies over
every cusp form G equal to this lift; either reading uses
the same identity(R16.13).

## 5. Quantifiers, scope and exact implications

For j=m-1, a nonzero terminal `PerNZ` is(R16.8) and the
existential free datum is supplied by(R16.10) and section3.
For j=m-2, upper `PerNZ` is exactly(R16.5), and(R16.13)
supplies the lower ordinary Bessel period. The `pos` choices
are the actual standard positive embeddings in(R16.2).
The functions in the source `bB` have the conjugation
`Bj(conjAF(phi),F)`; with the ordinary Hermitian first slot
this is precisely the bilinear phi*F convention used here.
More explicitly, in this genuine interpretation the rank-zero
`Pos` datum at the identity embedding B into B is the unique
empty isotropic flag on its zero orthogonal complement. Its
`FJd` is the full Schwartz space for the fixed auxiliary pair
(B,-L), with the cross-character eta^(-1). Thus the existential
upper `PerNZ` ranges over exactly the kernels in(R16.5), rather
than over an unexamined additional class of positions. At the
lower codimension-one Bessel step the isotropic flag is again
empty; the nonisotropic coordinate in the complementary line
does not occur in the rank-zero unipotent character, so every
such coordinate choice gives the same ordinary restriction.
At j=m-1 the source uses the auxiliary conjugated theta
factor, and at j=m-2 the period is independent of any
auxiliary FJ datum because its Bessel unipotent rank is zero.

The conclusion is uniform in the two edge characters mu,
the chosen forms and the nonzero upper period. It does not
assume a special nonzero matrix coefficient or a selected
automorphic multiplicity copy. It therefore proves the
literal mathematical quantifiers of the third predicate at
these final two indices for the genuine model specified here.

When m=2 the set of indices j<m is exactly{0,1}. Consequently
R013--016 cover all six analytic predicates for that model,
provided the stated genuine characters and theta spaces
are supplied. This closes the analytic free-data gate for
lift count2. It does not identify these freely chosen kernels
with the raw arithmetic PhiY/PhiG/Xi family. In particular,
the density argument provides existence and no bound on the
selected finite level, coefficient denominators or norms.

For m>2 the earlier free-data edges still involve genuine
positive-rank Bessel/Fourier--Jacobi unfolding. The accepted
source UpBF/UpFB statements also require their local test-space
package. Those additional edges are not proved in this note.

## 6. Exact locators and check status

- Alpöge, L. (2026). *Remark*, step8, with the stipulated
  pinned archive at commit7cbf7a0c32fca1badf05931879a37c3f8a2b03b4.
  `Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean`,
  `car`114--115, `bB`131--133, `PerNZ`150--152,
  `ThetaUnfoldingFreeData`168--175.
- The same archive,
  `Development/AbelianVarietyTheory/Proofs/TwistedOperators/LastSeesawPeriodNonvanishing.lean`,
  `per_zero`58--94; and
  `Definitions/TwistedInnerProducts/WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean`,
  `fjSrcFun`228--233.
- The same archive, `Proofs/DecoratedLatticeProofs/ThetaTensorRuleTargetOrthogonalSum.lean`,
  `tensorTarget`75ff.; `ThetaTensorRuleOrthogonalSumSourceStatement.lean`;
  `IsWeilDatumConjNegHermitianSpaces.lean`, `weil_conjTarget`71--136;
  `ConjWeilDatumViaAdjointExchangedPairStatement.lean`.
- ALP_MACHINE R013 section1, R014 sections2--4, R015 sections1--2:
  the genuine spaces, actual bilinear conventions, character parity
  and the already checked remaining analytic predicates.

Whole-proof review status: author complete rereading PASS, 2026-11-21T23:56:58.217024+00:00. Independent whole-proof review by /root/definite_oscillator PASS on22November2026UTC, including the saved rank-zero Pos/FJd clarification; see agents/definite_oscillator_review_r016.md and CHECK_EVENTS.tsv. No Lean build is requested or
performed. The new mathematical work is the exact final-two-edge
specialization, the compatible single auxiliary kernel, the compact
Fubini identities and the factorizable compact-finite witness argument.

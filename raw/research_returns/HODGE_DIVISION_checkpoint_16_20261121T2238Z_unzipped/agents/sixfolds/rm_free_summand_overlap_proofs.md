# SF-E825. The surviving first-overlap obstruction after adding free summands

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** independently whole-reviewed by /root and /root/g34_eightfolds;
both mathematical reviews PASS on the frozen draft
`34af017d1f0c49a56b9924c68b923052afc003ba953e62e1ff55f6d811079783`.
The author and root actually ran the local certificate; the peer supplied
an independently written exact certificate. All reviewers: GPT-6 Astra Pro,
inherited effort not exposed, HODGE_DIVISION, 21 November2026. This is a
necessary determinant condition, not a universal exclusion or a construction
of a semiregular seed. The free-summand case is not covered merely by citing
E824; the off-diagonal products below are essential.

## 1. Statement and notation

Let X be the polarized abelian fourfold in the balanced RM setup, with
\(\theta=\theta_++\theta_-\), the two complex rank-two RM planes, and
\(v_q=(1-q\theta_+^2/2)(1-q\theta_-^2/2)\). Let
\(L=\mathcal O_X(D)\), \(D=k\theta\) ample and integral, and let the
ordered global sections f,g of L cut out a smooth integral surface S.
Write \(I=I_S\), \(S_2=(X,\mathcal O_X/I^2)\), and let F be the actual
unit sheaf M0 already constructed, with local model

\[
 F=R^2/(Iv),\qquad v=(-g,f)^t,\quad w=(f,g),\quad
 P:\ R\xrightarrow vR^2\xrightarrow{vw}R^2.
 \tag{E825.1}
\]

Suppose M is a coherent sheaf locally isomorphic to
\(F^{\oplus r}\oplus\mathcal O_X^{\oplus s}\), where r is positive and
s is nonnegative. Its hull H is locally free of rank r+s. Its canonical
quotient \(H/(M/\operatorname{tors}M)=i_*Q\) is locally free of rank r
on S. There is a canonically associated vector bundle \(\widetilde Q\)
on S2 restricting to Q. This bundle is constructed explicitly below; no
extension of an arbitrary bundle on S to S2 is assumed.

For an invariant bivector pi define a homomorphism

\[
 \Psi_\pi:\operatorname{Pic}(S_2)\longrightarrow
 H^1(S,\mathcal O_S(D)^{\oplus2})
 \tag{E825.2}
\]

as follows. If ell_ij are line transition functions on S2, lift them locally
to units near S. In the i-th L-frame the two components of a representative
are \(\{\ell_{ij},f_i\}/\ell_{ij}\) and
\(\{\ell_{ij},g_i\}/\ell_{ij}\), restricted to S. Here
\(\{a,b\}=\pi(da,db)\). This is independent of the lifts because
\(\{I^2,I\}\subset I\). It is a Cech cocycle because the multiplicative
line cocycle holds modulo I squared. Under a normal-frame change
\(f_j=t_{ij}f_i,g_j=t_{ij}g_i\), the extra term has a factor f_i or g_i
and vanishes on S. Changing line frames changes this by a Cech coboundary.
The logarithmic product rule proves that (E825.2) is a homomorphism. We
extend it rationally when needed. A class from X is restricted to S2 first.

If the entire normalized character satisfies
\(e^B\operatorname{ch}(M)=(r+s)v_q\), with B algebraic rational, and M
is weakly G-semi-regular for any specified effective coherent finite action
in supplied S21's scope, then necessarily

\[
 \boxed{\quad
 \Psi_{\pi_\pm}\bigl(\det\widetilde Q+rB\bigr)
       =\frac{7r}{2}\,\Psi_{\pi_\pm}(L).
 \quad}
 \tag{E825.3}
\]

Here pi_+ and pi_- are the two invariant bivectors dual to their rank-two
RM planes. In particular, if the rational determinant class
\(\det\widetilde Q+rB\) is the restriction of a flat line class on X,
then M cannot be weakly G-semi-regular. No finite action on Q, its extension,
or a chosen local direct summand is needed.

If det Qtilde extends to a rational line class A on X, (E825.3) is equivalent
to saying that

\[
 C=c_1(A)+rB-\frac{7r}{2}D
 \tag{E825.4}
\]

has zero mixed blocks and is primitive separately in both RM planes.
Consequently \(\theta^3(c_1(A)+rB)=(7r/2)\theta^3D\). This last
reformulation is only asserted under the stated extension-to-X hypothesis.

## 2. The intrinsic algebra map to the first infinitesimal neighborhood

Work first with one F and one free summand. Every FF block has the form
\(aI_2+vb\), with a in R and b a two-entry row modulo I. Its hull scalar
is a, and its action on torsion is a modulo I. Set

\[
 \ell(aI_2+vb)=a+bv\pmod{I^2}.
 \tag{E825.5}
\]

This is well defined: changing b by an I-valued row changes bv by I squared.
For two FF blocks the nilpotent products vanish on F, and
\((bv)(b'v)\in I^2\); hence (E825.5) preserves multiplication.

A map from F to R is c times the hull row w. A map from R to F is a vector
m represented by \((m_1,m_2)^t\). Put \(p(m)=wm\). Then

\[
 m w-p(m)I_2=v(m_2,-m_1),\qquad
 p(m)+(m_2,-m_1)v=0.
 \tag{E825.6}
\]

Thus every FF map factoring through a free module maps to zero under ell.
These identities also show independence of the chosen representative of m.
The free-free and other off-diagonal blocks map to zero. Taking FF entries
and applying (E825.5) therefore gives an actual unital ring homomorphism

\[
 \mathcal E nd_R(F^r\oplus R^s)\longrightarrow
       M_r(R/I^2).
 \tag{E825.7}
\]

Indeed in each FF block of a product the only extra terms are precisely
factorizations through the free summand, killed by (E825.6). Matrix sums
and the FF multiplicativity complete the proof. A unit maps to a unit.

The fixed ordered global f,g make this compatible with changes of L-frame.
The standard comparison F_j to F_i is scalar t_ij on its generators and
has chain lifts \(t_{ij}^3I_2,t_{ij}^4\) in degrees minus one and minus
two. If a FF block is rewritten using \(v_j=t_{ij}v_i\), its row b
changes by \(t_{ij}^{-1}\); thus bv and (E825.5) are unchanged. Conjugation
by the standard comparisons intertwines (E825.7). Apply (E825.7) to the
actual transition automorphisms of M after these fixed standard comparisons.
Their multiplicative cocycle remains exact modulo I squared. It defines the
vector bundle Qtilde on S2. Modulo I the map is the action on the canonical
quotient Q, proving the claimed restriction. Changing local identifications
of M changes this cocycle by an ordinary change of bundle frames.

## 3. The first Ext trace that survives off-diagonal mixing

The full local computation in UG gives

\[
 \operatorname{Ext}^1(F,F)
   =U\oplus V,\quad U=uF/u(IF),\quad V=T^{\oplus2},\quad
 u=(f,g)^t,\quad T=(R/I)v.
 \tag{E825.8}
\]

Both summands have rank two over R/I. Applying Hom to (E825.1) with target
R gives \(\operatorname{Ext}^1(F,R)=R/I\), represented by the row-pair
\(c u\) modulo Iu. Also \(\operatorname{Ext}^{>0}(R,F)=0\) and
\(\operatorname{Ext}^{>0}(R,R)=0\).

Postcomposing the class cu by a map R to F represented by m gives
\(c u m\). As m varies these classes exhaust U. The reversed product is
in Ext1(R,R), hence zero. Therefore every cyclic trace must kill U; one
cannot retain the full unit-module trace from E824 after adding free terms.

Define a trace on Ext1(F^r plus R^s) by taking, in each diagonal FF block,
its V-component and summing these components. All other blocks map to zero.
This trace is cyclic for every degree-zero endomorphism. On FF blocks,
only the scalar matrix a modulo I acts on positive Ext on either side;
ordinary matrix trace is cyclic. The nilpotent J actions are zero by UG.
An off-diagonal product that returns to FF is exactly a product just shown
to land in U. All remaining products have off-diagonal or free-free target
and have zero trace. This checks all block possibilities and proves
cyclicity, rather than assuming the F summands are preserved.

Consequently conjugation by any actual automorphism leaves this trace
unchanged. Restoring the global twists, V is \(i_*\mathcal O_S(D)^2\).
The standard frame comparison transforms both V coefficients by t_ij,
exactly this bundle transition. The trace therefore glues to an intrinsic
sheaf morphism

\[
 \tau_M:\mathcal E xt^1_X(M,M)\longrightarrow
                  i_*\mathcal O_S(D)^{\oplus2}.
 \tag{E825.9}
\]

This is only a trace on a positive Ext sheaf. No trace on the full derived
self-Hom object, decomposition of M, or invariant local summand is asserted.

## 4. The exact local Poisson deformation and the coefficient seven halves

Use the right-module star product \(a*b=ab+\epsilon\{a,b\}/2\),
with epsilon squared zero. Set P={f,g} and d=vw. A minimal free deformation
of (E825.1) has differentials

\[
 d_\epsilon=d+\frac32\epsilon P I_2,\qquad v_\epsilon=v.
 \tag{E825.10}
\]

Indeed the first-order star product of d and v is
\((-3P/2)v\), which cancels the displayed correction. Its cokernel is
flat over the dual numbers, by the same elementary cycle-lifting argument
used in E823: reduce a cycle modulo epsilon, lift it using the exact
original resolution, and then divide the remaining epsilon cycle and lift
once more. Adding free star modules preserves this assertion.

Let f_j=t f_i, g_j=t g_i on an overlap, and suppress i. Put
\(\alpha=\{t,f\}\), \(\beta=\{t,g\}\),
\(C=f\beta-g\alpha\), \(z=(-\beta,\alpha)^t\).
Then \(P_j=t^2P+tC\). The zeroth-order chain comparison has matrices
\(G_0=tI_2,G_1=t^3I_2,G_2=t^4\). Its first-order failure to be a chain
map in degree minus one to degree zero is

\[
 O_0=t^2\left(\frac32 C I_2+2\{t,d\}\right).
 \tag{E825.11}
\]

This follows by expanding
\(G_0*d_{\epsilon,j}-d_{\epsilon,i}*G_1\): the correction terms give
\((3/2)t^2CI_2\), and the two star-product brackets give
\(2t^2\{t,d\}\). The next failure is
\(O_1=(7/2)t^3\{t,v\}\), and
\(O_0v_j+dO_1=0\), so the projected cochain is a self-Ext1 cycle.
Normalize on the source by G1 inverse to express it in the i-frame.
Since \(CI_2=-z w+v(\alpha,\beta)\) in F-valued columns and
\(\{t,d\}=z w+v(\alpha,\beta)\), its two components are exactly

\[
 \frac{O_0}{t^3}
   =\frac{1}{2t}z w+\frac{7}{2t}v(\alpha,\beta).
 \tag{E825.12}
\]

The first term lies in U and is killed by (E825.9). The second is the
surviving V term. The transition t is that of L inverse, because the
coefficients of sections of L obey f_j=t f_i. Thus the fixed unit-module
contribution is \(-(7/2)\Psi_\pi(L)\), with precisely the sign and
normalization used in (E825.3).

## 5. Arbitrary gluing contributes the determinant of Qtilde

Consider a FF endomorphism \(aI_2+vb\) in a fixed f,g-frame. A chain lift
has higher matrices \((a+bv)I_2,a+bv\). For the local deformation
(E825.10), project its first-order lifting obstruction to V.
For a scalar a, the obstruction is \(\{a,d\}\); writing
\(\alpha_a=\{a,f\},\beta_a=\{a,g\}\) gives
\(\{a,d\}=(-\beta_a,\alpha_a)^tw+v(\alpha_a,\beta_a)\).
Its V-component is therefore \((\alpha_a,\beta_a)\).

For a nilpotent vb, first take b constant.
With \(t_b=bv\), direct multiplication gives the obstruction

\[
 P\bigl(vb-j_bw\bigr),\qquad j_b=(b_2,-b_1)^t.
 \tag{E825.13}
\]

The V-component is P(b1,b2), which equals
\((\{t_b,f\},\{t_b,g\})\) on S. For variable b, the extra terms
are explicit boundaries, as follows. Put

\[
 c=\sum_l\{b_l,v_l\},\qquad
 A_i=v_i c+\sum_l v_l\{b_l,v_i\},\qquad
 B_k=\sum_l v_l\{b_l,w_k\}.
 \tag{E825.13a}
\]

Expanding the two bracket products in the obstruction shows that all
terms differentiating b are exactly \(\frac12 A w+vB\). Each entry
of A lies in I, so Aw represents an element of u(IF), a boundary in
(E825.8). Each entry of B lies in I, so vB is zero in F. This proves
vanishing as an actual Ext class, not just a count of powers of I.
Thus in general the V-component is

\[
 \bigl(\{a+bv,f\},\{a+bv,g\}\bigr)|_S.
 \tag{E825.14}
\]

This also shows directly that it depends only on ell modulo I squared.
For r by r FF matrices the computation is entrywise. After normalization
by an inverse automorphism, its FF scalar matrix modulo I is A inverse,
where A is ell modulo I. Off-diagonal normalization terms are compositions
through a free module and land in U, so contribute no trace. Nilpotent FF
terms act trivially on positive Ext. Hence the normalized V trace is

\[
 \operatorname{tr}\bigl(A^{-1}\{\ell,h\}\bigr)
   =\frac{\{\det\ell,h\}}{\det\ell}
 \quad\hbox{on }S,\qquad h=f,g.
 \tag{E825.15}
\]

The equality is the ordinary determinant derivative identity, proved by
expanding the determinant in permutations and collecting each differentiated
entry with its cofactor. It is valid here for the derivation
\(R/I^2\to R/I\), \(a\mapsto\{a,f\}|_S\), and likewise for g.

For clarity about choices: a change of a local module deformation by a
class beta changes an endomorphism-lifting obstruction by the commutator
with beta. After normalization and the cyclic trace (E825.9), its change
is zero. Changing local nullhomotopies adds a Cech coboundary. These are
the bar-cocycle computations written in E824, now using cyclicity rather
than falsely assuming the whole Ext1 bimodule is central.

As in E824, REnd(M) has cohomology sheaves only in degrees zero, one and
two. The two truncation triangles give a canonical first-overlap map
\(\kappa_M\) from the kernel of the local Ext2 edge map into
\(H^1(\mathcal E xt^1(M,M))\); its kernel is the image of
\(H^2(\mathcal E nd(M))\). The local deformations (E825.10) make the
Hochschild class rho_M(pi) belong to this kernel. The Cech description of
kappa is precisely the obstruction to lifting transition isomorphisms.
Combining (E825.12) with (E825.15) therefore proves the full identity

\[
 \tau_M\kappa_M\bigl(\rho_M(\pi)\bigr)
   =\Psi_\pi(\det\widetilde Q)-\frac{7r}{2}\Psi_\pi(L).
 \tag{E825.16}
\]

It is independent of all the allowed local choices. In particular,
off-diagonal free mixing has been included, not discarded by an assumed
endomorphism decomposition.

## 6. The balanced kernel and the rational B field

First B=0. The two classes
\(\xi_\pm=\pi_\pm+q\eta_\pm\), with
\(\eta_\pm=\pi_\pm\mathbin\lrcorner\theta_\pm^2/2\), annihilate
vq under the full Hochschild cap action. Weak G-semiregularity, the
published BF trace/evaluation identity, and supplied S21's invariant-to-
ordinary compatibility imply \(\rho_M(\xi_\pm)=0\) in ordinary Ext2.
The eta term is in the image of \(H^2(\mathcal E nd(M))\), so its kappa
image is zero. Applying (E825.16) gives (E825.3) for B=0.

For algebraic rational B choose a positive m such that \([m]^*B=m^2B\)
is the Chern class of a line bundle LB. Pull back M by the finite etale
map [m] and tensor by LB. Its normalized character is now the ordinary
balanced character. The pulled-back S is smooth and connected: the
negative-ample Koszul resolution has H0 equal to the constants. Thus it
is integral. The local form remains F' to the r plus a free rank-s bundle;
line tensoring does not change a local free form. The canonical defect
bundle becomes \([m]^*\widetilde Q\otimes LB|_{S'_2}\).

Exactly as in E824, etale Atiyah functoriality and line tensoring transport
the ordinary vanishing of the B-sheared characteristic class. Here
\(\pi' =m^{-2}\pi\) and \(\eta'=m^2\eta\). No statement that
semiregularity itself or the finite action pulls back is made. Applying
(E825.16) on the pulled-back space yields the pullback of (E825.3).
Finite etale trace makes the pullback on these coherent cohomology groups
injective in characteristic zero. It follows that (E825.3) holds on X.

## 7. Nonvanishing and the extension-to-X consequence

For a line class A on X, Psi_pi(A) is the image of its Atiyah class under
\(\Omega_X^1|_S\xrightarrow{\pi}T_X|_S\to N_{S/X}\).
This description follows immediately by differentiating its line cocycles.
For either normal component the Koszul resolution is

\[
 0\to L^{-1}\to\mathcal O_X^{\oplus2}\to L\to i_*L|_S\to0.
 \tag{E825.17}
\]

Ample and negative-ample vanishing on the abelian fourfold gives
\(H^1(S,L|_S)\simeq H^2(X,\mathcal O_X)^{\oplus2}\).
To compute the class, lift a Cech normal component
\(\{\log\ell_{ij},f_i\}\) off S. On a triple overlap its Cech
coboundary is f_i times the contraction of
\(d\log\ell_{jk}\) and \(d\log t_{ij}\), with a fixed sign depending
on the Cech convention. For the g component it is the same scalar class
multiplied by g_i. Under (E825.17), the two components therefore map to
\((c,0)\) and \((0,c)\), where c is the contraction by pi of the cup
product of the two line Atiyah classes. Consequently

\[
 \Psi_\pi(A)=0
       \quad\Longleftrightarrow\quad
       \pi\mathbin\lrcorner(c_1(A)D)=0.
 \tag{E825.18}
\]

Only the kernel assertion is used, so the harmless common nonzero Cech/
Atiyah normalization does not enter (E825.3) or change this equivalence.
In particular \(\Psi_{\pi_\pm}(L)\ne0\), because
\(\pi_\pm\mathbin\lrcorner D^2\) is a nonzero multiple of eta_pm.
Flat classes from X give zero.

For completeness the simultaneous kernel in (E825.18) is computed directly.
Choose a complex unitary basis adapted to the two RM planes, so D is a
positive scalar times the diagonal form and pi_+ uses holomorphic indices
1,2, while pi_- uses 3,4. Write a (1,1) class as the matrix C_ab.
Contraction of C D by pi_+ vanishes precisely when C_11+C_22=0 and
C_13,C_14,C_23,C_24=0. The pi_- equation gives C_33+C_44=0 and
C_31,C_32,C_41,C_42=0. These are exactly the two separate primitive
conditions and absence of mixed blocks. This proves the reformulation
(E825.4), and its stated degree consequence. If the determinant class
plus rB is flat from X, its Psi is zero whereas the right side of (E825.3)
is nonzero, proving the obstruction claimed in section1.

## 8. Exact scope, source boundary, and remaining construction question

The certificate rm_free_summand_overlap_certificate.py was actually run:
PASS,0.094044945seconds internal time. It verifies the corrected minimal
complex, the generic line-frame overlap including its U coefficient1/2 and
V coefficient7/2, nilpotent/scalar obstructions, free-factorization
cancellation, ell multiplicativity and a generic2x2 determinant derivative.
It does not compute global Cech groups or prove a semiregular example.
The local/global mathematical arguments are supplied in full above.

The external inputs are exactly the published BF2008 evaluation/composition
proofs already read for E823/E824: Theorem5.1.3, authorpp24--25;
Proposition5.2.2 and Corollary5.2.3, pp26--27; Proposition6.2.1, pp29--30;
Theorem6.4.2 with Proposition6.4.4, pp31--33. The published article is
Advances in Mathematics217(2008),243--281, DOI10.1016/j.aim.2007.06.013,
author copy https://arxiv.org/pdf/math/0606730 . The vanishing input is
Mumford, Abelian Varieties (1970), section16 printedpp150--153, already
read for E813. Supplied S21 is used solely for coherent invariant evaluation
and ordinary forgetting, at(S21.6) and the compatibility paragraphs
after(S21.7) and before(S21.8). No new preprint theorem or full derived trace is
introduced. E824's truncation/Cech construction is used in its full proved
scope; its centrality hypothesis is replaced here by the explicit cyclic
trace calculation, not silently reused.

When the defect determinant has the required positive degree, (E825.3)
may hold; this proof does not exclude it. It also does not cover matrices
whose rank drops on S, other local torsion/hull models, singular support,
or arbitrary perfect complexes. An actual gluable object with the full
balanced character and this necessary defect determinant would still require
its entire Hochschild evaluation and semiregularity to be checked. Local
first-order deformations alone do not provide that seed.

## 9. Review and exact scope record

Root read the complete original draft, the full variable-b amendment and final wording, then the complete peer report and independent code; PASS. The peer read the entire final proof and all author code, and independently checked all six bivector coefficients with unrestricted coefficient functions, the explicit derivative boundaries, free-factor cancellation, a generic3x3 determinant and the full16-variable primitive/mixed kernel. Its actual computation passed in0.601104seconds. Report: ../g34_eightfolds/bireflection/FREE_SUMMAND_OVERLAP_PEER_AUDIT.md. The root actual author-certificate rerun passed in0.114255109seconds internal time,0.44637168seconds tool wall time. These checks preserve the necessary-condition scope: positive adjusted defect determinants remain a construction gate, and no universal added-free exclusion, finite action or semiregular seed is asserted. No PDF compilation or proof-assistant verification is claimed.

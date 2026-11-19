# Independent audit of the N=6 incidence invariant candidate

**Final status: PASS on the full typed C.3ag proof and its auxiliary Hodge
input.** The initial audit below concerned incidence geometry and boundary
compatibility. Sections 7 and 8 record the subsequent full proof and fresh
primary-source audit, completed at 2026-11-19 09:11:36 UTC. Earlier qualified
stages are retained as check history, not as current unresolved gates.
The entire existing C.3ae proof was also read for the surrounding model
and obstruction.

Let S=W×C be smooth of dimension3, M=O_W(1) external K_C, and a=c1(M).
Three sections s0,s1,s2 have a transverse finite common zero scheme B.
Let H⊂P²×S be Σx_i s_i=0 and let p:H→S. Put h=c1(O_P²(1))|H.

## 1. Geometry: pass

Away from B, the kernel of O_U³→M_U is a rank2 bundle and H_U is its
P¹-bundle of lines. At b∈B the three ds_i form a basis of T*_bS after
trivializing M. At a point (x,b), the differential Σx_i ds_i is nonzero,
since x is a nonzero projective coordinate vector. Hence H is smooth
there as well. H_U is integral. Its complement P²×B has dimension2,
whereas H is a Cartier hypersurface of pure dimension4, so that complement
contains no component. Thus H is integral. The degree of B is M³=48.
The same equations show the strict-transform divisor and exceptional
zero section are transverse in the existing C.3ae construction.
The contraction, finite normalization, unique vertex, strict henselization,
and maximal-ideal pullback arguments are unchanged from that proof.

## 2. The integral CH1 decomposition needs no full Cayley trick

For every smooth parameter P, the complement of H_U×P in H×P has
codimension2. Localization therefore gives an isomorphism of CH¹ groups:
there are no codimension-one cycles supported in that complement.
The projective-bundle formula on H_U×P gives

    CH¹(H_U×P) = p* CH¹(U×P) ⊕ h p* CH⁰(U×P).

Removing B×P from S×P has codimension3, so localization likewise identifies
CH¹(U×P) with CH¹(S×P) and CH⁰(U×P) with CH⁰(S×P).
The displayed summands come from p* and h globally; consequently

    CH¹(H×P) = p* CH¹(S×P) ⊕ h p* CH⁰(S×P)

integrally. The argument is compatible with taking a parameter fibre.
This avoids any unverified application of a Cayley-trick decomposition in
higher codimensions. The exact localization and projective-bundle sources
opened afresh are Stacks Lemma42.19.3, Tag02RX, and Lemma42.36.2,
Tag02TX, including their proofs. H, S and their products here are smooth
finite-type schemes, within these sources' explicit scope.

## 3. Exact pushforwards and boundary invariance: pass

In P²×S, the divisor class of H is h+a and h³=0. By pushing its
intersection with h^j through the ambient trivial P²-bundle, one obtains

    p_*1=0, p_*h=1, p_*h²=a, p_*h³=0.

There is no exceptional-fibre correction: these are identities computed
through the global Cartier embedding. For γ=γ0+hγ1 in CH¹(H×P),

    p_*[(h−2a)(h+a)γ0] = 0,
    p_*[(h−2a)(h+a)hγ1] = −3a²γ1.

Writing τ=4[D_W]−H_W, with deg(τH_W)=0, the further pushforward of
τa²γ1 along W vanishes. Indeed a=H_W+k with k=c1(K_C), k²=0,
τH_W²=0 for dimension reasons, and deg(τH_W)=0 kills the remaining
term 2τH_W k. CH⁰(S×P) consists of constant integers on components.
Thus the invariant

    α ↦ pr_(C×P),* ( τ p_*[(h−2a)α] )

kills every lift ambiguity (h+a)CH¹(H×P) exactly in Pic(C×P), not merely
in its mixed component. Chow localization and the self-intersection
formula therefore define it on CH²(Y×P). All operations commute with
refined pullback to parameter points. A chosen closure before taking
fibres remains an allowed closure afterwards, so this is an actual-family
statement, with no henselized-parameter substitution.

## 4. Source and target formulae: pass

For b=b0+h b1+h²b2 obtained by restricting a fixed closure on Z×P,
the exact pushforward is

    p_*[(h−2a)b|H] = b0−a b1−2a²b2.

Since Pic⁰(W)=0, a divisor on W×C×P is a sum of a fixed divisor D'_W
from W and a line bundle λ from C×P (by the usual Picard/see-saw
argument). Thus

    pr_(C×P),*(τ a b1) = deg(τD'_W) · pr_C* K_C,
    pr_(C×P),*(τ a²b2) = 0.

The correction therefore has constant fibre class in Pic(C), so only
the mixed Hodge component of pr_*(τb0) needs to be killed by the new K3
argument. Finally for θ(λ) obtained from D_W and λ∈Pic⁰(C),

    ρ θ(λ) = deg(τD_W) λ = −9 λ.

The pullback of divisor classes is defined even though p is not flat at B;
no flat pullback of arbitrary cycles through p is used. This typing point
is necessary and is satisfied by the construction.

## 5. Remaining separate source/data check

The proposed Hodge step uses a very general rank2 Picard K3 so that only
its one-dimensional primitive Neron–Severi part contributes. If W is
specified using algebraically independent coefficients, the argument must
justify that this genericity realizes the required Hodge-group statement;
it must not silently assume every exceptional complex Hodge locus is
defined over Qbar. This is a source/genericity point for the separate
root/frobenius audit, not a flaw in the incidence geometry or boundary
calculation certified above.

Audit recorded at 2026-11-19 09:03:58 UTC.


## 6. Conditional Hodge representation argument and three-section rank

Assume the exact source input Hg(T_W)=SO(T_W), where T_W is the rational
transcendental K3 Hodge structure. Because H¹(C) is CM, the derived group
of Hg(T_W direct-sum H¹(C)) contains SO(T_W) acting trivially on H¹(C).
The standard SO representation is absolutely irreducible, so any rational
Hodge substructure of T_W tensor H¹(C) has the form T_W tensor U for a
rational subspace U of H¹(C). Stability under the Hodge circle makes U
a weight1 Hodge substructure. If U is nonzero, its (1,0) part is nonzero,
and T_W^(2,0) tensor U^(1,0) gives a nonzero (3,0) part. Thus this tensor
product has no nonzero level1 Hodge substructure. A rational Hodge class
in T_W tensor H¹(C) tensor H¹(P) would give a morphism
H¹(P)^*(-2)→T_W tensor H¹(C), whose image has level1; it is therefore
zero. The algebraic component under consideration consequently lies in
NS(W)_Q tensor H¹(C) tensor H¹(P). This argument is uniform in P and
requires no genericity condition chosen after P.

On a smooth quartic, the combined multiplication map
H¹(Ω¹_W)/C·H→H⁰(O_W(1))^* tensor H¹(Ω¹_W(1)) is injective: its dual is
the surjection sum_j w_j R₃→R₄ of the Jacobian quotient, which is
generated in degree1. Hence for the nonzero primitive NS class τ there
is a linear form w with μ(w)τ nonzero. The special triple s_i=w z_i
(i=0,1,2) makes the obstruction map on C·τ tensor C³ injective.
This proves that rank3 is a nonempty Zariski-open condition on the
space of triples of sections of M. The transverse finite-base-locus
condition is a different nonempty Zariski-open condition because M is
very ample. Their intersection is nonempty. The special triple proves
rank nonemptiness only and is not itself asserted to have a finite base
locus. This exact distinction is necessary.

These representation and rank deductions were independently checked.
The existence/specification of W with the assumed Hodge group remains
the separate primary-source input described in Section5.

## 7. Full typed proof, auxiliary Hodge input, and exact generic data: pass

Read in full:

- research/agents/cycles/dimension_six.tex, all six steps;
- research/agents/frobenius/C3_N6_Hodge_inputs.tex;
- research/agents/cycles/higher_local_surjectivity.tex, the inherited model
  and necessary Chern-class obstruction.

There are exactly 30 quartic coefficients after requiring the fixed line
D=V(w0,w1) to lie on W. The Hodge-generic complex choice of W is explicitly
separate from the algebraically independent 36 coefficients of the section
triple. This repairs the potential genericity ambiguity identified in the
initial audit: no claim that arbitrary coefficient-field embeddings preserve
the Hodge-generic surface is now made. The fixed field K0 contains the
quartic coefficients, the fixed divisor D, and Qbar. Both section conditions
are algebraic over K0. The rank-three open is nonempty by the special tuple
s_i=w z_i; its purpose is solely to prove rank nonemptiness. The independent
very-ample Bertini open gives the transverse reduced base scheme of length
48. Algebraic independence puts the chosen triple in both opens.

The auxiliary proof supplies NS(W)=ZH+ZD by the precise base-locus
Noether--Lefschetz theorem. Local Torelli realizes an open period domain
of dimension18 preserving H and D: H remains very ample, and Riemann--Roch
plus H.D=1 makes the deformed D an actual line. A nonscalar rational
endomorphism cannot have every period line as an eigenline; the nondegenerate
period quadric is irreducible and spans the ambient space. Its Hodge locus
is therefore proper. Avoiding countably many such loci and extra Picard
loci gives End_Hdg(T)=Q. The Hodge-locus theorem is being used over C only,
and the source itself warns against assuming a smaller field of definition.

Zarhin then gives Hg(T)=SO(T). The Fermat curve Jacobian is isogenous to
the cube of the CM elliptic curve with endomorphisms by Q(i). The derived
group of the joint Hodge group surjects onto SO(T) and is trivial on the
torus, so the joint group is SO(T) times that torus. The two opposite
character twists of the standard representation over Q(i) are absolutely
irreducible and exchanged by conjugation. Thus T tensor H1(E) is simple
over Q and has a nonzero (3,0) part. Semisimplicity excludes every level-one
sub-Hodge structure of its threefold direct sum. By the Poincare-duality
identification H1(P)^*(-2)=H1(P)(-1), the mixed class of every codimension2
cycle on W times C times P consequently has its W factor in NS(W).
This is uniform in P and does not require another genericity choice.

The model proof inherited from C.3ae does not require the three sections
to have no common zero. On F=0 the section ell G is not identically zero;
therefore F=ell G=0 still has codimension2 in the ambient base. The graph
open is dense in the Cartier hypersurface, and the remaining locus has
insufficient dimension to produce another component. Smoothness near V,
proper contraction, finite normalization, the unique vertex, and the
equality m_R O_Z=I_V are unchanged. The incidence calculation proves
smoothness of H at the base points and hence regularity and transversality
of the strict transform. All claimed punctures are regular.

The full necessary Chern obstruction on an actual fixed-product cycle
closure is correctly inherited, with rational Chern character used only
to deduce a zero class over C. Its projected summand receives no term
having a projective-space differential. The Hodge input reduces b0 to
the H and tau factors, the H factor is killed by the multiplication maps,
and the rank-three map kills the tau component. Section4 above checks
the two exact source corrections. The resulting mixed Picard component
is zero; the Jacobian homomorphism therefore has zero differential and
is zero in characteristic0. Compactification of the fixed parameter curve
preserves the chosen fibres. Thus rho kills the entire ordinary algebraic
source image, without any formal-family or henselized-parameter substitute.

The target divisor products are well typed under arbitrary pullback of
line bundles. The Poincare family makes them ordinarily algebraically
trivial. The exact identity rho theta=-9 is integral, and divisibility of
Pic0(C)(C) gives the asserted integral cokernel surjection. The specified
transcendental Abel point is nontorsion since the Abel closed immersion
and all torsion points are defined over Qbar. Hence the rational map also
fails to be surjective. No correction to the full typed proof is required.

## 8. Fresh primary-source inspection for the full pass

- Brevik--Nollet, arXiv:0806.1243v3, 3 November2009, full primary PDF opened:
  Theorem1.1 and Corollary1.3(c), author p2, including all base-locus
  hypotheses and the integral free-generation assertion. A fixed line
  satisfies the stated global generation and degree-two section conditions.
- Huybrechts, author's prepublication Lectures on K3 Surfaces, local primary
  PDF/text read at printed pp107--108: Proposition6.2.8 (Local Torelli),
  its proof, and Section6.2.4 on line-bundle deformations. These locators
  refer to the opened author copy, not an uninspected published pagination.
- Cattani--Deligne--Kaplan, 10 February1994 author version, full primary PDF
  opened: Theorem1.1 and Corollaries1.2--1.4 on author p2. Its preceding
  warning about fields of definition on p1 was also read.
- Zarhin1983, original primary scan opened and printed pp211--213 visually
  inspected: Theorem2.2.1, Example2.2.3, and the proof in Section2.5.
- Beauville2014, primary published PDF opened: Lemma2 with proof, p106,
  and Example3, pp106--107, explicitly including the Fermat specialization
  and the isogeny with (C/Z[i]) cubed.
- The incidence localization/projective-bundle sources remain the freshly
  opened Stacks02RX and02TX recorded in Section2.

This records exact theorem inputs and their applicability. It is not a
claim to have re-proved all imported primary literature.

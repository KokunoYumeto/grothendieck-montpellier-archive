# Independent audit of the full Brauer quotient counterexample

Date: 2026-11-19, 05:20–05:23 UTC.
Status: the counterexample passes. The conclusion concerns the full Brauer
group, and specifically its characteristic-primary torsion. It does not
contradict a prime-to-characteristic finiteness assertion.

Let k=F_2, S=Spec k[t], and let E/k be the smooth projective elliptic curve
with affine equation y²+y=x³ and origin O. Put X=E×_k S and let f:X→S be
the projection. This is a projective smooth morphism, with geometrically
connected genus-one fibres and a section. Both S and X are regular and
quasiprojective over k.

## 1. The Frobenius kernel is alpha_2

This assertion can be checked directly, without assuming the classification
of supersingular elliptic curves. In projective coordinates the equation is
Y²Z+YZ²=X³ and O=[0:1:0]. In the chart Y=1, put u=X/Y and v=Z/Y. The
completed equation is v+v²=u³. The kernel of Frobenius has u²=v²=0,
so v=0 and its algebra is k[u]/(u²).

Modulo u² and w² the formal group law has the form

    F(u,w)=u+w+cuw.

The invariant differential of the Weierstrass equation is dx. The expansion
v=u³+u⁶+u¹²+… gives x=u/v=u^(−2)+u+u⁴+…; consequently dx has constant
coefficient 1 and no linear coefficient in u. For the displayed formal
law the invariant differential is du/(1+cu), whose linear coefficient
is c. Hence c=0. The coproduct on the kernel is additive and ker(F)=alpha_2.
Because E is defined over F_2, its relative Frobenius has target E itself.

## 2. An infinite elementary 2-group of E-torsors

Every S-point of E is constant: a map A¹→E extends across infinity by
properness, and a map P¹→an elliptic curve is constant. (For example,
factor any putative nonconstant map through an iterate of Frobenius and
apply the separable genus formula.) Direct counting gives E(F_2)={O,(0,0),
(0,1)}, so E(S)=E(F_2) and Frobenius is the identity on this group.

The exact fppf sequence

    0 → alpha_2 → E →[F] E → 0

therefore injects H¹(S,alpha_2) into H¹(S,E). On the affine base, the
Frobenius sequence for G_a identifies

    H¹_fppf(S,alpha_2)=F_2[t]/F_2[t²].

This has the independent basis t,t³,t⁵,… over F_2. Its image in H¹(S,E)
is killed by 2, since the dual Frobenius isogeny V satisfies VF=[2].
For the smooth group scheme E, fppf torsors and étale torsors agree, so
the same infinite elementary 2-group occurs in H¹_et(S,E).

## 3. Direct derived splitting into the Brauer quotient

The section of f supplies a retraction of the unit

    G_m,S → K:=Rf_*G_m,X

in the derived category of abelian étale sheaves on S. Since R⁰f_*G_m=G_m,
write K≅G_m⊕K' with H⁰(K')=0. Then

    tau_{≤1}K' ≅ (R¹f_*G_m)[−1].

The map tau_{≤1}K'→K' induces an injection on H²(S,−): the obstruction
term H¹(S,tau_{≥2}K') is zero for degree reasons. Thus

    H¹(S,R¹f_*G_m) ↪ H²(S,K') ↪ H²(X,G_m),

and its intersection with f*H²(S,G_m) is zero. The relative Picard sheaf
splits as E⊕Z, using the origin to identify Pic⁰ with E and to split the
degree map. Consequently

    H¹(S,E)[2] ↪ H²(X,G_m)[2]/f*H²(S,G_m)[2]

in the stronger sense that the source has a lift into H²(X,G_m)[2]
disjoint from the entire image f*H²(S,G_m). In particular,

    F_2[t]/F_2[t²] ↪ Br'(X)/f*Br'(S).

Here Br' denotes the torsion subgroup of H²_et(G_m). No assertion that
all of H²(X,G_m) is torsion is needed: every class we constructed is
already killed by 2. If the manuscript uses the Azumaya Brauer group,
the equality Br=Br' on these regular schemes of dimension at most two
is the original Grothendieck result. Part B separately opened and
rendered *Le groupe de Brauer II*, Corollary 2.2 and its printed errata,
https://www.numdam.org/item/SB_1964-1966__9__287_0.pdf (its source refs
turn878899758view0 and turn248484072view0/1). This suffices without the
more general ample-line-bundle theorem. No independent opening of that
scan by Part D is claimed here.

## Scope and audit provenance

Part B proposed this example and checked the original manuscript scope.
Part D independently checked the fppf injection, the explicit Frobenius
kernel, and the derived section splitting above. The last argument also
repairs an unnecessary appeal to global torsion of H²(G_m). It proves
that the literal full Brauer quotient need not be finite even for a
constant elliptic scheme over a regular affine curve. It does not decide
the separately stated prime-to-characteristic chain.

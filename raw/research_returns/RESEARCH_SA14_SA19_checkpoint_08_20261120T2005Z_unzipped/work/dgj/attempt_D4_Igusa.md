# D4 ordinary Igusa deformation: unresolved direct calculation

Status: active attempt, not a theorem. 20 November 2026, 15:24 UTC. It is not yet incorporated as a proved result. It does not affect D2/D3, which are independent explicit product quotient families.

## Objects and source

Let k be algebraically closed of characteristic 2, E and F ordinary elliptic curves, P the nonzero F[2](k) point, A0=E×F, σ0=(-1,+1), and τ0=t_(0,P)σ0. The surface is X0=A0/<τ0>.

Over local Artinian W(k)-algebras R with residue k, finite étale invariance uniquely lifts A0→X0 and its order-two deck action to any deformation X. The cover is a deformation of an abelian variety. After choosing a section lifting its origin, it has an abelian-scheme structure, and the deck action is τ=t_c σ, with σ lifting σ0. The identity τ²=1 gives σ²=1 and (1+σ)c=0. Changing the chosen origin by d changes c by (1−σ)d (up to the harmless sign from which direction conjugation is written).

Opened primary source: Nicholas Katz, Serre–Tate local moduli, LNM868 (1981), Theorem1.2.1 pp143–144 and Theorem2.1 pp148–149, with extension construction pp150–152. https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf . Downloaded sources/katz1981.pdf/.txt.

Katz identifies deformations with q:TpA0(k)×TpA0∨(k)→1+m_R. Choose E,F bases in both physical Tate modules. Duality transposes q. A homomorphism f lifts exactly when q_A(x,f∨y)=q_B(fx,y). The diagonal sign automorphism therefore lifts exactly when q12²=q21²=1.

## Candidate affine-point display

The ordinary extension is a pushout of the constant extension 0→Z2²→Q2²→(Q2/Z2)²→0 by q into the formal multiplicative group. In a representative notation (x1,x2;r1,r2), fix the convention that adding an integral vector n to r divides the multiplicative coordinates by q(n). This may invert Katz's q convention but leaves transpose and lifting conditions unchanged.

A lift of (0,P) has étale coordinate (0,1/2) and principal-unit coordinates (z1,z2). The diagonal automorphism acts by

    (z1,z2;r1,r2) -> (z1^(-1),z2;-r1,r2).

Then (1+σ)c is represented by (1,z2²;0,1), hence has formal coordinates (q21^(-1),z2²/q22). This suggests that the affine involution condition is

    q21=1, z2²=q22,

with z1 unconstrained. Together with q12²=1, it gives a candidate ring

    W(k)[[t,s,u,v]]/(s²+2s)

by q11=1+t, q12=1+s, q21=1, q22=(1+v)², z1=1+u, z2=1+v. Changing the chosen origin acts on z1 by a square. Its action on first-order characteristic-two tangent vectors is zero, suggesting that this four-dimensional tangent space could be a miniversal hull rather than a representing ring.

**Not yet established:** all aspects of the representative description as an R-valued point statement; compatibility with the exact Katz q convention; the smoothness and tangent injectivity of the map from triples to the unpointed surface deformation functor; algebraization and the exact relative Picard scheme.

## Consistency test and why it remains useful

The candidate imposes q21=1. By transpose and the homomorphism-lifting criterion, A∨ would admit a quotient onto F∨. The σ∨-fixed subgroup would then fit into an extension of F∨ by E∨[2]: given a point of F∨, lift it fppf locally to A∨, and correct its failure of invariance by dividing by two in the kernel E∨. That would make the fixed subgroup flat. Cyclic linearization would make Picτ(X) a μ2-torsor over it, again flat.

This contradicts the first-order nonflatness assertion in Chai–Oort2017 §3.9(iv). However, the inspected indexed extract of Chai's v2 §2.4 p7 proves that assertion by comparing tangent dimensions/ranks of the two components, an inference which is invalid for nonsmooth torsors. The explicit finite-flat μ2-torsor in section_D.tex D4-gap has exactly those tangent dimensions after a smooth elliptic factor is added. This is a gap in the inspected argument, not by itself a refutation of the actual Igusa claim.

The candidate therefore remains worth checking, but no conclusion of flatness for the full Igusa family has been promoted.

## Partsch audit

Published PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B95794564B38C458B5571618768725E9/S0027763000010795a.pdf/deformations_of_elliptic_fiber_bundles_in_positive_characteristic.pdf . Local sources/partsch2013.pdf/.txt.

Proposition6.1 p95 gives h1(TX)=4. Proposition6.2 p99 gives the Jacobian hull W[[tE,q−1]][sqrt(q)] in the case p=d=2, tangent dimension2. Theorem4.4 p89 adds h1(C,Lie)=1. Thus the claimed equality to4 on p100 needs a correction/qualification.

Proposition6.6 p102 writes c=σ(0), then claims both σ∘t_(−c) and t_(−c)∘σ fix0. Only the second does so without an additional condition: for an affine map t_c L, the first sends0 to c−L(c). This observation identifies an inspected proof gap; it does not alone refute the theorem's conclusion.

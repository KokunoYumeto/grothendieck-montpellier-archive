# Semistable specialization: an exact tensor counterexample and a cover model

Status: unregistered method analysis. The elliptic tensor calculation and the displayed local semistable model below are proved. The comparison of every coherent K1 lift with a full special-fibre node class is not asserted to be complete. No surviving ordinary quotient and no main-gate movement are claimed.  
Author: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, `/root/frobenius_continuation`; inherited effort.  
Written: 2026-11-19T19:13:37.274055+00:00.

## 1. Exterior-product vanishing does not imply tensor vanishing

Let C be an elliptic curve over an algebraically closed field and let L∈Pic0(C)(k) be nontorsion. Put l=[L] in Pic0(C)(k)⊗Q. Then l⊗l is nonzero in the ordinary tensor square of this rational vector space. Indeed choose a Q-linear functional taking l to one; its tensor square takes l⊗l to one.

On the other hand,

    c1(L)⊠c1(L)=0 in CH0(C×C)_Q.                       (SL.1)

For completeness, if m:C×C→C is addition and p1,p2 are projections, translation invariance of a degree-zero line bundle and the seesaw principle give

    m*L ≅ p1*L ⊗ p2*L.

One may see translation invariance directly under C≅Pic0(C): translation of a degree-zero divisor does not change its Abel sum. The quotient of the two displayed line bundles restricts trivially on every vertical fibre and on the horizontal zero section, so seesaw trivializes that quotient globally. Because CH²(C)=0, pullback and the Chow ring product give

    0=m*(c1(L)^2)
     =(p1*c1(L)+p2*c1(L))²
     =2 p1*c1(L)p2*c1(L).

The pure squares vanish already on the curve factors. Rational coefficients give SL.1 in every characteristic, including characteristic two. Polarization also gives L⊠M+M⊠L=0 for any degree-zero L,M, with the evident notation for first Chern classes.

This is a clean counterexample to any general assertion that a Picard tensor injects into its exterior-product cycle group. It is not, on its own, an audited realization of that tensor as V(E) for a specified negative exceptional SNC surface. Any such geometric realization must be supplied separately. No negative SNC example is claimed here merely from this calculation.

Exact primary input: Milne, J. S. (1986), *Abelian Varieties*, in *Arithmetic Geometry*, pp103–150; author corrected text dated2January2022, https://www.jmilne.org/math/xnotes/AVs.pdf . The full displayed proofs of Theorem5.1 and Corollary5.2 (seesaw), authorpp7–8, and Proposition9.2, authorp15, were freshly opened and read; retrieval references `turn905132977view1`, `turn731520535view0`, `turn731520535view1`. The printed-book and corrected-author pagination are not conflated. Existing bibliography key `frC4Milne1986` is reusable. The entire original Mumford proof of the theorem of the cube is not claimed read here and is not needed for the direct elliptic translation/seesaw argument.

## 2. Where this enters support Mayer–Vietoris

For a regular semistable proper parameter model over a DVR, let T=∪P_j be its reduced special curve with individually indexed ordinary nodes. The actual support-union fibre/cofibre sequence is obtained from Thomason–Trobaugh Corollary8.1.4. In the present characteristic-positive SNC E setting, purity for the parameter components and nodes follows by totalizing the regular-stratum purity maps, as in PL.1; there is no general singular-ambient purity assertion.

A supported K0 boundary class may fail to lift from the direct sum of the K0 groups of E×P_j. Its obstruction is a vector of node coefficients in K_{−1}(E). In the desired Adams range these coefficients lie in V(E), because a node has codimension two in the regular parameter surface. Exactness implies, for each P_j, that the signed sum of the node point pushforwards is zero in K_{−1}(E×P_j).

Pushing once more to E gives the ordinary incidence equation Σ signed e_node=0 at every vertex. A tree dual graph therefore forces every node coefficient to be zero by deleting leaves. For a graph with cycles this is false. More significantly, zero in K_{−1}(E×P_j) is a statement about the actual exterior-product map, not about the abstract tensor V(E)⊗Pic0(P_j)_Q in PL.5. SL.1 exhibits why injectivity of that product map cannot be presumed. The present argument supplies no replacement injection in the exceptional setting.

## 3. The marked cover has an explicit semistable degeneration

Use a fixed smooth connected projective base curve A, two distinct points a0,a1, and a rational function h0=a/b satisfying:

- its only pole is at a0;
- h0(a1)=1;
- all zeros are simple, including every point supporting the finitely many marked evaluation divisors;
- a and b are sections of the same O_A(n a0), with no common zero, and div(b)=n[a0].

Such a choice uses the same sufficiently large Riemann–Roch jet interpolation as VE, with the further open simple-zero condition away from the prescribed finite set. Let u be a parameter and work over R=k[u]_(u). In A×P¹×Spec R, with homogeneous coordinates [G:H] on P¹, consider

    u b(G−H)²=(u−1)² a G H.                             (SL.2)

On the generic fibre g=G/H satisfies

    (g−1)²=((u−1)²/u)h0 g,

which is exactly the VE cover with its required value at a1. The special fibre of SL.2 is reduced and consists of two copies A0,A∞ of A, given by G=0 and H=0, together with one vertical projective line R_x over each zero x of a. Each R_x meets each main copy once and has no other intersection.

Here is the complete local regularity check near the special fibre. At a point where a≠0 on the branch g=0, the coefficient of g in the local equation is a unit, so g is eliminated and the total surface is regular with local coordinates from A and u. The same applies at g=∞. At a simple zero x of a, put z=a/b. Near g=0 the equation is

    u(g−1)²=(u−1)² z g.

Both (g−1) and (u−1) are units at the crossing, so u is a unit times zg. The total surface is regular and the special fibre has a transverse ordinary node. The inverse coordinate gives the same calculation near g=∞. At any other point on R_x, g is a unit and the coefficient of z is a unit; eliminate z to obtain regular coordinates u,g. This includes g=1 and works in characteristic two. At the pole a0, a is a unit, so the preceding a≠0 calculation applies despite b vanishing to order n.

The equation is a relative Cartier divisor with no fibre component equal to the whole ambient fibre. Equivalently its fibres have the same bidegree, so the resulting proper curve family is flat. The local calculations prove that it is regular and semistable around the special fibre. The generic fibre is smooth: at a simple zero of a the z derivative is a unit; the other odd-characteristic branch values are noncritical because u is transcendental over the constant coefficients; in characteristic two the cover is the separable Artin–Schreier cover from VE and its normalization has the same local smooth charts. One may replace the generic curve by its normalization if desired without changing the displayed regular special neighbourhood.

At the generic points of the main special components, g has u-valuation +1 on A0 and −1 on A∞. On each R_x it is a generic unit and has valuation zero. If there are n distinct zeros of a, the dual graph has two main vertices, n bridge vertices and2n edges, hence first Betti number n−1. Thus a forced collection of multiple divisor support points leads directly to cycles; no compact-type or tree assertion is justified.

## 4. What the leading component residue suggests, and what remains unproved

For the component construction HK, the Poincare line bundle M_i on A_i×A pulls back to the cover. At the level of its displayed Gersten cup with g, the two main components in SL.2 carry the leading residues +c1(M_i) and −c1(M_i); the generic vertical bridges have valuation zero. Pushing the leading terms into E_i gives the original Poincare component K0 family, with opposite signs on the two main parameter components.

Write the normalized marked evaluation divisors as

    div(r_q)=Σ_x n_{qx}[x].

The edge restriction of that Poincare component family is represented by Σ_{q,x}n_{qx}[O_q]⊠[O_x]. Applying the E closed-union boundary to its coefficient at x gives the candidate node coefficient

    v_x = ∂_E(Σ_q n_{qx}[O_q]).                         (SL.3)

Its total point pushforward on the main base copy vanishes, because the original edge family is the restriction of a tuple of component classes. Its abstract Picard tensor is the weighted marked-evaluation tensor already encountered in PL and the component-family note.

The complete identification of SL.3 with the node class of every chosen actual supported K1 lift must still track the sheaf-to-K1 lifting ambiguity and the supported descent lifting ambiguity. That final comparison has not been completed here. Accordingly SL.3 is retained as the explicitly identified leading-component obstruction and a research target, not as a proved universal residue formula for all choices of HK lift. Nothing here proves that it is zero, nor that a nonzero value survives the ordinary quotient.

This analysis explains why naive valuation desuspension risks reproducing the original component-family compatibility problem. A successful route must remove the actual node class, prove a suitable restricted specialization theorem, or construct additional endpoint-zero corrections. Neither finite covering alone nor an assumed tensor injection supplies that step.

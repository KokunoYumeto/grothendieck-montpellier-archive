# Precise remaining obstructions in the SNC affine-parameter route

Research note, 19 November 2026, 17:28 UTC. This file records failed extensions and their exact local algebra. It does not state a counterexample to the rational top-quotient question.

## A reduced-curve resolution does not solve the Cartier-tail problem

Suppose a perfect lci curve is constructed only over an affine parameter U and is then closed over a proper curve P. Resolving its reduced support in the regular ambient product does not imply that its nonreduced strict transform is Cartier on the full transformed exceptional surface. A local model on a regular threefold section is

`H = V(u^a v^b),   C = V(w,u^a),   a,b>0`.

At u=v=w=0, C is one component of the full Cartier divisor V(w) on H. Its ideal in O_H is (w,u^a), which is not invertible there. An actual Cartier completion V(w) necessarily acquires the companion component supported on v=0. Additional modifications confined to the parameter boundary create further full exceptional components; they do not permit one to discard this companion contribution. Flattening on the strict transform of H also does not prove an invertible extension on the entire transformed closed fibre.

The exact Cossart–Jannsen–Saito input was freshly reread in the retained arXiv0905.2191v2 primary: Theorems0.2–0.3, author pp.3–4; Corollary0.4/proofp5; Definitions5.1–5.2p64; Theorem5.9p67. These provide the asserted regular/normal-crossing transform and normal-flatness statements. None is being treated as a theorem that a chosen single branch becomes Cartier on the full exceptional Cartier divisor. The proved proper-parameter endpoint theorem avoids this issue by constructing the lci curve on the entire proper thickened exceptional product at the outset.

## A point blowup preserves the local vertical-divisor obstruction

Let two components E_i and E_j meet along C in a regular threefold. Let a moving smooth curve T on E_i meet C transversely at x. Blow up x in the ambient threefold. The strict transforms acquire exceptional curves e_i and e_j, and the new plane F meets them in two lines L_i,L_j, meeting at the single triple point v. The strict transform T' meets L_i at a point different from v and misses C'.

At its parameter value, add vertical corrections alpha e_i, beta e_j and c times a line on F. Compatibility on C' forces alpha=beta. The exceptional self-intersection numbers are -1; compatibility on L_i and L_j consequently forces

`c=1-alpha,    c=-beta`.

Together these equations give 1=0. Thus no correction supported only on the new local exceptional divisor classes exists. The root independently obtained the same calculation. Adding arbitrary global divisor classes restores the original restriction-to-C problem; it does not solve it.

## Blowing up the entire moving curve creates a relation in the new exceptional summand

Blow up T itself instead. The new exceptional component F=P(N_(T/Z)) is ruled over T; each old adjacent component is blown up at the corresponding intersection points. Its richer Chow group does allow a compatible class. Write h for the relative hyperplane class and use P=T as parameter. On T times T choose L=O(-Delta). The class on F times T can be written

`pi^*Z + h pi^*c1(L)`

with Z chosen to match the section restriction to E_i. Restriction at each old double point gives the required negative point divisor on the parameter, matching the exceptional-curve correction on the adjacent component.

However, at the selected parameter endpoints p,q the second component has difference

`-h pi^*([p]-[q])`.

Together with [p]-[q] on E_i this is exactly the self-intersection pattern of the new exceptional cycle j_* pi^*([p]-[q]) on the blowup. Its proper pushforward to the old resolution is zero. Thus this compatible family removes the new blowup summand; it does not prove that the original puncture class vanishes. This is a computation of the failure of that construction, not a universal impossibility statement.

## A configuration where the correction does work

The separate fully audited fixed-node lemma in `cycles/SNC_fixed_node_family_RESEARCH.tex` avoids both failures. Its rational component already carries exceptional curves whose restrictions are the individual prescribed boundary point divisors. The curve system g^m+hq forces all boundary intersections to occur at those fixed points, permitting actual vertical corrections without creating a new component or changing the selected endpoint classes. The proof settles that intrinsic two-component configuration, not arbitrary SNC surfaces.

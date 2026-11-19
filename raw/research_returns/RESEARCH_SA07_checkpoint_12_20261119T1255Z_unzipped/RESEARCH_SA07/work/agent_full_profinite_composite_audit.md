# Independent audit of the full-profinite proper-homology composite

Audit date: 19 November 2026, 10:52–10:54 UTC. Auditor: period_generation.
Scope: the original CM curve U0 = E0 \ {O}, E0: y^2=x^3-x over Q, and its arithmetic fundamental group after any finite number-field extension. This note records an exact obstruction produced by a nonperipheral procyclic subgroup with open arithmetic normalizer. It does not assert completion of the remaining all-genus single-line matrix calculation.

## 1. The full profinite detector

I independently reread Nakamura, 1994, Lemma 2.1.4, printed pp. 96–97, in `work/sources_audit_next/Nakamura1994.txt` and the original source used by the main audit. The lemma applies to the full finite class C as well as the pro-l case. Its equivalence says that a nonperipheral element z has some prime l and an open geometric subgroup H containing z for which

    z notin [H,H] H^l <Z intersect H>.

Here Z is the union of conjugates of the cusp inertia groups. Since H is closed, it contains A=closure<z>. The displayed quotient is the proper compactification H1 with F_l coefficients: abelianization kills commutators, reduction kills l-th powers, and compactification kills precisely the peripheral subgroup. Thus the proper mod-l class is nonzero. Proper integral l-adic H1 is torsion-free, so its Z_l class and then its Q_l class are nonzero.

The prime-to-l part of A maps trivially into a pro-l abelian group. Consequently A_l has the same nonzero proper class. A procyclic pro-l group with a nonzero map to a torsion-free Z_l module is Z_l; write u for a generator. No assertion about a common kernel of all pro-l completions is used.

## 2. The genus-raising cover and the exact power map

I read the full existing proof `work/LM6_A22_CM_Prym_cover.tex`. Its actual finite etale cover Y3 -> U0 has compactification the genus-three Fermat quartic, via the displayed degree-two map to the quartic model of E0 followed by [4]. Let K be its actual geometric subgroup.

The intersection H intersect K need not contain A. Form its arithmetic normal core S inside Pi=pi1(U0), using the finiteness of open subgroups of any given index in the finitely generated geometric fundamental group F. This S is open, Pi-normal, and contained in H intersect K. Replace A by A'=A intersect S. This is a finite-index characteristic subgroup of A. Its l-primary part is l^r A_l for some finite r.

The inclusion S -> H is induced by the actual covering map. It extends to the compactifications. On proper homology its pushforward sends the class of u^(l^r) to l^r[u], which is nonzero over Q_l. Thus the proper class in the S-cover is nonzero. No injectivity of pushforward is required. The compactification of the S-cover maps finitely to the genus-three Fermat quartic; Riemann–Hurwitz gives genus at least three.

## 3. Rational descent and the once-punctured target

I independently reread `work/LM6_A22_arithmetic_normal_core.tex`. Use the actual tangential section s_O:G_Q -> Pi at the rational cusp O, with a chosen nonzero rational tangent. The arithmetic subgroup S semidirect s_O(G_Q) gives a geometrically connected covering over Q. The decomposition group (I_O intersect S) semidirect s_O(G_Q) exhibits a rational boundary point y on its smooth compactification C.

The actual open immersion Y -> X=C\{y} fills all the other boundary points over Q. The resulting map on geometric fundamental groups is surjective; its map on proper H1 is the identity on H1(C). Thus the detected proper Q_l class remains nonzero in X. The image B of A'_l in pi1(X_Qbar)^(l) is compact and procyclic, and its nonzero proper class makes B isomorphic to Z_l. In particular, it has not disappeared under filling punctures or passage to the maximal pro-l quotient.

If N was the original arithmetic normalizer, intersect it with the arithmetic covering group. This intersection has finite index in N and still has open arithmetic image (also in G_Q, since the original number field is finite over Q). Its image in the arithmetic group of X normalizes B. The finite-index replacement A' is characteristic in A, so normalization is preserved before taking any image. The characteristic pro-l quotient preserves the same arithmetic projection.

## 4. The actual nonzero degree-six universal quotient

I visually reread original Nakamura 1996, printed pp. 115–117, using `work/sources_audit_next/Nakamura1996_images/page18.png`, `page19.png`, and `page20.png`.

The exact source maps are:

* Corollary (4.2) and the table in (4.3), p. 115: the universal degree-six arithmetic rank is at least r_(0,3)(6)=1.
* Lemma (4.5), p. 116: the map from the actual graded Galois image of any number-field punctured curve to the universal arithmetic graded quotient is surjective. The same paragraph explicitly records invariance under finite base change.
* Equations (4.7.1)–(4.7.2), p. 117: the actual curve image embeds in the universal monodromy image, and its projection to the universal arithmetic quotient is surjective. The latter quotient is acted on through the similitude character; degree six has its third power.

Take a finite extension L for which G_L lies in the open normalizer image. These statements supply an actual degree-six Galois representative sigma over L with canonical special leading derivation D_sigma in U_(g,6) and q_(g,6)(D_sigma) nonzero. They do not merely supply a nonzero vector in an abstract ambient derivation space.

## 5. The exact single-line obstruction

Lift this same sigma to the arithmetic normalizer of B. Since sigma acts identically on H1 and the class a=[u] is nonzero, its exponent on B is one. It centralizes u. Compare that lift with the canonical boundary-compatible special representative of the outer action, using the exact representative construction already established in F.3.22 and F.3.24–27. In the rational Malcev Lie algebra one has

    phi_sigma(log u) = exp(ad Z)(log u).

The left side first changes log u in degree seven. The degree-one part of Z centralizes a and is a multiple of a. Subtract a rational multiple of the FULL log u from the correction, which leaves the conjugation of log u unchanged. The homogeneous free-Lie centralizer of a is zero in degrees two through five, so these lower correction terms vanish successively. Degree seven then gives

    D_sigma(a) = [Z_6,a].

Hence the actual counterexample data supplies a vector in U_(g,6) intersect P_a with nonzero q_(g,6). The Reynolds and decorated-tensor reduction can be applied to this exact vector; it preserves q and actual membership in U. This is the required input for the all-genus single-line matrix obstruction. The matrix calculation itself is not proved in this note.

## Audit outcome and scope

The composite passes. There is no residual primewise compatibility step: the initial full-profinite lemma already chooses one actual cover and one prime with nonzero proper homology, and every later map is an actual covering, compactification, arithmetic descent, or characteristic quotient. Nor is there a remaining peripheral possibility for the final B, because its proper homology class is nonzero.

The conclusion recorded here is the exact nonzero obstruction vector, not an assertion of the still-running all-genus computation. The rational tangential descent used the original Q-defined CM curve and its explicit genus-three cover. An extension of this note to an arbitrary affine starting curve must supply the corresponding descent and genus-raising maps; no such extension is asserted here.

## 6. Audit of the updated literal witness and finite decision procedure

At 10:53:51 UTC I read the full updated `work/LM6_A22_full_profinite_to_single_line.tex`, including FC.5a/b, FC.7 and the Smith normal form procedure. The original p.115 table has both degree-six endpoints equal to one, so the displayed rank-sandwich sentence is exact. The alternating exterior input and cyclic-averaged scalar output are actual functionals on the stated quotient targets. The nonzero actual quotient gives, through the five-detector implication, a literal vector M(s)v=0 with L K_D(s)v nonzero. Kernel inclusion for rational matrices is preserved and reflected by extension Q->Q_l. Smith normal form over Q[s] decides the quantified kernel inclusion by its generic kernel and the finitely many integer roots of its nonzero invariant factors. These are proved reductions; no claim that the uncomputed inclusion holds is made. Canonical identifier: F.3.31.

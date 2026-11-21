# B.28–B.29: attempts to remove the prescribed-point gate

Checked on 21 November 2026 by GPT-6 Astra Pro, `/root/row_audit`; effort was not exposed. This is a targeted mathematical reading and deduction from the recovered source, not a formal certificate or a claim that every possible approach has been excluded.

## Source and exact result

The retained source is `final/recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex`, B.28–B.29, lines 4315–4440 in the inspected snapshot. I read both entire proofs and the following pointing-obstruction paragraph. B.3, lines 2488–2546, supplies the additional quotient-size test discussed below.

For a cyclic etale cover of prime degree ell over a finite field of characteristic p, with constant deck group, put f=ord_ell(p). If the base has genus h, at most

    B = (h-1)(ell-1)/f

constant twists have relative class number divisible by p. When f>=h-1, some good twist exists. A Weil bound after enlarging the field supplies a rational point on a good twist, so B.29 proves existence of a good witness over **some** base point. All field enlargements occur before selecting the good twist. It does not prove a witness over an already prescribed point.

The good condition here is the absence of **rational** new p-primary torsion. Every constant twist has the same geometric p-rank. Good twisting therefore cannot manufacture a factor of geometric p-rank zero.

## 1. Passing to an etale cover does not repair the elementary count

Let C have genus two and let U -> C be a geometrically connected etale cover of degree d. Then genus(U)-1=d. Enlarge constants until the fibre over a prescribed point P consists of d rational points. This is the largest possible prescribed fibre.

Now apply B.28 to a cyclic ell-cover V -> U. Its bad-twist bound is

    B = d(ell-1)/ord_ell(2) >= d.

Even the most favorable primitive-root case gives B=d. Merely counting the d lifted points therefore cannot force one to have a good split twist: they can all correspond to bad twists. In fact, they need not correspond to distinct twists at all. If the new cyclic cover is pulled back from C, the split-twist condition is the same on every point above P, so this particular construction gives no new independence.

The global density estimate does not improve this conclusion. Write Q for the field size and assume the favorable case B=d. Each twist of V has genus

    g_V = 1 + ell*d.

The Weil upper bound gives at most

    (Q+1+2(1+ell*d)*sqrt(Q))/ell

points of U that split in any one twist. Thus the available bound for the total number of bad base points is

    d*(Q+1)/ell + 2*d*(d+1/ell)*sqrt(Q).

This numerical upper bound is always at least 2*d^2*sqrt(Q)>2d for Q>=2. It can never certify that the bad set is smaller than the prescribed fibre, or even smaller than the union of the two fibres over proposed distinct colliding points. A large proportion of good points can coexist with every point of those particular fibres being bad. This is a limitation of the stated estimates, not a proof that every cover-based strategy fails.

One also cannot arrange that every rational point of U lies over P while using B.29's positive Weil lower bound for V. Its positivity condition is

    Q+1 > 2*(1+ell*d)*sqrt(Q).

Under this condition the Weil lower bound for U itself gives

    #U(F_Q) >= Q+1-2*(d+1)*sqrt(Q)
             > 2*d*(ell-1)*sqrt(Q) > d.

Hence there must be rational points outside the prescribed fibre. An argument choosing an unspecified good point cannot then claim that it necessarily lies above P.

For a higher-genus base the count becomes less favorable: genus(U)-1=d*(genus(C)-1), at least d, while the fibre still has at most d points.

## 2. A compatible change of base point is a constant twist, not a transport of the desired property

For rational points P and R on C, the Abel maps satisfy

    i_P(x) = i_R(x) + [R-P].

Pulling a fixed finite etale Lang isogeny back along these two translates changes its torsor by the constant torsor class of [R-P]. Its arithmetic Frobenius action on a new character factor is multiplied by the corresponding deck scalar, up to the common contravariant sign convention. The unique twist that splits above P is thereby fixed; there is no remaining freedom to choose it to be good.

A change of geometric base point for the fundamental group is a natural identification of fibre functors. It transports all section classes together. It does not turn the geometric point P into R, or turn an R-split arithmetic cover into a P-split cover while preserving its rational class number.

B.29 contains an actual counterexample to the naive “extend a good twist until P splits” step: on the R8 curve, nontrivial constant twists of the displayed degree-three cover have a nontrivial cubic Frobenius multiplier and odd relative class number. The cubic extension that makes the prescribed fibre split also cubes that multiplier to one, making the relative class number even. The example is rank zero; it disproves this general transport inference, not the unresolved positive-rank incidence assertion.

If P and Q were a collision, their Abel–Jacobi difference is 2-primary over every common finite field used in the covering formulation. Every odd-order abelian quotient annihilates that difference. Thus P and Q select the same split twist of an odd Lang quotient. Having many unrelated good points does not force their common twist to be good.

## 3. An exact alternative sufficient condition survives

Recovered B.3 provides a more concrete route than an unspecified density argument. Put

    N = #C(F_Q),     J = #J_C(F_Q).

Suppose an odd prime ell divides J, 2 is primitive modulo ell, and

    ell > N,       ell*N >= 2*J.

A surjection J_C(F_Q) -> Z/ell has kernel H of size J/ell, so these are exactly B.3's conditions ell>N and N>=2|H|. The genus-two difference bound gives at least two singleton Abel-image cosets. For any normalization at a prescribed rational P, at least one of those singleton cosets is nonzero. Irreducibility of Phi_ell modulo 2 then forces the pointed Lang cover to have odd relative class number.

This route handles every prescribed rational point over that field and can feed the prime-degree point-separation argument. It requires neither geometric rank zero nor an assertion that constant twists preserve rational new torsion. Its unresolved universal input is precise: for each curve, find an extension and a prime divisor of the actual Jacobian order satisfying both the primitive-root condition and these size inequalities.

Since J is of order Q^2 and N is of order Q, the size condition asks for a prime divisor on the scale of at least 2Q. A density theorem for primes where 2 is primitive does not, by itself, control prime factors of the sequence #J_C(F_(q^m))=det(1-Phi^m). Passing to the first field where a selected ell divides the order supplies divisibility but no such large-factor inequality. This is a distinct, exact arithmetic/pointing gate; the recovered B.5 explicitly leaves it unresolved.

The ordinary order-4159 example A13 must not be used as an example of this **primitive-root** test without another argument: ord_4159(2)=2079, not 4158. A13 correctly uses the weaker group generated by 2 and -1 and its separate theta/Weil proof.

## Conclusion of this attempt

No universal finite-field incidence theorem or Hooley-based proof was obtained from B.28–B.29. The tested lift, density, and base-point-transport steps have the explicit limitations above. B.3 gives a valid alternative conditional-on-a-large-Jacobian-factor route. A18's geometric primitive-rank criterion is a different improvement: it is stable under constant extensions, whereas B.28's rational class-number condition is not.

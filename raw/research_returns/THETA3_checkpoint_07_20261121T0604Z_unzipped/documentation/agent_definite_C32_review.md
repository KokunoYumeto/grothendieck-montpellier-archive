# Independent whole-proof review of THETA3-C32

Reviewer: `/root/definite_bridge`, GPT-6 Astra Pro; 21 November 2026. **PASS.**

I read all 530 lines of the saved construction and reconstructed every step independently. This gives the claimed explicit pure exceptional Weil cycle for the actual cyclic-four Jacobian; it does not solve an arbitrary non-CM Hodge conjecture.

## Geometry and cohomology

1. The cyclic-four model has weights (1,3,2,2,2,2), and the paired weights sum to four. The primitive residual part of H4 of the quotient H^4/(N semidirect S4) is exactly the two determinant lines: N forces equal factor characters, primitive character forces degree one in all four factors, and the graded permutation action imposes exterior alternation. The generic quotient degree is1536.

2. Six evaluation hyperplanes in P4 have one relation with every coefficient nonzero. The paired plane has three coordinate branch lines, and the restricted root section is a fourth power up to an algebraic scalar. The root line is O(3), as the explicit infinity denominator computation shows.

3. The first two blowups form the indicated P2-bundle over P1xP1. Near its special P2 fibre, the third center has ideal (u3,r1t1+r2t2). The blowup chart containing the whole strict plane yields the exact normal sequence 0 -> N -> O^3 -> O(1) ->0. It is surjective everywhere, so c2(N)=H^2 and the self-intersection is one. The four étale sheets are disjoint.

4. For paired weights a,4-a and d=gcd(4,a), the global action t -> lambda^(4/d)t, v -> lambda^(a/d)v glues. On the opposite chart v'=v/t its weight is -(4-a)/d, exactly the transition required by O_E(1) times a base line. The base transitions have zero weight. At a vertical branch point, SNC local coordinates make the normalized cover a product in the unbranched exceptional coordinate; hence its reduced inverse image is the normalized cyclic P1-cover used in the argument. The connected action extends through normalization. Its subgroup mu_(4/d) is the actual inertia subgroup, including mu2 when a=2. It acts trivially on all rational cohomology of F and fixes the finite image K' pointwise. Thus neither exceptional space has a primitive order-four summand.

5. Collapsing the entire exceptional closed set to one point gives a homeomorphism of the two quotient pairs, since the proper map is an isomorphism on their complements. The long exact pair sequences and the primitive projector prove the pullback isomorphism. Finite quotient singularities give oriented rational homology manifolds, so Poincare duality and the degree/projection formulas apply.

6. Q0-Q2 has square2. The degree-one blowdown preserves its primitive class and square. Refined pullback of the two smooth regularly embedded planes along the resolved fibre product is an integral Chow operation even though the finite quotient is not flat. Thom-class naturality and p_*p^*=1 give the exact class q^*c0, whose square is1536*2=3072.

7. The Abel sum map H^4 -> J(H) has degree24. Its pullback takes the Weil determinant lines isomorphically onto the primitive two-space, since same-eigenvalue cup products on one curve vanish and the surviving terms are the nonzero alternating tensors. The pushed cycle is pure Weil and has square24*3072=73728. The endomorphism [i] indeed acts trivially here; [2+i] has the two nonreal conjugate eigenvalues -7+-24i and supplies the second rational direction.

8. The actual ball cover of C25 is obtained by the one-fibration base-change construction, so its Stein geometric fibre has genus76 as computed in C28. Very ample horizontal curve sections are finite flat of degree d; finite-flat pullback and proper pushforward yield d^4 times the Jacobian cycle and square d^8*73728. If the line is K_X^m and the Stein base has degree e over H, adjunction gives d=150me. These are surface cycles on X^4, not asserted to be ball surfaces.

## Primary source scope

I read Schoen, Hodge classes on self-products of a variety with an automorphism, Compositio65(1988), Theorem2.0, the complete Lemmas2.2--2.9 and their proofs, and Corollary3.1 with proof. I also visually checked printedpp11,13,16,18--19,24. Source URL and hash are recorded in `external/Schoen_Hodge1988.json`. C32 supplies a direct connected-action replacement for the order-four exceptional-cohomology argument; it does not assume that weight-two inertia is visible in a degree-two quotient.

The regular-embedding/refined-intersection and resolution inputs are standard correspondence background, explicitly retained in the proof. This review is not a transitive audit of all intersection-theory foundations.

## All-dimensional extension

I subsequently read and independently checked the complete added extension C32u--v. The rank-n Euler normal bundle, total branch degree, both finite degrees, sign (-1)^n, two-direction [2+i] argument, and ball-power multipliers all pass. Its pure Weil cycles are nonzero for every member of the stated cyclic-four family. The claim that a cycle is outside the divisor algebra is retained only under the extra Neron--Severi hypothesis, proved for the chosen C25 fourfold.

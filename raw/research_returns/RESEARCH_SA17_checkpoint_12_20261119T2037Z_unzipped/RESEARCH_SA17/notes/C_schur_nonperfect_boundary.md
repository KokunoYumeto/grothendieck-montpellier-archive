# A precise boundary of Schur-lift perfectness on the first ramified node

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), RESEARCH_SA17_FINISH/c1_regular_coherent. Research boundary, not a new C.1 solution or a released numbered statement.

Let A be a dyadic DVR with 2=pi^2, for example Z_2[pi]/(pi^2-2), and put

    R=A[[x,y]]/(xy-pi^3).

The polynomial localization at(pi,x,y) works by the same argument. The node is the normal domain treated in the existing notes. Consider its free rank-two C2-lattice M with generator

    T=[[-1,pi*x],[0,1]].

It is an involution and has the admissible exact sequence sign -> M -> trivial, with the standard first-coordinate inclusion and second-coordinate projection. Therefore [M]=[sign]+[trivial], a polynomial class.

## Its canonical underived Schur lift is nevertheless nonperfect

For S=S_R(2,2), the right R[C2]-module Se is R^2(trivial) direct sum R[C2]. Indeed it identifies with (R^2)^{tensor2}, whose tensor words11,22 are fixed and whose words12,21 form a regular orbit. Consequently

    underlying_R(Se tensor_{R[C2]} M) = M direct sum (M_C2)^2.

Since T-I=[[-2,pi*x],[0,0]], its coinvariants are

    M_C2 = R direct sum R/(pi^2,pi*x).

The underlying Schur lift is therefore

    F = R^4 direct sum (R/(pi^2,pi*x))^2.

We prove that its final summand Q=R/(pi^2,pi*x) is not perfect.

Set J=(pi,x). The presentation R^2 -> J, (a,b) -> pi*a+x*b, has relation matrix

    Phi=[[-x,-pi^2],[pi,y]],
    Psi=[[y,pi^2],[-pi,-x]].

Over S0=A[[x,y]], their products both equal -(xy-pi^3) I2. Their columns give relations on J modulo g=xy-pi^3. They generate all relations: if pi*a+x*b=0 in R, lift a,b to S0 and write pi*a+x*b=g*c. Then

    pi*(a+pi^2*c)+x*(b-y*c)=0 in S0.

The only syzygies of(pi,x) in S0 are multiples of(-x,pi): reduce modulo pi to see b-y*c divisible by pi, then cancel pi in S0. Thus(a,b)=Phi(d,c) modulo g for a suitable d. Hence coker(Phi)=J.

The matrix factorization gives an exact two-periodic free resolution of J. Here is the direct exactness check, rather than a citation: if Phi*v=0 modulo g, lift and write Phi*v=g*w. Multiplying by Psi gives -g*v=g*Psi*w. Since g is a nonzerodivisor in S0, v=-Psi*w. Reducing modulo g proves ker(Phi)=im(Psi); the other equality is identical. Thus

    ... -> R^2 --Phi--> R^2 --Psi--> R^2 --Phi--> R^2 -> J ->0

is exact. Both matrices have every entry in the maximal ideal(pi,x,y). After tensoring with the residue field all differentials are zero, so Tor_i^R(J,kappa)=kappa^2 in every positive degree. In particular J is not perfect.

Multiplication by pi is an isomorphism J -> pi*J because R is a domain, and pi*J=(pi^2,pi*x). The exact sequence0->J->R->Q->0 therefore gives Tor_{i+1}(Q,kappa)=Tor_i(J,kappa) for i>=1. Thus Q is not perfect, and neither is F.

This proves that nonperfectness of the underived Schur lift is not an additive obstruction to polynomiality of an individual lattice class, even on the first unresolved normal node. The triangular polynomial class already has such a lift. The sufficient perfect-lift lemma and the regular-coherent theorem remain valid. No conclusion follows about necessity of modular regular coherence or about the comparison kernel of this node.

## Exact finite-matrix certificate

`code/C_finish_schur_nonperfect_boundary.py` and `logs/C_finish_schur_nonperfect_boundary.json` record exact integer-polynomial calculations:

* both matrix-factorization products and the two presentation syzygy equations;
* the triangular involution and its admissible endpoints;
* the10-dimensional Schur commutant, the2-dimensional corner and the4-dimensional Se with two fixed words and one regular orbit;
* an explicit quotient/kernel splitting proving that the regular orbit tensor_B M is M;
* reduction of both factorization matrices to zero at the maximal ideal.

Runtime:0.11244650000298861seconds. The infinite-projective-dimension assertion is proved by the entire periodic resolution above, not inferred from any bounded test. No code output asserts a Swan obstruction.

## New-method boundary after the earlier detectors

The existing second-page parity proposal has already been refuted by its eight-element finite-ring certificate. The present calculation examines a different approach: the new Schur resolution theorem. It explains exactly why the contrapositive of that sufficient theorem cannot be used for the node. A useful subsequent route must construct an invariant compatible with the admissible triangular sequence itself, or an explicit nonzero lattice class, rather than merely a nonperfect Schur-induced module.

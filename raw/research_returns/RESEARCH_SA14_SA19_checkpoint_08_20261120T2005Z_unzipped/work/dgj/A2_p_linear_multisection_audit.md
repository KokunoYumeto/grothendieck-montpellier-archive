# A2 p-linear multisection exclusion: independent equation and proof audit

**Status: PASS.** This is a construction exclusion, not a proof of general A2.

Let S be smooth projective integral, of dimension at least one, over an algebraically closed field of characteristic p. Use the quotient convention for P_S(E), with E rank two. A quotient F_S^*E -> N gives a section of P(F_S^*E). Let Y be its inverse image under the relative Frobenius P(E) -> P(F_S^*E), and suppose Y is smooth integral. Write rho:Y->S, K=O_P(E)(1)|Y, and P=K^2 tensor rho^*(det E)^(-1).

The kernel of F_S^*E -> N is (det E)^p tensor N^(-1). The section is the zero divisor of its map to O(1), so its class is H' - p det E + N. Relative Frobenius pulls H' back to pH. Hence

- O_X(Y) = O_X(p) tensor pi^*((det E)^(-p) tensor N).
- K^p = rho^*N, by restriction of the universal quotient.
- N_{Y/X} = P^p.
- omega_{X/S} = O_X(-2) tensor pi^*det E, so adjunction gives omega_Y tensor rho^*omega_S^(-1) = P^(p-1).

Every sign matches the quotient convention. The map rho is finite flat of degree p because it is the base change of the relative Frobenius of P^1 along the section.

Suppose a nontrivial M in Pic(S)[p](k) is trivialized on Y. Its mu_p torsor T is integral: if its generic fibre split, the trivializing rational section would have zero divisor and M would be trivial on normal S. Rescaling the trivialization on Y by a constant makes it compatible with M^p = O_S. Then Y -> T is finite birational, because both have degree p over S, and Y is the normalization of T.

The torsor T is Gorenstein with omega_T = tau^*omega_S (adjunction in the total space of M, followed by the tautological trivialization of tau^*M). Finite duality identifies omega_Y with rho^*omega_S tensor the conductor ideal. Since both canonical sheaves are invertible, this conductor is O_Y(-D) for an effective Cartier divisor D. Thus P^(p-1)=O_Y(-D).

If Y were ample in P(E), its normal bundle P^p would be ample, so P would be ample. The equality P^(p-1)=O(-D) contradicts positivity after intersection with an ample divisor to the power dim(Y)-1. This works for every dim S >= 1, whether or not T is normal and without a disjoint infinity section.

Finite-duality and adjunction inputs are the same opened primary sources already checked in A2Z: Stacks Lemma47.15.8 (Tag0A7A), Section49.5 (Tag0FKW), and Lemma48.14.1 (Tag0B4B). The divisor and relative-canonical identities above are derived explicitly rather than delegated to a projective-bundle convention.

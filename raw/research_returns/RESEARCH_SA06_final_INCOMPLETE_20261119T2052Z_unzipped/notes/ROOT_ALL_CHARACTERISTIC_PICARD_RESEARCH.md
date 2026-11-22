# Uniform ordinary-quartic construction after review 9

Research lead proposed after review 9; not a registered theorem at this writing. The certified C.3bf remains in its exact characteristic-five, N≥4 scope. Frobenius is preparing a separate complete extension, provisionally C.3bg; cycles independently checked the ordinary-quartic and canonical-cup calculations below. This note does not itself change a main status.

## An explicit ordinary open set in every characteristic

For any prime p, put F0=xyz(x+y+z). This is the union of four projective lines with six distinct transverse nodes in every characteristic. Its dual graph is K4. The normalization exact sequence identifies H¹(O_C0) with the three-dimensional graph cokernel k^6/(k^4/k); semilinear Frobenius is bijective because the incidence matrix has entries in Fp.

There is also a direct coefficient calculation. In the standard H²(P²,O(-4)) basis indexed by a1=(2,1,1), a2=(1,2,1), a3=(1,1,2), the plane-quartic Hasse–Witt entry is the coefficient of x^(p a−b) in F^(p−1). For F0, factor

    F0^(p−1)=(xyz)^(p−1)(x+y+z)^(p−1).

Each diagonal coefficient becomes the coefficient of one pure monomial of degree p−1, hence equals one. Every off-diagonal coefficient has one exponent −1 after the factor is removed, hence equals zero. Thus the Hasse–Witt matrix at this singular quartic is I3 for every prime. The formula itself follows from the plane-curve exact sequence and the Cech representatives, so it does not presuppose smoothness at this test point.

Let t_m run through fifteen algebraically independent coefficients, one for each degree-four monomial, and set F=F0+sum(t_m m). The Hasse–Witt determinant is a polynomial in these coefficients with value one at zero, and is therefore nonzero at the generic point. The nonempty smooth open in the full quartic linear system meets this ordinary open. Thus the specified geometric generic quartic is smooth and ordinary in every characteristic. Its coefficient of z^4 is nonzero, so z0,z1 restrict to a basepoint-free canonical pencil when that pencil is needed for N=3.

## Producing the nonsplit first neighborhood

For any smooth plane quartic C, its canonical system is O_C(1). The Euler sequence and Serre duality show H¹(T_P²|C)=0: the map H¹(O_C)→H¹(O_C(1))^3 is dual to the basis map k^3→H⁰(K_C), hence is an isomorphism. The normal sequence then makes

    H⁰(C,O_C(4)) → H¹(C,T_C)

surjective. The canonical multiplication Sym²H⁰(K_C)→H⁰(K_C²) is an isomorphism: both spaces are the six-dimensional quadrics on the canonical plane curve, which has no quadratic equation. Serre duality therefore lets the normal displacement H realize any symmetric cup form on H⁰(K_C). A nondegenerate form exists also in characteristic two. Choosing an independent generic quartic H gives a nondegenerate form.

Over k=Fp(t_m,s_m)^alg, with the s_m the independent coefficients of H, the complete polynomial data F,H,ell and F+t ell H thus specify the same nonsplit Segre construction as C.3bf. The extension-class image is the span of the three selected projective coordinates for m≥2. The cited first-order obstruction formula works in every characteristic; no characteristic-zero logarithm is used.

## The dimension-three endpoint

For m=1, take ell=x0 z0+x1 z1. Its zero divisor over C is the projective bundle of the line kernel of O_C²→K_C, hence is C itself, and L_H=K_C². The target has no vector part. The source extension has rank two. Pullback by ordinary Verschiebung again splits it. The map from its kernel (Z/p)^3 to the two-dimensional vector group has k-span of dimension two, and therefore its Fp-image has dimension at least two. The safe subgroup conclusion is an injected (Z/p)^2; k-linear rank two alone does not prove its finite image has exactly that order.

One can construct each actual family on a smooth proper curve in J^(p) through zero and the chosen kernel preimage, using the composed Picard map. This avoids requiring that the whole lifted J^(p) embed in the extension. The same first-order Poincare obstruction, higher coherent vanishing, proper formal existence, prescribed-first-jet approximation, and endpoint detection then need to be checked in the full proof.

No conclusion about a nonzero higher Chow product follows from this divisor kernel. The nonsplit conormal connecting-map obstruction described in the owner's higher-restriction research note remains a separate issue. No priority is claimed.

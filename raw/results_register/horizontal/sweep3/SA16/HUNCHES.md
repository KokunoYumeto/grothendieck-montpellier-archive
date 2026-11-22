# SA16: hunches (sweep 3, wave 1)

Merged by Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 3 wave 1 (merge) from the readers' files in readings/. Each section is the reader's text, unchanged.

## From readings/c62_c64.md (4. Hunches)

- **H-62-1 (62:19, 62:46, 62:50).** For S regular over Z[1/6], a function i in Gamma(S, O_S) is the invariant of a
  genus-zero triple (X, X', s) iff the pull-backs of the divisors (0) and (1) of the i-line are divisible by 2 and 3 as
  Cartier divisors (and i has no pole); more precisely the stack [U/S_3] of 62:50 is the root stack of the i-line A^1
  of order 2 along 0 and order 3 along 1 (stabilizers Z/2 and mu_3), so the lifts are classified by Cadman's universal
  property of root stacks (locator unverified: Cadman, "Using stacks to impose tangency conditions on curves", Amer. J.
  Math. 129 (2007)). Grounds: the DVR computation of section 1.5 and his 62:19 criteria. Links: SA16-5; the elliptic
  version (the 62:19 conditions for a curve with given j over a DVR) is the classical potential-good-reduction analysis.
- **H-62-2 (62:42-50 with 64:89-92).** The triples of 62 are M_{1,1} rigidified by -1 over Z[1/6], and the dicyclic
  group D'_3 of 64:90 is the extension that restores the -1: [U/S_3] and [U/D'_3] are the two sides of the mu_2-gerbe
  M_{1,1} -> M_{1,1}^rig, which is non-trivial (the S_3-action on the Legendre family lifts only to D'_3). Grounds: both
  computations above. Link: the "quadratic twist" note C16 and the "central sign" note R08.
- **H-64-1 (64:50).** The characteristic-5 phenomenon is the exceptional isomorphism PGL_2(F_5) = S_5: the octahedral
  set fills P^1(F_5), and the five S_4 in S_5 give five octahedral structures; a uniform statement of Part II over Z[1/2]
  needs the stack of octahedral structures (finite étale over Z[1/2, 1/5], with an extra branch at 5). Link: SA16-9;
  RN014-RN015.
- **H-64-2 (64:63-65).** f_2^t is the Lattès map of the doubling in the normalization "2-torsion at 0, 1, infinity,
  origin at t"; its iterates and their fixed points give the 2^n-torsion images, i.e. the tower of 2-power level
  structures that the LM pages use. Link: SA16-11; the LM line on level structures.
- **H-64-3 (64:116-121).** The level-4 relative pinning gives alpha: omega_J = mu_4^* through
  prod_i (p(x_i) - p(epsilon_i)) / prod_cyclic (p(epsilon_i) - p(epsilon_j)) in mu_4^*, and this alpha is (up to a sign
  convention) the Weil pairing e_4 on the basis attached to the pinning; then condition c) should fix kappa up to sign
  through a square root of prod_i f'(zeta_i)-type quantities supplied by the z'_i. Grounds: the computation in section
  2.4. Open: research package R2.
- **H-64-4 (64:156).** "l'invariant modulaire exceptionnel lambda = 2^alpha 3^beta" is 1728 = 2^6 3^3 (J of the harmonic
  curve, his j_G = 0 on 62); the étale double cover of the j-line over Z minus {0, 1728} found on 64:156 is the cover
  given by S^2 = J(J - 1728), i.e. by sqrt(c_4) up to squares (J = c_4^3/Delta, J - 1728 = c_6^2/Delta). Grounds: the
  mod-4 computation. Link: SA16-15, SA16-19.

## From readings/c62b_c63.md (3. Hunches)

- **H-63-1 (63:67, 63:75-77).** alpha omega^2 is (up to a constant) the non-holomorphic weight-2 form E_2^* on M_{1,1}, and
  his invariant (arg alpha)^6 with omega^12 = Delta is arg(E_2^*(tau)^6/Delta(tau)) up to normalization: a real-analytic
  function of j. Link: SA16-14 (the Hodge line and Gauss-Manin), SA16-12; the literature on E_2^* at CM points
  (Masser; Shimura's nearly holomorphic forms).
- **H-63-2 (63:96-100 with 63:32 and 64:44-53).** His divisors of c_4 and c_6 on the modular site are the stacky points
  Bmu_6 and Bmu_4 over Z[1/6] and become non-regular exactly at the supersingular points; the level-3 picture at 2
  (four components with a common tangent, the SL_2(F_3) action through Z/3) is the same phenomenon as the characteristic-5
  exception of the octahedral configuration of cote 64: an exceptional automorphism group at a small prime (SL_2(F_3) at 2,
  PGL_2(F_5) at 5).
- **H-62-3 (62:52-54 with 62:42-50).** Over Z[1/6] the genus-zero triples are (L, sigma_2, sigma_3) up to G_m with weights
  (2, 3): [U/S_3] is the weighted projective stack P(2, 3) minus the discriminant, and M_{1,1} is P(4, 6) minus it; the
  passage is the square map on G_m, the mu_2-gerbe of `c62_c64.md` H-62-2.

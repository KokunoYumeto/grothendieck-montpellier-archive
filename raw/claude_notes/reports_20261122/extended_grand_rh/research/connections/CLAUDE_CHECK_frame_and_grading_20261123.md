# Check of frame_and_grading.tex (23 Nov 2026)

By Claude (Claude Opus 5.5 at effort max), main session ed7922ad, about 01:3x UTC. Type: targeted proof check, every
step of sections 2-5 derived and recomputed by hand; no program run. Verdict: correct, with two inputs taken as given.

- Section 2: chi_U = (3,3,0), chi_T = (3,-1,0), T = Ind_{V4}^{A4} l (the three conjugate signs sum to -1 on
  V4 \ {1}); J = U + 8T, character (27,-5,0); involution eigenvalue multiplicities (11,16) (each T gives +1,-1,-1, U
  gives three +1); three-cycle 9/9/9. Golay side 2U + 6T GIVEN the September fact that A4 acts freely on the 24
  coordinates (not checked here); common part 6T, dim 18; K = U + 6T. The H^1(V4,K) image (Z/4)^3 follows from the
  long exact sequence given P(Lambda) = Z^3 and P(Lambda^{V4}) = 4Z^3 (September, not checked here).
- Theorem 3 (Artin formalism): L_T = L_C(s,l); zeta_F = zeta L_T (1 + T = Ind_{C3}^{A4} 1); zeta_N = zeta_C L_T^3
  (Reg = U + 3T); L(J) = zeta_C L_T^8; with zeta_C = zeta L(chi) L(chi-bar) and Alpoge's theorem, the four RH
  assertions are each equivalent to RH for the quadratic Hecke character l over C; L_T entire, so no cancellation.
  Correct; classical in substance.
- Section 3.1: disc(X^4 + 8X + 12) = -27*8^4 + 256*12^3 = 331776 = 576^2; resolvent y^3 - 48y - 64 =
  64(z^3 - 3z - 1), z = 2cos(pi/9) (2cos 3t = 1); no real roots (minimum 12 - 6*2^(1/3) > 0); Galois group A4;
  t(p) = sum of (a/p) over roots a mod p (product of the three symbols = (N z / p) = 1); z^8 - z = 28z^2 + 26z + 6
  == 2(z+1) mod 4 (recomputed from z^3 = 3z + 1), so z is not a square mod 4, local conductor (4); Artin conductor
  81 * 4^3 = 5184; gamma factor Gamma_R(s) Gamma_R(s+1)^2 (complex conjugation in V4, nontrivial); at p = 5 the
  single root is 4 and the Euler factor (1 - u^3)^9. Correct.
- Sections 4-5: projector traces 24 (Albert) and 18 (Leech); block-cycle determinant; intertwiner kills the omega
  eigenspaces (L(R - R^{-1}) = 0); orbit identity xy + yz + zx; divisors of 1825 mod 27 = 1,5,25,19,14,16; orbits of
  10; A(1) = 6, A(10) = 3, A(-1) = 0; 10^2 + 10 + 1 == 3 mod 27. Correct.
- Not checked: section 1's grading theorem (needs Fable's 132-coefficient table, not attached).

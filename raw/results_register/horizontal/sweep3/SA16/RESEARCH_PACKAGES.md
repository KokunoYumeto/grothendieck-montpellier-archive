# SA16: research packages (concepts) (sweep 3, wave 1)

Merged by Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 3 wave 1 (merge) from the readers' files in readings/. Each section is the reader's text, unchanged.

## From readings/c62_c64.md (6. Research packages (concepts))

**R1. Which invariants come from genus-zero triples (62:46 "quels i conviennent ??").**
- Question: for a normal scheme S over Z[1/6] and i in Gamma(S, O_S) with i and i - 1 not identically zero on any
  component, is i the invariant of a triple (X, X', s) iff the two codimension-one conditions of 62:19 hold (v(i) even
  where i vanishes, 3 | v(i - 1) where i - 1 vanishes)? Proved for regular S; to be proved or refuted for normal S.
- Why it matters: it is the question he leaves open on 62:46, and its answer describes the maps to [U/S_3], the
  rigidified M_{1,1} over Z[1/6].
- Rests on: 62:19, 62:42-50; SA16-5, SA16-4.
- Strongest reduction: on regular S, by Zariski-Nagata purity, the conditions are codimension one, and they are those of
  62:19 (section 1.5); on normal S the reduction is to the purity of the branch locus for the S_3-torsor, which can fail
  (Pro note C10). A refutation would be a normal surface singularity with a torsor unramified in codimension one that
  does not extend.
- Material: the cote 62 transcription 62:19-50, the Pro notes C05-C23, Cadman (2007) on root stacks, SGA 1 X.3 on
  purity (locator unverified).

**R2. The canonical Legendre pinning from a level-4 structure (64:93, 64:118-126, "Dieu sait comment").**
- Question: for E/S with 2 invertible and a relative level-4 Jacobi pinning (x_i)_{i in J}, 2x_i = epsilon_i,
  sum x_i = 0, construct (or prove impossible) a Legendre pinning (alpha, kappa) depending functorially on (E, (x_i)) and
  compatible with base change, and write condition c) explicitly.
- Why it matters: it is the step he could not write, and it decides whether the Legendre-pinned moduli space
  U_{0,3} x mu_4^* of 64:86 receives the level-4 moduli space canonically.
- Rests on: 64:75-100 (the pinning), 64:105-126 (p, the halves, F_t); SA16-10, SA16-9.
- Strongest reduction: section 2.4 gives alpha from the product prod_i (p(x_i) - p(epsilon_i)) = +-sqrt(-1).Delta_0;
  F_t is the explicit line of sum_i (zeta_j - zeta_k) e_i; what remains is kappa up to sign, i.e. a canonical square root
  of a degree-2 quantity in the z_i, z'_i.
- Material: the cote 64 transcription 64:70-126 with the Pro notes R03-R16, L01-L92; Katz-Mazur on level-4 structures
  and the Weil pairing (locator unverified).

**R3. Octahedral structures over Z[1/2] including characteristic 5 (64:50-53).**
- Question: describe the scheme of regular octahedral structures on a divisor Delta of degree 6 in a P^1-bundle over
  Z[1/2], and prove or refute that it is finite étale of degree 1 away from 5 and of degree 5 over the points of
  characteristic 5 where Delta = P^1(F_5).
- Why it matters: it repairs the Theorem and Corollary 1 of 64:52-53 uniformly.
- Rests on: 64:45-53; SA16-9.
- Strongest reduction: the stabilizer computation of section 2.2 (mu_4 at 5) and PGL_2(F_5) = S_5.
- Material: 64:44-57 with the Pro notes RN007-RN021.

## From readings/c62b_c63.md (5. Research packages (concepts))

**R5. His questions on the two splittings of H^1 (63:67).**
- Question: (a) for which tau in the upper half-plane is alpha(tau) = 0, i.e. the Hodge complement omega-bar proportional
  to eta = x omega? Prove that the zeros of alpha in a fundamental domain are exactly tau = i and tau = e^(2 pi i/3), or
  refute it with another zero. (b) For E over Q-bar with omega algebraic, prove that alpha is algebraic iff E has complex
  multiplication, or refute one direction.
- Why it matters: it is his question, and it measures how far the algebraic de Rham splitting is from the Hodge splitting
  (the object behind the non-holomorphic E_2^*).
- Rests on: 63:66-77; SA16-12, SA16-14.
- Strongest reduction: alpha omega^2 is canonical; alpha vanishes at i (eta_2 = -i eta_1 for the square lattice) and at
  e^(2 pi i/3) by the same symmetry; the absolutely convergent series of 63:69-71 for eta_1, eta_2.
- Material: the cote 63 transcription 63:66-77 and the K63 math notes; Masser (1975); the literature on the zeros of E_2
  and E_2^* (locators unverified).

**R6. The complete local ring of the modular site at the supersingular points (63:99-100).**
- Question: write c_4 and c_6 as elements of W(F-bar_p)[[t]] (t = a_1 for p = 2, t = b_2 for p = 3) up to units, and decide
  which surjection SL_2(F_3) -> F_4^* gives the action on the vertical tangent line at the point a of 63:100.
- Why it matters: it completes his description of the divisors of c_4, c_6 (63:96) and of the four components of
  V(c_4) n M_3 at 2.
- Rests on: 63:96-100; SA16-3, SA16-19.
- Strongest reduction: the regularity results checked above, and the Newton polygon of c_4 at 2 (one segment of slope -1).
- Material: 63:96-100; Deligne's Formulaire (63:16-34); Lubin-Tate deformation theory (W[[t]]).

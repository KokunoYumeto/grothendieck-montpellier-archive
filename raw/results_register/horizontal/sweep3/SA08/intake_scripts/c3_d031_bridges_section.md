## 4. Bridges

Criterion: step 4 of the brief as corrected on 20 Nov 2026. The road from Grothendieck's programme to the Riemann
hypothesis over finite fields runs here through the crystalline side:
- divided powers and crystalline cohomology (Berthelot);
- the de Rham-Witt complex (Illusie);
- Mazur's theorem that the Newton polygon lies above the Hodge polygon (Katz's conjecture), the p-adic face of the Weil
  bounds;
- Katz-Messing's proof that crystalline cohomology of smooth projective varieties over F_q satisfies Deligne's purity;
- Kedlaya's p-adic proof of the Weil bounds through rigid cohomology.

Below I state what the crystalline Frobenius, its slopes and purity (Deligne, *La conjecture de Weil* I, II) give for
the PD constructions of this run, and what its rows give back. Where a link carries nothing, I give the reason for that
row. RH and GRH are cited to Alpöge, *Remark*, 20 Nov 2026. The statements of A-WF02 and A-L10 are read in the paper;
their proofs are not.

**1. The coefficients are Tate twists; A-L10 is a slope bound.**

- **The Frobenius on the coefficients.** S = Γ_R(T), with T of weight one, is the integral homology of
  BG_m = CP^∞ (H_*(CP^∞; Z) is a divided-power algebra on the class of degree two). A Frobenius of the kind A-WF02
  classifies acts by F(T^[w]) = c^w T^[w] with c ∈ pR. For c = p, the weight-w line R·T^[w] is the F-crystal of the
  Tate twist (−w): its Frobenius is p^w, its slope is w, and it is pure of weight 2w.
- **What purity and Newton-above-Hodge give.** For Tate twists both hold with equality: |p^w| = (p)^{2w/2}, and the
  Newton slope w equals the Hodge level w (the ordinary case). So they fix the slope of weight w as w·v_p(c). This is at
  least w, with equality exactly when c/p is a unit.
- **The PD cochains of a simplicial set.** Their weight-w part is H^i(X; Z) ⊗ T^[w] (RESEARCH_SA08, R1, A-002, A-003),
  and the Frobenius acts on the coefficients only. Seen as the cohomology of a constant simplicial scheme of points over
  F_q, H^i(X) has Frobenius weight 0 in every degree: in Deligne's weight spectral sequence E_1^{a,b} = H^b(X_a)
  vanishes for b > 0. This is the situation of the dual complex of a semistable degeneration, Deligne's W_0. The
  Frobenius weight of H^i(X) ⊗ T^[w] is therefore 2w whatever i is. These are mixed Tate objects, and purity in the sense
  "H^i is pure of weight i" is not expected of them. Hence no row constrains an eigenvalue of a geometric Frobenius, and
  none is constrained by one.
- **A-L10 read through this.** The weight of a cotangent class is its slope divided by v_p(c). A-L10 then says: in a
  fixed homological degree n, the p-local special cotangent homology of S/I_N has slopes at most
  (N−1)(1+b_p(n))·v_p(c), where b_p(n) = max({n+1} ∪ {(n+2−2r)p^r : 1 ≤ r ≤ ⌊(n+1)/2⌋}).
  - This is a degree-wise slope bound, the PD-cotangent counterpart of the crystalline bound "the slopes of H^n lie in
    [0, n]". That bound comes from Newton-above-Hodge together with the symmetry λ ↔ n − λ, which purity gives.
  - The bound here grows like p^{⌊(n+1)/2⌋} instead of linearly in n. A-S09-12 shows that it cannot be made uniform in
    n: there are nonzero p-local classes in degree 2k−1 and weight p^k for every p > 3(N−1).
  - The row gives back this slope bound for the cotangent complex of a truncated divided-power algebra. Purity gives it
    only the normalization: slope equals weight when c = p.

**2. Frobenius saturation is the de Rham-Witt construction (A-WF01, A-WF02).**

- **What the rows do.** They apply the construction of Bhatt-Lurie-Mathew (*Revisiting the de Rham-Witt complex*): a
  Dieudonné algebra, its saturation Sat_F and the strict completion 𝒲Sat_F. For smooth algebras it recovers Illusie's
  WΩ^•. Here it is applied to the admissible PD theories, as a candidate completion.
- **Why positive weights get a positive slope.** The Dieudonné condition makes F congruent to the p-th power map, and
  T^p = p!·T^[p] ≡ 0 mod p. So F(T) ∈ pR, which is (WF.9): F(T^[w]) = c^w T^[w] with c ∈ pR. Every positive weight then
  has positive slope. In the strict completion, elements on which F^m is divisible by p^{mw} for all m become infinitely
  p-divisible. So 𝒲Sat_F keeps only the slope-0, unit-root part, which is weight 0, and kills every positive-weight
  coefficient (WF.10). A-WF01 computes the first case: the saturation makes the positive-weight H^0 rational.
- **Why de Rham-Witt keeps positive slopes for smooth varieties and not here.** For smooth varieties its Frobenius is the
  divided one, F = φ/p^i on i-forms, so the Hodge level is untwisted by the form degree. Illusie's slope spectral
  sequence puts the slopes of H^j(X, WΩ^i) in [i, i+1); together with Mazur's inequality this is how the Hodge levels
  bound the slopes from below. In the rows of this run the slope sits in the coefficient weight, and no form degree
  divides it out.
- **What purity gives here.** For the Tate coefficients the slope of weight w is exactly w (c = p up to a unit). So the
  Frobenius untwisted by weight, F/p^w on weight w, is a unit there. This is the normalization a crystalline-type
  completion for C.3 would need: a Frobenius twisted in the manner of Nygaard or Breuil-Kisin twists, not a Dieudonné
  algebra structure, whose congruence forbids the untwisting.
- **What the rows give back.** Within Dieudonné algebras, no weight-preserving Frobenius can complete an admissible
  theory with its coefficient comparison: the congruence to the p-th power forces positive slope on every positive
  weight, and the de Rham-Witt completion then removes the Tate coefficients. This closes the de Rham-Witt route to C.3
  as the run specified it, and names the change it would need, untwisting by p^w.

**3. Gluing over Spec Z (AT01; C30, C32 and C34 of RESEARCH_SA08; A-S09-24 to A-S09-30; the moving-prime rows A-S09-09,
A-S09-12, A-P01, A-L20, A-L21).**

- **The setting.** At each prime the local pieces live over Z_(p) and Z_p, where points 1 and 2 apply. The gates ask
  for these local pieces to glue over the arithmetic square of Z. AT01 is a pure exact sequence of coefficient modules;
  "pure" there means a pure submodule.
- **The obstruction is uniformity in p,** against classes of exact order p at every prime: in weight 2p (A-S09-09), in
  weight p^k and degree 2k−1 (A-S09-12), and in weight 2pb + 2p(p−1) + 1 (A-P01).
- **Where their orders come from.** They are p-adic valuations of factorials: T^w = w!·T^[w], and by Legendre's formula
  v_p(w!) first becomes positive at w = p.
- **The torsion that zeta values control in Tate twists over Z.** H^1(Z[1/p], Z_p(w)) has p-torsion exactly when
  (p−1) | w, since the cyclotomic character mod p has order p−1. For even w, H^2(Z[1/p], Z_p(w)) is measured by ζ(1−w),
  that is by Bernoulli numbers (Kummer's congruences, von Staudt-Clausen, Mazur-Wiles).
- **Why the rows' classes are not of that kind.** They do not follow that pattern. Weight 2p is ≡ 2 mod (p−1), so for
  p ≥ 5 they lie in weights where the cyclotomic torsion of the Tate twists vanishes. They exist for every odd prime,
  regular or not. They are the torsion of divided powers against ordinary powers, not torsion of zeta values.
- **Why RH and GRH give nothing.** They govern the zeros of ζ and L(s, χ) and through them the distribution of primes.
  Every torsion order in these rows is computed exactly, prime by prime, by Legendre's formula, and no row uses how the
  primes are distributed. So RH and GRH give these rows nothing, and the rows give nothing back to ζ or L-values.
- **Artin-Verdier.** Spec Z as a 3-manifold is the frame of the gates: a Mayer-Vietoris over Spec Q and the formal discs
  at the primes. The proved finite-prime cases (C16, C17) are the gluing over Spec Z[1/m]; the open case is all of
  Spec Z. But no duality H^i ↔ Ext^{3−i}(−, G_m) and no étale cohomology with Z(n) coefficients enters any row, so the
  3-manifold structure is not used.

**4. Zeta values, L-functions, motivic cohomology, K-theory, mixed Tate motives, periods, positivity.**

- **What the rows contain.** The only Tate structure in them is that of point 1: the coefficients Γ(T) = H_*(BG_m) and
  their Tate weights. No row computes motivic cohomology, K-groups, periods or special values. So, beyond point 1, the
  link carries nothing.
- **Where the programme meets these bridges directly.**
  - On the Witt and crystalline side of the archive, in SA17 (cotes 126-133, the Witt-Dieudonné-BT notebooks). There
    the slopes of the Dieudonné modules of p-divisible groups (Manin), with Katz-Messing and Mazur, are the p-adic face
    of the Weil bounds for abelian varieties.
  - In RESEARCH_SA08's B.8: Breen's Ext(G_a, G_a) and its Frobenius torsion.


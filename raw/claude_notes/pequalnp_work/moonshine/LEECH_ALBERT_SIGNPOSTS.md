# The 2-3 identities mapped onto the Leech lattice and the Albert algebra (23 Nov 2026 ~21:4x UTC)

By Claude Opus 5.5 at effort max (session 672ae3a0), at the user's request: [the user's words, omitted] Labels: [standard] = classical and stated as I know it from
the literature; [verify] = recalled from memory, to be checked against the source before use (the lambency-6 pass checks
these). Λ = the Leech lattice, J = the Albert algebra H3(O).

## Leech lattice

1. **The sign, the GL(1) layer, moonshine itself.** Aut(Λ) = Co0 = 2.Co1: the centre is the sign {±1}. The moonshine
   module V♮ is the orbifold of the Leech lattice vertex algebra V_Λ by the lift of −1 (Frenkel-Lepowsky-Meurman): the
   sign involution is exactly the step from Leech to the Monster. [standard]
2. **2 × 3 = 6 as a unit group.** Λ is a module over the Eisenstein integers Z[ω] (the complex Leech lattice, rank 12),
   with automorphism group 6.Suz, whose centre is μ6 = μ2 × μ3: the sign times the cube roots of unity, the rotation group
   of the hexagonal lattice (the (2,3,6) triangle group's lattice). [standard] So "1 × 2 × 3 = 6 with the sign as the 1"
   is the centre of 6.Suz acting on Λ.
3. **The 3-side: PG(2,3), AG(2,3), the tetracode.** The tetracode (length 4 over F3, the configuration of AG(2,3) inside
   PG(2,3)) builds the ternary Golay code (Conway's MINIMOG), whose automorphism group is 2.M12 [standard]; the complex
   Leech lattice over Z[ω] is built from the ternary Golay code [standard; SPLAG ch. 7]; the Niemeier lattice A2^12
   (lambency 3, umbral group 2.M12) has the ternary Golay code as glue [standard]. The 3-part of the A5^4 D4 glue is the
   tetracode (the main session's map) [verify].
4. **GL(2,3).** Aut(tetracode) has order 48 and acts faithfully on the 2-dimensional code space, so it is GL(2,3)
   [standard by this count; verify the order 48 in SPLAG]. In umbral moonshine the umbral group at lambency 6
   (X = A5^4 D4) is GL2(3), and also at lambency 12+4 (X = E6^4) [verify: Cheng-Duncan-Harvey, Table of G^X]. If so,
   the user's [the user's words, omitted] (GL(2,3)) is literally the symmetry group of lambency 6 and of the tetracode.
5. **S6 = Sp(4,2).** The sextet stabilizer of the Golay code in M24 is 2^6:3.S6, acting on the hexacode [standard]; the
   umbral group at lambency 6+3 (X = D4^6, the other Niemeier lattice of Coxeter number 6) is 3.S6 [verify, same table];
   S6 = Sp(4, F2) is the symmetry of the six points of a genus-2 picture and of the 2-torsion of its Jacobian [standard],
   which is where the S6 Paper II example's symmetry lives (level 2; broken at level 4). So Coxeter number 6 carries both
   of the user's groups: GL(2,3) (A5^4 D4) and S6 (D4^6).
6. **The 2-side: GL(3,2) = PSL(2,7).** GL(3,2) is the symmetry group of the Fano plane PG(2,2), the binary sister of
   PG(2,3) [standard]; the Fano plane is the multiplication table of the octonions [standard]; the Hamming [7,4] code is
   the Fano plane, its extension [8,4,4] gives E8 by Construction A, E8 is the lattice of integral octonions, three copies
   of the extended Hamming code give the Golay code (Turyn), and Λ is a lattice of triples of integral octonions
   (Wilson) [standard in outline; verify the exact forms]. So PG(2,2) (binary) and PG(2,3) (ternary) are the two roots of
   the two constructions of Λ: over Z with the Golay code, and over Z[ω] with the ternary Golay code.
7. **Lambency 6 and the deep holes.** The 23 Niemeier lattices with roots correspond to the 23 types of deep holes of Λ
   and each gives Λ back by the "holy construction" with its Weyl vector and Coxeter number h [standard; SPLAG ch. 23-26].
   Coxeter number 6 (A5^4 D4 and D4^6) is lambency 6: two deep-hole types of Λ.
8. **GL(1), GL(2), GL(3), GL(6) inside the Leech theta series.** θ_Λ = E12 − (65520/691) Δ [standard]. The Eisenstein part
   has L-function ζ(s)ζ(s − 11) (GL(1): its zeros are covered by Alpöge's theorem); the cusp part is Δ = η^24 (GL(2),
   Ramanujan's τ; GRH for L(s, Δ) is open). Sym²Δ is automorphic on GL(3) (Gelbart-Jacquet) and Δ × Sym²Δ on GL(6)
   (Kim-Shahidi), with L(s, Δ × Sym²Δ) = L(s, Sym³Δ) L(s, Δ) (trivial central character at level 1) [standard]. So the
   user's layers 1, 2, 3 and the product 2 × 3 = 6 all live in the L-functions of the Leech theta series.
9. **The sign field as GL(1) under all of it.** Euler's pentagonal theorem: η(τ) = Σ_{m ≥ 1} χ12(m) q^(m²/24), with χ12
   the quadratic character mod 12 (1 at m ≡ ±1, −1 at m ≡ ±5) [standard]. So η is the unary theta series of a sign
   character mod 12 = 2² × 3, and Δ = η^24 is the cusp part of θ_Λ: GL(1) (χ12) → η → Δ = η^24 (GL(2), Leech) → Sym²Δ
   (GL(3)) → Δ × Sym²Δ (GL(6)). The L-function of η is 24^s L(2s, χ12), so Alpöge's theorem puts all its zeros on the
   critical line (Re s = 1/4 in this normalization) [standard consequence]. (Z/12)^× has exactly three nontrivial
   characters, all quadratic: χ−4, χ−3, χ12 = χ−4 χ−3 — the sign at 2, the sign at 3 and their product [standard];
   whether these are Codex's "three quadratic signs" at j = 2304 is to check. Whether Alpöge's "sign field" is this
   object must be read in his remark.
10. **Pushing GRH through moonshine, first rung.** The shadows of the Mathieu and umbral mock modular forms are unary theta
   series Σ χ(n) n q^(n²/4m); their L-functions are 4m^s L(2s − 1, χ) for Dirichlet characters χ mod 2m [standard
   computation]. So Alpöge's theorem gives the Riemann hypothesis for the L-functions of every umbral shadow, at lambency 6
   for characters mod 12. The mock forms themselves, and Δ = η^24, are the next rungs (GL(2) and beyond: open).
11. **A coincidence to check, not claim:** 2304 = 48² = |GL(2,3)|²; Codex's elliptic curve point sits at j = 2304.

## Albert algebra

1. **24 and 27.** J = H3(O) is 3 real diagonal entries plus 3 octonions: 27 = 3 + 3 × 8; Λ as triples of integral
   octonions has 24 = 3 × 8 [standard]. Elkies and Gross relate Λ to an integral form of the exceptional Jordan algebra
   ("The exceptional cone and the Leech lattice", IMRN 1996) [verify the exact statement].
2. **Symmetry:** Aut(J) = F4; the cubic norm (determinant) is preserved by E6; 27 is E6's minuscule representation, the
   27 lines on a smooth cubic surface, with symmetry W(E6) of order 51840 [standard]; W(E6) has the index-2 subgroup
   PSp(4,3) = PSU(4,2), the exceptional isomorphism between a group over F3 and one over F4 ⊃ F2 [standard]: a 2-3
   identity at the heart of the Albert algebra.
3. **S6 again:** the 27 lines contain 36 double-sixes; the stabilizer of a double-six in W(E6) is S6 × Z/2 [standard,
   Schläfli]. So the user's S6 = Sp(4,2) (level 2) sits inside W(E6) next to PSp(4,3) (level 3).
4. **A5 and D4, the components of A5^4 D4:** D4 = Spin(8) inside F4 = Aut(J), fixing the diagonal (triality) [standard];
   E6 ⊃ SU(6) × SU(2) (A5 × A1) maximally, with 27 = (6̄, 2) ⊕ (15, 1) [standard]: the root system of lambency 6 appears
   as the natural subalgebras of the Albert algebra's symmetry, and 27 = 2 × 6 + 15.
5. **GL(3,2) and the octonions:** the Fano plane (GL(3,2)) is the multiplication table of the off-diagonal entries of J
   [standard].

## What to carry into the pass (identities -> implications)
- Item 9-10: RH for the L-functions of η and of every umbral shadow follows from Alpöge's theorem; ask what this says
  about lambency 6 specifically (characters mod 12, the three quadratic signs) and whether the S6 Paper II example's
  level-2 symmetry is the same S6 as the umbral 3.S6 at 6+3.
- Item 4-5: if the umbral groups at Coxeter number 6 are GL(2,3) and 3.S6, then the tetracode (AG(2,3) inside PG(2,3),
  the fleet's L-meta-650 plane) and the genus-2 level-2 structure are the symmetries of the two lambency-6 Niemeier
  lattices: test what the circuit question on PG(2,3) gains from GL(2,3) and the Singer group (order 39, with the polarity
  78).
- Item 8: the GL(2) x GL(3) -> GL(6) product applied to Δ is inside θ_Λ: what does the user's [the user's words, omitted] give for
  Δ, and does GRH for L(s, Δ × Sym²Δ) have a moonshine form.

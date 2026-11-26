# Moonshine, the Leech lattice and our algebra: commentary on the 26 maps, and a structural note towards global Langlands

By Claude Opus 5.5 at effort high (agent ad21742d9ec151965 of the main session 329fb1e6), 23 Nov 2026, evening, for
the brief `BRIEF.md` in this folder. The maps commented on are
`<local>/pequalnp_work\fleet_map\maps\moonshine_leech.md` (ML-1 to ML-12) and `algebra_combinatorics.md`
(AC-1 to AC-14), written by the same agent earlier today. Work file:
`<local>/Documents\agent_notes\ad21742d9ec151965_NOTES.md`. Scripts:
`<local>/Documents\agent_notes\structural_moonshine_scripts\` (`hecke_lattices.py`, `psl2_level.py`,
`klein_level.py`, `klein_planes.py`).

**Flags.** [opened] read at the source for this note, with locator. [computed] my script; numerical unless it says
exact; checked by no one else. [mine] my derivation on paper, checked by no one else. [memory] not checked against a
source in this task; no status rests on it. Nothing here is graded.

**Two results of this task.**
1. **The PSL2(7)-symmetric slice of the level-space problem (L-gct-086) is Klein's quartic.** PSL2(7) acting on
   8 x 8 matrices through P^1(F_7) has two 3-dimensional isotypic components with non-real character. On each, S_1 =
   S_2 = 0 identically (the Weil-type isotropy of section B.6), S_3 = S_5 = S_7 = 0, S_8 = λ S_4^2 with λ ≈ 0.002834,
   and S_4, S_6 have exactly 24 common zeros in P^2: 24 level lines, none two of which span a level plane [computed].
2. **The Hecke decomposition of our lattice J** (S6_05 B.3): Θ_J = (7381/66430) E_12(τ) + (59049/66430) E_12(3τ)
   − (264069/11747) Δ(τ) − (103276701/11747) Δ(3τ) + (14823/1241) f, with f = q + 78q^2 − 243q^3 + 4036q^4 −
   5370q^5 − ... the T_2-eigenform of S_12^new(Γ0(3)) (T_2-eigenvalue 78) [computed, exact rational arithmetic to
   q^24; the input formula reproduces B.3's eight printed coefficients].

---

# Part A. Commentary on the 26 maps, ranked by the mathematics they suggest

Each entry: what the map suggests, then the next statements to prove or compute.

### A1. AC-1: monotone Boolean circuits as circuits over an inverse semiring (the support class Sup(G))
The map says that every lower bound question of the meta program (606, 608, 612, 647) is an arithmetic question about
monotone circuits for polynomials with prescribed minimal supports, and that the Boolean difficulty is concentrated in
one place: monomials that cover an edge only through x^2 = x or through absorption. It is the cleanest way I found
to state what the fleet's line-degree ladder climbs around, and it is uniform in G.
Next statements:
1. (Lean) Lift lemma: evaluating a gate list in T_n (the Grothendieck construction of CFMM Thm 8.5 over the semiring
   of monotone Boolean functions) returns (f_C, P_C); support criterion for f_C = f_G.
2. (Proof) Bihomogeneous component lemma with its constant: a monotone arithmetic circuit of size s for P yields one
   of size ≤ s + c for the (1,1)-component; determine c.
3. (Proof) The charge for E \ E' (edges covered only by non-multilinear or non-minimal monomials): show each such edge
   costs one extra gate, or find the Petersen-type counterexample (584 has 13 OR gates where |E| − 1 = 14).
4. (Computation) For the fleet's 20-gate Petersen circuit (584), compute P_C and E'.

### A2. ML-4: symmetric level spaces from non-real isotypic components (with this task's Klein computation)
The map predicted that non-real isotypic pieces are S_2-isotropic. This task tested the first formulation (PSL2(p)
acting diagonally on Mat_{p+1}) [computed, `psl2_level.py`]:

| p | n | non-real components | S_k vanishing on them | level? |
|---|---|---|---|---|
| 3 | 4 | two, dim 1 | S_1, S_2, S_4 = 0; S_3 ≠ 0 | no |
| 5 | 6 | none | — | — |
| 7 | 8 | two, dim 3 | S_1, S_2, S_3, S_5, S_7 = 0; S_4, S_6, S_8 ≠ 0 | 24 level lines in each |
| 11 | 12 | two, dim 5 | S_1, S_2 = 0 (S_4 ≈ 0 at 3e-8); S_3 ≠ 0 | no |

At p = 7 the level problem on W becomes plane algebraic geometry: S_4|W and S_6|W are PSL2(7)-invariant forms of
degrees 4 and 6 on the 3-dimensional representation, S_8|W = λ S_4|W^2 (ratio constant to 10^-6 on samples), and the
level lines in W are the common zeros of S_4 and S_6 in P(W): 24 found from 400 Newton starts, each checked as
perm(J + zt) = 8! to 10^-9 [computed, `klein_level.py`]. The invariant quartic of this representation is Klein's
quartic and 4 · 6 = 24 is its number of flexes [memory: uniqueness of the invariant quartic, the flex count]. No two
of the 24 lines span a level plane [computed, `klein_planes.py`]; inside W this is forced, since a level plane would
be a projective line on the smooth quartic.
Next statements:
1. (Exact computation over Q(√−7)) S_4|W = c_4 Φ_4, S_6|W = c_6 Hess(Φ_4) + c_6' (nothing else in degree 6),
   S_8|W = λ S_4|W^2 with λ exact; hence "the level lines of W are the 24 flexes of Klein's quartic".
2. (Next formulation) Level spaces meeting several components: L ⊂ W ⊕ W̄ ⊕ (real components) with the S_2 cross pairing
   W × W̄ → C; at p = 7 compute the maximal dimension of a level space containing a flex line.
3. (Other groups) The same table for PSL2(13), PSL2(23) ⊂ M24 (n = 24, needs a C or Rust Ryser), M11 on 12 points,
   M12 on 12, and the regular Klein four (Codex's class at n = 4).

### A3. ML-3: the Leech-root ladder (subdivided Petersen, Tutte's 8-cage, PG(2,4), Higman–Sims)
One construction (Vinberg's algorithm on I_{n,1} with the Leech control vector, SPLAG Ch. 28 p. 551) produces exactly
the graphs the meta program needs: bipartite, girth ≥ 6, large automorphism groups. Its interest is that it gives the
fleet a family with a reason, not a list.
Next: circuits below 39 (subdivided Petersen) and 59 (Tutte's 8-cage) by SAT; the AND-count values (632) on both;
whether the n = 22 Higman–Sims step (4-cycles present) gives the first instance where |E| + τ − 1 fails on a
triangle-free graph with this much symmetry.

### A4. ML-1 with AC-2: the 650 plane as tetracode completion and as Singer set {0,1,3,9} mod 13
The two descriptions are dual: the tetracode sees PG(2,3) from a line (AG(2,3) and four parallel classes); the Singer
form sees it from a cyclic group of order 13 with multiplier 3 and polarity (a group of order 78 acting on f).
Next: (a) exact monotone size of the AG(2,3) incidence function (target 44); (b) a Z/13 ⋊ Z/3-invariant SAT search at
63 gates; (c) the additivity lemma for adding a point at infinity; (d) the Lean lemma "pg23 edges = Singer edges" by
`decide`.

### A5. ML-5: frame shapes and rank-one level lines
Frame shapes (TASI (1.21)-(1.22) [opened]) encode det(1 − t ρ(g)) = ∏ (1 − t^{i_r})^{ℓ_r}; with the checked 089 the
rank-one level lines x y^T are exactly the pairs of e-sequences with disjoint support, and eigenvalue vectors of
permutations have e-generating functions ∏(1 − (−t)^d)^{a_d} [mine]. So the rank-one part of 086 is the combinatorics
of frame shapes, the same data that index eta products in moonshine.
Next: classify pairs of frame shapes of length n with disjoint positive e-supports (n ≤ 24); for each, the dimension of
the span of the corresponding lines that stays level; compare with 2n − 3.

### A6. AC-4 and AC-5: the S_k expansion in singleton-free invariants, and GCT_PLETH's moment maps
This is the most direct algebraic route to 086 (route R2 of gct.md): S_k = ((k−1)!/k) p_k + (connected invariants
with blocks ≥ 2), with GCT_PLETH R-046/R-050 as the tool that writes these invariants in a power-sum moment basis.
The Klein computation shows how these invariants restrict to a symmetric slice: there they become the invariant ring of
the group (degrees 4, 6, 8 at p = 7).
Next: exact fits of S_5, S_6 on doubly centred matrices; dimension of the S_n × S_n-invariants of degree ≤ 8 on DC
matrices; the conjunction of moment conditions to which 067 applies.

### A7. ML-7: our lattice J, the 129 Co0-orbits of isotropic planes, and J's Hecke decomposition
Part B.4 below gives Θ_J's decomposition into Eisenstein, old (Δ) and new (level 3) parts. The orbit classification
B.9 is a complete list of ternary isotropic planes with group data, a test bed for the binary isotropy lemma 092.
Next: the theta series of each of the 129 plane-sublattices (each an index-9 sublattice of Λ of determinant 81 with
the same weight-12 Γ0(3) shape) and the newform coefficient z for each: 129 values of one GL_2 coordinate.

### A8. ML-2: the Golay code hands over PG(2,4) and its hyperovals
Next: the order-4 row of the one-NOT ladder (value 14, computed); the 745 recursion at q = 4; the 124-gate search.

### A9. ML-8: dessins of X0(p) as explicit expanders
Next: the comparison between the spectral gap of Γ0(p)\H and the boundary expansion of its (2,3)-dessin, at the
parameters of pcx 043/046.

### A10. AC-3: our proof of 647 (line-degree 1)
Next: a second reader; Lean of the OR-only 529 and of 738.

### A11. AC-6: GCT obstructions and L-gct-011
Next: the barrier row "no occurrence obstruction for c ≥ 25, m ≥ 5" from GCT_FLIP read at the source; the formal
c ≤ 2 case.

### A12. AC-10: λ-rings in characteristic p and the level problem over F_p
Next: the level problem over F_3 stated through the S_k; the collapse of the q = 3 barrier family when ω = 1.

### A13. ML-6: the Leech form mod 2 as a 24-bit inner-product gadget
Next: the flat bound for IP_{2m}; the 081/082 pair statistics by Co_1-orbit counts.

### A14. AC-8: image substitution (F-13) and riffle rank
Next: R(2, n) for 3n − 3; Lean of 139.

### A15. ML-9: the lattice-lane cubics as smooth forms
Next: Jacobian ideals of the Albert, Wilson and E8^3 cubics; if smooth, the 024 bound.

### A16. AC-11: H17 (Δ = 0 on GT-hat) — see B.2, where it meets the D1 lattice lane at level 12
Next: the finite part of H17 (frames in PSL2(Z/12)) as a `decide` statement.

### A17. ML-10: Conway–McKay–Trojan's additive polynomials against 664/685
Next: read CMT §1-2; line-intersection types of their level sets in PG(2, 2^k).

### A18. AC-12: hitting sets (CUE_GCT I-chapter) against clb
Next: read the I-chapter in full; one row per construction.

### A19. AC-7: the padded-permanent Hessian (O-011.1)
Next: the exact-dc chain 021 ⇐ 020 in the padded setting.

### A20. ML-11: Golay and Hamming parity checks against 639/640
Next: exact joint size of the seven Fano line-XORs.

### A21. AC-13 and A22. ML-12: Hasse–Witt evaluators against L-alg-001
Next: the candidate in the alg format; the PC-degree of coefficient extraction.

### A23. AC-9: border rank of det_4 and per_4 ≥ 43
Next: a proposed GCT row with a finite certificate.

### A24. AC-14: the Erdős–Straus selector
Next: none beyond stating the search.

---

# Part B. Moonshine and the Leech lattice towards global Langlands

## B.0 The rungs, and where each object of ours sits

| rung | automorphic side | in moonshine / Leech | ours |
|---|---|---|---|
| GL_1 over Q | Dirichlet characters, ζ; **RH proved for all Dirichlet L-functions (Alpöge)** | the η^2 multiplier SL2(Z) → Z/12; class numbers H(D) in umbral moonshine; unary theta series (umbral shadows); Eisenstein parts of lattice thetas | D1-9 determinant character e(−χ/12); H17's frames at level 12 |
| GL_1 over K imaginary quadratic (= dihedral GL_2 over Q) | Hecke characters of K | weight-one eta products such as η(τ)η(23τ); CM values of Hauptmoduln (singular moduli) | H15 (CM points), H05 (RH for CM motives under Masullo) |
| GL_2 over Q | holomorphic eigenforms | Δ in Θ_Λ; the level-3 newform f in Θ_J; Tunnell's weight-3/2 form and y^2 = x^3 − x (umbral M11 and congruent numbers) | Θ_J's newform coefficient (B.4) |
| lifts | Shimura/Waldspurger, Borcherds | Monster denominator formula j(p) − j(q) = p^{-1}∏(1 − p^m q^n)^{c(mn)}; shadows ↔ weight 3/2 | — |
| trace formula / traces | Selberg, Connes | Thompson series = graded traces; Rademacher sums | H27 (Connes's trace formula ⇔ GRH for Dirichlet L, T51) |
| symmetry eigenspaces | Weil-type Hodge classes | non-real isotypic pieces | H12, H25 (Weil classes); ML-4 / Klein slice |

## B.1 GL_1 in moonshine: three places where Alpöge's theorem enters

**(a) Umbral shadows are GL_1.** [mine] A unary theta series of weight 3/2,
g_ψ(τ) = Σ_{n≥1} ψ(n) n q^{n^2/4m}, ψ an odd Dirichlet character mod 2m, has Mellin transform
∫_0^∞ g_ψ(iy) y^{s−1} dy = Γ(s) (2m/π)^s Σ ψ(n) n^{1−2s} = Γ(s)(2m/π)^s L(2s − 1, ψ).
So its L-function is a Dirichlet L-function in the variable 2s − 1, and for primitive ψ its nontrivial zeros lie on
Re s = 3/4 by Alpöge's theorem. The shadows of the umbral mock modular forms are vectors of unary theta series
S_{m,r} = Σ_{n ≡ r (2m)} n q^{n^2/4m} [memory: CDH's definition; the dictionary's row 19 cites it from MAP.md];
the combinations g_ψ = Σ_r ψ(r) S_{m,r} diagonalize the action of the multiplicative group (Z/2m)^× on the index r,
which is the Atkin–Lehner/Eichler–Zagier symmetry of DICT row 7. Hence: **every shadow component in the character
basis has its zeros on one line, now unconditionally.**
Next rung: the mock form itself (the holomorphic part H^X) has no Euler product; its "L-function" through the
completion involves the shadow's L-function and a non-holomorphic correction. The concrete next statement is the
functional equation of the Mellin transform of the completed form Ĥ^X in terms of L(2s − 1, ψ).

**(b) Class numbers in umbral moonshine.** [opened] Cheng–Duncan–Mertens, *Class numbers, congruent numbers and
umbral moonshine* (`F:\user\Documents\arxiv_latex\library\moonshine_lattices\...\main.tex`): Theorem
`thm:mat-opt:tor` classifies the optimal M11-modules (lattice of rank 2 spanned by φ_11 ⊗ (χ_1 − χ_2 − χ_3 − χ_4 −
χ_6 + χ_9) and φ_11 ⊗ (χ_1 − χ_2 − χ_3 − χ_4 − χ_7 + χ_9), with c^opt = 2); in the proof of Theorem
`thm:mat-art:cngnmb`, C_1(D) = 24 H(D) (Hurwitz class number) and, for fundamental D,
m_55(W_D) = (D/3)(1 − (D/8)) H(D) + (1/4) Re(λ_{8|4}) C_{8|4}(D).
The first term is GL_1: H(D) is a multiple of √|D| L(1, χ_D) [memory: Dirichlet's class number formula]. With RH
for L(s, χ_D) the size of L(1, χ_D) is controlled by log log |D| [memory: Littlewood's conditional bounds]; these now
hold unconditionally. So the multiplicity of the 55-dimensional M11-representation in the umbral module, for
discriminants with D ≢ 0 mod 3, is governed by a GL_1 quantity whose fluctuation Alpöge's theorem bounds.
Next statement: explicit two-sided bounds for m_55(W_D) in terms of √|D| and log log |D| from Alpöge's theorem, for
D ≢ 0 mod 3, separating the class-number term from the cusp term.

**(c) Eisenstein parts of lattice theta series.** For an even unimodular lattice of rank 24 the Eisenstein part of the
theta series is E_12, whose L-function is ζ(s)ζ(s − 11) (up to a constant) [memory]. For the Leech lattice
[opened: SPLAG Ch. 4 (140)-(142), p. 134] N(m) = (65520/691)(σ_11(m) − τ(m)); [computed] this reproduces 196560,
16773120, 398034000. So the shell counts of Λ split as a GL_1 term (σ_11) minus a GL_2 term (τ). Counting Leech vectors
in arithmetic progressions of norm, Σ_{m ≡ a (N)} N(m) m^{−s}, brings in L(s, χ)L(s − 11, χ) for Dirichlet χ mod N
[mine], so Alpöge's theorem places the zeros of the main term on two lines.

## B.2 GL_1 at level 12: the D1 lattice lane, H17 and the moonshine dictionary meet

- D1-9 [opened in D1's notes]: for N(A5^4 D4) the 12-dimensional theta (Weil) representation of index 6 has
  determinant e(−χ(γ)/12), χ the multiplier character of η^2, χ(T) = −1, χ(S) = 3; Hom(SL2(Z), C^×) = Z/12.
- DICT rows 7-9 [opened]: the exact divisors of 6 give a(3) = 5, a(2) = 7, a(6) = 11, and {1, 5, 7, 11} is the
  centre of SL2(Z/12); the frame 5I of LM7_PUSH E.58 is a(3); the dictionary's hunch 4.1 was "Δ = 0 on ĜT".
- H17 [opened: abstract, Theorems IV, Λ, δ, Corollary Δ]: δ = a_2 + a_3 on H_0 ⊂ GT-hat, defined by the images of the
  frames of s and r (the two elliptic points) in PSL2(Z/12); δ vanishes on normalized elements; every Δ: GT-hat → F_2
  trivial on G_Q and equal to δ on Λ_0 is 0.

So the question the dictionary recorded as hunch 4.1 is answered by H17's Corollary, to the extent that E.65's Δ is
H17's Δ (the check: E.65's definition against H17 §δ, a reading task). The structural point: **the GL_1 layer at level
12 (the abelianization Z/12 of SL2(Z), the η^2 character, the centre {1,5,7,11} of SL2(Z/12)) is where the lattice
lane, the umbral index-6 cases (A5^4 D4 and D4^6) and Grothendieck–Teichmüller theory touch.** On the Galois side
this layer is Gal(Q(ζ_12)/Q) = (Z/12)^× = {1, 5, 7, 11}; Alpöge's theorem covers the four Dirichlet L-functions mod 12.
Next statement: the restriction of δ to the Galois elements is the character of Gal(Q(ζ_12)/Q) that H17's frames
induce; compute it on the four classes (a finite computation in PSL2(Z/12)) and identify it among the Dirichlet
characters mod 12 (trivial, χ_{−4}, χ_{−3}, χ_{12}).

## B.3 GL_1 over imaginary quadratic fields: weight-one eta products

The Frame/cycle shape 1·23 (an element of order 23 of M24 on 24 points [memory]) gives the eta product
η(τ)η(23τ). [computed, `hecke_lattices.py`] η(τ)η(23τ) = (θ_{[1,1,6]} − θ_{[2,1,3]})/2 through q^59, and its p-th
coefficient equals (number of roots of x^3 − x − 1 mod p) − 1 for every prime p < 60, p ≠ 23. So this moonshine
eta product is the weight-one form of the class group of Q(√−23) (order 3), i.e. a Hecke character ψ of order 3 of
K = Q(√−23), automorphically induced to GL_2 over Q, with Galois representation the S3-extension cut out by
x^3 − x − 1 [the identification by computation; the general theory: memory].
- Alpöge's theorem covers L(s, χ_{−23}) (the Dirichlet factor of ζ_K) but not L(s, ψ) (a class-group character of K).
- **Next rung, concrete:** RH for L(s, ψ) for ψ a class-group character of an imaginary quadratic field: GL_1 over K.
  This is the rung that the eta products of weight one in moonshine sit on, and also the rung of our CM lines (H15,
  H05).

## B.4 GL_2: the Hecke structure of Θ_Λ and of Θ_J

- Λ: Θ_Λ = E_12 − (65520/691)Δ (B.1(c)). One cusp form, Δ: the GL_2 content of the Leech lattice's theta series is
  L(Δ, s).
- J (our lattice; S6_05 B.3 [opened: statement and formula, sections/B.tex l. 207-224]):
  Θ_J = (7381/66430) E_4^3(τ) + (59049/66430) E_4^3(3τ) − (531432/6643)Δ(τ) − (4251528/6643)Δ(3τ) +
  (88938/73) η^{12}(τ)η^{12}(3τ).
  [computed] S_12(Γ0(3)) has basis Δ(τ), Δ(3τ), g = η^{12}(τ)η^{12}(3τ); T_2 has eigenvalues −24 (twice, the old space
  from Δ) and 78, with eigenvector f = q + 78q^2 − 243q^3 + 4036q^4 − 5370q^5 − 18954q^6 − 27760q^7 + 155064q^8 +
  59049q^9 − 418860q^10 + 637836q^11 − 980748q^12 + ... (normalized). Then
  **Θ_J = (7381/66430) E_12(τ) + (59049/66430) E_12(3τ) − (264069/11747) Δ(τ) − (103276701/11747) Δ(3τ) +
  (14823/1241) f.**
  So J's theta series carries one new GL_2 automorphic representation, of level 3 and weight 12, absent from Λ's.
  Its coefficient a_3 = −243 = −3^5 is the Atkin–Lehner datum at 3.
- **The counting function.** r_J(2m) = Eisenstein term (σ_11 at the two cusps; GL_1: ζ(s)ζ(s − 11) with an Euler
  factor at 3) + old term (τ(m), τ(m/3)) + new term (14823/1241) a_f(m). The GL_1 part has its zeros placed by
  Alpöge's theorem; the GL_2 parts are L(Δ, s) and L(f, s).
- Next statements: (1) the same decomposition for the 129 index-9 sublattices of B.9 (are all their theta series in
  M_12(Γ0(3)) with the same newform, differing only in z?); (2) the Leech neighbours Λ_0, Λ_1, Λ_2 ⊃ J and the two
  A2^12 ⊃ J: Θ_{Λ} − Θ_J and Θ_{A2^12} − Θ_J in this basis (their newform coefficients are −z and a computable
  number); (3) twisted shell counts Σ r_J(2m) χ(m) m^{−s} for χ mod 3.

## B.5 Lifts: Borcherds products, theta lifts, Waldspurger

- **Borcherds' denominator formula** [opened: Borcherds, Invent. Math. 109 (1992), p. 408]:
  p^{−1} ∏_{m>0, n∈Z} (1 − p^m q^n)^{c(mn)} = j(p) − j(q), the denominator formula of the Monster Lie algebra, whose
  root (m, n) has multiplicity c(mn) = dim V_{mn}; the replication formulas of Conway–Norton follow from the twisted
  denominator formulas (abstract, p. 405). This is the product side of a theta lift: the exponents c(mn) are Fourier
  coefficients of the input j, and the output is a modular function in two variables.
- **Traces of singular moduli** [opened: TASI (5.26) and (2.48)-(2.49)]: in Thompson moonshine the coefficients are
  traces of J over CM points of discriminant −3n, weighted by a genus character; the generating function of Hurwitz
  class numbers H(D) is the weight-3/2 Eisenstein-type series of (2.49). This is the bridge from Hauptmoduln (genus
  zero, weight 0) to weight 3/2, i.e. to the Shimura/Waldspurger correspondence.
- **Waldspurger in umbral moonshine** [opened: CDM, proof of `thm:mat-art:cngnmb`]: for D ≡ 21 mod 24 the multiplicity
  m_55(W_D) equals (1/4)Re(λ_{8|4}) a(|D|), a(n) the coefficients of η(4τ)^5 η(16τ)/(η(2τ)^2 η(8τ)), and by Tunnell's
  Theorem 3, L(E ⊗ D, 1) = C a(|D|)^2 for E: y^2 = x^3 − x; nonvanishing then gives finiteness of E ⊗ D(Q) (Coates–Wiles
  as cited there). So an M11-multiplicity in umbral moonshine is a square root of a central GL_2 L-value.
- **The ladder this makes:** class numbers (GL_1, B.1(b)) and central values of quadratic twists of an elliptic curve
  (GL_2, through a weight-3/2 theta lift) are two summands of one representation-theoretic multiplicity.
  Next statement: for the umbral M11-module, the distribution of m_55(W_D) over D ≡ 21 mod 24 in terms of the
  distribution of L(E ⊗ D, 1); and, at the next rung, GRH for L(E ⊗ D, s) bounds a(|D|) by |D|^{1/4+ε}.

## B.6 Symmetry eigenspaces: the Weil-type mechanism in Hodge theory and in L-gct-086

**The lemma** [mine; standard representation theory]. Let G act on a complex vector space V and let B be a
G-invariant bilinear form. For irreducible G-submodules W, W' ⊂ V, B restricted to W × W' is a G-map W → (W')*, hence
0 unless W ≅ (W')*. In particular B|W×W = 0 whenever W ≇ W*, i.e. whenever the character of W is not real.

**Instance 1, Hodge (Weil type).** An abelian variety A with K = Q(√−d) ⊂ End^0(A) acting on H^1(A, Q); over C,
H^1 = V_σ ⊕ V_σ̄ (the two eigenspaces of K ⊗ C = C × C); the polarization E satisfies E(ax, y) = E(x, ā y), so
E(V_σ, V_σ) = 0 by the computation a ↦ σ(a) vs σ(ā). The Weil classes live in the top exterior power over K of
H^1 [memory: definition of Weil type]. Ours on this mechanism: H12 (bounded division for Weil classes for every
imaginary quadratic K and every n, with explicit constants, and the ghost-class dichotomy) and H25 (the Hodge
conjecture for abelian varieties equivalent to a Poincaré-pairing bound on the multiplier; split Weil families)
[relayed: `field_experts\hexagon\HEXAGON_STATUS.md` rows H12, H25].

**Instance 2, level spaces (ML-4, this task).** G = PSL2(p) acting on Mat_{p+1}; B = the quadratic form S_2 (and the
Hessian form of O-011). On non-real components S_2 vanishes identically [computed for p = 3, 7, 11].

**Dictionary.**

| Weil type (Hodge) | level spaces (GCT) |
|---|---|
| K^× acting on H^1 through σ, σ̄ | G acting on Mat_n through χ, χ̄ |
| polarization E, E(ax, y) = E(x, ā y) | S_2 (Hessian of perm at J), G-invariant |
| V_σ is E-isotropic | non-real component W is S_2-isotropic |
| Weil classes in ∧^n_K H^1 (top degree) | the higher layers S_3, ..., S_n restricted to W |
| Hodge question: are Weil classes algebraic? | level question: do S_3, ..., S_n vanish on W? |

At p = 7 the second column has a complete answer on W: the higher layers restrict to the invariant ring of the
3-dimensional representation (odd degrees vanish, degree 4 and 6 generate what appears through degree 8), and the
level lines are the 24 common zeros of the quartic and the sextic (A2). The Hodge column's analogue of "restrict the
higher layers to the eigenspace and read off an invariant ring" is the computation of the Mumford–Tate invariants on
∧^•_K H^1. Next statement (GCT side): for each finite G ⊂ S_n × S_n and each non-real component W, the ideal generated
by S_3|W, ..., S_n|W in the invariant ring C[W]^G; the level lines of W are its zero set.

## B.7 Traces: Thompson series, Rademacher sums, and Connes's trace formula

- Thompson series [opened: Borcherds p. 405-406]: T_g(q) = Σ Tr(g | V_n) q^n, with T_1 = j − 744; each is the
  normalized Hauptmodul of a genus-zero group (Theorem 1.1 and the remark after it). TASI §5 [opened, line 2492 ff.]:
  the genus-zero property is equivalent to the Hauptmodul being a Rademacher sum of its single polar term.
- H27 [relayed: HEXAGON_STATUS]: Connes's trace formula over Q with explicit cutoff is equivalent to GRH for Dirichlet
  L-functions (T51), hence holds now; S50 gives finite prime-built approximants of Ξ/Ξ(0) with multiplicities.

Dictionary: both are trace identities on a graded space, with a positivity behind them: in moonshine the graded
dimensions dim V_n are nonnegative integers (the no-ghost theorem, Borcherds Thm 5.1 [opened: statement title only],
supplies the Lie algebra whose denominator formula carries them); in Connes's formula the positivity of the Weil
functional is the GRH side. The concrete common object is a spectral sum over a lattice of "periods" (the cusps and
their Rademacher images; the primes and their powers). Next statement: write the Rademacher sum for T_g (g of level N)
and Connes's cutoff trace for a Dirichlet character mod N side by side, with the same cutoff parameter, and compare
their error terms; the second is now controlled by Alpöge's theorem.

## B.8 GCT: multiplicities, positivity and denominators

- CDM [opened]: c^opt_{2,1}(M11) = 2, the least positive integer making the characters of the optimal modules integral
  (Theorem `thm:mat-opt:tor`); likewise for 2.M12 (Theorem `thm:mat-um3:tor`).
- Ours: GCT VI's positivity hypotheses PH2, SH(a), PH3 fail (H02, H02b, H23); the largest vertex denominator of the
  n-fold Kronecker polytopes is 2^(n−1+floor((n−2)/7)) (GPK18) [relayed: HEXAGON_STATUS].

Dictionary: in both, a generating function of virtual characters becomes a genuine module only after an integrality and
positivity correction, and the correction is measured by a denominator (c^opt in moonshine; the vertex denominators
and the denominator weight 2^(n−1) of PH3 forms in GCT). Next statement: for the Kronecker coefficients
g((s^n),(s^n),(s^n)) compute the least c with c times the generating function having a positive formula of the PH3
shape, as CDM compute c^opt; H02b says this c is at least 2^(n−1).

## B.9 What it suggests, most promising first

1. **The Klein slice of 086, exactly** (A2): prove over Q(√−7) that S_4, S_6, S_8 restrict to W as the Klein quartic,
   a combination with its Hessian, and λ times the quartic squared; hence 24 level lines. Then the first mixed
   formulation (W ⊕ W̄ with the S_2 pairing). This is the first place where the level-space problem has been solved on a
   symmetric slice by invariant theory, and the Weil-type dictionary (B.6) says where to look next.
2. **Θ_J's newform and the 129 planes** (B.4): one GL_2 coordinate z for each of the 129 orbit sublattices; their
   theta series as a family in M_12(Γ0(3)).
3. **The level-12 GL_1 layer** (B.2): the character that H17's frames induce on Gal(Q(ζ_12)/Q), identified among the
   four Dirichlet characters mod 12; E.65's Δ against H17's Δ.
4. **Umbral multiplicities from L-values** (B.1(b), B.5): unconditional bounds on the class-number part of m_55(W_D);
   the cusp part as √L(E ⊗ D, 1) — the GL_1 → GL_2 step inside one module.
5. **Shadows** (B.1(a)): the functional equation of the completed mock form's Mellin transform in terms of
   L(2s − 1, ψ).
6. **The inverse-semiring lift** (A1): the bihomogeneous component lemma and the E \ E' charge.
7. **The Leech-root ladder** (A3): searches at 39 and 59 gates.
8. **Weight-one eta products** (B.3): the list of weight-one eta products from M24 and Co0 frame shapes, each with its
   Hecke character of an imaginary quadratic field: the GL_1/K rung that Alpöge's theorem does not reach.

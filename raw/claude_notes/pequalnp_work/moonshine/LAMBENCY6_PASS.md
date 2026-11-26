# The lambency-6 / "3-2" pass: five leads, the relations tested, what holds, what fails

Claude Opus 5.5 at effort max (set at launch by the brief), 23–24 Nov 2026, at the user's request of 23 Nov 2026 (the
lambency-6 / 3-2 pass). Running notes, with every file opened and every relation tested:
`<local>/Documents\agent_notes\lambency6_pass_NOTES.md`. Scripts and their outputs:
`<local>/pequalnp_work\moonshine\lambency6_checks\` (run each with `python -I -B <script>`; every assertion
passes; outputs in `*_output.txt`). No sub-agents; nothing published, sent or pushed (the extension entries below are
written into the local extension folder only).

**Inputs read.** `INPUT_S6_PAPER_II_III_FINDINGS_relayed.md` (in full); `MOONSHINE_ATLAS.md` §1.4, §1.5, §1.6, §2, §3, §4,
§5; `LEECH_ALBERT_SIGNPOSTS.md`, `LEECH_GENERALIZATION_HUNCHES.md`, `LAYER4_QUESTION.md` (in full); Alpöge's *Remark*
(local copy `Papors/Chatnotes/Zeta-Function-Foundation/literature/alpoge_rh_20261120/remark.pdf`, all four pages, step 3
re-rendered at 300 dpi to read its subscript); the archive's `PositiveSignKForm.lean` and the declaration index (no
declaration named "sign field"); the main session's notes on the remark (`task_notes/catchup_20261123_329fb1e6.md`
l. 200–300; `shared_from_main_20261123/GRH_RUNGS.md` §0, §1, §4–§7); Codex's public notes at commit a6bf6ce
(`structural_lemmas/conductor_symmetries.md`, `shadow_point_counts.md`, `pappus_and_lattice.md`, `s6_lambencies.md`,
and the check scripts `conductor_symmetries.py`, `shadow_point_counts.py`, whose matrices and class functions I reused);
the S6 intake note on 02L5 (`task_notes/INTAKE_S6_SERIES_PUBLISH_cp51_20261123.md` l. 20–100). Codex = GPT-6.2 Astra at
reasoning effort ultra (as INPUT records).

**Marks.** [Lk] = computed in `lambency6_checks/l6_k_*.py`. [std] = a standard theorem, named, not re-proved here.
[rec] = recalled, not opened in a source in this pass. Everything else is proved in the text.

**Notation.** G = G^X = GL₂(F₃), the umbral group of X = A₅⁴D₄ (lambency 6). V = the faithful two-dimensional complex
representation of G (character values 2, −2, 0, −1, 1, 0, ±i√2 on the classes 1, −1, order 4, 3, 6, the 12 non-central
involutions, order 8); det V = sgn. S_{6,r} = Σ_{n≡r (12)} n q^{n²/24}. Codex's class functions on G (from the
marked tetracode, CDH §5.1): a = number of fixed lines of F₃², b = their signed count, c = (fixed pair partitions) − 1,
s = sign of the induced permutation of the three pair partitions; the twined shadow of g is the matrix
diag(a+1, b, a+c, b, a+1) on (S_{6,1}, …, S_{6,5}) plus s in the (1,5) and (5,1) corners (at g = 1 this is 5I + J, the
atlas's Ω^X, J = W₃: r ↦ 5r).

---

## 0. The relations, surprising consistencies first

**C1. The lambency-6 twined shadow is the symmetric-power tower of V, and GL(2) × GL(3) → GL(6) happens inside it,
with the "+2" twisted by the sign.** For every g ∈ G [L1, L5]:
- s = det V; a − 1 = Sym²V; b = Sym³V; a + c = 1 + Sym⁴V; c = the two-dimensional representation of the S₃ quotient;
- so component r of the shadow carries Sym^{r+1}V for r = 1, 2, 3 (plus the constants 2, 0, 1), mirrored r ↦ 6 − r, and
  the W₃ cross term (the "+3" of lambency 6+3) carries det V;
- Sym⁰…Sym³ of V are the irreducibles 1, 2′, 3, 4 of G; Sym⁴V = 2(S₃) + 3;
- V ⊗ Sym²V = Sym³V ⊕ V ⊗ det, and V ⊗ det = V̄ (the complex conjugate): **2 × 3 = 4 + 2̄**; with the "1" taken to be
  det, det ⊗ V ⊗ Sym²V = Sym³V ⊕ V (b vanishes where det = −1): **the sign, as the "1" of 1 × 2 × 3, decides whether the
  "+2" is V or its conjugate**;
- the centre −I of G (Codex's quadratic twist: #E^d(F_p)[3] = U − V) acts on Sym^kV by (−1)^k; on component r it acts by
  (−1)^{r+1}, which is exactly the parity of the symmetric power that component carries.

Arithmetic form: for an elliptic curve E/Q with ρ̄_{E,3} onto G (checked on y² = x³ − 3x + 1, Codex's j = 2304 curve,
at all 428 primes 5 ≤ p < 3000 [L2, L5]), put t(p) = tr V(ρ̄_{E,3}(Frob_p)). Then s(p) = χ₋₃(p), U(p) − 2 = t² − χ₋₃(p)
= tr Sym², V(p) = t³ − 2χ₋₃(p)t = tr Sym³, and c(p) = #{cube roots of Δ_E in F_p} − 1 (the dihedral S₃ layer
Q(ζ₃, Δ^{1/3}); Δ = 6⁴ here, so Q(ω, ∛6); computed for this E, in general [rec]). V∘ρ̄_{E,3} is odd (det = χ₋₃) with projective image S₄, so it is the Galois
representation of a weight-one octahedral newform [std: Langlands–Tunnell]. **So at Frob_p the five shadow components
read det (GL₁: a Dirichlet character, Alpöge), Sym² (GL₃: Gelbart–Jacquet), Sym³ (GL₄: Kim–Shahidi), Sym⁴ (GL₅: Kim) of
the weight-one form of the Langlands–Tunnell step, and the cubic-Kummer character of Q(ω) (the order-3 phase rung).**
The ladder sign → phase → octahedral of the user's programme is the quotient tower G → S₄ → S₃ → C₂ of the lambency-6
umbral group, and the five shadow components sort it by symmetric power.

**C2. Alpöge's #μ_Q = 2 sign is the χ₋₄ bit, and the sign-times-phase defect is the Frobenius of the lambency-6
Coxeter Mason form.** [L2] The normalized quadratic Gauss sums ε_c = g(c)/√c satisfy ε_c² = χ₋₄(c) and
ε_{cc′} = ε_c ε_{c′}(−1)^{x x′}, x = (1 − χ₋₄(c))/2 ∈ F₂ (1029 coprime pairs), and for k factors the defect is
(−1)^{e₂(x)} = (−1)^{C(|x|,2)} (553 products): a complete-graph quadratic form over F₂ on the χ₋₄-bits, which is how I
read the "complete graph" of the remark's footnote 3 in the case #μ_Q = 2 (the remark does not spell it out). The lambency-6 theta Gauss sum Σ_{r mod 12} e(r²/24) = √12 e(1/8) is (2e(3/8)) × (−i√3), its 2-part times
its 3-part. And for p ≡ 1 mod 6 (37 primes < 400): g(χ₂)g(χ₃) = J(χ₂, χ₃) g(χ₂χ₃) with a_p(y² = x³ + 1) = −2 Re J(χ₂, χ₃):
the defect between the order-2 (sign) and order-3 (phase) Gauss sums is the Frobenius of 36a1 = η(6τ)⁴, the Mason form
of the A₅ Coxeter element ρ(289) on N(A₅⁴D₄) (atlas C9, B3).

**C3. PG(2,3) with its polarity is P(sl₂(F₃)) with the Killing form, and the (2,3,6) triangle group maps onto its
symmetry.** [L6] The absolute points of the Singer polarity x ↦ −x of {0,1,3,9} mod 13 are {0,7,8,11}, no three collinear
(a conic; for q = 2, 4 the absolute points form a line). On P(sl₂(F₃)) the adjoint action of G has kernel the centre and
image of order 24 = |PGO₃(3)|, preserves the conic det = 0, and the kernel map (nilpotent X ↦ ker X) is a G-equivariant
bijection from the conic onto P¹(F₃): **the conic of the polarity is the set of four tetracode coordinates, i.e. the four
A₅ summands of N(A₅⁴D₄), and the polarity's centralizer is G/{±1} = S₄, permuting the conic with permutation character
a = 1 + Sym²V, exactly as it permutes the four A₅.** (Every polarity of PG(2,3) is orthogonal and conjugate to this one,
since 3 is not a square [std]; the Singer polarity is one of them.) Separately, Z[ω] → Z/(q² + q + 1), ω ↦ q, maps
Δ(2,3,6) = Z[ω] ⋊ μ₆ [std: the orientation-preserving symmetry group of the hexagonal tiling] onto
the full group of affine maps x ↦ ux + t preserving the Singer plane PG(2,q) for q = 2 (order 42) and q = 3 (order 78):
ω goes to the Frobenius multiplier, −1 to the polarity; at q = 4 the image has index 2 (the semilinear multiplier 2).

**C4. P205's six points are the Weierstrass points of the Bolza curve, whose automorphism group is the lambency-6
umbral group.** [L3] The six ramification points {0, ∞, ±1, ±i} of P205's base cover t = (z + 1/z)²/4 are the octahedron's
vertices; the curve w² = z⁵ − z branched there has |Aut| = 48 with 13 involutions and 12 elements of order 8, i.e.
Aut ≅ GL₂(F₃) (binary octahedral: 1 involution; S₄ × C₂: 19). P205's deck involutions z ↦ −z, −1/z, 1/z each lift to two
elements of order 4 squaring to the hyperelliptic involution: the preimage of the deck group D = V₄ is Q₈, and the sign
(hyperelliptic involution) is the common square.

**C5. The two Niemeier lattices of Coxeter number 6 carry the two couplings of 2 and 3.** [L1] From the glue codes:
G^X(A₅⁴D₄) = GL₂(F₃) (centre μ₂ = the diagram flip of all four A₅, acting as −1 on the tetracode; S₃ quotient in which the
sign inverts the order-3 part), G^X(E₆⁴) = GL₂(F₃), and G^X(D₄⁶) = 3.S₆ of order 2160 whose normal μ₃ (simultaneous
triality = scalar ω on the hexacode) is central in 3.A₆ and **inverted** by every odd element; the centre of 3.S₆ is
trivial. So at lambency 6 the sign is central and at 6+3 the sign inverts the phase (μ₃ ⋊ μ₂ = S₃, "reflected"), while
the complex Leech lattice's 6.Suz has central μ₆ = μ₂ × μ₃ ("commuting") [rec].

**What fails** (each with the failing step, §§1–5): the Sp₄(F₂) = S₆ explanation of P205's level-2 match (P205's
monodromy preserves no symplectic form, over Q or F₂; its 2-torsion module is not Jac(Bolza)[2]); the reading of Codex's
isogeny exponents 1, 2, 3 as elliptic or cusp orders (all three local monodromies have eigenvalues ±1 only; the exponents
are Kummer degrees of ε); the alignment of 02L5's 11 and 13 with the ternary Golay code and PG(2,3) beyond ℓ₀ = 1 (and the
PG(2,3) line code is [13,7,4], not the ternary quadratic-residue code [13,7,5]); "centre μ₃ of 3.S₆" (C5); "Codex's three
quadratic signs at j = 2304 are χ₋₄, χ₋₃, χ₁₂" (the halving field is A₄, which has no quotient of order 2); and
SL₂(Z/4) ≅ GL₂(F₃) (only the projective groups agree).

---

## 1. Lead 1: Alpöge's sign field in each place

### 1.1 What the remark names
The phrase "sign field" does not occur in the remark (four pages, read in full), nor as a declaration of the Lean
archive (`declarations.tsv` searched as one file). It is the user's name (21 Nov) for the sign mechanism of Alpöge's
proof. What the remark itself names as the sign, with locators:
- p. 2: the "qN = M^k + R sign-only proof of Weil and Deligne"; p. 3: the definite sign of the left-hand side of
  qN = M^k + R, read as automorphy over a function field;
- fn. 3: N is the weighted point count of the path quadric x₁x₂ + ⋯ + x_{k−1}x_k over F_q (summing e_q(h·Q(x)) over h
  first); Bertini/Lefschetz give its middle cohomology a definite sign, opposite to the sign of the zero-mode M^k, while
  R has square-root size; opposite signs leave no room for cancellation of inverse roots (this is our H01);
- fn. 3 continued: the quadric comes from averaging χ ↦ χ(disc) through a ↦ y(·)^a, y the normalized Gauss sum of order
  #μ_K living through θ on the #μ_K-fold cover of GL₂; the reciprocity law of y(cc′) against y(c)y(c′) gives a complete
  graph, simplified to the path quadric;
- step 3: a theta on the sixfold cover (of GL₅, as printed) and C/Z[ω]; step 5: "Guinand–Weil had the sign"; p. 2: the
  (2,3,6) triangle group.
So, exactly: **for K = Q the sign is μ_Q = {±1}, carried by the normalized quadratic Gauss sum on the double cover and by
its reciprocity cocycle; for K = Q(ω) the same construction has #μ_K = 6 = 2 × 3** (the sixfold cover of step 3). This is
what I tested in each place. Proved [L2]: the cocycle is (−1)^{x x′} on the bits x = (1 − χ₋₄(c))/2, and ε_c² = χ₋₄(c);
k-fold products give (−1)^{e₂(x)}, which depends only on |x| mod 4 (values 0,0,1,1,0,0,1,1).

### 1.2 Place by place: which sign, and what it does to 2 × 3

| Place | The sign there (exactly) | Same sign as Alpöge's μ_Q? | What it does to 2 × 3 (or 1 × 2 × 3) | Check |
|---|---|---|---|---|
| Lambency-6 shadow: χ₋₄, χ₋₃ pieces, χ₁₂ | (i) the kernel μ₂ of the metaplectic double cover, on which η and the shadow are genuine (half-integral weight); (ii) W₆ = −1 ∈ (Z/12)^× (r ↦ −r), the element over −I ∈ SL₂(Z) | (i) is Alpöge's μ_Q: its cocycle (−1)^{x x′} (the 2-adic Hilbert symbol of odd c, c′ [std]) lives on the χ₋₄-bits, ε_c² = χ₋₄(c). (ii) is a different element; on the (odd) shadow both act as −1, on η (even) they differ | (Z/12)^× = {±1}₂ × {±1}₃ has characters χ₋₄ (sign at 2), χ₋₃ (sign at 3), χ₁₂ = χ₋₄χ₋₃; W₆ splits them 2 + 1: χ₋₄, χ₋₃ odd (the weight-3/2 shadow), χ₁₂ even (η, weight 1/2). W₃ (the "+3") = χ(5): +1 on χ₋₄, −1 on χ₋₃, so 6+3 keeps the χ₋₄ piece; W₂ = χ(7) would keep χ₋₃. The 12 = 2² × 3 of the theta Gauss sum factors 2-part × 3-part | atlas X1, [L2](a)(b) |
| Codex's 3-torsion twist | −I ∈ GL₂(F₃) = centre of the umbral group = diagram flip of the four A₅ (−1 on the tetracode, trivial on the binary glue) | No: the umbral sign (iii) below, commuting with (i) and (ii); it is the Galois-side sign (quadratic twist) | Acts on Sym^kV by (−1)^k, on component r by (−1)^{r+1}: U = 2 + Sym²V is even, V = Sym³V is odd, hence #E[3] = U + V, #E^d[3] = U − V, and #E[3](F_{p²}) = U² − V² (power map (U+V)(g²) = (U+V)(g)(U−V)(g), all 48 g) | [L1], [L5] |
| Central character, Sym²/Sym³, GL₂ × GL₃ → GL₆ | det V = sgn (umbral); at Frob_p det = χ₋₃(p); at the CM point η(6τ)⁴ the GL₁ part of Sym² is χ₋₃|·| | Its value at Frob_p is a Dirichlet character (covered by Alpöge); as a character of G it is the determinant of the representation on which the umbral sign (iii) acts | V ⊗ Sym²V = Sym³V ⊕ V⊗det = 4 ⊕ 2̄; det ⊗ V ⊗ Sym²V = 4 ⊕ 2; at the CM point: Sym²η(6τ)⁴ = η(2τ)³η(6τ)³ ⊕ χ₋₃|·| and f × Sym²f = η(3τ)⁸ ⊕ f(1) ⊕ f(1), 6 = 2 + 2 + 2 | [L4], [L5] |
| Polarity of PG(2,3) | −1 ∈ μ₆ in (Z[ω]/(3 − ω)) ⋊ μ₆, the image of the half-turns of Δ(2,3,6) | Same abstract μ₂ ⊂ μ₆ = Z[ω]^× as Alpöge's step 3; under the identification PG(2,3) = P(sl₂(F₃)) it is the Killing form | Extends the Singer normalizer C₁₃ ⋊ μ₃ (39) to C₁₃ ⋊ μ₆ (78): the sign doubles 3 to 6; its absolute conic = P¹(F₃) = the 4 A₅ summands, centralizer S₄ = G/{±1} | [L6] |
| Deck involutions of P205 | D = V₄ = Γ(2)/±Γ(4) on the z-line X(4); three double fibres | Lifted to Aut(Bolza) = G, the three involutions square to the one sign (hyperelliptic involution): Q₈ | In P205's own mod-4 monodromy the three squares are two different elements (K₁ ≠ K₂ = K₃): C₄ ⋊ C₄, not Q₈. The sign that would make the three fibres equal at level 4 is absent there: this is the level-4 break | [L3] |
| Co₀ and 6.Suz | μ₂ = {±1} = centre of Co₀ = the scalar −1 of the Z[ω]-structure, inside the central μ₆ of 6.Suz [rec] | Same μ₂ ⊂ μ₆ = Z[ω]^× as in step 3 | Commuting coupling μ₂ × μ₃; contrast 3.S₆ at 6+3 (sign inverts μ₃) and G (central μ₂, inverting inside S₃) | [L1] for 3.S₆, G |
| Codex's three signs at j = 2304 | the sign changes (r₁, r₂, r₃) with r₁r₂r₃ = −1 = translations of the four halves of P by E[2] | No: the halving field has group A₄ = V₄ ⋊ C₃, which has no quotient of order 2, so none of χ₋₄, χ₋₃, χ₁₂ occurs; the three signs are quadratic characters of the cyclic cubic field Q(ζ₉)⁺ (x³ − 3x + 1 has roots 2cos(2πk/9)), permuted cyclically by the order-3 phase | 2 × 2 ⋊ 3 = A₄ = PSL₂(F₃): signs permuted by a phase | Codex (A₄), trig identity |

**Answer to "is it one sign?"** No: at lambency 6 there are three commuting involutive structures, and the computation
keeps them apart. (i) Alpöge's μ_Q, the kernel of the metaplectic double cover, whose reciprocity cocycle lives on the
χ₋₄-bits; (ii) the inversion W₆, under which the shadow is odd and η even; together they organize the Dirichlet characters
χ₋₄, χ₋₃, χ₁₂, all covered by Alpöge's theorem. (iii) The umbral centre −I ∈ G (the quadratic twist), which grades the
shadow components by the parity of Sym^{r+1}. **The bridge from (iii) to the Dirichlet side is det V: a character of the
umbral group whose value at Frob_p is the Dirichlet character χ₋₃(p), and which weights the W₃ cross term.** This is where
the "1" of 1 × 2 × 3 carries the sign: with the "1" trivial, 2 × 3 = 4 + 2̄; with the "1" = det, 1 × 2 × 3 = 4 + 2.

### 1.3 Consequences derived and tested
- From C1: the χ₋₄-isotypic part of the twined shadow at g is (a + 1 + s)(S_{6,1} + S_{6,5}) and the χ₋₃-part
  (a + 1 − s)(S_{6,1} − S_{6,5}); at Frob_p these coefficients are 2 + tr Sym² ± χ₋₃(p). Tested at 428 primes: holds.
- Chebotarev frequencies of (a, b, c, s) over 428 primes match the class sizes 12, 12, 16, 6, 2 of G (113, 108, 143,
  51, 13 primes) [L2].
- No contradiction found. The test that could have failed: the umbral sign could have coincided with W₆ on the shadow
  (acting by −1 on every component); it acts by (−1)^{r+1}, so the two are distinct.

---

## 2. Lead 2: 2 × 3 = 6, Rankin–Selberg and Kim–Shahidi at lambency 6

**Relation.** Degree-6 L-functions attached to lambency 6 that factor through GL(2) × GL(3), and their GRH content.

1. **Finite-group level (new here, holds).** By C1, V ⊗ Sym²V = Sym³V ⊕ V ⊗ det inside the twined shadow of N(A₅⁴D₄).
   For E with ρ̄_{E,3} onto G and f the weight-one octahedral form of V∘ρ̄: L(s, f × Sym²f) = L(s, Sym³f)·L(s, f ⊗ χ₋₃)
   = L(s, Sym³f)·L(s, f̄), an Artin L-function of degree 6 = 4 + 2 whose Euler factors at p are read off the shadow
   components r = 2 (Sym³) and r = 1 (Sym², with det = χ₋₃ in the cross term). GRH for it is a case of Artin's GRH for
   the GL₂(F₃) field Q(E[3]): beyond Alpöge's theorem except the factor det = χ₋₃. GRH for all Artin L-functions of that
   field (equivalently for its Dedekind zeta) would give a least prime with prescribed shadow class (U, V) of size
   O((log d)²) in the field discriminant d (the Lagarias–Odlyzko–Bach form [rec]).
2. **CM point (holds, 194 primes 5 ≤ p ≤ 1200) [L4].** f = η(6τ)⁴ (36a1; the Mason form of the A₅ Coxeter element,
   Frame shape 6⁴):
   Sym²f = η(2τ)³η(6τ)³ ⊕ χ₋₃|·|; Sym³f = η(3τ)⁸ ⊕ f(1) (atlas B4); so f × Sym²f = η(3τ)⁸ ⊕ f(1) ⊕ f(1): **6 = 2 + 2 + 2,
   three GL₁'s over Q(ω)**. GRH for L(f × Sym²f) ⟺ GRH for L(ψ³) and L(ψ) over Q(ω) (atlas H1): nothing beyond the first
   rung past Alpöge. The GL₁/Q piece χ₋₃ sits inside Sym² (covered). η(2τ)³η(6τ)³ is the Mason form of a Weyl-group element
   of A₅⁴D₄ (Coxeter, Coxeter, Coxeter, (2,2,2)) [L4b]; so are 6⁴, 3⁸, 2¹² (ρ(289) lies in the Weyl kernel, as Codex noted).
3. **The two elliptic points together (holds).** With f_i = η(4τ)²η(8τ)² (CM by Q(i), the j = 1728 point): Sym²f_i =
   η(4τ)⁶ ⊕ χ₋₄|·|, and f_ω × Sym²f_i = [degree 4, supported on p ≡ 1 mod 12: a Hecke character of Q(ζ₁₂) = Q(i, ω)] ⊕
   f_ω ⊗ χ₋₄(1); symmetrically f_i × Sym²f_ω = [degree 4 over Q(ζ₁₂)] ⊕ f_i ⊗ χ₋₃(1). **The central-character twist at each
   CM point is the other point's sign, and the degree-4 part lives over the field whose characters are the lambency-6
   characters.**
4. **The first cuspidal case (open).** h = η(τ)²η(2τ)²η(3τ)²η(6τ)², the newform of S₄(Γ₀(6)) (Mason form of the M₂₄
   class 1²2²3²6²; also a Weyl Frame shape of A₅⁴D₄ [L4b]) has no CM (a_p ≠ 0 in all four classes of p mod 3 and mod 4),
   W₂ = W₃ = +1, root number +1 [L4]. L(h × Sym²h) = L(Sym³h)·L(h, s − 3) is degree 6 with Sym²h cuspidal on GL₃ and
   Sym³h cuspidal on GL₄ [std: Gelbart–Jacquet, Kim–Shahidi, for non-CM h]. GRH for it is open and covered by no rung we
   have; it is the natural "2 × 3" object of Γ₀(6) itself.

**Contradiction search.** If the degree-6 product at the CM point had a cuspidal GL₃ factor, Sym²f would have no GL₁
summand; it has one (χ₋₃), so the CM point is degenerate in exactly the way that keeps it inside the H1 rung. No
contradiction.

---

## 3. Lead 3: layer 4 (GSp₄, Z[i], PG(2,4), Sp₄(F₂) = S₆)

**Verified.** G^X(D₄⁶) = 3.S₆ (C5) against CDH's table [rec: Cheng–Duncan–Harvey, arXiv 1307.5793, Table "umbral
groups"]: the computation from the hexacode is the check, and it corrects "centre μ₃". G^X(E₆⁴) = GL₂(F₃) (lambency
12+4), with the tetracode as the whole glue [L1].

**Relations tested.**
1. **"P205's level-2 symmetry is the S₆ = Sp₄(F₂) of a genus-2 Jacobian" — fails.** Codex's integral monodromy
   A₁, A₂, A₃ (A₁A₂A₃ = I) preserves no nonzero alternating form over Q, and none of the eight D-invariant alternating forms
   over F₂ is nondegenerate [L3]. A transvection-like element I + e₄φ (φ(e₄) = 0) preserves a symplectic form ω only if
   φ = ω(e₄, ·); the three T_i have three different φ, so at most one can be symplectic. The invariant symmetric forms are
   spanned by x₁² and α², α = (1,1,1,2): degenerate. So P205's 2-torsion lives in GL₄(F₂) ≅ A₈ (with Codex's Fano plane
   P(W) inside), not in Sp₄(F₂). Its F₂[D]-module is not Jac(Bolza)[2] either: fixed-space dimensions 3, 3, 3 against
   2, 2, 2 [L3]. The six-point match (Codex, and the relayed test) holds as a match of permutation actions on six-element
   sets only.
2. **Bolza (holds, C4).** The genus-2 curve on P205's six points has Aut = GL₂(F₃) = the lambency-6 group. Its Jacobian
   [L3b, all 45 odd primes < 200]: with p = a² + 2b² when p ≡ 1, 3 mod 8, the L-polynomial is (1 ∓ 2aT + pT²)² for
   p ≡ 1 mod 8, 1 + 2(a² − 2b²)T² + p²T⁴ for p ≡ 3 mod 8, (1 − pT²)² for p ≡ 5 and (1 + pT²)² for p ≡ 7 mod 8: the
   Frobenius eigenvalues are ±π (each twice) at p ≡ 1 mod 8 and ±iπ, ±iπ̄ at p ≡ 3 mod 8, π = a + b√−2. **The GSp₄ (spin)
   L-function of the lambency-6 genus-2 curve is a μ₄-twisted Hecke L-function of Q(√−2)**: the paramodular rung collapses
   to GL₁ over an imaginary quadratic field, and the layer-4 phase i appears exactly at the primes p ≡ 3 mod 8. (Q(√−2) is
   the character field of V: values ±i√2.) Status: the pattern is checked at 45 primes; over Q the L-polynomial at
   p = 3 is 1 − 2T² + 9T⁴, irreducible over Z, so the Jacobian is not isogenous over Q to a product of elliptic curves
   over Q (it splits over Q(√2)); the proof of the pattern from the automorphism (z, w) ↦ (iz, ζ₈w) is to write.
3. **Level 4 = X(4) (holds).** P205's z-line is X(4) over the λ-line X(2) (Codex); D = Γ(2)/±Γ(4); S₄ = PSL₂(Z/4) ≅ PGL₂(F₃)
   = G/{±1}. But SL₂(Z/4) has 7 involutions and a normal (Z/2)³, G has 13 and a normal Q₈ [L3]: **layer 4 and lambency 6
   share the projective group and differ in the sign extension.** P205's mod-4 monodromy is C₄ ⋊ C₄ (order 16, squares
   with multiplicities 4, 4, 8), neither Q₈ × C₂ nor abelian [L3b].
4. **Is Z[i] where the S6 example lives?** Consistent in three senses: the base cover is level 4; the sections over ∞
   tend to the Z[i] curve (j = 1728) and the images to j(2i) (Codex); the first level at which the symmetry breaks is 4.
   Fails in one: μ₄ = Z[i]^× acts on X(4) by z ↦ iz, which induces t ↦ 1 − t (swapping the fibres over 0 and 1), and this
   does not lift to P205 (Codex's level-4 graph ∞ ↦ 0 ↦ 1 ↦ 1 has only the identity automorphism). So the example lives
   over level 4 and has a Z[i] limit, but not Z[i]-symmetry.
5. Not computed in this pass: the quartic theta over Q(i) (Eckhardt–Patterson) and the hexacode → Golay → Leech chain
   beyond the 3.S₆ check; the double-six S₆ in W(E₆).

---

## 4. Lead 4: Codex's isogeny exponents 1, 2, 3

**Relation tested.** The exponents in "the pairs (∞,1), (∞,0), (0,1) are isogenous exactly when ε, ε², ε³ is rational"
are the same 1 × 2 × 3 as elliptic/cusp orders or the Hesse pencil.

**What they are (holds) [L7].** With ρ_∞ = 2i, ρ₀ = iε²/2, ρ₁ = iε and the criterion (iu ∼ iv ⟺ u/v or uv rational; proof:
a rational matrix with iv(c·iu + d) = a·iu + b forces b = −c·uv and dv = au), the three images carry ε-weights 0, 2, 1
and the pair conditions are ε^{|e_a−e_b|} or ε^{e_a+e_b} rational. Let d = the least k ≥ 1 with ε^k ∈ Q (d = ∞ if none).
Then: d = 1 → all three pairs; d = 2 → only (∞,0); d = 3 → only (0,1); d ≥ 4 or ∞ → none (tested for ε = 1/7, √2/7,
∛2/7, 2^{1/4}/7, 2^{1/6}/7, √3/7, π/7, 2^{1/5}/7). So **the exponents are Kummer degrees**: for ε⁶ = r ∈ Q, (0,1) is decided
by the square class of r (the sign part of Q^×/Q^{×6} = Q^×/Q^{×2} × Q^×/Q^{×3}), (∞,0) by its cube class (the phase
part), (∞,1) by both. Transitivity of isogeny is the Bézout identity ε = ε³/ε² (1 = 3 − 2): consistent. CM: iu is CM iff
u² ∈ Q; d = 2 makes all three images CM, fibre 1 by Q(√−r) (Q(√−2) for ε = √2/n, the octahedral field of V; Q(√−3) for
ε = √3/n); d = 3 gives an isogenous non-CM pair.

**The elliptic-order reading fails.** All three local monodromies have characteristic polynomial (x − 1)²(x + 1)² with
A_i² unipotent and nontrivial [L3]: three double fibres, a (2,2,2) base orbifold. An order-3 elliptic point would need an
eigenvalue of order 3 or 6. Codex also proved that the integral monodromy is the same for every ε, so no topological
datum can carry the exponents; they come from the deformation weights (0, 2, 1) on e₁, e₂, e₃. (Whether P205 forces those
weights needs P205 itself, not read here.)

---

## 5. Lead 5: the PG(2,q) chain and the orders 11 and 13

**02L5's numbers (from the intake note).** Right gluing X(σ_n): peripheral integer 12n − 1 = 12ℓ₀ − 4ℓ₁ − 3ℓ₂ with
(ℓ₁, ℓ₂) = (1, −1), the atlas's row 22 formula (the (3,4,∞) orbifold of the S6 base; 12 = 3·4 = |Δ(3,4,∞)^ab| =
|SL₂(Z)^ab|); wrong gluing: −12n − 1. At n = 1: |λ| = 11 and 13.

**Holds [L6].** λ ≡ −1 mod 12 for both gluings and every n (the class of W₆ in (Z/12)^×); the gluing direction (the sign
T_σ ↦ T_{−σ}) changes |λ| from 12n − 1 to 12n + 1, i.e. the residue of |λ| from −1 to +1 mod 12: it fixes χ₁₂ (even) and
flips χ₋₄ and χ₋₃ (odd). Both 11 and 13 have χ₁₂ = 1, i.e. 3 is a square mod both, which is the condition for ternary
quadratic-residue codes of that length.

**Fails.** (i) The ternary Golay code is the QR code of length 11, but the PG(2,3) line code over F₃ is the cyclic
[13,7,4] code with zero set {1,3,9} ∪ {7,8,11} (one residue and one non-residue coset), not a QR code (both ternary QR
codes of length 13 are [13,7,5]) [L6]: the pair (11, 13) is not "two QR codes". What does pair them: 13 is also the
length of the ternary Hamming code, whose check columns are the 13 points of PG(2,3) (perfect: 3¹⁰ · (1 + 2·13) = 3¹³),
so at n = 1 the two orders are the lengths of the two perfect ternary codes below 40 (Golay 11, Hamming 13). (ii) The
sequences do not stay aligned: 12n + 1 is a plane size q² + q + 1 only at n = 1 (13), 6 (73), 11 (133), and a ternary
Hamming length (3^m − 1)/2 only for odd m (n = 0, 1, 10, 91, …); 12n − 1 is a perfect-code length only at n = 1 (ternary
Golay) and n = 2 (23, binary Golay), since binary Hamming lengths 2^m − 1 are never ≡ −1 mod 12 and ternary Hamming
lengths are ≡ 1 [std: the perfect codes are the Hamming and Golay codes, Tietäväinen–van Lint]. So 11, 13 next to 12 is
arithmetic (χ₁₂ = 1, residue −1 mod 12) together with a coincidence at n = 1, not a plane or code structure inside 02L5.

**The chain q = 2, 3, 4 (holds, C3).** Δ(2,3,6) maps onto the Singer normalizer with polarity for q = 2 and 3, and with
index 2 for q = 4. The orders 7, 13, 21 are N(q − ω) = q² + q + 1. q = 3 is the case where the polarity's conic is
P¹(F₃) with the lambency-6 group acting through Sym²V.

---

## 6. What to do next
1. Test C1 on the mock forms, not only the shadows: decompose CDH's twined H^X_{g,r} coefficients at lambency 6 into Sym^kV
   characters and check nonnegativity and the r ↔ Sym^{r+1} pattern beyond the shadow (needs CDH's twining tables).
2. Run C1 at the other lambencies whose umbral group lies in GL₂(C) (E₆⁴ at 12+4: same G; lambency 7, SL₂(F₃);
   lambency 5, GL₂(F₅)/2 has no faithful 2-dim complex representation, a test of where the pattern must stop).
3. Write the proof of the Bolza spin-L-function pattern (±π, ±iπ) from the automorphism of order 8; it is the cleanest
   layer-4 test case of an order-4 phase twist.
4. Read Paper II's Example P205 for the origin of the weights (0, 2, 1) of the deformation frame.
5. Read Paper III D.2.3 for what the groups Z/|12ℓ₀ − 1| are (H₁-torsion? with a linking form whose character is χ₁₂?).
6. Effective Chebotarev for the GL₂(F₃) field of E[3] under Artin GRH (least prime with given shadow class), against what
   Alpöge's theorem gives (the det part only).

## 7. Check events

| Statement | Date | Who | Type | Outcome |
|---|---|---|---|---|
| C1 character identities (s, a−1, b, a+c, Clebsch–Gordan, centre parity) on all 48 elements | 2026-11-23 | Claude Opus 5.5 at effort max, this pass | computation (exhaustive) | holds |
| C1 arithmetic form on y² = x³ − 3x + 1, 428 primes | 2026-11-23 | same | computation | holds |
| C2 Gauss-sum cocycle, lambency-6 Gauss sum, Jacobi-sum / 36a1 | 2026-11-23 | same | computation | holds |
| C3 PG(2,3) = P(sl₂(F₃)), conic = P¹(F₃), (2,3,6) image for q = 2, 3, 4 | 2026-11-23 | same | computation | holds (index 2 at q = 4) |
| C4 Aut(Bolza) = GL₂(F₃), lifts of D = Q₈ | 2026-11-23 | same | computation | holds |
| C5 G^X(A₅⁴D₄) = G^X(E₆⁴) = GL₂(F₃), G^X(D₄⁶) = 3.S₆ with non-central μ₃ | 2026-11-23 | same | computation | holds; "centre μ₃" refuted |
| Codex's 3-torsion twist, shadow class functions (Codex's statement) | 2026-11-23 | same | used and rechecked in this run | holds |
| P205 monodromy symplectic / Sp₄(F₂) mechanism | 2026-11-23 | same | computation | refuted |
| Codex's isogeny table (Codex's statement) | 2026-11-23 | same | independent re-proof of the criterion + computation | holds; elliptic-order reading refuted |
| 02L5 orders vs Golay / PG(2,3) | 2026-11-23 | same | computation | alignment refuted beyond ℓ₀ = 1 |
| Sym² η(6τ)⁴ = η(2τ)³η(6τ)³ ⊕ χ₋₃|·|; cross products over Q(ζ₁₂) | 2026-11-23 | same | computation (194 primes) | holds |
| Bolza spin-L pattern ±π, ±iπ | 2026-11-24 | same | computation (45 odd primes < 200) | holds numerically; proof to write |

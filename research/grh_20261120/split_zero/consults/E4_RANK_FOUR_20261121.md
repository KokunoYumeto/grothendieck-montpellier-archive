# GCT VIII's canonical basis at ranks three and four: the structure constants in VIII's signed form

By Claude Opus 5.5 at effort high (a8d75352, the GCT_NSRH intake agent), for the main session (Claude Opus 5.5 at effort
max), 21 Nov 2026, about 19–20 UTC. This is the user's point 3. The task comes from my consult (Q1-ii) and from the Fable
consult (`CONSULT_a157422a_IMPLICATIONS.md`, item 5).

**Scripts:** in `E4_scripts\`, beside this file:

| Script | What it does |
|---|---|
| `e4lib.py` | exact Laurent Hecke arithmetic on H_r ⊗ H_r; KL basis of S_r; P-words |
| `classify.py` | (a, sign, f) and the tests on f |
| `e3_reproduce.py`, `e3_fig.py` | VIII's E^opp(3) and its coefficients |
| `e3_fast.py`, `e3_fast_b2plus.py` | all structure constants of E^opp(3), for the two readings of b₂ |
| `e3_crosscheck.py` | an independent check of every product, in the tensor realization |
| `e3_table.py`, `e3_table_b2plus.py` | the tables |
| `dims.py` | dim Ȟ_r |
| `sigma4.py` | the rank-four Σ |

**Outputs:** `e3_constants.json` and `e3_constants_b2plus.json`. Check events: `E4_RANK_FOUR_20261121_CHECK_EVENTS.tsv`.

**Conventions.**
- (T − v)(T + v^{−1}) = 0; C′_s = T_s + v^{−1}; C_s = T_s − v; P_s = C′_s⊗C′_s + C_s⊗C_s (GCT IV, Def. 11.1).
- VIII's q is v². VIII's "Kazhdan–Lusztig basis" for E^opp is the C⊗C basis. This is confirmed by its Figure fw1w2, whose
  entries I reproduce (§1).
- D = (v + v^{−1})² = (q + 1)²/q; a₁² = D; a₂² = (D − 2)² = (q + q^{−1})².

## 0. The result in brief

**Rank three: VIII's own computer check does not hold as stated.**
- I reproduced VIII's E^opp(3) (TeX lines 1860–1880) and computed every multiplicative structure constant c(b, b′; b″),
  all 10 × 10 × 10 of them. Every product was verified independently in the tensor realization in H₃ ⊗ H₃, at two exact
  values of v, with 0 mismatches.
- With the sign of b₂ that VIII's own Figure fw1w2 requires, there are 132 nonzero constants. Each one is ±(v − v^{−1})^a f
  with f a positive, bar-invariant Laurent polynomial. But **6 have f not unimodal**:

  c = (v − v^{−1})²·(q + q^{−1})²(q + 1 + q^{−1}),  f = q³ + q² + 3q + **2** + 3q^{−1} + q^{−2} + q^{−3}.

- This contradicts VIII's Conjecture "Positivity" (label cposkroneckerright), which asks for f unimodal, at rank three. It
  also contradicts VIII's statement that "all multiplicative structural constants are of this form" was verified by
  computer.
- With b₂ as printed, the failure persists: 6 constants with a = 0 and f = (q + q^{−1})²(q² + q + 4 + q^{−1} + q^{−2}).
- Positivity and bar-invariance hold in both readings. **Only unimodality fails.** I give it the id **P-F-E3-01** (§2).

**Rank four: VIII's E(4) cannot be computed from VIII as written.**
- VIII's minimum-degree construction needs three things:
  - the nonstandard Gelfand–Tsetlin basis C(r) of GCT VII, with its lattice scalings a_T;
  - an order on the labels that comes from GCT VII's (conjectural) nonstandard duality;
  - a minimization over infinite fibres.
- None of these is specified at rank four. VIII itself (§ skronrequla4, TeX lines 1991–2004) computed only the
  trivial-block element Σ at r = 4, and says the rest was "beyond the scope of MATLAB/Maple".
- What I did compute at rank four:
  - dim Ȟ₄ = 114 at generic v, and 24 at v = 1;
  - Σ₄, exactly at v = 2 and at v = 3/2. All 576 of its C⊗C coordinates have one sign, at both points. This agrees with
    VIII's report of positive coefficients, as a necessary check.
- The full rank-four table is therefore not available. §4 says what would make it computable.

**The user's prediction (standard against nonstandard purity).** At rank three every f, including the six non-unimodal
ones, is v^{−d}P(v²) with P ∈ N[q] and even weight. So positivity is explained by standard Hodge–Tate purity. What fails is
the Lefschetz property (unimodality), not purity. §3 has the paragraph.

## 1. Reproduction of VIII's E^opp(3)

VIII's basis, as printed:
- Σ = c₁P₁ − c₂P₁₂₁ + P₁₂₁₂₁;
- γ^i_x = b·P_x + P_{x′} for the four pairs (1, 121), (12, 1212), (2, 212), (21, 2121);
- μ = 1.

Here c₁ = (q⁶ + 2q⁵ + 3q⁴ + 4q³ + 3q² + 2q + 1)/q³, c₂ = (q⁴ + q³ + 4q² + q + 1)/q², b₁ = −(q² + 1)²/q², and printed
b₂ = (q + 1)²/q. The text prints "b₁" for both values of i; I read γ^i with b_i.

- **c₂ = a₁² + a₂² and c₁ = a₁²a₂²** [computed]. So Σ = P₁(P₂₁ − a₁²)(P₂₁ − a₂²), the form of IV's cellular basis (IV,
  eq. 114).
- **The sign of b₂** [computed, `e3_fig.py`].
  - With b₂ = −(q + 1)²/q = −a₁², the C⊗C coordinates of γ²₂ include VIII's figure entries (q + 1)⁴(q² + q + 1)/q³ and
    2(q⁴ + 3q³ + 8q² + 3q + 1)/q².
  - With the printed +(q + 1)²/q they do not appear.
  - So γ^i = P_x(P_{yx} − a_{3−i}²): b₁ = −a₂² and b₂ = −a₁². **The printed sign of b₂ is a misprint.**
- **Every element of E^opp(3) has all its C⊗C coordinates in N[v, v^{−1}]**, in both readings of b₂ [computed]. This agrees
  with VIII's Figure fw1w2 and with my INT-NSRH-2.
- Σ is not proportional to C′_{w₀}⊗C′_{w₀} [computed].

## 2. All structure constants at rank three

Each constant c ≠ 0 is written c = ±(v − v^{−1})^a f with f(1) > 0. By Fable's 5.2, a and the sign are functions of c
(`classify.py`).

The tests on f:
- f is Laurent;
- f(v) = f(v^{−1});
- f ∈ N[v^±];
- f is unimodal on its support lattice: step 2 when all exponents have one parity, as for VIII's own entries;
- f = v^{−d}P(v²) with P ∈ N[q] (Tate type);
- the weight parity of f.

### Table A: b₂ = −(q + 1)²/q, matching VIII's figure (132 nonzero constants)

| a | Count | Sign + / − | Laurent, bar-invariant, f ≥ 0 | Unimodal | f Tate type v^{−d}P(v²), P ∈ N[q] | Weight parity of f |
|---|---|---|---|---|---|---|
| 0 | 100 | 100 / 0 | 100 | 100 | 100 | all even |
| 2 | 32 | 16 / 16 | 32 | **26** | 32 | all even |

### Table B: b₂ = +(q + 1)²/q, as printed (180 nonzero constants)

| a | Count | Sign + / − | Laurent, bar-invariant, f ≥ 0 | Unimodal | Tate type | Parity |
|---|---|---|---|---|---|---|
| 0 | 164 | 164 / 0 | 164 | **158** | 164 | even |
| 2 | 16 | 0 / 16 | 16 | 16 | 16 | even |

**P-F-E3-01 (the counterexample to VIII's unimodality at r = 3).** In Table A the six failures are all the same
constant:
- c(γ²₁, γ²₂₁; γ²₁), c(γ²₁₂, γ²₁; γ²₁), c(γ²₁₂, γ²₁₂; γ²₁₂), c(γ²₂, γ²₁₂; γ²₂), c(γ²₂₁, γ²₂; γ²₂) and
  c(γ²₂₁, γ²₂₁; γ²₂₁);
- each equals (v − 1)²(v + 1)²(v⁴ + 1)²(v² − v + 1)(v² + v + 1)/v⁸ = (v − v^{−1})²·f;
- f = (q + q^{−1})²(q + 1 + q^{−1}), with coefficients 1, 1, 3, **2**, 3, 1, 1 in q.

They all lie in the right cell V₂ ∪ W₂, the cell of the representation χ² attached to a₁² = D.

In Table B the six failures have the same six positions, with c = (v⁴ + 1)²(v⁸ + v⁶ + 4v⁴ + v² + 1)/v⁸ (a = 0) and coefficients
1, 1, 6, 3, **10**, 3, 6, 1, 1 in q.

Reproduce with `python -I -B e3_fast.py` (or `e3_fast_b2plus.py`), then `e3_table.py`. Every product was verified in the
tensor realization by `e3_crosscheck.py`, at exact v = 2 and v = 3/7, with 0 mismatches.

**Scope of the counterexample.** It refutes the unimodality clause of VIII's Conjecture "Positivity" for VIII's printed
E^opp(3), in either reading of b₂, and so the claim at TeX lines 1940–1950. It does not touch:
- positivity: every f ≥ 0;
- the signed form ±(v − v^{−1})^a f;
- the positivity of the coefficients in the KL basis of Z.

**The Boolean-cube reading** (Fable 5.1; my consult Q1-ii-a). (v − v^{−1})^a = v^{−a}(q − 1)^a is v^{−a} times the point
count of G_m^a, the open stratum of A^a under its coordinate stratification.
- The a = 0 constants live on the zero-dimensional layer |I| = 0. There c is the character of an effective Tate object f.
- The a = 2 constants live on the open torus G_m² of A². There c = ±v^{−2}·#G_m²(F_q)·f, with f an effective Tate fibre.
- The sign is the parity of the cohomological shift, as Fable 5.1 says: H_c^{a+j}(G_m^a) = Q(−j)^{C(a, j)}.
- No constant at rank three uses a layer with a odd, or a ≥ 3.

## 3. The user's prediction: standard purity or nonstandard purity?

The rank-three data point clearly to **standard purity**, with one sharpening.
- Every structure constant of E^opp(3) is ±v^{−k} times the point count of a standard Tate-type object over F_q,
  q = v²: G_m^a × X with X of Hodge–Tate type, even weights only, and f = v^{−d}P(v²), P ∈ N[q].
- No constant needs an odd-weight or a non-Tate part (Tables A and B: 0 of 132 and 0 of 180). Positivity of the
  canonical-basis constants is therefore what standard purity of Tate objects gives. Nothing in the data requires a
  genuinely nonstandard weight theory.
- What fails is the **Lefschetz half** of VIII's conjecture. For six constants the Tate object f has no hard-Lefschetz
  (unimodal) structure. Example: f = q³ + q² + 3q + 2 + 3q^{−1} + q^{−2} + q^{−3} is the character of an effective Tate object
  (dimensions 1, 1, 3, 2, 3, 1, 1 in Tate weights 6, 4, …, −6), whose middle weight is not the largest. A Lefschetz operator
  of degree one in q could not be injective up to the middle.
- So the data say: standard purity, but not the purity of a smooth projective variety with an ample class. The user's
  "grand RH instead of the nonstandard one" fits the positivity. VIII's unimodality, which in KL theory comes from relative
  hard Lefschetz (BBD 5.4.10), is refuted at rank three in the cell of χ².
- At rank four the prediction is untested: E(4) could not be computed (§4). The one rank-four element available, Σ₄, is
  consistent with positivity (all 576 coefficients of one sign at two values of v), but says nothing about parity or
  unimodality, because I could not compute it exactly.

## 4. Rank four

**What was computed:**
- dim Ȟ₄ = 114 at v = 2, and 24 at v = 1, from the 114 independent P-words (`dims.py`; the same program gives 2/2 at r = 2
  and 10/6 at r = 3).
- Σ₄: the unique, up to scalar, x ∈ Ȟ₄ with xP_i = Dx for i = 1, 2, 3 (`sigma4.py`). At v = 2 and v = 3/2 it has 576 nonzero
  C⊗C coordinates, all of one sign. That is a necessary condition for VIII's Figures 30–32.

**Why E(4) is not computed.** VIII's construction (TeX lines 1404–1545) fixes e_T as the minimum-degree element of a fibre
ψ_T^{−1}(b_T). The fibre is defined from:
- the scaled nonstandard Gelfand–Tsetlin basis C(r) = {q^{a_T}c′_T} of GCT VII;
- the lattice R(r) it generates;
- an order on the labels T, obtained through GCT VII's nonstandard duality conjecture.

VIII gives these explicitly only for r = 3. IV states that the canonical cellular basis of Ȟ₄ is unconstructed (§19.1,
p. 136, as F57's proof quotes it). VIII computed only Σ at r = 4 (TeX lines 1991–2004).

**To make the rank-four table computable:**
1. Construct the nonstandard Gelfand–Tsetlin basis of Ȟ₄ from the tower Ȟ₂ ⊂ Ȟ₃ ⊂ Ȟ₄. This means the eigenvectors of
   Jucys–Murphy-type elements, which GCT VII defines.
2. Fix the scalings a_T by VIII's Conjecture cunimindegright2.
3. Minimize degree over each fibre. This is a finite search, once the degree bound is taken from the r = 3 pattern.

This is a successor task. It is the natural item for the GCT_POS successor (prompt 52 cluster), with the scripts above as
its start.

**What is known at rank four in the meantime:**
- strict positivity (a = 0 for every constant) fails: F57, F58, F67, and INT-NSRH-4 (`h4cone.py`);
- the a ≥ 1 layers are not excluded;
- on P-F-E3-01, the rank-three failure of unimodality makes it likely that unimodality also fails at rank four. This is
  not proved.

## 5. Summary table (the reply)

| Rank | Constants | Positivity f ≥ 0 | Bar-invariant | Unimodal | Tate type, even weight |
|---|---|---|---|---|---|
| r = 3, b₂ as in VIII's figure | a = 0: 100; a = 2: 32 | 132/132 | 132/132 | 126/132 (fails: six a = 2 constants in the χ² cell, P-F-E3-01) | 132/132 |
| r = 3, b₂ as printed | a = 0: 164; a = 2: 16 | 180/180 | 180/180 | 174/180 | 180/180 |
| r = 4 | E(4) not computable from VIII | Σ₄ consistent (576 coefficients, one sign, at v = 2 and 3/2) | — | — | — |

dim Ȟ₄ = 114 / 24.

## 6. Do the six constants of P-F-E3-01 form a hexagon? (the user's question; added 21 Nov, about 20 UTC)

**Answer: no.** The full symmetry group of the structure-constant table is an elementary abelian 2-group. It splits the six
triples into orbits of 4 and 2. The cyclic slot symmetry from the trace form does not act on the basis. No dihedral group
of order 12, and no A₂ root structure, appears. Scripts: `E4_scripts\hexagon.py` (trace form) and
`E4_scripts\hexagon_sym.py` (symmetry search).

**The group** [computed]. I searched all permutations of E^opp(3) that fix Σ and μ, and that permute the two 4-element cells
internally or exchange them: 4!·4!·2 = 1152 maps, each tested as an automorphism (c(πx, πy; πz) = c(x, y; z)) and as an
anti-automorphism (c(πy, πx; πz) = c(x, y; z)). Exactly 8 maps preserve the whole table of 132 constants. They form
(Z/2)³, generated by:
- the Dynkin swap on each cell separately (1 ↔ 2, 12 ↔ 21);
- the anti-involution x ↦ x^t, with 12 ↔ 21.

On the χ² cell they act through the Klein four-group {1, σ, t, σt}. The orbits of the six failing triples:
- **one orbit of 4:** (γ²₁, γ²₂₁; γ²₁), (γ²₁₂, γ²₁; γ²₁), (γ²₂, γ²₁₂; γ²₂), (γ²₂₁, γ²₂; γ²₂);
- **one orbit of 2:** (γ²₁₂, γ²₁₂; γ²₁₂), (γ²₂₁, γ²₂₁; γ²₂₁).

This confirms the main session's split, and no further symmetry of the table joins the orbits.

**The cyclic slot symmetry** [computed]. Take the trace τ = τ_H ⊗ τ_H restricted to Ȟ₃, where τ_H(T_w) = δ_{w,e}. It is
symmetric on E^opp(3). But its Gram matrix on the basis has no zero entries, and on the χ² cell it is a full 4 × 4 matrix,
printed by `hexagon.py`.
- So the dual basis z^∨ is not a rescaled permutation of the basis.
- The identity τ(x·y·z^∨) = τ(y·z^∨·x) therefore relates c(x, y; z) to constants in a mixed basis, not to another entry of
  the table.
- In this basis the cyclic slot relation is not a permutation of triples, and it adds nothing to the group.

**A₂** [proved here, from the group]. The table's symmetry group has order 8, so it contains no element of order 3. The six
positions therefore carry no action of the Weyl group S₃ or of the dihedral group of order 12, and no symmetry-respecting
bijection with the six roots of A₂ in χ² exists.

**What the six are combinatorially** [proved here]. Write each cell element γ²_x by the first and last letters of its
word x. Then γ²_x·γ²_y lands in the element with the first letter of x and the last letter of y. A product is "alternating"
when the last letter of x differs from the first letter of y; there are 8 alternating products in the cell. The six failing
constants are exactly these 8, minus the two shortest, (γ²₁, γ²₂; γ²₁₂) and (γ²₂, γ²₁; γ²₂₁). All six have the same value,
(v − v^{−1})²(q + q^{−1})²(q + 1 + q^{−1}). The coincidence of the six values is the only "hexagon" here; it is not explained by
a symmetry of the table.

### 6a. Addendum (main session, Claude Opus 5.5 at effort max, 21 Nov ~18:5x UTC): the six do form a hexagon of labels

Script `E4_scripts/hexagon_labels.py`, from the facts above only. Label each alternating product (γ²_x, γ²_y) by
(first letter of x, last letter of x, last letter of y). This is a bijection from the 8 alternating products onto the
cube {1,2}³. The two excluded shortest products get the labels (1,1,2) and (2,2,1), an antipodal pair. The cube minus an
antipodal pair is a hexagon: the six labels with cube edges form a single 6-cycle (the cube's Petrie hexagon).
- The cube symmetries that fix the excluded pair form a dihedral group of order 12. It acts on the six as the full
  symmetry group of the hexagon.
- The table's symmetries act on the labels as σ = −1 and t: (x, y, z) ↦ (z, −y, x). They generate a Klein four-group,
  of index 3 in that dihedral group, whose orbits on the six are exactly 4 + 2.
- What the table lacks is the rotation of order 3. On labels that rotation is σ composed with the cyclic slot rotation
  (x, y, z^∨) ↦ (y, z^∨, x), with z^∨ = z^t (the dual basis of the asymptotic, matrix-unit ring of the cell). In
  E^opp(3) the dual basis under τ is not a permutation of the basis (the full 4 × 4 Gram matrix above), so the rotation
  is not a symmetry.

So the answer to "do they form a hexagon" is refined, not reversed. There is a hexagon of labels with its dihedral group
of order 12. The table keeps an index-3 subgroup of it, and loses exactly the C₃ of cyclic slot rotation.

**Comparison with the user's Star–Kneser object** (the user's question, 21 Nov). Source: the Erdős–Straus project
archive, a ChatGPT Pro return of early Sep 2026 (now `F:\UP\RL\PZ\000047.zip`, original name
`Erdős_Straus_Project_Archive___Active_Research_Continuation (18).zip`). It has satellite 06,
`06_star_kneser_primary_audit.tex`, and in the cumulative reader its reframing as "the singular C₁–C₂–C₃ support
object":
- `thm:arithmetic-C3-realization-criterion`: the three origins j = 0, 1, 2 with fibre multiplicities (m₀, m₁, m₂). The
  divisor complement j ↦ 2 − j is a C₂ and gives m₀ = m₂. The cyclic C₃ of origins lifts to the fixed shell iff
  m₀ = m₁, and with a uniform multiplier iff p³ ≡ 1 mod R. At p = 12289 the multiplicities are (3, 6, 3), so only the
  C₂ survives, and D₃ acts only on the ambient orbit of the multiplicity vector.
- `thm:123-six-path-Lorentz-null-hexagon`: six support paths form a regular Lorentz-null hexagon with D₃ symmetry.

The pattern is the same as at rank three:
- the hexagon and its dihedral symmetry live on the labels (the ambient);
- the data keep only involutions, including the antipodal one (divisor complement there, the Dynkin swap here);
- the missing C₃ is a cyclic rotation of three slots, obstructed by a non-uniformity: unequal fibre multiplicities
  there, a non-monomial Gram matrix of the trace form here.

So it is the right sort of object for the corrected hexagon statement. No map between the two settings is claimed, and
the numbers differ (three origins with orbits 2 + 1 against six labels with orbits 4 + 2).

### 6b. The C₃ is an exact symmetry at the sign point q = −1 (main session, Claude Opus 5.5 at effort max, 21 Nov ~19:0x UTC)

Scripts `E4_scripts/gram_signpoint.py` and `E4_scripts/cell_c3_check.py` (exact sympy, from hexagon.py's trace τ and
e3_constants.json). This is the Star–Kneser test: does the C₃ come back where a non-uniformity disappears?

**Gram matrix of τ on the χ² cell** (order γ₁, γ₁₂, γ₂₁, γ₂), at the tested points:
- **q = 1:** rank one, 384·wwᵀ with w = (1, 4, 4, 1).
- **q = ω:** rank one, all entries 12.
- **q = i, and q = e^{iπ/3}:** full, not monomial.
- **q = −1 (v = i): monomial.** γ₁ ↔ γ₂ with weight 64; γ₁₂ and γ₂₁ each self-paired with weight 256. The full 10 × 10
  form has rank 6 there (the Hecke algebra is not semisimple at q = −1). The cell couples to the rest only through
  τ(γ₁₂ μ) = τ(γ₂₁ μ) = 16, and cell products have Σ-components 4 in four cases.

**At q = −1 the cyclic slot rotation is an exact symmetry of the cell's constants.** With π the pairing above and w its
weights, c(x, y; z)·w(z) = c(y, πz; π⁻¹x)·w(π⁻¹x) holds for all 64 triples of the cell. The rotation
(x, y; z) ↦ (y, πz; π⁻¹x) has order 3 on the 8 alternating products:
- it fixes the orbit-2 pair (γ₁₂, γ₁₂; γ₁₂) and (γ₂₁, γ₂₁; γ₂₁);
- it has two 3-cycles, {(γ₁, γ₂₁; γ₁), (γ₂₁, γ₂; γ₂), (γ₂, γ₁; γ₂₁)} and {(γ₂, γ₁₂; γ₂), (γ₁₂, γ₁; γ₁), (γ₁, γ₂; γ₁₂)}.
  Each contains two of the orbit-4 failures and one of the two unimodal shortest products.

The values are consistent: the six failures all equal 16 at q = −1, the two shortest products 4, and 16·64 = 4·256.

On the label cube this is the rotation about the diagonal through the orbit-2 pair, not about the excluded diagonal of
§6a. With σ and t, which survive specialization, it generates that diagonal's stabilizer, a dihedral group of order 12.
So at q = −1 the hexagon that carries a symmetry is {the four orbit-4 failures, the two shortest products}, around the
axis of the two diagonal failures.

What this does not show: there is no symmetry at generic q (§6), so the C₃ exists only at the specialization. Nothing
here explains why q = −1 restores it, or connects it to unimodality.

## 7. Quantum-integer realizations: are the non-unimodal traces sign cancellations? (added 21 Nov, about 20 UTC)

**The test** (the main session's reading, `SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md` §6). For each of the 132
constants of Table A, write f = (positive content) × (product of quantum integers) × (a non-cyclotomic part). The quantum
integers are [n]_{q^m} = (q^{mn} − 1)/(q^m − 1), up to v-powers; the torus factor (v − v^{−1})^a is G_m^a.
- Realize [n]_{q^m} as the point count of R = Res_{F_{q^m}/F_q} P^{n−1}. Its cohomology is H*(P^{n−1})^{⊗m}, with Frobenius
  permuting the factors cyclically. So its graded dimensions are the coefficients of (1 + t + … + t^{n−1})^m, while its
  Frobenius traces give [n]_{q^m}.
- Realize the non-cyclotomic part, when it has nonnegative coefficients, by a split Tate object, with dimensions equal to
  traces.
- Then compare the graded dimensions of the product (symmetric? unimodal?) with its traces (= f, by construction).

Script: `E4_scripts\quantum_realize.py`, output `quantum_realize.json`. It enumerates every way to write the cyclotomic part
as a product of quantum integers.

**Results** [computed, all 132 constants]:

| | Count |
|---|---|
| f is a pure product of quantum integers (times content) | 116 |
| f has a non-cyclotomic part, with nonnegative coefficients, realized split | 16: 8 with 5q² + 6q + 5, 8 with (q² + q + 2)(2q² + q + 1) |
| Some realization with symmetric, unimodal graded dimensions | **132 of 132** |
| The quantum factorization is unique | 130 |
| It is not unique (the realization is a choice) | 2 |
| The realization uses a Weil restriction (m ≥ 2) | 8 (the six failures and these two) |

**The six failures of P-F-E3-01.**
- For each of them, f = [3]_q·[2]_{q²}², and this is the **only** factorization into quantum integers. The cyclotomic
  multiset is Φ₃Φ₄², and Φ₄ occurs only in [2]_{q²} = Φ₄ and in [4]_{q^m}-type factors, which would bring a Φ₂.
- So the realization R² × P², with R = Res_{F_{q²}/F_q} P¹, is **forced by the factorization**: canonical among
  quantum-integer realizations.
- Its graded dimensions are (1, 5, 11, 14, 11, 5, 1): symmetric and unimodal.
- Its traces are (1, 1, 3, 2, 3, 1, 1) = f. On each H²(R) the swap has eigenvalues ±q, so the trace cancels there.
- This confirms the main session's reading exactly: the non-unimodality is a sign cancellation from Frobenius acting by a
  permutation (the −1 of the swap). Hard Lefschetz holds on dimensions.

**The two non-unique cases.** These are c(γ²₁₂, γ²₂₁; γ²₁) and c(γ²₂₁, γ²₁₂; γ²₂), with cyclotomic multiset Φ₂²Φ₃Φ₄². They
factor as:
- [2]_q²[3]_q[2]_{q²}²;
- [2]_q[3]_q[4]_q[2]_{q²};
- [3]_q[4]_q².

All three give symmetric, unimodal dimensions; the last is split, with dimensions = traces. Here f is unimodal anyway, and
the realization is a choice.

**What the realization is and is not.**
- It is a realization of each constant separately, by a pure Tate object with a permutation Frobenius. Weights stay even,
  as in §3. The only non-split Frobenius needed is the cyclic permutation of a Weil restriction.
- It is not shown to be compatible with the multiplication of E^opp(3). No category in which these objects compose as the
  structure constants do is constructed here [open].
- With that caveat, the rank-three data support the reading "standard purity with permutation Frobenii":
  - positivity: effective objects;
  - unimodality: hard Lefschetz on graded dimensions;
  - VIII's unimodality of the traces fails only through the cancellation that Weil restriction introduces.

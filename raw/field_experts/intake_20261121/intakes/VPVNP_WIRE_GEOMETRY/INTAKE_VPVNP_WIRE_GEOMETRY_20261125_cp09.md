# Intake: VPVNP_WIRE_GEOMETRY (run 99), final checkpoint 09 (25 Nov 2026, 04:32 UTC)

By Claude Opus 5.5 at effort max, agent a5ef71dd, a copy of af3258db, which did the gate-1 check. Written for the pequalnp
session 672ae3a0. Run 99 is GPT-6 Astra (ChatGPT Pro mode); its worker records say "inherited effort not exposed".
- Return: `grothendieck_archive_transcription_20261110/research_returns/VPVNP_WIRE_GEOMETRY_checkpoint_09_20261125T0432Z_unzipped`.
  The paper is in `workbench/papers/wire_geometry/` (141 pages at cp06).
- Prompt: `TO_SEND/PRO/1_Archive_research_by_topic/SENT/99_VPVNP_WIRE_GEOMETRY/PROMPT.md`. Its main question: decide
  whether the unit square, and the square with its centre, are prices over C. The further items:
  - the explicit spectrum;
  - the two dichotomies compared;
  - the field, including characteristic 2;
  - the exponent of the direct case;
  - what the claims give GCT;
  - checks of the claims.
- Spot check: `INTAKE_VPVNP_WIRE_GEOMETRY_20261125_CHECK_EVENTS.tsv`, beside this file.

**Notation.** (H_A) is Anthropic's Theorem A.6 (cover duality) together with its Proposition C.3 (the price-space
embedding), from hexagon:2611.00954. P_k(q) is the crossing (partial-transpose) rank: the least rank_{12|34}(A) +
rank_{14|23}(B) over all ways of writing C_q = A + B.

## Most interesting items, ranked by usefulness

1. **The crossing-exponent gap** (`crossing_exponent_gap.tex` thm:crossing-exponent-dichotomy, l.13).
   - Under (H_A), the limit ρ_k = lim log P_k(q)/log q exists.
   - It is 1 if the unit square is not a price, and √2 if it is.
   - Over C the complex Hurwitz sums-of-squares exponent has the same gap (cor:hurwitz-exponent-dichotomy).
   - Gate 1 checked it. Two inputs are carried: the upper bound in lem:pt-upper, and prop:optimal-crossing-hubs.
2. **The planar reduction.** These are equivalent: the square is a price; the centred square is a price; planar flatness;
   no planar strict shortening.
   - **Q3b, per dimension D:** no D-shortening ⟺ all finite D-configurations are prices. If q_D is not a price, the
     shortening needs only nonantipodal wires between terminals.
   - **thm:tree-price-dichotomy:** square ⟺ a non-tree price ⟺ a strict four-point witness ⟺ a spectral witness.
   - Gate 1 checked these. They need (H_A), and the tree dichotomy needs C.3 only.
3. **The field (Q4).**
   - Q4a: a complex nonprice has a number-field certificate valid outside the primes dividing D.
   - Q4e: the price cone depends only on the characteristic.
   - Q4f: one strict finite certificate excludes a neighbourhood in all large characteristics.
   - **Q4n, over every field including characteristic 2:** a weight-block restriction of the crossing gate. My spot check
     found it correct.
   - Q4d, characteristic 2, is still OPEN. Under (H_A) its exponent is 1 or √2.
4. **The explicit spectrum is classified (Q1d, Q2a to Q2c).**
   - The named families give clustered stars and trees only.
   - The 2026 papers that run 99 read: Sakabe–Doğan–Walter (support functionals = quantum functionals),
     Botero–Christandl–Fraser–Leigh–Nieuwboer, and Alman–Li–Pratt.
   - Q1d-7 states the gap to the cross-polytopes as 1 − 1/√2. Q2c (cp03) gave (√2 − 1)/2 for the square: two
     normalizations, to be fixed before quoting either.
5. **Q3d: contraction ⟺ √rank(A − B) on Mat_μ(F₂) is not a price, for some μ ≥ 3.** A 16-point submetric lies outside
   the cut cone. Q3d itself is OPEN: whether contraction implies a strict shortening.
6. **GCT (Q6).**
   - Q6a: the padding and border-dc equivalence.
   - Q6b: determinant circuits of size ≤ 8N⁴.
   - Q6c and Q6d: conditional (m, N) ranges.
   - Q6e: a separating highest-weight equation in characteristic 0, conditional on OpenAI's constants.
   - Q6f.
7. **Audits of the preprints** by the same model:
   - Anthropic A/B (Q7a) and C/D (Q7b): PROOF_CHECKED_NO_FAULT;
   - OpenAI's direct step (Q7c): PROOF_CHECKED_NO_FAULT;
   - Q7d: REFINED_AND_PROVED.
8. **Closed routes.** Twelve rows end as REFUTED_AS_CONSTRUCTION or REFUTED_AS_IMPROVING_CONSTRUCTION, including:
   - Q4m: in characteristic 2 every equivariant map to the SL₂ centralizer kills the identity;
   - Q4h and Q4k (coefficient spans);
   - Q1c-8, Q1c-11, Q1c-13 and Q1c-14.

## 1. Useful or not

**Useful, strongly.**
- Its exponent gap turns the square question into "is the crossing exponent, or over C the Hurwitz exponent, 1 or √2".
- It agrees with run 98 on every shared statement.
- The main question is still OPEN: Q1 and Q2 over C, and Q4d in characteristic 2.

## 2. What it proved

Exact forms, with hypotheses. Locators are files of `workbench/papers/wire_geometry/` at cp09.
- **thm:crossing-exponent-dichotomy** (`crossing_exponent_gap.tex` l.13).
  - Statement: fix k and assume C.3 and the cover duality thm:coverduality (= A.6). Then ρ_k exists, with ρ_k = 1 if the
    unit square is not a price over k and ρ_k = √2 if it is.
  - Gate 1 checked the nonprice branch and the price branch through thm:square-pt-exponent.
  - It uses lem:pt-upper, whose upper bound q^{√2+o(1)} comes from Anthropic Prop. B.2 and Khoruzhii's counting. That
    bound is carried.
- **thm:square-pt-exponent** (`cycle_search.tex` l.102). The square is a price iff lim log P/log q = √2. If it is not a
  price, P(q) ≤ q^{√2−δ} eventually. Gate 1 checked it. Its header names C.3 only, but the proof uses A.6.
- **cor:square-hurwitz** (l.194) **and cor:hurwitz-exponent-dichotomy.** σ_C ≤ 2P_C and P_C ≤ 2σ_C. Gate 1 checked both.
- **thm:tree-price-dichotomy** (`tree_prices.tex` l.23), under C.3. The square is a price ⟺ some non-tree price ⟺ a strict
  four-point witness ⟺ a spectral witness. In the negative branch, over C, the prices are exactly the tree pseudometrics.
  Gate 1 checked it.
- **thm:introplanar, lem:cross-polytope-flat and thm:cross-polytope-price-flat** (`planar.tex`), under C.3. Gate 1
  checked them.
- **thm:square-shortening-equivalence and thm:crosspolytope-shortening (Q3b)** (`shortening.tex` l.115 and l.196), under C.3
  and A.6. Gate 1 checked them.
- **prop:weight-block-gate and cor:weight-block-square-gate (Q4n)** (`weight_block_gate.tex`), over every field.
  - Statement: P_k(2^k) ≤ P_wt(k) ≤ ∏(2k_i + 1)·P_k(2^k). The admissible algebra has dimension ∏ C(4k_i, 2k_i) < 2^{4k}.
    Blocks of size ⌈√k⌉ keep the whole exponent.
  - **My spot check found it correct:**
    - pinching commutes with twisted partial transpose, because the masks coincide;
    - the rank overhead is H;
    - the dimension count follows from Vandermonde;
    - the characteristic-2 example satisfies p + Γ_J(p) = I₄.
- **Other rows, at statement level for me:** Q4a, Q4e, Q4f; Q1a-1 to Q1a-4; Q1c-1 to Q1c-3 (A.6 reconstructed);
  Q2a to Q2c; Q5a and Q5b (5/4 and 4/3); Q6a and Q6b.

**Checks.**
- Run 99's register: 24 PROVED, 10 PROVED_CONDITIONALLY, 13 OPEN, 4 PROOF_CHECKED_NO_FAULT, and several restricted or
  refuted labels.
- Check events: 247 targeted proof checks, 210 independent re-proofs, 67 computations, 21 used and rechecked, 10 carried,
  3 refuted. All are by GPT-6 Astra workers.
- By others:
  - gate 1 (Claude Opus 5.5 at effort max, af3258db, 25 Nov; `pequalnp_work/square_note/GATE1_CHECK_20261125.md`);
  - this intake's spot check.

## 3. New since the earlier readings

MAP_COMPLEXITY.md read cp01, and the convener read cp03's register. New since then:
- **The exponent gap.** At cp03, Q1 had "lim log_q P_C(q) = √2". The final has "1 or √2".
- **Further new results:**
  - Q1's reformulation as a strict non-tree four-point witness;
  - R_square = 2 or 2√2;
  - the SL₂ centralizer restriction over C (`centralizer_gates.tex`, not read by me);
  - Q4f, Q4g, Q4n, and Q4h to Q4m;
  - the extension of Q3d;
  - Q6f and Q7d;
  - the refuted rows Q1c-8, Q1c-11, Q1c-13 and Q1c-14.
- **Changed in the checked text:** run 99's `shortening.tex` gained a 12-line definitions paragraph at l.85–96 (gate 1).

## 4. Open, with each main question's gate

- **Q1 and Q2, the square over C.** The gate: any fixed superlinear lower exponent for P_C(q), or for σ_C(q), decides the
  price branch. A strict non-tree price, or a strict spectral witness, would too. The search may be restricted to the
  SL₂ centralizer, at polynomial overhead.
- **Q4d, characteristic 2.** The same gap holds under (H_A). The finite values P(8) ≤ 16 and P(32) ≤ 132 decide nothing.
  Coupled multiplication and larger spaces are open.
- **Q3d.** Is √rank on Mat_μ(F₂) a price? Equivalently, does contraction imply a strict shortening?
- **Q1c-4, Q1d-5, Q1d-7, Q1d-8, Q2d, Q4b, Q4c and Q5c** are open as stated.

## 5. Relations

- **To run 98.** Every shared statement agrees:
  - Q3b = SH-08;
  - thm:tree-price-dichotomy = PG-SQUARE-GATE;
  - the exponent gap = run 98's "two-cut rank exponent 1 or √2";
  - Q4a, Q4f = PG-CYCLE-SPECIALIZATION.

  I found no contradiction.
- **To the literature.**
  - Liu hexagon:2611.00994, p.3 ("Two crossing cuts", the √2 direction);
  - Singh 2026 (P ≥ 4q/3; P(4) = 7);
  - Naslund 2020, Problem 12 (a superlinear crossing bound);
  - Hrubeš 2026 (subquadratic Hurwitz);
  - Khoruzhii 2026, Cor. 3;
  - Rossman–Zhu 2026, Lemmas 3.12–3.14;
  - Hrubeš–Wigderson–Yehudayoff, JAMS 24 (2011): central width = P_k(q), and C(PERM^{nc}_{4r}) ≥ Ω(P(2^r)/(r³·2^r)).
    So if the square is a price, this bound is 2^{(√2−1−o(1))r} over every field;
  - Dragomir–Nicas 2021 (the quadrilateral constant ≤ √2 in CAT(0));
  - Berg–Nikolaev 2008;
  - Bridson–Haefliger;
  - Alexander–Kapovitch–Petrunin 2023, Thm 10.14;
  - Lytchak 2026.
- **To the fleet.** Mirror of 25 Nov, 8,977 lemmas. No node on prices, shortenings, the Hurwitz problem or noncommutative
  circuits. L-gct-011 is still a conjecture; Q6 bears on it only through the preprints.

## 6. Candidates

- **Hexagon.** The exponent gap belongs in the square note; do not write a separate note.
  - A possible separate note: "Explicit spectral points on wire networks give only tree prices" (Q1d and Q2a–c with the
    2026 literature). It would need a different-model check first.
- **What the successor 102_VPVNP_SQUARE must carry.** I did not read the 102 prompt.
  - The final Q1 and Q2 gates: the exponent gap; the strict four-point and spectral witnesses; the SL₂ centralizer
    restriction; the weight-block restriction for characteristic 2.
  - Q3d's characterization.
  - The hypothesis corrections below.
  - Run 98's finite targets: q = 128, and width 7.
- **Corrections to report to the run's records.** These all name C.3 alone although their proofs also use A.6:
  - the Q3b register row ("assuming the price-space theorem");
  - thm:square-pt-exponent's header;
  - cor:square-hurwitz ("Assuming the complex price-space theorem").

## 7. Problems

1. **Hypotheses understated** in the three places listed under 6. Each proof uses cover duality A.6 as well as C.3. Run
   99's own reconstruction of A.6 (Q1c-1) is same-model.
2. **Same-model checks.** The "independent statement-only reconstruction passed" for Q3b, and every row marked
   independent, were done by GPT-6 Astra.
3. **The run stopped without its final readings.** The fifth review (04:02 UTC) recorded "MOVEMENT: no", one review
   without movement. Checkpoint 09 is final by the user's rule; the ledger notes [the user's words, omitted]. The 141-page paper had no completed final reading.
4. **Two normalizations of the tree-family gap,** 1 − 1/√2 (Q1d-7) and (√2 − 1)/2 (Q2c). Settle which one before quoting.
5. **No contradiction with run 98 was found.**

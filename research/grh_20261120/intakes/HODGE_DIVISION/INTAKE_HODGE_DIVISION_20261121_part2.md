# Intake of HODGE_DIVISION, part 2: checkpoint 10 (prompt 46 v2)

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747, the author of the division attack the run is built on),
21 Nov 2026. Part 1 covered checkpoint 01. Check events: `INTAKE_HODGE_DIVISION_20261121_part2_CHECK_EVENTS.tsv`.
**Checks of statements from my own attack are marked as checks by their author.**

## 0. What I read, and my scope

**The return:** `research_returns\HODGE_DIVISION_checkpoint_10_20261121T1808Z_unzipped\`, from 18:08 UTC. The run is GPT-6
Astra (ChatGPT Pro mode) and is still going. Formal review 05 (17:39 UTC) recorded MOVEMENT, with no consecutive
no-movement reviews.

**What I read:**
- `QUESTIONS.tsv` (all states; the rows Q1e, QW2, Q2e–Q2h, Q2l, Q3d, Q5, Q5c, Q5f, Q5k, Q5p);
- `LEDGER.md`, from review 05 to checkpoint 10;
- `research\uniform_division.tex`, **in full** (HD-U, HD-U6);
- the statements of HD-COMP and HD-COMP4 (`research\general_compensation.tex`);
- the header of D-SR-01 to D-SR-04 and the statement of D-SR-04 (`agents\imprimitive\semiregular_section.tex`);
- the H12 and H19 rows of `HEXAGON_CANDIDATES.md`.

**Computation:** I reran `agents\g34_eightfolds\g34_reconstruct.py` from a scratch copy (standard library only):
**ALL EXACT CHECKS PASSED.**

**Scope:**
- **Targeted proof check:** HD-U (in full), HD-U6 (the arithmetic of the substitution).
- **Computation rerun:** the D-G34 reconstruction.
- **Statement level:** HD-COMP/COMP4, D-G24, D-GF4, SF-QC01–05, HD-CM4, HD-CM6, D-SR-01–06, the Q2 exclusions (D-BI,
  D-SPW, HD-ALT, D-AST), the Q5 exclusions (SF-E801–E819R).
- My context is near its limit, so the proofs of D-G34-04 to D-G34-06 and of the sixfold sources were not read.

## 1. Verdicts

### HD-U (a uniform symmetric integral projector): confirmed; I rederived it. It supersedes my Theorem W.

**Statement.** For any Weil-type (A, θ, K) of dimension 2n with signature (n,n), any integral a ∈ K with a/ā not a root
of unity, and a detector of degree ≤ D, with Q = Nm(a):

c_t ≤ ⌈8·16^n/n!⌉·δ·⌈√T⌉·Q^{2n(n+1)}·D².

The constants are 1024, 5462 and 21846 for n = 2, 3, 4.

**The check.**
- S = [a]^* + [ā]^* acts on the summand ∧^jV_a ⊗ ∧^{2n−j}V_ā by α_j = a^j ā^{2n−j} + a^{2n−j} ā^j ∈ Z. This is symmetric
  in j ↔ 2n − j.
- α₀ − α_j = ā^{2n}(1 − r^j)(1 − r^{2n−j}) ≠ 0, with r = a/ā.
- So ∏_{j=1}^n (S − α_j) = ±R·e_W, with R = |∏(α₀ − α_j)| ∈ Z_{>0}.
- Mass: (S − α_j) has mass ≤ 2q + |α_j| ≤ 4q, with q = Q^n, so κ and R are both ≤ (4q)^n.
- **Inserted into HD-WQ** (the Gram shape d·[[1, s/2], [s/2, q²]], s = α₀, H = 4q² − s² ≤ 4q²): N ≤ 4δ·16^n q^{2n+2}D²/(n!)²,
  and the degrees are ≤ 8δ·16^n q^{2n+2}√T·D²/n!.
- I recomputed 8·256/2 = 1024, 8·4096/6 → 5462 and 8·65536/24 → 21846.
- **"An endomorphism that always works": confirmed.** a = f(2 + √−m), with Q = f²(m+4). Re(a/ā) is 3/5 for Q(i) and 1/7
  for Q(√−3), so a/ā is not a root of unity.

**The relation to my attack (author's check).** My Theorem W, δ_W ≤ c_t ≤ C·δ_W⁴ with C built from a resultant, is true.
HD-WQ made it quadratic. HD-U now makes it quadratic **with a field-uniform constant, polynomial in Nm(a)**.

> **The reduction of the attack in its final form: δ_W ≤ c_t ≤ ⌈8·16^n/n!⌉·δ·⌈√T⌉·Nm(a)^{2n(n+1)}·δ_W².**

### Target 1 (Q(i) fourfolds): final, no open gate

The run states "no new open gate" for target 1. HD-G01 to HD-G06 stand as in part 1.

**Q1e (statement level) extends target 1 to every determinant:**
- **HD-COMP:** contraction from a split (2n+2)-fold gives δ_W(A,L) ≤ c_K·D_{n+1}(Δ²), with c_K = 1 + Nm(τ), and no
  determinant restriction.
- **HD-COMP4:** numerical fourfold bounds for every determinant:
  - Q(i): 128Δ¹²·D_{G,6};
  - Q(√−7): 3·D_{6,7}(Δ²);
  - Q(√−2): 3·D_{6,2}(Δ²).
- **HD-CM4:** every class-number-one field, through the supplied Perry input (a preprint).

### D-G34 (Q(ω) split eightfolds): the computation is reproduced

The rerun prints:
- root span 6, a connected nonorthogonality graph, and absolute irreducibility;
- the ten reflections preserve the 756 roots;
- parabolic quotient of dimension 8;
- nilpotent ranks [4,1,3,3,2,1,2,1,1,2,4,4,4,1,1,2,1];
- **rational span rank 16**;
- K-span minor 1728;
- negative-sum leading minors [96, 2379, 58722, 2344041].

**The nilpotent ranks and the leading minors are identical to those reconstructed independently in HECKE_DIV S2**
(prompt 38, a different run). This is a computation rerun plus a cross-run agreement, not a re-proof.

D-G34-04 to D-G34-06 (the supplier repair from Schoen 1988, the Brauer transfer) remain at statement level. The quadratic
bound is c_t ≤ 21846·δ⌈√T⌉·(7f²)⁴⁰·D₈(f¹⁶Δ)².

### Sixfolds (target 2): statement level

| What | Status |
|---|---|
| Split sixfolds, through reflection-group curve sources: Q(ω), Q(i), **Q(√−7) via G₂₄ (order 336, rank 9; D-G24-01 to 05)**, **Q(√−2) via an F₄ extension (order 2304, rank 9; D-GF4-01 to 04)** | numerical D₆ bounds |
| Every class-number-one split sixfold | numerical: D_CM ≤ 2³¹⁸d⁵¹, and family bounds ≤ 2³²⁴d⁵⁷Δ⁶ (SF-QC01–05, HD-CM6). **Through Perry's deformation theorem (a preprint)** applied to the actual semiregular perfect complex of D-SR-01–04 on balanced E_i⁶ |
| Eisenstein sixfolds, every determinant | HD-E6 |
| Gaussian sixfolds, signed determinant class 3 | proved |
| **Other nonsplit determinants** | **open** (Q2i). Narrowed by D-BI-21/22, D-SPW-01–04, HD-ALT-02–05 and D-AST-01–03 to the exceptional inducing profiles and the long A_n shapes (row/column > 6n/7) |

The reflection groups match my Corollary O″ (genus-0 sources need reflection monodromy of dimension m ≥ (n² − 2n + 3)/2;
for n = 3, m ≥ 3). G₂₄ is the rank-3 reflection group over Q(√−7). Author's remark: consistent.

### Target 4 (n ≥ 5) and target 5 (n = 4 balanced-RM seed)

- **Target 4:** negative for every natural imprimitive family. The n = 5 maxima are 15 and 14, below 25. There is a
  terminating rank procedure per Nielsen component.
- **Target 5:**
  - For n = 3 it is done: an actual perfect complex on E_i⁶ (D-SR), and numerically through Perry.
  - For n = 4 the balanced-RM eightfold seed is open (Q5i). Exclusions SF-E801–E819R rule out stable and polystable
    bundles, locally free hulls with point, curve or surface defects, and reduced modifications.

**Counts.**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 2 (HD-U, HD-U6 arithmetic); HD-U as a check by the author of the attack it supersedes |
| Computation rerun, PASS, with cross-run agreement | 1 (D-G34 reconstruction) |
| Statement level | the rest |
| Refuted by me | 0 |

## 2. How it bears on the Hodge conjecture for abelian varieties (Weil classes), and the attack it opens

**Where the quantity is now bounded numerically** (δ_W ≤ an explicit integer on the whole family, so c_t ≤ HD-U·δ_W²,
so the Weil classes are algebraic with explicit integral representatives):

| Family | Inputs |
|---|---|
| Fourfolds, Q(i): every determinant | published: Schoen 1988, van Geemen 1996, the run's sixfold sources |
| Fourfolds, Q(ω): every determinant | published: Schoen 1988/1998 |
| Fourfolds, Q(√−7), Q(√−2): every determinant | the run's G₂₄/F₄ sources (statement level) |
| Fourfolds, every class-number-one K | Perry (preprint) |
| Split sixfolds, Q(ω), Q(i), Q(√−7), Q(√−2) | curve sources |
| Split sixfolds, every class-number-one K | Perry (preprint) |
| Eisenstein sixfolds, every determinant | — |
| Split Q(ω) eightfolds | G₃₄, published inputs (statement level beyond the rerun) |

**What stays open:**
- nonsplit sixfold determinants outside Q(ω) and the Gaussian class 3;
- every eightfold family other than split Q(ω);
- n ≥ 5, where the natural sources fail;
- fields of class number > 1;
- every non-Weil exceptional class.

**The attacks it opens:**
1. **For n = 4: the balanced-RM semiregular seed.** The run's exclusions leave only non-locally-free coherent objects with
   nonreduced defect modules at every support point. That is the exact next object to construct.
2. **For nonsplit sixfolds:** the long A_n shapes and the exceptional inducing profiles. Each now needs a finite Nielsen
   computation, rank 9, and original-field descent.
3. **For n ≥ 5:** a source that is neither a natural imprimitive cover nor a curve cover. That means a non-curve sheaf
   seed, as in target 5.

## 3. In the project's terms

- **c_t and HD-U** are the integral, effective form of condition A (cote 16, scan 050, as corrected in SIGN_NEXT
  SN-C03/C04).
- **The symmetric projector ∏(S − α_j)** is the polynomial algebraic inverse of the letter dated 6.1.1966 (our scans
  048–049).
- **The Gram positivity** is condition I (scan 049) and cote 44's Th. 4 on the Weil plane. The run states these three
  identifications itself (end of `uniform_division.tex`).
- **Ghosts (GHOSTS B03):** on every family above, the local division bound is eventually constant, with an explicit
  ceiling. So no ghost lives there.
- **Our ids:** HD-U supersedes the attack's Theorem W and HODGE_DIVISION HD-WQ. HD-COMP generalizes GHOSTS R20–R24 to all
  class-number-one fields. D-G34 is HECKE_DIV S2's group, now with published inputs.

## 4. Hexagon readiness (register not edited; changes listed)

| Row | Tests | Gate left |
|---|---|---|
| **H12** (ghost dichotomy; explicit bounded division for Q(ω), now Q(i), all determinants) | 1 and 2: yes for the Q(i) principal case (published inputs; two derivations). 4: yes for target 1 (my §5 and HD-G04 agree; HD-U checked). 3: target 1 is final within the run ("no new open gate"), but the run is still going | a literature search (the principle has Brünjes–Serpé as precedent; the explicit integers are new). A self-contained write-up with HD-U, and my read of every page. **One gate (the write-up and search); flag-worthy now for Q(i) and Q(ω) fourfolds.** **Add:** "HD-U: c_t ≤ ⌈8·16^n/n!⌉δ⌈√T⌉Nm(a)^{2n(n+1)}δ_W² for all K and n" and "Q1e: all determinants for Q(i), Q(√−2), Q(√−7)" |
| **H19** (split Q(ω) eightfolds from published inputs) | 1 and 2: claimed (Severn's numbers used only as a recomputed witness). 4: **advanced** by the rerun's PASS and the cross-run agreement with HECKE_DIV S2, but D-G34-04 to 06 are still unread by an intake. 3: the run is going | an intake full read of D-G34-04 to 06 (the supplier repair and the Brauer transfer). The run's final. A literature search (Severn's manuscript is the prior unrefereed claim; memory: no priority claims; we state our proof from published inputs). **Test 5 strong. Two gates.** |
| **New: the split sixfolds for Q(√−7) and Q(√−2) (D-G24, D-GF4)** | statement level | a full read, the run's final, a literature search (Markman covers split sixfolds qualitatively, in a preprint) |

## 5. Prompt updates (for the successor)

1. Write HD-U into the paper as the main division theorem. Theorem W and HD-WQ become its history.
2. **H19:** state D-G34-04 to D-G34-06 with full proofs and exact Schoen 1988 locators (Th. 2.0, Cor. 3.1, and the
   ramified "paired branch" hypothesis), so that an intake can read them in one pass.
3. Keep Perry-dependent rows (HD-CM4, HD-CM6, SF-QC) separate from the published-input rows in every table.
4. **The GHOSTS paper** was still missing from the attachment at checkpoint 01 (part 1). Attach `GHOSTS.tex` and its
   `sections\`.
5. **Main remaining attack:** the n = 4 balanced-RM seed, among non-locally-free coherent objects with nonreduced defects
   (Q5i). Then the nonsplit sixfold profiles (Q2i).

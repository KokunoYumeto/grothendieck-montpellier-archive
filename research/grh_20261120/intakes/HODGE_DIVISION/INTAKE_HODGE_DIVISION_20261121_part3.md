# Intake of HODGE_DIVISION, part 3: checkpoint 16 (prompt 46 v2)

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747, the author of the division attack), 22 Nov 2026. Parts 1 and 2
covered checkpoints 01 and 10. Check events: `INTAKE_HODGE_DIVISION_20261121_part3_CHECK_EVENTS.tsv`.

## 0. What I read, and my scope

**The return:** `research_returns\HODGE_DIVISION_checkpoint_16_20261121T2238Z_unzipped\`, from 22:38 UTC on 21 Nov. The
run is GPT-6 Astra (ChatGPT Pro mode) and is **still going**. Formal reviews 06 to 10 all recorded MOVEMENT; at review 10,
no consecutive review was without it.

**What I read:**
- `QUESTIONS.tsv`: every row added since checkpoint 10 (Q2ba–Q2ce and Q5r–Q5am, 54 rows), and the open rows Q2i and Q5i;
- `LEDGER.md`: formal review 10 in full, its "Main-question gates", and the headings from checkpoint 10 to checkpoint 16;
- the rows Q5u, Q5w, Q5y (SF-US, SF-UG, SF-E825);
- the finite-field Gauss-sum step of D-SPW (`agents\imprimitive\lie_small_fields\symplectic_weil_section.tex`,
  lines 180–200);
- a search of the checkpoint for cubic residue characters, Jacobi or Gauss sums, metaplectic covers, Kubota and
  Patterson.

**Scope.** My context is near its limit. The new findings are many long exclusion proofs (D-HOS17–22, D-OL09–15,
HD-ALT07/08, HD-AST04–06, D-ATT01–03, SF-E823–E839). I read them at the level of the statement and of the review's
account. The one proof step I checked is elementary: G_ψ(cb) = η(c)G_ψ(b) and |G_ψ(b)|² = q in D-SPW.

## 1. What moved since checkpoint 10

**No main gate closed. Both open main questions shrank strictly.**

| Gate | State at checkpoint 16 |
|---|---|
| Target 1 (Q(i) fourfolds) | complete; unchanged |
| Target 3 (Q(ω) split eightfolds through G₃₄) | complete; unchanged |
| Target 4 (n ≥ 5 natural imprimitive) | negative; unchanged |
| **Q2i, nonsplit sixfold determinants outside Q(ω) and the Gaussian class 3** | open, the supplier gate strictly smaller (below) |
| **Q5i, a balanced-RM semiregular eightfold seed** | open, the candidate class strictly smaller (below) |

**Q2i, what a supplier must now be (all statement level):**
- D-HOS17–22: higher characteristic-3 ordinary symplectic sources are excluded.
- D-OL09–15: ordinary orthogonal transitive factors are bounded: natural dimension ≤ 21 over q ≥ 3, ≤ 1134 in even
  characteristic, ≤ 1133 for odd natural dimension.
- HD-ALT07/08: long ordinary A_n shapes need max row/column > ((1 + √(1 − 4/(5h)))/2)·n. This is above 0.947n for
  Q(√−2).
- HD-AST04–06 and D-ATT01–03: the scalar-conductor argument. The scalar coordinate is a character, so the inducing field
  lies in its cyclotomic field. This excludes standard and two-box-tail tensors below explicit cutoffs for every
  **non-Eisenstein** field.
- The surviving finite residue: the exceptional inducing profiles (D-BI11/12, D-R5, D-BI16, HD-E8IF1), and a single
  **Sp₄(3)** factor of degree 4 or 5 (D-SPW-01–04).

**Q5i, what a seed must now be (all statement level):**
- SF-E823/E824: the actual unit-form and non-tensor global objects, of rank 522,387,689,472, are constructed (SF-US,
  SF-UG) and then excluded.
- SF-E825: a first-overlap obstruction, Ψ_π(det Q̃ + rB) = (7r/2)·Ψ_π(L).
- SF-E836/E837: common complete-intersection point defects and formally mixed square thickenings are excluded.
- SF-E838/E839: quadratic jets are excluded; leading bracket pencils must have rank ≤ 4.
- Left open: unstable sheaves, other nonreduced defects, rank-≤4 quadratic pencils, higher initial degrees, and
  positive-dimensional defects.

**Counts.**

| Check | Findings |
|---|---|
| Targeted proof check | 1 (the elementary Gauss-sum step in D-SPW) |
| Statement level | the other new rows (54 QUESTIONS rows; about 30 named findings) |
| Refuted by me | 0 |

No statement of my attack is changed. HD-U (part 2) still stands as the division theorem.

## 2. How it bears, and what attack it opens

**For the Hodge conjecture (Weil classes).**
- Nothing new is proved algebraic since checkpoint 10. The boundary of what curve and coherent-sheaf sources can reach is
  much sharper.
- **Exactly the two fields with extra units carry the positive results:** Q(ω), with μ₆ = μ₂ × μ₃ (G₃₄ eightfolds,
  Eisenstein sixfolds of every determinant), and Q(i), with μ₄ (fourfolds of every determinant, Gaussian sixfold class 3).
- Every other class-number-one field meets the conductor exclusions of HD-AST and D-ATT. D-FIELD (part 2) found
  reflection sources only over Q(√−2) and Q(√−7), and none over the other five.

**The direction of 21 Nov, item by item.**

1. **Alpöge's sign mechanism.** The run never touches it: there is no trace, power-sum or remainder argument. Its only
   Gauss sums are **quadratic** finite-field Gauss sums of the symplectic Weil representation, η(c)·G(b). The sign
   identity there is the finite analogue of the order-2 phase. No cubic or quartic phase occurs.
2. **Order-3 and order-4 phases (cubic residue characters, Kubota, Patterson, Dunn–Radziwiłł).** No statement of the run
   uses cubic Gauss sums, Jacobi sums or metaplectic covers. **The μ₃- and μ₄-eigenspace structure is nevertheless where
   all its positive results live:**
   - G₃₄ is a reflection group over Z[ω], with unit group μ₆. Each of its 126 reflection hyperplanes carries 6 unit
     multiples of a root (756 roots).
   - The order-4 cyclic Prym of target 1 is the (±i)-eigenspace of σ.
   - The residual **Sp₄(3)** endpoint of D-SPW is a characteristic-3 group. From memory, to verify: G₃₂, the rank-4
     reflection group over Q(ω), is C₃ × Sp₄(3), so this endpoint may be the μ₃ (Witting) case in disguise.
   - **That is a test to run, not a result.**
3. **The record's C₂ × C₃ patterns.** The run gives no statement on Erdős–Straus, Δ on GT-hat or GCT. The structural
   parallel, stated exactly: the unit group μ₆ = C₂ × C₃ of Z[ω] is the source of both G₃₄'s 6-fold root multiplicity and
   the "Eisenstein exception" in every conductor argument of HD-AST and D-ATT.

**The attacks it opens.**
1. **Sp₄(3) and G₃₂.** Decide whether the single surviving Sp₄(3) profile of D-SPW is realized by the G₃₂
   (Q(ω)-reflection) source. If so, the remaining nonsplit Eisenstein-adjacent profiles reduce to a G₃₂ Hurwitz family,
   the n = 3 analogue of G₃₄ for n = 4 (my Corollary O″: m ≥ 3 for n = 3, and G₃₂ has rank 4).
2. **The order-3 phase in the division mechanism.**
   - On Weil classes over Q(ω), the projector of HD-U uses S = [a]^* + [ā]^*. For a = ω the eigenvalues are cube roots of
     unity, and the summands ∧^jV ⊗ ∧^{2n−j}V̄ are separated by **cubic** characters j ↦ ω^{2j−2n}.
   - A projector built from the cubic character values, as GHOSTS P06 did with R = [ω]^*, has denominators that are
     products of differences of cube roots of unity, so powers of (1 − ω), the prime above 3.
   - **The exact question:** is the minimal integral denominator of e_W over Z[ω] a power of 3 for every n? If yes, the
     division constant's dependence on n is governed by the 3-adic valuation of ∏(1 − ω^k): a cubic analogue of the
     quadratic Gauss-sum normalization.
3. **The n = 4 seed (Q5i).** The surviving candidates are unstable or have nonreduced defects, or are rank-≤4 quadratic
   pencils. A balanced-RM object built from the order-3 automorphism of E_ω⁸, i.e. one equivariant for μ₃ rather than for
   the order-2 bivector symmetry, is not covered by SF-E836–E839, which are stated for the RM bivectors. That is a
   candidate to test.

## 3. In the project's terms

- **The Q2i exclusions** concern the monodromy of curve sources (my Corollary O″'s reflection-group criterion), now with
  conductor constraints that single out Q(ω) and Q(i).
- **The Q5i exclusions** concern the deformation route (DEG_L S-14; Grothendieck's variational question). Every
  exclusion so far is of a sheaf with a locally free hull, or with a reduced or curvilinear defect.
- **Cote 16** (condition A, scan 050; the algebraic inverse, scans 048–049) is unchanged. HD-U is still the division
  theorem.

## 4. Hexagon (register not edited)

| Row | Change |
|---|---|
| H12 | No change; one gate (write-up and literature search) |
| H19 | No change. Target 3 is complete within the run. Gates: an intake full read of D-G34-04–06; the run's final; a literature search |
| New | None: the new rows are exclusions, not results for posting |

## 5. Prompt updates

1. Test whether the Sp₄(3) residual of D-SPW is realized by a G₃₂ Hurwitz family over Q(ω). State G₃₂'s structure with an
   exact reference.
2. **Add the cubic-phase question:** the minimal denominator of the Weil projector over Z[ω] for every n, with the 3-adic
   valuation.
3. **Q5i:** test μ₃-equivariant balanced objects on E_ω⁸, which the bivector-based SF-E836–E839 do not cover.

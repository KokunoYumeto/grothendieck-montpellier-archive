# Intake of GCT_POS (prompt 52), checkpoint 03: the nonstandard items (Q8, Q9a–Q9e; N-001 to N-016)

By Claude Opus 5.5 at effort high (a8d75352), for the main session (Claude Opus 5.5 at effort max), 22 Nov 2026. The run is
GPT-6 Astra (ChatGPT Pro mode), effort not exposed. The Kronecker, plethysm, saturation and density items are taken by
a0805369. Check events: `INTAKE_GCT_POS_20261121_nonstandard_CHECK_EVENTS.tsv`.

## 0. What I read

**Return:** `research_returns\GCT_POS_checkpoint_03_20261121T2215Z_unzipped\`, checkpoint 03 (22:15 UTC); the run is
active. Its nonstandard work sits in `branches\nonstandard\`.

**Read:**
- the root `QUESTIONS.tsv`, rows Q8 and Q9a–Q9e;
- the branch `QUESTIONS.tsv` (N-Q01 to N-Q09);
- the paragraph headings of all N-findings;
- in full: N-001 and N-002 (`nonstandard_results.tex`, lines 237–335) and N-012 (`viii_unbounded_scaling.tex`).

**Reran**, in my work folder (scratchpad `gctpos_work`), with `python -I -B`:
- `verify_local_obstructions.py` (N-001, N-002): PASS;
- `verify_dimension_improvements.py` (N-005): PASS.

**My own independent checks:**
- `n002_check.py`, with my `h4cone.py`;
- the D = 0 products, from our `e3_constants.json`.

R-NEW-003 is a rational expression for the tensor series H^ten_4(t), on the Kronecker side, so it is left to a0805369.

## 1. Verdicts

| Finding | Verdict |
|---|---|
| **N-012** (VIII Conj. 3.2 as printed has no minimum) | **Targeted proof check, confirmed** (§2) |
| **N-002** (the first negative P-word in the C⊗C cone has length five) | **Independent re-proof, confirmed** (§2) |
| **N-001** (the D = 0 cell rotation does not extend to the whole table) | **Targeted proof check, confirmed**, and its certificate reruns. At D = 0, μe = e and e² = 16e for e = γ²₁₂; I rechecked e² = 16e from our own constants at v = i. Applying the rotation identity to (μ, e; e) gives w(e) ≠ 0 on the left and 0 on the right |
| **N-005** (rank-three dimension rings with 7276 cancelling pairs, and 9040 with every constant unimodal) | **Computation, confirmed** by rerun: 0 negative, domination, parity or associativity failures |
| **N-006** (the stalk gate at fixed q) | **Targeted proof check, confirmed as stated** (§2) |
| N-003, N-004, N-007–N-011, N-013–N-016 | Statement level; certificates not rerun |

The statement-level findings:
- **N-003:** 114 bar-invariant C⊗C-positive elements forming a K-basis of Ȟ₄. Its certificate is `mixed_cone_certificate.json`.
- **N-009:** the P-generated order of Ȟ₄ is not free over Z[v^±]. Its image over (Z/1024)[η]/η⁸ needs 126 generators,
  more than the rank 114.
- **N-008:** at the sign point D = 0, the rank-four ambient image has dimension 55, with Gram rank 42.
- **N-010:** a split form of Ȟ₄ over Q(D), with Gelfand–Tsetlin path lines.
- **N-013 and N-016:** under an explicit bar-fixed repair of VIII's rule, any unique minimum descends to the Q[D] word
  order, and existence becomes a finite decision.
- **N-014:** VIII's printed highest-weight label order is not defined.
- **N-015:** a certified basis of the actual Q[D] order.

## 2. The main checks

**N-012 (an erratum to VIII).**
- VIII's Conjecture 3.2 (TeX label cunimindegright2) asks for a unique pair (a_T, e_T) minimizing degree over all
  rational a.
- In rank one, y_n = q^{−n} lies in R^{−n} ∩ R̄^{−n}, since R^{−n} = q^{−n}A₀ and R̄^{−n} = q^nA_∞. Its residue is 1, and
  its degree is −n.
- So no minimum exists. On every minimal GT line of Ȟ₄ the same family q^{−n}t is admissible.
- I checked that the rank-one argument survives whether the lattice is taken over A₀ or over Q[q^{1/2}].
- Bar invariance is a goal stated in VIII's prose, not a condition in the displayed fibre. Requiring y = ȳ, or bounding
  the exponents, repairs it (N-013, N-016).

**N-002.**
- Using my own code, P₁₂₁₃ lies in the C⊗C cone.
- P₁₂₁₃₂ has exactly four negative coordinates: (2431, 2314) and its transpose, each 2D(12 − D) =
  −2(v⁴ + v^{−4}) + 16(v² + v^{−2}) + 36; and (3421, 2314) and its transpose, each 4δ(8 − D) = −4(v³ + v^{−3}) + 20(v + v^{−1}).
- The run's minimality check covers all 121 words up to length four.

**N-006.**
- The constant sheaf π^*M(1) on A¹ has stalk weight w − 2, and H_c² = M, with the actual P-action by precomposition.
- It solves the literal problem, but its stalk purity is the purity of M itself.
- In the terms of my GCT_NSRH part 2 (F50) and part 4 (the stalk target), it supplies no independent weight input. The
  sign-only route's gate is unchanged.

## 3. Where this corrects or settles our record

- **INT-NSRH-4** (my GCT_NSRH part 3) found the 11-letter word ω outside the C⊗C cone. N-002 shows the cone fails already
  at length five.
  - My part 3 tested four shorter words, and they are positive; but my work notes said "words up to length 6 positive",
    which overstates what I tested. **Correct it to: "the four words P₁, P₁P₃, P₂P₁P₃P₂, P₁P₂P₁P₃P₂P₃ are positive"**.
- **My open question** (part 3: does Ȟ₄ have a C⊗C-positive basis?) is answered:
  - **yes over K (N-003)**;
  - **no Z[v^±]-basis of any kind exists, positive or not (N-009)**.
- **E4_RANK_FOUR §4** said E(4) cannot be computed because VIII's ingredients are unspecified. N-012 sharpens this: even
  with all the GT data supplied (N-010), VIII's printed prescription selects nothing. N-014 adds that the label order is
  undefined.
  - Our rank-three reproduction (E4 §1–§2) uses VIII's printed elements, not the prescription, and stands. N-012 says so
    itself.
- **Our dimension-ring minima** (SPLIT_ZERO_IN_CONNES_CONSANI_TERMS §… and `consults\dimension_ring_minimal_pairs.out`:
  7952 overall, 11764 among unimodal rings) were window minima, not global ones.
  - N-005 gives 7276 and 9040.
  - NEG_NIGHT goes lower (see that intake).
  - **Our "minimum … attained by exactly one ring" is to be read as "within the search window".**

## 4. How it bears, and the attacks it opens

1. **The construction of E(4).** The open gate is a repaired, bar-fixed minimization rule. N-013 and N-016 make it
   finite, so the attack is to run N-016's decision procedure. On the result, compute the rank-four structure constants
   with my `e3_table.py` tests (a, sign, f, unimodality, Tate type, quantum-integer realization). That is the rank-four
   table the user asked for.
2. **Positivity at rank four.** By N-003 and N-009, positivity can hold only over K, or over a saturated order. Compare
   N-003's positive K-basis with the repaired E(4). If they agree, the question is whether VIII's form ±(v − v^{−1})^a f
   holds there, and whether the unimodality failure P-F-E3-01 recurs. By E4 §7 it would be a sign cancellation from Weil
   restriction.
3. **The stalk gate (Q8)** is closed only literally (N-006). What remains is a sheaf whose stalk weights are known
   independently of its cohomology.

## 5. Errata and Hexagon readiness

**Errata to GCT VIII** (drafts only, to the author, under the outreach rules):
- (i) Conj. 3.2 as printed has no minimum (N-012, confirmed here);
- (ii) the unimodality clause of Conj. "Positivity" fails at r = 3 (our P-F-E3-01, H23);
- (iii) the printed b₂ = +(q + 1)²/q is a misprint for −(q + 1)²/q (E4 §1);
- (iv) the printed label order is undefined (N-014, statement level).

**Hexagon.**

| Candidate | Complete | Self-contained | Stable | Checked | Interest | Gate left |
|---|---|---|---|---|---|---|
| A GCT VIII errata note: N-012 with H23 (P-F-E3-01) and the b₂ misprint | yes | yes | N-012 is elementary and stable; the run is still active on the repair | N-012 targeted; P-F-E3-01 computed and cross-checked | moderate (GCT) | a literature check (has anyone noted these?); the note to Mulmuley first; an independent re-run of P-F-E3-01, as H23 already asks |
| N-003 with N-009 (a positive K-basis of Ȟ₄; no integral basis) | not yet | yes | no (run active) | statement level | GCT | the run's final and a rerun of the certificates |

## Full depth (22 Nov, second pass)

Every statement-level finding of §1 was taken further. The events are appended to the CHECK_EVENTS file. The certificates
were rerun in my work folder (scratchpad `gctpos_work`) with `python -I -B`.

| Finding | Check | Result |
|---|---|---|
| **N-003** (positive K-basis of Ȟ₄) | `mixed_cone.py` rerun | 114 basis elements, 0 failures. **Computation, confirmed.** |
| **N-009** (the integral order is not free) | `verify_mixed_jet_certificate.py` rerun | **PASS**: \|M\| = 2^3690 and \|𝔪M\| = 2^3564, so dim M/𝔪M = 126 > 114, with independent Smith levels. `lattice_specialization.py` also reruns: the word lattice is proper. I read the logic (a surjection onto M/𝔪M, then Nakayama) and it is correct. **Confirmed.** So Ȟ₄ has no Z[v^±]-basis of any kind. |
| **N-004** (free ⟺ cone basis) | proof read | z = ΣB_j has a positive coefficient at every coordinate, and ε₋(z) = 1 splits off Az. The step "stably free of rank > 1 over Z[v^±] is free" cites Abedelfatah 2010, Thm. 1.3. **Confirmed modulo that citation.** With N-009, there is no A-basis in the cone. |
| **N-007** (b = P₁/D²) | computed | b² = (1/D)b, with a pole at q = −1. **Confirmed.** It is the same phenomenon as NEG_NIGHT NN-G008. |
| **N-008** (the sign point D = 0) | `sign_specialization.py` rerun | Dimension 55, trace rank 42. **Computation, confirmed.** |
| **N-010** (split form over Q(D)) | `rational_gt_rank4.py` rerun | Exit 0. **Computation, confirmed.** |
| **N-011** (why the obstructions sit at the Laurent edges) | proof read | For g = δ^ε f(D), the extreme coefficients equal the leading D-coefficient of f. **Confirmed.** It explains every extreme-degree negative we have seen: N-002, F57, INT-NSRH-4, F67. |
| N-013, N-014, N-016 (the bar-fixed repair, the undefined label order, the finite decision procedure) | statements and set-up read | Statement level |
| N-015 (a basis of the Q[D] order) | `polynomial_order_rank4.py` rerun | Reached rank 60 of 114 before I stopped it for time. Statement level |

**Result:** no finding of the nonstandard branch is refuted. The integral and rank-four questions of my GCT_NSRH intakes
are now settled:
- positive over K (N-003);
- no integral basis (N-009);
- the extreme-degree signs are structural (N-011).

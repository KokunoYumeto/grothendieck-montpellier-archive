# Intake of GCT_NSRH, part 3: checkpoint 06 (what is new since checkpoint 05)

By Claude Opus 5.5 at effort high (the agent of parts 1 and 2), for the main session (Claude Opus 5.5 at effort max),
21 Nov 2026, about 06:xx UTC. The run is GPT-6 Astra (ChatGPT Pro mode); the run records its effort as "not exposed". It is
still going. Work file: `agent_notes\20261121_intake_GCT_NSRH_NOTES.md`.

## 0. What I read, and my scope

**Return:** `research_returns\GCT_NSRH_checkpoint_06_20261121T0330Z_unzipped\`, snapshot 03:28 UTC. It was the newest
present when I started. I had not read it before. Part 2 covered checkpoint 05 (02:47 UTC).

The paper is now F01–F57 (166 pages). Review 02 (03:00 UTC) recorded movement, so the no-movement count is 0.

**Read:**
- `STATUS_TIME.txt`;
- the `LEDGER.md` blocks from 03:00 to 03:29 UTC (review 02, F55, F56, the rank-four and rank-five word searches, the bar
  supplements, F57).

**Read in full, with its proof:**
- **F57**, the main new result (paper lines 8623–8934). I recomputed it.

**At the level of the statement:** F55 parts 1–3, F56, and the F56 supplement (the entrywise formal bar).

**GCT IV source**, checked for F57's input: Proposition 11.6(iii), Θ(P_s) = Q_s (TeX line 3815), and the Θ^op
contragredient (line 3925). Figure 22 itself was not reopened: I used the run's transcription of its matrices.

**My own computation:** an exact Laurent-integer program over S₄,
`<local>/AppData\Local\Temp\claude\f2c80a22394db22f\e0d20ada-e036-40ad-83b1-31e9a63b69bc\scratchpad\scripts\h4cone.py`,
with the checks in `h4cone_check.py` and `f57.py`. It tests my dual-cone point (part 1, INT-NSRH-2) at rank four.

## 1. Verdicts

### F57: a P-word with negative trace on an actual rank-four simple module. Computation certificate and targeted proof check: confirmed.

**What it says.** Take ω = P₂P₃P₂P₃P₂P₃P₁P₂P₁P₂P₁ on the additional five-dimensional simple module N^# of Ȟ₄ (IV, §11.8).
- Its trace is p(D) = −D⁹ + 20D⁸ − 163D⁷ + 734D⁶ − 2048D⁵ + 3712D⁴ − 4352D³ + 3072D² − 1024D.
- The coefficients of p(D) at v^{±18} are −1.
- So no basis of N^# makes P₁, P₂, P₃ nonnegative Laurent matrices.
- No single-parity finite power trace can equal ±p(D). A two-parity Tate complex can (dim E₊ = 4098, E₋ = Q_ℓ(∓9)).

**What I checked.**
- With the five-state matrices Q₁, Q₂, Q₃ as transcribed, I recomputed exactly (sympy):
  - Q_i² = DQ_i;
  - Q₁Q₃ = Q₃Q₁;
  - Tr(Q₁Q₂Q₁Q₂Q₁Q₃Q₂Q₃Q₂Q₃Q₂) = p(D);
  - the Laurent expansion −1, 0, 2, 0, 4, 0, 36, 0, 67, … from v^{18} down.
- The passage to N^# uses Θ(P_i) = Q_i (IV, Prop. 11.6(iii), confirmed in the source) and the Θ^op contragredient
  (IV §11.4). It gives ρ_{N^#}(ω) = (Q_w)^t with the reversed word, and the trace is unchanged.
- The occurrence argument, N^# ⊂ Res(M_{(2,1,1)} ⊗ M_{(3,1)}) when dim V ≥ 3 and dim W ≥ 2, is read at the level of the
  statement.
- The finite-power-trace and parity statements follow from F02.

**Scope, correctly stated by the run.** F57 excludes a strict, effective, simple-by-simple kernel model on the full
rank-four algebra. It does not touch:
- the two-row quotient;
- IV's signed and factored positivity;
- positive bases of the whole tensor module.

### F55, F56 and the F56 supplement: statement level only

| Finding | What it says |
|---|---|
| F55, part 1 | A regular one-place fractional model preserving the identity and marked traces |
| F55, part 2 | The all-places inserted-trace gate: no regular family at every place over v = 1 |
| F55, part 3 | Continuous genuine trace branches force f(v) = Σ m_i v^{r_i} |
| F56 | A graded matrix-kernel category with split K₀ equal to the actual word algebra; its Karoubi completion changes the algebra |
| F56 supplement | An entrywise formal bar |

The ledger records root and independent whole-proof checks for all of these. I checked none of them.

The rank-four and rank-five word-trace searches (no negative coefficient on the ordinary 16- and 32-dimensional modules)
are searches, as the run itself says; they are not findings.

**Changes to earlier findings.** Nothing I checked in parts 1 and 2 is changed or withdrawn.

**Counts for part 3.**

| Check | Findings |
|---|---|
| Confirmed, with an independent exact recomputation | 1: F57 |
| Read at the level of the statement | 5 |
| Gaps or refutations | 0 |

## 2. How checkpoint 06 bears on my three points

### (a) F50 and H01 (the H01 v2 write-up)

There is no change. Checkpoint 06 adds nothing to F50's construction or its weight gate. The ledger's pending item,
"compatible … realization with designated labels and independent local weight bounds", is exactly the stalk-side gate that
part 2 located. F50 stays as folded into H01: the worked Gaussian case, and the proof that the pointwise bound cannot be
removed.

### (b) My dual-cone point (part 1, INT-NSRH-1 and INT-NSRH-2): tested at rank four; it fails for P-words

**INT-NSRH-1 in IV's terms.** IV's algebra involution Θ (Prop. 11.6, with θ⊗1 ↦ Θ and 1⊗θ ↦ Θ) satisfies Θ(P_s) = Q_s. My
θ⊗θ, which fixes Ȟ_r, is Θ². The sign identity (C′⊗C′ coordinates = (−1)^{l(x)+l(y)} times C⊗C coordinates) is therefore
a direct consequence of IV's own involution. It is still not used in the run.

**INT-NSRH-4 (new; exact computation).** I computed the KL basis of H(S₄) by the standard reduction and checked it:
P_{e,3412} = P_{s₂,3412} = 1 + q, and the four nontrivial pairs below 4231. Then I expanded P-words of Ȟ₄ in the C′⊗C′
basis of H₄ ⊗ H₄.

| Word | C′⊗C′ coordinates | Violations of C⊗C positivity |
|---|---|---|
| P₁ | 4 | 0 |
| P₁P₃ | 16 | 0 |
| P₂P₁P₃P₂ | 196 | 0 |
| P₁P₂P₁P₃P₂P₃ | 324 | 0 |
| **ω** (F57's word) | 324 | **6** |

ω's six negative C⊗C coordinates:
- the pairs (2013, 3201) and (3201, 2013), with coefficient −5 at v^{±15};
- the pairs (2013, 3021) and (3021, 2013), with −3 at v^{±16};
- the pairs (2103, 3021) and (3021, 2103), with −3 at v^{±15}.

The negatives sit at the extreme degrees, as in F57. A rerun at r = 3 reproduces the positivity of part 1.

**Consequences.**
- INT-NSRH-2 (every alternating P-word is C⊗C-positive, giving a positive word basis) is a **rank-three phenomenon**. At
  rank four the P-words themselves leave the cone.
- Whether Ȟ₄ has *some* Z[v^±]-basis inside the C⊗C cone is still open. BMS say they are "uncertain" (IV, Remark 11.19).
- The decisive test is now finite: a linear-programming search over bounded-degree combinations of words, against the 576
  C⊗C coordinates.
- F57 (the simple N^#) and INT-NSRH-4 (the ambient cone) are **two independent faces of one rank-four obstruction**, carried
  by the same word ω. Neither implies the other.

**A correction to part 1.** Part 1 identified the C⊗C cone with the classes of simple objects in graded category O. For S₃
that is harmless, but in general it is not justified. The basis used here is KL's C_w = (−1)^{l(w)}θ(C′_w), with KL
polynomials. Classes of simple objects involve inverse KL polynomials and a w₀-twist. The categorical "Koszul-dual heart"
suggestion of part 1 therefore needs that identification checked before it is used. The sign identity and all the
computations are unaffected.

### (c) JAC1964

No bearing. Checkpoint 06 concerns the nonstandard Hecke algebras and their trace realizations, not cote 44 or Hodge
positivity.

## 3. Scope of the two proofs

No new finding uses Alpöge's or Masullo's theorems. F57 uses only IV's matrices and F02.

## 4. Integration and prompt updates

**QUESTIONS rows of GCT_NSRH:**
- **Q3-AMBIENT:** add "the C⊗C cone: positive word basis for r = 2, 3 (INT-NSRH-2; IV Rem. 11.19); at r = 4 the word ω
  leaves it (INT-NSRH-4); basis existence open".
- **Q3-POSITIVE-ACTION / F57:** cross-reference the same word ω.

**Successor of GCT_NSRH**, which extends my earlier prompt updates:
1. Give it INT-NSRH-1 in IV's language (Θ²), INT-NSRH-2 and INT-NSRH-4, together with the script.
2. Ask it to decide, by an exact linear-programming or lattice search, whether Ȟ₄ has a basis in the C⊗C cone or in the
   signed/factored form of IV Remark 11.19.
3. Ask it to explain why the ω-negativity sits at the extreme degrees in both F57 and INT-NSRH-4.
4. Correct the category O wording, as in section 2(b) above.

## 5. Hexagon readiness

Nothing new is ready. F57 and INT-NSRH-4 are rank-four obstructions of interest to GCT specialists; the run is active and
the basis question is open. Not a candidate yet.

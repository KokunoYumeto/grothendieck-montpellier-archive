# Sweep 1, scope tower: corrections and refinements

Written by Claude Opus 5.5 at effort max, sweep 1, scope `tower`, 18 Nov 2026. The returns are by GPT-6 Astra (ChatGPT
Pro mode). For each item: the row, what is wrong or can be sharpened, the fix, how sure I am, and what I read. "Read"
means the register row unless a proof file is named. The checks I made are in `CHECK_EVENTS.tsv`.

## A. Mathematics

**1. E.3 has a proof on record, and the programme map still calls it running.**
- Rows: LM7_PUSH E.3 (Open), EXIT_TOWER E.49, GT_TOWER_CHECK A.3 and A.7, DELTA_ON_GT A.84, LM8_PUSH C.21.
- What is the case:
  - E.3 asks whether full GT̂ reaches the extra CM coset.
  - LM8_PUSH C.21 (16 Nov) shows that the CM image of GT̂ is either the Galois index-two fibre product or the whole
    normalized product, according to Δ|GT̂. So E.3 is exactly the question whether Δ|GT̂ ≠ 0.
  - GT_TOWER_CHECK A.7 (checkpoint 10, 17 Nov) proves Δ|GT̂ = 0 for every multiplier, with G_Q ⊆ GT̂ ⊊ ker Δ ⊊ GT̂₀.
  - The proof of record is A.3 (EXIT_TOWER E.49, with its two label repairs) plus the passage to all multipliers.
- The fix: in `notes_headlines/PROGRAMME_MAP.md`, replace "GT_TOWER_CHECK, running, checks it" with this sentence:
  "GT_TOWER_CHECK (ended at checkpoint 10) proves it as A.3/A.7, after repairing E.49's label comparisons. It rests on
  EXIT_TOWER E.44 = GT_TOWER_CHECK A.1 (𝒥(A) = A on all of GT̂). The independent finite census (A.4) was not obtained.
  Every proof so far is by GPT-6 Astra."
  - The map's GT_TOWER_CHECK line (checkpoint 1: 29 Proved, 13 Open) is also stale: checkpoint 10 has 165 Proved,
    2 Known, 13 Open.
- How sure: high on the state of the records; I did not check the mathematics of A.1 or of the naturality equation
  (A.C14).
- Read: the rows; `pro_intake_20261117/GT_LINE_INTAKE_20261117.md`; EXIT_TOWER `sections/E_cm_parity_vanishing.tex`,
  lines 95–106 and 520–534.

**2. The descent subgroup C^φ of §47 has two markings, and the same formula names both.**
- Rows: LM8_PUSH C.1, C.3, C.8, C.25, C.27; GT_TOWER_CHECK B.1, B.1.1, B.1.2, B.1.8; DELTA_ON_GT A.62, A.65, A.68,
  A.69, A.85; LM2 E.1, E.3; LM8_LIE B.28.
- What is wrong:
  - LM8_PUSH C.1 defines C^φ = Fix(D). Its normalization check writes x = (rs)², y = (sr)²; these are LM2's generators
    x_L, y_L of GT_TOWER_CHECK B.1.1. So LM8_PUSH's C^φ is the physical C_L, and C.1's "C^φ contains the Galois image"
    is right: D_L(σ) = σ.
  - GT_TOWER_CHECK and DELTA_ON_GT call the literal C_P "the C^φ of the current question". C_P meets G_Q in {1, c}
    (B.1.2).
  - Both groups are written with "φ(x) = s, φ(y) = τ", in different letters.
- What follows:
  - There is no contradiction between LM8_PUSH C.1 and GT_TOWER_CHECK B.1.2.
  - LM8_PUSH C.3 (pentagon implies descent; Open at checkpoint 17) is decided positively by GT_TOWER_CHECK B.1.8, which
    proves D_L|GT̂ = id.
  - The same holds for the second half of LM8_LIE B.28, and for LM2 E.3 in LM2's own marking.
  - The open "C^φ ⊆ ker Δ" is two different questions: C_L ⊆ ker Δ (LM8_PUSH C.8; hunch H4 of the GT line intake) and
    C_P ⊆ ker Δ (GT_TOWER_CHECK B.1).
- The fix: every item about C^φ names its marking (C_L or C_P). In the handbook (I.1.3), one item defines both groups,
  with D_L = Ad_c ∘ D_P.
- How sure: medium-high. Not opened: LM2's own text of the "corrected additional orbifold compatibility" (E.1), to
  confirm that it is C_L.
- Read: LM8_PUSH `sections/C.tex`, lines 1–112, 5866–5885, 6045–6065 and 6160–6178; the GT_TOWER_CHECK rows.

**3. A sharpening: the literal descent group meets GT̂ in {1, c} only.**
- Rows: GT_TOWER_CHECK B.1.2, B.1.8; LM4_SUCCESSOR A.36.
- The argument: on GT̂, D_P = Ad_c (B.1.8), and the centralizer of c in GT̂ is {1, c} (LM4_SUCCESSOR A.36). So
  C_P ∩ GT̂ = {1, c}. This sharpens B.1.2's C_P ∩ G_Q = {1, c}.
- How sure: high, given B.1.8 and A.36. Neither has been checked outside its run.

**4. The quadratic characters vanishing on GT̂ were found first in LM8_PUSH, without A.7.**
- Rows: LM8_PUSH C.30 and C.9; GT_TOWER_CHECK B.2.25 and B.1.8; DELTA_ON_GT B.40.
- What is the case:
  - LM8_PUSH C.30 (checkpoint 17, 16 Nov 02:52) gives explicit independent quadratic characters indexed by the primes
    p ≡ 5 mod 12. They vanish on all of GT̂ and map onto a countable product of C₂, even on GT̂₀,₁ ∩ ker Δ. It proves the
    exact countably infinite quadratic rank, and it does not use Δ|GT̂ = 0.
  - GT_TOWER_CHECK B.2.25 (17 Nov) proves the same dimension statement with the family Δ ∘ D_Pⁿ. On GT̂ we have
    D_P = Ad_c (B.1.8), so Δ ∘ D_Pⁿ = Δ there. That family therefore vanishes on GT̂ exactly because of A.7; the
    statement lists A.7 among its dependencies.
  - The GT line intake (Claude Fable 5.2 at effort high, 17 Nov) reported "𝒳 has dimension ℵ₀" as new from
    GT_TOWER_CHECK. LM8_PUSH had never been read by an intake.
- The fix:
  - Make LM8_PUSH C.30 the item of record for the dimension statement, and keep GT_TOWER_CHECK B.2.25 as a second
    proof with the shift structure (`MERGES.tsv`).
  - Compare C.30's primes p ≡ 5 mod 12 with GT_TOWER_CHECK's d̄_p (p ≡ 3, 5 mod 8) before H7 of the intake is taken up.
  - LM8_PUSH's "gentle group" is GT̂₀ ∩ 𝒫₁; check that the two spaces are the same before calling them equal.
- How sure: high on the dates and the dependency; medium on the identity of the two spaces.

**5. EXIT_TOWER E.49 lists an open row as a dependency, but does not use it.**
- Rows: EXIT_TOWER E.49, E.46 and E.77, which list E.24 (Open: G_Q = GT̂?).
- What is the case: in E.49's proof, E.24 is cited only to say which tests the E.46 witness passes. It is not a step,
  and the vanishing of Δ does not rest on it.
- The fix: mark E.24 as context in E.49's dependencies. E.46 and E.77 still need a look: I did not read their proofs.
- How sure: high for E.49.
- Read: `sections/E_cm_parity_vanishing.tex`, lines 520–534.

**6. Other proved rows that rest on an open row of the same run (15 in the scope).**
- The rows:
  - CYCLOTOMIC_KERNEL C10 ← E3;
  - EXIT_TOWER E.46, E.49, E.77 ← E.24;
  - LM2 B.g15, E.6 ← B.g11;
  - LM4 C.28, C.29 ← C.12;
  - LM4 D.23 ← D.12;
  - LM4 D.31, F.8 ← F.7;
  - LM4_SUCCESSOR A.129 ← C.14;
  - LM8_LIE G.23, G.24 ← G.16;
  - LM8_PUSH C.19 ← B.2.
- What is known so far:
  - E.49 is settled (item 5).
  - LM4 D.31 ← F.7 (the nonsolvable centralizer comparison): LM4_SUCCESSOR B.36 audited exactly this path. It found
    that no proved statement of the attached returns uses the nonsolvable equality, so the use is likely sound.
- The fix: for each of the others, read whether the open row is a step or only context. Sweep 0 did not flag this
  case; add it to `build_register.py`.
- How sure: the list is by script and complete for same-run dependencies.

**7. LM8_PUSH corrects a step behind LM6's Fermat theorem.**
- Rows: LM8_PUSH D.22 (Refuted) and D.23; LM6_POINTS_AS_SECTIONS E.9 and E.12 (outside this scope).
- What is the case:
  - D.22: the "ramification-only Tate-parameter divisibility" cited as "Steklov Proposition 4.6/5.10" and as "LM6E8" is
    false. At the unit Fermat cusp q = 256⁻¹ t²ⁿ(1 + O(tⁿ)), whose 2-adic valuation −8 no odd n divides.
  - D.23 re-proves every Selmer section of U_n/Q cuspidal for odd n ≥ 3, with the corrected cusp constant. With D.56 it
    gives the full section set: three cusp packets, each an H¹(Q, Ẑ(1))-torsor.
- My check: I recomputed q = λ²/256 (1 + O(λ)) for the Legendre family from j = 256(λ² − λ + 1)³/(λ²(λ − 1)²). The
  arithmetic core of D.22 holds.
- The fix:
  - The sweep that holds LM6 reads which step of LM6 E.8–E.12 used the divisibility.
  - Until then, LM6's theorem is cited through LM8_PUSH D.23.
  - The source "Steklov Proposition 4.6/5.10" must be identified before any outreach.
- How sure: high on the computation; medium on what the failure touches in LM6.

**8. Δ names at least five things in the scope.**
- The uses:
  - the CM character: LM7_PUSH E.65, DELTA_ON_GT, GT_TOWER_CHECK, EXIT_TOWER E.49, LM4_SUCCESSOR A.105, LM8_PUSH part C;
  - Gal(K̄/K^ab): LM8_PUSH part A (A.1, A.3, A.6), CYCLOTOMIC_KERNEL E1–E3;
  - a discriminant, and Gal(k(μ₃)/k): both in LM8_PUSH;
  - Δ_σ: EXIT_TOWER E.47;
  - the tame relator Δ_q: LM8_PUSH D.29.
- LM8_PUSH alone uses Δ for the Galois group and for the character.
- The fix: in the handbook, Δ is the CM character only, and G_{K^ab} is written for the Galois group.
- How sure: high.
- Read: grep over LM8_PUSH's `sections/*.tex`, and the rows.

**9. "The element" of E.58 and E.46 is a family, and two different Δ = 1 witnesses are in use.**
- Rows: LM7_PUSH E.58, EXIT_TOWER E.46, GT_TOWER_CHECK A.2, LM4_SUCCESSOR B.42–B.45, DELTA_ON_GT B.15.
- What is the case:
  - Every member of the family has Δ = 1 and the same frames. Tripod and resolvent values vary over it.
  - There are two witnesses: parities (1, 0) (E.58, E.46) and (0, 1) (LM7 D.46 as repaired in DELTA_ON_GT B.15).
- The fix: texts that say "the element" or "the witness" say which family, and attribute to it only invariants that
  are constant on the family.
- How sure: high. These points are from the intakes of 17 Nov; they are listed here for the merges.

**10. The GT̂ half of LM4_SUCCESSOR A.13 follows from A.7 directly.**
- What is the case: Δ = 0 on the involutions of GT̂ is the restriction of GT_TOWER_CHECK A.7. A.105 then turns it into
  ε_A ≡ d mod 3 for every involution of GT̂.
- The GT̂₀ and 𝒫 halves stay open. For GT̂₀, Δ is now one of infinitely many characters vanishing on GT̂ (item 4), each an
  invariant of conjugacy classes of involutions.
- How sure: high on the logic; conditional on A.7.

**11. Cote 148.**
- Rows: EXIT_TOWER B.12 and B.25, GT_TOWER_CHECK B.5 and B.5.1, LM4_SUCCESSOR E.37 and E.38, DELTA_ON_GT B.31–B.33.
- Where the runs agree: 542 objects in nine families; 1620 arrows in fourteen named families forming sixteen
  S₅-orbits; "orbites" after "14" is struck out on the scan.
- What is still to check:
  - The 1080 relators fix one realization only. GT_TOWER_CHECK B.5.1 shows that the path classes form a torsor, so
    DELTA_ON_GT B.33 is closed only for the specified realization.
  - GT_TOWER_CHECK B.5 reads the lower fractional twist as 1/4, where our first-pass transcription has 1/3.
- The fix: check our scans 31–36 before the edition changes in every language.
- How sure: the counts agree in three runs; the 1/4 reading is not checked by me.

## B. The register and its records

**12. Sweep 0's lineage misses most cross-run links of this scope.**
- What `build_register.py` misses:
  - TeX-escaped run names ("EXIT\_TOWER E.44") are not matched. All 15 GT_TOWER_CHECK → EXIT_TOWER links are lost,
    including the audit of E.44 and E.49.
  - The short names are mapped wrongly or not at all:
    - "LM4 X" in LM4_SUCCESSOR means LM4_FINITE_GROUP_ACTIONS, but LM4 is mapped to LM4_SUCCESSOR itself, so 75 links
      are dropped;
    - "LM8 X" means LM8_LIE_APPROXIMATIONS, but is mapped to LM8_PUSH (one mislink: DELTA_ON_GT B.19's "LM8 A.22");
    - "LM6", "SECTIONS" and "LM1" have no alias.
- The fix:
  - Replace `\_` by `_` before matching.
  - Add the aliases LM4 → LM4_FINITE_GROUP_ACTIONS, LM8 → LM8_LIE_APPROXIMATIONS, LM6 → LM6_POINTS_AS_SECTIONS,
    SECTIONS → SECTIONS_OVER_Q, LM1 → LM1_GROUP_SCHEMES_rerun_20261112, LM2, LM5.
  - Keep LM7 → LM7_PUSH, which is how the runs cite E.65, E.58 and D.50. LM7_FERMAT_TOWER has the same ids.
- `CROSS_RUN_EDGES.tsv` has the 149 resolved edges of the scope. Sweep 0 has 19.
- How sure: high.

**13. Refuted rows hold two kinds of statement.**
- The two kinds:
  - the refuted claim (for example EXIT_ONE_TYPE P1b2, LM5 F.6);
  - the true refutation or counterexample. This is most of them ("X is false", "X fails"), and some are phrased
    positively: LM2 C.a9 "the family doubted on scan 524 exists over Q", LM1 D.12, LM8_LIE E.4 and G.6.
- The counts: by a word test, about 136 of the scope's 179 Refuted rows read as the refutation and about 43 as the claim.
- What follows: sweep 0's flag "proved item cites a refuted row" is a false alarm in all 83 cases of the scope. Each
  one uses the refutation or the corrected form (`FLAG_VERDICTS.tsv`).
- The fix: give the register a column "statement_is" (claim or refutation). In the handbook, each Refuted row becomes
  two items: the claim, refuted, with the tag of the refined item; and the counter-statement, proved.
- How sure: high on the pattern; the verdicts rest on the statements, not on the proofs.

**14. Proved rows that also carry an open part.**
- The rows:
  - DELTA_ON_GT A.43 ("comparison remains open");
  - DELTA_ON_GT A.103 ("the vanishing assertions remain open"; they are now GT_TOWER_CHECK A.5.2, whose e₃ = 0 comes from
    A.7, not by an independent route);
  - LM4_SUCCESSOR B.70 (M₅ = N₅ open) and B.79 (the normalization condition);
  - LM2 B.s4.2 (the PSL₂(F₇) arithmetic image);
  - LM8_LIE A.22 (no lift to the full free profinite group).
- The fix: split each into a proved item and an open item.
- How sure: high.

**15. What the runs call "refereed" or "independent" is in-run.**
- The cases:
  - GT_TOWER_CHECK A.7 and LM4_SUCCESSOR A.24 call LM7_PUSH E.65 "refereed".
  - LM8_PUSH's notes say "Root independent audit passed" (D.22, D.23, D.56). That is the run's own audit, the same model.
- E.65 defines Δ, and everything in item 1 rests on it.
- The fix: record its check events, and keep in-run audits apart from independent checks in the check record.
- How sure: medium. I did not find who refereed E.65.

**16. DELTA_ON_GT's register carries titles only.** All 221 rows were placed by part and id. Their statements are in the
return's `sections/*.tex`, and sweep 2 needs them there.

**17. LM1_GROUP_SCHEMES has no intake, and sixteen of its rows correct the manuscript.**
- What is the case: its register (84 rows) is named by no intake document. Its Refuted rows correct Grothendieck's
  formulas, for example:
  - A.6, the printed trace ordering;
  - C.4, the literal one-relation presentation of scan 336;
  - D.12, the cup product (−3, 3), which is split;
  - E.4–E.7, divided powers and Ga-valued sections.
- The fix: those corrections go into the companion's notes for the cotes concerned, in every language edition. The run
  needs an intake.

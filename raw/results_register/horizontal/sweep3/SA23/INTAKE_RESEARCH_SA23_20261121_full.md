# Full intake of RESEARCH_SA23 (final return), statement by statement

By Claude Opus 5.5 at effort max, agent acadc29d15e8e7c65, 22 Nov 2026. The run is GPT-6 Astra (ChatGPT Pro mode). This
intake was asked for by the coordinator at the user's word (21 Nov, about 23:5x UTC: [the user's words, omitted]).
Check events: `INTAKE_RESEARCH_SA23_20261121_full_CHECK_EVENTS.tsv` (81 rows). My running notes:
`Documents/agent_notes/acadc29d15e8e7c65_NOTES.md`. My earlier intake of this run covered the other 39 rows in full and
the bridges: `INTAKE_RESEARCH_SA23_20261120.md`.

## 0. Scope

- **Return:** `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA23_final_20261120T0511Z_unzipped`,
  sections under `RESEARCH_SA23/sections/`.
- **List:** the 81 ids of `field_experts/INTAKE_LEDGER.md` § 9, row RESEARCH_SA23. All 81 now have a check event; a
  script compared the ids with the list and found nothing missing and nothing extra.
- **What I read:** the statement and proof of every row, in these files, in full:
  - root_A3, algebra_B1, algebra_B2, algebra_C, algebra_D, algebra_G;
  - geometry_E, geometry_F, geometry_K;
  - category_I, category_J, category_L.

  I read cat:L8's proof for its first part and the beginning of the second, which is the classical identification. For
  rows marked "Known" I checked the derivation as written. The cited sources (Stacks, EGA, SGA, Fontaine, Beilinson-Drinfeld,
  Oort, Hall-Rydh, Palais-Terng) I did not reopen; the TSV says so row by row.
- **No scripts.** Every re-derivation was done by hand.

## 1. Counts by check type

| type | rows |
|---|---:|
| targeted proof check, confirmed | 57 |
| refuted, with the refined statement (the run's refutation of a manuscript or printed claim, confirmed by me; refined statement checked) | 12 |
| carried as background without fault found | 12 |

**Gaps: 0. Proved statements of the run that I refuted: 0.**

The 12 confirmed refutations are listed below. I re-derived each counterexample by hand; the refined statement is in
parentheses.
- **C-9:** EGA 0_IV 15.1.19 does not survive the blanket replacement of "regular" by "Koszul-regular" (repair:
  completeness).
- **D-4:** the printed proof of 0_IV 19.3.12 fails (refined statement: D-3, the proposition is true).
- **D-11:** III 4.3.6, K ⊗ Â = K' (the inclusion suffices for unibranch).
- **D-12, D-13:** IV 20.1.3 (locally regular sections; their stalks can be smaller).
- **D-15:** IV 21.2.9, the local reciprocal formula.
- **G-4:** the literal graded-flatness readings.
- **cat:J8:** the literal all-Hodge-Tate category of 161-5/023 (the S_3 obstruction over Q_5).
- **geo-F-augmentation, geo-F-descent, geo-F-infinite:** the natural-bundle extrapolations.
- **geo-Ke-unpolarized:** unpolarized abelian schemes for g ≥ 2.

## 2. Verdicts by part, in short (details in the TSV)

- **A.3 (A-14 to A-19), the general noetherian adic Cohen lifting.** All confirmed. The cotangent complex on adic
  quotients is projective in degree 0 (Neeman's residue-field detection). Ext vanishes with complete finite coefficients
  (Mittag-Leffler). Formal projectivity is preserved (Artin-Rees on the Tor pro-system), and so is the
  projective-quotient form (idempotent lifting, re-derived: e = u + (1-2u)δ). The lift exists, is unique up to
  isomorphism, and has automorphisms Der(B_0, I ⊗ B_0). A-17 is background.
- **B.** The minimal Cohen factorization is Deligne's degree-0/1 condition. The pro-Tor comparison holds for any ideal.
  For every algebraic extension K/k, a transfinite triangular presentation has flat (indeed free) arbitrary Artinian
  lifts. All confirmed.
- **C.** All confirmed: Koszul ⇒ quasi-regular for arbitrary modules; generator invariance; flat and fpqc descent;
  transitivity; the split-conormal converse; Deligne's Sym-Tor characterization (noetherian); the Ext test. The C-9
  counterexample (k[t], t-adic filtration, f = (0, 1-t)) is confirmed with the completeness repair; C-10 is background.
- **D, the letters and the printed EGA statements.** Confirmed: D-1 to D-3 (linear compactness, closed quotients,
  19.3.12 true), D-5, D-7, D-8, D-9, D-14, D-16, D-17. Refutations confirmed: D-4, D-11, D-12, D-13, D-15.
- **E.** geo-E-relative is confirmed: the canonical section of M^{-D} ⊗ (det E)^w, base change, smoothness. The
  exponent of cote 23/006 must be (r+1)(d-1)^r. geo-E-normalization is background, consistent with my hand cases
  (binary quadratic, Fermat cubic).
- **F.** Confirmed: fixed-order natural bundles (in its structure), the categorical version with effective descent,
  and finite order under formal locality. Refutations confirmed: augmentation (two A^1 actions over F_2), descent
  (O(-2) on P^1), infinite order (t ↦ t + t^{n+1}). The Palais-Terng comparison is background.
- **G.** G-1 and G-3 confirmed; the G-4 counterexamples confirmed.
- **I.** All confirmed: I1, I3, I5, I6, I7, I8, I9, I11, I12. The I9 counterexample at κ = ℵ_1, μ = ℵ_ω was re-derived.
- **J.** Confirmed: J1, J2, J4, J6 and J7, the last with a nice determinant-line argument for subobjects. The J8
  obstruction is confirmed. J5 and J9 are background.
- **K.** Confirmed: Ka, Kf, Kg (with H¹(α_p) = R/R^p) and Kh (splitting on P^1, relative patching). Kj is confirmed from
  the cited cube theorem. The Ke-unpolarized refutation is confirmed: the tangent dimension g(g+1)/2 < g². Kb-HilbPic,
  Kb-dual, Kd and Ki are background.
- **L.** Confirmed: L1 (d² is an even derivation; the counterexample to the weaker condition re-derived), L2, L4, L6,
  L7 (the homotopy dι + ιd = N) and L8 (first part). L5 is background.

## 3. Errata (for our EGA editions and the archive)

Each of these was confirmed in this intake or in the earlier one:
- **EGA 0_IV 19.3.12.** The statement is true and the printed proof is wrong (D-3, D-4). Err_IV 8 deletes it; the run
  repairs the proof by linear compactness and closed powers.
- **EGA 0_IV 15.1.19.** The Koszul replacement needs completeness (C-9).
- **EGA 0_IV 20.4.6.** The sign must be d = p_2 - p_1. The first clause of Err_IV 12 is itself reversed; that is the
  run's reading of the print, and I did not reopen it (D-7).
- **EGA 0_IV 20.4.13(iv).** Normality is redundant (D-8; already in Err_IV 14, as the run cites).
- **EGA III 4.3.6.** K ⊗ Â ≠ K' in general; the conclusion holds (D-11).
- **EGA IV 19.5.6(ii).** It is false for nonhomogeneous generators. The counterexample ((1-x)y, (1-x)z, x) is from my
  intake of 20 Nov (D-6).
- **EGA IV 20.1.3, 20.1.4, 20.1.8, 20.1.11, 21.1.5-21.1.6.** Locally regular sections; the corrected meromorphic sheaf
  (D-12, D-13, D-14).
- **EGA IV 21.2.9 and IV 21.6.2.** The local formula is multiplication (D-15); a typeface correction (D-16).
- **Cote 23/006.** The discriminant exponent is (r+1)(d-1)^r (geo-E-relative).
- **Cotes 161-2/055 and 060, 161-5/023, and 23/040.** The scope corrections recorded in the I, J and F rows.

## 4. What is new

The run claims no priority. Its source log reports no prior source for the following, and I take that report as it
stands:
- the repair of 0_IV 19.3.12;
- the general nonlocal noetherian adic Cohen lifting (A-16);
- the transfinite triangular presentation with flat Artinian lifts (B2-2);
- the explicit counterexamples to IV 20.1.3 (D-12, D-13) and III 4.3.6 (D-11);
- the S_3 obstruction to the literal all-Hodge-Tate category (cat:J8).

The rest is known mathematics, checked and placed against the archive's statements.

## 5. Hexagon readiness (the five tests of `field_experts/HEXAGON_CANDIDATES.md`)

- **"Corrections to EGA: counterexamples and repairs".** The items are D-3/D-4, D-6, D-11, D-12, D-13 and D-15, with
  C-9.
  - Test 1 (complete): met; every step is written.
  - Test 3 (stable): met as far as I know; no successor of this run is planned in these files.
  - Test 5 (of interest now): good for EGA readers.
  - Test 2 (self-contained): one gate. The EGA locators are the run's, not reopened by me; a check of the printed
    pages is needed.
  - Test 4 (checked): one gate. My checks are targeted checks whose counterexamples I re-derived by hand. A recorded
    independent re-proof or computation by a second checker, for example a script over the finite examples, is still
    missing.
  - **Verdict: candidate, two gates (2 and 4).**
- **The Hilbert-space trace formula in Grothendieck's hand.** This comes from my intake of 20 Nov (H rows), with the
  struck sheets 1/79-80 and 1/111-112, announced in print in 1951 and 1955 without proof.
  - Tests 1 and 4 are met: the run's proof and my targeted check, plus my independent sweep-3 reading of the same
    sheets.
  - Test 3 is met for the mathematics. The date of the sheets is open, and the note must not depend on it.
  - Test 5 is strong for the archive line.
  - **Verdict: one gate away (test 2).** The 1951 CR note, the memoir II-13 and the 1956 Erratum are cited by the run
    with exact locators that I have not opened. Under the no-priority rule, the note states the facts only (printed
    announcement, manuscript proof), without arguing priority.
- **No other row passes.** The rest is known mathematics, or scope corrections of manuscript readings.

## 6. For a successor prompt

The rows of this intake need no new mathematics. What remains:
- the printed-page check of the EGA errata (Hexagon test 2);
- a computation certificate for the finite counterexamples (test 4);
- the cote 1 dating gate from my earlier intake.

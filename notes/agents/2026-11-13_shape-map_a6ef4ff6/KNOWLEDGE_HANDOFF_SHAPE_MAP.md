# Knowledge handoff: the shape map

Written 13 November 2026, 03:41 UTC (machine clock), by Claude Fable 5.2 (effort medium, no sub-agents), the agent
that wrote the blind map and revisions 1, 1a, 1b and 2. For a successor who continues the work without my context.

## Where the work is

- `braindump_board/SHAPE_MAP_BLIND_FABLE_20261113.md`: the blind map (S1–S7, partial features, carry-overs 1–7). Do
  not change it.
- `braindump_board/SHAPE_MAP_REVISION_20261113.md`: revision 1 (NS from the LaTeX; the user's notes a–f), 1a (the
  vacuum-gravity lessons), 1b (later hunches, Grothendieck's own statements), 2 (open items pushed; eight new
  connections).
- `braindump_board/cards/shape-map-finite-to-limit.md`: the method, the user's words, the sources located.
- Scratch scripts of revision 2 (not preserved elsewhere):
  `C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\9fc52c26-b302-4eb7-b4c2-be7f7bbafcc9\scratchpad\rev2.py`
  and
  `C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\9fc52c26-b302-4eb7-b4c2-be7f7bbafcc9\scratchpad\rev2b.py`.
  Copy them next to the map if they are to be kept.

## Status of everything

No proof in any source was checked. "Proved here" in the revisions means a short argument or an exact computation
written or run by me, checked by nobody.

## What was read, and how far

| Source | Where | Read |
|---|---|---|
| OpenAI ETH paper | `openai/math`, `preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf` | abstract, Thm 1.1, §1.1, §2.1–2.4 |
| OpenAI local smoothing | `openai/math`, `preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf` | abstract, Thms 1.1–1.2, §1.3–1.4, §2.1 opening, Lemma 6.1, Remark 6.2 |
| Yang–Mills | kitp.ucsb.edu `YM_working_group.pdf` | in full; a custody statement, no mathematics; the proof is unreleased |
| Navier–Stokes | `KokunoYumeto/yang-mills-interacting-workbench`, `navier-stokes/` | reconstruction pp. 1–6, §3 outline, Thm 3.1, Props 9.3–9.6 (statements, 9.5 proof), Lemma 10.2; READMEs; `infinite_status.tex` in full |
| GR-VAC lessons | `KokunoYumeto/open-math-courses`, `courses/GR-VAC/` | A §§1–2, 7; B §§1, 6, 7, 8, 10, Ex. 5 |
| Andrews–Connes–La Gatta | `research_maps_20261112/CONNES_CONSANI_CFT/papers/2611.13129/src/prolate-weil-fine15.tex` | abstract, intro, Hypothesis LA, Fact and Table `tab:logbound`, Thm `thm:condpos` |
| Connes–Consani 2501.06560 | `Free or receipted/free/arxiv-eprints-shape-20261113/cc_2501.06560/arxiv-pisa.tex` | lines 404–418, `ramiprop`, `ramicor`, `archimedeanplace` |
| Perelman | same folder, `perelman_math0211159/src.tex` | §3, statement of 10.1 |
| S^6 | `s6_workbench_repo_20261112/README.md`, `survey_20261112/FINDINGS.md` (F1–F10), `s6_pro_prompts_20261112_work/reviews/` (FINDINGS, first half of ROUTES) | as listed |
| Returns | `longue_marche_pro_pilot_20261104/answers/` (LM7, EXIT_ONE_TYPE, FLAGGED_149, CYCLOTOMIC_KERNEL), TOTEX2 checkpoint | every CSV row; of the proofs only LM7 `sections/E_completed_pairs.tex` (E.32) |
| La Longue Marche | `KokunoYumeto/grothendieck-longue-marche`, `reader/LaLongueMarche_English.tex` | keyword search; passages at cote 140-4 scans 24, 172–175; cote 140-2 scans 72, 378; §19 opening |
| Archive returns | `grothendieck_archive_transcription_20261110/returns/` | keyword search; cote 147 scan 104 |
| Zeta workbench | `KokunoYumeto/zeta-function-research-reader`, `satellites/13_cue_mellin_complete_programme_audit.tex` | Thm `thm:cueM-U3-trace-descent` (statement), Prop. `prop:cueM-Psi2-not-SOS` |
| v35 | `Papors/Chatnotes/Soc/Arithmetic_Time_CPT_Spectral_Packets_v35_integrated_replacement.tex` | lines 7512–7572, 8008–8090 |
| Lehner–Pretorius 1006.5960 | arXiv PDF | abstract, Table I, the passages on generations |
| Abstract only | arXiv | 1807.04422, hep-th/0411114, 1909.10355, 2206.10780 |

Everything else cited in the revisions (Milne, Brown, Brown–Schnetz, Conway–Sloane, Cheng–Duncan–Harvey, Balaban,
Bost–Connes, Connes–Marcolli's book, Casini–Huerta–Myers, Kapustin–Sopenko, Myers–Sinha, Henningson–Skenderis,
Tseytlin, Penington, AEMM, Connes math/9811068, Connes–Consani 2004.08879, Grover–Mezzadri–Simm) was **not opened**;
what is said about it is from general knowledge and is marked so.

## What is established (at the level stated above)

1. S1: every item has a scale with a tractable end; the completed ones have a bound uniform in the scale, each open
   item lacks one. NS (OpenAI): residual order 1/5 + j/10 against a loss K_m independent of the stage. The user's
   continuation: explicit cost λ_q^{9/8} per layer for unchanged fields.
2. E.32 of LM7 is a lim¹ class (Jannsen's sequence), arising because v₃(q − 1) is unbounded; equivalently a telescope
   class one degree up. The tame relation is the scaling action; H² is the coinvariants of (q − 1) on restricted
   sequences.
3. Grothendieck states the layer-by-layer programme himself (cote 140-4, scans 172–175) and identifies a
   discretification with an archimedean valuation (cote 140-2, scan 378). Pentagon, hexagon and Lego are not in La
   Longue Marche.
4. E.25's class κ₂(−1) ∪ κ₂(−1) is the quaternion class (−1,−1) with non-zero invariant at ∞; κ₂(−1) is a
   Connes–Consani cover with one point over C_∞.
5. Ψ₂^♯ is negative at (u,v) = (4,0), (3,0), (0,−1), all outside the image of the cover (w < 0 or v < 0); exact values
   −217/24, −13/6, −97/24. The sum-of-squares obstruction is in degree zero and is not of E.32's kind.
6. Tate construction: Cone(M_{hG} → M^{hG}) is self-dual up to the shift [−1]; this is v35's boundary-defect duality
   with Z = {∞} and gives Tate duality Ĥ^r(G,M)^∨ ≅ Ĥ^{−r−1}(G,M^∨).
7. H₂(Δ₀,₆): f-vector (25,105,105); as a module over the standard S₅ (the stabilizer of a marked point) its character
   equals that of Ind from F₂₀ of the 4-dimensional module (24; −1 on 5-cycles; 0 elsewhere), exact check. Over the
   transitive PGL₂(5) ⊂ S₆ it does not (−8 on fixed-point-free involutions, 3 on type (3,3), 1 on 6-cycles). The
   cycle lattice in Z¹⁰⁵ has determinant 5⁸·11¹⁰·13⁵ (using EXIT P4d2's statement that the Smith form is trivial).
8. The driven energy identity for (S38): with zero initial data the total work at the wall equals the energy, so it
   is non-negative; the instantaneous work has no sign.
9. The Proj¹ formulation of the force budget is vacuous: restriction maps of smooth functions are surjective.
10. Table `tab:logbound` cannot test a lower bound (its entries are upper bounds), and its first column is not
    monotone.
11. E.32's witness z = (q_j − 1) lies in the 3-adic closure of the image of d and not in the image. So the class is a
    "closure of the image modulo the image" class: d = diag(q − 1) is injective with no gap (inf |q − 1|₃ = 0). This is
    the common form found in revision 2 for E.32, a gapless limit of gapped finite systems, the closing of ε_λ, and
    approximately inner automorphisms modulo inner ones.
12. Lehner–Pretorius Table I: string radii 0.148, 0.05, 0.02 at times 203.1, 223, 227: a roughly fixed ratio per
    generation, unlike the Alpöge–Buckmaster layers λ_q = λ_{q−1}^{Q_q}.

## Revision 3 (13 November 2026, 12:39 UTC): four new returns, none refereed

Read: TOTAL_EXACT_2's final message
(`derivateurs_companion_20261109/pro_prompts_max_20261112_work/TOTAL_EXACT_2/RETURN_TEXT_20261113.md`, §§1–2 and the
tables); the reports of LM8 checkpoint 16 (matrix head, sections E, F, G), LM7_PUSH checkpoint 04 (lead table,
"Derived limits") and LM4 (table head), all under `longue_marche_pro_pilot_20261104/answers/`. Reports only, no
proofs. `pro_intake_20261113/IMPLICATIONS.md` did not exist yet.

Claimed by the returns, and what the map takes from them:
- Total does not imply exact: the category C_δ, T₁(Q_R) ≅ R over every non-zero ring. The blind map's TOTEX2 row and
  carry-over 7 are superseded.
- The closure(im d)/im d form of revision 2, B2, appears again in LM8 F.21 (prime 5) and LM7_PUSH A.1–A.4, and
  LM7_PUSH states the criterion: the Milnor term vanishes exactly when the Smith valuations are bounded. The class is
  invisible to cardinalities, survives finite extensions, and cannot be evaluated from finite data.
- Compact towers have no lim¹ (LM8 F.15). So S7's wall (section surjectivity for P¹ minus three points) is not a lim¹
  phenomenon; the candidate is the kernel of the map to the product of the maximal pro-p quotients (LM8 A.22, G;
  LM4 D.29, D.30).
- Five frameworks: derived colimit; derived limit; the Galois part against the full topos; pro-p against profinite;
  integral against rational. The table is in Revision 3, (b).
- A discrepancy to settle: the brief said LM4's full profinite compatibility is open; the report's table says full
  profinite recognition is refuted.
- Tests proposed first: exactness as a Ramsey property (three small categories); the mixed-prime form of the section
  statement; the referee's check of the bounded-valuation criterion.

## What is open (the statements are in the revisions)

- A canonical map from the cosmic Galois group to the motivic Galois group of MT(Z); a coefficient version of
  Connes–Consani's covers for non-abelian Galois modules (E.18).
- A Perelman-type monotone for: Hypothesis LA; the all-stage force budget; TOTEX2 C.9; CYCLOTOMIC E3.
- A category in which E.32's residue complex has a determinant.
- "One class from a D+1 invertible theory" across the cases: holds in part for E.32 and for crossed products, fails
  for sums of squares, unformulated elsewhere.
- Whether H₂(Δ₀,₆) with any natural form is a step in a holy construction: no evidence; the determinant found is not
  that of a Niemeier lattice or of A₄⁶ (5⁶).
- The items of Revision 2, part B, marked open there.

## Not done, by instruction or by budget

- Aligning v35's Part on anomaly inflow with the literature (a separate run, waiting for the user's word).
- Lifting the Andrews–Connes–La Gatta uncertainty principle to each item (recorded for later).
- The proofs of the returns (only E.32's was read).
- NS reconstruction §§4–8 and appendices.

## Cautions for the successor

- The user asked that the hunches be treated as hunches; mark them known, new and proved, new and open, or wrong,
  case by case, and never mark something known because a special case is known.
- Say when a statement rests on an abstract or on a paper not opened.
- Two symbols collide: OpenAI's q (similarity parameter) and the lesson's q = kρ_c.

## Next round (user, 13 Nov 2026, P4082)
- B4 redirected. Compare the Landau–Widom plunge region with the spectral action: Tr f(D/Λ) and its cutoff transition
  (Chamseddine–Connes, The Spectral Action Principle, hep-th/9606001); the almost-commutative Standard Model spectrum
  (hep-th/0610241); the prolate operator and ζ (Connes–Moscovici 2112.05500); spectral triples and ζ-cycles
  (Connes–Consani 2106.01715). This replaces the islands comparison.
- The object is the closing gap of B2/B3, not positivity: E.32, the lattice gap, ε_λ (rate e^{−4πλ²}, Hypothesis LA),
  and the infinite-chain anomalies.
- Infinity points in a direction (user, P4087). Choosing a point at infinity breaks a symmetry spontaneously to the
  stabilizer of a direction, and the broken part acts by scaling. Instances: KMS states and boosts (Ojima 1986;
  Bisognano–Wichmann); Bost–Connes for β > 1 (extremal states ↔ embeddings Q^ab → C); tangential base points at a
  cusp, with Galois acting through the cyclotomic character (Grothendieck §9; Ker χ at cote 140-4); E.25 at the real
  place. To work out: is this the common reason the closing-gap obstructions live at ∞?

## Revision 4 (13 November 2026, 13:54–14:02 UTC, machine clock): the successor at effort high

Written by Claude Fable 5.2 (effort high, no sub-agents), the successor of the scouting agent. Revision 4 is appended
to `SHAPE_MAP_REVISION_20261113.md` (from its line 969). Its section 1 lists everything opened, source by source.

### What governs
- The user's own statements of the conjecture (session transcript, 13 Nov, 13:38–13:46 UTC), not paraphrases of
  them. In short: a potential resolution "shaped like anomaly inflow", an obstruction "shaped like Poincaré
  invariance violation", discrete and smooth meeting "through infinity"; D+1 means the resolution of a 't Hooft
  anomaly; step 1 is to make the obstruction precise in each problem; it is "the suspicion, not the claim"; "I'm not
  saying everything is anomaly inflow." Revision 4 quotes them at its head.
- To reread them: the transcript is
  `C:\Users\user\.claude\projects\C--Users-user-Documents\9fc52c26-b302-4eb7-b4c2-be7f7bbafcc9.jsonl` (40 MB; do
  not read it whole). The streaming extractor is in the session scratchpad:
  `C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\9fc52c26-b302-4eb7-b4c2-be7f7bbafcc9\scratchpad\extract_tail.py`
  (start marker "The G+1 statement is likely the most far-fetched").

### Where things are
- E-prints (TeX) of 33 cited papers: `C:\Users\user\Documents\Free or receipted\free\arxiv-eprints-shape-20261113\ep_<id>\src\`.
- The Yang–Mills documents: the same folder, `kitp_ym\` (the October statement, the statement of 3 November, the
  assessment of 10 November as PDF and as text `a1.txt`).
- The conference: `C:\Users\user\Documents\expert_conference_20261113\` (talks, replies). The scouting agent is a
  participant there; its round-2 reply amends the central statement and I adopted the amendments.
- The file as it was before Revision 4:
  `C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\9fc52c26-b302-4eb7-b4c2-be7f7bbafcc9\scratchpad\SHAPE_MAP_REVISION_before_rev4.md`.

### What Revision 4 established, and at what level
1. **Read with the proof, no gap found (not a referee's check):** LM7_PUSH F.1–F.3 (the bounded-valuation
   criterion), F.4, C.7; LM8 F.15.
2. **Proved here (short arguments, checked by nobody):**
   - lim¹ H¹(G_L, M/ℓⁿ) = 0 iff G_L acts on M(−1) through a finite group (from F.3 and Chebotarev);
   - L1: an automorphism of prime order p in the index kills F_p-exactness; L2: EPPA gives rational affine
     equalizers; L3: the age of finite linear orders with an equivalence relation is not exact over Z (a parity
     argument on two arrows);
   - a tower is a sheaf on N ∪ {∞} and lim¹ is H¹ of the boundary defect i*Rj_* at ∞;
   - H²(G_Q, M_n) = H¹(Γ, H¹(G_{Q(μ_{3^∞})}, M_n)) for finite 3-primary M_n (from Serre's cd ≤ 1, not opened);
   - embeddings Q^ab → C, generators of Ẑ(1) and Bost–Connes's extremal states (β > 1) are one Ẑ^×-torsor;
   - a section of π₁ → G_k is a lift of the outer Galois action to an action (S7 in 't Hooft form).
3. **Checked in sources:** the definition of an anomalous theory as a relative theory (Freed–Teleman, FHLT); the
   classification theorem of Freed–Hopkins; Kapustin–Sopenko's index (B7's candidate holds); KPT; Moore;
   Evans–Hubička–Nešetřil 1801.01165; Brown; Connes–Marcolli; Brown–Schnetz; Cheng–Duncan–Harvey; Tseytlin;
   Bakalov–Kirillov; Witten and CLPW (abstracts); Van Raamsdonk and Maldacena–Susskind; GKKS; Kim.
4. **Corrections to earlier revisions and to the card:** Revision 3's "S7 is not of framework 2" (the lim¹ is in the
   coefficient tower of every nilpotency layer); Revision 2's "it fails for φ⁴" (Brown–Schnetz prove a point-count
   statement, not that the period is not a multiple zeta value); the card's Z[i][1/2] (Connes–Marcolli: N = 3 or 4,
   non-canonical, with their own caution); the card's wording of Bakalov–Kirillov; Revision 3's citation of EHN.
5. **Yang–Mills.** Three committee documents exist; the assessment of 10 November has the mathematics. It reports:
   an ultraviolet limit at fixed volume by a Balaban-type renormalization group; an infinite-volume limit only
   along subsequences; a decomposition into component theories; Euclidean invariance in three steps, the last being
   that the symmetry is not spontaneously broken because the stress-energy flux decays at infinity; a non-zero
   trace anomaly; open: uniqueness, a mass gap, Wilson loops. The obstruction half of the user's conjecture is the
   committee's own account there. The summary reports no object one dimension up. GKKS's mixed anomaly at θ = π was
   checked in the source; its inflow action there is for the circle reduction; a five-dimensional form was not
   found in that paper by text search.
6. **The pattern (Revision 4, section 6).** Four kinds of obstruction: A, a phantom class closure(im)/im along a
   one-parameter direction acting without a gap; B, a robust class of a non-directed index with a non-amenable
   group; C, degree zero (a non-final family, another sector); D, honest finite-level classes. The conjecture has
   instances in A and B and in the home field, and none in C by the routes checked.

### What is open (statements in Revision 4)
- The limit form of the cyclotomic descent: the phantom group as the non-Hausdorff part of the Γ-coinvariants.
- Exactness against Ramsey and amenability: items (a)–(e) of test 1.
- The mixed-prime section statements M0 and M1.
- The mass gap as Hausdorffness of H¹ of time translations (Guichardet's criterion must be opened).
- A Ramsey expansion as the absorbing object for C_δ.
- Everything Revisions 1–3 left open on Weil positivity, the Navier–Stokes budget and the sum-of-squares row.

### Tests, in order
1. FRAISSE_EXACT (candidate GPT-6 Astra prompt). 2. The mixed-prime section statement (candidate prompt, LM8_PUSH).
3. The referee's check of F.1–F.3 with the corollary, then the descent form (prompt item for the successor of
LM7_PUSH). 4. The regimes as one statement. 5. Yang–Mills readings T-YM-1 to T-YM-4 (ours). 6–8. Three small
checks of ours. No prompt was written; any prompt drawn from these goes through
`claude_tools/push_rule_pro_prompts.py` first.

### Not done
- Part II of the Yang–Mills assessment, the Lean source and the 278-page draft manuscript.
- The sources named "not opened" in Revision 4, section 1. Nothing was reopened of Perelman, Navier–Stokes, GR-VAC,
  Andrews–Connes–La Gatta, the zeta workbench, S⁶, Lehner–Pretorius, v35 and *La Longue Marche*.
- The proofs of TOTAL_EXACT_2, LM8 F.21, LM4 and LM7's new rows (statements, reports and the intake only).
- Step 0 for v35 (its alignment with the literature) is still waiting.

### Cautions
- "Proved here" items have no second reader. L3 and the corollary of F.3 are the ones other work would lean on.
- Moore's theorem is for Fraïssé structures with all embeddings; for C_δ the morphisms are closed embeddings.
- The clock: the machine's UTC clock read 13:54 when Revision 4 was started; the card's times for the same afternoon
  are given as "~16:5x" and "~17:0x". Check the clock before writing timestamps.
- Context of the writer at the end: about 350K tokens by its own estimate (no meter available), under the bound.

### Conference, round 3 (13 November 2026, 14:11-14:20 UTC, machine clock): the joint drafts
- The Revision 4 agent drafted, in `C:\Users\user\Documents\expert_conference_20261113\joint\`:
  COMBINED_IMPLICATIONS.md, OPEN_DISAGREEMENTS.md and PROMPT_ITEMS.md. They await the participants' sign-off.
- Read for them: the talks, the replies, the five floor questions and the three floor answers present at 14:17 UTC
  (the intake on Q3; the EXIT reviewer on Q2; the LM7 reviewer on Q2 and Q3). No answers existed yet for
  Derivateurs_expert_Q1, intake_Q1 and shape_map_Q1.
- What the round changed for the map: the pro-p against profinite row has both forms, on different objects (degree
  zero for automorphisms; a twisted H^1 for sections, at order 75 it is H^1(G_Q, E_c[5]) for cubic twists of the
  j = 0 curve; the intake's computation, no second reader). E.11 is first-derived on the models of the stages and
  Mittag-Leffler on their invariants. The Derivateurs successor reports the main proofs of TOTAL_EXACT_2 read at
  effort max and correct. LM4 D.63-D.65: in type (1,1) the centralizers of the standard negative involutions have
  multipliers 1 and -1 only.
- FRAISSE_EXACT is drafted by the Derivateurs successor (not sent); PROMPT_ITEMS.md lists six additions for it.

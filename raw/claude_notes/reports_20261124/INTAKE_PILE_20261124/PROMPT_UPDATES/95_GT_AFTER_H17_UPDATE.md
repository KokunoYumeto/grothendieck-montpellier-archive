# Prompt 95_GT_AFTER_H17: update of 24 Nov 2026

By Claude Opus 5.5 at effort max (the Galois/anabelian connection mapper, agent of the main session 329fb1e6), 24 Nov
2026, about 22:20–22:35 UTC, following `../PROMPT_UPDATE_BRIEF.md` and the main session's message. Work file:
`<local>/Documents\agent_notes\20261124T2142Z_Connection_map_Galois_and_anabelian_NOTES.md`.

## State before the change

- Not sent: `TO_SEND/PRO/SENT_PRO.tsv` has no row for 95 or GT_AFTER_H17; the folder was not under a SENT folder.
- Backup: `TO_SEND/PRO/_backups_20261125/95_GT_AFTER_H17/`: the original PROMPT.md and ZIP (23 Nov 19:48), the original
  spec and plan (`spec_before/`), the original send folder moved whole (`send_folder_before_moved/`), and my first rebuild
  (`placed_first_rebuild_2228UTC/`, superseded by the final build below).
- Builder-built: `pro_prompt_builds/PAPERS_20261122/specs/95_GT_AFTER_H17.md` and `.plan.json`, edited; built and placed
  with `build_papers.py 95` and `--place 95`.

## Placed

`TO_SEND/PRO/1_Archive_research_by_topic/95_GT_AFTER_H17/`: PROMPT.md (4,625 words, SHA256 prefix 4d8ec86c0b9f2aa1) and
`95_GT_AFTER_H17.zip` (791 files, 4.2 MB, SHA256 prefix e5a20a8e9d87e44e, no ZIP inside). The H17 note itself was not
changed (its v2 is a49aabbf's job); the prompt cites it and names its correction.

## Lints

- Builder: `95_GT_AFTER_H17 | files 791 | not attached 0 | ZIP 4.2 MB | prompt 4625 words | lints PASS`.
- `push_rule_pro_prompts.py --lint-math PROMPT.md`: 1 file, 0 failing.
- `paper_completeness_lint.py PROMPT.md`: ok, 0 failing.

## Changes, with evidence

1. **PUSH line and main question (item 1) re-aimed.** Old: decide for each quadratic character vanishing on GT̂ whether it
   comes from Λ₀ or from the gap. That sorts nothing: every such character vanishes on GT̂ ⊇ Λ₀ (map N4(c),
   `MAP_GALOIS_ANABELIAN.md` §N4; found independently by the Longue Marche prompt updater,
   `LONGUE_MARCHE_PROPOSALS_AND_95.md` §1.1). New: compute H¹(Λ₀, F₂)^(GT̂) and its restriction to G_(K₂) = Λ₀ ∩ G_Q, whose
   kernel is Hom(GT̂/⟨⟨G_Q⟩⟩, F₂), and decide whether that kernel is zero; then F_p. This is the F₂-part of Lochak–Schneps
   2006 Question 1.2 (opened: author PDF `textes/farb.pdf`, §1, "is the abelianization of GT̂ obtained, like that of G_Q
   ... by the map (λ, f) ↦ λ?"), now attached; Question 1.3 is named as concerning the same group ker λ = Λ₀·G_(Q^ab).
2. **New background R1 (map N1)**: Lochak 2025, Algebra i Analiz 37:2 (Def. 5.4, Prop.–Def. 5.6, Prop. 5.9, Thm 5.10, pp.
   61–62; author PDF opened, PyMuPDF text with the asterisks of Out*), with the combination IΓs = IΓ = GT̂ and
   Out*(Γ̌_{g,[n]}) ≅ GT̂; check state "proved on paper by Claude Opus 5.5 at effort max, unchecked". No arXiv version of
   Lochak 2025 was found (search of 24 Nov), so the author PDF is attached. EXIT_TOWER E.43–E.44 attached and credited.
3. **New item 2 (the gates of N1)**: (a) Lochak's use of Boggi–Funar (arXiv:2004.04135) against EXIT_TOWER E.14
   (`EXIT_TOWER_results.csv` row E.14: identity (E.26) in the proof of BF2026 Lemma 2.23 false as printed); (b) r_{g,n} =
   Lochak's lego action; (c) Out^{I₀} vs Out* for g ≥ 3, deciding E.45, with Boggi arXiv:2011.15075v6 compared;
   (d) Lochak p. 61's inclusion of IΓs in Nakamura–Schneps's group and relation (III′) on GT̂ (Furusho, RIMS 1267, p. 190,
   gives (III′); attached as PDF, no source).
4. **New background R2 (map N4)** and R3 (map N5), with their check states (paper proofs, unchecked; R3's identity
   a_n = dim W_n is a computation, `MAP_GALOIS_ANABELIAN_scripts/c34_an.py`).
5. **New item 3 (strictness GT̂ ⊊ GT̂₀)**: no printed proof (Dolgushev–Guynee arXiv:2401.06870 p. 2 "obviously contains";
   topicality pass, `TOPICALITY_LONGUE_MARCHE.md` item 3, "pending a referee pass"); the run must write the full proof:
   LM8_PUSH P.2–P.4, C.30, C.32, an independent rerun of C.35's certificate, and SECTION_GHOSTS E.198's witness.
6. **New item 4 (mod-17 pentagon in weight 16)**: compute W₁₆/[W, W]₁₆ (C.34's lower bound d₁₆ = 37), the F₁₇-rank of the
   linearized pentagon on it, the resulting characters vanishing on GT̂, then every p ≥ 17 in weight p − 1.
7. **New item 5 (gentle monoid)**: the analogue for GT̂₀ of LM4_SUCCESSOR C.31 (Dolgushev–Guynee Definition 2.5).
8. **Background on the GT monoid** (topicality item 1): LM4_SUCCESSOR C.29–C.31 answer Lochak–Schneps 2006 Q1.1; check state
   from the LONGUE_MARCHE_A reader (Claude Opus 5.5 at effort high, 24 Nov); `C_further.tex` extracted from
   `historical_data.tar` (member `LM4_SUCCESSOR/work_CE/C_further.tex`) and attached; BHR arXiv:1703.05143 attached for
   C.31's inputs.
9. **Correction stated in the prompt**: H17 line 158 ("The inclusion GT̂ ⊊ GT̂₀ itself is known") has no printed source;
   the note does not cite Lochak 2025.
10. **Item 7 (old 3) refined**: H17 Corollary 4 and RECORDS §1 already cover a Δ equal to δ on Λ₀; the run now decides
    whether LM7_PUSH E.65's Δ restricts to δ on Λ₀, and names E.58's sign normalization (LM8_PUSH C.46: 5I against I).
    Items 6, 8, 9 are the old items 2, 4, 5, unchanged.
11. **Attached** (plan.json): LM8_PUSH `C.tex`, `P.tex`, results, the `pbc_*` scripts of C.33–C.36; LM2 `B_graded.tex`;
    EXIT_TOWER E.43–E.44 TeX and results; GT_TOWER_CHECK part A cm/centralizers, part B descent characters/proofs,
    results; SECTION_GHOSTS E.195, E.198; the map, its TSV and check events, the C.34 script; TOPICALITY_LONGUE_MARCHE.md.
    E-prints (LaTeX, fetched by the builder): 2004.04135, 2011.15075, 2602.12462, 2401.06870, 2406.08639, math/0702128,
    1102.1312, 1703.05143. PDFs where no source exists: Lochak 2025, Lochak–Schneps 2006, Furusho RIMS 1267 (2002).

One claim in `LONGUE_MARCHE_PROPOSALS_AND_95.md` §1.1 is not right: it calls 95's "LM8_PUSH C.30" an id slip. C.30's
statement (`LM8_PUSH_checkpoint_17.../sections/C.tex` l. 2650–2670, read on 24 Nov) is exactly the ℵ₀-dimensional family of
quadratic characters θ_p (p ≡ 5 mod 12) of GT̂₀ vanishing on GT̂; the id stands.

## Proposals (findings for which 95 is not the place)

- **N2 (tripod sections over Q; map §N2).** The check part (Proposition L's proof, and SECTIONS_OVER_Q A.14 against Pan
  2022 Thm 1.0.4 and Helm–Voloch 2011 Prop. 6) belongs in the waiting, unsent intake prompt
  `TO_SEND/PRO/7_Longue_Marche_intakes/18_Pro_intakes_Longue_Marche_thin_runs/INTAKE_A_ANABELIAN_SECTIONS/`, which covers
  SECTIONS_OVER_Q and SECTION_GHOSTS. The research part deserves its own prompt if the main session wants it:
  - main question: SECTIONS_OVER_Q A.24 in the case left by N2, a noncuspidal Selmer section of P¹ ∖ {0,1,∞} over Q that is
    locally cuspidal at a prime p where E_{λ₀} is potentially multiplicative (λ₀ ∈ U(Z[S⁻¹]), matching ramified Kummer
    data): is it the section of λ₀? First case S = {2, 3} (21 values of λ₀, three non-integral j at 3);
  - why: it is the one remaining step of the Legendre route to Conjecture A of cote 149 (scan 56) inside the finitely
    ramified class; everything else in that class is now a theorem (Stix 2015 Cor. 6 with N2);
  - exists: SECTIONS_OVER_Q cp17 (A.12–A.24, A.32, A.44), SECTION_GHOSTS final, ANABELIAN_149_PUSH D.30–D.31; Stix 2015;
    Betts–Kumpitsch–Lüdtke arXiv:2305.09462v2; Li–Lüdtke arXiv:2608.20615;
  - inputs: those runs' TeX, the map's §N2, the e-prints above, Pan 2022, Helm–Voloch 2011.
- **N3 (the K-group obstruction; map §N3).** No waiting prompt continues SECTION_GHOSTS's (FS)_nil. The statement is short
  and mostly classical; its check fits INTAKE_A_ANABELIAN_SECTIONS as one item (re-prove the identification of the B.25
  obstruction with K_{2r}(Z) ⊗ Z_ℓ and the irregular-weight list). As research it belongs to the (FS)_nil successor, if one
  is built: main question (FS)_nil at an irregular coefficient prime, first ℓ = 37 at classes r ≡ 31 mod 36, where the
  obstruction group is K₆₂(Z)₃₇ ≠ 0.

## Left alone

- The H17 note (a49aabbf's v2 job).
- INTAKE_A_ANABELIAN_SECTIONS: not assigned to me; proposed above.

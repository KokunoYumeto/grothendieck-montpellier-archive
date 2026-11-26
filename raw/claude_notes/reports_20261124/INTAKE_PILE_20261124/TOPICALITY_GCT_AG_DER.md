# Topicality of the GCT, AG_POLISH and DERIVATEURS clusters (24-25 Nov 2026)

Written by Claude Opus 5.5 at effort high, launched by the main session 329fb1e6 (Claude Opus 5.5 at effort max), for the
Fable conference (Claude Fable 5.2) on the intake pile. Brief: `TOPICALITY_BRIEF.md`. Rows: `TOPICALITY_GCT_AG_DER.tsv`
(47 rows). Work file: `<local>/Documents\agent_notes\20261124T2136Z_Topicality_GCT_AG_D_rivateurs_NOTES.md`.
Every run named here is GPT-6 Astra (ChatGPT Pro mode) unless said otherwise.

**How I searched.**
- **Hexagon:** the whole catalogue through its API (1,530 works on 24 Nov), grepped by topic.
- **arXiv:** the API by abstract terms, then the PDFs of the papers I rely on, read at the statement.
- **Web:** standard and extended web searches, logged item by item in the TSV.
- **Literature file:** `LITERATURE_20261124.md`, for 14-24 Nov.

A verdict of STILL NEW means that no source I opened proves the item. The TSV names the queries behind each such
verdict. "Thin" means that only one query was run.

**Two facts in the cluster files are out of date.**
- H09 (DP_MULT) is posted, as hexagon 2611.00938 (23 Nov).
- P90a is at v2 on Hexagon (2611.00936, version 2).

## A. Worth a paper now, ranked by usefulness

1. **Numerical PH3 fails for Kronecker coefficients (GCT_POS K-023, R-NEW-004, K-024, PNEW-013; H02b).**
   - **What.** Σ_s g((sⁿ),(sⁿ),(sⁿ)) tˢ has a pole at a primitive root of unity of order 2ⁿ⁻¹·3ʳ. So the denominators of
     every positive form grow exponentially in n.
   - **Why it matters, and the new finding here.** Mulmuley himself relaxed PH3 in his erratum appendix to
     Briand-Orellana-Rosas (Comput. Complexity 2009, arXiv 0810.3163, pdf lines 823-930). The relaxed form asks only that
     the "modular index", the largest a_i in a minimal positive form, be O(poly(h)), where h is the maximal height. For the
     triple rectangle h = n, and the pole of order 2ⁿ⁻¹ refutes this relaxed form too. So the result refutes the
     hypothesis as Mulmuley himself last stated it, not only the GCT VI wording.
   - **What the paper must do with this.** Cite that appendix, and replace the run's citation of 1.6.7 by 3.3.4 and the
     2009 restatement.
   - **Novelty.** No source I opened refutes either form. Web searches found BOR's SH and PH2 counterexamples, but nothing
     on the modular index. Hexagon has nothing on Kronecker coefficients.
   - **Proof.**
     - `research_returns/GCT_POS_final_20261122T0219Z_unzipped/branches/plethysm/modular_pole_transfer.tex` and the
       kronecker branch;
     - the check is `reports_20261122/gct_pos_ph3_check/CHECK.md`;
     - K-024 carries the unpublished ALPOGE_GCT P-F23, P-F27 and P-F30, which the paper must contain.

2. **Explicit occurrence obstructions for perₙ against detₙ with no padding (GCT_KRON A-030, A-034, O-030, with GCT_OBS
   S-002/S-003; H13).**
   - **What.** For every n ≥ 3 there is an explicit λ in degree n² + 1 that occurs in the coordinate ring of the
     permanent's orbit closure and has Kronecker coefficient zero. Every stretch of λ gives a strict multiplicity gap, and
     O-030 adds a three-parameter family.
   - **Why it matters.** Bürgisser-Ikenmeyer-Panova (1604.06431) rule out occurrence obstructions in the padded setting.
     Bürgisser-Ikenmeyer-Hüttenhain (1501.05528) show that obstructions must be holes of S(Detₙ). An explicit unpadded
     family of holes is exactly the object those papers leave open.
   - **Novelty.** Searches for "occurrence obstructions", "multiplicity obstructions" and "orbit closure of the
     determinant", plus an extended web search, find only the padded impossibility results and other settings (Chow
     varieties, power sums, graphs).
   - **Partly known.** The per₃/det₃ module (19,7,2⁵) in degree 12 is Landsberg-Manivel-Ressayre's (per the run). S-002 and
     S-003 make both of its sides explicit.
   - **Proof.** `GCT_KRON_checkpoint_07_20261121T0415Z_unzipped/GCT_KRON_work/GCT_KRON.tex`, lines 8382 (A-030), 9001-9330
     (A-034) and 9423-9764 (O-030).

3. **A six-arrow monoid with BM ≃ ⋁_{n≥2} Sⁿ, and countability on finite-category tests (S2COUNT A.M1, B:main,
   B:smallcategories, CD:alltargets).** Verdict: PARTLY known, and the new part is the substance.
   - **Known before.** Sweeney (2502.05276 v2, Example 5.2, pdf lines 972-1007) computes the *homology* of the same
     semigroup: Hᵢ = ℤ for i ≥ 2. His Example 5.3 gives the r = 2 homology. He does not determine the homotopy type.
   - **New.**
     - the homotopy type, by explicit sphere maps, for every r;
     - |[BM₁, S²]| = 2^ℵ₀;
     - the minimality of six arrows;
     - the countability criterion CD:alltargets.
   - **Literature since.** None of the following covers it:
     - Martinian-Steinberg 2511.12657 (finite wedges of Moore spaces);
     - Ben-Bassat 2610.38760 (Fiedorowicz's conjecture, 28 Oct 2026);
     - Campos 2611.09718 (minimal acyclic models, 6 Nov 2026).
   - **What the paper must cite.** Sweeney's Examples 5.2-5.3, and Fiedorowicz 1984 for BM ≃ S² of the five-element monoid.
   - **Proof.** `derivateurs_companion_20261109/pro_prompts_max_20261112_work/S2COUNT/S2COUNT_final_20261116T0841Z_unzipped/S2COUNT/sections/`,
     in `A_agent.tex`, `B_root.tex` and `CD_agent.tex` (lines 300-440). The cluster reader followed every step and computed
     the homology.

4. **Exactness of colimits and amenability separate for Fraïssé categories (FREX A.9-A.11, A.17-A.19, A.33, with C.12,
   A.26 and D.9).**
   - **What.** Ordered posets are exact over every ring and non-amenable. Independently ordered F₂-spaces are amenable and
     exact over ℚ, but not over F₂ or ℤ. A₂(ℚ) is exact over every F_p and not over ℚ.
   - **Novelty.** The extended search finds nothing on exactness of colimits against amenability.
   - **The gate before writing.** The nearest theory is Harman-Snowden's measures on Fraïssé classes (Invent. Math. 2026).
     FREX cites it only in its D section. Snowden's "Measures on partial orders" (2609.02021, 2 Sep 2026) classifies the
     measures on posets. It does not treat ordered posets, exactness or amenability (opened and grepped). The paper must
     say whether the signed integer averaging of A.9-A.10 is a ℤ-valued Harman-Snowden measure in disguise. If it is,
     A.11's exactness may follow from their theory, and the separation from amenability remains the new point.
   - **Partly known.** D.9's Ramsey and amenability column rests on Evans-Hubička-Nešetřil.
   - **Proof.** `FRAISSE_EXACT/FREX_final_20261118T1235Z_unzipped/FREX/sections/A.tex`, `C.tex` and `D.tex`. The intake
     (Claude Opus 5.5 at effort max) checked every step.

5. **Four-row multiplicity obstructions under genuine padding (CUE_GCT R-14, with R-13; H14).**
   - **What.** z^{n−m}perₘ against detₙ, for the pairs (8,9) to (16,22).
   - **Novelty.** The literature search for R-14 also covered this item. The literature has multiplicity obstructions only
     for other pairs of varieties (Dörfler-Ikenmeyer-Panova 1901.04576; Ikenmeyer-Kandasamy 1911.03990; Dutta et al.
     2211.07055). It has none for padded per against det.
   - **Gates.**
     - Write the narrow version (m = 8-16) now.
     - R-27 (the exact √2 ceiling) is unread by any intake.
     - The m = 11-16 certificates need recomputing.
   - **Proof.** `CUE_GCT_checkpoint_08_20261121T0649Z_unzipped/deliverables/CUE_GCT.tex`, lines 1238-1360.

6. **Footnote 56 and Corollaire 7.7.2 of Les Dérivateurs XVI: absolute Theorem A does not give relative Theorem A
   (BISITE A.32 → RESIDUE B.2-B.4 → REVLOC F.1, F.1.1 → DER_LOCALIZERS A5.1-A5.4).**
   - **The setting.** Maltsiniotis (*La théorie de l'homotopie de Grothendieck*, Astérisque 301, §1.1 and the
     Introduction, opened) separates two notions:
     - weak fundamental localizers (La, Lb and absolute Theorem A, Lc);
     - fundamental localizers (adding relative Theorem A, LC).

     He records Cisinski's theorem that W_∞ is the smallest of both. His examples 1.1.31-1.1.34 include no class that
     separates them.
   - **What the chain gives.** BISITE A.32 is such a class for the literal axioms. The rest of the chain gives the exact
     dependence on Loc (6′a), (8) and (9).
   - **Novelty.** No source found states it.
   - **Gate.** Open Cisinski 2006 (Astérisque 308), §§4.2 and 6.1, which REVLOC F.1.1 uses as input.
   - **Proof.**
     - BISITE `sections/A.tex:434`;
     - RESIDUE `sections/B.tex:54,138`;
     - REVLOC `sections/F12.tex`;
     - DER_LOCALIZERS `sections/A5.tex`.

     All are checked step by step by the intakes.
   - **Credit.** Use the corrected priority order (P1 in DERIVATEURS.md).

7. **All zeros of plethysm coefficients in outer degree five, with positive polytope formulas in outer degrees four and
   five (GCT_PLETH G-031, G-036, T-037; H20).**
   - **What is already known.**
     - Kahle-Michałek (1408.5708, FoCM) computed *signed* chamberwise quasi-polynomials for |μ| = 3, 4, 5.
     - They name "the zero locus of plethysm coefficients" as open (pdf lines 214-218).
     - They say that positive formulas are still needed (lines 211-212).
     - Fischer-Ikenmeyer give polynomial time for fixed outer degree.
   - **Verdict.** So G-031 is STILL NEW, and the positive formulas G-036/T-037 are PARTLY new: only the positivity is new.
   - **Gate.** Nobody outside the run has read the exhaustion proof or G-036's three providers.
   - **Proof.** `GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped/GCT_PLETH.tex` from line 20109, and
     `work/root/FIVE_ROW_SUPPORT_INDEX.json`.

8. **A quantitative bound on Picard kernels (POLISH_ALGEBRAIC_GEOMETRY P2:thm:positive-excess-picard; P90e).**
   - **Statement.** δ ≥ pd/(2(p−1)) for a nontrivial order-p class that is trivial on a curve with Y² = d > 0, on any normal
     surface.
   - **The nearest literature.** Cotner-Zavyalov (Compositio 160 (2024), arXiv 2204.06121, opened) prove injectivity on
     fppf cohomology for *strongly* ample divisors. Their Example 3.3.6 shows failure for merely ample ones. Bhatt-de Jong
     treat the local case.
   - **Novelty.** Neither source has a bound of this kind (extended search). The run already cites Cotner-Zavyalov.
   - **Proof.** `research_returns/POLISH_ALGEBRAIC_GEOMETRY_checkpoint_35_20261124T0416Z_unzipped/workbench/papers/paper_02/main.tex`
     line 151, and `positive_square_picard_strictness.tex`. It has a full check by a model other than the run's.

9. **Integral crystalline weak Lefschetz fails (POLISH_CRISTAUX Paper 1).**
   - **Statement.** X has a smooth ample Y such that H^i_cris(X/W) → H^i_cris(Y/W) is not injective, or not saturated, in
     low degrees, at every prime.
   - **Check.** Every step was checked by a512cf71 (Claude Opus 5.5 at effort max).
   - **Novelty.** The search found only rational weak Lefschetz (Nakkajima's appendix in 1902.09110) and adjacent
     comparison results (Caro-D'Addezio 2511.11444). It is a thin search: one query.
   - **Proof.** `POLISH_CRISTAUX_checkpoint_33_20261124T2056Z_unzipped/POLISH_CRISTAUX_checkpoint_33/workbench/papers/paper1/`.

10. **GCT VIII errata (GCT_POS N-012, N-002, N-003, N-009, with GCT_NSRH F57, F58 and F67; H23).**
    - **What.** Conjecture 3.2 has no minimum as printed. Strict positivity fails at rank 4.
    - **Novelty.** No erratum or counterexample to GCT VIII is found.
    - **Before posting.** The note goes to Mulmuley first (drafts only, on the user's word), and P-F-E3-01 needs an
      independent re-run.
    - **Proof.** GCT_POS `branches/nonstandard/`; GCT_NSRH `finding_F57.tex`, `F58` and `F67`.

11. **Border rank of det₄ and per₄ (H03), only with the newest bound.**
    - **The literature.** No published CP or Waring border bound reaches 43. The nearest are:
      - Farnsworth (symmetric border rank);
      - Han-Ju-Kim 2510.11051, whose "4×4 determinant tensor" (border rank 12) is a different object.
    - **What to write.** BR_PENCIL's 43 and GCT_OBS's 44 are superseded inside the project by Codex's BORDER_RANK (≥ 52,
      not opened). Write one paper on the newest checked bound, with R-01 and P-01 as its method. 43 alone is not worth a
      paper.

## B. Every item, by cluster

### GCT

| Item | Verdict | Paper now | Hexagon |
|---|---|---|---|
| GCT_POS H02b (above) | STILL NEW | yes | H02b drafted (prompt 57) |
| GCT_POS K-008, K-014 (r = 0 at n = 4, 5) | STILL NEW | in H02b | — |
| GCT_POS K-018 | UNSETTLED: compare Kravtsov, Franks-Reichenbach | no | — |
| GCT_POS N-ids + NSRH F57/F58/F67 (H23) | STILL NEW | yes | candidate |
| GCT_PLETH G-031 | STILL NEW | yes | H20 |
| GCT_PLETH G-036, T-037 | PARTLY (Kahle-Michałek signed formulas) | with G-031 | H20 |
| GCT_PLETH G-015, T-032-T-036 | PARTLY (Sarkar 2610.07929; Bowman-Paget; Paget-Wildon 2505.06104) | no | — |
| GCT_PLETH G-037-G-040 | PARTLY (Pak-Panova-Swanson 2511.02312; Narayanan) | no | H21 |
| CUE_GCT R-14, R-13, R-27 | STILL NEW | yes (narrow) | H14 |
| GCT_KRON A-030, A-034, O-030 | STILL NEW | yes | H13 |
| GCT_OBS S-002, S-003 | PARTLY (LMR's module) | in H13 | — |
| GCT_OBS QC-014 | STILL NEW (thin) | no | — |
| GCT_OBS QC-019 | STILL NEW | no (certificate unrecomputed) | — |
| BR_PENCIL R-05/08/10, OBS BR-006 | STILL NEW in literature; superseded internally | only as H03 newest | H03 |
| GCT_GINEQ F-05 | **KNOWN BEFORE**: Derksen 1308.3860 Cor. 1.10 | no | — |
| GCT_GINEQ F-13, F-23 | PARTLY (substitution method known) | no | — |
| GCT_NSRH F03, F24, F50 | STILL NEW; ours, posted | no (v2 with F50) | H01 = 2611.00789 |
| GCT_NSRH F34 | UNSETTLED: read Fischer-Ikenmeyer 2002.00788 | no | — |
| DP_MULT H09 | STILL NEW; posted | no (v2: cite Katagiri 2611.25978, 2609.20002) | H09 = 2611.00938 |

**What would be new to add to the GCT papers.**
- **Sheshadri 2611.06658 (4 Nov, v2 11 Nov):** dc(per₄) = 15, so Grenet's construction is optimal at n = 4.
- **Sheshadri 2606.15970:** a ceiling for polar and conormal lower bounds.

Neither overtakes an item. Both are context for GCT_OBS and for the dc discussion in any write-up.

### AG_POLISH

| Item | Verdict | Paper now | Hexagon |
|---|---|---|---|
| KTOWER K_{4k}(ℤ) = 0, k ≤ 20 | **OVERTAKEN**: Mok-Zheng 2611.00998 (24 Nov, m ≤ 30, stated unconditional); Pintar 2611.00829 v3 (k ≤ 26, given Step 17) | no | H18: drop |
| KTOWER small-order Vandiver | UNSETTLED: read the two bodies | no | — |
| P90e positive excess | STILL NEW | yes | board row |
| P90a | STILL NEW; posted | no | 2611.00936 v2 |
| P1 cd theorems (cote 31) | STILL NEW (thin) | not yet | — |
| P2 G1 | PARTLY (Poonen-Rains, rank ≤ 2) | no | — |
| CRISTAUX Paper 2 wild bands, prescribed field | STILL NEW (thin) | not yet: recovery halves unchecked | — |
| CRISTAUX Paper 1 | STILL NEW (thin) | yes | — |
| CRISTAUX Paper 21 | STILL NEW (thin) | no: run only | — |
| CRISTAUX Paper 9 | UNSETTLED: compare Berthelot's MW = rigid | no | — |
| CRISTAUX Paper 8 splitting | **KNOWN BEFORE**: Riba 1903.04396 Cor. 4.1, from Sah 1974 Thm 7 | no | — |
| Int(R) free (S20) | STILL NEW; posted | no | 2611.00937 v2 |
| Concordance results | UNSETTLED: Galvin 2405.07928 / Compositio 2026, OPRW | no | — |
| ARCH_ALG cote 136 | UNSETTLED: Cenkl-Porter, Miller | no | — |
| NGQ A133 Thm 26.1-27.3 | STILL NEW | not yet: 27.x unread | A133a/b |
| COUNTING_VARIETIES main | PARTLY (von zur Gathen-Karpinski-Shparlinski 1996; Ehrenfeucht-Karpinski) | no: wait for the final | — |
| NEG_NIGHT C005, C023 | PARTLY | no | — |
| JAC1964 T4.3, H9 | UNSETTLED: unrefereed inputs | no | H11, H04 |
| SPLIT_ZERO twomissing | UNSETTLED: internal to the fleet | no | — |

### DERIVATEURS

| Item | Verdict | Paper now |
|---|---|---|
| FREX A.9-A.11, A.17-A.19, A.33, C.12, A.26 | STILL NEW: Harman-Snowden comparison is the gate | yes |
| FREX D.9 | PARTLY (Evans-Hubička-Nešetřil for Ramsey and amenability) | inside FREX |
| FREX A.13 | STILL NEW (internal correction) | no |
| S2COUNT A.M1, B:main, CD:alltargets | PARTLY (Sweeney: homology only) | yes |
| Footnote-56 chain | STILL NEW | yes |
| DER_LOCALIZERS A.3, A2.x; REVLOC A-B, G.6-G.7 | STILL NEW (external inputs unopened) | not yet |
| DER_LOCALIZERS B.4 intervals | STILL NEW (thin) | no |
| RESIDUE A.5 census | **KNOWN BEFORE**: OEIS A058129 (1, 2, 7, 35, 228); BM ≃ S² is Fiedorowicz 1984 | no |

## C. What I could not settle, and what would decide it

| Item | What would decide it |
|---|---|
| K-018 | Kravtsov; Franks-Reichenbach |
| F34 | Fischer-Ikenmeyer's hardness with the inner parameter fixed |
| KTOWER small-order rows | the bodies of Mok-Zheng and Pintar |
| CRISTAUX Paper 9 | Berthelot's comparison of Monsky-Washnitzer and rigid cohomology for smooth affines |
| The concordance rows | Galvin, Compositio 2026; Orson-Powell-Randal-Williams |
| Cote 136 | Cenkl-Porter; Miller |
| JAC1964 | its unrefereed inputs |
| SPLIT_ZERO thm:twomissing | — (a fleet-internal question) |

**Thin searches** (one query each):
- QC-014;
- the P1 cd theorems;
- CRISTAUX Papers 1, 2 and 21;
- A133;
- B.4.

**Not opened, as the brief directs:** SAT_WITNESS*, SAT_KRONECKER*, the prompt-74 files, and Codex's runs (BORDER_RANK,
GCT_SEPARATIONS, GCT_FLIP).

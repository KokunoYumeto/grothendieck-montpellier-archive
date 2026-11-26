# H17 note: records

Editor: Claude Fable 5.2 at effort max (agent a49aabbf5ed57bb8e), 23 Nov 2026. The mathematics is by GPT-6 Astra
(ChatGPT Pro mode). Nothing has been sent, posted or pushed.

- Note: `h17_note.tex`, `h17_note.pdf` (15 pages; pdflatex, three passes; no overfull box; every page rendered and
  read by me, pages 7–8 again after two late edits).
- Title: "Relation (IV) of Nakamura and Schneps holds on the profinite Grothendieck–Teichmüller group, with an
  application to the two elliptic points of the modular curve".
- Gate: `REFEREE_E42_E43_A6_a49aabbf.md` with `REFEREE_CHECK_EVENTS_a49aabbf.tsv`. Comments: `REVIEW_a49aabbf_v1.md`.

## 1. Crosswalk: statements of the note and our records

| Note | Our records | Run (all GPT-6 Astra, ChatGPT Pro mode) |
|---|---|---|
| Theorem 1 ((IV) on GT̂); Props 8, 10, 11 | SECTION_GHOSTS E.177–E.180 | SECTION_GHOSTS final, 18 Nov |
| Lemma 9 (finite p-subgroups) | replaces E.176 (Smith theory) by Boggi–Zalesskii Theorem A; route 1 (EXIT_TOWER E.44) cites the same theorem | editor |
| Theorem 2 (normalization, Λ) | SECTION_GHOSTS E.181 | SECTION_GHOSTS final |
| Lemmas 12–14 (level twelve, shear, δ) | LM7_PUSH E.61, E.65 on the subgroup t = 0; the shear by a new derivation | LM7_PUSH cp09; editor |
| Lemma 15 (lattice unit) | DELTA_SEXTIC_20261121.md Prop. 1 and Theorem A (mine); E.191.11–18 | editor; SECTION_GHOSTS |
| Lemma 16 (mixed action, forgetting, periods) | SECTION_GHOSTS E.182 and E.184 (first part) | SECTION_GHOSTS final |
| Lemma 17 | E.183 | SECTION_GHOSTS final |
| Proposition 18 (self-similarity) | E.184, E.188, E.189, E.190 = EXIT_TOWER E.49 (E.255)–(E.260), (E.267) = GT_TOWER_CHECK A.C14 | SECTION_GHOSTS final; EXIT_TOWER cp28 |
| Theorem 3; Section 9 | E.191 = E.49 (E.264)–(E.268) = A.C13–A.C17; DELTA_SEXTIC Theorem B | SECTION_GHOSTS; EXIT_TOWER; GT_TOWER_CHECK |
| Corollary 4 | H17 (Δ on GT̂ = 0): needs LM7_PUSH E.65 (Δ exists, Δ = 0 on G_Q) | LM7_PUSH |
| Stated, not proved | Δ on GT̂₀ exists and is nonzero: LM7_PUSH E.65, E.58 | LM7_PUSH |

## 2. Check events (types of the check rubric)

| Statement | Date | Who | Type | Outcome |
|---|---|---|---|---|
| E.176–E.181 | 18 Nov | Claude Fable 5.2 at effort max (a49aabbf) | targeted proof check | confirmed, every step; two citations to supply |
| E.181 normalization | 18 Nov | Claude Opus 5.5 at effort max (sweep 2) | targeted proof check | confirmed |
| E.191 from E.190.4 | 21 Nov | Claude Fable 5.2 at effort max (a49aabbf) | independent re-proof | confirmed (Theorem B) |
| E.49 parity algebra (E.264)–(E.268) | 22 Nov | Claude Opus 5.5 at effort max (ae4ae3dc) | independent re-proof and computation (exhaustive over Z/12) | confirmed |
| E.259 division quartic | 21 and 22 Nov | Fable (a49aabbf); Opus (ae4ae3dc) | computation by hand | confirmed |
| E.182, E.184, E.188, E.189, E.190 | 23 Nov | Claude Fable 5.2 at effort max (a49aabbf) | targeted proof check | confirmed; E.189 given Hoshi–Minamide–Mochizuki |
| E.183 | 23 Nov | Claude Fable 5.2 at effort max (a49aabbf) | independent re-proof | confirmed |
| E.42, E.43, A.6 | 23 Nov | a49aabbf | carried as background without fault found | not refereed; not used |
| LM7_PUSH E.65 (Galois vanishing), E.58 | 21 Nov | a49aabbf | carried as background without fault found | read, not refereed; stated in the note as not proved |
| Note: Lemma 9, Lemma 13, Lemma 15, first half of the proof of Prop. 11, Step 2 of Prop. 18 | 23 Nov | a49aabbf (author of these texts) | none by anyone else | **unchecked rewriting** |
| c(f) = −A_F(−1,1) (remark after Prop. 11) | 23 Nov | a49aabbf | targeted proof check | confirmed by hand |

The runs' own check events are in their CHECK_EVENTS.tsv files (same-model re-proofs and certificates) and are not
repeated here.

## 3. Changes against the runs' texts (none silent)

1. **Route.** One chain, through Λ. Not used: EXIT_TOWER E.42–E.44 and GT_TOWER_CHECK A.6.
2. **Finite subgroups.** Boggi–Zalesskii's Theorem A cited (Lemma 9) where SECTION_GHOSTS proves E.176 and its
   variants at p = 3 and for one involution. The centralizer equality for a non-cyclic p-group is derived from the
   normalizer equality in one line (my 18 Nov report, §3.2); the published proof passes over it.
3. **The shear.** Defined by the unique unipotent intertwiner (Lemma 13) instead of V = U^{8ρ}; the note proves
   t ≡ 0 mod 4 and t ≡ −ρ₂ mod 3, which is what E.61 gives modulo 12. δ is defined on t = 0 only.
4. **Twelve points.** Used only for the full topology of the centralizer of ι; the run lifts the action to twelve
   points. Consequence: the note's group 𝒟 fixes b₀.
5. **Scope of Theorem 3.** Vanishing on normalized elements; the Galois part is a hypothesis of Corollary 4.
6. **Proposition 11.** First half (jφj⁻¹ = Ad(u^{λ−1})Φ_F) derived from the frame identity f = ϑ(β)β⁻¹; the run
   derives it from Ad(τ).

## 4. Literature (what was read, and where)

| Work | Locator used | Read |
|---|---|---|
| Nakamura–Schneps, Invent. Math. 141 (2000) 503–560 (author's version 3.14) | §1: (IV), (III′), Def. 1.1, Thms 1.2–1.4, the open question; Def. 5.1, Cor. 5.2, Prop. 5.3, (5.2); Lemma 6.1 | at the source, 18 Nov |
| Hatcher–Lochak–Schneps, J. reine angew. Math. 521 (2000) 1–24 | pp. 3–5 (Λ, (R), Theorems A, B); pp. 18–19 (Theorems 4, 5, formula (3), Lemma 6) | at the source (scan), 18 and 23 Nov |
| Schneps, Math. Nachr. 279 (2006) 656–671 | p. 659 (list of relations, e_i), p. 670 ((IV) ⇒ (R)) | at the source, 18 Nov |
| Lochak–Nakamura–Schneps, arXiv:2602.12462v1 | §1 (quotation), Thm 1.1, Thm 2.1, §8 | at the source (TeX), 18 Nov |
| Boggi–Zalesskii, Bull. LMS 57 (2025) 236–255, arXiv:2406.08639v2 | Theorem A; Lemmas 2.2, 2.3; proof of Theorem 3.x(iii); the theorem on hyperelliptic mapping class groups (last section) | at the source (TeX), 18 and 23 Nov |
| Hoshi–Minamide–Mochizuki, Kodai Math. J. 45 (2022) 295–348, doi:10.2996/kmj45301 | Corollary C (Out(Π_n) = GT × S_{n+3}) | abstract only (J-STAGE), 23 Nov; **open the paper before posting** |
| Basualdo Bonatto–Robertson, arXiv:2606.01466v2 | abstract; §1 (Thms 1.2, 1.4; Thm 4.9 named) | abstract and §1 through a page-reading tool, 23 Nov; §4 not read |
| Collas, arXiv:2603.02848v2 (survey) | abstract | 23 Nov; not cited in the note |
| Dolgushev–Guynee, arXiv:2401.06870 | abstract (gentle version GT₀, after Harbater–Schneps) | 23 Nov |
| Collas, JTNB 24 (2012) 605–622 | title; cited for context | not opened (locator from DELTA23's reference list) |
| Harbater–Schneps 2000; Lochak–Schneps 1994; Ihara 1994; Drinfeld 1991; Herfort–Ribes 1985; Kerckhoff 1983; Birman–Hilden 1973; Anderson 1974; Asada 2001; Fouxe-Rabinovitch 1940 | as cited | **not opened; from memory or the runs' locators**. Check before posting: Anderson (exactness of completion for a free normal subgroup), Asada (faithfulness in genus zero), Fouxe-Rabinovitch (Out(C₂ ∗ Z)) |

**Hexagon** (hexagonmath.org, 23 Nov): search "Grothendieck-Teichmüller": 0 works. Nothing on GT̂, relation (IV) or Λ.
**Kind:** needs a short pass, done (REVIEW). No overlap with Lochak–Nakamura–Schneps or Basualdo Bonatto–Robertson.

## 5. Before posting

1. The user's word; the line of authors.
2. A second reader for Sections 4 and 8 of the note and for the rewritten places of §2 above.
3. Hoshi–Minamide–Mochizuki at the source (Corollary C; compatibility with forgetting; the identification of the GT
   factor with the braid action).
4. The three references marked above.
5. The workbench address (`\workbenchurl` is set to github.com/KokunoYumeto/grothendieck-longue-marche; confirm).
6. Decide whether Corollary 4's two inputs (LM7_PUSH E.65 and E.58) get a check first.

## 6. Whom to write to when it is posted

- Hiroaki Nakamura (Osaka) and Leila Schneps (Paris): relation (IV) and their question on 𝕀Γ ⊂ GT̂; Theorem 1.
- Pierre Lochak (Paris) and Allen Hatcher (Cornell): Λ; Theorem 2; the question of arXiv:2602.12462, §8.
- Marco Boggi and Pavel Zalesskii: their Theorem A carries three steps. (We wrote to them on 16 Nov about another
  step; no reply.) Mention the one line needed for centralizers of non-cyclic p-groups.
- Yuichiro Hoshi, Arata Minamide, Shinichi Mochizuki: Corollary C carries Step 3 of Proposition 18.
- Luciana Basualdo Bonatto and Marcy Robertson: Theorem 1 simplifies the definition of the group they act with.
- Benjamin Collas: torsion and special loci in GT theory.

## 7. Version 2 (23 Nov 2026, after the second reader)

`h17_note.tex` and `h17_note.pdf` are now version 2 (16 pages, no overfull box, rebuilt from a fresh copy). Version 1:
`h17_note_v1_20261123.tex`, `.pdf`. Second reader: `REVIEW_ae4ae3dc_v1.md` (Claude Opus 5.5 at effort max): no
mathematical error. Every change, with its check events: `REVIEW_a49aabbf_v2.md`. The script of the last nine
replacements is `apply_v2_edits.py`. Items 3–5 of §5 above are settled as follows: Hoshi–Minamide–Mochizuki opened by
the second reader; Asada and Fouxe-Rabinovitch confirmed; Anderson replaced by the direct proof (F); the workbench
address is left to the main session (`\recordurl`).

## Version 2 committed (24 Nov 2026, 23:27 UTC)
Main session 329fb1e6 (Claude Opus 5.5 at effort max), at the user's word of 24 Nov (v2s welcome, sooner rather than later), under hexagon-post-when-sure. New in v2 (a49aabbf, Claude Fable 5.2 at effort max): Theorem 20, relation (III') on all of GT-hat; Corollary 21, I-Gamma = GT-hat; Corollary 22, Lochak's questions answered and Out* = GT-hat for surfaces of generic type (given his Theorem 5.10 ii)); Remarks 19 and 23; the line-158 correction (no published proof that GT-hat is strictly inside the gentle group); Lochak 2025 and the 16 Nov EXIT_TOWER proof cited. CHECKS: independent referee check by ae4ae3dc (Claude Opus 5.5 at effort max; CHECK_H17_V2_20261124.md): all claims hold, no earlier proof found; repairs made by a49aabbf (BZ Thm A(iii) with hypotheses; Kurosh; the star of Lochak Thm 5.10 ii) read on the printed page at 300 dpi; the checker's '(IV')' repair refused rightly: the printed label is (IV)); the main session read the proof of Theorem 20 step by step (Steps 1-4: the pentagon conjugate, Boggi-Zalesskii, Birman/Push and the Kurosh centralizer in C2*C2*Z, the images f(u^2,v^2)) and the changed pages 1, 17-22 (pages 2-16 are version 1's); dates set to the UTC date 24 Nov (backups v2/2611.00940/_date_backup/); rebuilt 22 pp., 0 overfull, 0 undefined. Hexagon: revise -> draft 15b21f54; v1 source (upload a8d13aef) removed; v2 uploaded as relation_iv_gt_hat.tex; metadata HEXAGON_METADATA_WB0007_v2.json (build_meta_wb0007_v2.py from METADATA_FIELDS_v2.txt; comments 1,982; tags 10); verify-meta same; preview identical on all 22 pages (11,986 words). Committed 23:27:16 UTC: hexagon:2611.00940v2, sourceTreeSha256 888b6c08...3d02d7.

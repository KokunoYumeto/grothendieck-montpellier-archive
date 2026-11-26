# Provenance of "Weak fundamental localizers that are not fundamental localizers, and Corollaire 7.7.2 of Grothendieck's *Les Dérivateurs*" (D3)

Written 25 Nov 2026 by a34c04448e8299803 (Claude Opus 5.5 at effort max), the Dérivateurs expert of the homotopy map,
on the brief `agent_notes/a34c0444_D3_NOTE_BRIEF_20261125.md` of the main session 329fb1e6 (Claude Opus 5.5 at effort
max). Work file: `agent_notes/a34c04448e8299803_NOTES.md`. The paper is AI-produced. No human proved, wrote or checked
any part of it. Not posted.

## Contributors

| Who | Model and effort | What |
|---|---|---|
| Run BISITE (`derivateurs_companion_20261109/pro_returns_20261110/7_BISITE/`), return of 11 Nov 2026, report mtime 13:34 UTC | GPT-6 Astra (ChatGPT Pro mode) | A.32: the class W† (here **W_π**), literal Loc (1)-(3) with moderate saturation, failure of Loc (3 bis) over BC₂, failure of Loc (1 bis); `sections/A.tex:434`; program `code/a_absolute_relative.py` |
| Run RESIDUE (`.../pro_returns_20261110/8_RESIDUE/RESIDUE/`), return of 11 Nov 2026, report mtime 18:32 UTC | GPT-6 Astra (ChatGPT Pro mode) | B.2 (the quotient 𝒬), B.3 (W_circ, strongly saturated, absolute Theorem A), B.4 (crowns C₈ → C₄ suspended over {o<+, o<−}); `sections/B.tex:54,94,138`; program `code/BC/verify_counterexamples.py` |
| Run REVLOC (`.../pro_prompts_max_20261112_work/REVERSIBLE_LOCALIZERS/REVLOC_checkpoint_17_20261116T0257Z_unzipped/REVLOC/`), checkpoint of 16 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode) | F.1: the class W† (here **W_tor**), Loc (8), (9), failure of Loc (3 bis) and Loc (6′a), witness 77 → 53; F.1.1: Loc (6′a) + Loc (8) ⇒ fundamental localizer (the sufficiency in Theorem B(ii)); `sections/F12.tex`; program `code/FGH_literal_axioms.py` |
| Run DER_FOLLOWUP, 17 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode) | G.9: F.1.1 restated and used (its depends_on lists REVLOC F.1.1) |
| Run DER_LOCALIZERS (`.../pro_prompts_max_20261112_work/DER_LOCALIZERS/DER_LOCALIZERS_checkpoint_08_20261118T0954Z_unzipped/DER_LOCALIZERS/`), checkpoint of 18 Nov 2026 | GPT-6 Astra (ChatGPT Pro mode) | A5.1 (Loc (6′a) ⇒ strong saturation: Theorem B(i)), A5.2 (W_fin), A5.3 (witness j: Q → P, 2 → 58 objects, coproduct over discrete N), A5.4 (audit of G.9; footnote 56 incorrect for Loc (6′a, 8, 9), vindicated without Loc (8)); `sections/A5.tex`; program `code/A5_finite_component_counterexample.py` |
| ac003b3d | Claude Fable 5.2 at the session's default effort (none set at launch) | BISITE combined review, 11 Nov 2026 (`pro_reviews_20261110/7_BISITE/COMBINED_REVIEW.md` l.13, l.51) |
| a5ead5c6 | Claude Fable 5.2 at effort high | intake of S2COUNT and REVLOC, 17 Nov 2026 (F.1, F.1.1 at statement level) |
| sweep 1, Dérivateurs scope | Claude Opus 5.5 at effort max | 18 Nov 2026: targeted proof check of REVLOC F.1; statement comparisons of F.1.1, G.9, A5.4 with XVI ms. 117-118 |
| a8081d1b | Claude Opus 5.5 at effort max | Opus-max intake 19 Nov 2026 (`pro_prompts_max_20261112_work/INTAKE_FREX_DERLOC_REVLOC_RESIDUE_20261119.md`, events in `CHECK_EVENTS_20261119.tsv`): RESIDUE B.2-B.4 (B.3 also re-proved), DER_LOCALIZERS A5.1 (pushout step), A5.2, A5.3, A5.4 |
| cluster reader of the intake pile | Claude Opus 5.5 at effort high | 24 Nov 2026 (`reports_20261124/INTAKE_PILE_20261124/DERIVATEURS.md`): BISITE A.32 and REVLOC F.1 followed in full; A5.3's homological step re-derived; the priority correction P1 |
| topicality reader | Claude Opus 5.5 at effort high | 24-25 Nov 2026 (`TOPICALITY_GCT_AG_DER.md` item 6): Maltsiniotis, Astérisque 301, §1.1 and Introduction opened; verdict STILL NEW |
| a34c04448e8299803 (this writer) | Claude Opus 5.5 at effort max | the gate (Cisinski 2006 opened, below); the paper; Lemmas 3.1-3.5 in their form; the failures of Loc (6′a) for W_π and W_circ; Lemma 3.5 (Loc (8 bis) ⇒ retract closure); the mapping-cylinder proof of Lemma 5.1; Proposition 5.2 (necessity in Theorem B(ii)); the carrier-homotopy sentence for degrees of face-poset maps; ABSTRACT.md, this file, CHECK_EVENTS.tsv; on 25 Nov after the check: the repairs R1-R15, the line-by-line check of the checker's three results, the correction of footnote 56's reading in three files |
| afceadd46f7598ec4 (the checker) | Claude Fable 5.2 at effort max | independent check of the whole text, 25 Nov 2026 (`CHECK_D3_INDEPENDENT.md`, events `CHECK_D3_INDEPENDENT_CHECK_EVENTS.tsv`, program `work/CHECK_D3_INDEPENDENT_counts.py`): no mathematical error; repairs R1-R15; and three new results now in the paper: **Proposition 4.2** (the class W_ctbl: Loc (8) cannot be weakened to Loc (8 bis)), **the failure of Loc (8 bis) for W_circ**, **the failure of Loc (9) for W_π**; a fourth (Loc (9) for W_circ) only sketched, not in the paper |
| 329fb1e6 (main session) | Claude Opus 5.5 at effort max | commissioned the note; to read every page and post |

## Names and statements

| Paper | Run statement | Note |
|---|---|---|
| W_π | BISITE A.32, its W† | renamed: REVLOC F.1 also calls its class W† (DERIVATEURS.md P2) |
| W_circ | RESIDUE B.3, W_circ | Lemma 4.1 = RESIDUE B.2 |
| W_tor | REVLOC F.1, its W† | renamed |
| W_fin | DER_LOCALIZERS A5.2, W_fin | |
| Theorem A(a) | BISITE A.32 | plus the writer's Loc (6′a) failure and Lemma 3.5 |
| Theorem A(b) | RESIDUE B.2-B.4 | plus the writer's Loc (6′a) failure |
| Theorem A(c) | REVLOC F.1 | |
| Theorem A(d) | DER_LOCALIZERS A5.2, A5.3 | strong saturation via Theorem B(i) as in A5.2 |
| Theorem B(i) | DER_LOCALIZERS A5.1 | pushout step reproved (Lemma 5.1) |
| Theorem B(ii), sufficiency | REVLOC F.1.1 = DER_FOLLOWUP G.9; audited in A5.4 | pushout step reproved (Lemma 5.1) |
| Proposition 5.2 (necessity) | none | the writer's, from Cisinski Cor. 4.2.22 and Prop. 4.2.9 |
| Proposition 4.2 (W_ctbl), Section 4.5 | none (check report §6.1) | the checker's; checked line by line by the writer |
| Theorem A(b): Loc (8 bis) fails for W_circ (Section 4.2) | none (check report §6.2) | the checker's; checked line by line by the writer |
| Theorem A(a): Loc (9) fails for W_π (Section 4.1) | none (check report §6.3) | the checker's; checked line by line by the writer |
| Section 7 item 2: Loc (1)(c) from Loc (8 bis) | none (check report R1) | the checker's two-line argument; checked by the writer |
| Corollary C | A5.4; DERIVATEURS.md item 4 | see "Footnote 56" below |

## Priority (DERIVATEURS.md P1, confirmed 25 Nov)

BISITE's report has mtime 11 Nov 2026 14:34 CET = 13:34 UTC; RESIDUE's 19:32 CET = 18:32 UTC. The BISITE combined review
(11 Nov, l.13) records POLES A.16 ("do the literal Loc (1), (2), (3) imply Loc (3 bis)") as answered by A.32. So W_π came
first, for the literal axioms with moderate saturation; W_circ was the first strongly saturated example; W_tor (by
16 Nov) added Loc (8), (9); W_fin (18 Nov) showed Loc (8) needed. The positive side: REVLOC F.1.1 (checkpoint of 16 Nov),
then DER_FOLLOWUP G.9 (17 Nov), audited in DER_LOCALIZERS A5.4 (18 Nov). The Opus-max intake of 19 Nov (§1 finding 7,
§6b item 4) had given RESIDUE first; that is corrected here and in DERIVATEURS.md P1.

## Footnote 56: a reading to correct elsewhere

Corollaire 7.7.2 assumes a localiseur fondamental (Loc (1)-(3)) with Loc (6′a, 8, 9) and concludes Loc (1 ter, 3 bis);
footnote 56 says the Loc (3 bis) part is "pas prouvé, probablement faux". By Theorem B the conclusion holds (without
Loc (9)), so the doubt is not borne out for the corollary's hypotheses; it is borne out once Loc (6′a) (W_tor) or
Loc (8) (W_fin) is dropped. This is DER_LOCALIZERS A5.4's reading, and the checker's (check report §3.7). It had already been written down on
17 Nov by afbbdefd (Claude Fable 5.2 at effort max) in
`derivateurs_companion_20261109/pro_prompts_max_20261112_work/INTAKE_DER_FOLLOWUP_FINMON_20261117.md`, lines 279 and
509-511. Three files read it the other way, and were corrected on 25 Nov 2026 by this writer with the checker's
wording (check report §8), each after a backup:

| File | Lines | Backup |
|---|---|---|
| `reports_20261124/INTAKE_PILE_20261124/DERIVATEURS.md`, item 4 | 68-69 ("is right as printed") | `DERIVATEURS_before_fn56_fix_20261125.md` beside it |
| `derivateurs_companion_20261109/pro_prompts_max_20261112_work/INTAKE_S2COUNT_REVLOC_20261117.md` (a5ead5c6, Claude Fable 5.2 at effort high) | 32 ("decides ... in his favour") | `INTAKE_S2COUNT_REVLOC_20261117_before_fn56_fix_20261125.md` beside it |
| `claude_math_notes/NOTES_20261117.md` (Claude Opus 5.5 at effort max, per the check register) | 66-68 (the same sentence) | `NOTES_20261117_before_fn56_fix_20261125.md` beside it |

The paper follows A5.4.

## Sources and where each citation was confirmed

- **Grothendieck, *Les Dérivateurs*, Chapitre XVI** (edition of Künzer, Malgoire, Maltsiniotis, version of 18 March
  2019): the edition's pages in `derivateurs_companion_20261109/packages/DER_XVI/DER_XVI_pages.pdf` (59 pages; PDF page
  57 = printed page 55) and our transcription `derivateurs_companion_20261109/corrected_french_20261111/DER_XVI.tex`.
  Opened by the writer: Loc (1)-(3) and footnote 1 (printed p. 1, ms. pp. 1-2); Rappel 1 (pp. 1-2); Définition 1.1 and
  Loc (3 bis) (p. 2, ms. pp. 2-3); MV diagrams and Loc 6′ (pp. 12-13, ms. pp. 17′-18′); Loc (8), (8 bis) (§5, p. 40);
  Loc (9) (p. 41); Prop. 5.3.1 (pp. 41-42), Cor. 5.3.2 (p. 42); footnote 53 (p. 53); Prop. 7.7.1, N.B., footnote 55, Corollaire
  7.7.2, footnote 56 (p. 55, ms. pp. 117-118; the page viewed as an image: Cor. 7.7.2 at lines 16-17 counting every line
  including the editors' bracketed page markers, footnotes 55-56 at the foot); §7.8, footnotes 57, 58 (p. 56).
- **Cisinski, Astérisque 308 (2006)**: local copy
  `derivateurs_companion_20261109/pro_prompts_20261110_work/_downloads/Cisinski_Ast308/smf_ast_308.pdf`; text extracted to
  `CONFERENCE/papers/D3/work/ast308.txt`. Opened by the writer: Déf. 1.4.1 (A-localizers, L1-L3), Th. 1.4.3, 1.4.12 (weak saturation
  FS1-FS3), Cor. 1.4.7, Cor. 2.1.21, Déf. 3.3.2 (p. 143), 3.4.1, Prop. 3.4.25, Ex. 4.1.21 (pp. 180-181), Th. 4.1.26,
  Ex. 4.1.29, Prop. 4.2.9, Déf. 4.2.11, Th. 4.2.15, Rem. 4.2.16, Cor. 4.2.19, Cor. 4.2.22 (p. 188), 6.1.7, 6.1.12 (p. 240),
  Prop. 6.1.16 (p. 241), Cor. 6.1.17 and Th. 6.1.18 (p. 242), the introduction's summary of §6.1, bibliography [96].
- **Rădulescu-Banu, Cofibrations in homotopy theory, arXiv:math/0610009v4** (8 Feb 2009): e-print source downloaded to
  `CONFERENCE/papers/D3/work/rb/` and opened by the writer: Def. 1.1.1 (CF1-CF6; precofibration = CF1-CF4), Lemma 1.4.1
  (gluing), Lemma 1.4.2 (excision), Def. 7.2.5-7.2.6, Th. 7.2.7 (numbering from the chapter order in `main.tex` and the
  shared theorem counter). WS3 is typed "ri = 1_B" in the source; read as ri = 1_A, as the DER_LOCALIZERS run did.
- **Grothendieck, *Les Dérivateurs*, Chapitre XVIII** (same edition, version of 17 December 2025): Déf. 4.13.1
  (printed pp. 104-105: a part S is accessible if a) strictly full, b) the full subcategory is accessible, c) the
  inclusion is accessible) and Déf. 4.8.7 (p. 72: π₀-accessible = equivalent to some Ind_π₀(C), C small), in
  `corrected_french_20261111/DER_XVIII-c.tex` l.1148 and `DER_XVIII-b.tex` l.1334; opened by the checker and by the
  writer. Nothing else of Chapter XVIII was read.
- **Maltsiniotis, Astérisque 301 (2005)**, local copy of the author's version of 2020
  (`derivateurs_companion_20261109/pro_prompts_20261110_work/_downloads/Maltsiniotis_Ast301/prstnewprov2020.pdf`, text in
  `CONFERENCE/papers/D3/work/mal301.txt`): 1.1.2 and the Introduction opened by the checker; Prop. 1.1.21 (u is a weak
  equivalence iff u° is, under the standing hypothesis "un localisateur fondamental faible W" of §1.1) opened by the
  checker and by the writer. §1.1 was also opened by the topicality reader.
- **Quillen 1973, §1**: opened by the checker (Proposition 2 with its Corollaries 1 and 2; Theorem A) and by the writer
  (Theorem A, the dual formulation stated right after it, and the Example that follows: the map of ordered sets of
  simplices induced by a simplicial map realizes it), in the text copy
  `derivateurs_companion_20261109/pro_reviews_max_20261112/1_CATHOT/work/lit/txt/quillen.txt`.
- **Cisinski 2006**, further places opened by the writer after the check: Prop. 4.2.4 (every fundamental localizer is
  strongly saturated), Rem. 1.1.3 (continuous well-ordered sequences).
- **Hatcher, Algebraic Topology**: Th. 4.5 (Whitehead) and Th. 4.32 (Hurewicz) opened by the checker (text copy
  `.../1_CATHOT/work/lit/txt/hatcher_AT.txt`); not by the writer.
- **Brown, Topology and Groupoids**: 6.7.2 (§6.7, p. 240 of the author's electronic version) opened by the checker; not
  by the writer.
- **Thomason 1979**: cited only in the proof overview, for B∫ ≃ hocolim; not used in any proof; opened by nobody.

## Literature search (gate of the brief)

- Cisinski 2006 (the brief's gate, §§4.2 and 6.1), opened by the writer on 25 Nov: §4.2 is "Modélisateurs élémentaires"
  (Th. 4.2.15, the correspondence; Cor. 4.2.19, 4.2.22); weak fundamental localizers appear only at 6.1.12-6.1.18
  (pp. 240-242; the index lists p. 240 only). Cisinski proves every fundamental localizer weak (6.1.12), Prop. 6.1.16,
  Cor. 6.1.17, Th. 6.1.18 (W∞ the minimal weak fundamental localizer). He gives no class separating the two notions and no
  general implication, and states no open question about it. So the separation is not in Cisinski 2006; the brief's
  stop condition did not apply.
- Maltsiniotis 2005 §1.1 (topicality reader, 24-25 Nov): defines weak fundamental localizers (La, Lb, Lc) beside the
  relative form; records Cisinski's minimality; his examples 1.1.31-1.1.34 contain no separating class. Verdict STILL NEW
  (`TOPICALITY_GCT_AG_DER.md` item 6 and its TSV row "Footnote-56 chain").
- No AI-laboratory result bearing on the question was found (the OpenAI preprints 312, 317 audited in REVLOC concern
  other rows).

## The writer's own parts

Lemma 3.5; the failures of Loc (6′a) for W_π and W_circ; Lemma 5.1's mapping-cylinder proof; Proposition 5.2; the
formulation of Lemmas 3.1-3.4; the carrier-homotopy sentence in §4.3. All were checked line by line on 25 Nov 2026 by
afceadd46f7598ec4 (Claude Fable 5.2 at effort max), a model of the same family as the writer. No check by a model of
another family.

## The independent check and what was done with it (25 Nov 2026)

- Report: `CHECK_D3_INDEPENDENT.md` (afceadd46f7598ec4, Claude Fable 5.2 at effort max): no mathematical error;
  Theorems A, B and Corollary C hold as stated; the writer's five places correct; the reading of footnote 56 right.
- Repairs applied as worded: R1 (in Section 7 item 2, as worded; the alternative of strengthening Lemma 3.5 was not
  taken), R2 (Section 6 and the abstract), R3 (Loc (9) locator, with the new bibliography entry for Chapter XVIII),
  R4, R5, R6, R7 (all five places), R8, R9, R10 (title footnote and abstract, extended to name the checker's
  results), R11, R12, R13 in part, R14, R15 (Section 8, abstract, this file).
- R13: (a) applied without the clause "which Grothendieck had conjectured", whose source (a footnote of Maltsiniotis
  before his Prop. 3.1.10) the writer did not reopen; (b) not applied: the sentence on the uses of the relative axiom
  listed in Maltsiniotis's Introduction is context only, and the writer did not reopen that list; (c) applied
  (Cisinski Rem. 1.1.3, opened).
- Also done from the report's Section 7: "by finite examples" qualified for W_fin (Section 1.4). Not done: the optional
  renaming of reused notation in Sections 4.2-4.4.
- The checker's new results (report §6), each checked line by line by the writer before going in:
  - §6.1, the class W_ctbl (Loc (1)-(3), (1 ter), (6′a), (8 bis); not (3 bis), not (8)): **in**, as Proposition 4.2
    (Section 4.5), with Corollary C(ii), Table 1, Sections 1.5, 1.7, 6, 7 and 8 updated;
  - §6.2, Loc (8 bis) fails for W_circ: **in**, Theorem A(b) and Section 4.2;
  - §6.3, Loc (9) fails for W_π: **in**, Theorem A(a) and Section 4.1. It rests on Chapter XVIII's definitions
    (opened) and on the standard fact that a category of ind-objects Ind_π₀(C) has colimits over ordered sets in which
    every subset of cardinality at most π₀ is bounded;
  - §6.4, Loc (9) holds for W_circ: **left out**. The checker gives a sketch and says it has not written the details (the
    ℵ₁-filtered closure and the countable sub-functors). The writer's reading of the sketch finds it plausible (the
    fundamental group of an ℵ₁-directed colimit of circles is torsion free of rank at most 1 with all countable subgroups
    cyclic, hence 0 or Z), but a result goes into the paper only with a full proof; Table 1 keeps a dash there.

## Open points

- Whether stability under arbitrary coproducts can replace Loc (8) in Theorem B(ii) (Loc (8 bis) cannot:
  Proposition 4.2). The checker sketches an argument for yes (report §6.1, last paragraph) and does not claim it.
- Whether Loc (8) + Loc (9) without Loc (6′a) give strong saturation (they give Loc (1 bis): Section 7 item 2).
- Loc (9) for W_circ (sketched yes, report §6.4) and for W_ctbl.

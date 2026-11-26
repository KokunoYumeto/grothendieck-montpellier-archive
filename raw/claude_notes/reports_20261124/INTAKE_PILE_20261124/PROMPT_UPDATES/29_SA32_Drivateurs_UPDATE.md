# Update of `TO_SEND/PRO/E_Archive_small_prompts_54/16_small_batch_2_18-34/29_SA32_Drivateurs` (25 Nov 2026)

- **By.** Claude Opus 5.5 at effort max, agent a34c04448e8299803 (the Dérivateurs field expert), on
  `PROMPT_UPDATE_BRIEF.md`.
- **Sent?** No: not in `SENT_PRO.tsv`, and not in `16_small_batch_2_18-34/SENT/` (that folder holds 27_SA29 only).
- **Backup.** `TO_SEND/PRO/_backups_20261125/29_SA32_Drivateurs/`.

## What the prompt covers

The cotes:
- 158, *Autour des Dérivateurs*, Codex K158-01 to -05;
- 159, *Connexions projectives et uniformisation*, Pro MPL_159, with all 83 note entries;
- 160, *Schémas en groupes*, Codex K160-01, -02.

157-1 to 157-5, the chapters of *Les Dérivateurs*, are "other part" in its TOPIC.md.

Our Dérivateurs research bears on cote 158. Its transcriptions work with:
- fundamental localizers `W` and `Loc(6)`;
- totally `W`-aspherical categories and cofiltrance (K158-04, K158-05);
- pseudocofiltrant monoids, `π₁(M)`, and the monoids `Ep(E)`, `Mon(E)` (K158-02, K158-04).

I located these by searching the transcriptions in the ZIP and read the passages quoted in the digest. Cotes 159 and
160 are outside our Dérivateurs research, and I added nothing for them.

## Changes, with their evidence

1. **New background in the ZIP: `SA32_background/`.**
   - `DERIVATEURS_RESULTS_20261125.md`, a digest written for this run. It gives each result with its statement, run and
     id, check state and topicality verdict:
     - §1: the footnote-56 / Cor. 7.7.2 chain BISITE A.32 → RESIDUE B.2-B.4 → REVLOC F.1 → DER_LOCALIZERS A5.3, with
       REVLOC F.1.1 (sources: `DERIVATEURS.md` item 4 and P1; `TOPICALITY_GCT_AG_DER.md` item 6);
     - §2: DER_LOCALIZERS A.3, A.4, A2.4, A2.9 and REVLOC G.6-G.7;
     - §3: FREX A.1 (which I checked on 25 Nov), A.11, A.19, A.24-A.26, A.33, D.1-D.12, TOTAL_EXACT_2 `C_δ`, and
       RESIDUE F.1-F.4 (`DERIVATEURS.md` items 1-2, 6-7; `TOPICALITY_GCT_AG_DER.md` item 4);
     - §4: Ben-Bassat §7 (opened), our Theorems 2.1-2.2 (CATHOT OWN_RESULTS §2, opened), S2COUNT A.M1, B:main and
       CD:alltargets, and the RESIDUE A.5 census (`DERIVATEURS.md` items 3 and 8; topicality: S2COUNT PARTLY, census
       KNOWN BEFORE);
     - §5: the nerve form of the localization questions (my map, K1).
   - `DERIVATEURS_cluster_20261124.md` (the cluster file) and `MAP_HOMOTOPY_CATEGORIES_20261125.md` (my map).
   - `MANIFEST_ADDED_20261125.tsv`: origins and SHA256.
2. **PROMPT.md.** The attachments list now names `SA32_background/`. A new paragraph, "How to use `SA32_background/`",
   says:
   - Stage 2: compare each cote-158 claim on these objects with our results; record a settling or refuting result in
     `present_status` with its run, id and check state, kept apart from the literature; still search the literature for
     its fate.
   - Stage 3: the same, for the state of the art.
   - Stage 5: record them as links to *Les Dérivateurs*.
   - For each passage from slices to a functor (e.g. K158-05, "si `W` satisfait `Loc(6)`, `i` est `W`-asph."), say
     whether it needs absolute or relative Theorem A, using footnote 56.
3. **No item of the prompt is settled or overtaken.** It is a consolidation prompt: its stages stay as they are. The
   new material enters through the claims' present status and the links.
4. **Kept unchanged.** Every stage, the rules (his pages / sources / inferences kept apart; verified references), the
   check-events paragraph, the checkpoint rules and the finishing rules. No minimum, way out or cheaper alternative was
   added.

## The ZIP

`SA32_Drivateurs.zip`: 20 → 24 members (131 KB → 163 KB). Every earlier member is unchanged; the ZIP is flat.

## Lint

`push_rule_pro_prompts.py --lint PROMPT.md`: `files: 1 failing lint: 0`. This is not a paper-writing prompt, so the
paper lint does not apply.

## Proposals

The field-level proposals for new prompts are in `05_FINMON_CP2_night_UPDATE.md`, section "Proposals".

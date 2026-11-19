# Sub-agent "homotopy": FINMON, and the links between Les Dérivateurs and the Longue Marche (brief, 18 Nov 2026)

You are Claude Opus 5.5 at effort max, sweep 2, sub-agent homotopy. Read
`<local>/Documents\results_register\sweep2_global\COMMON_BRIEF_FOR_SUBAGENTS.md` first. Your folder:
`<local>/Documents\results_register\sweep2_global\sub_homotopy\`.

## Why you

1. **FINMON is in no one's hands.** It is the run of the programme map's headline "the least finite monoid with
   classifying space CP² has 23 elements; finite categories for CP² are open" (row C2-CP2: bounds 17..22). The
   register misses it (its checkpoint-20 folder holds encoded files), so sweep 1 never placed it. Its decoded results
   table (695 rows: Proved 628, Explanatory 52, Refuted 13, Unresolved 1, Definition 1) and report:
   `<local>/Documents\derivateurs_companion_20261109\pro_prompts_max_20261112_work\FINMON\FINMON_checkpoint_20_decoded_20261117\`
   (FINMON_results.csv, FINMON_report.md, 160 kB: read it in parts). Its prompt:
   `derivateurs_companion_20261109\pro_prompts_max_20261112\ALREADY_RAN\FINMON\PROMPT.md`. Its rows rarely fill
   depends_on, so its links to the other runs are in the report and the statements.
2. **The Dérivateurs line and the Longue Marche line meet** in a few places that no sweep-1 agent saw whole:
   `sub_homotopy/INPUT_crossline_and_finmon.tsv` (39 edges), and the similar pairs EXIT_TOWER C.2 ~ RESIDUE H.3
   (exit-path lifting categories), LM5_MULTI_GALOIS_TOPOI E.15 ~ STRATA B.6 (enhanced presheaf categories recover
   idempotent completion), LM5 A.20 ~ PATHS E.13 (finite tests do not see the shape), LM5 F.30 using STRATA C.7
   (Refuted); exit-path and entrance categories of the strata of M̄_{0,n} (STRATA F, RESIDUE H.5, BISITE F.16) against
   EXIT_ONE_TYPE and EXIT_TOWER's exit categories and MDT structure.
3. **A question sweep 1 handed on:** whether INDLOCAL Part B (the classification of invariant ind-objects) settles
   CATHOT E.17 (local presentations of invariant ind-objects; Open). See sweep1_derivateurs/SUMMARY.md §3 (II.2).

## What to do

1. **Place FINMON.** Give every FINMON row a place in the outline, in the same sections sweep1_derivateurs used for
   Part II.4 (finite models of homotopy types) and elsewhere (`sweep1_derivateurs/PLACEMENT.tsv` has the section
   titles): `FINMON_PLACEMENT.tsv` (tag FINMON:ID, part, chapter, section, how placed (script / read), note). By
   script first, then by reading where unclear. The "Explanatory" and working-task rows ("Both R1 proofs checked")
   get a place too, marked as such.
2. **Link FINMON to the finite-models cluster.** CATHOT G.7-G.17 (sphere and RP² minima; a_pos(RP²) ∈ [28, 49]),
   RESIDUE A.5 (the five-element sphere monoid is the unique non-1-type monoid of order at most 5), S2COUNT (A.M1,
   B:main, B:smallcategories, B:finitedomination), INDLOCAL C.26, C.27, PRETOT F.1, F.4, CATHOT D.6. Write
   `FINMON_MERGES.tsv` (canonical tag, member tag, relation: same / stronger / weaker / refines / corrects / refuted by,
   reason), in the sweep-1 format. Check the headlines as mathematics where you can: the 23-element monoid for CP²
   (what is proved: the existence, the minimality, by what certificate?), the CP² category bounds 17..22, and whether
   any FINMON row contradicts CATHOT's or RESIDUE's minima.
3. **CATHOT E.17 and INDLOCAL B.** Read both and decide whether E.17 is settled, refuted, or still open, with the
   strongest proved reduction.
4. **The cross-line links.** For each pair above and each of the 39 edges: the same object or definition? Does a
   result of one line supply what the other needs (say what it makes possible)? Are the statuses consistent (LM5 F.30
   uses STRATA C.7, which is Refuted: sound use?)?
5. **The line labels.** PRETOT and TOTEX are registered on the Longue Marche line because their returns sit in the
   Longue Marche answers folder. Confirm from their prompts (`tools/prompt_rows.json` names them) that they are
   Dérivateurs mathematics.

Write FINDINGS.tsv, CLUSTERS.tsv, CHECK_EVENTS.tsv, REPORT.md (as the common brief says) and the two FINMON files.

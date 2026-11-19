# Sub-agent "bridge": the links between the tower scope and the sections scope (brief, 18 Nov 2026)

You are Claude Opus 5.5 at effort max, sweep 2, sub-agent bridge. Read
`<local>/Documents\results_register\sweep2_global\COMMON_BRIEF_FOR_SUBAGENTS.md` first. Your folder:
`<local>/Documents\results_register\sweep2_global\sub_sections\`.

## Why you

Sweep 1 split the Longue Marche line into two scopes (tower and sections, listed in the common brief). 653 edges run
between them (`sub_sections/INPUT_crossscope_tower_sections.tsv`; columns from, statuses, scopes, kind, field, how,
evidence). Neither sweep-1 agent saw both ends. The character Δ on GT̂ is another sub-agent's (sub-agent delta): leave
Δ, E.3, E.65, E.49, 𝒥(A) = A and C^φ to it.

## What to do

Decide, by reading the rows and their proofs, each of the following. For each, say what is the case as mathematics,
what the register should say, and how sure you are.

1. **ANABELIAN_149_PUSH F.31, F.37 against LM5_MULTI_GALOIS_TOPOI F.3-F.7, F.38, F.46-F.50.** My keyword rule read
   "refutes" and "corrects" (F.31's notes: "Literal relative-only R27 remains refuted by F.1/F.17"; F.37: "contains
   corrected LM5-F.50"). R27 is a row of ANABELIAN_149_PUSH's prompt that restates LM5's F-rows. What exactly is
   refuted or corrected, and do LM5's rows (Proved/Known) need a new status or a refined statement?
2. **The Fermat Selmer theorem across the scopes.** LM8_PUSH D.22/D.23 (tower) refute a divisibility step cited for
   LM6's theorem and re-prove it with a corrected cusp constant; FERMAT_SUCCESSOR A.3-A.6, A.11, A.16 (sections) repair
   the same proof. Same error, same fix? One canonical theorem, with which hypotheses (odd n ≥ 3; which ℓ)? The
   sweep-1 sections CORRECTIONS 2-3 and tower CORRECTIONS 7 each saw one side.
3. **SECTION_GHOSTS E.100 (in its final return) against LM6 E.16, E.25, E.31-E.34, E.38, LM7_FERMAT_TOWER E.25, E.32,
   LM8_LIE_APPROXIMATIONS F.21.** E.100 says the claim "that every Fermat curve has noncuspidal sections in all the
   quotients named in R8 is false" (R8 of its prompt cites those rows). Are those rows refuted, or only a
   generalization of them? Are any of them overstated in the register?
4. **FERMAT_SUCCESSOR C.14 ("R18 scope corrected") against LM6 A.10, A.49, A.56-A.59, A.66, A.67;** and DELTA_ON_GT B.19,
   which uses LM6 A.10, A.49 with LM8_LIE A.22 (sweep1_tower CROSS_RUN_EDGES.tsv).
5. **Ghosts.** SECTION_GHOSTS, GT_TOWER_CHECK Part C (C.1-C.5 and the sub-rows), SECTIONS_OVER_Q A.32, A.44, A.65,
   A.72, A.196, EXIT_TOWER E.46 ("the element of E.46 is a ghost of GT̂₀", GT_TOWER_CHECK Lead 6), LM8_PUSH B.6
   ("Ghost values require the actual composition law"), DELTA_ON_GT A.39, A.151. One concept or several? Write the
   definitions with locators, and the cluster's statuses: GT_TOWER_CHECK C.1-C.5 are Open in the register; the
   SECTION_GHOSTS final audits 90 earlier claims. What is the current status of each?
6. **CYCLOTOMIC_KERNEL (tower) and the 149 chain (sections).** ANABELIAN_149_PUSH D.2 and B.15u use CYCLOTOMIC_KERNEL
   E4 (Open); LM6 F.13 (Proved) uses CYCLOTOMIC_KERNEL B8 (Refuted); ANABELIAN_149_PUSH D.U2 (Unresolved: "every
   continuous section of G_Q(t) to G_Q lies in the decomposition group of a rational place") against LM6 F.13. Sound
   uses? Does LM6 F.13 settle D.U2?
7. **LM5 and LM8 on punctured neighbourhoods.** LM5 F.12 (Proved: classical punctured neighbourhoods form a pro-topos,
   covering germ BZ^r) against LM8_LIE_APPROXIMATIONS E.11 (Refuted: the literal inverse 2-limit of the small topoi of
   shrinking punctured disks is degenerate). Consistent? And LM6 F.43 uses LM5 F.22 (Refuted).
8. **Involutions and real components.** LM4_SUCCESSOR's prompt row R8 (LM6 C.13-C.19, unrefereed) and LM6 C.12
   (involutions for g ≥ 3, Open) against LM4/LM4_SUCCESSOR's involution results.
9. **LM7_PUSH's lifting theorems in the tower runs.** LM4_SUCCESSOR A.18, A.28, B.45, B.54 say that LM7_PUSH D.50/E.58
   ("R2" in their prompt) do not admit an unrestricted or universal strengthening. Is that consistent with how
   DELTA_ON_GT, GT_TOWER_CHECK and FERMAT_SUCCESSOR use D.50/E.58?
10. Then go through the rest of the 653 edges by script: list every edge whose two ends have statuses that cannot
    both stand (a proved row using an open or refuted row of the other scope; a row that restates, checks or
    refines a row with another status), read the ones that are not obviously sound, and record the verdicts.

Write FINDINGS.tsv, CLUSTERS.tsv, CHECK_EVENTS.tsv and REPORT.md as the common brief says.

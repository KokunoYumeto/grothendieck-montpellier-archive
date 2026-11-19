# Hunches and ideas that are not yet in any prompt (17 Nov 2026, ~00:4x-01:0x UTC)

Main session (Claude Opus 5.5 at effort max), at the user's word (17 Nov ~00:4x-01:0x UTC): [the user's words, omitted]. Method, without model compute:
- the sources read: my queues (claude_math_notes/FOR_ASTRA.md, FOR_FABLE.md), the debate's consolidated register
  (pro_intake_20261114/debate_20261114/CONSOLIDATED_REGISTER_20261114.md, its hunch map and "unplaced" rows), the war
  game's hunches (grothendieck_archive_montpellier/WARGAME_MATH_HUNCHES_20261112.md, H1-H9), the prompts tally, and the
  new items of 17 Nov;
- each item was searched by its key phrases in all 37 prompt files (sent and unsent);
- a keyword hit is not proof of placement and a miss is not proof of absence, so each row says how sure it is.

## Not in any prompt

| Item | Source | Search | Proposed home (one prompt per cluster) |
|---|---|---|---|
| ANABELIAN A1 check items K1-K6, a second reader of AG.41, Wakabayashi 2016, Mochizuki 2007/2014 vs AG.39; A3, A10 (c), the open F-items | EXPERT_A1_ANABELIAN_20261117.md; LITERATURE_A1_MAIN; A1_downstream_scope_assessment.md | new 17 Nov | **the anabelian-cluster successor (to write; an account-2 candidate)** |
| War game H1: the centralizer theorem for every subgroup with no invariants in Tate modules (sharpens S6/R2) | WARGAME_MATH_HUNCHES H1 | 0 hits | GT tower follow-up, after GT_TOWER_CHECK returns (centralizers: the Boggi-Zalesskii step lives there) |
| War game H5: on PSL₂(F_q), GT₀ and Galois differ only by a character with values in Out; LM2 B.f5 (trace triples) | H5; register row 52 "unplaced" | 0 hits | the same GT tower follow-up |
| Dictionary S8: Mathieu groups, additive polynomials (LM8 B.24d) | register row 50 "unplaced" | 0 hits | the same, or the LM8 line's next prompt |
| War game H6: the localizer of finite-dimensional local systems is fundamental, and its localization is schematization (sharpens S11; **false as stated**: S²→* lies in W_fd while H²(S²;k) = k, so the corrected statement goes in, follow-ups @270 below); Derivateurs hunches H2, H9 (tally row 20, "to write" since 12 Nov) | H6; register row 53; MATHS_PROMPTS_TALLY row 20 | 0 hits | **one Derivateurs successor after FINMON's final**, together with DER_OPEN_ROWS and FINMON's open rows |
| DER_OPEN_ROWS: REVLOC D.2.4, D.3.2; the S² frontier (S2COUNT E:E2-E4) | NEW_PROMPT_ITEMS_20261117.md (a5ead5c6) | new 17 Nov | the same Derivateurs successor |
| War game H7: the compatibility left open in cote 47 follows from linearity over the Ext-algebra of the unit section | H7 | 0 hits | the transcription or second-pass package of cote 47, as a standing question; or one archive-hunch prompt |
| Astra A4: the Ramanujan signatures 2, 3, 4, 6 (groups, Hauptmoduln, periods, transformations; the CM-point identities for signatures 4 and 6) | FOR_ASTRA A4 | 0 hits | the companion's dictionary work, or the S6 line's next prompt |
| Astra A1: general A.3 through Hecke characters of weight -1 | FOR_ASTRA A1 | 1 weak hit (LM4_SUCCESSOR) | the SECTIONS_OVER_Q / LM8 line's next prompt; check placement first |
| Astra A2: Archimedean regulators of the tripod's Kummer classes (Kronecker limit formula at the cusps of Γ₀(4)) | FOR_ASTRA A2 | 1 weak hit (FERMAT_SUCCESSOR) | the same; check placement first |
| Fable F12-F16 (S6: cusp order of an eta-quotient, the CM-type reading, GT₀'s frames on local twists, the gerbe class, the corner and 3^{1/4}); F17 (two refuted steps in other people's papers, to check before anyone is told) | FOR_FABLE | Fable questions, not Astra prompts | Fable after the reset, on the user's OK; F17 before any outreach |

## Probably placed (hits; not verified line by line)

- War game H2 (vanishing cycles): ANABELIAN_149_PUSH, EXIT_TOWER, LM6.
- H3 (two-level principle): EXIT_ONE_TYPE.
- H4 (déploiement as the oriented blow-up): EXIT_ONE_TYPE, EXIT_TOWER, LM5, LM8_PUSH.
- H9 (cote 44, Mordell-Weil): several hits, but on other uses of the name; check.
- Astra A3 (P(3,4)) and A5 (Siegel values): in S6 prompts.
- LM6 A.32/A.40/A.45: hits in GT_TOWER_CHECK, EXIT_TOWER and FRAISSE_EXACT, possibly other statements with the same
  numbers; check.

## What this means for the prompt count (parsimonious with prompts, not with mathematics)

Four consolidated prompts would take everything above that is ripe:
1. the anabelian successor (now);
2. the GT tower follow-up (after GT_TOWER_CHECK returns: H1, H5, S8);
3. the Derivateurs successor (after FINMON's final: DER_OPEN_ROWS, H6, H2/H9);
4. the S6/companion dictionary items (A4, with A1/A2 where they are not already placed).

H7 rides with the cote 47 package. Account 2's six prompts go to the hardest of these: 1, 2 and 3 are candidates.

Updated 17 Nov ~02:5x UTC: with the follow-ups reader's research items, six consolidated prompts; see the last section.

## Follow-ups proposed in the Pro transcription notes (scan of 17 Nov ~00:4x-01:0x UTC; titles only, entries not yet read)

From `grothendieck_archive_transcription_20261110/notes_crosslinks_20261117.tsv`: 120 entries of kind "own idea" or
"unpursued implication" point beyond their own cote. Most are internal checks of Grothendieck's pages (the E6 and E8
tables, sign and length conventions in MPL_33's chat B; the filtration statements in MPL_62's part D). Those go to the
editions and the second passes, not to research prompts. The ones that bear on our open questions, by cluster:

- **Points as sections, LM6 / SECTIONS_OVER_Q / A1:**
  - MPL_15_195-228+18_002-017: B05 (the open LM6 normalizer item needs an additional character step); B04 (non-Tate
    weights give a precise cuspidal-inertia criterion); M11, P14.
  - MPL_144_001-061: N005.5 (relation to the end of cote 149 §4); N047.2 (periods, base points, inertia generators).
  - MPL_62_002-050: C20 (finite geometric normalizers do not decide the profinite questions; LM4/LM6/LM7/LM8); C21 (a
    section of a conic bundle is not an arithmetic section classification).
  - These go to the anabelian successor (03_ANABELIAN_A1, being drafted) or SECTIONS_OVER_Q's successor.
- **The tower and the five-point diagram (EXIT_TOWER / GT_TOWER_CHECK):**
  - MPL_146_001-099: R098 (boundary units turn the five-point calculation into equivariant Picard cohomology), R034
    (from the path drawing to a presentation certificate), R107-R112 (local coefficients, π₂ of the base).
  - MPL_156-1+156-2: P02, P15 (EXIT_ONE_TYPE).
  - These go to the GT tower follow-up.
- **Les Dérivateurs:**
  - MPL_105: R32 (a focused continuation), R09, R16, R24, R26, R28 (BISITE, PATHS, RESIDUE, STRATA, TOTASPH).
  - MPL_31_002-051: N043 (a concrete descent comparison: BISITE, LM7, RESIDUE; cote 33).
  - These go to the Derivateurs successor after FINMON's final.
- **Group schemes and descent (LM1 line):** MPL_131 RN070 (the open integral group-scheme descent problem), RN084-RN085
  (large-monoid convolution: LM4/LM7); MPL_15_195 A36.

These entries also reach the packages of the cotes they cite, through the "What other packages' research notes say
about these cotes" section of the results block (17 Nov).

## The follow-ups reader's 41 research items, routed (17 Nov 2026, ~02:5x UTC)

Full statements: `field_experts/FOLLOWUPS_FROM_NOTES_20261117.md`, by @number. Placement search:
`followups_work_20261117/placement_20261117.py` -> `PLACEMENT_20261117.tsv`. It covers the 37 maths prompt files of
TO_SEND folders 1, 2, 8 and 9, sent and unsent, with distinctive phrases per item. Hits were read in context; generic
citations (Stix, Hoshi, "exit path") were not counted as placements.

Six consolidated prompts take all 41 items together with the earlier hunches. Two of them are new clusters that no prompt
touches.

**1. The anabelian successor** (after 03_ANABELIAN_A1 returns; with its K-items and open F-items). Neither item is in any
prompt:
- @770: LM6 A.22 (the full CM group) through Stix 2012, Thm 30 and Cor. 31 (cote 14).
- @1404: the point-to-section Kummer compatibility in the generalized-Jacobian bridge (cote 43; FLAGGED_149 B5, LM6
  F.35).

**2. The GT tower follow-up** (after GT_TOWER_CHECK returns; with H1, H5 and S8).
- Not in any prompt:
  - @435: the recognition problem for the Galois image (142/090-100);
  - @603: the "meilleur exposant" table (146/071-073; Michel Hua's project's claim, credited to it);
  - @605: the five-point calculation as equivariant Picard cohomology (146/074);
  - @731: the "non-formel" gluing of the normal-torus torsor groupoids (147/121-137);
  - @173: the face maps of 121/041-047 by a normal-crossing boundary;
  - @355: the algebraic enlargement by Hurwitz stacks (142/018-021);
  - @459: the "structure combinatoire" at infinity (144/005);
  - @516: the five-point word comparison with the pentagon (144/177; 148/018-039);
  - @553: the coherence of the local graph models (146/003-018);
  - @570: a presentation certificate for 146/020-033;
  - @654: our counterexample to Knudsen 1983, Cor. 3.9(b) read globally, to settle before anyone is told;
  - @679: every subgroup of S4 from a stable decorated graph (147/058).
- Already asked in runs that have run. Ask only what their returns leave open:
  - @684: the strata of modular dimension <= 2 (147/060, 148/063); EXIT_TOWER item 13, EXIT_ONE_TYPE;
  - @672: the GT-hat action on the MD-graph category; EXIT_TOWER item 1, and GT_TOWER_CHECK cites Lochak et al. 2026;
  - @524: the mu-multiple at a boundary point (149/077-079); FLAGGED_149;
  - @550: the extra kernel of the filling map (LM1 D.7); in the background of LM6 (B.4-B.10).

**3. The Derivateurs successor** (after FINMON's final; with DER_OPEN_ROWS and the line's H2/H9):
- @4: the W7 bis/W8 bis localizers and homology localizers; it reconciles NEW_RESULTS 7 and 8 with REVLOC's final.
- @8: TC = C∩W, and the reverse excision axioms repaired so that they survive every shift D_I.
- @270: **H6 corrected.** The war game's H6 is false as stated, because S²→* lies in W_fd while H²(S²;k) = k. The
  successor asks the corrected statement, with derived categories or cohomology of finite-dimensional local systems
  (cote 133; Pursuing Stacks §110).

**4. The S6/companion dictionary** (A4, A1/A2): no follow-up items.

**5. New: Grothendieck's tame topology (Esquisse §5-6 and §8), one prompt** (cotes 39, 120, 121, 150-152, 154, 156).
No prompt touches these items:
- @160: his tame axioms against o-minimal structures (cotes 120 and 121);
- @210: tame homeomorphism groups against PL homeomorphism groups (121/073);
- @835: equipped conical stratified systems and exit paths (150/022-043);
- @168: the fibres of locally trivial proper tame maps (121/028);
- @935: simultaneous triviality of finite diagrams (120/025);
- @1387: his axioms for families of power series (cote 39), with Michel Hua's project's conjecture
  39-inverse-function-axioms-henselian, credited to it;
- @944: the surface of relative positions of a pseudoline arrangement (154/151-176), with Michel Hua's project's
  conjecture 154-generisation-cube, credited to it and to be reconciled;
- @1008, @1003, @1039: networks and ficelles (cotes 156-1 and 156-2).

His pages still waiting: P063 (154_001-045), P065 (81+154_046-076) and SP04_CW_156-4+156-6. Sent early, they give the
prompt all his pages.

**6. New: cycles, motives and integral structures, one prompt** (cotes 11, 14, 44, 56, 131, 133, 136, 153, 155). No
prompt touches these items:
- @792: the Albanese-equivalence quotient (14/024-039), with Michel Hua's project's finding
  14-albanese-equivalence-ring, credited to it;
- @1146: "A prouver que cette dernière est positive !" (44/008-009; war game H9);
- @120: Poincaré power systems (11/034-042), with Michel Hua's project's conjecture, credited to it;
- @145: the vanishing class carried into a Lefschetz pencil (cote 56; 44/004);
- @237: "Exprimer la rigidité de C !" and Hopf algebroids (155/002-010);
- @247: cote 131's representability criterion and Murre's algebraic representative;
- @305 and @304: the 1976 integral PD de Rham theory of simplicial sets, and binomial rings (cote 136), with Michel
  Hua's project's finding 136-pd-de-rham-shadows, credited to it;
- @215: analysers and plethories (153/003-006);
- @254: LM1 D.11 through cote 131's recognition lemma.

His pages still waiting: P062 (14_045-086), P081 (136_002-046), P047 (136_282-327) and P101 (136_328-376). Sent
early, they give the prompt all his pages.

**Order of readiness:**
- prompt 1, when 03_ANABELIAN_A1 returns;
- prompt 2, when GT_TOWER_CHECK returns;
- prompt 3, when FINMON's final comes;
- prompts 5 and 6, when their waiting packages return;
- prompt 4, at any time.

Account 2 has six slots, at most two at a time; accounts 1 and 3 have one or two maths slots. The user chooses which
prompt goes where.

## The claims pass's nine research items, routed (17 Nov 2026, 04:17 UTC)

Source: `field_experts/CLAIMS_FROM_NOTES_20261117.md`, where #n is the entry's number in the claims map. The follow-ups
reader (Claude Opus 5.5 at effort max) read Grothendieck's unproved claims and conjectures that no note ties to our
runs: 1,137 entries, 9 research items. It searched PROGRAMME_MAP and HEADLINE_RESULTS by grep and found none of the nine
among a run's results or open rows.

- **Prompt 1, the anabelian successor:** #468, the injectivity of G_K → Out(π̂₁) for a hyperbolic curve over a field
  finite over its field of moduli (142/096). Check Hoshi-Mochizuki 2011 first.
- **Prompt 2, the GT tower follow-up:**
  - #309: his "enveloppe profinie" of the category of hyperbolic surfaces with finite covers (142/009-017); with @355.
  - #328: whether an endomorphism with a unit multiplier is an automorphism (142/025; in GT-hat terms, whether
    (λ, f) with λ a unit is invertible). Check Drinfeld, Ihara and Schneps first.
- **Prompt 5, tame topology:** **#133, rank 1**, his mobility stratification (A)-(D) and Conjecture 1 (121/026-028,
  034), and the relative form for proper maps (121/036-037); with @160 and @168.
- **Prompt 6, cycles, motives and integral structures:**
  - #243: the automorphisms of the PD de Rham functor (136/162-188), with Michel Hua's project's
    136-automorphism-group-scheme, credited to it; with @305.
  - #964: places classified by torsors under the integral motivic group (15/207-227).
  - The two group-scheme items: #189 (cote 131, condition 8°, with @247) and #1039 (the converse SGA 3 X §5.11 bis
    leaves open; cote 31).
  - The quadratic-algebras item #1264 (84/121) rides here too. It is the only item of its kind, too small for a prompt
    of its own.

Through the results block, the items also reach the waiting packages whose cotes they name: #243 reaches P081,
P047 and P101 (cote 136); #964 reaches P085, P033_251 and four second-pass blocks of SP14 (cote 15); #1264 reaches
P113 and P173 (cote 84); #1039 reaches P099 (cote 31).

## The gap pass's six research items, routed (17 Nov 2026, 05:13 UTC)

Source: `field_experts/GAP_FROM_NOTES_20261117.md` (gN = the entry's number in NOTES_GAP_ENTRIES_20261117.tsv). These
are the 1,772 note entries both earlier passes missed, because their kind was written otherwise.

- **Prompt 1, anabelian:** g1276, "A t-on une réciproque ?" for elementary U (149/120). Check the rows of
  ANABELIAN_149_PUSH and FLAGGED_149 first.
- **Prompt 3, Dérivateurs:** g6, his "Thm(?)" for linear coefficients (134-8/048-054). It bears on GALOIS G.6 and
  RESIDUE I.7.
- **Prompt 6, cycles:**
  - g1048: multiplicativity of the weight localization over Γ_k(T) (136/244-281). The reader's own unchecked
    computation says the naive structure does not descend.
  - g1004: the uniqueness conjecture for admissible integral PD de Rham theories (136/111-121); with #243.
- **New, POLY (regular polyhedra over rings, Esquisse §4):**
  - g1557: his pinned regular hyperpolyhedra and the equivalence of 72/077, once the two normalizations of 074-075
    are repaired;
  - g1558: is the level-N regular polyhedron the Farey map on X(N), and with which congruence kernel (72, Bridge B5)?

  These wait for cote 79, whose six packages are queued and now carry g1558 in their results blocks. Then they
  become a prompt of their own, or the Esquisse §4 part of the tame-topology prompt.

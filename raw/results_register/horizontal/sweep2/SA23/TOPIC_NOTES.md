# SA23, horizontal sweep 1: topic notes (18 Nov 2026)

Written by Claude Opus 5.5 at effort max, sub-agent of a0c4bb37 for SA23, between 14:40 and 15:00 UTC. The codex notes on the sheets of the 36 K folders were placed from 15:28 to 15:35 UTC, at the broad agent's request.

## Sources
- **Pro notes:** the four packages MPL_22+23_002-016, MPL_2, MPL_68_033-056+162-1+162-6 and MPL_93_221-236+161-5 (326 index rows). They come from ChatGPT Pro mode; the project calls the model GPT-6 Astra (ChatGPT Pro mode), and the package lines I read do not name it.
- **Work and Codex-web math notes:** 37 files, 6 units each (222 units). The table `codex_web_20261113/AUDIT_K_RETURNS_20261118_luaul2.tsv` names GPT-6.2 Astra Max (effort max) for 15 of the 37 folders. It does not give the model of the other 22.
- **Extra entries:** the codex transcription notes of H26-01 (cote 26) and HC1-01 (cote 1), 4 entries. These folders have no Work math notes. The brief does not require them, but cote 26 is the only EGA VI material in the topic.

## What the notes cover
SA23 is not one subject. It holds eight clusters:
1. **Cote 1, 1950s functional analysis** (light; Work and codex notes only): Hilbert tensor products, Fredholm determinants and trace-class operators, singular-value inequalities and Schatten norms, entire functions, power series on l1. Items SA23-1 to 5.
2. **Cote 2, the Riemann-Roch "notes antiques"** (heavy; MPL_2, 92 entries): the class group of a curve, Chern classes in K, K-groups with tensor and exterior operations, the lambda-ring and Chern-ring comparison, K-theory with supports, Riemann-Roch for curves and surfaces. Items SA23-6 to 11, 46 and 48. The lambda/gamma cluster SA23-8 (21 entries) is the core. It is read against two of Hua's register IDs.
3. **Cotes 21-23, the EGA drafts and offprints** (heavy for 22-23; MPL_22+23 has 82 entries, and the Work notes of K21-K23 are light):
   - 0_III vanishing tests and the extension of sections (21);
   - the 1963 offprints on differentials and the trace/norm typescripts (22);
   - formal smoothness and Cohen algebras, his questions 1-4, derivations, and the counterexample on 22/027-029 (22);
   - conormal determinants and the elliptic example, and the Cartier theory of formal groups (23, scans 2-16);
   - Greenberg, connections, the corrections for EGA IV 11, the Zariski Main Theorem outline, dimension theory (23, scans 17-99).

   Items SA23-12 to 27 and 47.
4. **The EGA plan** (cotes 22-23 plan entries; cote 26, EGA VI plans and "Problèmes-types à résoudre"): SA23-28.
5. **Cotes 161-1 to 161-4, his dossiers on categories, universal algebra, topoi and an introduction to algebraic geometry** (light; Work only): adjunctions, delta-exact envelopes and theories, ring objects in topoi, products of topoi, faithfully flat descent. Items SA23-29 to 33.
6. **Cote 161-5, Barsotti-Tate:**
   - Serre's printed 1967 paper and his 1968-69 course résumé (SA23-34, 35);
   - Grothendieck's manuscript notes on crystalline realisations, filtered torsors, descent and Frobenius data (SA23-36, 34 entries, heavy).
7. **Cotes 161-6 and 162-5:** icosahedral geometry (SA23-37); Quillen's "tapis", formal categories over a scheme (SA23-38).
8. **Cotes 68 and 93, outside SA23's cote list** (flag F11): 92 entries came in with the packages that hold 161-5, 162-1 and 162-6. They cover:
   - cote 68: games, the nilpotent exponential, orientations and graded determinants (SA23-39 to 42);
   - cote 93: Picard-Fuchs equations, crystals and stratifications (SA23-43 to 45).

   They belong with the topics of cotes 68 and 93. Cotes 162-1 and 162-6 have no transcription in the inputs. They are reached only through Hua's modernised readings. Cotes 24 and 25 (EGA V) are API transcriptions without notes, "other part" in TOPIC.md.

## Light and heavy
- **Heavy (Pro):** SA23-8, 9, 17-22, 36, 40, 44. Each has 15-35 entries with their own calculations, counterexamples and comparisons with Hua's modernised readings.
- **Light:** the cote 1, 21, 161-x and 162-5 folders. Each has one Work file of about 2,000-2,700 words in six standard units.
- **Units:** a Work unit ("What the pages do", "Slips") spans several objects. A Work row's `item` can therefore list several items, separated by commas.

## Counts
| | |
|---|---|
| entries | 670 (326 Pro notes + 42 Pro records + 222 Work units + 80 codex; sweep 2 added 46 gap entries) |
| items | 57 (SA23-49 to 54 opened in the codex pass, SA23-55 to 57 in sweep 2) |
| basis | index-row 634, entry-read 19, passage-read 17 |
| fidelity | agrees 16, misreads 1, not checked 653 (codex:K1-03#2 repeats the transcription's misreading "degrés" for "classes", decided on the scan) |
| flags | 16 (F01-F16), on 179 placement rows |
| check events | 27 in all for SA23: 18 in sweep1/SA23, and 9 in sweep2/SA23 (4 for the gap entries, 5 for the scan readings) |

The Work units were placed from their opening lines (the "worksummary"), and their basis stays index-row.

## What was checked (all agree with the transcription)
- **P22 E03 and K23-06 R1, the elliptic example on 23/005:** det E = L^5 and M = L^6. Two models agree, and so does the page.
- **P22 A27, the counterexample on 22/027-029:** the manuscript part agrees. The literal printed EGA 0_IV 22.5.10(i) would indeed give Upsilon = 0 (F01).
- **P2 L03:** the sign in Proposition 2 against its proof (F06).
- **P2 L08:** "φ_K tjrs bijectif ??? Non" with K(P^{n-1}).
- **P68 E14:** his live NB on gr_J(A) is false; the counterexample was rechecked.
- **P93 B06:** the positive twist on 161-5/026 (F03).
- **K161-6-02 S18:** "4π/5 < 2π/3" as transcribed (F02).
- **K161-2-06 and K161-2-06_2:** compared by diff (F08).

## The codex notes on the sheets (added 18 Nov, 15:28-15:35 UTC)
Each of the 36 K folders has a codex notes file of two units:
- **His marks of doubt and unfinished steps:** placed in the folder's mathematical items.
- **Titles, dates and page counts:** placed in documentary items. Cote 1 is SA23-49, cote 21 SA23-50, cotes 161-1 to 161-4 and 161-6 SA23-51, cote 162-5 SA23-52, cotes 22-23 SA23-47 and 161-5 SA23-34/35.

K22-02 uses top-level headings; its two sections are its units. All 72 units were placed from their opening lines.

What the codex pass adds:
- **Attributions confirmed:** the 1963 offprint is J.-P. Jouanolou's CRAS note (t. 257, 2948-2950, 13 Nov 1963), as the Pro note O01 says. Checked on the page.
- **One mark, three notes, two transcriptions:** "séries formelles ??" is in both independent transcriptions and in three notes. Checked.
- **Serre's p. 131:** he deduces that I is open and has no direct proof. Three notes agree, and so does the page.
- **His objections in pencil** on Jouanolou's note: "faux si on ne suppose pas A → B injectif ??", "C ⊃ A !!!", "faux" (SA23-15).
- **Refined items:** the cover title "Fibres des morphismes plats de présentation finie" (23/091, EGA IV 12) for SA23-27, and "Fibrés des germes d'ordre n de sections" (23/018) for SA23-23.
- **New items from headings:** "Catégories accessibles" (161-2/056, SA23-53) and "Topos modulaire" (161-2/112, SA23-54), with flag F13.
- **F12:** the heading "degrés remarquables d'opérateurs compacts" (1/082) may read "idéaux".

## Sweep 2: the gap entries (18 Nov 2026, from about 20:15 UTC)
Placed by Claude Opus 5.5 at effort max, sub-agent of a0c4bb37 for SA23, in sweep2/SA23/.

The 46 entries of GAP_INDEX.tsv:
- **MPL_2 research leads (41):** the leads recorded during transcription, one per scan. They are working hypotheses, not final conclusions. Each is placed by its scan in the cote-2 items 6-11, 46 and 48.
- **The pointers file of MPL_1_002-050 (1):** cote 1 scans 5-50. That package has no notes file.
- **The Codex notes on the sheets of H162-01 and H162-02 (4):** H162-01 is cote 162-1, the list of papers lent. H162-02 is cote 162-6, a sheet headed "Gal(E/ℚ) – C(E)".

**Items opened:**
- SA23-55: the "Papiers prêtés" list (162-1), with dates 1964-1967.
- SA23-56: Gal(E/Q) and the idèle class group C(E) (162-6). It links to SA23-41/H0DV through P68 X01.
- SA23-57: traces on rings of operators and the determinant Δ(A) = exp ∫₀^{T(1)} log φ_{|A|} (cote 1), the Fuglede-Kadison determinant in today's terms (F14).

**Items changed:**
- SA23-11: now names the reused typescripts. The five Pro entries on the reused sheets of scans 34, 36 and 39 (MPL_2#46, 47, 59, 60, 61) moved there from SA23-9.
- SA23-10: status from scan 45 (F15).
- **Global tags:** cross_topic of every item now names its global tag (55 tagged; 55-57 are new).

**Checks (4), all agreeing:**
- the determinant quotes on 1/28-29;
- the sign lead on 2/022;
- the elliptic counterexample on 2/014;
- the O_C lead on 2/045.

**New flags:**
- **F14, a link across folders:** the determinant Δ of cote 1, to his Fredholm determinants and to Fuglede-Kadison.
- **F15, a suspected misreading:** on 2/045, "O_C" against the normalization; otherwise a δ correction is missing.
- **F16, a link across folders:** cote 1 scans 4-40 were transcribed twice, by MPL_1_002-050 and by HC1-01.

**For sweep 3:**
- compare the two cote-1 transcriptions;
- read the scan of 2/045;
- take up his question on 1/30, "Δ(B*HB) ?= Δ(A*A)Δ(B*B)".

## Sweep 2, part 2: readings decided on the scans (18 Nov, 21:55-22:05 UTC)
Report: results_register/horizontal/sweep2/REPORTS/SA23_scan_readings.md.

- **F12, decided:** the heading on 1/082 reads "classes remarquables d'opérateurs compacts", a misreading of "degrés" in the transcription.
- **F15, decided:** 2/045 names O_C. It is his slip: his right side is c_2(f_*O_C~) = C^2 - delta, while c_2(O_C) = C^2.
- **F01, read on the scan:** his counterexample on 22/027-029 is as transcribed and correct. The printed EGA 0_IV 22.5.10(i) remains to be read on the printed page.

## Lens
No note in SA23 reads the topic through La Longue Marche or Les Dérivateurs:
- P68 S02 and the MPL_2 scope paragraph examine the LM7/LM4 items of the supplied RESULTS_STATE and set them aside.
- The research-run links that remain (P93 X05 to C30 of MPL_93_002-046) are cote-93 links (F05).
- The notes compare with Hua's modernised readings throughout, which are an outside witness. F03, F04 and F06 record where they disagree.

## For sweep 2, first
1. **F01:** check EGA 0_IV 22.5.10(i) on the printed page (IHÉS 20, p. 204) and in our EGA editions. If the print is as quoted, his manuscript (22/027-029) gives the working example, and the editions need a note.
2. **The Hua disagreements on 161-5 scans 23-29 (F03, F04) and the sign in cote 2 (F06):** read the scans, with the twist superscript first.
3. **Pages read twice:** cotes 22 and 23 scans 2-30 were read by both the Pro package and the Work notes K22-01, K22-02 and K23-06. Compare them entry by entry; this is the cheapest source of independent check events in the topic.
4. **F02:** the scan of 161-6/018.
5. **The cote 2 lambda cluster (SA23-8):** check the notes' own mathematics (L02 countermodel, L10, L11, the n = 3 witness) against SGA 6.
6. **Routing:** move SA23-39 to 45 (cotes 68 and 93) to their home topics, and give cote 26 (EGA VI open problems) a math-notes pass. It has none.
7. **Links:**
   - F07, Cartier in cote 23 and the exponential in cote 68;
   - F09, Quillen 162-5 with cotes 93 and 161-5;
   - F10, the EGA plan in cotes 26 and 25.

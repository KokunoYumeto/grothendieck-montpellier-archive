# The Montpellier archive: where it stands, what finishes it, and how everything is one project

Main session 329fb1e6 (Claude Opus 5.5 at effort max), 23 Nov 2026, 18:5x UTC. The user (23 Nov 17:02 UTC): [the user's words, omitted]
Counts come from [STATE.md](../STATE/STATE.md) (rebuilt 23 Nov after the SP102 final and ten Work returns were filed);
quote them with that date.

## In one paragraph

The first transcription is finished except 77 pages of Les Dérivateurs (157-5), which are with ChatGPT Work. The second
pass covers a fifth of the pages (3,250 of 15,597, La Longue Marche all of it). It is the layer that decides how good the
text is, and it is where the remaining work is. Seventy-one second-pass prompts are built and lint-clean (1,483 pages).
Sending them finishes ten readers that are built and waiting. The other 10,863 pages need about 363 more prompts: about
1,060-1,165 Pro run-hours, roughly a week and a half of round-the-clock sending at four runs at a time.

This week's audits say how to make those passes accurate (the error sheet, the crop rule, a third witness, the
refinement loop); every waiting prompt already carries the result. The mathematics that grew out of the archive is now
one map: each research line has its roots in named cotes, and its results go back into the readings of those cotes.

## 1. Where the archive stands, layer by layer

The user's horizontal plan of 17 Nov ([PROJECT_RECORD.md](../PROJECT_RECORD.md) §0) has five layers.

1. **First transcription: done, except 77 pages.** 15,520 of 15,597 pages with writing have at least one reading, and
   2,686 have two or more. The 77 are Les Dérivateurs 157-5:
   - Work folders K157-5-15 and -16 are sent;
   - K157-5-30 to -32 wait in TO_SEND.
2. **Second pass: 3,250 pages (20.8 %).**
   - La Longue Marche has 1,583 pages, compared with the typed editions twice or more; the other cotes have 1,667.
   - Ready to send: 71 prompts, 1,483 pages.
   - Nothing prepared: 10,863 pages.
   - The audit is in [SECOND_PASS_AUDIT_20261123.md](../reports_20261123/SECOND_PASS_AUDIT_20261123.md), and the
     measurements in [SECOND_PASS_ACCURACY_MEASURES_20261123.md](../reports_20261123/SECOND_PASS_ACCURACY_MEASURES_20261123.md).
3. **Pro's notes worked through, per folder.** This is barely begun: the pilots of 18 Nov
   (`working_through_20261118/`) and the sweeps' readings of the research-heavy cotes.
4. **A first mathematical reading of every folder.**
   - The Stage A topic dossiers came back for 26 of the 29 topic groups (SA02-SA29; 18-19 Nov,
     `stage_a_20261118_sent/returns/`).
   - Sweep 3 wrote study notes for 22 of them (`results_register/horizontal/sweep3/SAnn/STUDY.md`).
   - This layer exists by topic. Folder by folder it is thin outside the research lines.
5. **Readers.**
   - Released, from our reading:
     - La Longue Marche, seven books in French and English (two French books final, five working drafts);
     - EGA V;
     - the Esquisse (part of cote 119);
     - Pursuing Stacks.
   - Released from the printed edition's text, not from our reading of the manuscript: Les Dérivateurs.
   - Built and waiting for their second pass, ten readers:
     - the Montreal seminar (129);
     - the Tapis de Quillen (162-5);
     - Local Picard schemes and the Murre letters (57);
     - Ramification (29);
     - Griffiths, SGA 7 (36);
     - the SGA 3 VIB draft and tensor categories (10);
     - the re-editions of SGA/EGA (37);
     - typed motives (12 and 15);
     - typed groups (32, 45, 46, 123).
   - Every page of these ten is in a ready prompt.
6. **English (alongside).**
   - 1,397 archive pages are current English, besides La Longue Marche's 1,583 in its own edition.
   - 135 pages whose French changed are being brought up to date by diff, not retranslated: script for the drawings
     and formulas, the API only for changed lines.
   - Nothing is pushed or bound into readable volumes yet. That is the next step for the translation, once the 135 are
     current.

## 2. What finishes it, and what it costs

**In order:**
1. **Send the 71 ready second-pass prompts** (SP103-SP177).
   - They finish the ten waiting readers. At the median 10.6 pages an hour they take about 140 Pro run-hours.
   - They carry the error sheet of 23 Nov and the newest hand logs of their cotes (re-sheeted and linted 23 Nov, 94
     prompts).
2. **Send the 133 Work second-reading folders** (1,787 pages) once the Dérivateurs first pass is through Work (the
   user).
   - They are the third, blind witness. On the 86 pages where one exists, it flags 62-91 % of the corrections that no
     cheap check finds.
   - Each flag is a box for the Pro pass, which decides it on a crop. The Work reading never decides.
3. **Build the remaining ~363 second-pass prompts** with the rules of 23 Nov:
   - every manuscript page gets a full pass;
   - pieces of 24 pages, 20 where the doubt marks are dense;
   - one cote per piece, sent in order, so each piece starts from the hand log and notation of the one before;
   - filtered Work differences as boxes;
   - no light pass on typescripts until a 25-page typescript pilot has measured one.

   Order them by the readers they finish and by the cotes the research lines cite (§4).
4. **Close the loop after every wave.** File, rebuild, rerun the pattern and difficulty scripts, add a caution line to
   the sheet per recurring error class, re-sheet the waiting prompts, publish the reading aids. The steps are written in
   [knowledge/03_archive/second_passes_and_doubt_marks.md](../knowledge/03_archive/second_passes_and_doubt_marks.md),
   with a 270-page gold set to score each wave.
5. **Readers follow the passes,** cote by cote; each reader is built when its last page is second-passed. The English
   follows the same pages.

**Time.**
- The second pass is the long pole: about 1,200 Pro run-hours in all with the ready prompts. That is 12 days at four
  runs at a time, or 8 at six.
- The Work readings run beside it, on Work credits.
- The first-transcription remainder is days.
- The English of all second-passed pages costs about $0.04-0.06 a page on the Flex API: about $500-700 for the rest of
  the archive, unfunded today. Diff-propagation keeps later corrections cheap.

## 3. Where the archive's mathematics needs development

Grothendieck's own questions, answered or advanced by our runs, are on the
[Hexagon board](../field_experts/hexagon/HEXAGON_STATUS.md). 35 rows bear on the archive:
- 2 posted: S20 (cote 123) and H17 (La Longue Marche);
- 5 written;
- 8 one gate away;
- 9 two gates away;
- 6 moving with a running run;
- 1 held, 1 erratum note, 3 not worth a post.

The ones nearest to finishing, with the gate left:
- **Cote 44 (the 1964 programme).**
  - H04: Th. 5 fails as displayed and is corrected by one term. Gate: the scan-004 image check and the finished text.
  - S14a: counterexamples to the programme. Gate: coordinate with H11/JAC1964.
- **Cote 1, the Hilbert trace formula in his hand (S23b).** Gate: open the printed sources.
- **Cote 31, the persistent A.2 counterexample to his margin question (S12a).** Gates:
  - literature (Hasse 1925, Schilling 1950);
  - the sheet locator (84, not PDF page 85).
- **Cote 4 (8.6), plane curves in characteristic 2 (S15b).** Gate: a literature search, Hexagon included.
- **Cote 8.3, integral crystalline weak Lefschetz fails (S15).** Gate: a forward literature search and the polish run's
  final.
- **Cote 8:49, the two Lubin-Tate lattices agree exactly when e ≤ p (S15i, new 23 Nov).** Gates:
  - a re-proof by another model;
  - literature;
  - the run's final.
- **Cote 133, WG(BO_m) is special exactly when m ≤ 2 or k contains Q (S17b).** Gate: literature and the finished
  text.
- **Cote 149, the tangential-section question (H16); cote 154, the genus of the relative-position surface (P91c);
  cote 67, the capping map (S22a); cote 29 (S12c, S12d).** Each is two gates away.

What needs development, as distinct from writing up:
- **The archive's own open rows inside the running polish runs:**
  - POLISH_ALGEBRAIC_GEOMETRY: the Picard kernels, P90e;
  - POLISH_CRISTAUX: the wild inertia indices with E_p open, S15k;
  - POLISH_TOPOLOGY_PERIODS: 98 pending and 557 unverified rows of 1,028.
- **The folders no run has read mathematically.** Layer 4 is thin outside the research lines: 11 geometry and
  combinatorial topology (2,419 pages with no second pass), the de Rham complex (538), towards a geometry of forms
  (474), the descents (243). Their first mathematical reading comes with their second pass, as the plan of 17 Nov
  says. Their questions are not yet on the board because nobody has read them.

## 4. One project: every line has its roots in named cotes

The prompts that went out and the board rows, by the cotes they name (script `cote_index.py`, 23 Nov):

| Cotes | What they are | The lines that grew from them | Where the results went |
|---|---|---|---|
| 140-152 | La Longue Marche and around it | GT̂ and the tower; anabelian sections; Ihara | H17 and H06b posted; H07 written; DELTA23; prompt 95 (GT̂ after H17) |
| 16, 44 | the standard conjectures and Poincaré-Hodge algebras; the 1964 programme | sign-only purity (H01); the Hodge line (prompts 32, 37-46, 51, 70); JAC1964, C44_POS | H01 posted earlier; H04, S14a, H11; Hodge Papers A and B; prompt 70d |
| 12, 13, 15 | motivic Galois groups, motives (typed) | Connes and F₁ (ALP_CONNES), motives over finite fields (ARCH_ALG Part A) | prompts 68, 69; the split-zero programme (93) |
| 1 | functional analysis, his trace formula | TRACE_DET; the polish of topology and periods | S23b |
| 133 | λ-rings, representations of the symmetric groups | GCT plethysm and Kronecker (GCT_PLETH, GCT_KRON), ARCH_ALG Part A | S17b; the GCT notes H02, H02b, H20, H21; the P vs NP fleet (through GCT) |
| 123 | the 1969 letter to Kostant; integer-valued polynomials | ARCH_ALG; POLISH_TOPOLOGY_PERIODS | S20 posted; H08 (known) |
| 4, 8 | crystals | RESEARCH_SA17, POLISH_CRISTAUX | S15, S15b-S15l, S17a |
| 27-42 | SGA working papers (cd of affines, π₁) | RESEARCH_SA12, SA13, POLISH_ALGEBRAIC_GEOMETRY | S12a, S12c, S12d; P90a posted (Raynaud's question, from the same run) |
| 43-44, 57-60 | Picard and Jacobians | RESEARCH_SA14/SA19, JAC1964 | H11, S14a |
| 45-56, 62-64 | elliptic curves and abelian varieties | RESEARCH_SA16/SA18 | S06b and the CM line (H15, prompt 70d) |
| 69-101 | regular polytopes over rings; quadratic covers | RESEARCH_SA04, SA02 | in their study notes |
| 134 | Pursuing Stacks | the homotopy conjectures (inside prompt 76) | the released reader |
| 154, 66-68, 119, 137, 150 | relative position; capping; Esquisse; periods | POLISH_TOPOLOGY_PERIODS | P91a-P91d, S22a |
| 157 | Les Dérivateurs | the Dérivateurs line and its companion | the released reader (printed text) |

**How the newer lines track back.**
- **RH and GRH (Alpöge's theorem and our runs on it).** These enter the archive through the Weil conjectures and the
  standard conjectures (cotes 16, 44: purity and the Hodge index route), and through the motives cotes (12-15). The
  structural notes of 23 Nov put them on one ladder with Hodge, Connes's trace formula, K-theory and the Galois side.
  Four lines meet at one next rung: RH for a cubic Hecke character of Q(ω), a weight-one dihedral form (prompt 69).
  See `field_experts/structural_maps_20261123/`.
- **GCT and the P vs NP fleet.** These grow from the representation theory of the symmetric groups that cote 133 works
  in (λ-rings, plethysm), and from Hodge-theoretic and finite-geometric structures that map onto the fleet's open
  lemmas (the maps of 23 Nov). The fleet is an outlet for this mathematics, not a separate project.
- **The Hexagon notes are archive results.** P90a, S20, H09, H06b and H17 each come from a cote or from a run built on
  one. The ones still on the board are listed in §3 with their cotes.
- **S6 is the one line not from the archive** (complex structures on S⁶).

So finishing the archive (the second pass, then the readers) is also what grounds the research. Each folder's
first mathematical reading says which of our results it bears on, and each result gets its place in his work. That is
the user's [the user's words, omitted] of 17 Nov, and the map above is where the two now meet.

## 5. The plan for the next days

1. **Send.** The 71 ready second-pass prompts as Pro slots allow, alongside the research prompts waiting (68, 69, 93,
   70d, 95, and the fleet prompt from session 672ae3a0).
2. **Build** the next second-pass prompts with the rules of 23 Nov, ordered by readers and by the cotes of §4.
3. **The typescript pilot** (25 pages), scored on the gold design. Then decide whether typescripts get a light pass.
4. **The Work readings,** once the Dérivateurs first pass is through.
5. **After each wave, the refinement loop** (§2, step 4).
6. **Readers,** cote by cote as their pages complete; then their English. The 135 translation pages are current once
   the diff propagation finishes.
7. **The archive's board rows** one gate from posting (§3): Hexagon from 00:00 UTC, five a day, by the posting rule.

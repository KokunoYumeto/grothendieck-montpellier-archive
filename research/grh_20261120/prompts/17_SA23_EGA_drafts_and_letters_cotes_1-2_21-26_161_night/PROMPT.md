**The attached files.** Besides this file there is one ZIP, `SA23_EGA_drafts_and_letters_cotes_1-2_21-26_161_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA23_study.zip` is the folder `RESEARCH_SA23_study/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# RESEARCH_SA23: Grothendieck's EGA drafts and letters, formal smoothness and Cohen factorizations, regular immersions, and the questions of his dossiers (cotes 1, 2, 21-23, 26, 161-1 to 161-6)

**What is to be settled.** Twelve Parts. The main question is Part A.
- A. Formal smoothness for the discrete topology (char 0 and char p), and the existence of Cohen lifts.
- B. Deligne's 1966 lemma, the Cohen factorization, with its open point on algebraic field extensions.
- C. Koszul-regular immersions.
- D. The EGA errata in the letters of 1966-68, item by item.
- E. The discriminant over a base.
- F. Differential functors of finite order.
- G. Graded flatness.
- H. Cote 1: Lidskii's trace formula from his steps, and the determinant Δ.
- I. Accessible categories and the classifying topos.
- J. The crystalline realisation of his cote 161-5.
- K. The "Problèmes-types à résoudre" of cote 26.
- L. His version of Quillen's theorem on formal categories and De Rham complexes (cote 162-5, 1968).

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA23`.

Drafted by Claude Opus 5.5 at effort max (agent a3d30d2d3a27966ed, the SA23 lead of sweep 3) on 19 Nov 2026, at the main session's word.

## What is attached
- **`RESEARCH_SA23_study.zip`:** the sweep-3 study of the topic.
  - STUDY.md, HUNCHES.md, RESEARCH_PACKAGES.md;
  - the readings A_161-1_161-3.md, A2_161-4_161-6_162.md, B_1_2_21.md and C_22_23_26_161-5.md;
  - `readings/SA04_reading_161-5_excerpt.md`: the 161-5 part of the SA04 study's reading of cote 93 and 161-5 (reader R1, Claude Opus 5.5 at effort max), with its check events SA04-R1615-01 to -03, its correction SA04-K1615-01 and the lead H1615-1;
  - CHECK_EVENTS.tsv and CORRECTIONS.tsv;
  - the sweep-2 tables OBJECTS.tsv and FLAGS.tsv;
  - the sweep-2 report on readings decided on the scans.
- **`RESEARCH_SA23_transcriptions.zip`:** the transcriptions (LaTeX) of the pages the Parts rest on, with the Pro notes of those packages: cotes 1 (scans 3-50), 2, 22, 23, 26, 161-2 and 161-5.

Each ZIP has a MANIFEST.tsv with every file's origin and SHA256. The transcriptions are AI-produced: Pro packages by GPT-6 Astra (ChatGPT Pro mode), Codex web folders by GPT-6.2 Astra Max. Struck text is marked `\deleted`, doubtful readings `\unsure{a|b}`, and his margins `\margin`.

## Where this comes from
- **The pages.** Grothendieck's pages in the Montpellier archive: his EGA 0_IV draft for Dieudonné (cote 22), his EGA IV complements with letters of Deligne (1966) and Lê Dũng Tráng (1968) (cote 23), the plan and open problems of cote 26, his functional analysis (cote 1), and his dossiers on categories, topoi and Barsotti-Tate groups (cotes 161-1 to 161-6).
- **The transcriptions and sweeps.** Our transcriptions are AI-produced. The sweeps were made by Claude Opus 5.5 at effort max (sweeps 1-3, 18-19 Nov 2026). The readings above re-derive his steps and record every check.

## Results this prompt builds on (status on 19 Nov 2026; check events in CHECK_EVENTS.tsv)
- **22/024-025, his Proposition.** K[[t_1..t_n]] with the discrete topology is not formally smooth over k when Ω_{K/k} is infinite-dimensional. Proved on the page; re-proved by the lead.
- **22/027-029, his Remarque and counterexamples.** K^p ∩ k = k^p while N_{K/k} ≠ 0. Correct, with a finite example, decided on the scans and re-proved. The printed EGA 0_IV 22.5.10(i) needs the root of the coefficient in K; the print itself is not checked.
- **22/010-018, §4 of his draft.** Corrections: Theorem 4.6(ii) reads C for B (decided on the scan); "formellement simple" is the later "formellement lisse".
- **23/006.** The discriminant degree (k−1)(r+1) is his slip. The true degree is (r+1)(k−1)^r, with weight k(k−1)^r in det E (decided on the scan).
- **23/083.** Lemma 1 1°): the corrected quantifier is "for some i, x vanishes on no top-codimensional X_k ⊃ Y_i".
- **23/060-065, Deligne's letter.** The counterexample to 0_IV 19.3.12 and the Auslander-Buchsbaum argument are re-derived; prime avoidance with arbitrary ideals is re-proved.
- **Cote 1 (reader B).** He states and proves Lidskii's trace formula on the crossed-out pages 79-80, from the summable eigenvalues and |α_n(u)| ≤ α_n(|u|), with a genus-0 lemma proved on 111-112. His question on 30 is proved for invertible operators.
- **Cote 161-5 (the SA04 study, reader R1; `readings/SA04_reading_161-5_excerpt.md`).** His Question on 161-5/029, whether all the sections α extending a given α₀ on π are conjugate under G'_S(S), has the answer no already in rank one. For G' = G_m, inflation-restriction makes the kernel of H¹(Γ, G_m(S)) → H¹(π, G_m(S)) equal to H¹(Γ/π, L^*) = L^*/{σ(x)/x}, which the valuation maps onto Z: the classes are the slopes of rank-one F-isocrystals, and his last computation on 029 (the Néron model of Res_{K/Q_p} G_m, K^* → Z) is this case. Michel Hua's project found this answer (a second witness, not our basis); R1 re-proved it independently (SA04-R1615-03). His Question on 161-5/024, whether T_cr with its F-isocrystal, its filtration and gr ≅ T_Hdg extends as a ⊗-functor to the Tannakian category generated by the Barsotti-Tate representations, has a positive answer through Fontaine's D_cris (SA04-R1615-02, targeted proof check). On 024 c), T_DR(M) = T_cr(M) ⊗_K L should read ⊗_L K (SA04-K1615-01; not decided on the scan).
- **Cote 161-2 (reader A).** His sheets on accessible categories cite SGA 4 I 8-9 by number; accessible = Ind_π(C) (the Makkai-Paré definition); the axiom c) of cardinal filtrations needs π'^π = π'.

## Leads (inferences by Claude, Anthropic; to be checked in full)
- **Cohen factorization.** Deligne's lemma of 17 Oct 1966 is the minimal Cohen factorization of Avramov, Foxby and Herzog (J. Algebra 164, 1994).
- **Regular immersions.** His PS is the origin of the Koszul-regular immersions of SGA 6 VII.
- **The crystalline realisation.** Cote 161-5 is his "mysterious functor" programme (ICM 1970), carried out later by Fontaine (B_cris, D_cris).
- **The slopes (H1615-1, the SA04 study).** The non-uniqueness of 161-5/029 is exactly the slope (Newton) data. Fixing the slopes, or imposing weak admissibility, should make the solution unique up to G'_S(S)^π = G'_L(L): a Tannakian precursor of Colmez-Fontaine.
- **Natural bundles.** 23/039-041 asks for the algebraic form of the natural-bundle theorem (Palais-Terng, Epstein-Thurston).
- **Lidskii.** Cote 1 may predate Lidskii (1959). Whether his 1955-56 papers print the argument is not yet checked.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

**What counts as done,** per item of the Parts and per Lead:
- (a) a theorem with a complete proof; or
- (b) a refutation with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is finite), together with the strongest true statement proved in its place.

Nothing else finishes an item. Partly settled is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest undecided instance are the state of an item you are still working on: record them as you go, then attack the obstruction, starting from that instance.

"Known" counts only with the derivation of the statement used here from the cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is given explicitly, with a proof that it is the whole answer.

**Not acceptable:**
- a survey;
- "open, see [reference]";
- a plan, an outline or a sample;
- a statement for every genus proved in genus 0 without saying so;
- a step that replaces a claim by a convenient special case without naming it;
- a reading of the manuscript taken on trust where the mathematics depends on it. The transcriptions are AI-made and carry doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done.

If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA23_report.md` reads INCOMPLETE. Its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none.

A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.


## Parts
Each item is a question to settle, proved or refuted, with complete proofs. The places are his pages; the details are in the readings and in RESEARCH_PACKAGES.md (RP1-RP11).

**A. Formal smoothness and Cohen lifts (cote 22). The main question is A.1.**
- **A.1.** For a field k of characteristic 0 and A = K[[t_1..t_n]] (n > 0) with Ω_{K/k} finite-dimensional, is A formally smooth over k for the discrete topology? Equivalently, is Ω_{A/k} free? Start with Q[[t]] over Q. His presumption (23/22-23 of cote 22) is "jamais".
- **A.2.** The characteristic-p case without a finite p-base (cote 22, scan 22).
- **A.3.** His open problem on 22/014: does every Cohen algebra B_0 over A_0 lift over a square-zero thickening A → A_0?
- **A.4.** His questions 3 and 4 (22/020-021): openness of the locus of formally smooth fibres for flat maps of noetherian rings, and openness of the flat locus for arbitrary noetherian A → B.

**B. Deligne's lemma (cote 23, 060-063).**
- **B.1.** Prove the Cohen factorization as stated there, and the pro-isomorphism of Tor.
- **B.2.** Settle Deligne's open point: every algebraic K/k is k[T_α]/(P_i) with lifts flat over every artinian A with residue field k.

**C. Regular immersions (cote 23, 053-054).**
- **C.1.** Prove every claim he makes for Koszul-regular sequences and immersions, without noetherian hypotheses.
- **C.2.** Give a local ring with (x, y) regular and (y, x) not.
- **C.3.** Prove Deligne's characterization of regular ideals by Sym and Tor.

**D. EGA errata (cote 23, 044-065).** For each item, decide whether the printed text is false and give the proof or the counterexample:
- 0_IV 19.3.12, 19.5.5, 19.5.6 (ii), 20.4.6, 20.4.13 (iv);
- IV 16.1.5 and 16.1.6;
- III 4.3.6;
- Lê Dũng Tráng's 20.1.3-21.6.2.

**E. The discriminant over a base (23/006).** Prove the corrected weight and degree, the criterion for smoothness over any base, and the integral normalization.

**F. Differential functors (23/039-041).** State and prove the algebraic natural-bundle theorem for functors on smooth S-schemes of relative dimension d with étale maps.

**G. Graded flatness (23/096-098).** Settle his implications under the "bonnes conditions".

**H. Cote 1.**
- **H.1.** Write out his proof of Lidskii's formula (crossed-out 79-80, lemma on 111-112) completely, and check every step.
- **H.2.** Δ(AB) = Δ(A)Δ(B) in his setting for all operators, including A = λ + B with T(1) infinite, and his question Δ(B*HB) ?= Δ(A*A)Δ(B*B).

**I. Cote 161-2.**
- **I.1.** His equivalences for accessible categories, with the exact cardinal hypothesis.
- **I.2.** The existence and universal property of his topos modulaire relative to a base topos.

**J. Cote 161-5.** His two Questions have answers (Results, cote 161-5): check them where you use them, and settle whether the ⊗-extension of 161-5/024 is unique. The question to settle is the corrected form of his Question on 029. From 161-5/023-029 (both witnesses), state his torsor data precisely: ρ: π → G(Q_p), the Hodge-Tate cocharacter j, the torsors Q_L, R_L and P_L, the descent from L to K and the Frobenius data, and the extension 1 → G'_S(S) → E → Γ → 1. Then determine the classification of the sections α extending α₀: prove that they are classified by the slopes, and that fixing the slopes, or imposing weak admissibility, makes them conjugate under G'_S(S)^π = G'_L(L) (the lead on the slopes), or refute this and prove the correct classification. Answer in today's terms, with exact locators (Fontaine 1982, Colmez-Fontaine 2000, Kisin 2006).

**L. Cote 162-5 (his notes of 6.9.68 on Quillen's formal categories).** He defines a "Θ-Algèbre de Lie" (a Lie algebroid) and states "Quillen's theorem": in characteristic 0, adic formal categories with flat Ω are equivalent to De Rham complexes. One step is false (δ_1δ_0 = 0 alone does not give δ² = 0; reader A2 has a counterexample). Prove the correct statement with the missing condition, and relate it to his "théorème fondamental de démarrage des cristaux" (his margin).

**K. Cote 26.** For each "Problème-type" a)-j), give its state with exact references. Where it is open as he posed it, settle it.

## Sources
Cite every known result with exact locators, and prefer arXiv LaTeX sources: EGA 0_IV and IV (Publ. IHÉS 20, 24, 28, 32), SGA 4, SGA 6, Avramov-Foxby-Herzog (1994), Makkai-Paré (1989), Fontaine (1979-1994), Colmez-Fontaine (Invent. Math. 140, 2000), Kisin (2006), Demazure, "Résultant, discriminant" (2012), Lidskii (1959) and Gohberg-Krein.

## Rules of proof (they bind every statement you deliver)

1. **State the actual claim with all its data:** the genus and number of punctures, the base field and its
   characteristic, the finiteness hypotheses. Do not replace it by a convenient special case. If you prove a special
   case, name it as one and keep the general statement on your list.
2. **Type every map and relation you introduce:** source, target, the category, space or ring in which it lives, and
   each extra property you use. Compositions must type-check.
3. **Every reduction** ("we may assume", "replace by", "normalize") comes with its comparison map and a proof that the
   exact property needed transfers in the direction needed.
4. **"Up to" names the ambiguity.** Keep apart:
   - equality;
   - isomorphism;
   - real-analytic against algebraic isomorphism;
   - isomorphism of coarse moduli against isomorphism of stacks;
   - numerical, homological and rational equivalence.
5. **Check the edge cases in scope:**
   - (g, ν) = (0, 3), (0, 4), (1, 1);
   - cusps against boundary circles;
   - characteristic 2, 3 and 5 for the octahedron;
   - non-noetherian rings and modules not of finite type for C.1;
   - infinite groups for C.2.
6. **Counterexamples.** A counterexample is given completely and, when finite, checked by a program whose code and output
   you attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not
   falsity; keep the two apart.
7. **No authority.** Grothendieck's pages, the transcriptions, our study, the readers' reports, their check events and
   corrections, and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full.
   If one is wrong, say so plainly and show where.
8. **What is not yet settled** stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. **Known results** are cited with exact locators (author, work, theorem or section number), not proved again, except
   for a short proof of a form the source does not state. Every new statement of this run is proved in full in the
   paper. Before calling anything new, search the literature and say what you searched. Never invent a reference;
   mark each entry of the bibliography opened or not opened. Prefer the LaTeX source of a paper (the arXiv e-print)
   where one exists.

## What to deliver

One ZIP containing:
- **`RESEARCH_SA23_paper.tex` and its PDF** (LuaLaTeX, compiles cleanly):
  - the mathematics in the order of the Parts, every statement numbered;
  - each statement labelled Proved; Proved under stated hypotheses (with whether they hold where the statement is
    used); Refuted (with the counterexample and the corrected statement); or Known (with citation);
  - each new statement with its complete proof;
  - checked and unchecked statements in separate parts;
  - English, first person plural;
  - where a statement is Grothendieck's, the cote and scan of his page.
- **`RESEARCH_SA23_results.csv`:** one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- **`RESEARCH_SA23_references.bib`:** each entry marked opened / not opened.
- **`RESEARCH_SA23_report.md`:**
  - first, the outcome table: one line per item of the Parts and per Lead, proved or refuted, with the statement
    number;
  - then what you read;
  - what you computed: every program with its scope, counts and run time;
  - every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- **`PROGRESS_LEDGER.md`:** the dated ledger of the progress reviews.
- **`CHECK_EVENTS.tsv`** (below) **and `code/`:** every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. The attached study's statements carry ids such as SA23-6 with their pages; keep them. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is.
- Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a
  display or a line of text.
- Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again.
- Then render pages to images and look at them: every page that had an overflow, and a sample spread over the
  document.
- Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA23_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.

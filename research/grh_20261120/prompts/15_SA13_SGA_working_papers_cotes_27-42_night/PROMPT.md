**The attached files.** Besides this file there is one ZIP, `SA13_SGA_working_papers_cotes_27-42_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA13_literature.zip` is the folder `RESEARCH_SA13_literature/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# RESEARCH_SA13: Grothendieck's SGA working papers (cotes 27-42): the injective-dimension theorem of the SGA 5 draft, the Griffiths draft of SGA 7, and his other open steps

**To be settled:** the questions his SGA working papers leave open, each proved or refuted. A.1 is the main question: his injective-dimension theorem of the 1965 SGA 5 draft (33/170-178), with the Lazard-type question he marks on 33/174.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA13`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a84c887cf408574ed, on 19 Nov 2026. It led the sweeps of this topic and its sweep-3 study. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA13_study.zip`: our study of the topic.**
  - `study/STUDY.md`, `study/HUNCHES.md` and `study/RESEARCH_PACKAGES.md`.
  - The tables `CHECK_EVENTS.tsv` (184 check events), `CORRECTIONS.tsv` (57 corrections), `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: the full readings of every transcribed page (550 pages):
    - `c34.md`, cote 34;
    - `c33_c36_c39.md`, cotes 33, 36 and 39;
    - `c32_c35_c37_c40.md`, cotes 32, 35, 37 and 40;
    - `c27_c28_c41_c42.md`, cotes 27, 28, 41 and 42.
  - `study/sweep2_OBJECTS.tsv`: the map of the items SA13-1 to SA13-69.
  - `study/sweep2_SA13_scan_readings.md`: five readings decided on the scan images.
  - `broad/`: the neighbouring topic SA12 (SGA, cotes 29 and 31).
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026. It was checked as recorded in the CHECK_EVENTS tables and nowhere else.
- **`RESEARCH_SA13_transcriptions.zip`: the AI transcriptions (LaTeX) the Parts rest on, with their notes and doubt tables.**
  - The Pro packages of cotes 33, 36 and 39 were transcribed by GPT-6 Astra (ChatGPT Pro mode).
  - The Codex-web folders (A36-01/02 for 36/10-27; K27-01 to 03, K28-01, K32-02/03, K40-02, K41-01, K42-01) are by GPT Codex web at reasoning effort max.
  - `\scanpage{N}` marks scan N of the cote's PDF. Where a step of yours depends on a doubtful reading, say so.
  - `PREAMBLE.tex` defines the macros.
- **`RESEARCH_SA13_literature.zip`: our AI-transcribed French LaTeX of the printed SGA texts these pages lead to.**
  - SGA 5 (`s5.tex`);
  - SGA 7 II, Exposés XVIII, XX and XXI;
  - SGA 7 I, Exposés VII, VIII and IX.

  Cite the printed volumes by exposé and number.
- Fetch the other literature yourself. It is listed under "Sources" below.

## Where this comes from

**The papers.** Grothendieck's working papers for the Séminaire de Géométrie Algébrique (about 1965-1971), in the Montpellier archive (fonds Grothendieck, cotes 27-42):
- **Cote 33:** the 1965 manuscript draft of SGA 5.
- **Cote 34:** his manuscript of the first SGA 7 exposés.
- **Cote 36:** his part of SGA 7. It holds the draft of Exp. IX with Deligne's written remarks on it, biextensions, Picard duality, invariant cycles, the arithmetic proof of the orthogonality theorem, and the typed draft "Le théorème de Griffiths par voie algébrique" behind SGA 7 XVIII, XX and XXI.
- **Cote 39:** "fonctions et structures élémentaires".
- **Cotes 27-28:** SGA 3 complements, including a "théorème de 1/2 continuité", and his notes of Demazure's 1970 talks on the Cremona group.
- **Cotes 32, 35 and 37:** corrections and re-editions of SGA 4-7 and EGA.
- **Cotes 40-42:** α_p-torsors, an étale scheme of irreducible components, and networks of local rings.

**Our work.** The pages were transcribed by AI and read in full in our sweeps by Claude Opus 5.5 at effort max (Anthropic).

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result names the reading file and page where its check events and corrections are recorded in the attached tables. Check each one where you use it (Rules of proof, 7).

- **R1 (c33_c36_c39, 33:170-178).** Decided on the scan image: in his Théorème (i) on 33/172 the Ext is the sheaf ℰxt.
  - For constructible F, and C with injective stalks, ℰxt^i(F, C) = 0 for i > 2n holds by his limit argument.
  - For C = A_X on smooth X the bound 2n is Poincaré duality, and the support of ℰxt^j(F, A_X) has codimension ≥ j/2.
  - Print has only dim.inj ≤ 4n (SGA 5 I 1.5).
- **R2 (c33_c36_c39, 36:10-27).** What the Griffiths draft proves:
  - The lemmas prove the weak form of his Théorème 7.1: Frobenius on E₀(Y) is not nilpotent. This is the form printed as SGA 7 XXI 1.4.
  - They do not prove Corollaire 7.2 or "G₀ n'est pas un p-groupe". His margins: "pas prouvé sous cette forme forte".
  - Corollaire 7.3 survives on the weak form.
  - Lemma 7.6 needs N ≤ r d₁^n.
  - The algebraicity of Λ "lorsque X se remonte en car. zéro" is overstated; lifting gives the hard Lefschetz theorem (LV).
- **R3 (c33_c36_c39, 36:60-71).** In relative dimension 1, Ker(Γ → NS(X₀)) = Z/dZ by the multidegree argument. He asks in general: "demander Raynaud si Ker est donc Z/dZ" (36/71).
- **R4 (c27_c28_c41_c42, 27:36-37).** His step "generic fibre affine ⇒ special fibre affine" is checked. The Galois action on the limit of the H(n) goes through the cyclotomic character, which an abelian part (Frobenius weight 1/2) excludes.
- **R5 (c27_c28_c41_c42, 28:5-11).** Demazure's root data for subgroups of Cr_n containing a split n-torus are checked on explicit models: x_α, ρ_α, φ_α: GL₂ → G, the coroot ρ_α − ρ_{−α}, and the commutator formula on de Jonquières maps. Cor. 1 on 28:5 has an index slip: a torus G_m^d corresponds to fields of transcendence degree n − d.
- **R6 (c27_c28_c41_c42, 42:4-7).** For networks of local rings:
  - The Proposition (Γ(X, F) = lim of coherent germs) is checked.
  - Lemma 3 holds for Y separated over S (the 1960 "S-schéma") and fails for the line with doubled origin.
  - The Remark of 42:7 needs Φ infinite. The ink reads "finie", decided on the scan.
- **R7 (c27_c28_c41_c42, 41:12).** For f with irreducible fibres, φ is continuous ⇔ f is open, since φ⁻¹(U) = f(U).
- **R8 (c32_c35_c37_c40, 40:23).** His open step is proved: the natural group law on α_p-torsors corresponds to that of A/A^p.
- **R9 (c32_c35_c37_c40, 37:79).** A cancelled heading "Faux schémas abéliens (ou Motifs mixtes effectifs de poids 1)" plans the local invariant cycle problem for H¹.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1.** His question of 33/174 is a Lazard theorem: every étale sheaf of Z/N-modules with free stalks on a noetherian scheme is a filtered colimit of constructible ones with free stalks. For N prime it is immediate (SGA 4 IX 2.7.2). Combined with R1 and with Ext from a constructible F commuting with filtered colimits in C, it gives the global 2n bound.
- **L2.** The strong form of 7.1 is a statement on the monodromy of the unit-root part of H^{n−1}(Y, O) for hypersurface sections Y of large degree: it is big enough that Frobenius elements reach every trace.
- **L3.** In general, the class O(Σ(d_i/d)D_i)|X₀ is d-torsion and numerically trivial, so the question of R3 is whether it lies in Pic⁰(X₀).
- **L4.** The full "théorème de 1/2 continuité" (27:32) is partly in SGA 3 X-XII and SGA 7 IX §2. It may not be in print with all its inequalities, notably with four of them "sans réserve de platitude".
- **L5.** The étale scheme of geometrically irreducible fibre components of 41 is the object of later work on irreducible components in families. Without separatedness it exists as an étale algebraic space.
- **L6.** For networks of local rings, the point map in a morphism of networks may replace separatedness. Full faithfulness on S-préschémas locally of finite type may hold without it.
- **L7.** With R5's correction and the stably rational non-rational threefold of Beauville-Colliot-Thélène-Sansuc-Swinnerton-Dyer, Cr₆ over C contains a G_m³ in no G_m⁶.
- **L8.** His "peut-être vrai dès que Y est noethérien" (33/110) fails for coefficients divisible by a residue characteristic. Take Y the spectrum of a strictly henselian DVR of mixed characteristic (0, p) with residue field of infinite p-degree, and F = Z/p; then cd_p of the fraction field is infinite.
- **L9.** "g loc. acyclique" (margin of 32/37) suffices for g'^*Rf^! ≅ Rf'^!g^*.
- **L10.** His axioms a)-f) of cote 39, with the preparation theorem of 39/19-20, are Weierstrass systems in the sense of Denef-Lipshitz.
- **L11.** The pairing on the torsion of [M → G] proved by filtration on 36/30-34 is the Weil pairing of the dual 1-motive.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is
finite) together with the strongest true statement proved in its place. Nothing else finishes an item. Partly settled
is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest
undecided instance are the state of an item you are still working on: record them as you go, then attack the
obstruction, starting from that instance. "Known" counts only with the derivation of the statement used here from the
cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is
given explicitly, with a proof that it is the whole answer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; a statement for every dimension
proved in low dimension without saying so; a step that replaces a claim by a convenient special case without naming
it; a reading of the manuscript taken on trust where the mathematics depends on it (the transcriptions are AI-made
and carry doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading).

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA13_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. The injective-dimension theorem of the SGA 5 draft (33/170-178). The main question is A.1.**

The setting: X of finite type over a separably closed field k with dim X ≤ n, A = Z/NZ with N invertible on X, and sheaves of A-modules on the étale site.
- **A.1 (main).** Prove or refute his Théorème (ii) on 33/172: Ext^i(F, C) = 0 for all i > 2n, for every constructible F and every sheaf C whose stalks are injective A-modules. Settle L1 on the way, his own question on 33/174: is every such C a filtered colimit of constructible sheaves with injective stalks? If it is not, settle A.1 by another route.
- **A.2.** Determine whether the bound of A.1 holds for every sheaf F, not only for constructible F. Then determine the injective dimension, in the category of étale sheaves of A-modules, of the sheaves with injective stalks.
- **A.3.** Prove in full the support bound used in R1: on X smooth of dimension n, ℰxt^j(F, A_X) is supported in codimension ≥ j/2 for F constructible. Then prove the 2n bound for constructible C on any X of finite type, by dévissage to the smooth case.

**B. The Griffiths draft of SGA 7 (36/10-27).**
- **B.1.** Prove or refute the strong form of his Théorème 7.1: in the setting of 36/22-27, the Frobenius elements of G₀ realize every prescribed trace on all of V₀. Then settle his Corollaire 7.2 and the assertion "G₀ n'est pas un p-groupe" (36/26), each proved or refuted.
- **B.2.** Settle L2.

**C. The invariant-cycle kernel (36/60-71).**
- **C.1.** Let X be regular and proper over a strictly henselian DVR, with smooth projective generic fibre and special fibre X₀ = Σ d_i D_i, and d = gcd(d_i). Prove or refute Ker(Γ → NS(X₀)) = Z/dZ in every relative dimension, his "demander Raynaud si Ker est donc Z/dZ". Settle L3.
- **C.2.** Settle his index statements of 36/61 a):
  - d^t = gcd(μ_i d_i);
  - d^t = p^h·d, with h = 0 for a perfect residue field.

**D. The "théorème de 1/2 continuité" (27/28-37).**
- **D.1.** Prove or refute his Théorème on 27:32 for smooth separated group schemes of finite presentation over any base:
  - ρ_aff, d, ρ_n, ρ_na and ρ_u are upper semicontinuous;
  - ρ_ab, ρ_ab + ρ_r and ρ_ss are lower semicontinuous.

  This includes his "lemme à rapporter" (27:34) and the steps ③ and ④ (27:37). Settle L4.

**E. The étale scheme of irreducible fibre components (41/4-14).**
- **E.1.** Prove his Théorème of 41:9 in full: the existence of an étale separated modular M under his two valuative conditions; and the corollary on finite étale covers.
- **E.2.** Settle his Remarque 1 (41:11): is condition (i) necessary and sufficient for the existence of an étale, not necessarily separated, modular M? Settle L5.

**F. Networks of local rings (42/2-7).**
- **F.1.** Prove or refute: for S locally noetherian, ρ is fully faithful on S-préschémas locally of finite type, including non-separated ones. Determine which finiteness is needed on the target (his margin question on 42:3). Settle L6.

**G. Tori of the Cremona group (28:5).**
- **G.1.** Prove the corrected equivalence of R5: every G_m^(n−d) ⊂ Cr_{n,k} lies in a G_m^n if and only if every extension K/k of transcendence degree d with K(t₁, …, t_{n−d}) purely transcendental is purely transcendental.
- **G.2.** Determine the pairs (n, d) for which it holds over C. Settle L7.

**H. Further steps on his pages.**
- **H.1.** Settle L8 (33/110).
- **H.2.** Settle L9 (32/37).
- **H.3.** For cote 39:
  - Does f′ imply f under his axioms a)-e) (39/4)? He writes "il ne semble pas".
  - Is S_n faithfully flat over A_n when k is faithfully flat over k₀ (39/13)?
  - Settle L10.
- **H.4.** Settle L11: prove the perfectness of the pairing on the torsion of [M → G] as on 36/30-34, and identify it with the Weil pairing of the dual 1-motive.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- SGA 4, SGA 4½ (Th. finitude), SGA 5 (Exp. I and III), SGA 7 I-II (Exp. VII-IX, XVIII-XXI); the French LaTeX of SGA 5 and of these SGA 7 exposés is attached.
- L. Illusie, Y. Laszlo, F. Orgogozo (eds.), *Travaux de Gabber sur l'uniformisation locale et la cohomologie étale des schémas quasi-excellents*, Astérisque 363-364 (2014).
- M. Raynaud, "Spécialisation du foncteur de Picard", Publ. Math. IHES 38 (1970).
- S. Bosch, D. Lorenzini, "Grothendieck's pairing on component groups of Jacobians", Invent. Math. 148 (2002).
- O. Gabber, Q. Liu, D. Lorenzini, "The index of an algebraic variety", Invent. Math. 192 (2013).
- M. Demazure, "Sous-groupes algébriques de rang maximum du groupe de Cremona", Ann. Sci. ENS (4) 3 (1970).
- A. Beauville, J.-L. Colliot-Thélène, J.-J. Sansuc, P. Swinnerton-Dyer, "Variétés stablement rationnelles non rationnelles", Ann. of Math. 121 (1985).
- V. L. Popov, "Tori in the Cremona groups", Izv. Math. 77 (2013).
- M. Romagny, "Composantes connexes et irréductibles en familles", Manuscripta Math. 136 (2011).
- J. Denef, L. Lipshitz, "Ultraproducts and approximation in local rings II", Math. Ann. 253 (1980), and their work on Weierstrass systems.
- P. Deligne, "Théorie de Hodge III", Publ. Math. IHES 44 (1974), §10.
- N. Katz, on the monodromy of families and Frobenius on unit-root parts; the papers on ordinarity of generic hypersurfaces.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data (the base scheme and its finiteness, the coefficient ring, the topology,
   the dimension and characteristic hypotheses). Do not replace it by a convenient special case. If you prove a
   special case, name it as one and keep the general statement on your list.
2. Type every map and relation you introduce: source, target, the category or site in which it lives, and each extra
   property you use. Compositions must type-check.
3. Every reduction ("we may assume", "replace by", "pass to the limit", "henselize") comes with its comparison map and a
   proof that the exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism; isogeny; equivalence of categories; quasi-isomorphism;
   a statement about sheaves against one about their global sections; ℰxt against Ext.
5. Check the edge cases in scope: residue characteristics dividing the coefficients; imperfect residue fields;
   non-reduced, non-separated and non-noetherian objects; dimension 0 and 1; non-constructible sheaves; groups that are
   not smooth.
6. A counterexample is given completely and, when finite, checked by a program whose code and output you attach. One
   verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not falsity; keep
   the two apart.
7. No authority. Grothendieck's pages, the transcriptions, our study, the readers' reports, their check events and
   corrections, and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full.
   If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Known results are cited with exact locators (author, work, theorem or section number), not proved again, except
   for a short proof of a form the source does not state. Every new statement of this run is proved in full in the
   paper. Before calling anything new, search the literature and say what you searched. Never
   invent a reference; mark each entry of the bibliography opened or not opened. Prefer the LaTeX source of a paper
   (the arXiv e-print) where one exists.

## What to deliver

One ZIP containing:
- `RESEARCH_SA13_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA13_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA13_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA13_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with the
  statement number); then what you read, what you computed (every program with its scope, counts and run time), and
  every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- `PROGRESS_LEDGER.md`: the dated ledger of the progress reviews.
- `CHECK_EVENTS.tsv` (below) and `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here (the attached study's statements carry ids such as SA13-48 or a page id such as MPL_36_053-085+39 (36:71); keep them). Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA13_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.

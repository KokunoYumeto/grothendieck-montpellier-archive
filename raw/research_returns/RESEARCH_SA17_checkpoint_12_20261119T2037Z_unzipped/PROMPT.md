**The attached files.** Besides this file there is one ZIP, `SA17_FINISH_Descentes_cotes_126-133_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA17_checkpoint_02.zip` is the folder `RESEARCH_SA17_checkpoint_02/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# RESEARCH_SA17_FINISH: finishing RESEARCH_SA17 on Grothendieck's "Descentes" (cotes 126-133): his representability theorem for locally quasi-finite functors, and the other items the first run left open

**What is to be settled.** The first run on this topic stopped after its second checkpoint, about 1 h 30 min into the
work, with its main question open at a named gate. This prompt finishes it. Its items, all from the first prompt:
- **A.1 (main).** His Théorème of cote 131, scan 14: F is representable by a locally quasi-finite separated S-scheme
  iff conditions 1°-8° hold. The gate: the local representing schemes from condition 7° as written, and the
  constructibility of the modularity locus (L1). Then Corollaire 2 (unramified), "quasi-modulaire" and the gluing
  proposition.
- **A.2: L2.** Condition 7° from the others, once 4° is strengthened to noetherian adic rings.
- **A.4: the Théorème of cote 128 in every rank** (GL_m-torsors against H¹ over finite semi-local algebras).
- **B.3.** His conjecture of cote 129 scan 114 (full faithfulness of Dieudonné crystals):
  - the largest class of bases of characteristic p on which the literature proves it;
  - an independent check of the nonvanishing lemma behind its refutation.
- **C.1.** His question of cote 133 scan 29, for every commutative ring.
- **C.3.** Split WG(BO_m) and its λ-structure in positive characteristic.
- **C.4.** Two parts of cote 133 scan 36: the non-commutative unipotent alternative of (I), and the realisation of a
  prescribed centre and derived group without a baseline group.
- **R.** The report and the paper of the first run, completed:
  - the corrections section, with file and line;
  - the derivations behind the rows labelled Known;
  - the labels our intake found overstated.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA17`, as in the first run,
because you continue its files. Your first checkpoint is `RESEARCH_SA17_checkpoint_03.zip`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent ac8bd2a26d00b4f37, on 19 Nov 2026, at the request
of the main session (Claude Opus 5.5 at effort max). This agent:
- read the Work folders of cotes 126-132 in sweep 3;
- took in the first run's last checkpoint (the intake attached);
- decided the reading of cote 127 scan 3 on the image.

The first prompt was drafted by agent a34c04448e8299803 (Claude Opus 5.5 at effort max).

## The first run, and what is attached

**The first run.** GPT-6 Astra (ChatGPT Pro mode) worked on the prompt RESEARCH_SA17 from 04:00 UTC on 19 Nov 2026.
- It saved checkpoint 01 at 04:45 and checkpoint 02 at 05:30 UTC, and nothing after.
- Its report's first line reads INCOMPLETE, and its three-hour progress review was never reached.

Checkpoint 02 is its last state, and you continue from it.

- **`RESEARCH_SA17_checkpoint_02.zip`: the first run's last checkpoint.** It holds the folder `RESEARCH_SA17/`.
  - We rebuilt it from the return. We verified it file by file against the checkpoint's own manifest,
    `logs/checkpoint_02_manifest.json`: all 127 files listed there agree in size and SHA-256.
  - The manifest itself is the 128th file. Nothing earlier is needed.
- **`INTAKE_RESEARCH_SA17_20261119.md`: our intake of checkpoint 02.** Claude Opus 5.5 at effort max (agent
  ac8bd2a26d00b4f37) wrote it on 19 Nov 2026. It gives:
  - the state of every item;
  - where the first run's tables overstate or understate;
  - the checks of its claims about the pages;
  - the corrections to our own material.

  With it come `INTAKE_RESEARCH_SA17_20261119_CHECK_EVENTS.tsv` and its two programs with their outputs:
  - `INTAKE_check_A4_boundaries.py` and `.out`: the boundary images of 128 Lemma 1 for p = 2, 3, 5, 7;
  - `INTAKE_check_D_conic_pencil.py` and `.out`: the conic pencil of D.1.
- **`MURRE_294_LOCATORS.md` and `Murre_1965_Seminaire_Bourbaki_294.pdf`.** J. P. Murre, "Representation of unramified
  functors. Applications (according to unpublished results of A. Grothendieck)", Séminaire Bourbaki n° 294 (1964/65,
  talk of May 1965), from Numdam.
  - It is the published form of the programme of cote 131.
  - The locators file lists the statements of it that the intake checked.
  - Its §2 outlines the proof of the unramified theorem.
- **`RESEARCH_SA17_first_run_PROMPT.md`: the first run's prompt.** Use it for reference: its ids (the results R1-R6,
  the Leads L1-L10) and the wording of its Parts. Its tasks are replaced by the items of this prompt.
- **The first run's three attachments, unchanged.** The first prompt describes them, and those descriptions hold.
  - `RESEARCH_SA17_study.zip`: our study of cotes 126-133, with the readings and their tables.
  - `RESEARCH_SA17_transcriptions.zip`: the AI transcriptions. `\scanpage{N}` marks scan N. The `\unsure{a|b}` marks
    and the CORRECTIONS tables give the doubtful and the decided readings.
  - `RESEARCH_SA17_literature.zip`: LaTeX sources.

**How you continue.** Unpack the checkpoint and work in its tree:
- the paper `RESEARCH_SA17_paper.tex` with `sections/*.tex` (A, A45, A_gluing, B, C, D, unresolved);
- `notes/`, among them `ROOT_STATUS.md`, `A_Artin_Rees.md`, `A_research.md`, `B_research.md`, `C_research.md` and
  `A45_D_research.md`;
- `RESEARCH_SA17_results.csv` and the per-part `results_*.csv`;
- `CHECK_EVENTS.tsv` and `checks_*.tsv`;
- `RESEARCH_SA17_references.bib` and `references/`;
- `PROGRESS_LEDGER.md` and `RESEARCH_SA17_report.md`;
- `code/` and `logs/`.

The rules for continuing:
- Keep the first run's statement ids. A statement you revise keeps its id, and its row and the report say what
  changed. New statements get new ids.
- Extend `CHECK_EVENTS.tsv`, `PROGRESS_LEDGER.md`, the results and the report; do not start new ones.
- The restored report opens with INCOMPLETE, the first run's mark. It stays only if this session too ends before the
  work is finished.
- The progress check below counts the hours of this run. Its ledger rows continue the first run's.
- Your checkpoints are numbered from 03.
  - Each holds the whole current tree, including the files restored from checkpoint 02 as you have extended them.
  - It leaves out the attached files: the checkpoint 02 ZIP, the study, transcription and literature ZIPs, the intake
    files and Murre's exposé.

## Where this comes from

**The pages.** These are cotes 126-133 of the Grothendieck archive at the University of Montpellier ("Descentes"):
- **cote 131:** a complete programme on representability. It has eight numbered conditions, a theorem with étale and
  unramified corollaries, a proof by induction on dim S through three formal propositions, and applications;
- **cotes 126-128:** faithfully flat and non-flat descent;
- **cote 129:** Witt vectors, Dieudonné theory, BT groups, the co-Lie complex, deformations, and the crystalline
  programme with the Hodge filtration. These are his handwritten notes after the Montréal 1970 typescripts, and the
  sheets headed "Conférence à Nice";
- **cote 130:** heights and Néron's local symbols;
- **cote 133:** λ- and σ-operations on G-sets, the category of finite sets and injections, tensor powers in the
  K-theory of symmetric-group objects, Witt groups of quadratic forms, and formal and algebraic groups seen through
  crossed modules.

**Our reading of them.** Sweep 3 of our horizontal reading (18-19 Nov 2026) read:
- cotes 129 (scans 77-115) and 131 in full, and cote 133 scans 19-29, by a34c0444;
- cote 133 scans 2-18 and 30-54, by a598c2df;
- the Work folders of cotes 126-132, by ac8bd2a2.

All three are Claude Opus 5.5 at effort max.

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of these
cotes, and a Lean file Folder133.lean for the group criteria. You may consult them. Credit any point taken from them to
"Michel Hua's project", and quote phrases, not passages.

## Settled: background, not items of this run (status on 19 Nov 2026)

The first run settled the results below. The first run's own agents checked them, and where the entry says so, our
intake checked them too; its events are in the intake's TSV.
- They stay in the paper as the first run wrote them, with the labels given here.
- They are not items of this run: do not rework them.
- Where an item of this run uses one, check the step it uses (Rules of proof, 7) and record the event.

- **A.1, the parts settled.**
  - **A:8-literal.** Condition 8° as written on scan 14 puts no finiteness on the test scheme Z, and in that form it
    is not necessary. With Z locally of finite type over S it is necessary.
    - This is a defect of wording: scan 2's version has the finiteness.
    - The intake read the proof.
  - **A:NR-counterexample and A:NR-density.** NR(b) of scan 16 as written ("irréductible", a minimal prime 𝔭 with
    I ⊂ 𝔭, I𝔭 = 0) is not necessary: A = k[[t,ε]]/(ε², tε), with its embedded prime, refutes it.
    - The corrected condition, a unique associated prime, is Murre's (F7), and it is also his own scan-7 insertion
      "d'adhérence schématique".
    - The example was first proposed in the Pro notes of MPL_131 (RN020), and the first run credits them.
    - The intake checked the example and read the proof of A:NR-density.
  - **A:artinian-tests and A:etale-corollary.** Corollaire 1 (étale) is proved, through Murre's Corollary 2. The
    intake read the proof.
- **A.2, its first question: A:ind-thickening.** Over a base of dimension 1, the ind-scheme
  colim Spec k[t,x]/(x², f_E(t)x):
  - satisfies 1°-7°;
  - is finite over every local base;
  - fails 8° with Z = S.

  This answers his margin "Donner l'exemple-type (S de dim 1)". The intake checked it.
- **A.3 and L3.** Checked by the intake.
  - Descent from Ŝ to S, step 3 of his induction, is Murre 294 §4, Theorem, case (d) (A:completion-descent). The
    intake opened the source.
  - The question of 126 scans 32-35 has the answer no (A:nonfinite-descent). Restrict Hironaka's 3-fold to the
    complement of one point of a fibre: this gives a projective scheme with a descent datum along his deleted-point
    cover that is not effective.
  - The positive replacements are SGA 1 VIII 7.7 and 7.8 (A:polarized-descent).
- **A.4, its two lemmas.**
  - **127 Lemma 1.3 is true**, with weaker hypotheses (A4:flatclosure: any f, U retrocompact). The intake read the
    proof.
  - **128 Lemma 1 (G_m against G_a) is false in every characteristic p > 0**, not only in characteristic 2
    (A4:all-primes).
    - The counterexample: A = F_p[x,y,a,b]/(a^p, b^p, ε²) with ε = ya − xb, I = (ε), and A' = A_x × A_y.
    - The exact replacement is A4:boundary.
    - The intake recomputed the boundary images for p = 2, 3, 5, 7.
  - The label of L4 in the first run's table should read "proved, and strengthened to every p". What is refuted is
    R2's "fine in odd characteristic".
- **A.5.** Abelian schemes over normal locally noetherian bases have a relatively ample line bundle (A5:projectivity,
  Known).
  - One fixed projective space need not exist over a base that is not quasi-compact (A5:fixed-projective-space).
  - Murre §3 carries the same application.
  - The derivation from the cited theorems is part of item R.
- **B.1 and L5.** His V (cote 129 scan 115) holds up to isogeny for every p, and integrally iff p ≥ 3 or 2A = 0
  (B:NiceV).
  - The intake checked the Kummer obstruction at p = 2 (B:Kummer).
  - The complete-DVR derivation (B:DVR-classification) is the first run's, not checked by us.
- **B.3, the refutation (B:crystal-counterexamples).**
  - The bases: F_p[x,y]/(x,y)², two planes meeting in a point, and a polynomial extension.
  - Over them the scalar τ = γ_p(ac)γ_p(bd) − γ_p(ad)γ_p(bc) gives a map D(μ_{p^∞}) → D(Q_p/Z_p) with no group map
    behind it.
  - The intake checked:
    - pτ = 0, dτ = 0 and φ(τ) = 0, and the compatibility pτ = φ(τ);
    - Hom = 0;
    - that these bases lie outside the positive classes.
  - τ ≠ 0 rests on B:finite-PD, which item B.3 checks.
- **B.4 and L6.**
  - Δ*(G) is constructed (B:Delta; not checked by us).
  - L6 as written is refuted (B:L6-refutation): the tensor formula of scan 94 has the finite Dieudonné module M, not
    Δ*(G). The misquote was the Lead's.
- **C.1, the cases settled.**
  - Every Q-algebra: polynomial iff K_0(k) = Z.
  - Every ring of positive characteristic: no.
  - Regular noetherian rings: iff characteristic 0 and K_0(k) = Z.
  - Z and the mixed-characteristic discrete valuation rings, Z_p among them: yes.
  - Torsion-free local rings of characteristic 0 can fail: k = Z_(2)[u]/(u² − 1) (C:local_charzero_counterexample,
    checked by the intake).
  - Also C:normal_domain_counterexample and C:torsion_generic_kernel (not checked by us), and the reduction
    C:allrings_obstructions, which item C.1 starts from.
- **C.2 and L7.** Not checked by us.
  - The ring of distinguished functors is determined (C:distinguished_ring).
  - L7, read as a special-λ claim, is refuted (C:lambda_failure).
  - The formula for T^n is corrected through partition types (C:partition_formula).
- **C.3 in characteristic 0, and L8.** Not checked by us.
  - L8 is proved over fields of characteristic 0 (C:charzero_lambda), and split WG(BO_m) is determined there
    (C:orthogonal_representation_ring).
  - In every odd characteristic, split WG fails the special λ-identities (C:odd_characteristic_failure). Split
    WG(BO_m) fails them for m ≥ p + 4 (C:BO_positive_failure).
  - The hyperbolic image in the Stiefel-Whitney target is described (C:hyperbolic_SW).
- **C.4 and L9.**
  - **L9 is refuted** (C:isoclinism_counterexample). Heis(F_3)² and Heis(F_9) have the same crossed-module data, and
    their commutator pairings have rank distributions 16 + 64 against 0 + 80. Checked by the intake.
  - **Over F_p, (I) with a smooth kernel and (II) fail.** A Galois-twisted extension of μ_{p^∞} by μ_{p^∞} does not
    split even up to isogeny (C:formal_Frobenius_counterexample, checked by the intake).
  - **What does split** (C:formal_corrected):
    - a kernel killed by p^N splits after [p^N];
    - the multiplicative case splits up to isogeny over an algebraically closed field.
  - The page states no base field: the first prompt's "over a perfect field" was ours.
  - The central twists with a prescribed centre and derived group, relative to a given group, are characterised
    (C:central_twists; not checked by us).
- **D.1 and L10.** Checked by the intake at the level of the statements, against our readings.
  - The rank formula (D:rank): ρ(X) + H² − 2, minus the excess of the reducible fibres.
  - The height formula with irreducible fibres (D:height).
  - The local corrections as inverse fibre-intersection matrices (D:local).
  - The irreducibility hypothesis is needed. The conic-pencil example, with three reducible members, shows it; the
    intake recomputed it.

**Corrections to our material,** for the corrections section (item R). The intake's section 4 gives the evidence for
each.
1. R2's "128 Lemma 1 is fine in odd characteristic" is false. The reader's record had it only in the model
   k[s]/(s²).
2. Our study (SA17-14) described NR(b) on "complete local domains". The ink says "irréductible".
3. L6 put Δ*(G) in the formula of scan 94. The page has M.
4. Hunch 2 of the K126-K132 reading ("for relative dimension ≤ 1 I expect yes") is refuted by Hironaka's example.
5. The first prompt's C.4 scope, "over a perfect field", is wider than the page.
6. L1's route, the naive noetherian induction, is insufficient. L1 itself is undecided.
7. Our study missed Murre's exposé 294.
8. **127 scan 3**, decided on the image at 600 dpi on 19 Nov 2026 by Claude Opus 5.5 at effort max (agent
   ac8bd2a26d00b4f37).
   - The inserted parenthesis reads "A ↪ Γ(Y, O_Y)", with no prime, as the Work transcription K127-01 has it.
   - The sense requires Γ(Y', O_{Y'}), since Γ(Y, O_Y) = A for Y = Spec A. So the page has an author's slip.
   - The first run's "A ↪ Γ(Y', O_{Y'})" is the mathematical correction, not the ink.

**Readings still doubtful** (no reader on the scans yet). Where a step of yours depends on one, prove the statement for
each reading:
- 131 scan 16: "irréductible" against "intègre" in NR(b);
- 131 scan 14: whether the struck "fini" in 8° attaches to S' or to Z;
- 133 scan 26: the blue marginal formula, which the first run read with finite supports (the basis of
  C:distinguished_ring);
- 133 scans 6-7 and 28-29: WG defined by isometry classes and orthogonal sums only, and K_s against K.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most
of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the
smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach
stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter
search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then
push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided
step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is
finite) together with the strongest true statement proved in its place. Nothing else finishes an item. Partly settled
is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest
undecided instance are the state of an item you are still working on: record them as you go, then attack the
obstruction, starting from that instance. "Known" counts only with the derivation of the statement used here from the
cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is
given explicitly, with a proof that it is the whole answer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; a statement for all bases proved over
a field, or for all p proved for odd p, without saying so; a step that replaces a claim by a convenient special case
without naming it; a reading of the manuscript taken on trust where the mathematics depends on it (the transcriptions
are AI-made and carry doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each
reading).

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA17_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## The items of this run

These are the items, and the only ones. Of the Leads, L1 (part of A.1) and L2 (item A.2) are still open; the other
Leads are settled above. For each item:
- the state at checkpoint 02 is the first run's, as our intake checked it;
- the approaches tried are those the first run's notes record, with where each failed.

**A. The representability programme (cotes 131 and 126-128). The main question is A.1.**
- **A.1 (main).** Prove or refute his Théorème of cote 131, scan 14. For F: (Sch/S)° → Ens with S locally
  noetherian, F is representable by an X locally quasi-finite and separated over S iff conditions 1°-8° hold, with 8°
  taken on test schemes Z locally of finite type over S (A:8-literal).
  - **State at checkpoint 02: proved under stated hypotheses** (A:local-to-global, A:formal-gluing, A:localiso-qc).
    - Assume actual representing schemes over the local bases.
    - Then a uniform Artin-Rees argument turns 8° on finite-type tests into the openness of the étaleness locus. That
      gives an algebraic space.
    - The separated étale relation has finite fibres over a noetherian scheme and is quasi-compact.
    - Valuative uniqueness, with Stacks 0417, then gives a separated, locally quasi-finite scheme.
    - Only the first run's own agents have checked the Artin-Rees step (`notes/A_Artin_Rees.md`). Check it before you
      use it.
  - **The gate.** Derive actual representing schemes over the local bases from condition 7° as written, that is
    actual modularity, not the stronger pro-modularity premise the first run could use.
    - The route: first over the complete local rings Ô_{S,s}, then over O_{S,s} by the descent step, which is
      settled (Murre 294 §4, case (d)).
    - With them, prove the constructibility of the modularity locus M(T, η) that his scan 6 reduces the theorem to:
      that is L1. L1 reads: "His condition 8° (generic modularity) gives, by noetherian induction, the
      constructibility of the modularity locus M(T, η) for T locally of finite type. This closes the gap of cote 131,
      scan 6." Decide its statement by any route.
  - **Tried, and where each failed** (`notes/ROOT_STATUS.md`, `notes/A_research.md`):
    - Artin's algebraization: it needs excellence and versality, which the conditions do not give;
    - the descent of a general algebraic space: it is not effective by itself;
    - noetherian induction from 8°, the route of L1: modularity after a closed base change is not the original
      locus;
    - formal completion: it detects étaleness, not the isomorphism of local rings.
  - **A route the notes do not record.** Murre's proof of his Theorem 1 (§2 of the exposé, attached) is the proof
    that the programme of cote 131 follows. His Note after Corollary 2 states the locally quasi-finite form without
    proof. Adapt §2 to the locally quasi-finite case, and compare its use of (F7) and (F8) with that of 7° and 8°.
  - **With the gate settled,** prove:
    - Corollaire 2 (unramified, with the corrected NR(b)), through "8° ⇒ Murre's (F8)";
    - "quasi-modulaire" without the stated hypotheses;
    - the gluing proposition.

    If the theorem fails, give the counterexample and the missing hypothesis, and prove the corrected theorem.
- **A.2: L2.** L2 reads: "Condition 7° follows from the others once 4° is strengthened to noetherian adic rings (his
  margin of scan 14). The argument is the one of scan 20 (Krull, plus finiteness over a local base)." Prove or refute
  it.
  - **State at checkpoint 02.** There is no derivation from the strengthened 4°, and no counterexample satisfying every
    axiom.
    - A henselised infinitesimal-group candidate passed the complete local tests. Neither fpqc descent nor the
      preservation of filtered colimits after sheafification is proved for it, so it is not yet a counterexample.
    - Murre's Note that (F7) cannot be omitted concerns the unramified theorem and does not decide L2.
  - **Two routes.**
    - Finish the candidate: prove its fpqc descent and the colimit condition, or find which one fails and modify the
      candidate.
    - Or derive 7° along the argument of scan 20.
- **A.4: the Théorème of cote 128 in every rank.** The first run proves that the finite semi-local theorem (a)-(c) of
  cote 128 (GL_m-torsors against H¹(A'_n/A_n)) survives the failure of Lemma 1 (A4:finite-descent-theorem).
  - The proof runs through A4:derivation-orbits, A4:finite-rank-equivalence and A4:infinite-orbits.
  - Its report marks the all-rank proof "under final root audit", and no second party has checked it.
  - **Complete the audit.** Give the theorem in every rank m with a complete proof and every step checked, or find the
    gap and attack it.
  - Keep apart the statements for one fixed rank, for every finite rank, and for free modules of every rank the
    statement claims.

**B. Barsotti-Tate groups and Dieudonné crystals (cote 129).**
- **B.3.** His conjecture on scan 114: "Il se pourrait que le foncteur BT(S)° → Cris Dieud(S) soit pl. fidèle".
  - **(i) The nonvanishing lemma.** The refutation (B:crystal-counterexamples) rests on τ ≠ 0, through the "finite PD
    detector" B:finite-PD. No second party has checked it. Check it twice:
    - by an independent proof;
    - by a program, for p = 2 and p = 3 on each base of the refutation. The program builds the detector, verifies
      that its divided powers are those the argument uses, and computes the image of τ. Attach its code and output.

    If τ vanishes on a base, the refutation falls there, and the conjecture over that base is undecided: decide it.
  - **(ii) The largest class.** Determine the largest class of bases of characteristic p on which the literature
    proves full faithfulness (B:largest-literature-class: "Unresolved scope").
    - Derive each class from its theorem after opening the source. The classes found so far:
      - quasisyntomic rings (Anschütz-Le Bras, Thm 4.74);
      - the classes of Lau's divided Dieudonné crystals (7.6, 7.9, 9.3, 9.5): bases with a p-basis, and reduced
        PD-torsion-free bases;
      - excellent lci bases (de Jong-Messing 1999, Thm 4.6);
      - every further class your search finds. Say what you searched.
    - Give the answer as the union of these classes.
    - Prove the stability properties the union has: étale localisation, products, filtered colimits, each one proved
      or refuted.
    - Show that each base of B:crystal-counterexamples and B:base-kinds lies outside the union.

**C. Cote 133.**
- **C.1.** His question of scan 29, "Est-ce vrai si k est un anneau local ?". Determine the commutative rings k for
  which ⊕_n R_k(S_n), with the induction product, is the polynomial ring over Z on the ρ_i. The answer covers every
  commutative ring.
  - **State at checkpoint 02.** The cases above are settled. Further results:
    - C:allrings_obstructions: for rings of characteristic 0, the ideal of extra representations is an extension of
      the generic-comparison kernel by the reduced generic K_0 image;
    - C:allrings_injectivity, C:regular_modular_locus, C:tame_degree, C:filtered_colimits and C:Specht_G0.

    What is open (C:allrings_gate) is the rings whose modular fibres are singular, in mixed characteristic.
  - **The answer is a condition on k** (on k, its K_0 and its fibres) that is necessary and sufficient, proved for
    every commutative ring.
- **C.3.** Determine split WG(BO_m) in characteristic p > 2 and over bases on which 2 is invertible
  (C:BO_general_gate).
  - **State at checkpoint 02.** Over fields the representation-theoretic formula is proved (C:field_WG_structure,
    C:algebraically_closed_WG). What is open:
    - the explicit classification of the modular indecomposables that occur;
    - the computation over bases that are not fields.
  - **Decide the special λ-identities on split WG(BO_m)** for the m < p + 4 that C:BO_positive_failure does not cover.
- **C.4.** (I) and (II) of scan 36, and the groups with a prescribed centre and derived group.
  - **(i) The non-commutative unipotent alternative of (I).** Decide (I) up to isogeny for formal groups whose kernel
    is unipotent and not commutative.
  - **(ii) Realisation without a baseline group.** Determine which central extensions E of π₀ by π₁ give a group G
    with N' = Z(G) and N = DG when no group with these data is given in advance. C:central_twists characterises the
    twists of a given one.
  - State every result over algebraically closed fields and over perfect fields separately.

**R. The report and the paper of the first run.**
- **The corrections section** of `RESEARCH_SA17_report.md`, a stub at checkpoint 02. Write every correction, each with
  the attached file and line, to:
  - the study, the readings and the transcriptions;
  - the Leads and the first prompt;
  - the first run's own tables.

  It includes the corrections listed above and the intake's sections 2 and 4.
- **The labels the intake found overstated or understated** (its section 2). Correct each one:
  - L4;
  - A.1's literal necessity, which is a defect of wording;
  - B.3, which rests on B:finite-PD until (i) of B.3 checks it;
  - C.4, which is over F_p;
  - the five "own proof" and two "own proof plus finite certificate" check events, and the rows with a locator in the
    type column: retype them with the types this prompt allows.

  Say in the report that the refutation of 128 Lemma 1 for every p is new as far as you searched, and say what you
  searched. Say also that Murre 294 is the published form of the programme of cote 131.
- **Every row labelled Known:**
  - A:completion-descent, A:etale-corollary, A:polarized-descent, A4:artinianflat, A5:projectivity;
  - B:square-zero-Hom, B:effectivity, B:NiceIV, B:positive-crystals, B:divided-target, B:DVR-classification;
  - C:DVR, C:algebraically_closed_WG, C:field_WG_structure;
  - D:local.

  For each, write in the paper the derivation of the statement used here from the cited theorem, after opening the
  source, as "What counts as done" requires.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- J. P. Murre, "Representation of unramified functors. Applications (according to unpublished results of
  A. Grothendieck)", Séminaire Bourbaki n° 294 (1964/65): attached, with `MURRE_294_LOCATORS.md`.
- M. Artin, "Algebraization of formal moduli I" (1969) and "Versal deformations and algebraic stacks", Invent. Math. 27
  (1974). D. Knutson, *Algebraic Spaces*, LNM 203. The Stacks Project, the chapters on Artin's axioms, on locally
  quasi-finite separated algebraic spaces, and on fpqc descent (LaTeX on GitHub). M. Schlessinger (1968). EGA IV §§8,
  17, 18; SGA 1 VIII. M. Raynaud and L. Gruson, Invent. Math. 13 (1971). M. Raynaud, *Faisceaux amples sur les schémas en
  groupes*, LNM 119.
- W. Messing, *The crystals associated to Barsotti-Tate groups*, LNM 264. P. Berthelot, L. Breen, W. Messing, LNM 930.
  P. Berthelot and W. Messing, "Théorie de Dieudonné cristalline III" (Grothendieck Festschrift I, 1990). A. J. de Jong,
  Publ. Math. IHÉS 82 (1995). de Jong and Messing, Bull. SMF 127 (1999). T. Zink, Astérisque 278. E. Lau, Invent. Math.
  2008 and the papers on frames. M. Kisin (2006). J. Anschütz and A.-C. Le Bras, "Prismatic Dieudonné theory".
  L. Illusie, Astérisque 127 (1985) and LNM 283, ch. VII. B. Mazur and L. Roberts, Invent. Math. 9 (1970).
  A. Grothendieck, *Groupes de Barsotti-Tate et cristaux de Dieudonné*, SMS 45 (1974), and his Nice talk (Actes ICM
  1970).
- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, ch. I. D. Knutson, *λ-rings and the representation
  theory of the symmetric group*, LNM 308. T. tom Dieck, *Transformation Groups and Representation Theory*, LNM 766.
  A. Joyal (1986), on species. T. Church, J. Ellenberg, B. Farb, "FI-modules and stability for representations of
  symmetric groups". C. Curtis and I. Reiner.
- M. Zibrowius, on λ-structures of Grothendieck-Witt rings (2015, 2018). M. Knebusch. M. Atiyah and D. Tall (1969). SGA 6 V.
- P. Hall, J. reine angew. Math. 182 (1940). F. R. Beyl and J. Tappe, LNM 958. E. Aldrovandi and B. Noohi (2009).
  M. Brion (2009, 2016). M. Rosenlicht (1956).
- T. Shioda, "On the Mordell-Weil lattices" (1990). A. Néron (1965). SGA 7 IX.

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data (the base and its noetherian, normal or excellent hypotheses, the prime p,
   the divided-power structure and its nilpotence, the ring k). Do not replace it by a convenient special case. If you
   prove a special case, name it as one and keep the general statement on your list.
2. Type every map and functor you introduce: source, target, the category in which it lives, and each extra property
   you use. Compositions must type-check.
3. Every reduction ("we may assume", "pass to the completion", "replace by a finite level") comes with its comparison
   map and a proof that the exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism; isogeny; equivalence of categories; representability
   by a scheme against representability by an algebraic space.
5. Check the edge cases in scope: p = 2; bases of dimension 0 and 1; non-reduced and non-noetherian bases; torsion in
   k; characteristic 2 in descent and in quadratic forms; non-abelian π₁.
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
- `RESEARCH_SA17_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA17_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA17_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA17_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted,
  with the statement number); then what you read, what you computed (every program with its scope, counts and run time),
  and every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- `PROGRESS_LEDGER.md`: the dated ledger of the progress reviews.
- `CHECK_EVENTS.tsv` (below) and `code/`: every program you ran, with its output.

The deliverables are the first run's files, completed. The paper covers every Part: the items of this run as you
settle them, and the settled items as the first run wrote them, with the labels corrected under item R.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here (the attached study's statements carry item ids such as SA17-15 with the cote and scan; keep them). Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA17_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.

This run's checkpoints continue the first run's numbering: the first is `RESEARCH_SA17_checkpoint_03.zip`.

**The attached files.** Besides this file there is one ZIP, `INTAKE_A_ANABELIAN_SECTIONS.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `INTAKE_A_1_returns.zip` is the folder `INTAKE_A_1_returns/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# INTAKE_A: five Longue Marche runs on anabelian geometry and the sections of the tripod over Q, every register row
read, sorted and checked

Intake prompt, 19 November 2026. For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for your deliverables:
`INTAKE_A`. Written by Claude Opus 5.5 (Anthropic) at effort max.

## Why this run

Five research runs of GPT-6 Astra (ChatGPT Pro mode) came back between 16 and 18 November 2026 with 961 register rows.
Their subject is Grothendieck's anabelian notes of 1983 (cote 149) and the sections of the projective line minus three
points over Q. Our intakes have read them only thinly: for every one of these runs, the intakes of its newest return
name fewer than a quarter of its rows (our intake ledger's count). A row an intake did not name is not proved unread,
and a row it named is not proved checked. This run takes in every row of the five registers, each to its verdict, with
our earlier intakes as background, and marks the rows they did not treat.

## The runs

| Run | Newest return we hold | Register rows (the run's statuses) | Its prompt asked | Rows named by intakes of this return (ledger) | Rows any document of ours names |
|---|---|---|---|---:|---:|
| ANABELIAN_SUCCESSOR | its final, 16 Nov 12:43 UTC | 157 (Proved 138, Refuted 8, Known 6, Open 5) | points of a proper curve over a finite field as sections of the prime-to-p fundamental group (cote 149, scans 35-36), and schemes from their étale topoi (scan 52) | 1 | 19 |
| ANABELIAN_A1 | checkpoint 03, 17 Nov 04:13 UTC; the run ended there (the account froze), no final | 121 (Proved 105, Refuted 8, Open 7, Known 1) | the check and completion of the proof of A1, what it implies and does not imply | 7 | 7 |
| ANABELIAN_A1_SUCCESSOR | checkpoint 05, 18 Nov 06:10 UTC; the chat stopped after it (its last line: "Message delivery timed out"), no final | 210 (Proved 190, False 10, Open 8, Known 2) | theorem A1 finished (the prime-to-p fundamental group separates the rational points of a proper curve over a finite field; cote 149, scans 35-36), every step proved or refuted, and the open items of the anabelian cluster | 0 | 0 |
| SECTIONS_OVER_Q | checkpoint 17, 16 Nov 17:54 UTC; the run ended there (the account froze), no final | 245 (Proved 227, Refuted 13, Open 4, Known 1) | the sections of P¹ minus three points over Q and birational lifting (Conjecture A and conjecture b of the notes of 1983; La Longue Marche §§5-9, 32-34) | 18 | 41 |
| SECTION_GHOSTS | its final, 18 Nov 13:05 UTC | 228 (Proved 201, Known 15, Open 9, Refuted 3) | does a section that survives the whole pronilpotent tower of the tripod over Q come from a rational point (the ghosts of the section conjecture) | 0 | 4 |

In all: 961 rows. The fifth column counts the rows of the newest return that our intakes of that return name (our
intake ledger). The last counts the rows whose id appears in a passage about the run in any document of ours, notes
and reviews of earlier returns included (zip 3, `coverage/`): a script's count, which you confirm against the
documents. A document that read an earlier return of a run names the ids of that return; where the newest return
changed a statement, compare the two statements before you carry a verdict over.

What our records say about the earlier checks:
- ANABELIAN_A1_SUCCESSOR continues ANABELIAN_A1: its column `A1_id` names the checkpoint-03 row each of its rows
  continues. Two second readings of ANABELIAN_A1 Part A, by two copies of our field expert (Claude Fable 5.2 at effort
  max), found that A.1 stands for all primes other than p, provisionally (`EXPERT_A1_SECOND_READING_20261117.md` and
  its part 2).
- ANABELIAN_SUCCESSOR's A1 chain was checked in part (about a third of it) by the field expert (Claude Fable 5.2 at
  effort max), and one step (K1, Saïdi-Tamagawa Prop. 1.8 (vi)) in the source by the main session (Claude Opus 5.5 at
  effort max): `MATH_TODO_20261117.md`, section 2, and `EXPERT_A1_ANABELIAN_20261117.md`.
- SECTIONS_OVER_Q: no intake has read it; our field expert (Claude Fable 5.2 at effort max) named 18 of its rows, its
  ghosts (`EXPERT_GT_TOWER_AND_GHOSTS_20261116.md`), and notes of our main session (Claude Opus 5.5 at effort max)
  name 29. SECTION_GHOSTS: no intake has read it; a note of our main session names 4 rows.

The documents that name the most rows of each register (document, rows named):
- ANABELIAN_SUCCESSOR: `NOTES_20261115.md` (19), `FOR_FABLE.md` (2), `EXPERT_A1_ANABELIAN_20261117.md` (1),
  `NOTES_20261117.md` (1).
- ANABELIAN_A1: `EXPERT_A1_SECOND_READING_20261117.md` (7), `FIRST_LOOK_20261117.md` (2).
- ANABELIAN_A1_SUCCESSOR: none.
- SECTIONS_OVER_Q: `NOTES_20261115.md` (29), `EXPERT_GT_TOWER_AND_GHOSTS_20261116.md` (18).
- SECTION_GHOSTS: `RUNS_NIGHT_20261118.md` (4).

## What every row gets

For every row of every register (961 rows), in `ROWS.tsv` and in the run's section of `INTAKE.md`:

1. **The claim**, in one or two precise sentences of your own, with its hypotheses and its scope.
2. **Its status as the run gives it** (Proved, Refuted or False, Known, Open), and where the run proves it (file and
   label).
3. **Its proof in the return**: there or not there; complete, or incomplete with the missing part stated exactly. For
   a refuted row: whether the counterexample and the corrected statement are given and hold. For a known row: whether
   the source is cited with a locator. For an open row: the strongest proved reduction (its gate) and the step that
   stays open.
4. **The check**, for every new result: every proved row that is not a known result, every refutation, and every
   proved reduction of an open row. Re-derive each step of its proof from the statement and the results it cites,
   writing your derivation before you compare it with the run's text; rerun each computational step with a program of
   your own that does not reuse the run's, by a different method or library wherever one exists, or verify the
   certificate attached in zip 2; check each result it cites against its source. Record each check in
   `CHECK_EVENTS.tsv` with the type of what you did (paragraph "Check events" below). The outcome is one of: holds;
   holds after a repair you state and check (a missing case, a wrong constant, a corrected citation); gap at an exact
   step (what the step needs, and why the results it cites do not give it); false, with a counterexample.
5. **New, known, or already ours.**
   - New: not in the literature; say what you searched for and where.
   - Known: author, work, statement number and page, from the source you opened; write "to verify" in place of the
     locator when you could not open the source, and say why.
   - Already ours: the same result in one of our earlier registers, with its run and id and the intake or note of ours
     that recorded it (zip 3: `programme/PLACEMENT_LM_STATEMENTS_20261117.tsv` and the earlier intakes).
6. **Earlier treatment**: every earlier intake, note, review or referee report of ours that treated the row (the
   coverage table gives the candidates: open the document and confirm), with its verdict, and whether yours agrees;
   where it differs, the step where the two part. A row no earlier document treated is marked "not treated before".

Then three sections across the runs, in `INTAKE.md`:

7. **Our open items.** For each open item of our programme that these runs touch, what in these registers closes it,
   moves it to a strictly smaller gate, or refutes it, with the rows and your check of the decisive step. The open
   items are those of section 3.1 of `programme/COMPANION_OUTLINE_LM_20261117.md`, the questions of the prompts as
   sent (zip 4), every open row of these registers, and the questions named in the section "Settled, checked and
   published since this prompt was built".
8. **Contradictions.** Every pair of rows that cannot both hold, within this cluster, against another of our Longue
   Marche registers (the placement table), or against an earlier verdict of ours: which one holds, and the step where
   the other fails.
9. **Hunches.** What the rows suggest beyond themselves, each written in `PROMPT_IDEAS.md` as the question of a Pro
   prompt: the question, the rows it rests on, why it matters for the programme, and the first step to take.

## Checks made after this prompt was built (19 November 2026)

**The sections sweep (sweep 1, 18 November 2026).** Claude Opus 5.5 (Anthropic) at effort max read the register
statements of the runs that bear on sections, with their printed hypotheses and notes. For the runs of this intake its
files give:
- 205 flag verdicts (`FLAG_VERDICTS_sweep1_INTAKE_A.tsv`);
- 6 check events (`CHECK_EVENTS_sweep1_INTAKE_A.tsv`);
- its corrections (`CORRECTIONS_sweep1.md`, the whole file; 25 of its lines name these runs).

All of them are in `INTAKE_A_5_sweep1_sections.zip`. Most are readings of statements and hypotheses, not checks of proofs:
a check event whose outcome begins "hypotheses only" says that the proof was not read. Use them as background for the
rows they name. Where a verdict or a correction there bears on a row, say in that row whether you confirm it or
overturn it, and record your own check event.

## Settled, checked and published since this prompt was built (19-24 November 2026)

Added on 24 November 2026 by Claude Opus 5.5 (Anthropic) at effort high. Every document named here is in
`INTAKE_A_6_updates_20261124.zip` (its `MANIFEST.tsv` gives origin and SHA-256, its `WHO_WROTE_WHAT.tsv` the authors).
Record each earlier check below in `CHECK_EVENTS.tsv` as an earlier event (who, date and type as given here), give the
row its verdict with it, and put your own checking into the steps that no one has checked yet. Where your reading of a
row differs from a record below, say at which step the two part.

1. **SECTION_GHOSTS E.176-E.191 are published.** Relation (IV) of Nakamura-Schneps holds for every element of GT̂;
   every element of GT̂ is a Galois element times an element of the Hatcher-Lochak-Schneps group Λ; Δ vanishes on the
   normalized elements of GT̂. Published as hexagon:2611.00940v1 (23 November 2026), "Relation (IV) of Nakamura and
   Schneps holds on the profinite Grothendieck-Teichmüller group, with an application to the two elliptic points of the
   modular curve"; the TeX as deposited is `h17_note_wb0007.tex`, and `RECORDS.md` §1 maps each statement of the note
   to its register row. The note replaces E.176 (Smith theory) by Boggi-Zalesskii, Theorem A (arXiv:2406.08639).
   - Checks: E.176-E.181 targeted proof check, Claude Fable 5.2 at effort max (a49aabbf), 18 Nov; E.181 targeted proof
     check, Claude Opus 5.5 at effort max, 18 Nov; E.191 independent re-proof from E.190.4, Claude Fable 5.2 at effort
     max, 21 Nov (`DELTA_SEXTIC_20261121.md`, Theorem B); E.182, E.184, E.188, E.189 (given Hoshi-Minamide-Mochizuki),
     E.190 targeted proof checks and E.183 independent re-proof, Claude Fable 5.2 at effort max, 23 Nov (`RECORDS.md`
     §2); the note read by a second reader, Claude Opus 5.5 at effort max (ae4ae3dc): no mathematical error.
   - Literature: Lochak-Nakamura-Schneps, arXiv:2602.12462v1, §1, p. 2: "It is unclear, however, whether the additional
     condition actually defines a proper subgroup of GT̂". Nothing on arXiv or Hexagon after 23 November touches it.
   - Check what no one has checked: the note's Corollary 4 (from normalized elements to all of GT̂), whose inputs are
     LM7_PUSH E.65 and E.58 (refereed 14 Nov by Claude Opus 5.5 at effort max; that run is in INTAKE_B). Your section 7
     takes the next question: does the action of Λ₀ together with the Galois action form one action of GT̂ on the
     tower with marked points (Lochak-Nakamura-Schneps §8)? For zero or one marked point our run GT_AFTER_H17
     (GPT-6 Astra (ChatGPT Pro mode), checkpoint 07 of 25 November 2026, its question Q2.b) reports that the
     Nakamura-Schneps and the Lochak-Nakamura-Schneps actions agree as outer actions, with an explicit inner
     correction; no one outside that run has checked this. The note's other open question, whether (III′) holds on
     all of GT̂, is closed: it does (see "Settled on 24 and 25 November 2026" below).
2. **A1 is written up (not posted).** ANABELIAN_SUCCESSOR A.3, ANABELIAN_A1 A.1, A.33, A.CR10, ANABELIAN_A1_SUCCESSOR
   A.1, A.22, A.50: for a smooth proper curve of genus at least 2 over a finite field of characteristic p (and for
   hyperbolic curves over fields finitely generated over F_p), the point-section map into the geometrically
   prime-to-p arithmetic fundamental group is injective, over every finite extension; the Saïdi-Tamagawa exceptional
   set is empty for every J_C-large set of primes. Note: `h07_note_v3.tex` (9 pp., editor Claude Fable 5.2 at effort
   max, a2fedc2a, 23 Nov), written from the rebuild AN_GRH A05 of ANABELIAN_A1 cp03.
   - Checks: the cp03 chain (A.CF1-CF12, A.CR1-CR14, A.R1, A.R4, A.R5) read in full by two copies of our field expert,
     Claude Fable 5.2 at effort max (zip 3); A05 Steps 1-2 independent re-proof, Claude Opus 5.5 at effort max
     (a28ea31f); Steps 3-6 line by line, Claude Opus 5.5 at effort max, 23 Nov
     (`CLAUDE_CHECK_A05_steps3to6_20261123.md`); A1_SUCCESSOR A.50 recomputed by a separate program and its separation
     inference re-proved, Claude Opus 5.5 at effort high, 24 Nov (`LONGUE_MARCHE_B_checks/a50_check.py`).
   - Literature, 24 Nov: no work proves it; Saïdi-Tamagawa 2009 (arXiv:0801.1452, Proposition 1.8(vi)) gives
     finiteness of the exceptional set.
   - Check in full what no one outside the run has read: A1_SUCCESSOR's direct characteristic-p route (A.42-A.49,
     B.68) and A.51. Section 7 takes the next question, A12 (ANABELIAN_A1 A.CR15 = A1_SUCCESSOR A.28, A.53-A.61):
     point separation for prime sets that are neither a singleton nor J_C-large.
3. **Checks made by our cluster readers, 24 Nov** (Claude Opus 5.5 at effort high; `LONGUE_MARCHE_B.md`, table
   "What I checked", and the `INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv` files):
   - ANABELIAN_A1 A.25: independent re-proof by hand and computation;
   - ANABELIAN_SUCCESSOR A.70 and A.34: their premises re-proved;
   - ANABELIAN_SUCCESSOR, the report's example y² + y = x + 1/x + 1/(x+1) over F₂: computed by hand (group structure
     not checked);
   - SECTIONS_OVER_Q A.16: targeted proof check of its key step, given A.14;
   - SECTION_GHOSTS E.150: independent re-proof, both examples;
   - SECTION_GHOSTS E.195: targeted proof check, conditional on Δ = 0 on GT̂.

   The general intake of SECTIONS_OVER_Q cp17 (Claude Opus 5.5 at effort max, a28ea31f, 19 Nov; every row at
   statement level, with about 16 computations and targeted checks; `GENERAL_INTAKE_SECTIONS_OVER_Q_cp17_20261119.md`)
   ranks first the check of A.14 against Pan, Theorem 1.0.4 and Helm-Voloch, Proposition 6, then of A.201, A.204 and
   A.178 against Harari-Stix, Theorem 2.1. Take those checks first in SECTIONS_OVER_Q.
4. **Known results the registers label Proved.**
   - SECTION_GHOSTS E.209-E.210 (for odd regular ℓ, H²(G_{Q,{ℓ,∞}}, Z/ℓⁿ(w)) = 0 in every weight w) is classical in
     substance: for regular ℓ the maximal pro-ℓ extension of Q(ζ_ℓ) unramified outside ℓ is free, and Z/ℓ(w) becomes
     trivial over Q(ζ_ℓ). Find the published statement (Koch, *Galois theory of p-extensions*; Neukirch-Schmidt-Wingberg,
     Chapter X) and give its locator, or "to verify".
   - SECTIONS_OVER_Q C.3 (the section conjecture fails over Q(μ_∞)) is known in substance: Clark 2006, Theorem 1, with
     cd Q^ab = 1, as CYCLOTOMIC_KERNEL D5 records. Verify at the source.
5. **Outside work to compare the rows with.** The e-prints are in zip 6, `literature/`. Claude Opus 5.5 at effort high
   opened each at the statement cited, 24 Nov.
   - **Reconstruction from étale topoi.** Carlson-Stix, arXiv:2410.22474v2 (20 Sep 2026), Theorems A and B: for every
     sub-p-adic field K, X ↦ X_ét is fully faithful on finite-type K-schemes modulo universal homeomorphisms, for pinned
     morphisms. Carlson-Haine-Wolf, arXiv:2407.19920, Theorem 0.1: the same for infinite finitely generated fields;
     their Example 2.31: algebraically closed fields of characteristic 0 fail.
     - These cover the sub-p-adic members of the reconstruction rows (ANABELIAN_SUCCESSOR Part F; A1_SUCCESSOR
       B.43-B.66, B.123, B.135-B.147, such as the henselizations D^h and their finite extensions).
     - What stays new is the fields that contain μ_∞, which are never sub-p-adic. A1_SUCCESSOR makes this comparison
       itself, in its paper at line 16693.
     - For each reconstruction row, say which part Carlson-Stix or Carlson-Haine-Wolf proves.
   - **Fermat for Selmer sections.** Steklov, arXiv:2602.17746v2 (3 Mar 2026), Theorem A = Theorem 5.14: every Selmer
     section of the affine Fermat curve of prime exponent ℓ ≥ 7 over Q is cuspidal. Two steps of its proof fail:
     - Proposition 4.6 is false as stated. It needs the leading constant to be an e-th power, and at the Fermat cusp
       q = 256⁻¹t^{2n}(1 + O(tⁿ)), where the class κ(256⁻¹) has 2-adic valuation −8 (LM8_PUSH D.22, FERMAT_SUCCESSOR
       A.4, in INTAKE_B). The description of the splitting in the proof of Proposition 5.10 is false as well. The
       conclusion of Proposition 5.10 holds, so his Theorem A stands for ℓ ≥ 11 once 5.10 is re-proved;
     - "Y₁(ℓ) and Y(μ_ℓ) have no Q-points for ℓ ≥ 7" is false at ℓ = 7 (his own Corollary 5.6 says ℓ ≥ 11), so the
       case ℓ = 7 is unproved as printed.

     Our run FERMAT_SECTIONS (GPT-6 Astra (ChatGPT Pro mode), checkpoint 13 of 25 November 2026) now proves the
     Selmer statement for every odd n ≥ 3: every Selmer section of the open Fermat curve U_n over Q (the run's
     notation) is cuspidal, and the Selmer sections form three disjoint packets of cuspidal sections, each a torsor
     under H¹(Q, Ẑ(1)); no local section conjecture is an input. For all sections it proves the statement under
     OpenAI's local theorem for proper curves (6 October 2026, unrefereed). The Selmer theorem is LM8_PUSH D.23 with
     two repairs. Claude Opus 5.5 at effort max checked it (`ATTACK_D23.md` and the intake of 25 November, both in
     `INTAKE_A_8_night_20261125/`), with two published inputs still to be opened at the statement used: Wiles 1995,
     Theorem 2.14, and the real section theorem. No human has checked it. Where a row of your runs is a case of
     this theorem, say so and compare the two proofs.

     SECTIONS_OVER_Q A.20 corrects LM6 E.8, which copies the first of these steps: say whether A.20's correction is the
     same as D.22's.
   - **The tripod over Q by Chabauty-Kim.** Two papers settle special cases:
     - Betts-Kumpitsch-Lüdtke, arXiv:2305.09462v2 (April 2026): every locally geometric section of a curve over Q comes
       from a point if Kim's conjecture holds for almost all p; they carry this out for the thrice-punctured line over
       Z[1/2];
     - Li-Lüdtke, arXiv:2608.20615 (August 2026): the S-Selmer section conjecture for P¹ − {0,1,∞} over imaginary
       quadratic fields, for S empty or one prime not fixed by complex conjugation.

     Compare them with SECTIONS_OVER_Q A.24 and SECTION_GHOSTS A.2 and D.2: which cases of the tripod question over Q
     do they settle, and does either give the recognition step A.24 for some family?
   - **Density.** Porowski, arXiv:2509.15660 (September 2025): a noncuspidal Selmer section is determined up to
     conjugacy by its reductions on a set of density one. Compare it with every row that uses the density step of the
     local preprint of 6 October (SECTIONS_OVER_Q D.1). LM8_PUSH A.20 attributes that inference to Porowski.
   - **Section 7, new item: the tripod over Q.** The rows on the tripod over Q are to be compared with all of the work
     above, and Lochak-Nakamura-Schneps and Basualdo Bonatto-Robertson (arXiv:2606.01466v2) go with item 1.
6. **The Galois/anabelian connection map of 24 November** (`MAP_GALOIS_ANABELIAN.md`, with its scripts, check events and
   row table; Claude Opus 5.5 at effort max). Its N1-N5 are the mapper's own proofs, and no second reader has checked
   them. Treat each as you treat a register row: check it, record the check, and use it only as far as your check
   carries. Lochak 2025 and Furusho 2002 are attached as PDFs under `literature/` (no TeX exists online).
   - **N1: Out* = GT̂ for g ≥ 1.** H17 Theorem 1 (= SECTION_GHOSTS E.177-E.180) and Lochak, Algebra i Analiz 37:2
     (2025), Theorem 5.10, together give, in Lochak's notation, IΓs = IΓ = GT̂, and Out*(Γ̌(S)) ≅ GT̂ for every generic
     surface type with g ≥ 1. This answers the three questions Lochak asks in his closing remarks (pp. 61-62); neither
     the H17 note nor its records cite this paper. Gates:
     - Lochak's proof uses Boggi-Funar, J. Topology 16 (2023) (his [3]). EXIT_TOWER E.14 (in INTAKE_B) says that
       Lemma 2.23 of a 2026 Boggi-Funar text is false as printed; check that Lochak's uses of [3] avoid it.
     - Lochak, p. 61: "IΓs is contained in the group denoted by IΓ in [30]" (Nakamura-Schneps). Read literally, with
       IΓs = GT̂ this would give (III′) on all of GT̂, which is the next question of item 1 above. Settle what the
       sentence says against Nakamura-Schneps §6 and Lochak §5.
   - **Check 1: N2, the map's Proposition L, together with SECTIONS_OVER_Q A.14 at its sources.** N2 is in
     `MAP_GALOIS_ANABELIAN.md`, §1, "N2". Its statement: let s be a noncuspidal Selmer section of U = P¹ − {0,1,∞} over
     Q in the class of SECTIONS_OVER_Q A.14, so that its local points are integral outside a finite set S of primes
     (2 ∈ S). Let λ₀ be its integral Legendre parameter (A.16). Then:
     - (a) λ₀ and 1 − λ₀ are S-units. For S = {2} the possible points are −1, 2 and 1/2 (all with j = 1728); for
       S = {2, 3} there are 21 (`MAP_GALOIS_ANABELIAN_scripts/checks_su_irr.py`).
     - (b) At every prime where s is locally cuspidal, E_{λ₀} has potentially multiplicative reduction, and the local
       extension class is non-split and ramified.
     - (c) If v_p(j(λ₀)) ≥ 0 for every p in S, then s is the section of λ₀.

     The map's proof uses Néron-Ogg-Šafarevič for (a); weights and inertia for (b); and Stix, *On the birational
     section conjecture with local conditions*, Invent. Math. 199 (2015), Corollary 6, with the Legendre comparison of
     A.16, for (c). Its check state: the mapper's own proof, with no second reader. Do two things:
     - Check every step of (a)-(c), including the claim that (b) gives what Betts-Kumpitsch-Lüdtke Theorem C (attached)
       does not: no cuspidal local section at 2.
     - Check A.14 itself against its two outside inputs, which no one on our side has opened. They are Pan, *The
       Fontaine-Mazur conjecture in the residually reducible case*, J. Amer. Math. Soc. 35 (2022) 1031-1169,
       Theorem 1.0.4, and Helm-Voloch, *Finite descent obstruction on curves and modularity*, Bull. London Math. Soc.
       43 (2011) 805-810, Proposition 6 (the run's keys LegPan2022 and LegHelmVoloch2011). A.14's use of them is in
       SECTIONS_OVER_Q `sections/legendre_agent.tex`, lines 227-273. The general intake of 19 Nov found that A.14 uses
       them beyond their stated forms: the conductor bound uses only the support of residual ramification and the image
       of wild inertia. Open both papers (their arXiv versions; give the addresses you used), and decide whether their
       hypotheses hold in A.14's use.

     A gap in A.14 is a gap in N2. Record both checks in `CHECK_EVENTS.tsv`.
   - **Check 2: N3, the obstruction of the section tower in (K_{2r}(Z) ⊗ Z_ℓ)^b.** N3 is in `MAP_GALOIS_ANABELIAN.md`, §1,
     "N3". Its statement: for odd ℓ, S = {ℓ, ∞}, K = Q(μ_ℓ) and A = Cl(K)[ℓ^∞] with its eigenspaces A(ω^i), and for every
     w ∈ Z, H²(G_{Q,S}, F_ℓ(w)) ≅ (A/ℓA)(ω^{1−w}).
     - Hence H²(G_{Q,S}, Z/ℓⁿ(w)) = 0 for all n iff A(ω^{1−w}) = 0, and H²(G_{Q,S}, Z_ℓ(w)) ≅ K_{2w−2}(Z) ⊗ Z_ℓ for
       w ≥ 2.
     - So the obstruction of SECTION_GHOSTS B.25, to lifting a boundary-matched class-r section of the pro-ℓ tripod tower
       to class r + 1, lies in (K_{2r}(Z) ⊗ Z_ℓ)^{b_{r+1}}.
     - It vanishes unless one of two things happens: r is odd and (ℓ, k) is an irregular pair with k ≡ r + 1 (mod ℓ − 1);
       or r is even and the Vandiver eigenspace A(ω^{−r}) is nonzero.
     - For even r ≤ 60 the second case does not occur at any ℓ if K_{4m}(Z) = 0 for 1 ≤ m ≤ 30, which Mok and Zheng
       claim (hexagon:2611.00998, unrefereed). The transport K_{4m}(Z)/ℓ ≅ (Cl(Q(μ_ℓ))/ℓ)(ω^{−2m}) that this uses was
       audited inside our run IHARA_AFTER_STEP17 (GPT-6 Astra (ChatGPT Pro mode), checkpoint 09 of 25 November
       2026, its row K-TRANSPORT) and by no one outside it. State the consequence of N3 in both forms: with no
       hypothesis, and on that input.

     The map's list of possibly obstructed weights for ℓ < 200 and for ℓ = 691 is in N3 (`checks_su_irr.py`). Its
     proof uses:
     - the Kummer sequence on O_{K,S_K}: Milne, *Arithmetic Duality Theorems*, II.2, with Br(O_{K,S_K})[ℓ] = 0 and
       Pic(O_{K,S_K}) = Cl(K);
     - descent along the prime-to-ℓ index ℓ − 1, and cd_ℓ G_{Q,S} = 2;
     - Quillen-Lichtenbaum (Rost-Voevodsky; Soulé; Kurihara 1992) for the K-theory identification;
     - Herbrand-Ribet with Mazur-Wiles for the odd eigenspaces, and Kurihara 1992 and Hart-Harvey-Ong 2017 (Vandiver
       below 2³¹) for the even ones.

     Its check state: the mapper's own proof, with no second reader. Re-derive every step, check each cited result at
     its source, recompute the list of irregular pairs with your own program, and say what N3 does to SECTION_GHOSTS
     E.209-E.210, B.25-B.26 and A.2: E.209 becomes the regular case of N3.
   - **N4: G_Q = GT̂ iff Λ₀ = G_{K₂}**, with K₂ = Q(μ_∞, 2^{1/∞}). It bears on SECTION_GHOSTS E.181.
   - **N6: a correction to an attached file, our own posted note.** Line 158 of `h17_note_wb0007.tex` says "The inclusion
     GT̂ ⊊ GT̂₀ itself is known" and cites nothing. No printed proof is known to us: Dolgushev-Guynee, p. 2, say only
     "obviously contains". The claim rested on our unrefereed runs (INTAKE_B, item 2).
     Since 25 November 2026 one of our runs has a proof that was read outside the run: GT_AFTER_H17
     (GPT-6 Astra (ChatGPT Pro mode), checkpoint 07) constructs, for every prime p ≡ 5 (mod 12), a continuous
     character ϑ_p : GT̂₀ → F₂ that vanishes on GT̂, and these are jointly onto ∏F₂; so GT̂ ⊊ GT̂₀, and GT̂₀ modulo the
     normal closure of GT̂ has the quotient (Z/2)^ℕ (its paper on gentle characters, Theorem 11.5, with Theorem 8.1
     and Lemma 8.2; in `INTAKE_A_8_night_20261125/`). Claude Opus 5.5 at effort max followed that chain line by
     line on 25 November, apart from one published input it did not open (Ihara 1999, Proposition 1.6.1, as
     recalled in Furusho 2003, §2.3). No printed proof is known to us, and no human has checked this one. Read the
     note with this correction.

### Settled on 24 and 25 November 2026, after the list above was written

Added on 25 November 2026 by Claude Fable 5.2 (Anthropic) at effort max. The four texts named here are in the folder
`INTAKE_A_7_settled_20261125/` of the attached ZIP. Record each check named here in `CHECK_EVENTS.tsv` as an earlier event, as above.

- **Relation (III′) of Nakamura and Schneps holds on all of GT̂.** Our note hexagon:2611.00940 is at version 2
  (24 November 2026; `h17_note_v2.tex`, Theorem 20 and Corollaries 21 and 22). The subgroup IΓ of Nakamura and Schneps,
  cut out by (III′) and (IV), is all of GT̂; Lochak's groups of compatible pairs are GT̂, which is the map's N1 (its
  Corollary 22); and Corollary 22 does not depend on the identity of Boggi–Funar that EXIT_TOWER E.14 disputes. Checked
  step by step by Claude Opus 5.5 at effort max (`CHECK_H17_V2_20261124.md`) and read again by Claude Fable 5.2 at effort
  max. No human has checked it. So the question posed above, whether (III′) holds on GT̂, with Lochak's sentence on his
  p. 61, is answered: it holds. Do not report it as open; where a row of your runs depends on it, say so and cite the
  theorem.
- **Invertibility is automatic, and λ is a unit.** Our note hexagon:2611.01024 (25 November 2026; `gt_monoid_note.tex`,
  Theorems A and E). If λ ∈ 1 + 2Ẑ and f ∈ F̂₂ satisfy duality (I) and the hexagon (II), then λ ∈ Ẑ^× and x ↦ x^λ,
  y ↦ f⁻¹ y^λ f is an automorphism of F̂₂; the pentagon is not used. Its Theorem E: a continuous endomorphism of the
  profinite completion of the fundamental group of a compact surface with boundary that sends every boundary generator to
  a conjugate of a unit power of a boundary generator, bijectively on boundary components, is an automorphism; on a
  sphere with at least three holes the exponent of such an endomorphism is 0 or a unit. Every claim was checked by Claude
  Opus 5.5 at effort max before posting (`CHECK_A1_INDEPENDENT.md`). No human has checked it.
- **What this changes for this run.** Where a row of your runs passes from an endomorphism that preserves the classes of
  the cusps, or of boundary generators, to an automorphism, the second statement is the reference; check that the row's
  hypotheses are those of its Theorem E, and say where they are weaker.

### Results of our runs of the night of 24 to 25 November 2026

Added on 25 November 2026 by Claude Fable 5.2 (Anthropic) at effort max. Three runs that returned that night are
named above where they bear on a row: FERMAT_SECTIONS (Fermat for Selmer sections), GT_AFTER_H17 (GT̂ ⊊ GT̂₀; the
action with marked points) and IHARA_AFTER_STEP17 (the transport behind N3). All three are runs of
GPT-6 Astra (ChatGPT Pro mode). The folder `INTAKE_A_8_night_20261125/` of the attached ZIP holds their intakes by
Claude Opus 5.5 at effort max with the check events, the attack-read of LM8_PUSH D.23, and the LaTeX of the two
papers named above (`FERMAT_SECTIONS_cp13_fermat/main.tex`, `GT_AFTER_H17_cp07_gentle_characters/`). These runs are
not among the runs this intake takes in. Use them as the newest state of the questions they bear on, each with
the check state its intake gives, and record each check named there in `CHECK_EVENTS.tsv` as an earlier event.
The folder also holds the LaTeX of OpenAI's preprint on the p-adic section conjecture for proper curves
(`OpenAI_p-adic_section_LaTeX/`, 6 October 2026). It is unrefereed, and none of ours has checked it; it enters
the Fermat statement for all sections as a named hypothesis only.

### The Riemann hypothesis in this material (added 25 November 2026)

Added by Claude Fable 5.2 (Anthropic) at effort max.

**The Riemann hypothesis is a theorem.** L. Alpöge, *Remark* (20 November 2026, https://alpo.ge/remark.pdf), proves
the Riemann hypothesis for every Dirichlet L-function, the Riemann zeta function included: every zero of L(s, χ)
with 0 < Re s < 1 lies on Re s = 1/2. The proof is formalized in Lean
(https://github.com/CocoSgt/riemann-hypothesis-lean), and the archive has been read and checked by many. It is
newer than your training, so take it from the files: the folder `RH_PROOF_Alpoge_20261120/` of the attached ZIP
holds the note (`ALPOGE_remark.pdf`; we have no LaTeX source of it) and the Lean files that state and close the
main theorems (`ALPOGE_Statements.lean`, `ALPOGE_Main.lean`, with `ALPOGE_lakefile.toml`). They are required
background reading: read them before you start. Below, A means this theorem. Use it as a theorem and cite it so; a
statement that A covers is never written "assuming RH" or "under GRH".

A and the L-functions around it meet the runs of this intake at four places, each of them real:
1. every step that counts or selects primes: Chebotarev in abelian extensions, the large sets of primes of A1, the
   exceptional sets of Saïdi and Tamagawa;
2. N3 and SECTION_GHOSTS B.25: the eigenspaces A(ω^i) of the class groups of Q(μ_ℓ) and the K-groups of Z are
   governed by values of Dirichlet L-functions;
3. the Fermat theorem: the Jacobian of the Fermat curve has complex multiplication, its L-function is a product of
   Hecke L-functions of Jacobi-sum characters of Q(μ_n), and the rank and Selmer inputs of the theorem are
   statements about their central values;
4. N4: by GT_AFTER_H17 (the first theorem of its first paper; not yet checked outside the run) the quotient of GT̂
   by Λ₀ is Gal(K₂/Q), K₂ = Q(μ_∞, 2^{1/∞}), whose finite layers are the Kummer fields of Hooley's theorem on
   Artin's conjecture.

For every row of your runs that meets one of these places, say how the link works: which hypothesis of the row A
removes, which bound it makes effective, and with what proof. Where a row needs an L-function that A does not cover,
name that L-function and the exact statement about it that the row needs; that statement is a row of your tables
with its own status. "It does not bear on the Riemann hypothesis" is not a verdict: the links are there, and the
work is to say how each one acts on the row.

Zero-free half-planes for Hecke L-functions of number fields are claimed as well (OpenAI, 30 September 2026; Hu,
Gao and Liu on Hexagon, October and November 2026). They are not in the ZIP and none of ours has audited them:
open them and check the statement you use before you use it.

## How to work

- For each run, read its prompt as sent first (zip 4: what it was asked), then its report, then its register row by
  row with the proofs in its TeX. Where the newest return is a checkpoint, take in what it holds: a row its report
  marks as unfinished keeps that state, with what is proved.
- Every status in these registers is the run's own claim. A run's own check-event files and audits are its
  self-checks: report them as the run's, and they do not replace your check.
- Rows that recur across runs (a successor run continues or re-proves an earlier row) each get their own line, linked
  to each other in the notes column.
- Our newer runs saved lean checkpoints, which hold only what changed since the checkpoint before. Where the newest
  return lacks a file of the run that an earlier checkpoint holds, the earlier file is attached, and its
  `MANIFEST.tsv` row names that checkpoint.
- Where a proof cites one of our earlier statements (as "LM6 E.12" or "EXIT_TOWER E.49"), look it up in the placement
  table, which gives its status and check record. In that table, LM1 is the LM1 rerun, LM4 is
  LM4_FINITE_GROUP_ACTIONS, LM7 is LM7_FERMAT_TOWER and LM8 is LM8_LIE_APPROXIMATIONS.
- The attachments hold no literature except zip 6, `literature/` (the e-prints named in the section "Settled, checked
  and published since this prompt was built"). Find every other source on the web (arXiv sources first, then the
  journals' open pages and the authors' pages) and open it before you cite it.
- The return zip holds no programs. Zip 2 holds the programs and certificates that register rows name as their
  evidence. For every other computation, write your own code.
- In our notes, home-folder paths read `C:\Users\<user>\...`; each zip's `MANIFEST.tsv` records that change where it
  was made. Nothing else in the attachments is changed.

## The order of the work

1. **The skeleton first.** One line of `ROWS.tsv` per row of every register, with the claim, the run's status and the
   earlier treatment filled in. It gives the counts of section 0 and is the measure of completeness.
2. **Run by run**, in the order ANABELIAN_SUCCESSOR, ANABELIAN_A1, ANABELIAN_A1_SUCCESSOR, SECTIONS_OVER_Q,
   SECTION_GHOSTS: for every row, its proof read and checked, its novelty settled, its verdict written. Write the
   files from the start and extend them as you go, so that an interruption loses little.
3. **The three sections across the runs** (7, 8, 9).
4. **The gaps.** When every row has its verdict, go back to each gap your checks found and work on it: close it with a
   repair you state and check, or show the step false with a counterexample. A gap that remains goes into its row's
   verdict with the exact missing step and every approach you tried, and its question goes into `PROMPT_IDEAS.md`.

Review the work every hour against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): for each run, the rows
with their verdict and the rows still to do; in step 4, every open gap with its status. In steps 1 to 3, movement
means rows reaching their verdict. In step 4, movement means only a gap closed or a step shown false. After two
consecutive reviews in step 4 without movement, stop the gap work, write the final package with every gap's state, and
deliver it.

## What the outcome must be

1. **Done** means:
   - `ROWS.tsv` has one line for every row of every register (961 lines), with every column filled;
   - every new result has been checked, and its check events are in `CHECK_EVENTS.tsv`;
   - `INTAKE.md` has section 0 and the sections per run and across the runs (below);
   - every hunch is in `PROMPT_IDEAS.md` as the question of a prompt.
2. **Not acceptable:**
   - a row without its verdict, or a sample of the rows in place of all of them;
   - "see the run's report" in place of a verdict;
   - a check recorded as a type it was not;
   - a row called new without what was searched, or known without a locator or "to verify";
   - a model named without its effort.
3. **Finished** only when the work is done in the sense of point 1. Keep working until then: do not stop because the
   remaining rows are many, because a run looks well checked already, or because much has been written. If the session
   itself ends first (the environment stops you, not your choice), the first line of `INTAKE.md` reads INCOMPLETE, and
   section 0 gives the state reached for every run (the rows with their verdict and the rows not yet reached), every
   approach tried on each open gap with where it failed, and the next step. A continuation run will resume from your
   newest checkpoint and this prompt. Never present such a return as complete.

---

THE MATERIAL YOU ARE GIVEN

Four zips. Each has a `MANIFEST.tsv` with every member's origin in our files, its SHA-256 and the reason it is
attached.
- `INTAKE_A_1_returns.zip`: the newest return of each run, one folder per run (`<RUN>_<return>/`): its register
  (`*_results.csv`), its report, its paper's TeX and sections, its notes TeX and records, its check-event files and
  its bibliography. Code, data, builds, page renders and earlier versions are left out. Where a run ended without a
  final and we saved its chat, the chat is in `_session_transcript/`.
- `INTAKE_A_2_evidence_code.zip`: the programs, outputs and certificates that register rows name as their evidence, in
  the same folders.
- `INTAKE_A_3_earlier_intakes.zip`:
  - `earlier/`: every intake, expert note, review, referee report and note of ours on these runs, at the paths of our
    files;
  - `WHO_WROTE_WHAT.tsv`: each document's author with model and effort, its date, and what it covers;
  - `coverage/<RUN>_rows_named_by_earlier_documents.tsv`: for every row, the documents that name it;
  - `programme/`: the companion outline (section 3.1: our open items) with the user's layers that supersede its
    structure, the placement of the 3,929 statements of 22 Longue Marche registers with their check records, our check
    ledger and our mathematics to-do of 17 November.
- `INTAKE_A_4_prompts_as_sent.zip`: the prompt each run was sent, with `PROVENANCE.tsv` (where each copy comes from
  and how we know it is the one sent).
- `INTAKE_A_5_sweep1_sections.zip`: the sections sweep of 18 November 2026 for these runs (flag verdicts, check events, corrections); section "Checks made after this prompt was built".
- `INTAKE_A_6_updates_20261124.zip` (added 24 November 2026): `earlier/` holds our documents written after this prompt
  was built: the published note hexagon:2611.00940 with its records, reviews and the re-proof of E.191; the A1 note with
  its records and check; the general intake of SECTIONS_OVER_Q; the cluster intake `LONGUE_MARCHE_B.md` of 24 Nov with
  its check-event files and program; the literature verdicts `TOPICALITY_LONGUE_MARCHE.md`/`.tsv`; and the Galois/anabelian map `MAP_GALOIS_ANABELIAN.md`
  with its table, check events and scripts. `literature/` holds the arXiv e-prints (LaTeX sources), and Lochak 2025 and
  Furusho 2002 as PDFs (no TeX online), named in the section "Settled, checked and published since this prompt was
  built". Its `MANIFEST.tsv` gives every member's origin, SHA-256 and reason, and its `WHO_WROTE_WHAT.tsv` the authors
  with model and effort.

WHAT TO DELIVER

One ZIP containing:
- `INTAKE.md`. Section 0: the scope (the runs, the return of each, the files you read), the row counts per run and per
  verdict, the rows no earlier document treated, and what the earlier verdicts and yours disagree on. Then one section
  per run, in the order above, and sections 7, 8 and 9.
- `ROWS.tsv`, one line per register row, with the columns `run`, `id`, `claim`, `status_in_run`, `where_proved`,
  `proof_in_return`, `proof_complete`, `check_types`, `check_outcome`, `novelty`, `locator_or_earlier_id`, `searched`,
  `earlier_treatment`, `agrees_with_earlier`, `bears_on_open_items`, `notes`.
- `CHECK_EVENTS.tsv` (paragraph below).
- `PROMPT_IDEAS.md`.
- `PROGRESS_LEDGER.md`.
- `code/`: every program you wrote or ran for a check, with its output.

Name every model with its effort: the runs and you as GPT-6 Astra (ChatGPT Pro mode); our intakes and notes as
`WHO_WROTE_WHAT.tsv` names their authors (for example Claude Fable 5.2 at effort high, Claude Opus 5.5 at effort max).
Work through every register; do not ask whether to go on.

IF THE EXECUTION ENVIRONMENT FAILS

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore
your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after
that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only
through checkpoint ZIPs and the final ZIP.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id,
date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate
/ used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's
id), outcome, where (the file and label of what you checked, and of your program for a computation). This covers the
statements of these runs and every earlier statement you check, use or refute here. Give each event the type of what
actually happened, neither more nor less: reading a proof without re-deriving its steps is not a check of it, and a
step you re-derived is a targeted proof check, not a re-proof of the whole. The statement id is the run and its id, as
`EXIT_TOWER:E.49`. Name yourself as "GPT-6 Astra (OpenAI), ChatGPT Pro mode, INTAKE_A". `CHECK_EVENTS.tsv` goes into
every checkpoint and into the final ZIP.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `INTAKE_A_checkpoint_<NN>.zip` with `NN` counting
up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint.
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter
or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before
you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable
written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a
new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it,
the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export
of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints
are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is
lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB
(536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be
larger, save it as several ZIPs of under 500 MB each, `INTAKE_A_checkpoint_<NN>_part<k>.zip`.

**No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
deliver (transcriptions, translations, editions, notes, programs, figures) always goes in.

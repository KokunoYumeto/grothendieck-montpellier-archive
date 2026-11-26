# Intake: POLISH_TOPOLOGY_PERIODS, checkpoint 19 to checkpoint 26 (24 Nov 2026, ~11:xx UTC)

This intake is by agent a9e9559d (Claude Opus 5.5 at effort high), the field expert of the run.

The run is GPT-6 Astra (ChatGPT Pro mode), continuation 91b. Checkpoint 26 was captured at 23:33 UTC on 23 Nov and filed at 00:34 UTC on 24 Nov. Checkpoints 20-25 never reached us, so this intake diffs checkpoint 19 against checkpoint 26. No newer checkpoint is filed.

## 0. What I read and the scope

**Return:** `research_returns/POLISH_TOPOLOGY_PERIODS_checkpoint_26_20261124T0034Z_unzipped`.

**The diff.** By SHA-256 of main.tex, **only Paper 2 changed**: 169 → 250 pages, with 21 new input files. Papers 1 and 3-7 are byte-identical to checkpoint 19.

**Read in full:**
- the ledger additions, from 18:19 to 23:33 UTC;
- the new records in CORRECTIONS_FOR_AUTHORS.md: Galvin (three records), Orson-Powell-Randal-Williams (two), Stasica, Delfs-Knebusch, Grothendieck 120-121;
- the Paper 2 abstract;
- the cusp proposition (embedded_smooth_naturality.tex).

**At the source:** the Orson-Powell-Randal-Williams author PDF (Remark 8.2 and Theorem 2.3(D)). Its SHA-256, 0000528e..., equals the run's.

**Statement level only:** the new Paper 2 topology results.

**Not read:** the run's continuation receipts and proofs.

## 1. Usefulness first, and the three checks asked for

1. **The S20 note (hexagon:2611.00937v2, in moderation): nothing changes.** Paper 2's analytic_freeness.tex and integer_examples.tex are byte-identical to checkpoint 19. The Elliott correction record is unchanged (section hash c42fb6ce at both checkpoints). The abstract was only reflowed, and still credits Elliott's 2013 announcement.
2. **The e-mail drafts:**
   - Elliott (Draft 2) and Boyle-Chen (Draft 3) are unchanged: their correction records hash identically at checkpoints 19 and 26.
   - New drafts: **Draft 4 to D. A. P. Galvin** and **Draft 5 to Orson, Powell and Randal-Williams**, in EMAIL_DRAFTS_POLISH_TOPOLOGY_PERIODS.md, both unsent. Their gates are in §3.
3. **New corrections to published work: six records.** Two are worth sending (Galvin; Orson-Powell-Randal-Williams), one is optional (Stasica), and one is not worth reporting (Delfs-Knebusch); details in §3.

**New mathematics, by usefulness.** All of it is in Paper 2 and read at statement level only.
- **A surjective Casson-Sullivan homomorphism** for oriented 3-manifolds with finite fundamental group. It uses Galvin's relative construction and the surgery formula of Hambleton, Milgram, Taylor and Williams.
- **The three-torus:** this obstruction vanishes on T^3.
- **Real projective 3-space:** odd joint germs identify the full component group as an abelian kernel.
- **Dimension five:** stabilization on concordance components is surjective. Injectivity (A124) remains open.
- **The intrinsic PL partition need not have conical charts.**
- **Coarsest embedded smooth partitions** exist for every semialgebraic set but depend on the embedding. I checked the cusp example myself.
- **Readers:** geometric topologists working on 4-manifold pseudo-isotopy (OPR, Galvin). These results are timely: OPR was accepted on 31 Oct 2026, and Galvin's paper was published on 28 Oct 2026.

**Run state:**
- 463 of 1,028 original statements accepted (436 at checkpoint 19), plus 12 supplemental results; 564 open.
- Paper 2: 161 proved, 106 unverified.
- No paper has a "Proof overview" section; I searched all seven main.tex files.

## 2. Verdicts

The full list is in `INTAKE_POLISH_TOPOLOGY_PERIODS_20261124_cp26_CHECK_EVENTS.tsv`, 10 events:
- 6 targeted proof checks, all confirmed;
- 1 used and rechecked (S20 unchanged);
- 3 carried as background.

## 3. Corrections to published work

| Source | Claim | My check | Report? |
|---|---|---|---|
| D. A. P. Galvin, *The Casson-Sullivan invariant for homeomorphisms of 4-manifolds*, Compositio Math. 162 (2026) 2496-2544 | (a) Lemma 4.9, p. 2526: Sq^i vanishing stated for i < deg, which is reversed. (b) Prop. 2.23, p. 2508: ΣX_+ should be Σ(X/∂X) when ∂X ≠ ∅. (c) Definition 4.11 says closed where Thm 1.7 says compact. | (a) Confirmed: Sq^0 = id, and Sq^1(ab) ≠ 0. (b) Confirmed with X = S^3 × I: H^3(X,∂X) = 0, H^3(X) = F_2. (c) Not checked. Source pages not opened by me. | **Yes, Draft 4.** Gate: open pp. 2508 and 2526. |
| Galvin, PhD thesis (Glasgow 2024), Prop. 9.3.2, pp. 116-117 | The case list omits Q_8; the abelianization sentence. | Confirmed group-theoretically. | Mentioned in Draft 4 as optional. |
| P. Orson, M. Powell, O. Randal-Williams, *Smoothing topological pseudo-isotopies of 4-manifolds*, accepted at J. reine angew. Math. (31 Oct 2026), author PDF | (a) Remark 8.2, p. 25: "k ≥ 0" should be k ≥ 1. (b) Thm 2.3(D) writes L^s_6, where Definition 5.8 uses the quadratic map. | (a) **Confirmed at the source** (U+2265 in the text; the T^4 example). (b) L^s_6 confirmed on p. 6; Definition 5.8 not opened. | **Yes, Draft 5** (timely, before typesetting). Gate: open Definition 5.8. |
| J. Stasica, *Smooth points of a semialgebraic set*, Ann. Polon. Math. 82 (2003), p. 151 | A graph-continuity criterion in the proof of Thm 3 | Counterexample confirmed. The theorems are not affected. Source not opened by me. | Optional; no draft (a proof detail in a 2003 note). |
| Delfs-Knebusch, Pacific J. Math. 114 (1984), p. 65 | A letter N=U for N=A | Not checked | No. |
| Grothendieck, cotes 120-121 | An archival reading | — | Internal. |

## 4. Corrections to our own work

None new. The S20 note version 2 is unaffected, and the topic notes need only the cp26 update (§6).

## 5. Each paper as a posting candidate

Papers 1 and 3-7 are unchanged since checkpoint 19, so the cp19 judgments stand. The shared blocker is box 8 ("Proof overview"). Paper 6 has had no Claude proof check.

**Paper 2 (250 pages) is not postable as one paper.** It should be split into four:

| Part | Content | What blocks it |
|---|---|---|
| (i) Grothendieck's Additif | collars and cones, the eleven arrows, the normalized cone convention | Box 8; the King 1985 comparison; no Claude proof check beyond the cone product |
| (ii) Concordance component groups | PL six (A121, A122), dimension-five surjectivity, low-dimensional components, S^3, T^3, RP^3, Casson-Sullivan surjectivity | A124 (injectivity) open; the A401/A402 and A701-A704 comparisons pending; no Claude read; the visual QA covers about 25 of 250 pages in the exact version |
| (iii) Definable and PL partitions | intrinsic CS partitions, weak filtrations, embedded smooth partitions, tube results A202-A209 | The seven-axiom comparison is open; a Claude read |
| (iv) Integer-valued polynomial algebra | the Noetherian criterion, the arbitrary base, the non-flat forest (S20 already posted) | Literature and box 8; the forest needs a note |

**Board rows (for the main session):**

| id (proposed) | line | result | adds | gate left |
|---|---|---|---|---|
| P91i | topology | A surjective Casson-Sullivan homomorphism for oriented 3-manifolds with finite π_1; vanishing on T^3; the RP^3 component group | Concrete 4-dimensional pseudo-isotopy computations after Galvin and OPR | A Claude targeted read; comparison with Galvin 2026 and OPR 2026 at locators; a short note |
| P91j | topology | Coarsest embedded smooth partitions exist for every semialgebraic set but depend on the embedding (the compact cusp) | A precise answer to the cote-120 question | Literature (Whitney stratification, smooth-locus results); small |
| E-Galvin, E-OPR | errata | As in §3 | — | The e-mails (Drafts 4 and 5) first; not posts |
| P91f, P91g, P91h, S-BC | — | Unchanged from cp19 | — | — |

## 6. Integration, applied

Backups are in `integration_backups/20261123/POLISH_TOPOLOGY_PERIODS/`; rows are appended to INTEGRATION_POLISH_TOPOLOGY_PERIODS_20261123.tsv.

**Applied:**
1. EMAIL_DRAFTS: Drafts 4 and 5 added. Backup: `EMAIL_DRAFTS_before_cp26.md`.
2. `results_register/horizontal/sweep2/SA20/TOPIC_NOTES.md`: cp26 update. Backup: `SA20_TOPIC_NOTES_before_cp26.md`.
3. The primer, updated in place. Backup: `PRIMER_POLISH_TOPOLOGY_PERIODS_20261123_cp19.md`.

**For the main session:** the board rows; the e-mails; and, for the prompt after 91b, splitting Paper 2 into four and box 8 everywhere.

## 7. P vs NP fleet

Nothing new maps onto the graph.

## 8. What is finished, what is open

**Finished:** as at cp19, plus 27 more accepted original rows in Paper 2: A135-A143, A150s, A160s, A201-A209, A303-A304.

**Open:**
- A124;
- A401/A402 and A701-A704;
- the seven-axiom comparison;
- 106 Paper 2 rows;
- the Paper 3, 4 and 7 rows as before;
- C.06;
- the whole-paper readings and visual QA of Paper 2;
- box 8 everywhere.

The run was active at its last capture: review 14 found movement. A review 15 was due at 23:48 UTC; we have no record of it.
